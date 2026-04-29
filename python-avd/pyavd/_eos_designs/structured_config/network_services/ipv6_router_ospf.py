# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor
from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._utils import default

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns

    from . import AvdStructuredConfigNetworkServicesProtocol


class Ipv6RouterOspfMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def ipv6_router_ospf(self: AvdStructuredConfigNetworkServicesProtocol) -> None:
        """
        Set structured config for ipv6_router_ospf.

        If we have static_routes in default VRF and not EPVN, and underlay is OSPF
        Then add redistribute static to the underlay OSPFv3 process.
        """
        if not self.shared_utils.network_services_l3:
            return

        for tenant in self.shared_utils.filtered_tenants:
            for vrf in tenant.vrfs:
                if not vrf.ipv6_ospf.enabled or (vrf.ipv6_ospf.nodes and self.shared_utils.hostname not in vrf.ipv6_ospf.nodes):
                    continue

                process_id = default(vrf.ipv6_ospf.process_id, vrf.vrf_id)
                if not process_id:
                    msg = f"Missing or invalid 'ipv6_ospf.process_id' or 'vrf_id' under vrf '{vrf.name}"
                    raise AristaAvdInvalidInputsError(msg)

                process = EosCliConfigGen.Ipv6RouterOspf.ProcessIdsItem(
                    id=process_id,
                    router_id=self.get_protocol_vrf_router_id(vrf, tenant, vrf.ipv6_ospf.router_id),
                    auto_cost_reference_bandwidth=vrf.ipv6_ospf.auto_cost_reference_bandwidth,
                )

                if vrf.ipv6_ospf.structured_config:
                    self.custom_structured_configs.nested.ipv6_router_ospf.process_ids.obtain(process_id)._deepmerge(
                        vrf.ipv6_ospf.structured_config, list_merge=self.custom_structured_configs.list_merge_strategy
                    )

                if vrf.name != "default":
                    process.vrf = vrf.name
                self._update_ipv6_ospf_redistribute(process, vrf)

                # In theory only the underlay could have created an OSPF process before that.
                maybe_existing_process = self.structured_config.ipv6_router_ospf.process_ids.obtain(process_id)
                maybe_existing_process._combine(process)

    def _update_ipv6_ospf_redistribute(
        self: AvdStructuredConfigNetworkServicesProtocol,
        process: EosCliConfigGen.Ipv6RouterOspf.ProcessIdsItem,
        vrf: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem,
    ) -> None:
        """
        Configures OSPFv3 route redistribution settings for the given VRF.

        Args:
            process: The OSPFv3 process configuration object.
            vrf: The VRF object containing OSPFv3 redistribution settings.
        """
        if vrf.ipv6_ospf.redistribute_bgp.enabled:
            process.redistribute.bgp.enabled = True
            if route_map := vrf.ipv6_ospf.redistribute_bgp.route_map:
                process.redistribute.bgp.route_map = route_map
            if include_leaked := vrf.ipv6_ospf.redistribute_bgp.include_leaked:
                process.redistribute.bgp.include_leaked = include_leaked

        if vrf.ipv6_ospf.redistribute_connected.enabled:
            process.redistribute.connected.enabled = True
            if route_map := vrf.ipv6_ospf.redistribute_connected.route_map:
                process.redistribute.connected.route_map = route_map
            if include_leaked := vrf.ipv6_ospf.redistribute_bgp.include_leaked:
                process.redistribute.connected.include_leaked = include_leaked

        if vrf.ipv6_ospf.redistribute_isis.enabled:
            process.redistribute.isis.enabled = True
            if isis_level := vrf.ipv6_ospf.redistribute_isis.isis_level:
                process.redistribute.isis.isis_level = isis_level
            if route_map := vrf.ipv6_ospf.redistribute_isis.route_map:
                process.redistribute.isis.route_map = route_map
            if include_leaked := vrf.ipv6_ospf.redistribute_isis.include_leaked:
                process.redistribute.isis.include_leaked = include_leaked

        if vrf.ipv6_ospf.redistribute_ospfv3.enabled:
            process.redistribute.ospfv3.enabled = True
            if vrf.ipv6_ospf.redistribute_ospfv3.match_external.enabled:
                process.redistribute.ospfv3.match_external.enabled = True
                if route_map := vrf.ipv6_ospf.redistribute_ospfv3.match_external.route_map:
                    process.redistribute.ospfv3.match_external.route_map = route_map
                if include_leaked := vrf.ipv6_ospf.redistribute_ospfv3.match_external.include_leaked:
                    process.redistribute.ospfv3.match_external.include_leaked = include_leaked
            if vrf.ipv6_ospf.redistribute_ospfv3.match_internal.enabled:
                process.redistribute.ospfv3.match_internal.enabled = True
                if route_map := vrf.ipv6_ospf.redistribute_ospfv3.match_internal.route_map:
                    process.redistribute.ospfv3.match_internal.route_map = route_map
            if vrf.ipv6_ospf.redistribute_ospfv3.match_nssa_external.enabled:
                process.redistribute.ospfv3.match_nssa_external.enabled = True
                if route_map := vrf.ipv6_ospf.redistribute_ospfv3.match_nssa_external.route_map:
                    process.redistribute.ospfv3.match_nssa_external.route_map = route_map
            if route_map := vrf.ipv6_ospf.redistribute_ospfv3.route_map:
                process.redistribute.ospfv3.route_map = route_map

        if vrf.ipv6_ospf.redistribute_dhcp.enabled:
            process.redistribute.dhcp.enabled = True
            if route_map := vrf.ipv6_ospf.redistribute_dhcp.route_map:
                process.redistribute.dhcp.route_map = route_map

        if vrf.ipv6_ospf.redistribute_static.enabled:
            process.redistribute.static.enabled = True
            if route_map := vrf.ipv6_ospf.redistribute_static.route_map:
                process.redistribute.static.route_map = route_map
            if include_leaked := vrf.ipv6_ospf.redistribute_static.include_leaked:
                process.redistribute.static.include_leaked = include_leaked
