# Copyright (c) 2024-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING
from unittest.mock import AsyncMock

import pytest

from pyavd._cv.client.exceptions import CVResourceNotFound
from pyavd._cv.workflows.models import AvdDevice, CVDevice
from pyavd._cv.workflows.verify_devices_on_cv import missing_devices_handler, verify_devices_in_cloudvision_inventory

if TYPE_CHECKING:
    from unittest.mock import MagicMock

    from pyavd._cv.client import CVClient


@pytest.mark.asyncio
@pytest.mark.parametrize("cv_client", [{"static_recording": True}], ids=["CV_CLIENT_STATIC_RECORDINGS"], indirect=True)
@pytest.mark.parametrize(
    ("input_devices"),
    [
        pytest.param(
            [CVDevice(avd_device=AvdDevice(hostname="avd-ci-leaf2"), serial_number="B51AA89B6E51E89E1422107EDE3A9438")],
            id="SINGLE_STREAMING_DEVICE_SET_HOSTNAME_SERIAL",
        ),
        pytest.param(
            [CVDevice(avd_device=AvdDevice(hostname="avd-ci-leaf2"), system_mac_address="50:00:00:d5:5d:c0")],
            id="SINGLE_STREAMING_DEVICE_SET_HOSTNAME_SYSTEM_MAC",
        ),
    ],
)
async def test_verify_devices_in_cloudvision_inventory(
    cv_client: CVClient,
    input_devices: list[CVDevice],
) -> None:
    """
    Test verify_devices_in_cloudvision_inventory.

    Specific use cases:
    1. Verify device based on serial_number
        Exact test steps:
        -   description: Fetch device status
            request: 'DeviceStreamRequest(partial_eq_filter=[Device(key=DeviceKey(device_id='B51AA89B6E51E89E1422107EDE3A9438'),
                hostname=None, system_mac_address=None)], time=TimeBounds(start=None, end=None))'
            targeted_file: 'arista.inventory.v1.DeviceService/GetAll/www.cv-prod-us-central1-c.arista.io/cb93ca55d4e990c55560e7705c66afffdb732b2f.json'

    2. Verify device based on system_mac_address
        Exact test steps:
        -   description: Fetch device status
            request: 'DeviceStreamRequest(partial_eq_filter=[Device(key=DeviceKey(device_id=None), hostname=None, system_mac_address='50:00:00:d5:5d:c0')],
                time=TimeBounds(start=None, end=None))'
            targeted_file: 'arista.inventory.v1.DeviceService/GetAll/www.cv-prod-us-central1-c.arista.io/ddb4e4f8e3cc48c48ba838415ca9cbe44e51a2e1.json'
    """
    result = await verify_devices_in_cloudvision_inventory(
        devices=input_devices,
        skip_missing_devices=False,
        warnings=[],
        cv_client=cv_client,
    )
    assert result == [
        CVDevice(
            avd_device=AvdDevice(hostname="avd-ci-leaf2"),
            serial_number="B51AA89B6E51E89E1422107EDE3A9438",
            system_mac_address="50:00:00:d5:5d:c0",
            exists_on_cv=True,
            streaming=True,
        )
    ]


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "device",
    [
        pytest.param(CVDevice(avd_device=AvdDevice(hostname="mocked_eos_device", serial_number="MISSING_SERIAL")), id="MISSING_DEVICE_BY_SERIAL_NUMBER"),
        pytest.param(CVDevice(avd_device=AvdDevice(hostname="mocked_eos_device", system_mac_address="00:11:22:33:44:55")), id="MISSING_DEVICE_BY_MAC_ADDR"),
        pytest.param(CVDevice(avd_device=AvdDevice(hostname="mocked_eos_device")), id="MISSING_DEVICE_BY_HOSTNAME"),
    ],
)
async def test_verify_device_not_found_on_cv(mock_cv_client: MagicMock, device: CVDevice) -> None:
    """Test that device absent from CloudVision gets exists_on_cv=False that CVResourceNotFound exception gets appended to warnings."""
    mock_cv_client.get_inventory_devices = AsyncMock(return_value=[])
    warnings: list[Exception] = []
    result = await verify_devices_in_cloudvision_inventory(devices=[device], skip_missing_devices=True, warnings=warnings, cv_client=mock_cv_client)
    assert result == []
    assert device.exists_on_cv is False
    assert len(warnings) == 1
    assert isinstance(warnings[0], CVResourceNotFound)
    assert warnings[0].args[0] == "Missing devices on CloudVision"


def test_missing_devices_handler_skip_true() -> None:
    """Test that missing_devices_handler returns exception when skip_missing_devices is True."""
    device = CVDevice(avd_device=AvdDevice(hostname="mocked_eos_device"))
    returned_exception = missing_devices_handler(missing_devices=[device], skip_missing_devices=True, context="test context")
    assert isinstance(returned_exception, CVResourceNotFound)
    assert returned_exception.args[0] == "Missing devices on CloudVision"


def test_missing_devices_handler_skip_false() -> None:
    """Test that missing_devices_handler raises exception when skip_missing_devices is False."""
    device = CVDevice(avd_device=AvdDevice(hostname="mocked_eos_device"))
    with pytest.raises(CVResourceNotFound, match="Missing devices on CloudVision"):
        missing_devices_handler(missing_devices=[device], skip_missing_devices=False, context="test context")
