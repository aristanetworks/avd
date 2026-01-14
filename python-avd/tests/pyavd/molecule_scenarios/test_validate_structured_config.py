# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from copy import deepcopy

import pytest

from pyavd import validate_structured_config
from pyavd._schema.models.constants import EOS_CLI_CONFIG_GEN_INPUT_KEYS
from tests.models import MoleculeHost


@pytest.mark.molecule_scenarios(
    "digital_twin",
    "eos_designs_unit_tests",
    "eos_designs_deprecated_vars",
    "eos_designs-l2ls",
    "eos_designs-mpls-isis-sr-ldp",
    # TODO: "eos_designs-twodc-5stage-clos", # Remove inline jinja
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
    "eos_cli_config_gen",
    "eos_cli_config_gen_deprecated_vars",
)
@pytest.mark.digital_twin_molecule_scenarios("eos_designs-twodc-5stage-clos", "digital_twin")
def test_validate_structured_config_with_valid_data(molecule_host: MoleculeHost) -> None:
    """Test validate_structured_config."""
    structured_config = molecule_host.hostvars if molecule_host.scenario.name.startswith("eos_cli_config_gen") else molecule_host.structured_config

    validated_data_result = validate_structured_config(structured_config)
    assert validated_data_result.validation_result.violations == []
    assert validated_data_result.validated_data is not None


@pytest.mark.molecule_scenarios(
    "eos_designs_unit_tests",
    "eos_designs_deprecated_vars",
)
def test_validate_structured_config_with_invalid_data(molecule_host: MoleculeHost) -> None:
    """Test validate_structured_config."""
    if molecule_host.scenario.name.startswith("eos_cli_config_gen"):
        structured_config = deepcopy(molecule_host.hostvars)
    else:
        structured_config = deepcopy(molecule_host.structured_config)

    updated = False
    # Insert a bad key in a random dict (making sure the dict is covered by the schema)
    for key, value in structured_config.items():
        if not isinstance(value, dict) or "structured_config" in key or key not in EOS_CLI_CONFIG_GEN_INPUT_KEYS:
            continue
        value.update({"invalid_key": "some_value"})
        updated = True
        break

    # No dict found, so we insert our own instead
    if not updated:
        structured_config.update({"router_bgp": {"invalid_key": "some_value"}})

    validated_data_result = validate_structured_config(structured_config)
    assert validated_data_result.validated_data is None
    assert len(validated_data_result.validation_result.violations) >= 1
    assert validated_data_result.validation_result.violations[0].message == "Invalid key."
