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

from pyavd._cv.client.exceptions import CVResourceInvalidState, CVWorkspaceBuildFailed, CVWorkspaceSubmitFailed, CVWorkspaceSubmitFailedInactiveDevices
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
    MOCKED_WORKSPACE_REQUEST_ID_SUBMIT_FAILURE_OTHER_EXCEPTION,
    MOCKED_WORKSPACE_REQUEST_ID_SUBMIT_SUCCESS,
    MOCKED_WORKSPACE_REQUESTED_STATE_SUBMITTED,
)
from tests.pyavd.cv.mockery import mocked_cvdevices

if TYPE_CHECKING:
    from pyavd._cv.client import CVClient


LOGGER = getLogger(__name__)

# Environment variables
# TODO: avoid having a default server and instead run tests to all recorded servers in offline mode.
CV_SERVER = environ.get("CV_SERVER") or "www.cv-prod-us-central1-c.arista.io"
CV_TOKEN = environ.get("CV_ACCESS_TOKEN")
RECORDING = environ.get("RECORDING")

ExpectedExceptionContext = AbstractContextManager[pytest.ExceptionInfo | None]


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
async def test_verify_devices_on_cv_no_devices(cv_client: CVClient) -> None:
    """Test an attempt to verify empty lict of targeted devices."""
    result = await verify_devices_on_cv(devices=[], workspace_id="", skip_missing_devices=False, warnings=[], cv_client=cv_client)
    assert len(result) == 0


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


@pytest.mark.asyncio
@pytest.mark.parametrize("cv_client", [{"static_recording": True}], ids=["CV_CLIENT_STATIC_RECORDINGS"], indirect=True)
@pytest.mark.parametrize(
    ("workspace_id", "workspace_requested_state", "expected_exception"),
    [
        pytest.param("ws-cbf7c7ea-a57c-481d-b96b-97c128560000", "pending", does_not_raise(), id="PENDING"),
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
        Exact test steps:
        -   description: Fetch Workspace
            request: 'WorkspaceRequest(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c128560000'), time=None)'
            targeted_file: 'arista.workspace.v1.WorkspaceService/GetOne/www.cv-prod-us-central1-c.arista.io/bd1b5fdaa11249efe21fa9479c729168b06cda69.json'

    2. Attempt to create a Workspace which already exists and is not in a WorkspaceState.PENDING state. This raises CVResourceInvalidState.
        Exact test steps:
        -   description: Fetch Workspace
            request: 'WorkspaceRequest(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c128560001'), time=None)'
            targeted_file: 'arista.workspace.v1.WorkspaceService/GetOne/www.cv-prod-us-central1-c.arista.io/e3c8d23b2dffba4c050956c45d0bda0124500f00.json'
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
    result = await finalize_workspace_on_cv(workspace, cv_client, mocked_cvdevices(hostnames=["avd-ci-leaf1"]), [])

    assert result is None


@pytest.mark.asyncio
@pytest.mark.parametrize("cv_client", [{"static_recording": True}], ids=["CV_CLIENT_STATIC_RECORDINGS"], indirect=True)
async def test_finalize_workspace_on_cv_built_state(cv_client: CVClient) -> None:
    """
    Test Workspace in built state.

    Exact test steps:
    -   description: Start Workspace build
        request: 'WorkspaceConfigSetRequest(value=WorkspaceConfig(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'),
            request=Request.START_BUILD, request_params=RequestParams(request_id='req-914310f3-08dd-4239-bd42-6d78bf781229')))'
        targeted_file: 'arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/1fdd6fcd02728621447eeb8a1d8c9cbfdd9201c9.json'

    -   description: Fetch build results
        request: 'WorkspaceStreamRequest(partial_eq_filter=[Workspace(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'))])'
        targeted_file: 'arista.workspace.v1.WorkspaceService/Subscribe/www.cv-prod-us-central1-c.arista.io/1560c66d73da2be39448d710f15853fb124b2548.json'
    """
    workspace_id: str = MOCKED_WORKSPACE_ID
    workspace_build_id: str = MOCKED_WORKSPACE_REQUEST_ID_BUILD_SUCCESS["id"]
    workspace_requested_state: str = "built"
    workspace_expected_state: str = "built"

    with patch("pyavd._cv.client.workspace.uuid4", side_effect=[workspace_build_id.removeprefix("req-")]):
        workspace = CVWorkspace(id=workspace_id, requested_state=workspace_requested_state)
        await finalize_workspace_on_cv(workspace, cv_client, mocked_cvdevices(hostnames=["avd-ci-leaf1"]), [])

    assert workspace.state == workspace_expected_state


@pytest.mark.asyncio
@pytest.mark.parametrize("cv_client", [{"static_recording": True}], ids=["CV_CLIENT_STATIC_RECORDINGS"], indirect=True)
async def test_finalize_workspace_on_cv_abandoned_state(cv_client: CVClient) -> None:
    """
    Test Workspace in abandoned state.

    Exact test steps:
        -   description: Start Workspace build
        request: 'WorkspaceConfigSetRequest(value=WorkspaceConfig(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'),
            request=Request.START_BUILD, request_params=RequestParams(request_id='req-914310f3-08dd-4239-bd42-6d78bf781229')))'
        targeted_file: 'arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/1fdd6fcd02728621447eeb8a1d8c9cbfdd9201c9.json'

    -   description: Fetch build results
        request: 'WorkspaceStreamRequest(partial_eq_filter=[Workspace(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'))])'
        targeted_file: 'arista.workspace.v1.WorkspaceService/Subscribe/www.cv-prod-us-central1-c.arista.io/1560c66d73da2be39448d710f15853fb124b2548.json'

    -   description: Abandon Workspace
        request: 'WorkspaceConfigSetRequest(value=WorkspaceConfig(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'),
            request=Request.ABANDON, request_params=RequestParams(request_id='req-b65374c1-4333-4c68-9b09-d753e8560609')))'
        targeted_file: 'arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/c3455eeb927146c3ba4e5fbb3d51b959fc84da17.json'
    """
    workspace_id: str = MOCKED_WORKSPACE_ID
    workspace_build_id: str = MOCKED_WORKSPACE_REQUEST_ID_BUILD_SUCCESS["id"]
    workspace_abandon_id: str = MOCKED_WORKSPACE_REQUEST_ID_ABANDON["id"]
    workspace_requested_state: str = "abandoned"
    workspace_expected_state: str = "abandoned"

    with patch("pyavd._cv.client.workspace.uuid4", side_effect=[workspace_build_id.removeprefix("req-"), workspace_abandon_id.removeprefix("req-")]):
        workspace = CVWorkspace(id=workspace_id, requested_state=workspace_requested_state)
        await finalize_workspace_on_cv(workspace, cv_client, mocked_cvdevices(hostnames=["avd-ci-leaf1"]), [])

    assert workspace.state == workspace_expected_state


@pytest.mark.asyncio
@pytest.mark.parametrize("cv_client", [{"static_recording": True}], ids=["CV_CLIENT_STATIC_RECORDINGS"], indirect=True)
async def test_finalize_workspace_on_cv_deleted_state(cv_client: CVClient) -> None:
    """
    Test Workspace in deleted state.

    Exact test steps:
    -   description: Start Workspace build
        request: 'WorkspaceConfigSetRequest(value=WorkspaceConfig(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'),
            request=Request.START_BUILD, request_params=RequestParams(request_id='req-914310f3-08dd-4239-bd42-6d78bf781229')))'
        targeted_file: 'arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/1fdd6fcd02728621447eeb8a1d8c9cbfdd9201c9.json'

    -   description: Fetch build results
        request: 'WorkspaceStreamRequest(partial_eq_filter=[Workspace(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'))])'
        targeted_file: 'arista.workspace.v1.WorkspaceService/Subscribe/www.cv-prod-us-central1-c.arista.io/1560c66d73da2be39448d710f15853fb124b2548.json'

    -   description: Delete Workspace
        request: 'WorkspaceConfigDeleteRequest(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'))'
        targeted_file: 'arista.workspace.v1.WorkspaceConfigService/Delete/www.cv-prod-us-central1-c.arista.io/5cbea5d81be6faa13721aff0c3059bdfdfd188ce.json'
    """
    workspace_id: str = MOCKED_WORKSPACE_ID
    workspace_build_id: str = MOCKED_WORKSPACE_REQUEST_ID_BUILD_SUCCESS["id"]
    workspace_requested_state: str = "deleted"
    workspace_expected_state: str = "deleted"

    with patch("pyavd._cv.client.workspace.uuid4", side_effect=[workspace_build_id.removeprefix("req-")]):
        workspace = CVWorkspace(id=workspace_id, requested_state=workspace_requested_state)
        await finalize_workspace_on_cv(workspace, cv_client, mocked_cvdevices(hostnames=["avd-ci-leaf1"]), [])

    assert workspace.state == workspace_expected_state


@pytest.mark.asyncio
@pytest.mark.parametrize("cv_client", [{"static_recording": True}], ids=["CV_CLIENT_STATIC_RECORDINGS"], indirect=True)
@pytest.mark.parametrize(
    ("workspace_requested_state", "workspace_expected_state", "workspace_abandon_id", "logs_patterns", "expected_exception"),
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
        Exact test steps:
        -   description: Start Workspace build
            request: 'WorkspaceConfigSetRequest(value=WorkspaceConfig(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'),
                request=Request.START_BUILD, request_params=RequestParams(request_id='req-914310f3-08dd-4239-bd42-6d78b0000000')))'
            targeted_file: 'arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/094fa72d5437063770b645129730633334c7e4ed.json'

        -   description: Fetch build results
            request: 'WorkspaceStreamRequest(partial_eq_filter=[Workspace(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'))])'
            targeted_file: 'arista.workspace.v1.WorkspaceService/Subscribe/www.cv-prod-us-central1-c.arista.io/1560c66d73da2be39448d710f15853fb124b2548.json'

    2. Failing Workspace build for Workspace with requested_state == abandoned.
        Exact test steps:
        -   description: Start Workspace build
            request: 'WorkspaceConfigSetRequest(value=WorkspaceConfig(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'),
                request=Request.START_BUILD, request_params=RequestParams(request_id='req-914310f3-08dd-4239-bd42-6d78b0000000')))'
            targeted_file: 'arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/094fa72d5437063770b645129730633334c7e4ed.json'

        -   description: Fetch build results
            request: 'WorkspaceStreamRequest(partial_eq_filter=[Workspace(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'))])'
            targeted_file: 'arista.workspace.v1.WorkspaceService/Subscribe/www.cv-prod-us-central1-c.arista.io/1560c66d73da2be39448d710f15853fb124b2548.json'

        -   description: Abandon Workspace
            request: 'WorkspaceConfigSetRequest(value=WorkspaceConfig(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'),
                request=Request.ABANDON, request_params=RequestParams(request_id='req-b65374c1-4333-4c68-9b09-d753e8560609')))'
            targeted_file: 'arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/c3455eeb927146c3ba4e5fbb3d51b959fc84da17.json'
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
        await finalize_workspace_on_cv(workspace, cv_client, mocked_cvdevices(hostnames=["avd-ci-leaf1"]), [])

    assert workspace.state == workspace_expected_state

    # Assert that log messages match expected log patterns
    for expected_pattern in logs_patterns:
        assert any(re.search(re.compile(expected_pattern), str(record.message)) for record in caplog.records)

    # Assert that exception value contains all expected exception patterns
    for expected_pattern in exception_patterns:
        assert re.search(re.compile(expected_pattern), str(exception_info.value))


@pytest.mark.asyncio
@pytest.mark.parametrize("cv_client", [{"static_recording": True}], ids=["CV_CLIENT_STATIC_RECORDINGS"], indirect=True)
@pytest.mark.parametrize(("workspace_force_submission"), [pytest.param(False, id="UNFORCED"), pytest.param(True, id="FORCED")])
async def test_finalize_workspace_on_cv_submit_failed_unspecified(
    caplog: pytest.LogCaptureFixture,
    cv_client: CVClient,
    workspace_force_submission: bool,
) -> None:
    """
    Test building and submitting (forced and unforced) Workspace with streaming device.

    Specific use case where Workspace submission fails due to the UNSPECIFIED error.

    Exact test steps:
    -   description: Build Workspace
        request: 'WorkspaceConfigSetRequest(value=WorkspaceConfig(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'),
            request=Request.START_BUILD, request_params=RequestParams(request_id='req-914310f3-08dd-4239-bd42-6d78bf781229')))'
        targeted_file: 'arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/1fdd6fcd02728621447eeb8a1d8c9cbfdd9201c9.json'

    -   description: Fetch build results
        request: 'WorkspaceStreamRequest(partial_eq_filter=[Workspace(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'))])'
        targeted_file: 'arista.workspace.v1.WorkspaceService/Subscribe/www.cv-prod-us-central1-c.arista.io/1560c66d73da2be39448d710f15853fb124b2548.json'

    -   description: Submit Workspace (UNFORCED use case)
        request: 'WorkspaceConfigSetRequest(value=WorkspaceConfig(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'),
            request=Request.SUBMIT, request_params=RequestParams(request_id='req-725669d2-2ec5-4572-8c6a-453b1fea27c0')))'
        targeted_file: 'arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/0bc6d413bab676fd90504b4ba0d2a81d8fa54e03.json'

    -   description: Submit Workspace (FORCED use case)
        request: 'WorkspaceConfigSetRequest(value=WorkspaceConfig(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'),
            request=Request.SUBMIT_FORCE, request_params=RequestParams(request_id='req-725669d2-2ec5-4572-8c6a-453b1fea27c0')))'
        targeted_file: 'arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/a8201f6621fc75b37306a45e91ecf1db776ac617.json'

    -   description: Fetch submit results
        request: 'WorkspaceStreamRequest(partial_eq_filter=[Workspace(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'))])'
        targeted_file: 'arista.workspace.v1.WorkspaceService/Subscribe/www.cv-prod-us-central1-c.arista.io/1560c66d73da2be39448d710f15853fb124b2548.json'
    """
    warnings: list[Any] = []
    exception_patterns = [
        "Failed to submit workspace ws-cbf7c7ea-a57c-481d-b96b-97c12856395e: Response\\(status=ResponseStatus.FAIL, "
        "message='Unknown exception faced', code=ResponseCode.UNSPECIFIED\\)"
    ]
    cv_workspace = CVWorkspace(
        name=MOCKED_WORKSPACE_NAME,
        description=MOCKED_WORKSPACE_DESCRIPTION,
        id=MOCKED_WORKSPACE_ID,
        requested_state=MOCKED_WORKSPACE_REQUESTED_STATE_SUBMITTED,
        force=workspace_force_submission,
    )

    with (
        caplog.at_level(INFO),
        patch(
            "pyavd._cv.client.workspace.uuid4",
            side_effect=[
                MOCKED_WORKSPACE_REQUEST_ID_BUILD_SUCCESS["id"].removeprefix("req-"),
                MOCKED_WORKSPACE_REQUEST_ID_SUBMIT_FAILURE_OTHER_EXCEPTION["id"].removeprefix("req-"),
            ],
        ),
        pytest.raises(CVWorkspaceSubmitFailed) as exception_info,
    ):
        await finalize_workspace_on_cv(
            workspace=cv_workspace,
            cv_client=cv_client,
            devices=[
                CVDevice(
                    hostname="avd-ci-leaf2",
                    serial_number="50:00:00:d5:5d:c0",
                    system_mac_address="B51AA89B6E51E89E1422107EDE3A9438",
                    _exists_on_cv=True,
                    _streaming=True,
                )
            ],
            warnings=warnings,
        )

    # Assert that exception value contains all expected exception patterns
    for expected_pattern in exception_patterns:
        assert re.search(re.compile(expected_pattern), str(exception_info.value))

    # Assert number of returned warnings
    assert len(warnings) == 0

    # Assert returned workspace object
    assert cv_workspace.name == MOCKED_WORKSPACE_NAME
    assert cv_workspace.description == MOCKED_WORKSPACE_DESCRIPTION
    assert cv_workspace.id == MOCKED_WORKSPACE_ID
    assert cv_workspace.requested_state == MOCKED_WORKSPACE_REQUESTED_STATE_SUBMITTED
    assert cv_workspace.state == "submit failed"


@pytest.mark.asyncio
@pytest.mark.parametrize("cv_client", [{"static_recording": True}], ids=["CV_CLIENT_STATIC_RECORDINGS"], indirect=True)
@pytest.mark.parametrize(("workspace_force_submission"), [pytest.param(False, id="UNFORCED"), pytest.param(True, id="FORCED")])
async def test_deploy_to_cv_streaming_device_failure(
    caplog: pytest.LogCaptureFixture,
    cv_client: CVClient,
    workspace_force_submission: bool,
) -> None:
    """
    Test building and submitting Workspace (both forced and unforced) with streaming device.

    Specific use case where Workspace submission fails due to streaming status changing from ACTIVE to INACTIVE right before submission.

    Exact test steps:
    -   description: Start Workspace build
        request: 'WorkspaceConfigSetRequest(value=WorkspaceConfig(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'),
            request=Request.START_BUILD, request_params=RequestParams(request_id='req-914310f3-08dd-4239-bd42-6d78bf781229')))'
        targeted_file: 'arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/1fdd6fcd02728621447eeb8a1d8c9cbfdd9201c9.json''

    -   description: Fetch build status
        request: 'WorkspaceStreamRequest(partial_eq_filter=[Workspace(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'))])'
        targeted_file: 'arista.workspace.v1.WorkspaceService/Subscribe/www.cv-prod-us-central1-c.arista.io/1560c66d73da2be39448d710f15853fb124b2548.json'

    -   description: Submit Workspace (UNFORCED use case)
        request: 'WorkspaceConfigSetRequest(value=WorkspaceConfig(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'),
            request=Request.SUBMIT, request_params=RequestParams(request_id='req-18654b6a-9f75-4a57-878d-d40d73701238')))'
        targeted_file: 'arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/54f25797c08b0d4ca2c4497e73b4afbfd2959b6f.json'

    -   description: Submit Workspace (FORCED use case)
        request: 'WorkspaceConfigSetRequest(value=WorkspaceConfig(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'),
            request=Request.SUBMIT_FORCE, request_params=RequestParams(request_id='req-18654b6a-9f75-4a57-878d-d40d73701238')))''
        targeted_file: 'arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/a081b80838db991bd8bcd669f64f7aa24c00b715.json'

    -   description: Fetch submit status
        request: 'WorkspaceStreamRequest(partial_eq_filter=[Workspace(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'))])'
        targeted_file: 'arista.workspace.v1.WorkspaceService/Subscribe/www.cv-prod-us-central1-c.arista.io/1560c66d73da2be39448d710f15853fb124b2548.json'
    """
    result = DeployToCvResult(
        workspace=CVWorkspace(
            name=MOCKED_WORKSPACE_NAME,
            description=MOCKED_WORKSPACE_DESCRIPTION,
            id=MOCKED_WORKSPACE_ID,
            requested_state=MOCKED_WORKSPACE_REQUESTED_STATE_SUBMITTED,
            force=workspace_force_submission,
        )
    )

    with (
        caplog.at_level(INFO),
        patch(
            "pyavd._cv.client.workspace.uuid4",
            side_effect=[
                MOCKED_WORKSPACE_REQUEST_ID_BUILD_SUCCESS["id"].removeprefix("req-"),
                MOCKED_WORKSPACE_REQUEST_ID_SUBMIT_FAILURE_INACTIVE_DEVICES["id"].removeprefix("req-"),
            ],
        ),
        pytest.raises(CVWorkspaceSubmitFailedInactiveDevices) as exception_info,
    ):
        await finalize_workspace_on_cv(
            workspace=result.workspace,
            cv_client=cv_client,
            devices=[
                CVDevice(
                    hostname="avd-ci-leaf2",
                    serial_number="50:00:00:d5:5d:c0",
                    system_mac_address="B51AA89B6E51E89E1422107EDE3A9438",
                    _exists_on_cv=True,
                    _streaming=True,
                )
            ],
            warnings=result.warnings,
        )

    # Assert that exception value contains all expected exception patterns
    assert re.search(re.compile("Failed to submit CloudVision Workspace due to the presence of inactive devices. "), str(exception_info.value))

    # Assess result
    assert not result.failed

    # Assert number of returned warnings
    assert len(result.warnings) == 0

    # Assert returned workspace object
    assert result.workspace.name == MOCKED_WORKSPACE_NAME
    assert result.workspace.description == MOCKED_WORKSPACE_DESCRIPTION
    assert result.workspace.id == MOCKED_WORKSPACE_ID
    assert result.workspace.requested_state == MOCKED_WORKSPACE_REQUESTED_STATE_SUBMITTED
    assert result.workspace.force == workspace_force_submission
    assert result.workspace.state == "submit failed"


@pytest.mark.asyncio
@pytest.mark.parametrize("cv_client", [{"static_recording": True}], ids=["CV_CLIENT_STATIC_RECORDINGS"], indirect=True)
async def test_deploy_to_cv_non_streaming_device_unforced(
    caplog: pytest.LogCaptureFixture,
    cv_client: CVClient,
) -> None:
    """
    Test building and submitting Workspace with non-streaming device without forcing.

    Exact test steps:
    -   description: Build Workspace
        request: 'WorkspaceConfigSetRequest(value=WorkspaceConfig(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'),
            request=Request.START_BUILD, request_params=RequestParams(request_id='req-914310f3-08dd-4239-bd42-6d78bf781229')))'
        targeted_file: 'arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/1fdd6fcd02728621447eeb8a1d8c9cbfdd9201c9.json'

    -   description: Fetch build results
        request: 'WorkspaceStreamRequest(partial_eq_filter=[Workspace(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'))])'
        targeted_file: 'arista.workspace.v1.WorkspaceService/Subscribe/www.cv-prod-us-central1-c.arista.io/1560c66d73da2be39448d710f15853fb124b2548.json'

    -   description: Submit Workspace
        request: 'WorkspaceConfigSetRequest(value=WorkspaceConfig(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'),
            request=Request.SUBMIT, request_params=RequestParams(request_id='req-18654b6a-9f75-4a57-878d-d40d73701238')))'
        targeted_file: 'arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/54f25797c08b0d4ca2c4497e73b4afbfd2959b6f.json'

    -   description: Fetch submit results
        request: 'WorkspaceStreamRequest(partial_eq_filter=[Workspace(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'))])'
        targeted_file: 'arista.workspace.v1.WorkspaceService/Subscribe/www.cv-prod-us-central1-c.arista.io/1560c66d73da2be39448d710f15853fb124b2548.json'
    """
    result = DeployToCvResult(
        workspace=CVWorkspace(
            name=MOCKED_WORKSPACE_NAME,
            description=MOCKED_WORKSPACE_DESCRIPTION,
            id=MOCKED_WORKSPACE_ID,
            requested_state=MOCKED_WORKSPACE_REQUESTED_STATE_SUBMITTED,
            force=False,
        )
    )

    with (
        caplog.at_level(INFO),
        patch(
            "pyavd._cv.client.workspace.uuid4",
            side_effect=[
                MOCKED_WORKSPACE_REQUEST_ID_BUILD_SUCCESS["id"].removeprefix("req-"),
                MOCKED_WORKSPACE_REQUEST_ID_SUBMIT_FAILURE_INACTIVE_DEVICES["id"].removeprefix("req-"),
            ],
        ),
        pytest.raises(CVWorkspaceSubmitFailedInactiveDevices) as exception_info,
    ):
        await finalize_workspace_on_cv(
            workspace=result.workspace,
            cv_client=cv_client,
            devices=[
                CVDevice(
                    hostname="avd-ci-leaf1",
                    serial_number="50:00:00:72:8b:31",
                    system_mac_address="13C20F1EDCCED2D85F6DB2FB9E3AC5B6",
                    _exists_on_cv=True,
                    _streaming=False,
                )
            ],
            warnings=result.warnings,
        )

    # Assert that exception value contains all expected exception patterns
    for expected_pattern in ["Failed to submit CloudVision Workspace due to the presence of inactive devices: \\['avd-ci-leaf1.*"]:
        assert re.search(re.compile(expected_pattern), str(exception_info.value))

    # Assess result
    assert not result.failed

    # Assert number of returned warnings
    assert len(result.warnings) == 1
    # Assert that updated warnings match expected warning patterns
    for expected_pattern in ["Inactive devices present: \\['avd-ci-leaf1.*"]:
        assert any(re.search(re.compile(expected_pattern), str(warning_item)) for warning_item in result.warnings)

    # Assert returned workspace object
    assert result.workspace.name == MOCKED_WORKSPACE_NAME
    assert result.workspace.description == MOCKED_WORKSPACE_DESCRIPTION
    assert result.workspace.id == MOCKED_WORKSPACE_ID
    assert result.workspace.requested_state == MOCKED_WORKSPACE_REQUESTED_STATE_SUBMITTED
    assert not result.workspace.force
    assert result.workspace.state == "submit failed"


@pytest.mark.asyncio
@pytest.mark.parametrize("cv_client", [{"static_recording": True}], ids=["CV_CLIENT_STATIC_RECORDINGS"], indirect=True)
async def test_deploy_to_cv_non_streaming_device_forced(
    caplog: pytest.LogCaptureFixture,
    cv_client: CVClient,
) -> None:
    """
    Test building and submitting Workspace with non-streaming device with forcing.

    Exact test steps:
    -   description: Build Workspace
        request: 'WorkspaceConfigSetRequest(value=WorkspaceConfig(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'),
            request=Request.START_BUILD, request_params=RequestParams(request_id='req-914310f3-08dd-4239-bd42-6d78bf781229')))'
        targeted_file: 'arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/1fdd6fcd02728621447eeb8a1d8c9cbfdd9201c9.json'

    -   description: Fetch build results
        request: 'WorkspaceStreamRequest(partial_eq_filter=[Workspace(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'))])'
        targeted_file: 'arista.workspace.v1.WorkspaceService/Subscribe/www.cv-prod-us-central1-c.arista.io/1560c66d73da2be39448d710f15853fb124b2548.json'

    -   description: Submit Workspace
        request: 'WorkspaceConfigSetRequest(value=WorkspaceConfig(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'),
            request=Request.SUBMIT_FORCE, request_params=RequestParams(request_id='req-b8f4e511-58de-4afe-99f0-b75abf980131')))'
        targeted_file: 'arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/47049c8a6b520f110540f81bcd892ba0e4954908.json'

    -   description: Fetch submit results
        request: 'WorkspaceStreamRequest(partial_eq_filter=[Workspace(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'))])'
        targeted_file: 'arista.workspace.v1.WorkspaceService/Subscribe/www.cv-prod-us-central1-c.arista.io/1560c66d73da2be39448d710f15853fb124b2548.json'
    """
    with (
        caplog.at_level(INFO),
        patch(
            "pyavd._cv.client.workspace.uuid4",
            side_effect=[
                MOCKED_WORKSPACE_REQUEST_ID_BUILD_SUCCESS["id"].removeprefix("req-"),
                # Live attempt to force-submit Workspace targeting single non-streaming device returns ResponseStatus.SUCCESS.
                MOCKED_WORKSPACE_REQUEST_ID_SUBMIT_SUCCESS["id"].removeprefix("req-"),
            ],
        ),
        does_not_raise(),
    ):
        result = DeployToCvResult(
            workspace=CVWorkspace(
                name=MOCKED_WORKSPACE_NAME,
                description=MOCKED_WORKSPACE_DESCRIPTION,
                id=MOCKED_WORKSPACE_ID,
                requested_state=MOCKED_WORKSPACE_REQUESTED_STATE_SUBMITTED,
                force=True,
            )
        )

        await finalize_workspace_on_cv(
            workspace=result.workspace,
            cv_client=cv_client,
            devices=[
                CVDevice(
                    hostname="avd-ci-leaf1",
                    serial_number="50:00:00:72:8b:31",
                    system_mac_address="13C20F1EDCCED2D85F6DB2FB9E3AC5B6",
                    _exists_on_cv=True,
                    _streaming=False,
                )
            ],
            warnings=result.warnings,
        )

    # Assess result
    assert not result.failed
    # Assert number of returned warnings
    assert len(result.warnings) == 1
    # Assert that updated warnings match expected warning patterns
    for expected_pattern in ["Inactive devices present: \\['avd-ci-leaf1.*"]:
        assert any(re.search(re.compile(expected_pattern), str(warning_item)) for warning_item in result.warnings)

    # Assert returned workspace object
    assert result.workspace.name == MOCKED_WORKSPACE_NAME
    assert result.workspace.description == MOCKED_WORKSPACE_DESCRIPTION
    assert result.workspace.id == MOCKED_WORKSPACE_ID
    assert result.workspace.requested_state == MOCKED_WORKSPACE_REQUESTED_STATE_SUBMITTED
    assert result.workspace.force
    assert result.workspace.state == MOCKED_WORKSPACE_REQUESTED_STATE_SUBMITTED


@pytest.mark.asyncio
@pytest.mark.parametrize("cv_client", [{"static_recording": True, "cv_version": "CVaaS"}], ids=["CV_CLIENT_STATIC_RECORDINGS"], indirect=True)
@pytest.mark.parametrize(("workspace_force_submission"), [pytest.param(False, id="UNFORCED"), pytest.param(True, id="FORCED")])
async def test_deploy_to_cv(
    caplog: pytest.LogCaptureFixture,
    cv_client: CVClient,
    workspace_force_submission: bool,
) -> None:
    """
    Test full functionality of the deploy_to_cv by building and submitting (both forced and unforced) Workspace with a single streaming device.

    Exact test steps:
    -   description: Fethc Workspace status
        request: 'WorkspaceRequest(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'), time=None)'
        targeted_file: 'arista.workspace.v1.WorkspaceService/GetOne/www.cv-prod-us-central1-c.arista.io/a996cf0f4bc694971e5d4069f481faaba80f68b2.json'

    -   description: Create Workspace
        request: 'WorkspaceConfigSetRequest(value=WorkspaceConfig(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'),
            display_name='MOCKED_WS_NAME', description='MOCKED_WS_DESCRIPTION'))'
        targeted_file: 'arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/ce73310ec5154d57ac888fc8f93d69893962d804.json'

    -   description: Fetch device status
        request: 'DeviceStreamRequest(partial_eq_filter=[Device(key=DeviceKey(device_id=None), hostname='avd-ci-leaf2', system_mac_address=None)],
            time=TimeBounds(start=None, end=None))'
        targeted_file: 'arista.inventory.v1.DeviceService/GetAll/www.cv-prod-us-central1-c.arista.io/effc85b759a4d35ba98ae7c22bcef828c070752d.json'

    -   description: Fetch I&T Studio inputs
        request: 'InputsStreamRequest(partial_eq_filter=[Inputs(key=InputsKey(studio_id='TOPOLOGY', workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'))],
            time=None)'
        targeted_file: 'arista.studio.v1.InputsService/GetAll/www.cv-prod-us-central1-c.arista.io/0ab698a68a7f9f86eeda70fba362f57cb2f07fc4.json'

    -   description: Create configlet
        request: 'ConfigletConfigSetSomeRequest(values=[ConfigletConfig(key=ConfigletKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e',
            configlet_id='avd-B51AA89B6E51E89E1422107EDE3A9438'), display_name='TEST_CONFIGLET_NAME', description='Configuration created and
            uploaded by AVD for avd-ci-leaf2', body='alias test test')])'
        targeted_file: 'arista.configlet.v1.ConfigletConfigService/SetSome/www.cv-prod-us-central1-c.arista.io/9928854663237cf59f5710079cb64befccffd7cc.json'

    -   description: Fetch Configlet assignments
        request: 'ConfigletAssignmentStreamRequest(partial_eq_filter=[ConfigletAssignment(key=ConfigletAssignmentKey(workspace_id=
            'ws-cbf7c7ea-a57c-481d-b96b-97c12856395e', configlet_assignment_id='avd-configlets'))], time=TimeBounds(start=None, end=None))'
        targeted_file: 'arista.configlet.v1.ConfigletAssignmentService/GetAll/www.cv-prod-us-central1-c.arista.io/0462b04aed494937b07702371f123831a4e81036.json'

    -   description: Fetch configlets assignments
        request: Too long. Please consult JSON file for details.
        targeted_file: 'arista.configlet.v1.ConfigletAssignmentService/GetAll/www.cv-prod-us-central1-c.arista.io/15b2c867c1abf9b0d425ca76fa4327294c18c376.json'

    -   description: Build Workspace
        request: 'WorkspaceConfigSetRequest(value=WorkspaceConfig(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'),
            request=Request.START_BUILD, request_params=RequestParams(request_id='req-914310f3-08dd-4239-bd42-6d78bf781229')))'
        targeted_file: 'arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/1fdd6fcd02728621447eeb8a1d8c9cbfdd9201c9.json'

    -   description: Fetch build results
        request: 'WorkspaceStreamRequest(partial_eq_filter=[Workspace(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'))])'
        targeted_file: 'arista.workspace.v1.WorkspaceService/Subscribe/www.cv-prod-us-central1-c.arista.io/1560c66d73da2be39448d710f15853fb124b2548.json'

    -   description: Submit Workspace (UNFORCED use case)
        request: 'WorkspaceConfigSetRequest(value=WorkspaceConfig(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'),
            request=Request.SUBMIT, request_params=RequestParams(request_id='req-b8f4e511-58de-4afe-99f0-b75abf980131')))'
        targeted_file: 'arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/ba83e98eab07691e8b079958618ab2973822bfe8.json'

    -   description: Submit Workspace (FORCED use case)
        request: 'WorkspaceConfigSetRequest(value=WorkspaceConfig(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'),
            request=Request.SUBMIT_FORCE, request_params=RequestParams(request_id='req-b8f4e511-58de-4afe-99f0-b75abf980131')))'
        targeted_file: 'arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/47049c8a6b520f110540f81bcd892ba0e4954908.json'

    -   description: Fetch submit results
        request: 'WorkspaceStreamRequest(partial_eq_filter=[Workspace(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'))])'
        targeted_file: 'arista.workspace.v1.WorkspaceService/Subscribe/www.cv-prod-us-central1-c.arista.io/1560c66d73da2be39448d710f15853fb124b2548.json'
    """
    with (
        caplog.at_level(INFO),
        does_not_raise(),
        patch(
            "pyavd._cv.client.workspace.uuid4",
            side_effect=[
                MOCKED_WORKSPACE_REQUEST_ID_BUILD_SUCCESS["id"].removeprefix("req-"),
                MOCKED_WORKSPACE_REQUEST_ID_SUBMIT_SUCCESS["id"].removeprefix("req-"),
            ],
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
                name=MOCKED_WORKSPACE_NAME,
                description=MOCKED_WORKSPACE_DESCRIPTION,
                id=MOCKED_WORKSPACE_ID,
                requested_state=MOCKED_WORKSPACE_REQUESTED_STATE_SUBMITTED,
                force=workspace_force_submission,
            ),
            configs=[
                CVEosConfig(
                    file=temp_configlet_file.name, device=next(iter(mocked_cvdevices(hostnames=["avd-ci-leaf2"]))), configlet_name="TEST_CONFIGLET_NAME"
                )
            ],
        )

    # Assess result
    assert not result.failed

    # Assert number of returned warnings
    assert len(result.warnings) == 0

    # Assert number of returned errors
    assert len(result.errors) == 0

    # Assert returned workspace object
    assert result.workspace.name == MOCKED_WORKSPACE_NAME
    assert result.workspace.description == MOCKED_WORKSPACE_DESCRIPTION
    assert result.workspace.id == MOCKED_WORKSPACE_ID
    assert result.workspace.requested_state == MOCKED_WORKSPACE_REQUESTED_STATE_SUBMITTED
    assert result.workspace.force == workspace_force_submission
    assert result.workspace.state == MOCKED_WORKSPACE_REQUESTED_STATE_SUBMITTED
