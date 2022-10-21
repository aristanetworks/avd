"""
Test file for plugins/plugin_utils/schema/avdvalidator.py
"""
from __future__ import absolute_import, division, print_function

__metaclass__ = type

import pytest

# TODO this only covers type 7
PASSWORD_VALIDATOR_SCHEMA_BGP_TYPE = {
    "type": "dict",
    "keys": {
        "password": {
            "type": "str",
            "description": "BGP password",
        },
        "neighbor_ip": {"type": "str", "description": "The neighbor IP"},
    },
    "validate_password": {"password_field": "password", "password_type": "bgp", "password_key_field": "neighbor_ip"},
}
PASSWORD_VALIDATOR_SCHEMA_BGP_TYPE_MISSING_FIELD = {
    "type": "dict",
    "keys": {
        "password": {
            "type": "str",
            "description": "BGP password",
        }
    },
    "validate_password": {"password_field": "password", "password_type": "bgp"},
}
PASSWORD_VALIDATOR_SCHEMA_BGP_TYPE_UNKNOWN_FIELD = {
    "type": "dict",
    "keys": {
        "password": {
            "type": "str",
            "description": "BGP password",
        },
        "neighbor_ip": {"type": "str", "description": "The neighbor IP"},
    },
    "validate_password": {"password_field": "password", "password_type": "bgp", "password_key_field": "neighbor_ip_address"},
}

# TODO - fow now just verify that the correct validator is unhappy - should verify on the error messahe probably
PASSWORD_VALIDATOR_PARAMS = [
    pytest.param({"password": True}, PASSWORD_VALIDATOR_SCHEMA_BGP_TYPE, ["type"], id="wrong_type"),
    pytest.param({"password": "3QGcqpU2YTwKh2jVQ4Vj/A==", "neighbor_ip": "42.42.42.42"}, PASSWORD_VALIDATOR_SCHEMA_BGP_TYPE, [], id="valid_password"),
    pytest.param({"password": "toto", "neighbor_ip": "42.42.42.42"}, PASSWORD_VALIDATOR_SCHEMA_BGP_TYPE, ["validate_password"], id="invalid_password"),
    pytest.param({"password": "toto"}, PASSWORD_VALIDATOR_SCHEMA_BGP_TYPE_MISSING_FIELD, ["validate_password"], id="missing_password_key_field"),
    pytest.param({"password": "toto"}, PASSWORD_VALIDATOR_SCHEMA_BGP_TYPE_UNKNOWN_FIELD, ["validate_password"], id="unkown_password_key_field"),
]


@pytest.mark.parametrize("instance, schema, expected_errors", PASSWORD_VALIDATOR_PARAMS)
def test__password_validator(avdvalidator_factory, instance, schema, expected_errors):
    """
    Tests to verify the behavior of the _password_validator

    For the expected validation errors, for now the test only check that the correct validator triggered the error.
    """
    avdvalidator = avdvalidator_factory(schema)
    errors = list(avdvalidator.iter_errors(instance))
    print(errors)
    assert len(expected_errors) == len(errors)
    for index, error in enumerate(sorted(errors, key=lambda x: x.validator)):
        assert error.validator == expected_errors[index]
