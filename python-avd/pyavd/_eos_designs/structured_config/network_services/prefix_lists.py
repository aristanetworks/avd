# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from ipaddress import IPv4Network
from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor
from pyavd.j2filters import natural_sort

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServicesProtocol


class PrefixListsMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def prefix_lists(self: AvdStructuredConfigNetworkServicesProtocol) -> None:
        """
        Set the structured config for prefix_lists.

        Covers EVPN services in VRF "default" and redistribution of connected to BGP
        """
        # Set prefix-lists from EVPN services in VRF "default" (if any)
        self._set_prefix_lists_vrf_default()

        # Add prefix-list for VRFs where MLAG iBGP peering should not be redistributed
        if mlag_prefixes := self._mlag_ibgp_peering_subnets_without_redistribution:
            sequence_numbers = EosCliConfigGen.PrefixListsItem.SequenceNumbers()
            for index, mlag_prefix in enumerate(mlag_prefixes, start=1):
                sequence_numbers.append_new(sequence=index * 10, action=f"permit {mlag_prefix}")

            self.structured_config.prefix_lists.append_new(name="PL-MLAG-PEER-VRFS", sequence_numbers=sequence_numbers)

    def _set_prefix_lists_vrf_default(self: AvdStructuredConfigNetworkServicesProtocol) -> None:
        """Set the prefix_lists for EVPN services in VRF "default"."""
        if not self._vrf_default_evpn:
            return

        if subnets := self._vrf_default_ipv4_subnets:
            sequence_numbers = EosCliConfigGen.PrefixListsItem.SequenceNumbers()
            for index, subnet in enumerate(subnets, start=1):
                sequence_numbers.append_new(sequence=index * 10, action=f"permit {subnet}")
            self.structured_config.prefix_lists.append_new(name="PL-SVI-VRF-DEFAULT", sequence_numbers=sequence_numbers)

        if static_routes := self._vrf_default_ipv4_static_routes["static_routes"]:
            sequence_numbers = EosCliConfigGen.PrefixListsItem.SequenceNumbers()
            for index, static_route in enumerate(static_routes, start=1):
                sequence_numbers.append_new(sequence=index * 10, action=f"permit {static_route}")
            self.structured_config.prefix_lists.append_new(name="PL-STATIC-VRF-DEFAULT", sequence_numbers=sequence_numbers)

    @cached_property
    def _mlag_ibgp_peering_subnets_without_redistribution(self: AvdStructuredConfigNetworkServicesProtocol) -> list:
        """Return sorted list of MLAG peerings for VRFs where MLAG iBGP peering should not be redistributed."""
        mlag_prefixes = set()
        for tenant in self.shared_utils.filtered_tenants:
            for vrf in tenant.vrfs:
                if self._mlag_ibgp_peering_vlan_vrf(vrf, tenant) is None:
                    continue

                if not self._exclude_mlag_ibgp_peering_from_redistribute(vrf, tenant):
                    # By default the BGP peering is redistributed, so we only need the prefix-list for the false case.
                    continue

                if (mlag_ip_address := self._get_vlan_ip_config_for_mlag_peering(vrf).get("ip_address")) is None:
                    # No MLAG prefix for this VRF (could be RFC5549)
                    continue

                # Convert mlag_ip_address to network prefix string and add to set.
                mlag_prefixes.add(str(IPv4Network(mlag_ip_address, strict=False)))

        return natural_sort(mlag_prefixes)
