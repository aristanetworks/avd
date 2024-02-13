# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from ipaddress import ip_network
from pickle import TRUE

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
        ip_access_lists.extend(self._get_access_lists_inbound())
        ip_access_lists.extend(self._get_access_list_outbound())

        if ip_access_lists:
            return ip_access_lists

        return None

    def _get_access_list_outbound(self) -> list:
        """
        Returns the outbound access list.
        Blocks the RFC1918 traffic.
        """
        if self.shared_utils.wan_interfaces:
            outbound_access_list = {
                "name": "ACL-WAN-TRANSPORT-OUT",
                "entries": [
                    {"sequence": self._get_sequence(refresh=True), "remark": " ### Blocking RFC 1918 prefixes ###"},
                    {"sequence": self._get_sequence(), "action": "deny", "protocol": "ip", "source": "any", "destination": "10.0.0.0/8"},
                    {"sequence": self._get_sequence(), "action": "deny", "protocol": "ip", "source": "any", "destination": "172.16.0.0/12"},
                    {"sequence": self._get_sequence(), "action": "deny", "protocol": "ip", "source": "any", "destination": "192.168.0.0/16"},
                    {"sequence": self._get_sequence(), "action": "permit", "protocol": "ip", "source": "any", "destination": "any"},
                ],
            }
            return [outbound_access_list]
        return []

    def _get_access_lists_inbound(self) -> list:
        """
        Returns the inbound access lists for different interfaces.
        The ACL name per interface is of the form "WAN_TRANSPORT_<INTERFACE_NAME>_IN".
        """
        inbound_access_lists = []
        for l3_interface in self.shared_utils.wan_interfaces:
            interface_ip_cidr = l3_interface.get("ip_address")
            interface_ip = interface_ip_cidr.split("/")[0]
            # Need to see how to handle dhcp cases.
            if interface_ip and interface_ip != "dhcp":
                l3_interface_name = l3_interface.get("name")
                inbound_access_list = {
                    "name": self._get_inbound_wan_acl_name(l3_interface_name),
                    "entries": [],
                }

                # Allow IPSEC
                inbound_access_list["entries"].extend(
                    [
                        {
                            "sequence": self._get_sequence(refresh=TRUE),
                            "remark": "### Allow IPSEC ###",
                        },
                        {
                            "sequence": self._get_sequence(),
                            "action": "permit",
                            "protocol": "udp",
                            "source": "any",
                            "destination": interface_ip,
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
                            "destination": interface_ip,
                        },
                        {
                            "sequence": self._get_sequence(),
                            "action": "permit",
                            "protocol": "icmp",
                            "icmp_type": "unreachable",
                            "source": "any",
                            "destination": interface_ip,
                        },
                        {
                            "sequence": self._get_sequence(),
                            "action": "permit",
                            "protocol": "icmp",
                            "icmp_type": "time-exceeded",
                            "source": "any",
                            "destination": interface_ip,
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
        return inbound_access_lists

    def _get_sequence(self, refresh=False):
        """
            Returns sequence numbers starting from 10 and incrementing by 10.
            Set refresh to True to restart the sequence.
        """
        if refresh:
            self.sequence = 0
        self.sequence += 10
        return self.sequence
