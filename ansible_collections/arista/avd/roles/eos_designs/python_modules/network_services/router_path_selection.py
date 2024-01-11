# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.strip_empties import strip_empties_from_dict
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get

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

    @cached_property
    def _autovpn_policies(self) -> list:
        """
        Return a list of AutoVPN Policies.
        """
        if self.shared_utils.cv_pathfinder_role:
            return []

        autovpn_policies = []

        for policy in self._filtered_wan_policies:
            rule_id_offset = 0
            autovpn_policy = {
                "name": policy["name"],
            }

            policy_name = policy["name"]
            # TODO check if this is not possible to move this check in the self._default_vrf_policy generation
            if policy_name == self._default_vrf_policy["name"]:
                control_plane_virtual_topology = get(self._hostvars, "wan_virtual_topologies.control_plane_virtual_topology", default={})
                name = get(control_plane_virtual_topology, "name", default="CONTROL-PLANE-PROFILE")
                # This is the policy for the default VRF, inject control_plane_policy Profile first
                # TODO - this is a problem is the VRF default policy is reused in other place ..
                # TODO centralize the default value of the CONTROL-PLANE-PROFILE to avoid having the constant in two places..
                autovpn_policy.setdefault("rules", []).append(
                    {
                        "id": 10,
                        "application_profile": "CONTROL-PLANE-APPLICATION-PROFILE",
                        "load_balance": f"{name}_LB",
                    }
                )
                rule_id_offset = 1
                # Use the real name for shared LB policies
                policy_name = policy["realname"]

            for rule_id, application_virtual_topology in enumerate(get(policy, "application_virtual_topologies", []), start=1):
                name = get(application_virtual_topology, "name", default=f"{policy_name}_{application_virtual_topology['application_profile']}")
                autovpn_policy.setdefault("rules", []).append(
                    {
                        "id": 10 * (rule_id + rule_id_offset),
                        "application_profile": get(application_virtual_topology, "application_profile", required=True),
                        "load_balance": f"{name}_LB",
                    }
                )
            if (default_virtual_topology := get(policy, "default_virtual_topology")) is not None:
                name = get(default_virtual_topology, "name", default=f"{policy['name']}_default")
                autovpn_policy["default_match"] = {"load_balance": f"{name}_LB"}

            autovpn_policies.append(autovpn_policy)

        return autovpn_policies
