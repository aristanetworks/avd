# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from datetime import UTC, datetime
from typing import TYPE_CHECKING
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from aristaproto import _Timestamp

from pyavd._cv.api.arista.changecontrol.v1 import ApproveConfig, ChangeControlKey, FlagConfig

if TYPE_CHECKING:
    from pyavd._cv.client import CVClient


@pytest.mark.asyncio
async def test_unapprove_change_control(cv_client: CVClient) -> None:
    """Test that unapproving a Change Control sends the unapproval flag, note, and required version."""
    # Use _Timestamp conversion to initialize the private nanosecond value required by aristaproto serialization.
    timestamp = _Timestamp.from_datetime(datetime(2025, 10, 3, tzinfo=UTC)).to_datetime()
    response = ApproveConfig(
        key=ChangeControlKey(id="cc_id_1"),
        approve=FlagConfig(value=False, notes="Unapproved by operator"),
        version=timestamp,
    )
    set_method = AsyncMock(return_value=MagicMock(value=response))

    with patch("pyavd._cv.client.change_control.ApproveConfigServiceStub.set", set_method):
        result = await cv_client.unapprove_change_control(
            change_control_id="cc_id_1",
            timestamp=timestamp,
            description="Unapproved by operator",
        )

    set_method.assert_called_once()
    request = set_method.call_args.args[0]
    assert request.value.key.id == "cc_id_1"
    assert request.value.approve.value is False
    assert request.value.approve.notes == "Unapproved by operator"
    assert request.value.version == timestamp
    assert result == response
