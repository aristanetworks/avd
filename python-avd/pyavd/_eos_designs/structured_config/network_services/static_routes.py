# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import ipaddress
from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor
from pyavd._utils.run_once import run_once_method

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns

    from . import AvdStructuredConfigNetworkServicesProtocol

    _VrfsItem = EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem


class StaticRoutesMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    def _add_vrf_static_routes(self: AvdStructuredConfigNetworkServicesProtocol, vrf: _VrfsItem) -> None:
        """Append static routes defined under a VRF to structured config."""
        for static_route in vrf.static_routes:
            self.structured_config.static_routes.append_unique(
                EosCliConfigGen.StaticRoutesItem(
                    vrf=vrf.name,
                    prefix=static_route.prefix,
                    interface=static_route.interface,
                    next_hop=static_route.next_hop,
                    track_bfd=static_route.track_bfd,
                    distance=static_route.distance,
                    tag=static_route.tag,
                    metric=static_route.metric,
                    name=static_route.name,
                )
            )

    def _add_varp_static_routes(self: AvdStructuredConfigNetworkServicesProtocol, vrf: _VrfsItem) -> None:
        """Append auto-generated VARP static routes for SVIs with ip_virtual_router_addresses."""
        for svi in vrf.svis:
            if not svi.ip_virtual_router_addresses or not svi.ip_address:
                # Skip svi if VARP is not set or if there is no unique ip_address
                continue

            for virtual_router_address in svi.ip_virtual_router_addresses:
                if "/" not in virtual_router_address:
                    # Only create static routes for VARP entries with masks
                    continue

                self.structured_config.static_routes.append_unique(
                    EosCliConfigGen.StaticRoutesItem(
                        prefix=str(ipaddress.ip_network(virtual_router_address, strict=False)),
                        vrf=vrf.name,
                        name="VARP",
                        interface=f"Vlan{svi.id}",
                    )
                )

    def _add_vrf_ipv6_static_routes(self: AvdStructuredConfigNetworkServicesProtocol, vrf: _VrfsItem) -> None:
        """Append IPv6 static routes defined under a VRF to structured config."""
        for static_route in vrf.ipv6_static_routes:
            static_route_item = EosCliConfigGen.Ipv6StaticRoutesItem()
            static_route_item._update(
                vrf=vrf.name,
                prefix=static_route.prefix,
                interface=static_route.interface,
                next_hop=static_route.next_hop,
                track_bfd=static_route.track_bfd,
                distance=static_route.distance,
                tag=static_route.tag,
                metric=static_route.metric,
                name=static_route.name,
            )
            self.structured_config.ipv6_static_routes.append_unique(static_route_item)

    @run_once_method
    def set_once_static_routes_from_network_services(self: AvdStructuredConfigNetworkServicesProtocol) -> None:
        """
        Populate both static_routes and ipv6_static_routes from network services VRFs in a single pass.

        Called by both static_routes() and ipv6_static_routes() contributor methods.
        Uses @run_once_method to ensure the tenant/VRF iteration executes only once per render.
        """
        if not self.shared_utils.network_services_l3:
            return

        for tenant in self.shared_utils.filtered_tenants:
            for vrf in tenant.vrfs:
                self._add_vrf_static_routes(vrf)
                self._add_varp_static_routes(vrf)
                self._add_vrf_ipv6_static_routes(vrf)

    @structured_config_contributor
    def static_routes(self: AvdStructuredConfigNetworkServicesProtocol) -> None:
        """
        Set the structured config for static_routes.

        Consist of
        - static_routes defined under the vrfs
        - static routes added automatically for VARP with prefixes
        """
        self.set_once_static_routes_from_network_services()

    def set_zscaler_ie_connection_static_route(self: AvdStructuredConfigNetworkServicesProtocol, destination_ip: str, name: str, next_hop: str) -> None:
        """Set the static route for one Zscaler Internet Exit connection."""
        self.structured_config.static_routes.append_unique(
            EosCliConfigGen.StaticRoutesItem(
                prefix=f"{destination_ip}/32",
                name=name,
                next_hop=next_hop,
            )
        )
