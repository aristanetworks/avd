# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import re
from functools import cached_property
from ipaddress import ip_network
from itertools import islice

from ansible_collections.arista.avd.plugins.filter.convert_dicts import convert_dicts
from ansible_collections.arista.avd.plugins.plugin_utils.eos_designs_shared_utils import SharedUtils
from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdMissingVariableError
from ansible_collections.arista.avd.plugins.plugin_utils.merge import merge
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
    def _p2p_links_profiles(self) -> list:
        return get(self._hostvars, f"{self.data_model}.p2p_links_profiles", default=[])

    @cached_property
    def _p2p_links_ip_pools(self) -> list:
        return get(self._hostvars, f"{self.data_model}.p2p_links_ip_pools", default=[])

    @cached_property
    def _p2p_links(self) -> list:
        return get(self._hostvars, f"{self.data_model}.p2p_links", default=[])

    @cached_property
    def _p2p_links_sflow(self) -> bool | None:
        return get(self._hostvars, f"fabric_sflow.{self.data_model}")

    @cached_property
    def _filtered_p2p_links(self) -> list:
        """
        Returns a filtered list of p2p_links, which only contains links with our hostname.
        For each links any referenced profiles are applied and IP addresses are resolved
        from pools or subnets.
        """

        if not (p2p_links := self._p2p_links):
            return []

        # Apply p2p_profiles if set. Silently ignoring missing profile.
        if self._p2p_links_profiles:
            p2p_links = [self._apply_profile("p2p_links", p2p_link) for p2p_link in p2p_links]

        # Filter to only include p2p_links with our hostname under "nodes"
        p2p_links = [p2p_link for p2p_link in p2p_links if self.shared_utils.hostname in p2p_link.get("nodes", [])]
        if not p2p_links:
            return []

        # Resolve IPs from subnet or p2p_pools.
        p2p_links = [self._resolve_p2p_ips(p2p_link) for p2p_link in p2p_links]

        # Parse P2P data model and add simplified data
        [p2p_link.update({"data": self._get_p2p_data(p2p_link)}) for p2p_link in p2p_links]

        return p2p_links

    def _apply_profile(self, type: str, target_dict: dict) -> dict:
        """
        Apply a profile to a p2p_link or a l3_interface
        """
        if "profile" not in target_dict:
            # Nothing to do
            return target_dict

        # Silently ignoring missing profile and wrong types.
        if type == "l3_interfaces":
            profile = get_item(self._l3_interfaces_profiles, "profile", target_dict["profile"], default={})
            target_dict.pop("profile", None)
        elif type == "p2p_links":
            profile = get_item(self._p2p_links_profiles, "name", target_dict["profile"], default={})
            target_dict.pop("name", None)
        else:
            return target_dict

        target_dict = merge(profile, target_dict, list_merge="replace", destructive_merge=False)

        return target_dict

    def _resolve_p2p_ips(self, p2p_link: dict) -> dict:
        if "ip" in p2p_link:
            # ip already set, so nothing to do
            return p2p_link

        if "subnet" in p2p_link:
            # Resolve ip from subnet
            subnet = ip_network(p2p_link["subnet"], strict=False)

        elif "ip_pool" not in p2p_link or "id" not in p2p_link or not self._p2p_links_ip_pools:
            # Subnet not set and not possible to resolve from pool. Returning original
            return p2p_link
        else:
            # Resolving subnet from pool
            ip_pool = get_item(self._p2p_links_ip_pools, "name", p2p_link["ip_pool"], default={})
            ip_pool_subnet = ip_pool.get("ipv4_pool")
            if not ip_pool_subnet:
                return p2p_link
            prefix_size = int(ip_pool.get("prefix_size", 31))
            link_id = int(p2p_link["id"])
            subnet = list(islice(ip_network(ip_pool_subnet).subnets(new_prefix=prefix_size), link_id - 1, link_id))[0]

        # hosts() return an iterator of all hosts in subnet.
        # islice() return a generator with only the first two iterations of hosts.
        # List comprehension runs through the generator creating string from each.
        p2p_link["ip"] = [f"{ip}/{subnet.prefixlen}" for ip in islice(subnet.hosts(), 2)]
        return p2p_link

    def _get_p2p_data(self, p2p_link: dict) -> dict:
        """
        Parses p2p_link data model and extracts information which is easier to parse.
        Returns:
        {
            peer: <peer name>
            peer_type: <type of peer>
            interface: <interface on this node>
            peer_interface: <interface on peer>
            port_channel_id: <id on this node | None>
            port_channel_members:
              - interface: <interface on this node>
                peer_interface: <interface on peer>
            ip: <ip if set | None>
            peer_ip: <peer ip if set | None>
            bgp_as: <as if set | None>
            peer_bgp_as: <peer as if set | None>
        }
        """
        index = p2p_link["nodes"].index(self.shared_utils.hostname)
        peer_index = (index + 1) % 2
        peer = p2p_link["nodes"][peer_index]
        peer_facts = self.shared_utils.get_peer_facts(peer, required=False)
        if peer_facts is None:
            peer_type = "other"
        else:
            peer_type = peer_facts.get("type", "other")

        # Set ip or fallback to list with None values
        ip = get(p2p_link, "ip", default=[None, None])
        # Set bgp_as or fallback to list with None values
        bgp_as = get(p2p_link, "as", default=[None, None])
        # Set descriptions or fallback to list with None values
        descriptions = get(p2p_link, "descriptions", default=[None, None])

        data = {
            "peer": peer,
            "peer_type": peer_type,
            "ip": ip[index],
            "peer_ip": ip[peer_index],
            "bgp_as": str(bgp_as[index]),
            "peer_bgp_as": str(bgp_as[peer_index]),
            "description": descriptions[index],
        }

        node_child_interfaces = get(p2p_link, "port_channel.nodes_child_interfaces")
        # Convert to new data models
        node_child_interfaces = convert_dicts(node_child_interfaces, primary_key="node", secondary_key="interfaces")
        if member_interfaces := get_item(node_child_interfaces, "node", self.shared_utils.hostname, default={}).get("interfaces"):
            # Port-channel
            peer_member_interfaces = get_item(
                node_child_interfaces,
                "node",
                peer,
                required=True,
                var_name=f"{peer} under {self.data_model}.p2p_links.[].port_channel.nodes_child_interfaces",
            )["interfaces"]
            pc_id = int("".join(re.findall(r"\d", member_interfaces[0])))
            peer_id = int("".join(re.findall(r"\d", peer_member_interfaces[0])))
            data.update(
                {
                    "interface": f"Port-Channel{pc_id}",
                    "peer_interface": f"Port-Channel{peer_id}",
                    "port_channel_id": pc_id,
                    "port_channel_members": [
                        {
                            "interface": interface,
                            "peer_interface": peer_member_interfaces[index],
                        }
                        for index, interface in enumerate(member_interfaces)
                    ],
                }
            )
            return data

        if "interfaces" in p2p_link:
            # Ethernet
            data.update(
                {
                    "interface": p2p_link["interfaces"][index],
                    "peer_interface": p2p_link["interfaces"][peer_index],
                    "port_channel_id": None,
                    "port_channel_members": [],
                }
            )
            return data

        raise AristaAvdMissingVariableError(f"{self.data_model}.p2p_links must have either 'interfaces' or 'port_channel' with correct members set.")

    def _get_common_interface_cfg(self, p2p_link: dict) -> dict:
        """
        Return partial structured_config for one p2p_link.
        Covers common config that is applicable to both port-channels and ethernet interfaces.
        This config will only be used on the main interface - so not port-channel members.
        """

        index = p2p_link["nodes"].index(self.shared_utils.hostname)
        peer = p2p_link["data"]["peer"]
        peer_interface = p2p_link["data"]["peer_interface"]
        default_description = f"P2P_LINK_TO_{peer}_{peer_interface}"
        interface_cfg = {
            "name": p2p_link["data"]["interface"],
            "peer": peer,
            "peer_interface": peer_interface,
            "peer_type": p2p_link["data"]["peer_type"],
            "description": get(p2p_link, "data.description", default=default_description),
            "type": "routed",
            "shutdown": False,
            "mtu": p2p_link.get("mtu", self.shared_utils.p2p_uplinks_mtu) if self.shared_utils.platform_settings_feature_support_per_interface_mtu else None,
            "service_profile": p2p_link.get("qos_profile", self.shared_utils.p2p_uplinks_qos_profile),
            "eos_cli": p2p_link.get("raw_eos_cli"),
            "struct_cfg": get(p2p_link, "structured_config"),
        }

        if (ip := get(p2p_link, "ip")) is not None:
            interface_cfg["ip_address"] = ip[index]

        if p2p_link.get("include_in_underlay_protocol", True) is True:
            if self.shared_utils.underlay_rfc5549 or p2p_link.get("ipv6_enable") is True:
                interface_cfg["ipv6_enable"] = True

            if self.shared_utils.underlay_ospf:
                interface_cfg.update(
                    {
                        "ospf_network_point_to_point": True,
                        "ospf_area": self.shared_utils.underlay_ospf_area,
                    }
                )

            if self.shared_utils.underlay_isis:
                interface_cfg.update(
                    {
                        "isis_enable": self.shared_utils.isis_instance_name,
                        "isis_metric": default(p2p_link.get("isis_metric"), self.shared_utils.isis_default_metric),
                        "isis_network_point_to_point": p2p_link.get("isis_network_type", "point-to-point") == "point-to-point",
                        "isis_hello_padding": p2p_link.get("isis_hello_padding", True),
                        "isis_circuit_type": default(p2p_link.get("isis_circuit_type"), self.shared_utils.isis_default_circuit_type),
                        "isis_authentication_mode": p2p_link.get("isis_authentication_mode"),
                        "isis_authentication_key": p2p_link.get("isis_authentication_key"),
                    }
                )

        if p2p_link.get("macsec_profile"):
            interface_cfg["mac_security"] = {
                "profile": p2p_link["macsec_profile"],
            }

        if (p2p_link_sflow := get(p2p_link, "sflow", default=self._p2p_links_sflow)) is not None:
            interface_cfg["sflow"] = {"enable": p2p_link_sflow}

        if self.shared_utils.mpls_lsr and p2p_link.get("mpls_ip", True) is True:
            interface_cfg["mpls"] = {"ip": True}
            if p2p_link.get("include_in_underlay_protocol", True) is True and self.shared_utils.underlay_ldp and p2p_link.get("mpls_ldp", True) is True:
                interface_cfg["mpls"].update(
                    {
                        "ldp": {
                            "interface": True,
                            "igp_sync": True,
                        }
                    }
                )

        return interface_cfg

    def _get_ethernet_cfg(self, p2p_link: dict) -> dict:
        """
        Return partial structured_config for one p2p_link.
        Covers config that is only applicable to ethernet interfaces.
        This config will only be used on both main interfaces and port-channel members.
        """

        ethernet_cfg = {"speed": p2p_link.get("speed")}

        if get(p2p_link, "ptp.enabled") is not True:
            return ethernet_cfg

        ptp_config = {}

        # Apply PTP profile config
        if self.shared_utils.ptp_enabled:
            ptp_config.update(self.shared_utils.ptp_profile)

        ptp_config["enable"] = True
        ptp_config.pop("profile", None)
        ethernet_cfg["ptp"] = ptp_config

        return ethernet_cfg

    def _get_port_channel_member_cfg(self, p2p_link: dict, member: dict) -> dict:
        """
        Return partial structured_config for one p2p_link.
        Covers config for ethernet interfaces that are port-channel members.

        TODO: Change description for members to be the physical peer interface instead of port-channel
        """
        peer = p2p_link["data"]["peer"]
        peer_interface = member["peer_interface"]
        default_description = f"P2P_LINK_TO_{peer}_{peer_interface}"
        return {
            "name": member["interface"],
            "type": "port-channel-member",
            "peer": peer,
            "peer_interface": peer_interface,
            "peer_type": p2p_link["data"]["peer_type"],
            "description": get(p2p_link, "data.description", default=default_description),
            "shutdown": False,
            "channel_group": {
                "id": p2p_link["data"]["port_channel_id"],
                "mode": get(p2p_link, "port_channel.mode", default="active"),
            },
        }

    # l3_interfaces here
    @cached_property
    def _l3_interfaces_profiles(self) -> list:
        return get(self._hostvars, f"{self.data_model}.l3_interfaces_profiles", default=[])

    @cached_property
    def _l3_interfaces(self) -> list:
        return get(self._hostvars, f"{self.data_model}.l3_interfaces", default=[])

    @cached_property
    def _l3_interfaces_sflow(self) -> bool | None:
        return get(self._hostvars, f"fabric_sflow.{self.data_model}")

    @cached_property
    def _filtered_l3_interfaces(self) -> list:
        """
        Returns a filtered list of l3_interfaces, which only contains interfaces with our hostname.
        For each interface any referenced profiles are applied.
        """
        if not (l3_interfaces := self._l3_interfaces):
            return []

        # Apply l3_interfaces._profile if set. Silently ignoring missing profile.
        if self._l3_interfaces_profiles:
            l3_interfaces = [self._apply_profile("l3_interfaces", l3_interface) for l3_interface in l3_interfaces]

        # Filter to only include l3_interfaces with our hostname as node
        l3_interfaces = [l3_interface for l3_interface in l3_interfaces if self.shared_utils.hostname == get(l3_interface, "node", required=True)]
        if not l3_interfaces:
            return []

        return l3_interfaces

    def _get_l3_interface_cfg(self, l3_interface: dict) -> dict | None:
        """
        Returns structured_configuration for one L3 Physical interface
        """
        if l3_interface["node"] != self.shared_utils.hostname:
            return None

        interface_name = l3_interface["interface"]

        # TODO move this to description module?
        interface_description = (
            l3_interface.get("description")
            or "_".join([elem for elem in [l3_interface.get("peer"), l3_interface.get("peer_interface")] if elem is not None])
            or None
        )

        # TODO catch if ip_address is not valid or not dhcp
        ip_address = get(l3_interface, "ip", required=True)

        interface = {
            "name": interface_name,
            "peer_type": "l3_interface",
            "peer": l3_interface.get("peer"),
            "peer_interface": l3_interface.get("peer_interface"),
            "ip_address": ip_address,
            "shutdown": not l3_interface.get("enabled", True),
            "type": "routed",
            "description": interface_description,
            "service_profile": l3_interface.get("qos_profile"),
            "eos_cli": l3_interface.get("raw_eos_cli"),
            "struct_cfg": l3_interface.get("structured_config"),
        }

        if ip_address == "dhcp" and l3_interface.get("set_default_route", False):
            interface["dhcp_client_accept_default_route"] = True

        if self.shared_utils.cv_pathfinder_role:
            interface["flow_tracker"] = {"hardware": "WAN-FLOW-TRACKER"}

        return strip_empties_from_dict(interface)
