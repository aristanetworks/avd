# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import sys
from copy import deepcopy
from unittest.mock import patch

import pytest

from pyavd import get_device_structured_config, load_design
from pyavd.api.schemas import EOSConfig
from tests.models import MoleculeHost


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
# TODO: Remove inline jinja
# @pytest.mark.digital_twin_molecule_scenarios("eos_designs-twodc-5stage-clos")
@pytest.mark.digital_twin_molecule_scenarios("digital_twin")
def test_get_device_structured_config(molecule_host: MoleculeHost) -> None:
    """Test get_device_structured_config."""
    inputs = deepcopy(molecule_host.hostvars)

    # Load inputs
    load_design_result = load_design(inputs)

    assert load_design_result.design is not None

    design = load_design_result.design

    expected_structured_config = molecule_host.structured_config

    with patch("sys.path", [*sys.path, *molecule_host.scenario.extra_python_paths]):
        avd_facts = molecule_host.scenario.avd_facts
        structured_config = get_device_structured_config(molecule_host.name, design, avd_facts, digital_twin=molecule_host.scenario.digital_twin)

    assert isinstance(structured_config, EOSConfig)
    assert molecule_host.name == structured_config.hostname
    # Comparing with dict to get better assert output on diff.
    assert expected_structured_config == structured_config._asdict()
