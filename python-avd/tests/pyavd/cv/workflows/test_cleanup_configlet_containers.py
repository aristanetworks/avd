# Copyright (c) 2025-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from unittest.mock import MagicMock

import pytest

from pyavd._cv.workflows.cleanup_configlet_containers import cleanup_configlet_containers
from pyavd._cv.workflows.models import CVDevice, CVDeviceDeployment, CVWorkspace, DeployToCvResult

from .helpers import create_grpc_container

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


# === Test Cases ===


@pytest.mark.asyncio
class TestCleanupLegacyConfigletContainers:
    """Test suite for the cleanup_configlet_containers workflow."""

    async def test_empty_device_deployments_does_nothing(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that an empty device_deployments list results in no actions."""
        await cleanup_configlet_containers([], deployment_result, mock_cv_client)

        mock_cv_client.get_configlet_containers.assert_not_called()
        mock_cv_client.delete_configlet_container.assert_not_called()
        mock_cv_client.delete_configlets.assert_not_called()
        assert not deployment_result.removed_configs

    async def test_no_manifest_devices_does_nothing(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that deployments with no manifest-opted devices result in no actions."""
        deployments = [_config_deployment("device-1", "SERIAL1")]

        await cleanup_configlet_containers(deployments, deployment_result, mock_cv_client)

        mock_cv_client.get_configlet_containers.assert_not_called()
        assert not deployment_result.removed_configs

    async def test_manifest_devices_without_serial_numbers_does_nothing(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that manifest devices with no serial_number are skipped."""
        deployments = [_manifest_deployment("device-1")]

        await cleanup_configlet_containers(deployments, deployment_result, mock_cv_client)

        mock_cv_client.get_configlet_containers.assert_not_called()
        assert not deployment_result.removed_configs

    async def test_root_container_does_not_exist(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that no cleanup happens if the root container doesn't exist on CV."""
        deployments = [_manifest_deployment("device-1", "SERIAL1")]
        mock_cv_client.get_configlet_containers.return_value = []

        await cleanup_configlet_containers(deployments, deployment_result, mock_cv_client)

        mock_cv_client.get_configlet_containers.assert_called_once()
        mock_cv_client.delete_configlet_container.assert_not_called()
        mock_cv_client.delete_configlets.assert_not_called()
        assert not deployment_result.removed_configs

    async def test_devices_not_in_root_container(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that no cleanup happens if the target devices don't have containers under the root."""
        deployments = [_manifest_deployment("device-1", "SERIAL1")]

        # Root container exists but has different children.
        root_container = create_grpc_container(
            container_id="avd-configlets",
            name="AVD Configurations",
            description="",
            query="device:*",
            child_ids=["avd-OTHER_SERIAL"],
        )
        mock_cv_client.get_configlet_containers.return_value = [root_container]

        await cleanup_configlet_containers(deployments, deployment_result, mock_cv_client)

        mock_cv_client.delete_configlet_container.assert_not_called()
        mock_cv_client.delete_configlets.assert_not_called()
        assert not deployment_result.removed_configs

    async def test_cleanup_some_devices(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test cleanup of specific device containers while keeping others."""
        deployments = [
            _manifest_deployment("device-1", "SERIAL1"),
            _config_deployment("device-2", "SERIAL2"),  # Not manifest-opted — should be kept
        ]

        # Root container has two children, we're only removing one.
        root_container = create_grpc_container(
            container_id="avd-configlets",
            name="AVD Configurations",
            description="",
            query="device:*",
            child_ids=["avd-SERIAL1", "avd-SERIAL2"],
        )
        mock_cv_client.get_configlet_containers.return_value = [root_container]

        await cleanup_configlet_containers(deployments, deployment_result, mock_cv_client)

        # Container and configlet for SERIAL1 should be deleted.
        mock_cv_client.delete_configlet_container.assert_called_once_with(workspace_id="pytest_workspace", assignment_id="avd-SERIAL1")
        mock_cv_client.delete_configlets.assert_called_once_with(workspace_id="pytest_workspace", configlet_ids=["avd-SERIAL1"])

        # Root container should be updated with remaining children.
        mock_cv_client.set_configlet_container.assert_called_once_with(
            workspace_id="pytest_workspace",
            container_id="avd-configlets",
            child_assignment_ids=["avd-SERIAL2"],
        )

        # Root container should NOT be deleted.
        assert mock_cv_client.delete_configlet_container.call_count == 1

        assert deployment_result.removed_configs == ["avd-SERIAL1"]

    async def test_cleanup_all_devices_removes_root(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that removing all device containers also removes the root container and unregisters from studio."""
        deployments = [
            _manifest_deployment("device-1", "SERIAL1"),
            _manifest_deployment("device-2", "SERIAL2"),
        ]

        root_container = create_grpc_container(
            container_id="avd-configlets",
            name="AVD Configurations",
            description="",
            query="device:*",
            child_ids=["avd-SERIAL1", "avd-SERIAL2"],
        )
        mock_cv_client.get_configlet_containers.return_value = [root_container]
        mock_cv_client.get_studio_inputs_with_path.return_value = ["avd-configlets", "other-root"]

        await cleanup_configlet_containers(deployments, deployment_result, mock_cv_client)

        # Both device containers should be deleted + root.
        assert mock_cv_client.delete_configlet_container.call_count == 3  # 2 devices + 1 root
        mock_cv_client.delete_configlets.assert_called_once_with(workspace_id="pytest_workspace", configlet_ids=["avd-SERIAL1", "avd-SERIAL2"])

        # Root should be removed from studio inputs, preserving other roots.
        mock_cv_client.set_studio_inputs.assert_called_once_with(
            studio_id="studio-static-configlet",
            workspace_id="pytest_workspace",
            input_path=["configletAssignmentRoots"],
            inputs=["other-root"],
        )

        assert deployment_result.removed_configs == ["avd-SERIAL1", "avd-SERIAL2"]

    async def test_cleanup_all_devices_root_not_in_studio_inputs(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test cleanup when root is already absent from studio inputs."""
        deployments = [_manifest_deployment("device-1", "SERIAL1")]

        root_container = create_grpc_container(
            container_id="avd-configlets",
            name="AVD Configurations",
            description="",
            query="device:*",
            child_ids=["avd-SERIAL1"],
        )
        mock_cv_client.get_configlet_containers.return_value = [root_container]
        mock_cv_client.get_studio_inputs_with_path.return_value = []

        await cleanup_configlet_containers(deployments, deployment_result, mock_cv_client)

        # Root container should be deleted.
        assert mock_cv_client.delete_configlet_container.call_count == 2  # device + root

        # Studio inputs should NOT be updated (root wasn't there).
        mock_cv_client.set_studio_inputs.assert_not_called()
