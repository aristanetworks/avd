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


class AvdTestBaseReachability(AvdTestBase):
    """
    Base class for common reachability test functionalities.
    """

    def is_vtep(self) -> bool:
        """Check if the host is a VTEP by verifying the presence of a VXLAN interface."""
        return get(self.structured_config, "vxlan_interface") is not None

    def is_wan_vtep(self) -> bool:
        """Check if the host is a WAN VTEP by verifying the DPS source interface."""
        return "Dps" in get(self.structured_config, "vxlan_interface.Vxlan1.vxlan.source_interface", "")

    def create_reachability_tests(
        self, custom_msg: str, src_ip: str, mapping: list[tuple[str, str]], vrf: str = "default", dst_interface: str = "Loopback0"
    ) -> list[dict]:
        """Create reachability tests for a given interface type and source IP."""
        src_ip_str = str(ip_interface(src_ip).ip)
        return [
            {
                "VerifyReachability": {
                    "hosts": [{"source": src_ip_str, "destination": dst_ip, "vrf": vrf, "repeat": 1}],
                    "result_overwrite": {"custom_field": f"{custom_msg} (IP: {src_ip}) - Destination: {dst_node} {dst_interface} (IP: {dst_ip})"},
                }
            }
            for dst_node, dst_ip in mapping
            if self.is_peer_available(dst_node)
        ]


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


class AvdTestInbandReachability(AvdTestBaseReachability):
    """
    AvdTestInbandReachability class for inband management reachability tests.
    """

    anta_module = "anta.tests.connectivity"

    @cached_property
    def test_definition(self) -> dict | None:
        """
        Generates the proper ANTA test definition for all inband management reachability tests.

        Returns:
            dict | None: ANTA test definition if there are tests to run, otherwise None.
        """
        vlan_interfaces = self.structured_config.get("vlan_interfaces")
        if vlan_interfaces is None:
            LOGGER.info("No vlan interfaces found. %s is skipped.", self.__class__.__name__)
            return None

        required_keys = ["name", "ip_address"]
        anta_tests = []

        for idx, interface in enumerate(vlan_interfaces):
            self.update_interface_shutdown(interface)
            if not self.validate_data(data=interface, data_path=f"vlan_interfaces.[{idx}]", required_keys=required_keys, type="inband_mgmt", shutdown=False):
                continue

            vrf = interface.get("vrf", "default")
            src_ip = str(ip_interface(interface["ip_address"]).ip)
            custom_msg = f"Source: Inband MGMT SVI {interface['name']}"
            anta_tests.extend(self.create_reachability_tests(custom_msg, src_ip, self.loopback0_mapping, vrf=vrf))

        return {self.anta_module: anta_tests} if anta_tests else None


class AvdTestLoopback0Reachability(AvdTestBaseReachability):
    """
    AvdTestLoopback0Reachability class for Loopback0 reachability tests.
    """

    anta_module = "anta.tests.connectivity"

    @cached_property
    def test_definition(self) -> dict | None:
        """
        Generates the proper ANTA test definition for all Loopback0 reachability tests.

        Returns:
            dict | None: ANTA test definition if there are tests to run, otherwise None.
        """
        if not self.is_vtep():
            LOGGER.info("Host is not a VTEP since it doesn't have a VXLAN interface. %s is skipped.", self.__class__.__name__)
            return None

        loopback0_ip = self.get_interface_ip("loopback_interfaces", "Loopback0")
        if not loopback0_ip:
            return None
        src_ip = str(ip_interface(loopback0_ip).ip)

        custom_msg = "Source: Loopback0"
        anta_tests = self.create_reachability_tests(custom_msg, src_ip, self.loopback0_mapping)
        return {self.anta_module: anta_tests} if anta_tests else None


class AvdTestDpsReachability(AvdTestBaseReachability):
    """
    AvdTestDpsReachability class for DPS reachability tests.
    """

    anta_module = "anta.tests.connectivity"

    @cached_property
    def test_definition(self) -> dict | None:
        """
        Generates the proper ANTA test definition for all DPS reachability tests.

        Returns:
            dict | None: ANTA test definition if there are tests to run, otherwise None.
        """
        if not self.is_vtep():
            LOGGER.info("Host is not a VTEP since it doesn't have a VXLAN interface. %s is skipped.", self.__class__.__name__)
            return None

        if not self.is_wan_vtep():
            LOGGER.info("Host is not a WAN VTEP. %s is skipped.", self.__class__.__name__)
            return None

        dps_source_interface = get(self.structured_config, "vxlan_interface.Vxlan1.vxlan.source_interface")
        dps_ip = self.get_interface_ip("dps_interfaces", dps_source_interface)
        if not dps_ip:
            return None
        custom_msg = f"Source: {dps_source_interface}"
        anta_tests = self.create_reachability_tests(custom_msg, dps_ip, self.dps_mapping, dst_interface=dps_source_interface)
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
