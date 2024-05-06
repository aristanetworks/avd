# Copyright (c) 2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from datetime import datetime
from logging import getLogger
from typing import TYPE_CHECKING, Literal

from ..api.arista.swg.v1 import (
    EndpointConfig,
    EndpointConfigServiceStub,
    EndpointConfigSetRequest,
    EndpointStatus,
    EndpointStatusServiceStub,
    EndpointStatusStreamRequest,
    SwgKey,
)
from .exceptions import get_cv_client_exception

if TYPE_CHECKING:
    from .cv_client import CVClient


LOGGER = getLogger(__name__)


class SwgMixin:
    """
    Only to be used as mixin on CVClient class.
    """

    swg_api_version: Literal["v1"] = "v1"

    async def set_swg_device(
        self: CVClient,
        device_id: str,
        service: Literal["zscaler"],
        location: str,
        timeout: float = 10.0,
    ) -> EndpointConfig:
        """
        Get SWG Endpoints using arista.swg.v1.EndpointStatusService.GetOne API

        Parameters:
            device_id: Unique identifier of the Device - typically serial number.
            service: SWG service
            location: Device location/address. CloudVision will resolve a location from this address.
            time: Timestamp from which the information is fetched. `now()` if not set.
            timeout: Timeout in seconds.

        Returns:
            EndpointConfig including any server-generated values.
        """
        request = EndpointConfigSetRequest(
            value=EndpointConfig(
                key=SwgKey(device_id=device_id, service_name=service),
                address=location,
            )
        )
        client = EndpointConfigServiceStub(self._channel)

        try:
            LOGGER.info("set_swg_device: Setting location for '%s': %s", device_id, location)
            response = await client.set(request, metadata=self._metadata, timeout=timeout)
            return response.value

        except Exception as e:
            raise get_cv_client_exception(e, f"Device ID '{device_id}', service '{service}', location '{location}'") or e

    async def wait_for_swg_endpoint_status(
        self: CVClient,
        device_id: str,
        service: Literal["zscaler"],
        time: datetime | None = None,
        timeout: float = 10.0,
    ) -> EndpointStatus:
        """
        Subscribe and wait for one SWG Endpoint using arista.swg.v1.EndpointStatusService.Subscribe API

        Parameters:
            device_id: Unique identifier of the Device - typically serial number.
            time: Timestamp from which the information is fetched. `now()` if not set.
            timeout: Timeout in seconds.

        Returns:
            EndpointStatus object matching the device_id
        """
        request = EndpointStatusStreamRequest(
            partial_eq_filter=[
                EndpointStatus(
                    key=SwgKey(device_id=device_id, service_name=service),
                ),
            ],
            time=time,
        )
        client = EndpointStatusServiceStub(self._channel)

        try:
            responses = client.subscribe(request, metadata=self._metadata, timeout=timeout)
            async for response in responses:
                LOGGER.info("wait_for_swg_endpoint_status: Got SWG endpoints: %s", response.value)
                return response.value

        except Exception as e:
            raise get_cv_client_exception(e, f"Device ID '{device_id}', service '{service}") or e
