# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from unittest.mock import MagicMock

import pytest

from pyavd._cv.api.arista.changecontrol.v1 import ChangeControlStatus
from pyavd._cv.client.exceptions import CVChangeControlFailed, CVInvalidInputsError
from pyavd._cv.workflows.manage_change_control_on_cv import get_managed_change_control_state, manage_change_control_on_cv
from pyavd._cv.workflows.models import AvdChangeControl, CVChangeControl

from .helpers import DEFAULT_TIMESTAMP, create_grpc_change_control


@pytest.mark.parametrize(
    ("status", "approved", "error", "expected_state"),
    [
        pytest.param(ChangeControlStatus.NOT_STARTED, False, None, "pending approval", id="not_started_unapproved"),
        pytest.param(ChangeControlStatus.NOT_STARTED, True, None, "approved", id="not_started_approved"),
        pytest.param(ChangeControlStatus.NOT_STARTED, True, "CloudVision error", "approved", id="not_started_with_error"),
        pytest.param(ChangeControlStatus.SCHEDULED, True, None, "scheduled", id="scheduled"),
        pytest.param(ChangeControlStatus.SCHEDULED, True, "CloudVision error", "scheduled", id="scheduled_with_error"),
        pytest.param(ChangeControlStatus.RUNNING, True, None, "running", id="running"),
        pytest.param(ChangeControlStatus.RUNNING, True, "CloudVision error", "running", id="running_with_error"),
        pytest.param(ChangeControlStatus.COMPLETED, True, None, "completed", id="completed_successfully"),
        pytest.param(ChangeControlStatus.COMPLETED, True, "CloudVision error", "failed", id="completed_with_error"),
        pytest.param(ChangeControlStatus.UNSPECIFIED, False, None, "pending approval", id="unspecified_unapproved"),
        pytest.param(ChangeControlStatus.UNSPECIFIED, False, "CloudVision error", "pending approval", id="unspecified_unapproved_with_error"),
        pytest.param(ChangeControlStatus.UNSPECIFIED, True, None, "approved", id="unspecified_approved"),
        pytest.param(ChangeControlStatus.UNSPECIFIED, True, "CloudVision error", "approved", id="unspecified_approved_with_error"),
    ],
)
def test_get_managed_change_control_state(
    status: ChangeControlStatus,
    approved: bool,
    error: str | None,
    expected_state: str,
) -> None:
    """Test state resolution using execution status, approval metadata, and errors."""
    cv_change_control = create_grpc_change_control(status=status, approved=approved, error=error)

    assert get_managed_change_control_state(cv_change_control) == expected_state


@pytest.mark.asyncio
async def test_manage_running_with_custom_notes(mock_cv_client: MagicMock) -> None:
    """Test that custom approval and start notes are passed to CloudVision."""
    local_cc = CVChangeControl(
        avd_change_control=AvdChangeControl(id="cc_id_1", requested_state="running", approval_note="Approved by operator", start_note="Started by operator"),
    )
    mock_cv_client.get_change_control.return_value = create_grpc_change_control()

    await manage_change_control_on_cv(change_control=local_cc, cv_client=mock_cv_client)

    mock_cv_client.approve_change_control.assert_called_once_with(change_control_id="cc_id_1", timestamp=DEFAULT_TIMESTAMP, description="Approved by operator")
    mock_cv_client.start_change_control.assert_called_once_with(change_control_id="cc_id_1", description="Started by operator")


@pytest.mark.asyncio
async def test_manage_pending_approval(mock_cv_client: MagicMock) -> None:
    """Test that an unapproved Change Control remains pending approval."""
    local_cc = CVChangeControl(avd_change_control=AvdChangeControl(id="cc_id_1", requested_state="pending approval"))
    mock_cv_client.get_change_control.return_value = create_grpc_change_control()

    await manage_change_control_on_cv(change_control=local_cc, cv_client=mock_cv_client)

    mock_cv_client.approve_change_control.assert_not_called()
    mock_cv_client.unapprove_change_control.assert_not_called()
    mock_cv_client.start_change_control.assert_not_called()
    assert local_cc.state == "pending approval"
    assert local_cc.changed is False


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("status", "expected_state"),
    [
        pytest.param(ChangeControlStatus.NOT_STARTED, "pending approval", id="not_started"),
        pytest.param(ChangeControlStatus.UNSPECIFIED, "pending approval", id="unspecified"),
    ],
)
async def test_manage_unapproves_change_control(
    mock_cv_client: MagicMock,
    status: ChangeControlStatus,
    expected_state: str,
) -> None:
    """Test unapproving an approved Change Control that has not yet entered execution."""
    local_cc = CVChangeControl(
        avd_change_control=AvdChangeControl(
            id="cc_id_1",
            requested_state="pending approval",
            approval_note="Unapproved by operator",
        ),
    )
    mock_cv_client.get_change_control.return_value = create_grpc_change_control(status=status, approved=True)

    await manage_change_control_on_cv(change_control=local_cc, cv_client=mock_cv_client)

    mock_cv_client.unapprove_change_control.assert_called_once_with(
        change_control_id="cc_id_1",
        timestamp=DEFAULT_TIMESTAMP,
        description="Unapproved by operator",
    )
    mock_cv_client.approve_change_control.assert_not_called()
    mock_cv_client.start_change_control.assert_not_called()
    assert local_cc.state == expected_state
    assert local_cc.changed is True


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("status", "state"),
    [
        pytest.param(ChangeControlStatus.SCHEDULED, "scheduled", id="scheduled"),
        pytest.param(ChangeControlStatus.RUNNING, "running", id="running"),
        pytest.param(ChangeControlStatus.COMPLETED, "completed", id="completed"),
        pytest.param(ChangeControlStatus.COMPLETED, "failed", id="completed_with_error"),
    ],
)
async def test_manage_rejects_pending_approval_for_advanced_state(
    mock_cv_client: MagicMock,
    status: ChangeControlStatus,
    state: str,
) -> None:
    """Test that requesting 'pending approval' fails without mutations when the Change Control is already in an advanced execution state."""
    error = "Execution failed" if state == "failed" else None
    local_cc = CVChangeControl(avd_change_control=AvdChangeControl(id="cc_id_1", requested_state="pending approval"))
    mock_cv_client.get_change_control.return_value = create_grpc_change_control(status=status, approved=True, error=error)

    with pytest.raises(CVChangeControlFailed, match=rf"Change Control 'cc_id_1' is in '{state}' state and cannot be moved to 'pending approval'\."):
        await manage_change_control_on_cv(change_control=local_cc, cv_client=mock_cv_client)

    mock_cv_client.unapprove_change_control.assert_not_called()
    mock_cv_client.approve_change_control.assert_not_called()
    mock_cv_client.start_change_control.assert_not_called()
    assert local_cc.changed is False


@pytest.mark.asyncio
async def test_manage_rejects_deleted_before_fetching_change_control(mock_cv_client: MagicMock) -> None:
    """Test that the 'deleted' requested state is rejected before calling CloudVision."""
    local_cc = CVChangeControl(avd_change_control=AvdChangeControl(id="cc_id_1", requested_state="deleted"))

    with pytest.raises(
        CVInvalidInputsError, match=r"Change Control 'cc_id_1': the 'deleted' requested state is not supported for an existing Change Control\."
    ):
        await manage_change_control_on_cv(change_control=local_cc, cv_client=mock_cv_client)

    mock_cv_client.get_change_control.assert_not_called()
    mock_cv_client.approve_change_control.assert_not_called()
    mock_cv_client.start_change_control.assert_not_called()


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("status", "state"),
    [
        pytest.param(ChangeControlStatus.NOT_STARTED, "approved", id="not_started"),
        pytest.param(ChangeControlStatus.UNSPECIFIED, "approved", id="unspecified"),
    ],
)
async def test_manage_approves_change_control(
    mock_cv_client: MagicMock,
    status: ChangeControlStatus,
    state: str,
) -> None:
    """Test that approving an unapproved Change Control that has not yet entered execution transitions it to 'approved'."""
    local_cc = CVChangeControl(avd_change_control=AvdChangeControl(id="cc_id_1", requested_state="approved"))
    mock_cv_client.get_change_control.return_value = create_grpc_change_control(status=status, approved=False)

    await manage_change_control_on_cv(change_control=local_cc, cv_client=mock_cv_client)

    mock_cv_client.approve_change_control.assert_called_once_with(
        change_control_id="cc_id_1", timestamp=DEFAULT_TIMESTAMP, description="Automatic approval by AVD"
    )
    mock_cv_client.start_change_control.assert_not_called()
    assert local_cc.state == state
    assert local_cc.changed is True


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("status", "state"),
    [
        pytest.param(ChangeControlStatus.SCHEDULED, "scheduled", id="scheduled"),
        pytest.param(ChangeControlStatus.RUNNING, "running", id="running"),
        pytest.param(ChangeControlStatus.COMPLETED, "completed", id="completed"),
        pytest.param(ChangeControlStatus.COMPLETED, "failed", id="completed_with_error"),
    ],
)
async def test_manage_rejects_approved_for_advanced_state(
    mock_cv_client: MagicMock,
    status: ChangeControlStatus,
    state: str,
) -> None:
    """Test that requesting 'approved' fails without mutations when the Change Control is already in an advanced execution state."""
    error = "Execution failed" if state == "failed" else None
    local_cc = CVChangeControl(avd_change_control=AvdChangeControl(id="cc_id_1", requested_state="approved"))
    mock_cv_client.get_change_control.return_value = create_grpc_change_control(status=status, approved=True, error=error)

    with pytest.raises(CVChangeControlFailed, match=rf"Change Control 'cc_id_1' is in '{state}' state and cannot be moved to 'approved'\."):
        await manage_change_control_on_cv(change_control=local_cc, cv_client=mock_cv_client)

    mock_cv_client.unapprove_change_control.assert_not_called()
    mock_cv_client.approve_change_control.assert_not_called()
    mock_cv_client.start_change_control.assert_not_called()
    assert local_cc.changed is False


@pytest.mark.asyncio
async def test_manage_not_started_to_completed(mock_cv_client: MagicMock) -> None:
    """Test approving, starting, and waiting for an unapproved Change Control to complete."""
    local_cc = CVChangeControl(avd_change_control=AvdChangeControl(id="cc_id_1", requested_state="completed"))
    mock_cv_client.get_change_control.return_value = create_grpc_change_control()
    mock_cv_client.wait_for_change_control_state.return_value = create_grpc_change_control(status=ChangeControlStatus.COMPLETED, approved=True)

    await manage_change_control_on_cv(change_control=local_cc, cv_client=mock_cv_client)

    mock_cv_client.approve_change_control.assert_called_once_with(
        change_control_id="cc_id_1", timestamp=DEFAULT_TIMESTAMP, description="Automatic approval by AVD"
    )
    mock_cv_client.start_change_control.assert_called_once_with(change_control_id="cc_id_1", description="Automatically started by AVD")
    mock_cv_client.wait_for_change_control_state.assert_called_once_with(cc_id="cc_id_1", state="completed")
    assert local_cc.state == "completed"
    assert local_cc.changed is True


@pytest.mark.asyncio
async def test_manage_already_running_is_idempotent(mock_cv_client: MagicMock) -> None:
    """Test that an already-running Change Control is not approved or started again."""
    local_cc = CVChangeControl(avd_change_control=AvdChangeControl(id="cc_id_1", requested_state="running"))
    mock_cv_client.get_change_control.return_value = create_grpc_change_control(status=ChangeControlStatus.RUNNING, approved=True)

    await manage_change_control_on_cv(change_control=local_cc, cv_client=mock_cv_client)

    mock_cv_client.approve_change_control.assert_not_called()
    mock_cv_client.start_change_control.assert_not_called()
    assert local_cc.state == "running"
    assert local_cc.changed is False


@pytest.mark.asyncio
async def test_manage_scheduled_defers_start_decision_to_cloudvision(mock_cv_client: MagicMock) -> None:
    """Test that CloudVision decides whether a scheduled Change Control can be started."""
    local_cc = CVChangeControl(avd_change_control=AvdChangeControl(id="cc_id_1", requested_state="running"))
    mock_cv_client.get_change_control.return_value = create_grpc_change_control(status=ChangeControlStatus.SCHEDULED, approved=True)

    await manage_change_control_on_cv(change_control=local_cc, cv_client=mock_cv_client)

    mock_cv_client.start_change_control.assert_called_once_with(change_control_id="cc_id_1", description="Automatically started by AVD")
    assert local_cc.state == "running"
    assert local_cc.changed is True


@pytest.mark.asyncio
async def test_manage_scheduled_to_completed_defers_start_decision_to_cloudvision(mock_cv_client: MagicMock) -> None:
    """Test that CloudVision decides whether a scheduled Change Control can be started before waiting for completion."""
    local_cc = CVChangeControl(avd_change_control=AvdChangeControl(id="cc_id_1", requested_state="completed"))
    mock_cv_client.get_change_control.return_value = create_grpc_change_control(status=ChangeControlStatus.SCHEDULED, approved=True)
    mock_cv_client.wait_for_change_control_state.return_value = create_grpc_change_control(status=ChangeControlStatus.COMPLETED, approved=True)

    await manage_change_control_on_cv(change_control=local_cc, cv_client=mock_cv_client)

    mock_cv_client.start_change_control.assert_called_once_with(change_control_id="cc_id_1", description="Automatically started by AVD")
    mock_cv_client.wait_for_change_control_state.assert_called_once_with(cc_id="cc_id_1", state="completed")
    assert local_cc.state == "completed"
    assert local_cc.changed is True


@pytest.mark.asyncio
async def test_manage_already_running_to_completed_waits_for_completion(mock_cv_client: MagicMock) -> None:
    """Test waiting for an already-running Change Control to complete."""
    local_cc = CVChangeControl(avd_change_control=AvdChangeControl(id="cc_id_1", requested_state="completed"))
    mock_cv_client.get_change_control.return_value = create_grpc_change_control(status=ChangeControlStatus.RUNNING, approved=True)
    mock_cv_client.wait_for_change_control_state.return_value = create_grpc_change_control(status=ChangeControlStatus.COMPLETED, approved=True)

    await manage_change_control_on_cv(change_control=local_cc, cv_client=mock_cv_client)

    mock_cv_client.approve_change_control.assert_not_called()
    mock_cv_client.start_change_control.assert_not_called()
    mock_cv_client.wait_for_change_control_state.assert_called_once_with(cc_id="cc_id_1", state="completed")
    assert local_cc.state == "completed"
    assert local_cc.changed is False


@pytest.mark.asyncio
async def test_manage_completed_failure_raises_without_running_again(mock_cv_client: MagicMock) -> None:
    """Test that an existing failed execution raises without being run again."""
    local_cc = CVChangeControl(avd_change_control=AvdChangeControl(id="cc_id_1", requested_state="completed"))
    mock_cv_client.get_change_control.return_value = create_grpc_change_control(
        status=ChangeControlStatus.COMPLETED,
        approved=True,
        error="Previous execution failed",
    )

    with pytest.raises(
        CVChangeControlFailed,
        match="Change Control 'cc_id_1' was already completed with errors before this workflow ran: Previous execution failed",
    ):
        await manage_change_control_on_cv(change_control=local_cc, cv_client=mock_cv_client)

    mock_cv_client.start_change_control.assert_not_called()
    mock_cv_client.wait_for_change_control_state.assert_not_called()
    assert local_cc.state == "failed"
    assert local_cc.changed is False


@pytest.mark.asyncio
async def test_manage_running_completed_successfully_is_idempotent(mock_cv_client: MagicMock) -> None:
    """Test that requesting 'running' for an already successfully completed Change Control is a no-op."""
    local_cc = CVChangeControl(avd_change_control=AvdChangeControl(id="cc_id_1", requested_state="running"))
    mock_cv_client.get_change_control.return_value = create_grpc_change_control(status=ChangeControlStatus.COMPLETED, approved=True)

    await manage_change_control_on_cv(change_control=local_cc, cv_client=mock_cv_client)

    mock_cv_client.approve_change_control.assert_not_called()
    mock_cv_client.start_change_control.assert_not_called()
    assert local_cc.state == "completed"
    assert local_cc.changed is False


@pytest.mark.asyncio
async def test_manage_running_completed_with_errors_raises(mock_cv_client: MagicMock) -> None:
    """Test that requesting 'running' for a Change Control that completed with errors raises without retrying."""
    local_cc = CVChangeControl(avd_change_control=AvdChangeControl(id="cc_id_1", requested_state="running"))
    mock_cv_client.get_change_control.return_value = create_grpc_change_control(
        status=ChangeControlStatus.COMPLETED,
        approved=True,
        error="Previous execution failed",
    )

    with pytest.raises(
        CVChangeControlFailed,
        match="Change Control 'cc_id_1' was already completed with errors before this workflow ran: Previous execution failed",
    ):
        await manage_change_control_on_cv(change_control=local_cc, cv_client=mock_cv_client)

    mock_cv_client.start_change_control.assert_not_called()
    assert local_cc.state == "failed"
    assert local_cc.changed is False


@pytest.mark.asyncio
async def test_manage_unspecified_error_defers_start_decision_to_cloudvision(mock_cv_client: MagicMock) -> None:
    """Test that an error with unspecified status does not prevent CloudVision from handling a start request."""
    local_cc = CVChangeControl(avd_change_control=AvdChangeControl(id="cc_id_1", requested_state="running"))
    mock_cv_client.get_change_control.return_value = create_grpc_change_control(
        status=ChangeControlStatus.UNSPECIFIED,
        approved=True,
        error="Previous scheduling failure",
    )

    await manage_change_control_on_cv(change_control=local_cc, cv_client=mock_cv_client)

    mock_cv_client.start_change_control.assert_called_once_with(change_control_id="cc_id_1", description="Automatically started by AVD")
    assert local_cc.state == "running"
    assert local_cc.changed is True
