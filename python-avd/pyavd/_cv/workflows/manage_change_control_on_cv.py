# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from logging import getLogger
from typing import TYPE_CHECKING

from pyavd._cv.api.arista.changecontrol.v1 import ChangeControl, ChangeControlStatus
from pyavd._cv.client.exceptions import CVChangeControlFailed

from .utils import update_change_control_details_on_cv

if TYPE_CHECKING:
    from pyavd._cv.client import CVClient

    from .models import CVChangeControl, CVChangeControlState

LOGGER = getLogger(__name__)

CHANGE_CONTROL_STATUS_TO_STATE_MAP: dict[ChangeControlStatus, CVChangeControlState | None] = {
    ChangeControlStatus.COMPLETED: "completed",
    ChangeControlStatus.NOT_STARTED: None,
    ChangeControlStatus.RUNNING: "running",
    ChangeControlStatus.SCHEDULED: "scheduled",
    ChangeControlStatus.UNSPECIFIED: None,
}


def get_change_control_state(cv_change_control: ChangeControl, *, approved: bool | None = None) -> CVChangeControlState:
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
    change_control.changed = False

    cv_change_control, change_control.changed = await update_change_control_details_on_cv(change_control, cv_client)
    change_control.state = get_change_control_state(cv_change_control)
    LOGGER.info("manage_change_control_on_cv: %s", change_control)

    # TODO: Add support for stopping, unscheduling, unapproving, and deleting a Change Control
    if change_control.requested_state == "pending approval":
        return

    # Do not restart a completed Change Control when the requested state is "completed"
    if change_control.requested_state == "completed" and cv_change_control.status == ChangeControlStatus.COMPLETED:
        return

    if not cv_change_control.approve.value:
        await cv_client.approve_change_control(
            change_control_id=change_control.id,
            timestamp=cv_change_control.change.time,
            description=change_control.avd_change_control.approval_note,
        )
        change_control.state = get_change_control_state(cv_change_control, approved=True)
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
        msg = f"Change control failed during execution {change_control.id}: {cv_change_control.error}"
        raise CVChangeControlFailed(msg)

    change_control.state = "completed"
    LOGGER.info("manage_change_control_on_cv: %s", change_control)
