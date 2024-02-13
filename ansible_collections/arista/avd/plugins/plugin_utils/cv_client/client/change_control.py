# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Literal

from ..api.arista.changecontrol.v1 import (
    ApproveConfig,
    ApproveConfigServiceStub,
    ApproveConfigSetRequest,
    ChangeConfig,
    ChangeControl,
    ChangeControlConfig,
    ChangeControlConfigServiceStub,
    ChangeControlConfigSetRequest,
    ChangeControlConfigSetResponse,
    ChangeControlKey,
    ChangeControlRequest,
    ChangeControlServiceStub,
    FlagConfig,
)
from .exceptions import get_cv_client_exception

if TYPE_CHECKING:
    from aristaproto import _DateTime

    from .cv_client import CVClient


class ChangeControlMixin:
    """
    Only to be used as mixin on CVClient class.
    """

    workspace_api_version: Literal["v1"] = "v1"

    async def get_change_control(
        self: CVClient,
        change_control_id: str,
        time: datetime | None = None,
        timeout: float = 10.0,
    ) -> ChangeControl:
        """
        Get Change Control using arista.changecontrol.v1.ChangeControlService.GetOne API

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
        client = ChangeControlServiceStub(self._channel)

        try:
            response = await client.get_one(request, metadata=self._metadata, timeout=timeout)
            return response.value

        except Exception as e:
            raise get_cv_client_exception(e, f"Change Control ID '{change_control_id}'") or e

    async def set_change_control(
        self: CVClient,
        change_control_id: str,
        name: str | None = None,
        description: str | None = None,
        timeout: float = 10.0,
    ) -> ChangeControlConfigSetResponse:
        """
        Set Change Control details using arista.changecontrol.v1.ChangeControlConfigService.Set API

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
            )
        )
        client = ChangeControlConfigServiceStub(self._channel)

        try:
            response = await client.set(request, metadata=self._metadata, timeout=timeout)
            return response.value

        except Exception as e:
            raise get_cv_client_exception(e, f"Change Control ID '{change_control_id}'") or e

    async def approve_change_control(
        self: CVClient,
        change_control_id: str,
        timestamp: _DateTime,
        description: str | None = None,
        timeout: float = 10.0,
    ) -> ApproveConfig:
        """
        Get Change Control using arista.changecontrol.v1.ChangeControlService.GetOne API

        Parameters:
            change_control_id: Unique identifier the Change Control.
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
            )
        )
        client = ApproveConfigServiceStub(self._channel)

        try:
            response = await client.set(request, metadata=self._metadata, timeout=timeout)
            return response.value

        except Exception as e:
            raise get_cv_client_exception(e, f"Approving Change Control ID '{change_control_id}' for timestamp '{timestamp}'") or e

    async def start_change_control(
        self: CVClient,
        change_control_id: str,
        description: str | None = None,
        timeout: float = 10.0,
    ) -> ChangeControlConfig:
        """
        Set Change Control details using arista.changecontrol.v1.ChangeControlConfigService.Set API

        Parameters:
            change_control_id: Unique identifier the Change Control.
            description: Description to add for the start request.
            timeout: Timeout in seconds.

        Returns:
            ChangeControlConfig object including any server-generated values.
        """
        request = ChangeControlConfigSetRequest(
            value=ChangeControlConfig(
                key=ChangeControlKey(id=change_control_id),
                start=FlagConfig(value=True, notes=description),
            )
        )
        client = ChangeControlConfigServiceStub(self._channel)

        try:
            response = await client.set(request, metadata=self._metadata, timeout=timeout)
            return response.value

        except Exception as e:
            raise get_cv_client_exception(e, f"Change Control ID '{change_control_id}'") or e
