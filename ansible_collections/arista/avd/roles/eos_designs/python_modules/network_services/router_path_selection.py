# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.strip_empties import strip_empties_from_dict

from .utils import UtilsMixin


class RouterPathSelectionMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def router_path_selection(self) -> dict | None:
        """
        Return structured config for router path-selection (DPS)
        """

        if not self.shared_utils.wan_role:
            return None

        router_path_selection = {
            "load_balance_policies": self._wan_load_balance_policies,
        }

        # When running CV Pathfinder, only load balance policies
        if self.shared_utils.cv_pathfinder_role:
            return strip_empties_from_dict(router_path_selection)

        router_path_selection.update(
            {
                "policies": self._autovpn_policies,
                "vrfs": self._wan_vrfs,
            }
        )

        return strip_empties_from_dict(router_path_selection)
