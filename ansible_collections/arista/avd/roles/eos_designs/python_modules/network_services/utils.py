# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import ipaddress
from functools import cached_property

from ansible_collections.arista.avd.plugins.filter.range_expand import range_expand
from ansible_collections.arista.avd.plugins.plugin_utils.eos_designs_shared_utils import SharedUtils
from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError, AristaAvdMissingVariableError
from ansible_collections.arista.avd.plugins.plugin_utils.utils import default, get, get_item

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
    def _wan_vrfs(self) -> list:
        """
        Return a list of WAN VRFs based on filtered tenants and the AVT.

        Always render VRF on AutoVPN RRs / CV Pathfinder pathfinders
        """
        wan_vrfs = []

        # TODO replace this with VRFs fact once it has been implemented
        network_services_vrfs = {vrf["name"] for tenant in self._filtered_tenants for vrf in tenant["vrfs"]}

        for avt_vrf in get(self._hostvars, "wan_virtual_topologies.vrfs", []):
            vrf_name = avt_vrf["name"]
            if vrf_name in network_services_vrfs or self.shared_utils.wan_role == "server":
                # Needed because we can be rendering either for AutoVPN or CV Pathfinder and key names are different.
                policy_key = "policy" if self.shared_utils.cv_pathfinder_role else "path_selection_policy"
                policy_name = get(avt_vrf, "policy", required=True)

                wan_vrf = {
                    "name": vrf_name,
                    policy_key: policy_name,
                }

                # For CV Pathfinder, it is required to go through all the AVT profiles in the policy to assign an ID.
                if self.shared_utils.cv_pathfinder_role:
                    # Need to allocate an ID for each profile in the policy, for now picked up from the input.
                    policy = get_item(
                        self._cv_pathfinder_policies,
                        "name",
                        policy_name,
                        required=True,
                        custom_error_msg=f"The policy {policy_name} used in vrf {vrf_name} is not configured under 'wan_virtual_topologies.policies'.",
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

    def _generate_wan_load_balance_policy(self, name: str, input_dict: dict, default_all: bool = False) -> dict:
        """
        Generate and return a router path-selection load-balance policy.

        Attrs:
        ------
        name (str): The name of the load balance policy
        input_dict (dict): The dictionary containing
        default_all (bool): When set, if no path-group is found in the input_dict, all local path groups are added to the policy with priority 1.

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
            policy_entries = [{"names": wan_local_path_group_names, "priority": 1}]

        for policy_entry in policy_entries:
            for path_group_name in policy_entry.get("names"):
                # Skip path-group if not present on the router except for pathfinders
                if path_group_name not in wan_local_path_group_names and self.shared_utils.wan_role != "server":
                    continue

                wan_load_balance_policy["path_groups"].append(
                    {
                        "name": path_group_name,
                        "priority": self._path_group_priority_to_eos_priority(get(policy_entry, "priority", required=True)),
                    }
                )

        return wan_load_balance_policy

    def _path_group_priority_to_eos_priority(self, path_group_priority: int | str) -> int:
        """
        Convert "preferred" to 1 and "alternate" to 2. Everything else is returned as is.
        """
        if path_group_priority == "preferred":
            return 1
        elif path_group_priority == "alternate":
            return 2
        try:
            return int(path_group_priority)
        except ValueError as e:
            raise AristaAvdError(
                f"Invalid value {path_group_priority} for Path-Group priority - should be either 'preferred', 'alternate' or an integer."
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
        name = get(control_plane_virtual_topology, "name", default="CONTROL-PLANE-PROFILE")
        wan_load_balance_policies = [self._generate_wan_load_balance_policy(f"{name}_lb", control_plane_virtual_topology, default_all=True)]
        for avt_policy in get(self._hostvars, "wan_virtual_topologies.policies", []):
            for application_virtual_topology in get(avt_policy, "application_virtual_topologies", []):
                # TODO add internet exit once supported
                name = get(application_virtual_topology, "name", default=f"{avt_policy['name']}_{application_virtual_topology['application_profile']}")
                wan_load_balance_policies.append(self._generate_wan_load_balance_policy(f"{name}_lb", application_virtual_topology))

            if (default_virtual_topology := get(avt_policy, "default_virtual_topology")) is not None:
                name = get(default_virtual_topology, "name", default=f"{avt_policy['name']}_default")
                wan_load_balance_policies.append(self._generate_wan_load_balance_policy(f"{name}_lb", default_virtual_topology))

        return wan_load_balance_policies

    def _get_default_vrf_policy(self) -> str:
        """
        Retrieves the name of the policy name used for the default VRF.

        TODO - make it work
        """
        vrfs = get(self._hostvars, "wan_virtual_topologies.vrfs", [])
        if (default_vrf := get_item(vrfs, "name", "default")) is None:
            # TODO make error message better
            raise AristaAvdError("A 'default' VRF policy is required")
        else:
            return get(default_vrf, "policy", required=True)
