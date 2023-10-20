# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.filter.convert_dicts import convert_dicts
from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdMissingVariableError
from ansible_collections.arista.avd.plugins.plugin_utils.utils import append_if_not_duplicate, default, get

from .utils import UtilsMixin


class VlanInterfacesMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def vlan_interfaces(self) -> list | None:
        """
        Return structured config for vlan_interfaces

        Consist of svis and mlag peering vlans from filtered tenants
        """

        if not (self.shared_utils.network_services_l2 and self.shared_utils.network_services_l3):
            return None

        vlan_interfaces = []
        for tenant in self._filtered_tenants:
            for vrf in tenant["vrfs"]:
                for svi in vrf["svis"]:
                    vlan_interface = self._get_vlan_interface_config_for_svi(svi, vrf)
                    append_if_not_duplicate(
                        list_of_dicts=vlan_interfaces,
                        primary_key="name",
                        new_dict=vlan_interface,
                        context="VLAN Interfaces",
                        context_keys=["name", "tenant"],
                        ignore_keys={"tenant"},
                    )

                # MLAG IBGP Peering VLANs per VRF
                # Continue to next VRF if mlag vlan_id is not set
                if (vlan_id := self._mlag_ibgp_peering_vlan_vrf(vrf, tenant)) is None:
                    continue

                vlan_interface = {"name": f"Vlan{vlan_id}", **self._get_vlan_interface_config_for_mlag_peering(vrf)}
                append_if_not_duplicate(
                    list_of_dicts=vlan_interfaces,
                    primary_key="name",
                    new_dict=vlan_interface,
                    context="MLAG iBGP Peering VLAN Interfaces",
                    context_keys=["name", "tenant"],
                    ignore_keys={"tenant"},
                )

        if vlan_interfaces:
            return vlan_interfaces

        return None

    def _get_vlan_interface_config_for_svi(self, svi, vrf) -> dict:
        def _check_virtual_router_mac_address(vlan_interface_config: dict, variables: list):
            """
            Check if any variable in the list of variables is not None in vlan_interface_config
            and if it is the case, raise an Exception if virtual_router_mac_address is None
            """
            if any(vlan_interface_config.get(var) for var in variables) and self.shared_utils.virtual_router_mac_address is None:
                quoted_vars = [f"'{var}'" for var in variables]
                raise AristaAvdMissingVariableError(
                    f"'virtual_router_mac_address' must be set for node '{self.shared_utils.hostname}' when using {' or '.join(quoted_vars)} under 'svi'"
                )

        vlan_interface_config = {
            "name": f"Vlan{int(svi['id'])}",
            "tenant": svi["tenant"],
            "tags": svi.get("tags"),
            "description": default(svi.get("description"), svi["name"]),
            "shutdown": not (svi.get("enabled", False)),
            "ip_address": svi.get("ip_address"),
            "ipv6_address": svi.get("ipv6_address"),
            "ipv6_enable": svi.get("ipv6_enable"),
            "mtu": svi.get("mtu") if self.shared_utils.platform_settings_feature_support_per_interface_mtu else None,
            "eos_cli": svi.get("raw_eos_cli"),
            "struct_cfg": svi.get("structured_config"),
        }
        # Only set VARP if ip_address is set
        if vlan_interface_config["ip_address"] is not None:
            vlan_interface_config["ip_virtual_router_addresses"] = svi.get("ip_virtual_router_addresses")
            _check_virtual_router_mac_address(vlan_interface_config, ["ip_virtual_router_addresses"])

        # Only set Anycast GW if VARP is not set
        if vlan_interface_config.get("ip_virtual_router_addresses") is None:
            vlan_interface_config["ip_address_virtual"] = svi.get("ip_address_virtual")
            vlan_interface_config["ip_address_virtual_secondaries"] = svi.get("ip_address_virtual_secondaries")
            _check_virtual_router_mac_address(vlan_interface_config, ["ip_address_virtual", "ip_address_virtual_secondaries"])

        pim_config_ipv4 = {}
        if default(get(svi, "evpn_l3_multicast.enabled"), get(vrf, "_evpn_l3_multicast_enabled")) is True:
            if self.shared_utils.mlag:
                pim_config_ipv4["sparse_mode"] = True
            else:
                vlan_interface_config["ip_igmp"] = True

            if "ip_address_virtual" in vlan_interface_config:
                if (vrf_diagnostic_loopback := get(vrf, "vtep_diagnostic.loopback")) is None:
                    raise AristaAvdMissingVariableError(
                        f"No vtep_diagnostic loopback defined on VRF '{vrf['name']}' in Tenant '{svi['tenant']}'."
                        "This is required when 'l3_multicast' is enabled on the VRF and ip_address_virtual is used on an SVI in that VRF."
                    )
                pim_config_ipv4["local_interface"] = f"Loopback{vrf_diagnostic_loopback}"

            if pim_config_ipv4:
                vlan_interface_config["pim"] = {"ipv4": pim_config_ipv4}

        # Only set VARPv6 if ipv6_address is set
        if vlan_interface_config["ipv6_address"] is not None:
            vlan_interface_config["ipv6_virtual_router_addresses"] = svi.get("ipv6_virtual_router_addresses")
            _check_virtual_router_mac_address(vlan_interface_config, ["ipv6_virtual_router_addresses"])

        # Only set Anycast v6 GW if VARPv6 is not set
        if vlan_interface_config.get("ip_virtual_router_addresses") is None:
            if (ipv6_address_virtual := svi.get("ipv6_address_virtual")) is not None:
                # The singular ipv6_address_virtual is deprecated from eos_cli_config_gen. So set as list item into the new key.
                vlan_interface_config["ipv6_address_virtuals"] = [ipv6_address_virtual]

            if (ipv6_address_virtuals := svi.get("ipv6_address_virtuals")) is not None:
                vlan_interface_config.setdefault("ipv6_address_virtuals", []).extend(ipv6_address_virtuals)

            _check_virtual_router_mac_address(vlan_interface_config, ["ipv6_address_virtuals"])

            if vlan_interface_config.get("ipv6_address_virtuals"):
                # If any anycast IPs are set, we also enable link-local IPv6 per best practice, unless specifically disabled with 'ipv6_enable: false'
                vlan_interface_config["ipv6_enable"] = default(vlan_interface_config["ipv6_enable"], True)

        if vrf["name"] != "default":
            vlan_interface_config["vrf"] = vrf["name"]

        svi_ip_helpers: list[dict] = convert_dicts(default(svi.get("ip_helpers"), vrf.get("ip_helpers"), []), "ip_helper")
        if svi_ip_helpers:
            ip_helpers = []
            for svi_ip_helper in svi_ip_helpers:
                ip_helper = {"ip_helper": svi_ip_helper["ip_helper"]}
                if "source_interface" in svi_ip_helper:
                    ip_helper["source_interface"] = svi_ip_helper["source_interface"]
                if "source_vrf" in svi_ip_helper:
                    ip_helper["vrf"] = svi_ip_helper["source_vrf"]
                ip_helpers.append(ip_helper)
            if ip_helpers:
                vlan_interface_config["ip_helpers"] = ip_helpers

        if get(svi, "ospf.enabled") is True and get(vrf, "ospf.enabled") is True:
            vlan_interface_config["ospf_area"] = svi["ospf"].get("area", "0")
            vlan_interface_config["ospf_network_point_to_point"] = svi["ospf"].get("point_to_point", False)
            vlan_interface_config["ospf_cost"] = svi["ospf"].get("cost")
            ospf_authentication = svi["ospf"].get("authentication")
            if ospf_authentication == "simple" and (ospf_simple_auth_key := svi["ospf"].get("simple_auth_key")) is not None:
                vlan_interface_config["ospf_authentication"] = ospf_authentication
                vlan_interface_config["ospf_authentication_key"] = ospf_simple_auth_key
            elif ospf_authentication == "message-digest" and (ospf_message_digest_keys := svi["ospf"].get("message_digest_keys")) is not None:
                ospf_keys = []
                for ospf_key in ospf_message_digest_keys:
                    if not ("id" in ospf_key and "key" in ospf_key):
                        continue

                    ospf_keys.append({"id": ospf_key["id"], "hash_algorithm": ospf_key.get("hash_algorithm", "sha512"), "key": ospf_key["key"]})
                if ospf_keys:
                    vlan_interface_config["ospf_authentication"] = ospf_authentication
                    vlan_interface_config["ospf_message_digest_keys"] = ospf_keys

        # Strip None values from vlan_interface_config before adding to list
        vlan_interface_config = {key: value for key, value in vlan_interface_config.items() if value is not None}

        return vlan_interface_config

    def _get_vlan_interface_config_for_mlag_peering(self, vrf) -> dict:
        """
        Build config for MLAG peering SVI for the given SVI.
        Called from vlan_interfaces and prefix_lists
        """
        vlan_interface_config = {
            "tenant": vrf["tenant"],
            "type": "underlay_peering",
            "shutdown": False,
            "description": f"MLAG_PEER_L3_iBGP: vrf {vrf['name']}",
            "vrf": vrf["name"],
            "mtu": self.shared_utils.p2p_uplinks_mtu,
        }
        if self.shared_utils.underlay_rfc5549 and self.shared_utils.overlay_mlag_rfc5549:
            vlan_interface_config["ipv6_enable"] = True
        elif (mlag_ibgp_peering_ipv4_pool := vrf.get("mlag_ibgp_peering_ipv4_pool")) is not None:
            if self.shared_utils.mlag_role == "primary":
                vlan_interface_config["ip_address"] = f"{self.shared_utils.ip_addressing.mlag_ibgp_peering_ip_primary(mlag_ibgp_peering_ipv4_pool)}/31"
            else:
                vlan_interface_config["ip_address"] = f"{self.shared_utils.ip_addressing.mlag_ibgp_peering_ip_secondary(mlag_ibgp_peering_ipv4_pool)}/31"
        else:
            vlan_interface_config["ip_address"] = f"{self.shared_utils.mlag_ibgp_ip}/31"

        return vlan_interface_config
