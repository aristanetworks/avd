# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from unittest.mock import AsyncMock, MagicMock

import pytest

from pyavd._cv.api.arista.configlet.v1 import Configlet, ConfigletKey
from pyavd._cv.workflows.deploy_static_config_studio_manifest_to_cv import deploy_static_config_studio_manifest_to_cv
from pyavd._cv.workflows.models import AvdConfiglet, AvdContainer, AvdManifest, CVWorkspace, DeployToCvResult

from .helpers import create_grpc_container, generate_id

# === Test Fixtures ===


@pytest.fixture
def mock_cv_client() -> MagicMock:
    """Fixture to provide a mocked CVClient instance with AsyncMocks."""
    client = MagicMock()
    # Patch all required async methods with AsyncMock
    client.get_configlet_containers = AsyncMock()
    client.set_configlet_containers = AsyncMock()
    client.get_configlets = AsyncMock()
    client.set_configlets_from_files = AsyncMock()
    client.delete_configlets = AsyncMock()
    client.get_studio_inputs_with_path = AsyncMock()
    client.set_studio_inputs = AsyncMock()
    client.delete_configlet_container = AsyncMock()
    return client


@pytest.fixture
def avd_initial_manifest() -> AvdManifest:
    """Fixture to provide an AvdManifest instance for initial deployment."""
    vxlan_configlet = AvdConfiglet(name="VXLAN", file="vxlan.cfg")
    mlag_configlet = AvdConfiglet(name="MLAG", file="mlag.cfg")
    bgp_configlet = AvdConfiglet(name="BGP", file="bgp.cfg")

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
        assert not deployment_result.removed_static_config_root_containers

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
        cfl1 = AvdConfiglet(name="CF_LEAF1", file="/path/to/cfl1.cfg")
        cfl2 = AvdConfiglet(name="CF_LEAF2", file="/path/to/cfl2.cfg")
        cfs1 = AvdConfiglet(name="CF_SPINE1", file="/path/to/cfs1.cfg")  # New configlet

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
        assert deployment_result.removed_static_config_root_containers == ["UNUSED_ROOT"]

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
        assert deployment_result.removed_static_config_root_containers == ["AVD_ROOT1"]
