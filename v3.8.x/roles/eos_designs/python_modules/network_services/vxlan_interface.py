from __future__ import annotations

from functools import cached_property
from typing import NoReturn

from ansible_collections.arista.avd.plugins.filter.natural_sort import natural_sort
from ansible_collections.arista.avd.plugins.filter.range_expand import range_expand
from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError
from ansible_collections.arista.avd.plugins.plugin_utils.utils import default, get, unique
from ansible_collections.arista.avd.roles.eos_designs.python_modules.ip_addressing import AvdIpAddressing

from .utils import UtilsMixin


class VxlanInterfaceMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    # Set type hints for Attributes of the main class as needed
    _hostvars: dict
    _filtered_tenants: list[dict]
    _avd_ip_addressing: AvdIpAddressing

    @cached_property
    def vxlan_interface(self) -> dict | None:
        """
        Returns structured config for vxlan_interface

        Only used for VTEPs

        This function also detects duplicate VNIs and raise an error in case of duplicates between
        all Network Services deployed on this device.
        """
        if not self._overlay_vtep:
            return None

        vxlan = {
            "udp_port": 4789,
        }
        vtep_loopback = get(self._hostvars, "switch.vtep_loopback", required=True)
        if get(self._hostvars, "switch.multi_vtep") is True:
            vxlan["source_interface"] = "Loopback0"
            vxlan["mlag_source_interface"] = vtep_loopback
        else:
            vxlan["source_interface"] = vtep_loopback

        if self._mlag_l3 and self._network_services_l3 and self._overlay_evpn:
            vxlan["virtual_router_encapsulation_mac_address"] = "mlag-system-id"

        if self._overlay_routing_protocol == "her" and self._overlay_her_flood_list_per_vni is False:
            vxlan["flood_vteps"] = natural_sort(unique(self._overlay_her_flood_lists.get("common", [])))

        vlans = {}
        vrfs = {}
        # vnis is a dict of {<vni>: <tenant>}. Only used to detect duplicates.
        vnis = {}
        for tenant in self._filtered_tenants:
            for vrf in tenant["vrfs"]:
                for svi in vrf["svis"]:
                    if vlan := self._get_vxlan_interface_config_for_vlan(svi, tenant):
                        vlan_id = int(svi["id"])
                        if (vni := vlan["vni"]) in vnis:
                            self._raise_duplicate_vni_error(vni, f"SVI '{vlan_id} in vrf '{vrf['name']}'", tenant["name"], vnis[vni])

                        vnis[vni] = tenant["name"]
                        vlans[vlan_id] = vlan

                if self._network_services_l3 and self._overlay_evpn:
                    vrf_name = vrf["name"]
                    vni = default(
                        vrf.get("vrf_vni"),
                        vrf.get("vrf_id"),
                    )
                    if vni is not None:
                        # Silently ignore if we cannot set a VNI
                        # This is legacy behavior so we will leave stricter enforcement to the schema
                        if vni in vnis:
                            self._raise_duplicate_vni_error(vni, f"VRF '{vrf_name}'", tenant["name"], vnis[vni])

                        vnis[vni] = tenant["name"]
                        vrfs[vrf_name] = {"vni": vni}

                        if get(vrf, "_evpn_l3_multicast_enabled"):
                            underlay_l3_multicast_group_ipv4_pool = get(
                                tenant,
                                "evpn_l3_multicast.evpn_underlay_l3_multicast_group_ipv4_pool",
                                required=True,
                                org_key=f"'evpn_l3_multicast.evpn_underlay_l3_multicast_group_ipv4_pool' for Tenant: {tenant['name']}",
                            )
                            underlay_l3_mcast_group_ipv4_pool_offset = get(
                                tenant, "evpn_l3_multicast.evpn_underlay_l3_multicast_group_ipv4_pool_offset", default=0
                            )
                            offset = vni - 1 + underlay_l3_mcast_group_ipv4_pool_offset
                            vrfs[vrf_name]["multicast_group"] = self._avd_ip_addressing._ip(underlay_l3_multicast_group_ipv4_pool, 32, offset, 0)

            for l2vlan in tenant["l2vlans"]:
                if vlan := self._get_vxlan_interface_config_for_vlan(l2vlan, tenant):
                    vlan_id = int(l2vlan["id"])
                    if (vni := vlan["vni"]) in vnis:
                        self._raise_duplicate_vni_error(vni, f"L2VLAN '{vlan_id}'", tenant["name"], vnis[vni])

                    vnis[vni] = tenant["name"]
                    vlans[vlan_id] = vlan

        if vlans:
            vxlan["vlans"] = vlans

        if vrfs:
            vxlan["vrfs"] = vrfs

        return {
            "Vxlan1": {
                "description": f"{self._hostname}_VTEP",
                "vxlan": vxlan,
            }
        }

    def _get_vxlan_interface_config_for_vlan(self, vlan, tenant) -> dict:
        """
        vxlan_interface logic for one vlan

        Can be used for both svis and l2vlans
        """

        if vlan.get("vxlan") is False:
            return {}

        vxlan_interface_vlan = {}
        vlan_id = int(vlan["id"])
        if (vni_override := vlan.get("vni_override")) is not None:
            vxlan_interface_vlan["vni"] = int(vni_override)
        else:
            mac_vrf_vni_base = int(get(tenant, "mac_vrf_vni_base", required=True, org_key=f"'mac_vrf_vni_base' for Tenant: {tenant['name']}"))
            vxlan_interface_vlan["vni"] = mac_vrf_vni_base + vlan_id

        vlan_evpn_l2_multicast_enabled = default(get(vlan, "evpn_l2_multicast.enabled"), get(tenant, "evpn_l2_multicast.enabled"))
        if vlan_evpn_l2_multicast_enabled is True:
            underlay_l2_multicast_group_ipv4_pool = get(
                tenant,
                "evpn_l2_multicast.underlay_l2_multicast_group_ipv4_pool",
                required=True,
                org_key=f"'evpn_l2_multicast.underlay_l2_multicast_group_ipv4_pool' for Tenant: {tenant['name']}",
            )
            underlay_l2_multicast_group_ipv4_pool_offset = get(tenant, "evpn_l2_multicast.underlay_l2_multicast_group_ipv4_pool_offset", default=0)
            offset = vlan_id - 1 + underlay_l2_multicast_group_ipv4_pool_offset
            vxlan_interface_vlan["multicast_group"] = self._avd_ip_addressing._ip(underlay_l2_multicast_group_ipv4_pool, 32, offset, 0)

        if self._overlay_routing_protocol == "her" and self._overlay_her_flood_list_per_vni:
            vxlan_interface_vlan["flood_vteps"] = natural_sort(unique(self._overlay_her_flood_lists.get(vlan_id, [])))

        return vxlan_interface_vlan

    @cached_property
    def _overlay_her_flood_list_per_vni(self) -> bool:
        return get(self._hostvars, "overlay_her_flood_list_per_vni") is True

    @cached_property
    def _overlay_her_flood_lists(self) -> dict[list]:
        """
        Returns a dict with HER Flood Lists.

        Only used when overlay_route_protocol == 'HER'

        If "overlay_her_flood_list_per_vni" is True:
        - return {<vlan>: [<peer_vtep>, <peer_vtep>, ...], ...}
        Else
        - return {common: [<peer_vtep>, <peer_vtep> ...]}

        Uses "overlay_her_flood_list_scope" to find the peer switches
        If overlay_her_flood_list_scope == "dc"
          - dc_name *must* be set.
          - Otherwise an error will be raised
        """
        overlay_her_flood_lists = {}
        overlay_her_flood_list_scope = get(self._hostvars, "overlay_her_flood_list_scope")
        if overlay_her_flood_list_scope == "dc":
            scope = get(self._hostvars, "dc_name", required=True, org_key="With 'overlay_her_flood_list_scope: dc', 'dc_name'")
        else:
            scope = get(self._hostvars, "fabric_name", required=True)

        peers = get(self._hostvars, f"groups..{scope}", separator="..", required=True)
        avd_switch_facts = get(self._hostvars, "avd_switch_facts", required=True)
        for peer in peers:
            if peer == self._hostname:
                continue
            if (vtep_ip := get(avd_switch_facts, f"{peer}..switch..vtep_ip", separator="..")) is None:
                continue
            if not self._overlay_her_flood_list_per_vni:
                # Use common flood list
                overlay_her_flood_lists.setdefault("common", []).append(vtep_ip)
                continue

            # Use flood lists per vlan
            peer_vlans = get(avd_switch_facts, f"{peer}..switch..vlans", separator="..", default=[])
            peer_vlans_list = range_expand(peer_vlans)
            for vlan in peer_vlans_list:
                overlay_her_flood_lists.setdefault(int(vlan), []).append(vtep_ip)

        return overlay_her_flood_lists

    def _raise_duplicate_vni_error(self, vni: int, context: str, tenant_name: str, duplicate_vni_tenant: str) -> NoReturn:
        msg = f"Duplicate VXLAN VNI '{vni}' found in Tenant '{tenant_name}' during configuration of {context}."
        if duplicate_vni_tenant != tenant_name:
            msg = f"{msg} Other VNI is in Tenant '{duplicate_vni_tenant}'."

        raise AristaAvdError(msg)
