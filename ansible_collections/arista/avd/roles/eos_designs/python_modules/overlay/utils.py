from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.utils import get
from ansible_collections.arista.avd.roles.eos_designs.python_modules.interface_descriptions import AvdInterfaceDescriptions


class UtilsMixin:
    """
    Mixin Class with internal functions.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    # Set type hints for Attributes of the main class as needed
    _hostvars: dict
    _avd_interface_descriptions: AvdInterfaceDescriptions

    @cached_property
    def _avd_peers(self) -> list:
        """
        Returns a list of peers
        """
        return get(self._hostvars, f"avd_topology_peers..{self._hostname}", separator="..", default=[])

    @cached_property
    def _bgp_as(self) -> str | None:
        return get(self._hostvars, "switch.bgp_as")

    @cached_property
    def _enable_trunk_groups(self) -> bool:
        return get(self._hostvars, "switch.enable_trunk_groups") is True

    @cached_property
    def _evpn_role(self) -> str | None:
        return get(self._hostvars, "switch.evpn_role")

    @cached_property
    def _evpn_short_esi_prefix(self) -> str:
        return get(self._hostvars, "evpn_short_esi_prefix", required=True)

    @cached_property
    def _filter_peer_as(self) -> bool:
        return self._underlay_filter_peer_as is True and self._evpn_role not in ["client", "server"]

    @cached_property
    def _hostname(self) -> str:
        return get(self._hostvars, "switch.hostname", required=True)

    @cached_property
    def _isis_instance_name(self) -> str:
        return get(self._hostvars, "switch.isis_instance_name", required=True)

    @cached_property
    def _ipv6_router_id(self) -> str | None:
        return get(self._hostvars, "switch.ipv6_router_id")

    @cached_property
    def _ldp(self) -> bool:
        return self._underlay_routing_protocol in ["isis-ldp", "isis-sr-ldp", "ospf-ldp"]

    @cached_property
    def _loopback_ipv4_offset(self) -> int:
        return int(get(self._hostvars, "switch.loopback_ipv4_offset", required=True))

    @cached_property
    def _loopback_ipv4_pool(self) -> str:
        return get(self._hostvars, "switch.loopback_ipv4_pool")

    @cached_property
    def _loopback_ipv6_pool(self) -> str:
        return get(self._hostvars, "switch.loopback_ipv6_pool", required=True)

    @cached_property
    def _mlag(self) -> bool:
        return get(self._hostvars, "switch.mlag") is True

    @cached_property
    def _mlag_l3(self) -> bool:
        return get(self._hostvars, "switch.mlag_l3") is True

    @cached_property
    def _mpls_lsr(self) -> bool:
        return get(self._hostvars, "switch.mpls_lsr") is True

    @cached_property
    def _network_services_l3(self) -> bool:
        return get(self._hostvars, "switch.network_services_l3", required=True) is True

    @cached_property
    def _node_sid(self) -> str:
        return get(self._hostvars, "switch.node_sid", required=True)

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
    def _overlay_ler(self) -> bool:
        return get(self._hostvars, "switch.overlay.ler", required=True) is True

    @cached_property
    def _peer_group_rr_overlay_peers(self) -> str:
        return get(self._hostvars, "switch.bgp_peer_groups.rr_overlay_peers.name")

    @cached_property
    def _router_id(self) -> str | None:
        return get(self._hostvars, "switch.router_id")

    @cached_property
    def _uplinks(self) -> list:
        return get(self._hostvars, "switch.uplinks")

    @cached_property
    def _vtep_ip(self) -> str:
        return get(self._hostvars, "switch.vtep_ip")

    @cached_property
    def _vtep_loopback(self) -> str:
        return get(self._hostvars, "switch.vtep_loopback")

    @cached_property
    def _vtep_loopback_ipv4_pool(self) -> str:
        return get(self._hostvars, "switch.vtep_loopback_ipv4_pool")

    @cached_property
    def _vtep_vvtep_ip(self) -> str:
        return get(self._hostvars, "switch.vtep_vvtep_ip")

    # NEW
    @cached_property
    def _bfd_multihop(self) -> dict | None:
        return get(self._hostvars, "bfd_multihop")

    @cached_property
    def _configure_overlay(self) -> bool:
        return (
            get(self._hostvars, "switch.overlay.evpn") is True
            or get(self._hostvars, "switch.overlay.vpn_ipv4") is True
            or get(self._hostvars, "switch.overlay.vpn_ipv6") is True
        )

    @cached_property
    def _evpn_ebgp_multihop(self) -> int | None:
        return get(self._hostvars, "evpn_ebgp_multihop")

    @cached_property
    def _evpn_ebgp_gateway_multihop(self) -> int | None:
        return get(self._hostvars, "evpn_ebgp_gateway_multihop")

    @cached_property
    def _evpn_overlay_bgp_rtc(self) -> bool:
        return get(self._hostvars, "evpn_overlay_bgp_rtc") is True

    @cached_property
    def _evpn_prevent_readvertise_to_server(self) -> bool:
        return get(self._hostvars, "switch.evpn_prevent_readvertise_to_server") is True

    @cached_property
    def _peer_group_mpls_overlay_peers(self) -> str | None:
        return get(self._hostvars, "switch.bgp_peer_groups.mpls_overlay_peers.name")

    @cached_property
    def _peer_group_evpn_overlay_peers(self) -> str | None:
        return get(self._hostvars, "switch.bgp_peer_groups.evpn_overlay_peers.name")

    @cached_property
    def _peer_group_evpn_overlay_core(self) -> str | None:
        return get(self._hostvars, "switch.bgp_peer_groups.evpn_overlay_core.name")

    @cached_property
    def _overlay_evpn(self) -> bool:
        return get(self._hostvars, "switch.overlay.evpn") is True

    @cached_property
    def _overlay_mpls(self) -> bool:
        return (
            get(self._hostvars, "switch.overlay.evpn_mpls") is True
            or get(self._hostvars, "switch.overlay.vpn_ipv4") is True
            or get(self._hostvars, "switch.overlay.vpn_ipv6") is True
        )

    @cached_property
    def _mpls_overlay_role(self) -> str | None:
        return get(self._hostvars, "switch.mpls_overlay_role")

    @cached_property
    def _mpls_route_reflectors(self) -> dict:
        if self._mpls_overlay_role != "client":
            return {}

        mpls_route_reflectors = {}

        for route_reflector in sorted(get(self._hostvars, "switch.mpls_route_reflectors")):
            peer_facts = get(
                self._hostvars,
                f"avd_switch_facts..{route_reflector}..switch",
                separator="..",
                required=True,
                org_key=f"avd_switch_facts.{route_reflector}.switch",
            )
            if peer_facts.get("mpls_overlay_role") != "server":
                continue

            mpls_route_reflectors[route_reflector] = {
                "bgp_as": peer_facts.get("bgp_as"),
                "ip_address": get(peer_facts, "overlay.peering_address", required=True),
            }

        return mpls_route_reflectors

    def _overlay_evpn_mpls(self) -> bool:
        return get(self._hostvars, "switch.overlay.evpn_mpls") is True

    @cached_property
    def _mpls_rr_peers(self) -> dict:
        if not self._overlay_mpls:
            return {}

        if self._mpls_overlay_role != "server" or not (self._evpn_role == "server" and self._overlay_evpn_mpls):
            return {}

        mpls_rr_peers = {}

        for route_reflector in sorted(get(self._hostvars, "switch.mpls_route_reflectors", default=[])):
            peer_facts = get(
                self._hostvars,
                f"avd_switch_facts..{route_reflector}..switch",
                separator="..",
                required=True,
                org_key=f"avd_switch_facts.{route_reflector}.switch",
            )
            if peer_facts.get("mpls_overlay_role") != "server":
                continue

            mpls_rr_peers[route_reflector] = {
                "bgp_as": peer_facts.get("bgp_as"),
                "ip_address": get(peer_facts, "overlay.peering_address", required=True),
            }

        for avd_peer in self._avd_overlay_peers:
            peer_facts = get(
                self._hostvars,
                f"avd_switch_facts..{avd_peer}..switch",
                separator="..",
                required=True,
                org_key=f"avd_switch_facts.{avd_peer}.switch",
            )

            if peer_facts.get("mpls_overlay_role") != "server" or not (peer_facts.get("evpn_role") == "server" and self._overlay_evpn_mpls is True):
                continue

            if self._hostname in peer_facts.get("mpls_route_reflectors", []) and avd_peer not in self._mpls_route_reflectors.keys():
                mpls_rr_peers[avd_peer] = {
                    "bgp_as": peer_facts.get("bgp_as"),
                    "ip_address": get(peer_facts, "overlay.peering_address", required=True),
                }

        return mpls_rr_peers

    @cached_property
    def _fabric_name(self) -> str:
        return get(self._hostvars, "fabric_name", required=True)

    @cached_property
    def _fabric_group_devices(self) -> list:
        return get(self._hostvars, f"groups.{self._fabric_name}")

    @cached_property
    def _bgp_mesh_pe(self) -> bool:
        return get(self._hostvars, "bgp_mesh_pe") is True

    @cached_property
    def _mpls_mesh_pe(self) -> dict:
        if not self._overlay_mpls:
            return {}

        if self._bgp_mesh_pe is not True:
            return {}

        mpls_mesh_pe = {}

        for fabric_switch in self._fabric_group_devices:
            if self._mpls_route_reflectors is not None and fabric_switch in self._mpls_route_reflectors:
                continue
            if fabric_switch == self._hostname:
                continue

            peer_facts = get(
                self._hostvars,
                f"avd_switch_facts..{fabric_switch}..switch",
                separator="..",
                required=True,
                org_key=f"avd_switch_facts.{fabric_switch}.switch",
            )
            if peer_facts.get("mpls_overlay_role") != "client":
                continue

            mpls_mesh_pe[fabric_switch] = {
                "bgp_as": peer_facts.get("bgp_as"),
                "ip_address": get(peer_facts, "overlay.peering_address", required=True),
            }

        return mpls_mesh_pe

    @cached_property
    def _avd_overlay_peers(self) -> list:
        """
        Returns a list of overlay peers for the device
        """
        return get(self._hostvars, f"avd_overlay_peers..{self._hostname}", separator="..", default=[])

    @cached_property
    def _mpls_route_clients(self) -> dict:
        if not self._overlay_mpls:
            return {}

        if self._mpls_overlay_role != "server" or not (self._evpn_role == "server" and self._overlay_evpn_mpls):
            return {}

        mpls_route_clients = {}

        for avd_peer in self._avd_overlay_peers:
            peer_facts = get(
                self._hostvars,
                f"avd_switch_facts..{avd_peer}..switch",
                separator="..",
                required=True,
                org_key=f"avd_switch_facts.{avd_peer}.switch",
            )

            if peer_facts.get("mpls_overlay_role") != "client" or not (peer_facts.get("evpn_role") == "client" and self._overlay_evpn_mpls is True):
                continue

            if self._hostname in peer_facts.get("mpls_route_reflectors", []) and avd_peer not in self._mpls_route_reflectors.keys():
                mpls_route_clients[avd_peer] = {
                    "bgp_as": peer_facts.get("bgp_as"),
                    "ip_address": get(peer_facts, "overlay.peering_address", required=True),
                }

        return mpls_route_clients

    @cached_property
    def _evpn_route_servers(self) -> dict:
        if not self._overlay_evpn:
            return {}

        evpn_route_servers = {}

        for route_server in sorted(get(self._hostvars, "switch.evpn_route_servers", default=[])):
            peer_facts = get(
                self._hostvars,
                f"avd_switch_facts..{route_server}..switch",
                separator="..",
                required=True,
                org_key=f"avd_switch_facts.{route_server}.switch",
            )
            if peer_facts.get("evpn_role") != "server":
                continue

            evpn_route_servers[route_server] = {
                "bgp_as": peer_facts.get("bgp_as"),
                "ip_address": get(peer_facts, "overlay.peering_address", required=True),
            }

        return evpn_route_servers

    @cached_property
    def _evpn_gateway_remote_peers(self) -> dict:
        if not self._overlay_evpn:
            return {}

        evpn_gateway_remote_peers = {}

        for gw_remote_peer_dict in sorted(get(self._hostvars, "switch.evpn_gateway_remote_peers", default=[])):
            # These remote gw can be outside of the inventory
            gw_remote_peer = gw_remote_peer_dict["hostname"]
            peer_facts = get(
                self._hostvars,
                f"avd_switch_facts..{gw_remote_peer}..switch",
                separator="..",
                org_key=f"avd_switch_facts.{gw_remote_peer}.switch",
            )

            if peer_facts is not None:
                # Found a matching server in inventory
                bgp_as = peer_facts.get("bgp_as")
                ip_address = get(peer_facts, "overlay.peering_address", required=True)

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
        if not self._overlay_evpn:
            return {}

        if self._evpn_role != "server":
            return {}

        evpn_route_clients = {}

        for avd_peer in self._avd_overlay_peers:
            peer_facts = get(
                self._hostvars,
                f"avd_switch_facts..{avd_peer}..switch",
                separator="..",
                required=True,
                org_key=f"avd_switch_facts.{avd_peer}.switch",
            )

            if (
                self._hostname in peer_facts.get("evpn_route_servers", [])
                and peer_facts.get("evpn_role") in ["server", "client"]
                and avd_peer not in self._evpn_route_servers.keys()
            ):
                evpn_route_clients[avd_peer] = {
                    "bgp_as": peer_facts.get("bgp_as"),
                    "ip_address": get(peer_facts, "overlay.peering_address", required=True),
                }

        return evpn_route_clients

    @cached_property
    def _evpn_gateway_vxlan_l2(self) -> bool:
        return get(self._hostvars, "switch.evpn_gateway_vxlan_l2") is True

    @cached_property
    def _evpn_gateway_vxlan_l3(self) -> bool:
        return get(self._hostvars, "switch.evpn_gateway_vxlan_l3") is True
