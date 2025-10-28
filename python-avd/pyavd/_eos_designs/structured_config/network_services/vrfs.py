# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns

    from . import AvdStructuredConfigNetworkServicesProtocol


class VrfsMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def vrfs(self: AvdStructuredConfigNetworkServicesProtocol) -> None:
        """
        Return structured config for vrfs.

        Used for creating VRFs except VRF "default".

        This function also detects duplicate vrfs and raise an error in case of duplicates between
        all Tenants deployed on this device.
        """
        if not self.shared_utils.network_services_l3:
            self._set_l2_device_inband_mgmt_vrf()
            return

        for tenant in self.shared_utils.filtered_tenants:
            for vrf in tenant.vrfs:
                vrf_name = vrf.name
                if vrf_name == "default":
                    continue
                new_vrf = EosCliConfigGen.VrfsItem(name=vrf_name, tenant=tenant.name)

                # MLAG IBGP Peering VLANs per VRF
                if self.inputs.overlay_mlag_rfc5549 and self._mlag_ibgp_peering_enabled(vrf, tenant):
                    new_vrf._update(ip_routing_ipv6_interfaces=True, ipv6_routing=True)
                new_vrf.ip_routing = True

                if self._has_ipv6(vrf):
                    new_vrf.ipv6_routing = True

                if vrf.description:
                    new_vrf.description = vrf.description
                self.structured_config.vrfs.append(new_vrf, ignore_fields=("tenant",))

    def _set_l2_device_inband_mgmt_vrf(self: AvdStructuredConfigNetworkServicesProtocol) -> None:
        """
        On devices without l3 services, there may be the inband mgmt VRF to configure.

        For other devices the VRF is injected in the filtered tenants by AVD.
        """
        if (self.shared_utils.configure_inband_mgmt or self.shared_utils.configure_inband_mgmt_ipv6) and (
            vrf := self.shared_utils.filtered_mgmt_inband_vrf
        ) is not None:
            if vrf.name == "default":
                return
            tenant_name = self.shared_utils.filtered_mgmt_inband_tenant.name if self.shared_utils.filtered_mgmt_inband_tenant is not None else "inband_mgmt"
            new_vrf = EosCliConfigGen.VrfsItem(name=vrf.name, tenant=tenant_name)
            if vrf.description:
                new_vrf.description = vrf.description
            self.structured_config.vrfs.append(new_vrf, ignore_fields=("metadata",))

    def _has_ipv6(
        self: AvdStructuredConfigNetworkServicesProtocol, vrf: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem
    ) -> bool:
        """
        Return bool if IPv6 is configured in the given VRF.

        Expects a VRF definition coming from filtered_tenants, where all keys have been set and filtered
        """
        return any(svi.ipv6_address or svi.ipv6_address_virtuals for svi in vrf.svis)
