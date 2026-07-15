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
from pyavd._cv.client.exceptions import CVTimeoutError

from .async_decorators import GRPCRequestHandler, LimitCvVersion
from .constants import DEFAULT_API_TIMEOUT

if TYPE_CHECKING:
    from . import CVClientProtocol


LOGGER = getLogger(__name__)


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
    @GRPCRequestHandler(retry_on_stream_reset=True)
    async def wait_for_device_decommission_staging(
        self: CVClientProtocol,
        workspace_id: str,
        device_ids: list[str],
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> list[Decommission]:
        """
        Wait for staging of the devices for decommissioning to finish using arista.studio_topology.v1.DecommissionService.Subscribe API.

        Block until all Decommission operations reach terminal status, Stream is closed or timed out.

        Parameters:
            workspace_id: Unique identifier of the Workspace for which the information is set.
            device_ids: List of Device IDs / serial_numbers to decommission.
            timeout: Timeout in seconds.

        Returns:
            List of Decommission objects for all requested devices.

        Raises:
            CVTimeoutError: If the stream closed before all devices reached a terminal status.
        """
        request = DecommissionStreamRequest(
            partial_eq_filter=[Decommission(key=DeviceKey(device_id=device_id, workspace_id=workspace_id)) for device_id in device_ids]
        )
        client = DecommissionServiceStub(self._channel)
        responses = client.subscribe(request, metadata=self._metadata, timeout=timeout)

        # Set of device_ids for which we have not yet received a response in terminal status
        devices_missing_terminal_response = set(device_ids)
        terminal_responses: list[Decommission] = []

        async for response in responses:
            device_id = response.value.key.device_id
            # Explicitly access status field to make sure the default value is revealed by __repr__
            status = response.value.status
            if device_id and status in (DecommissionStatus.SUCCESS, DecommissionStatus.FAILURE):
                LOGGER.debug(
                    "wait_for_device_decommission_staging: Staging device %s for decommission completed: %s",
                    device_id,
                    response.value,
                )
                devices_missing_terminal_response.discard(device_id)
                terminal_responses.append(response.value)
            else:
                LOGGER.debug("wait_for_device_decommission_staging: Received decommission staging response: %s", response.value)

            # Return as soon as terminal responses received for all devices
            if not devices_missing_terminal_response:
                return terminal_responses

        if devices_missing_terminal_response:
            msg = f"Decommission staging timed out for the following devices: {devices_missing_terminal_response}."
            raise CVTimeoutError(msg)

        # Kept only to satisfy ruff's RET503.
        return terminal_responses  # pragma: no cover
