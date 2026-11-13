# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from pyavd import get_fabric_documentation
from pyavd._eos_designs.eos_designs_facts.schema import EosDesignsFacts
from pyavd.api.fabric_documentation import ContainerlabDigitalTwin, FabricDocumentation

if TYPE_CHECKING:
    from tests.models import MoleculeScenario


@pytest.mark.parametrize(
    ("mpls_config", "include_table"),
    [
        ({}, False),
        ({"ip": True}, False),
        ({"ldp": {"router_id": "192.0.2.1", "shutdown": False}}, True),
        ({"ldp": {"router_id": "192.0.2.1", "shutdown": True}}, True),
        ({"ldp": {"router_id": "192.0.2.1"}}, True),
        ({"ldp": {"shutdown": False}}, True),
    ],
)
def test_get_fabric_documentation_with_ldp_configuration(mpls_config: dict, include_table: bool) -> None:
    """Include configured LDP nodes even when LDP is shut down or shutdown is unspecified."""
    output = get_fabric_documentation(
        avd_facts={"p1": EosDesignsFacts(type="p", pod="POD1"), "p2": EosDesignsFacts(type="p", pod="POD1")},
        structured_configs={"p1": {"mpls": mpls_config}, "p2": {}},
        fabric_name="MPLS_CORE",
        toc=False,
    )

    assert ("### MPLS and LDP Configuration" in output.fabric_documentation) is include_table
    if include_table:
        router_id = mpls_config["ldp"].get("router_id", "-")
        assert output.fabric_documentation.count(f"| POD1 | p1 | p | {router_id} |") == 1
    assert "| POD1 | p2 | p |" not in output.fabric_documentation


@pytest.mark.molecule_scenarios("eos_designs-mpls-isis-sr-ldp")
@pytest.mark.parametrize(("include_vrf_summary", "include_bgp_peer_groups"), [(True, True), (True, False), (False, True), (False, False)])
def test_fabric_documentation_with_node_specific_settings(
    molecule_scenario: MoleculeScenario, include_vrf_summary: bool, include_bgp_peer_groups: bool
) -> None:
    """Render the MPLS fixture without hiding VRF or eBGP peer-group differences."""
    output = get_fabric_documentation(
        avd_facts=molecule_scenario.avd_facts,
        structured_configs={host.name: host.structured_config for host in molecule_scenario.hosts},
        fabric_name="MPLS_CORE",
        include_vrf_summary=include_vrf_summary,
        include_bgp_peer_groups=include_bgp_peer_groups,
    )
    documentation = output.fabric_documentation
    assert documentation is not None
    assert ("### VRF Summary" in documentation) is include_vrf_summary
    assert ("### BGP Peer Groups" in documentation) is include_bgp_peer_groups
    if include_vrf_summary:
        assert "| TENANT_B_WAN | 20 | vpn-ipv4 65000:20, vpn-ipv6 65000:20 | vpn-ipv4 65000:20, vpn-ipv6 65000:20 | SITE1-LER2 |" in documentation
        assert (
            "| TENANT_B_WAN | 20 | vpn-ipv4 65000:120, vpn-ipv4 65000:20, vpn-ipv6 65000:20 | "
            "vpn-ipv4 65000:20, vpn-ipv4 65000:220, vpn-ipv6 65000:20 | SITE2-LER1 |"
        ) in documentation
    if include_bgp_peer_groups:
        assert "| DOCUMENTATION-EBGP-PEERS | 65101 | Loopback0 | Yes | all | SITE1-LER2 |" in documentation
        assert "| DOCUMENTATION-EBGP-PEERS | 65102 | Ethernet1 | No | standard | SITE2-LER1 |" in documentation


def test_get_fabric_documentation_with_no_connected_endpoints(monkeypatch: pytest.MonkeyPatch) -> None:
    """Test connected endpoints documentation empty state."""

    class FabricDocumentationFacts:
        def __init__(self, *args: object, **kwargs: object) -> None:
            pass

        def render(self) -> dict[str, object]:
            return {
                "fabric_name": "EMPTY_FABRIC",
                "toc": False,
                "fabric_switches": [],
                "topology_links": [],
                "uplink_ipv4_networks": [],
                "loopback_ipv4_networks": [],
                "vtep_loopback_ipv4_networks": [],
                "has_isis": False,
                "has_mpls": False,
                "has_isis_sr": False,
                "has_mpls_overlay": False,
                "has_mpls_route_reflectors": False,
                "include_vrf_summary": False,
                "has_vrfs": False,
                "include_bgp_peer_groups": False,
                "has_bgp_peer_groups": False,
                "has_vrf_routing_protocols": False,
                "all_connected_endpoints": {},
                "all_connected_endpoints_keys": [],
                "all_port_profiles": [],
            }

    monkeypatch.setattr("pyavd._eos_designs.fabric_documentation_facts.FabricDocumentationFacts", FabricDocumentationFacts)

    fabric_documentation_obj = get_fabric_documentation(
        avd_facts={},
        structured_configs={},
        fabric_name="EMPTY_FABRIC",
        include_connected_endpoints=True,
        toc=False,
    )

    assert "## Connected Endpoints\n\nNo connected endpoint configured!" in fabric_documentation_obj.fabric_documentation


@pytest.mark.parametrize("digital_twin_enabled", [True, False])
def test_get_fabric_documentation_containerlab(digital_twin_enabled: bool) -> None:
    """Test Containerlab environment selection and the Digital Twin enable flag."""
    fabric_documentation_obj = get_fabric_documentation(
        avd_facts={"leaf1": EosDesignsFacts(mgmt_ip="192.0.2.1/24")},
        structured_configs={"leaf1": {"metadata": {"digital_twin": {"environment": "containerlab"}}}},
        fabric_name="CONTAINERLAB_FABRIC",
        fabric_documentation=False,
        digital_twin=digital_twin_enabled,
    )

    assert isinstance(fabric_documentation_obj, FabricDocumentation)
    if digital_twin_enabled:
        assert isinstance(fabric_documentation_obj.digital_twin, ContainerlabDigitalTwin)
        assert fabric_documentation_obj.digital_twin.name == "CONTAINERLAB_FABRIC"
        assert fabric_documentation_obj.digital_twin.prefix == ""
        assert fabric_documentation_obj.digital_twin.mgmt.ipv4_subnet == "192.0.2.0/24"
    else:
        assert fabric_documentation_obj.digital_twin is None


def test_get_digital_twin_returns_none_for_unsupported_environment() -> None:
    """Test fallback behavior through the public documentation API."""
    output = get_fabric_documentation(
        avd_facts={},
        structured_configs={"leaf1": {"metadata": {"digital_twin": {"environment": "unsupported"}}}},
        fabric_name="UNSUPPORTED_FABRIC",
        fabric_documentation=False,
        digital_twin=True,
    )

    assert output.digital_twin is None
