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

    ip_address: IPv4Address | IPv6Address
    vrf: str
    update_source: str | None = None


@dataclass(frozen=True)
class BgpNeighborInterface:
    """Represents a BGP neighbor interface (RFC5549) from the structured configuration."""

    interface: str
    vrf: str


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
        return bool(self.structured_config.vxlan_interface.vxlan1.vxlan._get("source_interface"))

    @cached_property
    def is_wan_router(self) -> bool:
        """Check if the device is a WAN router."""
        return self.is_vtep and "Dps" in self.structured_config.vxlan_interface.vxlan1.vxlan._get("source_interface")

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

    @cached_property
    def bgp_neighbor_interfaces(self) -> list[BgpNeighborInterface]:
        """Generate a list of BGP neighbor interfaces (RFC5549) for the device."""
        neighbor_interfaces = [
            bgp_neighbor_interface
            for neighbor_intf in self.structured_config.router_bgp.neighbor_interfaces
            if (bgp_neighbor_interface := self._process_bgp_neighbor_interface(neighbor_intf, "default"))
        ]

        # Skip VRF processing if disabled
        if not self.input_factory_settings.allow_bgp_vrfs:
            LOGGER.debug("<%s> Skipped BGP VRF RFC5549 peers - VRF processing disabled", self.hostname)
            return neighbor_interfaces

        # Add VRF neighbor interfaces to the list
        neighbor_interfaces.extend(
            bgp_neighbor_interface
            for vrf in self.structured_config.router_bgp.vrfs
            for neighbor_intf in vrf.neighbor_interfaces
            if (bgp_neighbor_interface := self._process_bgp_neighbor_interface(neighbor_intf, vrf.name))
        )

        return neighbor_interfaces

    def _process_bgp_neighbor_interface(
        self, neighbor_interface: EosCliConfigGen.RouterBgp.NeighborInterfacesItem | EosCliConfigGen.RouterBgp.VrfsItem.NeighborInterfacesItem, vrf: str
    ) -> BgpNeighborInterface | None:
        """
        Process a BGP neighbor interface (RFC5549) from the structured configuration and return a `BgpNeighborInterface` object.

        Returns `None` if the neighbor interface should be skipped.
        """
        from_default_vrf = isinstance(neighbor_interface, EosCliConfigGen.RouterBgp.NeighborInterfacesItem)
        if from_default_vrf:
            identifier = f"{neighbor_interface.name}" if neighbor_interface.peer is None else f"{neighbor_interface.peer} ({neighbor_interface.name})"
        else:
            identifier = f"{neighbor_interface.name} (VRF {vrf})"

        # Skip neighbor interfaces in shutdown peer groups
        if (
            neighbor_interface.peer_group
            and neighbor_interface.peer_group in self.structured_config.router_bgp.peer_groups
            and self.structured_config.router_bgp.peer_groups[neighbor_interface.peer_group].shutdown is True
        ):
            LOGGER.debug("<%s> Skipped BGP peer %s - Peer group %s shutdown", self.hostname, identifier, neighbor_interface.peer_group)
            return None

        # When peer field is set, check if the peer device is in the fabric and deployed
        if (
            from_default_vrf
            and neighbor_interface.peer
            and (neighbor_interface.peer not in self.minimal_structured_configs or not self.minimal_structured_configs[neighbor_interface.peer].is_deployed)
        ):
            LOGGER.debug("<%s> Skipped BGP peer %s - Peer not in fabric or not deployed", self.hostname, identifier)
            return None

        return BgpNeighborInterface(interface=neighbor_interface.name, vrf=vrf)

    def _process_bgp_neighbor(
        self, neighbor: EosCliConfigGen.RouterBgp.NeighborsItem | EosCliConfigGen.RouterBgp.VrfsItem.NeighborsItem, vrf: str
    ) -> BgpNeighbor | None:
        """
        Process a BGP neighbor from the structured configuration and return a `BgpNeighbor` object.

        Returns `None` if the neighbor should be skipped.
        """
        from_default_vrf = isinstance(neighbor, EosCliConfigGen.RouterBgp.NeighborsItem)
        if from_default_vrf:
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
            from_default_vrf
            and neighbor.peer
            and (neighbor.peer not in self.minimal_structured_configs or not self.minimal_structured_configs[neighbor.peer].is_deployed)
        ):
            LOGGER.debug("<%s> Skipped BGP peer %s - Peer not in fabric or not deployed", self.hostname, identifier)
            return None

        update_source = neighbor.update_source or (
            self.structured_config.router_bgp.peer_groups[neighbor.peer_group].update_source
            if neighbor.peer_group and neighbor.peer_group in self.structured_config.router_bgp.peer_groups
            else None
        )

        return BgpNeighbor(ip_address=ip_interface(neighbor.ip_address).ip, vrf=vrf, update_source=update_source)
