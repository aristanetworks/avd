# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from logging import getLogger
from typing import TYPE_CHECKING

from pyavd._cv.api.arista.changecontrol.v1 import ChangeControl, ChangeControlStatus
from pyavd._cv.client.exceptions import CVChangeControlFailed, CVResourceNotFound

if TYPE_CHECKING:
    from pyavd._cv.client import CVClient

    from .models import CVChangeControl

LOGGER = getLogger(__name__)

# TODO: AVD 7.0.0 - Remove this legacy map and use unified state handling for all Change Controls.
CHANGE_CONTROL_STATUS_TO_FINAL_STATE_MAP = {
    ChangeControlStatus.COMPLETED: "completed",
    ChangeControlStatus.RUNNING: "running",
    ChangeControlStatus.SCHEDULED: "scheduled",
    ChangeControlStatus.UNSPECIFIED: None,
}

CHANGE_CONTROL_ONLY_STATUS_TO_FINAL_STATE_MAP = {
    ChangeControlStatus.COMPLETED: "completed",
    ChangeControlStatus.NOT_STARTED: None,
    ChangeControlStatus.RUNNING: "running",
    ChangeControlStatus.SCHEDULED: "scheduled",
    ChangeControlStatus.UNSPECIFIED: None,
}

CHANGE_CONTROL_APPROVAL_TO_FINAL_STATE_MAP = {True: "approved", False: None}


def get_change_control_state(cv_change_control: ChangeControl, *, is_change_control_only: bool) -> str:
    """Return the current Change Control state."""
    if is_change_control_only:
        if cv_change_control.status == ChangeControlStatus.UNSPECIFIED:
            return CHANGE_CONTROL_APPROVAL_TO_FINAL_STATE_MAP[cv_change_control.approve.value] or "pending approval"
        # Case of failed Change Control execution
        if cv_change_control.status == ChangeControlStatus.COMPLETED and cv_change_control.error is not None:
            return "failed"
        return (
            CHANGE_CONTROL_ONLY_STATUS_TO_FINAL_STATE_MAP[cv_change_control.status]
            or CHANGE_CONTROL_APPROVAL_TO_FINAL_STATE_MAP[cv_change_control.approve.value]
            or "pending approval"
        )

    return (
        CHANGE_CONTROL_STATUS_TO_FINAL_STATE_MAP[cv_change_control.status]
        or CHANGE_CONTROL_APPROVAL_TO_FINAL_STATE_MAP[cv_change_control.approve.value]
        or "failed"
        if cv_change_control.error is not None
        else "pending approval"
    )


async def finalize_change_control_on_cv(change_control: CVChangeControl, cv_client: CVClient) -> None:
    """
    Update and finalize a Change Control on CloudVision from the given result.CVChangeControl object.

    Depending on the requested state the Change Control will be left pending approval, approved, running, completed, or deleted.
    In-place update the CVChangeControl object.
    """
    LOGGER.info("finalize_change_control_on_cv: %s", change_control)
    change_control.changed = False
    is_change_control_only = change_control.avd_change_control.id is not None

    if change_control.requested_state == "deleted" and not is_change_control_only:
        msg = "The 'deleted' state is only supported in Change-Control-only mode."
        raise CVChangeControlFailed(msg)

    try:
        cv_change_control = await cv_client.get_change_control(change_control_id=change_control.id)
    except CVResourceNotFound:
        if change_control.requested_state != "deleted":
            raise
        change_control.state = "deleted"
        return

    # Update missing fields on our local model with data from the CloudVision object.
    change_control.state = get_change_control_state(cv_change_control=cv_change_control, is_change_control_only=is_change_control_only)
    if change_control.name is None:
        change_control.name = cv_change_control.change.name
    if change_control.description is None:
        change_control.description = cv_change_control.change.notes

    # TODO: Add CC template

    # Verify compatibility between requested and operational state of the Change Control
    if change_control.requested_state == "deleted":
        if cv_change_control.status in {ChangeControlStatus.RUNNING, ChangeControlStatus.COMPLETED}:
            msg = f"Change control '{change_control.id}' cannot be deleted while in state '{change_control.state}'."
            raise CVChangeControlFailed(msg)
    elif is_change_control_only:
        # A Change Control which was already completed satisfies the requested state regardless of the execution result.
        if cv_change_control.status == ChangeControlStatus.COMPLETED and change_control.requested_state == "completed":
            return

        # Change-Control-only mode currently supports forward state transitions only.
        backward_transition = (
            (change_control.requested_state == "pending approval" and cv_change_control.approve.value)
            or (
                change_control.requested_state in {"pending approval", "approved"}
                and cv_change_control.status in {ChangeControlStatus.RUNNING, ChangeControlStatus.SCHEDULED}
            )
            or cv_change_control.status == ChangeControlStatus.COMPLETED
            or (cv_change_control.status == ChangeControlStatus.SCHEDULED and change_control.requested_state == "running")
        )
        if backward_transition:
            msg = (
                f"Change-Control-only mode does not support transitioning Change Control '{change_control.id}' "
                f"from state '{change_control.state}' to requested state '{change_control.requested_state}'."
            )
            raise CVChangeControlFailed(msg)

    # TODO: Add support for canceling a Change Control.
    # Delete before applying optional detail updates since the Change Control will no longer exist.
    if change_control.requested_state == "deleted":
        await cv_client.delete_change_control(change_control_id=change_control.id)
        change_control.state = "deleted"
        change_control.changed = True
        return

    # Update the change control with name, description etc from our local object if needed.
    if change_control.name != cv_change_control.change.name or change_control.description != cv_change_control.change.notes:
        await cv_client.set_change_control(change_control_id=change_control.id, name=change_control.name, description=change_control.description)
        change_control.changed = True
        # Update the local copy to get the exact "last updated" timestamp needed for approval.
        cv_change_control = await cv_client.get_change_control(change_control_id=change_control.id)
        change_control.state = get_change_control_state(cv_change_control=cv_change_control, is_change_control_only=is_change_control_only)
        LOGGER.info("finalize_change_control_on_cv: %s", change_control)

    # Return when pending approval was requested.
    if change_control.requested_state == "pending approval":
        return

    # Return when a Change-Control-only Change Control has already reached the requested state.
    if is_change_control_only and (
        (
            change_control.requested_state == "approved"
            and cv_change_control.status in {ChangeControlStatus.NOT_STARTED, ChangeControlStatus.UNSPECIFIED}
            and cv_change_control.approve.value
        )
        or (change_control.requested_state == "running" and cv_change_control.status == ChangeControlStatus.RUNNING)
    ):
        return

    # For all other requested states we first need to approve.
    if (is_change_control_only and not cv_change_control.approve.value) or (not is_change_control_only and change_control.state != "approved"):
        await cv_client.approve_change_control(
            change_control_id=change_control.id,
            timestamp=cv_change_control.change.time,
            description=change_control.avd_change_control.approval_note,
        )
        change_control.state = "approved"
        change_control.changed = True
        LOGGER.info("finalize_change_control_on_cv: %s", change_control)

    # If requested state is "approved" we are done.
    if change_control.requested_state == "approved":
        return

    if not is_change_control_only or change_control.state == "approved":
        await cv_client.start_change_control(change_control_id=change_control.id, description=change_control.avd_change_control.start_note)
        change_control.state = "running"
        change_control.changed = True
        LOGGER.info("finalize_change_control_on_cv: %s", change_control)

    # If requested state is "running" we are done.
    if change_control.requested_state == "running":
        return

    cv_change_control = await cv_client.wait_for_change_control_state(cc_id=change_control.id, state="completed")
    if cv_change_control.error is not None:
        change_control.state = "failed"
        LOGGER.info("finalize_change_control_on_cv: %s", change_control)
        msg = f"Change control failed during execution {change_control.id}: {cv_change_control.error}"
        raise CVChangeControlFailed(msg)

    change_control.state = "completed"
    LOGGER.info("finalize_change_control_on_cv: %s", change_control)
