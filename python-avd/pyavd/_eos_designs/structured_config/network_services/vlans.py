# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor
from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._utils import AvdStringFormatter
from pyavd.j2filters import list_compress, natural_sort

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns

    from . import AvdStructuredConfigNetworkServicesProtocol


class VlansMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def vlans(self: AvdStructuredConfigNetworkServicesProtocol) -> None:
        """
        Return structured config for vlans.

        Consist of svis, mlag peering vlans and l2vlans from filtered tenants.

        This function also detects duplicate vlans and raise an error in case of duplicates between
        SVIs in all VRFs and L2VLANs deployed on this device.
        """
        if not self.shared_utils.network_services_l2:
            return

        all_primary_vlans: set[int] = set()
        for tenant in self.shared_utils.filtered_tenants:
            for vrf in tenant.vrfs:
                for svi in vrf.svis:
                    self.structured_config.vlans.append(self._get_vlan_config(svi, tenant), ignore_fields=("tenant",))

                # MLAG IBGP Peering VLANs per VRF
                # Continue to next VRF if mlag vlan_id is not set
                if (vlan_id := self._mlag_ibgp_peering_vlan_vrf(vrf, tenant)) is None:
                    continue

                vlan = EosCliConfigGen.VlansItem(
                    id=vlan_id,
                    name=AvdStringFormatter().format(self.inputs.mlag_peer_l3_vrf_vlan_name, mlag_peer=self.shared_utils.mlag_peer, vlan=vlan_id, vrf=vrf.name),
                    trunk_groups=EosCliConfigGen.VlansItem.TrunkGroups([self.inputs.trunk_groups.mlag_l3.name]),
                    tenant=tenant.name,
                )
                self.structured_config.vlans.append(vlan, ignore_fields=("tenant",))

            # L2 Vlans per Tenant
            for l2vlan in tenant.l2vlans:
                vlan = self._get_vlan_config(l2vlan, tenant)

                if l2vlan.private_vlan:
                    if not self.shared_utils.platform_settings.feature_support.private_vlan:
                        msg = (
                            "The private VLAN feature is not enabled by default for this platform."
                            " It can be enabled in the platform settings, but might need additional configurations to work."
                        )
                        raise AristaAvdInvalidInputsError(msg)

                    all_primary_vlans.add(l2vlan.private_vlan.primary_vlan)
                    vlan.private_vlan._update(type=l2vlan.private_vlan.type, primary_vlan=l2vlan.private_vlan.primary_vlan)

                self.structured_config.vlans.append(vlan, ignore_fields=("tenant",))

        # Check that all referenced primary vlans exist
        if not all_primary_vlans.issubset(self.structured_config.vlans.keys()):
            missing_vlans = list_compress(list(all_primary_vlans.difference(self.structured_config.vlans.keys())))
            msg = (
                f"The primary VLANs '{missing_vlans}' referenced in a private_vlan definition, "
                "do not exist. The primary VLANs must be defined under 'l2vlans' or 'svis'."
            )
            raise AristaAvdInvalidInputsError(msg)

    def _get_vlan_config(
        self: AvdStructuredConfigNetworkServicesProtocol,
        vlan: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem.SvisItem
        | EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.L2vlansItem,
        tenant: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem,
    ) -> EosCliConfigGen.VlansItem:
        """
        Return structured config for one given vlan.

        Can be used for svis and l2vlans
        """
        vlans_vlan = EosCliConfigGen.VlansItem(
            id=vlan.id,
            name=vlan.name,
            tenant=tenant.name,
        )
        if vlan.address_locking.ipv4:
            if self.inputs.address_locking_settings.dhcp_servers_ipv4 or self.inputs.address_locking_settings.locked_address.ipv4_enforcement_disabled:
                vlans_vlan.address_locking.address_family.ipv4 = vlan.address_locking.ipv4
            else:
                msg = (
                    f"To configure address locking ipv4 for vlan {vlan.id} in Tenant '{tenant.name}' either `address_locking_settings.dhcp_servers_ipv4` "
                    "or `address_locking_settings.locked_address.ipv4_enforcement_disabled` is required."
                )
                raise AristaAvdInvalidInputsError(msg)
        if vlan.address_locking.ipv6:
            if self.inputs.address_locking_settings.dhcp_servers_ipv4 or self.inputs.address_locking_settings.locked_address.ipv6_enforcement_disabled:
                vlans_vlan.address_locking.address_family.ipv6 = vlan.address_locking.ipv6
            else:
                msg = (
                    f"To configure address locking ipv6 for vlan {vlan.id} in Tenant '{tenant.name}' either `address_locking_settings.dhcp_servers_ipv4` "
                    "or `address_locking_settings.locked_address.ipv6_enforcement_disabled` is required."
                )
                raise AristaAvdInvalidInputsError(msg)
        if self.inputs.enable_trunk_groups:
            trunk_groups = vlan.trunk_groups
            if self.shared_utils.only_local_vlan_trunk_groups:
                trunk_groups = list(self._local_endpoint_trunk_groups.intersection(trunk_groups))
            if self.shared_utils.mlag:
                trunk_groups.append(self.inputs.trunk_groups.mlag.name)
            if self.shared_utils.uplink_type == "port-channel":
                trunk_groups.append(self.inputs.trunk_groups.uplink.name)
            vlans_vlan.trunk_groups.extend(natural_sort(trunk_groups))

        return vlans_vlan
