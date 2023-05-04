from __future__ import annotations

import re
from functools import cached_property
from ipaddress import ip_network
from itertools import islice

from ansible_collections.arista.avd.plugins.filter.convert_dicts import convert_dicts
from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdMissingVariableError
from ansible_collections.arista.avd.plugins.plugin_utils.merge import merge
from ansible_collections.arista.avd.plugins.plugin_utils.utils import default, get, get_item
from ansible_collections.arista.avd.roles.eos_designs.python_modules.interface_descriptions import AvdInterfaceDescriptions
from ansible_collections.arista.avd.roles.eos_designs.python_modules.ip_addressing import AvdIpAddressing


class UtilsMixin:
    """
    Mixin Class with internal functions.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    # Set type hints for Attributes of the main class as needed
    _hostvars: dict
    _avd_ip_addressing: AvdIpAddressing
    _avd_interface_descriptions: AvdInterfaceDescriptions

    @cached_property
    def _l3_edge(self) -> list:
        return get(self._hostvars, "l3_edge")

    @cached_property
    def _p2p_links_profiles(self) -> list:
        return convert_dicts(get(self._hostvars, "l3_edge.p2p_links_profiles", default=[]), "name")

    @cached_property
    def _p2p_links_ip_pools(self) -> list:
        return convert_dicts(get(self._hostvars, "l3_edge.p2p_links_ip_pools", default=[]), primary_key="name", secondary_key="ipv4_pool")

    @cached_property
    def _p2p_links(self) -> list:
        return get(self._hostvars, "l3_edge.p2p_links", default=[])

    @cached_property
    def _hostname(self) -> str:
        return get(self._hostvars, "switch.hostname", required=True)

    @cached_property
    def _p2p_uplinks_mtu(self) -> str:
        return get(self._hostvars, "p2p_uplinks_mtu", required=True)

    @cached_property
    def _p2p_uplinks_qos_profile(self) -> str | None:
        return get(self._hostvars, "p2p_uplinks_qos_profile")

    @cached_property
    def _underlay_rfc5549(self) -> bool:
        return get(self._hostvars, "underlay_rfc5549") is True

    @cached_property
    def _underlay_bgp(self) -> bool:
        return get(self._hostvars, "switch.underlay.bgp") is True

    @cached_property
    def _underlay_ospf(self) -> bool:
        return get(self._hostvars, "switch.underlay.ospf") is True

    @cached_property
    def _underlay_isis(self) -> bool:
        return get(self._hostvars, "switch.underlay.isis") is True

    @cached_property
    def _underlay_ldp(self) -> bool:
        return get(self._hostvars, "switch.underlay.ldp") is True

    @cached_property
    def _mpls_lsr(self) -> bool:
        return get(self._hostvars, "switch.mpls_lsr") is True

    @cached_property
    def _underlay_ospf_area(self) -> str:
        return get(self._hostvars, "underlay_ospf_area", required=True)

    @cached_property
    def _underlay_ospf_process_id(self) -> int:
        return get(self._hostvars, "underlay_ospf_process_id", required=True)

    @cached_property
    def _isis_instance_name(self) -> str:
        return get(self._hostvars, "switch.isis_instance_name", required=True)

    @cached_property
    def _isis_default_metric(self) -> int | None:
        return get(self._hostvars, "isis_default_metric")

    @cached_property
    def _isis_default_circuit_type(self) -> str | None:
        return get(self._hostvars, "isis_default_circuit_type")

    @cached_property
    def _peer_group_ipv4_underlay_peers_name(self) -> str:
        return get(self._hostvars, "switch.bgp_peer_groups.ipv4_underlay_peers.name", required=True)

    @cached_property
    def _bgp_as(self) -> str | None:
        return get(self._hostvars, "switch.bgp_as")

    @cached_property
    def _ptp_profile(self) -> dict:
        if (ptp_profile_name := get(self._hostvars, "switch.ptp.profile")) is None:
            return {}

        ptp_profiles = get(self._hostvars, "ptp_profiles", [])
        return get_item(ptp_profiles, "profile", ptp_profile_name, default={})

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
            p2p_links = [self._apply_p2p_profile(p2p_link) for p2p_link in p2p_links]

        # Filter to only include p2p_links with our hostname under "nodes"
        p2p_links = [p2p_link for p2p_link in p2p_links if self._hostname in p2p_link.get("nodes", [])]
        if not p2p_links:
            return []

        # Resolve IPs from subnet or p2p_pools.
        p2p_links = [self._resolve_p2p_ips(p2p_link) for p2p_link in p2p_links]

        # Parse P2P data model and add simplified data
        [p2p_link.update({"data": self._get_p2p_data(p2p_link)}) for p2p_link in p2p_links]

        return p2p_links

    def _apply_p2p_profile(self, p2p_link: dict) -> dict:
        if "profile" not in p2p_link:
            # Nothing to do
            return p2p_link

        # Silently ignoring missing profile.
        profile = get_item(self._p2p_links_profiles, "name", p2p_link["profile"], default={})
        p2p_link = merge(profile, p2p_link, list_merge="replace", destructive_merge=False)
        p2p_link.pop("name", None)
        return p2p_link

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
            ip_pool = get_item(self._p2p_links_ip_pools, "name", p2p_link["ip_pool"], default={}).get("ipv4_pool")
            if not ip_pool:
                # Not possible to resolve from pool. Returning original
                return p2p_link
            id = int(p2p_link["id"])
            subnet = list(islice(ip_network(ip_pool).subnets(new_prefix=31), id - 1, id))[0]

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
        index = p2p_link["nodes"].index(self._hostname)
        peer_index = (index + 1) % 2
        peer = p2p_link["nodes"][peer_index]
        peer_type = get(self._hostvars, f"avd_switch_facts..{peer}..switch..type", default="other", separator="..")

        # Set ip or fallback to list with None values
        ip = get(p2p_link, "ip", default=[None, None])
        # Set bgp_as or fallback to list with None values
        bgp_as = get(p2p_link, "as", default=[None, None])

        data = {
            "peer": peer,
            "peer_type": peer_type,
            "ip": ip[index],
            "peer_ip": ip[peer_index],
            "bgp_as": str(bgp_as[index]) if bgp_as[index] is not None else None,
            "peer_bgp_as": str(bgp_as[peer_index]) if bgp_as[peer_index] is not None else None,
        }

        node_child_interfaces = get(p2p_link, "port_channel.nodes_child_interfaces")
        # Convert to new data models
        node_child_interfaces = convert_dicts(node_child_interfaces, primary_key="node", secondary_key="interfaces")
        if member_interfaces := get_item(node_child_interfaces, "node", self._hostname, default={}).get("interfaces"):
            # Port-channel
            peer_member_interfaces = get_item(
                node_child_interfaces,
                "node",
                peer,
                required=True,
                var_name=f"{peer} under l3_edge.p2p_links.[].port_channel.nodes_child_interfaces",
            )["interfaces"]
            id = int("".join(re.findall(r"\d", member_interfaces[0])))
            peer_id = int("".join(re.findall(r"\d", peer_member_interfaces[0])))
            data.update(
                {
                    "interface": f"Port-Channel{id}",
                    "peer_interface": f"Port-Channel{peer_id}",
                    "port_channel_id": id,
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

        raise AristaAvdMissingVariableError("l3_edge.p2p_links must have either 'interfaces' or 'port_channel' with correct members set.")

    def _get_common_interface_cfg(self, p2p_link: dict) -> dict:
        """
        Return partial structured_config for one p2p_link.
        Covers common config that is applicable to both port-channels and ethernet interfaces.
        This config will only be used on the main interface - so not port-channel members.
        """

        index = p2p_link["nodes"].index(self._hostname)
        peer = p2p_link["data"]["peer"]
        peer_interface = p2p_link["data"]["peer_interface"]
        interface_cfg = {
            "peer": peer,
            "peer_interface": peer_interface,
            "peer_type": p2p_link["data"]["peer_type"],
            "description": f"P2P_LINK_TO_{peer}_{peer_interface}",
            "type": "routed",
            "shutdown": False,
            "mtu": p2p_link.get("mtu", self._p2p_uplinks_mtu),
            # TODO: Set p2p_uplinks_qos_profile as default like it is in core_interfaces.
            "service_profile": p2p_link.get("qos_profile"),
            "eos_cli": p2p_link.get("raw_eos_cli"),
        }
        if (ip := get(p2p_link, "ip")) is not None:
            interface_cfg["ip_address"] = ip[index]

        if p2p_link.get("include_in_underlay_protocol") is True:
            if self._underlay_rfc5549 or p2p_link.get("ipv6_enable") is True:
                interface_cfg["ipv6_enable"] = True

            if self._underlay_ospf:
                interface_cfg.update(
                    {
                        "ospf_network_point_to_point": True,
                        "ospf_area": self._underlay_ospf_area,
                    }
                )

            if self._underlay_isis:
                interface_cfg.update(
                    {
                        "isis_enable": self._isis_instance_name,
                        "isis_metric": default(p2p_link.get("isis_metric"), self._isis_default_metric, 50),
                        "isis_network_point_to_point": (p2p_link.get("isis_network_type", "point-to-point") == "point-to-point"),
                        # TODO: Update defaults below to have same as core_interfaces - or vice versa
                        "isis_hello_padding": p2p_link.get("isis_hello_padding"),
                        "isis_circuit_type": default(p2p_link.get("isis_circuit_type"), self._isis_default_circuit_type),
                        "isis_authentication_mode": p2p_link.get("isis_authentication_mode"),
                        "isis_authentication_key": p2p_link.get("isis_authentication_key"),
                    }
                )

        if p2p_link.get("macsec_profile"):
            interface_cfg["mac_security"] = {
                "profile": p2p_link["macsec_profile"],
            }

        if self._mpls_lsr and p2p_link.get("mpls_ip", True) is True:
            interface_cfg["mpls"] = {"ip": True}
            if p2p_link.get("include_in_underlay_protocol") is True and self._underlay_ldp and p2p_link.get("mpls_ldp", True) is True:
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

        if p2p_link.get("ptp_enable") is not True:
            return ethernet_cfg

        ptp_config = {}

        # Apply PTP profile config
        ptp_config.update(self._ptp_profile)

        ptp_config["enable"] = True
        ptp_config.pop("profile", None)
        ethernet_cfg["ptp"] = ptp_config

        return ethernet_cfg

    def _get_port_channel_member_cfg(self, p2p_link: dict) -> dict:
        """
        Return partial structured_config for one p2p_link.
        Covers config for ethernet interfaces that are port-channel members.

        TODO: Change description for members to be the physical peer interface instead of port-channel
        """
        peer = p2p_link["data"]["peer"]
        peer_interface = p2p_link["data"]["peer_interface"]
        return {
            "peer": peer,
            "peer_interface": peer_interface,
            "peer_type": p2p_link["data"]["peer_type"],
            "description": f"P2P_LINK_TO_{peer}_{peer_interface}",
            "shutdown": False,
            "channel_group": {
                "id": p2p_link["data"]["port_channel_id"],
                "mode": get(p2p_link, "port_channel.mode", default="active"),
            },
        }
