# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.utils import append_if_not_duplicate

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

        Contains two parts.
        - Route-maps for tenant bgp peers set_ipv4_next_hop parameter
        - Route-maps for EVPN services in VRF "default" (using _route_maps_default_vrf)
        - Route-map for tenant redistribute connected if any VRF is not redistributing MLAG peer subnet
        """
        if not self.shared_utils.network_services_l3:
            return None

        route_maps = []

        for tenant in self._filtered_tenants:
            for vrf in tenant["vrfs"]:
                # BGP Peers are already filtered in _filtered_tenants
                #  so we only have entries with our hostname in them.
                for bgp_peer in vrf["bgp_peers"]:
                    ipv4_next_hop = bgp_peer.get("set_ipv4_next_hop")
                    ipv6_next_hop = bgp_peer.get("set_ipv6_next_hop")
                    if ipv4_next_hop is None and ipv6_next_hop is None:
                        continue

                    route_map_name = f"RM-{vrf['name']}-{bgp_peer['ip_address']}-SET-NEXT-HOP-OUT"
                    if ipv4_next_hop is not None:
                        set_action = f"ip next-hop {ipv4_next_hop}"
                    else:
                        set_action = f"ipv6 next-hop {ipv6_next_hop}"

                    route_map = {
                        "name": route_map_name,
                        "sequence_numbers": [
                            {
                                "sequence": 10,
                                "type": "permit",
                                "set": [set_action],
                            },
                        ],
                    }
                    append_if_not_duplicate(
                        list_of_dicts=route_maps,
                        primary_key="name",
                        new_dict=route_map,
                        context="Route-Maps",
                        context_keys=["name"],
                    )

        if (route_maps_vrf_default := self._route_maps_vrf_default) is not None:
            route_maps.extend(route_maps_vrf_default)

        if self._configure_bgp_mlag_peer_group and self.shared_utils.mlag_ibgp_origin_incomplete:
            route_maps.append(self._bgp_mlag_peer_group_route_map())

        if self._mlag_ibgp_peering_subnets_without_redistribution:
            route_maps.append(self._connected_to_bgp_vrfs_route_map())

        if route_maps:
            return route_maps

        return None

    @cached_property
    def _route_maps_vrf_default(self) -> list | None:
        """
        Route-maps for EVPN services in VRF "default"

        Called from main route_maps function
        """
        if not self._vrf_default_evpn:
            return None

        subnets = self._vrf_default_ipv4_subnets
        static_routes = self._vrf_default_ipv4_static_routes["static_routes"]
        if not subnets and not static_routes:
            return None

        vrf_default = {
            "name": "RM-EVPN-EXPORT-VRF-DEFAULT",
            "sequence_numbers": [],
        }

        peers_out = {
            "name": "RM-BGP-UNDERLAY-PEERS-OUT",
            "sequence_numbers": [
                {
                    "sequence": 20,
                    "type": "permit",
                },
            ],
        }

        if subnets:
            vrf_default["sequence_numbers"].append(
                {
                    "sequence": 10,
                    "type": "permit",
                    "match": ["ip address prefix-list PL-SVI-VRF-DEFAULT"],
                }
            )

            peers_out["sequence_numbers"].append(
                {
                    "sequence": 10,
                    "type": "deny",
                    "match": ["ip address prefix-list PL-SVI-VRF-DEFAULT"],
                }
            )

        if static_routes:
            vrf_default["sequence_numbers"].append(
                {
                    "sequence": 20,
                    "type": "permit",
                    "match": ["ip address prefix-list PL-STATIC-VRF-DEFAULT"],
                }
            )

            peers_out["sequence_numbers"].append(
                {
                    "sequence": 15,
                    "type": "deny",
                    "match": ["ip address prefix-list PL-STATIC-VRF-DEFAULT"],
                }
            )

        if not self.shared_utils.underlay_filter_redistribute_connected:
            return [vrf_default, peers_out]

        bgp = {
            "name": "RM-CONN-2-BGP",
            "sequence_numbers": [
                # Add subnets to redistribution in default VRF
                # sequence 10 is set in underlay and sequence 20 in inband management, so avoid setting those here
                {
                    "sequence": 30,
                    "type": "permit",
                    "match": ["ip address prefix-list PL-SVI-VRF-DEFAULT"],
                },
            ],
        }

        return [vrf_default, peers_out, bgp]

    def _bgp_mlag_peer_group_route_map(self) -> dict:
        """
        Return dict with one route-map
        Origin Incomplete for MLAG iBGP learned routes

        TODO: Partially duplicated from mlag. Should be moved to a common class
        """
        return {
            "name": "RM-MLAG-PEER-IN",
            "sequence_numbers": [
                {
                    "sequence": 10,
                    "type": "permit",
                    "set": ["origin incomplete"],
                    "description": "Make routes learned over MLAG Peer-link less preferred on spines to ensure optimal routing",
                }
            ],
        }

    def _connected_to_bgp_vrfs_route_map(self) -> dict:
        """
        Return dict with one route-map
        Filter MLAG peer subnets for redistribute connected for overlay VRFs
        """
        return {
            "name": "RM-CONN-2-BGP-VRFS",
            "sequence_numbers": [
                {
                    "sequence": 10,
                    "type": "deny",
                    "match": ["ip address prefix-list PL-MLAG-PEER-VRFS"],
                },
                {
                    "sequence": 20,
                    "type": "permit",
                },
            ],
        }
