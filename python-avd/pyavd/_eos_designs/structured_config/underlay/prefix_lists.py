# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import ipaddress
from ipaddress import collapse_addresses, ip_network
from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor
from pyavd._utils import get_ipv4_networks_from_pool, get_ipv6_networks_from_pool

if TYPE_CHECKING:
    from . import AvdStructuredConfigUnderlayProtocol


class PrefixListsMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def prefix_lists(self: AvdStructuredConfigUnderlayProtocol) -> None:
        """Set the structured config for prefix_lists."""
        if not self.inputs.underlay_filter_redistribute_connected:
            return

        if not self.shared_utils.is_wan_router and (not self.shared_utils.underlay_bgp or self.shared_utils.overlay_routing_protocol == "none"):
            return

        # IPv4 - PL-LOOPBACKS-EVPN-OVERLAY
        sequence_numbers = EosCliConfigGen.PrefixListsItem.SequenceNumbers()
        for index, network in enumerate(collapse_addresses(get_ipv4_networks_from_pool(self.shared_utils.loopback_ipv4_pool)), start=1):
            sequence_numbers.append_new(sequence=index * 10, action=f"permit {network} eq 32")

        if self.shared_utils.overlay_vtep and self.shared_utils.vtep_loopback.lower() != "loopback0" and not self.shared_utils.is_wan_router:
            for index, network in enumerate(
                collapse_addresses(get_ipv4_networks_from_pool(self.shared_utils.vtep_loopback_ipv4_pool)), start=len(sequence_numbers) + 1
            ):
                sequence_numbers.append_new(sequence=index * 10, action=f"permit {network} eq 32")

        if self.inputs.vtep_vvtep_ip is not None and self.shared_utils.network_services_l3 is True and not self.shared_utils.is_wan_router:
            sequence_numbers.append_new(sequence=(len(sequence_numbers) + 1) * 10, action=f"permit {self.inputs.vtep_vvtep_ip}")

        self.structured_config.prefix_lists.append_new(name="PL-LOOPBACKS-EVPN-OVERLAY", sequence_numbers=sequence_numbers)

        if self.shared_utils.underlay_multicast_rp_interfaces is not None:
            sequence_numbers = EosCliConfigGen.PrefixListsItem.SequenceNumbers()
            for index, interface in enumerate(self.shared_utils.underlay_multicast_rp_interfaces, start=1):
                sequence_numbers.append_new(sequence=index * 10, action=f"permit {interface.ip_address}")
            self.structured_config.prefix_lists.append_new(name="PL-LOOPBACKS-PIM-RP", sequence_numbers=sequence_numbers)

        # For now only configure it with eBGP towards LAN.
        if self.shared_utils.wan_ha and self.shared_utils.use_uplinks_for_wan_ha and self.shared_utils.underlay_routing_protocol == "ebgp":
            if self.shared_utils.wan_ha_ip_addresses:
                sequence_numbers = EosCliConfigGen.PrefixListsItem.SequenceNumbers()
                for index, ip_address in enumerate(self.shared_utils.wan_ha_ip_addresses, start=1):
                    sequence_numbers.append_new(sequence=10 * index, action=f"permit {ipaddress.ip_network(ip_address, strict=False)}")
                self.structured_config.prefix_lists.append_new(name="PL-WAN-HA-PREFIXES", sequence_numbers=sequence_numbers)
            if self.shared_utils.wan_ha_peer_ip_addresses:
                sequence_numbers = EosCliConfigGen.PrefixListsItem.SequenceNumbers()
                for index, ip_address in enumerate(self.shared_utils.wan_ha_peer_ip_addresses, start=1):
                    sequence_numbers.append_new(sequence=10 * index, action=f"permit {ipaddress.ip_network(ip_address, strict=False)}")
                self.structured_config.prefix_lists.append_new(name="PL-WAN-HA-PEER-PREFIXES", sequence_numbers=sequence_numbers)

        # P2P-LINKS needed for L3 inband ZTP
        sequence_number = 0
        p2p_links_sequence_numbers = EosCliConfigGen.PrefixListsItem.SequenceNumbers()
        for peer in self._avd_peers:
            peer_facts = self.shared_utils.get_peer_facts(peer)
            for uplink in peer_facts.uplinks:
                if (
                    uplink.peer == self.shared_utils.hostname
                    and uplink.type == "underlay_p2p"
                    and uplink.ip_address
                    and "unnumbered" not in uplink.ip_address
                    and peer_facts.inband_ztp
                ):
                    sequence_number += 10
                    subnet = str(ip_network(f"{uplink.ip_address}/{uplink.prefix_length}", strict=False))
                    p2p_links_sequence_numbers.append_new(sequence=sequence_number, action=f"permit {subnet}")
        if p2p_links_sequence_numbers:
            self.structured_config.prefix_lists.append_new(name="PL-P2P-LINKS", sequence_numbers=p2p_links_sequence_numbers)

    @structured_config_contributor
    def ipv6_prefix_lists(self: AvdStructuredConfigUnderlayProtocol) -> None:
        """Set the structured config for IPv6 prefix_lists."""
        if not self.inputs.underlay_filter_redistribute_connected:
            return

        # TODO: For now there is no support for IPv6 for WAN but this may need to be aligned.
        if not self.shared_utils.underlay_bgp or not self.shared_utils.underlay_ipv6:
            return

        if self.shared_utils.overlay_routing_protocol == "none" and not self.shared_utils.is_wan_router:
            return

        # IPv6 - PL-LOOPBACKS-EVPN-OVERLAY-V6
        sequence_numbers = EosCliConfigGen.Ipv6PrefixListsItem.SequenceNumbers()
        for index, network in enumerate(collapse_addresses(get_ipv6_networks_from_pool(self.shared_utils.loopback_ipv6_pool)), start=1):
            sequence_numbers.append_new(sequence=index * 10, action=f"permit {network} eq 128")
        self.structured_config.ipv6_prefix_lists.append_new(name="PL-LOOPBACKS-EVPN-OVERLAY-V6", sequence_numbers=sequence_numbers)
