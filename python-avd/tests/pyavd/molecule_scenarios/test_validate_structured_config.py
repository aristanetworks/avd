# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

import pytest

from pyavd import validate_structured_config
from tests.models import MoleculeHost


@pytest.mark.molecule_scenarios(
    "eos_cli_config_gen",
    "eos_cli_config_gen_deprecated_vars",
)
def test_validate_structured_config_with_valid_data(molecule_host: MoleculeHost) -> None:
    """Test validate_structured_config."""
    structured_config = molecule_host.hostvars if molecule_host.scenario.name.startswith("eos_cli_config_gen") else molecule_host.structured_config

    validated_data_result = validate_structured_config(structured_config)
    assert validated_data_result.validation_result.violations == []
    assert validated_data_result.validated_data is not None
