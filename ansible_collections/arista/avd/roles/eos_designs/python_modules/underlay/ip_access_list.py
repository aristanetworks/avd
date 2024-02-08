# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from ipaddress import ip_network
from typing import List

from .utils import UtilsMixin


class IPAccessListsMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    sequence = 0

    @cached_property
    def ip_access_lists(self) -> list | None:
        """
        Return structured config for ip_access_lists

        Used for the wan interfaces.
        """

        if self.shared_utils.wan_role is None:
            return None

        ip_access_lists = []
        if acl_inbound_lists := self._get_access_lists_inbound():
            ip_access_lists.extend(acl_inbound_lists)
        if acl_outbound := self._get_access_list_outbound():
            ip_access_lists.append(acl_outbound)

        if ip_access_lists:
            return ip_access_lists

        return None

    def _get_access_list_outbound(self) -> dict | None:
        """
        Returns the outbound access list.
        Blocks the RFC1918 traffic.
        """
        if self.shared_utils.wan_interfaces:
            outbound_access_list = {
                "name": "WAN_TRANSPORT_OUT",
                "entries": [
                    {"sequence": self._get_sequence(True), "remark": " ### Blocking RFC 1918 prefixes ###"},
                    {"sequence": self._get_sequence(), "action": "deny", "protocol": "ip", "source": "any", "destination": "10.0.0.0/8"},
                    {"sequence": self._get_sequence(), "action": "deny", "protocol": "ip", "source": "any", "destination": "172.16.0.0/12"},
                    {"sequence": self._get_sequence(), "action": "deny", "protocol": "ip", "source": "any", "destination": "192.168.0.0/16"},
                    {"sequence": self._get_sequence(), "action": "permit", "protocol": "ip", "source": "any", "destination": "any"},
                ],
            }
            return outbound_access_list
        return None

    def _get_access_lists_inbound(self) -> List | None:
        """
        Returns the inbound access lists for different interfaces.
        The ACL name per interface is of the form "WAN_TRANSPORT_<INTERFACE_NAME>_IN".
        """
        inbound_access_lists = []
        for l3_interface in self.shared_utils.wan_interfaces:
            interface_ip = l3_interface.get("ip_address")
            # Need to see how to handle dhcp cases.
            if interface_ip and interface_ip != "dhcp":
                subnet = str(ip_network(interface_ip, False))
                l3_interface_name = l3_interface.get("name")
                inbound_access_list = {
                    "name": self._get_inbound_wan_acl_name(l3_interface_name),
                    "entries": [],
                }
                # Allow BGP
                inbound_access_list["entries"].extend(
                    [
                        {
                            "sequence": self._get_sequence(refresh=True),
                            "remark": "### Allow BGP ###",
                        },
                        {
                            "sequence": self._get_sequence(),
                            "action": "permit",
                            "protocol": "tcp",
                            "source": "any",
                            "destination": subnet,
                            "destination_ports_match": "eq",
                            "destination_ports": ["bgp"],
                        },
                    ]
                )

                # Allow GRE
                inbound_access_list["entries"].extend(
                    [
                        {
                            "sequence": self._get_sequence(),
                            "remark": "### Allow GRE ###",
                        },
                        {
                            "sequence": self._get_sequence(),
                            "action": "permit",
                            "protocol": "gre",
                            "source": "any",
                            "destination": subnet,
                        },
                    ]
                )

                # Allow IPSEC
                inbound_access_list["entries"].extend(
                    [
                        {
                            "sequence": self._get_sequence(),
                            "remark": "### Allow IPSEC ###",
                        },
                        {
                            "sequence": self._get_sequence(),
                            "action": "permit",
                            "protocol": "udp",
                            "source": "any",
                            "destination": subnet,
                            "destination_ports_match": "eq",
                            "destination_ports": ["isakmp", "3478", "non500-isakmp"],
                        },
                    ]
                )

                # Allow ICMP
                inbound_access_list["entries"].extend(
                    [
                        {
                            "sequence": self._get_sequence(),
                            "remark": "### Allow ICMP ###",
                        },
                        {
                            "sequence": self._get_sequence(),
                            "action": "permit",
                            "protocol": "icmp",
                            "icmp_type": "echo-reply",
                            "source": "any",
                            "destination": subnet,
                        },
                        {
                            "sequence": self._get_sequence(),
                            "action": "permit",
                            "protocol": "icmp",
                            "icmp_type": "unreachable",
                            "source": "any",
                            "destination": subnet,
                        },
                        {
                            "sequence": self._get_sequence(),
                            "action": "permit",
                            "protocol": "icmp",
                            "icmp_type": "time-exceeded",
                            "source": "any",
                            "destination": subnet,
                        },
                    ]
                )
                inbound_access_list["entries"].append(
                    {
                        "sequence": self._get_sequence(),
                        "action": "deny",
                        "protocol": "ip",
                        "source": "any",
                        "destination": "any",
                    }
                )
                inbound_access_lists.append(inbound_access_list)
        if inbound_access_lists:
            return inbound_access_lists
        return None

    def _get_sequence(self, refresh=False):
        if refresh:
            self.sequence = 0
        self.sequence += 10
        return self.sequence
