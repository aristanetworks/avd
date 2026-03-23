# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""
Structured Config Utils Module.

This module provides utility classes for structured config generation.
"""

from __future__ import annotations

import ipaddress
from typing import TYPE_CHECKING, Literal

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.parent_interfaces import ParentInterfacesTracker
from pyavd._utils.run_once import RunOnceMethodStateHelper, run_once_method

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns
    from pyavd._eos_designs.shared_utils import SharedUtilsProtocol

    _VrfsItem = EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem


class StructuredConfigUtils(RunOnceMethodStateHelper):
    """
    Utility class for structured config generation.

    This class holds shared utilities and trackers used across all structured config modules.
    """

    def __init__(
        self,
        structured_config: EosCliConfigGen,
        inputs: EosDesigns,
        shared_utils: SharedUtilsProtocol,
    ) -> None:
        """Initialize the StructuredConfigUtils with a ParentInterfacesTracker instance and structured config instance."""
        super().__init__()
        self.structured_config = structured_config
        self.inputs = inputs
        self.shared_utils = shared_utils
        """The shared structured config instance to write config into."""
        self.parent_interfaces_tracker = ParentInterfacesTracker()
        """Tracker for parent interfaces that need to be created for subinterfaces."""

    def set_static_routes(
        self,
        static_route_type: Literal["ipv4", "ipv6"],
        gateway: str | None,
        vrf: str | None,
        destination_networks: EosDesigns.MgmtDestinationNetworks | EosDesigns.Ipv6MgmtDestinationNetworks | None = None,
        default_prefix: str = "",
    ) -> None:
        """Append static routes for a gateway."""
        if gateway is None:
            return

        routes = self.structured_config.static_routes if static_route_type == "ipv4" else self.structured_config.ipv6_static_routes
        for prefix in destination_networks or [default_prefix]:
            routes.append_new(vrf=vrf, prefix=prefix, next_hop=gateway)

    @run_once_method
    def set_once_mgmt_static_routes(self) -> None:
        """Populate static_routes and ipv6_static_routes from management gateway config in a single pass."""
        self.set_static_routes(
            "ipv4",
            self.shared_utils.mgmt_gateway,
            self.inputs.mgmt_interface_vrf,
            self.inputs.mgmt_destination_networks,
            "0.0.0.0/0",
        )

        if self.shared_utils.node_config.ipv6_mgmt_ip is not None:
            self.set_static_routes(
                "ipv6",
                self.shared_utils.ipv6_mgmt_gateway,
                self.inputs.mgmt_interface_vrf,
                self.inputs.ipv6_mgmt_destination_networks,
                "::/0",
            )

    def _add_vrf_static_routes(self, vrf: _VrfsItem) -> None:
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

    def _add_varp_static_routes(self, vrf: _VrfsItem) -> None:
        """Append auto-generated VARP static routes for SVIs with ip_virtual_router_addresses."""
        for svi in vrf.svis:
            if not svi.ip_virtual_router_addresses or not svi.ip_address:
                continue

            for virtual_router_address in svi.ip_virtual_router_addresses:
                if "/" not in virtual_router_address:
                    continue

                self.structured_config.static_routes.append_unique(
                    EosCliConfigGen.StaticRoutesItem(
                        prefix=str(ipaddress.ip_network(virtual_router_address, strict=False)),
                        vrf=vrf.name,
                        name="VARP",
                        interface=f"Vlan{svi.id}",
                    )
                )

    def _add_vrf_ipv6_static_routes(self, vrf: _VrfsItem) -> None:
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
    def set_once_static_routes_from_network_services(self) -> None:
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

    @run_once_method
    def set_once_inband_mgmt_static_routes(self) -> None:
        """Populate static_routes and ipv6_static_routes from inband management config in a single pass."""
        if self.shared_utils.configure_inband_mgmt:
            self.set_static_routes(
                "ipv4",
                self.shared_utils.inband_mgmt_gateway,
                self.shared_utils.inband_mgmt_vrf,
                default_prefix="0.0.0.0/0",
            )

        if self.shared_utils.configure_inband_mgmt_ipv6:
            self.set_static_routes(
                "ipv6",
                self.shared_utils.inband_mgmt_ipv6_gateway,
                self.shared_utils.inband_mgmt_vrf,
                default_prefix="::/0",
            )


__all__ = ["StructuredConfigUtils"]
