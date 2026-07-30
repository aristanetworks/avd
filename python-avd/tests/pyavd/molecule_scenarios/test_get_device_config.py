# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

import pytest

from pyavd import get_device_config, validate_structured_config
from pyavd._utils import get
from tests.models import MoleculeHost


@pytest.mark.molecule_scenarios(
    "eos_cli_config_gen",
    "eos_cli_config_gen_deprecated_vars",
)
@pytest.mark.digital_twin_molecule_scenarios("eos_designs-twodc-5stage-clos", "digital_twin")
def test_get_device_config(molecule_host: MoleculeHost) -> None:
    """Test get_device_config."""
    # For eos_designs scenarios, only load structured config, so this will fail if any inputs are not covered by eos_designs schemas.
    structured_config = molecule_host.hostvars if molecule_host.scenario.name.startswith("eos_cli_config_gen") else molecule_host.structured_config

    expected_config = molecule_host.config

    if not get(structured_config, "eos_cli_config_gen_configuration.enable", default=True):
        return

    validated_data_result = validate_structured_config(structured_config)
    assert validated_data_result.validated_data is not None
    device_config = get_device_config(validated_data_result.validated_data)

    assert isinstance(device_config, str)
    assert device_config == expected_config
