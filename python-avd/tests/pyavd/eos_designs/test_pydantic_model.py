# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import pytest
from pyavd.avd_schema_tools import AvdSchemaTools
from pyavd.schema.eos_cli_config_gen import EosCliConfigGen
from pyavd.schema.eos_designs import EosDesigns
from pydantic_core import ValidationError

SCHEMA = AvdSchemaTools(schema_id="eos_designs").avdschema.resolved_schema

CSC_DATA = {
    "fabric_name": "test",
    "custom_structured_configuration_router_bgp": {"as": 123},
    "csc_loopback_interfaces": [{"name": "Loopback0"}],
}

CSC_TESTS = [
    # (prefix, expected structured config)
    (None, [{"key": "custom_structured_configuration_router_bgp", "value": {"router_bgp": {"as": "123"}}}]),  # Notice the auto conversion to string.
    (["csc_"], [{"key": "csc_loopback_interfaces", "value": {"loopback_interfaces": CSC_DATA["csc_loopback_interfaces"]}}]),
]


@pytest.mark.parametrize(("prefix", "expected_data"), CSC_TESTS)
def test_eos_designs_custom_structured_configuration(prefix: str, expected_data: dict):
    data = {**CSC_DATA, "custom_structured_configuration_prefix": prefix}
    loaded_model = EosDesigns(**data)
    assert hasattr(loaded_model, "custom_structured_configurations")
    assert isinstance(loaded_model.custom_structured_configurations, list)
    returned_data = []
    for entry in loaded_model.custom_structured_configurations:
        assert isinstance(entry, EosDesigns.CustomStructuredConfiguration)
        returned_data.append(entry.model_dump(exclude_defaults=True, exclude_unset=True, by_alias=True))

    assert returned_data == expected_data

    # Ensure the keys got popped before validation.
    assert not [key for key in (loaded_model.model_extra or {}) if key.startswith(prefix)]


def test_eos_designs_with_valid_data(hostname: str, all_inputs: dict):
    """
    Test EosDesigns pydantic model with valid data.
    """
    structured_config = all_inputs[hostname]
    EosDesigns(**structured_config)
    # If nothing raises, the model is accepted.


def test_eos_designs_with_invalid_data(hostname: str, all_inputs: dict):
    """
    Test EosDesigns pydantic model with invalid data.
    """
    structured_config: dict = all_inputs[hostname]

    updated = False
    # Insert a bad key in a random dict (making sure the dict is covered by the schema)
    for key, value in structured_config.items():
        if not isinstance(value, dict) or key not in SCHEMA["keys"]:
            continue
        value.update({"invalid_key": "some_value"})
        updated = f"{key}.invalid_key"
        break

    # No dict found, so we insert our own instead
    if not updated:
        structured_config.update({"bgp_peer_groups": {"invalid_key": "some_value"}})
        updated = "bgp_peer_groups.invalid_key"

    with pytest.raises(ValidationError) as exc_info:
        EosDesigns(**structured_config)
    errors = exc_info.value.errors()
    msgs = set(error["msg"] for error in errors)
    assert msgs == {"Extra inputs are not permitted"}


def test_eos_cli_config_gen_with_valid_data(hostname: str, structured_configs: dict):
    """
    Test EosCliConfigGen pydantic model with valid data.
    Here we test with the structured configs of eos_designs so we get broader coverage.
    """
    structured_config = structured_configs[hostname]
    EosCliConfigGen(**structured_config)
    # If nothing raises, the model is accepted.


def test_eos_cli_config_gen_with_invalid_data(hostname: str, structured_configs: dict):
    """
    Test EosCliConfigGen pydantic model with invalid data.
    Here we test with the structured configs of eos_designs so we get broader coverage.
    """
    structured_config: dict = structured_configs[hostname]

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

    with pytest.raises(ValidationError) as exc_info:
        EosCliConfigGen(**structured_config)
    errors = exc_info.value.errors()
    msgs = set(error["msg"] for error in errors)
    assert msgs == {"Extra inputs are not permitted"}
