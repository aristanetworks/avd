# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from ipaddress import IPv4Address, ip_interface

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
    of other fabric device Loopback0 and VTEP IPs in the underlay. Only IPv4 (not IPv6) underlays are supported.

    Test is skipped if `vtep_fabric_reachability` is disabled.
    """

    def create(self) -> list[VerifyRoutingTableEntry.Input] | None:
        """Create a list of inputs for the `VerifyRoutingTableEntry` test."""
        if not self.device.input_factory_settings.vtep_fabric_reachability:
            self.logger_adapter.debug(LogMessage.VTEP_FABRIC_REACHABILITY_DISABLED)
            return None

        if not self.device.is_vtep or self.device.is_wan_router:
            self.logger_adapter.debug(LogMessage.DEVICE_NOT_VTEP)
            return None

        # Using a set to avoid duplicate tests for the same IP address (e.g. MLAG VTEPs)
        ips: set[str] = set()

        # TODO: Consider converting minimal_structured_configs to a dataclass with computed mappings of all
        #       fabric device Loopback0 and VTEP IPs to avoid repeating the same logic below for every device
        for device_name, device_config in self.minimal_structured_configs.items():
            if self.device.hostname == device_name:
                # No need to check ourself
                continue

            if not device_config.is_deployed:
                self.logger_adapter.debug(LogMessage.PEER_NOT_DEPLOYED, peer=device_name)
                continue

            if device_config.loopback0_ip is not None:
                ips.add(device_config.loopback0_ip)
            if device_config.vtep_ip is not None:
                ips.add(device_config.vtep_ip)

        # Convert to IPv4Address objects
        routes = {ip_obj for ip in ips if isinstance((ip_obj := ip_interface(ip).ip), IPv4Address)}
        return [VerifyRoutingTableEntry.Input(routes=natural_sort(routes), collect="all")] if routes else None
