# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from ipaddress import ip_network
from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._utils.run_once import run_once_method

if TYPE_CHECKING:
    from . import AvdStructuredConfigUnderlayProtocol


class RouteMapsMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    def set_route_map_underlay_filter_peer_as(self: AvdStructuredConfigUnderlayProtocol, asn: str) -> None:
        """Set route-map RM-BGP-AS{{ asn }}-OUT."""
        route_map_name = f"RM-BGP-AS{asn}-OUT"
        sequence_numbers = EosCliConfigGen.RouteMapsItem.SequenceNumbers()
        sequence_numbers.append_new(sequence=10, type="deny", match=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Match([f"as {asn}"]))
        sequence_numbers.append_new(sequence=20, type="permit")
        self.structured_config.route_maps.append_new(name=route_map_name, sequence_numbers=sequence_numbers)

    @run_once_method
    def set_once_route_map_connected_to_bgp(self: AvdStructuredConfigUnderlayProtocol) -> None:
        """
        Set route-map RM-CONN-2-BGP.

        TODO: Split this up into separate functions so it is the calling logic that decides what to add.
        """
        sequence_numbers = EosCliConfigGen.RouteMapsItem.SequenceNumbers()
        if not self.shared_utils.underlay_ipv6_numbered:
            sequence_10 = EosCliConfigGen.RouteMapsItem.SequenceNumbersItem(
                sequence=10,
                type="permit",
                match=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Match(["ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY"]),
            )
            # Create the prefix-list
            self.set_once_prefix_list_loopbacks_evpn_overlay()

            if self.shared_utils.wan_role:
                sequence_10.set = EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Set([f"extcommunity soo {self.shared_utils.evpn_soo} additive"])

            sequence_numbers.append(sequence_10)
            # SEQ 20 is set by inband management if applicable, so avoid setting that here

        if self.shared_utils.underlay_ipv6 is True:
            sequence_numbers.append_new(
                sequence=30,
                type="permit",
                match=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Match(["ipv6 address prefix-list PL-LOOPBACKS-EVPN-OVERLAY-V6"]),
            )
            # Create the prefix-list
            self.set_once_prefix_list_loopbacks_evpn_overlay_v6()

        if self.shared_utils.underlay_multicast_rp_interfaces:
            sequence_numbers.append_new(
                sequence=40,
                type="permit",
                match=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Match(["ip address prefix-list PL-LOOPBACKS-PIM-RP"]),
            )
            # Create the prefix-list
            self.set_once_prefix_list_loopbacks_pim_rp()

        if self.shared_utils.wan_ha and self.shared_utils.use_uplinks_for_wan_ha:
            sequence_numbers.append_new(
                sequence=50,
                type="permit",
                match=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Match(["ip address prefix-list PL-WAN-HA-PREFIXES"]),
            )
            # Create the prefix-list.
            self.set_once_prefix_list_wan_ha_prefixes()

        subnets = []
        for peer in self._avd_peers:
            peer_facts = self.shared_utils.get_peer_facts(peer)
            for uplink in peer_facts.uplinks:
                if (
                    uplink.peer == self.shared_utils.hostname
                    and uplink.type == "underlay_p2p"
                    and uplink.ip_address
                    and "unnumbered" not in uplink.ip_address.lower()
                    and peer_facts.inband_ztp
                ):
                    subnet = str(ip_network(f"{uplink.ip_address}/{uplink.prefix_length}", strict=False))
                    subnets.append(subnet)
        if subnets:
            sequence_numbers.append_new(
                sequence=70,
                type="permit",
                match=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Match(["ip address prefix-list PL-P2P-LINKS"]),
            )
            # Create the prefix-list
            self.set_once_prefix_list_p2p_links(subnets)

        if self.shared_utils.evpn_wan_gateway:
            sequence_numbers.append_new(
                sequence=80, type="permit", match=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Match(["ip address prefix-list PL-DPS-WAN-OVERLAY"])
            )
            # Create the prefix-list
            self.set_once_prefix_list_dps_wan_overlay()

        self.structured_config.route_maps.append_new(name="RM-CONN-2-BGP", sequence_numbers=sequence_numbers)
