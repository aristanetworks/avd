# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import logging
from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.eos_validate_state_utils.avdtestbase import AvdTestBase
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get, get_item

LOGGER = logging.getLogger(__name__)


class AvdTestRoutingTable(AvdTestBase):
    """
    AvdTestRoutingTable class for routing table entry verification tests.
    """

    anta_module = "anta.tests.routing.generic"
    categories = ["Routing Table"]

    @cached_property
    def test_definition(self) -> dict | None:
        """
        Generates the proper ANTA test definition for all routing table entry verification tests.

        Returns:
            test_definition (dict): ANTA test definition.
        """
        anta_tests = []

        def add_test(mapping: list, description: str) -> None:
            """
            Add a test with the proper parameters to the anta_tests list.

            Avoids duplicate tests for the same IP address (e.g. MLAG VTEPs).
            """

            processed_ips = set()

            for node, ip in mapping:
                if ip not in processed_ips:
                    anta_tests.append(
                        {
                            "VerifyRoutingTableEntry": {
                                "routes": [ip],
                                "result_overwrite": {"categories": self.categories, "description": description, "custom_field": f"{ip}"},
                            }
                        }
                    )
                    processed_ips.add(ip)

        if not hasattr(self, "loopback0_mapping") or not hasattr(self, "vtep_mapping"):
            LOGGER.info("'loopback0_mapping' or 'vtep_mapping' is not set. %s is skipped.", self.__class__.__name__)
            return None

        if (node_type := get(self.hostvars[self.device_name], "type")) is None:
            LOGGER.info("'type' is missing from structured_config. %s is skipped.", self.__class__.__name__)
            return None

        # TODO: Update loopback0_mapping to remove type `l3leaf`
        if node_type == "l3leaf":
            add_test(mapping=self.loopback0_mapping, description="Remote Lo0 address")

        if get(self.hostvars[self.device_name], "vxlan_interface.Vxlan1.vxlan.source_interface") is not None:
            add_test(mapping=self.vtep_mapping, description="Remote VTEP address")

        return {self.anta_module: anta_tests}


class AvdTestBGP(AvdTestBase):
    """
    AvdTestBGP class for BGP tests.
    """

    anta_module = "anta.tests.routing"
    categories = ["BGP"]

    @cached_property
    def test_definition(self) -> dict | None:
        """
        Generates the proper ANTA test definition for all BGP tests.

        Returns:
            test_definition (dict): ANTA test definition.

        """
        anta_tests = {}

        def add_verify_peers_test(description: str, afi: str, bgp_neighbor_ip: str, safi: str = None) -> None:
            """
            Add a test to BGP verify peers with the proper parameters to the anta_tests list.
            """
            custom_field = f"bgp_neighbor: {bgp_neighbor_ip}"
            address_family = {"afi": afi, "peers": [bgp_neighbor_ip]}
            if safi:
                address_family["safi"] = safi

            anta_tests.setdefault("bgp", []).append(
                {
                    "VerifyBGPSpecificPeers": {
                        "address_families": [address_family],
                        "result_overwrite": {"categories": self.categories, "description": description, "custom_field": custom_field},
                    }
                }
            )

        # Add Test to check service_routing_protocol_model
        if (
            service_routing_protocols_model := get(self.hostvars[self.device_name], "service_routing_protocols_model")
        ) is None or service_routing_protocols_model != "multi-agent":
            LOGGER.info(
                "'service_routing_protocols_model' is missing from structured_config or is NOT set to 'multi-agent'. %s is skipped.", self.__class__.__name__
            )
            return None

        anta_tests.setdefault("generic", []).append(
            {
                "VerifyRoutingProtocolModel": {
                    "model": "multi-agent",
                    "result_overwrite": {"categories": self.categories, "description": "ArBGP is configured and operating", "custom_field": "ArBGP"},
                }
            }
        )

        bgp_peer_groups = get(self.hostvars[self.device_name], "router_bgp.peer_groups", [])

        for bgp_neighbor in get(self.hostvars[self.device_name], "router_bgp.neighbors", []):
            # TOOO - this matches legacy eos_validate_state BUT works only for neighbors in peer-groups...
            if (neighbor_peer_group := get_item(bgp_peer_groups, "name", bgp_neighbor["peer_group"])) is not None:
                bgp_neighbor_ip = str(bgp_neighbor["ip_address"])
                if neighbor_peer_group["type"] == "ipv4":
                    add_verify_peers_test(description="ip bgp peer state established (ipv4)", afi="ipv4", safi="unicast", bgp_neighbor_ip=bgp_neighbor_ip)
                elif neighbor_peer_group["type"] == "evpn":
                    add_verify_peers_test(description="bgp evpn peer state established (evpn)", afi="evpn", bgp_neighbor_ip=bgp_neighbor_ip)
        return {self.anta_module: anta_tests}
