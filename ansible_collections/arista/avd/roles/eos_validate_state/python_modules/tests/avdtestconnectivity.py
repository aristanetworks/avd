# Copyright (c) 2023-2024 Arista Networks, Inc.
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

    @cached_property
    def test_definition(self) -> dict | None:
        """
        Generates the proper ANTA test definition for all fabric P2P IP reachability tests.

        Returns:
            test_definition (dict): ANTA test definition.
        """
        anta_tests = []

        if (ethernet_interfaces := self.structured_config.get("ethernet_interfaces")) is None:
            LOGGER.warning("No ethernet interfaces found. %s is skipped.", self.__class__.__name__)
            return None

        required_keys = ["name", "peer", "peer_interface", "ip_address"]

        for idx, interface in enumerate(ethernet_interfaces):
            self.update_interface_shutdown(interface)
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
            custom_field = f"Source: P2P Interface {interface['name']} (IP: {src_ip}) - Destination: {peer} {interface['peer_interface']} (IP: {dst_ip})"
            anta_tests.append(
                {
                    "VerifyReachability": {
                        "hosts": [{"source": src_ip, "destination": dst_ip, "vrf": "default", "repeat": 1}],
                        "result_overwrite": {"custom_field": custom_field},
                    }
                }
            )

        return {self.anta_module: anta_tests} if anta_tests else None


class AvdTestInbandReachability(AvdTestBase):
    """
    AvdTestInbandReachability class for inband management reachability tests.
    """

    anta_module = "anta.tests.connectivity"

    @cached_property
    def test_definition(self) -> dict | None:
        """
        Generates the proper ANTA test definition for all inband management reachability tests.

        Returns:
            test_definition (dict): ANTA test definition.
        """
        anta_tests = []

        if (vlan_interfaces := self.structured_config.get("vlan_interfaces")) is None:
            LOGGER.info("No vlan interfaces found. %s is skipped.", self.__class__.__name__)
            return None

        required_keys = ["name", "ip_address"]

        for idx, interface in enumerate(vlan_interfaces):
            self.update_interface_shutdown(interface)
            if not self.validate_data(data=interface, data_path=f"vlan_interfaces.[{idx}]", required_keys=required_keys, type="inband_mgmt", shutdown=False):
                continue

            vrf = interface.get("vrf", "default")

            src_ip = str(ip_interface(interface["ip_address"]).ip)

            for dst_node, dst_ip in self.loopback0_mapping:
                if not self.is_peer_available(dst_node):
                    continue

                custom_field = f"Source: Inband MGMT SVI {interface['name']} (IP: {src_ip}) - Destination: {dst_node} Loopback0 (IP: {dst_ip})"
                anta_tests.append(
                    {
                        "VerifyReachability": {
                            "hosts": [{"source": src_ip, "destination": dst_ip, "vrf": vrf, "repeat": 1}],
                            "result_overwrite": {"custom_field": custom_field},
                        }
                    }
                )

        return {self.anta_module: anta_tests} if anta_tests else None


class AvdTestLoopback0Reachability(AvdTestBase):
    """
    AvdTestLoopback0Reachability class for Loopback0 reachability tests.
    """

    anta_module = "anta.tests.connectivity"

    @cached_property
    def test_definition(self) -> dict | None:
        """
        Generates the proper ANTA test definition for all Loopback0 reachability tests.

        Returns:
            test_definition (dict): ANTA test definition.

        """
        anta_tests = []

        # Skip the test if the host is not a VTEP (no VXLAN interface)
        if get(self.structured_config, "vxlan_interface") is None:
            LOGGER.info("Host is not a VTEP since it doesn't have a VXLAN interface. %s is skipped.", self.__class__.__name__)
            return None

        # TODO: For now, we exclude WAN VTEPs from testing
        if "Dps" in get(self.structured_config, "vxlan_interface.Vxlan1.vxlan.source_interface"):
            LOGGER.info("Host is a VTEP with a DPS source interface for VXLAN. For now, WAN VTEPs are excluded. %s is skipped.", self.__class__.__name__)
            return None

        if (loopback0_ip := self.get_interface_ip(interface_model="loopback_interfaces", interface_name="Loopback0")) is None:
            return None

        src_ip = str(ip_interface(loopback0_ip).ip)

        for dst_node, dst_ip in self.loopback0_mapping:
            if not self.is_peer_available(dst_node):
                continue

            custom_field = f"Source: Loopback0 (IP: {src_ip}) - Destination: {dst_node} Loopback0 (IP: {dst_ip})"
            anta_tests.append(
                {
                    "VerifyReachability": {
                        "hosts": [{"source": src_ip, "destination": dst_ip, "vrf": "default", "repeat": 1}],
                        "result_overwrite": {"custom_field": custom_field},
                    }
                }
            )

        return {self.anta_module: anta_tests} if anta_tests else None


class AvdTestLLDPTopology(AvdTestBase):
    """
    AvdTestLLDPTopology class for the LLDP topology tests.
    """

    anta_module = "anta.tests.connectivity"

    @cached_property
    def test_definition(self) -> dict | None:
        """
        Generates the proper ANTA test definition for all LLDP topology tests.

        Returns:
            test_definition (dict): ANTA test definition.

        """
        anta_tests = []

        if (ethernet_interfaces := self.structured_config.get("ethernet_interfaces")) is None:
            LOGGER.warning("No ethernet interfaces found. %s is skipped.", self.__class__.__name__)
            return None

        required_keys = ["name", "peer", "peer_interface"]

        for idx, interface in enumerate(ethernet_interfaces):
            if self.is_subinterface(interface):
                LOGGER.info("Interface '%s' is a subinterface. %s is skipped.", interface["name"], self.__class__.__name__)
                continue

            self.update_interface_shutdown(interface)
            if not self.validate_data(data=interface, data_path=f"ethernet_interfaces.[{idx}]", required_keys=required_keys, shutdown=False):
                continue

            if not self.is_peer_available(peer := interface["peer"]):
                continue

            custom_field = f"Local: {interface['name']} - Remote: {peer} {interface['peer_interface']}"

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
                        "result_overwrite": {"custom_field": custom_field},
                    }
                }
            )

        return {self.anta_module: anta_tests} if anta_tests else None
