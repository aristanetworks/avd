# Copyright (c) 2024-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import re
from contextlib import AbstractContextManager
from contextlib import nullcontext as does_not_raise
from logging import DEBUG
from typing import TYPE_CHECKING, Any, Literal
from unittest.mock import AsyncMock, patch

import pytest

from pyavd._cv.client.exceptions import CVResourceInvalidState, CVWorkspaceFailed
from pyavd._cv.workflows.create_workspace_on_cv import create_workspace_on_cv
from pyavd._cv.workflows.models import AvdWorkspace, CVWorkspace, DeployToCvResult
from tests.pyavd.cv.constants import MOCKED_WORKSPACE_ID

if TYPE_CHECKING:
    from collections.abc import AsyncIterator

    from pyavd._cv.client import CVClient

ExpectedExceptionContext = AbstractContextManager[pytest.ExceptionInfo | None]


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
        result = DeployToCvResult(workspace=CVWorkspace(avd_workspace=AvdWorkspace(id=workspace_id)))
        await create_workspace_on_cv(workspace=result.workspace, cv_client=cv_client)

    assert result.workspace.avd_workspace.id == workspace_id
    assert result.workspace.state == workspace_requested_state


@pytest.mark.asyncio
@pytest.mark.parametrize("cv_client", [{"static_recording": True}], ids=["CV_CLIENT_STATIC_RECORDINGS"], indirect=True)
@pytest.mark.parametrize(
    ("workspace_id", "workspace_requested_state"),
    [
        pytest.param(MOCKED_WORKSPACE_ID, "pending", id="PENDING"),
        pytest.param(MOCKED_WORKSPACE_ID, "submitted", id="SUBMITTED"),
    ],
)
async def test_create_new_workspace_on_cv_success(
    caplog: pytest.LogCaptureFixture,
    cv_client: CVClient,
    workspace_id: str,
    workspace_requested_state: Literal["pending", "built", "submitted", "abandoned", "deleted"],
) -> None:
    """
    Test successful creation of the new Workspace and waiting for it to become PENDING.

    Exact test steps:
    -   description: Fetch Workspace status
        request: 'WorkspaceRequest(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'), time=None)'
        targeted_file: 'arista.workspace.v1.WorkspaceService/GetOne/www.cv-prod-us-central1-c.arista.io/a996cf0f4bc694971e5d4069f481faaba80f68b2.json'

    -   description: Create Workspace
        request: 'WorkspaceConfigSetRequest(value=WorkspaceConfig(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'),
            display_name='MOCKED_WS_NAME', description='MOCKED_WS_DESCRIPTION'))'
        targeted_file: 'arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/ce73310ec5154d57ac888fc8f93d69893962d804.json'

    -   description: Await until Workspace reaches PENDING state
        request: 'WorkspaceStreamRequest(partial_eq_filter=[Workspace(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'))])'
        targeted_file: 'arista.workspace.v1.WorkspaceService/Subscribe/www.cv-prod-us-central1-c.arista.io/1560c66d73da2be39448d710f15853fb124b2548.json'
    """
    # Mock original CVClient methods to assert them later.
    cv_client.get_workspace = AsyncMock(wraps=cv_client.get_workspace)
    cv_client.create_workspace = AsyncMock(wraps=cv_client.create_workspace)
    cv_client.wait_for_workspace_state = AsyncMock(wraps=cv_client.wait_for_workspace_state)

    with caplog.at_level(DEBUG):
        await create_workspace_on_cv(
            workspace=CVWorkspace(
                avd_workspace=AvdWorkspace(
                    name="MOCKED_WS_NAME",
                    description="MOCKED_WS_DESCRIPTION",
                    id=workspace_id,
                    requested_state=workspace_requested_state,
                )
            ),
            cv_client=cv_client,
        )

    assert cv_client.get_workspace.called
    cv_client.get_workspace.assert_called_once_with(workspace_id=workspace_id)
    assert any(
        re.search(
            re.compile(
                r"wait_for_workspace_state: Got workspace update: WorkspaceStreamResponse\(value=Workspace\(state=WorkspaceState.UNSPECIFIED\), "
                r"type=Operation.INITIAL_SYNC_COMPLETE\)"
            ),
            str(record.message),
        )
        for record in caplog.records
    )

    assert cv_client.create_workspace.called
    cv_client.create_workspace.assert_called_once_with(workspace_id=workspace_id, display_name="MOCKED_WS_NAME", description="MOCKED_WS_DESCRIPTION")

    assert cv_client.wait_for_workspace_state.called
    cv_client.wait_for_workspace_state.assert_called_once_with(workspace_id=workspace_id, state="pending")
    assert any(
        re.search(re.compile(r"wait_for_workspace_state: Workspace reached desired state \(pending\)"), str(record.message)) for record in caplog.records
    )


@pytest.mark.asyncio
@pytest.mark.parametrize("cv_client", [{"static_recording": True}], ids=["CV_CLIENT_STATIC_RECORDINGS"], indirect=True)
@pytest.mark.parametrize(
    ("workspace_id", "workspace_requested_state"),
    [
        pytest.param(MOCKED_WORKSPACE_ID, "pending", id="PENDING"),
        pytest.param(MOCKED_WORKSPACE_ID, "submitted", id="SUBMITTED"),
    ],
)
async def test_create_new_workspace_on_cv_failure(
    cv_client: CVClient,
    workspace_id: str,
    workspace_requested_state: Literal["pending", "built", "submitted", "abandoned", "deleted"],
) -> None:
    """
    Test unsuccessful creation of the new Workspace in PENDING state where Stream completes without Workspace reaching PENDING state.

    This test case emulates Subscription to the GRPC Service where GRPC Service:
    -   Returns WorkspaceStreamResponse object(s) for the initial state(s) (if any) of the Workspace. Messages have '"type": "INITIAL"'.
        This would be true if requested object existed prior to subscription.
    -   Returns WorkspaceStreamResponse object with 'type=Operation.INITIAL_SYNC_COMPLETE' to indicate that it has completed streaming all initial state(s).
        'value' and 'time' have default values.
    -   Returns WorkspaceStreamResponse object(s) for the subsequent state(s) of the Workspace. Messages may have 'type' of 'UPDATED', 'PARTIAL_DELETED', etc.

    Exact test steps:
    -   description: Fetch Workspace status
        request: 'WorkspaceRequest(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'), time=None)'
        targeted_file: 'arista.workspace.v1.WorkspaceService/GetOne/www.cv-prod-us-central1-c.arista.io/a996cf0f4bc694971e5d4069f481faaba80f68b2.json'

    -   description: Create Workspace
        request: 'WorkspaceConfigSetRequest(value=WorkspaceConfig(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'),
            display_name='MOCKED_WS_NAME', description='MOCKED_WS_DESCRIPTION'))'
        targeted_file: 'arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/ce73310ec5154d57ac888fc8f93d69893962d804.json'

    -   description: Await until Workspace reaches PENDING state
        request: 'WorkspaceStreamRequest(partial_eq_filter=[Workspace(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'))])'
        targeted_file: 'arista.workspace.v1.WorkspaceService/Subscribe/www.cv-prod-us-central1-c.arista.io/1560c66d73da2be39448d710f15853fb124b2548.json'

        Patched method `subscribe` of `arista.workspace.v1.WorkspaceServiceStub` emulates CloudVision returning no expected message.
        CVWorkspaceFailed is then raised by `wait_for_workspace_state` as a reaction to never getting a Workspace in PENDING state.
    """
    # Mock original CVClient method to assert it later.
    cv_client.wait_for_workspace_state = AsyncMock(wraps=cv_client.wait_for_workspace_state)

    # async generator that never yields.
    async def empty_async_iterator(*_args: Any, **_kwargs: Any) -> AsyncIterator[Any]:
        return
        yield "The message you will never get from me"

    with (
        pytest.raises(
            CVWorkspaceFailed,
            match=r"Workspace 'ws-cbf7c7ea-a57c-481d-b96b-97c12856395e' has not reached desired state 'pending'",
        ),
        patch(
            "pyavd._cv.client.workspace.WorkspaceServiceStub.subscribe",
            return_value=empty_async_iterator(),
        ),
    ):
        await create_workspace_on_cv(
            workspace=CVWorkspace(
                avd_workspace=AvdWorkspace(
                    name="MOCKED_WS_NAME",
                    description="MOCKED_WS_DESCRIPTION",
                    id=workspace_id,
                    requested_state=workspace_requested_state,
                )
            ),
            cv_client=cv_client,
        )

    assert cv_client.wait_for_workspace_state.called
    cv_client.wait_for_workspace_state.assert_called_once_with(workspace_id=workspace_id, state="pending")
