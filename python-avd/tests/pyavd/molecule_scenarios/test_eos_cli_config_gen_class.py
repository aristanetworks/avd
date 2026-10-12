# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import warnings
from copy import deepcopy

import pytest

from pyavd import validate_structured_config
from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._schema.store import create_store
from tests.models import MoleculeHost

SCHEMA = create_store()["eos_cli_config_gen"]


@pytest.mark.molecule_scenarios(
    "eos_cli_config_gen",
    "eos_cli_config_gen_deprecated_vars",
)
def test_eos_cli_config_gen_initialize_dict_with_valid_data(molecule_host: MoleculeHost) -> None:
    """Test EosCliConfigGen model with valid data."""
    if molecule_host.scenario.name.startswith("eos_cli_config_gen"):
        structured_config = deepcopy(molecule_host.hostvars)
    else:
        structured_config = deepcopy(molecule_host.structured_config)

    # If nothing raises, the model is accepted.
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        EosCliConfigGen._from_dict(structured_config)


@pytest.mark.molecule_scenarios(
    "eos_cli_config_gen",
    "eos_cli_config_gen_deprecated_vars",
)
def test_eos_cli_config_gen_initialize_kwargs_with_valid_data(molecule_host: MoleculeHost) -> None:
    """Test EosCliConfigGen model with valid data."""
    if molecule_host.scenario.name.startswith("eos_cli_config_gen"):
        structured_config = deepcopy(molecule_host.hostvars)
    else:
        structured_config = deepcopy(molecule_host.structured_config)

    # If nothing raises, the model is accepted.
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        EosCliConfigGen(**structured_config)


@pytest.mark.molecule_scenarios(
    "eos_cli_config_gen",
    "eos_cli_config_gen_deprecated_vars",
)
def test_eos_cli_config_gen_load_dump_consistency(molecule_host: MoleculeHost) -> None:
    """Test first loading and then dumping the EosDesigns model matches the original data."""
    if molecule_host.scenario.name.startswith("eos_cli_config_gen"):
        structured_config = deepcopy(molecule_host.hostvars)
    else:
        structured_config = deepcopy(molecule_host.structured_config)

    loaded_model = EosCliConfigGen._from_dict(structured_config)
    dumped_data = loaded_model._as_dict()

    # Coerce data types to match the loaded data.
    validated_data_result = validate_structured_config(structured_config)
    assert validated_data_result.validated_data is not None
    validated_data = validated_data_result.validated_data

    # Remove all ansible_* keys from the validated data.
    # This is only relevant for the scenarios loading from hostvars (eos_cli_config_gen*)
    expected_data = {
        k: v
        for k, v in validated_data.items()
        if not k.startswith(("ansible", "group_names", "groups", "inventory", "is_for_test", "omit", "playbook_dir", "root_dir"))
    }

    assert dumped_data == expected_data
