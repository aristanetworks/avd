# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import ipaddress
from functools import cached_property

from ansible_collections.arista.avd.plugins.filter.natural_sort import natural_sort
from ansible_collections.arista.avd.plugins.plugin_utils.eos_designs_shared_utils import SharedUtils
from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError, AristaAvdMissingVariableError
from ansible_collections.arista.avd.plugins.plugin_utils.utils import default, get, get_item


class UtilsMixin:
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
    def _local_endpoint_trunk_groups(self) -> set:
        return set(get(self._hostvars, "switch.local_endpoint_trunk_groups", default=[]))

    @cached_property
    def _vrf_default_evpn(self) -> bool:
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
    def _vrf_default_ipv4_subnets(self) -> list[str]:
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
    def _wan_control_plane_profile(self) -> str:
        """
        Control plane profile name
        """
        control_plane_virtual_topology = get(self._hostvars, "wan_virtual_topologies.control_plane_virtual_topology", default={})
        vrf_default_policy_name = get(get_item(self._filtered_wan_vrfs, "name", "default"), "original_policy")
        return get(control_plane_virtual_topology, "name", default=f"{vrf_default_policy_name}-CONTROL-PLANE")

    @cached_property
    def _wan_control_plane_application_profile(self) -> str:
        """
        Control plane application profile name

        TODO: make this configurable
        """
        return "APP-PROFILE-CONTROL-PLANE"

    @cached_property
    def _local_path_groups_connected_to_pathfinder(self) -> list:
        """
        Return list of names of local path_groups connected to pathfinder
        """
        return [
            path_group["name"]
            for path_group in self.shared_utils.wan_local_path_groups
            if any(wan_interface["connected_to_pathfinder"] for wan_interface in path_group["interfaces"])
        ]

    @cached_property
    def _default_control_plane_virtual_topology(self) -> dict:
        """
        Build the default control_plane_virtual_topology, excluding path_groups with excluded_from_default_policy
        """
        path_groups = [
            path_group["name"] for path_group in self.shared_utils.wan_path_groups if not get(path_group, "excluded_from_default_policy", default=False)
        ]
        if self.shared_utils.is_wan_client:
            # Filter only the path-groups connected to pathfinder
            path_groups = [path_group for path_group in path_groups if path_group in self._local_path_groups_connected_to_pathfinder]
        return {"path_groups": [{"names": path_groups}]}

    @cached_property
    def _filtered_wan_vrfs(self) -> list:
        """
        Loop through all the VRFs defined under `wan_virtual_topologies.vrfs` and returns a list of mode
        """
        wan_vrfs = []

        for vrf in get(self._hostvars, "wan_virtual_topologies.vrfs", []):
            vrf_name = vrf["name"]
            if vrf_name in self.shared_utils.vrfs or self.shared_utils.is_wan_server:
                wan_vrf = {
                    "name": vrf_name,
                    "policy": get(vrf, "policy", default=self._default_wan_policy["name"]),
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
                    "policy": f"{self._default_wan_policy['name']}-WITH-CP",
                    "wan_vni": 1,
                    "original_policy": self._default_wan_policy["name"],
                }
            )
        else:
            vrf_default["original_policy"] = vrf_default["policy"]
            vrf_default["policy"] = f"{vrf_default['policy']}-WITH-CP"

        return wan_vrfs

    @cached_property
    def _wan_policies(self) -> list:
        """ """
        policies = get(self._hostvars, "wan_virtual_topologies.policies", default=[])
        # If not overwritten, inject the default policy in case it is required for one of the VRFs
        if get_item(policies, "name", self._default_wan_policy["name"]) is None:
            policies.append(self._default_wan_policy)

        return policies

    @cached_property
    def _filtered_wan_policies(self) -> list:
        """
        Loop through all the VRFs defined under `wan_virtual_topologies.vrfs` and returns a list of policies to configure on this device.
        inject the default_vrf_policy
        """
        # to track the names already injected
        filtered_policy_names = []
        filtered_policies = []
        for vrf in self._filtered_wan_vrfs:
            # Need to handle VRF default differently and lookup for the original policy
            lookup_name = get(vrf, "original_policy", default=vrf["policy"])
            vrf_policy = get_item(
                self._wan_policies,
                "name",
                lookup_name,
                required=True,
                custom_error_msg=(
                    f"The policy {lookup_name} applied to vrf {vrf['name']} under `wan_virtual_topologies.vrfs` is not "
                    "defined under `wan_virtual_topologies.policies`."
                ),
            ).copy()

            if vrf["name"] == "default":
                vrf_policy["is_default"] = True
                vrf_policy["profile_prefix"] = lookup_name
                vrf_policy["name"] = f"{vrf_policy['name']}-WITH-CP"
            else:
                vrf_policy["profile_prefix"] = vrf_policy["name"]

            if vrf_policy["name"] not in filtered_policy_names:
                filtered_policy_names.append(vrf_policy["name"])
                filtered_policies.append(vrf_policy)

        return filtered_policies

    @cached_property
    def _default_wan_policy(self) -> dict:
        """
        If no policy is defined for a VRF under 'wan_virtual_topologies.vrfs', a default policy named DEFAULT-POLICY is used
        where all traffic is matched in the default category and distributed amongst all path-groups.
        Returning policy containing all path groups not excluded from default policy.
        """

        res = {
            "name": "DEFAULT-POLICY",
            "default_virtual_topology": {
                "path_groups": [
                    {
                        "names": [
                            path_group["name"] for path_group in self.shared_utils.wan_path_groups if not path_group.get("excluded_from_default_policy", False)
                        ]
                    }
                ]
            },
        }
        return res

    def _default_profile_name(self, profile_name: str, application_profile: str) -> str:
        """
        Helper function to consistently return the default name of a profile

        Returns {profile_name}-{application_profile}
        """
        return f"{profile_name}-{application_profile}"
