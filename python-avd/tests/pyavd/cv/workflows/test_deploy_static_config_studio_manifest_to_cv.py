# Copyright (c) 2025-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import logging
from pathlib import Path
from unittest.mock import MagicMock

import pytest

from pyavd._cv.api.arista.configlet.v1 import Configlet, ConfigletKey
from pyavd._cv.workflows.deploy_static_config_studio_manifest_to_cv import deploy_static_config_studio_manifest_to_cv
from pyavd._cv.workflows.models import AvdConfiglet, AvdContainer, AvdManifest, CVWorkspace, DeployToCvResult

from .helpers import create_grpc_container, generate_id

# === Test Fixtures ===


@pytest.fixture
def avd_initial_manifest() -> AvdManifest:
    """Fixture to provide an AvdManifest instance for initial deployment."""
    vxlan_configlet = AvdConfiglet(name="VXLAN", file=Path("vxlan.cfg"))
    mlag_configlet = AvdConfiglet(name="MLAG", file=Path("mlag.cfg"))
    bgp_configlet = AvdConfiglet(name="BGP", file=Path("bgp.cfg"))

    leafs_container = AvdContainer(
        name="LEAFS", tag_query="topology_hint_type:leaf", description="Leafs container", configlets=(vxlan_configlet.name, mlag_configlet.name)
    )
    spines_container = AvdContainer(name="SPINES", tag_query="topology_hint_type:spine", description="Spines container", configlets=(bgp_configlet.name,))
    global_container = AvdContainer(name="GLOBAL", tag_query="device:*", description="Global container", sub_containers=(leafs_container, spines_container))

    return AvdManifest(configlets=(vxlan_configlet, mlag_configlet, bgp_configlet), containers=(global_container,))


@pytest.fixture
def deployment_result() -> DeployToCvResult:
    """Fixture to provide a fresh deployment result object for each test."""
    workspace = CVWorkspace(name="pytest_workspace", id="pytest_workspace")
    return DeployToCvResult(workspace=workspace)


# === Test Cases ===


@pytest.mark.asyncio
class TestDeployStaticConfigStudio:
    """Test suite for the deploy_static_config_studio_manifest_to_cv workflow."""

    async def test_empty_manifest_does_nothing(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that an empty manifest results in no actions and an early return."""
        # Create an empty manifest with no configlets or containers.
        empty_manifest = AvdManifest(configlets=(), containers=())

        await deploy_static_config_studio_manifest_to_cv(empty_manifest, deployment_result, mock_cv_client)

        # No API calls should have been made to CloudVision.
        mock_cv_client.set_configlets_from_files.assert_not_called()
        mock_cv_client.set_configlet_containers.assert_not_called()
        mock_cv_client.set_studio_inputs.assert_not_called()
        mock_cv_client.delete_configlets.assert_not_called()
        mock_cv_client.delete_configlet_container.assert_not_called()

        # The result object should remain in its initial empty state.
        assert not deployment_result.deployed_static_config_configlets
        assert not deployment_result.deployed_static_config_containers

    async def test_initial_deployment(self, mock_cv_client: MagicMock, avd_initial_manifest: AvdManifest, deployment_result: DeployToCvResult) -> None:
        """Test initial deployment with no existing configlets or containers on CloudVision."""
        # CV is empty.
        mock_cv_client.get_configlet_containers.return_value = []
        mock_cv_client.get_configlets.return_value = []
        mock_cv_client.get_studio_inputs_with_path.return_value = []

        await deploy_static_config_studio_manifest_to_cv(avd_initial_manifest, deployment_result, mock_cv_client)

        # Verify configlets were created.
        mock_cv_client.set_configlets_from_files.assert_called_once()
        assert len(mock_cv_client.set_configlets_from_files.call_args[1]["configlets"]) == 3

        # Verify containers were created.
        mock_cv_client.set_configlet_containers.assert_called_once()
        assert len(mock_cv_client.set_configlet_containers.call_args[1]["containers"]) == 3

        # Verify root container was set in Studio.
        global_container_id = generate_id("GLOBAL")
        mock_cv_client.set_studio_inputs.assert_called_once_with(
            studio_id="studio-static-configlet",
            workspace_id=deployment_result.workspace.id,
            input_path=["configletAssignmentRoots"],
            inputs=[global_container_id],
        )

        # Verify nothing was deleted.
        mock_cv_client.delete_configlets.assert_not_called()
        mock_cv_client.delete_configlet_container.assert_not_called()

        # Verify deployment result object.
        assert len(deployment_result.deployed_static_config_configlets) == 3
        assert len(deployment_result.deployed_static_config_containers) == 3
        assert not deployment_result.skipped_static_config_containers
        assert not deployment_result.removed_static_config_configlets
        assert not deployment_result.removed_static_config_containers

    async def test_no_changes_run(self, mock_cv_client: MagicMock, avd_initial_manifest: AvdManifest, deployment_result: DeployToCvResult) -> None:
        """Test a subsequent run where the AVD manifest has not changed."""
        # CV initial state matches the avd_initial_manifest.
        vxlan_configlet_id, mlag_configlet_id, bgp_configlet_id = generate_id("VXLAN"), generate_id("MLAG"), generate_id("BGP")
        leafs_container_id, spines_container_id = generate_id("GLOBAL/LEAFS"), generate_id("GLOBAL/SPINES")
        global_container_id = generate_id("GLOBAL")

        existing_containers = [
            create_grpc_container(
                container_id=global_container_id,
                name="GLOBAL",
                description="Global container",
                query="device:*",
                child_ids=[leafs_container_id, spines_container_id],
            ),
            create_grpc_container(
                container_id=leafs_container_id,
                name="LEAFS",
                description="Leafs container",
                query="topology_hint_type:leaf",
                configlet_ids=[vxlan_configlet_id, mlag_configlet_id],
            ),
            create_grpc_container(
                container_id=spines_container_id,
                name="SPINES",
                description="Spines container",
                query="topology_hint_type:spine",
                configlet_ids=[bgp_configlet_id],
            ),
        ]
        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = []
        mock_cv_client.get_studio_inputs_with_path.return_value = [global_container_id]

        await deploy_static_config_studio_manifest_to_cv(avd_initial_manifest, deployment_result, mock_cv_client)

        # Configlets are always pushed for now.
        mock_cv_client.set_configlets_from_files.assert_called_once()

        # Containers should NOT be pushed as they match.
        mock_cv_client.set_configlet_containers.assert_not_called()

        # Studio container roots should NOT be updated as they match.
        mock_cv_client.set_studio_inputs.assert_not_called()

        # Nothing should be deleted.
        mock_cv_client.delete_configlets.assert_not_called()
        mock_cv_client.delete_configlet_container.assert_not_called()

        # Verify deployment result object.
        assert len(deployment_result.deployed_static_config_configlets) == 3
        assert not deployment_result.deployed_static_config_containers
        assert len(deployment_result.skipped_static_config_containers) == 3
        assert not deployment_result.removed_static_config_configlets

    async def test_updates_and_removals(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test modifying a container, adding a new configlet and removing unused AVD-managed entities."""
        # Initial state on CV.
        cf_leaf1_id, cf_leaf2_id = generate_id("CF_LEAF1"), generate_id("CF_LEAF2")
        cf_unused_id = generate_id("CF_UNUSED")
        root_id, cnt_leaf1_id, cnt_leaf2_id = generate_id("ROOT"), generate_id("ROOT/CNT_LEAF1"), generate_id("ROOT/CNT_LEAF2")
        unused_root_id = generate_id("UNUSED_ROOT")

        existing_containers = [
            create_grpc_container(container_id=root_id, name="ROOT", description="Root container", query="device:*", child_ids=[cnt_leaf1_id, cnt_leaf2_id]),
            create_grpc_container(
                container_id=cnt_leaf1_id, name="CNT_LEAF1", description="LEAF1 container - OLD", query="device:LEAF1", configlet_ids=[cf_leaf1_id]
            ),
            create_grpc_container(
                container_id=cnt_leaf2_id, name="CNT_LEAF2", description="LEAF2 container", query="device:LEAF2", configlet_ids=[cf_leaf2_id]
            ),
            create_grpc_container(container_id=unused_root_id, name="UNUSED_ROOT", description="Unused Root", query="tag:unused", configlet_ids=[cf_unused_id]),
        ]
        existing_configlets = [
            Configlet(key=ConfigletKey(configlet_id=cf_leaf1_id), display_name="CF_LEAF1"),
            Configlet(key=ConfigletKey(configlet_id=cf_leaf2_id), display_name="CF_LEAF2"),
            Configlet(key=ConfigletKey(configlet_id=cf_unused_id), display_name="CF_UNUSED"),
        ]
        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = existing_configlets
        mock_cv_client.get_studio_inputs_with_path.return_value = [root_id, unused_root_id]

        # New desired state from AVD.
        cfl1 = AvdConfiglet(name="CF_LEAF1", file=Path("/path/to/cfl1.cfg"))
        cfl2 = AvdConfiglet(name="CF_LEAF2", file=Path("/path/to/cfl2.cfg"))
        cfs1 = AvdConfiglet(name="CF_SPINE1", file=Path("/path/to/cfs1.cfg"))  # New configlet

        cnt_leaf1 = AvdContainer(
            name="CNT_LEAF1",
            tag_query="device:LEAF1",
            description="LEAF1 container - UPDATED",  # Modified description
            configlets=(cfl1.name,),
        )
        cnt_leaf2 = AvdContainer(name="CNT_LEAF2", tag_query="device:LEAF2", description="LEAF2 container", configlets=(cfl2.name,))
        root_container = AvdContainer(name="ROOT", tag_query="device:*", description="Root container", sub_containers=(cnt_leaf1, cnt_leaf2))
        spine_root_container = AvdContainer(name="SPINE_ROOT", tag_query="role:SPINE", configlets=(cfs1.name,))  # New root container

        updated_manifest = AvdManifest(configlets=(cfl1, cfl2, cfs1), containers=(root_container, spine_root_container))

        await deploy_static_config_studio_manifest_to_cv(updated_manifest, deployment_result, mock_cv_client)

        # Verify configlets were created/updated (3 total in manifest).
        mock_cv_client.set_configlets_from_files.assert_called_once()
        assert len(mock_cv_client.set_configlets_from_files.call_args[1]["configlets"]) == 3

        # Verify one unused AVD-managed configlet was deleted.
        mock_cv_client.delete_configlets.assert_called_once_with(workspace_id=deployment_result.workspace.id, configlet_ids=[cf_unused_id])

        # Verify containers were created/updated (CNT_LEAF1 is updated, SPINE_ROOT is new).
        mock_cv_client.set_configlet_containers.assert_called_once()
        pushed_containers = mock_cv_client.set_configlet_containers.call_args[1]["containers"]
        assert len(pushed_containers) == 2
        pushed_container_names = {c[1] for c in pushed_containers}
        assert {"CNT_LEAF1", "SPINE_ROOT"} == pushed_container_names

        # Verify studio roots were updated.
        new_root_ids = [generate_id("ROOT"), generate_id("SPINE_ROOT")]
        mock_cv_client.set_studio_inputs.assert_called_once()
        assert mock_cv_client.set_studio_inputs.call_args[1]["inputs"] == new_root_ids

        # Verify one stale AVD-managed root container was deleted.
        mock_cv_client.delete_configlet_container.assert_called_once_with(workspace_id=deployment_result.workspace.id, assignment_id=unused_root_id)

        # Verify deployment result object.
        assert len(deployment_result.deployed_static_config_configlets) == 3
        assert len(deployment_result.deployed_static_config_containers) == 2
        assert len(deployment_result.skipped_static_config_containers) == 2  # ROOT and CNT_LEAF2 were skipped
        assert deployment_result.removed_static_config_configlets == ["CF_UNUSED"]
        assert deployment_result.removed_static_config_containers == ["UNUSED_ROOT"]

    async def test_root_container_reordering_and_manual_preservation(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test reordering AVD root containers, deleting a stale one and preserving a manually-added root container."""
        # Initial state on CV.
        avd_root1_id = generate_id("AVD_ROOT1")
        avd_root2_id = generate_id("AVD_ROOT2")
        manual_root_id = "manual-root-container-123"  # Does not have the AVD prefix

        existing_containers = [
            create_grpc_container(container_id=avd_root1_id, name="AVD_ROOT1", description="", query="device:*"),
            create_grpc_container(container_id=avd_root2_id, name="AVD_ROOT2", description="", query="device:*"),
            create_grpc_container(container_id=manual_root_id, name="MANUAL_ROOT", description="", query="device:*"),
        ]

        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = []
        # Initial order: AVD, Manual, AVD.
        mock_cv_client.get_studio_inputs_with_path.return_value = [avd_root1_id, manual_root_id, avd_root2_id]

        # New desired state from AVD: AVD_ROOT3, AVD_ROOT2. AVD_ROOT1 is removed and the order is changed.
        avd_root2 = AvdContainer(name="AVD_ROOT2", tag_query="device:*")
        avd_root3 = AvdContainer(name="AVD_ROOT3", tag_query="device:*")
        updated_manifest = AvdManifest(containers=(avd_root3, avd_root2))

        await deploy_static_config_studio_manifest_to_cv(updated_manifest, deployment_result, mock_cv_client)

        # Verify AVD_ROOT3 was created.
        mock_cv_client.set_configlet_containers.assert_called_once()
        pushed_containers = mock_cv_client.set_configlet_containers.call_args[1]["containers"]
        assert len(pushed_containers) == 1
        assert pushed_containers[0][1] == "AVD_ROOT3"

        # Verify the stale AVD root container was deleted.
        mock_cv_client.delete_configlet_container.assert_called_once_with(workspace_id=deployment_result.workspace.id, assignment_id=avd_root1_id)

        # Verify the studio root list was re-ordered correctly, preserving the manual entry at the end.
        avd_root3_id = generate_id("AVD_ROOT3")
        expected_ordered_ids = [avd_root3_id, avd_root2_id, manual_root_id]
        mock_cv_client.set_studio_inputs.assert_called_once_with(
            studio_id="studio-static-configlet",
            workspace_id=deployment_result.workspace.id,
            input_path=["configletAssignmentRoots"],
            inputs=expected_ordered_ids,
        )

        # Verify deployment result object.
        assert len(deployment_result.deployed_static_config_containers) == 1
        assert len(deployment_result.skipped_static_config_containers) == 1  # AVD_ROOT2 was skipped
        assert deployment_result.removed_static_config_containers == ["AVD_ROOT1"]

    async def test_non_root_container_deletion(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that non-root (child) containers are properly deleted when removed from the manifest."""
        # Initial state on CV.
        cf_leaf1_id = generate_id("CF_LEAF1")
        root_id, cnt_leaf1_id, cnt_leaf2_id = generate_id("ROOT"), generate_id("ROOT/CNT_LEAF1"), generate_id("ROOT/CNT_LEAF2")

        existing_containers = [
            create_grpc_container(container_id=root_id, name="ROOT", description="Root container", query="device:*", child_ids=[cnt_leaf1_id, cnt_leaf2_id]),
            create_grpc_container(
                container_id=cnt_leaf1_id, name="CNT_LEAF1", description="LEAF1 container", query="device:LEAF1", configlet_ids=[cf_leaf1_id]
            ),
            create_grpc_container(container_id=cnt_leaf2_id, name="CNT_LEAF2", description="LEAF2 container", query="device:LEAF2"),
        ]

        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = []
        mock_cv_client.get_studio_inputs_with_path.return_value = [root_id]

        # New desired state from AVD: ROOT with only CNT_LEAF1, CNT_LEAF2 is removed from the manifest.
        cfl1 = AvdConfiglet(name="CF_LEAF1", file=Path("/path/to/cfl1.cfg"))
        cnt_leaf1 = AvdContainer(name="CNT_LEAF1", tag_query="device:LEAF1", description="LEAF1 container", configlets=(cfl1.name,))
        root_container = AvdContainer(name="ROOT", tag_query="device:*", description="Root container", sub_containers=(cnt_leaf1,))

        updated_manifest = AvdManifest(configlets=(cfl1,), containers=(root_container,))

        await deploy_static_config_studio_manifest_to_cv(updated_manifest, deployment_result, mock_cv_client)

        # Verify the non-root child container was deleted.
        mock_cv_client.delete_configlet_container.assert_called_once_with(workspace_id=deployment_result.workspace.id, assignment_id=cnt_leaf2_id)

        # Verify ROOT container was updated because child_ids changed.
        mock_cv_client.set_configlet_containers.assert_called_once()
        pushed_containers = mock_cv_client.set_configlet_containers.call_args[1]["containers"]
        assert len(pushed_containers) == 1
        assert pushed_containers[0][1] == "ROOT"

        # Studio roots should NOT be updated as they haven't changed.
        mock_cv_client.set_studio_inputs.assert_not_called()

        # Verify deployment result object.
        assert len(deployment_result.deployed_static_config_configlets) == 1
        assert len(deployment_result.deployed_static_config_containers) == 1  # ROOT was updated
        assert len(deployment_result.skipped_static_config_containers) == 1  # CNT_LEAF1 was skipped
        assert deployment_result.removed_static_config_containers == ["CNT_LEAF2"]
        assert not deployment_result.removed_static_config_configlets

    async def test_loose_container_preserves_existing_children(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that a loose container preserves existing children not in the manifest."""
        # Initial state on CV: ROOT has two children (DC1 and DC2, both AVD-managed) and one manual child.
        root_id = generate_id("ROOT")
        dc1_id = generate_id("ROOT/DC1")
        dc2_id = generate_id("ROOT/DC2")
        manual_child_id = "manual-child-123"

        existing_containers = [
            create_grpc_container(container_id=root_id, name="ROOT", description="Root", query="device:*", child_ids=[dc1_id, dc2_id, manual_child_id]),
            create_grpc_container(container_id=dc1_id, name="DC1", description="DC1", query="dc:DC1"),
            create_grpc_container(container_id=dc2_id, name="DC2", description="DC2", query="dc:DC2"),
            create_grpc_container(container_id=manual_child_id, name="MANUAL", description="Manual", query="dc:MANUAL"),
        ]
        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = []
        mock_cv_client.get_studio_inputs_with_path.return_value = [root_id]

        # New manifest only declares DC1 under a loose ROOT. DC2 and manual child should be preserved.
        dc1_container = AvdContainer(name="DC1", tag_query="dc:DC1", description="DC1")
        root_container = AvdContainer(name="ROOT", tag_query="device:*", description="Root", child_policy="loose", sub_containers=(dc1_container,))
        manifest = AvdManifest(configlets=(), containers=(root_container,))

        await deploy_static_config_studio_manifest_to_cv(manifest, deployment_result, mock_cv_client)

        # No containers should be deleted (loose preserves all children).
        mock_cv_client.delete_configlet_container.assert_not_called()

        # ROOT should NOT be pushed because its merged child_ids match the existing state.
        # Merged: desired [dc1_id] + existing [dc1_id, dc2_id, manual_child_id] -> [dc1_id, dc2_id, manual_child_id]
        # This matches existing, so ROOT is skipped.
        mock_cv_client.set_configlet_containers.assert_not_called()

        # DC1 and ROOT are both skipped (unchanged).
        assert len(deployment_result.skipped_static_config_containers) == 2
        assert not deployment_result.deployed_static_config_containers
        assert not deployment_result.removed_static_config_containers

    async def test_loose_container_adds_new_child(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that a loose container adds a new child while preserving existing ones."""
        # Initial state: ROOT has DC1.
        root_id = generate_id("ROOT")
        dc1_id = generate_id("ROOT/DC1")

        existing_containers = [
            create_grpc_container(container_id=root_id, name="ROOT", description="Root", query="device:*", child_ids=[dc1_id]),
            create_grpc_container(container_id=dc1_id, name="DC1", description="DC1", query="dc:DC1"),
        ]
        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = []
        mock_cv_client.get_studio_inputs_with_path.return_value = [root_id]

        # New manifest declares DC1 and DC2 under loose ROOT.
        dc1_container = AvdContainer(name="DC1", tag_query="dc:DC1", description="DC1")
        dc2_container = AvdContainer(name="DC2", tag_query="dc:DC2", description="DC2")
        root_container = AvdContainer(
            name="ROOT", tag_query="device:*", description="Root", child_policy="loose", sub_containers=(dc1_container, dc2_container)
        )
        manifest = AvdManifest(configlets=(), containers=(root_container,))

        await deploy_static_config_studio_manifest_to_cv(manifest, deployment_result, mock_cv_client)

        # No deletions.
        mock_cv_client.delete_configlet_container.assert_not_called()

        # ROOT should be pushed (child_ids changed: DC2 is new) and DC2 is new.
        mock_cv_client.set_configlet_containers.assert_called_once()
        pushed_containers = mock_cv_client.set_configlet_containers.call_args[1]["containers"]
        pushed_names = {c[1] for c in pushed_containers}
        assert "ROOT" in pushed_names
        assert "DC2" in pushed_names

        # Verify ROOT's pushed child_ids: DC2 (new) is prepended, DC1 (existing) keeps its position.
        dc2_id = generate_id("ROOT/DC2")
        root_pushed = next(c for c in pushed_containers if c[1] == "ROOT")
        assert root_pushed[5] == [dc2_id, dc1_id]

    async def test_loose_child_policy_idempotent_ordering(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that running the same loose manifest twice does not reorder existing children."""
        # Initial state: ROOT already has DC1, DC2, DC3 (e.g., from a previous run that merged multiple manifests).
        root_id = generate_id("ROOT")
        dc1_id = generate_id("ROOT/DC1")
        dc2_id = generate_id("ROOT/DC2")
        dc3_id = generate_id("ROOT/DC3")

        existing_containers = [
            create_grpc_container(container_id=root_id, name="ROOT", description="Root", query="device:*", child_ids=[dc1_id, dc2_id, dc3_id]),
            create_grpc_container(container_id=dc1_id, name="DC1", description="DC1", query="dc:DC1"),
            create_grpc_container(container_id=dc2_id, name="DC2", description="DC2", query="dc:DC2"),
            create_grpc_container(container_id=dc3_id, name="DC3", description="DC3", query="dc:DC3"),
        ]
        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = []
        mock_cv_client.get_studio_inputs_with_path.return_value = [root_id]

        # Manifest only declares DC1 and DC3 under loose ROOT. DC2 was added by another manifest.
        dc1_container = AvdContainer(name="DC1", tag_query="dc:DC1", description="DC1")
        dc3_container = AvdContainer(name="DC3", tag_query="dc:DC3", description="DC3")
        root_container = AvdContainer(
            name="ROOT", tag_query="device:*", description="Root", child_policy="loose", sub_containers=(dc1_container, dc3_container)
        )
        manifest = AvdManifest(configlets=(), containers=(root_container,))

        await deploy_static_config_studio_manifest_to_cv(manifest, deployment_result, mock_cv_client)

        # No containers should be pushed — all declared children already exist, order unchanged.
        mock_cv_client.set_configlet_containers.assert_not_called()

        # No deletions — loose preserves everything.
        mock_cv_client.delete_configlet_container.assert_not_called()

        # All containers skipped (unchanged).
        assert len(deployment_result.skipped_static_config_containers) == 3

    async def test_strict_container_warns_about_manual_children(
        self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult, caplog: pytest.LogCaptureFixture
    ) -> None:
        """Test that a strict container logs a warning when manual children are orphaned."""
        # Initial state: ROOT has DC1 (AVD) and MANUAL (non-AVD).
        root_id = generate_id("ROOT")
        dc1_id = generate_id("ROOT/DC1")
        manual_child_id = "manual-child-456"

        existing_containers = [
            create_grpc_container(container_id=root_id, name="ROOT", description="Root", query="device:*", child_ids=[dc1_id, manual_child_id]),
            create_grpc_container(container_id=dc1_id, name="DC1", description="DC1", query="dc:DC1"),
            create_grpc_container(container_id=manual_child_id, name="MANUAL", description="Manual", query="dc:MANUAL"),
        ]
        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = []
        mock_cv_client.get_studio_inputs_with_path.return_value = [root_id]

        # Strict ROOT only declares DC1. MANUAL will be orphaned.
        dc1_container = AvdContainer(name="DC1", tag_query="dc:DC1", description="DC1")
        root_container = AvdContainer(name="ROOT", tag_query="device:*", description="Root", child_policy="strict", sub_containers=(dc1_container,))
        manifest = AvdManifest(configlets=(), containers=(root_container,))

        with caplog.at_level(logging.WARNING):
            await deploy_static_config_studio_manifest_to_cv(manifest, deployment_result, mock_cv_client)

        # Verify the warning log includes the container name, ID, and the manual child details.
        assert any("child_policy='strict'" in record.message and "ROOT" in record.message and "MANUAL" in record.message for record in caplog.records)

        # Manual child is NOT deleted (we don't delete non-AVD containers).
        # But ROOT is pushed with only DC1 as child, orphaning MANUAL.
        mock_cv_client.set_configlet_containers.assert_called_once()
        pushed_containers = mock_cv_client.set_configlet_containers.call_args[1]["containers"]
        root_pushed = next(c for c in pushed_containers if c[1] == "ROOT")
        assert root_pushed[5] == [dc1_id]  # Only DC1, MANUAL is orphaned.

        # No container deletions (MANUAL is not AVD-managed).
        mock_cv_client.delete_configlet_container.assert_not_called()

    async def test_loose_root_list_preserves_old_avd_roots(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that manifest-level strict=false preserves old AVD roots in the Studio root list."""
        # Initial state: two AVD roots and one manual root.
        avd_root1_id = generate_id("AVD_ROOT1")
        avd_root2_id = generate_id("AVD_ROOT2")
        manual_root_id = "manual-root-789"

        existing_containers = [
            create_grpc_container(container_id=avd_root1_id, name="AVD_ROOT1", description="", query="device:*"),
            create_grpc_container(container_id=avd_root2_id, name="AVD_ROOT2", description="", query="device:*"),
            create_grpc_container(container_id=manual_root_id, name="MANUAL_ROOT", description="", query="device:*"),
        ]
        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = []
        mock_cv_client.get_studio_inputs_with_path.return_value = [avd_root1_id, manual_root_id, avd_root2_id]

        # New manifest (strict=false) declares AVD_ROOT3 and AVD_ROOT2. AVD_ROOT1 should NOT be removed.
        avd_root2 = AvdContainer(name="AVD_ROOT2", tag_query="device:*")
        avd_root3 = AvdContainer(name="AVD_ROOT3", tag_query="device:*")
        manifest = AvdManifest(root_policy="loose", configlets=(), containers=(avd_root3, avd_root2))

        await deploy_static_config_studio_manifest_to_cv(manifest, deployment_result, mock_cv_client)

        # Verify studio roots: only AVD_ROOT3 (new) is prepended. Existing roots keep their position.
        avd_root3_id = generate_id("AVD_ROOT3")
        mock_cv_client.set_studio_inputs.assert_called_once()
        new_root_ids = mock_cv_client.set_studio_inputs.call_args[1]["inputs"]
        assert new_root_ids == [avd_root3_id, avd_root1_id, manual_root_id, avd_root2_id]

    async def test_deep_subtree_preservation_with_loose(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that a loose container preserves deep subtrees including children of undeclared containers."""
        # Initial state: ROOT -> DC1 -> LEAF1, LEAF2.
        root_id = generate_id("ROOT")
        dc1_id = generate_id("ROOT/DC1")
        leaf1_id = generate_id("ROOT/DC1/LEAF1")
        leaf2_id = generate_id("ROOT/DC1/LEAF2")

        existing_containers = [
            create_grpc_container(container_id=root_id, name="ROOT", description="Root", query="device:*", child_ids=[dc1_id]),
            create_grpc_container(container_id=dc1_id, name="DC1", description="DC1", query="dc:DC1", child_ids=[leaf1_id, leaf2_id]),
            create_grpc_container(container_id=leaf1_id, name="LEAF1", description="LEAF1", query="device:LEAF1"),
            create_grpc_container(container_id=leaf2_id, name="LEAF2", description="LEAF2", query="device:LEAF2"),
        ]
        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = []
        mock_cv_client.get_studio_inputs_with_path.return_value = [root_id]

        # Loose ROOT only declares DC3. DC1 and its subtree are not in the manifest.
        dc3_container = AvdContainer(name="DC3", tag_query="dc:DC3", description="DC3")
        root_container = AvdContainer(name="ROOT", tag_query="device:*", description="Root", child_policy="loose", sub_containers=(dc3_container,))
        manifest = AvdManifest(configlets=(), containers=(root_container,))

        await deploy_static_config_studio_manifest_to_cv(manifest, deployment_result, mock_cv_client)

        # No containers should be deleted (DC1, LEAF1, LEAF2 are reachable through merged ROOT children).
        mock_cv_client.delete_configlet_container.assert_not_called()

        # ROOT should be pushed with merged child_ids (DC3 added, DC1 preserved).
        dc3_id = generate_id("ROOT/DC3")
        mock_cv_client.set_configlet_containers.assert_called_once()
        pushed_containers = mock_cv_client.set_configlet_containers.call_args[1]["containers"]
        root_pushed = next(c for c in pushed_containers if c[1] == "ROOT")
        assert set(root_pushed[5]) == {dc3_id, dc1_id}

    async def test_cascading_deletion_with_strict(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that removing a subtree from a strict container cascades deletion to all descendants."""
        root_id = generate_id("ROOT")
        dc1_id = generate_id("ROOT/DC1")
        leaf1_id = generate_id("ROOT/DC1/LEAF1")
        leaf2_id = generate_id("ROOT/DC1/LEAF2")

        existing_containers = [
            create_grpc_container(container_id=root_id, name="ROOT", description="Root", query="device:*", child_ids=[dc1_id]),
            create_grpc_container(container_id=dc1_id, name="DC1", description="DC1", query="dc:DC1", child_ids=[leaf1_id, leaf2_id]),
            create_grpc_container(container_id=leaf1_id, name="LEAF1", description="LEAF1", query="device:LEAF1"),
            create_grpc_container(container_id=leaf2_id, name="LEAF2", description="LEAF2", query="device:LEAF2"),
        ]
        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = []
        mock_cv_client.get_studio_inputs_with_path.return_value = [root_id]

        # Strict ROOT only declares DC2 (new). DC1 and its entire subtree should be deleted.
        dc2_container = AvdContainer(name="DC2", tag_query="dc:DC2", description="DC2")
        root_container = AvdContainer(name="ROOT", tag_query="device:*", description="Root", child_policy="strict", sub_containers=(dc2_container,))
        manifest = AvdManifest(configlets=(), containers=(root_container,))

        await deploy_static_config_studio_manifest_to_cv(manifest, deployment_result, mock_cv_client)

        # DC1, LEAF1, LEAF2 should all be deleted (unreachable after ROOT drops DC1).
        deleted_ids = {call.kwargs["assignment_id"] for call in mock_cv_client.delete_configlet_container.call_args_list}
        assert deleted_ids == {dc1_id, leaf1_id, leaf2_id}

    async def test_strict_inside_loose(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that a strict container nested inside a loose container correctly manages its children."""
        root_id = generate_id("ROOT")
        dc1_id = generate_id("ROOT/DC1")
        leaf1_id = generate_id("ROOT/DC1/LEAF1")
        leaf2_id = generate_id("ROOT/DC1/LEAF2")
        leaf3_id = generate_id("ROOT/DC1/LEAF3")

        existing_containers = [
            create_grpc_container(container_id=root_id, name="ROOT", description="Root", query="device:*", child_ids=[dc1_id]),
            create_grpc_container(container_id=dc1_id, name="DC1", description="DC1", query="dc:DC1", child_ids=[leaf1_id, leaf2_id, leaf3_id]),
            create_grpc_container(container_id=leaf1_id, name="LEAF1", description="LEAF1", query="device:LEAF1"),
            create_grpc_container(container_id=leaf2_id, name="LEAF2", description="LEAF2", query="device:LEAF2"),
            create_grpc_container(container_id=leaf3_id, name="LEAF3", description="LEAF3", query="device:LEAF3"),
        ]
        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = []
        mock_cv_client.get_studio_inputs_with_path.return_value = [root_id]

        # ROOT is loose (preserves existing children), DC1 is strict (only LEAF1 declared).
        leaf1_container = AvdContainer(name="LEAF1", tag_query="device:LEAF1", description="LEAF1")
        dc1_container = AvdContainer(name="DC1", tag_query="dc:DC1", description="DC1", child_policy="strict", sub_containers=(leaf1_container,))
        root_container = AvdContainer(name="ROOT", tag_query="device:*", description="Root", child_policy="loose", sub_containers=(dc1_container,))
        manifest = AvdManifest(configlets=(), containers=(root_container,))

        await deploy_static_config_studio_manifest_to_cv(manifest, deployment_result, mock_cv_client)

        # LEAF2 and LEAF3 should be deleted (DC1 is strict, only LEAF1 is declared → LEAF2/LEAF3 are unreachable).
        deleted_ids = {call.kwargs["assignment_id"] for call in mock_cv_client.delete_configlet_container.call_args_list}
        assert deleted_ids == {leaf2_id, leaf3_id}

        # DC1 should be pushed (child_ids changed from [LEAF1, LEAF2, LEAF3] to [LEAF1]).
        mock_cv_client.set_configlet_containers.assert_called_once()
        pushed_containers = mock_cv_client.set_configlet_containers.call_args[1]["containers"]
        dc1_pushed = next(c for c in pushed_containers if c[1] == "DC1")
        assert dc1_pushed[5] == [leaf1_id]  # Only LEAF1 remains.

    async def test_selective_child_policy_keeps_manual_drops_avd(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that selective child_policy keeps manual children but drops undeclared AVD-managed children."""
        root_id = generate_id("ROOT")
        dc1_id = generate_id("ROOT/DC1")
        dc2_id = generate_id("ROOT/DC2")
        manual_child_id = "manual-child-selective"

        existing_containers = [
            create_grpc_container(container_id=root_id, name="ROOT", description="Root", query="device:*", child_ids=[dc1_id, dc2_id, manual_child_id]),
            create_grpc_container(container_id=dc1_id, name="DC1", description="DC1", query="dc:DC1"),
            create_grpc_container(container_id=dc2_id, name="DC2", description="DC2", query="dc:DC2"),
            create_grpc_container(container_id=manual_child_id, name="MANUAL", description="Manual", query="dc:MANUAL"),
        ]
        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = []
        mock_cv_client.get_studio_inputs_with_path.return_value = [root_id]

        # Selective ROOT only declares DC1. DC2 (AVD) should be dropped, MANUAL should be preserved.
        dc1_container = AvdContainer(name="DC1", tag_query="dc:DC1", description="DC1")
        root_container = AvdContainer(name="ROOT", tag_query="device:*", description="Root", child_policy="selective", sub_containers=(dc1_container,))
        manifest = AvdManifest(configlets=(), containers=(root_container,))

        await deploy_static_config_studio_manifest_to_cv(manifest, deployment_result, mock_cv_client)

        # DC2 should be deleted (AVD-managed, not declared, unreachable after selective drops it).
        deleted_ids = {call.kwargs["assignment_id"] for call in mock_cv_client.delete_configlet_container.call_args_list}
        assert deleted_ids == {dc2_id}

        # ROOT should be pushed (child_ids changed: DC2 dropped, MANUAL preserved).
        mock_cv_client.set_configlet_containers.assert_called_once()
        pushed_containers = mock_cv_client.set_configlet_containers.call_args[1]["containers"]
        root_pushed = next(c for c in pushed_containers if c[1] == "ROOT")
        assert set(root_pushed[5]) == {dc1_id, manual_child_id}  # DC1 (declared) + MANUAL (preserved)

    async def test_strict_root_policy_drops_manual_roots(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that strict root_policy drops manual roots from the root list."""
        avd_root_id = generate_id("AVD_ROOT")
        manual_root_id = "manual-root-strict"

        existing_containers = [
            create_grpc_container(container_id=avd_root_id, name="AVD_ROOT", description="", query="device:*"),
            create_grpc_container(container_id=manual_root_id, name="MANUAL_ROOT", description="", query="device:*"),
        ]
        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = []
        mock_cv_client.get_studio_inputs_with_path.return_value = [avd_root_id, manual_root_id]

        # Strict root_policy: only declared roots remain, manual roots are dropped.
        avd_root = AvdContainer(name="AVD_ROOT", tag_query="device:*")
        manifest = AvdManifest(root_policy="strict", configlets=(), containers=(avd_root,))

        await deploy_static_config_studio_manifest_to_cv(manifest, deployment_result, mock_cv_client)

        # Root list should contain only the declared AVD root (manual root dropped).
        mock_cv_client.set_studio_inputs.assert_called_once()
        new_root_ids = mock_cv_client.set_studio_inputs.call_args[1]["inputs"]
        assert new_root_ids == [avd_root_id]

    async def test_pre_existing_orphans_are_always_cleaned_up(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that AVD-managed containers already orphaned on CV are cleaned up regardless of policy."""
        root_id = generate_id("ROOT")
        dc1_id = generate_id("ROOT/DC1")
        orphan_id = generate_id("OLD_ORPHAN")

        existing_containers = [
            create_grpc_container(container_id=root_id, name="ROOT", description="Root", query="device:*", child_ids=[dc1_id]),
            create_grpc_container(container_id=dc1_id, name="DC1", description="DC1", query="dc:DC1"),
            # Pre-existing orphan: AVD-managed but not referenced by any container.
            create_grpc_container(container_id=orphan_id, name="OLD_ORPHAN", description="Stale", query="device:old"),
        ]
        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = []
        mock_cv_client.get_studio_inputs_with_path.return_value = [root_id]

        # Manifest matches existing state (no changes) but uses loose policy.
        dc1_container = AvdContainer(name="DC1", tag_query="dc:DC1", description="DC1")
        root_container = AvdContainer(name="ROOT", tag_query="device:*", description="Root", child_policy="loose", sub_containers=(dc1_container,))
        manifest = AvdManifest(root_policy="loose", configlets=(), containers=(root_container,))

        await deploy_static_config_studio_manifest_to_cv(manifest, deployment_result, mock_cv_client)

        # The pre-existing orphan should be deleted even with loose policies.
        deleted_ids = {call.kwargs["assignment_id"] for call in mock_cv_client.delete_configlet_container.call_args_list}
        assert deleted_ids == {orphan_id}

    async def test_mixed_child_policies_in_same_manifest(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test a manifest with different child_policies on different containers."""
        root_id = generate_id("ROOT")
        dc1_id = generate_id("ROOT/DC1")
        dc2_id = generate_id("ROOT/DC2")
        leaf1_id = generate_id("ROOT/DC1/LEAF1")
        leaf2_id = generate_id("ROOT/DC1/LEAF2")
        leaf3_id = generate_id("ROOT/DC2/LEAF3")
        leaf4_id = generate_id("ROOT/DC2/LEAF4")

        existing_containers = [
            create_grpc_container(container_id=root_id, name="ROOT", description="Root", query="device:*", child_ids=[dc1_id, dc2_id]),
            create_grpc_container(container_id=dc1_id, name="DC1", description="DC1", query="dc:DC1", child_ids=[leaf1_id, leaf2_id]),
            create_grpc_container(container_id=dc2_id, name="DC2", description="DC2", query="dc:DC2", child_ids=[leaf3_id, leaf4_id]),
            create_grpc_container(container_id=leaf1_id, name="LEAF1", description="LEAF1", query="device:LEAF1"),
            create_grpc_container(container_id=leaf2_id, name="LEAF2", description="LEAF2", query="device:LEAF2"),
            create_grpc_container(container_id=leaf3_id, name="LEAF3", description="LEAF3", query="device:LEAF3"),
            create_grpc_container(container_id=leaf4_id, name="LEAF4", description="LEAF4", query="device:LEAF4"),
        ]
        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = []
        mock_cv_client.get_studio_inputs_with_path.return_value = [root_id]

        # DC1 is strict (only LEAF1), DC2 is loose (preserves LEAF3 and LEAF4).
        leaf1_container = AvdContainer(name="LEAF1", tag_query="device:LEAF1", description="LEAF1")
        dc1_container = AvdContainer(name="DC1", tag_query="dc:DC1", description="DC1", child_policy="strict", sub_containers=(leaf1_container,))
        dc2_container = AvdContainer(name="DC2", tag_query="dc:DC2", description="DC2", child_policy="loose")
        root_container = AvdContainer(name="ROOT", tag_query="device:*", description="Root", sub_containers=(dc1_container, dc2_container))
        manifest = AvdManifest(configlets=(), containers=(root_container,))

        await deploy_static_config_studio_manifest_to_cv(manifest, deployment_result, mock_cv_client)

        # LEAF2 should be deleted (DC1 is strict, only LEAF1 declared).
        # LEAF3 and LEAF4 should be preserved (DC2 is loose).
        deleted_ids = {call.kwargs["assignment_id"] for call in mock_cv_client.delete_configlet_container.call_args_list}
        assert deleted_ids == {leaf2_id}
