# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import re
import tempfile
from contextlib import AbstractContextManager
from contextlib import nullcontext as does_not_raise
from logging import INFO, getLogger
from os import environ
from typing import TYPE_CHECKING, Any
from unittest.mock import patch

import pytest

from pyavd._cv.client.exceptions import CVResourceInvalidState, CVWorkspaceBuildFailed, CVWorkspaceSubmitFailedInactiveDevices
from pyavd._cv.workflows.create_workspace_on_cv import create_workspace_on_cv
from pyavd._cv.workflows.deploy_to_cv import deploy_to_cv
from pyavd._cv.workflows.finalize_workspace_on_cv import finalize_workspace_on_cv
from pyavd._cv.workflows.models import CloudVision, CVDevice, CVEosConfig, CVWorkspace, DeployToCvResult
from pyavd._cv.workflows.verify_devices_on_cv import verify_devices_in_cloudvision_inventory, verify_devices_on_cv
from tests.pyavd.cv.constants import (
    MOCKED_WORKSPACE_DESCRIPTION,
    MOCKED_WORKSPACE_ID,
    MOCKED_WORKSPACE_NAME,
    MOCKED_WORKSPACE_REQUEST_ID_ABANDON,
    MOCKED_WORKSPACE_REQUEST_ID_BUILD_FAIL,
    MOCKED_WORKSPACE_REQUEST_ID_BUILD_SUCCESS,
    MOCKED_WORKSPACE_REQUEST_ID_SUBMIT_FAILURE_INACTIVE_DEVICES,
    MOCKED_WORKSPACE_REQUEST_ID_SUBMIT_SUCCESS,
    MOCKED_WORKSPACE_REQUESTED_STATE_SUBMITTED,
)

if TYPE_CHECKING:
    from pyavd._cv.client import CVClient


LOGGER = getLogger(__name__)

# Environment variables
# TODO: avoid having a default server and instead run tests to all recorded servers in offline mode.
CV_SERVER = environ.get("CV_SERVER") or "www.cv-prod-us-central1-c.arista.io"
CV_TOKEN = environ.get("CV_ACCESS_TOKEN")
RECORDING = environ.get("RECORDING")

ExpectedExceptionContext = AbstractContextManager[pytest.ExceptionInfo | None]


def _mocked_cvdevices(hostnames: list[str] | None = None, device_count: int | None = None) -> list[CVDevice]:
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


@pytest.mark.asyncio
@pytest.mark.parametrize("cv_client", [{"static_recording": True, "cv_version": "CVaaS"}], ids=["CV_CLIENT_STATIC_RECORDINGS"], indirect=True)
@pytest.mark.parametrize(
    ("mocked_cvdevices"),
    [
        # mocked API response: tests/pyavd/cv/mocked_api_recordings/arista.inventory.v1.DeviceService/GetAll/www.cv-prod-us-central1-c.arista.io/\\
        # effc85b759a4d35ba98ae7c22bcef828c070752d.json
        pytest.param(_mocked_cvdevices(hostnames=["avd-ci-leaf2"]), id="SINGLE_STREAMING_DEVICE"),
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
                "result_errors_qty": 0,
                "exception": does_not_raise(),
                "execution_failed": False,
            },
            id="SUBMIT_SUCCESS",
        ),
    ],
)
async def test_deploy_to_cv(
    caplog: pytest.LogCaptureFixture,
    cv_client: CVClient,
    mocked_cvdevices: list[CVDevice],
    workspace: dict[str, Any],
    expected: dict[str, Any],
    workspace_force_submission: bool,
) -> None:
    """
    Test building and submitting Workspace with single streaming device.

    Build request:
        WorkspaceConfigSetRequest(value=WorkspaceConfig(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'),
        request=Request.START_BUILD, request_params=RequestParams(request_id='req-914310f3-08dd-4239-bd42-6d78bf781229')))
    Recorded build response:
        tests/pyavd/cv/mocked_api_recordings/arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/
        1fdd6fcd02728621447eeb8a1d8c9cbfdd9201c9.json
    Submit request:
        WorkspaceConfigSetRequest(value=WorkspaceConfig(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'),
        request=Request.SUBMIT, request_params=RequestParams(request_id='req-b8f4e511-58de-4afe-99f0-b75abf980131')))
    Recorded submit responses:
        tests/pyavd/cv/mocked_api_recordings/arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/
        ba83e98eab07691e8b079958618ab2973822bfe8.json
    """
    with (
        caplog.at_level(INFO),
        expected["exception"],
        patch(
            "pyavd._cv.client.workspace.uuid4",
            side_effect=[workspace["build_request_id"]["id"].removeprefix("req-"), workspace["submit_request_id"]["id"].removeprefix("req-")],
        ),
        patch("pyavd._cv.workflows.deploy_to_cv.CVClient", return_value=cv_client),
        tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", delete=True) as temp_configlet_file,
    ):
        temp_configlet_file.write("alias test test")
        temp_configlet_file.flush()

        result = await deploy_to_cv(
            cloudvision=CloudVision(
                servers="",
                token="",
                username="",
                password="",
            ),
            workspace=CVWorkspace(
                name=workspace["name"],
                description=workspace["description"],
                id=workspace["id"],
                requested_state=workspace["requested_state"],
                force=workspace_force_submission,
            ),
            configs=[CVEosConfig(file=temp_configlet_file.name, device=next(iter(mocked_cvdevices)), configlet_name="TEST_CONFIGLET_NAME")],
        )

    # Assess result
    assert result.failed == expected["execution_failed"]

    # Assert number of returned warnings
    assert len(result.warnings) == expected["result_warnings_qty"]

    # Assert number of returned errors
    assert len(result.errors) == expected["result_errors_qty"]

    # Assert returned workspace object
    assert result.workspace.name == workspace["name"]
    assert result.workspace.description == workspace["description"]
    assert result.workspace.id == workspace["id"]
    assert result.workspace.requested_state == workspace["requested_state"]
    assert result.workspace.force == workspace_force_submission
    assert result.workspace.state == workspace["requested_state"]


@pytest.mark.asyncio
async def test_verify_devices_on_cv_no_devices(cv_client: CVClient) -> None:
    result = await verify_devices_on_cv(devices=[], workspace_id="", skip_missing_devices=False, warnings=[], cv_client=cv_client)
    assert len(result) == 0


@pytest.mark.asyncio
@pytest.mark.parametrize("cv_client", [{"static_recording": True}], ids=["CV_CLIENT_STATIC_RECORDINGS"], indirect=True)
@pytest.mark.parametrize(
    ("workspace_id", "workspace_requested_state", "expected_exception"),
    [
        # mocked API response: tests/pyavd/cv/mocked_api_recordings/arista.workspace.v1.WorkspaceService/GetOne/www.cv-prod-us-central1-c.arista.io/\\
        # bd1b5fdaa11249efe21fa9479c729168b06cda69.json
        pytest.param("ws-cbf7c7ea-a57c-481d-b96b-97c128560000", "pending", does_not_raise(), id="PENDING"),
        # mocked API response: tests/pyavd/cv/mocked_api_recordings/arista.workspace.v1.WorkspaceService/GetOne/www.cv-prod-us-central1-c.arista.io/\\
        # e3c8d23b2dffba4c050956c45d0bda0124500f00.json
        pytest.param("ws-cbf7c7ea-a57c-481d-b96b-97c128560001", None, pytest.raises(CVResourceInvalidState), id="ROLLED_BACK"),
    ],
)
async def test_create_existing_workspace_on_cv(
    cv_client: CVClient, workspace_id: str, workspace_requested_state: str | None, expected_exception: ExpectedExceptionContext
) -> None:
    """
    Test creation of the Workspace where Workspace with this ID already exists.

    Specific use cases:
        1. Attempt to create a Workspace which already exists and is in a WorkspaceState.PENDING state.
        2. Attempt to create a Workspace which already exists and is not in a WorkspaceState.PENDING state. This raises CVResourceInvalidState.
    """
    with expected_exception:
        result = DeployToCvResult(
            workspace=CVWorkspace(
                id=workspace_id,
            )
        )
        await create_workspace_on_cv(workspace=result.workspace, cv_client=cv_client)

    assert result.workspace.id == workspace_id
    assert result.workspace.state == workspace_requested_state


@pytest.mark.asyncio
@pytest.mark.parametrize("cv_client", [{"static_recording": True}], ids=["CV_CLIENT_STATIC_RECORDINGS"], indirect=True)
@pytest.mark.parametrize(
    ("workspace_id", "workspace_requested_state", "expected_exception"),
    [
        # recorded API response: tests/pyavd/cv/mocked_api_recordings/arista.workspace.v1.WorkspaceService/GetOne/www.cv-prod-us-central1-c.arista.io/\\
        # bd1b5fdaa11249efe21fa9479c729168b06cda69.json
        pytest.param("ws-cbf7c7ea-a57c-481d-b96b-97c128560000", "pending", does_not_raise(), id="PENDING"),
        # recorded API response: tests/pyavd/cv/mocked_api_recordings/arista.workspace.v1.WorkspaceService/GetOne/www.cv-prod-us-central1-c.arista.io/\\
        # e3c8d23b2dffba4c050956c45d0bda0124500f00.json
        pytest.param("ws-cbf7c7ea-a57c-481d-b96b-97c128560001", None, pytest.raises(CVResourceInvalidState), id="ROLLED_BACK"),
    ],
)
async def test_create_nonexisting_workspace_on_cv(
    cv_client: CVClient, workspace_id: str, workspace_requested_state: str | None, expected_exception: ExpectedExceptionContext
) -> None:
    """
    Test creation of the Workspace where Workspace with this ID does not yet exist.

    Specific use cases:
        1. Workspace is created with state == PENDING.
        2. Workspace is created with state == ROLLED_BACK.
    """
    with expected_exception:
        result = DeployToCvResult(
            workspace=CVWorkspace(
                id=workspace_id,
            )
        )
        await create_workspace_on_cv(workspace=result.workspace, cv_client=cv_client)

    assert result.workspace.id == workspace_id
    assert result.workspace.state == workspace_requested_state


@pytest.mark.asyncio
@pytest.mark.parametrize("cv_client", [{"static_recording": True}], ids=["CV_CLIENT_STATIC_RECORDINGS"], indirect=True)
async def test_finalize_workspace_on_cv_pending_state(cv_client: CVClient) -> None:
    """Test use case where requested_state == state == 'pending'."""
    workspace = CVWorkspace(requested_state="pending", state="pending")
    result = await finalize_workspace_on_cv(workspace, cv_client, _mocked_cvdevices(hostnames=["avd-ci-leaf1"]), [])

    assert result is None


@pytest.mark.asyncio
@pytest.mark.parametrize("cv_client", [{"static_recording": True}], ids=["CV_CLIENT_STATIC_RECORDINGS"], indirect=True)
async def test_finalize_workspace_on_cv_built_state(cv_client: CVClient) -> None:
    """
    Test Workspace in built state.

    Build request:
        WorkspaceConfigSetRequest(value=WorkspaceConfig(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'),
        request=Request.START_BUILD, request_params=RequestParams(request_id='req-914310f3-08dd-4239-bd42-6d78bf781229')))
    Recorded build response:
        tests/pyavd/cv/mocked_api_recordings/arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/
        1fdd6fcd02728621447eeb8a1d8c9cbfdd9201c9.json
    """
    workspace_id: str = MOCKED_WORKSPACE_ID
    workspace_build_id: str = MOCKED_WORKSPACE_REQUEST_ID_BUILD_SUCCESS["id"]
    workspace_requested_state: str = "built"
    workspace_expected_state: str = "built"

    with patch("pyavd._cv.client.workspace.uuid4", side_effect=[workspace_build_id.removeprefix("req-")]):
        workspace = CVWorkspace(id=workspace_id, requested_state=workspace_requested_state)
        await finalize_workspace_on_cv(workspace, cv_client, _mocked_cvdevices(hostnames=["avd-ci-leaf1"]), [])

    assert workspace.state == workspace_expected_state


@pytest.mark.asyncio
@pytest.mark.parametrize("cv_client", [{"static_recording": True}], ids=["CV_CLIENT_STATIC_RECORDINGS"], indirect=True)
async def test_finalize_workspace_on_cv_abandoned_state(cv_client: CVClient) -> None:
    """
    Test Workspace in abandoned state.

    Build request:
        WorkspaceConfigSetRequest(value=WorkspaceConfig(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'),
        request=Request.START_BUILD, request_params=RequestParams(request_id='req-914310f3-08dd-4239-bd42-6d78bf781229')))
    Recorded build response:
        tests/pyavd/cv/mocked_api_recordings/arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/
        1fdd6fcd02728621447eeb8a1d8c9cbfdd9201c9.json
    Abandon request:
        WorkspaceConfigSetRequest(value=WorkspaceConfig(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'),
        request=Request.ABANDON, request_params=RequestParams(request_id='req-b65374c1-4333-4c68-9b09-d753e8560609')))
    Recorded abandon responses:
        tests/pyavd/cv/mocked_api_recordings/arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/
        c3455eeb927146c3ba4e5fbb3d51b959fc84da17.json
    """
    workspace_id: str = MOCKED_WORKSPACE_ID
    workspace_build_id: str = MOCKED_WORKSPACE_REQUEST_ID_BUILD_SUCCESS["id"]
    workspace_abandon_id: str = MOCKED_WORKSPACE_REQUEST_ID_ABANDON["id"]
    workspace_requested_state: str = "abandoned"
    workspace_expected_state: str = "abandoned"

    with patch("pyavd._cv.client.workspace.uuid4", side_effect=[workspace_build_id.removeprefix("req-"), workspace_abandon_id.removeprefix("req-")]):
        workspace = CVWorkspace(id=workspace_id, requested_state=workspace_requested_state)
        await finalize_workspace_on_cv(workspace, cv_client, _mocked_cvdevices(hostnames=["avd-ci-leaf1"]), [])

    assert workspace.state == workspace_expected_state


@pytest.mark.asyncio
@pytest.mark.parametrize("cv_client", [{"static_recording": True}], ids=["CV_CLIENT_STATIC_RECORDINGS"], indirect=True)
async def test_finalize_workspace_on_cv_deleted_state(cv_client: CVClient) -> None:
    """
    Test Workspace in deleted state.

    Build request:
        WorkspaceConfigSetRequest(value=WorkspaceConfig(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'),
        request=Request.START_BUILD, request_params=RequestParams(request_id='req-914310f3-08dd-4239-bd42-6d78bf781229')))
    Recorded build response:
        tests/pyavd/cv/mocked_api_recordings/arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/
        1fdd6fcd02728621447eeb8a1d8c9cbfdd9201c9.json
    Delete request:
        WorkspaceConfigDeleteRequest(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'))
    Recorded Delete responses:
        tests/pyavd/cv/mocked_api_recordings/arista.workspace.v1.WorkspaceConfigService/Delete/www.cv-prod-us-central1-c.arista.io/
        5cbea5d81be6faa13721aff0c3059bdfdfd188ce.json
    """
    workspace_id: str = MOCKED_WORKSPACE_ID
    workspace_build_id: str = MOCKED_WORKSPACE_REQUEST_ID_BUILD_SUCCESS["id"]
    workspace_requested_state: str = "deleted"
    workspace_expected_state: str = "deleted"

    with patch("pyavd._cv.client.workspace.uuid4", side_effect=[workspace_build_id.removeprefix("req-")]):
        workspace = CVWorkspace(id=workspace_id, requested_state=workspace_requested_state)
        await finalize_workspace_on_cv(workspace, cv_client, _mocked_cvdevices(hostnames=["avd-ci-leaf1"]), [])

    assert workspace.state == workspace_expected_state


@pytest.mark.asyncio
@pytest.mark.parametrize("cv_client", [{"static_recording": True}], ids=["CV_CLIENT_STATIC_RECORDINGS"], indirect=True)
@pytest.mark.parametrize(
    (
        "workspace_requested_state",
        "workspace_expected_state",
        "workspace_abandon_id",
        "logs_patterns",
        "expected_exception",
    ),
    [
        pytest.param("built", "build failed", "", [], pytest.raises(CVWorkspaceBuildFailed), id="BUILT"),
        pytest.param(
            "abandoned",
            "abandoned",
            MOCKED_WORKSPACE_REQUEST_ID_ABANDON["id"],
            [f"Workspace {MOCKED_WORKSPACE_ID} has been successfully abandoned"],
            pytest.raises(CVWorkspaceBuildFailed),
            id="ABANDONED",
        ),
    ],
)
async def test_finalize_workspace_on_cv_build_failure(
    caplog: pytest.LogCaptureFixture,
    cv_client: CVClient,
    workspace_requested_state: str,
    workspace_expected_state: str,
    workspace_abandon_id: str,
    logs_patterns: str,
    expected_exception: ExpectedExceptionContext,
) -> None:
    """
    Test Workspace with failing build.

    Specific use cases:
        1. Failing Workspace build for Workspace with requested_state == built.
        2. Failing Workspace build for Workspace with requested_state == abandoned.

    Build request:
        WorkspaceConfigSetRequest(value=WorkspaceConfig(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'),
        request=Request.START_BUILD, request_params=RequestParams(request_id='req-914310f3-08dd-4239-bd42-6d78b0000000')))
    Recorded build response:
        tests/pyavd/cv/mocked_api_recordings/arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/
        094fa72d5437063770b645129730633334c7e4ed.json
    Abandon request:
        WorkspaceConfigSetRequest(value=WorkspaceConfig(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'),
        request=Request.ABANDON, request_params=RequestParams(request_id='req-b65374c1-4333-4c68-9b09-d753e8560609')))
    Recorded abandon responses:
        tests/pyavd/cv/mocked_api_recordings/arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/
        c3455eeb927146c3ba4e5fbb3d51b959fc84da17.json
    """
    workspace_id: str = MOCKED_WORKSPACE_ID
    workspace_build_id: str = MOCKED_WORKSPACE_REQUEST_ID_BUILD_FAIL["id"]
    workspace_name: str = "WORKSPACE_WITH_BUILD_FAILURE"
    exception_patterns: list[str] = [f"Failed to build workspace {workspace_id}.*See details.*{workspace_id}"]

    with (
        caplog.at_level(INFO),
        patch("pyavd._cv.client.workspace.uuid4", side_effect=[workspace_build_id.removeprefix("req-"), workspace_abandon_id.removeprefix("req-")]),
        expected_exception as exception_info,
    ):
        workspace = CVWorkspace(name=workspace_name, id=workspace_id, requested_state=workspace_requested_state)
        await finalize_workspace_on_cv(workspace, cv_client, _mocked_cvdevices(hostnames=["avd-ci-leaf1"]), [])

    assert workspace.state == workspace_expected_state

    # Assert that log messages match expected log patterns
    for expected_pattern in logs_patterns:
        assert any(re.search(re.compile(expected_pattern), str(record.message)) for record in caplog.records)

    # Assert that exception value contains all expected exception patterns
    for expected_pattern in exception_patterns:
        assert re.search(re.compile(expected_pattern), str(exception_info.value))


@pytest.mark.asyncio
@pytest.mark.parametrize("cv_client", [{"static_recording": True}], ids=["CV_CLIENT_STATIC_RECORDINGS"], indirect=True)
@pytest.mark.parametrize(
    ("input_devices"),
    [
        # mocked API response: tests/pyavd/cv/mocked_api_recordings/arista.inventory.v1.DeviceService/GetAll/www.cv-prod-us-central1-c.arista.io/\\
        # 76601a85f4ab2a9e434ec80eaeea2efc8dc02d71.json
        # mocked request: DeviceStreamRequest(partial_eq_filter=[Device(key=DeviceKey(device_id='B51AA89B6E51E89E1422107EDE3A9438'), hostname=None, \\
        # system_mac_address=None)]
        pytest.param([CVDevice(hostname="avd-ci-leaf2", serial_number="B51AA89B6E51E89E1422107EDE3A9438")], id="SINGLE_STREAMING_DEVICE_SET_HOSTNAME_SERIAL"),
        # mocked API response: tests/pyavd/cv/mocked_api_recordings/arista.inventory.v1.DeviceService/GetAll/www.cv-prod-us-central1-c.arista.io/\\
        # 396119d5076221da87045ff93ab5041f30e9d9e0.json
        # mocked request: DeviceStreamRequest(partial_eq_filter=[Device(key=DeviceKey(device_id=None), hostname=None, system_mac_address='50:00:00:d5:5d:c0')]
        pytest.param([CVDevice(hostname="avd-ci-leaf2", system_mac_address="50:00:00:d5:5d:c0")], id="SINGLE_STREAMING_DEVICE_SET_HOSTNAME_SYSTEM_MAC"),
    ],
)
async def test_verify_devices_in_cloudvision_inventory(
    cv_client: CVClient,
    input_devices: list[CVDevice],
) -> None:
    expected_result = [
        CVDevice(
            hostname="avd-ci-leaf2",
            serial_number="B51AA89B6E51E89E1422107EDE3A9438",
            system_mac_address="50:00:00:d5:5d:c0",
            _exists_on_cv=True,
            _streaming=True,
        )
    ]
    result = await verify_devices_in_cloudvision_inventory(
        devices=input_devices,
        skip_missing_devices=False,
        warnings=[],
        cv_client=cv_client,
    )
    assert result == expected_result


@pytest.mark.asyncio
@pytest.mark.parametrize("cv_client", [{"static_recording": True}], ids=["CV_CLIENT_STATIC_RECORDINGS"], indirect=True)
@pytest.mark.parametrize(
    ("mocked_cvdevices"),
    [
        # mocked API response: tests/pyavd/cv/mocked_api_recordings/arista.inventory.v1.DeviceService/GetAll/www.cv-prod-us-central1-c.arista.io/\\
        # effc85b759a4d35ba98ae7c22bcef828c070752d.json
        pytest.param(_mocked_cvdevices(hostnames=["avd-ci-leaf2"]), id="SINGLE_STREAMING_DEVICE"),
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
                "submit_request_id": MOCKED_WORKSPACE_REQUEST_ID_SUBMIT_FAILURE_INACTIVE_DEVICES,
            },
            {
                "result_warnings_qty": 0,
                "result_warnings_patterns": [],
                "result_errors_patterns": [],
                "logs_patterns": [],
                "exception_patterns": ["Failed to submit CloudVision Workspace due to the presence of inactive devices. "],
                "exception": pytest.raises(CVWorkspaceSubmitFailedInactiveDevices),
                "execution_failed": False,
                "workspace_state": "submit failed",
            },
            id="SUBMIT_FAILURE_INACTIVE",
        ),
    ],
)
async def test_deploy_to_cv_streaming_device_failure(
    caplog: pytest.LogCaptureFixture,
    cv_client: CVClient,
    mocked_cvdevices: list[CVDevice],
    workspace: dict[str, Any],
    expected: dict[str, Any],
    workspace_force_submission: bool,
) -> None:
    """
    Test building and submitting Workspace (both forced and unforced) with streaming device.

    Specific use case where Workspace submission fails due to streaming status changing from ACTIVE to INACTIVE right before submission.

    Build request:
        WorkspaceConfigSetRequest(value=WorkspaceConfig(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'),
        request=Request.START_BUILD, request_params=RequestParams(request_id='req-914310f3-08dd-4239-bd42-6d78bf781229')))
    Recorded build response:
        tests/pyavd/cv/mocked_api_recordings/arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/
        1fdd6fcd02728621447eeb8a1d8c9cbfdd9201c9.json
    Submit request:
        WorkspaceConfigSetRequest(value=WorkspaceConfig(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'),
        request=Request.SUBMIT, request_params=RequestParams(request_id='req-18654b6a-9f75-4a57-878d-d40d73701238')))
    Recorded submit responses:
        tests/pyavd/cv/mocked_api_recordings/arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/
        54f25797c08b0d4ca2c4497e73b4afbfd2959b6f.json
    """
    with (
        caplog.at_level(INFO),
        patch(
            "pyavd._cv.client.workspace.uuid4",
            side_effect=[workspace["build_request_id"]["id"].removeprefix("req-"), workspace["submit_request_id"]["id"].removeprefix("req-")],
        ),
        expected["exception"] as exception_info,
    ):
        result = DeployToCvResult(
            workspace=CVWorkspace(
                name=workspace["name"],
                description=workspace["description"],
                id=workspace["id"],
                requested_state=workspace["requested_state"],
                force=workspace_force_submission,
            )
        )

        _ = await verify_devices_in_cloudvision_inventory(
            devices=mocked_cvdevices,
            skip_missing_devices=False,
            warnings=result.warnings,
            cv_client=cv_client,
        )

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


# Targeting non-streaming device without forcing
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
            _mocked_cvdevices(hostnames=["avd-ci-leaf1"]),
            {
                "result_warnings_qty": 1,
                "result_warnings_patterns": ["Inactive devices present: \\['avd-ci-leaf1 \\(13C20F1EDCCED2D85F6DB2FB9E3AC5B6\\)'\\]"],
                "result_errors_patterns": [],
                "logs_patterns": [],
                "exception_patterns": [
                    "Failed to submit CloudVision Workspace due to the presence of inactive devices: "
                    "\\["
                    "'avd-ci-leaf1 \\(13C20F1EDCCED2D85F6DB2FB9E3AC5B6\\)'"
                    "\\]"
                ],
                "exception": pytest.raises(CVWorkspaceSubmitFailedInactiveDevices),
                "execution_failed": False,
                "workspace_state": "submit failed",
            },
            id="SINGLE_NON_STREAMING_DEVICE",
        ),
    ],
)
async def test_deploy_to_cv_non_streaming_device_unforced(
    caplog: pytest.LogCaptureFixture,
    cv_client: CVClient,
    mocked_cvdevices: list[CVDevice],
    workspace: dict[str, Any],
    expected: dict[str, Any],
    workspace_force_submission: bool,
) -> None:
    """
    Test building and submitting Workspace with non-streaming device without forcing.

    Build request:
        WorkspaceConfigSetRequest(value=WorkspaceConfig(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'),
        request=Request.START_BUILD, request_params=RequestParams(request_id='req-914310f3-08dd-4239-bd42-6d78bf781229')))
    Recorded build response:
        tests/pyavd/cv/mocked_api_recordings/arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/
        1fdd6fcd02728621447eeb8a1d8c9cbfdd9201c9.json
    Submit request:
        WorkspaceConfigSetRequest(value=WorkspaceConfig(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'),
        request=Request.SUBMIT, request_params=RequestParams(request_id='req-18654b6a-9f75-4a57-878d-d40d73701238')))
    Recorded submit responses:
        tests/pyavd/cv/mocked_api_recordings/arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/
        54f25797c08b0d4ca2c4497e73b4afbfd2959b6f.json
    """
    with (
        caplog.at_level(INFO),
        patch(
            "pyavd._cv.client.workspace.uuid4",
            side_effect=[workspace["build_request_id"]["id"].removeprefix("req-"), workspace["submit_request_id"]["id"].removeprefix("req-")],
        ),
        expected["exception"] as exception_info,
    ):
        result = DeployToCvResult(
            workspace=CVWorkspace(
                name=workspace["name"],
                description=workspace["description"],
                id=workspace["id"],
                requested_state=workspace["requested_state"],
                force=workspace_force_submission,
            )
        )

        _ = await verify_devices_in_cloudvision_inventory(
            devices=mocked_cvdevices,
            skip_missing_devices=False,
            warnings=result.warnings,
            cv_client=cv_client,
        )

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


# Targeting non-streaming device with forcing
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
            _mocked_cvdevices(hostnames=["avd-ci-leaf1"]),
            {
                "result_warnings_qty": 1,
                "result_warnings_patterns": ["Inactive devices present: \\['avd-ci-leaf1 \\(13C20F1EDCCED2D85F6DB2FB9E3AC5B6\\)'\\]"],
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
    ],
)
async def test_deploy_to_cv_non_streaming_device_forced(
    caplog: pytest.LogCaptureFixture,
    cv_client: CVClient,
    mocked_cvdevices: list[CVDevice],
    workspace: dict[str, Any],
    expected: dict[str, Any],
    workspace_force_submission: bool,
) -> None:
    """
    Test building and submitting Workspace with non-streaming device with forcing.

    Build request:
        WorkspaceConfigSetRequest(value=WorkspaceConfig(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'),
        request=Request.START_BUILD, request_params=RequestParams(request_id='req-914310f3-08dd-4239-bd42-6d78bf781229')))
    Recorded build response:
        tests/pyavd/cv/mocked_api_recordings/arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/
        1fdd6fcd02728621447eeb8a1d8c9cbfdd9201c9.json
    Submit request:
        WorkspaceConfigSetRequest(value=WorkspaceConfig(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'),
            request=Request.SUBMIT_FORCE, request_params=RequestParams(request_id='req-b8f4e511-58de-4afe-99f0-b75abf980131')))
    Recorded submit responses:
        tests/pyavd/cv/mocked_api_recordings/arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/
        47049c8a6b520f110540f81bcd892ba0e4954908.json
    """
    with (
        caplog.at_level(INFO),
        patch(
            "pyavd._cv.client.workspace.uuid4",
            side_effect=[workspace["build_request_id"]["id"].removeprefix("req-"), workspace["submit_request_id"]["id"].removeprefix("req-")],
        ),
        expected["exception"] as exception_info,
    ):
        result = DeployToCvResult(
            workspace=CVWorkspace(
                name=workspace["name"],
                description=workspace["description"],
                id=workspace["id"],
                requested_state=workspace["requested_state"],
                force=workspace_force_submission,
            )
        )

        _ = await verify_devices_in_cloudvision_inventory(
            devices=mocked_cvdevices,
            skip_missing_devices=False,
            warnings=result.warnings,
            cv_client=cv_client,
        )

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
