# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.filter.convert_dicts import convert_dicts
from ansible_collections.arista.avd.plugins.filter.natural_sort import natural_sort
from ansible_collections.arista.avd.plugins.filter.range_expand import range_expand
from ansible_collections.arista.avd.plugins.plugin_utils.eos_designs_shared_utils.shared_utils import SharedUtils
from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError
from ansible_collections.arista.avd.plugins.plugin_utils.strip_empties import strip_empties_from_dict
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
    def _avd_peers(self) -> list:
        """
        Returns a list of peers

        This cannot be loaded in shared_utils since it will not be calculated until EosDesignsFacts has been rendered
        and shared_utils are shared between EosDesignsFacts and AvdStructuredConfig classes like this one.
        """
        return natural_sort(get(self._hostvars, f"avd_topology_peers..{self.shared_utils.hostname}", separator="..", default=[]))

    @cached_property
    def _underlay_filter_peer_as_route_maps_asns(self) -> list:
        """
        Filtered ASNs
        """
        if self.shared_utils.underlay_filter_peer_as is False:
            return []

        # using set comprehension with `{}` to remove duplicates and then run natural_sort to convert to list.
        return natural_sort({link["peer_bgp_as"] for link in self._underlay_links if link["type"] == "underlay_p2p"})

    @cached_property
    def _underlay_links(self) -> list:
        """
        Returns the list of underlay links for this device
        """
        underlay_links = []
        underlay_links.extend(self._uplinks)
        if self.shared_utils.fabric_sflow_uplinks is not None:
            for uplink in underlay_links:
                uplink.update({"sflow": {"enable": self.shared_utils.fabric_sflow_uplinks}})

        for peer in self._avd_peers:
            peer_facts = self.shared_utils.get_peer_facts(peer, required=True)
            for uplink in peer_facts["uplinks"]:
                if uplink["peer"] == self.shared_utils.hostname:
                    link = {
                        "interface": uplink["peer_interface"],
                        "peer": peer,
                        "peer_interface": uplink["interface"],
                        "peer_type": get(peer_facts, "type"),
                        "peer_is_deployed": peer_facts["is_deployed"],
                        "peer_bgp_as": get(peer_facts, "bgp_as"),
                        "type": get(uplink, "type", required=True),
                        "speed": get(uplink, "peer_speed", default=get(uplink, "speed")),
                        "ip_address": get(uplink, "peer_ip_address"),
                        "peer_ip_address": get(uplink, "ip_address"),
                        "prefix_length": get(uplink, "prefix_length"),
                        "channel_group_id": get(uplink, "peer_channel_group_id"),
                        "peer_channel_group_id": get(uplink, "channel_group_id"),
                        "channel_description": get(uplink, "peer_channel_description"),
                        "vlans": get(uplink, "vlans"),
                        "native_vlan": get(uplink, "native_vlan"),
                        "trunk_groups": get(uplink, "peer_trunk_groups"),
                        "bfd": get(uplink, "bfd"),
                        "ptp": get(uplink, "ptp"),
                        "mac_security": get(uplink, "mac_security"),
                        "short_esi": get(uplink, "peer_short_esi"),
                        "mlag": get(uplink, "peer_mlag"),
                        "underlay_multicast": get(uplink, "underlay_multicast"),
                        "ipv6_enable": get(uplink, "ipv6_enable"),
                        "sflow": {"enable": self.shared_utils.fabric_sflow_downlinks},
                        "spanning_tree_portfast": get(uplink, "peer_spanning_tree_portfast"),
                        "structured_config": get(uplink, "structured_config"),
                    }
                    if (subinterfaces := get(uplink, "subinterfaces")) is not None:
                        link["subinterfaces"] = [
                            {
                                **subinterface,
                                "interface": subinterface["peer_interface"],
                                "peer_interface": subinterface["interface"],
                                "ip_address": subinterface.get("peer_ip_address"),
                                "peer_ip_address": subinterface.get("ip_address"),
                            }
                            for subinterface in subinterfaces
                        ]
                    underlay_links.append(strip_empties_from_dict(link))

        return natural_sort(underlay_links, "interface")

    @cached_property
    def _underlay_vlan_trunk_groups(self) -> list:
        """
        Returns a list of trunk groups to configure on the underlay link
        """
        if self.shared_utils.enable_trunk_groups is not True:
            return []

        trunk_groups = []

        for peer in self._avd_peers:
            peer_facts = self.shared_utils.get_peer_facts(peer, required=True)
            for uplink in peer_facts["uplinks"]:
                if uplink["peer"] == self.shared_utils.hostname:
                    if (peer_trunk_groups := get(uplink, "peer_trunk_groups")) is None:
                        continue

                    trunk_groups.append(
                        {
                            "vlan_list": uplink["vlans"],
                            "trunk_groups": peer_trunk_groups,
                        }
                    )

        if trunk_groups:
            return trunk_groups

        return []

    @cached_property
    def _uplinks(self) -> list:
        return get(self._hostvars, "switch.uplinks")

    def _get_l3_interface_cfg(self, l3_interface: dict) -> dict | None:
        """
        Returns structured_configuration for one L3 interface
        """
        interface_name = get(l3_interface, "name", required=True, org_key=f"<node_type_key>...[node={self.shared_utils.hostname}].l3_interfaces[].name]")
        if "." in interface_name:
            iface_type = "l3dot1q"
            encapsulation = int(get(l3_interface, "encapsulation_dot1q_vlan", default=interface_name.split(".")[-1]))
        else:
            iface_type = "routed"

        # TODO move this to description module?
        interface_description = (
            l3_interface.get("description")
            or "_".join([elem for elem in [l3_interface.get("peer"), l3_interface.get("peer_interface")] if elem is not None])
            or None
        )

        # TODO catch if ip_address is not valid or not dhcp
        ip_address = get(
            l3_interface,
            "ip_address",
            required=True,
            org_key=f"{self.shared_utils.node_type_key_data['key']}.nodes[name={self.shared_utils.hostname}].l3_interfaces[name={interface_name}].ip_address",
        )

        interface = {
            "name": interface_name,
            "peer_type": "l3_interface",
            "peer": l3_interface.get("peer"),
            "peer_interface": l3_interface.get("peer_interface"),
            "ip_address": ip_address,
            "shutdown": not l3_interface.get("enabled", True),
            "type": iface_type,
            "description": interface_description,
            "speed": l3_interface.get("speed"),
            "service_profile": l3_interface.get("qos_profile"),
            "eos_cli": l3_interface.get("raw_eos_cli"),
            "struct_cfg": l3_interface.get("structured_config"),
        }

        if iface_type == "l3dot1q":
            interface["encapsulation_dot1q_vlan"] = encapsulation

        if ip_address == "dhcp" and l3_interface.get("set_default_route", False):
            interface["dhcp_client_accept_default_route"] = True

        if self.shared_utils.cv_pathfinder_role:
            interface["flow_tracker"] = {"hardware": "WAN-FLOW-TRACKER"}

        return strip_empties_from_dict(interface)

    def _get_l3_uplink_with_l2_as_subint(self, link: dict) -> (dict, list[dict]):
        """
        Return a tuple with main uplink interface, list of subinterfaces representing each SVI.
        """
        vlans = [int(vlan) for vlan in range_expand(link["vlans"])]

        # Main interface
        # Routed interface with no config unless there is an SVI matching the native-vlan, then it will contain the config for that SVI

        interfaces = []
        for tenant in self.shared_utils.filtered_tenants:
            for vrf in tenant["vrfs"]:
                for svi in vrf["svis"]:
                    svi_id = int(svi["id"])
                    # Skip any vlans not part of the link
                    if svi_id not in vlans:
                        continue

                    interfaces.append(self._get_l2_as_subint(link, svi, vrf))

        # If we have the main interface covered, we can just exclude it from the list and return as main interface.
        # Otherwise we return an almost empty dict as the main interface since it was already covered by the calling function.
        main_interface = get_item(interfaces, "name", link["interface"], default={"type": "routed", "mtu": self.shared_utils.p2p_uplinks_mtu})
        main_interface.pop("description", None)

        if (mtu := main_interface.get("mtu", 1500)) != self.shared_utils.p2p_uplinks_mtu:
            raise AristaAvdError(
                f"MTU '{self.shared_utils.p2p_uplinks_mtu}' set for 'p2p_uplinks_mtu' conflicts with MTU '{mtu}' "
                f"set on SVI for uplink_native_vlan '{link['native_vlan']}'."
                "Either adjust the MTU on the SVI or p2p_uplinks_mtu or change/remove the uplink_native_vlan setting."
            )
        return main_interface, [interface for interface in interfaces if interface["name"] != link["interface"]]

    def _get_l2_as_subint(self, link: dict, svi: dict, vrf: dict) -> dict:
        """
        Return structured config for one subinterface representing the given SVI.
        Only supports static IPs or VRRP.
        """
        svi_id = int(svi["id"])
        is_native = svi_id == link.get("native_vlan")
        interface_name = link["interface"] if is_native else f"{link['interface']}.{svi_id}"
        subinterface = {
            "name": interface_name,
            "peer": link["peer"],
            "peer_interface": f"{link['peer_interface']} VLAN {svi_id}",
            "peer_type": link["peer_type"],
            "description": default(svi.get("description"), svi["name"]),
            "shutdown": not (svi.get("enabled", False)),
            "type": "routed" if is_native else "l3dot1q",
            "encapsulation_dot1q_vlan": None if is_native else svi_id,
            "vrf": vrf["name"] if vrf["name"] != "default" else None,
            "ip_address": svi.get("ip_address"),
            "ipv6_address": svi.get("ipv6_address"),
            "ipv6_enable": svi.get("ipv6_enable"),
            "mtu": svi.get("mtu") if self.shared_utils.platform_settings_feature_support_per_interface_mtu else None,
            "eos_cli": svi.get("raw_eos_cli"),
            "struct_cfg": svi.get("structured_config"),
        }
        if (mtu := subinterface["mtu"]) is not None and subinterface["mtu"] > self.shared_utils.p2p_uplinks_mtu:
            raise AristaAvdError(
                f"MTU '{self.shared_utils.p2p_uplinks_mtu}' set for 'p2p_uplinks_mtu' must be larger or equal to MTU '{mtu}' "
                f"set on the SVI '{svi_id}'."
                "Either adjust the MTU on the SVI or p2p_uplinks_mtu."
            )

        # Only set VRRPv4 if ip_address is set
        if subinterface["ip_address"] is not None:
            # TODO in separate PR adding VRRP support for SVIs
            pass

        # Only set VRRPv6 if ipv6_address is set
        if subinterface["ipv6_address"] is not None:
            # TODO in separate PR adding VRRP support for SVIs
            pass

        svi_ip_helpers: list[dict] = convert_dicts(default(svi.get("ip_helpers"), vrf.get("ip_helpers"), []), "ip_helper")
        if svi_ip_helpers:
            subinterface["ip_helpers"] = [
                {"ip_helper": svi_ip_helper["ip_helper"], "source_interface": svi_ip_helper.get("source_interface"), "vrf": svi_ip_helper.get("source_vrf")}
                for svi_ip_helper in svi_ip_helpers
            ]

        if get(svi, "ospf.enabled") is True and get(vrf, "ospf.enabled") is True:
            subinterface.update(
                {
                    "ospf_area": svi["ospf"].get("area", "0"),
                    "ospf_network_point_to_point": svi["ospf"].get("point_to_point", False),
                    "ospf_cost": svi["ospf"].get("cost"),
                }
            )
            ospf_authentication = svi["ospf"].get("authentication")
            if ospf_authentication == "simple" and (ospf_simple_auth_key := svi["ospf"].get("simple_auth_key")) is not None:
                subinterface.update({"ospf_authentication": ospf_authentication, "ospf_authentication_key": ospf_simple_auth_key})
            elif ospf_authentication == "message-digest" and (ospf_message_digest_keys := svi["ospf"].get("message_digest_keys")) is not None:
                ospf_keys = []
                for ospf_key in ospf_message_digest_keys:
                    if not ("id" in ospf_key and "key" in ospf_key):
                        continue

                    ospf_keys.append({"id": ospf_key["id"], "hash_algorithm": ospf_key.get("hash_algorithm", "sha512"), "key": ospf_key["key"]})
                if ospf_keys:
                    subinterface.update({"ospf_authentication": ospf_authentication, "ospf_message_digest_keys": ospf_keys})

        return strip_empties_from_dict(subinterface)
