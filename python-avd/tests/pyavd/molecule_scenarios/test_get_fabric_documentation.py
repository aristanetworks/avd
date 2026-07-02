# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import sys
from copy import deepcopy
from unittest.mock import patch

import pytest

from pyavd import get_fabric_documentation
from pyavd._utils import get
from pyavd.api.fabric_documentation import ACTDigitalTwin, FabricDocumentation
from tests.models import MoleculeScenario


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


@pytest.mark.molecule_scenarios(
    "digital_twin",
    "eos_designs_unit_tests",
    "eos_designs_deprecated_vars",
    "eos_designs-l2ls",
    "eos_designs-mpls-isis-sr-ldp",
    # TODO: "eos_designs-twodc-5stage-clos", # Remove inline jinja
    # TODO: "evpn_underlay_ebgp_overlay_ebgp", # Remove inline jinja
    "evpn_underlay_isis_overlay_ibgp",
    "evpn_underlay_ospf_overlay_ebgp",
    "evpn_underlay_rfc5549_overlay_ebgp",
    "example-campus-fabric",
    # TODO: "example-cv-pathfinder", # Work around Ansible vault
    "example-dual-dc-l3ls",
    "example-isis-ldp-ipvpn",
    "example-l2ls-fabric",
    "example-single-dc-l3ls",
    "example-single-dc-l3ls-ipv6",
)
@pytest.mark.digital_twin_molecule_scenarios("eos_designs-twodc-5stage-clos", "digital_twin")
def test_get_fabric_documentation(molecule_scenario: MoleculeScenario) -> None:
    """Test get_fabric_documentation."""
    with patch("sys.path", [*sys.path, *molecule_scenario.extra_python_paths]):
        molecule_structured_configs = {host.name: deepcopy(host.structured_config) for host in molecule_scenario.hosts}
        molecule_avd_facts = molecule_scenario.avd_facts

        # Get variables from the first molecule host.
        first_hostvars = next(iter(molecule_scenario.hosts)).hostvars
        molecule_fabric_name: str = first_hostvars["fabric_name"]
        enable = get(first_hostvars, "eos_designs_documentation.enable", default=True)
        connected_endpoints = get(first_hostvars, "eos_designs_documentation.connected_endpoints", default=False)
        topology_csv = get(first_hostvars, "eos_designs_documentation.topology_csv", default=False)
        p2p_links_csv = get(first_hostvars, "eos_designs_documentation.p2p_links_csv", default=False)
        toc = get(first_hostvars, "eos_designs_documentation.toc", default=True)
        include_vrf_summary = get(first_hostvars, "eos_designs_documentation.sections.vrf_summary", default=False)
        include_bgp_peer_groups = get(first_hostvars, "eos_designs_documentation.sections.bgp_peer_groups", default=False)

        fabric_documentation_obj = get_fabric_documentation(
            avd_facts=molecule_avd_facts,
            structured_configs=molecule_structured_configs,
            fabric_name=molecule_fabric_name,
            fabric_documentation=enable,
            include_connected_endpoints=connected_endpoints,
            topology_csv=topology_csv,
            p2p_links_csv=p2p_links_csv,
            toc=toc,
            digital_twin=molecule_scenario.digital_twin,
            include_vrf_summary=include_vrf_summary,
            include_bgp_peer_groups=include_bgp_peer_groups,
        )

    assert isinstance(fabric_documentation_obj, FabricDocumentation)

    if enable:
        # We expect fabric docs
        assert isinstance(molecule_scenario.fabric_documentation, str)
        assert fabric_documentation_obj.fabric_documentation == molecule_scenario.fabric_documentation
    else:
        # No fabric docs
        assert molecule_scenario.fabric_documentation is None
        assert fabric_documentation_obj.fabric_documentation == ""

    if topology_csv:
        # We expect topology csv
        assert isinstance(molecule_scenario.topology_csv, str)
        assert fabric_documentation_obj.topology_csv == molecule_scenario.topology_csv
    else:
        # No topology csv
        assert molecule_scenario.topology_csv is None
        assert fabric_documentation_obj.topology_csv == ""

    if p2p_links_csv:
        # We expect p2p links csv
        assert isinstance(molecule_scenario.p2p_links_csv, str)
        assert fabric_documentation_obj.p2p_links_csv == molecule_scenario.p2p_links_csv
    else:
        # No p2p links csv
        assert molecule_scenario.p2p_links_csv is None
        assert fabric_documentation_obj.p2p_links_csv == ""

    if molecule_scenario.digital_twin:
        # We expect digital twin topology
        assert isinstance(fabric_documentation_obj.digital_twin, ACTDigitalTwin)
        # TODO: add shortcut to the digital twin topology file contents in the MoleculeScenario object and assert that it matches.
    else:
        # No digital twin topology
        assert fabric_documentation_obj.digital_twin is None
