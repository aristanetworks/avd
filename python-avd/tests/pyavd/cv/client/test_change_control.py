# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from datetime import UTC, datetime
from typing import TYPE_CHECKING, cast

import pytest

from pyavd._cv.api.arista.changecontrol.v1 import ChangeControlStatus

if TYPE_CHECKING:
    from aristaproto import _DateTime

    from pyavd._cv.client import CVClient


@pytest.mark.asyncio
@pytest.mark.parametrize("cv_client", [{"static_recording": True}], ids=["CV_CLIENT_STATIC_RECORDINGS"], indirect=True)
async def test_unapprove_change_control(cv_client: CVClient) -> None:
    """
    Test that unapproving a Change Control updates its approval state while preserving its execution state.

    Exact test steps:
    -   description: Fetch initial state of the Change Control (Approved)
        request: 'ChangeControlRequest(key=ChangeControlKey(id='qyUnE6mfxhuDHibRgrr6S'), '
            'time=datetime.datetime(2026, 9, 22, 15, 10, 41, 38832, tzinfo=datetime.timezone.utc))'
        targeted_file: 'arista.changecontrol.v1.ChangeControlService/GetOne/www.cv-prod-us-central1-c.arista.io/fe60294f789bf41c7f202897c5c944f7c28996b0.json'

    -   description: Unapprove Change Control
        request: 'ApproveConfigSetRequest(value=ApproveConfig(key=ChangeControlKey(id='qyUnE6mfxhuDHibRgrr6S'), '
            'approve=FlagConfig(value=False, notes='Unapproval note'), version=datetime.datetime(2026, 9, 22, 5, 27, 10, 522805)))'
        targeted_file: 'arista.changecontrol.v1.ApproveConfigService/Set/www.cv-prod-us-central1-c.arista.io/6f512987a05989e1c64f0d7e77ae4401b4e09a3f.json'

    -   description: Fetch updated state of the Change Control (Unapproved)
        request: 'ChangeControlRequest(key=ChangeControlKey(id='qyUnE6mfxhuDHibRgrr6S'), '
            'time=datetime.datetime(2026, 9, 22, 15, 10, 41, 346148, tzinfo=datetime.timezone.utc))'
        targeted_file: 'arista.changecontrol.v1.ChangeControlService/GetOne/www.cv-prod-us-central1-c.arista.io/d31bdeb4325d47520cc9d09856513f4e75789057.json'
    """
    change_control_id = "qyUnE6mfxhuDHibRgrr6S"

    change_control_initial_timestamp = datetime(2026, 9, 22, 15, 10, 41, 38832, tzinfo=UTC)
    change_control_initial_state = await cv_client.get_change_control(change_control_id=change_control_id, time=change_control_initial_timestamp)
    assert change_control_initial_state.key.id == change_control_id
    assert change_control_initial_state.approve.value is True
    assert change_control_initial_state.approve.notes == "Approval note"
    assert change_control_initial_state.status == ChangeControlStatus.NOT_STARTED

    unapprove_response = await cv_client.unapprove_change_control(
        change_control_id=change_control_id,
        timestamp=cast("_DateTime", change_control_initial_state.change.time),
        description="Unapproval note",
    )
    assert unapprove_response.key.id == change_control_id
    assert unapprove_response.approve.value is False
    assert unapprove_response.approve.notes == "Unapproval note"
    assert unapprove_response.version == change_control_initial_state.change.time

    change_control_final_timestamp = datetime(2026, 9, 22, 15, 10, 41, 346148, tzinfo=UTC)
    change_control_final_state = await cv_client.get_change_control(change_control_id=change_control_id, time=change_control_final_timestamp)
    assert change_control_final_state.key.id == change_control_id
    assert change_control_final_state.approve.value is False
    assert change_control_final_state.approve.notes == "Unapproval note"
    assert change_control_final_state.status == ChangeControlStatus.NOT_STARTED
    assert change_control_final_state.change.time == change_control_initial_state.change.time
