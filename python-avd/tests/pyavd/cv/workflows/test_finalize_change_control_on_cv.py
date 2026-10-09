# Copyright (c) 2025-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from unittest.mock import MagicMock, call

import pytest

from pyavd._cv.api.arista.changecontrol.v1 import ChangeControlStatus
from pyavd._cv.client.exceptions import CVChangeControlFailed, CVResourceInvalidState
from pyavd._cv.workflows.finalize_change_control_on_cv import finalize_change_control_on_cv, get_change_control_state
from pyavd._cv.workflows.models import AvdChangeControl, CVChangeControl

from .helpers import DEFAULT_TIMESTAMP, create_grpc_change_control


@pytest.mark.parametrize(
    ("status", "approved", "error", "expected_state"),
    [
        pytest.param(ChangeControlStatus.COMPLETED, False, None, "completed", id="completed"),
        pytest.param(ChangeControlStatus.COMPLETED, True, None, "completed", id="completed-approved"),
        pytest.param(ChangeControlStatus.RUNNING, False, None, "running", id="running"),
        pytest.param(ChangeControlStatus.RUNNING, True, None, "running", id="running-approved"),
        pytest.param(ChangeControlStatus.SCHEDULED, False, None, "scheduled", id="scheduled"),
        pytest.param(ChangeControlStatus.SCHEDULED, True, None, "scheduled", id="scheduled-approved"),
        pytest.param(ChangeControlStatus.NOT_STARTED, False, None, "pending approval", id="not-started-pending-approval"),
        pytest.param(ChangeControlStatus.NOT_STARTED, True, None, "approved", id="not-started-approved"),
        pytest.param(ChangeControlStatus.UNSPECIFIED, False, None, "pending approval", id="unspecified-pending-approval"),
        pytest.param(ChangeControlStatus.UNSPECIFIED, True, None, "approved", id="unspecified-approved"),
        pytest.param(ChangeControlStatus.COMPLETED, False, "Something went wrong", "completed", id="completed-failed"),
        pytest.param(ChangeControlStatus.COMPLETED, True, "Something went wrong", "completed", id="completed-approved-failed"),
        pytest.param(ChangeControlStatus.RUNNING, False, "Something went wrong", "running", id="running-failed"),
        pytest.param(ChangeControlStatus.RUNNING, True, "Something went wrong", "running", id="running-approved-failed"),
        pytest.param(ChangeControlStatus.SCHEDULED, False, "Something went wrong", "scheduled", id="scheduled-failed"),
        pytest.param(ChangeControlStatus.SCHEDULED, True, "Something went wrong", "scheduled", id="scheduled-approved-failed"),
        pytest.param(ChangeControlStatus.UNSPECIFIED, False, "Something went wrong", "failed", id="unspecified-failed"),
        pytest.param(ChangeControlStatus.UNSPECIFIED, True, "Something went wrong", "approved", id="unspecified-approved-failed"),
        pytest.param(ChangeControlStatus.NOT_STARTED, False, "Something went wrong", "failed", id="not-started-failed"),
        pytest.param(ChangeControlStatus.NOT_STARTED, True, "Something went wrong", "approved", id="not-started-approved-failed"),
    ],
)
def test_get_change_control_state(status: ChangeControlStatus, approved: bool, error: str | None, expected_state: str) -> None:
    """Test that every supported Change Control status is mapped explicitly."""
    cv_change_control = create_grpc_change_control(status=status, approved=approved, error=error)

    assert get_change_control_state(cv_change_control) == expected_state


@pytest.mark.parametrize(
    ("approved", "error"),
    [
        pytest.param(False, None, id="pending-approval"),
        pytest.param(True, None, id="approved"),
        pytest.param(False, "Something went wrong", id="failed"),
        pytest.param(True, "Something went wrong", id="approved-failed"),
    ],
)
def test_get_change_control_state_rejects_unknown_status(approved: bool, error: str | None) -> None:
    """Test that unknown open-enum values raise a clear state error."""
    cv_change_control = create_grpc_change_control(status=ChangeControlStatus.try_value(99), approved=approved, error=error)
    cv_change_control.key.id = "cc_id_1"

    with pytest.raises(
        CVResourceInvalidState,
        match="Cannot finalize Change Control 'cc_id_1' with unknown CloudVision status value '99'",
    ):
        get_change_control_state(cv_change_control)


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
