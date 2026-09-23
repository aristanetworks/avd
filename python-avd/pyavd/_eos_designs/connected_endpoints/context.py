# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Resolved inputs consumed by the connected-endpoints interface builder."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from pyavd._utils.default import default
from pyavd._utils.undefined import Undefined, UndefinedType

if TYPE_CHECKING:
    from collections.abc import Callable
    from typing import TypeVar

    from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
    from pyavd._eos_designs.schema import EosDesigns

    T_FlowTracker = TypeVar("T_FlowTracker", EosCliConfigGen.EthernetInterfacesItem.FlowTracker, EosCliConfigGen.PortChannelInterfacesItem.FlowTracker)


@dataclass(frozen=True, slots=True)
class ConnectedEndpointsPlatformFeatures:
    """Platform capabilities used while building connected-endpoint interfaces."""

    address_locking: bool
    """Resolved ``platform_settings[].feature_support.address_locking.supported`` value."""

    address_locking_ipv6_ethernet_interface: bool
    """Resolved ``platform_settings[].feature_support.address_locking.ipv6_ethernet_interface`` value."""

    interface_storm_control: bool
    """Resolved ``platform_settings[].feature_support.interface_storm_control`` value."""

    per_interface_l2_mru: bool
    """Resolved ``platform_settings[].feature_support.per_interface_l2_mru`` value."""

    per_interface_l2_mtu: bool
    """Resolved ``platform_settings[].feature_support.per_interface_l2_mtu`` value."""

    per_interface_mtu: bool
    """Resolved ``platform_settings[].feature_support.per_interface_mtu`` value."""

    poe: bool
    """Resolved ``platform_settings[].feature_support.poe`` value."""

    ptp: bool
    """Resolved ``platform_settings[].feature_support.ptp`` value."""

    sflow: bool
    """Resolved ``platform_settings[].feature_support.sflow`` value."""

    sflow_subinterfaces: bool
    """Resolved ``platform_settings[].feature_support.sflow_subinterfaces`` value."""

    subinterface_mtu: bool
    """Resolved ``platform_settings[].feature_support.subinterface_mtu`` value."""


@dataclass(frozen=True, slots=True)
class ConnectedEndpointsDescriptionData:
    """Description inputs independent of the regular-build ``SharedUtils`` object."""

    interface: str
    """Name of the local Ethernet or Port-Channel interface."""

    peer: str
    """Connected endpoint name."""

    peer_interface: str | None
    """Connected endpoint interface or Port-Channel name."""

    peer_type: str | None
    """Connected endpoint type from ``connected_endpoints_keys[].type`` or ``network_port``."""

    description: str | None
    """Explicit adapter description, if configured."""

    port_channel_id: int | None = None
    """Resolved local Port-Channel ID when the interface belongs to a Port-Channel."""

    port_channel_description: str | None = None
    """Input ``connected_endpoints[].adapters[].port_channel.description`` value."""


@dataclass(frozen=True, slots=True)
class ConnectedEndpointsBuildContext:
    """
    Resolved, read-only inputs for one connected-endpoints build.

    The regular eos-designs pipeline constructs this model from its full inputs,
    facts, and shared utilities. The interface builder only receives this model,
    which makes additions to its dependency surface explicit. The source models
    are already filtered and have port profiles applied before they enter this
    context.

    Description rendering remains an injected capability because regular builds
    support user-defined description classes. It accepts the narrow data model
    above, so the builder never receives ``SharedUtils`` itself.
    """

    hostname: str
    """Hostname of the device for which interfaces are being built."""

    connected_endpoints: EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpoints
    """Connected endpoints filtered for ``hostname``, with port profiles resolved on every adapter."""

    network_ports: EosDesigns.NetworkPorts
    """Input ``network_ports`` filtered for ``hostname`` and platform, with port profiles resolved."""

    individual_adapter_settings: dict[str, EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem.AdaptersItem]
    """Resolved LACP fallback individual-adapter settings, keyed by the source adapter context path."""

    defined_vlans: str | None
    """Device facts ``vlans`` value used to expand an adapter configured with ``vlans: defined_vlans``."""

    evpn_short_esi_prefix: str
    """Input ``evpn_short_esi_prefix``."""

    enable_trunk_groups: bool
    """Input ``enable_trunk_groups``."""

    fabric_sflow_endpoints: bool | None
    """Input ``fabric_sflow.endpoints``."""

    flow_tracking_enabled: bool
    """Input ``fabric_flow_tracking.endpoints.enabled``."""

    flow_tracking_name: str
    """Input ``fabric_flow_tracking.endpoints.name``."""

    flow_tracking_type: str
    """Resolved node flow-tracker type used to select sampled or hardware interface output."""

    dot1x_enabled: bool
    """Input ``dot1x_settings.enabled``."""

    ipv4_acl_names: frozenset[str]
    """Names defined under input ``ipv4_acls`` and available for interface references."""

    ipv6_acl_names: frozenset[str]
    """Names defined under input ``ipv6_acls`` and available for interface references."""

    mac_acl_names: frozenset[str]
    """Names defined under input ``mac_acls`` and available for interface references."""

    ptp_profiles: EosDesigns.PtpProfiles
    """Input ``ptp_profiles``."""

    ptp_profile_name: str | None
    """Resolved node PTP profile from node ``ptp.profile`` or input ``ptp_settings.profile``."""

    link_tracking_group_default_name: str | None
    """Name of the first resolved node link-tracking group, used as the adapter default."""

    overlay_evpn: bool
    """Whether EVPN is enabled for the node after resolving its overlay roles and address families."""

    overlay_vtep: bool
    """Whether the node is a VXLAN VTEP after resolving node type and network-services settings."""

    overlay_ler: bool
    """Whether the node is an MPLS label edge router carrying network services."""

    mlag: bool
    """Whether MLAG is enabled for the node."""

    is_campus_device: bool
    """Whether campus tags are enabled and the node is resolved as a campus device."""

    digital_twin: bool
    """Whether this build is running in AVD digital-twin mode."""

    platform_features: ConnectedEndpointsPlatformFeatures
    """Platform feature flags needed to decide which interface fields are supported."""

    render_ethernet_description: Callable[[ConnectedEndpointsDescriptionData], str | None]
    """Renderer for Ethernet descriptions, including regular-build custom description classes."""

    render_port_channel_description: Callable[[ConnectedEndpointsDescriptionData], str | None]
    """Renderer for Port-Channel descriptions, including regular-build custom description classes."""

    custom_structured_config_list_merge: Literal["append_unique", "append", "replace", "keep", "prepend", "prepend_unique"]
    """Input ``custom_structured_configuration_list_merge``, normalized to the internal merge-strategy names."""

    def get_interface_mtu(self, interface_name: str, configured_mtu: int | None) -> int | None:
        """Return the configured MTU when the target platform supports it."""
        if not self.platform_features.per_interface_mtu:
            return None
        if "." in interface_name and not self.platform_features.subinterface_mtu:
            return None
        return configured_mtu

    def get_interface_sflow(self, interface_name: str, configured_sflow: bool | None) -> bool | None:
        """Return the per-interface sFlow state supported by the target platform."""
        if self.platform_features.sflow and ("." not in interface_name or self.platform_features.sflow_subinterfaces):
            return configured_sflow
        return None

    def get_interface_validate_state(self, user_input: bool | None) -> bool | UndefinedType:
        """Resolve interface state validation without depending on structured-config utilities."""
        if self.digital_twin:
            return False if user_input is False else Undefined
        return Undefined if user_input is None else user_input

    def get_flow_tracker(
        self,
        flow_tracking: EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem.AdaptersItem.FlowTracking,
        output_type: type[T_FlowTracker],
    ) -> T_FlowTracker | UndefinedType:
        """Resolve endpoint flow-tracking settings into the requested interface model."""
        enabled = default(flow_tracking.enabled, self.flow_tracking_enabled)
        if not enabled:
            return Undefined
        name = default(flow_tracking.name, self.flow_tracking_name)
        if self.flow_tracking_type == "hardware":
            return output_type(hardware=name)
        if self.flow_tracking_type == "sampled":
            return output_type(sampled=name)
        return Undefined
