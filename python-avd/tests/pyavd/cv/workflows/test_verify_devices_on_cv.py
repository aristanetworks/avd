# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from pyavd._cv.workflows.models import CVDevice
from pyavd._cv.workflows.verify_devices_on_cv import verify_devices_in_cloudvision_inventory

if TYPE_CHECKING:
    from pyavd._cv.client import CVClient


@pytest.mark.asyncio
@pytest.mark.parametrize("cv_client", [{"static_recording": True}], ids=["CV_CLIENT_STATIC_RECORDINGS"], indirect=True)
@pytest.mark.parametrize(
    ("input_devices"),
    [
        pytest.param([CVDevice(hostname="avd-ci-leaf2", serial_number="B51AA89B6E51E89E1422107EDE3A9438")], id="SINGLE_STREAMING_DEVICE_SET_HOSTNAME_SERIAL"),
        pytest.param([CVDevice(hostname="avd-ci-leaf2", system_mac_address="50:00:00:d5:5d:c0")], id="SINGLE_STREAMING_DEVICE_SET_HOSTNAME_SYSTEM_MAC"),
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
            targeted_file: 'arista.inventory.v1.DeviceService/GetAll/www.cv-prod-us-central1-c.arista.io/76601a85f4ab2a9e434ec80eaeea2efc8dc02d71.json'

    2. Verify device based on system_mac_address
        Exact test steps:
        -   description: Fetch device status
            request: 'DeviceStreamRequest(partial_eq_filter=[Device(key=DeviceKey(device_id=None), hostname=None, system_mac_address='50:00:00:d5:5d:c0')],
                time=TimeBounds(start=None, end=None))'
            targeted_file: 'arista.inventory.v1.DeviceService/GetAll/www.cv-prod-us-central1-c.arista.io/396119d5076221da87045ff93ab5041f30e9d9e0.json'
    """
    result = await verify_devices_in_cloudvision_inventory(
        devices=input_devices,
        skip_missing_devices=False,
        warnings=[],
        cv_client=cv_client,
    )
    assert result == [
        CVDevice(
            hostname="avd-ci-leaf2",
            serial_number="B51AA89B6E51E89E1422107EDE3A9438",
            system_mac_address="50:00:00:d5:5d:c0",
            _exists_on_cv=True,
            _streaming=True,
        )
    ]
