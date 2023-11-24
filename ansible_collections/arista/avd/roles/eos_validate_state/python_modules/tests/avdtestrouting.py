# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.eos_validate_state_utils.avdtestbase import AvdTestBase
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get, get_item


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

            for peer, ip in mapping:
                if not self.is_peer_available(peer):
                    continue

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

        if not self.validate_data(type="l3leaf"):
            return None

        add_test(mapping=self.loopback0_mapping, description="Remote Lo0 address")

        if get(self.hostvars[self.device_name], "vxlan_interface.Vxlan1.vxlan.source_interface") is not None:
            add_test(mapping=self.vtep_mapping, description="Remote VTEP address")

        return {self.anta_module: anta_tests} if anta_tests else None


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

        def add_test(description: str, afi: str, bgp_neighbor_ip: str, safi: str = None) -> None:
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

        if self.logged_get(key="router_bgp", logging_level="INFO") is None or not self.validate_data(
            service_routing_protocols_model="multi-agent", logging_level="WARNING"
        ):
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

        for idx, bgp_neighbor in enumerate(bgp_neighbors):
            # TODO - this matches legacy eos_validate_state BUT works only for neighbors in peer groups...
            if not self.validate_data(data=bgp_neighbor, data_path=f"router_bgp.neighbors.[{idx}]", required_keys=["ip_address", "peer_group", "peer"]):
                continue

            if not self.is_peer_available(bgp_neighbor["peer"]):
                continue

            if (neighbor_peer_group := get_item(bgp_peer_groups, "name", bgp_neighbor["peer_group"])) is None:
                self.log_skip_message(message=f"Peer group '{bgp_neighbor['peer_group']}' not found.", logging_level="WARNING")
                continue

            if not self.validate_data(data=neighbor_peer_group, data_path=f"router_bgp.peer_groups.{neighbor_peer_group['name']}", required_keys="type"):
                continue

            if neighbor_peer_group["type"] == "ipv4":
                add_test(description="ip bgp peer state established (ipv4)", afi="ipv4", safi="unicast", bgp_neighbor_ip=str(bgp_neighbor["ip_address"]))
            elif neighbor_peer_group["type"] == "evpn":
                add_test(description="bgp evpn peer state established (evpn)", afi="evpn", bgp_neighbor_ip=str(bgp_neighbor["ip_address"]))

        return {self.anta_module: anta_tests} if anta_tests.get("bgp") else None
