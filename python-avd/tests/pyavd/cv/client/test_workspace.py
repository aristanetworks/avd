# Copyright (c) 2024-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import asyncio
from typing import TYPE_CHECKING, Any
from unittest.mock import patch

import pytest

from pyavd._cv.client.exceptions import CVTimeoutError, CVWorkspaceFailed
from tests.pyavd.cv.constants import MOCKED_WORKSPACE_ID

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

    This is to replicate the following real events:
    -  `grpclib.client.Stream` object fetches messages by removing them from the `asyncio` queue
    -  If queue is empty for <timeout> seconds, `asyncio.exceptions.CancelledError` is raised
    -  This exception is caught by `grpclib` client
    -  `grpclib` client then raises `TimeoutError("Deadline exceeded.")`
    -  `pyavd`'s `async_decorator` intercepts this exception and raises `CVTimeoutError`
    """

    async def async_iterator_with_timeout(timeout: float = 1.0) -> AsyncIterator[Any]:
        """Async iterator that yields a message and waits for the specified 'timeout' time before raising a TimeoutError."""
        yield "Single message that you will get before I timeout."
        await asyncio.sleep(int(timeout))
        msg = "Deadline exceeded."
        raise TimeoutError(msg)

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
