# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.strip_empties import strip_empties_from_dict

from .utils import UtilsMixin


class RouterAdaptiveVirtualTopologyMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def router_adaptive_virtual_topology(self) -> dict | None:
        """
        Return structured config for profiles, policies and VRFs for router adaptive-virtual-topology (AVT)
        """
        if not self.shared_utils.cv_pathfinder_role:
            return None

        router_adaptive_virtual_topology = {
            "profiles": self._cv_pathfinder_profiles,
            "policies": self._cv_pathfinder_policies,
            "vrfs": self._wan_vrfs,
        }

        return strip_empties_from_dict(router_adaptive_virtual_topology)
