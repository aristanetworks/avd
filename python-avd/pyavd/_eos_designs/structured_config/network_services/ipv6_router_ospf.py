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

                # Allowing network_services to influence the underlay OSPF configuration in a manner similar to BGP
                if vrf.ipv6_ospf.process_id == self.inputs.underlay_ospf_process_id and vrf.name != "default":
                    msg = f"'tenants[name={tenant.name}].vrfs[name={vrf.name}].ipv6_ospf.process_id[process_id={vrf.ospf.process_id}]' should not match the \
underlay OSPFv3 process id '{self.inputs.underlay_ospf_process_id}'."
                    raise AristaAvdInvalidInputsError(msg)

                process_id = default(vrf.ipv6_ospf.process_id, vrf.vrf_id)
                if not process_id:
                    msg = f"Missing or invalid 'ipv6_ospf.process_id' or 'vrf_id' under vrf '{vrf.name}"
                    raise AristaAvdInvalidInputsError(msg)

                process = EosCliConfigGen.Ipv6RouterOspf.ProcessIdsItem(
                    id=process_id, router_id=self.get_protocol_vrf_router_id(vrf, tenant, vrf.ipv6_ospf.router_id)
                )

                if vrf.ipv6_ospf.structured_config:
                    self.custom_structured_configs.nested.ipv6_router_ospf.process_ids.obtain(process_id)._deepmerge(
                        vrf.ipv6_ospf.structured_config, list_merge=self.custom_structured_configs.list_merge_strategy
                    )

                if vrf.name != "default":
                    process.vrf = vrf.name
                self._update_ospf_redistribute(process, vrf)

                # In theory only the underlay could have created an OSPFv3 process before that.
                maybe_existing_process = self.structured_config.ipv6_router_ospf.process_ids.obtain(process_id)
                maybe_existing_process._combine(process)

        # TODO: Need to confirm
        # If we have static_routes in default VRF and not EVPN, and underlay is OSPF
        # Then add redistribute static to the underlay OSPF process.
        # if self._vrf_default_ipv4_static_routes["redistribute_in_underlay"] and self.shared_utils.underlay_routing_protocol in ["ospf", "ospf-ldp"]:
        #     self.structured_config.router_ospf.process_ids.obtain(self.inputs.underlay_ospf_process_id).redistribute.static.enabled = True

    def _update_ospf_redistribute(
        self: AvdStructuredConfigNetworkServicesProtocol,
        process: EosCliConfigGen.RouterOspf.ProcessIdsItem,
        vrf: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem,
    ) -> None:
        """
        Configures OSPF route redistribution settings for the given VRF.

        This method enables redistribution of BGP and connected routes into OSPF,
        setting the associated route maps if specified.

        Args:
            process: The OSPF process configuration object.
            vrf: The VRF object containing OSPF redistribution settings.
        """
        if vrf.ospf.redistribute_bgp.enabled:
            process.redistribute.bgp.enabled = True
            if route_map := vrf.ospf.redistribute_bgp.route_map:
                process.redistribute.bgp.route_map = route_map

        if vrf.ospf.redistribute_connected.enabled:
            process.redistribute.connected.enabled = True
            if route_map := vrf.ospf.redistribute_connected.route_map:
                process.redistribute.connected.route_map = route_map

