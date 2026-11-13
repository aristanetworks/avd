# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""
Unit tests for FabricDocumentationFacts class.

These tests validate the changes made to use avd_facts as the authoritative source
for bgp_as and router_id fields, and the addition of isis_node_sid_ipv6_index.
"""

from __future__ import annotations

from copy import deepcopy
from typing import TYPE_CHECKING
from unittest.mock import MagicMock

import pytest

from pyavd._eos_designs.fabric_documentation_facts import FabricDocumentationFacts

if TYPE_CHECKING:
    from pyavd._eos_designs.eos_designs_facts.schema import EosDesignsFacts


class TestFabricDocumentationFacts:
    """Test suite for FabricDocumentationFacts."""

    @pytest.fixture
    def mock_avd_facts(self) -> dict[str, EosDesignsFacts]:
        """Create mock AVD facts for testing."""
        # Create mock for host1
        host1_facts = MagicMock()
        host1_facts.type = "l3leaf"
        host1_facts.pod = "POD1"
        host1_facts.mgmt_ip = "192.168.1.1"
        host1_facts.platform = "cEOS"
        host1_facts.is_deployed = True
        host1_facts.serial_number = "SN12345"
        host1_facts.inband_mgmt_ip = None
        host1_facts.inband_mgmt_interface = None
        host1_facts.bgp_as = "65001"  # Using avd_facts as authoritative source
        host1_facts.router_id = "10.255.0.1"  # Using avd_facts as authoritative source

        # Create mock for host2 (MPLS route reflector)
        host2_facts = MagicMock()
        host2_facts.type = "p"
        host2_facts.pod = "POD1"
        host2_facts.mgmt_ip = "192.168.1.2"
        host2_facts.platform = "cEOS"
        host2_facts.is_deployed = True
        host2_facts.serial_number = "SN12346"
        host2_facts.inband_mgmt_ip = None
        host2_facts.inband_mgmt_interface = None
        host2_facts.bgp_as = "65000"
        host2_facts.router_id = "10.255.0.2"

        return {"host1": host1_facts, "host2": host2_facts}

    @pytest.fixture
    def mock_structured_configs(self) -> dict[str, dict]:
        """Create mock structured configs for testing."""
        return {
            "host1": {
                "loopback_interfaces": [
                    {
                        "name": "Loopback0",
                        "ip_address": "10.255.0.1/32",
                        "node_segment": {
                            "ipv4_index": 1,
                            "ipv6_index": 101,  # Testing ISIS node-SID IPv6
                        },
                    }
                ],
                "router_isis": {
                    "net": "49.0001.0100.2550.0001.00",
                    "segment_routing_mpls": {"enabled": True},
                },
                "mpls": {"ldp": {"router_id": "10.255.0.1", "shutdown": False}},
                "router_bgp": {
                    "as": "99901",  # Deliberately different from avd_facts to prove we use the right source
                    "router_id": "99.99.0.1",  # Deliberately different from avd_facts to prove we use the right source
                    "address_family_vpn_ipv4": {"peer_groups": [{"name": "MPLS-OVERLAY-PEERS", "activate": True}]},
                },
            },
            "host2": {
                "loopback_interfaces": [
                    {
                        "name": "Loopback0",
                        "ip_address": "10.255.0.2/32",
                        "node_segment": {
                            "ipv4_index": 2,
                            "ipv6_index": 102,
                        },
                    }
                ],
                "router_isis": {
                    "net": "49.0001.0100.2550.0002.00",
                    "segment_routing_mpls": {"enabled": True},
                },
                "mpls": {"ldp": {"router_id": "10.255.0.2", "shutdown": False}},
                "router_bgp": {
                    "as": "99900",  # Deliberately different from avd_facts to prove we use the right source
                    "router_id": "99.99.0.2",  # Deliberately different from avd_facts to prove we use the right source
                    "bgp_cluster_id": "10.255.0.2",  # Testing correct field path
                    "peer_groups": [
                        {
                            "name": "MPLS-OVERLAY-PEERS",
                            "route_reflector_client": True,
                            "metadata": {"type": "mpls"},
                        }
                    ],
                    "address_family_vpn_ipv4": {"peer_groups": [{"name": "MPLS-OVERLAY-PEERS", "activate": True}]},
                },
            },
        }

    @pytest.fixture
    def fabric_doc_facts(self, mock_avd_facts: dict[str, EosDesignsFacts], mock_structured_configs: dict[str, dict]) -> FabricDocumentationFacts:
        """Create FabricDocumentationFacts instance for testing."""
        return FabricDocumentationFacts(
            avd_facts=mock_avd_facts,
            structured_configs=mock_structured_configs,
            fabric_name="TEST_FABRIC",
            include_connected_endpoints=False,
            toc=True,
        )

    def test_fabric_switches_uses_avd_facts_bgp_as(self, fabric_doc_facts: FabricDocumentationFacts) -> None:
        """Test that fabric_switches uses avd_facts.bgp_as instead of structured_config."""
        fabric_switches = fabric_doc_facts.fabric_switches

        # Verify bgp_as comes from avd_facts
        host1_switch = next(s for s in fabric_switches if s["node"] == "host1")
        assert host1_switch["bgp_as"] == "65001", "Should use avd_facts[hostname].bgp_as"

        host2_switch = next(s for s in fabric_switches if s["node"] == "host2")
        assert host2_switch["bgp_as"] == "65000", "Should use avd_facts[hostname].bgp_as"

    def test_fabric_switches_uses_avd_facts_router_id(self, fabric_doc_facts: FabricDocumentationFacts) -> None:
        """Test that fabric_switches uses avd_facts.router_id instead of structured_config."""
        fabric_switches = fabric_doc_facts.fabric_switches

        # Verify router_id comes from avd_facts
        host1_switch = next(s for s in fabric_switches if s["node"] == "host1")
        assert host1_switch["router_id"] == "10.255.0.1", "Should use avd_facts[hostname].router_id"

        host2_switch = next(s for s in fabric_switches if s["node"] == "host2")
        assert host2_switch["router_id"] == "10.255.0.2", "Should use avd_facts[hostname].router_id"

    def test_fabric_switches_has_isis_node_sid_ipv6_index(self, fabric_doc_facts: FabricDocumentationFacts) -> None:
        """Test that fabric_switches includes isis_node_sid_ipv6_index field."""
        fabric_switches = fabric_doc_facts.fabric_switches

        # Verify isis_node_sid_ipv6_index is present
        host1_switch = next(s for s in fabric_switches if s["node"] == "host1")
        assert "isis_node_sid_ipv6_index" in host1_switch, "Should include isis_node_sid_ipv6_index field"
        assert host1_switch["isis_node_sid_ipv6_index"] == 101, "Should extract IPv6 node-SID index from loopback"

        host2_switch = next(s for s in fabric_switches if s["node"] == "host2")
        assert host2_switch["isis_node_sid_ipv6_index"] == 102, "Should extract IPv6 node-SID index from loopback"

    def test_fabric_switches_has_isis_node_sid_ipv4_index(self, fabric_doc_facts: FabricDocumentationFacts) -> None:
        """Test that fabric_switches includes isis_node_sid_ipv4_index field (renamed from node_sid_ipv4_index)."""
        fabric_switches = fabric_doc_facts.fabric_switches

        # Verify isis_node_sid_ipv4_index is present (not the old node_sid_ipv4_index)
        host1_switch = next(s for s in fabric_switches if s["node"] == "host1")
        assert "isis_node_sid_ipv4_index" in host1_switch, "Should include isis_node_sid_ipv4_index field"
        assert "node_sid_ipv4_index" not in host1_switch, "Should NOT include old node_sid_ipv4_index field"
        assert host1_switch["isis_node_sid_ipv4_index"] == 1, "Should extract IPv4 node-SID index from loopback"

    def test_mpls_overlay_nodes_uses_avd_facts(self, fabric_doc_facts: FabricDocumentationFacts) -> None:
        """Test that mpls_overlay_nodes uses avd_facts for bgp_as and router_id."""
        overlay_nodes = fabric_doc_facts.mpls_overlay_nodes

        # Both hosts have VPN-IPv4 address family, so both should be in the list
        assert len(overlay_nodes) == 2, "Both hosts have MPLS overlay configured"

        host1_node = next(n for n in overlay_nodes if n["node"] == "host1")
        assert host1_node["bgp_as"] == "65001", "Should use avd_facts[hostname].bgp_as"
        assert host1_node["router_id"] == "10.255.0.1", "Should use avd_facts[hostname].router_id"
        assert host1_node["address_families"] == "vpn-ipv4", "Should detect VPN-IPv4 address family"

        host2_node = next(n for n in overlay_nodes if n["node"] == "host2")
        assert host2_node["bgp_as"] == "65000", "Should use avd_facts[hostname].bgp_as"
        assert host2_node["router_id"] == "10.255.0.2", "Should use avd_facts[hostname].router_id"

    def test_mpls_route_reflectors_uses_avd_facts(self, fabric_doc_facts: FabricDocumentationFacts) -> None:
        """Test that mpls_route_reflectors uses avd_facts for bgp_as and router_id."""
        rr_nodes = fabric_doc_facts.mpls_route_reflectors

        # Only host2 is configured as route reflector
        assert len(rr_nodes) == 1, "Only host2 has route reflector client configured"

        host2_rr = rr_nodes[0]
        assert host2_rr["node"] == "host2"
        assert host2_rr["bgp_as"] == "65000", "Should use avd_facts[hostname].bgp_as"
        assert host2_rr["router_id"] == "10.255.0.2", "Should use avd_facts[hostname].router_id"
        assert host2_rr["cluster_id"] == "10.255.0.2", "Should use bgp_cluster_id (not bgp.cluster_id)"

    def test_mpls_route_reflectors_correct_cluster_id_field(self, fabric_doc_facts: FabricDocumentationFacts) -> None:
        """Test that mpls_route_reflectors uses correct field path for cluster_id (bgp_cluster_id not bgp.cluster_id)."""
        rr_nodes = fabric_doc_facts.mpls_route_reflectors

        host2_rr = rr_nodes[0]
        # The bug was using "bgp.cluster_id" instead of "bgp_cluster_id"
        # This test verifies the fix by checking we get the actual value, not "-"
        assert host2_rr["cluster_id"] == "10.255.0.2", "Should correctly read from bgp_cluster_id field"
        assert host2_rr["cluster_id"] != "-", "Should NOT be default value if bgp_cluster_id is configured"

    def test_has_isis_sr_property(self, fabric_doc_facts: FabricDocumentationFacts) -> None:
        """Test that has_isis_sr correctly identifies ISIS SR configuration."""
        assert fabric_doc_facts.has_isis_sr is True, "Should detect ISIS SR is enabled on fabric switches"

    def test_has_mpls_property(self, fabric_doc_facts: FabricDocumentationFacts) -> None:
        """Test that has_mpls correctly identifies MPLS/LDP configuration."""
        assert fabric_doc_facts.has_mpls is True, "Should detect MPLS/LDP is enabled on fabric switches"

    def test_has_mpls_overlay_property(self, fabric_doc_facts: FabricDocumentationFacts) -> None:
        """Test that has_mpls_overlay correctly identifies MPLS overlay configuration."""
        assert fabric_doc_facts.has_mpls_overlay is True, "Should detect MPLS overlay BGP is configured"

    def test_has_mpls_route_reflectors_property(self, fabric_doc_facts: FabricDocumentationFacts) -> None:
        """Test that has_mpls_route_reflectors correctly identifies MPLS route reflectors."""
        assert fabric_doc_facts.has_mpls_route_reflectors is True, "Should detect MPLS route reflectors are configured"


class TestFabricDocumentationFactsEdgeCases:
    """Test edge cases and None handling."""

    def test_avd_facts_bgp_as_none_handling(self) -> None:
        """Test that None bgp_as from avd_facts is handled with 'or' operator."""
        mock_facts = MagicMock()
        mock_facts.type = "l3leaf"
        mock_facts.pod = "POD1"
        mock_facts.mgmt_ip = "192.168.1.1"
        mock_facts.platform = "cEOS"
        mock_facts.is_deployed = True
        mock_facts.serial_number = "SN123"
        mock_facts.inband_mgmt_ip = None
        mock_facts.inband_mgmt_interface = None
        mock_facts.bgp_as = None  # Testing None handling
        mock_facts.router_id = "10.255.0.1"

        structured_config = {
            "loopback_interfaces": [],
            "router_bgp": {"address_family_vpn_ipv4": {"peer_groups": []}},
        }

        fabric_facts = FabricDocumentationFacts(
            avd_facts={"host1": mock_facts},
            structured_configs={"host1": structured_config},
            fabric_name="TEST",
            include_connected_endpoints=False,
            toc=True,
        )

        # Test that overlay_nodes handles None bgp_as correctly
        overlay_nodes = fabric_facts.mpls_overlay_nodes
        if overlay_nodes:
            assert overlay_nodes[0]["bgp_as"] == "-", "None bgp_as should be rendered as '-'"

    def test_avd_facts_router_id_none_handling(self) -> None:
        """Test that None router_id from avd_facts is handled with 'or' operator."""
        mock_facts = MagicMock()
        mock_facts.type = "l3leaf"
        mock_facts.pod = "POD1"
        mock_facts.mgmt_ip = "192.168.1.1"
        mock_facts.platform = "cEOS"
        mock_facts.is_deployed = True
        mock_facts.serial_number = "SN123"
        mock_facts.inband_mgmt_ip = None
        mock_facts.inband_mgmt_interface = None
        mock_facts.bgp_as = "65001"
        mock_facts.router_id = None  # Testing None handling

        structured_config = {
            "loopback_interfaces": [],
            "router_bgp": {"address_family_vpn_ipv4": {"peer_groups": []}},
        }

        fabric_facts = FabricDocumentationFacts(
            avd_facts={"host1": mock_facts},
            structured_configs={"host1": structured_config},
            fabric_name="TEST",
            include_connected_endpoints=False,
            toc=True,
        )

        # Test that overlay_nodes handles None router_id correctly
        overlay_nodes = fabric_facts.mpls_overlay_nodes
        if overlay_nodes:
            assert overlay_nodes[0]["router_id"] == "-", "None router_id should be rendered as '-'"


@pytest.mark.parametrize("changed_field", [None, "rd", "import", "export", "import_address_family", "export_address_family"])
def test_vrf_summary_preserves_node_differences(changed_field: str | None) -> None:
    """Only combine VRFs whose displayed RD and route targets match across nodes."""
    vrf = {
        "name": "BLUE",
        "rd": "192.0.2.1:10",
        "route_targets": {
            "import": [
                {"address_family": "vpn-ipv4", "route_targets": ["65000:20", "65000:10"]},
                {"address_family": "vpn-ipv6", "route_targets": ["65000:10"]},
            ],
            "export": [{"address_family": "vpn-ipv4", "route_targets": ["65000:10"]}],
        },
    }
    other_vrf = deepcopy(vrf)
    other_vrf["rd"] = "192.0.2.2:10"
    if changed_field == "rd":
        other_vrf["rd"] = "192.0.2.2:11"
    elif changed_field in ("import", "export"):
        other_vrf["route_targets"][changed_field][0]["route_targets"].append("65000:30")
    elif changed_field in ("import_address_family", "export_address_family"):
        other_vrf["route_targets"][changed_field.removesuffix("_address_family")][0]["address_family"] = "vpn-ipv6"
        if changed_field == "import_address_family":
            other_vrf["route_targets"]["import"][1]["address_family"] = "vpn-ipv4"

    facts = FabricDocumentationFacts(
        avd_facts={},
        structured_configs={
            "node10": {"router_bgp": {"vrfs": [vrf]}},
            "node2": {"router_bgp": {"vrfs": [other_vrf]}},
            "node1": {"router_bgp": {"vrfs": [vrf]}},
        },
        fabric_name="TEST",
        include_connected_endpoints=False,
        toc=False,
    )
    entry = {
        "vrf": "BLUE",
        "rd_pattern": "10",
        "import_rt": "vpn-ipv4 65000:10, vpn-ipv4 65000:20, vpn-ipv6 65000:10",
        "export_rt": "vpn-ipv4 65000:10",
        "nodes": "node1, node2, node10",
    }
    if changed_field is None:
        assert facts.vrf_summary == [entry]
        return

    entry["nodes"] = "node1, node10"
    other_entry = dict(entry, nodes="node2")
    if changed_field == "rd":
        other_entry["rd_pattern"] = "11"
    elif changed_field == "import":
        other_entry["import_rt"] = "vpn-ipv4 65000:10, vpn-ipv4 65000:20, vpn-ipv4 65000:30, vpn-ipv6 65000:10"
    elif changed_field == "export":
        other_entry["export_rt"] = "vpn-ipv4 65000:10, vpn-ipv4 65000:30"
    elif changed_field == "import_address_family":
        other_entry["import_rt"] = "vpn-ipv4 65000:10, vpn-ipv6 65000:10, vpn-ipv6 65000:20"
    elif changed_field == "export_address_family":
        other_entry["export_rt"] = "vpn-ipv6 65000:10"
    assert facts.vrf_summary == [entry, other_entry]


@pytest.mark.parametrize(
    ("field", "value", "display_value"),
    [
        (None, None, None),
        ("remote_as", "65102", "65102"),
        ("update_source", "Ethernet1", "Ethernet1"),
        ("bfd", False, "No"),
        ("send_community", "standard", "standard"),
    ],
)
def test_bgp_peer_groups_preserves_node_differences(field: str | None, value: str | bool | None, display_value: str | None) -> None:
    """A peer-group name shared by nodes must not hide different settings."""
    peer_group = {"name": "EXTERNAL-PEERS", "remote_as": "65101", "update_source": "Loopback0", "bfd": True, "send_community": "all"}
    other_peer_group = deepcopy(peer_group)
    if field is not None:
        other_peer_group[field] = value
    facts = FabricDocumentationFacts(
        avd_facts={},
        structured_configs={
            "node10": {"router_bgp": {"peer_groups": [peer_group]}},
            "node2": {"router_bgp": {"peer_groups": [other_peer_group]}},
            "node1": {"router_bgp": {"peer_groups": [peer_group]}},
        },
        fabric_name="TEST",
        include_connected_endpoints=False,
        toc=False,
    )
    entry = dict(peer_group, bfd="Yes", nodes="node1, node2, node10")
    if field is None:
        assert facts.bgp_peer_groups == [entry]
        return

    entry["nodes"] = "node1, node10"
    other_entry = dict(entry, nodes="node2")
    other_entry[field] = display_value
    assert facts.bgp_peer_groups == [entry, other_entry]
