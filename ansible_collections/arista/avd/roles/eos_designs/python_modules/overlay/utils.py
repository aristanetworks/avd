from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.filter.natural_sort import natural_sort
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get


class UtilsMixin:
    """
    Mixin Class with internal functions.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    # Set type hints for Attributes of the main class as needed
    _hostvars: dict

    @cached_property
    def _avd_overlay_peers(self) -> list:
        """
        Returns a list of overlay peers for the device
        """
        return get(self._hostvars, f"avd_overlay_peers..{self._hostname}", separator="..", default=[])

    @cached_property
    def _bfd_multihop(self) -> dict | None:
        return get(self._hostvars, "bfd_multihop")

    @cached_property
    def _bgp_as(self) -> str | None:
        bgp_as = get(self._hostvars, "switch.bgp_as")
        return str(bgp_as) if bgp_as is not None else None

    @cached_property
    def _evpn_ebgp_multihop(self) -> int | None:
        return get(self._hostvars, "evpn_ebgp_multihop")

    @cached_property
    def _evpn_ebgp_gateway_multihop(self) -> int | None:
        return get(self._hostvars, "evpn_ebgp_gateway_multihop")

    @cached_property
    def _evpn_gateway_vxlan_l2(self) -> bool:
        return get(self._hostvars, "switch.evpn_gateway_vxlan_l2") is True

    @cached_property
    def _evpn_gateway_vxlan_l3(self) -> bool:
        return get(self._hostvars, "switch.evpn_gateway_vxlan_l3") is True

    @cached_property
    def _evpn_gateway_remote_peers(self) -> dict:
        if not self._overlay_evpn:
            return {}

        evpn_gateway_remote_peers = {}

        for gw_remote_peer_dict in natural_sort(get(self._hostvars, "switch.evpn_gateway_remote_peers", default=[]), sort_key="hostname"):
            # These remote gw can be outside of the inventory
            gw_remote_peer = gw_remote_peer_dict["hostname"]
            peer_facts = self._get_peer_facts(gw_remote_peer, required=False)

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
    def _evpn_overlay_bgp_rtc(self) -> bool:
        return get(self._hostvars, "evpn_overlay_bgp_rtc") is True

    @cached_property
    def _evpn_prevent_readvertise_to_server(self) -> bool:
        return get(self._hostvars, "evpn_prevent_readvertise_to_server") is True

    @cached_property
    def _evpn_route_clients(self) -> dict:
        if not self._overlay_evpn:
            return {}

        if self._evpn_role != "server":
            return {}

        evpn_route_clients = {}

        for avd_peer in self._avd_overlay_peers:
            peer_facts = self._get_peer_facts(avd_peer)
            if not peer_facts:
                continue

            if (
                self._hostname in peer_facts.get("evpn_route_servers", [])
                and peer_facts.get("evpn_role") in ["server", "client"]
                and avd_peer not in self._evpn_route_servers.keys()
            ):
                self._append_peer(evpn_route_clients, avd_peer, peer_facts)

        return evpn_route_clients

    @cached_property
    def _evpn_route_servers(self) -> dict:
        if not self._overlay_evpn:
            return {}

        evpn_route_servers = {}

        for route_server in natural_sort(get(self._hostvars, "switch.evpn_route_servers", default=[])):
            peer_facts = self._get_peer_facts(route_server)
            if not peer_facts or peer_facts.get("evpn_role") != "server":
                continue

            self._append_peer(evpn_route_servers, route_server, peer_facts)

        return evpn_route_servers

    @cached_property
    def _evpn_role(self) -> str | None:
        return get(self._hostvars, "switch.evpn_role")

    @cached_property
    def _fabric_group_devices(self) -> list:
        fabric_name = get(self._hostvars, "fabric_name", required=True)
        return get(self._hostvars, f"groups.{fabric_name}")

    @cached_property
    def _hostname(self) -> str:
        return get(self._hostvars, "switch.hostname", required=True)

    # The next four should probably be moved to facts
    @cached_property
    def _is_mpls_client(self) -> bool:
        return self._mpls_overlay_role == "client" or (self._evpn_role == "client" and self._overlay_evpn_mpls is True)

    @cached_property
    def _is_mpls_server(self) -> bool:
        return self._mpls_overlay_role == "server" or (self._evpn_role == "server" and self._overlay_evpn_mpls is True)

    def _is_peer_mpls_client(self, peer_facts: dict) -> bool:
        return peer_facts.get("mpls_overlay_role", None) == "client" or (
            peer_facts.get("evpn_role", None) == "client" and get(peer_facts, "overlay.evpn_mpls") is True
        )

    def _is_peer_mpls_server(self, peer_facts: dict) -> bool:
        return peer_facts.get("mpls_overlay_role", None) == "server" or (
            peer_facts.get("evpn_role", None) == "server" and get(peer_facts, "overlay.evpn_mpls") is True
        )

    @cached_property
    def _ipvpn_gateway_remote_peers(self) -> dict:
        if self._overlay_ipvpn_gateway is not True:
            return {}

        ipvpn_gateway_remote_peers = {}

        for ipvpn_gw_peer_dict in natural_sort(get(self._hostvars, "switch.ipvpn_gateway.remote_peers", default=[]), "hostname"):
            # These remote gw are outside of the inventory

            bgp_as = ipvpn_gw_peer_dict["bgp_as"]

            ipvpn_gateway_remote_peers[ipvpn_gw_peer_dict["hostname"]] = {
                "bgp_as": str(bgp_as) if bgp_as is not None else None,
                "ip_address": ipvpn_gw_peer_dict["ip_address"],
            }

        return ipvpn_gateway_remote_peers

    @cached_property
    def _mpls_overlay_role(self) -> str | None:
        return get(self._hostvars, "switch.mpls_overlay_role")

    @cached_property
    def _mpls_route_clients(self) -> dict:
        if self._is_mpls_server is not True:
            return {}

        mpls_route_clients = {}

        for avd_peer in self._avd_overlay_peers:
            peer_facts = self._get_peer_facts(avd_peer)
            if not peer_facts or self._is_peer_mpls_client(peer_facts) is not True:
                continue

            if self._hostname in peer_facts.get("mpls_route_reflectors", []) and avd_peer not in self._mpls_route_reflectors.keys():
                self._append_peer(mpls_route_clients, avd_peer, peer_facts)

        return mpls_route_clients

    @cached_property
    def _mpls_mesh_pe(self) -> dict:
        if self._overlay_mpls is not True:
            return {}

        _bgp_mesh_pe = get(self._hostvars, "bgp_mesh_pe") is True
        if _bgp_mesh_pe is not True:
            return {}

        mpls_mesh_pe = {}

        for fabric_switch in self._fabric_group_devices:
            if self._mpls_route_reflectors is not None and fabric_switch in self._mpls_route_reflectors:
                continue
            if fabric_switch == self._hostname:
                continue

            peer_facts = self._get_peer_facts(fabric_switch)
            if not peer_facts or self._is_peer_mpls_client(peer_facts) is not True:
                continue

            self._append_peer(mpls_mesh_pe, fabric_switch, peer_facts)

        return mpls_mesh_pe

    @cached_property
    def _mpls_route_reflectors(self) -> dict:
        if self._is_mpls_client is not True:
            return {}

        mpls_route_reflectors = {}

        for route_reflector in natural_sort(get(self._hostvars, "switch.mpls_route_reflectors", default=[])):
            if route_reflector == self._hostname:
                continue

            peer_facts = self._get_peer_facts(route_reflector)
            if not peer_facts or self._is_peer_mpls_server(peer_facts) is not True:
                continue

            self._append_peer(mpls_route_reflectors, route_reflector, peer_facts)

        return mpls_route_reflectors

    @cached_property
    def _mpls_rr_peers(self) -> dict:
        if self._is_mpls_server is not True:
            return {}

        mpls_rr_peers = {}

        for route_reflector in natural_sort(get(self._hostvars, "switch.mpls_route_reflectors", default=[])):
            if route_reflector == self._hostname:
                continue

            peer_facts = self._get_peer_facts(route_reflector)
            if not peer_facts or self._is_peer_mpls_server(peer_facts) is not True:
                continue

            self._append_peer(mpls_rr_peers, route_reflector, peer_facts)

        for avd_peer in self._avd_overlay_peers:
            peer_facts = self._get_peer_facts(avd_peer)
            if not peer_facts or self._is_peer_mpls_server(peer_facts) is not True:
                continue

            if self._hostname in peer_facts.get("mpls_route_reflectors", []) and avd_peer not in get(
                self._hostvars, "switch.mpls_route_reflectors", default=[]
            ):
                self._append_peer(mpls_rr_peers, avd_peer, peer_facts)

        return mpls_rr_peers

    @cached_property
    def _overlay_dpath(self) -> bool:
        return get(self._hostvars, "switch.overlay.dpath") is True

    @cached_property
    def _overlay_evpn(self) -> bool:
        return get(self._hostvars, "switch.overlay.evpn") is True

    @cached_property
    def _overlay_evpn_mpls(self) -> bool:
        return get(self._hostvars, "switch.overlay.evpn_mpls") is True

    @cached_property
    def _overlay_evpn_vxlan(self) -> bool:
        return get(self._hostvars, "switch.overlay.evpn_vxlan") is True

    @cached_property
    def _overlay_ipvpn_gateway(self) -> bool:
        return get(self._hostvars, "switch.overlay.ipvpn_gateway", required=True) is True

    @cached_property
    def _overlay_ler(self) -> bool:
        return get(self._hostvars, "switch.overlay.ler", required=True) is True

    @cached_property
    def _overlay_mpls(self) -> bool:
        return (self._overlay_evpn_mpls is True or self._overlay_vpn_ipv4 is True or self._overlay_vpn_ipv6 is True) and self._overlay_evpn_vxlan is not True

    @cached_property
    def _overlay_routing_protocol(self) -> str | None:
        return get(self._hostvars, "switch.overlay_routing_protocol")

    @cached_property
    def _overlay_vtep(self) -> bool:
        return get(self._hostvars, "switch.overlay.vtep", required=True) is True

    @cached_property
    def _overlay_vpn_ipv4(self) -> bool:
        return get(self._hostvars, "switch.overlay.vpn_ipv4", required=True) is True

    @cached_property
    def _overlay_vpn_ipv6(self) -> bool:
        return get(self._hostvars, "switch.overlay.vpn_ipv6", required=True) is True

    @cached_property
    def _peer_group_evpn_overlay_core(self) -> str | None:
        return get(self._hostvars, "switch.bgp_peer_groups.evpn_overlay_core.name")

    @cached_property
    def _peer_group_evpn_overlay_peers(self) -> str | None:
        return get(self._hostvars, "switch.bgp_peer_groups.evpn_overlay_peers.name")

    @cached_property
    def _peer_group_ipvpn_gateway_peers(self) -> str | None:
        return get(self._hostvars, "switch.bgp_peer_groups.ipvpn_gateway_peers.name")

    @cached_property
    def _peer_group_mpls_overlay_peers(self) -> str | None:
        return get(self._hostvars, "switch.bgp_peer_groups.mpls_overlay_peers.name")

    @cached_property
    def _peer_group_rr_overlay_peers(self) -> str:
        return get(self._hostvars, "switch.bgp_peer_groups.rr_overlay_peers.name")

    @cached_property
    def _router_id(self) -> str | None:
        return get(self._hostvars, "switch.router_id")

    @cached_property
    def _vtep_ip(self) -> str:
        return get(self._hostvars, "switch.vtep_ip")

    # utils functions
    def _get_peer_facts(self, peer_name: str, required: bool = True) -> dict | None:
        """
        util function to retrieve peer_facts for peer_name

        returns avd_switch_facts.{peer_name}.switch

        by default required is True and so the function will raise is peer_facts cannot be found
        using the separator `..` to be able to handle hostnames with `.` inside
        """
        return get(
            self._hostvars,
            f"avd_switch_facts..{peer_name}..switch",
            separator="..",
            required=required,
            org_key=f"avd_switch_facts.{peer_name}.switch",
        )

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
            "ip_address": get(peer_facts, "overlay.peering_address", required=True),
        }
