# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import ipaddress
from functools import cached_property
from typing import TYPE_CHECKING

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServices


class StaticRoutesMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def static_routes(self: AvdStructuredConfigNetworkServices) -> list[dict] | None:
        """
        Returns structured config for static_routes.

        Consist of
        - static_routes defined under the vrfs
        - static routes added automatically for VARP with prefixes
        """
        if not self.shared_utils.network_services_l3:
            return None

        static_routes = []
        for tenant in self.shared_utils.filtered_tenants:
            for vrf in tenant["vrfs"]:
                # Static routes are already filtered inside filtered_tenants
                for static_route in vrf["static_routes"]:
                    static_route["vrf"] = vrf["name"]
                    static_route.pop("nodes", None)

                    # Ignore duplicate items in case of duplicate VRF definitions across multiple tenants.
                    if static_route not in static_routes:
                        static_routes.append(static_route)

                for svi in vrf["svis"]:
                    if "ip_virtual_router_addresses" not in svi or "ip_address" not in svi:
                        # Skip svi if VARP is not set or if there is no unique ip_address
                        continue

                    for virtual_router_address in svi["ip_virtual_router_addresses"]:
                        if "/" not in virtual_router_address:
                            # Only create static routes for VARP entries with masks
                            continue

                        static_route = {
                            "destination_address_prefix": str(ipaddress.ip_network(virtual_router_address, strict=False)),
                            "vrf": vrf["name"],
                            "name": "VARP",
                            "interface": f"Vlan{svi['id']}",
                        }

                        # Ignore duplicate items in case of duplicate VRF definitions across multiple tenants.
                        if static_route not in static_routes:
                            static_routes.append(static_route)

        for internet_exit_policy in self._filtered_internet_exit_policies:
            for connection in internet_exit_policy.get("connections", []):
                if connection["type"] == "tunnel":
                    static_route = {
                        "destination_address_prefix": f"{connection['tunnel_destination_ip']}/32",
                        "name": f"IE-ZSCALER-{connection['suffix']}",
                        "gateway": connection["next_hop"],
                    }
                    # Ignore duplicate items in case of multiple connections generating the same route
                    if static_route not in static_routes:
                        static_routes.append(static_route)

        if static_routes:
            return static_routes

        return None
