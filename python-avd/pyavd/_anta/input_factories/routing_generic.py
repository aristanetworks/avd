# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from anta.tests.routing.generic import VerifyRoutingProtocolModel, VerifyRoutingTableEntry

from pyavd._anta.logs import LogMessage
from pyavd.j2filters import natural_sort

from ._base_classes import AntaTestInputFactory


class VerifyRoutingProtocolModelInputFactory(AntaTestInputFactory[VerifyRoutingProtocolModel.Input]):
    """
    Input factory class for the `VerifyRoutingProtocolModel` test.

    The test input `model` is collected from the value of `service_routing_protocols_model`
    of the device structured config.
    """

    def create(self) -> list[VerifyRoutingProtocolModel.Input] | None:
        """Create a list of inputs for the `VerifyRoutingProtocolModel` test."""
        model = self.structured_config.service_routing_protocols_model
        return [VerifyRoutingProtocolModel.Input(model=model)] if model else None


class VerifyRoutingTableEntryInputFactory(AntaTestInputFactory[VerifyRoutingTableEntry.Input]):
    """
    Input factory class for the `VerifyRoutingTableEntry` test.

    On VTEP devices (excluding WAN routers), generates inputs to verify IPv4 routing table entries
    for other fabric non-WAN devices' Loopback0 and VTEP IPs in the underlay. Only IPv4 underlays are supported.

    No inputs are generated if `extra_fabric_validation` is disabled.
    """

    def create(self) -> list[VerifyRoutingTableEntry.Input] | None:
        """Create a list of inputs for the `VerifyRoutingTableEntry` test."""
        if not self.device.settings.extra_fabric_validation:
            self.logger_adapter.debug(LogMessage.EXTRA_FABRIC_VALIDATION_DISABLED)
            return None

        if self.device.is_wan_router:
            self.logger_adapter.debug(LogMessage.DEVICE_IS_WAN_ROUTER)
            return None

        return [VerifyRoutingTableEntry.Input(routes=natural_sort(list(self.fabric_data.special_ips)), collect="all")] if self.fabric_data.special_ips else None
