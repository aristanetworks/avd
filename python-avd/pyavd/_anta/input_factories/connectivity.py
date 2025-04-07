# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from ipaddress import ip_interface

from anta.input_models.connectivity import Host, LLDPNeighbor
from anta.models import AntaTest
from anta.tests.connectivity import VerifyLLDPNeighbors, VerifyReachability

from pyavd._anta.logs import LogMessage
from pyavd.j2filters import natural_sort

from ._base_classes import AntaTestInputFactory


class VerifyLLDPNeighborsInputFactory(AntaTestInputFactory):
    """
    Input factory class for the `VerifyLLDPNeighbors` test.

    This factory collects LLDP neighbors for Ethernet interfaces that have
    `peer` and `peer_interface` fields defined in their configuration.

    Peers must be available (`is_deployed: true`).

    The factory respects `validate_state` and `validate_lldp` settings, excludes
    subinterfaces and shutdown interfaces (considering `interface_defaults.ethernet.shutdown`
    when not set), and uses peer FQDN when `dns_domain` is configured to match EOS
    LLDP format.
    """

    def create(self) -> list[VerifyLLDPNeighbors.Input] | None:
        """Create a list of inputs for the `VerifyLLDPNeighbors` test."""
        neighbors = []
        for intf in self.structured_config.ethernet_interfaces:
            if intf.validate_state is False or intf.validate_lldp is False:
                self.logger.debug(LogMessage.INTERFACE_VALIDATION_DISABLED, caller=intf.name)
                continue

            if "." in intf.name:
                self.logger.debug(LogMessage.INTERFACE_IS_SUBINTERFACE, caller=intf.name)
                continue

            if intf.shutdown or (intf.shutdown is None and self.structured_config.interface_defaults.ethernet.shutdown):
                self.logger.debug(LogMessage.INTERFACE_SHUTDOWN, caller=intf.name)
                continue

            if not intf.peer or not intf.peer_interface:
                self.logger.debug(LogMessage.INPUT_MISSING_FIELDS, caller=intf.name, fields="peer, peer_interface")
                continue

            if not self.is_peer_available(intf.peer, caller=intf.name):
                continue

            # LLDP neighbor is the FQDN when dns domain is set in EOS
            fqdn = f"{intf.peer}.{dns_domain}" if (dns_domain := self.structured_configs[intf.peer].dns_domain) is not None else intf.peer

            neighbors.append(
                LLDPNeighbor(
                    port=intf.name,
                    neighbor_device=fqdn,
                    neighbor_port=intf.peer_interface,
                )
            )

        return [VerifyLLDPNeighbors.Input(neighbors=natural_sort(neighbors, sort_key="port"))] if neighbors else None


class VerifyReachabilityInputFactory(AntaTestInputFactory):
    """
    Input factory class for the `VerifyReachability` test.

    Generates test inputs for verifying the following reachability checks:

    - Point-to-point links between Ethernet interfaces with `peer`, `peer_interface`,
    and `ip_address` (non-dhcp) configured. Links are checked when interfaces are not `shutdown`,
    fabric peers exist and are deployed (`is_deployed: true`), and peer interfaces have IP addresses.

    - IPv4 BGP neighbors with `update_source` configured.
    """

    def create(self) -> list[VerifyReachability.Input] | None:
        """Create a list of inputs for the `VerifyReachability` test."""
        inputs: list[VerifyReachability.Input] = []

        # Get the P2P reachability inputs
        with self.logger.context("Point-to-Point Links"):
            p2p_inputs = self._get_p2p_inputs()
            if p2p_inputs.hosts:
                inputs.append(p2p_inputs)

        # Get the BGP neighbor reachability inputs
        with self.logger.context("BGP Neighbors"):
            bgp_inputs = self._get_bgp_inputs()
            if bgp_inputs.hosts:
                inputs.append(bgp_inputs)

        return inputs if inputs else None

    def _get_p2p_inputs(self) -> VerifyReachability.Input:
        """Generate the inputs for the point-to-point reachability test."""
        description = "Verifies point-to-point reachability between Ethernet interfaces."
        hosts = []

        for intf in self.structured_config.ethernet_interfaces:
            if intf.shutdown or (intf.shutdown is None and self.structured_config.interface_defaults.ethernet.shutdown):
                self.logger.debug(LogMessage.INTERFACE_SHUTDOWN, caller=intf.name)
                continue

            if not intf.ip_address or not intf.peer or not intf.peer_interface:
                self.logger.debug(LogMessage.INPUT_MISSING_FIELDS, caller=intf.name, fields="ip_address, peer, peer_interface")
                continue

            if intf.ip_address == "dhcp":
                self.logger.debug(LogMessage.INTERFACE_USING_DHCP, caller=intf.name)
                continue

            if (peer_interface_ip := self.get_interface_ip(intf.peer, intf.peer_interface, caller=intf.name)) is None:
                continue

            hosts.append(
                Host(
                    destination=ip_interface(peer_interface_ip).ip,
                    source=ip_interface(intf.ip_address).ip,
                    vrf="default",
                    repeat=1,
                )
            )

        return VerifyReachability.Input(
            result_overwrite=AntaTest.Input.ResultOverwrite(description=description), hosts=natural_sort(hosts, sort_key="destination")
        )

    # TODO: When https://github.com/aristanetworks/anta/issues/1112 is resolved, also add BGP direct neighbors
    def _get_bgp_inputs(self) -> VerifyReachability.Input:
        """
        Generate the inputs for the BGP neighbor reachability test.

        Only support BGP neighbors with an update source configured for now.
        """
        description = "Verifies reachability to IPv4 BGP neighbors with an update source configured."
        hosts = [
            Host(
                destination=neighbor.ip_address,
                source=neighbor.update_source,
                vrf=neighbor.vrf,
                repeat=1,
            )
            for neighbor in self.device.bgp_neighbors
            if neighbor.update_source is not None
        ]

        return VerifyReachability.Input(
            result_overwrite=AntaTest.Input.ResultOverwrite(description=description), hosts=natural_sort(hosts, sort_key="destination")
        )
