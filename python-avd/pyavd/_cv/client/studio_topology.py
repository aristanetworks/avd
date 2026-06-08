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
    async def stage_devices_for_decommission(
        self: CVClientProtocol,
        workspace_id: str,
        device_ids: list[str],
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> list[tuple[DeviceKey, str]]:
        """
        Stage devices for decommission using arista.studio_topology.v1.DecommissionConfigService.SetSome API.

        Parameters:
            workspace_id: Unique identifier of the Workspace for which the information is set.
            device_ids: List of Device IDs / serial_numbers to decommission.
            timeout: Timeout in seconds.

        Returns:
            List of (<DeviceKey>, <gRPC error message>) tuples for devices that failed to be staged for decommission due to encountered CloudVision error(s).
        """
        request = DecommissionConfigSetSomeRequest(
            values=[DecommissionConfig(key=DeviceKey(device_id=device_id, workspace_id=workspace_id)) for device_id in device_ids]
        )
        client = DecommissionConfigServiceStub(self._channel)
        responses = client.set_some(request, metadata=self._metadata, timeout=timeout)

        return [(response.key, response.error) async for response in responses]

    @LimitCvVersion(min_ver="2025.1.0")
    @GRPCRequestHandler()
    async def wait_for_device_decommission_staging(
        self: CVClientProtocol,
        workspace_id: str,
        device_ids: list[str],
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> list[Decommission]:
        """
        Wait for staging of the devices for decommissioning to succeed using arista.studio_topology.v1.DecommissionService.Subscribe API.

        Block until all Decommission operations reach SUCCESS status, Stream is closed or timed out.

        Parameters:
            workspace_id: Unique identifier of the Workspace for which the information is set.
            device_ids: List of Device IDs / serial_numbers to decommission.
            timeout: Timeout in seconds.

        Returns:
            List of Decommission objects for all devices.

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
        # Tracks per-device latest failure responses
        latest_per_device_failure_response: dict[str, Decommission] = {}
        successful_responses: list[Decommission] = []

        async for response in responses:
            device_id = response.value.key.device_id
            current_status = response.value.status
            if current_status == DecommissionStatus.UNSPECIFIED:
                # Non-terminal status. Includes the INITIAL_SYNC_COMPLETE update which references no device.
                LOGGER.debug("wait_for_device_decommission_staging: Got decommission staging update: %s", response.value)
                # Avoid tracking INITIAL_SYNC_COMPLETE update referencing no devices
                # TODO: Figure out a way to test
                if device_id:
                    latest_per_device_failure_response[device_id] = response.value
            elif device_id:
                if current_status == DecommissionStatus.SUCCESS:
                    remaining_device_ids.discard(device_id)
                    latest_per_device_failure_response.pop(device_id, None)
                    successful_responses.append(response.value)
                    LOGGER.debug(
                        "wait_for_device_decommission_staging: Staging device %s for decommission succeeded: %s",
                        device_id,
                        response.value,
                    )
                # Other terminal status
                else:
                    remaining_device_ids.discard(device_id)
                    latest_per_device_failure_response[device_id] = response.value
                    LOGGER.debug(
                        "wait_for_device_decommission_staging: Staging device %s for decommission failed: %s",
                        device_id,
                        response.value,
                    )

            # Return as soon as all devices got SUCCESS responses
            if not remaining_device_ids and not latest_per_device_failure_response:
                return successful_responses

            # Break async loop if we got terminal responses for all devices and some of them are just not successful.
            if not remaining_device_ids:
                break

        no_response_device_ids = remaining_device_ids - latest_per_device_failure_response.keys()

        if no_response_device_ids or latest_per_device_failure_response:
            msg_parts = []
            if no_response_device_ids:
                msg_parts.append(f"No decommission staging response received for the following devices: {no_response_device_ids}.")
            if latest_per_device_failure_response:
                msg_parts.append(f"Decommission staging failed for the following devices: {latest_per_device_failure_response}.")
            raise CVDeviceDecommissionFailed(" ".join(msg_parts))
        # Kept only to satisfy ruff's RET503.
        return successful_responses  # pragma: no cover
