# Copyright (c) 2024-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import asyncio
from asyncio.exceptions import TimeoutError as AsyncioTimeoutError
from typing import TYPE_CHECKING, Any
from unittest.mock import patch

import pytest

from pyavd._cv.api.arista.subscriptions import Operation
from pyavd._cv.api.arista.workspace.v1 import WorkspaceConfig, WorkspaceStreamResponse
from pyavd._cv.client.exceptions import CVTimeoutError, CVWorkspaceFailed
from tests.pyavd.cv.constants import (
    MOCKED_WORKSPACE_B_ID,
    MOCKED_WORKSPACE_B_REQUEST_ID_REBASE_1_SUCCESS,
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
    -  The gRPC stream object fetches messages by removing them from the `asyncio` queue
    -  If queue is empty for <timeout> seconds, `asyncio.exceptions.CancelledError` is raised
    -  This exception is caught by the gRPC client
    -  The gRPC client then raises `asyncio.TimeoutError("Deadline exceeded")`
    -  `pyavd`'s `async_decorator` intercepts this exception and raises `CVTimeoutError`
    """

    async def async_iterator_with_timeout(timeout: float = 1.0) -> AsyncIterator[Any]:
        """Async iterator that yields a message and waits for the specified 'timeout' time before raising a TimeoutError."""
        yield WorkspaceStreamResponse(type=Operation.INITIAL_SYNC_COMPLETE)
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
        targeted_file: 'arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/9c3c1c2a6d572ea4ac06a4d2aef65b9e58d27f2c.json'
    """
    with (
        patch(
            "pyavd._cv.client.workspace.uuid4",
            side_effect=[MOCKED_WORKSPACE_B_REQUEST_ID_REBASE_1_SUCCESS["id"].removeprefix("req-")],
        ),
    ):
        response_workspace_config = await cv_client.rebase_workspace(workspace_id=MOCKED_WORKSPACE_B_ID)

    assert isinstance(response_workspace_config, WorkspaceConfig)
