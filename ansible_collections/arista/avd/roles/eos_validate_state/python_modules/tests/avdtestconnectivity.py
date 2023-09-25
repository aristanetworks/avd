# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import logging
from functools import cached_property
from ipaddress import ip_interface

from ansible_collections.arista.avd.plugins.plugin_utils.eos_validate_state_utils.avdtestbase import AvdTestBase
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

        if (ethernet_interfaces := get(self.hostvars[self.device_name], "ethernet_interfaces")) is None:
            LOGGER.error("'ethernet_interfaces' is missing from structured_config. %s is skipped.", self.__class__.__name__)
            return None

        for ethernet_interface in ethernet_interfaces:
            if (
                ethernet_interface.get("type") == "routed"
                and (interface_ip := ethernet_interface.get("ip_address")) is not None
                and (peer_name := ethernet_interface.get("peer")) is not None
                and (peer_interface_name := ethernet_interface.get("peer_interface")) is not None
            ):
                if (peer_ethernet_interfaces := get(self.hostvars, f"{peer_name}..ethernet_interfaces", separator="..")) is None:
                    LOGGER.info("'ethernet_interfaces' is missing from peer %s structured_config.", peer_name)
                    continue

                if (peer_interface := get_item(peer_ethernet_interfaces, "name", peer_interface_name)) is None:
                    LOGGER.info("'ethernet interface %s' is missing from peer %s structured_config.", peer_interface_name, peer_name)
                    continue

                if (peer_interface_ip := get(peer_interface, "ip_address")) is None:
                    LOGGER.info("'ethernet interface %s' is missing an 'ip_address' in peer %s structured_config.", peer_interface_name, peer_name)
                    continue

                src_ip = str(ip_interface(interface_ip).ip)
                dst_ip = str(ip_interface(peer_interface_ip).ip)
                custom_field = f"Source: {self.device_name}_{ethernet_interface['name']} - Destination: {peer_name}_{peer_interface_name}"
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

        if (management_interfaces := get(self.hostvars[self.device_name], "management_interfaces")) is None:
            LOGGER.info("'management_interfaces' is missing from structured_config. %s is skipped.", self.__class__.__name__)
            return None

        if not hasattr(self, "loopback0_mapping"):
            LOGGER.info("'loopback0_mapping' is not set. %s is skipped.", self.__class__.__name__)
            return None

        for management_interface in management_interfaces:
            if management_interface["type"] == "inband":
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

        if not hasattr(self, "loopback0_mapping"):
            LOGGER.info("'loopback0_mapping' is not set. %s is skipped.", self.__class__.__name__)
            return None

        # To be removed once 'l3leaf' check is removed
        if (node_type := get(self.hostvars[self.device_name], "type")) is None:
            LOGGER.error("'type' is missing from structured_config. %s is skipped.", self.__class__.__name__)
            return None

        # TODO: Update loopback0_mapping to remove type `l3leaf`
        if node_type == "l3leaf":
            if (loopback_interfaces := get(self.hostvars[self.device_name], "loopback_interfaces")) is None:
                # TODO - logging
                return None
            if (loopback0 := get_item(loopback_interfaces, "name", "Loopback0")) is None:
                # TODO - logging
                return None
            if (src_ip := get(loopback0, "ip_address")) is None:
                # TODO - logging
                return None

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

        if (ethernet_interfaces := get(self.hostvars[self.device_name], "ethernet_interfaces")) is None:
            LOGGER.info("'ethernet_interfaces' is missing from structured_config. %s is skipped.", self.__class__.name)
            return None

        for ethernet_interface in ethernet_interfaces:
            name = get(ethernet_interface, "name")

            if ethernet_interface.get("shutdown"):
                continue

            if (peer := get(ethernet_interface, "peer")) is None or (peer_interface := get(ethernet_interface, "peer_interface")) is None:
                LOGGER.info("'peer' or 'peer_interface' is missing from %s structured_config.", name)
                continue

            if peer not in self.hostvars:
                LOGGER.info("structured_config is missing for peer %s", peer)
                continue

            custom_field = f"local: {name} - remote: {peer}_{peer_interface}"

            if (dns_domain := get(self.hostvars[peer], "dns_domain")) is not None:
                peer = f"{peer}.{dns_domain}"

            anta_tests.append(
                {
                    "VerifyLLDPNeighbors": {
                        "neighbors": [{"port": str(name), "neighbor_device": str(peer), "neighbor_port": str(peer_interface)}],
                        "result_overwrite": {"categories": self.categories, "description": self.description, "custom_field": custom_field},
                    }
                }
            )

        return {self.anta_module: anta_tests}
