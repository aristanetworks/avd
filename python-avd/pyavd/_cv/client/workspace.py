# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from logging import getLogger
from typing import TYPE_CHECKING, Literal, Protocol
from uuid import uuid4

from pyavd._cv.api.arista.workspace.v1 import (
    Request,
    RequestParams,
    Response,
    ResponseCode,  # Added import for checking failure codes
    ResponseStatus,
    Workspace,
    WorkspaceConfig,
    WorkspaceConfigDeleteRequest,
    WorkspaceConfigServiceStub,
    WorkspaceConfigSetRequest,
    WorkspaceKey,
    WorkspaceRequest,
    WorkspaceServiceStub,
    WorkspaceStreamRequest,
)

from .async_decorators import GRPCRequestHandler
from .constants import DEFAULT_API_TIMEOUT
from .exceptions import CVResourceNotFound

if TYPE_CHECKING:
    from datetime import datetime

    from . import CVClientProtocol


LOGGER = getLogger(__name__)

REQUEST_MAP = {
    "abandon": Request.ABANDON,
    "cancel_build": Request.CANCEL_BUILD,
    "rollback": Request.ROLLBACK,
    "start_build": Request.START_BUILD,
    "submit": Request.SUBMIT,
    None: None,
}


class WorkspaceMixin(Protocol):
    """Only to be used as mixin on CVClient class."""

    workspace_api_version: Literal["v1"] = "v1"

    @GRPCRequestHandler()
    async def get_workspace(
        self: CVClientProtocol,
        workspace_id: str,
        time: datetime | None = None,
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> Workspace:
        """
        Get Workspace using arista.workspace.v1.WorkspaceService.GetOne API.

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

        response = await client.get_one(request, metadata=self._metadata, timeout=timeout)

        return response.value

    @GRPCRequestHandler()
    async def create_workspace(
        self: CVClientProtocol,
        workspace_id: str,
        display_name: str | None = None,
        description: str | None = None,
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> WorkspaceConfig:
        """
        Create Workspace using arista.workspace.v1.WorkspaceConfigService.Set API.

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
            ),
        )
        client = WorkspaceConfigServiceStub(self._channel)
        response = await client.set(request, metadata=self._metadata, timeout=timeout)
        return response.value

    @GRPCRequestHandler()
    async def abandon_workspace(
        self: CVClientProtocol,
        workspace_id: str,
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> WorkspaceConfig:
        """
        Abandon Workspace using arista.workspace.v1.WorkspaceConfigService.Set API.

        Parameters:
            workspace_id: Unique identifier the workspace.
            timeout: Timeout in seconds.

        Returns:
            WorkspaceConfig object after being set including any server-generated values.
        """
        request = WorkspaceConfigSetRequest(
            WorkspaceConfig(
                key=WorkspaceKey(workspace_id=workspace_id),
                request=Request.ABANDON,
                request_params=RequestParams(
                    request_id=f"req-{uuid4()}",
                ),
            ),
        )
        client = WorkspaceConfigServiceStub(self._channel)
        response = await client.set(request, metadata=self._metadata, timeout=timeout)
        return response.value

    @GRPCRequestHandler()
    async def build_workspace(
        self: CVClientProtocol,
        workspace_id: str,
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> WorkspaceConfig:
        """
        Request a build of the Workspace using arista.workspace.v1.WorkspaceConfigService.Set API.

        Parameters:
            workspace_id: Unique identifier the workspace.
            timeout: Timeout in seconds.

        Returns:
            WorkspaceConfig object after being set including any server-generated values.
        """
        request = WorkspaceConfigSetRequest(
            WorkspaceConfig(
                key=WorkspaceKey(workspace_id=workspace_id),
                request=Request.START_BUILD,
                request_params=RequestParams(
                    request_id=f"req-{uuid4()}",
                ),
            ),
        )
        client = WorkspaceConfigServiceStub(self._channel)
        response = await client.set(request, metadata=self._metadata, timeout=timeout)
        return response.value

    @GRPCRequestHandler()
    async def delete_workspace(
        self: CVClientProtocol,
        workspace_id: str,
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> WorkspaceKey:
        """
        Delete Workspace using arista.workspace.v1.WorkspaceConfigService.Delete API.

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

    @GRPCRequestHandler()
    async def submit_workspace(
        self: CVClientProtocol,
        workspace_id: str,
        force: bool = False,
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> WorkspaceConfig:
        """
        Request submission of the Workspace using arista.workspace.v1.WorkspaceConfigService.Set API.

        Parameters:
            workspace_id: Unique identifier the Workspace.
            force: Force submit the Workspace.
            timeout: Timeout in seconds.

        Returns:
            WorkspaceConfig object after being set including any server-generated values.
        """
        request = WorkspaceConfigSetRequest(
            WorkspaceConfig(
                key=WorkspaceKey(workspace_id=workspace_id),
                request=Request.SUBMIT_FORCE if force else Request.SUBMIT,
                request_params=RequestParams(request_id=f"req-{uuid4()}"),
            ),
        )
        client = WorkspaceConfigServiceStub(self._channel)
        response = await client.set(request, metadata=self._metadata, timeout=timeout)
        LOGGER.debug("submit_workspace: Got response to submission: %s", response.value)
        return response.value

    @GRPCRequestHandler()
    async def wait_for_workspace_response(
        self: CVClientProtocol,
        workspace_id: str,
        request_id: str,
        timeout: float = 3600.0,
    ) -> tuple[Response, Workspace]:
        """
        Monitor a Workspace using arista.workspace.v1.WorkspaceService.Subscribe API for a response to the given request_id.

        Blocks until a response in a terminal state (ResponseStatus.SUCCESS or ResponseStatus.FAIL) is returned or timed out.
        If a build fails with DECOMMISSION_DEVICES_INCOMPLETE, it will wait for the workspace to signal it needs another
        build, trigger it, and then monitor the new build request.

        Parameters:
            workspace_id: Unique identifier for the Workspace.
            request_id: Unique identifier for the initial Request.
            timeout: Timeout in seconds for the entire operation, including retries.

        Returns:
            Tuple of (<Response object for the final request_id>, <Full Workspace object>)
        """
        request = WorkspaceStreamRequest(
            partial_eq_filter=[
                Workspace(
                    key=WorkspaceKey(workspace_id=workspace_id),
                ),
            ],
        )
        client = WorkspaceServiceStub(self._channel)
        responses = client.subscribe(request, metadata=self._metadata, timeout=timeout)

        current_request_id = request_id
        waiting_for_rebuild = False

        async for resp in responses:
            workspace = resp.value
            workspace_responses = workspace.responses.values

            # If we are waiting to rebuild, check if the workspace is ready
            if waiting_for_rebuild and workspace.needs_build:
                LOGGER.info("Workspace '%s' is ready for rebuild. Triggering a new build.", workspace_id)

                new_build_config = await self.build_workspace(workspace_id=workspace_id)
                new_request_id = new_build_config.request_params.request_id
                LOGGER.info(
                    "New build triggered for workspace '%s'. Now monitoring new request ID: '%s'",
                    workspace_id,
                    new_request_id,
                )
                current_request_id = new_request_id
                waiting_for_rebuild = False
                continue  # Continue the loop to wait for the new response

            # Check for a response matching our current request ID
            if current_request_id in workspace_responses:
                request_response = workspace_responses[current_request_id]
                LOGGER.info("Got response for request '%s': %s", current_request_id, request_response)

                if request_response.status == ResponseStatus.SUCCESS:
                    LOGGER.info("Request '%s' for workspace '%s' completed successfully.", current_request_id, workspace_id)
                    return request_response, workspace

                if request_response.status == ResponseStatus.FAIL and request_response.code == ResponseCode.DECOMMISSION_DEVICES_INCOMPLETE:
                    LOGGER.warning(
                        "Build for request '%s' failed with DECOMMISSION_DEVICES_INCOMPLETE. "
                        "Waiting for workspace '%s' to signal 'needs_build'=True for retry.",
                        current_request_id,
                        workspace_id,
                    )
                    waiting_for_rebuild = True
                    continue  # Continue loop, waiting for needs_build to become True

            else:
                LOGGER.debug(
                    "wait_for_workspace_response: Got workspace update but not for request_id '%s'. Workspace State: %s.",
                    current_request_id,
                    workspace.state,
                )

        # This is reached if the stream completes (e.g., timeout) without a terminal response
        msg = f"Failed to get a terminal response for request '{current_request_id}' on workspace '{workspace_id}' before timeout."
        raise CVResourceNotFound(msg)
