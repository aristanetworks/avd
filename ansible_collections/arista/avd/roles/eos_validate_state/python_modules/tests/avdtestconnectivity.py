# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from ipaddress import ip_interface

from ansible_collections.arista.avd.plugins.plugin_utils.eos_validate_state_utils.avdtestbase import AvdTestBase
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get


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

        if (ethernet_interfaces := self.logged_get(key="ethernet_interfaces")) is None:
            return None

        required_keys = ["name", "peer", "peer_interface", "ip_address"]

        for idx, interface in enumerate(ethernet_interfaces):
            if not self.validate_data(data=interface, data_path=f"ethernet_interfaces.[{idx}]", required_keys=required_keys, type="routed", shutdown=False):
                continue

            if not self.is_peer_available(peer := interface["peer"]):
                continue

            if (
                peer_interface_ip := self.get_interface_ip(interface_model="ethernet_interfaces", interface_name=interface["peer_interface"], host=peer)
            ) is None:
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

        if (management_interfaces := self.logged_get(key="management_interfaces")) is None:
            return None

        for idx, interface in enumerate(management_interfaces):
            if not self.validate_data(data=interface, data_path=f"management_interface.[{idx}]", required_keys="name", type="inband", shutdown=False):
                continue

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

        if not self.validate_data(type="l3leaf"):
            return None

        if (src_ip := self.get_interface_ip(interface_model="loopback_interfaces", interface_name="Loopback0")) is None:
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

        if (ethernet_interfaces := self.logged_get(key="ethernet_interfaces")) is None:
            return None

        required_keys = ["name", "peer", "peer_interface"]

        for idx, interface in enumerate(ethernet_interfaces):
            if not self.validate_data(data=interface, data_path=f"ethernet_interfaces.[{idx}]", required_keys=required_keys, shutdown=False):
                continue

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
