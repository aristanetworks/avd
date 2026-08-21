# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import re
from dataclasses import dataclass
from functools import cached_property
from typing import TYPE_CHECKING, Any, Protocol, cast, overload

from pyavd._eos_designs.schema import EosDesigns as AVDDesign
from pyavd._errors import AristaAvdError, AristaAvdInvalidInputsError

from .models import (
    ConsolidatedConnectedEndpoint,
    ConsolidatedConnectedEndpointGroups,
    ConsolidatedConnectedEndpoints,
    ConsolidatedConnectedEndpointsItem,
    ConsolidatedNetworkPort,
    ConsolidatedNetworkPorts,
    ConsolidatedPortProfileName,
    ConsolidatedPortProfileNames,
)

if TYPE_CHECKING:
    from .consolidator import AVDDesignConsolidatorProtocol

    Adapter = AVDDesign._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem.AdaptersItem
    RootAdapter = AVDDesign.ConnectedEndpointsItem.AdaptersItem
    AdapterOrNetworkPort = Adapter | RootAdapter | AVDDesign.NetworkPortsItem
    ConnectedEndpoints = AVDDesign.ConnectedEndpoints | AVDDesign._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpoints


@dataclass(frozen=True, slots=True)
class ConnectedEndpointSourceGroup:
    """Lightweight context around one unmodified connected-endpoint input collection."""

    key: str
    type: str | None
    description: str | None
    value: ConnectedEndpoints


class ConnectedEndpointsMixin(Protocol):
    """Mixin consolidating connected endpoints, network ports, and their port profiles."""

    @cached_property
    def resolved_port_profiles(self: AVDDesignConsolidatorProtocol) -> dict[str, AVDDesign.PortProfilesItem]:
        """Cache of port profiles with parent profiles inherited."""
        return {}

    def get_merged_port_profile(self: AVDDesignConsolidatorProtocol, profile_name: str, context: str) -> AVDDesign.PortProfilesItem:
        """Return a copied port profile with its parent profile inherited."""
        if profile_name in self.resolved_port_profiles:
            return self.resolved_port_profiles[profile_name]

        if profile_name not in self.inputs.port_profiles:
            msg = f"Profile '{profile_name}' applied under '{context}' does not exist in `port_profiles`."
            raise AristaAvdInvalidInputsError(msg)

        port_profile = self.inputs.port_profiles[profile_name]._deepcopy()
        if port_profile.parent_profile:
            if port_profile.parent_profile not in self.inputs.port_profiles:
                msg = f"Profile '{port_profile.parent_profile}' applied under port profile '{profile_name}' does not exist in `port_profiles`."
                raise AristaAvdInvalidInputsError(msg)

            port_profile._deepinherit(self.inputs.port_profiles[port_profile.parent_profile])

        delattr(port_profile, "parent_profile")
        self.resolved_port_profiles[profile_name] = port_profile
        return port_profile

    @overload
    def get_merged_adapter_settings(
        self: AVDDesignConsolidatorProtocol,
        adapter_or_network_port_settings: Adapter,
    ) -> Adapter: ...

    @overload
    def get_merged_adapter_settings(
        self: AVDDesignConsolidatorProtocol,
        adapter_or_network_port_settings: RootAdapter,
    ) -> RootAdapter: ...

    @overload
    def get_merged_adapter_settings(
        self: AVDDesignConsolidatorProtocol,
        adapter_or_network_port_settings: AVDDesign.NetworkPortsItem,
    ) -> AVDDesign.NetworkPortsItem: ...

    def get_merged_adapter_settings(self: AVDDesignConsolidatorProtocol, adapter_or_network_port_settings: AdapterOrNetworkPort) -> AdapterOrNetworkPort:
        """Return copied adapter or network-port settings with the referenced port profile inherited."""
        merged_settings = adapter_or_network_port_settings._deepcopy()
        if (profile_name := merged_settings.profile) is None:
            return merged_settings

        port_profile = self.get_merged_port_profile(profile_name, merged_settings._internal_data.context)
        if isinstance(merged_settings, AVDDesign.NetworkPortsItem) and port_profile.port_channel._get("subinterfaces"):
            msg = f"'port_profiles[profile={profile_name}].port_channel.subinterfaces' is not supported since this profile is referenced under a network_port."
            raise AristaAvdInvalidInputsError(msg)

        merged_settings._deepinherit(cast("Any", port_profile._cast_as(type(merged_settings))))
        return merged_settings

    def resolve_individual_adapter_settings(self: AVDDesignConsolidatorProtocol, adapter: AdapterOrNetworkPort) -> None:
        """Resolve a nested LACP individual-fallback profile in-place on the copied adapter."""
        if not adapter.port_channel.mode or adapter.port_channel.lacp_fallback.mode != "individual":
            return

        individual = adapter.port_channel.lacp_fallback.individual
        individual_adapter = individual._cast_as(AVDDesign._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem.AdaptersItem)
        individual_adapter._internal_data.context = f"{adapter._internal_data.context}.port_channel.lacp_fallback.individual"
        merged_individual_adapter = self.get_merged_adapter_settings(individual_adapter)
        adapter.port_channel.lacp_fallback.individual = cast("Any", merged_individual_adapter)

    def set_connected_endpoints(self: AVDDesignConsolidatorProtocol) -> None:
        """Set profile-resolved connected endpoints containing adapters relevant to this device."""
        consolidated_groups = ConsolidatedConnectedEndpointGroups()

        for source_group in self._connected_endpoint_source_groups:
            endpoints = ConsolidatedConnectedEndpoints()
            for connected_endpoint in source_group.value:
                adapters = AVDDesign._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem.Adapters()
                adapter_indices = []
                for adapter_index, adapter in enumerate(connected_endpoint.adapters):
                    adapter._internal_data.context = f"{source_group.key}[name={connected_endpoint.name}].adapters[{adapter_index}]"
                    adapter_settings = self.get_merged_adapter_settings(adapter)
                    if not adapter_settings.switches or self.device_name not in adapter_settings.switches:
                        continue

                    nodes_length = len(adapter_settings.switches)
                    endpoint_ports = adapter_settings.endpoint_ports
                    if len(adapter_settings.switch_ports) != nodes_length or (endpoint_ports and len(endpoint_ports) != nodes_length):
                        msg = (
                            f"Length of lists 'switches' ({len(adapter.switches)}), 'switch_ports' ({len(adapter.switch_ports)}), "
                            f"'endpoint_ports' ({len(endpoint_ports) or '-'}) (if used) did not match on adapter {adapter_index} on"
                            f" connected_endpoint '{connected_endpoint.name}' under '{source_group.key}'."
                            " Notice that some or all of these variables could be inherited from 'port_profiles'"
                        )
                        raise AristaAvdError(msg)

                    consolidated_adapter_settings = (
                        adapter_settings
                        if isinstance(adapter_settings, AVDDesign._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem.AdaptersItem)
                        else adapter_settings._cast_as(AVDDesign._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem.AdaptersItem)
                    )
                    self.resolve_individual_adapter_settings(consolidated_adapter_settings)
                    adapters.append(consolidated_adapter_settings)
                    adapter_indices.append(adapter_index)

                if not adapters:
                    continue

                consolidated_endpoint = connected_endpoint._cast_as(ConsolidatedConnectedEndpoint)
                consolidated_endpoint.adapters = adapters
                consolidated_endpoint._adapter_indices = adapter_indices
                if not consolidated_endpoint.type:
                    consolidated_endpoint.type = source_group.type
                endpoints.append(consolidated_endpoint)

            if endpoints:
                consolidated_groups.append(
                    ConsolidatedConnectedEndpointsItem(
                        key=source_group.key,
                        type=source_group.type,
                        description=source_group.description,
                        value=endpoints,
                    )
                )

        self.consolidated.connected_endpoints = consolidated_groups

    @cached_property
    def _connected_endpoint_source_groups(self: AVDDesignConsolidatorProtocol) -> list[ConnectedEndpointSourceGroup]:
        """Combine all connected endpoint inputs while preserving custom-key precedence."""
        source_groups = []
        if self.inputs.connected_endpoints:
            source_groups.append(
                ConnectedEndpointSourceGroup(
                    key="connected_endpoints",
                    type=None,
                    description=None,
                    value=self.inputs.connected_endpoints,
                )
            )

        for dynamic_group in self.inputs._dynamic_keys.custom_connected_endpoints:
            key_data = self.inputs.custom_connected_endpoints_keys[dynamic_group.key]
            source_groups.append(
                ConnectedEndpointSourceGroup(
                    key=dynamic_group.key,
                    type=key_data.type,
                    description=key_data.description,
                    value=dynamic_group.value._cast_as(AVDDesign._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpoints),
                )
            )

        for dynamic_group in self.inputs._dynamic_keys.connected_endpoints:
            if any(dynamic_group.key == source_group.key for source_group in source_groups):
                continue
            key_data = self.inputs.connected_endpoints_keys[dynamic_group.key]
            source_groups.append(
                ConnectedEndpointSourceGroup(
                    key=dynamic_group.key,
                    type=key_data.type,
                    description=key_data.description,
                    value=dynamic_group.value,
                )
            )

        return source_groups

    def set_network_ports(self: AVDDesignConsolidatorProtocol) -> None:
        """
        Set profile-resolved network ports whose switch selectors match this device.

        Platform filtering is intentionally deferred to SharedUtils since the effective platform may come from
        CV topology or digital-twin substitution, neither of which is available during this consolidation phase.
        """
        network_ports = ConsolidatedNetworkPorts()
        for source_index, network_port in enumerate(self.inputs.network_ports):
            network_port._internal_data.context = f"network_ports[{source_index}]"
            network_port_settings = self.get_merged_adapter_settings(network_port)

            if not network_port_settings.switches and not network_port_settings.platforms:
                continue
            if network_port_settings.switches and not any(re.fullmatch(regex, self.device_name) for regex in network_port_settings.switches):
                continue

            consolidated_network_port = network_port_settings._cast_as(ConsolidatedNetworkPort)
            consolidated_network_port._source_index = source_index
            self.resolve_individual_adapter_settings(consolidated_network_port)
            network_ports.append(consolidated_network_port)

        self.consolidated.network_ports = network_ports

    def set_port_profile_names(self: AVDDesignConsolidatorProtocol) -> None:
        """Set minimal port-profile metadata required by fabric documentation."""
        self.consolidated.port_profile_names = ConsolidatedPortProfileNames(
            ConsolidatedPortProfileName(profile=profile.profile, parent_profile=profile.parent_profile) for profile in self.inputs.port_profiles
        )

    def prune_connected_endpoint_inputs(self: AVDDesignConsolidatorProtocol) -> None:
        """Remove connected endpoint inputs and profiles replaced by consolidated models."""
        self._unset_avd_model(
            self.inputs,
            ("connected_endpoints", "connected_endpoints_keys", "custom_connected_endpoints_keys", "network_ports", "port_profiles"),
        )
        self._unset_avd_model(self.inputs._dynamic_keys, ("connected_endpoints", "custom_connected_endpoints"))
