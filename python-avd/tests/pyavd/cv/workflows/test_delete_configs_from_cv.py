# Copyright (c) 2025-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from pyavd._cv.api.arista.configlet.v1 import Configlet, ConfigletAssignment, ConfigletKey
from pyavd._cv.workflows.deploy_configs_to_cv import CONFIGLET_CONTAINER_ID, delete_configs_from_cv
from pyavd._cv.workflows.models import AvdDevice, AvdWorkspace, CVDevice, CVDeviceDeployment, CVWorkspace, DeployToCvResult

from .helpers import create_grpc_container

if TYPE_CHECKING:
    from unittest.mock import MagicMock

# === Test Fixtures ===


@pytest.fixture
def deployment_result() -> DeployToCvResult:
    """Fixture to provide a fresh deployment result object for each test."""
    workspace = CVWorkspace(avd_workspace=AvdWorkspace(name="pytest_workspace", id="pytest_workspace"))
    return DeployToCvResult(workspace=workspace)


def _manifest_deployment(hostname: str, serial_number: str | None = None) -> CVDeviceDeployment:
    """Helper to create a CVDeviceDeployment with use_static_config_manifest=True."""
    return CVDeviceDeployment(device=CVDevice(avd_device=AvdDevice(hostname=hostname), serial_number=serial_number), use_static_config_manifest=True)


def _config_deployment(hostname: str, serial_number: str | None = None) -> CVDeviceDeployment:
    """Helper to create a CVDeviceDeployment with use_static_config_manifest=False (default)."""
    return CVDeviceDeployment(device=CVDevice(avd_device=AvdDevice(hostname=hostname), serial_number=serial_number))


def _make_configlet(configlet_id: str, display_name: str | None = None) -> Configlet:
    """Build a minimal Configlet object exposing key.configlet_id and display_name to the workflow."""
    return Configlet(
        key=ConfigletKey(workspace_id="pytest_workspace", configlet_id=configlet_id),
        display_name=display_name if display_name is not None else f"AVD-{configlet_id}",
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

        # No GET means no downstream delete/set is possible.
        mock_cv_client.get_configlets.assert_not_called()
        mock_cv_client.get_configlet_containers.assert_not_called()
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
        """Test that no delete or update is issued when the configlet, the container, and the root are all absent."""
        deployments = [_manifest_deployment("device-1", "SERIAL1")]

        mock_cv_client.get_configlets.return_value = []
        mock_cv_client.get_configlet_containers.return_value = []

        await delete_configs_from_cv(deployments, deployment_result, mock_cv_client)

        mock_cv_client.delete_configlet_container.assert_not_called()
        mock_cv_client.delete_configlets.assert_not_called()
        mock_cv_client.set_configlet_container.assert_not_called()
        mock_cv_client.set_studio_inputs.assert_not_called()
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
        assert deployment_result.removed_configs == ["AVD-avd-SERIAL1"]

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
        assert deployment_result.removed_configs == ["AVD-avd-SERIAL1"]

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
        assert deployment_result.removed_configs == ["AVD-avd-SERIAL1", "AVD-avd-SERIAL2"]

    async def test_delete_existing_empty_root(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that an existing empty root container is deleted and unregistered from studio."""
        deployments = [_manifest_deployment("device-1", "SERIAL1")]

        mock_cv_client.get_configlets.return_value = []
        root_container = create_grpc_container(
            container_id=CONFIGLET_CONTAINER_ID,
            name="AVD Configurations",
            description="",
            query="device:*",
            child_ids=[],
        )
        mock_cv_client.get_configlet_containers.return_value = [root_container]
        mock_cv_client.get_studio_inputs_with_path.return_value = [CONFIGLET_CONTAINER_ID, "other-root"]

        await delete_configs_from_cv(deployments, deployment_result, mock_cv_client)

        # Root container is deleted, no per-device deletes since none existed.
        mock_cv_client.delete_configlet_container.assert_called_once_with(workspace_id="pytest_workspace", assignment_id=CONFIGLET_CONTAINER_ID)
        mock_cv_client.delete_configlets.assert_not_called()
        mock_cv_client.set_configlet_container.assert_not_called()
        # Root is unregistered from the studio, preserving other roots.
        mock_cv_client.set_studio_inputs.assert_called_once_with(
            studio_id="studio-static-configlet",
            workspace_id="pytest_workspace",
            input_path=["configletAssignmentRoots"],
            inputs=["other-root"],
        )
        assert not deployment_result.removed_configs

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


def _decommission_flat(hostname: str, serial_number: str | None = None, exists_on_cv: bool = True) -> CVDeviceDeployment:
    """Helper to create a flat-layout decommission CVDeviceDeployment (no manifest)."""
    return CVDeviceDeployment(
        device=CVDevice(avd_device=AvdDevice(hostname=hostname), serial_number=serial_number, exists_on_cv=exists_on_cv, action="decommission"),
        use_static_config_manifest=False,
    )


def _decommission_manifest(hostname: str, serial_number: str | None = None, exists_on_cv: bool = True) -> CVDeviceDeployment:
    """Helper to create a manifest-layout decommission CVDeviceDeployment."""
    return CVDeviceDeployment(
        device=CVDevice(avd_device=AvdDevice(hostname=hostname), serial_number=serial_number, exists_on_cv=exists_on_cv, action="decommission"),
        use_static_config_manifest=True,
    )


@pytest.mark.asyncio
class TestDeleteConfigsFromCvWithDecommission:
    """Test suite for delete_configs_from_cv when decommission deployments are included."""

    async def test_no_decommission_deployments_does_nothing(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that an empty device_deployments list produces no API calls."""
        await delete_configs_from_cv([], deployment_result, mock_cv_client)

        mock_cv_client.get_configlets.assert_not_called()
        mock_cv_client.get_configlet_containers.assert_not_called()
        assert not deployment_result.removed_configs

    async def test_only_deploy_devices_with_no_manifest_transition_does_nothing(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that a list containing only deploy devices with no manifest-transition produces no API calls."""
        await delete_configs_from_cv([_config_deployment("device-1", "SERIAL1")], deployment_result, mock_cv_client)

        mock_cv_client.get_configlets.assert_not_called()
        mock_cv_client.get_configlet_containers.assert_not_called()
        assert not deployment_result.removed_configs

    async def test_manifest_decommission_device_not_targeted(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that manifest-layout decommission devices are excluded from the target IDs (the manifest handles their cleanup)."""
        await delete_configs_from_cv([_decommission_manifest("device-1", "SERIAL1")], deployment_result, mock_cv_client)

        mock_cv_client.get_configlets.assert_not_called()
        mock_cv_client.get_configlet_containers.assert_not_called()
        assert not deployment_result.removed_configs

    async def test_flat_decommission_device_without_serial_not_targeted(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that flat-layout decommission devices with no serial_number are excluded from the target IDs."""
        await delete_configs_from_cv([_decommission_flat("device-1", serial_number=None)], deployment_result, mock_cv_client)

        mock_cv_client.get_configlets.assert_not_called()
        mock_cv_client.get_configlet_containers.assert_not_called()
        assert not deployment_result.removed_configs

    async def test_flat_decommission_device_not_on_cv_not_targeted(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that flat-layout decommission devices with exists_on_cv=False are excluded from the target IDs."""
        await delete_configs_from_cv([_decommission_flat("device-1", "SERIAL1", exists_on_cv=False)], deployment_result, mock_cv_client)

        mock_cv_client.get_configlets.assert_not_called()
        mock_cv_client.get_configlet_containers.assert_not_called()
        assert not deployment_result.removed_configs

    async def test_flat_decommission_device_configlet_deleted(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that the configlet and container for a flat-layout decommission device are deleted when they exist on CV."""
        mock_cv_client.get_configlets.return_value = [_make_configlet("avd-SERIAL1")]
        mock_cv_client.get_configlet_containers.return_value = [_make_target_container("avd-SERIAL1")]

        await delete_configs_from_cv([_decommission_flat("device-1", "SERIAL1")], deployment_result, mock_cv_client)

        mock_cv_client.delete_configlets.assert_called_once_with(workspace_id="pytest_workspace", configlet_ids=["avd-SERIAL1"])
        mock_cv_client.delete_configlet_container.assert_called_once_with(workspace_id="pytest_workspace", assignment_id="avd-SERIAL1")
        assert deployment_result.removed_configs == ["AVD-avd-SERIAL1"]

    async def test_flat_decommission_and_manifest_transition_combined(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that flat-layout decommission devices and manifest-transition deploy devices are cleaned up in the same call."""
        manifest_device = _manifest_deployment("manifest-dev", "MANIFEST_SN")
        decom = _decommission_flat("decommission-dev", "DECOM_SN")
        mock_cv_client.get_configlets.return_value = [_make_configlet("avd-MANIFEST_SN"), _make_configlet("avd-DECOM_SN")]
        root_container = create_grpc_container(
            container_id=CONFIGLET_CONTAINER_ID,
            name="AVD Configurations",
            description="",
            query="device:*",
            child_ids=["avd-MANIFEST_SN", "avd-DECOM_SN"],
        )
        mock_cv_client.get_configlet_containers.return_value = [
            _make_target_container("avd-MANIFEST_SN"),
            _make_target_container("avd-DECOM_SN"),
            root_container,
        ]
        mock_cv_client.get_studio_inputs_with_path.return_value = [CONFIGLET_CONTAINER_ID]

        await delete_configs_from_cv([manifest_device, decom], deployment_result, mock_cv_client)

        # Both configlets deleted.
        mock_cv_client.delete_configlets.assert_called_once()
        deleted_ids: list[str] = mock_cv_client.delete_configlets.call_args[1]["configlet_ids"]
        assert set(deleted_ids) == {"avd-MANIFEST_SN", "avd-DECOM_SN"}

        # Both device containers deleted plus root = 3 total.
        assert mock_cv_client.delete_configlet_container.call_count == 3
        assert set(deployment_result.removed_configs) == {"AVD-avd-MANIFEST_SN", "AVD-avd-DECOM_SN"}

    async def test_multiple_flat_decommission_devices(self, mock_cv_client: MagicMock, deployment_result: DeployToCvResult) -> None:
        """Test that multiple flat-layout decommission devices are all cleaned up in one batch."""
        decom1 = _decommission_flat("leaf1", "SN1")
        decom2 = _decommission_flat("leaf2", "SN2")
        mock_cv_client.get_configlets.return_value = [_make_configlet("avd-SN1"), _make_configlet("avd-SN2")]
        root_container = create_grpc_container(
            container_id=CONFIGLET_CONTAINER_ID,
            name="AVD Configurations",
            description="",
            query="device:*",
            child_ids=["avd-SN1", "avd-SN2"],
        )
        mock_cv_client.get_configlet_containers.return_value = [
            _make_target_container("avd-SN1"),
            _make_target_container("avd-SN2"),
            root_container,
        ]
        mock_cv_client.get_studio_inputs_with_path.return_value = [CONFIGLET_CONTAINER_ID]

        await delete_configs_from_cv([decom1, decom2], deployment_result, mock_cv_client)

        mock_cv_client.delete_configlets.assert_called_once()
        deleted_ids: list[str] = mock_cv_client.delete_configlets.call_args[1]["configlet_ids"]
        assert set(deleted_ids) == {"avd-SN1", "avd-SN2"}
        # Both device containers + root deleted.
        assert mock_cv_client.delete_configlet_container.call_count == 3
        assert set(deployment_result.removed_configs) == {"AVD-avd-SN1", "AVD-avd-SN2"}
