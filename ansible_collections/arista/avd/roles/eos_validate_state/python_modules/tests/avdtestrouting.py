# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.eos_validate_state_utils.avdtestbase import AvdTestBase
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get


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

        if get(self.structured_config, "vxlan_interface.Vxlan1.vxlan.source_interface") is not None:
            add_test(mapping=self.vtep_mapping, description="Remote VTEP address")

        return {self.anta_module: anta_tests} if anta_tests else None


class AvdTestBGP(AvdTestBase):
    """AvdTestBGP class for BGP tests.

    Supports IPv4 and EVPN address families.
    """

    anta_module = "anta.tests.routing"
    categories = ["BGP"]
    anta_tests = {}

    def add_test(self, afi: str, bgp_neighbor_ip: str, safi: str | None = None) -> dict:
        """Add a BGP test definition with the proper input parameters."""
        custom_field = f"BGP {afi.upper() + ' ' + safi.capitalize() if safi else afi.upper()} Peer: {bgp_neighbor_ip}"
        address_family = {"afi": afi, "peers": [bgp_neighbor_ip]}
        if safi:
            address_family["safi"] = safi

        self.anta_tests.setdefault(f"{self.anta_module}.bgp", []).append(
            {
                "VerifyBGPSpecificPeers": {
                    "address_families": [address_family],
                    "result_overwrite": {"categories": self.categories, "custom_field": custom_field},
                },
            },
        )

    def create_tests(self, afi: str, safi: str | None = None) -> None:
        """Create BGP tests for the given AFI and SAFI."""
        bgp_neighbors = get(self.structured_config, "router_bgp.neighbors", [])

        # Retrieve peer groups and direct neighbors
        peer_groups = get(self.structured_config, f"router_bgp.address_family_{afi}.peer_groups", [])
        direct_neighbors = get(self.structured_config, f"router_bgp.address_family_{afi}.neighbors", [])

        # If `bgp default ipv4-unicast` is enabled, all addresses are IPv4 address family active unless explicitly deactivated
        condition = afi == "ipv4" and safi == "unicast" and get(self.structured_config, "router_bgp.bgp.default.ipv4_unicast", default=False)

        filtered_peer_groups = [peer_group["name"] for peer_group in peer_groups if peer_group.get("activate") != condition]
        filtered_neighbors = [neighbor["ip_address"] for neighbor in direct_neighbors if neighbor.get("activate") != condition]

        # Combine neighbors from peer groups and direct neighbors.
        # Depending on the condition, we either keep all the neighbors minus the explicitly deactivated ones, or we keep only the explicitly activated ones.
        all_neighbors = [
            (neighbor["ip_address"], neighbor.get("peer"))
            for neighbor in bgp_neighbors
            if (condition and neighbor.get("peer_group") not in filtered_peer_groups and neighbor["ip_address"] not in filtered_neighbors)
            or (not condition and (neighbor.get("peer_group") in filtered_peer_groups or neighbor["ip_address"] in filtered_neighbors))
        ]

        # Add tests for all neighbors
        for ip, peer in all_neighbors:
            # If peer key is present, check if peer is available
            if peer is not None and not self.is_peer_available(peer):
                continue
            self.add_test(afi=afi, safi=safi, bgp_neighbor_ip=str(ip))

    @cached_property
    def test_definition(self) -> dict | None:
        """Generates the proper ANTA test definition for all BGP tests.

        Returns
        -------
            test_definition (dict): ANTA test definition.

        """
        # Check if BGP configuration is present with ArBGP model
        if self.logged_get(key="router_bgp") is None or not self.validate_data(service_routing_protocols_model="multi-agent", logging_level="WARNING"):
            return None

        self.anta_tests.setdefault(f"{self.anta_module}.generic", []).append(
            {
                "VerifyRoutingProtocolModel": {
                    "model": "multi-agent",
                    "result_overwrite": {"categories": self.categories},
                },
            },
        )
        # Create tests for IPv4 and EVPN address families
        self.create_tests(afi="evpn")
        self.create_tests(afi="ipv4", safi="unicast")

        return self.anta_tests if self.anta_tests.get(f"{self.anta_module}.bgp") else None
