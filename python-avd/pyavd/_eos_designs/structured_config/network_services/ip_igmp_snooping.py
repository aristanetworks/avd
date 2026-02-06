# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from ipaddress import AddressValueError, IPv4Address
from typing import TYPE_CHECKING, Protocol, cast, overload

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor
from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._utils import default

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns

    from . import AvdStructuredConfigNetworkServicesProtocol


class IpIgmpSnoopingMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def ip_igmp_snooping(self: AvdStructuredConfigNetworkServicesProtocol) -> None:
        """Set structured config for ip_igmp_snooping."""
        if not self.shared_utils.network_services_l2:
            return

        igmp_snooping_enabled = self.shared_utils.igmp_snooping_enabled
        self.structured_config.ip_igmp_snooping.globally_enabled = igmp_snooping_enabled
        if not igmp_snooping_enabled:
            return

        for tenant in self.shared_utils.filtered_tenants:
            for vrf in tenant.vrfs:
                for svi in vrf.svis:
                    self._set_ip_igmp_snooping_vlan(svi, tenant, vrf)

            for l2vlan in tenant.l2vlans:
                self._set_ip_igmp_snooping_vlan(l2vlan, tenant, vrf=None)

    @overload
    def _set_ip_igmp_snooping_vlan(
        self: AvdStructuredConfigNetworkServicesProtocol,
        vlan: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem.SvisItem,
        tenant: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem,
        vrf: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem,
    ) -> None: ...

    @overload
    def _set_ip_igmp_snooping_vlan(
        self: AvdStructuredConfigNetworkServicesProtocol,
        vlan: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.L2vlansItem,
        tenant: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem,
        vrf: None,
    ) -> None: ...

    def _set_ip_igmp_snooping_vlan(
        self: AvdStructuredConfigNetworkServicesProtocol,
        vlan: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem.SvisItem
        | EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.L2vlansItem,
        tenant: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem,
        vrf: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem | None,
    ) -> None:
        """
        Set ip_igmp_snooping structured_config for one vlan.

        Can be used for both SVIs and L2VLANs

        This function assumes that when a L2vlansItem is passed, the VRF is set to None, and when an SvisItem is passed,
        the VRF is not None.
        """
        igmp_snooping_enabled = None
        igmp_snooping_querier_enabled = None
        evpn_l2_multicast_enabled = bool(default(vlan.evpn_l2_multicast.enabled, tenant.evpn_l2_multicast.enabled)) and self.shared_utils.evpn_multicast
        if self.shared_utils.overlay_vtep and evpn_l2_multicast_enabled:
            # Leaving igmp_snooping_enabled unset, to avoid extra line of config as we already check
            # that global igmp snooping is enabled and igmp snooping is required for evpn_l2_multicast.

            # Forcing querier to True since evpn_l2_multicast requires
            # querier on all vteps
            igmp_snooping_querier_enabled = True

        else:
            igmp_snooping_enabled = vlan.igmp_snooping_enabled
            if self.shared_utils.network_services_l3 and self.shared_utils.uplink_type in ["p2p", "p2p-vrfs"]:
                igmp_snooping_querier_enabled = default(vlan.igmp_snooping_querier.enabled, tenant.igmp_snooping_querier.enabled)

        vlan_item = EosCliConfigGen.IpIgmpSnooping.VlansItem()
        if igmp_snooping_enabled is not None:
            vlan_item.enabled = igmp_snooping_enabled

        if igmp_snooping_querier_enabled is not None:
            vlan_item.querier.enabled = igmp_snooping_querier_enabled
            if igmp_snooping_querier_enabled:
                if vrf is None:
                    vlan = cast("EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.L2vlansItem", vlan)
                    vlan_item.querier.address = self._get_l2vlan_igmp_querier_source_address(vlan, tenant)
                else:  # SVI
                    vlan = cast("EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem.SvisItem", vlan)
                    vlan_item.querier.address = self._get_svi_igmp_querier_source_address(vlan, tenant, vrf)

                vlan_item.querier.version = default(vlan.igmp_snooping_querier.version, tenant.igmp_snooping_querier.version)

        if evpn_l2_multicast_enabled:
            vlan_item.fast_leave = default(vlan.igmp_snooping_querier.fast_leave, tenant.evpn_l2_multicast.fast_leave)

        if vlan_item:
            vlan_item.id = vlan.id
            self.structured_config.ip_igmp_snooping.vlans.append(vlan_item)

    def _get_l2vlan_igmp_querier_source_address(
        self: AvdStructuredConfigNetworkServicesProtocol,
        l2vlan: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.L2vlansItem,
        tenant: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem,
    ) -> str:
        """Return the IGMP snooping querier source address for an L2VLAN."""
        source_address_key = default(l2vlan.igmp_snooping_querier.source_address, tenant.igmp_snooping_querier.source_address)

        source_address = self.shared_utils.router_id if source_address_key in {"main_router_id", "diagnostic_loopback", "vrf_router_id"} else source_address_key
        msg = (
            f"Invalid IGMP snooping querier source address for VLAN '{l2vlan.name}' "
            f"in Tenant '{tenant.name}'. The value '{source_address}' resolved from "
            f"'igmp_snooping_querier.source_address: {source_address_key}' "
            "is not a valid IPv4 address."
        )
        if source_address is not None:
            try:
                IPv4Address(source_address)
            except AddressValueError:
                raise AristaAvdInvalidInputsError(msg) from None
            else:
                return source_address
        raise AristaAvdInvalidInputsError(msg)

    def _get_svi_igmp_querier_source_address(
        self: AvdStructuredConfigNetworkServicesProtocol,
        svi: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem.SvisItem,
        tenant: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem,
        vrf: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem,
    ) -> str:
        """Return the IGMP snooping querier source address for an SVI."""
        source_address_key = default(svi.igmp_snooping_querier.source_address, tenant.igmp_snooping_querier.source_address)

        match source_address_key:
            case "main_router_id":
                source_address = self.shared_utils.router_id
            case "vrf_router_id":
                # Using the BGP router ID configuration.
                source_address = self.get_vrf_router_id(vrf, tenant, vrf.bgp.router_id)
            case "diagnostic_loopback":
                try:
                    source_address = self.get_vrf_router_id(vrf, tenant, source_address_key)
                except AristaAvdInvalidInputsError:
                    # Re-raise with IGMP-specific context
                    msg = (
                        f"Invalid configuration on VRF '{vrf.name}' in Tenant '{tenant.name}'. 'vtep_diagnostic.loopback' along with either "
                        "'vtep_diagnostic.loopback_ip_pools' or 'vtep_diagnostic.loopback_ip_range' must be defined "
                        "when 'igmp_snooping_querier.source_address' is set to 'diagnostic_loopback' on the VRF."
                    )
                    raise AristaAvdInvalidInputsError(msg) from None
            case _:
                source_address = source_address_key

        msg = (
            f"Invalid IGMP snooping querier source address for VLAN '{svi.name}' "
            f"in VRF '{vrf.name}' in Tenant '{tenant.name}'. "
            f"The value '{source_address}' resolved from "
            f"'igmp_snooping_querier.source_address: {source_address_key}' is not a valid IPv4 address."
        )

        if source_address is not None:
            try:
                IPv4Address(source_address)
            except AddressValueError:
                raise AristaAvdInvalidInputsError(msg) from None
            else:
                return source_address

        raise AristaAvdInvalidInputsError(msg)
