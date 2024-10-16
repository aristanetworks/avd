# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import warnings

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._schema.store import create_store

SCHEMA = create_store()["eos_cli_config_gen"]


def test_eos_cli_config_gen_initialize_dict_with_valid_data(hostname: str, all_inputs: dict) -> None:
    """Test EosCliConfigGen model with valid data."""
    structured_config = all_inputs[hostname]

    # If nothing raises, the model is accepted.
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        EosCliConfigGen._from_dict(structured_config)


def test_eos_cli_config_gen_initialize_kwargs_with_valid_data(hostname: str, all_inputs: dict) -> None:
    """Test EosCliConfigGen model with valid data."""
    structured_config = all_inputs[hostname]

    # If nothing raises, the model is accepted.
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        EosCliConfigGen(**structured_config)
