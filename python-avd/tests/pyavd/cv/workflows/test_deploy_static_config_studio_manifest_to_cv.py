# Copyright (c) 2025-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
# pylint: disable=too-many-lines
from pathlib import Path
from unittest.mock import MagicMock

import pytest

from pyavd._cv.api.arista.configlet.v1 import Configlet, ConfigletKey
from pyavd._cv.client.exceptions import CVManifestError
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

    async def test_root_container_removal_only(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that removing an AVD root container updates the Studio even if no new roots are added."""
        avd_root_keep_id, avd_root_remove_id = generate_id("ROOT_KEEP"), generate_id("ROOT_REMOVE")

        existing_containers = [
            create_grpc_container(container_id=avd_root_keep_id, name="ROOT_KEEP", description="Kept Root", query="device:*"),
            create_grpc_container(container_id=avd_root_remove_id, name="ROOT_REMOVE", description="Removed Root", query="device:*"),
        ]
        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = []
        mock_cv_client.get_studio_inputs_with_path.return_value = [avd_root_keep_id, avd_root_remove_id]

        # Desired state: Only ROOT_KEEP remains. ROOT_REMOVE is omitted.
        root_keep = AvdContainer(name="ROOT_KEEP", tag_query="device:*", description="Kept Root")
        manifest = AvdManifest(containers=(root_keep,))

        await deploy_static_config_studio_manifest_to_cv(manifest, deployment_result, mock_cv_client)

        # Verify the Studio inputs were updated to remove the orphaned root.
        mock_cv_client.set_studio_inputs.assert_called_once_with(
            studio_id="studio-static-configlet",
            workspace_id=deployment_result.workspace.id,
            input_path=["configletAssignmentRoots"],
            inputs=[avd_root_keep_id],
        )

        # Verify the container itself was deleted.
        mock_cv_client.delete_configlet_container.assert_called_once_with(workspace_id=deployment_result.workspace.id, assignment_id=avd_root_remove_id)

        # Verify deployment result object.
        assert deployment_result.removed_static_config_containers == ["ROOT_REMOVE"]

    async def test_root_removal_preserves_manual_position(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that removing an AVD root keeps manually-added containers in their current position."""
        avd_root1_id = generate_id("AVD_ROOT1")
        avd_root2_id = generate_id("AVD_ROOT2")
        manual_root1_id = "manual-root-container-456"
        manual_root2_id = "manual-root-container-789"

        existing_containers = [
            create_grpc_container(container_id=avd_root1_id, name="AVD_ROOT1", description="", query="device:*"),
            create_grpc_container(container_id=avd_root2_id, name="AVD_ROOT2", description="", query="device:*"),
            create_grpc_container(container_id=manual_root1_id, name="MANUAL_ROOT_1", description="", query="device:*"),
            create_grpc_container(container_id=manual_root2_id, name="MANUAL_ROOT_2", description="", query="device:*"),
        ]
        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = []
        # Manual roots are placed first and interleaved with the AVD roots.
        mock_cv_client.get_studio_inputs_with_path.return_value = [manual_root1_id, avd_root1_id, manual_root2_id, avd_root2_id]

        # New desired state: AVD_ROOT2 removed, AVD_ROOT1 kept.
        avd_root1 = AvdContainer(name="AVD_ROOT1", tag_query="device:*")
        updated_manifest = AvdManifest(containers=(avd_root1,))

        await deploy_static_config_studio_manifest_to_cv(updated_manifest, deployment_result, mock_cv_client)

        # Verify AVD_ROOT2 was deleted.
        mock_cv_client.delete_configlet_container.assert_called_once_with(workspace_id=deployment_result.workspace.id, assignment_id=avd_root2_id)

        # Verify the studio root list preserves both manual roots in their original positions.
        mock_cv_client.set_studio_inputs.assert_called_once_with(
            studio_id="studio-static-configlet",
            workspace_id=deployment_result.workspace.id,
            input_path=["configletAssignmentRoots"],
            inputs=[manual_root1_id, avd_root1_id, manual_root2_id],
        )

        assert deployment_result.removed_static_config_containers == ["AVD_ROOT2"]

    async def test_configlets_only_manifest(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that a manifest containing only configlets (unassigned) and no containers is supported."""
        mock_cv_client.get_configlet_containers.return_value = []
        mock_cv_client.get_configlets.return_value = []
        mock_cv_client.get_studio_inputs_with_path.return_value = []

        configlet = AvdConfiglet(name="STANDALONE_CFG", file=Path("standalone.cfg"))
        manifest = AvdManifest(configlets=(configlet,), containers=())

        await deploy_static_config_studio_manifest_to_cv(manifest, deployment_result, mock_cv_client)

        # Configlet was created.
        mock_cv_client.set_configlets_from_files.assert_called_once()
        assert len(mock_cv_client.set_configlets_from_files.call_args[1]["configlets"]) == 1

        # No container actions.
        mock_cv_client.set_configlet_containers.assert_not_called()
        mock_cv_client.delete_configlet_container.assert_not_called()

        # No studio root update needed (existing list is already empty and no desired roots).
        mock_cv_client.set_studio_inputs.assert_not_called()

        # No deletions.
        mock_cv_client.delete_configlets.assert_not_called()

        # Result.
        assert len(deployment_result.deployed_static_config_configlets) == 1
        assert not deployment_result.deployed_static_config_containers
        assert not deployment_result.skipped_static_config_containers
        assert not deployment_result.removed_static_config_configlets
        assert not deployment_result.removed_static_config_containers

    async def test_configlet_deletion_when_manifest_has_no_configlets(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that existing AVD-managed configlets are deleted when the manifest has containers but no configlets."""
        stale_avd_configlet_id = generate_id("STALE_CFG")
        root_id = generate_id("ROOT")

        existing_containers = [
            create_grpc_container(container_id=root_id, name="ROOT", description="Root", query="device:*"),
        ]
        existing_configlets = [
            Configlet(key=ConfigletKey(configlet_id=stale_avd_configlet_id), display_name="STALE_CFG"),
        ]
        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = existing_configlets
        mock_cv_client.get_studio_inputs_with_path.return_value = [root_id]

        # Manifest has a container but no configlets at all.
        root = AvdContainer(name="ROOT", tag_query="device:*", description="Root")
        manifest = AvdManifest(configlets=(), containers=(root,))

        await deploy_static_config_studio_manifest_to_cv(manifest, deployment_result, mock_cv_client)

        # No configlets to push, so the create/update API must not be called.
        mock_cv_client.set_configlets_from_files.assert_not_called()

        # The stale AVD-managed configlet must be deleted.
        mock_cv_client.delete_configlets.assert_called_once_with(workspace_id=deployment_result.workspace.id, configlet_ids=[stale_avd_configlet_id])

        assert deployment_result.removed_static_config_configlets == ["STALE_CFG"]
        assert not deployment_result.deployed_static_config_configlets

    async def test_non_avd_configlets_are_preserved(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that existing configlets without the AVD prefix are never deleted."""
        non_avd_configlet_id = "manually-created-configlet-xyz"
        root_id = generate_id("ROOT")

        existing_containers = [
            create_grpc_container(container_id=root_id, name="ROOT", description="Root", query="device:*"),
        ]
        existing_configlets = [
            Configlet(key=ConfigletKey(configlet_id=non_avd_configlet_id), display_name="NON_AVD_CFG"),
        ]
        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = existing_configlets
        mock_cv_client.get_studio_inputs_with_path.return_value = [root_id]

        root = AvdContainer(name="ROOT", tag_query="device:*", description="Root")
        manifest = AvdManifest(configlets=(), containers=(root,))

        await deploy_static_config_studio_manifest_to_cv(manifest, deployment_result, mock_cv_client)

        # Non-AVD configlet must NOT be deleted.
        mock_cv_client.delete_configlets.assert_not_called()
        assert not deployment_result.removed_static_config_configlets

    async def test_non_avd_containers_are_preserved(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that unrelated manual containers are preserved, even if they are orphaned."""
        avd_root_id = generate_id("AVD_ROOT")
        non_avd_container_id = "manually-created-container-abc"
        manual_orphan_id = "manual-orphan-container"

        existing_containers = [
            create_grpc_container(container_id=avd_root_id, name="AVD_ROOT", description="Root", query="device:*"),
            create_grpc_container(container_id=non_avd_container_id, name="MANUAL_CONTAINER", description="Manual", query="device:*"),
            create_grpc_container(container_id=manual_orphan_id, name="MANUAL_ORPHAN", description="", query="device:*"),
        ]
        # All containers
        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = []
        # Root containers - manual-orphan-container is intentionally not a root and has no parent.
        mock_cv_client.get_studio_inputs_with_path.return_value = [avd_root_id, non_avd_container_id]

        # Manifest matches the existing AVD root (so AVD_ROOT is unchanged).
        avd_root = AvdContainer(name="AVD_ROOT", tag_query="device:*", description="Root")
        manifest = AvdManifest(containers=(avd_root,))

        await deploy_static_config_studio_manifest_to_cv(manifest, deployment_result, mock_cv_client)

        # Non-AVD container must NOT be deleted.
        mock_cv_client.delete_configlet_container.assert_not_called()
        mock_cv_client.set_configlet_containers.assert_not_called()
        assert not deployment_result.removed_static_config_containers

    async def test_container_update_on_tag_query_change(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that a change in tag_query alone triggers a container update."""
        root_id = generate_id("ROOT")
        existing_containers = [
            create_grpc_container(container_id=root_id, name="ROOT", description="Root", query="device:OLD"),
        ]
        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = []
        mock_cv_client.get_studio_inputs_with_path.return_value = [root_id]

        # Only tag_query changes.
        root = AvdContainer(name="ROOT", tag_query="device:NEW", description="Root")
        manifest = AvdManifest(containers=(root,))

        await deploy_static_config_studio_manifest_to_cv(manifest, deployment_result, mock_cv_client)

        mock_cv_client.set_configlet_containers.assert_called_once()
        pushed = mock_cv_client.set_configlet_containers.call_args[1]["containers"]
        assert len(pushed) == 1
        assert pushed[0][1] == "ROOT"
        assert len(deployment_result.deployed_static_config_containers) == 1
        assert not deployment_result.skipped_static_config_containers

    async def test_container_update_on_configlets_change(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that a change in attached configlet IDs alone triggers a container update."""
        root_id = generate_id("ROOT")
        cfg_id = generate_id("CFG")
        # Existing container has no configlets attached.
        existing_containers = [
            create_grpc_container(container_id=root_id, name="ROOT", description="Root", query="device:*", configlet_ids=[]),
        ]
        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = []
        mock_cv_client.get_studio_inputs_with_path.return_value = [root_id]

        # Manifest now attaches one configlet to the same container.
        cfg = AvdConfiglet(name="CFG", file=Path("cfg.cfg"))
        root = AvdContainer(name="ROOT", tag_query="device:*", description="Root", configlets=(cfg.name,))
        manifest = AvdManifest(configlets=(cfg,), containers=(root,))

        await deploy_static_config_studio_manifest_to_cv(manifest, deployment_result, mock_cv_client)

        mock_cv_client.set_configlet_containers.assert_called_once()
        pushed = mock_cv_client.set_configlet_containers.call_args[1]["containers"]
        assert len(pushed) == 1
        # The pushed container has the new configlet ID attached.
        assert pushed[0][1] == "ROOT"
        assert pushed[0][3] == [cfg_id]

    async def test_container_update_on_match_policy_change(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that a change in match_policy alone triggers a container update."""
        root_id = generate_id("ROOT")
        existing_containers = [
            create_grpc_container(container_id=root_id, name="ROOT", description="Root", query="device:*"),
        ]
        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = []
        mock_cv_client.get_studio_inputs_with_path.return_value = [root_id]

        root = AvdContainer(name="ROOT", tag_query="device:*", description="Root", match_policy="match_first")
        manifest = AvdManifest(containers=(root,))

        await deploy_static_config_studio_manifest_to_cv(manifest, deployment_result, mock_cv_client)

        mock_cv_client.set_configlet_containers.assert_called_once()
        pushed = mock_cv_client.set_configlet_containers.call_args[1]["containers"]
        assert len(pushed) == 1
        # The match_policy is the last element of the api_tuple.
        assert pushed[0][-1] == "match_first"

    async def test_multiple_avd_root_containers_deleted_in_parallel(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that multiple stale AVD-managed root containers are all deleted in a single run via gather."""
        stale_root1_id, stale_root2_id, stale_root3_id = (
            generate_id("STALE_ROOT_1"),
            generate_id("STALE_ROOT_2"),
            generate_id("STALE_ROOT_3"),
        )

        existing_containers = [
            create_grpc_container(container_id=stale_root1_id, name="STALE_ROOT_1", description="", query="device:*"),
            create_grpc_container(container_id=stale_root2_id, name="STALE_ROOT_2", description="", query="device:*"),
            create_grpc_container(container_id=stale_root3_id, name="STALE_ROOT_3", description="", query="device:*"),
        ]
        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = []
        mock_cv_client.get_studio_inputs_with_path.return_value = [stale_root1_id, stale_root2_id, stale_root3_id]

        # Manifest has a single new root that replaces all three stale ones.
        new_root = AvdContainer(name="NEW_ROOT", tag_query="device:*")
        manifest = AvdManifest(containers=(new_root,))

        await deploy_static_config_studio_manifest_to_cv(manifest, deployment_result, mock_cv_client)

        # All three stale AVD-managed containers must be deleted.
        assert mock_cv_client.delete_configlet_container.call_count == 3
        deleted_ids = {call.kwargs["assignment_id"] for call in mock_cv_client.delete_configlet_container.call_args_list}
        assert deleted_ids == {stale_root1_id, stale_root2_id, stale_root3_id}

        # All three must be reported in the result, in any order.
        assert set(deployment_result.removed_static_config_containers) == {"STALE_ROOT_1", "STALE_ROOT_2", "STALE_ROOT_3"}

    async def test_manual_studio_reordering_preserved_on_no_change_repush(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that a user's manual reordering of the studio root list is preserved on a no-change re-push."""
        avd_root1_id, avd_root2_id = generate_id("AVD_ROOT1"), generate_id("AVD_ROOT2")
        manual_root_id = "manual-root-foo"

        existing_containers = [
            create_grpc_container(container_id=avd_root1_id, name="AVD_ROOT1", description="", query="device:*"),
            create_grpc_container(container_id=avd_root2_id, name="AVD_ROOT2", description="", query="device:*"),
            create_grpc_container(container_id=manual_root_id, name="MANUAL_ROOT", description="", query="device:*"),
        ]
        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = []
        # User manually reordered to: AVD_ROOT2, MANUAL_ROOT, AVD_ROOT1 (different from manifest order).
        mock_cv_client.get_studio_inputs_with_path.return_value = [avd_root2_id, manual_root_id, avd_root1_id]

        # Manifest declares the same AVD roots in their original (different) order.
        avd_root1 = AvdContainer(name="AVD_ROOT1", tag_query="device:*")
        avd_root2 = AvdContainer(name="AVD_ROOT2", tag_query="device:*")
        manifest = AvdManifest(containers=(avd_root1, avd_root2))

        await deploy_static_config_studio_manifest_to_cv(manifest, deployment_result, mock_cv_client)

        # Studio root list must NOT be updated — the user's manual ordering is preserved.
        mock_cv_client.set_studio_inputs.assert_not_called()
        # No container deletions either.
        mock_cv_client.delete_configlet_container.assert_not_called()
        # No containers were modified (matched the existing CV state).
        mock_cv_client.set_configlet_containers.assert_not_called()

    async def test_orphaned_avd_containers_are_cleaned_up(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that AVD-managed containers existing in the DB but no longer referenced by any root or parent get cleaned up."""
        orphan_root_id = generate_id("ORPHAN_ROOT")
        orphan_child_id = generate_id("ORPHAN_ROOT/ORPHAN_CHILD")
        new_root_id = generate_id("NEW_ROOT")

        # An old AVD hierarchy still in the DB but no longer referenced by the studio root list.
        existing_containers = [
            create_grpc_container(container_id=orphan_root_id, name="ORPHAN_ROOT", description="", query="device:*", child_ids=[orphan_child_id]),
            create_grpc_container(container_id=orphan_child_id, name="ORPHAN_CHILD", description="", query="device:LEAF"),
        ]
        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = []
        # Studio root list is empty — the orphan was already unregistered as a root.
        mock_cv_client.get_studio_inputs_with_path.return_value = []

        # Manifest declares a brand-new root, unrelated to the orphans.
        new_root = AvdContainer(name="NEW_ROOT", tag_query="device:*")
        manifest = AvdManifest(containers=(new_root,))

        await deploy_static_config_studio_manifest_to_cv(manifest, deployment_result, mock_cv_client)

        # Both orphan containers must be deleted, even though neither was ever in the studio root list.
        assert mock_cv_client.delete_configlet_container.call_count == 2
        deleted_ids = {call.kwargs["assignment_id"] for call in mock_cv_client.delete_configlet_container.call_args_list}
        assert deleted_ids == {orphan_root_id, orphan_child_id}
        assert set(deployment_result.removed_static_config_containers) == {"ORPHAN_ROOT", "ORPHAN_CHILD"}

        # The new root is created.
        mock_cv_client.set_configlet_containers.assert_called_once()
        pushed = mock_cv_client.set_configlet_containers.call_args[1]["containers"]
        assert len(pushed) == 1
        assert pushed[0][1] == "NEW_ROOT"

        # The studio root list is updated to include only the new root.
        mock_cv_client.set_studio_inputs.assert_called_once_with(
            studio_id="studio-static-configlet",
            workspace_id=deployment_result.workspace.id,
            input_path=["configletAssignmentRoots"],
            inputs=[new_root_id],
        )

    async def test_avd_parent_unassigns_non_avd_sub_container(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that a non-AVD sub-container under an AVD parent is unassigned and removed as an orphan when the parent is re-pushed."""
        avd_parent_id = generate_id("PARENT")
        avd_child_id = generate_id("PARENT/AVD_CHILD")
        non_avd_child_id = "manually-added-child-xyz"

        existing_containers = [
            # Existing parent has BOTH an AVD and a non-AVD child.
            create_grpc_container(
                container_id=avd_parent_id,
                name="PARENT",
                description="Parent",
                query="device:*",
                child_ids=[avd_child_id, non_avd_child_id],
            ),
            create_grpc_container(container_id=avd_child_id, name="AVD_CHILD", description="", query="device:LEAF"),
            create_grpc_container(container_id=non_avd_child_id, name="MANUAL_CHILD", description="", query="device:MANUAL"),
        ]
        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = []
        mock_cv_client.get_studio_inputs_with_path.return_value = [avd_parent_id]

        # Manifest declares only the AVD parent + AVD child (no awareness of MANUAL_CHILD).
        avd_child = AvdContainer(name="AVD_CHILD", tag_query="device:LEAF")
        avd_parent = AvdContainer(name="PARENT", tag_query="device:*", description="Parent", sub_containers=(avd_child,))
        manifest = AvdManifest(containers=(avd_parent,))

        await deploy_static_config_studio_manifest_to_cv(manifest, deployment_result, mock_cv_client)

        # Parent must be re-pushed because its child_ids differ from CV state.
        mock_cv_client.set_configlet_containers.assert_called_once()
        pushed = mock_cv_client.set_configlet_containers.call_args[1]["containers"]
        parent_push = next(c for c in pushed if c[1] == "PARENT")
        # Pushed child_ids contains ONLY the AVD child — the non-AVD child has been unassigned.
        assert parent_push[5] == [avd_child_id]
        assert non_avd_child_id not in parent_push[5]

        # The non-AVD sub-container is removed as an orphan since it no longer has a parent in the tree.
        mock_cv_client.delete_configlet_container.assert_called_once_with(workspace_id=deployment_result.workspace.id, assignment_id=non_avd_child_id)
        assert deployment_result.removed_static_config_containers == ["MANUAL_CHILD"]

    async def test_sub_containers_excluded_from_studio_roots(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that only top-level (root) containers are added to the Studio root list, not nested sub-containers."""
        mock_cv_client.get_configlet_containers.return_value = []
        mock_cv_client.get_configlets.return_value = []
        mock_cv_client.get_studio_inputs_with_path.return_value = []

        # Build a hierarchy with a sub-container that should NOT appear in studio root list.
        leaf = AvdContainer(name="LEAF", tag_query="device:LEAF")
        spine = AvdContainer(name="SPINE", tag_query="device:SPINE")
        root_a = AvdContainer(name="ROOT_A", tag_query="device:*", sub_containers=(leaf,))
        root_b = AvdContainer(name="ROOT_B", tag_query="device:*", sub_containers=(spine,))
        manifest = AvdManifest(containers=(root_a, root_b))

        await deploy_static_config_studio_manifest_to_cv(manifest, deployment_result, mock_cv_client)

        # 4 containers were created (2 roots + 2 leaves).
        mock_cv_client.set_configlet_containers.assert_called_once()
        assert len(mock_cv_client.set_configlet_containers.call_args[1]["containers"]) == 4

        # But only the 2 roots should be in the studio root list.
        mock_cv_client.set_studio_inputs.assert_called_once()
        studio_root_ids = mock_cv_client.set_studio_inputs.call_args[1]["inputs"]
        assert studio_root_ids == [generate_id("ROOT_A"), generate_id("ROOT_B")]
        # Sub-container IDs must NOT be present.
        assert generate_id("ROOT_A/LEAF") not in studio_root_ids
        assert generate_id("ROOT_B/SPINE") not in studio_root_ids

    async def test_multiple_avd_configlets_deleted_in_batch(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that multiple stale AVD-managed configlets are deleted in a single batched delete_configlets call."""
        stale1_id, stale2_id, stale3_id = generate_id("STALE_1"), generate_id("STALE_2"), generate_id("STALE_3")
        root_id = generate_id("ROOT")

        existing_containers = [
            create_grpc_container(container_id=root_id, name="ROOT", description="Root", query="device:*"),
        ]
        existing_configlets = [
            Configlet(key=ConfigletKey(configlet_id=stale1_id), display_name="STALE_1"),
            Configlet(key=ConfigletKey(configlet_id=stale2_id), display_name="STALE_2"),
            Configlet(key=ConfigletKey(configlet_id=stale3_id), display_name="STALE_3"),
        ]
        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = existing_configlets
        mock_cv_client.get_studio_inputs_with_path.return_value = [root_id]

        # Manifest has the container but no configlets — all 3 stale configlets must be deleted.
        root = AvdContainer(name="ROOT", tag_query="device:*", description="Root")
        manifest = AvdManifest(configlets=(), containers=(root,))

        await deploy_static_config_studio_manifest_to_cv(manifest, deployment_result, mock_cv_client)

        # All 3 deletions must happen in ONE batched call.
        mock_cv_client.delete_configlets.assert_called_once()
        deleted_ids = mock_cv_client.delete_configlets.call_args[1]["configlet_ids"]
        assert set(deleted_ids) == {stale1_id, stale2_id, stale3_id}

        assert set(deployment_result.removed_static_config_configlets) == {"STALE_1", "STALE_2", "STALE_3"}

    async def test_studio_root_list_cleared_when_no_avd_roots_and_no_manual_entries(
        self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult
    ) -> None:
        """Test that set_studio_inputs is called with an empty list when all AVD roots are removed and no manual entries exist."""
        avd_root_id = generate_id("AVD_ROOT")

        existing_containers = [
            create_grpc_container(container_id=avd_root_id, name="AVD_ROOT", description="", query="device:*"),
        ]
        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = []
        # Studio root list contains only the AVD root — no manual entries to preserve.
        mock_cv_client.get_studio_inputs_with_path.return_value = [avd_root_id]

        # Manifest has only configlets, no containers — wipes the AVD root completely.
        configlet = AvdConfiglet(name="CFG", file=Path("cfg.cfg"))
        manifest = AvdManifest(configlets=(configlet,), containers=())

        await deploy_static_config_studio_manifest_to_cv(manifest, deployment_result, mock_cv_client)

        # Studio root list must be updated to empty — not short-circuited.
        mock_cv_client.set_studio_inputs.assert_called_once_with(
            studio_id="studio-static-configlet",
            workspace_id=deployment_result.workspace.id,
            input_path=["configletAssignmentRoots"],
            inputs=[],
        )

        # The AVD root container is also deleted.
        mock_cv_client.delete_configlet_container.assert_called_once_with(workspace_id=deployment_result.workspace.id, assignment_id=avd_root_id)

    async def test_configlets_only_manifest_wipes_existing_avd_containers(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that a configlets-only manifest deletes all existing AVD containers and clears them from the studio root list."""
        # Existing CV state has an AVD-managed container hierarchy plus one manual root.
        avd_root_id = generate_id("AVD_ROOT")
        avd_child_id = generate_id("AVD_ROOT/AVD_CHILD")
        manual_root_id = "manual-root-foo"

        existing_containers = [
            create_grpc_container(container_id=avd_root_id, name="AVD_ROOT", description="", query="device:*", child_ids=[avd_child_id]),
            create_grpc_container(container_id=avd_child_id, name="AVD_CHILD", description="", query="device:LEAF"),
            create_grpc_container(container_id=manual_root_id, name="MANUAL_ROOT", description="", query="device:*"),
        ]
        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = []
        mock_cv_client.get_studio_inputs_with_path.return_value = [avd_root_id, manual_root_id]

        # Manifest has only configlets, no containers.
        configlet = AvdConfiglet(name="STANDALONE", file=Path("standalone.cfg"))
        manifest = AvdManifest(configlets=(configlet,), containers=())

        await deploy_static_config_studio_manifest_to_cv(manifest, deployment_result, mock_cv_client)

        # The configlet was created.
        mock_cv_client.set_configlets_from_files.assert_called_once()

        # Both AVD containers are deleted, the manual root is preserved.
        assert mock_cv_client.delete_configlet_container.call_count == 2
        deleted_ids = {call.kwargs["assignment_id"] for call in mock_cv_client.delete_configlet_container.call_args_list}
        assert deleted_ids == {avd_root_id, avd_child_id}
        assert set(deployment_result.removed_static_config_containers) == {"AVD_ROOT", "AVD_CHILD"}

        # Studio root list is updated to remove the AVD root, keeping the manual root.
        mock_cv_client.set_studio_inputs.assert_called_once_with(
            studio_id="studio-static-configlet",
            workspace_id=deployment_result.workspace.id,
            input_path=["configletAssignmentRoots"],
            inputs=[manual_root_id],
        )

        # No containers were pushed (manifest declared none).
        mock_cv_client.set_configlet_containers.assert_not_called()

    async def test_container_moved_between_parents(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that moving a sub-container under a different parent treats it as new (path change generates a new ID)."""
        # Initial state: PARENT_A holds CHILD as a sub-container, PARENT_B does not exist.
        parent_a_id = generate_id("PARENT_A")
        old_child_id = generate_id("PARENT_A/CHILD")

        existing_containers = [
            create_grpc_container(container_id=parent_a_id, name="PARENT_A", description="", query="device:*", child_ids=[old_child_id]),
            create_grpc_container(container_id=old_child_id, name="CHILD", description="", query="device:LEAF"),
        ]
        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = []
        mock_cv_client.get_studio_inputs_with_path.return_value = [parent_a_id]

        # New manifest: CHILD moves from PARENT_A to a brand-new PARENT_B.
        child = AvdContainer(name="CHILD", tag_query="device:LEAF")
        parent_a = AvdContainer(name="PARENT_A", tag_query="device:*")
        parent_b = AvdContainer(name="PARENT_B", tag_query="device:*", sub_containers=(child,))
        manifest = AvdManifest(containers=(parent_a, parent_b))

        new_parent_b_id = generate_id("PARENT_B")
        new_child_id = generate_id("PARENT_B/CHILD")

        await deploy_static_config_studio_manifest_to_cv(manifest, deployment_result, mock_cv_client)

        # The old CHILD (under PARENT_A) is deleted because the new path produces a different ID.
        mock_cv_client.delete_configlet_container.assert_called_once_with(workspace_id=deployment_result.workspace.id, assignment_id=old_child_id)

        # PARENT_A is updated (lost its child), PARENT_B is new, CHILD is new at its new path.
        mock_cv_client.set_configlet_containers.assert_called_once()
        pushed = mock_cv_client.set_configlet_containers.call_args[1]["containers"]
        pushed_by_name = {c[1]: c for c in pushed}
        assert set(pushed_by_name.keys()) == {"PARENT_A", "PARENT_B", "CHILD"}
        # PARENT_A is pushed with empty child_ids.
        assert pushed_by_name["PARENT_A"][5] == []
        # PARENT_B holds the new path-based CHILD id.
        assert pushed_by_name["PARENT_B"][5] == [new_child_id]
        # The new CHILD has the new path-based id.
        assert pushed_by_name["CHILD"][0] == new_child_id

        # Studio root list is updated to include the new PARENT_B alongside PARENT_A.
        mock_cv_client.set_studio_inputs.assert_called_once_with(
            studio_id="studio-static-configlet",
            workspace_id=deployment_result.workspace.id,
            input_path=["configletAssignmentRoots"],
            inputs=[parent_a_id, new_parent_b_id],
        )

        assert deployment_result.removed_static_config_containers == ["CHILD"]

    async def test_fails_when_container_has_unmanaged_parent(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that the deploy fails when an in-manifest container has a parent assignment the manifest does not manage."""
        global_id = generate_id("GLOBAL")
        leafs_id = generate_id("GLOBAL/LEAFS")
        custom_parent_id = "custom-parent-001"

        existing_containers = [
            create_grpc_container(container_id=global_id, name="GLOBAL", description="", query="device:*", child_ids=[]),
            create_grpc_container(container_id=leafs_id, name="LEAFS", description="", query="device:LEAF"),
            create_grpc_container(container_id=custom_parent_id, name="MY_CUSTOM", description="", query="device:*", child_ids=[leafs_id]),
        ]
        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = []
        mock_cv_client.get_studio_inputs_with_path.return_value = [global_id]

        leafs = AvdContainer(name="LEAFS", tag_query="device:LEAF")
        global_c = AvdContainer(name="GLOBAL", tag_query="device:*", sub_containers=(leafs,))
        manifest = AvdManifest(containers=(global_c,))

        with pytest.raises(CVManifestError) as exc_info:
            await deploy_static_config_studio_manifest_to_cv(manifest, deployment_result, mock_cv_client)

        # Error message identifies both the offending parent and the child (name + id for each).
        assert "MY_CUSTOM" in str(exc_info.value)
        assert custom_parent_id in str(exc_info.value)
        assert "LEAFS" in str(exc_info.value)
        assert leafs_id in str(exc_info.value)

        # No updates on CV — workspace must be untouched.
        mock_cv_client.set_configlets_from_files.assert_not_called()
        mock_cv_client.set_configlet_containers.assert_not_called()
        mock_cv_client.set_studio_inputs.assert_not_called()
        mock_cv_client.delete_configlets.assert_not_called()
        mock_cv_client.delete_configlet_container.assert_not_called()

    async def test_fails_when_deleted_container_has_unmanaged_parent(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that the deploy fails when a manifest container scheduled for deletion has a parent assignment the manifest does not manage."""
        global_id = generate_id("GLOBAL")
        old_leafs_id = generate_id("OLD_LEAFS")  # Previously deployed by the manifest, absent from this run -> scheduled for delete.
        custom_parent_id = "custom-parent-002"

        existing_containers = [
            create_grpc_container(container_id=global_id, name="GLOBAL", description="", query="device:*"),
            create_grpc_container(container_id=old_leafs_id, name="OLD_LEAFS", description="", query="device:*"),
            create_grpc_container(container_id=custom_parent_id, name="MY_CUSTOM", description="", query="device:*", child_ids=[old_leafs_id]),
        ]
        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = []
        mock_cv_client.get_studio_inputs_with_path.return_value = [global_id]

        global_c = AvdContainer(name="GLOBAL", tag_query="device:*")
        manifest = AvdManifest(containers=(global_c,))

        with pytest.raises(CVManifestError) as exc_info:
            await deploy_static_config_studio_manifest_to_cv(manifest, deployment_result, mock_cv_client)

        assert "MY_CUSTOM" in str(exc_info.value)
        assert custom_parent_id in str(exc_info.value)
        assert "OLD_LEAFS" in str(exc_info.value)
        assert old_leafs_id in str(exc_info.value)

        mock_cv_client.set_configlets_from_files.assert_not_called()
        mock_cv_client.set_configlet_containers.assert_not_called()
        mock_cv_client.set_studio_inputs.assert_not_called()
        mock_cv_client.delete_configlets.assert_not_called()
        mock_cv_client.delete_configlet_container.assert_not_called()

    async def test_fails_when_unchanged_container_has_unmanaged_parent(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that the deploy fails when an unchanged in-manifest container has a parent assignment the manifest does not manage."""
        leafs_id = generate_id("LEAFS")
        custom_parent_id = "custom-parent-001"

        # Existing LEAFS body matches the manifest's LEAFS.
        existing_containers = [
            create_grpc_container(container_id=leafs_id, name="LEAFS", description="", query="device:LEAF"),
            create_grpc_container(container_id=custom_parent_id, name="MY_CUSTOM", description="", query="device:*", child_ids=[leafs_id]),
        ]
        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = []
        mock_cv_client.get_studio_inputs_with_path.return_value = []

        leafs = AvdContainer(name="LEAFS", tag_query="device:LEAF")
        manifest = AvdManifest(containers=(leafs,))

        with pytest.raises(CVManifestError) as exc_info:
            await deploy_static_config_studio_manifest_to_cv(manifest, deployment_result, mock_cv_client)

        assert "MY_CUSTOM" in str(exc_info.value)
        assert custom_parent_id in str(exc_info.value)
        assert "LEAFS" in str(exc_info.value)
        assert leafs_id in str(exc_info.value)

        # Validator ran before the push/skip decision: neither list was populated.
        assert deployment_result.skipped_static_config_containers == []
        assert deployment_result.deployed_static_config_containers == []

        mock_cv_client.set_configlets_from_files.assert_not_called()
        mock_cv_client.set_configlet_containers.assert_not_called()
        mock_cv_client.set_studio_inputs.assert_not_called()
        mock_cv_client.delete_configlets.assert_not_called()
        mock_cv_client.delete_configlet_container.assert_not_called()

    async def test_fails_when_root_container_has_unmanaged_parent(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that the deploy fails when a manifest top-level container has been manually placed under an unmanaged parent in CV."""
        root_id = generate_id("ROOT")
        custom_parent_id = "custom-parent-003"

        existing_containers = [
            create_grpc_container(container_id=root_id, name="ROOT", description="", query="device:*"),
            create_grpc_container(container_id=custom_parent_id, name="MY_CUSTOM", description="", query="device:*", child_ids=[root_id]),
        ]
        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = []
        # ROOT is currently NOT in the Studio root list — it was reparented under MY_CUSTOM.
        mock_cv_client.get_studio_inputs_with_path.return_value = [custom_parent_id]

        root = AvdContainer(name="ROOT", tag_query="device:*")
        manifest = AvdManifest(containers=(root,))

        with pytest.raises(CVManifestError) as exc_info:
            await deploy_static_config_studio_manifest_to_cv(manifest, deployment_result, mock_cv_client)

        # Error message identifies both the offending parent and the root container.
        assert "MY_CUSTOM" in str(exc_info.value)
        assert custom_parent_id in str(exc_info.value)
        assert "ROOT" in str(exc_info.value)
        assert root_id in str(exc_info.value)

        # No updates on CV — workspace must be untouched.
        mock_cv_client.set_configlets_from_files.assert_not_called()
        mock_cv_client.set_configlet_containers.assert_not_called()
        mock_cv_client.set_studio_inputs.assert_not_called()
        mock_cv_client.delete_configlets.assert_not_called()
        mock_cv_client.delete_configlet_container.assert_not_called()

    async def test_passes_when_container_has_stale_parent_that_is_in_manifest(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that a stale parent reference does not raise when the parent is in the manifest (it will be updated and self-heal)."""
        a_id = generate_id("GLOBAL_A")
        b_id = generate_id("GLOBAL_B")
        leafs_id = generate_id("GLOBAL_A/LEAFS")  # Manifest places LEAFS under GLOBAL_A.

        # Existing CV state: user manually moved LEAFS from GLOBAL_A's child list to GLOBAL_B's child list.
        existing_containers = [
            create_grpc_container(container_id=a_id, name="GLOBAL_A", description="", query="device:*", child_ids=[]),
            create_grpc_container(container_id=b_id, name="GLOBAL_B", description="", query="device:*", child_ids=[leafs_id]),
            create_grpc_container(container_id=leafs_id, name="LEAFS", description="", query="device:LEAF"),
        ]
        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = []
        mock_cv_client.get_studio_inputs_with_path.return_value = [a_id, b_id]

        leafs = AvdContainer(name="LEAFS", tag_query="device:LEAF")
        global_a = AvdContainer(name="GLOBAL_A", tag_query="device:*", sub_containers=(leafs,))
        global_b = AvdContainer(name="GLOBAL_B", tag_query="device:*")
        manifest = AvdManifest(containers=(global_a, global_b))

        # Must not raise — both parents are in the manifest, so the deploy reconciles the divergence on its own.
        await deploy_static_config_studio_manifest_to_cv(manifest, deployment_result, mock_cv_client)

        # GLOBAL_A and GLOBAL_B both get re-pushed: A regains LEAFS as child, B loses it.
        mock_cv_client.set_configlet_containers.assert_called_once()
        pushed = mock_cv_client.set_configlet_containers.call_args[1]["containers"]
        pushed_by_name = {c[1]: c for c in pushed}
        assert set(pushed_by_name.keys()) == {"GLOBAL_A", "GLOBAL_B"}
        assert pushed_by_name["GLOBAL_A"][5] == [leafs_id]
        assert pushed_by_name["GLOBAL_B"][5] == []

        # No deletions: every previously-deployed container is still in the manifest.
        mock_cv_client.delete_configlet_container.assert_not_called()

    async def test_passes_when_container_has_stale_parent_scheduled_for_deletion(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that a stale parent reference does not raise when the parent is itself scheduled for deletion by this deploy."""
        global_id = generate_id("GLOBAL")
        leafs_id = generate_id("GLOBAL/LEAFS")
        stale_manifest_parent_id = generate_id("STALE_MANIFEST_PARENT")  # Previously deployed by the manifest, absent from this run -> scheduled for deletion.

        # User manually moved LEAFS from GLOBAL to STALE_MANIFEST_PARENT. STALE_MANIFEST_PARENT is no longer in the manifest.
        existing_containers = [
            create_grpc_container(container_id=global_id, name="GLOBAL", description="", query="device:*", child_ids=[]),
            create_grpc_container(container_id=leafs_id, name="LEAFS", description="", query="device:LEAF"),
            create_grpc_container(container_id=stale_manifest_parent_id, name="STALE_MANIFEST_PARENT", description="", query="device:*", child_ids=[leafs_id]),
        ]
        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = []
        mock_cv_client.get_studio_inputs_with_path.return_value = [global_id, stale_manifest_parent_id]

        leafs = AvdContainer(name="LEAFS", tag_query="device:LEAF")
        global_c = AvdContainer(name="GLOBAL", tag_query="device:*", sub_containers=(leafs,))
        manifest = AvdManifest(containers=(global_c,))

        # Must not raise — STALE_MANIFEST_PARENT is in the list of managed containers (via containers to delete),
        # so its stale reference to LEAFS goes away with the parent when it's deleted.
        await deploy_static_config_studio_manifest_to_cv(manifest, deployment_result, mock_cv_client)

        # GLOBAL is rewritten to include LEAFS again.
        mock_cv_client.set_configlet_containers.assert_called_once()
        pushed = mock_cv_client.set_configlet_containers.call_args[1]["containers"]
        pushed_by_name = {c[1]: c for c in pushed}
        assert pushed_by_name["GLOBAL"][5] == [leafs_id]

        # STALE_MANIFEST_PARENT is deleted.
        mock_cv_client.delete_configlet_container.assert_called_once_with(workspace_id=deployment_result.workspace.id, assignment_id=stale_manifest_parent_id)
        assert deployment_result.removed_static_config_containers == ["STALE_MANIFEST_PARENT"]

    async def test_passes_when_managed_container_is_in_studio_root_list(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that a managed container with no parent assignment because it's in the Studio root list does not raise."""
        parent_id = generate_id("GLOBAL_PARENT")
        stray_id = generate_id("GLOBAL_PARENT/STRAY")

        # User manually moved STRAY out of GLOBAL_PARENT and into the Studio root list.
        existing_containers = [
            create_grpc_container(container_id=parent_id, name="GLOBAL_PARENT", description="", query="device:*", child_ids=[]),
            create_grpc_container(container_id=stray_id, name="STRAY", description="", query="device:STRAY"),
        ]
        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = []
        mock_cv_client.get_studio_inputs_with_path.return_value = [parent_id, stray_id]

        stray = AvdContainer(name="STRAY", tag_query="device:STRAY")
        global_parent = AvdContainer(name="GLOBAL_PARENT", tag_query="device:*", sub_containers=(stray,))
        manifest = AvdManifest(containers=(global_parent,))

        # Must not raise — STRAY has no parent assignment so no violation.
        await deploy_static_config_studio_manifest_to_cv(manifest, deployment_result, mock_cv_client)

        # GLOBAL_PARENT is rewritten to include STRAY again.
        mock_cv_client.set_configlet_containers.assert_called_once()
        pushed = mock_cv_client.set_configlet_containers.call_args[1]["containers"]
        pushed_by_name = {c[1]: c for c in pushed}
        assert pushed_by_name["GLOBAL_PARENT"][5] == [stray_id]

        # STRAY is removed from the Studio root list (it's a manifest-managed orphan root).
        mock_cv_client.set_studio_inputs.assert_called_once_with(
            studio_id="studio-static-configlet",
            workspace_id=deployment_result.workspace.id,
            input_path=["configletAssignmentRoots"],
            inputs=[parent_id],
        )

        # Nothing is deleted — STRAY is in the manifest, just being reparented.
        mock_cv_client.delete_configlet_container.assert_not_called()

    async def test_passes_when_orphaned_container_in_manifest_is_reparented(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that an orphan manifest container (no parent assignment, not in Studio root list) but in the manifest does not raise and gets reparented."""
        parent_id = generate_id("GLOBAL_PARENT")
        child_id = generate_id("GLOBAL_PARENT/CHILD")

        # CHILD exists in CV but is fully orphaned: no parent references it and it's not in the Studio root list.
        existing_containers = [
            create_grpc_container(container_id=parent_id, name="GLOBAL_PARENT", description="", query="device:*", child_ids=[]),
            create_grpc_container(container_id=child_id, name="CHILD", description="", query="device:CHILD"),
        ]
        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = []
        mock_cv_client.get_studio_inputs_with_path.return_value = [parent_id]  # CHILD intentionally NOT here.

        child = AvdContainer(name="CHILD", tag_query="device:CHILD")
        global_parent = AvdContainer(name="GLOBAL_PARENT", tag_query="device:*", sub_containers=(child,))
        manifest = AvdManifest(containers=(global_parent,))

        # Must not raise — CHILD has no parent (parent is None in the validator) so the check skips it.
        await deploy_static_config_studio_manifest_to_cv(manifest, deployment_result, mock_cv_client)

        # GLOBAL_PARENT is rewritten to include CHILD; CHILD itself matches its manifest spec so it's not re-pushed.
        mock_cv_client.set_configlet_containers.assert_called_once()
        pushed = mock_cv_client.set_configlet_containers.call_args[1]["containers"]
        pushed_by_name = {c[1]: c for c in pushed}
        assert "GLOBAL_PARENT" in pushed_by_name
        assert pushed_by_name["GLOBAL_PARENT"][5] == [child_id]
        assert "CHILD" not in pushed_by_name

        # Nothing is deleted — CHILD is in the manifest, just being reparented.
        mock_cv_client.delete_configlet_container.assert_not_called()

    async def test_root_container_demoted_to_sub_container(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that demoting a root container to a sub-container deletes the old root and creates the nested one."""
        # Initial state: SOLO is a root container.
        old_solo_id = generate_id("SOLO")

        existing_containers = [
            create_grpc_container(container_id=old_solo_id, name="SOLO", description="", query="device:*"),
        ]
        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = []
        mock_cv_client.get_studio_inputs_with_path.return_value = [old_solo_id]

        # New manifest: SOLO is now nested under GROUP.
        solo = AvdContainer(name="SOLO", tag_query="device:*")
        group = AvdContainer(name="GROUP", tag_query="device:*", sub_containers=(solo,))
        manifest = AvdManifest(containers=(group,))

        new_group_id = generate_id("GROUP")
        new_solo_id = generate_id("GROUP/SOLO")

        await deploy_static_config_studio_manifest_to_cv(manifest, deployment_result, mock_cv_client)

        # Old root SOLO is deleted (path change generated a different ID).
        mock_cv_client.delete_configlet_container.assert_called_once_with(workspace_id=deployment_result.workspace.id, assignment_id=old_solo_id)

        # GROUP and the new nested SOLO are pushed.
        mock_cv_client.set_configlet_containers.assert_called_once()
        pushed_ids = {c[0] for c in mock_cv_client.set_configlet_containers.call_args[1]["containers"]}
        assert pushed_ids == {new_group_id, new_solo_id}

        # Studio root list is replaced: old SOLO removed, new GROUP added.
        mock_cv_client.set_studio_inputs.assert_called_once_with(
            studio_id="studio-static-configlet",
            workspace_id=deployment_result.workspace.id,
            input_path=["configletAssignmentRoots"],
            inputs=[new_group_id],
        )

        assert deployment_result.removed_static_config_containers == ["SOLO"]

    async def test_fails_when_deleted_configlet_is_held_by_unmanaged_container(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that the deploy fails when a manifest configlet scheduled for deletion is still assigned to a container the manifest does not manage."""
        manifest_root_id = generate_id("MANIFEST_ROOT")
        stale_cfg_id = generate_id("STALE_CFG")
        manual_holder_id = "manual-holder-001"

        existing_containers = [
            create_grpc_container(container_id=manifest_root_id, name="MANIFEST_ROOT", description="", query="device:*"),
            create_grpc_container(container_id=manual_holder_id, name="MY_CUSTOM", description="", query="device:*", configlet_ids=[stale_cfg_id]),
        ]
        existing_configlets = [
            Configlet(key=ConfigletKey(configlet_id=stale_cfg_id), display_name="STALE_CFG"),
        ]
        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = existing_configlets
        mock_cv_client.get_studio_inputs_with_path.return_value = [manifest_root_id, manual_holder_id]

        # Manifest declares only the root container, no configlets — STALE_CFG is scheduled for deletion.
        manifest_root = AvdContainer(name="MANIFEST_ROOT", tag_query="device:*")
        manifest = AvdManifest(containers=(manifest_root,))

        with pytest.raises(CVManifestError) as exc_info:
            await deploy_static_config_studio_manifest_to_cv(manifest, deployment_result, mock_cv_client)

        # Error message identifies both the offending holder and the configlet (name + id for each).
        assert "MY_CUSTOM" in str(exc_info.value)
        assert manual_holder_id in str(exc_info.value)
        assert "STALE_CFG" in str(exc_info.value)
        assert stale_cfg_id in str(exc_info.value)

        # No updates on CV — workspace must be untouched.
        mock_cv_client.set_configlets_from_files.assert_not_called()
        mock_cv_client.set_configlet_containers.assert_not_called()
        mock_cv_client.set_studio_inputs.assert_not_called()
        mock_cv_client.delete_configlets.assert_not_called()
        mock_cv_client.delete_configlet_container.assert_not_called()

    async def test_passes_when_deleted_configlet_holder_is_also_scheduled_for_deletion(
        self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult
    ) -> None:
        """Test that no violation is raised when both the deleted manifest configlet and its holder are scheduled for deletion by this deploy."""
        manifest_root_id = generate_id("MANIFEST_ROOT")
        stale_cfg_id = generate_id("STALE_CFG")
        # Manifest-managed holder absent from this manifest is scheduled for deletion, so its reference to STALE_CFG disappears when the holder is deleted.
        stale_holder_id = generate_id("STALE_HOLDER")

        existing_containers = [
            create_grpc_container(container_id=manifest_root_id, name="MANIFEST_ROOT", description="", query="device:*"),
            create_grpc_container(container_id=stale_holder_id, name="STALE_HOLDER", description="", query="device:*", configlet_ids=[stale_cfg_id]),
        ]
        existing_configlets = [
            Configlet(key=ConfigletKey(configlet_id=stale_cfg_id), display_name="STALE_CFG"),
        ]
        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = existing_configlets
        mock_cv_client.get_studio_inputs_with_path.return_value = [manifest_root_id, stale_holder_id]

        # Manifest declares only MANIFEST_ROOT — STALE_HOLDER and STALE_CFG are both scheduled for deletion.
        manifest_root = AvdContainer(name="MANIFEST_ROOT", tag_query="device:*")
        manifest = AvdManifest(containers=(manifest_root,))

        # Must not raise — STALE_HOLDER is managed (being deleted), so its stale reference goes away with it.
        await deploy_static_config_studio_manifest_to_cv(manifest, deployment_result, mock_cv_client)

        # Both the configlet and the holder are deleted in the same deploy.
        mock_cv_client.delete_configlets.assert_called_once_with(workspace_id=deployment_result.workspace.id, configlet_ids=[stale_cfg_id])
        deleted_container_ids = {call.kwargs["assignment_id"] for call in mock_cv_client.delete_configlet_container.call_args_list}
        assert stale_holder_id in deleted_container_ids

    async def test_passes_when_deleted_configlet_is_only_held_by_managed_containers(
        self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult
    ) -> None:
        """Test that a deleted manifest configlet held only by managed containers does not raise (the holders are themselves being rewritten or deleted)."""
        root_id = generate_id("ROOT")
        stale_cfg_id = generate_id("STALE_CFG")

        # ROOT currently references STALE_CFG. Manifest will drop STALE_CFG from ROOT's configlets and from the manifest.
        existing_containers = [
            create_grpc_container(container_id=root_id, name="ROOT", description="Root", query="device:*", configlet_ids=[stale_cfg_id]),
        ]
        existing_configlets = [
            Configlet(key=ConfigletKey(configlet_id=stale_cfg_id), display_name="STALE_CFG"),
        ]
        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = existing_configlets
        mock_cv_client.get_studio_inputs_with_path.return_value = [root_id]

        # Manifest redeclares ROOT but without STALE_CFG, and drops STALE_CFG entirely.
        root = AvdContainer(name="ROOT", tag_query="device:*", description="Root")
        manifest = AvdManifest(containers=(root,))

        # Must not raise — ROOT is being rewritten, so the stale reference disappears.
        await deploy_static_config_studio_manifest_to_cv(manifest, deployment_result, mock_cv_client)

        # ROOT is re-pushed without STALE_CFG.
        mock_cv_client.set_configlet_containers.assert_called_once()
        pushed = mock_cv_client.set_configlet_containers.call_args[1]["containers"]
        assert pushed[0][3] == []

        # STALE_CFG is deleted.
        mock_cv_client.delete_configlets.assert_called_once_with(workspace_id=deployment_result.workspace.id, configlet_ids=[stale_cfg_id])
        assert deployment_result.removed_static_config_configlets == ["STALE_CFG"]

    async def test_passes_when_deleted_configlet_has_no_holders(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that an orphan manifest configlet (not referenced by any container) is deleted cleanly without raising."""
        root_id = generate_id("ROOT")
        orphan_cfg_id = generate_id("ORPHAN_CFG")

        existing_containers = [
            create_grpc_container(container_id=root_id, name="ROOT", description="Root", query="device:*"),
        ]
        existing_configlets = [
            Configlet(key=ConfigletKey(configlet_id=orphan_cfg_id), display_name="ORPHAN_CFG"),
        ]
        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = existing_configlets
        mock_cv_client.get_studio_inputs_with_path.return_value = [root_id]

        root = AvdContainer(name="ROOT", tag_query="device:*", description="Root")
        manifest = AvdManifest(containers=(root,))

        await deploy_static_config_studio_manifest_to_cv(manifest, deployment_result, mock_cv_client)

        # Orphan configlet is deleted, no violation.
        mock_cv_client.delete_configlets.assert_called_once_with(workspace_id=deployment_result.workspace.id, configlet_ids=[orphan_cfg_id])
        assert deployment_result.removed_static_config_configlets == ["ORPHAN_CFG"]

    async def test_fails_lists_multiple_holders_for_single_configlet(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that a single deleted manifest configlet referenced by multiple unmanaged holders produces one violation entry per holder."""
        manifest_root_id = generate_id("MANIFEST_ROOT")
        stale_cfg_id = generate_id("STALE_CFG")
        holder_a_id = "manual-holder-a"
        holder_b_id = "manual-holder-b"

        existing_containers = [
            create_grpc_container(container_id=manifest_root_id, name="MANIFEST_ROOT", description="", query="device:*"),
            create_grpc_container(container_id=holder_a_id, name="HOLDER_A", description="", query="device:*", configlet_ids=[stale_cfg_id]),
            create_grpc_container(container_id=holder_b_id, name="HOLDER_B", description="", query="device:*", configlet_ids=[stale_cfg_id]),
        ]
        existing_configlets = [
            Configlet(key=ConfigletKey(configlet_id=stale_cfg_id), display_name="STALE_CFG"),
        ]
        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = existing_configlets
        mock_cv_client.get_studio_inputs_with_path.return_value = [manifest_root_id, holder_a_id, holder_b_id]

        manifest_root = AvdContainer(name="MANIFEST_ROOT", tag_query="device:*")
        manifest = AvdManifest(containers=(manifest_root,))

        with pytest.raises(CVManifestError) as exc_info:
            await deploy_static_config_studio_manifest_to_cv(manifest, deployment_result, mock_cv_client)

        # Both holders appear in the message.
        msg = str(exc_info.value)
        assert "HOLDER_A" in msg
        assert "HOLDER_B" in msg
        assert holder_a_id in msg
        assert holder_b_id in msg
        # The configlet is named once per holder.
        assert msg.count("STALE_CFG") == 2

    async def test_orphan_unmanaged_subtree_deleted_when_managed_parent_updates(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that a multi-level unmanaged sub-tree is fully removed when its managed parent drops the top of the chain."""
        managed_parent_id = generate_id("PARENT")
        unmanaged_mid_id = "manual-mid-123"
        unmanaged_leaf_id = "manual-leaf-456"

        existing_containers = [
            # Managed parent currently owns an unmanaged sub-tree mid -> leaf.
            create_grpc_container(container_id=managed_parent_id, name="PARENT", description="Parent", query="device:*", child_ids=[unmanaged_mid_id]),
            create_grpc_container(container_id=unmanaged_mid_id, name="UNMANAGED_MID", description="", query="device:*", child_ids=[unmanaged_leaf_id]),
            create_grpc_container(container_id=unmanaged_leaf_id, name="UNMANAGED_LEAF", description="", query="device:LEAF"),
        ]
        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = []
        mock_cv_client.get_studio_inputs_with_path.return_value = [managed_parent_id]

        # Manifest declares the managed parent with no children.
        managed_parent = AvdContainer(name="PARENT", tag_query="device:*", description="Parent")
        manifest = AvdManifest(containers=(managed_parent,))

        await deploy_static_config_studio_manifest_to_cv(manifest, deployment_result, mock_cv_client)

        # Both unmanaged descendants are orphan-deleted.
        assert mock_cv_client.delete_configlet_container.call_count == 2
        deleted_ids = {call.kwargs["assignment_id"] for call in mock_cv_client.delete_configlet_container.call_args_list}
        assert deleted_ids == {unmanaged_mid_id, unmanaged_leaf_id}
        assert set(deployment_result.removed_static_config_containers) == {"UNMANAGED_MID", "UNMANAGED_LEAF"}

    async def test_managed_container_reparented_by_manifest_is_not_orphan_deleted(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that a managed container reachable through an orphan path is reparented by the manifest instead of being deleted."""
        managed_parent_id = generate_id("PARENT")
        unmanaged_mid_id = "manual-mid-789"
        managed_grand_id = generate_id("PARENT/MANAGED_GRAND")  # In the manifest as a child of PARENT.

        # Existing layout: PARENT -> UNMANAGED_MID -> MANAGED_GRAND. Manifest wants PARENT -> MANAGED_GRAND directly.
        existing_containers = [
            create_grpc_container(container_id=managed_parent_id, name="PARENT", description="Parent", query="device:*", child_ids=[unmanaged_mid_id]),
            create_grpc_container(container_id=unmanaged_mid_id, name="UNMANAGED_MID", description="", query="device:*", child_ids=[managed_grand_id]),
            create_grpc_container(container_id=managed_grand_id, name="MANAGED_GRAND", description="", query="device:LEAF"),
        ]
        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = []
        mock_cv_client.get_studio_inputs_with_path.return_value = [managed_parent_id]

        managed_grand = AvdContainer(name="MANAGED_GRAND", tag_query="device:LEAF")
        managed_parent = AvdContainer(name="PARENT", tag_query="device:*", description="Parent", sub_containers=(managed_grand,))
        manifest = AvdManifest(containers=(managed_parent,))

        # Must not raise even though MANAGED_GRAND currently has an unmanaged parent that is about to be orphan-deleted.
        await deploy_static_config_studio_manifest_to_cv(manifest, deployment_result, mock_cv_client)

        # Only UNMANAGED_MID is deleted. MANAGED_GRAND is reparented by the manifest, not deleted.
        mock_cv_client.delete_configlet_container.assert_called_once_with(workspace_id=deployment_result.workspace.id, assignment_id=unmanaged_mid_id)
        assert deployment_result.removed_static_config_containers == ["UNMANAGED_MID"]

        # PARENT was updated to point directly at MANAGED_GRAND.
        mock_cv_client.set_configlet_containers.assert_called_once()
        pushed = mock_cv_client.set_configlet_containers.call_args[1]["containers"]
        parent_push = next(c for c in pushed if c[1] == "PARENT")
        assert parent_push[5] == [managed_grand_id]

    async def test_subtree_under_deleted_managed_container_is_fully_removed(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that an entire unmanaged sub-tree hanging off a removed managed container is deleted together with the parent."""
        stale_managed_root_id = generate_id("STALE_ROOT")  # Managed, NOT in this manifest -> deleted.
        unmanaged_mid_id = "manual-mid-abc"
        unmanaged_leaf_id = "manual-leaf-def"
        new_root_id = generate_id("NEW_ROOT")

        existing_containers = [
            create_grpc_container(container_id=stale_managed_root_id, name="STALE_ROOT", description="", query="device:*", child_ids=[unmanaged_mid_id]),
            create_grpc_container(container_id=unmanaged_mid_id, name="UNMANAGED_MID", description="", query="device:*", child_ids=[unmanaged_leaf_id]),
            create_grpc_container(container_id=unmanaged_leaf_id, name="UNMANAGED_LEAF", description="", query="device:LEAF"),
        ]
        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = []
        mock_cv_client.get_studio_inputs_with_path.return_value = [stale_managed_root_id]

        new_root = AvdContainer(name="NEW_ROOT", tag_query="device:*")
        manifest = AvdManifest(containers=(new_root,))

        await deploy_static_config_studio_manifest_to_cv(manifest, deployment_result, mock_cv_client)

        # All three (STALE_ROOT, UNMANAGED_MID, UNMANAGED_LEAF) are deleted in one go.
        assert mock_cv_client.delete_configlet_container.call_count == 3
        deleted_ids = {call.kwargs["assignment_id"] for call in mock_cv_client.delete_configlet_container.call_args_list}
        assert deleted_ids == {stale_managed_root_id, unmanaged_mid_id, unmanaged_leaf_id}
        assert set(deployment_result.removed_static_config_containers) == {"STALE_ROOT", "UNMANAGED_MID", "UNMANAGED_LEAF"}

        # The new root container is pushed.
        mock_cv_client.set_configlet_containers.assert_called_once()
        pushed = mock_cv_client.set_configlet_containers.call_args[1]["containers"]
        assert {c[0] for c in pushed} == {new_root_id}

    async def test_deep_unmanaged_chain_is_fully_removed(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that every container of a long unmanaged chain below a managed parent is removed when the parent drops it."""
        managed_parent_id = generate_id("PARENT")
        m2, m3, m4, m5 = "manual-2", "manual-3", "manual-4", "manual-5"

        existing_containers = [
            create_grpc_container(container_id=managed_parent_id, name="PARENT", description="Parent", query="device:*", child_ids=[m2]),
            create_grpc_container(container_id=m2, name="M2", description="", query="device:*", child_ids=[m3]),
            create_grpc_container(container_id=m3, name="M3", description="", query="device:*", child_ids=[m4]),
            create_grpc_container(container_id=m4, name="M4", description="", query="device:*", child_ids=[m5]),
            create_grpc_container(container_id=m5, name="M5", description="", query="device:*"),
        ]
        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = []
        mock_cv_client.get_studio_inputs_with_path.return_value = [managed_parent_id]

        managed_parent = AvdContainer(name="PARENT", tag_query="device:*", description="Parent")
        manifest = AvdManifest(containers=(managed_parent,))

        await deploy_static_config_studio_manifest_to_cv(manifest, deployment_result, mock_cv_client)

        deleted_ids = {call.kwargs["assignment_id"] for call in mock_cv_client.delete_configlet_container.call_args_list}
        assert deleted_ids == {m2, m3, m4, m5}
        assert set(deployment_result.removed_static_config_containers) == {"M2", "M3", "M4", "M5"}

    async def test_managed_parent_dropping_mixed_children_removes_both(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that when a managed parent drops both a managed and an unmanaged child at once, both are removed."""
        managed_parent_id = generate_id("PARENT")
        dropped_managed_child_id = generate_id("PARENT/DROPPED_CHILD")
        dropped_unmanaged_child_id = "manual-dropped-child"

        existing_containers = [
            # Managed parent currently owns one managed child and one unmanaged child; the manifest drops both.
            create_grpc_container(
                container_id=managed_parent_id,
                name="PARENT",
                description="Parent",
                query="device:*",
                child_ids=[dropped_managed_child_id, dropped_unmanaged_child_id],
            ),
            create_grpc_container(container_id=dropped_managed_child_id, name="DROPPED_CHILD", description="", query="device:LEAF"),
            create_grpc_container(container_id=dropped_unmanaged_child_id, name="UNMANAGED_DROPPED", description="", query="device:LEAF"),
        ]
        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = []
        mock_cv_client.get_studio_inputs_with_path.return_value = [managed_parent_id]

        # Manifest declares only the parent with no children.
        managed_parent = AvdContainer(name="PARENT", tag_query="device:*", description="Parent")
        manifest = AvdManifest(containers=(managed_parent,))

        await deploy_static_config_studio_manifest_to_cv(manifest, deployment_result, mock_cv_client)

        # Both children are removed (each via its own removal path) and the parent is updated to have no children.
        assert mock_cv_client.delete_configlet_container.call_count == 2
        deleted_ids = {call.kwargs["assignment_id"] for call in mock_cv_client.delete_configlet_container.call_args_list}
        assert deleted_ids == {dropped_managed_child_id, dropped_unmanaged_child_id}
        assert set(deployment_result.removed_static_config_containers) == {"DROPPED_CHILD", "UNMANAGED_DROPPED"}

        mock_cv_client.set_configlet_containers.assert_called_once()
        pushed = mock_cv_client.set_configlet_containers.call_args[1]["containers"]
        parent_push = next(c for c in pushed if c[1] == "PARENT")
        assert parent_push[5] == []

    async def test_deleted_managed_container_with_mixed_children_is_fully_removed(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that a removed managed container together with its managed and unmanaged children are all deleted in one deploy."""
        stale_managed_root_id = generate_id("STALE_ROOT")  # Managed, NOT in this manifest -> deleted.
        stale_managed_child_id = generate_id("STALE_ROOT/MANAGED_CHILD")  # Managed and a child of the deleted root.
        unmanaged_child_id = "manual-child-xyz"
        new_root_id = generate_id("NEW_ROOT")

        existing_containers = [
            create_grpc_container(
                container_id=stale_managed_root_id,
                name="STALE_ROOT",
                description="",
                query="device:*",
                child_ids=[stale_managed_child_id, unmanaged_child_id],
            ),
            create_grpc_container(container_id=stale_managed_child_id, name="MANAGED_CHILD", description="", query="device:LEAF"),
            create_grpc_container(container_id=unmanaged_child_id, name="UNMANAGED_CHILD", description="", query="device:LEAF"),
        ]
        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = []
        mock_cv_client.get_studio_inputs_with_path.return_value = [stale_managed_root_id]

        new_root = AvdContainer(name="NEW_ROOT", tag_query="device:*")
        manifest = AvdManifest(containers=(new_root,))

        await deploy_static_config_studio_manifest_to_cv(manifest, deployment_result, mock_cv_client)

        # The deleted root and both of its children are removed in one deploy.
        assert mock_cv_client.delete_configlet_container.call_count == 3
        deleted_ids = {call.kwargs["assignment_id"] for call in mock_cv_client.delete_configlet_container.call_args_list}
        assert deleted_ids == {stale_managed_root_id, stale_managed_child_id, unmanaged_child_id}
        assert set(deployment_result.removed_static_config_containers) == {"STALE_ROOT", "MANAGED_CHILD", "UNMANAGED_CHILD"}

        # The new root container is pushed.
        mock_cv_client.set_configlet_containers.assert_called_once()
        pushed = mock_cv_client.set_configlet_containers.call_args[1]["containers"]
        assert {c[0] for c in pushed} == {new_root_id}

    async def test_deleted_configlet_with_only_orphan_holder_does_not_raise(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that removing a configlet still referenced only by a container scheduled for orphan deletion succeeds without raising."""
        managed_parent_id = generate_id("PARENT")
        unmanaged_holder_id = "manual-holder-xyz"
        stale_cfg_id = generate_id("STALE_CFG")

        existing_containers = [
            # Managed parent currently owns an unmanaged sub-container that holds the manifest configlet.
            create_grpc_container(container_id=managed_parent_id, name="PARENT", description="Parent", query="device:*", child_ids=[unmanaged_holder_id]),
            create_grpc_container(container_id=unmanaged_holder_id, name="UNMANAGED_HOLDER", description="", query="device:*", configlet_ids=[stale_cfg_id]),
        ]
        existing_configlets = [
            Configlet(key=ConfigletKey(configlet_id=stale_cfg_id), display_name="STALE_CFG"),
        ]
        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = existing_configlets
        mock_cv_client.get_studio_inputs_with_path.return_value = [managed_parent_id]

        # Manifest drops the unmanaged holder (PARENT updated with no children) and the configlet.
        managed_parent = AvdContainer(name="PARENT", tag_query="device:*", description="Parent")
        manifest = AvdManifest(configlets=(), containers=(managed_parent,))

        # Must not raise -- UNMANAGED_HOLDER is about to be orphan-deleted, taking its stale STALE_CFG reference with it.
        await deploy_static_config_studio_manifest_to_cv(manifest, deployment_result, mock_cv_client)

        # The configlet and its orphan holder are both deleted.
        mock_cv_client.delete_configlets.assert_called_once_with(workspace_id=deployment_result.workspace.id, configlet_ids=[stale_cfg_id])
        mock_cv_client.delete_configlet_container.assert_called_once_with(workspace_id=deployment_result.workspace.id, assignment_id=unmanaged_holder_id)
        assert deployment_result.removed_static_config_configlets == ["STALE_CFG"]
        assert deployment_result.removed_static_config_containers == ["UNMANAGED_HOLDER"]

    async def test_chained_managed_deletion_pulls_unmanaged_leaf(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that an unmanaged leaf two levels below a deleted managed root is removed when its managed mid-parent is also deleted."""
        stale_managed_root_id = generate_id("STALE_ROOT")  # Managed, NOT in this manifest -> deleted.
        stale_managed_mid_id = generate_id("STALE_MID")  # Managed, NOT in this manifest -> deleted as a child of STALE_ROOT.
        unmanaged_leaf_id = "manual-leaf-xyz"
        new_root_id = generate_id("NEW_ROOT")

        existing_containers = [
            # Chain: STALE_ROOT -> STALE_MID -> UNMANAGED_LEAF. The unmanaged leaf is only reachable by traversing through the managed mid-parent.
            create_grpc_container(container_id=stale_managed_root_id, name="STALE_ROOT", description="", query="device:*", child_ids=[stale_managed_mid_id]),
            create_grpc_container(container_id=stale_managed_mid_id, name="STALE_MID", description="", query="device:*", child_ids=[unmanaged_leaf_id]),
            create_grpc_container(container_id=unmanaged_leaf_id, name="UNMANAGED_LEAF", description="", query="device:LEAF"),
        ]
        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = []
        mock_cv_client.get_studio_inputs_with_path.return_value = [stale_managed_root_id]

        # Manifest replaces the entire chain with a brand-new root.
        new_root = AvdContainer(name="NEW_ROOT", tag_query="device:*")
        manifest = AvdManifest(containers=(new_root,))

        await deploy_static_config_studio_manifest_to_cv(manifest, deployment_result, mock_cv_client)

        # All three (STALE_ROOT, STALE_MID, UNMANAGED_LEAF) are deleted in one go,
        # the subtree walk traverses through the managed mid-parent to reach the unmanaged leaf.
        assert mock_cv_client.delete_configlet_container.call_count == 3
        deleted_ids = {call.kwargs["assignment_id"] for call in mock_cv_client.delete_configlet_container.call_args_list}
        assert deleted_ids == {stale_managed_root_id, stale_managed_mid_id, unmanaged_leaf_id}
        assert set(deployment_result.removed_static_config_containers) == {"STALE_ROOT", "STALE_MID", "UNMANAGED_LEAF"}

        # The new root container is pushed.
        mock_cv_client.set_configlet_containers.assert_called_once()
        pushed = mock_cv_client.set_configlet_containers.call_args[1]["containers"]
        assert {c[0] for c in pushed} == {new_root_id}

        # Studio root list is updated to replace the stale root with the new root.
        mock_cv_client.set_studio_inputs.assert_called_once_with(
            studio_id="studio-static-configlet",
            workspace_id=deployment_result.workspace.id,
            input_path=["configletAssignmentRoots"],
            inputs=[new_root_id],
        )

    async def test_preserve_existing_sub_containers_keeps_manifest_managed_sibling(
        self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult
    ) -> None:
        """Test that a partial manifest can preserve an existing manifest-managed sibling under a shared parent."""
        sites_id = generate_id("SITES")
        site1_id = generate_id("SITES/SITE1")
        site2_id = generate_id("SITES/SITE2")

        existing_containers = [
            create_grpc_container(container_id=sites_id, name="SITES", description="", query="device:*", child_ids=[site1_id, site2_id]),
            create_grpc_container(container_id=site1_id, name="SITE1", description="", query="site:1"),
            create_grpc_container(container_id=site2_id, name="SITE2", description="", query="site:2"),
        ]
        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = []
        mock_cv_client.get_studio_inputs_with_path.return_value = [sites_id]

        site1 = AvdContainer(name="SITE1", tag_query="site:1")
        sites = AvdContainer(name="SITES", tag_query="device:*", sub_containers=(site1,), preserve_existing_sub_containers=True)
        manifest = AvdManifest(containers=(sites,))

        await deploy_static_config_studio_manifest_to_cv(manifest, deployment_result, mock_cv_client)

        mock_cv_client.set_configlet_containers.assert_not_called()
        mock_cv_client.delete_configlet_container.assert_not_called()
        assert not deployment_result.removed_static_config_containers

    async def test_preserve_existing_sub_containers_keeps_manual_sibling(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that a preserved manual sibling is not deleted or removed from the parent child list."""
        sites_id = generate_id("SITES")
        site1_id = generate_id("SITES/SITE1")
        manual_site_id = "manual-site-2"

        existing_containers = [
            create_grpc_container(container_id=sites_id, name="SITES", description="", query="device:*", child_ids=[site1_id, manual_site_id]),
            create_grpc_container(container_id=site1_id, name="SITE1", description="", query="site:1"),
            create_grpc_container(container_id=manual_site_id, name="SITE2", description="", query="site:2"),
        ]
        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = []
        mock_cv_client.get_studio_inputs_with_path.return_value = [sites_id]

        site1 = AvdContainer(name="SITE1", tag_query="site:1")
        sites = AvdContainer(name="SITES", tag_query="device:*", sub_containers=(site1,), preserve_existing_sub_containers=True)
        manifest = AvdManifest(containers=(sites,))

        await deploy_static_config_studio_manifest_to_cv(manifest, deployment_result, mock_cv_client)

        mock_cv_client.set_configlet_containers.assert_not_called()
        mock_cv_client.delete_configlet_container.assert_not_called()
        assert not deployment_result.removed_static_config_containers

    async def test_preserve_existing_sub_containers_pushes_effective_child_list(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that a parent update keeps preserved existing children in the pushed child list."""
        sites_id = generate_id("SITES")
        site1_id = generate_id("SITES/SITE1")
        site2_id = generate_id("SITES/SITE2")

        existing_containers = [
            create_grpc_container(container_id=sites_id, name="SITES", description="", query="device:*", child_ids=[site2_id]),
            create_grpc_container(container_id=site2_id, name="SITE2", description="", query="site:2"),
        ]
        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = []
        mock_cv_client.get_studio_inputs_with_path.return_value = [sites_id]

        site1 = AvdContainer(name="SITE1", tag_query="site:1")
        sites = AvdContainer(name="SITES", tag_query="device:*", sub_containers=(site1,), preserve_existing_sub_containers=True)
        manifest = AvdManifest(containers=(sites,))

        await deploy_static_config_studio_manifest_to_cv(manifest, deployment_result, mock_cv_client)

        mock_cv_client.set_configlet_containers.assert_called_once()
        pushed = mock_cv_client.set_configlet_containers.call_args[1]["containers"]
        pushed_by_name = {container[1]: container for container in pushed}
        assert set(pushed_by_name) == {"SITES", "SITE1"}
        assert pushed_by_name["SITES"][5] == [site2_id, site1_id]
        mock_cv_client.delete_configlet_container.assert_not_called()

    async def test_deleted_configlet_held_by_preserved_container_raises(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that preserved holders still block deletion of manifest-managed configlets."""
        sites_id = generate_id("SITES")
        site1_id = generate_id("SITES/SITE1")
        site2_id = generate_id("SITES/SITE2")
        stale_cfg_id = generate_id("STALE_CFG")

        existing_containers = [
            create_grpc_container(container_id=sites_id, name="SITES", description="", query="device:*", child_ids=[site1_id, site2_id]),
            create_grpc_container(container_id=site1_id, name="SITE1", description="", query="site:1"),
            create_grpc_container(container_id=site2_id, name="SITE2", description="", query="site:2", configlet_ids=[stale_cfg_id]),
        ]
        existing_configlets = [
            Configlet(key=ConfigletKey(configlet_id=stale_cfg_id), display_name="STALE_CFG"),
        ]
        mock_cv_client.get_configlet_containers.return_value = existing_containers
        mock_cv_client.get_configlets.return_value = existing_configlets
        mock_cv_client.get_studio_inputs_with_path.return_value = [sites_id]

        site1 = AvdContainer(name="SITE1", tag_query="site:1")
        sites = AvdContainer(name="SITES", tag_query="device:*", sub_containers=(site1,), preserve_existing_sub_containers=True)
        manifest = AvdManifest(containers=(sites,))

        with pytest.raises(CVManifestError) as exc_info:
            await deploy_static_config_studio_manifest_to_cv(manifest, deployment_result, mock_cv_client)

        assert "SITE2" in str(exc_info.value)
        assert site2_id in str(exc_info.value)
        assert "STALE_CFG" in str(exc_info.value)
        assert stale_cfg_id in str(exc_info.value)
        mock_cv_client.delete_configlets.assert_not_called()
        mock_cv_client.delete_configlet_container.assert_not_called()
