# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import ipaddress
from functools import cached_property

from ansible_collections.arista.avd.plugins.filter.range_expand import range_expand
from ansible_collections.arista.avd.plugins.plugin_utils.eos_designs_shared_utils import SharedUtils
from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError, AristaAvdMissingVariableError
from ansible_collections.arista.avd.plugins.plugin_utils.utils import append_if_not_duplicate, default, get, get_item

from .utils_filtered_tenants import UtilsFilteredTenantsMixin


class UtilsMixin(UtilsFilteredTenantsMixin):
    """
    Mixin Class with internal functions.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    # Set type hints for Attributes of the main class as needed
    _hostvars: dict
    shared_utils: SharedUtils

    @cached_property
    def _trunk_groups_mlag_name(self) -> str:
        return get(self.shared_utils.trunk_groups, "mlag.name", required=True)

    @cached_property
    def _trunk_groups_mlag_l3_name(self) -> str:
        return get(self.shared_utils.trunk_groups, "mlag_l3.name", required=True)

    @cached_property
    def _trunk_groups_uplink_name(self) -> str:
        return get(self.shared_utils.trunk_groups, "uplink.name", required=True)

    @cached_property
    def _endpoint_trunk_groups(self) -> set:
        return set(get(self._hostvars, "switch.endpoint_trunk_groups", default=[]))

    @cached_property
    def _local_endpoint_trunk_groups(self) -> set:
        return set(get(self._hostvars, "switch.local_endpoint_trunk_groups", default=[]))

    @cached_property
    def _endpoint_vlans(self) -> list:
        endpoint_vlans = get(self._hostvars, "switch.endpoint_vlans", default="")
        if not endpoint_vlans:
            return []
        return [int(id) for id in range_expand(endpoint_vlans)]

    @cached_property
    def _vrf_default_evpn(self) -> bool:
        """
        Return boolean telling if VRF "default" is running EVPN or not.
        """
        if not (self.shared_utils.network_services_l3 and self.shared_utils.overlay_vtep and self.shared_utils.overlay_evpn):
            return False

        for tenant in self._filtered_tenants:
            if (vrf_default := get_item(tenant["vrfs"], "name", "default")) is None:
                continue

            if "evpn" in vrf_default.get("address_families", ["evpn"]):
                if self.shared_utils.underlay_filter_peer_as:
                    raise AristaAvdError("'underlay_filter_peer_as' cannot be used while there are EVPN services in the default VRF.")
                return True

        return False

    @cached_property
    def _vrf_default_ipv4_subnets(self) -> list[str]:
        """
        Return list of ipv4 subnets in VRF "default"
        """
        subnets = []
        for tenant in self._filtered_tenants:
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
    def _vrf_default_ipv4_static_routes(self) -> dict:
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
        for tenant in self._filtered_tenants:
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
            "static_routes": list(vrf_default_ipv4_static_routes),
            "redistribute_in_underlay": redistribute_in_underlay,
            "redistribute_in_overlay": redistribute_in_overlay,
        }

    def _mlag_ibgp_peering_enabled(self, vrf, tenant) -> bool:
        """
        Returns True if mlag ibgp_peering is enabled
        False otherwise
        """
        if not self.shared_utils.mlag_l3 or not self.shared_utils.network_services_l3:
            return False

        mlag_ibgp_peering: bool = default(vrf.get("enable_mlag_ibgp_peering_vrfs"), tenant.get("enable_mlag_ibgp_peering_vrfs"), True)
        return vrf["name"] != "default" and mlag_ibgp_peering

    def _mlag_ibgp_peering_vlan_vrf(self, vrf, tenant) -> int | None:
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

    def _mlag_ibgp_peering_redistribute(self, vrf, tenant) -> bool:
        """
        Returns True if MLAG IBGP Peering subnet should be redistributed for the given vrf/tenant.
        False otherwise.

        Does _not_ include checks if the peering is enabled at all, so that should be checked first.
        """
        return default(vrf.get("redistribute_mlag_ibgp_peering_vrfs"), tenant.get("redistribute_mlag_ibgp_peering_vrfs"), True) is True

    @cached_property
    def _configure_bgp_mlag_peer_group(self) -> bool:
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
    def _evpn_multicast(self) -> bool:
        return get(self._hostvars, "switch.evpn_multicast") is True

    @cached_property
    def _wan_control_plane_profile(self) -> str:
        """
        Control plane profile name
        """
        control_plane_virtual_topology = get(self._hostvars, "wan_virtual_topologies.control_plane_virtual_topology", default={})
        return get(control_plane_virtual_topology, "name", default="CONTROL-PLANE-PROFILE")

    @cached_property
    def _wan_control_plane_application_profile(self) -> str:
        """
        Control plane application profile name
        """
        return "CONTROL-PLANE-APPLICATION-PROFILE"

    @cached_property
    def _wan_policy_key(self) -> str:
        """
        The key for policies is different for AutoVPN and CV Pathfinder
        """
        return "policy" if self.shared_utils.wan_mode == "cv-pathfinder" else "path_selection_policy"

    def _generate_wan_load_balance_policy(self, name: str, input_dict: dict, default_all: bool = False) -> dict:
        """
        Generate and return a router path-selection load-balance policy.

        Attrs:
        ------
        name (str): The name of the load balance policy
        input_dict (dict): The dictionary containing
        default_all (bool): When set, if no path-group is found in the input_dict, all local path groups connected to pathfinder
                            are added to the policy with priority 1.

        TODO:
        * add LAN_HA with prio 1 when HA is implemented
        * for now hardcoding priorities as requested by team
        * implement also the jitter / ...
        """
        wan_local_path_group_names = [path_group["name"] for path_group in self.shared_utils.wan_local_path_groups]
        wan_load_balance_policy = {"name": name, "path_groups": []}

        # An entry is composed of a list of path-groups in `names` and a `priority`
        policy_entries = get(input_dict, "path_groups", [])
        if not policy_entries and default_all:
            local_path_groups_connected_to_pathfinder = [
                path_group["name"]
                for path_group in self.shared_utils.wan_local_path_groups
                if any(wan_interface["connected_to_pathfinder"] for wan_interface in path_group["interfaces"])
            ]
            policy_entries = [{"names": local_path_groups_connected_to_pathfinder, "preference": 1}]

        at_least_one_priority_1_found = False
        for policy_entry in policy_entries:
            # TODO check if it cannot be optimized further in shared_utils or validated in a global fashion - maybe
            # schema?
            # check that the LB policy has at least one prio 1 / preferred EVEN if the path group is not configured.
            if (priority := self._path_group_preference_to_eos_priority(get(policy_entry, "preference", default=1))) == 1:
                at_least_one_priority_1_found = True
            for path_group_name in policy_entry.get("names"):
                # Skip path-group on this device if not present on the router except for pathfinders
                if path_group_name not in wan_local_path_group_names and self.shared_utils.wan_role != "server":
                    continue

                path_group = {
                    "name": path_group_name,
                    "priority": priority if priority != 1 else None,
                }

                wan_load_balance_policy["path_groups"].append(path_group)
        if not at_least_one_priority_1_found:
            raise AristaAvdError(f"At least one path-group must be configured with preference '1' or 'preferred' for policy {name[:-3]}.")

        return wan_load_balance_policy

    def _path_group_preference_to_eos_priority(self, path_group_preference: int | str) -> int:
        """
        Convert "preferred" to 1 and "alternate" to 2. Everything else is returned as is.
        """
        if path_group_preference == "preferred":
            return 1
        if path_group_preference == "alternate":
            return 2
        try:
            return int(path_group_preference)
        except ValueError as e:
            raise AristaAvdError(
                f"Invalid value {path_group_preference} for Path-Group preference - should be either 'preferred', 'alternate' or an integer."
            ) from e

    @cached_property
    def _wan_load_balance_policies(self) -> list:
        """
        Return a list of WAN router path-selection load-balance policy based on the local path-groups.
        """
        if not self.shared_utils.wan_role:
            return []

        # Control plane Load Balancing policy - if not configured, render the default one.
        control_plane_virtual_topology = get(self._hostvars, "wan_virtual_topologies.control_plane_virtual_topology", default={})
        wan_load_balance_policies = [
            self._generate_wan_load_balance_policy(f"LB-{self._wan_control_plane_profile}", control_plane_virtual_topology, default_all=True)
        ]
        for policy in self._filtered_wan_policies:
            for application_virtual_topology in get(policy, "application_virtual_topologies", []):
                # TODO add internet exit once supported
                name = get(application_virtual_topology, "name", default=f"{policy['name']}-{application_virtual_topology['application_profile']}")
                append_if_not_duplicate(
                    list_of_dicts=wan_load_balance_policies,
                    primary_key="name",
                    new_dict=self._generate_wan_load_balance_policy(f"LB-{name}", application_virtual_topology),
                    context="Router Path-Selection Load-Balance policies.",
                    context_keys=["name"],
                )

            default_virtual_topology = get(policy, "default_virtual_topology", required=True)
            if not get(default_virtual_topology, "drop_unmatched", default=False):
                name = get(default_virtual_topology, "name", default=f"{policy['name']}-DEFAULT")
                append_if_not_duplicate(
                    list_of_dicts=wan_load_balance_policies,
                    primary_key="name",
                    new_dict=self._generate_wan_load_balance_policy(f"LB-{name}", default_virtual_topology),
                    context="Router Path-Selection Load-Balance policies.",
                    context_keys=["name"],
                )

        return wan_load_balance_policies

    @cached_property
    def _filtered_wan_vrfs(self) -> list:
        """
        Loop through all the VRFs defined under `wan_virtual_topologies.vrfs` and returns a list of mode
        """
        wan_vrfs = []
        # TODO replace this with VRFs fact once it has been implemented
        network_services_vrfs = {vrf["name"] for tenant in self._filtered_tenants for vrf in tenant["vrfs"]}

        for avt_vrf in get(self._hostvars, "wan_virtual_topologies.vrfs", []):
            vrf_name = avt_vrf["name"]
            if vrf_name in network_services_vrfs or self.shared_utils.wan_role == "server":
                # TODO check that the policy exists or raise
                wan_vrf = {
                    "name": vrf_name,
                    self._wan_policy_key: get(avt_vrf, "policy", required=True),
                }

                wan_vrfs.append(wan_vrf)

        # Check that default is in the list as it is required everywhere
        if (vrf_default := get_item(wan_vrfs, "name", "default")) is None:
            wan_vrfs.append(
                {
                    "name": "default",
                    self._wan_policy_key: f"{self._default_vrf_policy['name']}-WITH-CP",
                }
            )
        else:
            vrf_default[self._wan_policy_key] = f"{vrf_default[self._wan_policy_key]}-WITH-CP"

        return wan_vrfs

    @cached_property
    def _filtered_wan_policies(self) -> list:
        """
        Loop through all the VRFs defined under `wan_virtual_topologies.vrfs` and returns a list of policies to configure on this device.

        inject the default_vrf_policy
        """
        policies = get(self._hostvars, "wan_virtual_topologies.policies", default=[])
        # Need to handle VRF default differently
        filtered_policies = [get_item(policies, "name", wan_vrf[self._wan_policy_key]) for wan_vrf in self._filtered_wan_vrfs if wan_vrf["name"] != "default"]
        filtered_policies.append(self._default_vrf_policy)
        return filtered_policies

    @cached_property
    def _default_vrf_policy(self) -> dict:
        """
        Retrieves the name of the policy used for the default VRF and appending -WITH-CP to its name.
        """
        vrfs = get(self._hostvars, "wan_virtual_topologies.vrfs", [])

        if (default_vrf := get_item(vrfs, "name", "default")) is None:
            # TODO make error message better
            raise AristaAvdError("A 'default' VRF policy is required")

        policies = get(self._hostvars, "wan_virtual_topologies.policies", default=[])
        # copy is safe here as we change only the name
        vrf_default_policy = get(default_vrf, "policy", required=True, org_key="VRF default under 'wan_virtual_topologies.vrfs' is missing a 'policy'.")
        default_policy = get_item(
            policies,
            "name",
            vrf_default_policy,
            required=True,
            custom_error_msg=(
                f"The policy {vrf_default_policy} defined for vrf default under 'wan_virtual_topologies.vrfs' "
                "is not defined under 'wan_virtual_topologies.policies'."
            ),
        ).copy()
        default_policy["is_default"] = True
        return default_policy
