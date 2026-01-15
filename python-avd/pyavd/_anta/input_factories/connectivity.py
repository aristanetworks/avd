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
from ._decorators import skip_if_extra_fabric_validation_disabled, skip_if_not_vtep, skip_if_wan_router

if TYPE_CHECKING:
    from collections.abc import Iterator

    from pyavd._anta.models import InputFactoryDataSource
    from pyavd._eos_cli_config_gen.schema import EosCliConfigGen

    class Metadata(Protocol):
        """Required metadata for a candidate interface."""

        peer: str
        peer_interface: str

    class CandidateEthernetInterfacesItemLLDP(Protocol):
        """Protocol representing an interface that is a valid candidate for LLDP testing."""

        name: str
        metadata: Metadata

    class CandidateEthernetInterfacesItemP2P(Protocol):
        """Protocol representing an interface that is a valid candidate for P2P reachability testing."""

        name: str
        metadata: Metadata
        ip_address: str


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

    def _is_interface_candidate(self, interface: EosCliConfigGen.EthernetInterfacesItem) -> TypeGuard[CandidateEthernetInterfacesItemLLDP]:
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

    Generates test inputs for verifying network reachability.

    1. Generates inputs for reachability between directly connected Ethernet interfaces (P2P).
       Includes interfaces that are not administratively shutdown, considering `interface_defaults.ethernet.shutdown`,
       with static IP addresses defined (not DHCP/unnumbered). The peer device must be deployed and the same requirements
       apply for its interface (not shutdown, not DHCP/unnumbered, etc.). IPv6 is not supported.

    2. Generates inputs to verify underlay reachability from VTEP devices local Loopback0 to all other fabric devices Loopback0 addresses.
       No inputs are generated if `extra_fabric_validation` is disabled. WAN routers and non-deployed devices are excluded.
       Fabric devices marked with `exclude_as_extra_fabric_validation_target` are excluded from the destinations. IPv6 is not supported.

    3. Generates inputs for BGP neighbor reachability across all VRFs.
       Includes neighbors that are not administratively shutdown or part of a shutdown peer group.
       Also considers `metadata.validate_state` and ensures the peer is deployed if `metadata.peer` is set.
       To avoid duplicate checks, neighbors already verified (same destination IP and VRF) by the P2P or VTEP tests are skipped.
    """

    def __init__(self, data_source: InputFactoryDataSource, test_name: str) -> None:
        super().__init__(data_source=data_source, test_name=test_name)

        self._covered_destinations: set[tuple[str, str]] = set()
        """Set of tuples (destination_ip, vrf) to track coverage and avoid duplicate checks. Source can be added to the tuple later if needed."""

    def create(self) -> Iterator[VerifyReachability.Input]:
        """Generate the inputs for the `VerifyReachability` test."""
        # Reset tracker in case factory is reused
        self._covered_destinations.clear()

        # Generate the P2P reachability inputs
        with self.logger_adapter.context("P2P Links"):
            p2p_hosts = natural_sort(self._get_p2p_hosts(), sort_key="destination")
            if p2p_hosts:
                yield VerifyReachability.Input(
                    result_overwrite=AntaTest.Input.ResultOverwrite(description="Verifies point-to-point reachability between Ethernet interfaces."),
                    hosts=p2p_hosts,
                )

        # Generate the VTEP fabric-wide underlay reachability inputs
        with self.logger_adapter.context("VTEP Underlay"):
            vtep_hosts = natural_sort(self._get_vtep_underlay_hosts(), sort_key="destination")
            if vtep_hosts:
                yield VerifyReachability.Input(
                    result_overwrite=AntaTest.Input.ResultOverwrite(description="Verifies VTEP fabric-wide underlay reachability."),
                    hosts=natural_sort(vtep_hosts, sort_key="destination"),
                )

        # Generate the BGP neighbor reachability inputs
        with self.logger_adapter.context("BGP Neighbors"):
            bgp_hosts = natural_sort(self._get_bgp_hosts(), sort_key="destination")
            if bgp_hosts:
                yield VerifyReachability.Input(
                    result_overwrite=AntaTest.Input.ResultOverwrite(
                        description="Verifies reachability to BGP neighbors. Some neighbor destinations might already be covered in other reachability tests."
                    ),
                    hosts=bgp_hosts,
                )

    def _get_p2p_hosts(self) -> Iterator[Host]:
        """Generate Host objects for the point-to-point reachability test."""
        for intf in self.structured_config.ethernet_interfaces:
            if not self._is_interface_candidate(intf):
                continue

            # Get and validate the peer interface
            if (peer_interface_ip := self.get_peer_interface_ip(intf.metadata.peer, intf.metadata.peer_interface, intf.name)) is None:
                continue

            if self.is_peer_interface_shutdown(intf.metadata.peer, intf.metadata.peer_interface, intf.name) is True:
                continue

            host = Host(
                destination=ip_interface(peer_interface_ip).ip,
                source=ip_interface(intf.ip_address).ip,
                description=f"{intf.metadata.peer}_{intf.metadata.peer_interface}",
                vrf="default",
                repeat=1,
            )
            self._track_host(host)
            yield host

    @skip_if_extra_fabric_validation_disabled
    @skip_if_not_vtep
    @skip_if_wan_router
    def _get_vtep_underlay_hosts(self) -> Iterator[Host]:
        """Generate Host objects for the VTEP underlay reachability test."""
        if not self.data_source.fabric_loopback0_mapping or not self.data_source.loopback0_ip:
            self.logger_adapter.debug(LogMessage.NO_INPUTS_GENERATED)
            return

        for hostname, ip in self.data_source.fabric_loopback0_mapping.items():
            if hostname == self.data_source.hostname:
                # Don't ping ourself
                continue

            host = Host(destination=ip, source=self.data_source.loopback0_ip, description=hostname, vrf="default", repeat=1)
            if not self._is_host_seen(host):
                self._track_host(host)
                yield host

    def _get_bgp_hosts(self) -> Iterator[Host]:
        """Generate Host objects for the BGP neighbor reachability test."""
        for neighbor in self.data_source.bgp_neighbors:
            if neighbor.update_source is not None:
                host = Host(
                    destination=neighbor.ip_address,
                    source=neighbor.update_source,
                    description=neighbor.description,
                    vrf=neighbor.vrf,
                    repeat=1,
                )
            else:
                # BGP direct neighbors (no source)
                host = Host(
                    destination=neighbor.ip_address,
                    description=neighbor.description,
                    vrf=neighbor.vrf,
                    repeat=1,
                )
            if not self._is_host_seen(host):
                self._track_host(host)
                yield host

    def _is_interface_candidate(self, interface: EosCliConfigGen.EthernetInterfacesItem) -> TypeGuard[CandidateEthernetInterfacesItemP2P]:
        """Check if an interface is valid for P2P reachability testing."""
        if interface.shutdown or (interface.shutdown is None and self.structured_config.interface_defaults.ethernet.shutdown):
            self.logger_adapter.debug(LogMessage.INTERFACE_SHUTDOWN, interface=interface.name)
            return False

        if not interface.ip_address or not interface.metadata.peer or not interface.metadata.peer_interface:
            self.logger_adapter.debug(LogMessage.INPUT_MISSING_FIELDS, identity=interface.name, fields="ip_address, metadata.peer, metadata.peer_interface")
            return False

        if interface.ip_address == "dhcp":
            self.logger_adapter.debug(LogMessage.INTERFACE_USING_DHCP, interface=interface.name)
            return False

        if "unnumbered" in interface.ip_address:
            self.logger_adapter.debug(LogMessage.INTERFACE_UNNUMBERED, interface=interface.name)
            return False
        return True

    def _track_host(self, host: Host) -> None:
        """Register a Host destination in the covered_destinations tracker."""
        self._covered_destinations.add((str(host.destination), host.vrf))

    def _is_host_seen(self, host: Host) -> bool:
        """Check if the destination for this Host has already been covered."""
        return (str(host.destination), host.vrf) in self._covered_destinations
