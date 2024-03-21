# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.filter.natural_sort import natural_sort

from .utils import UtilsMixin


class RouteMapsMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def route_maps(self) -> list | None:
        """
        Return structured config for route_maps
        """

        if self.shared_utils.overlay_cvx:
            return None

        route_maps = []

        if self.shared_utils.overlay_routing_protocol == "ebgp":
            if self.shared_utils.evpn_prevent_readvertise_to_server is True:
                remote_asns = natural_sort(set(rs_dict.get("bgp_as") for route_server, rs_dict in self._evpn_route_servers.items()))
                for remote_asn in remote_asns:
                    route_map_name = f"RM-EVPN-FILTER-AS{remote_asn}"
                    route_maps.append(
                        {
                            "name": route_map_name,
                            "sequence_numbers": [
                                {
                                    "sequence": 10,
                                    "type": "deny",
                                    "match": [f"as {remote_asn}"],
                                },
                                {
                                    "sequence": 20,
                                    "type": "permit",
                                },
                            ],
                        }
                    )

        elif self.shared_utils.overlay_routing_protocol == "ibgp" and self.shared_utils.overlay_vtep and self.shared_utils.evpn_role != "server":
            # Route-map IN and OUT for SOO
            route_maps.append(
                {
                    "name": "RM-EVPN-SOO-IN",
                    "sequence_numbers": [
                        {
                            "sequence": 10,
                            "type": "deny",
                            "match": ["extcommunity ECL-EVPN-SOO"],
                        },
                        {
                            "sequence": 20,
                            "type": "permit",
                        },
                    ],
                }
            )
            route_maps.append(
                {
                    "name": "RM-EVPN-SOO-OUT",
                    "sequence_numbers": [
                        {
                            "sequence": 10,
                            "type": "permit",
                            "match": ["extcommunity ECL-EVPN-SOO"],
                            # "set": [f"extcommunity soo {self.shared_utils.evpn_soo} additive"],
                        },
                    ],
                }
            )
            if self.shared_utils.wan_ha:
                route_maps.append(
                    {
                        "name": "RM-WAN-HA-LOCAL-PREF-IN",
                        "sequence_numbers": [
                            {
                                "sequence": 10,
                                "type": "permit",
                                "description": "Make EVPN routes originated from WAN HA peer less preferred and tag them",
                                "set": ["local-preference 75", "tag 50"],
                            },
                            {
                                "sequence": 20,
                                "type": "permit",
                                "description": "Make EVPN routes received by WAN HA peer less preferred and tag them",
                                "set": ["local-preference 50", "tag 50"],
                            },
                        ],
                    }
                )

        if route_maps:
            return route_maps

        return None
