# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from ansible_collections.arista.avd.plugins.plugin_utils.merge import merge
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get, get_item

if TYPE_CHECKING:
    from .shared_utils import SharedUtils


# TODO only handle l3_edge for now need to look at core_interfaces too
class L3EdgeMixin:
    """
    Mixin Class providing a subset of SharedUtils
    Class should only be used as Mixin to the SharedUtils class
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    def _apply_profile(self: SharedUtils, target_dict: dict) -> dict:
        """
        Apply a profile to a p2p_link or a l3_interface
        """
        if "profile" not in target_dict:
            # Nothing to do
            return target_dict

        profiles = get(self.hostvars, "l3_edge.l3_interfaces_profiles", default=[])
        profile = get_item(profiles, "profile", target_dict["profile"], default={})

        target_dict = merge(profile, target_dict, list_merge="replace", destructive_merge=False)

        target_dict.pop("profile", None)

        return target_dict

    @cached_property
    def filtered_l3_interfaces(self: SharedUtils) -> list:
        """
        Returns a filtered list of l3_interfaces, which only contains interfaces with our hostname.
        For each interface any referenced profiles are applied.
        """
        if not (l3_interfaces := get(self.hostvars, "l3_edge.l3_interfaces", default=[])):
            return []

        l3_interfaces = [self._apply_profile(l3_interface) for l3_interface in l3_interfaces]

        # Filter to only include l3_interfaces with our hostname as node
        return [l3_interface for l3_interface in l3_interfaces if self.hostname == get(l3_interface, "node", required=True)]
