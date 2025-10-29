# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from contextlib import AbstractContextManager
from contextlib import nullcontext as does_not_raise
from typing import TYPE_CHECKING

import pytest

from pyavd._cv.client.exceptions import CVResourceInvalidState
from pyavd._cv.workflows.create_workspace_on_cv import create_workspace_on_cv
from pyavd._cv.workflows.models import CVWorkspace, DeployToCvResult

if TYPE_CHECKING:
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
