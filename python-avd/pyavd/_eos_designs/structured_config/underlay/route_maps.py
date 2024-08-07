# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._utils import get

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigUnderlay


class RouteMapsMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def route_maps(self: AvdStructuredConfigUnderlay) -> list | None:
        """
        Return structured config for route_maps.

        Contains two parts.
        - Route map for connected routes redistribution in BGP
        - Route map to filter peer AS in underlay
        """
        if not self.shared_utils.underlay_bgp and not self.shared_utils.is_wan_router:
            return None

        route_maps = []

        if self.shared_utils.overlay_routing_protocol != "none" and self.shared_utils.underlay_filter_redistribute_connected:
            # RM-CONN-2-BGP
            sequence_10 = {
                "sequence": 10,
                "type": "permit",
                "match": ["ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY"],
            }
            if self.shared_utils.wan_role:
                sequence_10["set"] = [f"extcommunity soo {self.shared_utils.evpn_soo} additive"]

            sequence_numbers = [sequence_10]
            # SEQ 20 is set by inband management if applicable, so avoid setting that here

            if self.shared_utils.underlay_ipv6 is True:
                sequence_numbers.append(
                    {
                        "sequence": 30,
                        "type": "permit",
                        "match": ["ipv6 address prefix-list PL-LOOPBACKS-EVPN-OVERLAY-V6"],
                    },
                )

            if self.shared_utils.underlay_multicast_rp_interfaces is not None:
                sequence_numbers.append(
                    {
                        "sequence": 40,
                        "type": "permit",
                        "match": ["ip address prefix-list PL-LOOPBACKS-PIM-RP"],
                    },
                )

            if self.shared_utils.wan_ha and self.shared_utils.use_uplinks_for_wan_ha:
                sequence_numbers.append(
                    {
                        "sequence": 50,
                        "type": "permit",
                        "match": ["ip address prefix-list PL-WAN-HA-PREFIXES"],
                    },
                )

            route_maps.append({"name": "RM-CONN-2-BGP", "sequence_numbers": sequence_numbers})

        # RM-BGP-AS{{ asn }}-OUT
        for asn in self._underlay_filter_peer_as_route_maps_asns:
            route_map_name = f"RM-BGP-AS{asn}-OUT"
            route_maps.append(
                {
                    "name": route_map_name,
                    "sequence_numbers": [
                        {
                            "sequence": 10,
                            "type": "deny",
                            "match": [f"as {asn}"],
                        },
                        {
                            "sequence": 20,
                            "type": "permit",
                        },
                    ],
                },
            )

        # Route-map IN and OUT for SOO, rendered for WAN routers
        if self.shared_utils.underlay_routing_protocol == "ebgp" and self.shared_utils.wan_role == "client":
            # RM-BGP-UNDERLAY-PEERS-IN
            sequence_numbers = [
                {
                    "sequence": 40,
                    "type": "permit",
                    "description": "Mark prefixes originated from the LAN",
                    "set": [f"extcommunity soo {self.shared_utils.evpn_soo} additive"],
                },
            ]
            if self.shared_utils.wan_ha and self.shared_utils.use_uplinks_for_wan_ha:
                sequence_numbers.extend(
                    [
                        {
                            "sequence": 10,
                            "type": "permit",
                            "description": "Allow WAN HA peer interface prefixes",
                            "match": ["ip address prefix-list PL-WAN-HA-PEER-PREFIXES"],
                        },
                        {
                            "sequence": 20,
                            "type": "deny",
                            "description": "Deny other routes from the HA peer",
                            "match": ["as-path ASPATH-WAN"],
                        },
                    ],
                )
            route_maps.append({"name": "RM-BGP-UNDERLAY-PEERS-IN", "sequence_numbers": sequence_numbers})

            # RM-BGP-UNDERLAY-PEERS-OUT
            if self.shared_utils.wan_ha:
                sequence_numbers = [
                    {
                        "sequence": 10,
                        "type": "permit",
                        "description": "Make routes learned from WAN HA peer less preferred on LAN routers",
                        "match": ["tag 50", "route-type internal"],
                        "set": ["metric 50"],
                    },
                    {
                        "sequence": 20,
                        "type": "permit",
                    },
                ]
                route_maps.append({"name": "RM-BGP-UNDERLAY-PEERS-OUT", "sequence_numbers": sequence_numbers})

        for neighbor in self.shared_utils.l3_interfaces_bgp_neighbors:
            # RM-BGP-<PEER-IP>-IN
            if prefix_list_in := get(neighbor, "ipv4_prefix_list_in"):
                sequence_numbers = [
                    {
                        "sequence": 10,
                        "type": "permit",
                        "match": [f"ip address prefix-list {prefix_list_in}"],
                    },
                ]
                # set no advertise is set only for wan neighbors, which will also have
                # prefix_list_in
                if neighbor.get("set_no_advertise"):
                    sequence_numbers[0]["set"] = ["community no-advertise additive"]

                route_maps.append({"name": neighbor["route_map_in"], "sequence_numbers": sequence_numbers})

            # RM-BGP-<PEER-IP>-OUT
            if prefix_list_out := get(neighbor, "ipv4_prefix_list_out"):
                sequence_numbers = [
                    {
                        "sequence": 10,
                        "type": "permit",
                        "match": [f"ip address prefix-list {prefix_list_out}"],
                    },
                    {
                        "sequence": 20,
                        "type": "deny",
                    },
                ]
            else:
                sequence_numbers = [
                    {
                        "sequence": 10,
                        "type": "deny",
                    },
                ]

            route_maps.append({"name": neighbor["route_map_out"], "sequence_numbers": sequence_numbers})

        if route_maps:
            return route_maps

        return None
