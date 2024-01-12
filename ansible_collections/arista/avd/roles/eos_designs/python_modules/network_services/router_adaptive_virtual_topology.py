# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.strip_empties import strip_empties_from_dict
from ansible_collections.arista.avd.plugins.plugin_utils.utils import append_if_not_duplicate, get, get_item

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
            "vrfs": self._cv_pathfinder_wan_vrfs(),
            "policies": self._cv_pathfinder_policies(),
        }

        return strip_empties_from_dict(router_adaptive_virtual_topology)

    def _cv_pathfinder_wan_vrfs(self) -> list:
        """
        Return a list of WAN VRFs based on filtered tenants and the AVT.
        """
        # For CV Pathfinder, it is required to go through all the AVT profiles in the policy to assign an ID.
        wan_vrfs = []

        for vrf in self._filtered_wan_vrfs:
            wan_vrf = vrf.copy()

            # Need to allocate an ID for each profile in the policy, for now picked up from the input.
            policy = get_item(
                self._augmented_cv_pathfinder_policies,
                "name",
                wan_vrf[self._wan_policy_key],
                required=True,
                custom_error_msg=(
                    f"The policy {wan_vrf[self._wan_policy_key]} used in vrf {wan_vrf['name']} is not configured under 'wan_virtual_topologies.policies'."
                ),
            )

            for match in policy.get("matches", []):
                wan_vrf.setdefault("profiles", []).append(
                    {
                        "name": get(match, "avt_profile", required=True),
                        "id": get(match, "_id", required=False),
                    }
                )

            wan_vrfs.append(wan_vrf)

        return wan_vrfs

    @cached_property
    def _augmented_cv_pathfinder_policies(self) -> list:
        """
        Return a list of augmented CV_Pathfinder Policies with an `_id` key to be used when rendering VRFs.

        Insert the policy for default VRF using  {name}-WITH-CP
        """
        if not self.shared_utils.cv_pathfinder_role:
            return []

        cv_pathfinder_policies = []

        control_plane_virtual_topology = get(self._hostvars, "wan_virtual_topologies.control_plane_virtual_topology", default={"id": 254})

        for avt_policy in self._filtered_wan_policies:
            cv_pathfinder_policy = {
                "name": avt_policy["name"],
                "matches": [],
            }

            if get(avt_policy, "is_default", default=False):
                # Update policy name
                cv_pathfinder_policy["name"] = f"{cv_pathfinder_policy['name']}-WITH-CP"
                cv_pathfinder_policy["matches"].append(
                    {
                        "application_profile": "CONTROL-PLANE-APPLICATION-PROFILE",
                        "avt_profile": self._wan_control_plane_profile,
                        "traffic_class": get(control_plane_virtual_topology, "traffic_class"),
                        "dscp": get(control_plane_virtual_topology, "dscp"),
                        "_id": 254,
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

            default_virtual_topology = get(avt_policy, "default_virtual_topology", required=True)
            if not get(default_virtual_topology, "drop_unmatched", default=False):
                cv_pathfinder_policy["matches"].append(
                    {
                        "application_profile": get(default_virtual_topology, "application_profile", default="default"),
                        "avt_profile": get(default_virtual_topology, "name", default=f"{avt_policy['name']}_default"),
                        "traffic_class": get(default_virtual_topology, "traffic_class"),
                        "dscp": get(default_virtual_topology, "dscp"),
                        # Storing id as _id to avoid schema validation and be able to pick up in VRFs
                        "_id": 1,
                    }
                )

            cv_pathfinder_policies.append(cv_pathfinder_policy)

        return cv_pathfinder_policies

    def _cv_pathfinder_policies(self) -> list:
        """
        Return the policies generated by _augmented_cv_pathfinder_policies popping the `_id` key
        """
        policies = []
        for policy in self._augmented_cv_pathfinder_policies:
            new_policy = policy.copy()
            for match in get(policy, "matches", default=[]):
                match.pop("_id")
            policies.append(new_policy)
        return policies

    @cached_property
    def _cv_pathfinder_profiles(self) -> list:
        """
        Return a list of router adaptive-virtual-topology profiles for this router.

        TODO: add internet exit once supported
        """
        if not self.shared_utils.cv_pathfinder_role:
            return []

        # Control Plan profile
        cv_pathfinder_profiles = [{"name": self._wan_control_plane_profile, "load_balance_policy": f"LB-{self._wan_control_plane_profile}"}]
        for avt_policy in self._filtered_wan_policies:
            for application_virtual_topology in get(avt_policy, "application_virtual_topologies", []):
                name = get(application_virtual_topology, "name", default=f"{avt_policy['name']}_{application_virtual_topology['application_profile']}")
                append_if_not_duplicate(
                    list_of_dicts=cv_pathfinder_profiles,
                    primary_key="name",
                    new_dict={
                        "name": name,
                        "load_balance_policy": f"LB-{name}",
                    },
                    context="Router Adaptive Virtual Topology profiles.",
                    context_keys=["name"],
                )
            default_virtual_topology = get(avt_policy, "default_virtual_topology", required=True)
            if not get(default_virtual_topology, "drop_unmatched", default=False):
                name = get(default_virtual_topology, "name", default=f"{avt_policy['name']}_default")
                append_if_not_duplicate(
                    list_of_dicts=cv_pathfinder_profiles,
                    primary_key="name",
                    new_dict={
                        "name": name,
                        "load_balance_policy": f"LB-{name}",
                    },
                    context="Router Adaptive Virtual Topology profiles.",
                    context_keys=["name"],
                )

        return cv_pathfinder_profiles
