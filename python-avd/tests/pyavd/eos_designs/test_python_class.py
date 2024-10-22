# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import warnings

import pytest

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.schema import EosDesigns
from pyavd._schema.store import create_store

SCHEMA = create_store()["eos_designs"]
EOS_CLI_CONFIG_GEN_SCHEMA = create_store()["eos_cli_config_gen"]

CSC_DATA = {
    "fabric_name": "test",
    "custom_structured_configuration_router_bgp": {"as": 123},
    "csc_loopback_interfaces": [{"name": "Loopback0"}],
}

CSC_TESTS = [
    # prefix, expected_data
    (
        None,
        [
            EosDesigns._CustomStructuredConfigurationsItem(
                key="custom_structured_configuration_router_bgp", value=EosCliConfigGen(router_bgp=EosCliConfigGen.RouterBgp(field_as="123"))
            )
        ],
    ),  # Notice the auto conversion to string.
    (
        ["csc_"],
        [
            EosDesigns._CustomStructuredConfigurationsItem(
                key="csc_loopback_interfaces",
                value=EosCliConfigGen(loopback_interfaces=EosCliConfigGen.LoopbackInterfaces([EosCliConfigGen.LoopbackInterfacesItem(name="Loopback0")])),
            )
        ],
    ),
]


@pytest.mark.parametrize(("prefix", "expected_data"), CSC_TESTS)
def test_eos_designs_custom_structured_configuration(prefix: str | None, expected_data: dict) -> None:
    data = CSC_DATA.copy()
    if prefix:
        data.update({"custom_structured_configuration_prefix": prefix})
    loaded_model = EosDesigns._from_dict(data)
    assert hasattr(loaded_model, "_custom_structured_configurations")
    assert isinstance(loaded_model._custom_structured_configurations, list)

    for entry in loaded_model._custom_structured_configurations:
        assert isinstance(entry, EosDesigns._CustomStructuredConfigurationsItem)

    assert loaded_model._custom_structured_configurations == expected_data


def test_eos_designs_initialize_kwargs_with_valid_data(hostname: str, all_inputs: dict) -> None:
    """Test EosDesigns model with valid data."""
    inputs = all_inputs[hostname]

    # The class will not accept _custom_keys to be given directly. They must be given as `_custom_data: <dict>`.
    # This is normally handled by the loader, but since we here test loading with kwargs, we need to remove any
    # custom keys from the test data.
    # For now we will just skip those tests.
    # TODO: Remove custom keys recursively from data.
    if "'_" in str(inputs):
        return

    # If nothing raises, the model is accepted.
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        EosDesigns(**inputs)


def test_eos_designs_initialize_dict_with_valid_data(hostname: str, all_inputs: dict) -> None:
    """Test EosDesigns model with valid data."""
    inputs = all_inputs[hostname]

    # If nothing raises, the model is accepted.
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        EosDesigns._from_dict(inputs)


def test_eos_cli_config_gen_initialize_kwargs_with_valid_data(hostname: str, structured_configs: dict) -> None:
    """
    Test EosCliConfigGen model with valid data.

    Here we test with the structured configs of eos_designs so we get broader coverage.
    """
    structured_config = structured_configs[hostname]

    # The class will not accept _custom_keys to be given directly. They must be given as `_custom_data: <dict>`.
    # This is normally handled by the loader, but since we here test loading with kwargs, we need to remove any
    # custom keys from the test data.
    # For now we will just skip those tests.
    # TODO: Remove custom keys recursively from data.
    if "'_" in str(structured_config):
        return

    # If nothing raises, the model is accepted.
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        EosCliConfigGen(**structured_config)


def test_eos_cli_config_gen_initialize_dict_with_valid_data(hostname: str, structured_configs: dict) -> None:
    """
    Test EosCliConfigGen model with valid data.

    Here we test with the structured configs of eos_designs so we get broader coverage.
    """
    structured_config = structured_configs[hostname]

    # If nothing raises, the model is accepted.
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        EosCliConfigGen._from_dict(structured_config)
