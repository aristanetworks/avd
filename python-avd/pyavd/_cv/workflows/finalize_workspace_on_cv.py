# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from logging import getLogger
from typing import TYPE_CHECKING

from pyavd._cv.api.arista.workspace.v1 import ResponseStatus, WorkspaceState
from pyavd._cv.client.exceptions import CVWorkspaceBuildFailed, CVWorkspaceSubmitFailed

if TYPE_CHECKING:
    from pyavd._cv.client import CVClient

    from .models import CVWorkspace, CVWSBuildError

LOGGER = getLogger(__name__)

WORKSPACE_STATE_TO_FINAL_STATE_MAP = {
    WorkspaceState.ABANDONED: "abandoned",
    WorkspaceState.CONFLICTS: "build failed",
    WorkspaceState.PENDING: "pending",
    WorkspaceState.ROLLED_BACK: "pending",
    WorkspaceState.SUBMITTED: "submitted",
    WorkspaceState.UNSPECIFIED: None,
}


async def finalize_workspace_on_cv(workspace: CVWorkspace, cv_client: CVClient) -> None:
    """
    Finalize a Workspace from the given result.CVWorkspace object.

    Depending on the requested state the Workspace will be left in pending, built, submitted, abandoned or deleted.
    In-place update the workspace state and creates/updates a ChangeControl object on the result object if applicable.
    """
    LOGGER.info("finalize_workspace_on_cv: %s", workspace)

    if workspace.requested_state in (workspace.state, "pending"):
        return

    workspace_config = await cv_client.build_workspace(workspace_id=workspace.id)
    build_result, cv_workspace = await cv_client.wait_for_workspace_response(workspace_id=workspace.id, request_id=workspace_config.request_params.request_id)
    workspace.build_id = cv_workspace.last_build_id
    if build_result.status != ResponseStatus.SUCCESS:
        workspace.state = "build failed"
        ws_build_errors = await process_workspace_build_errors(workspace_id=workspace.id, build_id=workspace.build_id, cv_client=cv_client)
        if ws_build_errors:
            workspace.build_errors = ws_build_errors
        LOGGER.info("finalize_workspace_on_cv: %s", workspace)
        msg = (
            f"Failed to build workspace {workspace.id}: {build_result}. "
            f"See details: https://{cv_client._servers[0]}/cv/provisioning/workspaces?ws={workspace.id}"
        )
        raise CVWorkspaceBuildFailed(msg)

    workspace.state = "built"
    LOGGER.info("finalize_workspace_on_cv: %s", workspace)
    if workspace.requested_state == "built":
        return

    # We can only submit if the build was successful
    if workspace.requested_state == "submitted" and workspace.state == "built":
        workspace_config = await cv_client.submit_workspace(workspace_id=workspace.id, force=workspace.force)
        submit_result, cv_workspace = await cv_client.wait_for_workspace_response(
            workspace_id=workspace.id,
            request_id=workspace_config.request_params.request_id,
        )
        if submit_result.status != ResponseStatus.SUCCESS:
            workspace.state = "submit failed"
            LOGGER.info("finalize_workspace_on_cv: %s", workspace)
            msg = f"Failed to submit workspace {workspace.id}: {submit_result}"
            raise CVWorkspaceSubmitFailed(msg)

        workspace.state = "submitted"
        if cv_workspace.cc_ids.values:
            workspace.change_control_id = cv_workspace.cc_ids.values[0]
        LOGGER.info("finalize_workspace_on_cv: %s", workspace)
        return

    # We can abort or delete even if we got some unexpected build state.
    if workspace.requested_state == "abandoned":
        await cv_client.abandon_workspace(workspace_id=workspace.id)
        workspace.state = "abandoned"
        LOGGER.info("finalize_workspace_on_cv: %s", workspace)
        return

    if workspace.requested_state == "deleted":
        await cv_client.delete_workspace(workspace_id=workspace.id)
        workspace.state = "deleted"
        LOGGER.info("finalize_workspace_on_cv: %s", workspace)
        return

    return


async def process_workspace_build_errors(
    workspace_id: str,
    build_id: str,
    cv_client: CVClient,
) -> list[CVWSBuildError]:
    """
    Get and parse Workspace Build Details Response.

    Extract the following errors:
    - Config validation errors.
    - TODO: Image validation errors.

    Parameters:
        workspace_id: Unique identifier the workspace.
        build_id: Unique identifier of the last WS build attempt.
        cv_client: CVClient.

    Returns:
        List of CVWSBuildError objects describing observed WS build validation errors.
    """
    try:
        ws_build_details = await cv_client.get_workspace_build_details(workspace_id=workspace_id, build_id=build_id)

        ws_build_errors = [
            {
                "serial_number": response.value.key.device_id,
                "config_validation": [
                    {
                        "error_msg": error.error_msg,
                        "line_num": error.line_num,
                        "configlet_name": error.configlet_name,
                    }
                    for error in response.value.config_validation_result.errors.values
                ],
            }
            async for response in ws_build_details
            if response.value.config_validation_result.errors
        ]

    except Exception:
        LOGGER.info("finalize_workspace_on_cv: Failed to fetch WS build errors for workspace '%s'", workspace_id)
        return []

    else:
        return ws_build_errors
