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
        if self._overlay_cvx:
            return None

        router_bgp = {
            "bgp_cluster_id": self._bgp_cluster_id(),
            "peer_groups": self._peer_groups(),
            "address_family_ipv4": self._address_family_ipv4(),
            "address_family_evpn": self._address_family_evpn(),
            "address_family_rtc": self._address_family_rtc(),
            "bgp": self._bgp_overlay_dpath(),
            "address_family_vpn_ipv4": self._address_family_vpn_ipvx(4),
            "address_family_vpn_ipv6": self._address_family_vpn_ipvx(6),
            "neighbors": self._neighbors(),
        }

        # Need to keep potentially empty dict for redistribute_routes
        return strip_empties_from_dict(router_bgp, strip_values_tuple=(None, ""))

    def _bgp_cluster_id(self) -> str | None:
        if self._overlay_routing_protocol == "ibgp":
            if self._evpn_role == "server" or self._mpls_overlay_role == "server":
                return get(self._hostvars, "switch.bgp_cluster_id", default=self._router_id)
        return None

    def _generate_base_peer_group(self, pg_type: str, pg_name: str) -> dict:
        if pg_type not in ["mpls", "evpn"]:
            raise AristaAvdError("_generate_base_peer_group should be called with pg_type in ['mpls', 'evpn']")

        peer_group = {
            "type": pg_type,
            "update_source": "Loopback0",
            "bfd": True,
            "password": get(self._hostvars, f"switch.bgp_peer_groups.{pg_name}.password"),
            "send_community": "all",
            "maximum_routes": 0,
            "struct_cfg": get(self._hostvars, f"switch.bgp_peer_groups.{pg_name}.structured_config"),
        }

        return peer_group

    def _peer_groups(self) -> list | None:
        """ """
        peer_groups = []

        if self._overlay_routing_protocol == "ebgp":
            # EVPN OVERLAY peer group
            ebgp_peer_group = {
                "name": self._peer_group_evpn_overlay_peers,
                **self._generate_base_peer_group("evpn", "evpn_overlay_peers"),
                "ebgp_multihop": self._evpn_ebgp_multihop,
            }

            if self._evpn_role == "server":
                ebgp_peer_group["next_hop_unchanged"] = True

            peer_groups.append(ebgp_peer_group)

            if self._evpn_gateway_vxlan_l2 is True or self._evpn_gateway_vxlan_l3 is True:
                peer_groups.append(
                    {
                        "name": self._peer_group_evpn_overlay_core,
                        **self._generate_base_peer_group("evpn", "evpn_overlay_core"),
                        "ebgp_multihop": self._evpn_ebgp_gateway_multihop,
                    }
                )

                # peer_groups[self._peer_group_evpn_overlay_core] = self._generate_base_peer_group("evpn", "evpn_overlay_core")
                # peer_groups[self._peer_group_evpn_overlay_core]["ebgp_multihop"] = self._evpn_ebgp_gateway_multihop

        elif self._overlay_routing_protocol == "ibgp":
            if self._overlay_mpls is True:
                # MPLS OVERLAY peer group
                local_as = str(_as) if (_as := get(self._hostvars, "switch.ipvpn_gateway.local_as")) is not None else None
                mpls_peer_group = {
                    "name": self._peer_group_mpls_overlay_peers,
                    **self._generate_base_peer_group("mpls", "mpls_overlay_peers"),
                    "local_as": local_as,
                    "remote_as": self._bgp_as,
                }
                # peer_groups[self._peer_group_mpls_overlay_peers] = self._generate_base_peer_group("mpls", "mpls_overlay_peers")
                # peer_groups[self._peer_group_mpls_overlay_peers].update(
                #     {
                #         "local_as": local_as,
                #         "remote_as": self._bgp_as,
                #     }
                # )

                if self._mpls_overlay_role == "server" or (self._evpn_role == "server" and get(self._hostvars, "overlay.evpn_mpls") is True):
                    mpls_peer_group["route_reflector_client"] = True

                peer_groups.append(mpls_peer_group)

            if self._overlay_evpn_vxlan is True:
                # EVPN OVERLAY peer group - also in EBGP..
                ebgp_peer_group = {
                    "name": self._peer_group_evpn_overlay_peers,
                    **self._generate_base_peer_group("evpn", "evpn_overlay_peers"),
                    "remote_as": self._bgp_as,
                }
                # peer_groups[self._peer_group_evpn_overlay_peers] = self._generate_base_peer_group("evpn", "evpn_overlay_peers")
                # peer_groups[self._peer_group_evpn_overlay_peers]["remote_as"] = self._bgp_as
                if self._evpn_role == "server":
                    ebgp_peer_group["route_reflector_client"] = True

                peer_groups.append(ebgp_peer_group)

            if self._is_mpls_server is True:
                peer_groups.append(
                    {"name": self._peer_group_rr_overlay_peers, **self._generate_base_peer_group("mpls", "rr_overlay_peers"), "remote_as": self._bgp_as}
                )
                # peer_groups[self._peer_group_rr_overlay_peers] = self._generate_base_peer_group("mpls", "rr_overlay_peers")
                # peer_groups[self._peer_group_rr_overlay_peers]["remote_as"] = self._bgp_as

        # same for ebgp and ibgp
        if self._overlay_ipvpn_gateway is True:
            # peer_groups[self._peer_group_ipvpn_gateway_peers] = self._generate_base_peer_group("mpls", "ipvpn_gateway_peers")

            local_as = str(_as) if (_as := get(self._hostvars, "switch.ipvpn_gateway.local_as")) is not None else None
            # peer_groups[self._peer_group_ipvpn_gateway_peers]["local_as"] = local_as
            # overwriting maximum_routes
            # peer_groups[self._peer_group_ipvpn_gateway_peers]["maximum_routes"] = get(self._hostvars, "switch.ipvpn_gateway.max_routes")

            peer_groups.append(
                {
                    "name": self._peer_group_ipvpn_gateway_peers,
                    **self._generate_base_peer_group("mpls", "ipvpn_gateway_peers"),
                    "local_as": local_as,
                    "maximum_routes": get(self._hostvars, "switch.ipvpn_gateway.max_routes"),
                }
            )

        return peer_groups

    def _address_family_ipv4(self) -> list:
        """
        deactivate the relevant peer_groups in address_family_ipv4
        """
        peer_groups = []

        if self._overlay_evpn_vxlan is True:
            peer_groups.append({"name": self._peer_group_evpn_overlay_peers, "activate": False})

        if self._overlay_routing_protocol == "ebgp":
            if self._evpn_gateway_vxlan_l2 is True or self._evpn_gateway_vxlan_l3 is True:
                peer_groups.append({"name": self._peer_group_evpn_overlay_core, "activate": False})

        if self._overlay_routing_protocol == "ibgp":
            if self._overlay_mpls is True:
                peer_groups.append({"name": self._peer_group_mpls_overlay_peers, "activate": False})

            if self._is_mpls_server is True:
                peer_groups.append({"name": self._peer_group_rr_overlay_peers, "activate": False})

        if self._overlay_ipvpn_gateway is True:
            peer_groups.append({"name": self._peer_group_ipvpn_gateway_peers, "activate": False})

        return {"peer_groups": peer_groups}

    # def _address_family_evpn(self) -> dict:
    #     """ """
    #     address_family_evpn = {}
    #
    #     peer_groups = {}
    #
    #     if self._overlay_evpn_vxlan is True:
    #         overlay_peer_group_name = self._peer_group_evpn_overlay_peers
    #         peer_groups[overlay_peer_group_name] = {"activate": True}
    #
    #     if self._overlay_routing_protocol == "ebgp":
    #         if self._evpn_gateway_vxlan_l2 is True or self._evpn_gateway_vxlan_l3 is True:
    #             peer_groups[self._peer_group_evpn_overlay_core] = {
    #                 "domain_remote": True,
    #                 "activate": True,
    #             }
    #
    #         if self._evpn_gateway_vxlan_l3 is True:
    #             address_family_evpn["neighbor_default"] = {
    #                 "next_hop_self_received_evpn_routes": {
    #                     "enable": True,
    #                     "inter_domain": get(self._hostvars, "switch.evpn_gateway_vxlan_l3_inter_domain"),
    #                 }
    #             }
    #
    #     if self._overlay_routing_protocol == "ibgp":
    #         # TODO - assess this condition
    #         if self._overlay_evpn_mpls is True and self._overlay_evpn_vxlan is not True:
    #             overlay_peer_group_name = self._peer_group_mpls_overlay_peers
    #             peer_groups[overlay_peer_group_name] = {"activate": True}
    #             address_family_evpn["neighbor_default"] = {"encapsulation": "mpls"}
    #             if self._overlay_ler is True:
    #                 address_family_evpn["neighbor_default"]["next_hop_self_source_interface"] = "Loopback0"
    #
    #         if self._is_mpls_server is True:
    #             peer_groups[self._peer_group_rr_overlay_peers] = {"activate": True}
    #
    #         # partly duplicate with ebgp
    #         if self._overlay_vtep is True:
    #             peer_groups[overlay_peer_group_name].update(
    #                 {
    #                     "route_map_in": "RM-EVPN-SOO-IN",
    #                     "route_map_out": "RM-EVPN-SOO-OUT",
    #                 }
    #             )
    #
    #     address_family_evpn["peer_groups"] = peer_groups
    #
    #     # host flap detection & route pruning
    #     if self._overlay_vtep is True:
    #         if (evpn_host_flap := get(self._hostvars, "evpn_hostflap_detection")) is not None:
    #             address_family_evpn["evpn_hostflap_detection"] = {
    #                 "window": evpn_host_flap.get("window", 180),
    #                 "threshold": evpn_host_flap.get("threshold", 5),
    #                 "enabled": evpn_host_flap.get("enabled", True),
    #                 "expiry_timeout": evpn_host_flap.get("expiry_timeout"),
    #             }
    #         if get(self._hostvars, "evpn_import_pruning") is True:
    #             address_family_evpn["route"] = {
    #                 "import_match_failure_action": "discard",
    #             }
    #
    #     if self._overlay_dpath is True:
    #         address_family_evpn["domain_identifier"] = get(self._hostvars, "switch.ipvpn_gateway.evpn_domain_id",
    #                                                        required=True)
    #
    #     return address_family_evpn

    def _address_family_evpn(self) -> list:
        """ """
        address_family_evpn = {}

        peer_groups = []

        if self._overlay_evpn_vxlan is True:
            overlay_peer_group_name = self._peer_group_evpn_overlay_peers
            peer_groups.append({"name": overlay_peer_group_name, "activate": True})

        if self._overlay_routing_protocol == "ebgp":
            if self._evpn_gateway_vxlan_l2 is True or self._evpn_gateway_vxlan_l3 is True:
                peer_groups.append(
                    {
                        "name": self._peer_group_evpn_overlay_core,
                        "domain_remote": True,
                        "activate": True,
                    }
                )

            if self._evpn_gateway_vxlan_l3 is True:
                address_family_evpn["neighbor_default"] = {
                    "next_hop_self_received_evpn_routes": {
                        "enable": True,
                        "inter_domain": get(self._hostvars, "switch.evpn_gateway_vxlan_l3_inter_domain"),
                    }
                }

        if self._overlay_routing_protocol == "ibgp":
            # TODO - assess this condition
            if self._overlay_evpn_mpls is True and self._overlay_evpn_vxlan is not True:
                overlay_peer_group_name = self._peer_group_mpls_overlay_peers
                peer_groups.append({"name": overlay_peer_group_name, "activate": True})
                address_family_evpn["neighbor_default"] = {"encapsulation": "mpls"}
                if self._overlay_ler is True:
                    address_family_evpn["neighbor_default"]["next_hop_self_source_interface"] = "Loopback0"

            # partly duplicate with ebgp
            if self._overlay_vtep is True:
                for peer_group in peer_groups:
                    if peer_group["name"] == overlay_peer_group_name:
                        peer_group.update(
                            {
                                "route_map_in": "RM-EVPN-SOO-IN",
                                "route_map_out": "RM-EVPN-SOO-OUT",
                            }
                        )
                    # else:
                    #     peer_groups.append({
                    #             "name": overlay_peer_group_name,
                    #             "route_map_in": "RM-EVPN-SOO-IN",
                    #             "route_map_out": "RM-EVPN-SOO-OUT",
                    #         })

            if self._is_mpls_server is True:
                peer_groups.append({"name": self._peer_group_rr_overlay_peers, "activate": True})

        address_family_evpn["peer_groups"] = peer_groups

        # host flap detection & route pruning
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

        if self._overlay_dpath is True:
            address_family_evpn["domain_identifier"] = get(self._hostvars, "switch.ipvpn_gateway.evpn_domain_id", required=True)

        return address_family_evpn

    def _address_family_rtc(self) -> list | None:
        """
        Activate EVPN OVERLAY peer group and EVPN OVERLAY CORE peer group (if present)
        in address_family_rtc

        if the evpn_role is server, enable default_route_target only
        """
        if self._evpn_overlay_bgp_rtc is not True:
            return None

        address_family_rtc = {}

        peer_groups = []
        evpn_overlay_peers = {}
        if self._overlay_evpn_vxlan is True:
            evpn_overlay_peers = {"name": self._peer_group_evpn_overlay_peers, "activate": True}

        if self._overlay_routing_protocol == "ebgp":
            if self._evpn_gateway_vxlan_l2 is True or self._evpn_gateway_vxlan_l3 is True:
                core_peer_group = {"name": self._peer_group_evpn_overlay_core, "activate": True}
                # TODO @Claus told me to remove this
                if self._evpn_role == "server":
                    core_peer_group["default_route_target"] = {"only": True}
                peer_groups.append(core_peer_group)

            # Transposing the Jinja2 logic which is that if the selfevpn_overlay_core peer group is not
            # configured thenthe default_route_target is applied in the evpn_overlay_peers peer group.
            elif self._evpn_role == "server":
                evpn_overlay_peers.update({"name": self._peer_group_evpn_overlay_peers, "default_route_target": {"only": True}})

        if self._overlay_routing_protocol == "ibgp":
            if self._overlay_mpls is True:
                mpls_peer_group = {"name": self._peer_group_mpls_overlay_peers, "activate": True}
                if self._evpn_role == "server" or self._mpls_overlay_role == "server":
                    mpls_peer_group["default_route_target"] = {"only": True}
                peer_groups.append(mpls_peer_group)

            if self._overlay_evpn_vxlan is True:
                if self._evpn_role == "server" or self._mpls_overlay_role == "server":
                    evpn_overlay_peers.update({"name": self._peer_group_evpn_overlay_peers, "default_route_target": {"only": True}})

        peer_groups.append(evpn_overlay_peers)

        address_family_rtc["peer_groups"] = peer_groups

        return address_family_rtc

    def _address_family_vpn_ipvx(self, version: int) -> list | None:
        if version not in [4, 6]:
            raise AristaAvdError("_address_family_vpn_ipvx should be called with version 4 or 6 only")

        if (version == 4 and self._overlay_vpn_ipv4 is not True) or (version == 6 and self._overlay_vpn_ipv6 is not True):
            return None

        address_family_vpn_ipvx = {}

        if self._overlay_ler is True or self._overlay_ipvpn_gateway is True:
            address_family_vpn_ipvx["neighbor_default_encapsulation_mpls_next_hop_self"] = {"source_interface": "Loopback0"}

        peer_groups = []

        if self._overlay_ipvpn_gateway is True:
            peer_groups.append({"name": self._peer_group_ipvpn_gateway_peers, "activate": True})

        if self._overlay_routing_protocol == "ibgp":
            if self._overlay_mpls is True:
                peer_groups.append({"name": self._peer_group_mpls_overlay_peers, "activate": True})

            if self._peer_group_rr_overlay_peers is not None and self._mpls_overlay_role == "server":
                peer_groups.append({"name": self._peer_group_rr_overlay_peers, "activate": True})

        if peer_groups:
            address_family_vpn_ipvx["peer_groups"] = peer_groups

        if self._overlay_dpath is True:
            address_family_vpn_ipvx["domain_identifier"] = get(self._hostvars, "switch.ipvpn_gateway.ipvpn_domain_id", required=True)

        return address_family_vpn_ipvx

    def _create_neighbor(self, name: str, peer_group: str, remote_as: str = None) -> dict:
        """ """
        neighbor = {"peer_group": peer_group, "description": name}

        if self._overlay_routing_protocol == "ebgp":
            if remote_as is None:
                raise AristaAvdError("Configuring eBGP neighor without a remote_as")

            neighbor["remote_as"] = remote_as

        return neighbor

    def _neighbors(self) -> list | None:
        """ """
        neighbors = []

        if self._overlay_routing_protocol == "ebgp":
            for route_server, data in natural_sort(self._evpn_route_servers.items()):
                neighbor = {"ip_address": data["ip_address"]}
                neighbor.update(self._create_neighbor(route_server, self._peer_group_evpn_overlay_peers, remote_as=data["bgp_as"]))
                if self._evpn_prevent_readvertise_to_server is True:
                    neighbor["route_map_out"] = f"RM-EVPN-FILTER-AS{data['bgp_as']}"
                neighbors.append(neighbor)

            for route_client, data in natural_sort(self._evpn_route_clients.items()):
                neighbor = {"ip_address": data["ip_address"]}
                neighbor.update(self._create_neighbor(route_client, self._peer_group_evpn_overlay_peers, remote_as=data["bgp_as"]))
                neighbors.append(neighbor)

            for gw_remote_peer, data in natural_sort(self._evpn_gateway_remote_peers.items()):
                neighbor = {"ip_address": data["ip_address"]}
                neighbor.update(self._create_neighbor(gw_remote_peer, self._peer_group_evpn_overlay_core, remote_as=data["bgp_as"]))
                neighbors.append(neighbor)

        if self._overlay_routing_protocol == "ibgp":
            if self._overlay_mpls is True:
                for route_reflector, data in natural_sort(self._mpls_route_reflectors.items()):
                    neighbor = {"ip_address": data["ip_address"]}
                    neighbor.update(self._create_neighbor(route_reflector, self._peer_group_mpls_overlay_peers))
                    neighbors.append(neighbor)

                for route_client, data in natural_sort(self._mpls_route_clients.items()):
                    neighbor = {"ip_address": data["ip_address"]}
                    neighbor.update(self._create_neighbor(route_client, self._peer_group_mpls_overlay_peers))
                    neighbors.append(neighbor)

                for mesh_pe, data in natural_sort(self._mpls_mesh_pe.items()):
                    neighbor = {"ip_address": data["ip_address"]}
                    neighbor.update(self._create_neighbor(mesh_pe, self._peer_group_mpls_overlay_peers))
                    neighbors.append(neighbor)

                if self._is_mpls_server is True:
                    for rr_peer, data in natural_sort(self._mpls_rr_peers.items()):
                        neighbor = {"ip_address": data["ip_address"]}
                        neighbor.update(self._create_neighbor(rr_peer, self._peer_group_rr_overlay_peers))
                        neighbors.append(neighbor)

            if self._overlay_evpn_vxlan is True:
                for route_server, data in natural_sort(self._evpn_route_servers.items()):
                    neighbor = {"ip_address": data["ip_address"]}
                    neighbor.update(self._create_neighbor(route_server, self._peer_group_evpn_overlay_peers))
                    neighbors.append(neighbor)

                for route_client, data in natural_sort(self._evpn_route_clients.items()):
                    neighbor = {"ip_address": data["ip_address"]}
                    neighbor.update(self._create_neighbor(route_client, self._peer_group_evpn_overlay_peers))
                    neighbors.append(neighbor)

        for ipvpn_gw_peer, data in natural_sort(self._ipvpn_gateway_remote_peers.items()):
            neighbor = {"ip_address": data["ip_address"]}
            neighbor.update(self._create_neighbor(ipvpn_gw_peer, self._peer_group_ipvpn_gateway_peers, remote_as=data["bgp_as"]))
            neighbors.append(neighbor)

        if neighbors:
            return neighbors

        return None

    def _bgp_overlay_dpath(self) -> dict | None:
        if self._overlay_dpath is True:
            return {
                "bestpath": {
                    "d_path": True,
                }
            }
        return None
