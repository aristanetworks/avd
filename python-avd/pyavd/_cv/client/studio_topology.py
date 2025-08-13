# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import json
from logging import getLogger
from typing import TYPE_CHECKING, Literal, Protocol

from aristaproto import Casing

from pyavd._cv.api.arista.studio.v1 import (
    InputsConfig,
    InputsConfigServiceStub,
    InputsConfigSetSomeRequest,
    InputsKey,
)
from pyavd._cv.api.arista.studio_topology.v1 import (
    Decommission,
    DecommissionConfig,
    DecommissionConfigServiceStub,
    DecommissionConfigSetSomeRequest,
    DecommissionServiceStub,
    DecommissionStatus,
    DecommissionStreamRequest,
    DeviceInfo,
    DeviceInputConfig,
    DeviceInputConfigServiceStub,
    DeviceInputConfigSetSomeRequest,
    DeviceKey,
    DeviceState,
    DeviceStateServiceStub,
    DeviceStateStreamRequest,
)
from pyavd._cv.api.arista.time import TimeBounds
from pyavd._cv.api.fmp import MacAddress, RepeatedString

from .async_decorators import GRPCRequestHandler
from .constants import DEFAULT_API_TIMEOUT
from .exceptions import CVDecommissioningFailed

if TYPE_CHECKING:
    from datetime import datetime

    from . import CVClientProtocol

LOGGER = getLogger(__name__)

GRPCRequestHandler.max_retries = 25

DECOMMISSION_STATUS_MAP = {"unspecified": DecommissionStatus.UNSPECIFIED, "success": DecommissionStatus.SUCCESS, "failure": DecommissionStatus.FAILURE}

TOPOLOGY_STUDIO_ID = "TOPOLOGY"


class StudioTopologyMixin(Protocol):
    """Only to be used as mixin on CVClient class."""

    async def get_studio_topology(
        self: CVClientProtocol,
        workspace_id: str,
        device_ids: list[str] | None = None,
        time: datetime | None = None,
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> list[dict]:
        """
        Get Studio Topology using either studio inputs API or studio_topology API depending on the supported APIs.

        Parameters:
            workspace_id: Unique identifier of the Workspace for which the information is fetched. Use "" for mainline.
            device_ids: List of Device IDs / Serial numbers to get inputs for. If not given, all devices are returned.
            time: Timestamp from which the information is fetched. `now()` if not set.
            timeout: Timeout in seconds.

        Returns:
            TopologyInput objects for the requested devices.
        """
        LOGGER.info("get_studio_topology: Trying the legacy Topology Studio Inputs API")
        try:
            return await self.get_topology_studio_inputs(workspace_id, device_ids, time, timeout)
        except Exception as e:
            # The old API is not working. Try the new.
            LOGGER.info("get_studio_topology: Failed the legacy Topology Studio Inputs API, %s", e)

        LOGGER.info("get_studio_topology: Trying the New Studio Topology API")
        return await self._get_studio_topology(workspace_id, device_ids, time, timeout)

    @GRPCRequestHandler()
    async def _get_studio_topology(
        self: CVClientProtocol,
        workspace_id: str,
        device_ids: list[str] | None = None,
        time: datetime | None = None,
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> list[dict]:
        """
        Get Studio Topology using arista.studio_topology.v1.GetAll API.

        Parameters:
            workspace_id: Unique identifier of the Workspace for which the information is fetched. Use "" for mainline.
            device_ids: List of Device IDs / Serial numbers to get inputs for. If not given, all devices are returned.
            time: Timestamp from which the information is fetched. `now()` if not set.
            timeout: Timeout in seconds.

        Returns:
            TopologyInput objects for the requested devices.
        """
        topology_inputs: list[dict] = []
        request = DeviceStateStreamRequest(partial_eq_filter=[DeviceState(key=DeviceKey(workspace_id=workspace_id))], time=TimeBounds(start=None, end=time))

        client = DeviceStateServiceStub(self._channel)

        responses = client.get_all(request, metadata=self._metadata, timeout=timeout)
        async for response in responses:
            device_state = response.value
            if device_ids and device_state.key.device_id not in device_ids:
                continue
            device_info = device_state.device_info.to_dict(casing=Casing.SNAKE)
            # MAC address is wrapped in a special fmp object. Unwrapping.
            device_info["mac_address"] = device_state.device_info.mac_address.value
            device_info["interfaces"] = [interface_info.to_dict(casing=Casing.SNAKE) for interface_info in device_state.interface_infos.values]
            topology_inputs.append(device_info)

        return topology_inputs

    async def get_topology_studio_inputs(
        self: CVClientProtocol,
        workspace_id: str,
        device_ids: list[str] | None = None,
        time: datetime | None = None,
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> list[dict]:
        """
        Get Topology Studio Inputs using arista.studio.v1.InputsService.GetAll and arista.studio.v1.InputsConfigService.GetAll APIs.

        Parameters:
            workspace_id: Unique identifier of the Workspace for which the information is fetched. Use "" for mainline.
            device_ids: List of Device IDs / Serial numbers to get inputs for. If not given, all devices are returned.
            time: Timestamp from which the information is fetched. `now()` if not set.
            timeout: Timeout in seconds.

        Returns:
            TopologyInput objects for the requested devices.
        """
        topology_inputs: list[dict] = []
        studio_inputs: dict = await self.get_studio_inputs(
            studio_id=TOPOLOGY_STUDIO_ID,
            workspace_id=workspace_id,
            default_value={},
            time=time,
            timeout=timeout,
        )
        for device_entry in studio_inputs.get("devices", []):
            if not isinstance(device_entry, dict):
                continue
            device_id = str(device_entry.get("tags", {}).get("query", "")).removeprefix("device:")

            # Ignore the device if it is not one of the requested devices.
            if device_ids and device_id not in device_ids:
                continue

            device_info: dict = device_entry.get("inputs", {}).get("device", {})
            interfaces: list[dict] = device_info.get("interfaces", [])
            topology_inputs.append(
                {
                    "device_id": device_id,
                    "hostname": device_info.get("hostname"),
                    "mac_address": device_info.get("macAddress"),
                    "model_name": device_info.get("modelName"),
                    "interfaces": [
                        {
                            "name": str(interface.get("tags", {}).get("query", "")).removeprefix("interface:").split("@", maxsplit=1)[0],
                            "neighbor_device_id": interface.get("inputs", {}).get("interface", {}).get("neighborDeviceId"),
                            "neighbor_interface_name": interface.get("inputs", {}).get("interface", {}).get("neighborInterfaceName"),
                        }
                        for interface in interfaces
                    ],
                },
            )
        return topology_inputs

    @GRPCRequestHandler()
    async def set_studio_topology(
        self: CVClientProtocol,
        workspace_id: str,
        device_inputs: list[tuple[str, str, str]],
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> None:
        """
        Set Studio Topology using either studio inputs API or studio_topology API depending on the supported APIs.

        Parameters:
            workspace_id: Unique identifier of the Workspace for which the information is set.
            device_inputs: List of Tuples with the format (<device_id>, <hostname>, <system_mac>).
            timeout: Base timeout in seconds. 0.1 second will be added per device.
        """
        LOGGER.info("set_studio_topology: Trying the legacy Topology Studio Inputs API")
        await self.set_topology_studio_inputs(workspace_id, device_inputs, timeout)

        LOGGER.info("set_studio_topology: Trying the New Studio Topology API")
        await self._set_studio_topology(workspace_id, device_inputs, timeout)

    @GRPCRequestHandler()
    async def _set_studio_topology(
        self: CVClientProtocol,
        workspace_id: str,
        device_inputs: list[tuple[str, str, str]],
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> list[DeviceKey]:
        """
        Set Topology Studio Inputs using arista.studio.v1.InputsConfigService.Set API.

        Parameters:
            workspace_id: Unique identifier of the Workspace for which the information is set.
            device_inputs: List of Tuples with the format (<device_id>, <hostname>, <system_mac>).
            timeout: Base timeout in seconds. 0.1 second will be added per device.
        """
        request = DeviceInputConfigSetSomeRequest(
            values=[
                DeviceInputConfig(
                    key=DeviceKey(device_id=device_id, workspace_id=workspace_id),
                    device_info=DeviceInfo(device_id=device_id, hostname=hostname, mac_address=MacAddress(value=system_mac)),
                )
                for device_id, hostname, system_mac in device_inputs
            ]
        )

        client = DeviceInputConfigServiceStub(self._channel)
        responses = client.set_some(request, metadata=self._metadata, timeout=timeout)
        return [response.key async for response in responses]

    @GRPCRequestHandler()
    async def set_topology_studio_inputs(
        self: CVClientProtocol,
        workspace_id: str,
        device_inputs: list[tuple[str, str, str]],
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> list[InputsKey]:
        """
        Set Topology Studio Inputs using arista.studio.v1.InputsConfigService.Set API.

        Parameters:
            workspace_id: Unique identifier of the Workspace for which the information is set.
            device_inputs: List of Tuples with the format (<device_id>, <hostname>, <system_mac>).
            timeout: Base timeout in seconds. 0.1 second will be added per device.
        """
        device_inputs_by_id = {device_id: {"hostname": hostname, "macAddress": system_mac} for device_id, hostname, system_mac in device_inputs}

        # We need to get all the devices to make sure we get the correct index of devices.
        studio_inputs: dict = await self.get_studio_inputs(studio_id=TOPOLOGY_STUDIO_ID, workspace_id=workspace_id, default_value={}, timeout=timeout)

        request = InputsConfigSetSomeRequest(values=[])

        for device_index, device_entry in enumerate(studio_inputs.get("devices", [])):
            if not isinstance(device_entry, dict):
                continue

            device_id = str(device_entry.get("tags", {}).get("query", "")).removeprefix("device:")

            # Ignore the device if it is not one of the requested devices.
            if device_id not in device_inputs_by_id:
                continue

            # Update the given fields for the device and add a separate SetSome entry for this device.
            device_info: dict = device_entry.get("inputs", {}).get("device", {})
            device_info.update(device_inputs_by_id.pop(device_id))

            request.values.append(
                InputsConfig(
                    key=InputsKey(
                        studio_id=TOPOLOGY_STUDIO_ID,
                        workspace_id=workspace_id,
                        path=RepeatedString(values=["devices", str(device_index), "inputs", "device"]),
                    ),
                    inputs=json.dumps(device_info),
                ),
            )

        index_offset = len(studio_inputs.get("devices", []))
        # Add any devices not part of the topology studio already.
        for index, device in enumerate(device_inputs_by_id.items()):
            device_id, device_inputs = device
            device_index = index + index_offset
            device_entry = {
                "inputs": {"device": {**device_inputs, "modelName": "", "interfaces": []}},
                "tags": {"query": f"device:{device_id}"},
            }
            request.values.append(
                InputsConfig(
                    key=InputsKey(
                        studio_id=TOPOLOGY_STUDIO_ID,
                        workspace_id=workspace_id,
                        path=RepeatedString(values=["devices", str(device_index)]),
                    ),
                    inputs=json.dumps(device_entry),
                ),
            )

        client = InputsConfigServiceStub(self._channel)
        responses = client.set_some(request, metadata=self._metadata, timeout=timeout + len(request.values) * 0.1)
        return [response.key async for response in responses]

    @GRPCRequestHandler()
    async def set_topology_decommissions(
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

    @GRPCRequestHandler()
    async def get_all_decommissions(
        self: CVClientProtocol,
        device_ids: list[str],
        workspace_id: str,
        state: Literal["success", "unspecified", "failure"],
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> list[DecommissionConfig]:
        """
        Subscribe to the decommission status with arista.studio_topology.v1.DecommissionService.Subscribe API.

        Parameters:
            device_ids: Device IDs to decommission.
            workspace_id: Workspace ID to decommission the devices from.
            state: Decommission state to wait for.
            timeout: Timeout in seconds.

        Returns:
            List of DecommissionConfig objects.
        """
        decommissioning_devices = [Decommission(key=DeviceKey(device_id=device_id, workspace_id=workspace_id)) for device_id in device_ids]
        request = DecommissionStreamRequest(decommissioning_devices)
        client = DecommissionServiceStub(self._channel)
        responses = client.subscribe(request, metadata=self._metadata, timeout=timeout)
        async for response in responses:
            LOGGER.debug("wait_for_decommission_success: Response is '%s.'", response)
            if hasattr(response, "value") and response.value.status == DECOMMISSION_STATUS_MAP[state]:
                LOGGER.info("wait_for_decommission_success: Got response for request '%s': %s", device_ids, response.value.status)
                return response.value
        # Use case where stream completed without getting Decommissioning status update in the desired state
        msg = f"Device decommissioning has not reached desired state '{state}'."
        raise CVDecommissioningFailed(msg)
