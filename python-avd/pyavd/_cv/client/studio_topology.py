# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from logging import getLogger
from typing import TYPE_CHECKING, Literal, Protocol

from pyavd._cv.api.arista.studio_topology.v1 import (
    Decommission,
    DecommissionConfig,
    DecommissionConfigServiceStub,
    DecommissionConfigSetSomeRequest,
    DecommissionServiceStub,
    DecommissionStatus,
    DecommissionStreamRequest,
    DeviceKey,
)
from pyavd._cv.client.exceptions import CVDeviceDecommissionFailed

from .async_decorators import GRPCRequestHandler, LimitCvVersion
from .constants import DEFAULT_API_TIMEOUT

if TYPE_CHECKING:
    from . import CVClientProtocol


LOGGER = getLogger(__name__)

TOPOLOGY_STUDIO_ID = "TOPOLOGY"


class StudioTopologyMixin(Protocol):
    """Only to be used as mixin on CVClient class."""

    studio_topology_api_version: Literal["v1"] = "v1"

    @LimitCvVersion(min_ver="2025.1.0")
    @GRPCRequestHandler(list_field="device_ids", check_bulk_response_errors=True)
    async def decommission_devices(
        self: CVClientProtocol,
        workspace_id: str,
        device_ids: list[str] | None = None,
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> list[tuple[DeviceKey, str]]:
        """
        Decommission devices using arista.studio_topology.v1.DecommissionConfigService.SetSome API.

        Parameters:
            workspace_id: Unique identifier of the Workspace for which the information is set.
            device_ids: List of Device IDs / serial_numbers to decommission.
            timeout: Timeout in seconds.

        Returns:
            List of (<DeviceKey>, <gRPC error message>) tuples for devices that failed to be decommissioned due to encountered gRPC error.
        """
        request = DecommissionConfigSetSomeRequest(
            values=[DecommissionConfig(key=DeviceKey(device_id=device_id, workspace_id=workspace_id)) for device_id in device_ids]
        )
        client = DecommissionConfigServiceStub(self._channel)
        responses = client.set_some(request, metadata=self._metadata, timeout=timeout)

        return [(response.key, response.error) async for response in responses]

    @LimitCvVersion(min_ver="2025.1.0")
    @GRPCRequestHandler()
    async def wait_for_devices_decommission(
        self: CVClientProtocol,
        workspace_id: str,
        device_ids: list[str] | None = None,
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> None:
        """
        Monitor decommissioning of devices using arista.studio_topology.v1.DecommissionService.Subscribe API.

        Block until all Decommission operations reach a SUCCESS status, Stream is closed or timed out.

        Parameters:
            workspace_id: Unique identifier of the Workspace for which the information is set.
            device_ids: List of Device IDs / serial_numbers to decommission.
            timeout: Timeout in seconds.

        Raises:
            CVDeviceDecommissioningFailed: If the stream closed before all devices reached a SUCCESS status or errors are faced.
        """
        request = DecommissionStreamRequest(
            partial_eq_filter=[Decommission(key=DeviceKey(device_id=device_id, workspace_id=workspace_id)) for device_id in device_ids]
        )
        client = DecommissionServiceStub(self._channel)
        responses = client.subscribe(request, metadata=self._metadata, timeout=timeout)

        # Set of device_ids for which we have not yet received a response in terminal status
        remaining_device_ids = set(device_ids)
        # Tracks per-device latest non-success responses
        latest_per_device_nonsuccess_response: dict[str, Decommission] = {}

        async for response in responses:
            device_id = response.value.key.device_id
            current_status = response.value.status
            if current_status == DecommissionStatus.SUCCESS:
                remaining_device_ids.discard(device_id)
                latest_per_device_nonsuccess_response.pop(device_id, None)
                LOGGER.debug(
                    "wait_for_devices_decommission: Decommissioning of device %s succeeded: %s",
                    device_id,
                    response.value,
                )
            # Other terminal status
            elif current_status != DecommissionStatus.UNSPECIFIED:
                remaining_device_ids.discard(device_id)
                latest_per_device_nonsuccess_response[device_id] = response.value
                LOGGER.debug(
                    "wait_for_devices_decommission: Decommissioning of device %s reached non-success terminal status %s: %s",
                    device_id,
                    current_status,
                    response.value,
                )
            # Non-terminal status.
            else:
                LOGGER.debug("wait_for_devices_decommission: Got decommission update: %s", response.value)
                # Avoid tracking INITIAL_SYNC_COMPLETE update referencing no devices
                if device_id:
                    latest_per_device_nonsuccess_response[device_id] = response.value

            # Return as soon as all devices got SUCCESS responses
            if not remaining_device_ids and not latest_per_device_nonsuccess_response:
                return

            # Break async loop if we got terminal responses for all devices and some of them are just not successful.
            if not remaining_device_ids:
                break

        no_response_device_ids = remaining_device_ids - latest_per_device_nonsuccess_response.keys()

        if no_response_device_ids or latest_per_device_nonsuccess_response:
            msg_parts = []
            if no_response_device_ids:
                msg_parts.append(f"No decommission response received for the following devices: {no_response_device_ids}.")
            if latest_per_device_nonsuccess_response:
                msg_parts.append(f"Non-success decommission response received for the following devices: {latest_per_device_nonsuccess_response}.")
            raise CVDeviceDecommissionFailed(" ".join(msg_parts))
