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

from pyavd._cv.client.exceptions import CVResourceInvalidState, CVResourceNotFound
from pyavd._cv.workflows.create_workspace_on_cv import create_workspace_on_cv
from pyavd._cv.workflows.models import CVWorkspace, DeployToCvResult

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
    ("workspace_id", "workspace_requested_state"),
    [
        pytest.param("ws-cbf7c7ea-a57c-481d-b96b-97c12856395e", "pending", id="PENDING"),
        pytest.param("ws-cbf7c7ea-a57c-481d-b96b-97c12856395e", "submitted", id="SUBMITTED"),
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

        While waiting for the Workspace to reach PENDING state, it first goes through UNSPECIFIED state:
            'WorkspaceStreamResponse(value=Workspace(state=WorkspaceState.UNSPECIFIED), type=Operation.INITIAL_SYNC_COMPLETE)'
        It then gets a message confirming that the Workspace has reached PENDING state:
            'WorkspaceStreamResponse(
                value=Workspace(
                    key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'),
                    created_at=datetime.datetime(2025, 5, 6, 16, 28, 2, 14825),
                    created_by='agorbunov',
                    last_modified_at=datetime.datetime(2025, 5, 6, 16, 28, 2, 169589),
                    last_modified_by='agorbunov',
                    state=WorkspaceState.PENDING,
                    last_build_id='',
                    responses=Responses(),
                    cc_ids=RepeatedString(),
                    needs_build=False,
                    needs_rebase=False,
                    display_name='MOCKED_WS_NAME',
                    description='MOCKED_WS_DESCRIPTION'
                ),
                time=datetime.datetime(2025, 5, 6, 16, 28, 2, 222973),
                type=Operation.INITIAL
            )'
    """
    # Mock original CVClient methods to assert them later.
    cv_client.get_workspace = AsyncMock(wraps=cv_client.get_workspace)
    cv_client.create_workspace = AsyncMock(wraps=cv_client.create_workspace)
    cv_client.wait_for_new_workspace_readiness = AsyncMock(wraps=cv_client.wait_for_new_workspace_readiness)

    with caplog.at_level(DEBUG):
        await create_workspace_on_cv(
            workspace=CVWorkspace(
                name="MOCKED_WS_NAME",
                description="MOCKED_WS_DESCRIPTION",
                id=workspace_id,
                requested_state=workspace_requested_state,
            ),
            cv_client=cv_client,
        )

    assert cv_client.get_workspace.called
    cv_client.get_workspace.assert_called_once_with(workspace_id=workspace_id)
    assert any(
        re.search(
            re.compile("wait_for_workspace_readiness: Got workspace update but it is not yet in PENDING state.*type=Operation.INITIAL_SYNC_COMPLETE"),
            str(record.message),
        )
        for record in caplog.records
    )

    assert cv_client.create_workspace.called
    cv_client.create_workspace.assert_called_once_with(workspace_id=workspace_id, display_name="MOCKED_WS_NAME", description="MOCKED_WS_DESCRIPTION")

    assert cv_client.wait_for_new_workspace_readiness.called
    cv_client.wait_for_new_workspace_readiness.assert_called_once_with(workspace_id=workspace_id)
    assert any(
        re.search(re.compile("wait_for_workspace_readiness: Workspace reached required state \\(PENDING\\)"), str(record.message)) for record in caplog.records
    )


@pytest.mark.asyncio
@pytest.mark.parametrize("cv_client", [{"static_recording": True}], ids=["CV_CLIENT_STATIC_RECORDINGS"], indirect=True)
@pytest.mark.parametrize(
    ("workspace_id", "workspace_requested_state"),
    [
        pytest.param("ws-cbf7c7ea-a57c-481d-b96b-97c12856395e", "pending", id="PENDING"),
        pytest.param("ws-cbf7c7ea-a57c-481d-b96b-97c12856395e", "submitted", id="SUBMITTED"),
    ],
)
async def test_create_new_workspace_on_cv_failure(
    cv_client: CVClient,
    workspace_id: str,
    workspace_requested_state: Literal["pending", "built", "submitted", "abandoned", "deleted"],
) -> None:
    """
    Test unsuccessful creation of the new Workspace where waiting for it to become PENDING times out.

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
        CVResourceNotFound is then raised by `wait_for_new_workspace_readiness` a as reaction to never getting WOrkspace in PENDING state.
    """
    # Mock original CVClient method to assert it later.
    cv_client.wait_for_new_workspace_readiness = AsyncMock(wraps=cv_client.wait_for_new_workspace_readiness)

    # async generator that yields nothing
    async def empty_async_iterator(*_args: Any, **_kwargs: Any) -> AsyncIterator[None]:
        return
        yield

    with (
        pytest.raises(
            CVResourceNotFound,
            match=r"wait_for_workspace_readiness: Timed out waiting for Workspace 'ws-cbf7c7ea-a57c-481d-b96b-97c12856395e' to get in PENDING state.",
        ),
        patch(
            "pyavd._cv.client.workspace.WorkspaceServiceStub.subscribe",
            side_effect=empty_async_iterator,
        ),
    ):
        await create_workspace_on_cv(
            workspace=CVWorkspace(
                name="MOCKED_WS_NAME",
                description="MOCKED_WS_DESCRIPTION",
                id=workspace_id,
                requested_state=workspace_requested_state,
            ),
            cv_client=cv_client,
        )

    assert cv_client.wait_for_new_workspace_readiness.called
    cv_client.wait_for_new_workspace_readiness.assert_called_once_with(workspace_id=workspace_id)
