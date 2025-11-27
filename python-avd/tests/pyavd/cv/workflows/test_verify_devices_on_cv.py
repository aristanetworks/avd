# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from contextlib import nullcontext as does_not_raise
from logging import INFO, getLogger
from os import environ

import pytest

from pyavd._cv.client import CVClient
from pyavd._cv.workflows.create_workspace_on_cv import create_workspace_on_cv
from pyavd._cv.workflows.models import CVDevice, CVWorkspace
from pyavd._cv.workflows.verify_devices_on_cv import verify_devices_in_cloudvision_inventory

LOGGER = getLogger(__name__)


@pytest.fixture(scope="module")
def device_topology_inputs() -> list[tuple[str, str, str]]:
    return [(f"l{i}_serial", f"l{i}_hostname", f"l{i}_mac") for i in range(1, 95000)]


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


## Live tests ##
@pytest.mark.skipif(environ.get("CV_LIVE_TEST") is None, reason="CV_LIVE_TEST env variable is not set. Live cv_deploy tests are skipped.")
@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("targeted_cv", "verify_certs"),
    [
        pytest.param(
            {
                "cv_access_token": environ.get("CV_PRD_ACCESS_TOKEN", default=""),
                "cv_server": environ.get("CV_PRD_SERVER", default=""),
            },
            True,
            id="CVAAS_PRD",
        ),
        pytest.param(
            {
                "cv_access_token": environ.get("CV_STG_ACCESS_TOKEN", default=""),
                "cv_server": environ.get("CV_STG_SERVER", default=""),
            },
            True,
            id="CVAAS_STG",
        ),
        pytest.param(
            {
                "cv_access_token": environ.get("CV_ONPREM_ACCESS_TOKEN", default=""),
                "cv_server": environ.get("CV_ONPREM_SERVER", default=""),
            },
            False,
            id="CV_ONPREM",
        ),
    ],
)
@pytest.mark.filterwarnings("ignore:Unverified HTTPS request is being made to host")
async def test_verify_devices_on_cv_message_splitting(
    caplog: pytest.LogCaptureFixture,
    targeted_cv: dict[str, str],
    verify_certs: bool,
    device_topology_inputs: list[tuple[str, str, str]],
) -> None:
    """Test ability to gracefully push amount of device inputs which exceeds the message limit (23230607 vs. 20971520 max)."""
    with does_not_raise(), caplog.at_level(INFO):
        async with CVClient(
            servers=targeted_cv["cv_server"],
            token=targeted_cv["cv_access_token"],
            verify_certs=verify_certs,
        ) as cv_client:
            workspace = CVWorkspace(name="AVD_CI_PYTEST_TEST_VERIFY_DEVICES_ON_CV_MESSAGE_SPLITTING", requested_state="pending")
            try:
                # Create Workspace in pending state
                await create_workspace_on_cv(workspace=workspace, cv_client=cv_client)
                # Set I&T Studio topology inputs
                await cv_client.set_topology_studio_inputs(workspace_id=workspace.id, device_inputs=device_topology_inputs)
                # Confirm MAX message size
                assert "exceeded the max of 20971520 for" in next(iter(msg.message for msg in caplog.records if "Message size" in msg.message))
            finally:
                try:
                    # Try to clean Workspace on all CVs to leave no traces
                    await cv_client.abandon_workspace(workspace_id=workspace.id)
                    await cv_client.delete_workspace(workspace_id=workspace.id)
                except Exception as e:
                    LOGGER.warning(
                        "The following exception faced while trying to abandon/clean Workspace %s on %s: %s", workspace.id, targeted_cv["cv_server"], e
                    )
