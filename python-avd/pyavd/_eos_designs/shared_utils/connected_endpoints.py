# Copyright (c) 2025-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from collections import defaultdict
from functools import cached_property
from itertools import chain
from typing import TYPE_CHECKING, Protocol

from pyavd._eos_designs.schema import EosDesigns
from pyavd._errors import AristaAvdError

if TYPE_CHECKING:
    from collections.abc import Iterable

    from . import SharedUtilsProtocol


class ConnectedEndpointsMixin(Protocol):
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def filtered_connected_endpoints(
        self: SharedUtilsProtocol,
    ) -> EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpoints:
        """
        Return list of endpoints defined under one of the keys in "connected_endpoints_keys" which are connected to this switch.

        Adapters are filtered to contain only the ones connected to this switch.
        """
        connected_endpoints = self.all_connected_endpoints
        filtered_connected_endpoints = EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpoints()
        for connected_endpoints_key in connected_endpoints:
            for connected_endpoint in connected_endpoints_key.value:
                filtered_adapters = EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem.Adapters()
                for adapter_index, adapter in enumerate(connected_endpoint.adapters):
                    adapter._internal_data.context = f"{connected_endpoints_key.key}[name={connected_endpoint.name}].adapters[{adapter_index}]"
                    adapter_settings = self.get_merged_adapter_settings(adapter)
                    if not adapter_settings.switches or self.hostname not in adapter_settings.switches:
                        continue

                    # Verify that length of all lists are the same
                    nodes_length = len(adapter_settings.switches)
                    endpoint_ports = adapter_settings.endpoint_ports
                    if len(adapter_settings.switch_ports) != nodes_length or (endpoint_ports and len(endpoint_ports) != nodes_length):
                        msg = (
                            f"Length of lists 'switches' ({len(adapter.switches)}), 'switch_ports' ({len(adapter.switch_ports)}), "
                            f"'endpoint_ports' ({len(endpoint_ports) or '-'}) (if used) did not match on adapter {adapter_index} on"
                            f" connected_endpoint '{connected_endpoint.name}' under '{connected_endpoints_key.key}'."
                            " Notice that some or all of these variables could be inherited from 'port_profiles'"
                        )
                        raise AristaAvdError(msg)

                    filtered_adapters.append(adapter_settings)

                if filtered_adapters:
                    # The object was deepcopied inside "get_merged_adapter_settings" so we can modify it here.
                    connected_endpoint.adapters = filtered_adapters
                    connected_endpoint._internal_data.context = connected_endpoints_key.key
                    if not connected_endpoint.type:
                        connected_endpoint.type = connected_endpoints_key._internal_data.type
                    filtered_connected_endpoints.append(connected_endpoint)

        return filtered_connected_endpoints

    @cached_property
    def filtered_network_ports(self: SharedUtilsProtocol) -> EosDesigns.NetworkPorts:
        """Return list of endpoints defined under "network_ports" which are connected to this switch."""
        filtered_network_ports = EosDesigns.NetworkPorts()
        for index, network_port in enumerate(self.inputs.network_ports):
            network_port._internal_data.context = f"network_ports[{index}]"
            network_port_settings = self.get_merged_adapter_settings(network_port)

            if not network_port_settings.switches and not network_port_settings.platforms:
                continue
            if network_port_settings.switches and not self.match_regexes(network_port_settings.switches, self.hostname):
                continue
            if network_port_settings.platforms and (not self.platform or not self.match_regexes(network_port_settings.platforms, self.platform)):
                continue

            filtered_network_ports.append(network_port_settings)

        return filtered_network_ports

    @cached_property
    def _network_services_vlans_by_tag(self: SharedUtilsProtocol) -> dict[str, frozenset[int]]:
        """
        Return a map from tag to the set of network services VLAN IDs carrying that tag.

        Covers both l2vlans and SVIs from tenants accepted by "filter.tenants" with tags accepted by "filter.tags".
        Deliberately not filtered on "filter.only_vlans_in_use", since this is used to decide which VLANs are in use.

        Used to resolve "vlan_tags" on connected endpoints adapters, network_ports and port_profiles.
        """
        if not self.any_network_services:
            return {}

        tenant_filter = set(self.node_config.filter.tenants)
        filter_tags = set(self.filter_tags)
        accepted_tenants = chain(
            (
                tenant
                for network_services_key in self.inputs._dynamic_keys.network_services
                for tenant in network_services_key.value
                if tenant_filter.intersection((tenant.name, "all"))
            ),
            (tenant for tenant in self.inputs.network_services if tenant_filter.intersection((tenant.name, "all"))),
        )

        vlans_by_tag: defaultdict[str, set[int]] = defaultdict(set)
        for tenant in accepted_tenants:
            for vlan in chain((svi for vrf in tenant.vrfs for svi in vrf.svis), tenant.l2vlans):
                if "all" not in filter_tags and not filter_tags.intersection(vlan.tags):
                    continue
                for tag in vlan.tags:
                    vlans_by_tag[tag].add(vlan.id)

        return {tag: frozenset(vlans) for tag, vlans in vlans_by_tag.items()}

    def get_vlans_from_vlan_tags(self: SharedUtilsProtocol, vlan_tags: Iterable[str]) -> set[int]:
        """
        Return the set of network services VLAN IDs carrying at least one of the given tags.

        The VLANs are filtered on "filter.tenants" and "filter.tags" but not on "filter.only_vlans_in_use"
        or on VLAN availability on uplink switches.
        Callers in structured config should intersect with "accepted_vlans" to get the VLANs actually configured on the device.
        """
        vlans_by_tag = self._network_services_vlans_by_tag
        return set(chain.from_iterable(vlans_by_tag.get(tag, ()) for tag in vlan_tags))
