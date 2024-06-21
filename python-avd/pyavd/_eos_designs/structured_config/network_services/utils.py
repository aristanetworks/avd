# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import ipaddress
from functools import cached_property
from typing import TYPE_CHECKING, Literal, Tuple

from ...._errors import AristaAvdError, AristaAvdMissingVariableError
from ...._utils import default, get, get_item
from ...._utils.password_utils.password import simple_7_encrypt
from ....j2filters import natural_sort, range_expand
from .utils_zscaler import UtilsZscalerMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServices


class UtilsMixin(UtilsZscalerMixin):
    """
    Mixin Class with internal functions.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def _trunk_groups_mlag_name(self: AvdStructuredConfigNetworkServices) -> str:
        return get(self.shared_utils.trunk_groups, "mlag.name", required=True)

    @cached_property
    def _trunk_groups_mlag_l3_name(self: AvdStructuredConfigNetworkServices) -> str:
        return get(self.shared_utils.trunk_groups, "mlag_l3.name", required=True)

    @cached_property
    def _trunk_groups_uplink_name(self: AvdStructuredConfigNetworkServices) -> str:
        return get(self.shared_utils.trunk_groups, "uplink.name", required=True)

    @cached_property
    def _local_endpoint_trunk_groups(self: AvdStructuredConfigNetworkServices) -> set:
        return set(get(self._hostvars, "switch.local_endpoint_trunk_groups", default=[]))

    @cached_property
    def _vrf_default_evpn(self: AvdStructuredConfigNetworkServices) -> bool:
        """
        Return boolean telling if VRF "default" is running EVPN or not.
        """
        if not (self.shared_utils.network_services_l3 and self.shared_utils.overlay_vtep and self.shared_utils.overlay_evpn):
            return False

        for tenant in self.shared_utils.filtered_tenants:
            if (vrf_default := get_item(tenant["vrfs"], "name", "default")) is None:
                continue

            if "evpn" in vrf_default.get("address_families", ["evpn"]):
                if self.shared_utils.underlay_filter_peer_as:
                    raise AristaAvdError("'underlay_filter_peer_as' cannot be used while there are EVPN services in the default VRF.")
                return True

        return False

    @cached_property
    def _vrf_default_ipv4_subnets(self: AvdStructuredConfigNetworkServices) -> list[str]:
        """
        Return list of ipv4 subnets in VRF "default"
        """
        subnets = []
        for tenant in self.shared_utils.filtered_tenants:
            if (vrf_default := get_item(tenant["vrfs"], "name", "default")) is None:
                continue

            for svi in vrf_default["svis"]:
                ip_address = default(svi.get("ip_address"), svi.get("ip_address_virtual"))
                if ip_address is None:
                    continue

                subnet = str(ipaddress.ip_network(ip_address, strict=False))
                if subnet not in subnets:
                    subnets.append(subnet)

        return subnets

    @cached_property
    def _vrf_default_ipv4_static_routes(self: AvdStructuredConfigNetworkServices) -> dict:
        """
        Finds static routes defined under VRF "default" and find out if they should be redistributed in underlay and/or overlay.

        Returns
        -------
        dict
            static_routes: []
                List of ipv4 static routes in VRF "default"
            redistribute_in_underlay: bool
                Whether to redistribute static into the underlay protocol.
                True when there are any static routes this device is not an EVPN VTEP.
                Can be overridden with "vrf.redistribute_static: False".
            redistribute_in_overlay: bool
                Whether to redistribute static into overlay protocol for vrf default.
                True there are any static routes and this device is an EVPN VTEP.
                Can be overridden with "vrf.redistribute_static: False".
        """
        vrf_default_ipv4_static_routes = set()
        vrf_default_redistribute_static = True
        for tenant in self.shared_utils.filtered_tenants:
            if (vrf_default := get_item(tenant["vrfs"], "name", "default")) is None:
                continue

            if (static_routes := vrf_default.get("static_routes")) is None:
                continue

            for static_route in static_routes:
                vrf_default_ipv4_static_routes.add(static_route["destination_address_prefix"])

            vrf_default_redistribute_static = vrf_default.get("redistribute_static", vrf_default_redistribute_static)

        if self.shared_utils.overlay_evpn and self.shared_utils.overlay_vtep:
            # This is an EVPN VTEP
            redistribute_in_underlay = False
            redistribute_in_overlay = vrf_default_redistribute_static and vrf_default_ipv4_static_routes
        else:
            # This is a not an EVPN VTEP
            redistribute_in_underlay = vrf_default_redistribute_static and vrf_default_ipv4_static_routes
            redistribute_in_overlay = False

        return {
            "static_routes": natural_sort(vrf_default_ipv4_static_routes),
            "redistribute_in_underlay": redistribute_in_underlay,
            "redistribute_in_overlay": redistribute_in_overlay,
        }

    def _mlag_ibgp_peering_enabled(self: AvdStructuredConfigNetworkServices, vrf, tenant) -> bool:
        """
        Returns True if mlag ibgp_peering is enabled
        False otherwise
        """
        if not self.shared_utils.mlag_l3 or not self.shared_utils.network_services_l3:
            return False

        mlag_ibgp_peering: bool = default(vrf.get("enable_mlag_ibgp_peering_vrfs"), tenant.get("enable_mlag_ibgp_peering_vrfs"), True)
        return vrf["name"] != "default" and mlag_ibgp_peering

    def _mlag_ibgp_peering_vlan_vrf(self: AvdStructuredConfigNetworkServices, vrf, tenant) -> int | None:
        """
        MLAG IBGP Peering VLANs per VRF

        Performs all relevant checks if MLAG IBGP Peering is enabled
        Returns None if peering is not enabled
        """
        if not self._mlag_ibgp_peering_enabled(vrf, tenant):
            return None

        if (mlag_ibgp_peering_vlan := get(vrf, "mlag_ibgp_peering_vlan")) is not None:
            vlan_id = mlag_ibgp_peering_vlan
        else:
            base_vlan = self.shared_utils.mlag_ibgp_peering_vrfs_base_vlan
            vrf_id = vrf.get("vrf_id", vrf.get("vrf_vni"))
            if vrf_id is None:
                raise AristaAvdMissingVariableError(
                    f"Unable to assign MLAG VRF Peering VLAN for vrf {vrf['name']}.Set either 'mlag_ibgp_peering_vlan' or 'vrf_id' or 'vrf_vni' on the VRF"
                )
            vlan_id = base_vlan + int(vrf_id) - 1

        return vlan_id

    def _mlag_ibgp_peering_redistribute(self: AvdStructuredConfigNetworkServices, vrf, tenant) -> bool:
        """
        Returns True if MLAG IBGP Peering subnet should be redistributed for the given vrf/tenant.
        False otherwise.

        Does _not_ include checks if the peering is enabled at all, so that should be checked first.
        """
        return default(vrf.get("redistribute_mlag_ibgp_peering_vrfs"), tenant.get("redistribute_mlag_ibgp_peering_vrfs"), True) is True

    @cached_property
    def _configure_bgp_mlag_peer_group(self: AvdStructuredConfigNetworkServices) -> bool:
        """
        Flag set during creating of BGP VRFs if an MLAG peering is needed.
        Decides if MLAG BGP peer-group should be configured.
        Catches cases where underlay is not BGP but we still need MLAG iBGP peering
        """
        if self.shared_utils.underlay_bgp or (bgp_vrfs := self._router_bgp_vrfs) is None:
            return False

        for bgp_vrf in bgp_vrfs:
            if "neighbors" not in bgp_vrf:
                continue
            for neighbor_settings in bgp_vrf["neighbors"]:
                if neighbor_settings.get("peer_group") == self.shared_utils.bgp_peer_groups["mlag_ipv4_underlay_peer"]["name"]:
                    return True

        return False

    @cached_property
    def _filtered_wan_vrfs(self: AvdStructuredConfigNetworkServices) -> list:
        """
        Loop through all the VRFs defined under `wan_virtual_topologies.vrfs` and returns a list of mode
        """
        wan_vrfs = []

        for vrf in get(self._hostvars, "wan_virtual_topologies.vrfs", []):
            vrf_name = vrf["name"]
            if vrf_name in self.shared_utils.vrfs or self.shared_utils.is_wan_server:
                wan_vrf = {
                    "name": vrf_name,
                    "policy": get(vrf, "policy", default=self._default_wan_policy_name),
                    "wan_vni": get(
                        vrf, "wan_vni", required=True, org_key=f"Required `wan_vni` is missing for VRF {vrf_name} under `wan_virtual_topologies.vrfs`."
                    ),
                }

                wan_vrfs.append(wan_vrf)

        # Check that default is in the list as it is required everywhere
        if (vrf_default := get_item(wan_vrfs, "name", "default")) is None:
            wan_vrfs.append(
                {
                    "name": "default",
                    "policy": f"{self._default_wan_policy_name}-WITH-CP",
                    "wan_vni": 1,
                    "original_policy": self._default_wan_policy_name,
                }
            )
        else:
            vrf_default["original_policy"] = vrf_default["policy"]
            vrf_default["policy"] = f"{vrf_default['policy']}-WITH-CP"

        return wan_vrfs

    @cached_property
    def _wan_virtual_topologies_policies(self: AvdStructuredConfigNetworkServices) -> list:
        """
        This function parses the input data and append the default-policy if not already present
        """
        policies = get(self._hostvars, "wan_virtual_topologies.policies", default=[])
        # If not overwritten, inject the default policy in case it is required for one of the VRFs
        if get_item(policies, "name", self._default_wan_policy_name) is None:
            policies.append(self._default_wan_policy)

        return policies

    @cached_property
    def _filtered_wan_policies(self: AvdStructuredConfigNetworkServices) -> list:
        """
        Loop through all the VRFs defined under `wan_virtual_topologies.vrfs` and returns a list of policies to configure on this device.

        This returns a structure where every policy contains a list of match statement and a default_match statement if any is required by inputs.
        Inside each match and default_match statetement, the fully resolved load_balancing policy is present (it guarantees that the load-balance policy
        is not empty).

        The default VRF is marked as non default.
        """
        # to track the names already injected
        filtered_policy_names = []
        filtered_policies = []

        for vrf in self._filtered_wan_vrfs:
            # Need to handle VRF default differently and lookup for the original policy
            lookup_name = get(vrf, "original_policy", default=vrf["policy"])
            vrf_policy = get_item(
                self._wan_virtual_topologies_policies,
                "name",
                lookup_name,
                required=True,
                custom_error_msg=(
                    f"The policy {lookup_name} applied to vrf {vrf['name']} under `wan_virtual_topologies.vrfs` is not "
                    "defined under `wan_virtual_topologies.policies`."
                ),
            ).copy()

            vrf_policy["profile_prefix"] = lookup_name

            if vrf["name"] == "default":
                vrf_policy["is_default"] = True
                vrf_policy["name"] = f"{vrf_policy['name']}-WITH-CP"

            if vrf_policy["name"] in filtered_policy_names:
                continue

            self._update_policy_match_statements(vrf_policy)

            filtered_policy_names.append(vrf_policy["name"])
            filtered_policies.append(vrf_policy)

        return filtered_policies

    def _update_policy_match_statements(self: AvdStructuredConfigNetworkServices, policy: dict) -> None:
        """
        Update the policy dict with two keys: `matches` and `default_match`
        For each match (or default_match), the load_balancing policy is resolved and if it is empty
        the match statement is not included.
        """
        matches = []

        if get(policy, "is_default", default=False):
            control_plane_virtual_topology = self._wan_control_plane_virtual_topology
            load_balance_policy_name = self.shared_utils.generate_lb_policy_name(self._wan_control_plane_profile_name)

            if (
                load_balance_policy := self._generate_wan_load_balance_policy(
                    load_balance_policy_name,
                    control_plane_virtual_topology,
                    policy["name"],
                )
            ) is None:
                raise AristaAvdError("The WAN control-plane load-balance policy is empty. Make sure at least one path-group can be used in the policy")
            matches.append(
                {
                    "application_profile": self._wan_control_plane_application_profile_name,
                    "avt_profile": self._wan_control_plane_profile_name,
                    "internet_exit_policy_name": get(control_plane_virtual_topology, "internet_exit.policy"),
                    "traffic_class": get(control_plane_virtual_topology, "traffic_class"),
                    "dscp": get(control_plane_virtual_topology, "dscp"),
                    "load_balance_policy": load_balance_policy,
                    "id": 254,
                }
            )

        for application_virtual_topology in get(policy, "application_virtual_topologies", []):
            name = get(
                application_virtual_topology,
                "name",
                default=self._default_profile_name(policy["profile_prefix"], application_virtual_topology["application_profile"]),
            )

            load_balance_policy_name = self.shared_utils.generate_lb_policy_name(name)
            context_path = (
                f"wan_virtual_topologies.policies[{policy['profile_prefix']}]."
                f"application_virtual_topologies[{application_virtual_topology['application_profile']}]"
            )
            load_balance_policy = self._generate_wan_load_balance_policy(load_balance_policy_name, application_virtual_topology, context_path)
            if not load_balance_policy:
                # Empty load balance policy so skipping
                # TODO: Add "nodes" or similar under the profile and raise here
                # if the node is set and there are no matching path groups.
                continue

            application_profile = get(application_virtual_topology, "application_profile", required=True)
            profile_id = get(
                application_virtual_topology,
                "id",
                required=self.shared_utils.is_cv_pathfinder_router,
                org_key=(
                    f"Missing mandatory `id` in "
                    f"`wan_virtual_topologies.policies[{policy['name']}].application_virtual_topologies[{application_profile}]` "
                    "when `wan_mode` is 'cv-pathfinder"
                ),
            )

            matches.append(
                {
                    "application_profile": application_profile,
                    "avt_profile": name,
                    "internet_exit_policy_name": get(application_virtual_topology, "internet_exit.policy"),
                    "traffic_class": get(application_virtual_topology, "traffic_class"),
                    "dscp": get(application_virtual_topology, "dscp"),
                    "load_balance_policy": load_balance_policy,
                    "id": profile_id,
                }
            )

        default_virtual_topology = get(
            policy, "default_virtual_topology", required=True, org_key=f"wan_virtual_topologies.policies[{policy['profile_prefix']}].default_virtual_toplogy"
        )
        # Separating default_match as it is used differently
        default_match = None
        if not get(default_virtual_topology, "drop_unmatched", default=False):
            name = get(
                default_virtual_topology,
                "name",
                default=self._default_profile_name(policy["profile_prefix"], "DEFAULT"),
            )
            context_path = f"wan_virtual_topologies.policies[{policy['profile_prefix']}].default_virtual_topology"
            # Verify that path_groups are set or raise
            get(
                default_virtual_topology,
                "path_groups",
                required=True,
                org_key=f"Either 'drop_unmatched' or 'path_groups' must be set under '{context_path}'.",
            )
            load_balance_policy_name = self.shared_utils.generate_lb_policy_name(name)
            load_balance_policy = self._generate_wan_load_balance_policy(load_balance_policy_name, default_virtual_topology, context_path)
            if not load_balance_policy:
                raise AristaAvdError(
                    f"The `default_virtual_topology` path-groups configuration for `wan_virtual_toplogies.policies[{policy['name']}]` produces "
                    "an empty load-balancing policy. Make sure at least one path-group present on the device is allowed in the "
                    "`default_virtual_topology` path-groups."
                )
            application_profile = get(default_virtual_topology, "application_profile", default="default")

            default_match = {
                "application_profile": application_profile,
                "avt_profile": name,
                "internet_exit_policy_name": get(default_virtual_topology, "internet_exit.policy"),
                "traffic_class": get(default_virtual_topology, "traffic_class"),
                "dscp": get(default_virtual_topology, "dscp"),
                "load_balance_policy": load_balance_policy,
                "id": 1,
            }

        if not matches and not default_match:
            # The policy is empty but should be assigned to a VRF
            raise AristaAvdError(
                f"The policy `wan_virtual_toplogies.policies[{policy['name']}]` cannot match any traffic but is assigned to a VRF. "
                "Make sure at least one path-group present on the device is used in the policy."
            )

        policy["matches"] = matches
        policy["default_match"] = default_match

    def _generate_wan_load_balance_policy(self: AvdStructuredConfigNetworkServices, name: str, input_dict: dict, context_path: str) -> dict | None:
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

        if self.shared_utils.wan_mode == "cv-pathfinder":
            wan_load_balance_policy["lowest_hop_count"] = get(input_dict, "lowest_hop_count")

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
                if self.shared_utils.is_wan_client and path_group_name not in self.shared_utils.wan_local_path_group_names:
                    continue

                path_group = {
                    "name": path_group_name,
                    "priority": priority if priority != 1 else None,
                }

                wan_load_balance_policy["path_groups"].append(path_group)

        if len(wan_load_balance_policy["path_groups"]) == 0:
            # The policy is empty
            return None

        # TODO for now adding LAN_HA only if the path-groups list is not empty
        # then need to add the logic to check HA peer path-group and maybe return a policy with LAN_HA only.
        if self.shared_utils.wan_ha or self.shared_utils.is_cv_pathfinder_server:
            # Adding HA path-group with priority 1 - it does not count as an entry with priority 1
            wan_load_balance_policy["path_groups"].append({"name": self.shared_utils.wan_ha_path_group_name})

        return wan_load_balance_policy

    def _path_group_preference_to_eos_priority(self: AvdStructuredConfigNetworkServices, path_group_preference: int | str, context_path: str) -> int:
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

        if failed_conversion or not 1 <= priority <= 65535:
            raise AristaAvdError(
                f"Invalid value '{path_group_preference}' for Path-Group preference - should be either 'preferred', "
                f"'alternate' or an integer[1-65535] for {context_path}."
            )

        return priority

    @cached_property
    def _default_wan_policy_name(self: AvdStructuredConfigNetworkServices) -> str:
        """
        TODO make this configurable
        """
        return "DEFAULT-POLICY"

    @cached_property
    def _default_policy_path_group_names(self: AvdStructuredConfigNetworkServices) -> list:
        """
        Return the list of path-groups to consider when generating a default policy with AVD
        whether for the default policy or the special Control-plane policy.
        """
        path_group_names = {
            path_group["name"] for path_group in self.shared_utils.wan_path_groups if not get(path_group, "excluded_from_default_policy", default=False)
        }
        if not path_group_names.intersection(self.shared_utils.wan_local_path_group_names):
            # No common path-group between this device local path-groups and the available path-group for the default policy
            raise AristaAvdError(
                f"Unable to generate the default WAN policy as none of the device local path-groups {self.shared_utils.wan_local_path_group_names} "
                "is eligible to be included. Make sure that at least one path-group for the device is not configured with "
                "`excluded_from_default_policy: true` under `wan_path_groups`."
            )
        return natural_sort(path_group_names)

    @cached_property
    def _default_wan_policy(self: AvdStructuredConfigNetworkServices) -> dict:
        """
        If no policy is defined for a VRF under 'wan_virtual_topologies.vrfs', a default policy named DEFAULT-POLICY is used
        where all traffic is matched in the default category and distributed amongst all path-groups.

        Returning policy containing all path groups not excluded from default policy.
        """

        return {
            "name": self._default_wan_policy_name,
            "default_virtual_topology": {"path_groups": [{"names": self._default_policy_path_group_names}]},
        }

    def _default_profile_name(self: AvdStructuredConfigNetworkServices, profile_name: str, application_profile: str) -> str:
        """
        Helper function to consistently return the default name of a profile

        Returns {profile_name}-{application_profile}
        """
        return f"{profile_name}-{application_profile}"

    @cached_property
    def _wan_control_plane_virtual_topology(self: AvdStructuredConfigNetworkServices) -> dict:
        """
        Return the Control plane virtual topology or the default one.

        The default control_plane_virtual_topology, excluding path_groups with excluded_from_default_policy
        """
        if (control_plane_virtual_topology := get(self._hostvars, "wan_virtual_topologies.control_plane_virtual_topology")) is None:
            path_groups = self._default_policy_path_group_names
            if self.shared_utils.is_wan_client:
                # Filter only the path-groups connected to pathfinder
                path_groups = [path_group for path_group in path_groups if path_group in self._local_path_groups_connected_to_pathfinder]
            control_plane_virtual_topology = {"path_groups": [{"names": path_groups}]}
        return control_plane_virtual_topology

    @cached_property
    def _wan_control_plane_profile_name(self: AvdStructuredConfigNetworkServices) -> str:
        """
        Control plane profile name
        """
        vrf_default_policy_name = get(get_item(self._filtered_wan_vrfs, "name", "default"), "original_policy")
        return get(self._wan_control_plane_virtual_topology, "name", default=f"{vrf_default_policy_name}-CONTROL-PLANE")

    @cached_property
    def _wan_control_plane_application_profile_name(self: AvdStructuredConfigNetworkServices) -> str:
        """
        Control plane application profile name
        """
        return get(self._hostvars, "wan_virtual_topologies.control_plane_virtual_topology.application_profile", default="APP-PROFILE-CONTROL-PLANE")

    @cached_property
    def _local_path_groups_connected_to_pathfinder(self: AvdStructuredConfigNetworkServices) -> list:
        """
        Return list of names of local path_groups connected to pathfinder
        """
        return [
            path_group["name"]
            for path_group in self.shared_utils.wan_local_path_groups
            if any(wan_interface["connected_to_pathfinder"] for wan_interface in path_group["interfaces"])
        ]

    def get_internet_exit_nat_profile_name(self: AvdStructuredConfigNetworkServices, internet_exit_policy_type: Literal["zscaler", "direct"]) -> str:
        if internet_exit_policy_type == "zscaler":
            return "IE-ZSCALER-NAT"

        return "IE-DIRECT-NAT"

    def get_internet_exit_nat_pool_and_profile(
        self: AvdStructuredConfigNetworkServices, internet_exit_policy_type: Literal["zscaler", "direct"]
    ) -> Tuple[dict | None, dict | None]:
        if internet_exit_policy_type == "zscaler":
            pool = {
                "name": "PORT-ONLY-POOL",
                "type": "port-only",
                "ranges": [
                    {
                        "first_port": 1500,
                        "last_port": 65535,
                    }
                ],
            }

            profile = {
                "name": self.get_internet_exit_nat_profile_name(internet_exit_policy_type),
                "source": {
                    "dynamic": [
                        {
                            "access_list": "ALLOW-ALL",
                            "pool_name": "PORT-ONLY-POOL",
                            "nat_type": "pool",
                        }
                    ]
                },
            }
            return pool, profile

        if internet_exit_policy_type == "direct":
            profile = {
                "name": self.get_internet_exit_nat_profile_name(internet_exit_policy_type),
                "source": {
                    "dynamic": [
                        {
                            "access_list": "ALLOW-ALL",
                            "nat_type": "overload",
                        }
                    ]
                },
            }
            return None, profile

        return None, None

    @cached_property
    def _svi_acls(self: AvdStructuredConfigNetworkServices) -> dict[str, dict[str, dict]] | None:
        """
        Returns a dict of
            <interface_name>: {
                "ipv4_acl_in": <generated_ipv4_acl>,
                "ipv4_acl_out": <generated_ipv4_acl>,
            }
        Only contains interfaces with ACLs and only the ACLs that are set,
        so use `get(self._svi_acls, f"{interface_name}.ipv4_acl_in")` to get the value.
        """
        if not self.shared_utils.network_services_l3:
            return None

        svi_acls = {}
        for tenant in self.shared_utils.filtered_tenants:
            for vrf in tenant["vrfs"]:
                for svi in vrf["svis"]:
                    ipv4_acl_in = get(svi, "ipv4_acl_in")
                    ipv4_acl_out = get(svi, "ipv4_acl_out")
                    if ipv4_acl_in is None and ipv4_acl_out is None:
                        continue

                    interface_name = f"Vlan{svi['id']}"
                    interface_ip: str | None = svi.get("ip_address_virtual")
                    if interface_ip is not None and "/" in interface_ip:
                        interface_ip = interface_ip.split("/", maxsplit=1)[0]

                    if ipv4_acl_in is not None:
                        svi_acls.setdefault(interface_name, {})["ipv4_acl_in"] = self.shared_utils.get_ipv4_acl(
                            name=ipv4_acl_in,
                            interface_name=interface_name,
                            interface_ip=interface_ip,
                        )
                    if ipv4_acl_out is not None:
                        svi_acls.setdefault(interface_name, {})["ipv4_acl_out"] = self.shared_utils.get_ipv4_acl(
                            name=ipv4_acl_out,
                            interface_name=interface_name,
                            interface_ip=interface_ip,
                        )

        return svi_acls

    @cached_property
    def _filtered_internet_exit_policies(self: AvdStructuredConfigNetworkServices) -> list:
        """
        Only supported for CV Pathfinder Edge routers. Returns an empty list for pathfinders.

        - Parse self._filtered_wan_policies looking to internet_exit_policies.
        - Verify each internet_exit_policy is present in inputs `cv_pathfinder_internet_exit_policies`.
        - get_internet_exit_connections and insert into the policy dict.
        - Return the list of relevant internet_exit_policies.
        """
        if not self.shared_utils.is_cv_pathfinder_client:
            return []

        internet_exit_policy_names = set()
        candidate_internet_exit_policies = []
        configured_internet_exit_policies = get(self._hostvars, "cv_pathfinder_internet_exit_policies", [])

        for policy in self._filtered_wan_policies:
            for match in get(policy, "matches", default=[]):
                internet_exit_policy_name = match.get("internet_exit_policy_name")
                if not internet_exit_policy_name or internet_exit_policy_name in internet_exit_policy_names:
                    continue
                internet_exit_policy = get_item(
                    configured_internet_exit_policies,
                    "name",
                    internet_exit_policy_name,
                    required=True,
                    custom_error_msg=(
                        f"The internet exit policy {internet_exit_policy_name} configured under "
                        f"`wan_virtual_topologies.policies[name={policy['name']}].internet_exit.policy` "
                        "is not defined under `cv_pathfinder_internet_exit_policies`."
                    ),
                ).copy()
                internet_exit_policy_names.add(internet_exit_policy_name)
                candidate_internet_exit_policies.append(internet_exit_policy)

            if (default_match := policy.get("default_match")) is not None:
                internet_exit_policy_name = default_match.get("internet_exit_policy_name")
                if not internet_exit_policy_name or internet_exit_policy_name in internet_exit_policy_names:
                    continue
                internet_exit_policy = get_item(
                    configured_internet_exit_policies,
                    "name",
                    internet_exit_policy_name,
                    required=True,
                    custom_error_msg=(
                        f"The internet exit policy {internet_exit_policy_name} configured under "
                        f"`wan_virtual_topologies.policies[name={policy['name']}].internet_exit.policy` "
                        "is not defined under `cv_pathfinder_internet_exit_policies`."
                    ),
                ).copy()
                internet_exit_policy_names.add(internet_exit_policy_name)
                candidate_internet_exit_policies.append(internet_exit_policy)

        if not internet_exit_policy_names:
            return []

        internet_exit_policies = []

        for internet_exit_policy in candidate_internet_exit_policies:
            internet_exit_policy["connections"] = self.get_internet_exit_connections(internet_exit_policy)
            if not internet_exit_policy["connections"]:
                # No local interface for this policy
                # TODO: Decide if we should raise here instead
                continue
            internet_exit_policies.append(internet_exit_policy)

        return internet_exit_policies

    def get_internet_exit_connections(self: AvdStructuredConfigNetworkServices, internet_exit_policy: dict) -> list:
        """
        Return a list of connections (dicts) for the given internet_exit_policy.

        These are useful for easy creation of connectivity-monitor, service-insertion connections, exit-groups, tunnels etc.
        """
        policy_name = internet_exit_policy["name"]
        policy_type = internet_exit_policy["type"]

        if policy_type == "direct":
            return self.get_direct_internet_exit_connections(internet_exit_policy)

        if policy_type == "zscaler":
            return self.get_zscaler_internet_exit_connections(internet_exit_policy)

        raise AristaAvdError(f"Unsupported type '{policy_type}' found in cv_pathfinder_internet_exit[name={policy_name}].")

    def get_direct_internet_exit_connections(self: AvdStructuredConfigNetworkServices, internet_exit_policy: dict) -> list:
        """
        Return a list of connections (dicts) for the given internet_exit_policy of type direct.
        """
        if get(internet_exit_policy, "type") != "direct":
            return []

        connections = []

        # Check if the policy has any local interface
        for wan_interface in self.shared_utils.wan_interfaces:
            wan_interface_internet_exit_policies = get(wan_interface, "cv_pathfinder_internet_exit.policies", default=[])
            if get_item(wan_interface_internet_exit_policies, "name", internet_exit_policy["name"]) is None:
                continue

            if not wan_interface.get("peer_ip"):
                raise AristaAvdMissingVariableError(
                    f"{wan_interface['name']} peer_ip needs to be set. When using wan interface "
                    "for direct type internet exit, peer_ip is used for nexthop, and connectivity monitoring."
                )
            sanitized_interface_name = self.shared_utils.sanitize_interface_name(wan_interface["name"])
            connections.append(
                {
                    "type": "ethernet",
                    "name": f"IE-{sanitized_interface_name}",
                    "monitor_name": f"IE-{sanitized_interface_name}",
                    "monitor_host": wan_interface["peer_ip"],
                    "next_hop": wan_interface["peer_ip"],
                    "source_interface": wan_interface["name"],
                    "description": f"Internet Exit {internet_exit_policy['name']}",
                    "exit_group": f"{internet_exit_policy['name']}",
                }
            )

        return connections

    def get_zscaler_internet_exit_connections(self: AvdStructuredConfigNetworkServices, internet_exit_policy: dict) -> list:
        """
        Return a list of connections (dicts) for the given internet_exit_policy of type zscaler.
        """
        if get(internet_exit_policy, "type") != "zscaler":
            return []

        policy_name = internet_exit_policy["name"]

        cloud_name = get(self._zscaler_endpoints, "cloud_name", required=True)
        connections = []

        # Check if the policy has any local interface
        for wan_interface in self.shared_utils.wan_interfaces:
            wan_interface_internet_exit_policies = get(wan_interface, "cv_pathfinder_internet_exit.policies", default=[])
            if (interface_policy_config := get_item(wan_interface_internet_exit_policies, "name", internet_exit_policy["name"])) is None:
                continue

            connection_base = {
                "type": "tunnel",
                "source_interface": wan_interface["name"],
                "next_hop": get(
                    wan_interface,
                    "peer_ip",
                    required=True,
                    org_key=f"The configured internet-exit policy requires `peer_ip` configured under the WAN Interface {wan_interface['name']}",
                ),
                # Accepting SonarLint issue: The URL is just for verifying connectivity. No data is passed.
                "monitor_url": f"http://gateway.{cloud_name}.net/vpntest",  # NOSONAR
            }

            tunnel_interface_numbers = get(interface_policy_config, "tunnel_interface_numbers")
            if tunnel_interface_numbers is None:
                raise AristaAvdMissingVariableError(
                    f"{wan_interface['name']}.cv_pathfinder_internet_exit.policies[{internet_exit_policy['name']}]."
                    "tunnel_interface_numbers needs to be set, when using wan interface for zscaler type internet exit."
                )

            tunnel_id_range = range_expand(tunnel_interface_numbers)

            zscaler_endpoint_keys = ("primary", "secondary", "tertiary")
            for index, zscaler_endpoint_key in enumerate(zscaler_endpoint_keys):
                if zscaler_endpoint_key not in self._zscaler_endpoints:
                    continue

                zscaler_endpoint = self._zscaler_endpoints[zscaler_endpoint_key]

                # PRI, SEC, TER used for groups
                # TODO: consider if we should use DC names as group suffix.
                suffix = zscaler_endpoint_key[0:3].upper()

                destination_ip = zscaler_endpoint["ip_address"]
                tunnel_id = tunnel_id_range[index]
                connections.append(
                    {
                        **connection_base,
                        "name": f"IE-Tunnel{tunnel_id}",
                        "monitor_name": f"IE-Tunnel{tunnel_id}",
                        "monitor_host": destination_ip,
                        "tunnel_id": tunnel_id,
                        # Using Loopback0 as source interface as using the WAN interface causes issues for DPS.
                        "tunnel_ip_address": "unnumbered Loopback0",
                        "tunnel_destination_ip": destination_ip,
                        "ipsec_profile": f"IE-{policy_name}-PROFILE",
                        "description": f"Internet Exit {policy_name} {suffix}",
                        "exit_group": f"{policy_name}_{suffix}",
                        "preference": zscaler_endpoint_key,
                        "suffix": suffix,
                    }
                )

        return connections

    def _get_ipsec_credentials(self: AvdStructuredConfigNetworkServices, internet_exit_policy: dict) -> tuple[str, str]:
        """
        Returns ufqdn, shared_key based on various details from the given internet_exit_policy.
        """
        policy_name = internet_exit_policy["name"]
        domain_name = get(internet_exit_policy, "zscaler.domain_name", required=True)
        ipsec_key_salt = get(internet_exit_policy, "zscaler.ipsec_key_salt", required=True)
        ipsec_key = self._generate_ipsec_key(name=policy_name, salt=ipsec_key_salt)
        ufqdn = f"{self.shared_utils.hostname}_{policy_name}@{domain_name}"
        return ufqdn, ipsec_key

    def _generate_ipsec_key(self: AvdStructuredConfigNetworkServices, name: str, salt: str) -> str:
        """
        Build a secret containing various components for this policy and device.
        Run type-7 obfuscation using a algorithmic salt so we ensure the same key every time.

        TODO: Maybe introduce some formatting with max length of each element, since the keys can be come very very long.
        """
        secret = "_".join((self.shared_utils.hostname, name, salt))
        type_7_salt = sum(salt.encode("utf-8")) % 16
        return simple_7_encrypt(secret, type_7_salt)
