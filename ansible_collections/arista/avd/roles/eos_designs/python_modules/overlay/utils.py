# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.filter.natural_sort import natural_sort
from ansible_collections.arista.avd.plugins.plugin_utils.eos_designs_shared_utils.shared_utils import SharedUtils
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get


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
