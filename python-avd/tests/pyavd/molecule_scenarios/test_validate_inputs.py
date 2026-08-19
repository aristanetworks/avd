# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

from pyavd_utils.validation import Configuration

from pyavd import validate_inputs
from pyavd.api.schemas import AVDDesign


def test_validate_inputs_normalizes_dynamic_keys_before_model_loading() -> None:
    inputs = {
        "fabric_name": "TEST-FABRIC",
        "custom_node_type_keys": [{"key": "l3leaf", "type": "l3leaf"}],
        "custom_connected_endpoints_keys": [{"key": "servers", "type": "server"}],
        "l3leaf": {"defaults": {}},
        "servers": [],
        "tenants": [],
    }

    result = validate_inputs(inputs)

    assert result.validation_result.violations == []
    assert result.validated_data is not None
    assert all(key not in result.validated_data for key in ("l3leaf", "servers", "tenants"))
    assert set(result.validated_data["_dynamic_keys"]) == {"connected_endpoints", "network_services", "node_types"}
    avd_design = AVDDesign._from_dict(result.validated_data)
    assert "l3leaf" in avd_design._dynamic_keys.node_types
    assert "servers" in avd_design._dynamic_keys.connected_endpoints
    assert "tenants" in avd_design._dynamic_keys.network_services
    assert avd_design._dynamic_keys.node_types["l3leaf"].source == "custom_node_types"
    assert avd_design._dynamic_keys.connected_endpoints["servers"].source == "custom_connected_endpoints"
    assert avd_design._dynamic_keys.network_services["tenants"].source == "network_services"


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
