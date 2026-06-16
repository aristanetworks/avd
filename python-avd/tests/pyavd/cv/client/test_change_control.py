# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING
from unittest.mock import patch

import pytest

from pyavd._cv.api.arista.changecontrol.v1 import ChangeControl, ChangeControlKey, ChangeControlStatus, ChangeControlStreamResponse
from pyavd._cv.api.arista.subscriptions import Operation

if TYPE_CHECKING:
    from collections.abc import AsyncIterator

    from pyavd._cv.client import CVClient


@pytest.mark.asyncio
@pytest.mark.parametrize("cv_client", [{"static_recording": True}], ids=["CV_CLIENT_STATIC_RECORDINGS"], indirect=True)
async def test_wait_for_change_control_state_skips_empty_stream_responses(cv_client: CVClient) -> None:
    """Empty subscription notifications must not hide later ChangeControl updates."""

    async def async_iterator_with_empty_response() -> AsyncIterator[ChangeControlStreamResponse]:
        yield ChangeControlStreamResponse(type=Operation.INITIAL_SYNC_COMPLETE)
        yield ChangeControlStreamResponse(
            value=ChangeControl(
                key=ChangeControlKey(id="cc_id_1"),
                status=ChangeControlStatus.COMPLETED,
            ),
            type=Operation.UPDATED,
        )

    with patch(
        "pyavd._cv.client.change_control.ChangeControlServiceStub.subscribe",
        return_value=async_iterator_with_empty_response(),
    ):
        response = await cv_client.wait_for_change_control_state(cc_id="cc_id_1", state="completed")

    assert response.status == ChangeControlStatus.COMPLETED
