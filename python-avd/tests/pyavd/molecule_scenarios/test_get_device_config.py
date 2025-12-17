# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import json

import pytest

from pyavd import get_device_config, validate_structured_config
from pyavd._utils import get
from tests.models import MoleculeHost


@pytest.mark.molecule_scenarios(
    "digital_twin",
    "eos_designs_unit_tests",
    "eos_designs_deprecated_vars",
    "eos_cli_config_gen",
    "eos_cli_config_gen_deprecated_vars",
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
@pytest.mark.digital_twin_molecule_scenarios("eos_designs-twodc-5stage-clos", "digital_twin")
def test_get_device_config(molecule_host: MoleculeHost) -> None:
    """Test get_device_config."""
    # For eos_designs scenarios, only load structured config, so this will fail if any inputs are not covered by eos_designs schemas.
    structured_config = molecule_host.hostvars if molecule_host.scenario.name.startswith("eos_cli_config_gen") else molecule_host.structured_config

    expected_config = molecule_host.config

    if not get(structured_config, "eos_cli_config_gen_configuration.enable", default=True):
        return

    # TODO: Figure out why the commented code reorders certain outputs that are sorted without case sensitivity.
    # TODO: Seen with `pytest python-avd/tests/pyavd/molecule_scenarios/test_get_device_config.py::test_get_device_config[eos_cli_config_gen__host1]`
    # TODO: load_eos_config_result = load_eos_config(structured_config)
    # TODO: assert load_eos_config_result.eos_config is not None
    # TODO: device_config = get_device_config(load_eos_config_result.eos_config)

    validated_data_result = validate_structured_config(structured_config)
    assert validated_data_result.validated_data is not None
    structured_config = json.loads(validated_data_result.validated_data)
    device_config = get_device_config(structured_config)

    assert isinstance(device_config, str)
    assert device_config == expected_config
