# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from logging import getLogger
from typing import TYPE_CHECKING

from pyavd._cv.api.arista.changecontrol.v1 import ChangeControl, ChangeControlStatus
from pyavd._cv.client.exceptions import CVChangeControlFailed, CVInvalidInputsError

from .utils import update_change_control_details_on_cv

if TYPE_CHECKING:
    from pyavd._cv.client import CVClient

    from .models import CVChangeControl, CVChangeControlState

LOGGER = getLogger(__name__)

# Statuses of the CloudVision Change Control which should not be moved back to a pre-execution state.
CHANGE_CONTROL_EXECUTION_STATUSES: frozenset[ChangeControlStatus] = frozenset(
    {ChangeControlStatus.RUNNING, ChangeControlStatus.SCHEDULED, ChangeControlStatus.COMPLETED}
)
CHANGE_CONTROL_STATUS_TO_STATE_MAP: dict[ChangeControlStatus, CVChangeControlState | None] = {
    ChangeControlStatus.COMPLETED: "completed",
    ChangeControlStatus.NOT_STARTED: None,
    ChangeControlStatus.RUNNING: "running",
    ChangeControlStatus.SCHEDULED: "scheduled",
    ChangeControlStatus.UNSPECIFIED: None,
}


def get_managed_change_control_state(cv_change_control: ChangeControl, *, approved: bool | None = None) -> CVChangeControlState:
    """Return the current state of an existing Change Control."""
    if approved is None:
        approved = cv_change_control.approve.value
    approval_state = "approved" if approved else None

    if cv_change_control.status == ChangeControlStatus.UNSPECIFIED:
        return approval_state or "pending approval"
    # Case of failed Change Control execution
    if cv_change_control.status == ChangeControlStatus.COMPLETED and cv_change_control.error is not None:
        return "failed"
    return CHANGE_CONTROL_STATUS_TO_STATE_MAP[cv_change_control.status] or approval_state or "pending approval"


async def manage_change_control_on_cv(change_control: CVChangeControl, cv_client: CVClient) -> None:
    """Manage an existing Change Control on CloudVision and update the CVChangeControl object in place."""
    LOGGER.info("manage_change_control_on_cv: %s", change_control)

    if change_control.requested_state == "deleted":
        msg = f"Change Control '{change_control.id}': the 'deleted' requested state is not supported for an existing Change Control."
        raise CVInvalidInputsError(msg)

    change_control.changed = False

    # Fetch the current state of the CloudVision Change Control without performing any mutations
    cv_change_control = await cv_client.get_change_control(change_control_id=change_control.id)
    change_control.state = get_managed_change_control_state(cv_change_control)
    LOGGER.info("manage_change_control_on_cv: %s", change_control)

    # TODO: Add support for stopping, unscheduling, rolling back, and deleting a Change Control
    # Change Control that has already entered execution state can't be moved back
    if change_control.requested_state in {"pending approval", "approved"} and cv_change_control.status in CHANGE_CONTROL_EXECUTION_STATUSES:
        msg = f"Change Control '{change_control.id}' is in '{change_control.state}' state and cannot be moved to '{change_control.requested_state}'."
        raise CVChangeControlFailed(msg)

    if change_control.requested_state in {"completed", "running"} and cv_change_control.status == ChangeControlStatus.COMPLETED:
        if cv_change_control.error is not None:
            msg = f"Change Control '{change_control.id}' was already completed with errors before this workflow ran: {cv_change_control.error}"
            raise CVChangeControlFailed(msg)
        return

    # Update name/description on CloudVision if needed. Then re-fetch to get the latest timestamp for approval
    cv_change_control, change_control.changed = await update_change_control_details_on_cv(change_control, cv_client)

    if change_control.requested_state == "pending approval":
        if cv_change_control.approve.value:
            await cv_client.unapprove_change_control(
                change_control_id=change_control.id,
                timestamp=cv_change_control.change.time,
                description=change_control.avd_change_control.approval_note,
            )
            change_control.state = get_managed_change_control_state(cv_change_control, approved=False)
            change_control.changed = True
            LOGGER.info("manage_change_control_on_cv: %s", change_control)
        return

    if not cv_change_control.approve.value:
        await cv_client.approve_change_control(
            change_control_id=change_control.id,
            timestamp=cv_change_control.change.time,
            description=change_control.avd_change_control.approval_note,
        )
        change_control.state = get_managed_change_control_state(cv_change_control, approved=True)
        change_control.changed = True
        LOGGER.info("manage_change_control_on_cv: %s", change_control)

    if change_control.requested_state == "approved":
        return

    if cv_change_control.status != ChangeControlStatus.RUNNING:
        await cv_client.start_change_control(change_control_id=change_control.id, description=change_control.avd_change_control.start_note)
        change_control.state = "running"
        change_control.changed = True
        LOGGER.info("manage_change_control_on_cv: %s", change_control)

    if change_control.requested_state == "running":
        return

    cv_change_control = await cv_client.wait_for_change_control_state(cc_id=change_control.id, state="completed")
    if cv_change_control.error is not None:
        change_control.state = "failed"
        LOGGER.info("manage_change_control_on_cv: %s", change_control)
        msg = f"Change Control failed during execution {change_control.id}: {cv_change_control.error}"
        raise CVChangeControlFailed(msg)

    change_control.state = "completed"
    LOGGER.info("manage_change_control_on_cv: %s", change_control)
