# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Literal, Protocol

from pyavd._cv.api.arista.studio_topology.v1 import DecommissionConfig, DecommissionConfigServiceStub, DecommissionConfigSetSomeRequest, DeviceKey

from .async_decorators import GRPCRequestHandler
from .constants import DEFAULT_API_TIMEOUT

if TYPE_CHECKING:
    from . import CVClientProtocol


class StudioTopologyMixin(Protocol):
    """Only to be used as mixin on CVClient class."""

    studio_topology_api_version: Literal["v1"] = "v1"

    @GRPCRequestHandler()
    async def decommission_device(
        self: CVClientProtocol,
        device_ids: list[str],
        workspace_id: str,
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> list[DecommissionConfig]:
        """
        Decommission devices using arista.studio_topology.v1.DecommissionConfigService.SetSome API.

        Parameters:
            device_ids: Device IDs to decommission.
            workspace_id: Workspace ID to decommission the devices from.
            timeout: Timeout in seconds.

        Returns:
            List of DecommissionConfig objects.
        """
        decommission_configs = [DecommissionConfig(key=DeviceKey(device_id=device_id, workspace_id=workspace_id)) for device_id in device_ids]
        request = DecommissionConfigSetSomeRequest(decommission_configs)
        client = DecommissionConfigServiceStub(self._channel)
        responses = client.set_some(request, metadata=self._metadata, timeout=timeout)

        return [response.key async for response in responses]
