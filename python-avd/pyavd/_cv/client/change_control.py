# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from logging import getLogger
from typing import TYPE_CHECKING, Literal, Protocol

from pyavd._cv.api.arista.changecontrol.v1 import (
    ApproveConfig,
    ApproveConfigServiceStub,
    ApproveConfigSetRequest,
    ChangeConfig,
    ChangeControl,
    ChangeControlConfig,
    ChangeControlConfigServiceStub,
    ChangeControlConfigSetRequest,
    ChangeControlKey,
    ChangeControlRequest,
    ChangeControlServiceStub,
    ChangeControlStatus,
    ChangeControlStreamRequest,
    FlagConfig,
)

from .async_decorators import GRPCRequestHandler
from .constants import DEFAULT_API_TIMEOUT
from .exceptions import CVChangeControlFailed, CVClientException
from .models import get_required_field

if TYPE_CHECKING:
    from datetime import datetime

    from aristaproto.nano_datetime import NanoDatetime

    from . import CVClientProtocol


LOGGER = getLogger(__name__)

CHANGE_CONTROL_STATUS_MAP = {
    "completed": ChangeControlStatus.COMPLETED,
    "unspecified": ChangeControlStatus.UNSPECIFIED,
    "running": ChangeControlStatus.RUNNING,
    "scheduled": ChangeControlStatus.SCHEDULED,
}


class ChangeControlMixin(Protocol):
    """Only to be used as mixin on CVClient class."""

    workspace_api_version: Literal["v1"] = "v1"

    @GRPCRequestHandler()
    async def get_change_control(
        self: CVClientProtocol,
        change_control_id: str,
        time: datetime | None = None,
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> ChangeControl:
        """
        Get Change Control using arista.changecontrol.v1.ChangeControlService.GetOne API.

        Parameters:
            change_control_id: Unique identifier of the Change Control.
            time: Timestamp from which the information is fetched. `now()` if not set.
            timeout: Timeout in seconds.

        Returns:
            ChangeControl object matching the change_control_id
        """
        request = ChangeControlRequest(
            key=ChangeControlKey(id=change_control_id),
            time=time,
        )
        client = self.new_stub(ChangeControlServiceStub)

        response = await client.get_one(request, timeout=timeout)
        if response.value is None:
            msg = f"CloudVision returned an empty Change Control response for '{change_control_id}'."
            raise CVClientException(msg)

        return response.value

    @GRPCRequestHandler()
    async def set_change_control(
        self: CVClientProtocol,
        change_control_id: str,
        name: str | None = None,
        description: str | None = None,
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> ChangeControlConfig:
        """
        Set Change Control details using arista.changecontrol.v1.ChangeControlConfigService.Set API.

        Parameters:
            change_control_id: Unique identifier of the Change Control.
            name: Change Control Name.
            description: Change Control description.
            TODO: Add CC template
            timeout: Timeout in seconds.

        Returns:
            ChangeControlConfig object after being set including any server-generated values.
        """
        request = ChangeControlConfigSetRequest(
            value=ChangeControlConfig(
                key=ChangeControlKey(id=change_control_id),
                change=ChangeConfig(name=name, notes=description),
            ),
        )
        client = self.new_stub(ChangeControlConfigServiceStub)

        response = await client.set(request, timeout=timeout)
        return get_required_field(response, "value", response.value)

    @GRPCRequestHandler()
    async def approve_change_control(
        self: CVClientProtocol,
        change_control_id: str,
        timestamp: NanoDatetime | datetime,
        description: str | None = None,
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> ApproveConfig:
        """
        Get Change Control using arista.changecontrol.v1.ChangeControlService.GetOne API.

        Parameters:
            change_control_id: Unique identifier of the Change Control.
            timestamp: Timestamp for the change control information to be approved. \
                This must be using the aristaproto._DateTime subclass which contains nanosecond information.
            description: Description to set on the approval.
            timeout: Timeout in seconds.

        Returns:
            ApproveConfig object carrying all the values given in the ApproveConfigSetRequest as well
            as any server-generated values.
        """
        request = ApproveConfigSetRequest(
            value=ApproveConfig(
                key=ChangeControlKey(id=change_control_id),
                approve=FlagConfig(value=True, notes=description),
                version=timestamp,
            ),
        )
        client = self.new_stub(ApproveConfigServiceStub)

        response = await client.set(request, timeout=timeout)
        if response.value is None:
            msg = f"CloudVision returned an empty Change Control approval response for '{change_control_id}'."
            raise CVClientException(msg)

        return response.value

    @GRPCRequestHandler()
    async def start_change_control(
        self: CVClientProtocol,
        change_control_id: str,
        description: str | None = None,
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> ChangeControlConfig:
        """
        Set Change Control details using arista.changecontrol.v1.ChangeControlConfigService.Set API.

        Parameters:
            change_control_id: Unique identifier of the Change Control.
            description: Description to add for the start request.
            timeout: Timeout in seconds.

        Returns:
            ChangeControlConfig object including any server-generated values.
        """
        request = ChangeControlConfigSetRequest(
            value=ChangeControlConfig(
                key=ChangeControlKey(id=change_control_id),
                start=FlagConfig(value=True, notes=description),
            ),
        )
        client = self.new_stub(ChangeControlConfigServiceStub)

        response = await client.set(request, timeout=timeout)
        if response.value is None:
            msg = f"CloudVision returned an empty Change Control start response for '{change_control_id}'."
            raise CVClientException(msg)

        return response.value

    @GRPCRequestHandler(retry_on_stream_reset=True)
    async def wait_for_change_control_state(
        self: CVClientProtocol,
        cc_id: str,
        state: Literal["completed", "unspecified", "running", "scheduled"],
        timeout: float = 3600.0,
    ) -> ChangeControl:
        """
        Monitor a Change control using arista.changecontrol.v1.ChangeControlService.Subscribe API for a response to the given cc_id.

        Blocks until a response is returned or timed out.

        Parameters:
            cc_id: Unique identifier of the change control.
            state: Change Control state to wait for.
            timeout: Timeout in seconds for the Change Control to reach the expected state.

        Returns:
            Full change control object
        """
        request = ChangeControlStreamRequest(
            partial_eq_filter=[
                ChangeControl(
                    key=ChangeControlKey(id=cc_id),
                ),
            ],
        )
        client = self.new_stub(ChangeControlServiceStub)
        responses = client.subscribe(request, timeout=timeout)
        async for response in responses:
            LOGGER.debug("wait_for_change_control_complete: Response is '%s.'", response)
            if response.value is None:
                LOGGER.debug("wait_for_change_control_complete: Got change control update without value: %s", response)
                continue

            change_control = response.value
            if change_control.status == CHANGE_CONTROL_STATUS_MAP[state]:
                LOGGER.info("wait_for_change_control_complete: Got response for request '%s': %s", cc_id, change_control.status)
                return change_control

        # Use case where stream completed without getting ChangeControl update in the desired state
        msg = f"Change control '{cc_id}' has not reached desired state '{state}'."
        raise CVChangeControlFailed(msg)
