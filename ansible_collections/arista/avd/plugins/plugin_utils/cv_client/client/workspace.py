# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Literal
from uuid import uuid4

from async_timeout import timeout as atimeout

from ..api.arista.workspace.v1 import (
    BuildState,
    Request,
    RequestParams,
    Workspace,
    WorkspaceBuild,
    WorkspaceBuildKey,
    WorkspaceBuildServiceStub,
    WorkspaceBuildStreamRequest,
    WorkspaceConfig,
    WorkspaceConfigDeleteRequest,
    WorkspaceConfigServiceStub,
    WorkspaceConfigSetRequest,
    WorkspaceKey,
    WorkspaceRequest,
    WorkspaceServiceStub,
)
from .exceptions import CVWorkspaceBuildFailed, CVWorkspaceBuildTimeout, get_cv_client_exception

if TYPE_CHECKING:
    from .cv_client import CVClient


REQUEST_MAP = {
    "abandon": Request.REQUEST_ABANDON,
    "cancel_build": Request.REQUEST_CANCEL_BUILD,
    "rollback": Request.REQUEST_ROLLBACK,
    "start_build": Request.REQUEST_START_BUILD,
    "submit": Request.REQUEST_SUBMIT,
    None: None,
}


class WorkspaceMixin:
    workspace_api_version: Literal["v1"] = "v1"

    async def get_workspace(
        self: CVClient,
        workspace_id: str,
        time: datetime = None,
        timeout: float = 10.0,
    ) -> Workspace:
        """
        Get Workspace using arista.workspace.v1.WorkspaceService.GetOne API

        Parameters:
            workspace_id: Unique identifier the workspace.
            time: Timestamp from which the information is fetched. `now()` if not set.
            timeout: Timeout in seconds.

        Returns:
            Workspace object matching the workspace_id
        """
        request = WorkspaceRequest(
            key=WorkspaceKey(
                workspace_id=workspace_id,
            ),
            time=time,
        )
        client = WorkspaceServiceStub(self._channel)

        try:
            response = await client.get_one(request, metadata=self._metadata, timeout=timeout)
            return response.value

        except Exception as e:
            raise get_cv_client_exception(e, f"Workspace ID '{workspace_id}'") or e

    async def create_workspace(
        self: CVClient,
        workspace_id: str,
        display_name: str | None = None,
        description: str | None = None,
        timeout: float = 10.0,
    ) -> WorkspaceConfig:
        """
        Create Workspace using arista.workspace.v1.WorkspaceConfigService.Set API

        Parameters:
            workspace_id: Unique identifier the workspace.
            display_name: Workspace Name.
            description: Workspace description.
            timeout: Timeout in seconds.

        Returns:
            WorkspaceConfig object after being set including any server-generated values.
        """
        request = WorkspaceConfigSetRequest(
            WorkspaceConfig(
                key=WorkspaceKey(workspace_id=workspace_id),
                display_name=display_name,
                description=description,
            )
        )
        client = WorkspaceConfigServiceStub(self._channel)
        response = await client.set(request, metadata=self._metadata, timeout=timeout)
        return response.value

    async def abandon_workspace(
        self: CVClient,
        workspace_id: str,
        timeout: float = 10.0,
    ) -> WorkspaceConfig:
        """
        Abandon Workspace using arista.workspace.v1.WorkspaceConfigService.Set API

        Parameters:
            workspace_id: Unique identifier the workspace.
            timeout: Timeout in seconds.

        Returns:
            WorkspaceConfig object after being set including any server-generated values.
        """
        request = WorkspaceConfigSetRequest(
            WorkspaceConfig(
                key=WorkspaceKey(workspace_id=workspace_id),
                request=Request.REQUEST_ABANDON,
                request_params=RequestParams(
                    request_id=f"req-{uuid4()}",
                ),
            )
        )
        client = WorkspaceConfigServiceStub(self._channel)
        response = await client.set(request, metadata=self._metadata, timeout=timeout)
        return response.value

    async def build_workspace(
        self: CVClient,
        workspace_id: str,
        timeout: float = 10.0,
    ) -> WorkspaceConfig:
        """
        Request a build of the Workspace using arista.workspace.v1.WorkspaceConfigService.Set API

        Parameters:
            workspace_id: Unique identifier the workspace.
            timeout: Timeout in seconds.

        Returns:
            WorkspaceConfig object after being set including any server-generated values.
        """
        request = WorkspaceConfigSetRequest(
            WorkspaceConfig(
                key=WorkspaceKey(workspace_id=workspace_id),
                request=Request.REQUEST_START_BUILD,
                request_params=RequestParams(
                    request_id=f"req-{uuid4()}",
                ),
            )
        )
        client = WorkspaceConfigServiceStub(self._channel)
        response = await client.set(request, metadata=self._metadata, timeout=timeout)
        return response.value

    async def delete_workspace(
        self: CVClient,
        workspace_id: str,
        timeout: float = 10.0,
    ) -> WorkspaceKey:
        """
        Delete Workspace using arista.workspace.v1.WorkspaceConfigService.Delete API

        Parameters:
            workspace_id: Unique identifier the workspace.
            timeout: Timeout in seconds.

        Returns:
            WorkspaceConfig object after being set including any server-generated values.
        """
        request = WorkspaceConfigDeleteRequest(key=WorkspaceKey(workspace_id=workspace_id))
        client = WorkspaceConfigServiceStub(self._channel)
        response = await client.delete(request, metadata=self._metadata, timeout=timeout)
        return response.key

    async def submit_workspace(
        self: CVClient,
        workspace_id: str,
        timeout: float = 10.0,
    ) -> WorkspaceConfig:
        """
        Request submission of the Workspace using arista.workspace.v1.WorkspaceConfigService.Set API

        Parameters:
            workspace_id: Unique identifier the workspace.

            timeout: Timeout in seconds.

        Returns:
            WorkspaceConfig object after being set including any server-generated values.
        """
        request = WorkspaceConfigSetRequest(
            WorkspaceConfig(
                key=WorkspaceKey(workspace_id=workspace_id),
                request=Request.REQUEST_SUBMIT,
                request_params=RequestParams(
                    request_id=f"req-{uuid4()}",
                ),
            )
        )
        client = WorkspaceConfigServiceStub(self._channel)
        response = await client.set(request, metadata=self._metadata, timeout=timeout)
        return response.value

    async def wait_for_workspace_build(
        self: CVClient,
        workspace_id: str,
        build_id: str,
        time: datetime | None = None,
        build_timeout: float = 3600.0,
        timeout: float = 10.0,
    ) -> WorkspaceBuild:
        """
        Monitor a build of the Workspace using arista.workspace.v1.WorkspaceBuildService.Subscribe API
        Blocks until the build has succeeded, failed or timed out.

        Parameters:
            workspace_id: Unique identifier the Workspace.
            build_id: Unique identifier for the Build
            build_timeout: Timeout in seconds for the build operation.
            time: Timestamp from which the information is fetched. `now()` if not set.
            timeout: Timeout in seconds for the subscripe operation.

        Returns:
            WorkspaceBuild object after being set including any server-generated values.

        Raises:
            CVWorkspaceBuildFailed: If the build fails.
            CVWorkspaceBuildTimeout: If the build timeout expired.
        """
        request = WorkspaceBuildStreamRequest(
            partial_eq_filter=[
                WorkspaceBuild(
                    key=WorkspaceBuildKey(
                        workspace_id=workspace_id,
                        build_id=build_id,
                    )
                )
            ],
            time=time,
        )
        client = WorkspaceBuildServiceStub(self._channel)
        try:
            async with atimeout(build_timeout):
                responses = client.subscribe(request, metadata=self._metadata, timeout=timeout)
                async for response in responses:
                    if response.value.state in [BuildState.BUILD_STATE_IN_PROGRESS, BuildState.BUILD_STATE_UNSPECIFIED]:
                        continue

                    if response.value.state == BuildState.BUILD_STATE_FAIL:
                        raise CVWorkspaceBuildFailed(f"Build of Workspace ID '{workspace_id}' failed", response.value.build_results.to_json())

                    return response.value
        except TimeoutError as e:
            raise CVWorkspaceBuildTimeout(f"Build of Workspace ID '{workspace_id}' not completed within timeout of {build_timeout} seconds") from e
