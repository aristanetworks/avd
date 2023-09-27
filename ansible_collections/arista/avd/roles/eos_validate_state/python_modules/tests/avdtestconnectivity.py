# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import logging
from functools import cached_property
from ipaddress import ip_interface

from ansible_collections.arista.avd.plugins.plugin_utils.eos_validate_state_utils.avdtestbase import AvdTestBase
from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdMissingVariableError
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get, get_item

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

        try:
            ethernet_interfaces = get(self.hostvars[self.device_name], "ethernet_interfaces", required=True)
        except AristaAvdMissingVariableError as e:
            LOGGER.warning("Variable '%s' is missing from the structured_config. %s is skipped.", str(e), self.__class__.__name__)
            return None

        required_vars = ["type", "ip_address", "peer", "peer_interface"]

        for ethernet_interface in ethernet_interfaces:
            try:
                for var in required_vars:
                    get(ethernet_interface, var, required=True)

                peer_ethernet_interfaces = get(self.hostvars, f"{ethernet_interface['peer']}.ethernet_interfaces", required=True)
                peer_interface = get_item(
                    peer_ethernet_interfaces,
                    "name",
                    ethernet_interface["peer_interface"],
                    required=True,
                    var_name=f"name: {ethernet_interface['peer_interface']}",
                )
                peer_interface_ip = get(peer_interface, "ip_address", required=True)

                if ethernet_interface["type"] == "routed":
                    src_ip = str(ip_interface(ethernet_interface["ip_address"]).ip)
                    dst_ip = str(ip_interface(peer_interface_ip).ip)
                    custom_field = (
                        f"Source: {self.device_name}_{ethernet_interface['name']} - Destination:"
                        f" {ethernet_interface['peer']}_{ethernet_interface['peer_interface']}"
                    )
                    anta_tests.append(
                        {
                            "VerifyReachability": {
                                "hosts": [{"source": src_ip, "destination": dst_ip, "vrf": "default", "repeat": 1}],
                                "result_overwrite": {"categories": self.categories, "description": self.description, "custom_field": custom_field},
                            }
                        }
                    )

            except AristaAvdMissingVariableError as e:
                LOGGER.info("Variable '%s' is missing. Please validate the Ethernet interfaces data model of this host and his peer(s).", str(e))
                continue

        return {self.anta_module: anta_tests}


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

        try:
            management_interfaces = get(self.hostvars[self.device_name], "management_interfaces", required=True)
        except AristaAvdMissingVariableError as e:
            LOGGER.warning("Variable '%s' is missing from the structured_config. %s is skipped.", str(e), self.__class__.__name__)
            return None

        for management_interface in management_interfaces:
            try:
                _type = get(management_interface, "type", required=True)
                if _type == "inband":
                    for dst_node, dst_ip in self.loopback0_mapping:
                        custom_field = f"Source: {self.device_name} - {management_interface['name']} Destination: {dst_ip}"
                        anta_tests.append(
                            {
                                "VerifyReachability": {
                                    "hosts": [{"source": management_interface["name"], "destination": dst_ip, "vrf": "default", "repeat": 1}],
                                    "result_overwrite": {"categories": self.categories, "description": self.description, "custom_field": custom_field},
                                }
                            }
                        )
            except AristaAvdMissingVariableError as e:
                LOGGER.warning("Variable '%s' is missing. Please validate the Management interfaces data model of this host.", str(e))
                continue

        return {self.anta_module: anta_tests}


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

        try:
            # To be removed once 'l3leaf' check is removed
            node_type = get(self.hostvars[self.device_name], "type", required=True)

            if node_type == "l3leaf":
                loopback_interfaces = get(self.hostvars[self.device_name], "loopback_interfaces", required=True)
                loopback0 = get_item(loopback_interfaces, "name", "Loopback0", required=True, var_name="name: Loopback0")
                src_ip = get(loopback0, "ip_address", required=True)

                for dst_node, dst_ip in self.loopback0_mapping:
                    custom_field = f"Source: {self.device_name} - {src_ip} Destination: {dst_ip}"
                    anta_tests.append(
                        {
                            "VerifyReachability": {
                                "hosts": [{"source": str(ip_interface(src_ip).ip), "destination": dst_ip, "vrf": "default", "repeat": 1}],
                                "result_overwrite": {"categories": self.categories, "description": self.description, "custom_field": custom_field},
                            }
                        }
                    )
        except AristaAvdMissingVariableError as e:
            if str(e) == "type":
                LOGGER.warning("Variable '%s' is missing from the structured_config. %s is skipped.", str(e), self.__class__.__name__)
            else:
                LOGGER.warning("Variable '%s' is missing. Please validate the Loopback interfaces data model of this host.", str(e))
            return None

        return {self.anta_module: anta_tests}


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

        try:
            ethernet_interfaces = get(self.hostvars[self.device_name], "ethernet_interfaces", required=True)
        except AristaAvdMissingVariableError as e:
            LOGGER.warning("Variable '%s' is missing from the structured_config. %s is skipped.", str(e), self.__class__.__name__)
            return None

        required_vars = ["name", "shutdown", "peer", "peer_interface"]

        for ethernet_interface in ethernet_interfaces:
            try:
                for var in required_vars:
                    get(ethernet_interface, var, required=True)

                if (peer := ethernet_interface["peer"]) not in self.hostvars:
                    LOGGER.info("The structured_config is missing for peer %s.", peer)
                    continue

                custom_field = f"local: {ethernet_interface['name']} - remote: {peer}_{ethernet_interface['peer_interface']}"

                if (dns_domain := get(self.hostvars[peer], "dns_domain")) is not None:
                    peer = f"{peer}.{dns_domain}"

                anta_tests.append(
                    {
                        "VerifyLLDPNeighbors": {
                            "neighbors": [
                                {
                                    "port": str(ethernet_interface["name"]),
                                    "neighbor_device": str(peer),
                                    "neighbor_port": str(ethernet_interface["peer_interface"]),
                                }
                            ],
                            "result_overwrite": {"categories": self.categories, "description": self.description, "custom_field": custom_field},
                        }
                    }
                )
            except AristaAvdMissingVariableError as e:
                LOGGER.info("Variable '%s' is missing. Please validate the Ethernet interfaces data model of this host.", str(e))
                continue

        return {self.anta_module: anta_tests}
