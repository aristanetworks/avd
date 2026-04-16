# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

from anta.input_models.routing.generic import IPv4RouteEntry
from anta.tests.routing.generic import VerifyIPv4RoutePresencePerVRF, VerifyRoutingProtocolModel

from pyavd._anta.constants import StructuredConfigKey
from pyavd._anta.logs import LogMessage

from .base_classes import AntaTestInputFactory
from .decorators import skip_if_extra_fabric_validation_disabled, skip_if_missing_config, skip_if_not_vtep, skip_if_wan_router

if TYPE_CHECKING:
    from collections.abc import Iterator


class VerifyRoutingProtocolModelInputFactory(AntaTestInputFactory[VerifyRoutingProtocolModel.Input]):
    """
    Input factory class for the `VerifyRoutingProtocolModel` test.

    The test input `model` is collected from the value of `service_routing_protocols_model`
    of the device structured config.
    """

    @skip_if_missing_config(StructuredConfigKey.SERVICE_ROUTING_PROTOCOLS_MODEL)
    def create(self) -> Iterator[VerifyRoutingProtocolModel.Input]:
        """Generate the inputs for the `VerifyRoutingProtocolModel` test."""
        if not (model := self.structured_config.service_routing_protocols_model):
            self.logger_adapter.debug(LogMessage.NO_INPUTS_GENERATED)
            return

        yield VerifyRoutingProtocolModel.Input(model=model)


class VerifyIPv4RoutePresencePerVRFInputFactory(AntaTestInputFactory[VerifyIPv4RoutePresencePerVRF.Input]):
    """
    Input factory class for the `VerifyIPv4RoutePresencePerVRF` test.

    On VTEP devices (excluding WAN routers), generates inputs to verify IPv4 routing table entries
    for other fabric non-WAN devices' Loopback0 and VTEP IPs in the underlay. Only IPv4 underlays are supported.

    No inputs are generated if `extra_fabric_validation` is disabled.
    """

    @skip_if_extra_fabric_validation_disabled
    @skip_if_not_vtep
    @skip_if_wan_router
    def create(self) -> Iterator[VerifyIPv4RoutePresencePerVRF.Input]:
        """Generate the inputs for the `VerifyIPv4RoutePresencePerVRF` test."""
        if not self.data_source.fabric_underlay_reachability_prefixes:
            self.logger_adapter.debug(LogMessage.NO_INPUTS_GENERATED)
            return

        # TODO: Provide the target hostname as the description for each route entry.
        yield VerifyIPv4RoutePresencePerVRF.Input(
            route_entries=[IPv4RouteEntry(prefix=prefix, vrf="default") for prefix in self.data_source.fabric_underlay_reachability_prefixes]
        )
