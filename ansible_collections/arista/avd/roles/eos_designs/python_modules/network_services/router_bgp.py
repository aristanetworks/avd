from __future__ import annotations

import ipaddress
from functools import cached_property
from re import fullmatch as re_fullmatch

from ansible_collections.arista.avd.plugins.filter.list_compress import list_compress
from ansible_collections.arista.avd.plugins.filter.natural_sort import natural_sort
from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdMissingVariableError
from ansible_collections.arista.avd.plugins.plugin_utils.merge import merge
from ansible_collections.arista.avd.plugins.plugin_utils.strip_empties import strip_empties_from_dict
from ansible_collections.arista.avd.plugins.plugin_utils.utils import default, get, groupby

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

        if not (self._bgp_as):
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
    def _router_bgp_peer_groups(self) -> dict | None:
        """
        Return the structured config for router_bgp.peer_groups

        Covers two areas:
        - bgp_peer_groups defined under the vrf
        - adding route-map to the underlay peer-group in case of services in vrf default
        """

        if not self._network_services_l3:
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
                        if (self._hostname in peer_group.get("nodes", []) or peer_group["name"] in vrf_peer_peergroups)
                    ]
                )
                peer_peergroups.update(vrf_peer_peergroups)

            peer_groups.extend(
                [
                    peer_group
                    for peer_group in tenant.get("bgp_peer_groups", [])
                    if (self._hostname in peer_group.get("nodes", []) or peer_group["name"] in peer_peergroups)
                ]
            )

        bgp_peer_groups = {}
        if peer_groups:
            for peer_group in peer_groups:
                peer_group_name = peer_group.pop("name")
                peer_group.pop("nodes", None)
                bgp_peer_groups[peer_group_name] = peer_group

        # router bgp default vrf configuration for evpn
        if (self._vrf_default_ipv4_subnets or self._vrf_default_ipv4_static_routes["static_routes"]) and self._overlay_vtep and self._overlay_evpn:
            peer_group_name = self._peer_group_ipv4_underlay_peers_name
            bgp_peer_groups[peer_group_name] = {
                "type": "ipv4",
                "route_map_out": "RM-BGP-UNDERLAY-PEERS-OUT",
            }

        if bgp_peer_groups:
            return bgp_peer_groups

        return None

    @cached_property
    def _router_bgp_vrfs(self) -> dict | None:
        """
        Return structured config for router_bgp.vrfs

        TODO: Optimize this to allow bgp VRF config without overlays (vtep or mpls)
        """
        if not (self._overlay_vtep or self._overlay_ler):
            return None

        if not self._network_services_l3:
            return None

        vrfs = {}
        for tenant in self._filtered_tenants:
            for vrf in tenant["vrfs"]:
                vrf_address_families = [af for af in vrf.get("address_families", ["evpn"]) if af in self._overlay_address_families]
                if not vrf_address_families:
                    continue

                vrf_name = vrf["name"]

                if (bgp_vrf_id := vrf.get("vrf_id", vrf.get("vrf_vni"))) is None:
                    raise AristaAvdMissingVariableError(f"'vrf_id' or 'vrf_vni' for VRF '{vrf_name}")

                leaf_overlay_rt = f"{self._rt_admin_subfield or bgp_vrf_id}:{bgp_vrf_id}"
                route_targets = {
                    "import": {af: [leaf_overlay_rt] for af in vrf_address_families},
                    "export": {af: [leaf_overlay_rt] for af in vrf_address_families},
                }
                for rt in vrf["additional_route_targets"]:
                    route_targets.setdefault(rt["type"], {}).setdefault(rt["address_family"], []).append(rt["route_target"])

                if vrf_name == "default" and self._overlay_evpn and self._vrf_default_ipv4_subnets:
                    # Special handling of vrf default.
                    route_targets["export"].setdefault("evpn", []).append("route-map RM-EVPN-EXPORT-VRF-DEFAULT")
                    bgp_vrf = {
                        "rd": f"{self._overlay_rd_type_admin_subfield}:{bgp_vrf_id}",
                        "route_targets": route_targets,
                        "eos_cli": get(vrf, "bgp.raw_eos_cli"),
                        "struct_cfg": get(vrf, "bgp.structured_config"),
                    }
                    # Strip None values from vlan before returning
                    bgp_vrf = {key: value for key, value in bgp_vrf.items() if value is not None}
                    vrfs[vrf_name] = bgp_vrf
                    continue

                bgp_vrf = {
                    "router_id": self._router_id,
                    "rd": f"{self._overlay_rd_type_admin_subfield}:{bgp_vrf_id}",
                    "route_targets": route_targets,
                    "redistribute_routes": ["connected"],
                    "eos_cli": get(vrf, "bgp.raw_eos_cli"),
                    "struct_cfg": get(vrf, "bgp.structured_config"),
                    "evpn_multicast": get(vrf, "_evpn_l3_multicast_enabled"),
                }
                # MLAG IBGP Peering VLANs per VRF
                if (vlan_id := self._mlag_ibgp_peering_vlan_vrf(vrf, tenant)) is not None:
                    if self._underlay_rfc5549 and self._overlay_mlag_rfc5549:
                        interface_name = f"Vlan{vlan_id}"
                        bgp_vrf.setdefault("neighbor_interfaces", {})[interface_name] = {
                            "peer_group": self._peer_group_mlag_ipv4_underlay_peer_name,
                            "remote_as": self._bgp_as,
                            "description": self._mlag_peer,
                        }

                    else:
                        if (mlag_ibgp_peering_ipv4_pool := vrf.get("mlag_ibgp_peering_ipv4_pool")) is not None:
                            if self._mlag_role == "primary":
                                ip_address = self._avd_ip_addressing.mlag_ibgp_peering_ip_secondary(mlag_ibgp_peering_ipv4_pool)
                            else:
                                ip_address = self._avd_ip_addressing.mlag_ibgp_peering_ip_primary(mlag_ibgp_peering_ipv4_pool)
                        else:
                            ip_address = self._mlag_peer_ibgp_ip

                        bgp_vrf.setdefault("neighbors", {})[ip_address] = {"peer_group": self._peer_group_mlag_ipv4_underlay_peer_name}

                address_families = {}
                for bgp_peer in vrf["bgp_peers"]:
                    peer_ip = bgp_peer.pop("ip_address")
                    address_family = f"ipv{ipaddress.ip_address(peer_ip).version}"
                    address_families.setdefault(address_family, {}).setdefault("neighbors", {})[peer_ip] = {"activate": True}
                    if bgp_peer.get("set_ipv4_next_hop") is not None or bgp_peer.get("set_ipv6_next_hop") is not None:
                        route_map = f"RM-{vrf_name}-{peer_ip}-SET-NEXT-HOP-OUT"
                        bgp_peer["route_map_out"] = route_map
                        if bgp_peer.get("default_originate") is not None:
                            bgp_peer["default_originate"]["route_map"] = bgp_peer["default_originate"].get("route_map", route_map)

                        bgp_peer.pop("set_ipv4_next_hop", None)
                        bgp_peer.pop("set_ipv6_next_hop", None)

                    bgp_peer.pop("nodes", None)
                    bgp_vrf.setdefault("neighbors", {})[peer_ip] = bgp_peer

                bgp_vrf_redistribute_static = vrf.get("redistribute_static")
                if bgp_vrf_redistribute_static is True or (vrf["static_routes"] and bgp_vrf_redistribute_static is not False):
                    bgp_vrf["redistribute_routes"].append("static")

                if (
                    get(vrf, "ospf.enabled") is True
                    and vrf.get("redistribute_ospf") is not False
                    and self._hostname in get(vrf, "ospf.nodes", default=[self._hostname])
                ):
                    bgp_vrf["redistribute_routes"].append("ospf")

                if address_families:
                    bgp_vrf["address_families"] = address_families

                if (evpn_multicast_transit_mode := get(vrf, "_evpn_l3_multicast_evpn_peg_transit")) is True:
                    bgp_vrf["evpn_multicast_address_family"] = {"ipv4": {"transit": evpn_multicast_transit_mode}}

                # Strip None values from vlan before returning
                bgp_vrf = {key: value for key, value in bgp_vrf.items() if value is not None}
                vrfs[vrf_name] = bgp_vrf

        if vrfs:
            return vrfs

        return None

    @cached_property
    def _router_bgp_vlans(self) -> dict | None:
        """
        Return structured config for router_bgp.vlans
        """
        if not (
            self._network_services_l2
            and "evpn" in self._overlay_address_families
            and not self._evpn_vlan_aware_bundles
            and (self._overlay_vtep or self._overlay_ler)
            and (self._overlay_evpn)
        ):
            return None

        vlans = {}
        for tenant in self._filtered_tenants:
            for vrf in tenant["vrfs"]:
                for svi in vrf["svis"]:
                    if (vlan := self._router_bgp_vlans_vlan(svi, tenant, vrf)) is not None:
                        vlan_id = int(svi["id"])
                        vlans[vlan_id] = vlan

            # L2 Vlans per Tenant
            for l2vlan in tenant["l2vlans"]:
                if (vlan := self._router_bgp_vlans_vlan(l2vlan, tenant, vrf={})) is not None:
                    vlan_id = int(l2vlan["id"])
                    vlans[vlan_id] = vlan

        if vlans:
            return vlans

        return None

    def _router_bgp_vlans_vlan(self, vlan, tenant, vrf) -> dict | None:
        """
        Return structured config for one given vlan under router_bgp.vlans
        """
        if vlan.get("vxlan") is False:
            return None

        vlan_id = int(vlan["id"])
        tenant_mac_vrf_id_base = default(tenant.get("mac_vrf_id_base"), tenant.get("mac_vrf_vni_base"))
        rt_override = default(
            vlan.get("rt_override"),
            vlan.get("vni_override"),
        )
        if rt_override is None and tenant_mac_vrf_id_base is None:
            raise AristaAvdMissingVariableError(
                "'rt_override' or 'vni_override' or 'mac_vrf_id_base' or 'mac_vrf_vni_base' must be set. "
                f"Unable to set EVPN RD/RT for vlan {vlan_id} in Tenant '{tenant['name']}'"
            )

        vlan_rt_id = default(rt_override, (tenant_mac_vrf_id_base + vlan_id))
        vlan_rd = f"{self._overlay_rd_type_admin_subfield}:{vlan_rt_id}"
        vlan_rt = f"{self._rt_admin_subfield or vlan_rt_id}:{vlan_rt_id}"
        bgp_vlan = {
            "tenant": tenant["name"],
            "rd": vlan_rd,
            "route_targets": {"both": [vlan_rt]},
            "redistribute_routes": ["learned"],
            "eos_cli": get(vlan, "bgp.raw_eos_cli"),
            "struct_cfg": get(vlan, "bgp.structured_config"),
        }
        if (
            self._evpn_gateway_vxlan_l2
            and default(vlan.get("evpn_l2_multi_domain"), vrf.get("evpn_l2_multi_domain"), tenant.get("evpn_l2_multi_domain"), True) is True
        ):
            bgp_vlan["rd_evpn_domain"] = {"domain": "remote", "rd": vlan_rd}
            bgp_vlan["route_targets"]["import_export_evpn_domains"] = [{"domain": "remote", "route_target": vlan_rt}]

        vlan_evpn_l2_multicast_enabled = default(get(vlan, "evpn_l2_multicast.enabled"), get(tenant, "evpn_l2_multicast.enabled"))
        if vlan_evpn_l2_multicast_enabled is True:
            bgp_vlan["redistribute_routes"].append("igmp")

        # Strip None values from vlan before returning
        bgp_vlan = {key: value for key, value in bgp_vlan.items() if value is not None}
        return bgp_vlan

    @cached_property
    def _evpn_gateway_vxlan_l2(self) -> bool:
        return get(self._hostvars, "switch.evpn_gateway_vxlan_l2") is True

    @cached_property
    def _evpn_vlan_aware_bundles(self) -> bool:
        return default(get(self._hostvars, "vxlan_vlan_aware_bundles"), get(self._hostvars, "evpn_vlan_aware_bundles"), False)

    @cached_property
    def _router_bgp_vlan_aware_bundles(self) -> dict | None:
        """
        Return structured config for router_bgp.vlan_aware_bundles
        """

        if not (self._network_services_l2 and self._overlay_evpn):
            return None

        if not self._evpn_vlan_aware_bundles:
            return None

        bundles = {}
        for tenant in self._filtered_tenants:
            for vrf in tenant["vrfs"]:
                if (bundle := self._router_bgp_vlan_aware_bundles_vrf(vrf, tenant)) is not None:
                    bundle_name = vrf["name"]
                    bundles[bundle_name] = bundle

            # L2 Vlans per Tenant
            # If multiple L2 Vlans share the same name, they will be part of the same bundle
            for bundle_name, l2vlans in groupby(tenant["l2vlans"], "name"):
                l2vlans = list(l2vlans)
                if (bundle := self._router_bgp_vlans_vlan(l2vlans[0], tenant, vrf={})) is not None:
                    # We are reusing the regular bgp vlan function so need to add vlan info
                    bundle["vlan"] = list_compress([int(l2vlan["id"]) for l2vlan in l2vlans])
                    bundles[bundle_name] = bundle

        if bundles:
            return bundles

        return None

    def _router_bgp_vlan_aware_bundles_vrf(self, vrf, tenant) -> dict | None:
        """
        Return structured config for one vrf under router_bgp.vlan_aware_bundles
        """
        vlans = [vlan for vlan in vrf["svis"] if vlan.get("vxlan") is not False]
        if not vlans:
            return None

        vrf_name = vrf["name"]
        if (bgp_vrf_id := vrf.get("vrf_id", vrf.get("vrf_vni"))) is None:
            raise AristaAvdMissingVariableError(f"'vrf_id' or 'vrf_vni' for VRF '{vrf_name}")

        bundle_number = int(bgp_vrf_id) + int(tenant.get("vlan_aware_bundle_number_base", 0))

        bundle_rd = f"{self._overlay_rd_type_admin_subfield}:{bundle_number}"
        bundle_rt = f"{self._rt_admin_subfield or bundle_number}:{bundle_number}"
        bundle = {
            "rd": bundle_rd,
            "route_targets": {
                "both": [bundle_rt],
            },
            "redistribute_routes": ["learned"],
            "vlan": list_compress([int(vlan["id"]) for vlan in vlans]),
        }
        if self._evpn_gateway_vxlan_l2 and default(vrf.get("evpn_l2_multi_domain"), tenant.get("evpn_l2_multi_domain", True)) is True:
            bundle["rd_evpn_domain"] = {"domain": "remote", "rd": bundle_rd}
            bundle["route_targets"]["import_export_evpn_domains"] = [{"domain": "remote", "route_target": bundle_rt}]

        evpn_l2_multicast_enabled_vlans = [vlan for vlan in vlans if get(vlan, "evpn_l2_multicast.enabled", get(tenant, "evpn_l2_multicast.enabled")) is True]
        if evpn_l2_multicast_enabled_vlans:
            bundle["redistribute_routes"].append("igmp")

        return bundle

    @cached_property
    def _rt_admin_subfield(self) -> str | None:
        """
        Return a string with the route-target admin subfield
        Returns None if not set, since the calling functions will use
        per-vlan or per-vrf numbers by default.
        """
        admin_subfield = get(self._hostvars, "overlay_rt_type.admin_subfield")
        if admin_subfield is None:
            return None

        if admin_subfield == "bgp_as":
            return self._bgp_as

        if re_fullmatch(r"[0-9]+", str(admin_subfield)):
            return admin_subfield

        return None

    @cached_property
    def _router_bgp_redistribute_routes(self) -> dict | None:
        """
        Return structured config for router_bgp.redistribute_routes

        Add redistribute static to default if either "redistribute_in_overlay" is set or
        "redistribute_in_underlay" and underlay protocol is BGP.
        """
        if self._vrf_default_ipv4_static_routes["redistribute_in_overlay"] or (
            self._vrf_default_ipv4_static_routes["redistribute_in_underlay"] and self._underlay_bgp
        ):
            return {"static": {}}

        return None

    @cached_property
    def _router_bgp_vpws(self) -> list[dict] | None:
        """
        Return structured config for router_bgp.vpws
        """

        if not (self._network_services_l1 and self._overlay_ler and self._overlay_evpn_mpls):
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
                    if not (self._hostname in endpoint.get("nodes", []) and endpoint.get("interfaces") is not None):
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
                rd = f"{self._overlay_rd_type_admin_subfield}:{rt_base}"
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
        peer_group_name = self._peer_group_mlag_ipv4_underlay_peer_name
        router_bgp = {}
        peer_group = {
            "type": "ipv4",
            "remote_as": self._bgp_as,
            "next_hop_self": True,
            "description": self._mlag_peer,
            "password": get(self._hostvars, "switch.bgp_peer_groups.mlag_ipv4_underlay_peer.password"),
            "maximum_routes": 12000,
            "send_community": "all",
            "struct_cfg": get(self._hostvars, "switch.bgp_peer_groups.mlag_ipv4_underlay_peer.structured_config"),
        }

        if self._mlag_ibgp_origin_incomplete is True:
            peer_group["route_map_in"] = "RM-MLAG-PEER-IN"

        router_bgp["peer_groups"] = {peer_group_name: peer_group}

        if get(self._hostvars, "switch.underlay_ipv6") is True:
            router_bgp["address_family_ipv6"] = {
                "peer_groups": {
                    peer_group_name: {
                        "activate": True,
                    }
                }
            }

        address_family_ipv4_peer_group = {"activate": True}
        if self._underlay_rfc5549 is True:
            address_family_ipv4_peer_group["next_hop"] = {"address_family_ipv6_originate": True}

        router_bgp["address_family_ipv4"] = {
            "peer_groups": {
                peer_group_name: address_family_ipv4_peer_group,
            }
        }
        return strip_empties_from_dict(router_bgp)
