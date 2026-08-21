# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_designs.schema import EosDesigns as AVDDesign

from .models import ConsolidatedNetworkServices, ConsolidatedNetworkServicesItem

if TYPE_CHECKING:
    from .consolidator import AVDDesignConsolidatorProtocol


class NetworkServicesMixin(Protocol):
    """Mixin consolidating device-local network-services inputs."""

    def set_network_services(self: AVDDesignConsolidatorProtocol) -> None:
        """Set tenant- and tag-filtered network-services groups for this device."""
        consolidated_groups = ConsolidatedNetworkServices()
        tenant_filter = set(self.node_config.filter.tenants)
        filter_tags = set(self.node_config.filter.tags)
        if self.group is not None:
            filter_tags.add(self.group)

        source_groups: list[tuple[str, AVDDesign._DynamicKeys.DynamicNetworkServicesItem.NetworkServices]] = []
        if self.inputs.network_services:
            root_tenants = AVDDesign.NetworkServices(
                tenant for tenant in self.inputs.network_services if "all" in tenant_filter or tenant.name in tenant_filter
            )._cast_as(AVDDesign._DynamicKeys.DynamicNetworkServicesItem.NetworkServices)
            source_groups.append(("network_services", root_tenants))
        source_groups.extend(
            (
                source_group.key,
                AVDDesign._DynamicKeys.DynamicNetworkServicesItem.NetworkServices(
                    tenant for tenant in source_group.value if "all" in tenant_filter or tenant.name in tenant_filter
                ),
            )
            for source_group in self.inputs._dynamic_keys.network_services
        )

        for source_key, source_tenants in source_groups:
            tenants = AVDDesign._DynamicKeys.DynamicNetworkServicesItem.NetworkServices()
            for tenant in source_tenants:
                tenant.l2vlans = tenant.l2vlans._filtered(lambda l2vlan: "all" in filter_tags or bool(filter_tags.intersection(l2vlan.tags)))
                for vrf in tenant.vrfs:
                    vrf.svis = vrf.svis._filtered(lambda svi: "all" in filter_tags or bool(filter_tags.intersection(svi.tags)))
                tenants.append(tenant)

            if tenants:
                consolidated_groups.append(ConsolidatedNetworkServicesItem(key=source_key, tenants=tenants))

        self.consolidated.network_services = consolidated_groups

    def prune_network_services_inputs(self: AVDDesignConsolidatorProtocol) -> None:
        """Remove network-services inputs replaced by the consolidated groups."""
        self._unset_avd_model(self.inputs, ("network_services", "network_services_keys"))
        self._unset_avd_model(self.inputs._dynamic_keys, ("network_services",))
