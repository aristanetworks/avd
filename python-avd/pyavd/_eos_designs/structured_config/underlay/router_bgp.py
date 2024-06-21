# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from ...._utils import append_if_not_duplicate, get, strip_empties_from_dict
from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigUnderlay


class RouterBgpMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def router_bgp(self: AvdStructuredConfigUnderlay) -> dict | None:
        """
        Return the structured config for router_bgp
        """

        if not self.shared_utils.underlay_bgp:
            if self.shared_utils.is_wan_router:
                # Configure redistribute connected with or without route-map in case it the underlay is not BGP.
                # TODO: Currently only implemented for WAN routers but should probably be
                # implemented for anything with EVPN services in default VRF.
                return {"redistribute_routes": self._router_bgp_redistribute_routes}

            return None

        router_bgp = {}

        peer_group = {
            "name": self.shared_utils.bgp_peer_groups["ipv4_underlay_peers"]["name"],
            "type": "ipv4",
            "password": self.shared_utils.bgp_peer_groups["ipv4_underlay_peers"]["password"],
            "bfd": self.shared_utils.bgp_peer_groups["ipv4_underlay_peers"]["bfd"],
            "maximum_routes": 12000,
            "send_community": "all",
            "struct_cfg": self.shared_utils.bgp_peer_groups["ipv4_underlay_peers"]["structured_config"],
        }

        if self.shared_utils.overlay_routing_protocol == "ibgp" and self.shared_utils.is_cv_pathfinder_router:
            peer_group["route_map_in"] = "RM-BGP-UNDERLAY-PEERS-IN"
            # TODO: no RM-BGP-UNDERLAY-PEERS-OUT route-map, one will be added in a future PR for HA.
            if self.shared_utils.wan_ha:
                # For HA need to add allowas_in 1
                peer_group["allowas_in"] = {"enabled": True, "times": 1}

        router_bgp["peer_groups"] = [strip_empties_from_dict(peer_group)]

        # Address Families
        # TODO - see if it makes sense to extract logic in method
        address_family_ipv4_peer_group = {"activate": True}

        if self.shared_utils.underlay_rfc5549 is True:
            address_family_ipv4_peer_group["next_hop"] = {"address_family_ipv6": {"enabled": True, "originate": True}}

        router_bgp["address_family_ipv4"] = {
            "peer_groups": [{"name": self.shared_utils.bgp_peer_groups["ipv4_underlay_peers"]["name"], **address_family_ipv4_peer_group}]
        }

        if self.shared_utils.underlay_ipv6 is True:
            router_bgp["address_family_ipv6"] = {"peer_groups": [{"name": self.shared_utils.bgp_peer_groups["ipv4_underlay_peers"]["name"], "activate": True}]}

        # Redistribute routes
        router_bgp["redistribute_routes"] = self._router_bgp_redistribute_routes

        vrfs_dict = {}

        # Neighbor Interfaces and VRF Neighbor Interfaces
        if self.shared_utils.underlay_rfc5549 is True:
            neighbor_interfaces = []
            for link in self._underlay_links:
                if link["type"] != "underlay_p2p":
                    continue

                neighbor_interfaces.append(
                    {
                        "name": link["interface"],
                        "peer_group": self.shared_utils.bgp_peer_groups["ipv4_underlay_peers"]["name"],
                        "remote_as": link["peer_bgp_as"],
                        "peer": link["peer"],
                        "description": "_".join([link["peer"], link["peer_interface"]]),
                    }
                )

                if "subinterfaces" in link:
                    for subinterface in link["subinterfaces"]:
                        vrfs_dict.setdefault(
                            subinterface["vrf"],
                            {
                                "name": subinterface["vrf"],
                                "router_id": self.shared_utils.router_id,
                                "neighbor_interfaces": [],
                            },
                        )
                        vrfs_dict[subinterface["vrf"]]["neighbor_interfaces"].append(
                            {
                                "name": subinterface["interface"],
                                "peer_group": self.shared_utils.bgp_peer_groups["ipv4_underlay_peers"]["name"],
                                "remote_as": link["peer_bgp_as"],
                                # TODO - implement some centralized way to generate these descriptions
                                "description": f"{'_'.join([link['peer'], subinterface['peer_interface']])}_vrf_{subinterface['vrf']}",
                            }
                        )

            if neighbor_interfaces:
                router_bgp["neighbor_interfaces"] = neighbor_interfaces

        # Neighbors and VRF Neighbors
        else:
            neighbors = []
            for link in self._underlay_links:
                if link["type"] != "underlay_p2p":
                    continue

                neighbor = {
                    "ip_address": link["peer_ip_address"],
                    "peer_group": self.shared_utils.bgp_peer_groups["ipv4_underlay_peers"]["name"],
                    "remote_as": get(link, "peer_bgp_as"),
                    "peer": link["peer"],
                    "description": "_".join([link["peer"], link["peer_interface"]]),
                    "bfd": get(link, "bfd"),
                }

                if self.shared_utils.shutdown_bgp_towards_undeployed_peers is True and link["peer_is_deployed"] is False:
                    neighbor["shutdown"] = True

                if self.shared_utils.underlay_filter_peer_as is True:
                    neighbor["route_map_out"] = f"RM-BGP-AS{link['peer_bgp_as']}-OUT"

                append_if_not_duplicate(
                    list_of_dicts=neighbors,
                    primary_key="ip_address",
                    new_dict=neighbor,
                    context="IP address defined under BGP neighbor for underlay",
                    context_keys=["ip_address", "peer_group"],
                )

                if "subinterfaces" in link:
                    for subinterface in link["subinterfaces"]:
                        neighbor = {
                            "ip_address": subinterface["peer_ip_address"],
                            "peer_group": self.shared_utils.bgp_peer_groups["ipv4_underlay_peers"]["name"],
                            "remote_as": get(link, "peer_bgp_as"),
                            "description": f"{'_'.join([link['peer'], subinterface['peer_interface']])}_vrf_{subinterface['vrf']}",
                            "bfd": get(link, "bfd"),
                        }
                        # We need to add basic BGP VRF config in case the device is not covered by network_services. (Like a spine)
                        vrfs_dict.setdefault(
                            subinterface["vrf"],
                            {
                                "name": subinterface["vrf"],
                                "router_id": self.shared_utils.router_id,
                                "neighbors": [],
                            },
                        )
                        append_if_not_duplicate(
                            list_of_dicts=vrfs_dict[subinterface["vrf"]]["neighbors"],
                            primary_key="ip_address",
                            new_dict=neighbor,
                            context="IP address defined under BGP neighbor for underlay",
                            context_keys=["ip_address", "peer_group"],
                        )

            if neighbors:
                router_bgp["neighbors"] = neighbors

        if vrfs_dict:
            router_bgp["vrfs"] = list(vrfs_dict.values())

        # Need to keep potentially empty dict for redistribute_routes
        return strip_empties_from_dict(router_bgp, strip_values_tuple=(None, ""))

    @cached_property
    def _router_bgp_redistribute_routes(self: AvdStructuredConfigUnderlay) -> list:
        """
        Return structured config for router_bgp.redistribute_routes
        """
        if self.shared_utils.overlay_routing_protocol == "none" or not self.shared_utils.underlay_filter_redistribute_connected:
            return [{"source_protocol": "connected"}]

        # TODO - RM-CONN-2-BGP could now be empty
        return [{"source_protocol": "connected", "route_map": "RM-CONN-2-BGP"}]
