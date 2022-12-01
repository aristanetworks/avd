from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.strip_empties import strip_empties_from_dict
from ansible_collections.arista.avd.plugins.plugin_utils.utils import default, get
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
        peers = default(get(get(self._hostvars, "avd_topology_peers"), self._hostname, separator=".."), [])
        return peers

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
    def _p2p_uplinks_mtu(self):
        return get(self._hostvars, "p2p_uplinks_mtu", required=True)

    @cached_property
    def _peer_group_ipv4_underlay_peers_name(self) -> str:
        return get(self._hostvars, "switch.bgp_peer_groups.ipv4_underlay_peers.name", required=True)

    @cached_property
    def _router_id(self) -> str | None:
        return get(self._hostvars, "switch.router_id")

    @cached_property
    def _shutdown_interfaces_towards_undeployed_peers(self) -> bool:
        return get(self._hostvars, "shutdown_interfaces_towards_undeployed_peers") is True

    @cached_property
    def _underlay_filter_peer_as(self) -> bool:
        return get(self._hostvars, "underlay_filter_peer_as") is True

    @cached_property
    def _underlay_ipv6(self) -> bool:
        return get(self._hostvars, "underlay_ipv6") is True

    @cached_property
    def _underlay_links(self) -> list:
        """
        Returns the list of underlay links for this device
        """
        underlay_links = []
        underlay_links.extend(self._uplinks)

        for peer in self._avd_peers:
            peer_facts = get(self._hostvars, f"avd_switch_facts..{peer}..switch", separator="..")
            for uplink in peer_facts["uplinks"]:
                if uplink["peer"] == self._hostname:
                    link = {
                        "interface": uplink["peer_interface"],
                        "peer": peer,
                        "peer_interface": uplink["interface"],
                        "peer_type": get(peer_facts, "type"),
                        "peer_is_deployed": peer_facts["is_deployed"],
                        "peer_bgp_as": get(peer_facts, "bgp_as"),
                        "type": get(uplink, "type", required=True),
                        "speed": get(uplink, "speed"),
                        "ip_address": get(uplink, "peer_ip_address"),
                        "peer_ip_address": get(uplink, "ip_address"),
                        "channel_group_id": get(uplink, "peer_channel_group_id"),
                        "peer_channel_group_id": get(uplink, "channel_group_id"),
                        "channel_description": get(uplink, "peer_channel_description"),
                        "vlans": get(uplink, "vlans"),
                        "trunk_groups": get(uplink, "peer_trunk_groups"),
                        "bfd": get(uplink, "bfd"),
                        "ptp": get(uplink, "ptp"),
                        "mac_security": get(uplink, "mac_security"),
                        "short_esi": get(uplink, "peer_short_esi"),
                        "underlay_multicast": get(uplink, "underlay_multicast"),
                        "ipv6_enable": get(uplink, "ipv6_enable"),
                        "structured_config": get(uplink, "structured_config"),
                    }
                    underlay_links.append(strip_empties_from_dict(link))

        return underlay_links

    @cached_property
    def _underlay_multicast(self) -> bool:
        return get(self._hostvars, "switch.underlay_mullticast") is True

    @cached_property
    def _underlay_ospf_area(self) -> str:
        return get(self._hostvars, "underlay_ospf_area", required=True)

    @cached_property
    def _underlay_ospf_process_id(self) -> int:
        return get(self._hostvars, "underlay_ospf_process_id", required=True)

    @cached_property
    def _underlay_rfc5549(self) -> bool:
        return get(self._hostvars, "underlay_rfc5549") is True

    @cached_property
    def _underlay_router(self) -> str | None:
        return get(self._hostvars, "switch.underlay_router")

    @cached_property
    def _underlay_routing_protocol(self) -> str | None:
        return get(self._hostvars, "switch.underlay_routing_protocol")

    @cached_property
    def _underlay_vlan_trunk_groups(self) -> list:
        """
        Returns a list of trunk groups to configure on the underlay link
        """
        if self._enable_trunk_groups is not True:
            return []

        trunk_groups = []

        for peer in self._avd_peers:
            peer_facts = get(self._hostvars, f"avd_switch_facts..{peer}..switch", separator="..")
            for uplink in peer_facts["uplinks"]:
                if uplink["peer"] == self._hostname:
                    if (peer_trunk_groups := get(uplink, "peer_trunk_groups")) is None:
                        continue

                    trunk_groups.append({"vlan_list": uplink["vlans"], "trunk_groups": peer_trunk_groups})

        if trunk_groups:
            return trunk_groups

        return []

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
