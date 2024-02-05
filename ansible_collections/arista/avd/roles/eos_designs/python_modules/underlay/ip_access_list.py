# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from ipaddress import ip_network

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
        return structured config for ip_access_lists

        Used for the wan interfaces.
        """

        if self.shared_utils.wan_role is None:
            return None

        ipAccessList = []
        if acl_inbound := self._get_access_list_inbound():
            ipAccessList.append(acl_inbound)
        if acl_outbound := self._get_access_list_outbound():
            ipAccessList.append(acl_outbound)

        if ipAccessList:
            return ipAccessList

        return None

    def _get_access_list_outbound(self) -> dict | None:
        outbound_access_list = {
            "name": "PUBLIC_TRANSPORT_OUT",
            "entries": [
                {"sequence": self._get_sequence(True), "remark": " ### Blocking RFC 1918 prefixes ###"},
                {"sequence": self._get_sequence(), "action": "deny", "protocol": "ip", "source": "any", "destination": "10.0.0.0/8"},
                {"sequence": self._get_sequence(), "action": "deny", "protocol": "ip", "source": "any", "destination": "172.16.0.0/12"},
                {"sequence": self._get_sequence(), "action": "deny", "protocol": "ip", "source": "any", "destination": "192.168.0.0/16"},
                {"sequence": self._get_sequence(), "action": "permit", "protocol": "ip", "source": "any", "destination": "any"},
            ],
        }
        return outbound_access_list

    def _get_access_list_inbound(self) -> dict | None:
        interface_subnets = []
        for l3_interface in self.shared_utils.l3_interfaces:
            interface_ip = l3_interface.get("ip_address")
            if interface_ip and interface_ip != "dhcp":
                subnet = str(ip_network(interface_ip, False))
                if subnet not in interface_subnets:
                    interface_subnets.append(subnet)
            # Need to see how to handle dhcp cases.

        if not interface_subnets:
            return {}

        outbound_access_list = {
            "name": "PUBLIC_TRANSPORT_IN",
            "entries": [],
        }
        # Allow BGP
        outbound_access_list["entries"].append(
            {
                "sequence": self._get_sequence(True),
                "remark": "### Allow BGP ###",
            },
        )
        for source in interface_subnets:
            outbound_access_list["entries"].append(
                {
                    "sequence": self._get_sequence(),
                    "action": "permit",
                    "protocol": "tcp",
                    "source": source,
                    "destination": "any",
                    "destination_ports_match": "eq",
                    "destination_ports": ["bgp"],
                },
            )

        # Allow GRE
        outbound_access_list["entries"].append(
            {
                "sequence": self._get_sequence(),
                "remark": "### Allow GRE ###",
            },
        )
        for source in interface_subnets:
            outbound_access_list["entries"].append(
                {
                    "sequence": self._get_sequence(),
                    "action": "permit",
                    "protocol": "gre",
                    "source": source,
                    "destination": "any",
                },
            )

        # Allow IPSEC
        outbound_access_list["entries"].append(
            {
                "sequence": self._get_sequence(),
                "remark": "### Allow IPSEC ###",
            },
        )
        for source in interface_subnets:
            outbound_access_list["entries"].append(
                {
                    "sequence": self._get_sequence(),
                    "action": "permit",
                    "protocol": "udp",
                    "source": source,
                    "destination": "any",
                    "destination_ports_match": "eq",
                    "destination_ports": ["isakmp", "3478", "non500-isakmp"],
                },
            )

        # Allow ICMP
        outbound_access_list["entries"].append(
            {
                "sequence": self._get_sequence(),
                "remark": "### Allow ICMP ###",
            },
        )
        for source in interface_subnets:
            outbound_access_list["entries"].extend(
                [
                    {
                        "sequence": self._get_sequence(),
                        "action": "permit",
                        "protocol": "icmp",
                        "icmp_type": "echo-reply",
                        "source": source,
                        "destination": "any",
                    },
                    {
                        "sequence": self._get_sequence(),
                        "action": "permit",
                        "protocol": "icmp",
                        "icmp_type": "unreachable",
                        "source": source,
                        "destination": "any",
                    },
                    {
                        "sequence": self._get_sequence(),
                        "action": "permit",
                        "protocol": "icmp",
                        "icmp_type": "time-exceeded",
                        "source": source,
                        "destination": "any",
                    },
                ]
            )

        # Deny other kind of packets
        outbound_access_list["entries"].append(
            {
                "sequence": self._get_sequence(),
                "action": "deny",
                "protocol": "ip",
                "source": "any",
                "destination": "any",
            }
        )
        return outbound_access_list

    def _get_sequence(self, refresh=False):
        if refresh:
            self.sequence = 0
        self.sequence += 10
        return self.sequence
