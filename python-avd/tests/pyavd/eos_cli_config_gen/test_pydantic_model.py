# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import pytest
from pyavd.avd_schema_tools import AvdSchemaTools
from pyavd.schema.eos_cli_config_gen import EosCliConfigGen
from pydantic_core import ValidationError

SCHEMA = AvdSchemaTools(schema_id="eos_cli_config_gen").avdschema.resolved_schema


def test_eos_cli_config_gen_with_valid_data(hostname: str, all_inputs: dict):
    """
    Test EosCliConfigGen pydantic model with valid data.
    """
    structured_config = all_inputs[hostname]
    EosCliConfigGen(**structured_config)
    # If nothing raises, the model is accepted.


def test_eos_cli_config_gen_with_invalid_data(hostname: str, all_inputs: dict):
    """
    Test EosCliConfigGen pydantic model with invalid data.
    """
    structured_config: dict = all_inputs[hostname]

    updated = False
    # Insert a bad key in a random dict (making sure the dict is covered by the schema)
    for key, value in structured_config.items():
        if not isinstance(value, dict) or "structured_config" in key or key not in SCHEMA["keys"]:
            continue
        value.update({"invalid_key": "some_value"})
        updated = f"{key}.invalid_key"
        break

    # No dict found, so we insert our own instead
    if not updated:
        structured_config.update({"ethernet_interfaces": [{"name": "dummy", "invalid_key": "some_value"}]})
        updated = "ethernet_interfaces.0.invalid_key"

    with pytest.raises(ValidationError, match=rf"{updated}\n  Extra inputs are not permitted"):
        EosCliConfigGen(**structured_config)
