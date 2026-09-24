# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Regular structured-config adapter for the isolated connected-endpoints builder."""

from __future__ import annotations

from typing import TYPE_CHECKING, Literal

from pyavd._eos_designs.connected_endpoints import (
    ConnectedEndpointsBuildContext,
    ConnectedEndpointsBuildTarget,
    ConnectedEndpointsDescriptionData,
    ConnectedEndpointsPlatformFeatures,
    build_connected_endpoints,
)
from pyavd._eos_designs.structured_config.structured_config_generator import StructuredConfigGenerator, structured_config_contributor
from pyavd.api.interface_descriptions import InterfaceDescriptionData

from .mac_access_lists import MacAccessListsMixin

if TYPE_CHECKING:
    from pyavd._eos_designs.eos_designs_facts.schema import EosDesignsFacts
    from pyavd._eos_designs.schema import EosDesigns
    from pyavd._eos_designs.shared_utils import SharedUtilsProtocol


def _get_interface_support(supported: bool, subinterfaces_supported: bool) -> Literal["none", "main_interfaces", "all_interfaces"]:
    """Map platform feature flags to the interface support level consumed by the isolated builder."""
    if not supported:
        return "none"
    if subinterfaces_supported:
        return "all_interfaces"
    return "main_interfaces"


def _get_address_locking_support(supported: bool, ipv6_ethernet_interface: bool) -> Literal["none", "ipv4", "ipv4_ipv6"]:
    """Map platform feature flags to the Ethernet address families supported for address locking."""
    if not supported:
        return "none"
    if ipv6_ethernet_interface:
        return "ipv4_ipv6"
    return "ipv4"


def get_connected_endpoints_build_context(
    inputs: EosDesigns,
    facts: EosDesignsFacts,
    shared_utils: SharedUtilsProtocol,
) -> ConnectedEndpointsBuildContext:
    """
    Map full regular-build state into the isolated builder's dependency model.

    Keeping this mapping outside the core package ensures that only this adapter
    knows about full eos-designs inputs, facts, and ``SharedUtils``. It is also
    used by integration scenarios until the external isolated-input schema and
    its mapping are introduced.

    Filtering, port-profile inheritance, LACP fallback individual-profile
    resolution, platform lookup, and other full-build calculations happen here.
    The returned context therefore contains everything the core builder needs
    without giving it access to any of the broad source objects.

    Args:
        inputs: Complete, validated eos-designs inputs for the device.
        facts: Facts for the device being built. Facts from other devices are
            consumed indirectly while ``shared_utils`` resolves the context.
        shared_utils: Regular-build utilities used only while mapping broad
            inputs and facts into the narrow context.

    Returns:
        A resolved context that can be passed to ``build_connected_endpoints``.
        Source endpoint models are filtered for the current hostname and have
        their port profiles applied before being placed in the context.
    """

    def render_ethernet_description(data: ConnectedEndpointsDescriptionData) -> str | None:
        """
        Render an Ethernet description through the regular-build description API.

        This closure deliberately captures ``shared_utils`` at the adapter
        boundary. The core builder only passes ``ConnectedEndpointsDescriptionData``
        and never gains access to ``SharedUtils`` or custom description internals.

        Args:
            data: Narrow description data prepared by the interface builder.

        Returns:
            The rendered description, or ``None`` when no description is produced.
        """
        return shared_utils.interface_descriptions.connected_endpoints_ethernet_interface(
            InterfaceDescriptionData(
                shared_utils=shared_utils,
                interface=data.interface,
                peer=data.peer,
                peer_interface=data.peer_interface,
                peer_type=data.peer_type,
                description=data.description,
                port_channel_id=data.port_channel_id,
                port_channel_description=data.port_channel_description,
            )
        )

    def render_port_channel_description(data: ConnectedEndpointsDescriptionData) -> str | None:
        """
        Render a Port-Channel description through the regular-build description API.

        Like the Ethernet renderer, this keeps support for custom description
        classes outside the isolated builder's dependency surface.

        Args:
            data: Narrow description data prepared by the interface builder.

        Returns:
            The rendered description, or ``None`` when no description is produced.
        """
        return shared_utils.interface_descriptions.connected_endpoints_port_channel_interface(
            InterfaceDescriptionData(
                shared_utils=shared_utils,
                interface=data.interface,
                peer=data.peer,
                peer_interface=data.peer_interface,
                peer_type=data.peer_type,
                description=data.description,
                port_channel_id=data.port_channel_id,
                port_channel_description=data.port_channel_description,
            )
        )

    connected_endpoints = shared_utils.filtered_connected_endpoints
    network_ports = shared_utils.filtered_network_ports
    individual_adapter_settings = {}
    for connected_endpoint in connected_endpoints:
        for adapter in connected_endpoint.adapters:
            if individual_adapter := shared_utils.get_merged_individual_adapter_settings(adapter):
                individual_adapter_settings[adapter._internal_data.context] = individual_adapter
    for network_port in network_ports:
        if individual_adapter := shared_utils.get_merged_individual_adapter_settings(network_port):
            individual_adapter_settings[network_port._internal_data.context] = individual_adapter

    feature_support = shared_utils.platform_settings.feature_support
    link_tracking_groups = shared_utils.link_tracking_groups
    return ConnectedEndpointsBuildContext(
        hostname=shared_utils.hostname,
        connected_endpoints=connected_endpoints,
        network_ports=network_ports,
        individual_adapter_settings=individual_adapter_settings,
        defined_vlans=facts.vlans,
        evpn_short_esi_prefix=inputs.evpn_short_esi_prefix,
        enable_trunk_groups=inputs.enable_trunk_groups,
        fabric_sflow_endpoints=inputs.fabric_sflow.endpoints,
        flow_tracking_enabled=inputs.fabric_flow_tracking.endpoints.enabled,
        flow_tracking_name=inputs.fabric_flow_tracking.endpoints.name,
        flow_tracking_type=shared_utils.flow_tracking_type,
        dot1x_enabled=inputs.dot1x_settings.enabled,
        ipv4_acl_names=frozenset(acl.name for acl in inputs.ipv4_acls),
        ipv6_acl_names=frozenset(acl.name for acl in inputs.ipv6_acls),
        mac_acl_names=frozenset(acl.name for acl in inputs.mac_acls),
        ptp_profiles=inputs.ptp_profiles,
        ptp_profile_name=shared_utils.ptp_profile_name,
        link_tracking_group_default_name=next(iter(link_tracking_groups)).name if link_tracking_groups else None,
        evpn_ethernet_segments_enabled=shared_utils.overlay_evpn and (shared_utils.overlay_vtep or shared_utils.overlay_ler),
        mlag=shared_utils.mlag,
        is_campus_device=shared_utils.is_campus_device,
        digital_twin=shared_utils.digital_twin,
        platform_features=ConnectedEndpointsPlatformFeatures(
            address_locking_support=_get_address_locking_support(
                feature_support.address_locking.supported,
                feature_support.address_locking.ipv6_ethernet_interface,
            ),
            interface_storm_control=feature_support.interface_storm_control,
            per_interface_l2_mru=feature_support.per_interface_l2_mru,
            per_interface_l2_mtu=feature_support.per_interface_l2_mtu,
            mtu_support=_get_interface_support(feature_support.per_interface_mtu, feature_support.subinterface_mtu),
            poe=feature_support.poe,
            ptp=feature_support.ptp,
            sflow_support=_get_interface_support(feature_support.sflow, feature_support.sflow_subinterfaces),
        ),
        render_ethernet_description=render_ethernet_description,
        render_port_channel_description=render_port_channel_description,
    )


class AvdStructuredConfigConnectedEndpoints(StructuredConfigGenerator, MacAccessListsMixin):
    """
    Adapt a regular eos-designs build to the interface-only builder.

    This class is intentionally the only place where the connected-endpoints
    package can see full-build objects. It resolves the narrow context, lends the
    builder the live interface lists and parent tracker, and finally applies the
    non-interface ACL and global sFlow requirements reported by the builder.
    """

    def render(self) -> None:
        """
        Run the adapter when connected-endpoint generation is enabled for the node type.

        The surrounding structured-config pipeline still owns ordering. Keeping
        this generator in its original position ensures that the target contains
        interfaces contributed by earlier generators and remains available to
        parent-interface, flow, metadata, and custom-config generators that run
        afterwards.
        """
        if self.shared_utils.connected_endpoints:
            super().render()

    @structured_config_contributor
    def connected_endpoints(self) -> None:
        """
        Adapt live regular-build state, run the core builder, and finish global output.

        The target receives the existing Ethernet and Port-Channel indexed lists,
        custom interface overlays, and parent tracker by reference. The core
        builder mutates those exact objects, preserving identity, collision
        behavior, and downstream visibility in the regular pipeline.

        The core builder is restricted to interface output. It records referenced
        ACLs and the need for global sFlow configuration on the target instead of
        writing those global models itself. This adapter consumes those declared
        requirements after the interface build to preserve complete regular-build
        behavior without widening the isolated builder's output contract.
        """
        target = ConnectedEndpointsBuildTarget(
            structured_config=self.structured_config,
            custom_structured_configs=self.custom_structured_configs,
            parent_interfaces_tracker=self.structured_config_utils.parent_interfaces_tracker,
        )
        context = get_connected_endpoints_build_context(self.inputs, self.facts, self.shared_utils)
        build_connected_endpoints(context, target)

        # The isolated builder is interface-only. Regular builds retain their
        # established global output by consuming requirements at this boundary.
        for acl_name in target.referenced_mac_acls:
            self._set_mac_acl(acl_name)
        for acl_name in target.referenced_ipv4_acls:
            self.structured_config_utils._set_ipv4_acl(self.inputs.ipv4_acls[acl_name])
        for acl_name in target.referenced_ipv6_acls:
            self.structured_config_utils._set_ipv6_acl(self.inputs.ipv6_acls[acl_name])
        if target.sflow_required:
            self.structured_config_utils.set_once_sflow()
