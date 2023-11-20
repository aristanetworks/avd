# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import ipaddress
from functools import cached_property
from itertools import groupby as itertools_groupby
from re import fullmatch as re_fullmatch

from ansible_collections.arista.avd.plugins.filter.list_compress import list_compress
from ansible_collections.arista.avd.plugins.filter.natural_sort import natural_sort
from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError, AristaAvdMissingVariableError
from ansible_collections.arista.avd.plugins.plugin_utils.merge import merge
from ansible_collections.arista.avd.plugins.plugin_utils.strip_empties import strip_empties_from_dict
from ansible_collections.arista.avd.plugins.plugin_utils.utils import append_if_not_duplicate, default, get, get_item

from .utils import UtilsMixin


class RouterBgpMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def router_bgp(self) -> dict | None:
        """
        Return the structured config for router_bgp

        Changing legacy behavior is to only render this on vtep or mpls_ler
        by instead skipping vlans/bundles if not vtep or mpls_ler
        TODO: Fix so this also works for L2LS with VRFs
        """

        if not self.shared_utils.bgp:
            return None

        router_bgp = {
            "peer_groups": self._router_bgp_peer_groups,
            "vrfs": self._router_bgp_vrfs,
            "vlans": self._router_bgp_vlans,
            "vlan_aware_bundles": self._router_bgp_vlan_aware_bundles,
            "redistribute_routes": self._router_bgp_redistribute_routes,
            "vpws": self._router_bgp_vpws,
        }
        # Configure MLAG iBGP peer-group if needed
        if self._configure_bgp_mlag_peer_group:
            merge(router_bgp, self._router_bgp_mlag_peer_group())

        # Strip None values from vlan before returning
        router_bgp = {key: value for key, value in router_bgp.items() if value is not None}
        return router_bgp

    @cached_property
    def _router_bgp_peer_groups(self) -> list | None:
        """
        Return the structured config for router_bgp.peer_groups

        Covers two areas:
        - bgp_peer_groups defined under the vrf
        - adding route-map to the underlay peer-group in case of services in vrf default
        """

        if not self.shared_utils.network_services_l3:
            return None

        peer_groups = []
        peer_peergroups = set()
        for tenant in self._filtered_tenants:
            for vrf in tenant["vrfs"]:
                # bgp_peers is already filtered in _filtered_tenants to only contain entries with our hostname
                if not (vrf["bgp_peers"] or vrf.get("bgp_peer_groups")):
                    continue

                vrf_peer_peergroups = set([peer["peer_group"] for peer in vrf["bgp_peers"] if "peer_group" in peer])
                peer_groups.extend(
                    [
                        peer_group
                        for peer_group in vrf.get("bgp_peer_groups", [])
                        if (self.shared_utils.hostname in peer_group.get("nodes", []) or peer_group["name"] in vrf_peer_peergroups)
                    ]
                )
                peer_peergroups.update(vrf_peer_peergroups)

            peer_groups.extend(
                [
                    peer_group
                    for peer_group in tenant.get("bgp_peer_groups", [])
                    if (self.shared_utils.hostname in peer_group.get("nodes", []) or peer_group["name"] in peer_peergroups)
                ]
            )

        bgp_peer_groups = []
        if peer_groups:
            for peer_group in peer_groups:
                peer_group.pop("nodes", None)
                append_if_not_duplicate(
                    list_of_dicts=bgp_peer_groups,
                    primary_key="name",
                    new_dict=peer_group,
                    context="BGP Peer Groups defined under network services",
                    context_keys=["name"],
                )

        # router bgp default vrf configuration for evpn
        if self._vrf_default_evpn and (self._vrf_default_ipv4_subnets or self._vrf_default_ipv4_static_routes["static_routes"]):
            bgp_peer_groups.append(
                {
                    "name": self.shared_utils.bgp_peer_groups["ipv4_underlay_peers"]["name"],
                    "type": "ipv4",
                    "route_map_out": "RM-BGP-UNDERLAY-PEERS-OUT",
                }
            )

        if bgp_peer_groups:
            return bgp_peer_groups

        return None

    @cached_property
    def _router_bgp_vrfs(self) -> list | None:
        """
        Return structured config for router_bgp.vrfs

        TODO: Optimize this to allow bgp VRF config without overlays (vtep or mpls)
        """
        if not (self.shared_utils.overlay_vtep or self.shared_utils.overlay_ler):
            return None

        if not self.shared_utils.network_services_l3:
            return None

        vrfs = []

        for tenant in self._filtered_tenants:
            for vrf in tenant["vrfs"]:
                vrf_address_families = [af for af in vrf.get("address_families", ["evpn"]) if af in self.shared_utils.overlay_address_families]
                if not vrf_address_families:
                    continue

                vrf_name = vrf["name"]
                vrf_rd = self.get_vrf_rd(vrf)
                vrf_rt = self.get_vrf_rt(vrf)
                route_targets = {"import": [], "export": []}

                for af in vrf_address_families:
                    if (target := get_item(route_targets["import"], "address_family", af)) is None:
                        route_targets["import"].append({"address_family": af, "route_targets": [vrf_rt]})
                    else:
                        target["route_targets"].append(vrf_rt)

                    if (target := get_item(route_targets["export"], "address_family", af)) is None:
                        route_targets["export"].append({"address_family": af, "route_targets": [vrf_rt]})
                    else:
                        target["route_targets"].append(vrf_rt)

                for rt in vrf["additional_route_targets"]:
                    if (target := get_item(route_targets[rt["type"]], "address_family", rt["address_family"])) is None:
                        route_targets[rt["type"]].append({"address_family": rt["address_family"], "route_targets": [rt["route_target"]]})
                    else:
                        target["route_targets"].append(rt["route_target"])

                if vrf_name == "default" and self._vrf_default_evpn and self._vrf_default_ipv4_subnets:
                    # Special handling of vrf default.

                    if (target := get_item(route_targets["export"], "address_family", "evpn")) is None:
                        route_targets["export"].append({"address_family": "evpn", "route_targets": ["route-map RM-EVPN-EXPORT-VRF-DEFAULT"]})
                    else:
                        target.setdefault("route_targets", []).append("route-map RM-EVPN-EXPORT-VRF-DEFAULT")

                    bgp_vrf = {
                        "name": vrf_name,
                        "rd": vrf_rd,
                        "route_targets": route_targets,
                        "eos_cli": get(vrf, "bgp.raw_eos_cli"),
                        "struct_cfg": get(vrf, "bgp.structured_config"),
                    }
                    # Strip None values from vlan before appending
                    bgp_vrf = {key: value for key, value in bgp_vrf.items() if value is not None}

                    append_if_not_duplicate(
                        list_of_dicts=vrfs,
                        primary_key="name",
                        new_dict=bgp_vrf,
                        context="BGP VRFs defined under network services",
                        context_keys=["name"],
                    )

                    continue

                # Regular VRF handling (not "default" with EVPN)
                bgp_vrf = {
                    "name": vrf_name,
                    "router_id": self.shared_utils.router_id,
                    "rd": vrf_rd,
                    "route_targets": route_targets,
                    "redistribute_routes": [{"source_protocol": "connected"}],
                    "eos_cli": get(vrf, "bgp.raw_eos_cli"),
                    "struct_cfg": get(vrf, "bgp.structured_config"),
                    "evpn_multicast": get(vrf, "_evpn_l3_multicast_enabled"),
                }
                # MLAG IBGP Peering VLANs per VRF
                if (vlan_id := self._mlag_ibgp_peering_vlan_vrf(vrf, tenant)) is not None:
                    if not self._mlag_ibgp_peering_redistribute(vrf, tenant):
                        bgp_vrf["redistribute_routes"][0]["route_map"] = "RM-CONN-2-BGP-VRFS"

                    if self.shared_utils.underlay_rfc5549 and self.shared_utils.overlay_mlag_rfc5549:
                        interface_name = f"Vlan{vlan_id}"
                        bgp_vrf.setdefault("neighbor_interfaces", []).append(
                            {
                                "name": interface_name,
                                "peer_group": self.shared_utils.bgp_peer_groups["mlag_ipv4_underlay_peer"]["name"],
                                "remote_as": self.shared_utils.bgp_as,
                                "description": self.shared_utils.mlag_peer,
                            }
                        )
                    else:
                        if (mlag_ibgp_peering_ipv4_pool := vrf.get("mlag_ibgp_peering_ipv4_pool")) is not None:
                            if self.shared_utils.mlag_role == "primary":
                                ip_address = self.shared_utils.ip_addressing.mlag_ibgp_peering_ip_secondary(mlag_ibgp_peering_ipv4_pool)
                            else:
                                ip_address = self.shared_utils.ip_addressing.mlag_ibgp_peering_ip_primary(mlag_ibgp_peering_ipv4_pool)
                        else:
                            ip_address = self.shared_utils.mlag_peer_ibgp_ip

                        bgp_vrf.setdefault("neighbors", []).append(
                            {
                                "ip_address": ip_address,
                                "peer_group": self.shared_utils.bgp_peer_groups["mlag_ipv4_underlay_peer"]["name"],
                            }
                        )
                        if self.shared_utils.underlay_rfc5549:
                            bgp_vrf.setdefault("address_family_ipv4", {}).setdefault("neighbors", []).append(
                                {
                                    "ip_address": ip_address,
                                    "next_hop": {
                                        "address_family_ipv6": {
                                            "enabled": False,
                                        }
                                    },
                                }
                            )

                for bgp_peer in vrf["bgp_peers"]:
                    # Below we pop various keys that are not supported by the eos_cli_config_gen schema.
                    # The rest of the keys are relayed directly to eos_cli_config_gen.
                    # 'ip_address' is popped even though it is supported. It will be added again later
                    # to ensure it comes first in the generated dict.
                    peer_ip = bgp_peer.pop("ip_address")
                    address_family = f"address_family_ipv{ipaddress.ip_address(peer_ip).version}"
                    neighbor = strip_empties_from_dict(
                        {
                            "ip_address": peer_ip,
                            "activate": True,
                            "prefix_list_in": bgp_peer.pop("prefix_list_in", None),
                            "prefix_list_out": bgp_peer.pop("prefix_list_out", None),
                        }
                    )
                    bgp_vrf.setdefault(address_family, {}).setdefault("neighbors", []).append(neighbor)

                    if bgp_peer.get("set_ipv4_next_hop") is not None or bgp_peer.get("set_ipv6_next_hop") is not None:
                        route_map = f"RM-{vrf_name}-{peer_ip}-SET-NEXT-HOP-OUT"
                        bgp_peer["route_map_out"] = route_map
                        if bgp_peer.get("default_originate") is not None:
                            bgp_peer["default_originate"]["route_map"] = bgp_peer["default_originate"].get("route_map", route_map)

                        bgp_peer.pop("set_ipv4_next_hop", None)
                        bgp_peer.pop("set_ipv6_next_hop", None)

                    bgp_peer.pop("nodes", None)
                    bgp_vrf.setdefault("neighbors", []).append({"ip_address": peer_ip, **bgp_peer})

                bgp_vrf_redistribute_static = vrf.get("redistribute_static")
                if bgp_vrf_redistribute_static is True or (vrf["static_routes"] and bgp_vrf_redistribute_static is not False):
                    bgp_vrf["redistribute_routes"].append({"source_protocol": "static"})

                if (
                    get(vrf, "ospf.enabled") is True
                    and vrf.get("redistribute_ospf") is not False
                    and self.shared_utils.hostname in get(vrf, "ospf.nodes", default=[self.shared_utils.hostname])
                ):
                    bgp_vrf["redistribute_routes"].append({"source_protocol": "ospf"})

                if (evpn_multicast_transit_mode := get(vrf, "_evpn_l3_multicast_evpn_peg_transit")) is True:
                    bgp_vrf["evpn_multicast_address_family"] = {"ipv4": {"transit": evpn_multicast_transit_mode}}

                if bgp_vrf.get("neighbors"):
                    platform_bgp_update_wait_install = get(self.shared_utils.platform_settings, "feature_support.bgp_update_wait_install", default=True) is True
                    if get(self._hostvars, "bgp_update_wait_install", default=True) is True and platform_bgp_update_wait_install:
                        bgp_vrf.setdefault("updates", {})["wait_install"] = True

                # Strip None values from vlan before appending
                bgp_vrf = {key: value for key, value in bgp_vrf.items() if value is not None}

                append_if_not_duplicate(
                    list_of_dicts=vrfs,
                    primary_key="name",
                    new_dict=bgp_vrf,
                    context="BGP VRFs defined under network services",
                    context_keys=["name"],
                )

        if vrfs:
            return vrfs

        return None

    @cached_property
    def _router_bgp_vlans(self) -> list | None:
        """
        Return structured config for router_bgp.vlans
        """
        if not (
            self.shared_utils.network_services_l2
            and "evpn" in self.shared_utils.overlay_address_families
            and not self._evpn_vlan_aware_bundles
            and (self.shared_utils.overlay_vtep or self.shared_utils.overlay_ler)
            and (self.shared_utils.overlay_evpn)
        ):
            return None

        vlans = []
        for tenant in self._filtered_tenants:
            for vrf in tenant["vrfs"]:
                for svi in vrf["svis"]:
                    if (vlan := self._router_bgp_vlans_vlan(svi, tenant, vrf)) is not None:
                        vlan_id = int(svi["id"])
                        vlan = {"id": vlan_id, **vlan}
                        append_if_not_duplicate(
                            list_of_dicts=vlans,
                            primary_key="id",
                            new_dict=vlan,
                            context="BGP VLANs defined under network services",
                            context_keys=["id", "tenant"],
                            ignore_keys={"tenant"},
                        )

            # L2 Vlans per Tenant
            for l2vlan in tenant["l2vlans"]:
                if (vlan := self._router_bgp_vlans_vlan(l2vlan, tenant, vrf={})) is not None:
                    vlan_id = int(l2vlan["id"])
                    vlan = {"id": vlan_id, **vlan}
                    append_if_not_duplicate(
                        list_of_dicts=vlans,
                        primary_key="id",
                        new_dict=vlan,
                        context="BGP VLANs defined under network services",
                        context_keys=["id", "tenant"],
                        ignore_keys={"tenant"},
                    )

        if vlans:
            return vlans

        return None

    def _router_bgp_vlans_vlan(self, vlan, tenant, vrf) -> dict | None:
        """
        Return structured config for one given vlan under router_bgp.vlans
        """
        if vlan.get("vxlan") is False:
            return None

        vlan_rd = self.get_vlan_rd(vlan, tenant)
        vlan_rt = self.get_vlan_rt(vlan, tenant)

        bgp_vlan = {
            "tenant": vlan["tenant"],
            "rd": vlan_rd,
            "route_targets": {"both": [vlan_rt]},
            "redistribute_routes": ["learned"],
            "eos_cli": get(vlan, "bgp.raw_eos_cli"),
            "struct_cfg": get(vlan, "bgp.structured_config"),
        }
        if (
            self.shared_utils.evpn_gateway_vxlan_l2
            and default(vlan.get("evpn_l2_multi_domain"), vrf.get("evpn_l2_multi_domain"), tenant.get("evpn_l2_multi_domain"), True) is True
        ):
            bgp_vlan["rd_evpn_domain"] = {"domain": "remote", "rd": vlan_rd}
            bgp_vlan["route_targets"]["import_export_evpn_domains"] = [{"domain": "remote", "route_target": vlan_rt}]

        vlan_evpn_l2_multicast_enabled = default(get(vlan, "evpn_l2_multicast.enabled"), get(tenant, "evpn_l2_multicast.enabled"))
        if vlan_evpn_l2_multicast_enabled is True and self._evpn_multicast is not True:
            raise AristaAvdError(
                f"'evpn_l2_multicast: true' under VLAN {vlan['id']}({vlan['name']}) or Tenant {tenant['name']}; this requires 'evpn_multicast' to also be set"
                " to true."
            )
        if vlan_evpn_l2_multicast_enabled is True:
            bgp_vlan["redistribute_routes"].append("igmp")

        # Strip None values from vlan before returning
        bgp_vlan = {key: value for key, value in bgp_vlan.items() if value is not None}
        return bgp_vlan

    @cached_property
    def _evpn_vlan_aware_bundles(self) -> bool:
        return get(self._hostvars, "evpn_vlan_aware_bundles", default=False)

    def _get_vlan_aware_bundle_name_tuple(self, vlan: dict) -> tuple[str, bool] | None:
        """
        Return a tuple with string with the vlan-aware-bundle name for one VLAN and a boolean saying if this is a evpn_vlan_bundle.
        """
        if vlan.get("evpn_vlan_bundle") is not None:
            return (str(vlan.get("evpn_vlan_bundle")), True)
        return (str(vlan.get("name")), False)

    @cached_property
    def _router_bgp_vlan_aware_bundles(self) -> list | None:
        """
        Return structured config for router_bgp.vlan_aware_bundles
        """

        if not (self.shared_utils.network_services_l2 and self.shared_utils.overlay_evpn):
            return None

        if not self._evpn_vlan_aware_bundles:
            return None

        bundles = []
        for tenant in self._filtered_tenants:
            for vrf in tenant["vrfs"]:
                if (bundle := self._router_bgp_vlan_aware_bundles_vrf(vrf, tenant)) is not None:
                    append_if_not_duplicate(
                        list_of_dicts=bundles,
                        primary_key="name",
                        new_dict=bundle,
                        context="BGP VLAN-Aware Bundles defined under network services",
                        context_keys=["name"],
                    )

            # L2 Vlans per Tenant
            # If multiple L2 Vlans share the same evpn_vlan_bundle name, they will be part of the same vlan-aware-bundle else they use the vlan name as bundle
            sorted_vlan_list = sorted(tenant["l2vlans"], key=self._get_vlan_aware_bundle_name_tuple)
            bundle_groups = itertools_groupby(sorted_vlan_list, self._get_vlan_aware_bundle_name_tuple)
            for vlan_aware_bundle_name_tuple, l2vlans in bundle_groups:
                bundle_name, is_evpn_vlan_bundle = vlan_aware_bundle_name_tuple
                l2vlans = list(l2vlans)
                if is_evpn_vlan_bundle:
                    # If "evpn_vlan_bundle" in l2vlan bundle group, we use the same logic for rd/rt as VRFs
                    # using the settings under the given evpn_vlan_bundle only.

                    # check if the referred name exists in the global evpn_vlan_bundles
                    if (evpn_vlan_bundle := get_item(self._hostvars["evpn_vlan_bundles"], "name", bundle_name)) is None:
                        raise AristaAvdMissingVariableError(
                            "The 'evpn_vlan_bundle' of the l2vlans must be defined in the common 'evpn_vlan_bundles' setting. First occurence seen for l2vlan"
                            f" {l2vlans[0]['id']} in Tenant '{l2vlans[0]['tenant']}' and evpn_vlan_bundle '{l2vlans[0]['evpn_vlan_bundle']}'."
                        )

                    if (
                        bundle := self._router_bgp_vlan_aware_bundle(
                            name=evpn_vlan_bundle["name"],
                            vlans=l2vlans,
                            rd=self.get_vlan_aware_bundle_rd(
                                id=evpn_vlan_bundle["id"], tenant=tenant, is_vrf=False, rd_override=evpn_vlan_bundle.get("rd_override")
                            ),
                            rt=self.get_vlan_aware_bundle_rt(
                                id=evpn_vlan_bundle["id"],
                                vni=evpn_vlan_bundle["id"],
                                tenant=tenant,
                                is_vrf=False,
                                rt_override=evpn_vlan_bundle.get("rt_override"),
                            ),
                            evpn_l2_multi_domain=default(evpn_vlan_bundle.get("evpn_l2_multi_domain"), tenant.get("evpn_l2_multi_domain", True)) is True,
                            tenant=tenant,
                        )
                    ) is None:
                        # Skip bundle since no vlans were enabled for vxlan.
                        continue

                    if (eos_cli := get(evpn_vlan_bundle, "bgp.raw_eos_cli")) is not None:
                        bundle["eos_cli"] = eos_cli

                else:
                    # Without "evpn_vlan_bundle" we fall back to per-vlan behavior
                    if (bundle := self._router_bgp_vlans_vlan(l2vlans[0], tenant, vrf={})) is None:
                        # Skip bundle since no vlans were enabled for vxlan.
                        continue

                    # We are reusing the regular bgp vlan function so need to add vlan info
                    bundle["vlan"] = list_compress([int(l2vlan["id"]) for l2vlan in l2vlans])
                    bundle = {"name": bundle_name, **bundle}

                append_if_not_duplicate(
                    list_of_dicts=bundles,
                    primary_key="name",
                    new_dict=bundle,
                    context=(
                        "BGP VLAN-Aware Bundles defined under network services. A common reason is that an 'l2vlan' name overlaps with an 'evpn_vlan_bundle'"
                        " name"
                    ),
                    context_keys=["name"],
                )

        if bundles:
            return bundles

        return None

    def _router_bgp_vlan_aware_bundles_vrf(self, vrf, tenant) -> dict | None:
        """
        Return structured config for one vrf under router_bgp.vlan_aware_bundles
        """
        return self._router_bgp_vlan_aware_bundle(
            name=vrf["name"],
            vlans=vrf["svis"],
            rd=self.get_vlan_aware_bundle_rd(id=self.get_vrf_id(vrf), tenant=tenant, is_vrf=True),
            rt=self.get_vlan_aware_bundle_rt(id=self.get_vrf_id(vrf), vni=self.get_vrf_vni(vrf), tenant=tenant, is_vrf=True),
            evpn_l2_multi_domain=default(vrf.get("evpn_l2_multi_domain"), tenant.get("evpn_l2_multi_domain", True)) is True,
            tenant=tenant,
        )

    def _router_bgp_vlan_aware_bundle(self, name: str, vlans: list, rd: str, rt: str, evpn_l2_multi_domain: bool, tenant: dict) -> dict | None:
        """
        Return structured config for one vlan-aware-bundle.
        Used for VRFs and bundles defined under "evpn_vlan_bundles" referred by l2vlans (and later also SVIs)
        """
        vlans = [vlan for vlan in vlans if vlan.get("vxlan") is not False]
        if not vlans:
            return None

        bundle = {
            "name": name,
            "rd": rd,
            "route_targets": {
                "both": [rt],
            },
            "redistribute_routes": ["learned"],
            "vlan": list_compress([int(vlan["id"]) for vlan in vlans]),
        }
        if self.shared_utils.evpn_gateway_vxlan_l2 and evpn_l2_multi_domain:
            bundle["rd_evpn_domain"] = {"domain": "remote", "rd": rd}
            bundle["route_targets"]["import_export_evpn_domains"] = [{"domain": "remote", "route_target": rt}]

        evpn_l2_multicast_enabled_vlans = [vlan for vlan in vlans if get(vlan, "evpn_l2_multicast.enabled", get(tenant, "evpn_l2_multicast.enabled")) is True]
        if evpn_l2_multicast_enabled_vlans:
            bundle["redistribute_routes"].append("igmp")

        return bundle

    @cached_property
    def _rt_admin_subfield(self) -> str | None:
        """
        Return a string with the route-target admin subfield unless set to "vrf_id" or "vrf_vni" or "id".
        Returns None if not set, since the calling functions will use
        per-vlan numbers by default.
        """
        admin_subfield = self.shared_utils.overlay_rt_type["admin_subfield"]
        if admin_subfield is None:
            return None

        if admin_subfield == "bgp_as":
            return self.shared_utils.bgp_as

        if re_fullmatch(r"[0-9]+", str(admin_subfield)):
            return admin_subfield

        return None

    def get_vlan_mac_vrf_id(self, vlan, tenant) -> int:
        mac_vrf_id_base = default(tenant.get("mac_vrf_id_base"), tenant.get("mac_vrf_vni_base"))
        if mac_vrf_id_base is None:
            raise AristaAvdMissingVariableError(
                "'rt_override' or 'vni_override' or 'mac_vrf_id_base' or 'mac_vrf_vni_base' must be set. "
                f"Unable to set EVPN RD/RT for vlan {vlan['id']} in Tenant '{vlan['tenant']}'"
            )
        return mac_vrf_id_base + int(vlan["id"])

    def get_vlan_mac_vrf_vni(self, vlan, tenant) -> int:
        mac_vrf_vni_base = default(tenant.get("mac_vrf_vni_base"), tenant.get("mac_vrf_id_base"))
        if mac_vrf_vni_base is None:
            raise AristaAvdMissingVariableError(
                "'rt_override' or 'vni_override' or 'mac_vrf_id_base' or 'mac_vrf_vni_base' must be set. "
                f"Unable to set EVPN RD/RT for vlan {vlan['id']} in Tenant '{vlan['tenant']}'"
            )
        return mac_vrf_vni_base + int(vlan["id"])

    def get_vlan_rd(self, vlan, tenant) -> str:
        """
        Return a string with the route-destinguisher for one VLAN
        """
        rd_override = default(vlan.get("rd_override"), vlan.get("rt_override"), vlan.get("vni_override"))

        if ":" in str(rd_override):
            return rd_override

        if rd_override is not None:
            assigned_number_subfield = rd_override
        elif self.shared_utils.overlay_rd_type["vlan_assigned_number_subfield"] == "mac_vrf_vni":
            assigned_number_subfield = self.get_vlan_mac_vrf_vni(vlan, tenant)
        elif self.shared_utils.overlay_rd_type["vlan_assigned_number_subfield"] == "vlan_id":
            assigned_number_subfield = vlan["id"]
        else:
            assigned_number_subfield = self.get_vlan_mac_vrf_id(vlan, tenant)

        return f"{self.shared_utils.overlay_rd_type_admin_subfield}:{assigned_number_subfield}"

    def get_vlan_rt(self, vlan: dict, tenant: dict) -> str:
        """
        Return a string with the route-target for one VLAN
        """
        rt_override = default(vlan.get("rt_override"), vlan.get("vni_override"))

        if ":" in str(rt_override):
            return rt_override

        if self._rt_admin_subfield is not None:
            admin_subfield = self._rt_admin_subfield
        elif rt_override is not None:
            admin_subfield = rt_override
        elif self.shared_utils.overlay_rt_type["admin_subfield"] == "vrf_vni":
            admin_subfield = self.get_vlan_mac_vrf_vni(vlan, tenant)
        elif self.shared_utils.overlay_rt_type["admin_subfield"] == "id":
            admin_subfield = vlan["id"]
        else:
            admin_subfield = self.get_vlan_mac_vrf_id(vlan, tenant)

        if rt_override is not None:
            assigned_number_subfield = rt_override
        elif self.shared_utils.overlay_rt_type["vlan_assigned_number_subfield"] == "mac_vrf_vni":
            assigned_number_subfield = self.get_vlan_mac_vrf_vni(vlan, tenant)
        elif self.shared_utils.overlay_rt_type["vlan_assigned_number_subfield"] == "vlan_id":
            assigned_number_subfield = vlan["id"]
        else:
            assigned_number_subfield = self.get_vlan_mac_vrf_id(vlan, tenant)

        return f"{admin_subfield}:{assigned_number_subfield}"

    @cached_property
    def _vrf_rt_admin_subfield(self) -> str | None:
        """
        Return a string with the VRF route-target admin subfield unless set to "vrf_id" or "vrf_vni" or "id".
        Returns None if not set, since the calling functions will use
        per-vrf numbers by default.
        """
        admin_subfield = self.shared_utils.overlay_rt_type["vrf_admin_subfield"]
        if admin_subfield is None:
            return None

        if admin_subfield == "bgp_as":
            return self.shared_utils.bgp_as

        if re_fullmatch(r"[0-9]+", str(admin_subfield)):
            return admin_subfield

        return None

    def get_vrf_id(self, vrf) -> int:
        vrf_id = default(vrf.get("vrf_id"), vrf.get("vrf_vni"))
        if vrf_id is None:
            raise AristaAvdMissingVariableError(f"'vrf_id' or 'vrf_vni' for VRF '{vrf['name']} must be set.")
        return int(vrf_id)

    def get_vrf_vni(self, vrf) -> int:
        vrf_vni = default(vrf.get("vrf_vni"), vrf.get("vrf_id"))
        if vrf_vni is None:
            raise AristaAvdMissingVariableError(f"'vrf_vni' or 'vrf_id' for VRF '{vrf['name']} must be set.")
        return int(vrf_vni)

    def get_vrf_rd(self, vrf) -> str:
        """
        Return a string with the route-destinguisher for one VRF
        """
        return f"{self.shared_utils.overlay_rd_type_vrf_admin_subfield}:{self.get_vrf_id(vrf)}"

    def get_vrf_rt(self, vrf: dict) -> str:
        """
        Return a string with the route-target for one VRF
        """
        if self._vrf_rt_admin_subfield is not None:
            admin_subfield = self._vrf_rt_admin_subfield
        elif self.shared_utils.overlay_rt_type["vrf_admin_subfield"] == "vrf_vni":
            admin_subfield = self.get_vrf_vni(vrf)
        else:
            # Both for 'id' and 'vrf_id' options.
            admin_subfield = self.get_vrf_id(vrf)

        return f"{admin_subfield}:{self.get_vrf_id(vrf)}"

    def get_vlan_aware_bundle_rd(self, id: int, tenant: dict, is_vrf: bool, rd_override: str = None) -> str:
        """
        Return a string with the route-destinguisher for one VLAN Aware Bundle
        """
        if is_vrf:
            admin_subfield = self.shared_utils.overlay_rd_type_vrf_admin_subfield
        else:
            admin_subfield = self.shared_utils.overlay_rd_type_admin_subfield

        if rd_override is not None:
            if ":" in str(rd_override):
                return rd_override

            return f"{admin_subfield}:{rd_override}"

        bundle_number = id + int(get(tenant, "vlan_aware_bundle_number_base", default=0))
        return f"{admin_subfield}:{bundle_number}"

    def get_vlan_aware_bundle_rt(self, id: int, vni: int, tenant: dict, is_vrf: bool, rt_override: str = None) -> str:
        """
        Return a string with the route-target for one VLAN Aware Bundle
        """
        if rt_override is not None and ":" in str(rt_override):
            return rt_override

        bundle_number = id + int(get(tenant, "vlan_aware_bundle_number_base", default=0))

        if is_vrf and self._vrf_rt_admin_subfield is not None:
            admin_subfield = self._vrf_rt_admin_subfield
        elif is_vrf and self.shared_utils.overlay_rt_type["vrf_admin_subfield"] == "vrf_vni":
            admin_subfield = vni
        else:
            # Both for 'id' and 'vrf_id' options.
            admin_subfield = bundle_number

        if rt_override is not None:
            return f"{admin_subfield}:{rt_override}"

        return f"{admin_subfield}:{bundle_number}"

    @cached_property
    def _router_bgp_redistribute_routes(self) -> dict | None:
        """
        Return structured config for router_bgp.redistribute_routes

        Add redistribute static to default if either "redistribute_in_overlay" is set or
        "redistribute_in_underlay" and underlay protocol is BGP.
        """
        if self._vrf_default_ipv4_static_routes["redistribute_in_overlay"] or (
            self._vrf_default_ipv4_static_routes["redistribute_in_underlay"] and self.shared_utils.underlay_bgp
        ):
            return [{"source_protocol": "static"}]

        return None

    @cached_property
    def _router_bgp_vpws(self) -> list[dict] | None:
        """
        Return structured config for router_bgp.vpws
        """

        if not (self.shared_utils.network_services_l1 and self.shared_utils.overlay_ler and self.shared_utils.overlay_evpn_mpls):
            return None

        vpws = []
        for tenant in self._filtered_tenants:
            if "point_to_point_services" not in tenant:
                continue

            if get(tenant, "pseudowire_rt_base") is None:
                continue

            pseudowires = []
            for point_to_point_service in natural_sort(tenant["point_to_point_services"], "name"):
                if subifs := point_to_point_service.get("subinterfaces", []):
                    subifs = [subif for subif in subifs if subif.get("number") is not None]

                endpoints = point_to_point_service.get("endpoints", [])
                for local_index, endpoint in enumerate(endpoints):
                    if not (self.shared_utils.hostname in endpoint.get("nodes", []) and endpoint.get("interfaces") is not None):
                        continue

                    # Endpoints can only have two entries with index 0 and 1.
                    # So the remote must be the other index.
                    remote_endpoint = endpoints[(local_index + 1) % 2]

                    if subifs:
                        for subif in subifs:
                            subif_number = int(subif["number"])
                            pseudowires.append(
                                {
                                    "name": f"{point_to_point_service['name']}_{subif_number}",
                                    "id_local": int(endpoint["id"]) + subif_number,
                                    "id_remote": int(remote_endpoint["id"]) + subif_number,
                                }
                            )

                    else:
                        pseudowires.append(
                            {
                                "name": f"{point_to_point_service['name']}",
                                "id_local": int(endpoint["id"]),
                                "id_remote": int(remote_endpoint["id"]),
                            }
                        )

            if pseudowires:
                rt_base = get(tenant, "pseudowire_rt_base", required=True, org_key=f"'pseudowire_rt_base' under Tenant '{tenant['name']}")
                rd = f"{self.shared_utils.overlay_rd_type_admin_subfield}:{rt_base}"
                rt = f"{self._rt_admin_subfield or rt_base}:{rt_base}"
                vpws.append(
                    {
                        "name": tenant["name"],
                        "rd": rd,
                        "route_targets": {"import_export": rt},
                        "pseudowires": pseudowires,
                    }
                )

        if vpws:
            return vpws

        return None

    def _router_bgp_mlag_peer_group(self) -> dict:
        """
        Return a partial router_bgp structured_config covering the MLAG peer_group
        and associated address_family activations

        TODO: Partially duplicated from mlag. Should be moved to a common class
        """
        peer_group_name = self.shared_utils.bgp_peer_groups["mlag_ipv4_underlay_peer"]["name"]
        router_bgp = {}
        peer_group = {
            "name": peer_group_name,
            "type": "ipv4",
            "remote_as": self.shared_utils.bgp_as,
            "next_hop_self": True,
            "description": self.shared_utils.mlag_peer,
            "password": self.shared_utils.bgp_peer_groups["mlag_ipv4_underlay_peer"]["password"],
            "maximum_routes": 12000,
            "send_community": "all",
            "struct_cfg": self.shared_utils.bgp_peer_groups["mlag_ipv4_underlay_peer"]["structured_config"],
        }

        if self.shared_utils.mlag_ibgp_origin_incomplete is True:
            peer_group["route_map_in"] = "RM-MLAG-PEER-IN"

        router_bgp["peer_groups"] = [peer_group]

        if self.shared_utils.underlay_ipv6:
            router_bgp["address_family_ipv6"] = {
                "peer_groups": [
                    {
                        "name": peer_group_name,
                        "activate": True,
                    }
                ]
            }

        address_family_ipv4_peer_group = {"name": peer_group_name, "activate": True}
        if self.shared_utils.underlay_rfc5549:
            address_family_ipv4_peer_group["next_hop"] = {"address_family_ipv6": {"enabled": True, "originate": True}}

        router_bgp["address_family_ipv4"] = {"peer_groups": [address_family_ipv4_peer_group]}
        return strip_empties_from_dict(router_bgp)
