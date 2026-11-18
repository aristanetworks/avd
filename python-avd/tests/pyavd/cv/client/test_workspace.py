# Copyright (c) 2024-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import asyncio
import re
from asyncio.exceptions import TimeoutError as AsyncioTimeoutError
from collections import defaultdict
from contextlib import nullcontext as does_not_raise
from logging import DEBUG
from typing import TYPE_CHECKING, Any
from unittest.mock import call, patch

import pytest

from pyavd._cv.api.arista.workspace.v1 import (
    Request,
    Response,
    Responses,
    ResponseStatus,
    Workspace,
    WorkspaceConfig,
    WorkspaceKey,
    WorkspaceState,
    WorkspaceStreamResponse,
)
from pyavd._cv.client.exceptions import CVTimeoutError, CVWorkspaceFailed
from pyavd._cv.workflows.finalize_workspace_on_cv import build_workspace_on_cv
from tests.pyavd.cv import mockery
from tests.pyavd.cv.constants import (
    MOCKED_WORKSPACE_B_ID,
    MOCKED_WORKSPACE_B_REQUEST_ID_REBASE_1_SUCCESS,
    MOCKED_WORKSPACE_C_BUILD_REQUEST_ID_1,
    MOCKED_WORKSPACE_C_BUILD_REQUEST_ID_2,
    MOCKED_WORKSPACE_C_ID,
    MOCKED_WORKSPACE_ID,
)

if TYPE_CHECKING:
    from collections.abc import AsyncIterator

    from pyavd._cv.client import CVClient


@pytest.mark.asyncio
@pytest.mark.parametrize("cv_client", [{"static_recording": True}], ids=["CV_CLIENT_STATIC_RECORDINGS"], indirect=True)
async def test_wait_for_workspace_state_stream_closes(cv_client: CVClient) -> None:
    """
    Test unsuccessful attempt to wait for a Workspace to reach `rolled_back` state where Stream completes without Workspace reaching the desired state.

    Exact test steps:
    -   description: Fetch Workspace status
        request: 'WorkspaceStreamRequest(partial_eq_filter=[Workspace(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'))])'
        targeted_file: 'arista.workspace.v1.WorkspaceService/Subscribe/www.cv-prod-us-central1-c.arista.io/1560c66d73da2be39448d710f15853fb124b2548.json'
    """
    with pytest.raises(CVWorkspaceFailed, match=r"Workspace 'ws-cbf7c7ea-a57c-481d-b96b-97c12856395e' has not reached desired state 'rolled_back'."):
        _ = await cv_client.wait_for_workspace_state(workspace_id=MOCKED_WORKSPACE_ID, state="rolled_back")


@pytest.mark.asyncio
@pytest.mark.parametrize("cv_client", [{"static_recording": True}], ids=["CV_CLIENT_STATIC_RECORDINGS"], indirect=True)
async def test_wait_for_workspace_state_timeout(cv_client: CVClient) -> None:
    """
    Test unsuccessful attempt to wait for a Workspace to reach `rolled_back` state where timeout expires before Workspace reaches the desired state.

    This is to replicate the following real events (high level):
    -  `grpclib.client.Stream` object fetches messages by removing them from the `asyncio` queue
    -  If queue is empty for <timeout> seconds, `asyncio.exceptions.CancelledError` is raised
    -  This exception is caught by `grpclib` client
    -  `grpclib` client then raises `asyncio.TimeoutError("Deadline exceeded")`
    -  `pyavd`'s `async_decorator` intercepts this exception and raises `CVTimeoutError`
    """

    async def async_iterator_with_timeout(timeout: float = 1.0) -> AsyncIterator[Any]:
        """Async iterator that yields a message and waits for the specified 'timeout' time before raising a TimeoutError."""
        yield "Single message that you will get before I timeout and raise asyncio.TimeoutError."
        await asyncio.sleep(int(timeout))
        msg = "Deadline exceeded"
        raise AsyncioTimeoutError(msg)

    with (
        pytest.raises(
            CVTimeoutError,
            match=r".*Deadline exceeded.*'workspace_id': 'ws-cbf7c7ea-a57c-481d-b96b-97c12856395e', 'state': 'rolled_back', 'timeout': 1.0.*",
        ),
        patch(
            "pyavd._cv.client.workspace.WorkspaceServiceStub.subscribe",
            return_value=async_iterator_with_timeout(),
        ),
    ):
        _ = await cv_client.wait_for_workspace_state(workspace_id=MOCKED_WORKSPACE_ID, state="rolled_back", timeout=1.0)


@pytest.mark.asyncio
@pytest.mark.parametrize("cv_client", [{"static_recording": True}], ids=["CV_CLIENT_STATIC_RECORDINGS"], indirect=True)
async def test_rebase_workspace(cv_client: CVClient) -> None:
    """
    Test rebasing of the Workspace.

    Exact test steps:
    -   description: Request rebasing of the Workspace
        request: WorkspaceConfigSetRequest(value=WorkspaceConfig(key=WorkspaceKey(workspace_id='ws-833a9e6b-9cc0-484b-a5bb-a57f7fa1438f'), "
            "request=Request.REBASE, request_params=RequestParams(request_id='req-73d17f5a-3db7-4527-ae9a-e43ca99d983c')))'
        targeted_file: 'arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/6343b1d9dd797d90a6b6544c468eeb02d3c5daf7.json'
    """
    with (
        patch(
            "pyavd._cv.client.workspace.uuid4",
            side_effect=[MOCKED_WORKSPACE_B_REQUEST_ID_REBASE_1_SUCCESS["id"].removeprefix("req-")],
        ),
    ):
        response_workspace_config = await cv_client.rebase_workspace(workspace_id=MOCKED_WORKSPACE_B_ID)

    assert isinstance(response_workspace_config, WorkspaceConfig)


@pytest.mark.asyncio
@pytest.mark.parametrize("terminal_status", [ResponseStatus.SUCCESS, ResponseStatus.FAIL])
async def test_wait_for_workspace_response_ignores_non_terminal_statuses(cv_client: CVClient, terminal_status: ResponseStatus) -> None:
    """Test that workspace response polling waits for a known terminal status."""
    request_id = "req-test"
    unknown_status = ResponseStatus.try_value(99)

    async def workspace_responses() -> AsyncIterator[WorkspaceStreamResponse]:
        for status in (ResponseStatus.IN_PROGRESS, unknown_status, terminal_status):
            yield WorkspaceStreamResponse(
                value=Workspace(
                    key=WorkspaceKey(workspace_id=MOCKED_WORKSPACE_ID),
                    responses=Responses(values={request_id: Response(status=status)}),
                ),
            )

    with patch(
        "pyavd._cv.client.workspace.WorkspaceServiceStub.subscribe",
        return_value=workspace_responses(),
    ):
        response, workspace = await cv_client.wait_for_workspace_response(
            workspace_id=MOCKED_WORKSPACE_ID,
            request_id=request_id,
        )

    assert response.status == terminal_status
    assert workspace.key.workspace_id == MOCKED_WORKSPACE_ID


@pytest.mark.asyncio
@pytest.mark.parametrize("cv_client", [{"static_recording": True}], ids=["CV_CLIENT_STATIC_RECORDINGS"], indirect=True)
@pytest.mark.parametrize(
    ("max_retries", "expected_attempts"),
    [
        pytest.param(0, 1, id="NO_RETRIES"),
        pytest.param(1, 2, id="ONE_RETRY"),
        pytest.param(5, 2, id="STOPS_EARLY_WHEN_NO_BUILD_NEEDED"),
    ],
)
async def test_rebuild_workspace(
    caplog: pytest.LogCaptureFixture,
    monkeypatch: pytest.MonkeyPatch,
    cv_client: CVClient,
    max_retries: int,
    expected_attempts: int,
) -> None:
    """
    Test rebuild of the Workspace when CloudVision tags are asynchronously updated in the Workspace while initial build request is being processed.

    Specific use cases:
    1. No retries: Return the initial successful build response with Workspace.needs_build set to True.
    2. One retry: Return the second successful build response with Workspace.needs_build set to False.
    3. Five retries: Stop after the second build when Workspace.needs_build is False.

    Exact test steps:
    -   description: Request build of the Workspace
        request: 'WorkspaceConfigSetRequest(value=WorkspaceConfig(key=WorkspaceKey(workspace_id='ws-1740c9fa-3fc1-4bde-a979-9c40a3f33c16'),
            request=Request.START_BUILD, request_params=RequestParams(request_id='req-792f8bc7-3994-4844-ad57-07f2ed27248e')))'
        targeted_file: 'arista.workspace.v1.WorkspaceConfigService/Set/www.cv-staging.corp.arista.io/4953167a7364d3f5b3c2b426a5a420ac7accfdd6_1.json'

    -   description: Fetch build results
        request: 'WorkspaceStreamRequest(partial_eq_filter=[Workspace(key=WorkspaceKey(workspace_id='ws-1740c9fa-3fc1-4bde-a979-9c40a3f33c16'))])'
        targeted_file: 'arista.workspace.v1.WorkspaceService/Subscribe/www.cv-staging.corp.arista.io/c9adecc8b16d037077f8428325642c0d41c4da0e_1.json'

    -   description: Request second build of the Workspace
        request: 'WorkspaceConfigSetRequest(value=WorkspaceConfig(key=WorkspaceKey(workspace_id='ws-1740c9fa-3fc1-4bde-a979-9c40a3f33c16'),
            request=Request.START_BUILD, request_params=RequestParams(request_id='req-01c8f794-31f6-43ae-b759-5b61074b0e9c')))'
        targeted_file: 'arista.workspace.v1.WorkspaceConfigService/Set/www.cv-staging.corp.arista.io/53576309820ba5067e0fdbb63c1e3d1a76f0e236_1.json'

    -   description: Fetch build results
        request: 'WorkspaceStreamRequest(partial_eq_filter=[Workspace(key=WorkspaceKey(workspace_id='ws-1740c9fa-3fc1-4bde-a979-9c40a3f33c16'))])'
        targeted_file: 'arista.workspace.v1.WorkspaceService/Subscribe/www.cv-staging.corp.arista.io/c9adecc8b16d037077f8428325642c0d41c4da0e_2.json'
    """
    expected_requests = [MOCKED_WORKSPACE_C_BUILD_REQUEST_ID_1, MOCKED_WORKSPACE_C_BUILD_REQUEST_ID_2][:expected_attempts]
    expected_final_request = expected_requests[-1]
    with (
        caplog.at_level(DEBUG),
        does_not_raise(),
        patch(
            "pyavd._cv.client.workspace.uuid4",
            side_effect=[
                MOCKED_WORKSPACE_C_BUILD_REQUEST_ID_1["id"].removeprefix("req-"),
                MOCKED_WORKSPACE_C_BUILD_REQUEST_ID_2["id"].removeprefix("req-"),
            ],
        ) as mock_uuid4,
        patch.object(cv_client, "build_workspace", wraps=cv_client.build_workspace) as mock_build,
        patch.object(cv_client, "wait_for_workspace_response", wraps=cv_client.wait_for_workspace_response) as mock_wait,
        monkeypatch.context() as test_patch,
    ):
        # Enable mode where recording files are unique for every repetitive call
        test_patch.setenv("UNIQUE_FILES_FOR_REPETITIVE_CALLS", "yes")
        # Mock default production cluster with staging (as recordings are collected on staging)
        test_patch.setattr(cv_client._channel, "_host", "www.cv-staging.corp.arista.io")
        # Reset the shared counter so each test case starts with recording suffix _1
        test_patch.setattr(mockery, "RECORDING_FILE_CALLS_PER_REQUEST_TRACKER", defaultdict(int))
        build_result, cv_workspace = await build_workspace_on_cv(workspace_id=MOCKED_WORKSPACE_C_ID, cv_client=cv_client, max_retries=max_retries)

    assert mock_uuid4.call_count == expected_attempts
    assert mock_build.await_args_list == [call(workspace_id=MOCKED_WORKSPACE_C_ID)] * expected_attempts
    assert mock_wait.await_args_list == [call(workspace_id=MOCKED_WORKSPACE_C_ID, request_id=request["id"]) for request in expected_requests]

    assert isinstance(build_result, Response)
    assert build_result.status == expected_final_request["status"]
    assert build_result.code == expected_final_request["code"]
    assert build_result.message == expected_final_request["message"]
    assert build_result.request_type == Request.START_BUILD
    assert build_result.start_time < build_result.end_time

    assert isinstance(cv_workspace, Workspace)
    assert cv_workspace.key.workspace_id == MOCKED_WORKSPACE_C_ID
    assert cv_workspace.last_build_id == expected_final_request["id"]
    assert cv_workspace.state == WorkspaceState.PENDING
    assert cv_workspace.needs_build is (expected_attempts == 1)
    assert cv_workspace.needs_rebase is False
    assert cv_workspace.display_name == "AVD_CI_PYTEST_WS_REBUILD"
    assert cv_workspace.cc_ids.values == []
    assert len(cv_workspace.responses.values) == expected_attempts
    assert build_result is cv_workspace.responses.values[expected_final_request["id"]]
    for request in expected_requests:
        response = cv_workspace.responses.values[request["id"]]
        assert response.status == request["status"]
        assert response.code == request["code"]
        assert response.message == request["message"]
        assert response.request_type == Request.START_BUILD
        assert response.start_time < response.end_time

    # Assert that log messages match expected log patterns
    log_patterns = [
        f"wait_for_workspace_response: Got response for request '{request['id']}': .*{re.escape(request['message'])}" for request in expected_requests
    ]
    if expected_attempts > 1:
        log_patterns.append(
            rf"build_workspace_on_cv: Workspace {MOCKED_WORKSPACE_C_ID} still needs a build after a successful build response\. "
            rf"Starting build attempt 2/{max_retries + 1}\."
        )
    for expected_pattern in log_patterns:
        assert any(re.search(re.compile(expected_pattern), str(record.message)) for record in caplog.records)
