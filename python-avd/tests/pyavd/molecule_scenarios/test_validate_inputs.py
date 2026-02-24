# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

import pytest
from pyavd_utils.validation import Configuration

from pyavd import validate_inputs
from tests.models import MoleculeHost


# eos_cli_config_gen inputs are validated by `validate_structured_config` in another file.
@pytest.mark.molecule_scenarios(
    "digital_twin",
    "eos_designs_unit_tests",
    "eos_designs_deprecated_vars",
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
def test_validate_inputs_with_valid_inputs(molecule_host: MoleculeHost) -> None:
    """Test validate_inputs."""
    inputs = molecule_host.hostvars
    validated_data_result = validate_inputs(inputs)
    assert validated_data_result.validation_result.violations == []


def test_validate_inputs_with_eos_cli_config_gen_keys() -> None:
    """
    Test that validate_inputs returns ignored_eos_config_keys warning.

    When EOS Config keys are used in the inputs and the configuration object has warn_eos_config_keys set to True.
    """
    inputs = {
        "fabric_name": "TEST-FABRIC",
        "dns_domain": "this.should.warn.test",
        "dns_settings": {"servers": [{"ip_address": "8.8.8.8"}]},
    }

    # Test with warnings enabled
    configuration = Configuration(warn_eos_config_keys=True)
    validated_data_result = validate_inputs(inputs, configuration=configuration)

    # Should have no violations
    assert validated_data_result.validation_result.violations == []

    # Should have ignored_eos_config_keys
    assert len(validated_data_result.validation_result.ignored_eos_config_keys) == 1
    assert validated_data_result.validation_result.ignored_eos_config_keys[0].path == ["dns_domain"]
    assert "EOS Config" in validated_data_result.validation_result.ignored_eos_config_keys[0].message


def test_validate_inputs_with_eos_cli_config_gen_keys_disabled() -> None:
    """
    Test that validate_inputs does not return ignored_eos_config_keys warning.

    When EOS Config keys are used in the inputs and the configuration object has warn_eos_config_keys set to False.
    """
    inputs = {
        "fabric_name": "TEST-FABRIC",
        "dns_domain": "this.should.not.warn.test",
        "dns_settings": {"servers": [{"ip_address": "8.8.8.8"}]},
    }

    # Test with warnings disabled using Configuration object
    configuration = Configuration(warn_eos_config_keys=False)
    validated_data_result = validate_inputs(inputs, configuration=configuration)

    # Should have no violations
    assert validated_data_result.validation_result.violations == []

    # Should NOT have ignored_eos_config_keys
    assert len(validated_data_result.validation_result.ignored_eos_config_keys) == 0


def test_validate_with_allow_with_new_key_deprecation() -> None:
    """
    Test that validation handles allow_with_new_key deprecation correctly through the Rust path.

    This test creates a custom schema with a deprecated key that has allow_with_new_key=True
    and validates that both old and new keys can coexist without a conflict error.
    """
    import json

    from pyavd_utils.validation import validate_json_with_adhoc_schema

    from pyavd._schema.store import init_store

    # Initialize the store (required before validation)
    init_store()

    # Define a custom test schema with deprecation
    test_schema = {
        "type": "dict",
        "keys": {
            "old_key": {
                "type": "str",
                "deprecation": {
                    "warning": True,
                    "new_key": "new_key",
                    "allow_with_new_key": True,
                    "remove_in_version": "1.0.0",
                },
            },
            "new_key": {
                "type": "str",
            },
        },
    }

    # Test data with both old and new keys
    test_data = {
        "old_key": "old_value",
        "new_key": "new_value",
    }

    # Validate through the Rust path using adhoc schema
    validation_result = validate_json_with_adhoc_schema(
        data_as_json=json.dumps(test_data),
        schema_as_json=json.dumps(test_schema),
    )

    # Should have no violations (no conflict error)
    assert validation_result.violations == []

    # Should have exactly one deprecation warning
    assert len(validation_result.deprecations) == 1
    deprecation = validation_result.deprecations[0]
    assert deprecation.path == ["old_key"]
    assert "deprecated" in deprecation.message.lower()
    assert "new_key" in deprecation.message.lower()
