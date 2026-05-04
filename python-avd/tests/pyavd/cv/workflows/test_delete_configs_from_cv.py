# Copyright (c) 2025-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from pyavd._cv.api.arista.configlet.v1 import Configlet, ConfigletAssignment, ConfigletKey
from pyavd._cv.workflows.deploy_configs_to_cv import CONFIGLET_CONTAINER_ID, delete_configs_from_cv
from pyavd._cv.workflows.models import CVDevice, CVDeviceDeployment, CVWorkspace, DeployToCvResult

from .helpers import create_grpc_container

if TYPE_CHECKING:
    from unittest.mock import MagicMock

# === Test Fixtures ===


@pytest.fixture
def deployment_result() -> DeployToCvResult:
    """Fixture to provide a fresh deployment result object for each test."""
    workspace = CVWorkspace(name="pytest_workspace", id="pytest_workspace")
    return DeployToCvResult(workspace=workspace)


def _manifest_deployment(hostname: str, serial_number: str | None = None) -> CVDeviceDeployment:
    """Helper to create a CVDeviceDeployment with use_static_config_manifest=True."""
    return CVDeviceDeployment(device=CVDevice(hostname=hostname, serial_number=serial_number), use_static_config_manifest=True)


def _config_deployment(hostname: str, serial_number: str | None = None) -> CVDeviceDeployment:
    """Helper to create a CVDeviceDeployment with use_static_config_manifest=False (default)."""
    return CVDeviceDeployment(device=CVDevice(hostname=hostname, serial_number=serial_number))


def _make_configlet(configlet_id: str, display_name: str | None = None) -> Configlet:
    """Build a minimal Configlet object exposing key.configlet_id and display_name to the workflow."""
    return Configlet(
        key=ConfigletKey(workspace_id="pytest_workspace", configlet_id=configlet_id),
        display_name=display_name if display_name is not None else f"AVD_{configlet_id}",
    )


def _make_target_container(container_id: str) -> ConfigletAssignment:
    """Build a minimal per-device ConfigletAssignment for use as a get_configlet_containers fixture."""
    return create_grpc_container(container_id=container_id, name=container_id, description="", query=f"device:{container_id}", child_ids=[])


# === Test Cases ===


@pytest.mark.asyncio
class TestDeleteConfigsFromCv:
    """Test suite for the delete_configs_from_cv workflow."""

    async def test_empty_device_deployments_does_nothing(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that an empty device_deployments list results in no actions."""
        await delete_configs_from_cv([], deployment_result, mock_cv_client)

        mock_cv_client.get_configlets.assert_not_called()
        mock_cv_client.get_configlet_containers.assert_not_called()
        mock_cv_client.delete_configlet_container.assert_not_called()
        mock_cv_client.delete_configlets.assert_not_called()
        assert not deployment_result.removed_configs

    async def test_no_manifest_devices_does_nothing(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that deployments with no manifest-opted devices result in no actions."""
        deployments = [_config_deployment("device-1", "SERIAL1")]

        await delete_configs_from_cv(deployments, deployment_result, mock_cv_client)

        mock_cv_client.get_configlets.assert_not_called()
        mock_cv_client.get_configlet_containers.assert_not_called()
        assert not deployment_result.removed_configs

    async def test_manifest_devices_without_serial_numbers_does_nothing(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that manifest devices with no serial_number are skipped."""
        deployments = [_manifest_deployment("device-1")]

        await delete_configs_from_cv(deployments, deployment_result, mock_cv_client)

        mock_cv_client.get_configlets.assert_not_called()
        mock_cv_client.get_configlet_containers.assert_not_called()
        assert not deployment_result.removed_configs

    async def test_nothing_exists_on_cv_does_nothing(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that no delete is issued when the configlet, the container, and the root are all absent."""
        deployments = [_manifest_deployment("device-1", "SERIAL1")]

        mock_cv_client.get_configlets.return_value = []
        mock_cv_client.get_configlet_containers.return_value = []

        await delete_configs_from_cv(deployments, deployment_result, mock_cv_client)

        mock_cv_client.delete_configlet_container.assert_not_called()
        mock_cv_client.delete_configlets.assert_not_called()
        mock_cv_client.set_configlet_container.assert_not_called()
        mock_cv_client.get_studio_inputs_with_path.assert_not_called()
        assert not deployment_result.removed_configs

    async def test_delete_orphan_configlet_when_root_missing(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that a leftover configlet is deleted even if the root container no longer exists."""
        deployments = [_manifest_deployment("device-1", "SERIAL1")]

        mock_cv_client.get_configlets.return_value = [_make_configlet("avd-SERIAL1")]
        mock_cv_client.get_configlet_containers.return_value = []

        await delete_configs_from_cv(deployments, deployment_result, mock_cv_client)

        mock_cv_client.delete_configlets.assert_called_once_with(workspace_id="pytest_workspace", configlet_ids=["avd-SERIAL1"])
        mock_cv_client.delete_configlet_container.assert_not_called()
        mock_cv_client.set_configlet_container.assert_not_called()
        assert deployment_result.removed_configs == ["AVD_avd-SERIAL1"]

    async def test_delete_orphan_container_not_in_root(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that a leftover container is deleted even if it is no longer a child of the root."""
        deployments = [_manifest_deployment("device-1", "SERIAL1")]

        # Configlet is gone, but the per-device container still exists. Root exists with unrelated children.
        mock_cv_client.get_configlets.return_value = []
        root_container = create_grpc_container(
            container_id=CONFIGLET_CONTAINER_ID,
            name="AVD Configurations",
            description="",
            query="device:*",
            child_ids=["avd-OTHER_SERIAL"],
        )
        mock_cv_client.get_configlet_containers.return_value = [_make_target_container("avd-SERIAL1"), root_container]

        await delete_configs_from_cv(deployments, deployment_result, mock_cv_client)

        # Orphan container is deleted...
        mock_cv_client.delete_configlet_container.assert_called_once_with(workspace_id="pytest_workspace", assignment_id="avd-SERIAL1")
        # ...but the root container is left untouched because none of our targets were children of it.
        mock_cv_client.set_configlet_container.assert_not_called()
        # No configlets to delete in this scenario.
        mock_cv_client.delete_configlets.assert_not_called()
        assert not deployment_result.removed_configs

    async def test_delete_subset_of_targets_updates_root(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test deletion of configlets and containers for a subset of targets while keeping unrelated children of the root."""
        deployments = [
            _manifest_deployment("device-1", "SERIAL1"),
            _config_deployment("device-2", "SERIAL2"),  # Not manifest-opted — should be kept
        ]

        mock_cv_client.get_configlets.return_value = [_make_configlet("avd-SERIAL1")]
        root_container = create_grpc_container(
            container_id=CONFIGLET_CONTAINER_ID,
            name="AVD Configurations",
            description="",
            query="device:*",
            child_ids=["avd-SERIAL1", "avd-SERIAL2"],
        )
        mock_cv_client.get_configlet_containers.return_value = [_make_target_container("avd-SERIAL1"), root_container]

        await delete_configs_from_cv(deployments, deployment_result, mock_cv_client)

        mock_cv_client.delete_configlet_container.assert_called_once_with(workspace_id="pytest_workspace", assignment_id="avd-SERIAL1")
        mock_cv_client.delete_configlets.assert_called_once_with(workspace_id="pytest_workspace", configlet_ids=["avd-SERIAL1"])

        # Root container should be updated with remaining children.
        mock_cv_client.set_configlet_container.assert_called_once_with(
            workspace_id="pytest_workspace",
            container_id=CONFIGLET_CONTAINER_ID,
            child_assignment_ids=["avd-SERIAL2"],
        )
        # Studio inputs should NOT be touched (root still has children).
        mock_cv_client.get_studio_inputs_with_path.assert_not_called()
        mock_cv_client.set_studio_inputs.assert_not_called()
        assert deployment_result.removed_configs == ["AVD_avd-SERIAL1"]

    async def test_delete_all_targets_removes_root(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that deleting configlets and containers for all targets also removes the root container and unregisters it from studio."""
        deployments = [
            _manifest_deployment("device-1", "SERIAL1"),
            _manifest_deployment("device-2", "SERIAL2"),
        ]

        mock_cv_client.get_configlets.return_value = [_make_configlet("avd-SERIAL1"), _make_configlet("avd-SERIAL2")]
        root_container = create_grpc_container(
            container_id=CONFIGLET_CONTAINER_ID,
            name="AVD Configurations",
            description="",
            query="device:*",
            child_ids=["avd-SERIAL1", "avd-SERIAL2"],
        )
        mock_cv_client.get_configlet_containers.return_value = [
            _make_target_container("avd-SERIAL1"),
            _make_target_container("avd-SERIAL2"),
            root_container,
        ]
        mock_cv_client.get_studio_inputs_with_path.return_value = [CONFIGLET_CONTAINER_ID, "other-root"]

        await delete_configs_from_cv(deployments, deployment_result, mock_cv_client)

        # Both device containers + root should be deleted (3 total).
        assert mock_cv_client.delete_configlet_container.call_count == 3
        mock_cv_client.delete_configlets.assert_called_once_with(workspace_id="pytest_workspace", configlet_ids=["avd-SERIAL1", "avd-SERIAL2"])

        # Root should be removed from studio inputs, preserving other roots.
        mock_cv_client.set_studio_inputs.assert_called_once_with(
            studio_id="studio-static-configlet",
            workspace_id="pytest_workspace",
            input_path=["configletAssignmentRoots"],
            inputs=["other-root"],
        )
        assert deployment_result.removed_configs == ["AVD_avd-SERIAL1", "AVD_avd-SERIAL2"]

    async def test_delete_all_targets_when_root_not_in_studio_inputs(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that deletion still completes when the root container is already absent from the studio inputs."""
        deployments = [_manifest_deployment("device-1", "SERIAL1")]

        mock_cv_client.get_configlets.return_value = [_make_configlet("avd-SERIAL1")]
        root_container = create_grpc_container(
            container_id=CONFIGLET_CONTAINER_ID,
            name="AVD Configurations",
            description="",
            query="device:*",
            child_ids=["avd-SERIAL1"],
        )
        mock_cv_client.get_configlet_containers.return_value = [_make_target_container("avd-SERIAL1"), root_container]
        mock_cv_client.get_studio_inputs_with_path.return_value = []

        await delete_configs_from_cv(deployments, deployment_result, mock_cv_client)

        # Device container + root container deleted.
        assert mock_cv_client.delete_configlet_container.call_count == 2

        # Studio inputs should NOT be updated (root wasn't there).
        mock_cv_client.set_studio_inputs.assert_not_called()
