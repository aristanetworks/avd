# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

import pytest

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.schema import EosDesigns
from pyavd._schema.store import create_store

SCHEMA = create_store()["eos_designs"]

CSC_DATA = {
    "fabric_name": "test",
    "custom_structured_configuration_router_bgp": {"as": 123},
    "csc_loopback_interfaces": [{"name": "Loopback0"}],
}

CSC_TESTS = [
    # prefix, expected_data
    (
        None,
        EosDesigns._CustomStructuredConfigurations(
            [
                EosDesigns._CustomStructuredConfigurationsItem(
                    key="custom_structured_configuration_router_bgp", value=EosCliConfigGen(router_bgp=EosCliConfigGen.RouterBgp(field_as="123"))
                )
            ]
        ),
    ),  # Notice the auto conversion to string.
    (
        ["csc_"],
        EosDesigns._CustomStructuredConfigurations(
            [
                EosDesigns._CustomStructuredConfigurationsItem(
                    key="csc_loopback_interfaces",
                    value=EosCliConfigGen(loopback_interfaces=EosCliConfigGen.LoopbackInterfaces([EosCliConfigGen.LoopbackInterfacesItem(name="Loopback0")])),
                )
            ]
        ),
    ),
]


@pytest.mark.parametrize(("prefix", "expected_data"), CSC_TESTS)
def test_eos_designs_custom_structured_configuration(prefix: str | None, expected_data: EosDesigns._CustomStructuredConfigurations) -> None:
    data = CSC_DATA.copy()
    if prefix:
        data.update({"custom_structured_configuration_prefix": prefix})
    loaded_model = EosDesigns._from_dict(data)
    assert hasattr(loaded_model, "_custom_structured_configurations")
    assert isinstance(loaded_model._custom_structured_configurations, EosDesigns._CustomStructuredConfigurations)

    for entry in loaded_model._custom_structured_configurations:
        assert isinstance(entry, EosDesigns._CustomStructuredConfigurationsItem)

    assert repr(loaded_model._custom_structured_configurations) == repr(expected_data)
