from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.strip_empties import strip_empties_from_dict
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get
from ansible_collections.arista.avd.roles.eos_designs.python_modules.underlay.utils import UtilsMixin


class RouterBgpMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def router_bgp(self) -> dict | None:
        """
        Return the structured config for router_bgp
        """
        if self._underlay_bgp is not True:
            return None

        router_bgp = {}

        peer_group = {
            "type": "ipv4",
            "password": get(self._hostvars, "switch.bgp_peer_groups.ipv4_underlay_peers.password"),
            "maximum_routes": 12000,
            "send_community": "all",
            "struct_cfg": get(self._hostvars, "switch.bgp_peer_groups.ipv4_underlay_peers.structured_config"),
        }

        router_bgp["peer_groups"] = {self._peer_group_ipv4_underlay_peers_name: peer_group}

        # Address Families
        # TODO - see if it makes sense to extract logic in method
        address_family_ipv4_peer_group = {"activate": True}

        if self._underlay_rfc5549 is True:
            address_family_ipv4_peer_group["next_hop"] = {"address_family_ipv6_originate": True}

        router_bgp["address_family_ipv4"] = {
            "peer_groups": {
                self._peer_group_ipv4_underlay_peers_name: address_family_ipv4_peer_group,
            }
        }

        if self._underlay_ipv6 is True:
            router_bgp["address_family_ipv6"] = {
                "peer_groups": {
                    self._peer_group_ipv4_underlay_peers_name: {"activate": True},
                }
            }

        # Redistribute routes
        router_bgp["redistribute_routes"] = self._router_bgp_redistribute_routes

        # Neighbor Interfaces
        if self._underlay_rfc5549 is True:
            neighbor_interfaces = {}
            for link in self._underlay_links:
                if link["type"] != "underlay_p2p":
                    continue

                neighbor_interface = {
                    "peer_group": self._peer_group_ipv4_underlay_peers_name,
                    "remote_as": link["peer_bgp_as"],
                    "description": "_".join([link["peer"], link["peer_interface"]]),
                }

                if self._filter_peer_as is True:
                    self._underlay_filter_peer_as_route_maps_asns.append(link["peer_bgp_as"])

                neighbor_interfaces[link["interface"]] = neighbor_interface

            if neighbor_interfaces:
                router_bgp["neighbor_interfaces"] = neighbor_interfaces

        # Neighbors
        else:
            neighbors = {}
            for link in self._underlay_links:
                if link["type"] != "underlay_p2p":
                    continue

                neighbor = {
                    "peer_group": self._peer_group_ipv4_underlay_peers_name,
                    "remote_as": get(link, "peer_bgp_as"),
                    "description": "_".join([link["peer"], link["peer_interface"]]),
                    "bfd": get(link, "bfd"),
                }

                if self._filter_peer_as is True:
                    neighbor["route_map_out"] = f"RM-BGP-AS{link['peer_bgp_as']}-OUT"

                neighbors[link["peer_ip_address"]] = neighbor

            if neighbors:
                router_bgp["neighbors"] = neighbors

        # Need to keep potentially empty dict for redistribute_routes
        return strip_empties_from_dict(router_bgp, strip_values_tuple=(None, ""))

    @cached_property
    def _router_bgp_redistribute_routes(self) -> dict | None:
        """
        Return structured config for router_bgp.redistribute_routes
        """
        if self._overlay_routing_protocol == "none":
            return {"connected": {}}

        return {"connected": {"route_map": "RM-CONN-2-BGP"}}
