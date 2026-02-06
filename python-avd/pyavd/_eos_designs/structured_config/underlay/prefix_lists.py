# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import ipaddress
from ipaddress import collapse_addresses
from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._utils import get_ipv4_networks_from_pool, get_ipv6_networks_from_pool
from pyavd._utils.run_once import run_once_method

if TYPE_CHECKING:
    from . import AvdStructuredConfigUnderlayProtocol


class PrefixListsMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @run_once_method
    def set_once_prefix_list_dps_wan_overlay(self: AvdStructuredConfigUnderlayProtocol) -> None:
        """
        Set prefix-list PL-DPS-WAN-OVERLAY.

        IPv4 - PL-DPS-WAN-OVERLAY - Prefix list distributes DPS VTEPs from WAN to LAN.
        Not bundled with LOOPBACKS prefix list to avoid tagging DPS VTEPs with SOO, to prevent
        DPS VTEPs from being redistributed within WAN overlay directly.
        """
        sequence_numbers_dps = EosCliConfigGen.PrefixListsItem.SequenceNumbers()
        sequence_numbers_dps.append_new(sequence=(len(sequence_numbers_dps) + 1) * 10, action=f"permit {self.shared_utils.vtep_ip}/32 eq 32")
        self.structured_config.prefix_lists.append_new(name="PL-DPS-WAN-OVERLAY", sequence_numbers=sequence_numbers_dps)

    @run_once_method
    def set_once_prefix_list_p2p_links(self: AvdStructuredConfigUnderlayProtocol, subnets: list[str]) -> None:
        """Set prefix-list PL-P2P-LINKS."""
        p2p_links_sequence_numbers = EosCliConfigGen.PrefixListsItem.SequenceNumbers()
        for index, subnet in enumerate(subnets, start=1):
            p2p_links_sequence_numbers.append_new(sequence=index * 10, action=f"permit {subnet}")

        self.structured_config.prefix_lists.append_new(name="PL-P2P-LINKS", sequence_numbers=p2p_links_sequence_numbers)

    @run_once_method
    def set_once_prefix_list_loopbacks_pim_rp(self: AvdStructuredConfigUnderlayProtocol) -> None:
        """Set prefix-list PL-LOOPBACKS-PIM-RP."""
        sequence_numbers = EosCliConfigGen.PrefixListsItem.SequenceNumbers()
        for index, interface in enumerate(self.shared_utils.underlay_multicast_rp_interfaces, start=1):
            sequence_numbers.append_new(sequence=index * 10, action=f"permit {interface.ip_address}")
        self.structured_config.prefix_lists.append_new(name="PL-LOOPBACKS-PIM-RP", sequence_numbers=sequence_numbers)

    @run_once_method
    def set_once_prefix_list_loopbacks_evpn_overlay_v6(self: AvdStructuredConfigUnderlayProtocol) -> None:
        """Set prefix-list PL-LOOPBACKS-EVPN-OVERLAY-V6."""
        sequence_numbers = EosCliConfigGen.Ipv6PrefixListsItem.SequenceNumbers()
        for index, network in enumerate(collapse_addresses(get_ipv6_networks_from_pool(self.shared_utils.loopback_ipv6_pool)), start=1):
            sequence_numbers.append_new(sequence=index * 10, action=f"permit {network} eq {self.inputs.fabric_ip_addressing.loopback.ipv6_prefix_length}")
        if self.shared_utils.overlay_vtep and self.shared_utils.underlay_ipv6_numbered and self.shared_utils.vtep_loopback.lower() != "loopback0":
            for index, network in enumerate(
                collapse_addresses(get_ipv6_networks_from_pool(self.shared_utils.vtep_loopback_ipv6_pool)), start=len(sequence_numbers) + 1
            ):
                sequence_numbers.append_new(sequence=index * 10, action=f"permit {network} eq {self.inputs.fabric_ip_addressing.loopback.ipv6_prefix_length}")
        self.structured_config.ipv6_prefix_lists.append_new(name="PL-LOOPBACKS-EVPN-OVERLAY-V6", sequence_numbers=sequence_numbers)

    @run_once_method
    def set_once_prefix_list_loopbacks_evpn_overlay(self: AvdStructuredConfigUnderlayProtocol) -> None:
        """Set prefix-list PL-LOOPBACKS-EVPN-OVERLAY."""
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

    @run_once_method
    def set_once_prefix_list_wan_ha_prefixes(self: AvdStructuredConfigUnderlayProtocol) -> None:
        """Set prefix-list PL-WAN-HA-PREFIXES."""
        sequence_numbers = EosCliConfigGen.PrefixListsItem.SequenceNumbers()
        for index, ip_address in enumerate(self.shared_utils.wan_ha_ip_addresses, start=1):
            sequence_numbers.append_new(sequence=10 * index, action=f"permit {ipaddress.ip_network(ip_address, strict=False)}")
        self.structured_config.prefix_lists.append_new(name="PL-WAN-HA-PREFIXES", sequence_numbers=sequence_numbers)
