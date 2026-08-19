# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from unittest.mock import MagicMock

import pytest

from pyavd._cv.api.arista.changecontrol.v1 import ChangeControlStatus
from pyavd._cv.workflows.manage_change_control_on_cv import get_change_control_state, manage_change_control_on_cv
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
    """Test state resolution using execution status, approval metadata, and errors."""
    cv_change_control = create_grpc_change_control(status=status, approved=approved, error=error)

    assert get_change_control_state(cv_change_control) == expected_state


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
    """Test that pending approval does not approve or start an existing Change Control."""
    local_cc = CVChangeControl(avd_change_control=AvdChangeControl(id="cc_id_1", requested_state="pending approval"))
    mock_cv_client.get_change_control.return_value = create_grpc_change_control()

    await manage_change_control_on_cv(change_control=local_cc, cv_client=mock_cv_client)

    mock_cv_client.approve_change_control.assert_not_called()
    mock_cv_client.start_change_control.assert_not_called()
    assert local_cc.state == "pending approval"
    assert local_cc.changed is False


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
@pytest.mark.parametrize(
    ("status", "expected_state"),
    [
        pytest.param(ChangeControlStatus.SCHEDULED, "scheduled", id="scheduled"),
        pytest.param(ChangeControlStatus.RUNNING, "running", id="running"),
        pytest.param(ChangeControlStatus.COMPLETED, "completed", id="completed"),
    ],
)
async def test_manage_approval_preserves_execution_state(
    mock_cv_client: MagicMock,
    status: ChangeControlStatus,
    expected_state: str,
) -> None:
    """Test that approving an existing Change Control preserves its execution state."""
    local_cc = CVChangeControl(avd_change_control=AvdChangeControl(id="cc_id_1", requested_state="approved"))
    mock_cv_client.get_change_control.return_value = create_grpc_change_control(status=status, approved=False)

    await manage_change_control_on_cv(change_control=local_cc, cv_client=mock_cv_client)

    mock_cv_client.approve_change_control.assert_called_once_with(
        change_control_id="cc_id_1", timestamp=DEFAULT_TIMESTAMP, description="Automatic approval by AVD"
    )
    assert local_cc.state == expected_state
    assert local_cc.changed is True


@pytest.mark.asyncio
async def test_manage_existing_completed_failure_is_unchanged(mock_cv_client: MagicMock) -> None:
    """Test that an existing failed execution satisfies a request for the completed state."""
    local_cc = CVChangeControl(avd_change_control=AvdChangeControl(id="cc_id_1", requested_state="completed"))
    mock_cv_client.get_change_control.return_value = create_grpc_change_control(
        status=ChangeControlStatus.COMPLETED,
        approved=True,
        error="Previous execution failed",
    )

    await manage_change_control_on_cv(change_control=local_cc, cv_client=mock_cv_client)

    mock_cv_client.start_change_control.assert_not_called()
    mock_cv_client.wait_for_change_control_state.assert_not_called()
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
