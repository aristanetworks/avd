# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Literal, Protocol

from pyavd._cv.api.arista.inventory.v1 import Device, DeviceKey, DeviceServiceStub, DeviceStreamRequest
from pyavd._cv.api.arista.time import TimeBounds

from .async_decorators import GRPCRequestHandler
from .constants import DEFAULT_API_TIMEOUT
from .models import get_required_field

if TYPE_CHECKING:
    from collections.abc import Collection
    from datetime import datetime

    from . import CVClientProtocol


class InventoryMixin(Protocol):
    """Only to be used as mixin on CVClient class."""

    inventory_api_version: Literal["v1"] = "v1"

    @GRPCRequestHandler(retry_on_stream_reset=True)
    async def get_inventory_devices(
        self: CVClientProtocol,
        devices: Collection[tuple[str | None, str | None, str | None]] | None = None,
        time: datetime | None = None,
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> list[Device]:
        """
        Get Devices using arista.inventory.v1.DeviceService.GetAll API.

        If 'devices' is set to None, all devices will be returned.

        Parameters:
            devices: Set of tuples where each tuple is in the format (serial number, system_mac_address, hostname)
            time: Timestamp from which the information is fetched. `now()` if not set.
            timeout: Timeout in seconds.

        Returns:
            Device objects.
        """
        request = DeviceStreamRequest(partial_eq_filter=[], time=TimeBounds(start=None, end=time) if time else None)
        if devices:
            for serial_number, system_mac_address, hostname in devices:
                device_filter = Device()
                if serial_number is not None:
                    device_filter.key = DeviceKey(device_id=serial_number)
                if system_mac_address is not None:
                    device_filter.system_mac_address = system_mac_address
                if hostname is not None:
                    device_filter.hostname = hostname
                request.partial_eq_filter.append(device_filter)
        client = self.new_stub(DeviceServiceStub)
        responses = client.get_all(request, timeout=timeout)

        return [get_required_field(response, "value", response.value) async for response in responses]
