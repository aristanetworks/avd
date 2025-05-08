# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import re
from contextlib import nullcontext as does_not_raise
from dataclasses import dataclass, field
from logging import DEBUG, getLogger
from os import environ
from typing import TYPE_CHECKING, Literal
from unittest.mock import patch

import aristaproto
import pytest
import pytest_asyncio

from pyavd._cv.client import CVClient
from pyavd._cv.client.exceptions import CVWorkspaceSubmitFailed, CVWorkspaceSubmitFailedInactiveDevices
from pyavd._cv.workflows.create_workspace_on_cv import create_workspace_on_cv
from pyavd._cv.workflows.finalize_workspace_on_cv import finalize_workspace_on_cv
from pyavd._cv.workflows.models import CVDevice, CVWorkspace, DeployToCvResult
from pyavd._cv.workflows.verify_devices_on_cv import verify_devices_in_cloudvision_inventory
from pyavd._utils import get_v2
from tests.pyavd.cv.constants import (
    MOCKED_WORKSPACE_DESCRIPTION,
    MOCKED_WORKSPACE_ID,
    MOCKED_WORKSPACE_NAME,
    MOCKED_WORKSPACE_REQUEST_ID_BUILD_SUCCESS,
    MOCKED_WORKSPACE_REQUEST_ID_SUBMIT_FAILURE_INACTIVE_DEVICES,
    MOCKED_WORKSPACE_REQUEST_ID_SUBMIT_FAILURE_OTHER_EXCEPTION,
    MOCKED_WORKSPACE_REQUEST_ID_SUBMIT_SUCCESS,
    MOCKED_WORKSPACE_REQUESTED_STATE_SUBMITTED,
)
from tests.pyavd.cv.mockery import (
    mocked_cv_client_aenter,
    mocked_cv_client_build_workspace,
    mocked_cv_client_submit_workspace,
    playback_static_recording_unary_stream,
    playback_static_recording_unary_unary,
    playback_unary_stream,
    playback_unary_unary,
    recording_unary_stream,
    recording_unary_unary,
)

if TYPE_CHECKING:
    from collections.abc import AsyncGenerator

    from _pytest.python_api import RaisesContext

    from pyavd._cv.api.arista.workspace.v1 import ResponseCode, ResponseStatus

LOGGER = getLogger(__name__)

# Environment variables
# TODO: avoid having a default server and instead run tests to all recorded servers in offline mode.
CV_SERVER = environ.get("CV_SERVER") or "www.cv-prod-us-central1-c.arista.io"
CV_TOKEN = environ.get("CV_ACCESS_TOKEN")
RECORDING = environ.get("RECORDING")


@pytest_asyncio.fixture
async def cv_client(request: pytest.FixtureRequest) -> AsyncGenerator[CVClient, None]:
    """
    Instance of CVClient.

    If CV_ACCESS_TOKEN environment variable is set, but RECORDING environment variable is not set,
    this will return a proper instance of CVClient connected to CloudVision with the token.

    If CV_ACCESS_TOKEN environment variable is set, but RECORDING environment variable is set,
    this will return an instance of CVClient connected to CloudVision with the token where all API calls will be recorded.

    Otherwise this will return an instance of CVClient where API calls are mocked using previously recorded API messages.
    """
    static_recording = get_v2(request, "param.static_recording")
    if CV_SERVER and CV_TOKEN:
        LOGGER.info("Running in online mode connecting to %s.", CV_SERVER)
        if RECORDING:
            LOGGER.info("Mocking ServiceStub to RecordingServiceStub")
            aristaproto.grpc.grpclib_client.ServiceStub._org_unary_unary = aristaproto.grpc.grpclib_client.ServiceStub._unary_unary
            aristaproto.grpc.grpclib_client.ServiceStub._org_unary_stream = aristaproto.grpc.grpclib_client.ServiceStub._unary_stream
            aristaproto.grpc.grpclib_client.ServiceStub._unary_unary = recording_unary_unary
            aristaproto.grpc.grpclib_client.ServiceStub._unary_stream = recording_unary_stream
            async with CVClient(servers=CV_SERVER, token=CV_TOKEN) as cv_client:
                yield cv_client

            aristaproto.grpc.grpclib_client.ServiceStub._unary_unary = aristaproto.grpc.grpclib_client.ServiceStub._org_unary_stream
            aristaproto.grpc.grpclib_client.ServiceStub._unary_stream = aristaproto.grpc.grpclib_client.ServiceStub._org_unary_stream

        else:
            async with CVClient(servers=CV_SERVER, token=CV_TOKEN) as cv_client:
                yield cv_client

    else:
        LOGGER.info("Mocking ServiceStub to MockedServiceStub")
        aristaproto.grpc.grpclib_client.ServiceStub._org_unary_unary = aristaproto.grpc.grpclib_client.ServiceStub._unary_unary
        aristaproto.grpc.grpclib_client.ServiceStub._org_unary_stream = aristaproto.grpc.grpclib_client.ServiceStub._unary_stream
        if static_recording:
            aristaproto.grpc.grpclib_client.ServiceStub._unary_unary = playback_static_recording_unary_unary
            aristaproto.grpc.grpclib_client.ServiceStub._unary_stream = playback_static_recording_unary_stream
            with (
                patch("pyavd._cv.client.CVClient.__aenter__", new=mocked_cv_client_aenter),
                patch("pyavd._cv.client.workspace.WorkspaceMixin.build_workspace", new=mocked_cv_client_build_workspace),
                patch("pyavd._cv.client.workspace.WorkspaceMixin.submit_workspace", new=mocked_cv_client_submit_workspace),
            ):
                async with CVClient(servers=CV_SERVER, token=CV_TOKEN) as cv_client:
                    yield cv_client
        else:
            aristaproto.grpc.grpclib_client.ServiceStub._unary_unary = playback_unary_unary
            aristaproto.grpc.grpclib_client.ServiceStub._unary_stream = playback_unary_stream
            with patch("pyavd._cv.client.CVClient.__aenter__", new=mocked_cv_client_aenter):
                async with CVClient(servers=CV_SERVER, token=CV_TOKEN) as cv_client:
                    yield cv_client

        aristaproto.grpc.grpclib_client.ServiceStub._unary_unary = aristaproto.grpc.grpclib_client.ServiceStub._org_unary_unary
        aristaproto.grpc.grpclib_client.ServiceStub._unary_stream = aristaproto.grpc.grpclib_client.ServiceStub._org_unary_stream
        return


@pytest.mark.asyncio
async def test_get_inventory_devices(cv_client: CVClient) -> None:
    result = await cv_client.get_inventory_devices()
    assert len(result) > 0


@pytest.mark.asyncio
async def test_get_inventory_devices_with_filter(cv_client: CVClient) -> None:
    result = await cv_client.get_inventory_devices([(None, None, "avd-ci-spine1")])
    assert len(result) == 1
    assert hasattr(result[0], "hostname")
    assert result[0].hostname == "avd-ci-spine1"


def mocked_cvdevices(hostnames: list[str] | None = None, device_count: int | None = None) -> list[CVDevice]:
    """
    Generate mocked CVDevice instances.

    Parameters:
        hostnames (list[str]): List of device hostnames.
        device_count (int): Number of CVDevice instances to generate.

    Returns:
        list[CVDevice]: List of CVDevice instances.
    """
    if hostnames:
        return [CVDevice(item) for item in hostnames]
    if device_count:
        return [CVDevice(str(item), str(item), str(item)) for item in range(device_count)]
    return [CVDevice(str(item), str(item), str(item)) for item in range(1000000)]


@dataclass
class DataUnderTest:
    workspace_id: str
    workspace_name: str
    workspace_description: str
    workspace_requested_state: Literal["pending", "built", "submitted", "abandoned", "deleted"]
    expected_result_warnings_qty: int
    expected_result_errors_qty: int
    expected_exception: RaisesContext | does_not_raise
    expected_execution_failed: bool
    force_workspace_submission: bool
    expected_workspace_state: str | None
    mocked_cvdevices: list[CVDevice] = field(default_factory=list)
    workspace_build_request_id: dict[str, str | ResponseCode | ResponseStatus] = field(default_factory=dict)
    workspace_submit_request_id: dict[str, str | ResponseCode | ResponseStatus] = field(default_factory=dict)
    expected_result_warnings_patterns: list[str] = field(default_factory=list)
    expected_result_errors_patterns: list[str] = field(default_factory=list)
    expected_logs_patterns: list[str] = field(default_factory=list)
    expected_exception_patterns: list[str] = field(default_factory=list)


@pytest.mark.asyncio
@pytest.mark.parametrize("cv_client", [{"static_recording": True}], indirect=True)
@pytest.mark.parametrize(
    "test_case_data",
    [
        # Targeting single streaming device without forcing
        pytest.param(
            DataUnderTest(
                # mocked API response: tests/pyavd/cv/mocked_api_recordings/arista.inventory.v1.DeviceService/GetAll/www.cv-prod-us-central1-c.arista.io/\\
                # effc85b759a4d35ba98ae7c22bcef828c070752d.json
                mocked_cvdevices=mocked_cvdevices(
                    hostnames=["avd-ci-leaf2"],
                ),
                workspace_id=MOCKED_WORKSPACE_ID,
                workspace_name=MOCKED_WORKSPACE_NAME,
                workspace_description=MOCKED_WORKSPACE_DESCRIPTION,
                workspace_requested_state=MOCKED_WORKSPACE_REQUESTED_STATE_SUBMITTED,
                workspace_build_request_id=MOCKED_WORKSPACE_REQUEST_ID_BUILD_SUCCESS,
                workspace_submit_request_id=MOCKED_WORKSPACE_REQUEST_ID_SUBMIT_SUCCESS,
                expected_result_warnings_qty=0,
                expected_result_warnings_patterns=[],
                expected_result_errors_qty=0,
                expected_result_errors_patterns=[],
                expected_logs_patterns=[],
                expected_exception_patterns=[],
                expected_exception=does_not_raise(),
                expected_execution_failed=False,
                force_workspace_submission=False,
                expected_workspace_state=None,
            ),
            id="TARGETING_SINGLE_STREAMING_DEVICE_UNFORCED",
        ),
        # Targeting single streaming device with forcing
        pytest.param(
            DataUnderTest(
                # mocked CVDevices
                # mocked API response: tests/pyavd/cv/mocked_api_recordings/arista.inventory.v1.DeviceService/GetAll/www.cv-prod-us-central1-c.arista.io/\\
                # effc85b759a4d35ba98ae7c22bcef828c070752d.json
                mocked_cvdevices=mocked_cvdevices(
                    hostnames=["avd-ci-leaf2"],
                ),
                workspace_id=MOCKED_WORKSPACE_ID,
                workspace_name=MOCKED_WORKSPACE_NAME,
                workspace_description=MOCKED_WORKSPACE_DESCRIPTION,
                workspace_requested_state=MOCKED_WORKSPACE_REQUESTED_STATE_SUBMITTED,
                workspace_build_request_id=MOCKED_WORKSPACE_REQUEST_ID_BUILD_SUCCESS,
                workspace_submit_request_id=MOCKED_WORKSPACE_REQUEST_ID_SUBMIT_SUCCESS,
                expected_result_warnings_qty=0,
                expected_result_warnings_patterns=[],
                expected_result_errors_qty=0,
                expected_result_errors_patterns=[],
                expected_logs_patterns=[],
                expected_exception_patterns=[],
                expected_exception=does_not_raise(),
                expected_execution_failed=False,
                force_workspace_submission=True,
                expected_workspace_state=None,
            ),
            id="TARGETING_SINGLE_STREAMING_DEVICE_FORCED",
        ),
        # Targeting four streaming devices without forcing
        pytest.param(
            DataUnderTest(
                # mocked CVDevices
                # mocked API response: tests/pyavd/cv/mocked_api_recordings/arista.inventory.v1.DeviceService/GetAll/www.cv-prod-us-central1-c.arista.io/\\
                # 3543d2564818cd282327bdcdc383c795af31f8b3.json
                mocked_cvdevices=mocked_cvdevices(
                    hostnames=["avd-ci-leaf2", "avd-ci-leaf3", "avd-ci-leaf4", "avd-ci-spine2"],
                ),
                workspace_id=MOCKED_WORKSPACE_ID,
                workspace_name=MOCKED_WORKSPACE_NAME,
                workspace_description=MOCKED_WORKSPACE_DESCRIPTION,
                workspace_requested_state=MOCKED_WORKSPACE_REQUESTED_STATE_SUBMITTED,
                workspace_build_request_id=MOCKED_WORKSPACE_REQUEST_ID_BUILD_SUCCESS,
                workspace_submit_request_id=MOCKED_WORKSPACE_REQUEST_ID_SUBMIT_SUCCESS,
                expected_result_warnings_qty=0,
                expected_result_warnings_patterns=[],
                expected_result_errors_qty=0,
                expected_result_errors_patterns=[],
                expected_logs_patterns=[],
                expected_exception_patterns=[],
                expected_exception=does_not_raise(),
                expected_execution_failed=False,
                force_workspace_submission=False,
                expected_workspace_state=None,
            ),
            id="TARGETING_FOUR_STREAMING_DEVICES_UNFORCED",
        ),
        # Targeting four streaming devices with forcing
        pytest.param(
            DataUnderTest(
                # mocked CVDevices
                # mocked API response: tests/pyavd/cv/mocked_api_recordings/arista.inventory.v1.DeviceService/GetAll/www.cv-prod-us-central1-c.arista.io/\\
                # 3543d2564818cd282327bdcdc383c795af31f8b3.json
                mocked_cvdevices=mocked_cvdevices(
                    hostnames=["avd-ci-leaf2", "avd-ci-leaf3", "avd-ci-leaf4", "avd-ci-spine2"],
                ),
                workspace_id=MOCKED_WORKSPACE_ID,
                workspace_name=MOCKED_WORKSPACE_NAME,
                workspace_description=MOCKED_WORKSPACE_DESCRIPTION,
                workspace_requested_state=MOCKED_WORKSPACE_REQUESTED_STATE_SUBMITTED,
                workspace_build_request_id=MOCKED_WORKSPACE_REQUEST_ID_BUILD_SUCCESS,
                workspace_submit_request_id=MOCKED_WORKSPACE_REQUEST_ID_SUBMIT_SUCCESS,
                expected_result_warnings_qty=0,
                expected_result_warnings_patterns=[],
                expected_result_errors_qty=0,
                expected_result_errors_patterns=[],
                expected_logs_patterns=[],
                expected_exception_patterns=[],
                expected_exception=does_not_raise(),
                expected_execution_failed=False,
                force_workspace_submission=True,
                expected_workspace_state=None,
            ),
            id="TARGETING_FOUR_STREAMING_DEVICES_FORCED",
        ),
        # Targeting single non-streaming device without forcing
        pytest.param(
            DataUnderTest(
                # mocked CVDevices
                # mocked API response: tests/pyavd/cv/mocked_api_recordings/arista.inventory.v1.DeviceService/GetAll/www.cv-prod-us-central1-c.arista.io/\\
                # 196b71ff9d79dd22efd981b7cbbd601e7173f18c.json
                mocked_cvdevices=mocked_cvdevices(
                    hostnames=["avd-ci-leaf1"],
                ),
                workspace_id=MOCKED_WORKSPACE_ID,
                workspace_name=MOCKED_WORKSPACE_NAME,
                workspace_description=MOCKED_WORKSPACE_DESCRIPTION,
                workspace_requested_state=MOCKED_WORKSPACE_REQUESTED_STATE_SUBMITTED,
                workspace_build_request_id=MOCKED_WORKSPACE_REQUEST_ID_BUILD_SUCCESS,
                workspace_submit_request_id=MOCKED_WORKSPACE_REQUEST_ID_SUBMIT_FAILURE_INACTIVE_DEVICES,
                expected_result_warnings_qty=1,
                expected_result_warnings_patterns=[
                    "Inactive devices present: \\["
                    "CVDevice\\(hostname='avd-ci-leaf1', serial_number='13C20F1EDCCED2D85F6DB2FB9E3AC5B6', system_mac_address='50:00:00:72:8b:31', "
                    "_exists_on_cv=True, _streaming=False\\)\\]"
                ],
                expected_result_errors_qty=0,
                expected_result_errors_patterns=[],
                expected_logs_patterns=[
                    "Failed to submit CloudVision Workspace due to the presence of inactive devices.*Inactive devices: "
                    "\\[CVDevice\\(hostname='avd-ci-leaf1', serial_number='13C20F1EDCCED2D85F6DB2FB9E3AC5B6', system_mac_address='50:00:00:72:8b:31', "
                    "_exists_on_cv=True, _streaming=False\\)\\]"
                ],
                expected_exception_patterns=[
                    "Failed to submit CloudVision Workspace due to the presence of inactive devices.*Inactive devices: "
                    "\\[CVDevice\\(hostname='avd-ci-leaf1', serial_number='13C20F1EDCCED2D85F6DB2FB9E3AC5B6', system_mac_address='50:00:00:72:8b:31', "
                    "_exists_on_cv=True, _streaming=False\\)\\]"
                ],
                expected_exception=pytest.raises(CVWorkspaceSubmitFailedInactiveDevices),
                expected_execution_failed=False,
                force_workspace_submission=False,
                expected_workspace_state="submit failed",
            ),
            id="TARGETING_SINGLE_NON_STREAMING_DEVICE_UNFORCED",
        ),
        # Targeting single non-streaming device with forcing
        pytest.param(
            DataUnderTest(
                # mocked CVDevices
                # mocked API response: tests/pyavd/cv/mocked_api_recordings/arista.inventory.v1.DeviceService/GetAll/www.cv-prod-us-central1-c.arista.io/\\
                # 196b71ff9d79dd22efd981b7cbbd601e7173f18c.json
                mocked_cvdevices=mocked_cvdevices(
                    hostnames=["avd-ci-leaf1"],
                ),
                workspace_id=MOCKED_WORKSPACE_ID,
                workspace_name=MOCKED_WORKSPACE_NAME,
                workspace_description=MOCKED_WORKSPACE_DESCRIPTION,
                workspace_requested_state=MOCKED_WORKSPACE_REQUESTED_STATE_SUBMITTED,
                workspace_build_request_id=MOCKED_WORKSPACE_REQUEST_ID_BUILD_SUCCESS,
                # workspace Submit request ID
                # Live attempt to submit WS targeting single non-streaming device returns ResponseStatus.SUCCESS. Live example shown below:
                #   Response(status=ResponseStatus.SUCCESS, message='Submitted successfully. No change control was created because no config or \\  # ERA001
                #   software changes were created.', code=ResponseCode.UNSPECIFIED)
                workspace_submit_request_id=MOCKED_WORKSPACE_REQUEST_ID_SUBMIT_SUCCESS,
                expected_result_warnings_qty=1,
                expected_result_warnings_patterns=[
                    "Inactive devices present: \\["
                    "CVDevice\\(hostname='avd-ci-leaf1', serial_number='13C20F1EDCCED2D85F6DB2FB9E3AC5B6', system_mac_address='50:00:00:72:8b:31', "
                    "_exists_on_cv=True, _streaming=False\\)\\]"
                ],
                expected_result_errors_qty=0,
                expected_result_errors_patterns=[],
                expected_logs_patterns=[],
                expected_exception_patterns=[],
                expected_exception=does_not_raise(),
                expected_execution_failed=False,
                force_workspace_submission=True,
                expected_workspace_state=None,
            ),
            id="TARGETING_SINGLE_NON_STREAMING_DEVICE_FORCED",
        ),
        # Targeting three non-streaming devices without forcing
        pytest.param(
            DataUnderTest(
                # mocked CVDevices
                # mocked API response: tests/pyavd/cv/mocked_api_recordings/arista.inventory.v1.DeviceService/GetAll/www.cv-prod-us-central1-c.arista.io/\\
                # 1e402c0d434ec24517a43c0905b1de5833f580e1.json
                mocked_cvdevices=mocked_cvdevices(
                    hostnames=["avd-ci-core1", "avd-ci-leaf1", "avd-ci-spine1"],
                ),
                workspace_id=MOCKED_WORKSPACE_ID,
                workspace_name=MOCKED_WORKSPACE_NAME,
                workspace_description=MOCKED_WORKSPACE_DESCRIPTION,
                workspace_requested_state=MOCKED_WORKSPACE_REQUESTED_STATE_SUBMITTED,
                workspace_build_request_id=MOCKED_WORKSPACE_REQUEST_ID_BUILD_SUCCESS,
                workspace_submit_request_id=MOCKED_WORKSPACE_REQUEST_ID_SUBMIT_FAILURE_INACTIVE_DEVICES,
                expected_result_warnings_qty=1,
                expected_result_warnings_patterns=[
                    "Inactive devices present: \\["
                    "CVDevice\\(hostname='avd-ci-core1', serial_number='20C292B489214DF32F9506C242A722FF', system_mac_address='50:00:00:a1:33:1a', "
                    "_exists_on_cv=True, _streaming=False\\), "
                    "CVDevice\\(hostname='avd-ci-leaf1', serial_number='13C20F1EDCCED2D85F6DB2FB9E3AC5B6', system_mac_address='50:00:00:72:8b:31', "
                    "_exists_on_cv=True, _streaming=False\\), "
                    "CVDevice\\(hostname='avd-ci-spine1', serial_number='DCC816CEAC4BBD6319385043AD318362', system_mac_address='50:00:00:d7:ee:0b', "
                    "_exists_on_cv=True, _streaming=False\\)\\]"
                ],
                expected_result_errors_qty=0,
                expected_result_errors_patterns=[],
                expected_logs_patterns=[
                    "Failed to submit CloudVision Workspace due to the presence of inactive devices.*Inactive devices: "
                    "\\["
                    "CVDevice\\(hostname='avd-ci-core1', serial_number='20C292B489214DF32F9506C242A722FF', system_mac_address='50:00:00:a1:33:1a', "
                    "_exists_on_cv=True, _streaming=False\\), "
                    "CVDevice\\(hostname='avd-ci-leaf1', serial_number='13C20F1EDCCED2D85F6DB2FB9E3AC5B6', system_mac_address='50:00:00:72:8b:31', "
                    "_exists_on_cv=True, _streaming=False\\), "
                    "CVDevice\\(hostname='avd-ci-spine1', serial_number='DCC816CEAC4BBD6319385043AD318362', system_mac_address='50:00:00:d7:ee:0b', "
                    "_exists_on_cv=True, _streaming=False\\)"
                    "\\]"
                ],
                expected_exception_patterns=[
                    "Failed to submit CloudVision Workspace due to the presence of inactive devices.*Inactive devices: "
                    "\\["
                    "CVDevice\\(hostname='avd-ci-core1', serial_number='20C292B489214DF32F9506C242A722FF', system_mac_address='50:00:00:a1:33:1a', "
                    "_exists_on_cv=True, _streaming=False\\), "
                    "CVDevice\\(hostname='avd-ci-leaf1', serial_number='13C20F1EDCCED2D85F6DB2FB9E3AC5B6', system_mac_address='50:00:00:72:8b:31', "
                    "_exists_on_cv=True, _streaming=False\\), "
                    "CVDevice\\(hostname='avd-ci-spine1', serial_number='DCC816CEAC4BBD6319385043AD318362', system_mac_address='50:00:00:d7:ee:0b', "
                    "_exists_on_cv=True, _streaming=False\\)"
                    "\\]"
                ],
                expected_exception=pytest.raises(CVWorkspaceSubmitFailedInactiveDevices),
                expected_execution_failed=False,
                force_workspace_submission=False,
                expected_workspace_state="submit failed",
            ),
            id="TARGETING_THREE_NON_STREAMING_DEVICES_UNFORCED",
        ),
        # Targeting three non-streaming devices with forcing
        pytest.param(
            DataUnderTest(
                # mocked CVDevices
                # mocked API response: tests/pyavd/cv/mocked_api_recordings/arista.inventory.v1.DeviceService/GetAll/www.cv-prod-us-central1-c.arista.io/\\
                # 1e402c0d434ec24517a43c0905b1de5833f580e1.json
                mocked_cvdevices=mocked_cvdevices(
                    hostnames=["avd-ci-core1", "avd-ci-leaf1", "avd-ci-spine1"],
                ),
                workspace_id=MOCKED_WORKSPACE_ID,
                workspace_name=MOCKED_WORKSPACE_NAME,
                workspace_description=MOCKED_WORKSPACE_DESCRIPTION,
                workspace_requested_state=MOCKED_WORKSPACE_REQUESTED_STATE_SUBMITTED,
                workspace_build_request_id=MOCKED_WORKSPACE_REQUEST_ID_BUILD_SUCCESS,
                workspace_submit_request_id=MOCKED_WORKSPACE_REQUEST_ID_SUBMIT_SUCCESS,
                expected_result_warnings_qty=1,
                expected_result_warnings_patterns=[
                    "Inactive devices present: \\["
                    "CVDevice\\(hostname='avd-ci-core1', serial_number='20C292B489214DF32F9506C242A722FF', system_mac_address='50:00:00:a1:33:1a', "
                    "_exists_on_cv=True, _streaming=False\\), "
                    "CVDevice\\(hostname='avd-ci-leaf1', serial_number='13C20F1EDCCED2D85F6DB2FB9E3AC5B6', system_mac_address='50:00:00:72:8b:31', "
                    "_exists_on_cv=True, _streaming=False\\), "
                    "CVDevice\\(hostname='avd-ci-spine1', serial_number='DCC816CEAC4BBD6319385043AD318362', system_mac_address='50:00:00:d7:ee:0b', "
                    "_exists_on_cv=True, _streaming=False\\)\\]"
                ],
                expected_result_errors_qty=0,
                expected_result_errors_patterns=[],
                expected_logs_patterns=[],
                expected_exception_patterns=[],
                expected_exception=does_not_raise(),
                expected_execution_failed=False,
                force_workspace_submission=True,
                expected_workspace_state=None,
            ),
            id="TARGETING_THREE_NON_STREAMING_DEVICES_FORCED",
        ),
        # Targeting four streaming devices without forcing
        # Use case where WS submission fails because devices became inactive after we fetched their status from CV (they were all active)
        # but before we initiated WS submission
        pytest.param(
            DataUnderTest(
                # mocked CVDevices
                # mocked API response: tests/pyavd/cv/mocked_api_recordings/arista.inventory.v1.DeviceService/GetAll/www.cv-prod-us-central1-c.arista.io/\\
                # 3543d2564818cd282327bdcdc383c795af31f8b3.json
                mocked_cvdevices=mocked_cvdevices(
                    hostnames=["avd-ci-leaf2", "avd-ci-leaf3", "avd-ci-leaf4", "avd-ci-spine2"],
                ),
                workspace_id=MOCKED_WORKSPACE_ID,
                workspace_name=MOCKED_WORKSPACE_NAME,
                workspace_description=MOCKED_WORKSPACE_DESCRIPTION,
                workspace_requested_state=MOCKED_WORKSPACE_REQUESTED_STATE_SUBMITTED,
                workspace_build_request_id=MOCKED_WORKSPACE_REQUEST_ID_BUILD_SUCCESS,
                workspace_submit_request_id=MOCKED_WORKSPACE_REQUEST_ID_SUBMIT_FAILURE_INACTIVE_DEVICES,
                expected_result_warnings_qty=0,
                expected_result_warnings_patterns=[],
                expected_result_errors_qty=0,
                expected_result_errors_patterns=[],
                expected_logs_patterns=[],
                expected_exception_patterns=[
                    "Failed to submit CloudVision Workspace due to the presence of inactive devices\\..*Exact list of inactive devices is unknown\\."
                ],
                expected_exception=pytest.raises(CVWorkspaceSubmitFailedInactiveDevices),
                expected_execution_failed=False,
                force_workspace_submission=False,
                expected_workspace_state="submit failed",
            ),
            id="TARGETING_FOUR_STREAMING_DEVICES_UNFORCED_STILL_RAISED_CVWORKSPACESUBMITFAILEDINACTIVEDEVICES",
        ),
        # Targeting all devices (mix of streaming and non-streaming) without forcing
        pytest.param(
            DataUnderTest(
                # mocked CVDevices
                # mocked API response: tests/pyavd/cv/mocked_api_recordings/arista.inventory.v1.DeviceService/GetAll/www.cv-prod-us-central1-c.arista.io/\\
                # 6eadbac40b99ea6f9510fb9fca9e3f9888882285.json
                mocked_cvdevices=mocked_cvdevices(
                    hostnames=["avd-ci-core1", "avd-ci-leaf1", "avd-ci-leaf2", "avd-ci-leaf3", "avd-ci-leaf4", "avd-ci-spine1", "avd-ci-spine2"],
                ),
                workspace_id=MOCKED_WORKSPACE_ID,
                workspace_name=MOCKED_WORKSPACE_NAME,
                workspace_description=MOCKED_WORKSPACE_DESCRIPTION,
                workspace_requested_state=MOCKED_WORKSPACE_REQUESTED_STATE_SUBMITTED,
                workspace_build_request_id=MOCKED_WORKSPACE_REQUEST_ID_BUILD_SUCCESS,
                workspace_submit_request_id=MOCKED_WORKSPACE_REQUEST_ID_SUBMIT_FAILURE_INACTIVE_DEVICES,
                expected_result_warnings_qty=1,
                expected_result_warnings_patterns=[
                    "Inactive devices present: \\["
                    "CVDevice\\(hostname='avd-ci-core1', serial_number='20C292B489214DF32F9506C242A722FF', system_mac_address='50:00:00:a1:33:1a', "
                    "_exists_on_cv=True, _streaming=False\\), "
                    "CVDevice\\(hostname='avd-ci-leaf1', serial_number='13C20F1EDCCED2D85F6DB2FB9E3AC5B6', system_mac_address='50:00:00:72:8b:31', "
                    "_exists_on_cv=True, _streaming=False\\), "
                    "CVDevice\\(hostname='avd-ci-spine1', serial_number='DCC816CEAC4BBD6319385043AD318362', system_mac_address='50:00:00:d7:ee:0b', "
                    "_exists_on_cv=True, _streaming=False\\)\\]"
                ],
                expected_result_errors_qty=0,
                expected_result_errors_patterns=[],
                expected_logs_patterns=[],
                expected_exception_patterns=[
                    "Failed to submit CloudVision Workspace due to the presence of inactive devices\\..*Inactive devices: \\["
                    "CVDevice\\(hostname='avd-ci-core1', serial_number='20C292B489214DF32F9506C242A722FF', system_mac_address='50:00:00:a1:33:1a', "
                    "_exists_on_cv=True, _streaming=False\\), "
                    "CVDevice\\(hostname='avd-ci-leaf1', serial_number='13C20F1EDCCED2D85F6DB2FB9E3AC5B6', system_mac_address='50:00:00:72:8b:31', "
                    "_exists_on_cv=True, _streaming=False\\), "
                    "CVDevice\\(hostname='avd-ci-spine1', serial_number='DCC816CEAC4BBD6319385043AD318362', system_mac_address='50:00:00:d7:ee:0b', "
                    "_exists_on_cv=True, _streaming=False\\)\\]"
                ],
                expected_exception=pytest.raises(CVWorkspaceSubmitFailedInactiveDevices),
                expected_execution_failed=False,
                force_workspace_submission=False,
                expected_workspace_state="submit failed",
            ),
            id="TARGETING_ALL_STREAMING_NONSTREAMING_DEVICES_UNFORCED",
        ),
        # Targeting all devices (mix of streaming and non-streaming) with forcing
        pytest.param(
            DataUnderTest(
                # mocked CVDevices
                # mocked API response: tests/pyavd/cv/mocked_api_recordings/arista.inventory.v1.DeviceService/GetAll/www.cv-prod-us-central1-c.arista.io/\\
                # 6eadbac40b99ea6f9510fb9fca9e3f9888882285.json
                mocked_cvdevices=mocked_cvdevices(
                    hostnames=["avd-ci-core1", "avd-ci-leaf1", "avd-ci-leaf2", "avd-ci-leaf3", "avd-ci-leaf4", "avd-ci-spine1", "avd-ci-spine2"],
                ),
                workspace_id=MOCKED_WORKSPACE_ID,
                workspace_name=MOCKED_WORKSPACE_NAME,
                workspace_description=MOCKED_WORKSPACE_DESCRIPTION,
                workspace_requested_state=MOCKED_WORKSPACE_REQUESTED_STATE_SUBMITTED,
                workspace_build_request_id=MOCKED_WORKSPACE_REQUEST_ID_BUILD_SUCCESS,
                workspace_submit_request_id=MOCKED_WORKSPACE_REQUEST_ID_SUBMIT_SUCCESS,
                expected_result_warnings_qty=1,
                expected_result_warnings_patterns=[
                    "Inactive devices present: \\["
                    "CVDevice\\(hostname='avd-ci-core1', serial_number='20C292B489214DF32F9506C242A722FF', system_mac_address='50:00:00:a1:33:1a', "
                    "_exists_on_cv=True, _streaming=False\\), "
                    "CVDevice\\(hostname='avd-ci-leaf1', serial_number='13C20F1EDCCED2D85F6DB2FB9E3AC5B6', system_mac_address='50:00:00:72:8b:31', "
                    "_exists_on_cv=True, _streaming=False\\), "
                    "CVDevice\\(hostname='avd-ci-spine1', serial_number='DCC816CEAC4BBD6319385043AD318362', system_mac_address='50:00:00:d7:ee:0b', "
                    "_exists_on_cv=True, _streaming=False\\)\\]"
                ],
                expected_result_errors_qty=0,
                expected_result_errors_patterns=[],
                expected_logs_patterns=[],
                expected_exception_patterns=[],
                expected_exception=does_not_raise(),
                expected_execution_failed=False,
                force_workspace_submission=True,
                expected_workspace_state=None,
            ),
            id="TARGETING_ALL_STREAMING_NONSTREAMING_DEVICES_FORCED",
        ),
        # Targeting all devices (mix of streaming and non-streaming) without forcing
        # Facing unspecified error
        pytest.param(
            DataUnderTest(
                # mocked CVDevices
                # mocked API response: tests/pyavd/cv/mocked_api_recordings/arista.inventory.v1.DeviceService/GetAll/www.cv-prod-us-central1-c.arista.io/\\
                # 6eadbac40b99ea6f9510fb9fca9e3f9888882285.json
                mocked_cvdevices=mocked_cvdevices(
                    hostnames=["avd-ci-core1", "avd-ci-leaf1", "avd-ci-leaf2", "avd-ci-leaf3", "avd-ci-leaf4", "avd-ci-spine1", "avd-ci-spine2"],
                ),
                workspace_id=MOCKED_WORKSPACE_ID,
                workspace_name=MOCKED_WORKSPACE_NAME,
                workspace_description=MOCKED_WORKSPACE_DESCRIPTION,
                workspace_requested_state=MOCKED_WORKSPACE_REQUESTED_STATE_SUBMITTED,
                workspace_build_request_id=MOCKED_WORKSPACE_REQUEST_ID_BUILD_SUCCESS,
                workspace_submit_request_id=MOCKED_WORKSPACE_REQUEST_ID_SUBMIT_FAILURE_OTHER_EXCEPTION,
                expected_result_warnings_qty=1,
                expected_result_warnings_patterns=[
                    "Inactive devices present: \\["
                    "CVDevice\\(hostname='avd-ci-core1', serial_number='20C292B489214DF32F9506C242A722FF', system_mac_address='50:00:00:a1:33:1a', "
                    "_exists_on_cv=True, _streaming=False\\), "
                    "CVDevice\\(hostname='avd-ci-leaf1', serial_number='13C20F1EDCCED2D85F6DB2FB9E3AC5B6', system_mac_address='50:00:00:72:8b:31', "
                    "_exists_on_cv=True, _streaming=False\\), "
                    "CVDevice\\(hostname='avd-ci-spine1', serial_number='DCC816CEAC4BBD6319385043AD318362', system_mac_address='50:00:00:d7:ee:0b', "
                    "_exists_on_cv=True, _streaming=False\\)\\]"
                ],
                expected_result_errors_qty=0,
                expected_result_errors_patterns=[],
                expected_logs_patterns=[
                    "Inactive devices present: \\["
                    "CVDevice\\(hostname='avd-ci-core1', serial_number='20C292B489214DF32F9506C242A722FF', system_mac_address='50:00:00:a1:33:1a', "
                    "_exists_on_cv=True, _streaming=False\\), "
                    "CVDevice\\(hostname='avd-ci-leaf1', serial_number='13C20F1EDCCED2D85F6DB2FB9E3AC5B6', system_mac_address='50:00:00:72:8b:31', "
                    "_exists_on_cv=True, _streaming=False\\), "
                    "CVDevice\\(hostname='avd-ci-spine1', serial_number='DCC816CEAC4BBD6319385043AD318362', system_mac_address='50:00:00:d7:ee:0b', "
                    "_exists_on_cv=True, _streaming=False\\)\\]"
                ],
                expected_exception_patterns=[
                    "Failed to submit workspace ws-cbf7c7ea-a57c-481d-b96b-97c12856395e: Response\\(status=ResponseStatus.FAIL, "
                    "message='Unknown exception faced', code=ResponseCode.UNSPECIFIED\\)"
                ],
                expected_exception=pytest.raises(CVWorkspaceSubmitFailed),
                expected_execution_failed=False,
                force_workspace_submission=False,
                expected_workspace_state="submit failed",
            ),
            id="TARGETING_ALL_STREAMING_NONSTREAMING_DEVICES_UNFORCED_OTHER_EXCEPTION",
        ),
        # Targeting all devices (mix of streaming and non-streaming) with forcing
        # Facing unspecified error
        pytest.param(
            DataUnderTest(
                # mocked CVDevices.
                # mocked API response: tests/pyavd/cv/mocked_api_recordings/arista.inventory.v1.DeviceService/GetAll/www.cv-prod-us-central1-c.arista.io/\\
                # 6eadbac40b99ea6f9510fb9fca9e3f9888882285.json
                mocked_cvdevices=mocked_cvdevices(
                    hostnames=["avd-ci-core1", "avd-ci-leaf1", "avd-ci-leaf2", "avd-ci-leaf3", "avd-ci-leaf4", "avd-ci-spine1", "avd-ci-spine2"],
                ),
                workspace_id=MOCKED_WORKSPACE_ID,
                workspace_name=MOCKED_WORKSPACE_NAME,
                workspace_description=MOCKED_WORKSPACE_DESCRIPTION,
                workspace_requested_state=MOCKED_WORKSPACE_REQUESTED_STATE_SUBMITTED,
                workspace_build_request_id=MOCKED_WORKSPACE_REQUEST_ID_BUILD_SUCCESS,
                workspace_submit_request_id=MOCKED_WORKSPACE_REQUEST_ID_SUBMIT_FAILURE_OTHER_EXCEPTION,
                expected_result_warnings_qty=1,
                expected_result_warnings_patterns=[
                    "Inactive devices present: \\["
                    "CVDevice\\(hostname='avd-ci-core1', serial_number='20C292B489214DF32F9506C242A722FF', system_mac_address='50:00:00:a1:33:1a', "
                    "_exists_on_cv=True, _streaming=False\\), "
                    "CVDevice\\(hostname='avd-ci-leaf1', serial_number='13C20F1EDCCED2D85F6DB2FB9E3AC5B6', system_mac_address='50:00:00:72:8b:31', "
                    "_exists_on_cv=True, _streaming=False\\), "
                    "CVDevice\\(hostname='avd-ci-spine1', serial_number='DCC816CEAC4BBD6319385043AD318362', system_mac_address='50:00:00:d7:ee:0b', "
                    "_exists_on_cv=True, _streaming=False\\)\\]"
                ],
                expected_result_errors_qty=0,
                expected_result_errors_patterns=[],
                expected_logs_patterns=[
                    "Inactive devices present: \\["
                    "CVDevice\\(hostname='avd-ci-core1', serial_number='20C292B489214DF32F9506C242A722FF', system_mac_address='50:00:00:a1:33:1a', "
                    "_exists_on_cv=True, _streaming=False\\), "
                    "CVDevice\\(hostname='avd-ci-leaf1', serial_number='13C20F1EDCCED2D85F6DB2FB9E3AC5B6', system_mac_address='50:00:00:72:8b:31', "
                    "_exists_on_cv=True, _streaming=False\\), "
                    "CVDevice\\(hostname='avd-ci-spine1', serial_number='DCC816CEAC4BBD6319385043AD318362', system_mac_address='50:00:00:d7:ee:0b', "
                    "_exists_on_cv=True, _streaming=False\\)\\]"
                ],
                expected_exception_patterns=[
                    "Failed to submit workspace ws-cbf7c7ea-a57c-481d-b96b-97c12856395e: Response\\(status=ResponseStatus.FAIL, "
                    "message='Unknown exception faced', code=ResponseCode.UNSPECIFIED\\)"
                ],
                expected_exception=pytest.raises(CVWorkspaceSubmitFailed),
                expected_execution_failed=False,
                force_workspace_submission=True,
                expected_workspace_state="submit failed",
            ),
            id="TARGETING_ALL_STREAMING_NONSTREAMING_DEVICES_FORCED_OTHER_EXCEPTION",
        ),
    ],
)
async def test_deploy_to_cv_inactive_devices(
    caplog: pytest.LogCaptureFixture,
    cv_client: CVClient,
    test_case_data: DataUnderTest,
) -> None:
    with caplog.at_level(DEBUG):
        with test_case_data.expected_exception as exception_info:
            result = DeployToCvResult(
                workspace=CVWorkspace(
                    name=test_case_data.workspace_name,
                    description=test_case_data.workspace_description,
                    id=test_case_data.workspace_id,
                    requested_state=test_case_data.workspace_requested_state,
                    force=test_case_data.force_workspace_submission,
                )
            )

            await create_workspace_on_cv(workspace=result.workspace, cv_client=cv_client)

            _ = await verify_devices_in_cloudvision_inventory(
                devices=test_case_data.mocked_cvdevices,
                skip_missing_devices=False,
                warnings=result.warnings,
                cv_client=cv_client,
            )

            # Use cv_client instance to pass required request_ids for building and submitting mocked Workspace
            cv_client._workspace_build_id = test_case_data.workspace_build_request_id["id"]
            cv_client._workspace_submit_id = test_case_data.workspace_submit_request_id["id"]

            await finalize_workspace_on_cv(workspace=result.workspace, cv_client=cv_client, devices=test_case_data.mocked_cvdevices, warnings=result.warnings)

        # Assert that log messages match expected log patterns
        for expected_pattern in test_case_data.expected_logs_patterns:
            assert any(re.search(re.compile(expected_pattern), str(record.message)) for record in caplog.records)

        # If exception is raised, assert that exception value contains all expected exception patterns
        if exception_info and (exception_string := str(exception_info.value)):
            for expected_pattern in test_case_data.expected_exception_patterns:
                assert re.search(re.compile(expected_pattern), exception_string)

        # Assess result
        assert result.failed == test_case_data.expected_execution_failed

        # Assert number of returned warnings
        assert len(result.warnings) == test_case_data.expected_result_warnings_qty
        # Assert that updated warnings match expected warning patterns
        for expected_pattern in test_case_data.expected_result_warnings_patterns:
            assert any(re.search(re.compile(expected_pattern), str(warning_item)) for warning_item in result.warnings)

        # Assert number of returned errors
        assert len(result.errors) == test_case_data.expected_result_errors_qty
        # Assert that updated errors match expected error patterns
        for expected_pattern in test_case_data.expected_result_errors_patterns:
            assert any(re.search(re.compile(expected_pattern), str(error_item)) for error_item in result.errors)

        # Assert returned workspace object
        assert result.workspace.name == test_case_data.workspace_name
        assert result.workspace.description == test_case_data.workspace_description
        assert result.workspace.id == test_case_data.workspace_id
        assert result.workspace.requested_state == test_case_data.workspace_requested_state
        assert result.workspace.force == test_case_data.force_workspace_submission
        if test_case_data.expected_workspace_state:
            assert result.workspace.state == test_case_data.expected_workspace_state
        else:
            assert result.workspace.state == test_case_data.workspace_requested_state
