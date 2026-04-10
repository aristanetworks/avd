# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""
Structured Config Utils Module.

This module provides utility classes for structured config generation.
"""

from __future__ import annotations

import ipaddress
from typing import TYPE_CHECKING

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.parent_interfaces import ParentInterfacesTracker
from pyavd._utils import as_path_list_match_from_bgp_asns
from pyavd._utils.format_string import AvdStringFormatter
from pyavd._utils.run_once import RunOnceMethodStateHelper, run_once_method

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns
    from pyavd._eos_designs.shared_utils import SharedUtilsProtocol
    from pyavd._eos_designs.structured_config.structured_config_generator import StructCfgs


class StructuredConfigUtils(RunOnceMethodStateHelper):
    """
    Utility class for structured config generation.

    This class holds shared utilities and trackers used across all structured config modules.
    """

    def __init__(
        self, structured_config: EosCliConfigGen, inputs: EosDesigns, shared_utils: SharedUtilsProtocol, custom_structured_configs: StructCfgs
    ) -> None:
        """Initialize the StructuredConfigUtils with a ParentInterfacesTracker instance and structured config instance."""
        super().__init__()
        self.structured_config = structured_config
        self.custom_structured_configs = custom_structured_configs
        self.inputs = inputs
        """The shared structured config instance to write config into."""
        self.shared_utils = shared_utils
        self.custom_structured_configs = custom_structured_configs
        """Tracker for parent interfaces that need to be created for subinterfaces."""
        self.parent_interfaces_tracker = ParentInterfacesTracker()

    @run_once_method
    def set_once_peer_group_ipv4_underlay_peers(self: StructuredConfigUtils) -> None:
        """
        Add IPv4 underlay peer group to structured_config.

        Also adds required route-maps and prefix-lists.
        """
        af_type = "ipv4" if not self.shared_utils.underlay_ipv6_numbered else "ipv6"

        peer_group = EosCliConfigGen.RouterBgp.PeerGroupsItem(
            name=self.inputs.bgp_peer_groups.ipv4_underlay_peers.name,
            password=self.shared_utils.get_bgp_password(self.inputs.bgp_peer_groups.ipv4_underlay_peers),
            bfd=self.inputs.bgp_peer_groups.ipv4_underlay_peers.bfd or None,
            maximum_routes=self.inputs.bgp_peer_groups.ipv4_underlay_peers.maximum_routes,
            send_community="all",
        )
        peer_group.metadata.type = af_type
        if self.inputs.bgp_peer_groups.ipv4_underlay_peers.structured_config:
            self.custom_structured_configs.nested.router_bgp.peer_groups.obtain(self.inputs.bgp_peer_groups.ipv4_underlay_peers.name)._deepmerge(
                self.inputs.bgp_peer_groups.ipv4_underlay_peers.structured_config, list_merge=self.custom_structured_configs.list_merge_strategy
            )

        if self.shared_utils.is_cv_pathfinder_router:
            peer_group.route_map_in = "RM-BGP-UNDERLAY-PEERS-IN"
            self.set_route_map_bgp_underlay_peers_in()
            if self.shared_utils.wan_ha:
                peer_group.route_map_out = "RM-BGP-UNDERLAY-PEERS-OUT"
                self.set_route_map_bgp_underlay_peers_out()
                if self.shared_utils.use_uplinks_for_wan_ha:
                    # For HA need to add allowas_in 1
                    peer_group.allowas_in._update(enabled=True, times=1)

        self.structured_config.router_bgp.peer_groups.append(peer_group)

        # Address Families
        # TODO: - see if it makes sense to extract logic in method
        if not self.shared_utils.underlay_ipv6_numbered:
            address_family_ipv4_peer_group = EosCliConfigGen.RouterBgp.AddressFamilyIpv4.PeerGroupsItem(
                name=self.inputs.bgp_peer_groups.ipv4_underlay_peers.name, activate=True
            )
            if self.inputs.underlay_rfc5549 is True:
                address_family_ipv4_peer_group.next_hop.address_family_ipv6._update(enabled=True, originate=True)

            self.structured_config.router_bgp.address_family_ipv4.peer_groups.append(address_family_ipv4_peer_group)

        if self.shared_utils.underlay_ipv6:
            self.structured_config.router_bgp.address_family_ipv6.peer_groups.append_new(
                name=self.inputs.bgp_peer_groups.ipv4_underlay_peers.name, activate=True
            )

    def set_route_map_bgp_underlay_peers_in(self: StructuredConfigUtils) -> None:
        """Set route-map RM-BGP-UNDERLAY-PEERS-IN."""
        # RM-BGP-UNDERLAY-PEERS-IN
        sequence_numbers = EosCliConfigGen.RouteMapsItem.SequenceNumbers()
        sequence_numbers.append_new(
            sequence=40,
            type="permit",
            set=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Set([f"extcommunity soo {self.shared_utils.evpn_soo} additive"]),
            description="Mark prefixes originated from the LAN",
        )
        if self.shared_utils.wan_ha and self.shared_utils.use_uplinks_for_wan_ha:
            sequence_numbers.append_new(
                sequence=10,
                type="permit",
                match=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Match(["ip address prefix-list PL-WAN-HA-PEER-PREFIXES"]),
                description="Allow WAN HA peer interface prefixes",
            )
            # Create the prefix-list.
            self.set_prefix_list_wan_ha_peer_prefixes()

            sequence_numbers.append_new(
                sequence=20,
                type="deny",
                match=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Match(["as-path ASPATH-WAN"]),
                description="Deny other routes from the HA peer",
            )
            # Create AS Path ACL
            self.set_as_path_acl_aspath_wan()

        self.structured_config.route_maps.append_new(name="RM-BGP-UNDERLAY-PEERS-IN", sequence_numbers=sequence_numbers)

    def set_route_map_bgp_underlay_peers_out(self: StructuredConfigUtils) -> None:
        """Set route-map RM-BGP-UNDERLAY-PEERS-OUT."""
        sequence_numbers = EosCliConfigGen.RouteMapsItem.SequenceNumbers()
        sequence_numbers.append_new(
            sequence=10,
            type="permit",
            match=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Match(["tag 50", "route-type internal"]),
            description="Make routes learned from WAN HA peer less preferred on LAN routers",
            set=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Set(["metric 50"]),
        )
        sequence_numbers.append_new(sequence=20, type="permit")

        self.structured_config.route_maps.append_new(name="RM-BGP-UNDERLAY-PEERS-OUT", sequence_numbers=sequence_numbers)

    def set_prefix_list_wan_ha_peer_prefixes(self: StructuredConfigUtils) -> None:
        """Set prefix-list PL-WAN-HA-PEER-PREFIXES."""
        sequence_numbers = EosCliConfigGen.PrefixListsItem.SequenceNumbers()
        for index, ip_address in enumerate(self.shared_utils.wan_ha_peer_ip_addresses, start=1):
            sequence_numbers.append_new(sequence=10 * index, action=f"permit {ipaddress.ip_network(ip_address, strict=False)}")
        self.structured_config.prefix_lists.append_new(name="PL-WAN-HA-PEER-PREFIXES", sequence_numbers=sequence_numbers)

    def set_as_path_acl_aspath_wan(self: StructuredConfigUtils) -> None:
        """Set as-path access-list ASPATH-WAN."""
        entries = EosCliConfigGen.AsPath.AccessListsItem.Entries()
        entries.append_new(type="permit", match=as_path_list_match_from_bgp_asns((self.shared_utils.bgp_as,)))  # pyright: ignore[reportArgumentType]
        self.structured_config.as_path.access_lists.append_new(name="ASPATH-WAN", entries=entries)

    @run_once_method
    def set_once_ip_extcommunity_list_evpn_soo(self: StructuredConfigUtils) -> None:
        """Set ip extcommunity-list ECL-EVPN-SOO."""
        ip_extcommunity_list = EosCliConfigGen.IpExtcommunityListsItem(name="ECL-EVPN-SOO")
        ip_extcommunity_list.entries.append_new(type="permit", extcommunities=f"soo {self.shared_utils.evpn_soo}")
        self.structured_config.ip_extcommunity_lists.append(ip_extcommunity_list)

    @run_once_method
    def set_once_route_map_mlag_peer_in(self) -> None:
        """
        Set route-map RM-MLAG-PEER-IN.

        Makes routes learned over the MLAG Peer-link less preferred on spines
        to ensure optimal routing by setting origin to incomplete.
        """
        route_map = EosCliConfigGen.RouteMapsItem(name="RM-MLAG-PEER-IN")
        route_map.sequence_numbers.append_new(
            sequence=10,
            type="permit",
            description="Make routes learned over MLAG Peer-link less preferred on spines to ensure optimal routing",
            set=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Set(["origin incomplete"]),
        )
        self.structured_config.route_maps.append(route_map)

    @run_once_method
    def set_once_peer_group_mlag_ipv4_underlay_peer(self) -> None:
        """
        Set router_bgp structured_config covering the MLAG peer_group and associated address_family activations.

        This is called from:
        - MLAG in the case of BGP underlay routing protocol.
        - Network services in the case of iBGP MLAG peering for VRFs

        """
        bgp_peer_group = self.inputs.bgp_peer_groups.mlag_ipv4_underlay_peer
        self.set_mlag_peer_group(bgp_peer_group)
        if not self.shared_utils.underlay_ipv6_numbered:
            self.structured_config.router_bgp.address_family_ipv4.peer_groups.append(
                self.shared_utils.get_mlag_peer_group_address_familiy_ipv4(bgp_peer_group, self.inputs.underlay_rfc5549)
            )
        if self.shared_utils.underlay_ipv6:
            self.structured_config.router_bgp.address_family_ipv6.peer_groups.append_new(name=bgp_peer_group.name, activate=True)

    def set_mlag_peer_group(self, bgp_peer_group: EosDesigns.BgpPeerGroups.MlagIpv4UnderlayPeer | EosDesigns.BgpPeerGroups.MlagIpv4VrfsPeer) -> None:
        """Set structured_config for one MLAG peer_group."""
        router_bgp = self.structured_config.router_bgp
        peer_group_name = bgp_peer_group.name
        peer_group = EosCliConfigGen.RouterBgp.PeerGroupsItem(
            name=peer_group_name,
            remote_as=self.shared_utils.formatted_bgp_as,
            next_hop_self=True,
            description=AvdStringFormatter().format(self.inputs.mlag_bgp_peer_group_description, mlag_peer=self.shared_utils.mlag_peer),
            password=self.shared_utils.get_bgp_password(bgp_peer_group),
            bfd=bgp_peer_group.bfd or None,
            maximum_routes=bgp_peer_group.maximum_routes,
            send_community="all",
        )
        peer_group.metadata.type = "ipv4"

        if bgp_peer_group.structured_config:
            self.custom_structured_configs.nested.router_bgp.peer_groups.obtain(peer_group_name)._deepmerge(
                bgp_peer_group.structured_config, list_merge=self.custom_structured_configs.list_merge_strategy
            )

        if self.shared_utils.node_config.mlag_ibgp_origin_incomplete:
            peer_group.route_map_in = "RM-MLAG-PEER-IN"
            self.set_once_route_map_mlag_peer_in()

        router_bgp.peer_groups.append(peer_group)


__all__ = ["StructuredConfigUtils"]
