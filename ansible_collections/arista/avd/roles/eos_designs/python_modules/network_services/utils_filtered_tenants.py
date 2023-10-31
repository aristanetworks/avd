# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.filter.convert_dicts import convert_dicts
from ansible_collections.arista.avd.plugins.filter.default import default
from ansible_collections.arista.avd.plugins.filter.natural_sort import natural_sort
from ansible_collections.arista.avd.plugins.filter.range_expand import range_expand
from ansible_collections.arista.avd.plugins.plugin_utils.eos_designs_shared_utils import SharedUtils
from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError
from ansible_collections.arista.avd.plugins.plugin_utils.merge import merge
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get, get_item, unique


class UtilsFilteredTenantsMixin(object):
    """
    Utils Mixin Class with internal functions.
    Class should only be used as Mixin to the UtilsMixin class

    These filtered functions should not be moved to shared_utils, since expand a lot more data than needed
    in EosDesignsFacts.
    """

    # Set type hints for Attributes of the main class as needed
    _hostvars: dict
    shared_utils: SharedUtils

    @cached_property
    def _filtered_tenants(self) -> list[dict]:
        """
        Return sorted tenants list from all network_services_keys and filtered based on switch.filter_tenants
        Keys of Tenant data model will be converted to lists.
        All sub data models like vrfs and l2vlans are also converted and filtered.
        """
        filtered_tenants = []
        filter_tenants = self.shared_utils.filter_tenants
        for network_services_key in self.shared_utils.network_services_keys:
            tenants = convert_dicts(get(self._hostvars, network_services_key["name"]), "name")
            for tenant in tenants:
                if tenant["name"] in filter_tenants or "all" in filter_tenants:
                    tenant["l2vlans"] = self._filtered_l2vlans(tenant)
                    tenant["vrfs"] = self._filtered_vrfs(tenant)
                    filtered_tenants.append(tenant)

        return natural_sort(filtered_tenants, "name")

    def _filtered_l2vlans(self, tenant: dict) -> list[dict]:
        """
        Return sorted and filtered l2vlan list from given tenant.
        Filtering based on l2vlan tags.
        """
        if "l2vlans" not in tenant:
            return []

        l2vlans: list[dict] = natural_sort(convert_dicts(tenant["l2vlans"], "id"), "id")
        l2vlans = [
            l2vlan
            for l2vlan in l2vlans
            if self._is_accepted_vlan(l2vlan)
            and ("all" in self.shared_utils.filter_tags or set(l2vlan.get("tags", ["all"])).intersection(self.shared_utils.filter_tags))
        ]
        # Set tenant key on all l2vlans
        for l2vlan in l2vlans:
            l2vlan.update({"tenant": tenant["name"]})

        return l2vlans

    def _is_accepted_vlan(self, vlan: dict) -> bool:
        """
        Check if vlan is in accepted_vlans list
        If filter.only_vlans_in_use is True also check if vlan id or trunk group is assigned to connected endpoint
        """
        vlan_id = int(vlan["id"])

        if vlan_id not in self._accepted_vlans:
            return False

        if not self.shared_utils.filter_only_vlans_in_use:
            # No further filtering
            return True

        if vlan_id in self._endpoint_vlans:
            return True

        if self.shared_utils.enable_trunk_groups and vlan.get("trunk_groups") and self._endpoint_trunk_groups.intersection(vlan["trunk_groups"]):
            return True

        return False

    @cached_property
    def _accepted_vlans(self) -> list[int]:
        """
        switch.vlans is a string representing a vlan range (ex. "1-200")
        For l2 switches return intersection of switch.vlans and switch.vlans from uplink switches
        For anything else return the expanded switch.vlans
        """
        switch_vlans = get(self._hostvars, "switch.vlans")
        if not switch_vlans:
            return []
        switch_vlans_list = range_expand(switch_vlans)
        accepted_vlans = [int(vlan) for vlan in switch_vlans_list]
        if self.shared_utils.uplink_type != "port-channel":
            return accepted_vlans

        uplink_switches = unique(self.shared_utils.uplink_switches)
        uplink_switches = [uplink_switch for uplink_switch in uplink_switches if uplink_switch in self.shared_utils.all_fabric_devices]
        for uplink_switch in uplink_switches:
            uplink_switch_facts = self.shared_utils.get_peer_facts(uplink_switch, required=True)
            uplink_switch_vlans = uplink_switch_facts.get("vlans", [])
            uplink_switch_vlans_list = range_expand(uplink_switch_vlans)
            uplink_switch_vlans_list = [int(vlan) for vlan in uplink_switch_vlans_list]
            accepted_vlans = [vlan for vlan in accepted_vlans if vlan in uplink_switch_vlans_list]

        return accepted_vlans

    def _filtered_vrfs(self, tenant: dict) -> list[dict]:
        """
        Return sorted and filtered vrf list from given tenant.
        Filtering based on svi tags, l3interfaces and filter.always_include_vrfs_in_tenants.
        Keys of VRF data model will be converted to lists.
        """
        filtered_vrfs = []

        always_include_vrfs_in_tenants = get(self.shared_utils.switch_data_combined, "filter.always_include_vrfs_in_tenants", default=[])

        vrfs: list[dict] = natural_sort(convert_dicts(tenant.get("vrfs", []), "name"), "name")
        for vrf in vrfs:
            # Storing tenant on VRF for use by child objects like SVIs
            vrf["tenant"] = tenant["name"]
            bgp_peers = natural_sort(convert_dicts(vrf.get("bgp_peers"), "ip_address"), "ip_address")
            vrf["bgp_peers"] = [bgp_peer for bgp_peer in bgp_peers if self.shared_utils.hostname in bgp_peer.get("nodes", [])]
            vrf["static_routes"] = [
                route
                for route in get(vrf, "static_routes", default=[])
                if self.shared_utils.hostname in get(route, "nodes", default=[self.shared_utils.hostname])
            ]
            vrf["ipv6_static_routes"] = [
                route
                for route in get(vrf, "ipv6_static_routes", default=[])
                if self.shared_utils.hostname in get(route, "nodes", default=[self.shared_utils.hostname])
            ]
            vrf["svis"] = self._filtered_svis(vrf)
            vrf["l3_interfaces"] = [
                l3_interface
                for l3_interface in get(vrf, "l3_interfaces", default=[])
                if (
                    self.shared_utils.hostname in get(l3_interface, "nodes", default=[])
                    and l3_interface.get("ip_addresses") is not None
                    and l3_interface.get("interfaces") is not None
                )
            ]

            if self.shared_utils.vtep is True:
                evpn_l3_multicast_enabled = default(get(vrf, "evpn_l3_multicast.enabled"), get(tenant, "evpn_l3_multicast.enabled"))
                if evpn_l3_multicast_enabled is True and self._evpn_multicast is not True:
                    raise AristaAvdError(
                        f"'evpn_l3_multicast: true' under VRF {vrf['name']} or Tenant {tenant['name']}; this requires 'evpn_multicast' to also be set to true."
                    )

                if self._evpn_multicast:
                    vrf["_evpn_l3_multicast_enabled"] = evpn_l3_multicast_enabled

                    rps = []
                    for rp_entry in default(get(vrf, "pim_rp_addresses"), get(tenant, "pim_rp_addresses"), []):
                        if self.shared_utils.hostname in get(rp_entry, "nodes", default=[self.shared_utils.hostname]):
                            for rp_ip in get(
                                rp_entry,
                                "rps",
                                required=True,
                                org_key=f"pim_rp_addresses.rps under VRF '{vrf['name']}' in Tenant '{tenant['name']}'",
                            ):
                                rp_address = {"address": rp_ip}
                                if (rp_groups := get(rp_entry, "groups")) is not None:
                                    if (acl := rp_entry.get("access_list_name")) is not None:
                                        rp_address["access_lists"] = [acl]
                                    else:
                                        rp_address["groups"] = rp_groups

                                rps.append(rp_address)

                    if rps:
                        vrf["_pim_rp_addresses"] = rps

                    for evpn_peg in default(get(vrf, "evpn_l3_multicast.evpn_peg"), get(tenant, "evpn_l3_multicast.evpn_peg"), []):
                        if self.shared_utils.hostname in evpn_peg.get("nodes", [self.shared_utils.hostname]) and rps:
                            vrf["_evpn_l3_multicast_evpn_peg_transit"] = evpn_peg.get("transit")
                            break

            if vrf["svis"] or vrf["l3_interfaces"] or "all" in always_include_vrfs_in_tenants or tenant["name"] in always_include_vrfs_in_tenants:
                filtered_vrfs.append(vrf)

            vrf["additional_route_targets"] = [
                rt
                for rt in get(vrf, "additional_route_targets", default=[])
                if (
                    self.shared_utils.hostname in get(rt, "nodes", default=[self.shared_utils.hostname])
                    and rt.get("address_family") is not None
                    and rt.get("route_target") is not None
                    and rt.get("type") in ["import", "export"]
                )
            ]

        return filtered_vrfs

    @cached_property
    def _svi_profiles(self) -> list[dict]:
        """
        Return list of svi_profiles

        The key "nodes" is filtered to only contain one item with the relevant dict from "nodes" or {}
        """
        svi_profiles = convert_dicts(get(self._hostvars, "svi_profiles", default=[]), "profile")
        for svi_profile in svi_profiles:
            svi_profile["nodes"] = convert_dicts(svi_profile.get("nodes", []), "node")
            svi_profile["nodes"] = [get_item(svi_profile["nodes"], "node", self.shared_utils.hostname, default={})]

        return svi_profiles

    def _get_merged_svi_config(self, svi: dict) -> list[dict]:
        """
        Return structured config for one svi after inheritance

        Handle inheritance of node config as svi_profiles in two levels:

        First variables will be merged
        svi > svi_profile > svi_parent_profile --> svi_cfg
        &
        svi.nodes.<hostname> > svi_profile.nodes.<hostname> > svi_parent_profile.nodes.<hostname> --> svi_node_cfg

        Then svi is updated with the result of merging svi_node_cfg over svi_cfg
        svi_node_cfg > svi_cfg --> svi
        """
        svi_profile = {"nodes": [{}]}
        svi_parent_profile = {"nodes": [{}]}

        svi["nodes"] = convert_dicts(svi.get("nodes", []), "node")
        svi["nodes"] = [get_item(svi["nodes"], "node", self.shared_utils.hostname, default={})]

        if (svi_profile_name := svi.get("profile")) is not None:
            svi_profile = get_item(self._svi_profiles, "profile", svi_profile_name, default={})

        if (svi_parent_profile_name := svi_profile.get("parent_profile")) is not None:
            svi_parent_profile = get_item(self._svi_profiles, "profile", svi_parent_profile_name, default={})

        # deepmerge all levels of config - later vars override previous.
        # Using destructive_merge=False to avoid having references to profiles and other data.
        # Instead it will be doing deep copies inside merge.
        merged_svi = merge(
            svi_parent_profile,
            svi_profile,
            svi,
            svi_parent_profile["nodes"][0],
            svi_profile["nodes"][0],
            svi["nodes"][0],
            list_merge="replace",
            destructive_merge=False,
        )

        # Override structured configs since we don't want to deep-merge those
        merged_svi["structured_config"] = default(
            svi["nodes"][0].get("structured_config"),
            svi_profile["nodes"][0].get("structured_config"),
            svi_parent_profile["nodes"][0].get("structured_config"),
            svi.get("structured_config"),
            svi_profile.get("structured_config"),
            svi_parent_profile.get("structured_config"),
        )

        # Override bgp.structured configs since we don't want to deep-merge those
        merged_svi.setdefault("bgp", {})["structured_config"] = default(
            get(svi["nodes"][0], "bgp.structured_config"),
            get(svi_profile["nodes"][0], "bgp.structured_config"),
            get(svi_parent_profile["nodes"][0], "bgp.structured_config"),
            get(svi, "bgp.structured_config"),
            get(svi_profile, "bgp.structured_config"),
            get(svi_parent_profile, "bgp.structured_config"),
        )
        return merged_svi

    def _filtered_svis(self, vrf: dict) -> list[dict]:
        """
        Return sorted and filtered svi list from given tenant vrf.
        Filtering based on accepted vlans since eos_designs_facts already
        filtered that on tags and trunk_groups.
        """
        svis: list[dict] = natural_sort(convert_dicts(vrf.get("svis", []), "id"), "id")
        svis = [svi for svi in svis if self._is_accepted_vlan(svi)]

        # Handle svi_profile inheritance
        svis = [self._get_merged_svi_config(svi) for svi in svis]

        # Perform filtering on tags after merge of profiles, to support tags being set inside profiles.
        svis = [svi for svi in svis if "all" in self.shared_utils.filter_tags or set(svi.get("tags", ["all"])).intersection(self.shared_utils.filter_tags)]

        # Set tenant key on all SVIs
        for svi in svis:
            svi.update({"tenant": vrf["tenant"]})

        return svis
