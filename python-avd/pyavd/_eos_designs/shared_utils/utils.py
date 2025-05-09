# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Literal, Protocol, overload

from pyavd._errors import AristaAvdError, AristaAvdInvalidInputsError
from pyavd._utils import template_var

if TYPE_CHECKING:
    from typing import TypeVar

    from pyavd._eos_designs.eos_designs_facts.schema import EosDesignsFactsProtocol
    from pyavd._eos_designs.schema import EosDesigns

    from . import SharedUtilsProtocol

    ADAPTER_SETTINGS = TypeVar(
        "ADAPTER_SETTINGS", EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem.AdaptersItem, EosDesigns.NetworkPortsItem
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

    def template_var(self: SharedUtilsProtocol, template_file: str, template_vars: dict) -> str:
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
        profile_as_adapter_or_network_port_settings = adapter_profile._cast_as(type(adapter_or_network_port_settings))
        adapter_or_network_port_settings._deepinherit(profile_as_adapter_or_network_port_settings)
        return adapter_or_network_port_settings
