# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import pytest

from pyavd import load_inputs
from pyavd._eos_designs.schema import EosDesigns
from tests.models import MoleculeHost


# eos_cli_config_gen inputs are validated by `validate_structured_config` in another file.
@pytest.mark.molecule_scenarios(
    "digital_twin",
    "eos_designs_unit_tests",
    "eos_designs_deprecated_vars",
    "eos_designs-l2ls",
    "eos_designs-mpls-isis-sr-ldp",
    "eos_designs-twodc-5stage-clos",
    "evpn_underlay_ebgp_overlay_ebgp",
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
def test_validate_inputs_with_valid_inputs(molecule_host: MoleculeHost) -> None:
    """Test validate_inputs."""
    load_inputs_result = load_inputs(molecule_host.hostvars)
    assert len(load_inputs_result.validation_errors) == 0
    assert isinstance(load_inputs_result.inputs, EosDesigns)
