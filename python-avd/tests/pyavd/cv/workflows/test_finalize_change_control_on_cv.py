# Copyright (c) 2025-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from unittest.mock import MagicMock, call

import pytest

from pyavd._cv.api.arista.changecontrol.v1 import ChangeControlStatus
from pyavd._cv.client.exceptions import CVChangeControlFailed, CVResourceNotFound
from pyavd._cv.workflows.finalize_change_control_on_cv import finalize_change_control_on_cv, get_change_control_state
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
def test_get_change_control_state(
    status: ChangeControlStatus,
    approved: bool,
    error: str | None,
    expected_state: str,
) -> None:
    """Test CC-only state resolution using execution status, approval metadata, and errors."""
    cv_change_control = create_grpc_change_control(status=status, approved=approved, error=error)

    assert get_change_control_state(cv_change_control, is_change_control_only=True) == expected_state


@pytest.mark.asyncio
async def test_finalize_pending_approval(mock_cv_client: MagicMock) -> None:
    """Test that a Change Control with requested_state='pending approval' is finalized correctly."""
    # Arrange
    local_cc = CVChangeControl(avd_change_control=AvdChangeControl(requested_state="pending approval"), id="cc_id_1")
    cv_cc_not_started = create_grpc_change_control()
    mock_cv_client.get_change_control.return_value = cv_cc_not_started

    # Act
    await finalize_change_control_on_cv(change_control=local_cc, cv_client=mock_cv_client)

    # Assert
    mock_cv_client.get_change_control.assert_called_once_with(change_control_id="cc_id_1")
    mock_cv_client.set_change_control.assert_not_called()
    mock_cv_client.approve_change_control.assert_not_called()
    mock_cv_client.start_change_control.assert_not_called()
    mock_cv_client.wait_for_change_control_state.assert_not_called()
    assert local_cc.state == "pending approval"


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("current_status", "current_state", "requested_state"),
    [
        pytest.param(ChangeControlStatus.NOT_STARTED, "approved", "pending approval", id="approved_to_pending_approval"),
        pytest.param(ChangeControlStatus.COMPLETED, "completed", "approved", id="completed_to_approved"),
    ],
)
async def test_finalize_rejects_backward_transition(
    mock_cv_client: MagicMock,
    current_status: ChangeControlStatus,
    current_state: str,
    requested_state: str,
) -> None:
    """Test that unsupported backward transitions fail before metadata updates."""
    local_cc = CVChangeControl(avd_change_control=AvdChangeControl(id="cc_id_1", name="New name", requested_state=requested_state))
    mock_cv_client.get_change_control.return_value = create_grpc_change_control(status=current_status, approved=True)

    with pytest.raises(
        CVChangeControlFailed,
        match=f"does not support transitioning Change Control 'cc_id_1' from state '{current_state}' to requested state '{requested_state}'",
    ):
        await finalize_change_control_on_cv(change_control=local_cc, cv_client=mock_cv_client)

    mock_cv_client.set_change_control.assert_not_called()
    assert local_cc.changed is False


@pytest.mark.asyncio
async def test_finalize_workspace_change_control_preserves_legacy_state_handling(mock_cv_client: MagicMock) -> None:
    """Test that a Workspace-created Change Control retains the legacy state handling."""
    local_cc = CVChangeControl(avd_change_control=AvdChangeControl(requested_state="approved"), id="cc_id_1")
    mock_cv_client.get_change_control.return_value = create_grpc_change_control(status=ChangeControlStatus.RUNNING, approved=True)

    await finalize_change_control_on_cv(change_control=local_cc, cv_client=mock_cv_client)

    mock_cv_client.approve_change_control.assert_called_once_with(
        change_control_id="cc_id_1", timestamp=DEFAULT_TIMESTAMP, description="Automatic approval by AVD"
    )
    mock_cv_client.start_change_control.assert_not_called()
    assert local_cc.state == "approved"
    assert local_cc.changed is True


@pytest.mark.asyncio
async def test_finalize_approved(mock_cv_client: MagicMock) -> None:
    """Test that a Change Control with requested_state='approved' is approved and finalized."""
    # Arrange
    local_cc = CVChangeControl(avd_change_control=AvdChangeControl(requested_state="approved"), id="cc_id_1")
    cv_cc_not_started = create_grpc_change_control()
    mock_cv_client.get_change_control.return_value = cv_cc_not_started

    # Act
    await finalize_change_control_on_cv(change_control=local_cc, cv_client=mock_cv_client)

    # Assert
    mock_cv_client.get_change_control.assert_called_once_with(change_control_id="cc_id_1")
    mock_cv_client.approve_change_control.assert_called_once_with(
        change_control_id="cc_id_1",
        timestamp=DEFAULT_TIMESTAMP,
        description="Automatic approval by AVD",
    )
    mock_cv_client.start_change_control.assert_not_called()
    mock_cv_client.wait_for_change_control_state.assert_not_called()
    assert local_cc.state == "approved"
    assert local_cc.changed is True


@pytest.mark.asyncio
async def test_finalize_running(mock_cv_client: MagicMock) -> None:
    """Test that a Change Control with requested_state='running' is approved, started, and finalized."""
    # Arrange
    local_cc = CVChangeControl(avd_change_control=AvdChangeControl(requested_state="running"), id="cc_id_1")
    cv_cc_not_started = create_grpc_change_control()
    mock_cv_client.get_change_control.return_value = cv_cc_not_started

    # Act
    await finalize_change_control_on_cv(change_control=local_cc, cv_client=mock_cv_client)

    # Assert
    mock_cv_client.get_change_control.assert_called_once_with(change_control_id="cc_id_1")
    mock_cv_client.approve_change_control.assert_called_once_with(
        change_control_id="cc_id_1", timestamp=DEFAULT_TIMESTAMP, description="Automatic approval by AVD"
    )
    mock_cv_client.start_change_control.assert_called_once_with(
        change_control_id="cc_id_1",
        description="Automatically started by AVD",
    )
    mock_cv_client.wait_for_change_control_state.assert_not_called()
    assert local_cc.state == "running"


@pytest.mark.asyncio
async def test_finalize_running_with_custom_notes(mock_cv_client: MagicMock) -> None:
    """Test that custom approval and start notes are passed to CloudVision."""
    local_cc = CVChangeControl(
        avd_change_control=AvdChangeControl(id="cc_id_1", requested_state="running", approval_note="Approved by operator", start_note="Started by operator"),
    )
    mock_cv_client.get_change_control.return_value = create_grpc_change_control()

    await finalize_change_control_on_cv(change_control=local_cc, cv_client=mock_cv_client)

    mock_cv_client.approve_change_control.assert_called_once_with(change_control_id="cc_id_1", timestamp=DEFAULT_TIMESTAMP, description="Approved by operator")
    mock_cv_client.start_change_control.assert_called_once_with(change_control_id="cc_id_1", description="Started by operator")


@pytest.mark.asyncio
async def test_finalize_already_running_is_idempotent(mock_cv_client: MagicMock) -> None:
    """Test that an already-running Change Control is not approved or started again."""
    local_cc = CVChangeControl(avd_change_control=AvdChangeControl(id="cc_id_1", requested_state="running"))
    mock_cv_client.get_change_control.return_value = create_grpc_change_control(status=ChangeControlStatus.RUNNING, approved=True)

    await finalize_change_control_on_cv(change_control=local_cc, cv_client=mock_cv_client)

    mock_cv_client.approve_change_control.assert_not_called()
    mock_cv_client.start_change_control.assert_not_called()
    assert local_cc.state == "running"
    assert local_cc.changed is False


@pytest.mark.asyncio
async def test_finalize_scheduled_does_not_satisfy_running(mock_cv_client: MagicMock) -> None:
    """Test that a scheduled Change Control does not satisfy a request for the running state."""
    local_cc = CVChangeControl(avd_change_control=AvdChangeControl(id="cc_id_1", requested_state="running"))
    mock_cv_client.get_change_control.return_value = create_grpc_change_control(status=ChangeControlStatus.SCHEDULED, approved=True)

    with pytest.raises(
        CVChangeControlFailed,
        match="does not support transitioning Change Control 'cc_id_1' from state 'scheduled' to requested state 'running'",
    ):
        await finalize_change_control_on_cv(change_control=local_cc, cv_client=mock_cv_client)

    mock_cv_client.start_change_control.assert_not_called()
    assert local_cc.changed is False


@pytest.mark.asyncio
async def test_finalize_deleted(mock_cv_client: MagicMock) -> None:
    """Test that a Change Control which has not started can be deleted."""
    local_cc = CVChangeControl(avd_change_control=AvdChangeControl(id="cc_id_1", requested_state="deleted"))
    mock_cv_client.get_change_control.return_value = create_grpc_change_control()

    await finalize_change_control_on_cv(change_control=local_cc, cv_client=mock_cv_client)

    mock_cv_client.set_change_control.assert_not_called()
    mock_cv_client.delete_change_control.assert_called_once_with(change_control_id="cc_id_1")
    assert local_cc.state == "deleted"
    assert local_cc.changed is True


@pytest.mark.asyncio
async def test_finalize_missing_change_control_is_already_deleted(mock_cv_client: MagicMock) -> None:
    """Test that deleting a missing Change Control is idempotent."""
    local_cc = CVChangeControl(avd_change_control=AvdChangeControl(id="cc_id_1", requested_state="deleted"))
    mock_cv_client.get_change_control.side_effect = CVResourceNotFound("Change Control not found")

    await finalize_change_control_on_cv(change_control=local_cc, cv_client=mock_cv_client)

    mock_cv_client.delete_change_control.assert_not_called()
    assert local_cc.state == "deleted"
    assert local_cc.changed is False


@pytest.mark.asyncio
@pytest.mark.parametrize("requested_state", ["pending approval", "approved", "running", "completed"])
async def test_finalize_missing_change_control_raises_for_other_states(mock_cv_client: MagicMock, requested_state: str) -> None:
    """Test that a missing Change Control fails when a state other than deleted is requested."""
    local_cc = CVChangeControl(avd_change_control=AvdChangeControl(id="cc_id_1", requested_state=requested_state))
    mock_cv_client.get_change_control.side_effect = CVResourceNotFound("Change Control not found")

    with pytest.raises(CVResourceNotFound, match="Change Control not found"):
        await finalize_change_control_on_cv(change_control=local_cc, cv_client=mock_cv_client)

    assert local_cc.state is None
    assert local_cc.changed is False


@pytest.mark.asyncio
async def test_finalize_workspace_change_control_cannot_be_deleted(mock_cv_client: MagicMock) -> None:
    """Test that deletion is not supported for a Workspace-created Change Control."""
    local_cc = CVChangeControl(avd_change_control=AvdChangeControl(requested_state="deleted"), id="cc_id_1")
    mock_cv_client.get_change_control.return_value = create_grpc_change_control()

    with pytest.raises(CVChangeControlFailed, match="'deleted' state is only supported in Change-Control-only mode"):
        await finalize_change_control_on_cv(change_control=local_cc, cv_client=mock_cv_client)

    mock_cv_client.get_change_control.assert_not_called()
    mock_cv_client.delete_change_control.assert_not_called()


@pytest.mark.asyncio
async def test_finalize_running_cannot_be_deleted(mock_cv_client: MagicMock) -> None:
    """Test that a running Change Control cannot be deleted."""
    local_cc = CVChangeControl(avd_change_control=AvdChangeControl(id="cc_id_1", requested_state="deleted"))
    mock_cv_client.get_change_control.return_value = create_grpc_change_control(status=ChangeControlStatus.RUNNING, approved=True)

    with pytest.raises(CVChangeControlFailed, match="cannot be deleted while in state 'running'"):
        await finalize_change_control_on_cv(change_control=local_cc, cv_client=mock_cv_client)

    mock_cv_client.delete_change_control.assert_not_called()


@pytest.mark.asyncio
async def test_finalize_scheduled_can_be_deleted(mock_cv_client: MagicMock) -> None:
    """Test that a scheduled Change Control can be deleted."""
    local_cc = CVChangeControl(avd_change_control=AvdChangeControl(id="cc_id_1", requested_state="deleted"))
    mock_cv_client.get_change_control.return_value = create_grpc_change_control(status=ChangeControlStatus.SCHEDULED, approved=True)

    await finalize_change_control_on_cv(change_control=local_cc, cv_client=mock_cv_client)

    mock_cv_client.delete_change_control.assert_called_once_with(change_control_id="cc_id_1")
    assert local_cc.state == "deleted"
    assert local_cc.changed is True


@pytest.mark.asyncio
async def test_finalize_completed_failure_cannot_be_retried(mock_cv_client: MagicMock) -> None:
    """Test that a Change Control with a completed failed execution is not started again."""
    local_cc = CVChangeControl(avd_change_control=AvdChangeControl(id="cc_id_1", requested_state="running"))
    mock_cv_client.get_change_control.return_value = create_grpc_change_control(
        status=ChangeControlStatus.COMPLETED,
        approved=True,
        error="Previous execution failed",
    )

    with pytest.raises(CVChangeControlFailed, match="does not support transitioning Change Control 'cc_id_1' from state 'failed' to requested state 'running'"):
        await finalize_change_control_on_cv(change_control=local_cc, cv_client=mock_cv_client)

    mock_cv_client.start_change_control.assert_not_called()
    assert local_cc.changed is False


@pytest.mark.asyncio
async def test_finalize_existing_completed_failure_is_unchanged(mock_cv_client: MagicMock) -> None:
    """Test that an existing failed execution satisfies a request for the completed state."""
    local_cc = CVChangeControl(avd_change_control=AvdChangeControl(id="cc_id_1", requested_state="completed"))
    mock_cv_client.get_change_control.return_value = create_grpc_change_control(
        status=ChangeControlStatus.COMPLETED,
        approved=True,
        error="Previous execution failed",
    )

    await finalize_change_control_on_cv(change_control=local_cc, cv_client=mock_cv_client)

    mock_cv_client.start_change_control.assert_not_called()
    mock_cv_client.wait_for_change_control_state.assert_not_called()
    assert local_cc.state == "failed"
    assert local_cc.changed is False


@pytest.mark.asyncio
async def test_finalize_unspecified_error_defers_start_decision_to_cloudvision(mock_cv_client: MagicMock) -> None:
    """Test that an error with unspecified status does not prevent CloudVision from handling a start request."""
    local_cc = CVChangeControl(avd_change_control=AvdChangeControl(id="cc_id_1", requested_state="running"))
    mock_cv_client.get_change_control.return_value = create_grpc_change_control(
        status=ChangeControlStatus.UNSPECIFIED,
        approved=True,
        error="Previous scheduling failure",
    )

    await finalize_change_control_on_cv(change_control=local_cc, cv_client=mock_cv_client)

    mock_cv_client.start_change_control.assert_called_once_with(change_control_id="cc_id_1", description="Automatically started by AVD")
    assert local_cc.state == "running"
    assert local_cc.changed is True


@pytest.mark.asyncio
async def test_finalize_completed_success(mock_cv_client: MagicMock) -> None:
    """Test that a Change Control with requested_state='completed' runs to successful completion."""
    # Arrange
    local_cc = CVChangeControl(avd_change_control=AvdChangeControl(requested_state="completed"), id="cc_id_1")
    cv_cc_not_started = create_grpc_change_control()
    cv_cc_completed = create_grpc_change_control(status=ChangeControlStatus.COMPLETED, approved=True)
    mock_cv_client.get_change_control.return_value = cv_cc_not_started
    mock_cv_client.wait_for_change_control_state.return_value = cv_cc_completed

    # Act
    await finalize_change_control_on_cv(change_control=local_cc, cv_client=mock_cv_client)

    # Assert
    mock_cv_client.get_change_control.assert_called_once_with(change_control_id="cc_id_1")
    mock_cv_client.approve_change_control.assert_called_once_with(
        change_control_id="cc_id_1", timestamp=DEFAULT_TIMESTAMP, description="Automatic approval by AVD"
    )
    mock_cv_client.start_change_control.assert_called_once_with(change_control_id="cc_id_1", description="Automatically started by AVD")
    mock_cv_client.wait_for_change_control_state.assert_called_once_with(cc_id="cc_id_1", state="completed")
    assert local_cc.state == "completed"


@pytest.mark.asyncio
async def test_finalize_completed_failure(mock_cv_client: MagicMock) -> None:
    """Test that a Change Control which fails during execution raises an exception."""
    # Arrange
    local_cc = CVChangeControl(avd_change_control=AvdChangeControl(requested_state="completed"), id="cc_id_1")
    cv_cc_not_started = create_grpc_change_control()
    cv_cc_failed = create_grpc_change_control(status=ChangeControlStatus.COMPLETED, approved=True, error="Something went wrong")

    mock_cv_client.get_change_control.return_value = cv_cc_not_started
    mock_cv_client.wait_for_change_control_state.return_value = cv_cc_failed

    # Act
    with pytest.raises(CVChangeControlFailed) as exc_info:
        await finalize_change_control_on_cv(change_control=local_cc, cv_client=mock_cv_client)

    # Assert
    assert "Change control failed during execution cc_id_1: Something went wrong" in str(exc_info.value)
    assert local_cc.state == "failed"
    mock_cv_client.wait_for_change_control_state.assert_called_once_with(cc_id="cc_id_1", state="completed")


@pytest.mark.asyncio
async def test_finalize_updates_local_cc_from_cv(mock_cv_client: MagicMock) -> None:
    """Test that local CC name and description are updated from CloudVision if they are None."""
    # Arrange
    local_cc = CVChangeControl(avd_change_control=AvdChangeControl(name=None, description=None, requested_state="pending approval"), id="cc_id_1")
    cv_cc_not_started = create_grpc_change_control(name="CV Name", notes="CV Notes")
    mock_cv_client.get_change_control.return_value = cv_cc_not_started

    # Act
    await finalize_change_control_on_cv(change_control=local_cc, cv_client=mock_cv_client)

    # Assert
    mock_cv_client.get_change_control.assert_called_once_with(change_control_id="cc_id_1")
    mock_cv_client.set_change_control.assert_not_called()
    assert local_cc.name == "CV Name"
    assert local_cc.description == "CV Notes"


@pytest.mark.asyncio
async def test_finalize_updates_cv_from_local_cc(mock_cv_client: MagicMock) -> None:
    """Test that the remote CC on CloudVision is updated if local name and description differ."""
    # Arrange
    local_cc = CVChangeControl(
        avd_change_control=AvdChangeControl(name="Local Name", description="Local Desc", requested_state="pending approval"), id="cc_id_1"
    )
    cv_cc_initial = create_grpc_change_control(name="CV Name Initial", notes="CV Notes Initial")
    cv_cc_updated = create_grpc_change_control(name="Local Name", notes="Local Desc")
    # Configure get_change_control to be called twice, returning the updated object the second time
    mock_cv_client.get_change_control.side_effect = [cv_cc_initial, cv_cc_updated]

    # Act
    await finalize_change_control_on_cv(change_control=local_cc, cv_client=mock_cv_client)

    # Assert
    mock_cv_client.set_change_control.assert_called_once_with(
        change_control_id="cc_id_1",
        name="Local Name",
        description="Local Desc",
    )
    get_calls = [call(change_control_id="cc_id_1"), call(change_control_id="cc_id_1")]
    mock_cv_client.get_change_control.assert_has_calls(get_calls)
    assert mock_cv_client.get_change_control.call_count == 2
