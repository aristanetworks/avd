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

        required_vars = ["name", "peer", "peer_interface", "type"]

        for idx, ethernet_interface in enumerate(ethernet_interfaces, start=1):
            try:
                for var in required_vars:
                    get(ethernet_interface, var, required=True)
            except AristaAvdMissingVariableError as e:
                LOGGER.warning("Ethernet interface entry #%d from the 'ethernet_interfaces' data model is missing the variable '%s'.", idx, str(e))
                continue

            if (peer := ethernet_interface["peer"]) not in self.hostvars:
                LOGGER.info(
                    "Ethernet interface '%s' connected peer '%s' is not configured by AVD. 'VerifyReachability' is skipped for this interface",
                    ethernet_interface["name"],
                    peer,
                )
                continue

            # If is_deployed is missing from the peer structured_config by mistake, we set it to True
            if not get(self.hostvars[peer], "is_deployed", default=True):
                LOGGER.info(
                    "Ethernet interface '%s' connected peer '%s' is marked as not deployed. 'VerifyReachability' is skipped for this interface.",
                    ethernet_interface["name"],
                    peer,
                )
                continue

            try:
                peer_ethernet_interfaces = get(self.hostvars[peer], "ethernet_interfaces", required=True)
            except AristaAvdMissingVariableError as e:
                LOGGER.warning("Ethernet interface '%s' connected peer '%s' is missing the '%s' data model.", ethernet_interface["name"], peer, str(e))
                continue

            try:
                peer_ethernet_interface = get_item(
                    peer_ethernet_interfaces,
                    "name",
                    ethernet_interface["peer_interface"],
                    required=True,
                    var_name=ethernet_interface["peer_interface"],
                )
            except AristaAvdMissingVariableError as e:
                LOGGER.warning(
                    "Ethernet interface '%s' connected peer '%s' is missing interface '%s' from the 'ethernet_interfaces' data model.",
                    ethernet_interface["name"],
                    peer,
                    str(e),
                )
                continue

            try:
                peer_ethernet_interface_ip = get(peer_ethernet_interface, "ip_address", required=True)
            except AristaAvdMissingVariableError as e:
                LOGGER.warning(
                    "Ethernet interface '%s' connected peer '%s' is missing the variable '%s' from interface '%s'.",
                    ethernet_interface["name"],
                    peer,
                    str(e),
                    ethernet_interface["peer_interface"],
                )
                continue

            if ethernet_interface["type"] == "routed":
                try:
                    ethernet_interface_ip = get(ethernet_interface, "ip_address", required=True)
                except AristaAvdMissingVariableError as e:
                    LOGGER.warning("Ethernet interface '%s' is of type 'routed' but the variable '%s' is missing.", ethernet_interface["name"], str(e))
                    continue

                src_ip = str(ip_interface(ethernet_interface_ip).ip)
                dst_ip = str(ip_interface(peer_ethernet_interface_ip).ip)
                custom_field = f"Source: {self.device_name}_{ethernet_interface['name']} - Destination: {peer}_{ethernet_interface['peer_interface']}"
                anta_tests.append(
                    {
                        "VerifyReachability": {
                            "hosts": [{"source": src_ip, "destination": dst_ip, "vrf": "default", "repeat": 1}],
                            "result_overwrite": {"categories": self.categories, "description": self.description, "custom_field": custom_field},
                        }
                    }
                )

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
