# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor
from pyavd._errors import AristaAvdInvalidInputsError

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
        """
        Set structured config for router_ospfv3.

        An OSPFv3 instance is created for each VRF with at least one OSPFv3-enabled SVI on this device.
        """
        if not self.shared_utils.network_services_l3:
            return

        for tenant in self.shared_utils.filtered_tenants:
            for vrf in tenant.vrfs:
                if not self.shared_utils.ospfv3_enabled_for_vrf(vrf):
                    continue

                # With 'uplink_type: lan', SVIs are only deployed as subinterfaces on the uplink, where OSPFv3 is not supported yet.
                # The SVI configuration already raises for every rendered subinterface.
                # OSPFv3 SVIs that are not rendered at all, for example without 'uplink_switches', must also raise here,
                # otherwise an OSPFv3 instance without any interface would be created.
                if self.shared_utils.network_services_l2_as_subint:
                    msg = (
                        f"'{tenant._internal_data.context}[name={tenant.name}].vrfs[name={vrf.name}].svis[].ospfv3.enabled: true' "
                        f"is not supported on node '{self.shared_utils.hostname}' with 'uplink_type: lan', since SVIs are deployed as subinterfaces."
                    )
                    raise AristaAvdInvalidInputsError(msg)

                instance = EosCliConfigGen.RouterOspfv3.VrfsItem(
                    name=vrf.name,
                    passive_interface_default=True,
                    router_id=self.get_protocol_vrf_router_id(vrf, tenant, vrf.ospfv3.router_id),
                )
                instance.address_family_ipv6.enabled = True
                self._update_ospfv3_redistribute(instance, vrf)

                if vrf.ospfv3.structured_config:
                    self.custom_structured_configs.nested.router_ospfv3.vrfs.obtain(vrf.name)._deepmerge(
                        vrf.ospfv3.structured_config, list_merge=self.custom_structured_configs.list_merge_strategy
                    )

                # The same VRF can be defined in multiple tenants.
                self.structured_config.router_ospfv3.vrfs.obtain(vrf.name)._combine(instance)

    def _update_ospfv3_redistribute(
        self: AvdStructuredConfigNetworkServicesProtocol,
        instance: EosCliConfigGen.RouterOspfv3.VrfsItem,
        vrf: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem,
    ) -> None:
        """
        Configure redistribution into OSPFv3 for the given VRF.

        BGP is only redistributed when the VRF has BGP on this device.
        """
        if vrf.ospfv3.redistribute_bgp.enabled and self.shared_utils.bgp_enabled_for_vrf(vrf):
            instance.address_family_ipv6.redistribute.bgp.enabled = True

        if vrf.ospfv3.redistribute_connected.enabled:
            instance.address_family_ipv6.redistribute.connected.enabled = True
