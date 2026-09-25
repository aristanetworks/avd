# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from pyavd._cv.api.arista.studio_topology.v1 import Decommission, DecommissionStatus, DeviceKey
from pyavd._cv.workflows.decommission_devices_on_cv import stage_devices_for_decommission_on_cv, wait_for_device_decommission_staging_on_cv
from pyavd._cv.workflows.models import AvdDevice, AvdWorkspace, CVDevice, CVWorkspace, DeployToCvResult

if TYPE_CHECKING:
    from unittest.mock import MagicMock

WORKSPACE = CVWorkspace(avd_workspace=AvdWorkspace(name="pytest_workspace", id="pytest_workspace"))

# === Helpers ===


def _device(hostname: str, serial: str | None, exists_on_cv: bool = True) -> CVDevice:
    """Build a CVDevice object."""
    return CVDevice(avd_device=AvdDevice(hostname=hostname), serial_number=serial, exists_on_cv=exists_on_cv)


def _result() -> DeployToCvResult:
    """Build a DeployToCvResult object."""
    return DeployToCvResult(workspace=WORKSPACE)


def _decommission(device_id: str, status: DecommissionStatus) -> Decommission:
    """Build a Decommission object."""
    return Decommission(key=DeviceKey(device_id=device_id, workspace_id=WORKSPACE.id), status=status)


# === stage_devices_for_decommission_on_cv ===


@pytest.mark.asyncio
class TestStageDevicesForDecommissionOnCv:
    """Test suite for stage_devices_for_decommission_on_cv."""

    async def test_no_devices_returns_empty(self, mock_cv_client: MagicMock) -> None:
        """Test that no devices to stage returns an empty list and makes no API calls."""
        result = _result()
        staged = await stage_devices_for_decommission_on_cv(devices=[], workspace_id=WORKSPACE.id, result=result, cv_client=mock_cv_client)

        assert staged == []
        mock_cv_client.stage_devices_for_decommission.assert_not_called()
        assert not result.warnings

    async def test_devices_without_serial_are_skipped(self, mock_cv_client: MagicMock) -> None:
        """Test that devices with serial_number=None are excluded from the staging call."""
        devices = [_device("leaf1", serial=None), _device("leaf2", serial=None)]
        result = _result()

        staged = await stage_devices_for_decommission_on_cv(devices=devices, workspace_id=WORKSPACE.id, result=result, cv_client=mock_cv_client)

        assert staged == []
        mock_cv_client.stage_devices_for_decommission.assert_not_called()
        assert not result.warnings

    async def test_all_devices_staged_successfully(self, mock_cv_client: MagicMock) -> None:
        """Test that all devices are returned and no warnings added when the API reports no errors."""
        devices = [_device("leaf1", "SN1"), _device("leaf2", "SN2")]
        mock_cv_client.stage_devices_for_decommission.return_value = []
        result = _result()

        staged = await stage_devices_for_decommission_on_cv(devices=devices, workspace_id=WORKSPACE.id, result=result, cv_client=mock_cv_client)

        assert sorted(staged, key=lambda device: device.serial_number or "") == sorted(devices, key=lambda device: device.serial_number or "")
        assert not result.warnings
        mock_cv_client.stage_devices_for_decommission.assert_called_once()
        stage_call_args: dict = mock_cv_client.stage_devices_for_decommission.call_args[1]
        assert stage_call_args["workspace_id"] == WORKSPACE.id
        assert set(stage_call_args["device_ids"]) == {"SN1", "SN2"}

    async def test_partially_failed_staging(self, mock_cv_client: MagicMock) -> None:
        """Test that failed devices are excluded from the returned list and a warning is added per failure."""
        leaf1 = _device("leaf1", "SN1")
        leaf2 = _device("leaf2", "SN2")
        mock_cv_client.stage_devices_for_decommission.return_value = [
            (DeviceKey(device_id="SN2", workspace_id=WORKSPACE.id), "device not found"),
        ]
        result = _result()

        staged = await stage_devices_for_decommission_on_cv(devices=[leaf1, leaf2], workspace_id=WORKSPACE.id, result=result, cv_client=mock_cv_client)

        assert staged == [leaf1]
        assert len(result.warnings) == 1
        assert "SN2" in result.warnings[0]

    async def test_all_devices_fail_staging(self, mock_cv_client: MagicMock) -> None:
        """Test that when every device fails staging, the returned list is empty and warnings are added for each."""
        leaf1 = _device("leaf1", "SN1")
        leaf2 = _device("leaf2", "SN2")
        mock_cv_client.stage_devices_for_decommission.return_value = [
            (DeviceKey(device_id="SN1", workspace_id=WORKSPACE.id), "error1"),
            (DeviceKey(device_id="SN2", workspace_id=WORKSPACE.id), "error2"),
        ]
        result = _result()

        staged = await stage_devices_for_decommission_on_cv(devices=[leaf1, leaf2], workspace_id=WORKSPACE.id, result=result, cv_client=mock_cv_client)

        assert staged == []
        assert len(result.warnings) == 2

    async def test_api_called_with_correct_workspace(self, mock_cv_client: MagicMock) -> None:
        """Test that the workspace_id passed to the API matches the argument given."""
        devices = [_device("leaf1", "SN1")]
        mock_cv_client.stage_devices_for_decommission.return_value = []
        result = _result()

        await stage_devices_for_decommission_on_cv(devices=devices, workspace_id="custom-ws-id", result=result, cv_client=mock_cv_client)

        mock_cv_client.stage_devices_for_decommission.assert_called_once()
        stage_call_args: dict = mock_cv_client.stage_devices_for_decommission.call_args[1]
        assert stage_call_args["workspace_id"] == "custom-ws-id"
        assert set(stage_call_args["device_ids"]) == {"SN1"}


# === wait_for_device_decommission_staging_on_cv ===


@pytest.mark.asyncio
class TestWaitForDeviceDecommissionStagingOnCv:
    """Test suite for wait_for_device_decommission_staging_on_cv."""

    async def test_no_devices_makes_no_api_call(self, mock_cv_client: MagicMock) -> None:
        """Test that an empty device list causes an early return with no API call."""
        result = _result()
        await wait_for_device_decommission_staging_on_cv(devices=[], workspace_id=WORKSPACE.id, result=result, cv_client=mock_cv_client)

        mock_cv_client.wait_for_device_decommission_staging.assert_not_called()
        assert not result.removed_devices
        assert not result.warnings

    async def test_devices_without_serial_are_skipped(self, mock_cv_client: MagicMock) -> None:
        """Test that devices with no serial_number are excluded from the wait call."""
        devices = [_device("leaf1", serial=None)]
        result = _result()
        await wait_for_device_decommission_staging_on_cv(devices=devices, workspace_id=WORKSPACE.id, result=result, cv_client=mock_cv_client)

        mock_cv_client.wait_for_device_decommission_staging.assert_not_called()

    async def test_all_succeed(self, mock_cv_client: MagicMock) -> None:
        """Test that devices with SUCCESS status are added to removed_devices."""
        leaf1 = _device("leaf1", "SN1")
        leaf2 = _device("leaf2", "SN2")
        mock_cv_client.wait_for_device_decommission_staging.return_value = [
            _decommission("SN1", DecommissionStatus.SUCCESS),
            _decommission("SN2", DecommissionStatus.SUCCESS),
        ]
        result = _result()

        await wait_for_device_decommission_staging_on_cv(devices=[leaf1, leaf2], workspace_id=WORKSPACE.id, result=result, cv_client=mock_cv_client)

        assert sorted(result.removed_devices, key=lambda d: d.serial_number or "") == sorted([leaf1, leaf2], key=lambda d: d.serial_number or "")
        assert not result.warnings

    async def test_all_fail(self, mock_cv_client: MagicMock) -> None:
        """Test that devices with FAILURE status produce warnings and are not added to removed_devices."""
        leaf1 = _device("leaf1", "SN1")
        leaf2 = _device("leaf2", "SN2")
        mock_cv_client.wait_for_device_decommission_staging.return_value = [
            _decommission("SN1", DecommissionStatus.FAILURE),
            _decommission("SN2", DecommissionStatus.FAILURE),
        ]
        result = _result()

        await wait_for_device_decommission_staging_on_cv(devices=[leaf1, leaf2], workspace_id=WORKSPACE.id, result=result, cv_client=mock_cv_client)

        assert not result.removed_devices
        assert len(result.warnings) == 2

    async def test_mixed_results(self, mock_cv_client: MagicMock) -> None:
        """Test that successful devices go to removed_devices and failed ones produce a warning."""
        leaf1 = _device("leaf1", "SN1")
        leaf2 = _device("leaf2", "SN2")
        mock_cv_client.wait_for_device_decommission_staging.return_value = [
            _decommission("SN1", DecommissionStatus.SUCCESS),
            _decommission("SN2", DecommissionStatus.FAILURE),
        ]
        result = _result()

        await wait_for_device_decommission_staging_on_cv(devices=[leaf1, leaf2], workspace_id=WORKSPACE.id, result=result, cv_client=mock_cv_client)

        assert result.removed_devices == [leaf1]
        assert len(result.warnings) == 1
        assert "SN2" in result.warnings[0]

    async def test_api_called_with_correct_serial_numbers(self, mock_cv_client: MagicMock) -> None:
        """Test that the wait API is called with the correct workspace_id and device_ids."""
        leaf1 = _device("leaf1", "SN1")
        leaf2 = _device("leaf2", "SN2")
        mock_cv_client.wait_for_device_decommission_staging.return_value = [
            _decommission("SN1", DecommissionStatus.SUCCESS),
            _decommission("SN2", DecommissionStatus.SUCCESS),
        ]
        result = _result()

        await wait_for_device_decommission_staging_on_cv(devices=[leaf1, leaf2], workspace_id=WORKSPACE.id, result=result, cv_client=mock_cv_client)

        mock_cv_client.wait_for_device_decommission_staging.assert_called_once()
        wait_call_args: dict = mock_cv_client.wait_for_device_decommission_staging.call_args[1]
        assert wait_call_args["workspace_id"] == WORKSPACE.id
        assert set(wait_call_args["device_ids"]) == {"SN1", "SN2"}
