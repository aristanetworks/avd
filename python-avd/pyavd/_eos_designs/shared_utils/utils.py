# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import re
from functools import cached_property
from typing import TYPE_CHECKING, Literal, Protocol, overload

from pyavd._eos_designs.schema import EosDesigns
from pyavd._errors import AristaAvdError, AristaAvdInvalidInputsError
from pyavd._utils import template_var
from pyavd.j2filters import range_expand

if TYPE_CHECKING:
    from collections.abc import Iterable, MutableMapping, Sequence
    from typing import TypeVar

    from pyavd._eos_designs.eos_designs_facts.schema import EosDesignsFactsProtocol

    from . import SharedUtilsProtocol

    ADAPTER_SETTINGS = TypeVar(
        "ADAPTER_SETTINGS", EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem.AdaptersItem, EosDesigns.NetworkPortsItem
    )

    T_ProtocolVrfs = TypeVar(
        "T_ProtocolVrfs",
        EosDesigns.DnsSettings.Vrfs,
        EosDesigns.LoggingSettings.Vrfs,
        EosDesigns.SflowSettings.Vrfs,
        EosDesigns.SnmpSettings.Vrfs,
        EosDesigns.AaaSettings.Tacacs.Vrfs,
        EosDesigns.AaaSettings.Radius.Vrfs,
    )


class UtilsMixin(Protocol):
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    resolved_port_profiles_cache: dict[str, EosDesigns.PortProfilesItem] | None = None
    """Poor-mans cache to only resolve and deepmerge a port_profile once."""

    @cached_property
    def switch_facts(self: SharedUtilsProtocol) -> EosDesignsFactsProtocol:
        return self.get_peer_facts(self.hostname)

    @overload
    def get_peer_facts(self: SharedUtilsProtocol, peer_name: str, required: Literal[True] = True) -> EosDesignsFactsProtocol: ...

    @overload
    def get_peer_facts(self: SharedUtilsProtocol, peer_name: str, required: Literal[False]) -> EosDesignsFactsProtocol | None: ...

    def get_peer_facts(self: SharedUtilsProtocol, peer_name: str, required: bool = True) -> EosDesignsFactsProtocol | None:
        """
        Util function to retrieve peer_facts for peer_name.

        returns avd_switch_facts.{peer_name}.switch

        by default required is True and so the function will raise is peer_facts cannot be found
        using the separator `..` to be able to handle hostnames with `.` inside
        """
        if peer_name not in self.peer_facts:
            if not required:
                return None
            msg = (
                f"Facts not found for node '{peer_name}'. Something in the input vars is pointing to this node. "
                f"Check that '{peer_name}' is in the inventory and is part of the group set by 'fabric_name'. Node is required."
            )
            raise AristaAvdInvalidInputsError(msg)
        return self.peer_facts[peer_name]

    def template_var(self: SharedUtilsProtocol, template_file: str, template_vars: MutableMapping) -> str:
        """Run the simplified templater using the passed Ansible "templar" engine."""
        try:
            return template_var(template_file, template_vars, self.templar)
        except Exception as e:
            msg = f"Error during templating of template: {template_file}"
            raise AristaAvdError(msg) from e

    def get_merged_port_profile(self: SharedUtilsProtocol, profile_name: str, context: str) -> EosDesigns.PortProfilesItem:
        """
        Returns a merged "port_profile" where "parent_profile" has been applied.

        Leverages a dict of resolved profiles as a cache.
        """
        if self.resolved_port_profiles_cache and profile_name in self.resolved_port_profiles_cache:
            return self.resolved_port_profiles_cache[profile_name]

        resolved_profile = self.resolve_port_profile(profile_name, context)

        # Update the cache so we don't resolve again next time.
        if self.resolved_port_profiles_cache is None:
            self.resolved_port_profiles_cache = {}
        self.resolved_port_profiles_cache[profile_name] = resolved_profile

        return resolved_profile

    def resolve_port_profile(self: SharedUtilsProtocol, profile_name: str, context: str) -> EosDesigns.PortProfilesItem:
        """Resolve one port-profile and return it."""
        if profile_name not in self.inputs.port_profiles:
            msg = f"Profile '{profile_name}' applied under '{context}' does not exist in `port_profiles`."
            raise AristaAvdInvalidInputsError(msg)

        port_profile = self.inputs.port_profiles[profile_name]
        if port_profile.parent_profile:
            if port_profile.parent_profile not in self.inputs.port_profiles:
                msg = f"Profile '{port_profile.parent_profile}' applied under port profile '{profile_name}' does not exist in `port_profiles`."
                raise AristaAvdInvalidInputsError(msg)

            parent_profile = self.inputs.port_profiles[port_profile.parent_profile]

            # Notice reuse of the same variable with the merged content.
            port_profile = port_profile._deepinherited(parent_profile)

        delattr(port_profile, "parent_profile")

        return port_profile

    def get_merged_adapter_settings(self: SharedUtilsProtocol, adapter_or_network_port_settings: ADAPTER_SETTINGS) -> ADAPTER_SETTINGS:
        """
        Applies port-profiles to the given adapter_or_network_port and returns the combined result.

        Args:
            adapter_or_network_port_settings: can either be an adapter of a connected endpoint or one item under network_ports.
        """
        # Deepcopy to avoid modifying the original.
        adapter_or_network_port_settings = adapter_or_network_port_settings._deepcopy()

        if (profile_name := adapter_or_network_port_settings.profile) is None:
            # No profile to apply
            return adapter_or_network_port_settings

        adapter_profile = self.get_merged_port_profile(profile_name, adapter_or_network_port_settings._internal_data.context)

        # Need this to assist the type checker.
        if isinstance(adapter_or_network_port_settings, EosDesigns.NetworkPortsItem):  # NOSONAR(S3923)
            profile_as_adapter_or_network_port_settings = adapter_profile._cast_as(type(adapter_or_network_port_settings))
            adapter_or_network_port_settings._deepinherit(profile_as_adapter_or_network_port_settings)
        else:
            profile_as_adapter_or_network_port_settings = adapter_profile._cast_as(type(adapter_or_network_port_settings))
            adapter_or_network_port_settings._deepinherit(profile_as_adapter_or_network_port_settings)

        return adapter_or_network_port_settings

    def get_merged_individual_adapter_settings(
        self: SharedUtilsProtocol, adapter_or_network_port_settings: ADAPTER_SETTINGS
    ) -> EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem.AdaptersItem | None:
        if not adapter_or_network_port_settings.port_channel.mode or adapter_or_network_port_settings.port_channel.lacp_fallback.mode != "individual":
            return None

        individual_adapter = adapter_or_network_port_settings.port_channel.lacp_fallback.individual._cast_as(
            EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem.AdaptersItem
        )
        individual_adapter._internal_data.context = f"{adapter_or_network_port_settings._internal_data.context}.port_channel.lacp_fallback.individual"
        return self.get_merged_adapter_settings(individual_adapter)

    def match_regexes(self: SharedUtilsProtocol, regexes: Iterable[str], value: str) -> bool:
        """
        Match a list of regexes with the supplied value.

        Regex must match the full value to pass.
        """
        return any(re.fullmatch(regex, value) for regex in regexes)

    def match_nodes(self: SharedUtilsProtocol, nodes: Sequence[str]) -> bool:
        """
        Returns True when nodes is empty.

        Otherwise returns self.match_regexes.
        """
        if not nodes:
            return True
        return self.match_regexes(nodes, self.hostname)

    @cached_property
    def underlay_vlan_trunk_groups(self: SharedUtilsProtocol) -> dict[int, set[str]]:
        """Return an EosCliConfigGen.Vlans object containing all the underlay VLAN with their trunk groups."""
        vlans: dict[int, set[str]] = {}
        for peer in self.switch_facts.downlink_switches:
            peer_facts = self.get_peer_facts(peer)
            for uplink in peer_facts.uplinks:
                if uplink.peer != self.hostname or not uplink.peer_trunk_groups or not uplink.vlans:
                    continue

                for vlan_id in map(int, range_expand(uplink.vlans)):
                    vlans.setdefault(vlan_id, set()).update(uplink.peer_trunk_groups)
                # No need to go through the other uplinks as the configuration is the same
                break
        return vlans

    def get_vrf_and_source_interface(
        self: SharedUtilsProtocol,
        vrf_input: str | None,
        vrfs: T_ProtocolVrfs,
        set_source_interfaces: bool,
        context: str,
    ) -> tuple[str, str | None]:
        """
        Helper function to interpret the VRF field for a management protocol.

        The value of `vrf` will be interpreted according to these rules:
        - `use_mgmt_interface_vrf` will return `(<mgmt_interface_vrf>, <vrfs[].source_interface or mgmt_interface>)`.
          An error will be raised if `mgmt_ip` or `ipv6_mgmt_ip` are not configured for the device.
        - `use_inband_mgmt_vrf` will return `(<inband_mgmt_vrf>, <vrfs[].source_interface or inband_mgmt_interface>)`.
          An error will be raised if inband management is not configured for the device.
        - `use_default_mgmt_method_vrf` will return one of the options above depending on the value of `default_mgmt_method`.
          If `default_mgmt_method: none` an error will be raised.
        - Any other string will return `(<vrf_input>, <vrfs[].source_interface or None)`

        Args:
            vrf_input: The VRF input value for one server.
            vrfs: The 'vrfs' input list with potential source interface overrides.
            set_source_interfaces: Automatically set source interface when VRF is set to `use_mgmt_interface_vrf` and `use_inband_mgmt_vrf`.
            context: The variable path for the vrf input used for error messages.

        Returns:
            VRF name
            Source Interface if available.

        Raises:
            AristaAvdInvalidInputsError raised by get_vrf() if conditions mentioned above are not met.
        """
        source_interface: str | None = None
        vrf = self.get_vrf(vrf_input, context=context)
        if set_source_interfaces:
            source_interface = self.get_source_interface(vrf_input, source_interface_override=vrfs[vrf].source_interface if vrf in vrfs else None)

        return (vrf, source_interface)

    def get_source_interface(self: SharedUtilsProtocol, vrf_input: str | None, source_interface_override: str | None) -> str | None:
        """Returns source interface for the given vrf, letting the given override take precedence."""
        if source_interface_override:
            return source_interface_override

        match vrf_input:
            case None | "" | "use_default_mgmt_method_vrf":
                return self.default_mgmt_protocol_interface
            case "use_mgmt_interface_vrf":
                return self.mgmt_interface
            case "use_inband_mgmt_vrf":
                return self.inband_mgmt_interface

    def get_vrf(
        self: SharedUtilsProtocol,
        vrf_input: str | None,
        context: str,
    ) -> str:
        """
        Helper function to interpret the VRF field for a management protocol.

        The value of `vrf` will be interpreted according to these rules:
        - `use_mgmt_interface_vrf` will return `(<mgmt_interface_vrf>, <vrfs[].source_interface or mgmt_interface>)`.
          An error will be raised if `mgmt_ip` or `ipv6_mgmt_ip` are not configured for the device.
        - `use_inband_mgmt_vrf` will return `(<inband_mgmt_vrf>, <vrfs[].source_interface or inband_mgmt_interface>)`.
          An error will be raised if inband management is not configured for the device.
        - `use_default_mgmt_method_vrf` will return one of the options above depending on the value of `default_mgmt_method`.
          If `default_mgmt_method: none` an error will be raised.
        - Any other string will be returned directly.

        Args:
            vrf_input: The VRF input value for one server.
            context: The variable path for the vrf input used for error messages.

        Returns:
            VRF name

        Raises:
            AristaAvdInvalidInputsError: If `vrf` is unset or set to `use_default_mgmt_method_vrf` and `default_mgmt_method` is set to 'none'.
            AristaAvdInvalidInputsError: If `vrf` is set to `use_mgmt_interface_vrf` and no `mgmt_ip` is set for this device.
            AristaAvdInvalidInputsError: If `vrf` is set to `use_inband_mgmt_vrf` and inband management is not configured for this device.
        """
        if not vrf_input or vrf_input == "use_default_mgmt_method_vrf":
            match self.inputs.default_mgmt_method:
                case "oob":
                    vrf_input = "use_mgmt_interface_vrf"
                case "inband":
                    vrf_input = "use_inband_mgmt_vrf"
                case "none":
                    msg = f"The VRF '{context}' must be set when 'default_mgmt_method' is set to 'none'. Use 'default' for the default VRF."
                    raise AristaAvdInvalidInputsError(msg)

        match vrf_input:
            case "use_mgmt_interface_vrf":
                has_mgmt_ip = (self.node_config.mgmt_ip is not None) or (self.node_config.ipv6_mgmt_ip is not None)
                if not has_mgmt_ip:
                    msg = f"'{context}' is set to 'use_mgmt_interface_vrf' but this node is missing 'mgmt_ip' or 'ipv6_mgmt_ip'."
                    raise AristaAvdInvalidInputsError(msg)

                return self.inputs.mgmt_interface_vrf
            case "use_inband_mgmt_vrf":
                if self.inband_mgmt_interface is None:
                    msg = f"'{context}' is set to 'use_inband_mgmt_vrf' but this node is missing configuration for inband management."
                    raise AristaAvdInvalidInputsError(msg)

                return self.inband_mgmt_vrf or "default"
            case _:
                return vrf_input

    def get_local_interface(self: SharedUtilsProtocol, input_interface: str | None) -> str | None:
        """
        Resolve and return the appropriate local interface.

        Given an `input_interface`, this function determines the corresponding local interface.
        If the input is None, empty, or one of the predefined keywords, it returns the relevant
        management or inband interface.
        Otherwise, the provided interface name is returned as-is.
        """
        match input_interface:
            case None | "" | "use_default_mgmt_method_interface":
                return self.default_mgmt_protocol_interface
            case "use_mgmt_interface":
                return self.mgmt_interface
            case "use_inband_mgmt_interface":
                return self.inband_mgmt_interface
        return input_interface
