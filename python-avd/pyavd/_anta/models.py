# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Data models used by PyAVD for ANTA."""

from __future__ import annotations

from dataclasses import dataclass
from functools import cached_property
from ipaddress import IPv4Address, IPv6Address, ip_interface
from logging import getLogger
from typing import TYPE_CHECKING

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen

if TYPE_CHECKING:
    from pyavd.api._anta import InputFactorySettings, MinimalStructuredConfig

LOGGER = getLogger(__name__)


@dataclass(frozen=True)
class BgpNeighbor:
    """Represents a BGP neighbor from the structured configuration."""

    ip_address: IPv4Address
    vrf: str
    update_source: str | None = None


@dataclass
class DeviceTestContext:
    """Stores device test context data for ANTA test generation."""

    hostname: str
    structured_config: EosCliConfigGen
    minimal_structured_configs: dict[str, MinimalStructuredConfig]
    input_factory_settings: InputFactorySettings

    @cached_property
    def is_vtep(self) -> bool:
        """Check if the device is a VTEP."""
        return bool(self.structured_config.vxlan_interface.vxlan1.vxlan.source_interface)

    @cached_property
    def is_wan_router(self) -> bool:
        """Check if the device is a WAN router."""
        return self.is_vtep and "Dps" in self.structured_config.vxlan_interface.vxlan1.vxlan.source_interface

    @cached_property
    def bgp_neighbors(self) -> list[BgpNeighbor]:
        """Generate a list of BGP neighbors for the device."""
        neighbors = [
            bgp_neighbor for neighbor in self.structured_config.router_bgp.neighbors if (bgp_neighbor := self._process_bgp_neighbor(neighbor, "default"))
        ]

        # Skip VRF processing if disabled
        if not self.input_factory_settings.allow_bgp_vrfs:
            LOGGER.debug("<%s> Skipped BGP VRF peers - VRF processing disabled", self.hostname)
            return neighbors

        # Add VRF neighbors to the list
        neighbors.extend(
            bgp_neighbor
            for vrf in self.structured_config.router_bgp.vrfs
            for neighbor in vrf.neighbors
            if (bgp_neighbor := self._process_bgp_neighbor(neighbor, vrf.name))
        )

        return neighbors

    def _process_bgp_neighbor(
        self, neighbor: EosCliConfigGen.RouterBgp.NeighborsItem | EosCliConfigGen.RouterBgp.VrfsItem.NeighborsItem, vrf: str
    ) -> BgpNeighbor | None:
        """
        Process a BGP neighbor from the structured configuration and return a `BgpNeighbor` object.

        Returns `None` if the neighbor should be skipped.
        """
        if isinstance(neighbor, EosCliConfigGen.RouterBgp.NeighborsItem):
            identifier = f"{neighbor.ip_address}" if neighbor.peer is None else f"{neighbor.peer} ({neighbor.ip_address})"
        else:
            identifier = f"{neighbor.ip_address} (VRF {vrf})"

        # Skip neighbors that are shutdown
        if neighbor.shutdown is True:
            LOGGER.debug("<%s> Skipped BGP peer %s - Shutdown", self.hostname, identifier)
            return None

        # Skip neighbors in shutdown peer groups
        if (
            neighbor.peer_group
            and neighbor.peer_group in self.structured_config.router_bgp.peer_groups
            and self.structured_config.router_bgp.peer_groups[neighbor.peer_group].shutdown is True
        ):
            LOGGER.debug("<%s> Skipped BGP peer %s - Peer group %s shutdown", self.hostname, identifier, neighbor.peer_group)
            return None

        # When peer field is set, check if the peer device is in the fabric and deployed
        if (
            isinstance(neighbor, EosCliConfigGen.RouterBgp.NeighborsItem)
            and neighbor.peer
            and (neighbor.peer not in self.minimal_structured_configs or not self.minimal_structured_configs[neighbor.peer].is_deployed)
        ):
            LOGGER.debug("<%s> Skipped BGP peer %s - Peer not in fabric or not deployed", self.hostname, identifier)
            return None

        # TODO: IPv6 neighbors are not supported in ANTA yet
        ip_address = ip_interface(neighbor.ip_address).ip
        if isinstance(ip_address, IPv6Address):
            LOGGER.debug("<%s> Skipped BGP peer %s - IPv6 not supported", self.hostname, identifier)
            return None

        update_source = neighbor.update_source or (
            self.structured_config.router_bgp.peer_groups[neighbor.peer_group].update_source
            if neighbor.peer_group and neighbor.peer_group in self.structured_config.router_bgp.peer_groups
            else None
        )

        return BgpNeighbor(ip_address=ip_address, vrf=vrf, update_source=update_source)

    @cached_property
    def l3_mtu_interfaces(self) -> tuple[list[dict[str, int]], list[str]]:
        """
        Generate MTU mappings for Layer 3 interfaces.

        This includes:
        - Ethernet interfaces configured in routed mode.
        - Port-channel interfaces configured in routed mode.
        - VLAN interfaces (always treated as routed interfaces).

        Interfaces without an MTU configured or not applicable for L3 validation
        are logged and added to the ignored list.

        Returns:
            A tuple containing:
            - List of dictionaries with interface name and MTU.
            - List of ignored interface names.
        """
        l3_interfaces: list[dict[str, int]] = []
        ignored_interfaces: list[str] = []

        l3_interfaces, ignored_interfaces = self._process_interfaces(
            self.structured_config.ethernet_interfaces, l3_interfaces, ignored_interfaces, is_l2_mtu=False
        )
        l3_interfaces, ignored_interfaces = self._process_interfaces(
            self.structured_config.port_channel_interfaces, l3_interfaces, ignored_interfaces, is_l2_mtu=False
        )

        for vlan_interface in self.structured_config.vlan_interfaces:
            if vlan_interface.mtu is not None:
                l3_interfaces.append({vlan_interface.name: vlan_interface.mtu})
            else:
                LOGGER.debug("%s skipped - no mtu on interface", vlan_interface.name)
                ignored_interfaces.append(vlan_interface.name)

        ignored_interfaces += ["Dps", "Fabric", "Loopback", "Management", "Recirc-Channel", "Tunnel", "Vxlan"]
        return l3_interfaces, ignored_interfaces

    @cached_property
    def l2_mtu_interfaces(self) -> tuple[list[dict[str, int]], list[str]]:
        """
        Generate MTU mappings for Layer 2 interfaces.

        This includes:
        - Ethernet interfaces operating in switchport mode.
        - Port-channel interfaces operating in switchport mode.

        Routed or unsupported interfaces and those without MTU configuration
        are logged and added to the ignored list.

        Returns:
            A tuple containing:
            - List of dictionaries with interface name and MTU.
            - List of ignored interface names.
        """
        l2_interfaces: list[dict[str, int]] = []
        ignored_interfaces: list[str] = []

        l2_interfaces, ignored_interfaces = self._process_interfaces(
            self.structured_config.ethernet_interfaces, l2_interfaces, ignored_interfaces, is_l2_mtu=True
        )
        l2_interfaces, ignored_interfaces = self._process_interfaces(
            self.structured_config.port_channel_interfaces, l2_interfaces, ignored_interfaces, is_l2_mtu=True
        )

        ignored_interfaces += ["Dps", "Fabric", "Loopback", "Management", "Recirc-Channel", "Tunnel", "Vlan", "Vxlan"]
        return l2_interfaces, ignored_interfaces

    def _process_interfaces(
        self,
        interfaces_to_process: EosCliConfigGen.EthernetInterfaces | EosCliConfigGen.PortChannelInterfaces,
        interfaces: list[dict[str, int]],
        ignored_interfaces: list[str],
        is_l2_mtu: bool,
    ) -> tuple[list[dict[str, int]], list[str]]:
        """
        Process a list of interfaces for MTU validation.

        Args:
            interfaces_to_process: List of interface objects to evaluate.
            interfaces: List of collected MTU mappings.
            ignored_interfaces: List to record interfaces excluded from validation.
            is_l2_mtu: Whether the validation is for L2 (switchport) or L3 (routed) context.

        Returns:
            A tuple of (interfaces, ignored_interfaces)
        """
        for interface in interfaces_to_process:
            if interface.validate_state is False:
                LOGGER.debug("%s skipped - validate_state or validate_lldp disabled", interface.name)
                ignored_interfaces.append(interface.name)
                continue

            if is_l2_mtu:
                if interface.switchport and interface.switchport.enabled is False:
                    LOGGER.debug("%s skipped - routed interface", interface.name)
                    ignored_interfaces.append(interface.name)
                    continue
            elif interface.switchport and interface.switchport.enabled is True:
                LOGGER.debug("%s skipped - switchport interface", interface.name)
                ignored_interfaces.append(interface.name)
                continue

            if interface.mtu is not None:
                interfaces.append({interface.name: interface.mtu})
            else:
                LOGGER.debug("%s skipped - no mtu on interface", interface.name)
                ignored_interfaces.append(interface.name)

        return interfaces, ignored_interfaces
