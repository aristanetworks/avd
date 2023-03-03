from __future__ import annotations

import ipaddress
from functools import cached_property

from ansible_collections.arista.avd.plugins.filter.natural_sort import natural_sort
from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdMissingVariableError
from ansible_collections.arista.avd.plugins.plugin_utils.utils import default, get, get_item
from ansible_collections.arista.avd.roles.eos_designs.python_modules.interface_descriptions import AvdInterfaceDescriptions
from ansible_collections.arista.avd.roles.eos_designs.python_modules.ip_addressing import AvdIpAddressing

from .utils_filtered_tenants import UtilsFilteredTenantsMixin


class UtilsMixin(UtilsFilteredTenantsMixin):
    """
    Mixin Class with internal functions.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    # Set type hints for Attributes of the main class as needed
    _hostvars: dict
    _avd_ip_addressing: AvdIpAddressing
    _avd_interface_descriptions: AvdInterfaceDescriptions

    @cached_property
    def _any_network_services(self) -> bool:
        return self._network_services_l2 or self._network_services_l3 or self._network_services_l1

    @cached_property
    def _network_services_l1(self) -> bool:
        return get(self._hostvars, "switch.network_services_l1", required=True) is True

    @cached_property
    def _network_services_l2(self) -> bool:
        return get(self._hostvars, "switch.network_services_l2", required=True) is True

    @cached_property
    def _network_services_l3(self) -> bool:
        return get(self._hostvars, "switch.network_services_l3", required=True) is True

    @cached_property
    def _hostname(self) -> str:
        return get(self._hostvars, "switch.hostname", required=True)

    @cached_property
    def _network_services_keys(self) -> list[dict]:
        """
        Return sorted network_services_keys filtered for invalid entries and unused keys
        """
        network_services_keys = get(self._hostvars, "network_services_keys", required=True)
        network_services_keys = [entry for entry in network_services_keys if "name" in entry and entry["name"] in self._hostvars]
        return natural_sort(network_services_keys, "name")

    @cached_property
    def _mlag(self) -> bool:
        return get(self._hostvars, "switch.mlag") is True

    @cached_property
    def _mlag_l3(self) -> bool:
        return get(self._hostvars, "switch.mlag_l3") is True

    @cached_property
    def _trunk_groups_mlag_name(self) -> str:
        return get(self._hostvars, "switch.trunk_groups.mlag.name", required=True)

    @cached_property
    def _trunk_groups_mlag_l3_name(self) -> str:
        return get(self._hostvars, "switch.trunk_groups.mlag_l3.name", required=True)

    @cached_property
    def _uplink_type(self) -> str:
        return get(self._hostvars, "switch.uplink_type", required=True)

    @cached_property
    def _trunk_groups_uplink_name(self) -> str:
        return get(self._hostvars, "switch.trunk_groups.uplink.name", required=True)

    @cached_property
    def _endpoint_trunk_groups(self) -> set:
        return set(get(self._hostvars, "switch.endpoint_trunk_groups", default=[]))

    @cached_property
    def _only_local_vlan_trunk_groups(self) -> bool:
        return get(self._hostvars, "switch.only_local_vlan_trunk_groups") is True

    @cached_property
    def _enable_trunk_groups(self) -> bool:
        return get(self._hostvars, "switch.enable_trunk_groups") is True

    @cached_property
    def _underlay_rfc5549(self) -> bool:
        return get(self._hostvars, "underlay_rfc5549") is True

    @cached_property
    def _overlay_mlag_rfc5549(self) -> bool:
        return get(self._hostvars, "overlay_mlag_rfc5549") is True

    @cached_property
    def _mlag_role(self) -> str:
        return get(self._hostvars, "switch.mlag_role", required=True)

    @cached_property
    def _mlag_ibgp_ip(self) -> str:
        if (mlag_ip := get(self._hostvars, "switch.mlag_l3_ip")) is not None:
            return mlag_ip

        return get(self._hostvars, "switch.mlag_ip", required=True)

    @cached_property
    def _mlag_peer_ibgp_ip(self) -> str:
        if (mlag_peer_ip := get(self._hostvars, "switch.mlag_peer_l3_ip")) is not None:
            return mlag_peer_ip

        return get(self._hostvars, "switch.mlag_peer_ip", required=True)

    @cached_property
    def _p2p_uplinks_mtu(self) -> int:
        return int(get(self._hostvars, "p2p_uplinks_mtu", required=True))

    @cached_property
    def _mlag_ibgp_peering_vrfs_base_vlan(self) -> int:
        return int(get(self._hostvars, "mlag_ibgp_peering_vrfs.base_vlan", required=True))

    @cached_property
    def _router_id(self) -> str | None:
        return get(self._hostvars, "switch.router_id")

    @cached_property
    def _overlay_evpn(self) -> bool:
        return get(self._hostvars, "switch.overlay.evpn", required=True) is True

    @cached_property
    def _overlay_vtep(self) -> bool:
        return get(self._hostvars, "switch.overlay.vtep", required=True) is True

    @cached_property
    def _overlay_ler(self) -> bool:
        return get(self._hostvars, "switch.overlay.ler") is True

    @cached_property
    def _overlay_evpn_mpls(self) -> bool:
        return get(self._hostvars, "switch.overlay.evpn_mpls") is True

    @cached_property
    def _bgp_as(self) -> str | None:
        return get(self._hostvars, "switch.bgp_as")

    @cached_property
    def _pod_name(self) -> str | None:
        return get(self._hostvars, "pod_name")

    @cached_property
    def _id(self) -> int:
        return int(get(self._hostvars, "switch.id", required=True))

    @cached_property
    def _loopback_ipv4_offset(self) -> int:
        return int(get(self._hostvars, "switch.loopback_ipv4_offset", required=True))

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

        if self._overlay_evpn and self._overlay_vtep:
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

    @cached_property
    def _evpn_short_esi_prefix(self) -> str:
        return get(self._hostvars, "evpn_short_esi_prefix", required=True)

    @cached_property
    def _underlay_routing_protocol(self) -> str | None:
        return get(self._hostvars, "switch.underlay_routing_protocol")

    @cached_property
    def _underlay_bgp(self) -> bool:
        return get(self._hostvars, "switch.underlay.bgp") is True

    @cached_property
    def _overlay_routing_protocol(self) -> str | None:
        return get(self._hostvars, "switch.overlay_routing_protocol")

    @cached_property
    def _underlay_ospf_process_id(self) -> int:
        return get(self._hostvars, "underlay_ospf_process_id", required=True)

    @cached_property
    def _overlay_address_families(self) -> set[str]:
        return set(get(self._hostvars, "switch.overlay_address_families", default=["evpn"]))

    @cached_property
    def _overlay_rd_type_admin_subfield(self) -> str:
        return get(self._hostvars, "switch.overlay_rd_type_admin_subfield", required=True)

    @cached_property
    def _peer_group_mlag_ipv4_underlay_peer_name(self) -> str:
        return get(self._hostvars, "switch.bgp_peer_groups.mlag_ipv4_underlay_peer.name", required=True)

    @cached_property
    def _peer_group_ipv4_underlay_peers_name(self) -> str:
        return get(self._hostvars, "switch.bgp_peer_groups.ipv4_underlay_peers.name", required=True)

    @cached_property
    def _mlag_peer(self) -> str:
        return get(self._hostvars, "switch.mlag_peer", required=True)

    def _mlag_ibgp_peering_vlan_vrf(self, vrf, tenant) -> int | None:
        """
        MLAG IBGP Peering VLANs per VRF

        Performs all relevant checks if MLAG IBGP Peering is enabled
        Returns None if peering is not enabled
        """

        if not (self._mlag_l3 and self._network_services_l3):
            return None

        mlag_ibgp_peering = default(vrf.get("enable_mlag_ibgp_peering_vrfs"), tenant.get("enable_mlag_ibgp_peering_vrfs"), True)
        if vrf["name"] == "default" or not mlag_ibgp_peering:
            return None

        if (mlag_ibgp_peering_vlan := get(vrf, "mlag_ibgp_peering_vlan")) is not None:
            vlan_id = mlag_ibgp_peering_vlan
        else:
            base_vlan = self._mlag_ibgp_peering_vrfs_base_vlan
            vrf_id = vrf.get("vrf_id", vrf.get("vrf_vni"))
            if vrf_id is None:
                raise AristaAvdMissingVariableError(
                    f"Unable to assign MLAG VRF Peering VLAN for vrf {vrf['name']}.Set either 'mlag_ibgp_peering_vlan' or 'vrf_id' or 'vrf_vni' on the VRF"
                )
            vlan_id = base_vlan + int(vrf_id) - 1

        return vlan_id

    @cached_property
    def _mpls_overlay_role(self) -> str | None:
        return get(self._hostvars, "switch.mpls_overlay_role")

    @cached_property
    def _mlag_ibgp_origin_incomplete(self) -> bool | None:
        return get(self._hostvars, "switch.mlag_ibgp_origin_incomplete")

    @cached_property
    def _configure_bgp_mlag_peer_group(self) -> bool:
        """
        Flag set during creating of BGP VRFs if an MLAG peering is needed.
        Decides if MLAG BGP peer-group should be configured.
        Catches cases where underlay is not BGP but we still need MLAG iBGP peering
        """
        if self._underlay_bgp or (bgp_vrfs := self._router_bgp_vrfs) is None:
            return False

        for bgp_vrf in bgp_vrfs.values():
            if "neighbors" not in bgp_vrf:
                continue
            for neighbor_settings in bgp_vrf["neighbors"].values():
                if neighbor_settings.get("peer_group") == self._peer_group_mlag_ipv4_underlay_peer_name:
                    return True

        return False

    @cached_property
    def _evpn_multicast(self) -> bool:
        return get(self._hostvars, "switch.evpn_multicast") is True

    @cached_property
    def _virtual_router_mac_address(self) -> str | None:
        return get(self._hostvars, "switch.virtual_router_mac_address")
