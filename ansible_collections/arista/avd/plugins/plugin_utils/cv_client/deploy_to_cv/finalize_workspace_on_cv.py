# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from ..api.arista.workspace.v1 import BuildState, WorkspaceState
from ..client import CVClient
from ..client.exceptions import CVWorkspaceBuildFailed
from ..models import CVWorkspace

WORKSPACE_STATE_TO_FINAL_STATE_MAP = {
    WorkspaceState.WORKSPACE_STATE_ABANDONED: "abandoned",
    WorkspaceState.WORKSPACE_STATE_CONFLICTS: "build failed",
    WorkspaceState.WORKSPACE_STATE_PENDING: "pending",
    WorkspaceState.WORKSPACE_STATE_ROLLED_BACK: "pending",
    WorkspaceState.WORKSPACE_STATE_SUBMITTED: "submitted",
    WorkspaceState.WORKSPACE_STATE_UNSPECIFIED: None,
}


async def finalize_workspace_on_cv(workspace: CVWorkspace, cv_client: CVClient) -> None:
    """
    Finalize a Workspace from the given result.CVWorkspace object.
    Depending on the requested final_state the Workspace will be left in pending, built, submitted, abandoned or deleted.
    In-place update the workspace state and creates/updates a ChangeControl object on the result object if applicable.
    """
    if workspace.requested_state == workspace.final_state or workspace.requested_state == "pending":
        return

    workspace_config = await cv_client.build_workspace(workspace_id=workspace.id)
    try:
        build_result = await cv_client.wait_for_workspace_build(workspace_id=workspace.id, build_id=workspace_config.request_params.request_id)

    except CVWorkspaceBuildFailed as e:
        workspace.final_state = "build failed"
        raise e

    if build_result.state == BuildState.BUILD_STATE_SUCCESS:
        workspace.final_state = "built"
        if workspace.requested_state == "built":
            return

        # We can only submit if the build was successful
        if workspace.requested_state == "submitted":
            await cv_client.submit_workspace(workspace_id=workspace.id)

    # We can abort or delete even if we got some unexpected build state.
    if workspace.requested_state == "abandoned":
        await cv_client.abandon_workspace(workspace_id=workspace.id)
        return

    elif workspace.requested_state == "deleted":
        await cv_client.delete_workspace(workspace_id=workspace.id)
        workspace.final_state = "deleted"
        return

    cv_workspace = await cv_client.wait_for_workspace_states(
        workspace_id=workspace.id, states=[WorkspaceState.WORKSPACE_STATE_CONFLICTS, WorkspaceState.WORKSPACE_STATE_SUBMITTED]
    )

    workspace.final_state = WORKSPACE_STATE_TO_FINAL_STATE_MAP.get(cv_workspace.state)
    if cv_workspace.cc_ids is not None and cv_workspace.cc_ids.values:
        # Workspaces only create a single CC so we just only the first value.
        workspace.change_control_id = cv_workspace.cc_ids.values[0]

    return
