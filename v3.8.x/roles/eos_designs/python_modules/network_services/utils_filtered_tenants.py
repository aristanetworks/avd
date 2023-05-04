from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.filter.convert_dicts import convert_dicts
from ansible_collections.arista.avd.plugins.filter.default import default
from ansible_collections.arista.avd.plugins.filter.natural_sort import natural_sort
from ansible_collections.arista.avd.plugins.filter.range_expand import range_expand
from ansible_collections.arista.avd.plugins.plugin_utils.merge import merge
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get, get_item, unique


class UtilsFilteredTenantsMixin(object):
    """
    Utils Mixin Class with internal functions.
    Class should only be used as Mixin to the UtilsMixin class
    """

    # Set type hints for Attributes of the main class as needed
    _hostname: str
    _hostvars: dict
    _network_services_keys: list[dict]

    @cached_property
    def _filtered_tenants(self) -> list[dict]:
        """
        Return sorted tenants list from all network_services_keys and filtered based on switch.filter_tenants
        Keys of Tenant data model will be converted to lists.
        All sub data models like vrfs and l2vlans are also converted and filtered.
        """
        filtered_tenants = []
        filter_tenants = get(self._hostvars, "switch.filter_tenants", required=True)
        for network_services_key in self._network_services_keys:
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
            if self._is_accepted_vlan(l2vlan) and ("all" in self._filter_tags or set(l2vlan.get("tags", ["all"])).intersection(self._filter_tags))
        ]
        return l2vlans

    def _is_accepted_vlan(self, vlan: dict) -> bool:
        """
        Check if vlan is in accepted_vlans list
        If filter.only_vlans_in_use is True also check if vlan id or trunk group is assigned to connected endpoint
        """
        vlan_id = int(vlan["id"])

        if vlan_id not in self._accepted_vlans:
            return False

        if not self._filter_only_vlans_in_use:
            # No further filtering
            return True

        if vlan_id in self._endpoint_vlans:
            return True

        if self._enable_trunk_groups and vlan.get("trunk_groups") and self._endpoint_trunk_groups.intersection(vlan["trunk_groups"]):
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
        if self._uplink_type != "port-channel":
            return accepted_vlans

        fabric_name = get(self._hostvars, "fabric_name", required=True)
        fabric_group = get(self._hostvars, f"groups.{fabric_name}", required=True)
        uplink_switches = unique(get(self._hostvars, "switch.uplink_switches", default=[]))
        uplink_switches = [uplink_switch for uplink_switch in uplink_switches if uplink_switch in fabric_group]
        for uplink_switch in uplink_switches:
            uplink_switch_vlans = get(
                self._hostvars,
                f"avd_switch_facts..{uplink_switch}..switch..vlans",
                default=[],
                separator="..",
                org_key="avd_switch_facts[{uplink_switch}].switch.vlans",
            )
            uplink_switch_vlans_list = range_expand(uplink_switch_vlans)
            uplink_switch_vlans_list = [int(vlan) for vlan in uplink_switch_vlans_list]
            accepted_vlans = [vlan for vlan in accepted_vlans if vlan in uplink_switch_vlans_list]

        return accepted_vlans

    @cached_property
    def _filter_tags(self) -> list[str]:
        """
        Return switch.filter_tags + switch.group if defined
        """
        filter_tags = get(self._hostvars, "switch.filter_tags", default=[])
        if (switch_group := get(self._hostvars, "switch.group")) is not None:
            filter_tags.append(switch_group)

        return filter_tags

    def _filtered_vrfs(self, tenant: dict) -> list[dict]:
        """
        Return sorted and filtered vrf list from given tenant.
        Filtering based on svi tags, l3interfaces and switch.always_include_vrfs_in_tenants.
        Keys of VRF data model will be converted to lists.
        """
        filtered_vrfs = []
        always_include_vrfs_in_tenants = get(self._hostvars, "switch.always_include_vrfs_in_tenants", default=[])

        vrfs: list[dict] = natural_sort(convert_dicts(tenant.get("vrfs", []), "name"), "name")
        for vrf in vrfs:
            bgp_peers = natural_sort(convert_dicts(vrf.get("bgp_peers"), "ip_address"), "ip_address")
            vrf["bgp_peers"] = [bgp_peer for bgp_peer in bgp_peers if self._hostname in bgp_peer.get("nodes", [])]
            vrf["static_routes"] = [route for route in vrf.get("static_routes", []) if self._hostname in route.get("nodes", [self._hostname])]
            vrf["ipv6_static_routes"] = [route for route in vrf.get("ipv6_static_routes", []) if self._hostname in route.get("nodes", [self._hostname])]
            vrf["svis"] = self._filtered_svis(vrf)
            vrf["l3_interfaces"] = [
                l3_interface
                for l3_interface in vrf.get("l3_interfaces", [])
                if (
                    self._hostname in l3_interface.get("nodes", [])
                    and l3_interface.get("ip_addresses") is not None
                    and l3_interface.get("interfaces") is not None
                )
            ]

            if self._evpn_multicast:
                vrf["_evpn_l3_multicast_enabled"] = default(get(vrf, "evpn_l3_multicast.enabled"), get(tenant, "evpn_l3_multicast.enabled"))

                rps = []
                for rp_address in default(get(vrf, "pim_rp_addresses"), get(tenant, "pim_rp_addresses"), []):
                    if self._hostname in get(rp_address, "nodes", default=[self._hostname]):
                        for rp_ip in get(
                            rp_address,
                            "rps",
                            required=True,
                            org_key=f"pim_rp_addresses.rps under VRF '{vrf['name']}' in Tenant '{tenant['name']}'",
                        ):
                            if rp_groups := get(rp_address, "groups"):
                                rps.append({"address": rp_ip, "groups": rp_groups})
                            else:
                                rps.append({"address": rp_ip})
                if rps:
                    vrf["_pim_rp_addresses"] = rps

                for evpn_peg in default(get(vrf, "evpn_l3_multicast.evpn_peg"), get(tenant, "evpn_l3_multicast.evpn_peg"), []):
                    if self._hostname in evpn_peg.get("nodes", [self._hostname]) and rps:
                        vrf["_evpn_l3_multicast_evpn_peg_transit"] = evpn_peg.get("transit")
                        break

            if vrf["svis"] or vrf["l3_interfaces"] or "all" in always_include_vrfs_in_tenants or tenant["name"] in always_include_vrfs_in_tenants:
                filtered_vrfs.append(vrf)

            vrf["additional_route_targets"] = [
                rt
                for rt in vrf.get("additional_route_targets", [])
                if (
                    self._hostname in rt.get("nodes", [self._hostname])
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

        The key "node_config" is inserted with relevant dict from "nodes" or {}
        """
        svi_profiles = convert_dicts(get(self._hostvars, "svi_profiles", default=[]), "profile")
        for svi_profile in svi_profiles:
            svi_profile["nodes"] = convert_dicts(svi_profile.get("nodes", []), "node")
            svi_profile["node_config"] = get_item(svi_profile["nodes"], "node", self._hostname, default={})

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
        svi_profile = {"node_config": {}}
        svi_parent_profile = {"node_config": {}}

        svi["nodes"] = convert_dicts(svi.get("nodes", []), "node")
        svi_node_config = get_item(svi.get("nodes", []), "node", self._hostname, default={})

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
            svi_parent_profile["node_config"],
            svi_profile["node_config"],
            svi_node_config,
            list_merge="replace",
            destructive_merge=False,
        )

        # Override structured configs since we don't want to deep-merge those
        merged_svi["structured_config"] = default(
            svi_node_config.get("structured_config"),
            svi_profile["node_config"].get("structured_config"),
            svi_parent_profile["node_config"].get("structured_config"),
            svi.get("structured_config"),
            svi_profile.get("structured_config"),
            svi_parent_profile.get("structured_config"),
        )

        # Override bgp.structured configs since we don't want to deep-merge those
        merged_svi.setdefault("bgp", {})["structured_config"] = default(
            get(svi_node_config, "bgp.structured_config"),
            get(svi_profile["node_config"], "bgp.structured_config"),
            get(svi_parent_profile["node_config"], "bgp.structured_config"),
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
        svis = [svi for svi in svis if "all" in self._filter_tags or set(svi.get("tags", ["all"])).intersection(self._filter_tags)]

        return svis
