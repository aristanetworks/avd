# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from logging import getLogger

from ..api.arista.changecontrol.v1 import ChangeControl, ChangeControlStatus
from ..client import CVClient
from .models import CVChangeControl

LOGGER = getLogger(__name__)

CHANGE_CONTROL_STATUS_TO_FINAL_STATE_MAP = {
    ChangeControlStatus.COMPLETED: "completed",
    ChangeControlStatus.RUNNING: "running",
    ChangeControlStatus.SCHEDULED: "scheduled",
    ChangeControlStatus.UNSPECIFIED: None,
}

CHANGE_CONTROL_APPROVAL_TO_FINAL_STATE_MAP = {True: "approved", False: None}


def get_change_control_final_state(cv_change_control: ChangeControl) -> str:
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
    Depending on the requested final_state the Change Control will be left in pending approval, approved, started, completed or canceled.
    In-place update the CVChangeControl object.
    """

    LOGGER.info("finalize_change_control_on_cv: %s", change_control)

    cv_change_control = await cv_client.get_change_control(change_control_id=change_control.id)

    # Update missing fields on our local model with data from the CloudVision object.
    change_control.final_state = get_change_control_final_state(cv_change_control=cv_change_control)
    if change_control.description is None:
        change_control.name = cv_change_control.change.name
    if change_control.description is None:
        change_control.description = cv_change_control.change.notes

    # TODO: Add CC template

    # Update the change control with name, description etc from our local object if needed.
    if change_control.name != cv_change_control.change.name or change_control.description != cv_change_control.change.notes:
        await cv_client.set_change_control(change_control_id=change_control.id, name=change_control.name, description=change_control.description)
        # Update the local copy to get the exact "last updated" timestamp needed for approval.
        cv_change_control = await cv_client.get_change_control(change_control_id=change_control.id)
        change_control.final_state = get_change_control_final_state(cv_change_control=cv_change_control)

    # If requested state is "pending approval" we are done
    if change_control.requested_state == "pending approval":
        return

    # TODO: Add cancel/delete

    # For all other requested states we first need to approve.
    if not change_control.final_state == "approved":
        await cv_client.approve_change_control(
            change_control_id=change_control.id, timestamp=cv_change_control.change.time, description="Automatic approval by AVD"
        )
        change_control.final_state = "approved"

    # If requested state is "approved" we are done.
    if change_control.requested_state == "approved":
        return

    await cv_client.start_change_control(change_control_id=change_control.id, description="Automatically started by AVD")
    change_control.final_state = "running"

    # If requested state is "running" we are done.
    if change_control.requested_state == "running":
        return
