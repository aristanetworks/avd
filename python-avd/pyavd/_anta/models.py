# Copyright (c) 2023-2026 Arista Networks, Inc.
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
from pyavd._errors import AristaAvdError
from pyavd.j2filters import natural_sort

if TYPE_CHECKING:
    from pyavd.api._anta import AvdCatalogGenerationSettings, AvdFabricData
    from pyavd.api._anta.avd_fabric_data import AvdDeviceData, AvdEthernetInterface

LOGGER = getLogger(__name__)


@dataclass(frozen=True)
class ResolvedBgpNeighbor:
    """Model to represent a BGP neighbor resolved from the structured configuration."""

    ip_address: IPv4Address | IPv6Address
    vrf: str
    update_source: str | None = None


@dataclass(frozen=True)
class ResolvedBgpNeighborInterface:
    """Model to represent a BGP neighbor interface (RFC5549) resolved from the structured configuration."""

    interface: str
    vrf: str


@dataclass
class InputFactoryDataSource:
    """Model to store the data required by the input factories to generate test inputs to build an ANTA catalog for a single device."""

    hostname: str
    structured_config: EosCliConfigGen
    _fabric_data: AvdFabricData
    _settings: AvdCatalogGenerationSettings

    @property
    def is_vtep(self) -> bool:
        """Check if the device is a VTEP."""
        return self._device_data.is_vtep

    @property
    def is_wan_router(self) -> bool:
        """Check if the device is a WAN router."""
        return self._device_data.is_wan_router

    @property
    def extra_fabric_validation(self) -> bool:
        """Check if extra fabric-wide validation inputs should be generated."""
        return self._settings.extra_fabric_validation

    @cached_property
    def _device_data(self) -> AvdDeviceData:
        """Get the AvdDeviceData object for this device."""
        device_data = self._fabric_data.devices.get(self.hostname)
        if device_data is None:
            raise AristaAvdError(message=f"Device '{self.hostname}' structured configuration is not loaded in AvdFabricData.")
        return device_data

    @cached_property
    def special_ips(self) -> list[IPv4Address]:
        """Get a sorted list of all 'special' IPv4 addresses (Loopback0, VTEP, and MLAG VTEP) from deployed non-WAN devices in the fabric."""
        return natural_sort(self._fabric_data.special_ips)

    @cached_property
    def bgp_neighbors(self) -> list[ResolvedBgpNeighbor]:
        """Generate a list of BGP neighbors for the device."""
        neighbors = [
            bgp_neighbor for neighbor in self.structured_config.router_bgp.neighbors if (bgp_neighbor := self._process_bgp_neighbor(neighbor, "default"))
        ]
        neighbors.extend(
            bgp_neighbor
            for vrf in self.structured_config.router_bgp.vrfs
            for neighbor in vrf.neighbors
            if (bgp_neighbor := self._process_bgp_neighbor(neighbor, vrf.name))
        )

        return neighbors

    @cached_property
    def bgp_neighbor_interfaces(self) -> list[ResolvedBgpNeighborInterface]:
        """Generate a list of BGP neighbor interfaces (RFC5549) for the device."""
        neighbor_interfaces = [
            bgp_neighbor_interface
            for neighbor_intf in self.structured_config.router_bgp.neighbor_interfaces
            if (bgp_neighbor_interface := self._process_bgp_neighbor_interface(neighbor_intf, "default"))
        ]
        neighbor_interfaces.extend(
            bgp_neighbor_interface
            for vrf in self.structured_config.router_bgp.vrfs
            for neighbor_intf in vrf.neighbor_interfaces
            if (bgp_neighbor_interface := self._process_bgp_neighbor_interface(neighbor_intf, vrf.name))
        )

        return neighbor_interfaces

    def get_peer_device(self, peer_hostname: str) -> AvdDeviceData | None:
        """Return the peer device data if it exists and is deployed."""
        device = self._fabric_data.devices.get(peer_hostname)
        if device and device.is_deployed:
            return device
        return None

    def get_peer_interface(self, peer_hostname: str, interface_name: str) -> AvdEthernetInterface | None:
        """Return the Ethernet interface data for a peer, or None if peer/interface is missing."""
        peer = self.get_peer_device(peer_hostname)
        if peer:
            return peer.ethernet_interfaces.get(interface_name)
        return None

    def _process_bgp_neighbor_interface(
        self, neighbor_interface: EosCliConfigGen.RouterBgp.NeighborInterfacesItem | EosCliConfigGen.RouterBgp.VrfsItem.NeighborInterfacesItem, vrf: str
    ) -> ResolvedBgpNeighborInterface | None:
        """
        Process a BGP neighbor interface (RFC5549) from the structured configuration and return a `BgpNeighborInterface` object.

        Returns `None` if the neighbor interface should be skipped.
        """
        from_default_vrf = isinstance(neighbor_interface, EosCliConfigGen.RouterBgp.NeighborInterfacesItem)
        if from_default_vrf:
            identifier = (
                f"{neighbor_interface.name}" if neighbor_interface.metadata.peer is None else f"{neighbor_interface.metadata.peer} ({neighbor_interface.name})"
            )
        else:
            identifier = f"{neighbor_interface.name} (VRF {vrf})"

        # Skip neighbor interfaces if `metadata.validate_state` is disabled
        if not neighbor_interface.metadata.validate_state:
            LOGGER.debug("<%s> Skipped BGP peer %s - validate_state disabled", self.hostname, identifier)
            return None

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
            and neighbor_interface.metadata.peer
            and (
                neighbor_interface.metadata.peer not in self._fabric_data.devices or not self._fabric_data.devices[neighbor_interface.metadata.peer].is_deployed
            )
        ):
            LOGGER.debug("<%s> Skipped BGP peer %s - Peer not in fabric or not deployed", self.hostname, identifier)
            return None

        return ResolvedBgpNeighborInterface(interface=neighbor_interface.name, vrf=vrf)

    def _process_bgp_neighbor(
        self, neighbor: EosCliConfigGen.RouterBgp.NeighborsItem | EosCliConfigGen.RouterBgp.VrfsItem.NeighborsItem, vrf: str
    ) -> ResolvedBgpNeighbor | None:
        """
        Process a BGP neighbor from the structured configuration and return a `BgpNeighbor` object.

        Returns `None` if the neighbor should be skipped.
        """
        from_default_vrf = isinstance(neighbor, EosCliConfigGen.RouterBgp.NeighborsItem)
        if from_default_vrf:
            identifier = f"{neighbor.ip_address}" if neighbor.metadata.peer is None else f"{neighbor.metadata.peer} ({neighbor.ip_address})"
        else:
            identifier = f"{neighbor.ip_address} (VRF {vrf})"

        # Skip neighbors if `metadata.validate_state` is disabled
        if not neighbor.metadata.validate_state:
            LOGGER.debug("<%s> Skipped BGP peer %s - validate_state disabled", self.hostname, identifier)
            return None

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
            and neighbor.metadata.peer
            and (neighbor.metadata.peer not in self._fabric_data.devices or not self._fabric_data.devices[neighbor.metadata.peer].is_deployed)
        ):
            LOGGER.debug("<%s> Skipped BGP peer %s - Peer not in fabric or not deployed", self.hostname, identifier)
            return None

        update_source = neighbor.update_source or (
            self.structured_config.router_bgp.peer_groups[neighbor.peer_group].update_source
            if neighbor.peer_group and neighbor.peer_group in self.structured_config.router_bgp.peer_groups
            else None
        )

        return ResolvedBgpNeighbor(ip_address=ip_interface(neighbor.ip_address).ip, vrf=vrf, update_source=update_source)
