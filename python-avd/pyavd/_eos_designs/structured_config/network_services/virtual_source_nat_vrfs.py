# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._utils import get_ip_from_ip_prefix

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServicesProtocol


class VirtualSourceNatVrfsMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    def _set_virtual_source_nat_for_vrf_loopback(
        self: AvdStructuredConfigNetworkServicesProtocol, loopback_interface: EosCliConfigGen.LoopbackInterfacesItem
    ) -> None:
        """
        Set the structured config for virtual_source_nat_vrfs.

        Only used by VTEPs with L2 and L3 services.
        Called from loopback_interfaces while creating each loopback.
        """
        if not (self.shared_utils.overlay_vtep and self.shared_utils.network_services_l2 and self.shared_utils.network_services_l3):
            return

        if (vrf := loopback_interface.vrf) is None:
            return

        # Using append with ignore_fields.
        # It will append the VirtualSourceNatVrfsItem unless the same "name" is already in the list.
        # It will never raise since we only have these two keys.
        virtual_source_nat_vrf = EosCliConfigGen.VirtualSourceNatVrfsItem(
            name=vrf, ip_address=get_ip_from_ip_prefix(loopback_interface.ip_address) if loopback_interface.ip_address else None
        )

        if len(loopback_interface.ipv6_addresses) > 1:
            msg = f"Only one IPv6 address is supported for SVI L3 interfaces in VRF {vrf} for virtual source NAT."
            raise AristaAvdInvalidInputsError(msg)
        if len(loopback_interface.ipv6_addresses) == 1:
            virtual_source_nat_vrf.ipv6_address = get_ip_from_ip_prefix(loopback_interface.ipv6_addresses[0])

        self.structured_config.virtual_source_nat_vrfs.append(virtual_source_nat_vrf, ignore_fields=("ip_address", "ipv6_address"))
