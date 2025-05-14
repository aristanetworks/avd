# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import re
from contextlib import nullcontext as does_not_raise
from logging import INFO, getLogger
from os import environ
from typing import TYPE_CHECKING, Any
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


async def _deploy_to_cv_core_logic(
    caplog: pytest.LogCaptureFixture,
    cv_client: CVClient,
    mocked_cvdevices: list[CVDevice],
    workspace: dict[str, Any],
    expected: dict[str, Any],
    workspace_force_submission: bool,
) -> None:
    with caplog.at_level(INFO):
        with expected["exception"] as exception_info:
            result = DeployToCvResult(
                workspace=CVWorkspace(
                    name=workspace["name"],
                    description=workspace["description"],
                    id=workspace["id"],
                    requested_state=workspace["requested_state"],
                    force=workspace_force_submission,
                )
            )

            await create_workspace_on_cv(workspace=result.workspace, cv_client=cv_client)

            _ = await verify_devices_in_cloudvision_inventory(
                devices=mocked_cvdevices,
                skip_missing_devices=False,
                warnings=result.warnings,
                cv_client=cv_client,
            )

            # Use cv_client instance to pass required request_ids for building and submitting mocked Workspace
            cv_client._workspace_build_id = workspace["build_request_id"]["id"]
            cv_client._workspace_submit_id = workspace["submit_request_id"]["id"]

            await finalize_workspace_on_cv(workspace=result.workspace, cv_client=cv_client, devices=mocked_cvdevices, warnings=result.warnings)

        # Assert that log messages match expected log patterns
        for expected_pattern in expected["logs_patterns"]:
            assert any(re.search(re.compile(expected_pattern), str(record.message)) for record in caplog.records)

        # Assert that exception value contains all expected exception patterns
        for expected_pattern in expected["exception_patterns"]:
            assert re.search(re.compile(expected_pattern), str(exception_info.value))

        # Assess result
        assert result.failed == expected["execution_failed"]

        # Assert number of returned warnings
        assert len(result.warnings) == expected["result_warnings_qty"]
        # Assert that updated warnings match expected warning patterns
        for expected_pattern in expected["result_warnings_patterns"]:
            assert any(re.search(re.compile(expected_pattern), str(warning_item)) for warning_item in result.warnings)

        # Assert number of returned errors
        assert len(result.errors) == expected["result_errors_qty"]
        # Assert that updated errors match expected error patterns
        for expected_pattern in expected["result_errors_patterns"]:
            assert any(re.search(re.compile(expected_pattern), str(error_item)) for error_item in result.errors)

        # Assert returned workspace object
        assert result.workspace.name == workspace["name"]
        assert result.workspace.description == workspace["description"]
        assert result.workspace.id == workspace["id"]
        assert result.workspace.requested_state == workspace["requested_state"]
        assert result.workspace.force == workspace_force_submission
        assert result.workspace.state == (expected["workspace_state"] or workspace["requested_state"])


# Targeting streaming device(s) without and with forcing
@pytest.mark.asyncio
@pytest.mark.parametrize("cv_client", [{"static_recording": True}], ids=["CV_CLIENT_STATIC_RECORDINGS"], indirect=True)
@pytest.mark.parametrize(
    ("mocked_cvdevices"),
    [
        # mocked API response: tests/pyavd/cv/mocked_api_recordings/arista.inventory.v1.DeviceService/GetAll/www.cv-prod-us-central1-c.arista.io/\\
        # effc85b759a4d35ba98ae7c22bcef828c070752d.json
        pytest.param(mocked_cvdevices(hostnames=["avd-ci-leaf2"]), id="SINGLE_STREAMING_DEVICE"),
        # mocked API response: tests/pyavd/cv/mocked_api_recordings/arista.inventory.v1.DeviceService/GetAll/www.cv-prod-us-central1-c.arista.io/\\
        # 3543d2564818cd282327bdcdc383c795af31f8b3.json
        pytest.param(mocked_cvdevices(hostnames=["avd-ci-leaf2", "avd-ci-leaf3", "avd-ci-leaf4", "avd-ci-spine2"]), id="FOUR_STREAMING_DEVICES"),
    ],
)
@pytest.mark.parametrize(("workspace_force_submission"), [pytest.param(False, id="UNFORCED"), pytest.param(True, id="FORCED")])
@pytest.mark.parametrize(
    (
        "workspace",
        "expected",
    ),
    [
        pytest.param(
            {
                "id": MOCKED_WORKSPACE_ID,
                "name": MOCKED_WORKSPACE_NAME,
                "description": MOCKED_WORKSPACE_DESCRIPTION,
                "requested_state": MOCKED_WORKSPACE_REQUESTED_STATE_SUBMITTED,
                "build_request_id": MOCKED_WORKSPACE_REQUEST_ID_BUILD_SUCCESS,
                "submit_request_id": MOCKED_WORKSPACE_REQUEST_ID_SUBMIT_SUCCESS,
            },
            {
                "result_warnings_qty": 0,
                "result_warnings_patterns": [],
                "result_errors_qty": 0,
                "result_errors_patterns": [],
                "logs_patterns": [],
                "exception_patterns": [],
                "exception": does_not_raise(),
                "execution_failed": False,
                "workspace_state": None,
            },
            id="SUBMIT_SUCCESS",
        ),
    ],
)
async def test_deploy_to_cv_streaming_devices(
    caplog: pytest.LogCaptureFixture,
    cv_client: CVClient,
    mocked_cvdevices: list[CVDevice],
    workspace: dict[str, Any],
    expected: dict[str, Any],
    workspace_force_submission: bool,
) -> None:
    await _deploy_to_cv_core_logic(**locals())


# Targeting non-streaming device(s) (or those that become non-streaming right before Workspace submission) without forcing
@pytest.mark.asyncio
@pytest.mark.parametrize("cv_client", [{"static_recording": True}], ids=["CV_CLIENT_STATIC_RECORDINGS"], indirect=True)
@pytest.mark.parametrize(
    ("workspace"),
    [
        pytest.param(
            {
                "id": MOCKED_WORKSPACE_ID,
                "name": MOCKED_WORKSPACE_NAME,
                "description": MOCKED_WORKSPACE_DESCRIPTION,
                "requested_state": MOCKED_WORKSPACE_REQUESTED_STATE_SUBMITTED,
                "build_request_id": MOCKED_WORKSPACE_REQUEST_ID_BUILD_SUCCESS,
                "submit_request_id": MOCKED_WORKSPACE_REQUEST_ID_SUBMIT_FAILURE_INACTIVE_DEVICES,
            },
            id="SUBMIT_FAILURE",
        )
    ],
)
@pytest.mark.parametrize(("workspace_force_submission"), [pytest.param(False, id="UNFORCED")])
@pytest.mark.parametrize(
    (
        "mocked_cvdevices",
        "expected",
    ),
    [
        # Targeting single non-streaming device
        pytest.param(
            # mocked API response: tests/pyavd/cv/mocked_api_recordings/arista.inventory.v1.DeviceService/GetAll/www.cv-prod-us-central1-c.arista.io/\\
            # 196b71ff9d79dd22efd981b7cbbd601e7173f18c.json
            mocked_cvdevices(hostnames=["avd-ci-leaf1"]),
            {
                "result_warnings_qty": 1,
                "result_warnings_patterns": [
                    "Inactive devices present: \\["
                    "CVDevice\\(hostname='avd-ci-leaf1', serial_number='13C20F1EDCCED2D85F6DB2FB9E3AC5B6', system_mac_address='50:00:00:72:8b:31', "
                    "_exists_on_cv=True, _streaming=False\\)\\]"
                ],
                "result_errors_qty": 0,
                "result_errors_patterns": [],
                "logs_patterns": [
                    "Failed to submit CloudVision Workspace due to the presence of inactive devices.*Inactive devices: "
                    "\\[CVDevice\\(hostname='avd-ci-leaf1', serial_number='13C20F1EDCCED2D85F6DB2FB9E3AC5B6', system_mac_address='50:00:00:72:8b:31', "
                    "_exists_on_cv=True, _streaming=False\\)\\]"
                ],
                "exception_patterns": [
                    "Failed to submit CloudVision Workspace due to the presence of inactive devices.*Inactive devices: "
                    "\\[CVDevice\\(hostname='avd-ci-leaf1', serial_number='13C20F1EDCCED2D85F6DB2FB9E3AC5B6', system_mac_address='50:00:00:72:8b:31', "
                    "_exists_on_cv=True, _streaming=False\\)\\]"
                ],
                "exception": pytest.raises(CVWorkspaceSubmitFailedInactiveDevices),
                "execution_failed": False,
                "workspace_state": "submit failed",
            },
            id="SINGLE_NON_STREAMING_DEVICE",
        ),
        pytest.param(
            # mocked API response: tests/pyavd/cv/mocked_api_recordings/arista.inventory.v1.DeviceService/GetAll/www.cv-prod-us-central1-c.arista.io/\\
            # 1e402c0d434ec24517a43c0905b1de5833f580e1.json
            mocked_cvdevices(hostnames=["avd-ci-core1", "avd-ci-leaf1", "avd-ci-spine1"]),
            {
                "result_warnings_qty": 1,
                "result_warnings_patterns": [
                    "Inactive devices present: \\["
                    "CVDevice\\(hostname='avd-ci-core1', serial_number='20C292B489214DF32F9506C242A722FF', system_mac_address='50:00:00:a1:33:1a', "
                    "_exists_on_cv=True, _streaming=False\\), "
                    "CVDevice\\(hostname='avd-ci-leaf1', serial_number='13C20F1EDCCED2D85F6DB2FB9E3AC5B6', system_mac_address='50:00:00:72:8b:31', "
                    "_exists_on_cv=True, _streaming=False\\), "
                    "CVDevice\\(hostname='avd-ci-spine1', serial_number='DCC816CEAC4BBD6319385043AD318362', system_mac_address='50:00:00:d7:ee:0b', "
                    "_exists_on_cv=True, _streaming=False\\)\\]"
                ],
                "result_errors_qty": 0,
                "result_errors_patterns": [],
                "logs_patterns": [
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
                "exception_patterns": [
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
                "exception": pytest.raises(CVWorkspaceSubmitFailedInactiveDevices),
                "execution_failed": False,
                "workspace_state": "submit failed",
            },
            id="THREE_NON_STREAMING_DEVICES",
        ),
        # Targeting four streaming devices
        # Use case where WS submission fails because devices became inactive after we fetched their status from CV (they were all active)
        # but right before we initiated WS submission
        pytest.param(
            # mocked API response: tests/pyavd/cv/mocked_api_recordings/arista.inventory.v1.DeviceService/GetAll/www.cv-prod-us-central1-c.arista.io/\\
            # 3543d2564818cd282327bdcdc383c795af31f8b3.json
            mocked_cvdevices(hostnames=["avd-ci-leaf2", "avd-ci-leaf3", "avd-ci-leaf4", "avd-ci-spine2"]),
            {
                "result_warnings_qty": 0,
                "result_warnings_patterns": [],
                "result_errors_qty": 0,
                "result_errors_patterns": [],
                "logs_patterns": [],
                "exception_patterns": [
                    "Failed to submit CloudVision Workspace due to the presence of inactive devices\\..*Exact list of inactive devices is unknown\\."
                ],
                "exception": pytest.raises(CVWorkspaceSubmitFailedInactiveDevices),
                "execution_failed": False,
                "workspace_state": "submit failed",
            },
            id="FOUR_STREAMING_DEVICES_BECOME_NON_STREAMING",
        ),
    ],
)
async def test_deploy_to_cv_non_streaming_devices_unforced(
    caplog: pytest.LogCaptureFixture,
    cv_client: CVClient,
    mocked_cvdevices: list[CVDevice],
    workspace: dict[str, Any],
    expected: dict[str, Any],
    workspace_force_submission: bool,
) -> None:
    await _deploy_to_cv_core_logic(**locals())


# Targeting non-streaming device(s) with forcing
@pytest.mark.asyncio
@pytest.mark.parametrize("cv_client", [{"static_recording": True}], ids=["CV_CLIENT_STATIC_RECORDINGS"], indirect=True)
@pytest.mark.parametrize(
    ("workspace"),
    [
        pytest.param(
            {
                "id": MOCKED_WORKSPACE_ID,
                "name": MOCKED_WORKSPACE_NAME,
                "description": MOCKED_WORKSPACE_DESCRIPTION,
                "requested_state": MOCKED_WORKSPACE_REQUESTED_STATE_SUBMITTED,
                "build_request_id": MOCKED_WORKSPACE_REQUEST_ID_BUILD_SUCCESS,
                # Live attempt to submit WS targeting single non-streaming device returns ResponseStatus.SUCCESS. Live example shown below:
                #   Response(status=ResponseStatus.SUCCESS, message='Submitted successfully. No change control was created because no config or \\  # ERA001
                #   software changes were created.', code=ResponseCode.UNSPECIFIED)
                "submit_request_id": MOCKED_WORKSPACE_REQUEST_ID_SUBMIT_SUCCESS,
            },
            id="SUBMIT_SUCCESS",
        )
    ],
)
@pytest.mark.parametrize(("workspace_force_submission"), [pytest.param(True, id="FORCED")])
@pytest.mark.parametrize(
    (
        "mocked_cvdevices",
        "expected",
    ),
    [
        pytest.param(
            # mocked API response: tests/pyavd/cv/mocked_api_recordings/arista.inventory.v1.DeviceService/GetAll/www.cv-prod-us-central1-c.arista.io/\\
            # 196b71ff9d79dd22efd981b7cbbd601e7173f18c.json
            mocked_cvdevices(hostnames=["avd-ci-leaf1"]),
            {
                "result_warnings_qty": 1,
                "result_warnings_patterns": [
                    "Inactive devices present: \\["
                    "CVDevice\\(hostname='avd-ci-leaf1', serial_number='13C20F1EDCCED2D85F6DB2FB9E3AC5B6', system_mac_address='50:00:00:72:8b:31', "
                    "_exists_on_cv=True, _streaming=False\\)\\]"
                ],
                "result_errors_qty": 0,
                "result_errors_patterns": [],
                "logs_patterns": [],
                "exception_patterns": [],
                "exception": does_not_raise(),
                "execution_failed": False,
                "workspace_state": None,
            },
            id="SINGLE_NON_STREAMING_DEVICE",
        ),
        pytest.param(
            # mocked API response: tests/pyavd/cv/mocked_api_recordings/arista.inventory.v1.DeviceService/GetAll/www.cv-prod-us-central1-c.arista.io/\\
            # 1e402c0d434ec24517a43c0905b1de5833f580e1.json
            mocked_cvdevices(hostnames=["avd-ci-core1", "avd-ci-leaf1", "avd-ci-spine1"]),
            {
                "result_warnings_qty": 1,
                "result_warnings_patterns": [
                    "Inactive devices present: \\["
                    "CVDevice\\(hostname='avd-ci-core1', serial_number='20C292B489214DF32F9506C242A722FF', system_mac_address='50:00:00:a1:33:1a', "
                    "_exists_on_cv=True, _streaming=False\\), "
                    "CVDevice\\(hostname='avd-ci-leaf1', serial_number='13C20F1EDCCED2D85F6DB2FB9E3AC5B6', system_mac_address='50:00:00:72:8b:31', "
                    "_exists_on_cv=True, _streaming=False\\), "
                    "CVDevice\\(hostname='avd-ci-spine1', serial_number='DCC816CEAC4BBD6319385043AD318362', system_mac_address='50:00:00:d7:ee:0b', "
                    "_exists_on_cv=True, _streaming=False\\)\\]"
                ],
                "result_errors_qty": 0,
                "result_errors_patterns": [],
                "logs_patterns": [],
                "exception_patterns": [],
                "exception": does_not_raise(),
                "execution_failed": False,
                "workspace_state": None,
            },
            id="THREE_NON_STREAMING_DEVICES",
        ),
    ],
)
async def test_deploy_to_cv_non_streaming_devices_forced(
    caplog: pytest.LogCaptureFixture,
    cv_client: CVClient,
    mocked_cvdevices: list[CVDevice],
    workspace: dict[str, Any],
    expected: dict[str, Any],
    workspace_force_submission: bool,
) -> None:
    await _deploy_to_cv_core_logic(**locals())


# Targeting mixed (streaming and non-streaming) devices without and with forcing
@pytest.mark.asyncio
@pytest.mark.parametrize("cv_client", [{"static_recording": True}], ids=["CV_CLIENT_STATIC_RECORDINGS"], indirect=True)
@pytest.mark.parametrize(
    ("mocked_cvdevices"),
    [
        # mocked API response: tests/pyavd/cv/mocked_api_recordings/arista.inventory.v1.DeviceService/GetAll/www.cv-prod-us-central1-c.arista.io/\\
        # 6eadbac40b99ea6f9510fb9fca9e3f9888882285.json
        pytest.param(
            mocked_cvdevices(hostnames=["avd-ci-core1", "avd-ci-leaf1", "avd-ci-leaf2", "avd-ci-leaf3", "avd-ci-leaf4", "avd-ci-spine1", "avd-ci-spine2"]),
            id="MIXED_DEVICES",
        ),
    ],
)
@pytest.mark.parametrize(
    (
        "workspace",
        "workspace_force_submission",
        "expected",
    ),
    [
        # Targeting all devices (mix of streaming and non-streaming) without forcing
        pytest.param(
            {
                "submit_request_id": MOCKED_WORKSPACE_REQUEST_ID_SUBMIT_FAILURE_INACTIVE_DEVICES,
            },
            False,
            {
                "result_warnings_qty": 1,
                "result_warnings_patterns": [
                    "Inactive devices present: \\["
                    "CVDevice\\(hostname='avd-ci-core1', serial_number='20C292B489214DF32F9506C242A722FF', system_mac_address='50:00:00:a1:33:1a', "
                    "_exists_on_cv=True, _streaming=False\\), "
                    "CVDevice\\(hostname='avd-ci-leaf1', serial_number='13C20F1EDCCED2D85F6DB2FB9E3AC5B6', system_mac_address='50:00:00:72:8b:31', "
                    "_exists_on_cv=True, _streaming=False\\), "
                    "CVDevice\\(hostname='avd-ci-spine1', serial_number='DCC816CEAC4BBD6319385043AD318362', system_mac_address='50:00:00:d7:ee:0b', "
                    "_exists_on_cv=True, _streaming=False\\)\\]"
                ],
                "result_errors_qty": 0,
                "result_errors_patterns": [],
                "logs_patterns": [],
                "exception_patterns": [
                    "Failed to submit CloudVision Workspace due to the presence of inactive devices\\..*Inactive devices: \\["
                    "CVDevice\\(hostname='avd-ci-core1', serial_number='20C292B489214DF32F9506C242A722FF', system_mac_address='50:00:00:a1:33:1a', "
                    "_exists_on_cv=True, _streaming=False\\), "
                    "CVDevice\\(hostname='avd-ci-leaf1', serial_number='13C20F1EDCCED2D85F6DB2FB9E3AC5B6', system_mac_address='50:00:00:72:8b:31', "
                    "_exists_on_cv=True, _streaming=False\\), "
                    "CVDevice\\(hostname='avd-ci-spine1', serial_number='DCC816CEAC4BBD6319385043AD318362', system_mac_address='50:00:00:d7:ee:0b', "
                    "_exists_on_cv=True, _streaming=False\\)\\]"
                ],
                "exception": pytest.raises(CVWorkspaceSubmitFailedInactiveDevices),
                "execution_failed": False,
                "workspace_state": "submit failed",
            },
            id="SUBMIT_FAILURE_INACTIVE-UNFORCED",
        ),
        # Targeting all devices (mix of streaming and non-streaming) with forcing
        pytest.param(
            {
                "submit_request_id": MOCKED_WORKSPACE_REQUEST_ID_SUBMIT_SUCCESS,
            },
            True,
            {
                "result_warnings_qty": 1,
                "result_warnings_patterns": [
                    "Inactive devices present: \\["
                    "CVDevice\\(hostname='avd-ci-core1', serial_number='20C292B489214DF32F9506C242A722FF', system_mac_address='50:00:00:a1:33:1a', "
                    "_exists_on_cv=True, _streaming=False\\), "
                    "CVDevice\\(hostname='avd-ci-leaf1', serial_number='13C20F1EDCCED2D85F6DB2FB9E3AC5B6', system_mac_address='50:00:00:72:8b:31', "
                    "_exists_on_cv=True, _streaming=False\\), "
                    "CVDevice\\(hostname='avd-ci-spine1', serial_number='DCC816CEAC4BBD6319385043AD318362', system_mac_address='50:00:00:d7:ee:0b', "
                    "_exists_on_cv=True, _streaming=False\\)\\]"
                ],
                "result_errors_qty": 0,
                "result_errors_patterns": [],
                "logs_patterns": [],
                "exception_patterns": [],
                "exception": does_not_raise(),
                "execution_failed": False,
                "workspace_state": None,
            },
            id="SUBMIT_SUCCESS-FORCED",
        ),
        # Targeting all devices (mix of streaming and non-streaming) without forcing and facing unspecified error
        pytest.param(
            {
                "submit_request_id": MOCKED_WORKSPACE_REQUEST_ID_SUBMIT_FAILURE_OTHER_EXCEPTION,
            },
            False,
            {
                "result_warnings_qty": 1,
                "result_warnings_patterns": [
                    "Inactive devices present: \\["
                    "CVDevice\\(hostname='avd-ci-core1', serial_number='20C292B489214DF32F9506C242A722FF', system_mac_address='50:00:00:a1:33:1a', "
                    "_exists_on_cv=True, _streaming=False\\), "
                    "CVDevice\\(hostname='avd-ci-leaf1', serial_number='13C20F1EDCCED2D85F6DB2FB9E3AC5B6', system_mac_address='50:00:00:72:8b:31', "
                    "_exists_on_cv=True, _streaming=False\\), "
                    "CVDevice\\(hostname='avd-ci-spine1', serial_number='DCC816CEAC4BBD6319385043AD318362', system_mac_address='50:00:00:d7:ee:0b', "
                    "_exists_on_cv=True, _streaming=False\\)\\]"
                ],
                "result_errors_qty": 0,
                "result_errors_patterns": [],
                "logs_patterns": [
                    "Inactive devices present: \\["
                    "CVDevice\\(hostname='avd-ci-core1', serial_number='20C292B489214DF32F9506C242A722FF', system_mac_address='50:00:00:a1:33:1a', "
                    "_exists_on_cv=True, _streaming=False\\), "
                    "CVDevice\\(hostname='avd-ci-leaf1', serial_number='13C20F1EDCCED2D85F6DB2FB9E3AC5B6', system_mac_address='50:00:00:72:8b:31', "
                    "_exists_on_cv=True, _streaming=False\\), "
                    "CVDevice\\(hostname='avd-ci-spine1', serial_number='DCC816CEAC4BBD6319385043AD318362', system_mac_address='50:00:00:d7:ee:0b', "
                    "_exists_on_cv=True, _streaming=False\\)\\]"
                ],
                "exception_patterns": [
                    "Failed to submit workspace ws-cbf7c7ea-a57c-481d-b96b-97c12856395e: Response\\(status=ResponseStatus.FAIL, "
                    "message='Unknown exception faced', code=ResponseCode.UNSPECIFIED\\)"
                ],
                "exception": pytest.raises(CVWorkspaceSubmitFailed),
                "execution_failed": False,
                "workspace_state": "submit failed",
            },
            id="SUBMIT_FAILURE_UNSPECIFIED-UNFORCED",
        ),
        # Targeting all devices (mix of streaming and non-streaming) with forcing and facing unspecified error
        pytest.param(
            {
                "submit_request_id": MOCKED_WORKSPACE_REQUEST_ID_SUBMIT_FAILURE_OTHER_EXCEPTION,
            },
            True,
            {
                "result_warnings_qty": 1,
                "result_warnings_patterns": [
                    "Inactive devices present: \\["
                    "CVDevice\\(hostname='avd-ci-core1', serial_number='20C292B489214DF32F9506C242A722FF', system_mac_address='50:00:00:a1:33:1a', "
                    "_exists_on_cv=True, _streaming=False\\), "
                    "CVDevice\\(hostname='avd-ci-leaf1', serial_number='13C20F1EDCCED2D85F6DB2FB9E3AC5B6', system_mac_address='50:00:00:72:8b:31', "
                    "_exists_on_cv=True, _streaming=False\\), "
                    "CVDevice\\(hostname='avd-ci-spine1', serial_number='DCC816CEAC4BBD6319385043AD318362', system_mac_address='50:00:00:d7:ee:0b', "
                    "_exists_on_cv=True, _streaming=False\\)\\]"
                ],
                "result_errors_qty": 0,
                "result_errors_patterns": [],
                "logs_patterns": [
                    "Inactive devices present: \\["
                    "CVDevice\\(hostname='avd-ci-core1', serial_number='20C292B489214DF32F9506C242A722FF', system_mac_address='50:00:00:a1:33:1a', "
                    "_exists_on_cv=True, _streaming=False\\), "
                    "CVDevice\\(hostname='avd-ci-leaf1', serial_number='13C20F1EDCCED2D85F6DB2FB9E3AC5B6', system_mac_address='50:00:00:72:8b:31', "
                    "_exists_on_cv=True, _streaming=False\\), "
                    "CVDevice\\(hostname='avd-ci-spine1', serial_number='DCC816CEAC4BBD6319385043AD318362', system_mac_address='50:00:00:d7:ee:0b', "
                    "_exists_on_cv=True, _streaming=False\\)\\]"
                ],
                "exception_patterns": [
                    "Failed to submit workspace ws-cbf7c7ea-a57c-481d-b96b-97c12856395e: Response\\(status=ResponseStatus.FAIL, "
                    "message='Unknown exception faced', code=ResponseCode.UNSPECIFIED\\)"
                ],
                "exception": pytest.raises(CVWorkspaceSubmitFailed),
                "execution_failed": False,
                "workspace_state": "submit failed",
            },
            id="SUBMIT_FAILURE_UNSPECIFIED-FORCED",
        ),
    ],
)
async def test_deploy_to_cv_mixed_devices(
    caplog: pytest.LogCaptureFixture,
    cv_client: CVClient,
    mocked_cvdevices: list[CVDevice],
    workspace: dict[str, Any],
    expected: dict[str, Any],
    workspace_force_submission: bool,
) -> None:
    workspace.update(
        {
            "id": MOCKED_WORKSPACE_ID,
            "name": MOCKED_WORKSPACE_NAME,
            "description": MOCKED_WORKSPACE_DESCRIPTION,
            "requested_state": MOCKED_WORKSPACE_REQUESTED_STATE_SUBMITTED,
            "build_request_id": MOCKED_WORKSPACE_REQUEST_ID_BUILD_SUCCESS,
        }
    )
    await _deploy_to_cv_core_logic(**locals())
