# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns

    from . import AvdStructuredConfigNetworkServicesProtocol


class RouterOspfv3Mixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def router_ospfv3(self: AvdStructuredConfigNetworkServicesProtocol) -> None:
        """Set structured config for router_ospfv3."""
        if not self.shared_utils.network_services_l3:
            return

        for tenant in self.shared_utils.filtered_tenants:
            for vrf in tenant.vrfs:
                if not vrf.ospfv3.enabled or (vrf.ospfv3.nodes and self.shared_utils.hostname not in vrf.ospfv3.nodes):
                    continue

                vrf_config = EosCliConfigGen.RouterOspfv3.VrfsItem(
                    name=vrf.name,
                    router_id=self.get_protocol_vrf_router_id(vrf, tenant, vrf.ospfv3.router_id),
                    passive_interface_default=vrf.ospfv3.passive_interface_default,
                )

                self._update_ospfv3_redistribute(vrf_config, vrf)

                self.structured_config.router_ospfv3.vrfs.append(vrf_config)

    def _update_ospfv3_redistribute(
        self: AvdStructuredConfigNetworkServicesProtocol,
        vrf_config: EosCliConfigGen.RouterOspfv3.VrfsItem,
        vrf: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem,
    ) -> None:
        """Populate address family and redistribution settings on the given OSPFv3 VRF config."""
        ospfv3 = vrf.ospfv3

        if ospfv3.address_family_ipv4.enabled:
            af_ipv4 = EosCliConfigGen.RouterOspfv3.VrfsItem.AddressFamilyIpv4(enabled=True)
            if ospfv3.address_family_ipv4.redistribute_bgp.enabled:
                af_ipv4.redistribute.bgp.enabled = True
                if ospfv3.address_family_ipv4.redistribute_bgp.route_map:
                    af_ipv4.redistribute.bgp.route_map = ospfv3.address_family_ipv4.redistribute_bgp.route_map
            if ospfv3.address_family_ipv4.redistribute_connected and ospfv3.address_family_ipv4.redistribute_connected.enabled:
                af_ipv4.redistribute.connected.enabled = True
                if ospfv3.address_family_ipv4.redistribute_connected.route_map:
                    af_ipv4.redistribute.connected.route_map = ospfv3.address_family_ipv4.redistribute_connected.route_map
            if ospfv3.address_family_ipv4.redistribute_static and ospfv3.address_family_ipv4.redistribute_static.enabled:
                af_ipv4.redistribute.static.enabled = True
                if ospfv3.address_family_ipv4.redistribute_static.route_map:
                    af_ipv4.redistribute.static.route_map = ospfv3.address_family_ipv4.redistribute_static.route_map
            vrf_config.address_family_ipv4 = af_ipv4

        if ospfv3.address_family_ipv6.enabled:
            af_ipv6 = EosCliConfigGen.RouterOspfv3.VrfsItem.AddressFamilyIpv6(enabled=True)
            if ospfv3.address_family_ipv6.redistribute_bgp.enabled:
                af_ipv6.redistribute.bgp.enabled = True
                if ospfv3.address_family_ipv6.redistribute_bgp.route_map:
                    af_ipv6.redistribute.bgp.route_map = ospfv3.address_family_ipv6.redistribute_bgp.route_map
            if ospfv3.address_family_ipv6.redistribute_connected.enabled:
                af_ipv6.redistribute.connected.enabled = True
                if ospfv3.address_family_ipv6.redistribute_connected.route_map:
                    af_ipv6.redistribute.connected.route_map = ospfv3.address_family_ipv6.redistribute_connected.route_map
            if ospfv3.address_family_ipv6.redistribute_static.enabled:
                af_ipv6.redistribute.static.enabled = True
                if ospfv3.address_family_ipv6.redistribute_static.route_map:
                    af_ipv6.redistribute.static.route_map = ospfv3.address_family_ipv6.redistribute_static.route_map
            vrf_config.address_family_ipv6 = af_ipv6
