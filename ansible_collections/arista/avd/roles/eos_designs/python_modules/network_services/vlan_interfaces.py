from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.filter.convert_dicts import convert_dicts
from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdMissingVariableError
from ansible_collections.arista.avd.plugins.plugin_utils.utils import default, get

from .utils import UtilsMixin


class VlanInterfacesMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def vlan_interfaces(self) -> dict | None:
        """
        Return structured config for vlan_interfaces

        Consist of svis and mlag peering vlans from filtered tenants
        """

        if not (self._network_services_l2 and self._network_services_l3):
            return None

        vlan_interfaces = {}
        for tenant in self._filtered_tenants:
            for vrf in tenant["vrfs"]:
                for svi in vrf["svis"]:
                    vlan_id = int(svi["id"])
                    vlan_interfaces[f"Vlan{vlan_id}"] = self._get_vlan_interface_config_for_svi(svi, vrf, tenant)

                # MLAG IBGP Peering VLANs per VRF
                # Continue to next VRF if mlag vlan_id is not set
                if (vlan_id := self._mlag_ibgp_peering_vlan_vrf(vrf, tenant)) is None:
                    continue

                vlan_interfaces[f"Vlan{vlan_id}"] = self._get_vlan_interface_config_for_mlag_peering(vrf, tenant)

        if vlan_interfaces:
            return vlan_interfaces

        return None

    def _get_vlan_interface_config_for_svi(self, svi, vrf, tenant) -> dict:
        vlan_interface_config = {
            "tenant": tenant["name"],
            "tags": svi.get("tags"),
            "description": default(svi.get("description"), svi["name"]),
            "shutdown": not (svi.get("enabled", False)),
            "ip_address": svi.get("ip_address"),
            "ipv6_address": svi.get("ipv6_address"),
            "mtu": svi.get("mtu"),
            "eos_cli": svi.get("raw_eos_cli"),
            "struct_cfg": svi.get("structured_config"),
        }
        # Only set VARP if ip_address is set
        if vlan_interface_config["ip_address"] is not None:
            vlan_interface_config["ip_virtual_router_addresses"] = svi.get("ip_virtual_router_addresses")
            if vlan_interface_config["ip_virtual_router_addresses"] is not None and self._virtual_router_mac_address is None:
                raise AristaAvdMissingVariableError(
                    f"'virtual_router_mac_address' must be set for node '{self._hostname}' when using 'ip_virtual_router_addresses' under 'svi'"
                )

        # Only set Anycast GW if VARP is not set
        if vlan_interface_config.get("ip_virtual_router_addresses") is None:
            vlan_interface_config["ip_address_virtual"] = svi.get("ip_address_virtual")
            vlan_interface_config["ip_address_virtual_secondaries"] = svi.get("ip_address_virtual_secondaries")
            if (
                vlan_interface_config["ip_address_virtual"] is not None or vlan_interface_config["ip_address_virtual_secondaries"] is not None
            ) and self._virtual_router_mac_address is None:
                raise AristaAvdMissingVariableError(
                    f"'virtual_router_mac_address' must be set for node '{self._hostname}' when using 'ip_address_virtual' under 'svi'"
                )

        pim_config_ipv4 = {}
        if default(get(svi, "evpn_l3_multicast.enabled"), get(vrf, "_evpn_l3_multicast_enabled")) is True:
            if self._mlag:
                pim_config_ipv4["sparse_mode"] = True
            else:
                vlan_interface_config["ip_igmp"] = True

            if "ip_address_virtual" in vlan_interface_config:
                if (vrf_diagnostic_loopback := get(vrf, "vtep_diagnostic.loopback")) is None:
                    raise AristaAvdMissingVariableError(
                        f"No vtep_diagnostic loopback defined on VRF '{vrf['name']}' in Tenant '{tenant['name']}'."
                        "This is required when 'l3_multicast' is enabled on the VRF and ip_address_virtual is used on an SVI in that VRF."
                    )
                pim_config_ipv4["local_interface"] = f"Loopback{vrf_diagnostic_loopback}"

            if pim_config_ipv4:
                vlan_interface_config["pim"] = {"ipv4": pim_config_ipv4}

        # Only set VARPv6 if ipv6_address is set
        if vlan_interface_config["ipv6_address"] is not None:
            vlan_interface_config["ipv6_virtual_router_addresses"] = svi.get("ipv6_virtual_router_addresses")
            if vlan_interface_config["ipv6_virtual_router_addresses"] is not None and self._virtual_router_mac_address is None:
                raise AristaAvdMissingVariableError(
                    f"'virtual_router_mac_address' must be set for node '{self._hostname}' when using 'ipv6_virtual_router_addresses' under 'svi'"
                )

        # Only set Anycast v6 GW if VARPv6 is not set
        if vlan_interface_config.get("ip_virtual_router_addresses") is None:
            vlan_interface_config["ipv6_address_virtual"] = svi.get("ipv6_address_virtual")
            vlan_interface_config["ipv6_address_virtuals"] = svi.get("ipv6_address_virtuals")
            if (
                vlan_interface_config["ipv6_address_virtual"] is not None or vlan_interface_config["ipv6_address_virtuals"] is not None
            ) and self._virtual_router_mac_address is None:
                raise AristaAvdMissingVariableError(
                    f"'virtual_router_mac_address' must be set for node '{self._hostname}' when using 'ipv6_address_virtual' or 'ipv6_address_virtuals' under"
                    " 'svi'"
                )

        if vrf["name"] != "default":
            vlan_interface_config["vrf"] = vrf["name"]

        svi_ip_helpers: list[dict] = convert_dicts(default(svi.get("ip_helpers"), vrf.get("ip_helpers"), []), "ip_helper")
        if svi_ip_helpers:
            ip_helpers = {}
            for svi_ip_helper in svi_ip_helpers:
                key = svi_ip_helper["ip_helper"]
                ip_helpers[key] = {}
                if "source_interface" in svi_ip_helper:
                    ip_helpers.setdefault(key, {})["source_interface"] = svi_ip_helper["source_interface"]
                if "source_vrf" in svi_ip_helper:
                    ip_helpers.setdefault(key, {})["vrf"] = svi_ip_helper["source_vrf"]
            if ip_helpers:
                vlan_interface_config["ip_helpers"] = ip_helpers

        if get(svi, "ospf.enabled") is True and get(vrf, "ospf.enabled") is True:
            vlan_interface_config["ospf_area"] = svi["ospf"].get("area", 0)
            vlan_interface_config["ospf_network_point_to_point"] = svi["ospf"].get("point_to_point", False)
            vlan_interface_config["ospf_cost"] = svi["ospf"].get("cost")
            ospf_authentication = svi["ospf"].get("authentication")
            if ospf_authentication == "simple" and (ospf_simple_auth_key := svi["ospf"].get("simple_auth_key")) is not None:
                vlan_interface_config["ospf_authentication"] = ospf_authentication
                vlan_interface_config["ospf_authentication_key"] = ospf_simple_auth_key
            elif ospf_authentication == "message-digest" and (ospf_message_digest_keys := svi["ospf"].get("message_digest_keys")) is not None:
                ospf_keys = {}
                for ospf_key in ospf_message_digest_keys:
                    if not ("id" in ospf_key and "key" in ospf_key):
                        continue

                    ospf_keys[ospf_key["id"]] = {"hash_algorithm": ospf_key.get("hash_algorithm", "sha512"), "key": ospf_key["key"]}
                if ospf_keys:
                    vlan_interface_config["ospf_message_digest_keys"] = ospf_keys

        # Strip None values from vlan_interface_config before adding to list
        vlan_interface_config = {key: value for key, value in vlan_interface_config.items() if value is not None}

        return vlan_interface_config

    def _get_vlan_interface_config_for_mlag_peering(self, vrf, tenant) -> dict:
        vlan_interface_config = {
            "tenant": tenant["name"],
            "type": "underlay_peering",
            "shutdown": False,
            "description": f"MLAG_PEER_L3_iBGP: vrf {vrf['name']}",
            "vrf": vrf["name"],
            "mtu": self._p2p_uplinks_mtu,
        }
        if self._underlay_rfc5549 and self._overlay_mlag_rfc5549:
            vlan_interface_config["ipv6_enable"] = True
        elif (mlag_ibgp_peering_ipv4_pool := vrf.get("mlag_ibgp_peering_ipv4_pool")) is not None:
            if self._mlag_role == "primary":
                vlan_interface_config["ip_address"] = f"{self._avd_ip_addressing.mlag_ibgp_peering_ip_primary(mlag_ibgp_peering_ipv4_pool)}/31"
            else:
                vlan_interface_config["ip_address"] = f"{self._avd_ip_addressing.mlag_ibgp_peering_ip_secondary(mlag_ibgp_peering_ipv4_pool)}/31"
        else:
            vlan_interface_config["ip_address"] = f"{self._mlag_ibgp_ip}/31"

        return vlan_interface_config
