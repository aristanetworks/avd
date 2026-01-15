# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from ipaddress import ip_interface
from typing import TYPE_CHECKING, Protocol, TypeGuard

from anta.input_models.connectivity import Host, LLDPNeighbor
from anta.models import AntaTest
from anta.tests.connectivity import VerifyLLDPNeighbors, VerifyReachability

from pyavd._anta.logs import LogMessage
from pyavd.j2filters import natural_sort

from ._base_classes import AntaTestInputFactory

if TYPE_CHECKING:
    from collections.abc import Iterator

    from pyavd._eos_cli_config_gen.schema import EosCliConfigGen

    class CandidateEthernetInterfacesItem(Protocol):
        """Protocol representing an interface that is a valid candidate for LLDP testing."""

        class Metadata(Protocol):
            """Required metadata for a candidate interface."""

            peer: str
            peer_interface: str

        name: str
        metadata: Metadata


class VerifyLLDPNeighborsInputFactory(AntaTestInputFactory[VerifyLLDPNeighbors.Input]):
    """
    Input factory class for the `VerifyLLDPNeighbors` test.

    This factory collects LLDP neighbors for Ethernet interfaces that have
    `metadata.peer` and `metadata.peer_interface` fields defined in their configuration.

    Peers must be available (`is_deployed: true`).

    The factory respects `metadata.validate_state` and `metadata.validate_lldp` settings, excludes
    subinterfaces and shutdown interfaces on the local device (considering
    `interface_defaults.ethernet.shutdown` when not explicitly set), and, when
    `metadata.validate_lldp` is not defined, validates that the peer device is available
    and the peer interface is not shutdown.
    """

    def create(self) -> Iterator[VerifyLLDPNeighbors.Input]:
        """Generate the inputs for the `VerifyLLDPNeighbors` test."""
        neighbors = [
            LLDPNeighbor(port=intf.name, neighbor_device=intf.metadata.peer, neighbor_port=intf.metadata.peer_interface)
            for intf in self.structured_config.ethernet_interfaces
            if self._is_interface_candidate(intf)
        ]

        if not neighbors:
            self.logger_adapter.debug(LogMessage.NO_INPUTS_GENERATED)
            return

        yield VerifyLLDPNeighbors.Input(neighbors=natural_sort(neighbors, sort_key="port"), require_fqdn=False)

    def _is_interface_candidate(self, interface: EosCliConfigGen.EthernetInterfacesItem) -> TypeGuard[CandidateEthernetInterfacesItem]:
        """Check if an interface is valid for LLDP testing."""
        if interface.metadata.validate_state is False or interface.metadata.validate_lldp is False:
            self.logger_adapter.debug(LogMessage.INTERFACE_VALIDATION_DISABLED, interface=interface.name)
            return False

        if "." in interface.name:
            self.logger_adapter.debug(LogMessage.INTERFACE_IS_SUBINTERFACE, interface=interface.name)
            return False

        if interface.shutdown or (interface.shutdown is None and self.structured_config.interface_defaults.ethernet.shutdown):
            self.logger_adapter.debug(LogMessage.INTERFACE_SHUTDOWN, interface=interface.name)
            return False

        if not interface.metadata.peer or not interface.metadata.peer_interface:
            self.logger_adapter.debug(LogMessage.INPUT_MISSING_FIELDS, identity=interface.name, fields="metadata.peer, metadata.peer_interface")
            return False

        # Default behavior (None) implies we treat the peer as an AVD-managed device in the inventory
        treat_as_avd_peer = interface.metadata.validate_lldp is None
        if treat_as_avd_peer:
            if not self.is_peer_available(interface.metadata.peer, identity=interface.name):
                return False

            if self.is_peer_interface_shutdown(interface.metadata.peer, interface.metadata.peer_interface, interface.name):
                return False

        return True


class VerifyReachabilityInputFactory(AntaTestInputFactory[VerifyReachability.Input]):
    """
    Input factory class for the `VerifyReachability` test.

    Generates test inputs for verifying the following reachability checks:

    - Point-to-Point Ethernet Links:
        Inputs are generated for Ethernet interfaces that meet all the following criteria:
        * `peer`, `peer_interface` and `ip_address` are defined
        * `ip_address` is static - *not* 'dhcp' and *not* 'unnumbered'
        * Interface is not shutdown - considers `shutdown` and `interface_defaults.ethernet.shutdown`
        * `peer` device is deployed - `is_deployed=True`
        * `peer_interface` on the `peer` device has a defined static `ip_address` - *not* 'dhcp' and *not* 'unnumbered'
        * `peer_interface` is not shutdown - considers `shutdown` and `interface_defaults.ethernet.shutdown`

    - BGP Neighbors:
        Inputs are generated for BGP neighbors that meet all the following criteria:
        * `update_source` IP address defined
    """

    def create(self) -> Iterator[VerifyReachability.Input]:
        """Generate the inputs for the `VerifyReachability` test."""
        # Generate the P2P reachability inputs
        with self.logger_adapter.context("P2P link"):
            p2p_inputs = self._get_p2p_inputs()
            if p2p_inputs.hosts:
                yield p2p_inputs

        # Generate the BGP neighbor reachability inputs
        with self.logger_adapter.context("BGP neighbor"):
            bgp_inputs = self._get_bgp_inputs()
            if bgp_inputs.hosts:
                yield bgp_inputs

    def _get_p2p_inputs(self) -> VerifyReachability.Input:
        """Get the inputs for the point-to-point reachability test."""
        description = "Verifies point-to-point reachability between Ethernet interfaces."
        hosts: list[Host] = []

        for intf in self.structured_config.ethernet_interfaces:
            if intf.shutdown or (intf.shutdown is None and self.structured_config.interface_defaults.ethernet.shutdown):
                self.logger_adapter.debug(LogMessage.INTERFACE_SHUTDOWN, interface=intf.name)
                continue

            if not intf.ip_address or not intf.metadata.peer or not intf.metadata.peer_interface:
                self.logger_adapter.debug(LogMessage.INPUT_MISSING_FIELDS, identity=intf.name, fields="ip_address, metadata.peer, metadata.peer_interface")
                continue

            if intf.ip_address == "dhcp":
                self.logger_adapter.debug(LogMessage.INTERFACE_USING_DHCP, interface=intf.name)
                continue

            # TODO: Consider adding reachability check between lending interfaces without creating duplicate src-dst pairs
            if "unnumbered" in intf.ip_address:
                self.logger_adapter.debug(LogMessage.INTERFACE_UNNUMBERED, interface=intf.name)
                continue

            if (peer_interface_ip := self.get_peer_interface_ip(intf.metadata.peer, intf.metadata.peer_interface, intf.name)) is None:
                continue

            if self.is_peer_interface_shutdown(intf.metadata.peer, intf.metadata.peer_interface, intf.name) is True:
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
        Get the inputs for the BGP neighbor reachability test.

        Only support BGP neighbors with an update source configured for now.
        """
        description = "Verifies reachability to BGP neighbors with an update source configured."
        hosts = [
            Host(
                destination=neighbor.ip_address,
                source=neighbor.update_source,
                vrf=neighbor.vrf,
                repeat=1,
            )
            for neighbor in self.data_source.bgp_neighbors
            if neighbor.update_source is not None
        ]

        return VerifyReachability.Input(
            result_overwrite=AntaTest.Input.ResultOverwrite(description=description), hosts=natural_sort(hosts, sort_key="destination")
        )
