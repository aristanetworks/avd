# Copyright (c) 2023-2026 Arista Networks, Inc.
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
from pyavd._utils import get_ipv4_networks_from_pool, get_ipv6_networks_from_pool
from pyavd._utils.run_once import RunOnceMethodStateHelper, run_once_method

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns
    from pyavd._eos_designs.shared_utils import SharedUtilsProtocol


class StructuredConfigUtils(RunOnceMethodStateHelper):
    """
    Utility class for structured config generation.

    This class holds shared utilities and trackers used across all structured config modules.
    """

    def __init__(
        self,
        structured_config: EosCliConfigGen,
        inputs: EosDesigns,
        shared_utils: SharedUtilsProtocol,
    ) -> None:
        """Initialize the StructuredConfigUtils with a ParentInterfacesTracker instance and structured config instance."""
        super().__init__()
        self.structured_config = structured_config
        self.inputs = inputs
        self.shared_utils = shared_utils
        """The shared structured config instance to write config into."""
        self.parent_interfaces_tracker = ParentInterfacesTracker()
        """Tracker for parent interfaces that need to be created for subinterfaces."""

    @run_once_method
    def set_once_route_map_connected_to_bgp(self: StructuredConfigUtils) -> None:
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

        if self.shared_utils.inband_management_parent_vlans and self.shared_utils.inband_mgmt_vrf is None:
            if self.shared_utils.inband_mgmt_ipv4_parent:
                sequence_numbers.append_new(
                    sequence=20, type="permit", match=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Match(["ip address prefix-list PL-L2LEAF-INBAND-MGMT"])
                )
                self.set_prefix_list_l2leaf_inband_mgmt()
            if self.shared_utils.inband_mgmt_ipv6_parent:
                sequence_numbers.append_new(
                    sequence=60,
                    type="permit",
                    match=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Match(["ipv6 address prefix-list IPv6-PL-L2LEAF-INBAND-MGMT"]),
                )
                self.set_prefix_list_l2leaf_ipv6_inband_mgmt()

        if self.shared_utils.vrf_default_evpn and self.shared_utils.vrf_default_ipv4_subnets:
            # Add subnets to redistribution in default VRF
            sequence_30 = EosCliConfigGen.RouteMapsItem.SequenceNumbersItem(
                sequence=30, type="permit", match=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Match(["ip address prefix-list PL-SVI-VRF-DEFAULT"])
            )
            # Create prefix-list
            self.set_once_prefix_list_svi_vrf_default()

            if self.shared_utils.wan_role:
                sequence_30.set = EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Set([f"extcommunity soo {self.shared_utils.evpn_soo} additive"])

            sequence_numbers.append(sequence_30)

        subnets = []
        for peer in self.shared_utils.switch_facts.downlink_switches:
            peer_facts = self.shared_utils.get_peer_facts(peer)
            for uplink in peer_facts.uplinks:
                if (
                    uplink.peer == self.shared_utils.hostname
                    and uplink.type == "underlay_p2p"
                    and uplink.ip_address
                    and "unnumbered" not in uplink.ip_address.lower()
                    and peer_facts.inband_ztp
                ):
                    subnet = str(ipaddress.ip_network(f"{uplink.ip_address}/{uplink.prefix_length}", strict=False))
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

    def set_once_prefix_list_loopbacks_evpn_overlay_v6(self: StructuredConfigUtils) -> None:
        """Set prefix-list PL-LOOPBACKS-EVPN-OVERLAY-V6."""
        sequence_numbers = EosCliConfigGen.Ipv6PrefixListsItem.SequenceNumbers()
        for index, network in enumerate(ipaddress.collapse_addresses(get_ipv6_networks_from_pool(self.shared_utils.loopback_ipv6_pool)), start=1):
            sequence_numbers.append_new(sequence=index * 10, action=f"permit {network} eq {self.inputs.fabric_ip_addressing.loopback.ipv6_prefix_length}")
        if self.shared_utils.overlay_vtep and self.shared_utils.underlay_ipv6_numbered and self.shared_utils.vtep_loopback.lower() != "loopback0":
            for index, network in enumerate(
                ipaddress.collapse_addresses(get_ipv6_networks_from_pool(self.shared_utils.vtep_loopback_ipv6_pool)), start=len(sequence_numbers) + 1
            ):
                sequence_numbers.append_new(sequence=index * 10, action=f"permit {network} eq {self.inputs.fabric_ip_addressing.loopback.ipv6_prefix_length}")
        self.structured_config.ipv6_prefix_lists.append_new(name="PL-LOOPBACKS-EVPN-OVERLAY-V6", sequence_numbers=sequence_numbers)

    def set_once_prefix_list_loopbacks_evpn_overlay(self: StructuredConfigUtils) -> None:
        """Set prefix-list PL-LOOPBACKS-EVPN-OVERLAY."""
        sequence_numbers = EosCliConfigGen.PrefixListsItem.SequenceNumbers()
        for index, network in enumerate(ipaddress.collapse_addresses(get_ipv4_networks_from_pool(self.shared_utils.loopback_ipv4_pool)), start=1):
            sequence_numbers.append_new(sequence=index * 10, action=f"permit {network} eq 32")

        if self.shared_utils.overlay_vtep and self.shared_utils.vtep_loopback.lower() != "loopback0" and not self.shared_utils.is_wan_router:
            for index, network in enumerate(
                ipaddress.collapse_addresses(get_ipv4_networks_from_pool(self.shared_utils.vtep_loopback_ipv4_pool)), start=len(sequence_numbers) + 1
            ):
                sequence_numbers.append_new(sequence=index * 10, action=f"permit {network} eq 32")

        if self.inputs.vtep_vvtep_ip is not None and self.shared_utils.network_services_l3 is True and not self.shared_utils.is_wan_router:
            sequence_numbers.append_new(sequence=(len(sequence_numbers) + 1) * 10, action=f"permit {self.inputs.vtep_vvtep_ip}")

        self.structured_config.prefix_lists.append_new(name="PL-LOOPBACKS-EVPN-OVERLAY", sequence_numbers=sequence_numbers)

    def set_once_prefix_list_loopbacks_pim_rp(self: StructuredConfigUtils) -> None:
        """Set prefix-list PL-LOOPBACKS-PIM-RP."""
        sequence_numbers = EosCliConfigGen.PrefixListsItem.SequenceNumbers()
        for index, interface in enumerate(self.shared_utils.underlay_multicast_rp_interfaces, start=1):
            sequence_numbers.append_new(sequence=index * 10, action=f"permit {interface.ip_address}")
        self.structured_config.prefix_lists.append_new(name="PL-LOOPBACKS-PIM-RP", sequence_numbers=sequence_numbers)

    def set_once_prefix_list_wan_ha_prefixes(self: StructuredConfigUtils) -> None:
        """Set prefix-list PL-WAN-HA-PREFIXES."""
        sequence_numbers = EosCliConfigGen.PrefixListsItem.SequenceNumbers()
        for index, ip_address in enumerate(self.shared_utils.wan_ha_ip_addresses, start=1):
            sequence_numbers.append_new(sequence=10 * index, action=f"permit {ipaddress.ip_network(ip_address, strict=False)}")
        self.structured_config.prefix_lists.append_new(name="PL-WAN-HA-PREFIXES", sequence_numbers=sequence_numbers)

    def set_once_prefix_list_p2p_links(self: StructuredConfigUtils, subnets: list[str]) -> None:
        """Set prefix-list PL-P2P-LINKS."""
        p2p_links_sequence_numbers = EosCliConfigGen.PrefixListsItem.SequenceNumbers()
        for index, subnet in enumerate(subnets, start=1):
            p2p_links_sequence_numbers.append_new(sequence=index * 10, action=f"permit {subnet}")

        self.structured_config.prefix_lists.append_new(name="PL-P2P-LINKS", sequence_numbers=p2p_links_sequence_numbers)

    def set_once_prefix_list_dps_wan_overlay(self: StructuredConfigUtils) -> None:
        """
        Set prefix-list PL-DPS-WAN-OVERLAY.

        IPv4 - PL-DPS-WAN-OVERLAY - Prefix list distributes DPS VTEPs from WAN to LAN.
        Not bundled with LOOPBACKS prefix list to avoid tagging DPS VTEPs with SOO, to prevent
        DPS VTEPs from being redistributed within WAN overlay directly.
        """
        sequence_numbers_dps = EosCliConfigGen.PrefixListsItem.SequenceNumbers()
        sequence_numbers_dps.append_new(sequence=(len(sequence_numbers_dps) + 1) * 10, action=f"permit {self.shared_utils.vtep_ip}/32 eq 32")
        self.structured_config.prefix_lists.append_new(name="PL-DPS-WAN-OVERLAY", sequence_numbers=sequence_numbers_dps)

    def set_prefix_list_l2leaf_inband_mgmt(self: StructuredConfigUtils) -> None:
        """Set prefix list PL-L2LEAF-INBAND-MGMT."""
        sequence_numbers = EosCliConfigGen.PrefixListsItem.SequenceNumbers()
        for index, subnet in enumerate(self.shared_utils.inband_management_parent_vlans.values(), start=1):
            sequence_numbers.append_new(sequence=(index) * 10, action=f"permit {subnet['ipv4']}")

        self.structured_config.prefix_lists.append_new(name="PL-L2LEAF-INBAND-MGMT", sequence_numbers=sequence_numbers)

    def set_prefix_list_l2leaf_ipv6_inband_mgmt(self: StructuredConfigUtils) -> None:
        """Set prefix list IPv6-PL-L2LEAF-INBAND-MGMT."""
        sequence_numbers = EosCliConfigGen.Ipv6PrefixListsItem.SequenceNumbers()
        for index, subnet in enumerate(self.shared_utils.inband_management_parent_vlans.values(), start=1):
            sequence_numbers.append_new(sequence=(index) * 10, action=f"permit {subnet['ipv6']}")

        self.structured_config.ipv6_prefix_lists.append_new(name="IPv6-PL-L2LEAF-INBAND-MGMT", sequence_numbers=sequence_numbers)

    @run_once_method
    def set_once_prefix_list_svi_vrf_default(self: StructuredConfigUtils) -> None:
        """Set prefix-list PL-SVI-VRF-DEFAULT."""
        sequence_numbers = EosCliConfigGen.PrefixListsItem.SequenceNumbers()
        for index, subnet in enumerate(self.shared_utils.vrf_default_ipv4_subnets, start=1):
            sequence_numbers.append_new(sequence=index * 10, action=f"permit {subnet}")
        self.structured_config.prefix_lists.append_new(name="PL-SVI-VRF-DEFAULT", sequence_numbers=sequence_numbers)


__all__ = ["StructuredConfigUtils"]
