# Copyright (c) 2025-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Protocol

from pyavd._eos_designs.schema import EosDesigns

if TYPE_CHECKING:
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
        """Return the consolidated connected endpoints for this device as one flat list."""
        filtered_connected_endpoints = EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpoints()
        for connected_endpoints_group in self.inputs._connected_endpoints:
            for connected_endpoint in connected_endpoints_group.value:
                connected_endpoint._internal_data.context = connected_endpoints_group.key
                for adapter_index, adapter in zip(connected_endpoint._adapter_indices, connected_endpoint.adapters, strict=True):
                    adapter._internal_data.context = f"{connected_endpoints_group.key}[name={connected_endpoint.name}].adapters[{adapter_index}]"
                filtered_connected_endpoints.append(connected_endpoint)

        return filtered_connected_endpoints

    @cached_property
    def filtered_network_ports(self: SharedUtilsProtocol) -> EosDesigns.NetworkPorts:
        """Apply the deferred effective-platform filter to consolidated network-port candidates."""
        filtered_network_ports = EosDesigns.NetworkPorts()
        for network_port in self.inputs._network_ports:
            network_port._internal_data.context = f"network_ports[{network_port._source_index}]"
            if network_port.platforms and (not self.platform or not self.match_regexes(network_port.platforms, self.platform)):
                continue
            filtered_network_ports.append(network_port)

        return filtered_network_ports
