# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""
Structured Config Utils Module.

This module provides utility classes for structured config generation.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.parent_interfaces import ParentInterfacesTracker
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
        self,
        structured_config: EosCliConfigGen,
        custom_structured_configs: StructCfgs,
        inputs: EosDesigns,
        shared_utils: SharedUtilsProtocol,
    ) -> None:
        """Initialize the StructuredConfigUtils with a ParentInterfacesTracker instance and structured config instance."""
        super().__init__()
        self.structured_config = structured_config
        self.custom_structured_configs = custom_structured_configs
        self.inputs = inputs
        self.shared_utils = shared_utils
        """The shared structured config instance to write config into."""
        self.parent_interfaces_tracker = ParentInterfacesTracker()
        """Tracker for parent interfaces that need to be created for subinterfaces."""

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

    def update_router_bgp_with_mlag_peer_group(self) -> None:
        """
        Update router_bgp structured_config covering the MLAG peer_group(s) and associated address_family activations.

        This is called from MLAG in the case of BGP underlay routing protocol.
        In the case of another underlay routing protocol, it may be called from network_services instead in case there are VRFs with iBGP peerings.
        """
        router_bgp = self.structured_config.router_bgp
        shared_utils = self.shared_utils

        # Only create the underlay peer group if the underlay is BGP or if we reuse the same peer-group from network services.
        if shared_utils.underlay_bgp or not shared_utils.use_separate_peer_group_for_mlag_vrfs:
            bgp_peer_group = self.inputs.bgp_peer_groups.mlag_ipv4_underlay_peer
            router_bgp.peer_groups.append(self.get_mlag_peer_group(bgp_peer_group))
            if not shared_utils.underlay_ipv6_numbered:
                router_bgp.address_family_ipv4.peer_groups.append(
                    shared_utils.get_mlag_peer_group_address_familiy_ipv4(bgp_peer_group, self.inputs.underlay_rfc5549)
                )
            if shared_utils.underlay_ipv6:
                router_bgp.address_family_ipv6.peer_groups.append_new(name=bgp_peer_group.name, activate=True)

        if shared_utils.use_separate_peer_group_for_mlag_vrfs:
            bgp_peer_group = self.inputs.bgp_peer_groups.mlag_ipv4_vrfs_peer
            router_bgp.peer_groups.append(self.get_mlag_peer_group(bgp_peer_group))
            router_bgp.address_family_ipv4.peer_groups.append(
                shared_utils.get_mlag_peer_group_address_familiy_ipv4(bgp_peer_group, self.inputs.overlay_mlag_rfc5549)
            )

    def get_mlag_peer_group(
        self, bgp_peer_group: EosDesigns.BgpPeerGroups.MlagIpv4UnderlayPeer | EosDesigns.BgpPeerGroups.MlagIpv4VrfsPeer
    ) -> EosCliConfigGen.RouterBgp.PeerGroupsItem:
        """Return structured_config for one MLAG peer_group."""
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

        return peer_group


__all__ = ["StructuredConfigUtils"]
