# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import logging
from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.eos_validate_state_utils.avdtestbase import AvdTestBase
from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdMissingVariableError
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

        try:
            # To be removed once 'l3leaf' check is removed
            node_type = get(self.hostvars[self.device_name], "type", required=True)

            if node_type == "l3leaf":
                add_test(mapping=self.loopback0_mapping, description="Remote Lo0 address")

            if get(self.hostvars[self.device_name], "vxlan_interface.Vxlan1.vxlan.source_interface") is not None:
                add_test(mapping=self.vtep_mapping, description="Remote VTEP address")

        except AristaAvdMissingVariableError as e:
            LOGGER.warning("Variable '%s' is missing from the structured_config. %s is skipped.", str(e), self.__class__.__name__)
            return None

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

        try:
            get(self.hostvars[self.device_name], "router_bgp", required=True)
        except AristaAvdMissingVariableError as e:
            LOGGER.info("Variable '%s' is missing from the structured_config. %s is skipped.", str(e), self.__class__.__name__)
            return None

        try:
            service_routing_protocols_model = get(self.hostvars[self.device_name], "service_routing_protocols_model", required=True)
        except AristaAvdMissingVariableError as e:
            LOGGER.warning("Variable '%s' is missing from the structured_config. %s is skipped.", str(e), self.__class__.__name__)
            return None

        if service_routing_protocols_model != "multi-agent":
            LOGGER.warning("Variable 'service_routing_protocols_model' is NOT set to 'multi-agent'. %s is skipped.", self.__class__.__name__)
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
        bgp_neighbors = get(self.hostvars[self.device_name], "router_bgp.neighbors", [])

        for idx, bgp_neighbor in enumerate(bgp_neighbors, start=1):
            # TODO - this matches legacy eos_validate_state BUT works only for neighbors in peer groups...
            try:
                neighbor_peer_group = get_item(bgp_peer_groups, "name", bgp_neighbor["peer_group"], required=True, var_name=bgp_neighbor["peer_group"])
            except AristaAvdMissingVariableError as e:
                LOGGER.warning("Peer group '%s' dictionary is missing from the 'peer_groups' list of the 'router_bgp' data model.", str(e))
                continue

            try:
                bgp_neighbor_ip = str(get(bgp_neighbor, "ip_address", required=True))
            except AristaAvdMissingVariableError as e:
                LOGGER.warning("Neighbor entry #%d from the 'neighbors' list of the 'router_bgp' data model is missing the variable '%s'.", idx, str(e))
                continue

            try:
                neighbor_peer_group_type = get(neighbor_peer_group, "type", required=True)
            except AristaAvdMissingVariableError as e:
                LOGGER.warning(
                    "Peer group '%s' from the 'peer_groups' list of the 'router_bgp' data model is missing the variable '%s'.",
                    bgp_neighbor["peer_group"],
                    str(e),
                )
                continue

            if neighbor_peer_group_type == "ipv4":
                add_verify_peers_test(description="ip bgp peer state established (ipv4)", afi="ipv4", safi="unicast", bgp_neighbor_ip=bgp_neighbor_ip)
            elif neighbor_peer_group_type == "evpn":
                add_verify_peers_test(description="bgp evpn peer state established (evpn)", afi="evpn", bgp_neighbor_ip=bgp_neighbor_ip)

        return {self.anta_module: anta_tests} if anta_tests.get("bgp") else None
