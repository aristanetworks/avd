from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError
from ansible_collections.arista.avd.plugins.plugin_utils.strip_empties import strip_empties_from_dict
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get, get_item
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
        if self.shared_utils.underlay_bgp is not True:
            return None

        router_bgp = {}

        peer_group = {
            "name": self.shared_utils.bgp_peer_groups["ipv4_underlay_peers"]["name"],
            "type": "ipv4",
            "password": self.shared_utils.bgp_peer_groups["ipv4_underlay_peers"]["password"],
            "maximum_routes": 12000,
            "send_community": "all",
            "struct_cfg": self.shared_utils.bgp_peer_groups["ipv4_underlay_peers"]["structured_config"],
        }

        router_bgp["peer_groups"] = [peer_group]

        # Address Families
        # TODO - see if it makes sense to extract logic in method
        address_family_ipv4_peer_group = {"activate": True}

        if self.shared_utils.underlay_rfc5549 is True:
            address_family_ipv4_peer_group["next_hop"] = {"address_family_ipv6_originate": True}

        router_bgp["address_family_ipv4"] = {
            "peer_groups": [{"name": self.shared_utils.bgp_peer_groups["ipv4_underlay_peers"]["name"], **address_family_ipv4_peer_group}]
        }

        if self.shared_utils.underlay_ipv6 is True:
            router_bgp["address_family_ipv6"] = {"peer_groups": [{"name": self.shared_utils.bgp_peer_groups["ipv4_underlay_peers"]["name"], "activate": True}]}

        # Redistribute routes
        router_bgp["redistribute_routes"] = self._router_bgp_redistribute_routes

        # Neighbor Interfaces
        if self.shared_utils.underlay_rfc5549 is True:
            neighbor_interfaces = []
            for link in self._underlay_links:
                if link["type"] != "underlay_p2p":
                    continue

                neighbor_interface = {
                    "name": link["interface"],
                    "peer_group": self.shared_utils.bgp_peer_groups["ipv4_underlay_peers"]["name"],
                    "remote_as": link["peer_bgp_as"],
                    "description": "_".join([link["peer"], link["peer_interface"]]),
                }

                if self.shared_utils.underlay_filter_peer_as is True:
                    self._underlay_filter_peer_as_route_maps_asns.append(link["peer_bgp_as"])

                neighbor_interfaces.append(neighbor_interface)

            if neighbor_interfaces:
                router_bgp["neighbor_interfaces"] = neighbor_interfaces

        # Neighbors
        else:
            neighbors = []
            for link in self._underlay_links:
                if link["type"] != "underlay_p2p":
                    continue

                neighbor = {
                    "ip_address": link["peer_ip_address"],
                    "peer_group": self.shared_utils.bgp_peer_groups["ipv4_underlay_peers"]["name"],
                    "remote_as": get(link, "peer_bgp_as"),
                    "description": "_".join([link["peer"], link["peer_interface"]]),
                    "bfd": get(link, "bfd"),
                }

                if self.shared_utils.underlay_filter_peer_as is True:
                    neighbor["route_map_out"] = f"RM-BGP-AS{link['peer_bgp_as']}-OUT"

                if (found_neighbor := get_item(neighbors, "ip_address", link["peer_ip_address"])) is None:
                    neighbors.append(neighbor)
                else:
                    if found_neighbor == neighbor:
                        # Same neighbor information twice in the input data. So not duplicate IPs.
                        continue

                    raise AristaAvdError(
                        f"Duplicate ip_address {link['peer_ip_address']} found while generating BGP neighbor configuration for {link['peer']},"
                        f" {link['peer_interface']}. Duplicate IP of {found_neighbor['description']}"
                    )

            if neighbors:
                router_bgp["neighbors"] = neighbors

        # Need to keep potentially empty dict for redistribute_routes
        return strip_empties_from_dict(router_bgp, strip_values_tuple=(None, ""))

    @cached_property
    def _router_bgp_redistribute_routes(self) -> list:
        """
        Return structured config for router_bgp.redistribute_routes
        """
        if self.shared_utils.overlay_routing_protocol == "none" or not self.shared_utils.underlay_filter_redistribute_connected:
            return [{"source_protocol": "connected"}]

        return [{"source_protocol": "connected", "route_map": "RM-CONN-2-BGP"}]
