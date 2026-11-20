# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._utils.get_ip_from_ip_prefix import get_ip_from_ip_prefix

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServicesProtocol


class VirtualSourceNatVrfsMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    def _set_virtual_source_nat_for_vrf_loopback(
        self: AvdStructuredConfigNetworkServicesProtocol,
        vrf: str | None,
        ipv4_address: str | None = None,
        ipv6_address: str | None = None,
        *,
        fill_missing_ipv6: bool = False,
    ) -> None:
        """
        Set the structured config for virtual_source_nat_vrfs.

        Only used by VTEPs with L2 and L3 services.
        Called from loopback_interfaces while creating each loopback.
        """
        if not (self.shared_utils.overlay_vtep and self.shared_utils.network_services_l2 and self.shared_utils.network_services_l3):
            return

        if vrf is None:
            return

        ipv4 = get_ip_from_ip_prefix(ipv4_address) if ipv4_address else None
        ipv6 = get_ip_from_ip_prefix(ipv6_address) if ipv6_address else None

        # Using append with ignore_fields.
        # It will append the VirtualSourceNatVrfsItem unless the same "name" is already in the list.
        # It will never raise since we only have these two keys.
        self.structured_config.virtual_source_nat_vrfs.append(
            EosCliConfigGen.VirtualSourceNatVrfsItem(
                name=vrf,
                ip_address=ipv4,
                ipv6_address=ipv6,
            ),
            ignore_fields=("ip_address", "ipv6_address"),
        )

        # With the future knob, any loopback may set a missing IPv4 or IPv6 address.
        # Without it, only tenant loopbacks may set a missing IPv6 address, to preserve the configuration for existing inputs.
        fix_address_families = self.inputs.avd_design_future.fix_virtual_source_nat_address_families
        if not (fix_address_families or fill_missing_ipv6):
            return

        virtual_source_nat_vrf = self.structured_config.virtual_source_nat_vrfs[vrf]
        if fix_address_families and ipv4 and not virtual_source_nat_vrf.ip_address:
            virtual_source_nat_vrf.ip_address = ipv4
        if ipv6 and not virtual_source_nat_vrf.ipv6_address:
            virtual_source_nat_vrf.ipv6_address = ipv6
