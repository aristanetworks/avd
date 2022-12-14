from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.filter.natural_sort import natural_sort
from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError
from ansible_collections.arista.avd.plugins.plugin_utils.strip_empties import strip_empties_from_dict
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get

from .utils import UtilsMixin


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
        if self._overlay_mpls is True:
            # some logic
            pass
        if self._overlay_evpn is True:
            # some logic
            pass

        router_bgp = {}

        if self._overlay_routing_protocol == "ebgp":
            # peer_groups
            router_bgp["peer_groups"] = self._ebgp_peer_groups()

            # address_family_ipv4
            router_bgp["address_family_ipv4"] = self._ebgp_address_family_ipv4()

            # address_family_evpn
            router_bgp["address_family_evpn"] = self._ebgp_address_family_evpn()

            # address_family_rtc
            router_bgp["address_family_rtc"] = self._ebgp_address_family_rtc()

            # neighbors
            router_bgp["neighbors"] = self._ebgp_neighbors()

        elif self._overlay_routing_protocol == "ibgp":
            if self._evpn_role == "server" or self._mpls_overlay_role == "server":
                router_bgp["bgp_cluster_id"] = get(self._hostvars, "switch.bgp_cluster_id", default=self._router_id)

            # peer_groups
            router_bgp["peer_groups"] = self._ibgp_peer_groups()

            # address_family_ipv4
            router_bgp["address_family_ipv4"] = self._ibgp_address_family_ipv4()

            if self._overlay_evpn is True:
                # address_family_evpn
                router_bgp["address_family_evpn"] = self._ibgp_address_family_evpn()

            # address_family_rtc
            router_bgp["address_family_rtc"] = self._ibgp_address_family_rtc()

            # address_family_vpn_ipv4
            router_bgp["address_family_vpn_ipv4"] = self._ibgp_address_family_vpn_ipv4()

            # address_family_vpn_ipv6
            router_bgp["address_family_vpn_ipv6"] = self._ibgp_address_family_vpn_ipv6()

            # neighbors
            router_bgp["neighbors"] = self._ibgp_neighbors()

        # Need to keep potentially empty dict for redistribute_routes
        return strip_empties_from_dict(router_bgp, strip_values_tuple=(None, ""))

    def _ebgp_peer_groups(self) -> dict | None:
        """ """
        peer_groups = {}

        # EVPN OVERLAY peer group
        # TODO - for now Loopback0 is hardcoded as per original template
        peer_groups[self._peer_group_evpn_overlay_peers] = {
            "type": "evpn",
            "update_source": "Loopback0",
            "bfd": True,
            "ebgp_multihop": self._evpn_ebgp_multihop,
            "password": get(self._hostvars, "switch.bgp_peer_groups.evpn_overlay_peers.password"),
            "send_community": "all",
            "maximum_routes": 0,
            "struct_cfg": get(self._hostvars, "switch.bgp_peer_groups.evpn_overlay_peers.structured_config"),
        }

        if self._evpn_role == "server":
            peer_groups[self._peer_group_evpn_overlay_peers]["next_hop_unchanged"] = True

        if self._evpn_gateway_vxlan_l2 is True or self._evpn_gateway_vxlan_l3 is True:
            peer_groups[self._peer_group_evpn_overlay_core] = {
                "type": "evpn",
                "update_source": "Loopback0",
                "bfd": True,
                "ebgp_multihop": self._evpn_ebgp_gateway_multihop,
                "password": get(self._hostvars, "switch.bgp_peer_groups.evpn_overlay_core.password"),
                "send_community": "all",
                "maximum_routes": 0,
                "struct_cfg": get(self._hostvars, "switch.bgp_peer_groups.evpn_overlay_core.structured_config"),
            }

        return peer_groups

    def _ebgp_address_family_ipv4(self) -> dict:
        """
        deactivate the relevant peer_groups in address_family_ipv4
        """
        peer_groups = {}

        if self._peer_group_evpn_overlay_peers is not None:
            peer_groups[self._peer_group_evpn_overlay_peers] = {"activate": False}

        if self._evpn_gateway_vxlan_l2 is True or self._evpn_gateway_vxlan_l3 is True:
            peer_groups[self._peer_group_evpn_overlay_core] = {"activate": False}

        return {"peer_groups": peer_groups}

    def _ebgp_address_family_evpn(self) -> dict:
        """ """
        address_family_evpn = {}

        peer_groups = {self._peer_group_evpn_overlay_peers: {"activate": True}}

        if self._evpn_gateway_vxlan_l2 is True or self._evpn_gateway_vxlan_l3 is True:
            peer_groups[self._peer_group_evpn_overlay_core] = {
                "domain_remote": True,
                "activate": True,
            }

        address_family_evpn["peer_groups"] = peer_groups

        if self._evpn_gateway_vxlan_l3 is True:
            address_family_evpn["neighbor_default"] = {
                "next_hop_self_received_evpn_routes": {
                    "enable": True,
                    "inter_domain": get(self._hostvars, "switch.evpn_gateway_vxlan_l3_inter_domain"),
                }
            }

        if self._overlay_vtep is True:
            if (evpn_host_flap := get(self._hostvars, "evpn_hostflap_detection")) is not None:
                address_family_evpn["evpn_hostflap_detection"] = {
                    "window": evpn_host_flap.get("window", 180),
                    "threshold": evpn_host_flap.get("threshold", 5),
                    "enabled": evpn_host_flap.get("enabled", True),
                    "expiry_timeout": evpn_host_flap.get("expiry_timeout"),
                }
            if get(self._hostvars, "evpn_import_pruning") is True:
                address_family_evpn["route"] = {
                    "import_match_failure_action": "discard",
                }

        return address_family_evpn

    def _ebgp_address_family_rtc(self) -> dict | None:
        """
        Activate EVPN OVERLAY peer group and EVPN OVERLAY CORE peer group (if present)
        in address_family_rtc

        if the evpn_role is server, enable default_route_target only
        """
        if self._evpn_overlay_bgp_rtc is not True:
            return None

        address_family_rtc = {}

        peer_groups = {self._peer_group_evpn_overlay_peers: {"activate": True}}

        if self._evpn_gateway_vxlan_l2 is True or self._evpn_gateway_vxlan_l3 is True:
            peer_groups[self._peer_group_evpn_overlay_core] = {"activate": True}
            if self._evpn_role == "server":
                peer_groups[self._peer_group_evpn_overlay_core]["default_route_target"] = {"only": True}

        # Transposing the Jinja2 logic which is that if the selfevpn_overlay_core peer group is not
        # configured thenthe default_route_target is applied in the evpn_overlay_peers peer group.
        elif self._evpn_role == "server":
            peer_groups[self._peer_group_evpn_overlay_peers]["default_route_target"] = {"only": True}

        address_family_rtc["peer_groups"] = peer_groups

        return address_family_rtc

    def _ebgp_neighbors(self) -> dict | None:
        """ """
        neighbors = {}

        for route_server in natural_sort(self._evpn_route_servers):
            neighbor = {
                "peer_group": self._peer_group_evpn_overlay_peers,
                "description": route_server,
                "remote_as": self._evpn_route_servers[route_server]["bgp_as"],
            }

            if self._evpn_prevent_readvertise_to_server is True:
                neighbor["route_map_out"] = f"RM-EVPN-FILTER-AS{self._evpn_route_servers[route_server]['bgp_as']}"

            neighbors[self._evpn_route_servers[route_server]["ip_address"]] = neighbor

        for route_client in natural_sort(self._evpn_route_clients):
            neighbors[self._evpn_route_clients[route_client]["ip_address"]] = {
                "peer_group": self._peer_group_evpn_overlay_peers,
                "description": route_client,
                "remote_as": self._evpn_route_clients[route_client]["bgp_as"],
            }

        for gw_remote_peers in natural_sort(self._evpn_gateway_remote_peers):
            neighbors[self._evpn_gateway_remote_peers[gw_remote_peers]["ip_address"]] = {
                "peer_group": self._peer_group_evpn_overlay_core,
                "description": gw_remote_peers,
                "remote_as": self._evpn_gateway_remote_peers[gw_remote_peers]["bgp_as"],
            }

        if neighbors:
            return neighbors

        return None

    def _ibgp_peer_groups(self) -> dict:
        """ """
        peer_groups = {}

        # TODO adapt logic from latest PR
        if self._overlay_mpls is True:
            # MPLS OVERLAY peer group
            # TODO - for now Loopback0 is hardcoded as per original template
            peer_groups[self._peer_group_mpls_overlay_peers] = {
                "type": "mpls",
                "update_source": "Loopback0",
                "remote_as": self._bgp_as,
                "bfd": True,
                "password": get(self._hostvars, "switch.bgp_peer_groups.mpls_overlay_peers.password"),
                "send_community": "all",
                "maximum_routes": 0,
                "struct_cfg": get(self._hostvars, "switch.bgp_peer_groups.mpls_overlay_peers.structured_config"),
            }

            if self._mpls_overlay_role == "server" or (self._evpn_role == "server" and get(self._hostvars, "overlay.evpn_mpls") is True):
                peer_groups[self._peer_group_mpls_overlay_peers]["route_reflector_client"] = True

        # TODO - think if this can be grouped with ebgp_peer_group
        if self._overlay_evpn_vxlan is True:
            # EVPN OVERLAY peer group
            # TODO - for now Loopback0 is hardcoded as per original template
            peer_groups[self._peer_group_evpn_overlay_peers] = {
                "type": "evpn",
                "update_source": "Loopback0",
                "remote_as": self._bgp_as,
                "bfd": True,
                "password": get(self._hostvars, "switch.bgp_peer_groups.evpn_overlay_peers.password"),
                "send_community": "all",
                "maximum_routes": 0,
                "struct_cfg": get(self._hostvars, "switch.bgp_peer_groups.evpn_overlay_peers.structured_config"),
            }

            if self._evpn_role == "server":
                peer_groups[self._peer_group_evpn_overlay_peers]["route_reflector_client"] = True

        if self._mpls_overlay_role == "server" or (self._evpn_role == "server" and get(self._hostvars, "switch.overlay.evpn_mpls") is True):
            peer_groups[self._peer_group_rr_overlay_peers] = {
                "type": "mpls",
                "update_source": "Loopback0",
                "remote_as": self._bgp_as,
                "bfd": True,
                "password": get(self._hostvars, "switch.bgp_peer_groups.rr_overlay_peers.password"),
                "send_community": "all",
                "maximum_routes": 0,
                "struct_cfg": get(self._hostvars, "switch.bgp_peer_groups.rr_overlay_peers.structured_config"),
            }

        return peer_groups

    def _ibgp_address_family_ipv4(self) -> dict:
        """
        deactivate the relevant peer_groups in address_family_ipv4
        """
        peer_groups = {}

        if self._overlay_mpls is True:
            peer_groups[self._peer_group_mpls_overlay_peers] = {"activate": False}

        if self._overlay_evpn_vxlan is True:
            peer_groups[self._peer_group_evpn_overlay_peers] = {"activate": False}

        if self._mpls_overlay_role == "server" or (self._evpn_role == "server" and get(self._hostvars, "overlay.evpn_mpls") is True):
            peer_groups[self._peer_group_rr_overlay_peers] = {"activate": False}

        return {"peer_groups": peer_groups}

    def _ibgp_address_family_evpn(self) -> dict:
        """ """
        address_family_evpn = {}

        peer_groups = {}

        if self._overlay_evpn_vxlan is True:
            overlay_peer_group_name = self._peer_group_evpn_overlay_peers
        elif self._overlay_mpls is True:
            overlay_peer_group_name = self._peer_group_mpls_overlay_peers
            address_family_evpn["neighbor_default"] = {"encapsulation": "mpls"}
            if get(self._hostvars, "switch.overlay.ler") is True:
                address_family_evpn["neighbor_default"]["next_hop_self_source_interface"] = "Loopback0"
        else:
            raise AristaAvdError("No name for overlay_peer_group")

        peer_groups[overlay_peer_group_name] = {"activate": True}

        if self._mpls_overlay_role == "server" or (self._evpn_role == "server" and get(self._hostvars, "overlay.evpn_mpls") is True):
            peer_groups[self._peer_group_rr_overlay_peers] = {"activate": True}

        address_family_evpn["peer_groups"] = peer_groups

        # partly duplicate with ebgp
        if self._overlay_vtep is True:
            peer_groups[overlay_peer_group_name].update(
                {
                    "route_map_in": "RM-EVPN-SOO-IN",
                    "route_map_out": "RM-EVPN-SOO-OUT",
                }
            )

            if (evpn_host_flap := get(self._hostvars, "evpn_hostflap_detection")) is not None:
                address_family_evpn["evpn_hostflap_detection"] = {
                    "window": evpn_host_flap.get("window", default=180),
                    "threshold": evpn_host_flap.get("threshold", default=5),
                    "enabled": evpn_host_flap.get("enabled", default=True),
                    "expiry_timeout": evpn_host_flap.get("expiry_timeout"),
                }
            if get(self._hostvars, "evpn_import_pruning") is True:
                address_family_evpn["route"] = {
                    "import_match_failure_action": "discard",
                }

        return address_family_evpn

    def _ibgp_address_family_rtc(self) -> dict | None:
        """
        TODO - refactor leaner
        """
        if self._evpn_overlay_bgp_rtc is not True:
            return None

        peer_groups = {}
        if self._overlay_mpls is True:
            peer_groups[self._peer_group_mpls_overlay_peers] = {"activate": True}
            if self._evpn_role == "server" or self._mpls_overlay_role == "server":
                peer_groups[self._peer_group_mpls_overlay_peers]["default_route_target"] = {"only": True}

        if self._overlay_evpn_vxlan is True:
            peer_groups[self._peer_group_evpn_overlay_peers] = {"activate": True}
            if self._evpn_role == "server" or self._mpls_overlay_role == "server":
                peer_groups[self._peer_group_evpn_overlay_peers]["default_route_target"] = {"only": True}

        return {"peer_groups": peer_groups}

    def _ibgp_address_family_vpn_ipv4(self) -> dict | None:
        if self._overlay_vpn_ipv4 is not True:
            return None

        address_family_vpn_ipv4 = {}
        if self._overlay_ler is True:
            address_family_vpn_ipv4["neighbor_default_encapsulation_mpls_next_hop_self"] = {"source_interface": "Loopback0"}

        peer_groups = {}
        peer_groups[self._peer_group_mpls_overlay_peers] = {"activate": True}

        if self._peer_group_rr_overlay_peers is not None and self._mpls_overlay_role == "server":
            peer_groups[self._peer_group_rr_overlay_peers] = {"activate": True}

        address_family_vpn_ipv4["peer_groups"] = peer_groups

        return address_family_vpn_ipv4

    def _ibgp_address_family_vpn_ipv6(self) -> dict | None:
        # TODO - refactor as it is exactly the same as vpn_ipv4
        if self._overlay_vpn_ipv6 is not True:
            return None

        address_family_vpn_ipv6 = {}
        if self._overlay_ler is True:
            address_family_vpn_ipv6["neighbor_default_encapsulation_mpls_next_hop_self"] = {"source_interface": "Loopback0"}

        peer_groups = {}
        peer_groups[self._peer_group_mpls_overlay_peers] = {"activate": True}

        if self._peer_group_rr_overlay_peers is not None and self._mpls_overlay_role == "server":
            peer_groups[self._peer_group_rr_overlay_peers] = {"activate": True}

        address_family_vpn_ipv6["peer_groups"] = peer_groups

        return address_family_vpn_ipv6

    def _ibgp_neighbors(self) -> dict | None:
        """ """
        neighbors = {}

        if self._overlay_mpls is True:
            for route_reflector in natural_sort(self._mpls_route_reflectors):
                neighbors[self._mpls_route_reflectors[route_reflector]["ip_address"]] = {
                    "peer_group": self._peer_group_mpls_overlay_peers,
                    "description": route_reflector,
                }

            for route_client in natural_sort(self._mpls_route_clients):
                neighbors[self._mpls_route_clients[route_client]["ip_address"]] = {
                    "peer_group": self._peer_group_mpls_overlay_peers,
                    "description": route_client,
                }

            for mesh_pe in natural_sort(self._mpls_mesh_pe):
                neighbors[self._mpls_mesh_pe[mesh_pe]["ip_address"]] = {
                    "peer_group": self._peer_group_mpls_overlay_peers,
                    "description": mesh_pe,
                }

            # TODO this check comes often - maybe cache it
            if self._mpls_overlay_role == "server" or (self._evpn_role == "server" and get(self._hostvars, "overlay.evpn_mpls") is True):
                for rr_peers in natural_sort(self._mpls_rr_peers):
                    neighbors[self._mpls_rr_peers[rr_peers]["ip_address"]] = {
                        "peer_group": self._peer_group_rr_overlay_peers,
                        "description": rr_peers,
                    }

        if self._overlay_evpn_vxlan is True:
            for route_server in natural_sort(self._evpn_route_servers):
                neighbors[self._evpn_route_servers[route_server]["ip_address"]] = {
                    "peer_group": self._peer_group_evpn_overlay_peers,
                    "description": route_server,
                }

            for route_client in natural_sort(self._evpn_route_clients):
                neighbors[self._evpn_route_clients[route_client]["ip_address"]] = {
                    "peer_group": self._peer_group_evpn_overlay_peers,
                    "description": route_client,
                }

        if neighbors:
            return neighbors

        return None
