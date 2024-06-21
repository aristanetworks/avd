# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from ..._utils import get, get_item, merge

if TYPE_CHECKING:
    from . import SharedUtils


class L3InterfacesMixin:
    """
    Mixin Class providing a subset of SharedUtils
    Class should only be used as Mixin to the SharedUtils class
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    def sanitize_interface_name(self: SharedUtils, interface_name: str) -> str:
        """
        Interface name is used as value for certain fields, but `/` are not allowed in the value.

        So we transform `/` to `_`
        Ethernet1/1.1 is transformed into Ethernet1_1.1
        """
        return interface_name.replace("/", "_")

    def apply_l3_interfaces_profile(self: SharedUtils, l3_interface: dict) -> dict:
        """
        Apply a profile to an l3_interface
        """
        if "profile" not in l3_interface:
            # Nothing to do
            return l3_interface

        profile = get_item(self.l3_interface_profiles, "profile", l3_interface["profile"], default={})
        merged_dict: dict = merge(profile, l3_interface, list_merge="replace", destructive_merge=False)
        merged_dict.pop("profile", None)
        return merged_dict

    @cached_property
    def l3_interface_profiles(self: SharedUtils) -> list:
        return get(self.hostvars, "l3_interface_profiles", default=[])

    # TODO: Add sflow knob under fabric_sflow to cover l3_interfaces defined under the node_types.
    # @cached_property
    # def _l3_interfaces_sflow(self) -> bool | None:
    #     return get(self._hostvars, f"fabric_sflow.{self.data_model}")

    @cached_property
    def l3_interfaces(self: SharedUtils) -> list:
        """
        Returns the list of l3_interfaces, where any referenced profiles are applied.
        """
        if not (l3_interfaces := get(self.switch_data_combined, "l3_interfaces")):
            return []

        # Apply l3_interfaces._profile if set. Silently ignoring missing profile.
        if self.l3_interface_profiles:
            l3_interfaces = [self.apply_l3_interfaces_profile(l3_interface) for l3_interface in l3_interfaces]

        return l3_interfaces
