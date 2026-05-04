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
                    msg = f"Missing or invalid 'ipv6_ospf.process_id' or 'vrf_id' under vrf '{vrf.name}'."
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
        """Populate redistribution settings on the given OSPFv3 process from the VRF's ipv6_ospf config."""
        ospfv3 = vrf.ipv6_ospf
        redistribution = process.redistribute

        if ospfv3.redistribute_bgp.enabled:
            self._apply_redistribute(ospfv3.redistribute_bgp, redistribution.bgp)

        if ospfv3.redistribute_connected.enabled:
            self._apply_redistribute(ospfv3.redistribute_connected, redistribution.connected)

        if ospfv3.redistribute_isis.enabled:
            self._apply_redistribute(ospfv3.redistribute_isis, redistribution.isis)
            if isis_level := ospfv3.redistribute_isis.isis_level:
                redistribution.isis.isis_level = isis_level

        if ospfv3.redistribute_ospfv3.enabled:
            self._apply_ospfv3_redistribute(ospfv3.redistribute_ospfv3, redistribution.ospfv3)

        if ospfv3.redistribute_dhcp.enabled:
            redistribution.dhcp.enabled = True
            if route_map := ospfv3.redistribute_dhcp.route_map:
                redistribution.dhcp.route_map = route_map

        if ospfv3.redistribute_static.enabled:
            self._apply_redistribute(ospfv3.redistribute_static, redistribution.static)

    def _apply_redistribute(
        self: AvdStructuredConfigNetworkServicesProtocol,
        src: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem.Ipv6Ospf.RedistributeBgp
        | EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem.Ipv6Ospf.RedistributeConnected
        | EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem.Ipv6Ospf.RedistributeIsis
        | EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem.Ipv6Ospf.RedistributeStatic,
        process: EosCliConfigGen.Ipv6RouterOspf.ProcessIdsItem.Redistribute.Bgp
        | EosCliConfigGen.Ipv6RouterOspf.ProcessIdsItem.Redistribute.Connected
        | EosCliConfigGen.Ipv6RouterOspf.ProcessIdsItem.Redistribute.Isis
        | EosCliConfigGen.Ipv6RouterOspf.ProcessIdsItem.Redistribute.Static,
    ) -> None:
        """Set enabled, route_map, and include_leaked."""
        process.enabled = True
        if route_map := src.route_map:
            process.route_map = route_map
        if include_leaked := src.include_leaked:
            process.include_leaked = include_leaked

    def _apply_ospfv3_redistribute(
        self: AvdStructuredConfigNetworkServicesProtocol,
        src: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem.Ipv6Ospf.RedistributeOspfv3,
        process: EosCliConfigGen.Ipv6RouterOspf.ProcessIdsItem.Redistribute.Ospfv3,
    ) -> None:
        """Set OSPFv3 redistribution settings (external, internal, NSSA-external match filters and route_map)."""
        process.enabled = True

        if src.match_external.enabled:
            process.match_external.enabled = True
            if route_map := src.match_external.route_map:
                process.match_external.route_map = route_map
            if include_leaked := src.match_external.include_leaked:
                process.match_external.include_leaked = include_leaked

        if src.match_internal.enabled:
            process.match_internal.enabled = True
            if route_map := src.match_internal.route_map:
                process.match_internal.route_map = route_map

        if src.match_nssa_external.enabled:
            process.match_nssa_external.enabled = True
            if route_map := src.match_nssa_external.route_map:
                process.match_nssa_external.route_map = route_map

        if route_map := src.route_map:
            process.route_map = route_map
