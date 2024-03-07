# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError
from ansible_collections.arista.avd.plugins.plugin_utils.strip_empties import strip_empties_from_dict
from ansible_collections.arista.avd.plugins.plugin_utils.utils import append_if_not_duplicate, get, get_item

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

        if not self.shared_utils.is_wan_router:
            return None

        router_path_selection = {
            "load_balance_policies": self._wan_load_balance_policies(),
        }

        # When running CV Pathfinder, only load balance policies are configured
        # for AutoVPN, need also vrfs and policies.
        if self.shared_utils.wan_mode == "autovpn":
            vrfs = [{"name": vrf["name"], "path_selection_policy": vrf["policy"]} for vrf in self._filtered_wan_vrfs]

            router_path_selection.update(
                {
                    "policies": self._autovpn_policies(),
                    "vrfs": vrfs,
                }
            )

        return strip_empties_from_dict(router_path_selection)

    def _wan_load_balance_policies(self) -> list:
        """
        Return a list of WAN router path-selection load-balance policies based on the local path-groups.
        """
        if not self.shared_utils.is_wan_router:
            return []

        wan_load_balance_policies = []

        for policy in self._filtered_wan_policies:
            if get(policy, "is_default", default=False):
                # for the default policy, need to render the control_plane_virtual_topology
                # Control plane Load Balancing policy - if not configured, render the default one.
                control_plane_virtual_topology = get(
                    self._hostvars,
                    "wan_virtual_topologies.control_plane_virtual_topology",
                    default=self._default_control_plane_virtual_topology,
                )

                wan_load_balance_policies.append(
                    self._generate_wan_load_balance_policy(
                        self.shared_utils.generate_lb_policy_name(self._wan_control_plane_profile),
                        control_plane_virtual_topology,
                        policy["name"],
                    )
                )

            for application_virtual_topology in get(policy, "application_virtual_topologies", []):
                # TODO add internet exit once supported
                name = get(
                    application_virtual_topology,
                    "name",
                    default=self._default_profile_name(policy["profile_prefix"], application_virtual_topology["application_profile"]),
                )
                context_path = (
                    f"wan_virtual_topologies.policies[{policy['profile_prefix']}]."
                    f"application_virtual_topologies[{application_virtual_topology['application_profile']}]"
                )
                append_if_not_duplicate(
                    list_of_dicts=wan_load_balance_policies,
                    primary_key="name",
                    new_dict=self._generate_wan_load_balance_policy(
                        self.shared_utils.generate_lb_policy_name(name), application_virtual_topology, context_path
                    ),
                    context="Router Path-Selection Load-Balance policies.",
                    context_keys=["name"],
                )

            default_virtual_topology = get(
                policy,
                "default_virtual_topology",
                required=True,
                org_key=f"wan_virtual_topologies.policies[{policy['profile_prefix']}].default_virtual_toplogy",
            )
            if not get(default_virtual_topology, "drop_unmatched", default=False):
                name = get(default_virtual_topology, "name", default=self._default_profile_name(policy["profile_prefix"], "DEFAULT"))
                context_path = f"wan_virtual_topologies.policies[{policy['profile_prefix']}].default_virtual_topology"

                # Verify that path_groups are set or raise
                get(
                    default_virtual_topology,
                    "path_groups",
                    required=True,
                    org_key=f"Either 'drop_unmatched' or 'path_groups' must be set under '{context_path}'.",
                )

                append_if_not_duplicate(
                    list_of_dicts=wan_load_balance_policies,
                    primary_key="name",
                    new_dict=self._generate_wan_load_balance_policy(self.shared_utils.generate_lb_policy_name(name), default_virtual_topology, context_path),
                    context="Router Path-Selection Load-Balance policies.",
                    context_keys=["name"],
                )

        return wan_load_balance_policies

    def _generate_wan_load_balance_policy(self, name: str, input_dict: dict, context_path: str) -> dict:
        """
        Generate and return a router path-selection load-balance policy.
        If HA is enabled, inject the HA path-group with priority 1.

        Attrs:
        ------
        name (str): The name of the load balance policy
        input_dict (dict): The dictionary containing the list of path-groups and their preference.
        context_path (str): Key used for context for error messages.
        """
        wan_load_balance_policy = {
            "name": name,
            "path_groups": [],
            **get(input_dict, "constraints", default={}),
        }

        local_path_groups_names = [path_group["name"] for path_group in self.shared_utils.wan_local_path_groups]

        if self.shared_utils.wan_mode == "cv-pathfinder":
            wan_load_balance_policy["lowest_hop_count"] = get(input_dict, "lowest_hop_count")

        if self.shared_utils.wan_ha or self.shared_utils.is_cv_pathfinder_server:
            # Adding HA path-group with priority 1 - it does not count as an entry with priority 1
            wan_load_balance_policy["path_groups"].append({"name": self.shared_utils.wan_ha_path_group_name})

        # An entry is composed of a list of path-groups in `names` and a `priority`
        policy_entries = get(input_dict, "path_groups", [])

        for policy_entry in policy_entries:
            policy_entry_priority = None
            if preference := get(policy_entry, "preference"):
                policy_entry_priority = self._path_group_preference_to_eos_priority(preference, f"{context_path}[{policy_entry.get('names')}]")

            for path_group_name in policy_entry.get("names"):
                if (priority := policy_entry_priority) is None:
                    # No preference defined at the policy level, need to retrieve the default preference
                    wan_path_group = get_item(
                        self.shared_utils.wan_path_groups,
                        "name",
                        path_group_name,
                        required=True,
                        custom_error_msg=(
                            f"Failed to retrieve path-group {path_group_name} from `wan_path_groups` when generating load balance policy {name}. "
                            f"Verify the path-groups defined under {context_path}."
                        ),
                    )
                    priority = self._path_group_preference_to_eos_priority(wan_path_group["default_preference"], f"wan_path_groups[{wan_path_group['name']}]")

                # Skip path-group on this device if not present on the router except for pathfinders
                if self.shared_utils.is_wan_client and path_group_name not in local_path_groups_names:
                    continue

                path_group = {
                    "name": path_group_name,
                    "priority": priority if priority != 1 else None,
                }

                wan_load_balance_policy["path_groups"].append(path_group)

        return wan_load_balance_policy

    def _path_group_preference_to_eos_priority(self, path_group_preference: int | str, context_path: str) -> int:
        """
        Convert "preferred" to 1 and "alternate" to 2. Everything else is returned as is.

        Arguments:
        ----------
        path_group_preference (str|int): The value of the preference key to be converted. It must be either "preferred", "alternate" or an integer.
        context_path (str): Input path context for the error message.
        """
        if path_group_preference == "preferred":
            return 1
        if path_group_preference == "alternate":
            return 2

        failed_conversion = False
        try:
            priority = int(path_group_preference)
        except ValueError:
            failed_conversion = True

        if failed_conversion or not (1 <= priority <= 65535):
            raise AristaAvdError(
                f"Invalid value '{path_group_preference}' for Path-Group preference - should be either 'preferred', "
                f"'alternate' or an integer[1-65535] for {context_path}."
            )

        return priority

    def _autovpn_policies(self) -> list:
        """
        Return a list of AutoVPN Policies.
        """
        autovpn_policies = []

        for policy in self._filtered_wan_policies:
            rule_id_offset = 0
            autovpn_policy = {
                "name": policy["name"],
            }

            if get(policy, "is_default", default=False):
                autovpn_policy.setdefault("rules", []).append(
                    {
                        "id": 10,
                        "application_profile": self._wan_control_plane_application_profile,
                        "load_balance": self.shared_utils.generate_lb_policy_name(self._wan_control_plane_profile),
                    }
                )
                rule_id_offset = 1

            for rule_id, application_virtual_topology in enumerate(get(policy, "application_virtual_topologies", []), start=1):
                name = get(
                    application_virtual_topology,
                    "name",
                    default=self._default_profile_name(policy["profile_prefix"], application_virtual_topology["application_profile"]),
                )
                application_profile = get(application_virtual_topology, "application_profile", required=True)
                autovpn_policy.setdefault("rules", []).append(
                    {
                        "id": 10 * (rule_id + rule_id_offset),
                        "application_profile": application_profile,
                        "load_balance": self.shared_utils.generate_lb_policy_name(name),
                    }
                )
            default_virtual_topology = get(policy, "default_virtual_topology", required=True)
            if not get(default_virtual_topology, "drop_unmatched", default=False):
                name = get(
                    default_virtual_topology,
                    "name",
                    default=self._default_profile_name(policy["profile_prefix"], "DEFAULT"),
                )
                autovpn_policy["default_match"] = {"load_balance": self.shared_utils.generate_lb_policy_name(name)}

            autovpn_policies.append(autovpn_policy)

        return autovpn_policies
