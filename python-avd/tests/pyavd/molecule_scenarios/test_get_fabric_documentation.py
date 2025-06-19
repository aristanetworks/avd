# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import sys
from copy import deepcopy
from unittest.mock import patch

import pytest

from pyavd import get_fabric_documentation
from pyavd._utils import get
from pyavd.api.fabric_documentation import FabricDocumentation
from tests.models import MoleculeScenario


@pytest.mark.molecule_scenarios(
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
)
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

        fabric_documentation_obj = get_fabric_documentation(
            avd_facts=molecule_avd_facts,
            structured_configs=molecule_structured_configs,
            fabric_name=molecule_fabric_name,
            fabric_documentation=enable,
            include_connected_endpoints=connected_endpoints,
            topology_csv=topology_csv,
            p2p_links_csv=p2p_links_csv,
            toc=toc,
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
