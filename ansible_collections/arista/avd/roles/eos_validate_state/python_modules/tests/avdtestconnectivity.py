# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import logging
from functools import cached_property
from ipaddress import ip_interface

from ansible_collections.arista.avd.plugins.plugin_utils.eos_validate_state_utils.avdtestbase import AvdTestBase
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get

LOGGER = logging.getLogger(__name__)


class AvdTestP2PIPReachability(AvdTestBase):
    """
    AvdTestP2PIPReachability class for P2P IP reachability tests.
    """

    anta_module = "anta.tests.connectivity"
    categories = ["IP Reachability"]
    description = "ip reachability test p2p links"

    @cached_property
    def test_definition(self) -> dict | None:
        """
        Generates the proper ANTA test definition for all fabric P2P IP reachability tests.

        Returns:
            test_definition (dict): ANTA test definition.
        """
        anta_tests = []

        if not self.safe_get(key="ethernet_interfaces"):
            return None

        required_keys = ["name", "peer", "peer_interface", "ip_address"]

        if not (valid_ethernet_interfaces := self.validate_vars(data_model="ethernet_interfaces", required_keys=required_keys, type="routed", shutdown=False)):
            return None

        for interface in valid_ethernet_interfaces:
            if not self.is_peer_available(peer := interface["peer"]):
                continue

            if not (peer_interface_ip := self.get_interface_ip(interface_model="ethernet_interfaces", interface_name=interface["peer_interface"], host=peer)):
                continue

            src_ip = str(ip_interface(interface["ip_address"]).ip)
            dst_ip = str(ip_interface(peer_interface_ip).ip)
            custom_field = f"Source: {self.device_name}_{interface['name']} - Destination: {peer}_{interface['peer_interface']}"
            anta_tests.append(
                {
                    "VerifyReachability": {
                        "hosts": [{"source": src_ip, "destination": dst_ip, "vrf": "default", "repeat": 1}],
                        "result_overwrite": {"categories": self.categories, "description": self.description, "custom_field": custom_field},
                    }
                }
            )

        return {self.anta_module: anta_tests} if anta_tests else None


class AvdTestInbandReachability(AvdTestBase):
    """
    AvdTestInbandReachability class for inband management reachability tests.
    """

    anta_module = "anta.tests.connectivity"
    categories = ["Loopback0 Reachability"]
    description = "Inband Mgmt Reachability"

    @cached_property
    def test_definition(self) -> dict | None:
        """
        Generates the proper ANTA test definition for all inband management reachability tests.

        Returns:
            test_definition (dict): ANTA test definition.
        """
        anta_tests = []

        if not self.safe_get(key="management_interfaces"):
            return None

        if not (valid_management_interfaces := self.validate_vars(data_model="management_interfaces", required_keys="name", type="inband", shutdown=False)):
            return None

        for interface in valid_management_interfaces:
            for dst_node, dst_ip in self.loopback0_mapping:
                if not self.is_peer_available(dst_node):
                    continue

                custom_field = f"Source: {self.device_name} - {interface['name']} Destination: {dst_ip}"
                anta_tests.append(
                    {
                        "VerifyReachability": {
                            "hosts": [{"source": interface["name"], "destination": dst_ip, "vrf": "default", "repeat": 1}],
                            "result_overwrite": {"categories": self.categories, "description": self.description, "custom_field": custom_field},
                        }
                    }
                )

        return {self.anta_module: anta_tests} if anta_tests else None


class AvdTestLoopback0Reachability(AvdTestBase):
    """
    AvdTestLoopback0Reachability class for Loopback0 reachability tests.
    """

    anta_module = "anta.tests.connectivity"
    categories = ["Loopback0 Reachability"]
    description = "Loopback0 Reachability"

    @cached_property
    def test_definition(self) -> dict | None:
        """
        Generates the proper ANTA test definition for all Loopback0 reachability tests.

        Returns:
            test_definition (dict): ANTA test definition.

        """
        anta_tests = []

        # To be removed once 'l3leaf' check is removed
        if not (node_type := self.safe_get(key="type")):
            return None

        if node_type == "l3leaf":
            if not (src_ip := self.get_interface_ip(interface_model="loopback_interfaces", interface_name="Loopback0")):
                return None

            for dst_node, dst_ip in self.loopback0_mapping:
                if not self.is_peer_available(dst_node):
                    continue

                custom_field = f"Source: {self.device_name} - {src_ip} Destination: {dst_ip}"
                anta_tests.append(
                    {
                        "VerifyReachability": {
                            "hosts": [{"source": str(ip_interface(src_ip).ip), "destination": dst_ip, "vrf": "default", "repeat": 1}],
                            "result_overwrite": {"categories": self.categories, "description": self.description, "custom_field": custom_field},
                        }
                    }
                )

        return {self.anta_module: anta_tests} if anta_tests else None


class AvdTestLLDPTopology(AvdTestBase):
    """
    AvdTestLLDPTopology class for the LLDP topology tests.
    """

    anta_module = "anta.tests.connectivity"
    categories = ["LLDP Topology"]
    description = "LLDP topology - validate peer and interface"

    @cached_property
    def test_definition(self) -> dict | None:
        """
        Generates the proper ANTA test definition for all LLDP topology tests.

        Returns:
            test_definition (dict): ANTA test definition.

        """
        anta_tests = []

        if not self.safe_get(key="ethernet_interfaces"):
            return None

        required_keys = ["name", "peer", "peer_interface"]

        if not (valid_ethernet_interfaces := self.validate_vars(data_model="ethernet_interfaces", required_keys=required_keys, shutdown=False)):
            return None

        for interface in valid_ethernet_interfaces:
            if not self.is_peer_available(peer := interface["peer"]):
                continue

            custom_field = f"local: {interface['name']} - remote: {peer}_{interface['peer_interface']}"

            if (dns_domain := get(self.hostvars[peer], "dns_domain")) is not None:
                peer = f"{peer}.{dns_domain}"

            anta_tests.append(
                {
                    "VerifyLLDPNeighbors": {
                        "neighbors": [
                            {
                                "port": str(interface["name"]),
                                "neighbor_device": str(peer),
                                "neighbor_port": str(interface["peer_interface"]),
                            }
                        ],
                        "result_overwrite": {"categories": self.categories, "description": self.description, "custom_field": custom_field},
                    }
                }
            )

        return {self.anta_module: anta_tests} if anta_tests else None
