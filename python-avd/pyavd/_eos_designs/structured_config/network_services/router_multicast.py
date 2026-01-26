# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServicesProtocol


class RouterMulticastMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def router_multicast(self: AvdStructuredConfigNetworkServicesProtocol) -> None:
        """
        Set the structured config for router_multicast.

        Used to enable multicast routing on the VRF.
        """
        if not self.shared_utils.network_services_l3:
            return

        for tenant in self.shared_utils.filtered_tenants:
            for vrf in tenant.vrfs:
                # Get the evpn_l3_multicast_enabled value which can be True, False, or None
                evpn_l3_multicast_enabled = getattr(vrf._internal_data, "evpn_l3_multicast_enabled", None)

                # Always create a VRF object to detect conflicts via _combine
                # But only set routing=True when evpn_l3_multicast_enabled is True
                if evpn_l3_multicast_enabled is True:
                    router_multicast_vrf = EosCliConfigGen.RouterMulticast.VrfsItem(
                        name=vrf.name, ipv4=EosCliConfigGen.RouterMulticast.VrfsItem.Ipv4(routing=True)
                    )
                elif evpn_l3_multicast_enabled is False:
                    # Create with routing=False to detect conflicts
                    router_multicast_vrf = EosCliConfigGen.RouterMulticast.VrfsItem(
                        name=vrf.name, ipv4=EosCliConfigGen.RouterMulticast.VrfsItem.Ipv4(routing=False)
                    )
                else:
                    # evpn_l3_multicast_enabled is None, skip this VRF
                    continue

                maybe_existing_vrf = self.structured_config.router_multicast.vrfs.obtain(vrf.name)
                maybe_existing_vrf._combine(router_multicast_vrf)

        # Post-processing: Remove VRFs where routing is not True
        # This ensures we only render VRFs with multicast enabled, but conflicts are detected above
        vrfs_to_remove = [vrf_name for vrf_name, vrf in self.structured_config.router_multicast.vrfs.items() if getattr(vrf.ipv4, "routing", None) is not True]
        for vrf_name in vrfs_to_remove:
            del self.structured_config.router_multicast.vrfs[vrf_name]
