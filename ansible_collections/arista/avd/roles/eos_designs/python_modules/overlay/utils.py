# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.filter.natural_sort import natural_sort
from ansible_collections.arista.avd.plugins.plugin_utils.eos_designs_shared_utils.shared_utils import SharedUtils
from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError, AristaAvdMissingVariableError
from ansible_collections.arista.avd.plugins.plugin_utils.strip_empties import strip_empties_from_dict
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get, get_item


class UtilsMixin:
    """
    Mixin Class with internal functions.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    # Set type hints for Attributes of the main class as needed
    _hostvars: dict
    shared_utils: SharedUtils

    @cached_property
    def _avd_overlay_peers(self) -> list:
        """
        Returns a list of overlay peers for the device

        This cannot be loaded in shared_utils since it will not be calculated until EosDesignsFacts has been rendered
        and shared_utils are shared between EosDesignsFacts and AvdStructuredConfig classes like this one.
        """
        return get(self._hostvars, f"avd_overlay_peers..{self.shared_utils.hostname}", separator="..", default=[])

    @cached_property
    def _evpn_gateway_remote_peers(self) -> dict:
        if not self.shared_utils.overlay_evpn:
            return {}

        evpn_gateway_remote_peers = {}

        evpn_gateway_remote_peers_list = get(self.shared_utils.switch_data_combined, "evpn_gateway.remote_peers", default=[])

        for gw_remote_peer_dict in natural_sort(evpn_gateway_remote_peers_list, sort_key="hostname"):
            # These remote gw can be outside of the inventory
            gw_remote_peer = gw_remote_peer_dict["hostname"]
            peer_facts = self.shared_utils.get_peer_facts(gw_remote_peer, required=False)

            if peer_facts is not None:
                # Found a matching server in inventory
                self._append_peer(evpn_gateway_remote_peers, gw_remote_peer, peer_facts)

            else:
                # Server not found in inventory, adding manually
                # TODO - what if the values are None - this is not handled by the template today
                bgp_as = str(_as) if (_as := gw_remote_peer_dict.get("bgp_as")) else None
                ip_address = gw_remote_peer_dict.get("ip_address")

                evpn_gateway_remote_peers[gw_remote_peer] = {
                    "bgp_as": bgp_as,
                    "ip_address": ip_address,
                }

        return evpn_gateway_remote_peers

    @cached_property
    def _evpn_route_clients(self) -> dict:
        if not self.shared_utils.overlay_evpn:
            return {}

        if self.shared_utils.evpn_role != "server":
            return {}

        evpn_route_clients = {}

        for avd_peer in self._avd_overlay_peers:
            peer_facts = self.shared_utils.get_peer_facts(avd_peer, required=True)
            if (
                self.shared_utils.hostname in peer_facts.get("evpn_route_servers", [])
                and peer_facts.get("evpn_role") in ["server", "client"]
                and avd_peer not in self._evpn_route_servers.keys()
            ):
                self._append_peer(evpn_route_clients, avd_peer, peer_facts)

        return evpn_route_clients

    @cached_property
    def _evpn_route_servers(self) -> dict:
        if not self.shared_utils.overlay_evpn:
            return {}

        evpn_route_servers = {}

        for route_server in natural_sort(get(self._hostvars, "switch.evpn_route_servers", default=[])):
            peer_facts = self.shared_utils.get_peer_facts(route_server, required=True)
            if peer_facts.get("evpn_role") != "server":
                continue

            self._append_peer(evpn_route_servers, route_server, peer_facts)

        return evpn_route_servers

    # The next four should probably be moved to facts
    @cached_property
    def _is_mpls_client(self) -> bool:
        return self.shared_utils.mpls_overlay_role == "client" or (self.shared_utils.evpn_role == "client" and self.shared_utils.overlay_evpn_mpls)

    @cached_property
    def _is_mpls_server(self) -> bool:
        return self.shared_utils.mpls_overlay_role == "server" or (self.shared_utils.evpn_role == "server" and self.shared_utils.overlay_evpn_mpls)

    def _is_peer_mpls_client(self, peer_facts: dict) -> bool:
        return peer_facts.get("mpls_overlay_role", None) == "client" or (
            peer_facts.get("evpn_role", None) == "client" and get(peer_facts, "overlay.evpn_mpls") is True
        )

    def _is_peer_mpls_server(self, peer_facts: dict) -> bool:
        return peer_facts.get("mpls_overlay_role", None) == "server" or (
            peer_facts.get("evpn_role", None) == "server" and get(peer_facts, "overlay.evpn_mpls") is True
        )

    @cached_property
    def _ipvpn_gateway_local_as(self) -> str | None:
        return str(_as) if (_as := get(self.shared_utils.switch_data_combined, "ipvpn_gateway.local_as")) is not None else None

    @cached_property
    def _ipvpn_gateway_remote_peers(self) -> dict:
        if self.shared_utils.overlay_ipvpn_gateway is not True:
            return {}

        ipvpn_gateway_remote_peers = {}

        for ipvpn_gw_peer_dict in natural_sort(
            get(
                self.shared_utils.switch_data_combined,
                "ipvpn_gateway.remote_peers",
                default=[],
            ),
            "hostname",
        ):
            # These remote gw are outside of the inventory

            bgp_as = ipvpn_gw_peer_dict["bgp_as"]

            ipvpn_gateway_remote_peers[ipvpn_gw_peer_dict["hostname"]] = {
                "bgp_as": str(bgp_as) if bgp_as is not None else None,
                "ip_address": ipvpn_gw_peer_dict["ip_address"],
            }

        return ipvpn_gateway_remote_peers

    @cached_property
    def _mpls_route_clients(self) -> dict:
        if self._is_mpls_server is not True:
            return {}

        mpls_route_clients = {}

        for avd_peer in self._avd_overlay_peers:
            peer_facts = self.shared_utils.get_peer_facts(avd_peer, required=True)
            if self._is_peer_mpls_client(peer_facts) is not True:
                continue

            if self.shared_utils.hostname in peer_facts.get("mpls_route_reflectors", []) and avd_peer not in self._mpls_route_reflectors.keys():
                self._append_peer(mpls_route_clients, avd_peer, peer_facts)

        return mpls_route_clients

    @cached_property
    def _mpls_mesh_pe(self) -> dict:
        if self.shared_utils.overlay_mpls is not True:
            return {}

        if get(self._hostvars, "bgp_mesh_pes") is not True:
            return {}

        mpls_mesh_pe = {}

        for fabric_switch in self.shared_utils.all_fabric_devices:
            if self._mpls_route_reflectors is not None and fabric_switch in self._mpls_route_reflectors:
                continue
            if fabric_switch == self.shared_utils.hostname:
                continue

            peer_facts = self.shared_utils.get_peer_facts(fabric_switch, required=True)
            if self._is_peer_mpls_client(peer_facts) is not True:
                continue

            self._append_peer(mpls_mesh_pe, fabric_switch, peer_facts)

        return mpls_mesh_pe

    @cached_property
    def _mpls_route_reflectors(self) -> dict:
        if self._is_mpls_client is not True:
            return {}

        mpls_route_reflectors = {}

        for route_reflector in natural_sort(get(self._hostvars, "switch.mpls_route_reflectors", default=[])):
            if route_reflector == self.shared_utils.hostname:
                continue

            peer_facts = self.shared_utils.get_peer_facts(route_reflector, required=True)
            if self._is_peer_mpls_server(peer_facts) is not True:
                continue

            self._append_peer(mpls_route_reflectors, route_reflector, peer_facts)

        return mpls_route_reflectors

    @cached_property
    def _mpls_rr_peers(self) -> dict:
        if self._is_mpls_server is not True:
            return {}

        mpls_rr_peers = {}

        for route_reflector in natural_sort(get(self._hostvars, "switch.mpls_route_reflectors", default=[])):
            if route_reflector == self.shared_utils.hostname:
                continue

            peer_facts = self.shared_utils.get_peer_facts(route_reflector, required=True)
            if self._is_peer_mpls_server(peer_facts) is not True:
                continue

            self._append_peer(mpls_rr_peers, route_reflector, peer_facts)

        for avd_peer in self._avd_overlay_peers:
            peer_facts = self.shared_utils.get_peer_facts(avd_peer, required=True)
            if self._is_peer_mpls_server(peer_facts) is not True:
                continue

            if self.shared_utils.hostname in peer_facts.get("mpls_route_reflectors", []) and avd_peer not in get(
                self._hostvars, "switch.mpls_route_reflectors", default=[]
            ):
                self._append_peer(mpls_rr_peers, avd_peer, peer_facts)

        return mpls_rr_peers

    def _append_peer(self, peers_dict: dict, peer_name: str, peer_facts: dict) -> None:
        """
        Retieve bgp_as and "overlay.peering_address" from peer_facts and append
        a new peer to peers_dict
        {
            peer_name: {
                "bgp_as": bgp_as,
                "ip_address": overlay.peering_address,
            }
        }
        """
        bgp_as = peer_facts.get("bgp_as")
        peers_dict[peer_name] = {
            "bgp_as": str(bgp_as) if bgp_as is not None else None,
            "ip_address": get(
                peer_facts,
                "overlay.peering_address",
                required=True,
                org_key=f"switch.overlay.peering_address for {peer_name}",
            ),
        }

    @cached_property
    def _is_wan_server_with_peers(self) -> bool:
        return self.shared_utils.wan_role == "server" and len(self._filtered_wan_route_servers) > 0

    @cached_property
    def _wan_listen_ranges(self):
        return get(self.shared_utils.bgp_peer_groups["wan_overlay_peers"], "listen_range_prefixes", required=True)

    @cached_property
    def _wan_site(self) -> dict | None:
        """
        Here assuming that cv_pathfinder_name is unique across zones and regions
        """
        if not self.shared_utils.cv_pathfinder_role:
            return None

        node_defined_site = get(
            self.shared_utils.switch_data_combined,
            "cv_pathfinder_site",
            required=True,
            org_key="A node variable 'cv_pathfinder_site' must be defined when 'cv_pathfinder_role' is 'edge' or 'transit'.",
        )
        sites = get(self._wan_region, "sites", required=True, org_key=f"The CV Pathfinder region '{self._wan_region['name']}' is missing a list of sites")
        return get_item(
            sites,
            "name",
            node_defined_site,
            required=True,
            custom_error_msg=(
                f"The 'cv_pathfinder_site '{node_defined_site}' defined at the node level could not be found under the 'sites' list for the region"
                f" '{self._wan_region['name']}'."
            ),
        )

    @cached_property
    def _wan_region(self) -> dict | None:
        """
        WAN region for Pathfinder
        """
        if not self.shared_utils.cv_pathfinder_role:
            return None

        node_defined_region = get(
            self.shared_utils.switch_data_combined,
            "cv_pathfinder_region",
            required=True,
            org_key="A node variable 'cv_pathfinder_region' must be defined when 'cv_pathfinder_role' is 'edge' or 'transit'.",
        )
        regions = get(
            self._hostvars, "cv_pathfinder_regions", required=True, org_key="'cv_pathfinder_regions' key must be set when 'wan_mode' is 'cv-pathfinder'."
        )

        return get_item(
            regions,
            "name",
            node_defined_region,
            required=True,
            custom_error_msg="The 'cv_pathfinder_region' defined at the node level could not be found under the 'cv_pathfinder_regions' key.",
        )

    @cached_property
    def _wan_zone(self) -> dict | None:
        """
        WAN zone for Pathfinder

        Currently, only default zone DEFAULT-ZONE with ID 1 is supported.
        """
        if not self.shared_utils.cv_pathfinder_role:
            return None

        # Injecting zone DEFAULT-ZONE with id 1.
        return {"name": "DEFAULT-ZONE", "id": 1}

    @cached_property
    def _wan_route_servers(self) -> dict:
        """
        Return a dict keyed by Wan RR based on the the wan_mode type.

        It the RR is part of the inventory, the peer_facts are read..
        If any key is specified in the variables, it overwrites whatever is in the peer_facts.

        If no peer_fact is found the variables are required in the inventory.
        """
        # TODO - need to factor this with other function once we fix
        # https://github.com/aristanetworks/ansible-avd/issues/3392
        if not self.shared_utils.wan_mode:
            return {}

        wan_route_servers = {}

        wan_route_servers_list = get(self._hostvars, "wan_route_servers", default=[])

        for wan_rs_dict in natural_sort(wan_route_servers_list, sort_key="hostname"):
            # These remote gw can be outside of the inventory
            wan_rs = wan_rs_dict["hostname"]

            if wan_rs == self.shared_utils.hostname:
                # Don't add yourself
                continue

            if (peer_facts := self.shared_utils.get_peer_facts(wan_rs, required=False)) is not None:
                # Found a matching server in inventory
                bgp_as = peer_facts.get("bgp_as")
                # Only ibgp is supported for WAN so raise if peer from peer_facts BGP AS is different from ours.
                if bgp_as != self.shared_utils.bgp_as:
                    raise AristaAvdError(
                        f"Only iBGP is supported for WAN, the BGP AS {bgp_as} on {wan_rs} is different from our own: {self.shared_utils.bgp_as}."
                    )

                # Prefer values coming from the input variables over peer facts
                router_id = get(wan_rs_dict, "router_id", default=peer_facts.get("router_id"))
                wan_path_groups = get(wan_rs_dict, "path_groups", default=peer_facts.get("wan_path_groups"))

                if router_id is None:
                    raise AristaAvdMissingVariableError(
                        f"'router_id' is missing for peering with {wan_rs}, either set it in under 'wan_route_servers' or something is wrong with the peer"
                        " facts."
                    )
                if wan_path_groups is None:
                    raise AristaAvdMissingVariableError(
                        f"'wan_path_groups' is missing for peering with {wan_rs}, either set it in under 'wan_route_servers'"
                        " or something is wrong with the peer facts."
                    )

            else:
                # Retrieve the values from the dictionary, making them required if the peer_facts were not found
                router_id = get(wan_rs_dict, "router_id", required=True)
                wan_path_groups = get(
                    wan_rs_dict,
                    "path_groups",
                    required=True,
                    org_key=(
                        f"'path_groups' is missing for peering with {wan_rs} which was not found in the inventory, either set it in under 'wan_route_servers'"
                        " or check your inventory."
                    ),
                )

            wan_rs_result_dict = {
                "router_id": router_id,
                "wan_path_groups": wan_path_groups,
            }

            if any(interface["ip_address"] == "dhcp" for path_group in wan_rs_result_dict["wan_path_groups"] for interface in path_group.get("interfaces", [])):
                raise AristaAvdError(
                    f"The IP address for a WAN interface on a Route Server '{wan_rs}' is set 'dhcp'. Clients need to peer with a static IP which can be set"
                    " under the 'wan_route_servers.path_groups.interfaces' key."
                )

            wan_route_servers[wan_rs] = strip_empties_from_dict(wan_rs_result_dict)

        return wan_route_servers

    def _stun_server_profile_name(self, wan_route_server_name: str, path_group_name: str, interface_name: str) -> str:
        """
        Return a string to use as the name of the stun server_profile
        """
        return f"{path_group_name}-{wan_route_server_name}-{interface_name}"

    def _should_connect_to_wan_rs(self, path_groups: list) -> bool:
        """
        This helper implements wherther or not a connection to the wan_rs should be made or not based on a list of path-groups.

        To do this the logic is the following:
        * Look at the wan_interfaces on the router and check if there is any path-group in common with the RR where
          `connected_to_pathfinder` is not False.
        """
        return any(
            self.shared_utils.get_carrier_path_group(wan_interface["wan_carrier"])["name"] in path_groups
            and get(
                wan_interface,
                "connected_to_pathfinder",
                default=True,
            )
            for wan_interface in self.shared_utils.wan_interfaces
        )

    @cached_property
    def _filtered_wan_route_servers(self) -> dict:
        """
        Return a dictionary of wan_route_servers with only the path_groups the router should connect to
        """
        filtered_wan_route_servers = {}
        for wan_route_server, data in self._wan_route_servers.items():
            if wan_route_server == self.shared_utils.hostname:
                # Do not include yourself
                continue
            for path_group in data.get("wan_path_groups", []):
                if self._should_connect_to_wan_rs([path_group["name"]]):
                    filtered_wan_route_servers.setdefault(wan_route_server, {"router_id": data["router_id"], "wan_path_groups": []})["wan_path_groups"].append(
                        path_group
                    )

        return filtered_wan_route_servers

    @cached_property
    def _stun_server_profiles(self) -> list:
        """
        Return a dictionary of _stun_server_profiles with ip_address per local path_group
        """
        stun_server_profiles = {}
        for wan_route_server, data in self._filtered_wan_route_servers.items():
            for path_group in data.get("wan_path_groups", []):
                stun_server_profiles.setdefault(path_group["name"], []).extend(
                    {
                        "name": self._stun_server_profile_name(wan_route_server, path_group["name"], get(interface_dict, "name", required=True)),
                        "ip_address": get(interface_dict, "ip_address", required=True),
                    }
                    for interface_dict in get(path_group, "interfaces", required=True)
                )
        return stun_server_profiles
