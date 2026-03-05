# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServicesProtocol


class ArpMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def arp(self: AvdStructuredConfigNetworkServicesProtocol) -> None:
        """
        Set the structured config for arp.static_entries.

        Consist of static ARP entries defined under the VRFs.
        """
        if not self.shared_utils.network_services_l3:
            return

        for tenant in self.shared_utils.filtered_tenants:
            for vrf in tenant.vrfs:
                # ARP static entries are already filtered inside filtered_tenants
                for arp_entry in vrf.static_arp_entries:
                    arp_static_entry_item = EosCliConfigGen.Arp.StaticEntriesItem(
                        ipv4_address=arp_entry.ipv4_address,
                        vrf=vrf.name,
                        mac_address=arp_entry.mac_address,
                    )
                    self.structured_config.arp.static_entries.append(arp_static_entry_item)
