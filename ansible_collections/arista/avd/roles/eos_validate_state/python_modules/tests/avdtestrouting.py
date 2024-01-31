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

    Supports IPv4, IPv6 and EVPN address families.
    """

    anta_module = "anta.tests.routing"
    categories = ["BGP"]
    anta_tests = {}

    def add_test(self, afi: str, bgp_neighbor_ip: str, safi: str | None = None) -> dict:
        """Add a BGP test definition with the proper input parameters."""
        formatted_afi = "IPv4" if afi.lower() == "ipv4" else "IPv6" if afi.lower() == "ipv6" else afi.upper()
        formatted_safi = f" {safi.capitalize()}" if safi else ""
        custom_field = f"BGP {formatted_afi}{formatted_safi} Peer: {bgp_neighbor_ip}"

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

        # Retrieve peer groups and direct neighbors.
        peer_groups = get(self.structured_config, f"router_bgp.address_family_{afi}.peer_groups", [])
        direct_neighbors = get(self.structured_config, f"router_bgp.address_family_{afi}.neighbors", [])

        # Only explicitely activated neighbors and peer groups are tested.
        filtered_peer_groups = [peer_group["name"] for peer_group in peer_groups if peer_group.get("activate")]
        filtered_neighbors = [neighbor["ip_address"] for neighbor in direct_neighbors if neighbor.get("activate")]

        # Combine neighbors from peer groups and direct neighbors
        all_neighbors = [
            (neighbor["ip_address"], neighbor.get("peer"))
            for neighbor in bgp_neighbors
            if neighbor.get("peer_group") in filtered_peer_groups or neighbor["ip_address"] in filtered_neighbors
        ]

        # Add tests for all neighbors
        for ip, peer in all_neighbors:
            # Check peer availability if the 'peer' key exists. Otherwise, still include the test for potential BGP external peers.
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
        # Check if BGP configuration is present with multi-agent model
        if self.logged_get(key="router_bgp") is None or not self.validate_data(service_routing_protocols_model="multi-agent", logging_level="WARNING"):
            return None

        self.anta_tests.setdefault(f"{self.anta_module}.generic", []).append(
            {
                "VerifyRoutingProtocolModel": {
                    "model": "multi-agent",
                    # TODO @carl-baillargeon: Remove description and categories once we bump ANTA version.
                    "result_overwrite": {
                        "description": "Verifies the configured routing protocol model.",
                        "categories": self.categories,
                        "custom_field": "Routing protocol model: multi-agent",
                    },
                },
            },
        )
        # Create tests for IPv4, IPv6 and EVPN address families
        for afi, safi in [("evpn", None), ("ipv4", "unicast"), ("ipv6", "unicast")]:
            self.create_tests(afi=afi, safi=safi)

        return self.anta_tests if self.anta_tests.get(f"{self.anta_module}.bgp") else None
