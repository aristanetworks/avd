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
        """
        wan_vrfs = []

        network_services_vrfs = set(vrf["name"] for tenant in self._filtered_tenants for vrf in tenant["vrfs"])

        for avt_vrf in get(self._hostvars, "wan_virtual_topologies.vrfs", []):
            if avt_vrf["name"] in network_services_vrfs or self.shared_utils.wan_role == "server":
                # Needed becuase we can be rendering either for AutoVPN or CV Pathfinder
                policy_key = "policy" if self.shared_utils.cv_pathfinder_role else "path_selection_policy"
                policy_name = get(avt_vrf, "policy", required=True)

                wan_vrf = {
                    "name": avt_vrf["name"],
                    policy_key: policy_name,
                }

                if self.shared_utils.cv_pathfinder_role:
                    # Need to allocate an ID for each profile in the policy, for now picked up from the input.
                    # TODO - custom_error_msg
                    policy = get_item(self._cv_pathfinder_policies, "name", policy_name, required=True)
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
    def _cv_pathfinder_policies(self) -> list:
        """
        Return a list of CV_Pathfinder Policies.
        """
        if not self.shared_utils.cv_pathfinder_role:
            return []

        cv_pathfinder_policies = []

        for avt_policy in get(self._hostvars, "wan_virtual_topologies.policies", []):
            cv_pathfinder_policy = {
                "name": avt_policy["name"],
            }

            for application_policy in get(avt_policy, "application_policies", []):
                cv_pathfinder_policy.setdefault("matches", []).append(
                    {
                        "application_profile": get(application_policy, "application_profile", required=True),
                        "avt_profile": get(application_policy, "name", default=f"{avt_policy['name']}_{application_policy['application_profile']}"),
                        "traffic_class": get(application_policy, "traffic_class"),
                        "dscp": get(application_policy, "dscp"),
                        # Storing id as _id to avoid schema validation and be able to pick up in VRFs
                        "_id": get(application_policy, "id"),
                    }
                )
            if default_policy := get(avt_policy, "default_policy"):
                cv_pathfinder_policy.setdefault("matches", []).append(
                    {
                        "application_profile": get(default_policy, "application_profile", default="default"),
                        "avt_profile": get(default_policy, "name", default=f"{avt_policy['name']}_default"),
                        "traffic_class": get(default_policy, "traffic_class"),
                        "dscp": get(default_policy, "dscp"),
                        # Storing id as _id to avoid schema validation and be able to pick up in VRFs
                        "_id": get(default_policy, "id"),
                    }
                )

            cv_pathfinder_policies.append(cv_pathfinder_policy)

        return cv_pathfinder_policies

    @cached_property
    def _cv_pathfinder_profiles(self) -> list:
        """
        Return a list of router adaptive-virtual-topology profiles for this router.
        """
        if not self.shared_utils.cv_pathfinder_role:
            return []

        cv_pathfinder_profiles = []

        for avt_policy in get(self._hostvars, "wan_virtual_topologies.policies", []):
            for application_policy in get(avt_policy, "application_policies", []):
                # TODO add internet exit once supported
                name = get(application_policy, "name", default=f"{avt_policy['name']}_{application_policy['application_profile']}")
                cv_pathfinder_profiles.append(
                    {
                        "name": name,
                        "load_balance_policy": f"{name}_lb",
                    }
                )
            if default_policy := get(avt_policy, "default_policy"):
                name = get(default_policy, "name", default=f"{avt_policy['name']}_default")
                cv_pathfinder_profiles.append(
                    {
                        "name": name,
                        "load_balance_policy": f"{name}_lb",
                    }
                )

        return cv_pathfinder_profiles

    @cached_property
    def _autovpn_policies(self) -> list:
        """
        Return a list of AutoVPN Policies.
        """
        if self.shared_utils.cv_pathfinder_role:
            return []

        autovpn_policies = []

        for avt_policy in get(self._hostvars, "wan_virtual_topologies.policies", []):
            autovpn_policy = {
                "name": avt_policy["name"],
            }

            for rule_id, application_policy in enumerate(get(avt_policy, "application_policies", []), start=1):
                name = get(application_policy, "name", default=f"{avt_policy['name']}_{application_policy['application_profile']}")
                autovpn_policy.setdefault("rules", []).append(
                    {
                        "id": 10 * rule_id,
                        "application_profile": get(application_policy, "application_profile", required=True),
                        "load_balance": f"{name}_lb",
                    }
                )
            if default_policy := get(avt_policy, "default_policy"):
                name = get(default_policy, "name", default=f"{avt_policy['name']}_default")
                autovpn_policy["default_match"] = {"load_balance": f"{name}_lb"}

            autovpn_policies.append(autovpn_policy)

        return autovpn_policies

    def _path_group_priority_to_eos_priority(self, path_group_priority: int | str) -> int:
        """
        Convert "preferred" to 1 and "alternate" to 2. Everything else is returned as is
        """
        if path_group_priority == "preferred":
            return 1
        elif path_group_priority == "alternate":
            return 2
        elif isinstance(path_group_priority, str):
            raise AristaAvdError(f"Invalid value {path_group_priority} for Path-Group priority - should be either 'preferred', 'alternate' or an integer.")
        return path_group_priority

    @cached_property
    def _wan_load_balance_policies(self) -> list:
        """
        Return a list of WAN router path-selection load-balance policy based on the local path-groups.
        """
        if not self.shared_utils.wan_role:
            return []

        wan_load_balance_policies = []
        wan_local_path_group_names = [path_group["name"] for path_group in self.shared_utils.wan_local_path_groups]

        for avt_policy in get(self._hostvars, "wan_virtual_topologies.policies", []):
            for application_policy in get(avt_policy, "application_policies", []):
                # TODO add internet exit once supported
                name = get(application_policy, "name", default=f"{avt_policy['name']}_{application_policy['application_profile']}")
                wan_load_balance_policy = {"name": f"{name}_lb"}

                # TODO add LAN_HA with prio 1 when HA is implemented
                # TODO for now hardcoding priorities as requested by team
                for path_groups in get(application_policy, "path_groups", []):
                    for path_group_name in path_groups.get("names"):
                        # Skip path-group if not present on the router except for pathfinders
                        if path_group_name not in wan_local_path_group_names and self.shared_utils.wan_role != "server":
                            continue

                        wan_load_balance_policy.setdefault("path_groups", []).append(
                            {
                                "name": path_group_name,
                                "priority": self._path_group_priority_to_eos_priority(get(path_groups, "priority", required=True)),
                            }
                        )

                # TODO implement also the jitter / ...
                wan_load_balance_policies.append(wan_load_balance_policy)

            if default_policy := get(avt_policy, "default_policy"):
                name = get(default_policy, "name", default=f"{avt_policy['name']}_default")
                wan_load_balance_policy = {"name": f"{name}_lb"}

                # TODO add LAN_HA with prio 1 when HA is implemented
                # TODO for now hardcoding priorities as requested by team
                for path_groups in get(application_policy, "path_groups", []):
                    for path_group_name in path_groups.get("names"):
                        if path_group_name not in wan_local_path_group_names and self.shared_utils.wan_role != "server":
                            continue

                        wan_load_balance_policy.setdefault("path_groups", []).append(
                            {
                                "name": path_group_name,
                                "priority": self._path_group_priority_to_eos_priority(get(path_groups, "priority", required=True)),
                            }
                        )

                wan_load_balance_policies.append(wan_load_balance_policy)

        return wan_load_balance_policies
