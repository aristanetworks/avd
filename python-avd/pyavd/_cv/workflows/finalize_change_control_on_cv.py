# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from logging import getLogger
from typing import TYPE_CHECKING

from pyavd._cv.api.arista.changecontrol.v1 import ChangeControl, ChangeControlStatus
from pyavd._cv.client.exceptions import CVChangeControlFailed

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

    Depending on the requested state the Change Control will be left pending approval, approved, running, or completed.
    In-place update the CVChangeControl object.
    """
    LOGGER.info("finalize_change_control_on_cv: %s", change_control)
    change_control.changed = False
    is_change_control_only = change_control.avd_change_control.id is not None

    cv_change_control = await cv_client.get_change_control(change_control_id=change_control.id)

    # Update missing fields on our local model with data from the CloudVision object.
    change_control.state = get_change_control_state(cv_change_control=cv_change_control, is_change_control_only=is_change_control_only)
    if change_control.name is None:
        change_control.name = cv_change_control.change.name
    if change_control.description is None:
        change_control.description = cv_change_control.change.notes

    # TODO: Add CC template

    # Update the change control with name, description etc from our local object if needed.
    if change_control.name != cv_change_control.change.name or change_control.description != cv_change_control.change.notes:
        await cv_client.set_change_control(change_control_id=change_control.id, name=change_control.name, description=change_control.description)
        change_control.changed = True
        # Update the local copy to get the exact "last updated" timestamp needed for approval.
        cv_change_control = await cv_client.get_change_control(change_control_id=change_control.id)
        change_control.state = get_change_control_state(cv_change_control=cv_change_control, is_change_control_only=is_change_control_only)
        LOGGER.info("finalize_change_control_on_cv: %s", change_control)

    # TODO: Add support for canceling and deleting a Change Control.
    # If requested state is "pending approval" we are done.
    if change_control.requested_state == "pending approval":
        return

    # Return when the requested operation is already satisfied in Change-Control-only mode.
    if is_change_control_only and (
        (change_control.requested_state == "approved" and cv_change_control.approve.value)
        or (change_control.requested_state == "running" and cv_change_control.status == ChangeControlStatus.RUNNING)
        or (change_control.requested_state == "completed" and cv_change_control.status == ChangeControlStatus.COMPLETED)
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

    start_required = (
        not is_change_control_only
        or change_control.requested_state == "running"
        or cv_change_control.status not in {ChangeControlStatus.RUNNING, ChangeControlStatus.SCHEDULED}
    )
    if start_required:
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
