# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import json
from datetime import datetime
from logging import getLogger
from typing import TYPE_CHECKING, Any, Literal

from ..api.arista.studio.v1 import (
    Inputs,
    InputsConfig,
    InputsConfigServiceStub,
    InputsConfigSetRequest,
    InputsConfigSetSomeRequest,
    InputsConfigStreamRequest,
    InputsKey,
    InputsRequest,
    InputsServiceStub,
    InputsStreamRequest,
    Studio,
    StudioConfig,
    StudioConfigServiceStub,
    StudioConfigStreamRequest,
    StudioKey,
    StudioRequest,
    StudioServiceStub,
)
from ..api.arista.time import TimeBounds
from ..api.fmp import RepeatedString
from .constants import DEFAULT_API_TIMEOUT
from .exceptions import CVResourceNotFound, get_cv_client_exception

if TYPE_CHECKING:
    from . import CVClient

LOGGER = getLogger(__name__)

TOPOLOGY_STUDIO_ID = "TOPOLOGY"


class StudioMixin:
    """
    Only to be used as mixin on CVClient class.
    """

    studio_api_version: Literal["v1"] = "v1"

    async def get_studio(
        self: CVClient,
        studio_id: str,
        workspace_id: str,
        time: datetime | None = None,
        timeout: float = 10.0,
    ) -> Studio:
        """
        Get Studio definition using arista.studio.v1.StudioService.GetOne.

        The Studio GetOne API for the workspace does not return anything from mainline and does not return deletions in the workspace.
        So to produce the Workspace Studio we need to fetch from the workspace, and if we find nothing, we need to check if the studio
        got deleted in the workspace by retrieving config. Finally we can fetch from mainline.

        Parameters:
            studio_id: Unique identifier for the studio.
            workspace_id: Unique identifier of the Workspace for which the information is fetched. Use "" for mainline.
            time: Timestamp from which the information is fetched. `now()` if not set.
            timeout: Timeout in seconds.

        Returns:
            Studio object.
        """
        request = StudioRequest(
            # First attempt to fetch studio from workspace.
            key=StudioKey(studio_id=studio_id, workspace_id=workspace_id),
            time=time,
        )
        client = StudioServiceStub(self._channel)
        try:
            response = await client.get_one(request, metadata=self._metadata, timeout=timeout)
            return response.value
        except Exception as e:  # pylint: disable=broad-exception-caught
            e = get_cv_client_exception(e, f"Studio ID '{studio_id}, Workspace ID '{workspace_id}'") or e
            if isinstance(e, CVResourceNotFound):
                # Continue execution if we did not find any state in the workspace.
                # This simply means the studio itself was not changed in this workspace.
                pass
            else:
                raise e

        # If we get here, it means no studio was returned by the workspace call.
        # So now we fetch the studio config from the workspace to see if the studio was deleted in this workspace.
        request = StudioConfigStreamRequest(
            partial_eq_filter=[
                StudioConfig(
                    key=StudioKey(studio_id=studio_id, workspace_id=workspace_id),
                    remove=True,
                )
            ],
            time=TimeBounds(start=None, end=time),
        )
        client = StudioConfigServiceStub(self._channel)
        try:
            responses = client.get_all(request, metadata=self._metadata, timeout=timeout)
            async for response in responses:
                # If we get here it means we got an entry with "removed: True" so no need to look further.
                raise CVResourceNotFound("The studio was deleted in the workspace.", f"Studio ID '{studio_id}, Workspace ID '{workspace_id}'")

        except Exception as e:
            raise get_cv_client_exception(e, f"Studio ID '{studio_id}, Workspace ID '{workspace_id}'") or e

        # If we get here, it means there are no inputs in the workspace and they are not deleted, so we can fetch from mainline.
        request = StudioRequest(
            # First attempt to fetch studio from workspace.
            key=StudioKey(studio_id=studio_id, workspace_id=""),
            time=time,
        )
        client = StudioServiceStub(self._channel)
        try:
            response = await client.get_one(request, metadata=self._metadata, timeout=timeout)
            return response.value
        except Exception as e:
            raise get_cv_client_exception(e, f"Studio ID '{studio_id}, Workspace ID '{workspace_id}'") or e

    async def get_studio_inputs(
        self: CVClient,
        studio_id: str,
        workspace_id: str,
        default_value: Any = None,
        time: datetime | None = None,
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> Any:
        """
        Get Studio Inputs using arista.studio.v1.InputsService.GetAll and arista.studio.v1.InputsConfigServer.GetAll APIs.

        The Studio Inputs GetAll API for the workspace does not return anything from mainline and does not return deletions in the workspace.
        So to produce the Workspace Studio Inputs we need to fetch from the workspace, and if we find nothing, we need to check if inputs
        got deleted in the workspace by retrieving config. Finally we can fetch from mainline.

        Parameters:
            studio_id: Unique identifier for the studio.
            workspace_id: Unique identifier of the Workspace for which the information is fetched. Use "" for mainline.
            default_value: Value to return if no inputs are found.
            time: Timestamp from which the information is fetched. `now()` if not set.
            timeout: Timeout in seconds.

        Returns:
            Value of the studio inputs or the default_value if no inputs are found.
        """
        request = InputsStreamRequest(
            # First attempt to fetch inputs from workspace.
            partial_eq_filter=[
                Inputs(
                    key=InputsKey(studio_id=studio_id, workspace_id=workspace_id),
                )
            ],
            time=time,
        )
        client = InputsServiceStub(self._channel)
        studio_inputs = {}
        try:
            # We use get_all since inputs can be larger than the maximum message size.
            # The inputs are split up by the server to send the value of each key in the underlying data instead of one big JSON blob.
            # Each response will contain a path on which a value must be set.
            # After all responses have been handled the data built from the paths/values contain the full inputs.
            responses = client.get_all(request, metadata=self._metadata, timeout=timeout)
            async for response in responses:
                if response.value.inputs is None:
                    continue

                self._set_value_from_path(
                    path=response.value.key.path.values,
                    data=studio_inputs,
                    value=json.loads(response.value.inputs),
                )

            # We only get a response if the inputs are set/changed in the workspace.
            if studio_inputs:
                return studio_inputs or default_value
        except Exception as e:
            raise get_cv_client_exception(e, f"Studio ID '{studio_id}, Workspace ID '{workspace_id}'") or e

        # If we get here, it means no inputs were returned by the workspace call.
        # So now we fetch the inputs config from the workspace to see if the inputs were deleted in this workspace.
        request = InputsConfigStreamRequest(
            partial_eq_filter=[
                InputsConfig(
                    key=InputsKey(studio_id=studio_id, workspace_id=workspace_id),
                    remove=True,
                )
            ],
            time=time,
        )
        client = InputsConfigServiceStub(self._channel)
        try:
            responses = client.get_all(request, metadata=self._metadata, timeout=timeout)
            async for response in responses:
                # If we get here it means we got an entry with "removed: True" so no need to look further.
                return default_value

        except Exception as e:
            raise get_cv_client_exception(e, f"Studio ID '{studio_id}, Workspace ID '{workspace_id}'") or e

        # If we get here, it means there are no inputs in the workspace and they are not deleted, so we can fetch from mainline.
        request = InputsStreamRequest(
            # Notice using workspace="" for mainline.
            partial_eq_filter=[
                Inputs(
                    key=InputsKey(studio_id=studio_id, workspace_id=""),
                )
            ],
            time=time,
        )
        client = InputsServiceStub(self._channel)
        try:
            responses = client.get_all(request, metadata=self._metadata, timeout=timeout)
            async for response in responses:
                if response.value.inputs is None:
                    continue

                self._set_value_from_path(
                    path=response.value.key.path.values,
                    data=studio_inputs,
                    value=json.loads(response.value.inputs),
                )

            return studio_inputs or default_value
        except Exception as e:
            raise get_cv_client_exception(e, f"Studio ID '{studio_id}, Workspace ID '{workspace_id}'") or e

    async def get_studio_inputs_with_path(
        self: CVClient,
        studio_id: str,
        workspace_id: str,
        input_path: list[str],
        default_value: Any = None,
        time: datetime | None = None,
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> Any:
        """
        Get Studio Inputs for a specific path using arista.studio.v1.InputsService.GetOne and arista.studio.v1.InputsConfigServer.GetAll APIs.

        The Studio Inputs GetOne API for the workspace does not return anything from mainline and does not return deletions in the workspace.
        So to produce the Workspace Studio Inputs we need to fetch from the workspace, and if we find nothing, we need to check if inputs
        got deleted in the workspace by retrieving config. Finally we can fetch from mainline.

        Parameters:
            studio_id: Unique identifier for the studio.
            workspace_id: Unique identifier of the Workspace for which the information is fetched. Use "" for mainline.
            input_path: Data elements leading to specific inputs.
            default_value: Value to return if no inputs are found.
            time: Timestamp from which the information is fetched. `now()` if not set.
            timeout: Timeout in seconds.

        Returns:
            Value of the requested path or the default_value if no inputs are found.
        """
        request = InputsRequest(
            # First attempt to fetch inputs from workspace.
            key=InputsKey(
                studio_id=studio_id,
                workspace_id=workspace_id,
                path=RepeatedString(values=input_path),
            ),
            time=time,
        )
        client = InputsServiceStub(self._channel)
        try:
            response = await client.get_one(request, metadata=self._metadata, timeout=timeout)

            # We only get a response if the inputs are set/changed in the workspace.
            if response.value.inputs is not None:
                return json.loads(response.value.inputs)
            return default_value

        except Exception as e:  # pylint: disable=broad-exception-caught
            e = get_cv_client_exception(e, f"Studio ID '{studio_id}, Workspace ID '{workspace_id}', Path '{input_path}'") or e
            if isinstance(e, CVResourceNotFound) and workspace_id != "":
                # Ignore this error, since it simply means we have to check if inputs got deleted in this workspace or fetch from mainline as last resort.
                pass
            else:
                raise e

        # If we get here, it means no inputs were returned by the workspace call.
        # So now we fetch the inputs config from the workspace to see if the inputs were deleted in this workspace.
        request = InputsConfigStreamRequest(
            partial_eq_filter=InputsConfig(
                key=InputsKey(
                    studio_id=studio_id,
                    workspace_id=workspace_id,
                    path=RepeatedString(values=input_path),
                ),
                remove=True,
            ),
            time=time,
        )
        client = InputsConfigServiceStub(self._channel)
        try:
            responses = client.get_all(request, metadata=self._metadata, timeout=timeout)
            async for response in responses:
                # If we get here it means we got an entry with "removed: True" so no need to look further.
                return default_value

        except Exception as e:
            raise get_cv_client_exception(e, f"Studio ID '{studio_id}, Workspace ID '{workspace_id}', Path '{input_path}'") or e

        # If we get here, it means there are no inputs in the workspace and they are not deleted, so we can fetch from mainline.
        request = InputsRequest(
            # Notice using workspace="" for mainline.
            key=InputsKey(
                studio_id=studio_id,
                workspace_id="",
                path=RepeatedString(values=input_path),
            ),
            time=time,
        )
        client = InputsServiceStub(self._channel)
        try:
            response = await client.get_one(request, metadata=self._metadata, timeout=timeout)
            if response.value.inputs is not None:
                return json.loads(response.value.inputs)
            return default_value
        except Exception as e:  # pylint: disable=broad-exception-caught
            e = get_cv_client_exception(e, f"Studio ID '{studio_id}, Workspace ID '{workspace_id}', Path '{input_path}'") or e
            if isinstance(e, CVResourceNotFound):
                # Ignore this error, since it simply means we no inputs are in the studio so we will return the default value.
                return default_value
            raise e

    async def set_studio_inputs(
        self: CVClient,
        studio_id: str,
        workspace_id: str,
        inputs: Any,
        input_path: list[str] | None = None,
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> InputsConfig:
        """
        Set Studio Inputs using arista.studio.v1.InputsConfigService.Set API.

        Parameters:
            studio_id: Unique identifier for the studio.
            workspace_id: Unique identifier of the Workspace for which the information is set.
            inputs: Data to set at the given path.
            input_path: Data path elements for setting specific inputs. If not given, inputs are set at the root, replacing all existing inputs.
            timeout: Timeout in seconds.

        TODO: Refactor to split inputs into multiple messages in case of larger input sets.

        Returns:
            InputsConfig object after being set including any server-generated values.
        """
        request = InputsConfigSetRequest(
            InputsConfig(
                key=InputsKey(
                    studio_id=studio_id,
                    workspace_id=workspace_id,
                    path=RepeatedString(values=input_path),
                ),
                inputs=json.dumps(inputs),
            )
        )
        client = InputsConfigServiceStub(self._channel)
        try:
            response = await client.set(request, metadata=self._metadata, timeout=timeout)
            return response.value

        except Exception as e:
            raise get_cv_client_exception(e, f"Studio ID '{studio_id}, Workspace ID '{workspace_id}', Path '{input_path}'") or e

    async def get_topology_studio_inputs(
        self: CVClient,
        workspace_id: str,
        device_ids: list[str] | None = None,
        time: datetime | None = None,
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> list[dict]:
        """
        TODO: Once the topology studio inputs API is public, this function can be replaced by the _future variant.
              It will probably need some version detection to see if the API is supported.

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
            studio_id=TOPOLOGY_STUDIO_ID, workspace_id=workspace_id, default_value={}, time=time, timeout=timeout
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
                }
            )
        return topology_inputs

    async def set_topology_studio_inputs(
        self: CVClient,
        workspace_id: str,
        device_inputs: list[tuple[str, str, str]],
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> list[InputsKey]:
        """
        TODO: Once the topology studio inputs API is public, this function can be replaced by the _future variant.
              It will probably need some version detection to see if the API is supported.

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
                )
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
                )
            )

        input_keys = []
        client = InputsConfigServiceStub(self._channel)
        try:
            responses = client.set_some(request, metadata=self._metadata, timeout=timeout + len(request.values) * 0.1)
            async for response in responses:
                input_keys.append(response.key)

            return input_keys

        except Exception as e:
            raise get_cv_client_exception(e, f"Studio ID '{TOPOLOGY_STUDIO_ID}, Workspace ID '{workspace_id}', Devices '{device_inputs}'") or e

    # Future versions for once topology studio API is available.
    #
    # async def _future__get_topology_studio_inputs(
    #     self: CVClient,
    #     workspace_id: str,
    #     device_ids: list[str] | None = None,
    #     time: datetime | None = None,
    #     timeout: float = DEFAULT_API_TIMEOUT,
    # ) -> list[TopologyInput]:
    #     """
    #     TODO: Once the topology studio inputs API is public, this function can be put in place.
    #           It will probably need some version detection to see if the API is supported.

    #     Get Topology Studio Inputs using arista.studio.v1.TopologyInputsService.GetAll and arista.studio.v1.TopologyInputsConfigService.GetAll APIs.

    #     Parameters:
    #         workspace_id: Unique identifier of the Workspace for which the information is fetched. Use "" for mainline.
    #         device_ids: List of Device IDs / Serial numbers to get inputs for.
    #         time: Timestamp from which the information is fetched. `now()` if not set.
    #         timeout: Timeout in seconds.

    #     Returns:
    #         Inputs object.
    #     """
    #     request = TopologyInputStreamRequest(partial_eq_filter=[], time=time)
    #     if device_ids:
    #         for device_id in device_ids:
    #             request.partial_eq_filter.append(
    #                 TopologyInput(
    #                     key=TopologyInputKey(workspace_id=workspace_id, device_id=device_id),
    #                 )
    #             )
    #     else:
    #         request.partial_eq_filter.append(
    #             TopologyInput(
    #                 key=TopologyInputKey(workspace_id=workspace_id),
    #             )
    #         )
    #     client = TopologyInputServiceStub(self._channel)
    #     topology_inputs = []
    #     try:
    #         responses = client.get_all(request, metadata=self._metadata, timeout=timeout)
    #         async for response in responses:
    #             topology_inputs.append(response.value)
    #         return topology_inputs
    #     except Exception as e:
    #         raise get_cv_client_exception(e, f"Workspace ID '{workspace_id}', Device IDs '{device_ids}'") or e

    # async def _future_set_topology_studio_inputs(
    #     self: CVClient,
    #     workspace_id: str,
    #     device_inputs: list[tuple[str, str]],
    #     timeout: float = DEFAULT_API_TIMEOUT,
    # ) -> list[TopologyInputKey]:
    #     """
    #     TODO: Once the topology studio inputs API is public, this function can be put in place.
    #           It will probably need some version detection to see if the API is supported.

    #     Set Topology Studio Inputs using arista.studio.v1.TopologyInputsConfigService.Set API.

    #     Parameters:
    #         workspace_id: Unique identifier of the Workspace for which the information is set.
    #         device_inputs: List of Tuples with the format (<device_id>, <hostname>).
    #         timeout: Timeout in seconds.

    #     Returns:
    #         TopologyInputKey objects after being set including any server-generated values.
    #     """
    #     request = TopologyInputConfigSetSomeRequest(
    #         values=[
    #             TopologyInputConfig(
    #                 key=TopologyInputKey(workspace_id=workspace_id, device_id=device_id),
    #                 device_info=DeviceInfo(device_id=device_id, hostname=hostname),
    #             )
    #             for device_id, hostname in device_inputs
    #         ]
    #     )

    #     client = TopologyInputConfigServiceStub(self._channel)
    #     topology_input_keys = []
    #     try:
    #         responses = client.set_some(request, metadata=self._metadata, timeout=timeout)
    #         async for response in responses:
    #             topology_input_keys.append(response.key)
    #         return topology_input_keys

    #     except Exception as e:
    #         raise get_cv_client_exception(e, f"Workspace ID '{workspace_id}', Device IDs '{device_inputs}'") or e
