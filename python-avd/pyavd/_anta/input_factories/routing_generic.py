# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

from anta.tests.routing.generic import VerifyRoutingProtocolModel, VerifyRoutingTableEntry

from pyavd._anta.logs import LogMessage
from pyavd.j2filters import natural_sort

from ._base_classes import AntaTestInputFactory
from ._decorators import skip_if_extra_fabric_validation_disabled, skip_if_wan_router

if TYPE_CHECKING:
    from collections.abc import Iterator


class VerifyRoutingProtocolModelInputFactory(AntaTestInputFactory[VerifyRoutingProtocolModel.Input]):
    """
    Input factory class for the `VerifyRoutingProtocolModel` test.

    The test input `model` is collected from the value of `service_routing_protocols_model`
    of the device structured config.
    """

    def create(self) -> Iterator[VerifyRoutingProtocolModel.Input]:
        """Generate the inputs for the `VerifyRoutingProtocolModel` test."""
        if not (model := self.structured_config.service_routing_protocols_model):
            self.logger_adapter.debug(LogMessage.NO_INPUTS_GENERATED)
            return

        yield VerifyRoutingProtocolModel.Input(model=model)


class VerifyRoutingTableEntryInputFactory(AntaTestInputFactory[VerifyRoutingTableEntry.Input]):
    """
    Input factory class for the `VerifyRoutingTableEntry` test.

    On VTEP devices (excluding WAN routers), generates inputs to verify IPv4 routing table entries
    for other fabric non-WAN devices' Loopback0 and VTEP IPs in the underlay. Only IPv4 underlays are supported.

    No inputs are generated if `extra_fabric_validation` is disabled.
    """

    @skip_if_extra_fabric_validation_disabled
    @skip_if_wan_router
    def create(self) -> Iterator[VerifyRoutingTableEntry.Input]:
        """Generate the inputs for the `VerifyRoutingTableEntry` test."""
        if not self.fabric_data.special_ips:
            self.logger_adapter.debug(LogMessage.NO_INPUTS_GENERATED)
            return

        yield VerifyRoutingTableEntry.Input(routes=natural_sort(list(self.fabric_data.special_ips)), collect="all")
