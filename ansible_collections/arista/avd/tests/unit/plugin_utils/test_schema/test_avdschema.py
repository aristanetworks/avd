"""
Test file for plugins/plugin_utils/schema/avdschema.py
"""
from __future__ import absolute_import, division, print_function

__metaclass__ = type

import pytest

from ansible_collections.arista.avd.plugins.plugin_utils.schema.errors import AvdValidationError

from ...conftest import does_not_raise

PASSWORD_VALIDATOR_SCHEMA_MISSING_PASSWORD_FIELD = {
    "type": "dict",
    "keys": {
        "password": {"type": "str", "description": "Password"},
    },
    "validate_password": {"password_type": "bgp"},
    "description": "Missing required password_field in validate_password",
}
PASSWORD_VALIDATOR_SCHEMA_MISSING_PASSWORD_TYPE = {
    "type": "dict",
    "keys": {
        "password": {"type": "str", "description": "Password"},
    },
    "validate_password": {"password_field": "password"},
    "description": "Missing required password_type in validate_password",
}
PASSWORD_VALIDATOR_SCHEMA_WRONG_PASSWORD_TYPE = {
    "type": "dict",
    "keys": {
        "password": {"type": "str", "description": "Password"},
    },
    "validate_password": {"password_field": "password", "password_type": "toto"},
    "description": "Missing required password_type in validate_password",
}
PASSWORD_VALIDATOR_SCHEMA_VALID = {
    "type": "dict",
    "keys": {
        "password": {"type": "str", "description": "Password"},
    },
    "validate_password": {"password_field": "password", "password_type": "bgp"},
    "description": "Missing required password_type in validate_password",
}

PASSWORD_VALIDATOR_PARAMS = [
    pytest.param(PASSWORD_VALIDATOR_SCHEMA_MISSING_PASSWORD_FIELD, pytest.raises(AvdValidationError), id="missing_password_field"),
    pytest.param(PASSWORD_VALIDATOR_SCHEMA_MISSING_PASSWORD_TYPE, pytest.raises(AvdValidationError), id="missing_password_type"),
    pytest.param(PASSWORD_VALIDATOR_SCHEMA_WRONG_PASSWORD_TYPE, pytest.raises(AvdValidationError), id="wrong_password_type"),
    pytest.param(PASSWORD_VALIDATOR_SCHEMA_VALID, does_not_raise(), id="valid_schema"),
]


@pytest.mark.parametrize("schema, expected_raise", PASSWORD_VALIDATOR_PARAMS)
def test_password_schema(avdschema_factory, schema, expected_raise):
    """
    Tests to verify that only acceptable password schema are accepted
    """
    with expected_raise:
        avdschema_factory(schema)
