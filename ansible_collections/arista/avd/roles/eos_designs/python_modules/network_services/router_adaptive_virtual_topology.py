# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.strip_empties import strip_empties_from_dict
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get

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

    @cached_property
    def _cv_pathfinder_policies(self) -> list:
        """
        Return a list of CV_Pathfinder Policies.
        Does not render any policy for AutoVPN
        """
        if not self.shared_utils.cv_pathfinder_role:
            return []

        cv_pathfinder_policies = []

        control_plane_virtual_topology = get(self._hostvars, "wan_virtual_topologies.control_plane_virtual_topology", default={"id": 254})

        for avt_policy in get(self._hostvars, "wan_virtual_topologies.policies", []):
            cv_pathfinder_policy = {
                "name": avt_policy["name"],
                "matches": [],
            }

            if avt_policy["name"] == self._get_default_vrf_policy():
                # This is the policy for the default VRF, inject control_plane_policy Profile first
                # TODO - this is a problem is the VRF default policy is reused in other place ..
                # TODO centralize the default value of the CONTROL-PLANE-PROFILE to avoid having the constant in two places..
                cv_pathfinder_policy["matches"].append(
                    {
                        "application_profile": "CONTROL-PLANE-APPLICATION-PROFILE",
                        "avt_profile": get(control_plane_virtual_topology, "name", default="CONTROL-PLANE-PROFILE"),
                        "traffic_class": get(control_plane_virtual_topology, "traffic_class"),
                        "dscp": get(control_plane_virtual_topology, "dscp"),
                        # Storing id as _id to avoid schema validation and be able to pick up in VRFs
                        "_id": get(control_plane_virtual_topology, "id"),
                    }
                )

            for application_virtual_topology in get(avt_policy, "application_virtual_topologies", []):
                cv_pathfinder_policy["matches"].append(
                    {
                        "application_profile": get(application_virtual_topology, "application_profile", required=True),
                        "avt_profile": get(
                            application_virtual_topology, "name", default=f"{avt_policy['name']}_{application_virtual_topology['application_profile']}"
                        ),
                        "traffic_class": get(application_virtual_topology, "traffic_class"),
                        "dscp": get(application_virtual_topology, "dscp"),
                        # Storing id as _id to avoid schema validation and be able to pick up in VRFs
                        "_id": get(application_virtual_topology, "id"),
                    }
                )
            if (default_virtual_topology := get(avt_policy, "default_virtual_topology")) is not None:
                cv_pathfinder_policy["matches"].append(
                    {
                        "application_profile": get(default_virtual_topology, "application_profile", default="default"),
                        "avt_profile": get(default_virtual_topology, "name", default=f"{avt_policy['name']}_default"),
                        "traffic_class": get(default_virtual_topology, "traffic_class"),
                        "dscp": get(default_virtual_topology, "dscp"),
                        # Storing id as _id to avoid schema validation and be able to pick up in VRFs
                        "_id": get(default_virtual_topology, "id"),
                    }
                )

            cv_pathfinder_policies.append(cv_pathfinder_policy)

        return cv_pathfinder_policies

    @cached_property
    def _cv_pathfinder_profiles(self) -> list:
        """
        Return a list of router adaptive-virtual-topology profiles for this router.

        TODO: add internet exit once supported
        """
        if not self.shared_utils.cv_pathfinder_role:
            return []

        cv_pathfinder_profiles = []

        # Control Plan profile
        control_plane_virtual_topology = get(self._hostvars, "wan_virtual_topologies.control_plane_virtual_topology", {})
        name = get(control_plane_virtual_topology, "name", default="CONTROL-PLANE-PROFILE")
        cv_pathfinder_profiles.append(
            {
                "name": name,
                "load_balance_policy": f"{name}_lb",
            }
        )

        for avt_policy in get(self._hostvars, "wan_virtual_topologies.policies", []):
            for application_virtual_topology in get(avt_policy, "application_virtual_topologies", []):
                name = get(application_virtual_topology, "name", default=f"{avt_policy['name']}_{application_virtual_topology['application_profile']}")
                cv_pathfinder_profiles.append(
                    {
                        "name": name,
                        "load_balance_policy": f"{name}_lb",
                    }
                )
            if default_virtual_topology := get(avt_policy, "default_virtual_topology"):
                name = get(default_virtual_topology, "name", default=f"{avt_policy['name']}_default")
                cv_pathfinder_profiles.append(
                    {
                        "name": name,
                        "load_balance_policy": f"{name}_lb",
                    }
                )

        return cv_pathfinder_profiles
