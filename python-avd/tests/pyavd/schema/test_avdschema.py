# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import os

import pytest
import yaml
from deepmerge import always_merger
from pyavd._errors import AvdValidationError
from pyavd._schema.avdschema import DEFAULT_SCHEMA, AvdSchema
from pyavd._schema.avdschemaresolver import AvdSchemaResolver
from schema_tools.constants import SCHEMA_PATHS
from schema_tools.store import create_store

script_dir = os.path.dirname(__file__)
with open(f"{script_dir}/access_lists.schema.yml", "r", encoding="utf-8") as schema_file:
    acl_schema = yaml.load(schema_file, Loader=yaml.SafeLoader)
with open(f"{script_dir}/ipv6_standard_access_lists.schema.yml", "r", encoding="utf-8") as schema_file:
    ipv6_acl_schema = yaml.load(schema_file, Loader=yaml.SafeLoader)
with open(f"{script_dir}/combined.schema.yml", "r", encoding="utf-8") as schema_file:
    combined_schema = yaml.load(schema_file, Loader=yaml.SafeLoader)
with open(f"{script_dir}/acl.yml", "r", encoding="utf-8") as data_file:
    acl_test_data = yaml.load(data_file, Loader=yaml.SafeLoader)
with open(f"{script_dir}/ipv6-access-lists.yml", "r", encoding="utf-8") as data_file:
    ipv6_acl_test_data = yaml.load(data_file, Loader=yaml.SafeLoader)

INVALID_SCHEMA = {"type": "something_invalid"}

VALID_TEST_SCHEMAS = [DEFAULT_SCHEMA, acl_schema, ipv6_acl_schema, combined_schema]

combined_data = {}
always_merger.merge(combined_data, acl_test_data)
always_merger.merge(combined_data, ipv6_acl_test_data)

TEST_DATA_SETS = [{}, acl_test_data, ipv6_acl_test_data, combined_data]

TEST_DATA_PATHS = [
    [],
    ["access_lists", "name"],
    ["access_lists", "sequence_numbers", "action"],
]

# Expected responses for .subschema() when tested with TEST_DATA_PATHS
EXPECTED_SUBSCHEMAS = {
    "_empty": combined_schema,
    "access_lists.name": acl_schema["keys"]["access_lists"]["items"]["keys"]["name"],
    "access_lists.sequence_numbers.action": acl_schema["keys"]["access_lists"]["items"]["keys"]["sequence_numbers"]["items"]["keys"]["action"],
}

# Testing invalid data for "access-lists" data model
INVALID_ACL_DATA = [
    # Wrong data type (string instead of dict)
    "String",
    # Wrong data type (None instead of dict)
    None,
    # Wrong item type (None instead of dict)
    {"access_lists": [None]},
    # Missing Multiple Required keys ("name", "sequence_numbers")
    {"access_lists": [{}]},
    # Missing One Required key ("sequence_numbers")
    {"access_lists": [{"name": "name"}]},
    # Wrong type for deeply nested key (int instead of str)
    {"access_lists": [{"name": "name", "sequence_numbers": [{"sequence": 10, "action": 123}]}]},
    # Unexpected key (extra_key)
    {"access_lists": [{"extra_key": "extra_value", "name": "name", "sequence_numbers": [{"sequence": 10, "action": "permit ip any any"}]}]},
    # Duplicate primary key values (two sequence:10)
    {"access_lists": [{"name": "name", "sequence_numbers": [{"sequence": 10, "action": "permit ip any any"}, {"sequence": 10, "action": "deny ip any any"}]}]},
    # Primary key not set on one list item.
    {"access_lists": [{"name": "name", "sequence_numbers": [{"sequence": 10, "action": "permit ip any any"}, {"action": "deny ip any any"}]}]},
]


UNIQUE_KEYS_SCHEMAS = [
    {
        "type": "list",
        "unique_keys": ["key", "nested_list.nested_list_key"],
        "items": {
            "type": "dict",
            "keys": {"key": {"type": "str"}, "nested_list": {"type": "list", "items": {"type": "dict", "keys": {"nested_list_key": {"type": "int"}}}}},
        },
    }
]

UNIQUE_KEYS_VALID_DATA = [
    [
        {"key": "a", "nested_list": [{"nested_list_key": 1}, {"nested_list_key": 2}]},
        {"key": "b", "nested_list": [{"nested_list_key": 3}, {"nested_list_key": 4}]},
    ],
    [
        {"key": "a", "nested_list": [{"nested_list_key": 1}, {}]},
        {"nested_list": [{"nested_list_key": 3}, {"nested_list_key": 4}]},
    ],
    [],
    [{}],
    [{"nested_list": []}],
]

UNIQUE_KEYS_INVALID_DATA = [
    [
        {"key": "a", "nested_list": [{"nested_list_key": 1}, {"nested_list_key": 2}]},
        {"key": "b", "nested_list": [{"nested_list_key": 3}, {"nested_list_key": 3}]},
    ],
    [
        {"key": "a", "nested_list": [{"nested_list_key": 1}, {"nested_list_key": 2}]},
        {"key": "b", "nested_list": [{"nested_list_key": 1}, {"nested_list_key": 4}]},
    ],
    [
        {"key": "a", "nested_list": [{"nested_list_key": 1}, {"nested_list_key": 2}]},
        {"key": "a", "nested_list": [{"nested_list_key": 3}, {"nested_list_key": 4}]},
    ],
]


class TestAvdSchema:
    def test_avd_schema_init_without_schema(self):
        avdschema = AvdSchema()
        assert isinstance(avdschema, AvdSchema)
        assert avdschema._schema == DEFAULT_SCHEMA

    @pytest.mark.parametrize("test_schema", VALID_TEST_SCHEMAS)
    def test_avd_schema_init_with_schema(self, test_schema):
        avdschema = AvdSchema(test_schema)
        assert isinstance(avdschema, AvdSchema)
        assert avdschema._schema == test_schema

    def test_avd_schema_init_with_invalid_schema(self):
        with pytest.raises(AvdValidationError):
            AvdSchema(INVALID_SCHEMA)

    @pytest.mark.parametrize("test_schema", VALID_TEST_SCHEMAS)
    def test_avd_schema_validate_schema(self, test_schema):
        try:
            for validation_error in AvdSchema().validate_schema(test_schema):
                assert False, f"Validation Error '{validation_error.message}' returned"
        except Exception as e:  # pylint: disable=broad-exception-caught
            assert False, f"AvdSchema().validate_schema(TEST_SCHEMA) raised an exception: {e}"

    def test_avd_schema_validate_invalid_schema(self):
        try:
            for validation_error in AvdSchema().validate_schema(INVALID_SCHEMA):
                assert isinstance(validation_error, AvdValidationError)
        except Exception as e:  # pylint: disable=broad-exception-caught
            assert False, f"AvdSchema().validate_schema(INVALID_SCHEMA) raised an exception: {e}"

    @pytest.mark.parametrize("test_data", TEST_DATA_SETS)
    def test_avd_schema_validate_without_schema(self, test_data):
        try:
            list(AvdSchema().validate(test_data))
        except Exception as e:  # pylint: disable=broad-exception-caught
            assert False, f"AvdSchema().validate(TEST_DATA) raised an exception: {e}"

    @pytest.mark.parametrize("test_schema", VALID_TEST_SCHEMAS)
    @pytest.mark.parametrize("test_data", TEST_DATA_SETS)
    def test_avd_schema_validate_with_loaded_schema(self, test_schema, test_data):
        try:
            for validation_error in AvdSchema(test_schema).validate(test_data):
                assert False, f"Validation Error '{validation_error.message}' returned"
        except Exception as e:  # pylint: disable=broad-exception-caught
            assert False, f"AvdSchema(TEST_SCHEMA).validate(TEST_DATA) raised an exception: {e}"

    @pytest.mark.parametrize("invalid_data", INVALID_ACL_DATA)
    def test_avd_schema_validate_with_invalid_data(self, invalid_data):
        try:
            for validation_error in AvdSchema(combined_schema).validate(invalid_data):
                assert isinstance(validation_error, AvdValidationError)
        except Exception as e:  # pylint: disable=broad-exception-caught
            assert False, f"AvdSchema(combined_schema).validate(INVALID_DATA) raised an exception: {e}"

    @pytest.mark.parametrize("test_schema", VALID_TEST_SCHEMAS)
    def test_avd_schema_load_valid_schema(self, test_schema):
        try:
            avdschema = AvdSchema()
            avdschema.load_schema(test_schema)
        except Exception as e:  # pylint: disable=broad-exception-caught
            assert False, f"load_schema(TEST_SCHEMA) raised an exception: {e}"
        assert avdschema._schema == test_schema

    def test_avd_schema_load_invalid_schema(self):
        with pytest.raises(AvdValidationError):
            avdschema = AvdSchema()
            avdschema.load_schema(INVALID_SCHEMA)

    @pytest.mark.parametrize("test_schema", VALID_TEST_SCHEMAS)
    def test_avd_schema_extend_valid_schema(self, test_schema):
        expected_schema = {}
        expected_schema = always_merger.merge(expected_schema, DEFAULT_SCHEMA)
        expected_schema = always_merger.merge(expected_schema, test_schema)
        try:
            avdschema = AvdSchema()
            avdschema.extend_schema(test_schema)
        except Exception as e:  # pylint: disable=broad-exception-caught
            assert False, f"extend_schema(TEST_SCHEMA) raised an exception: {e}"
        assert avdschema._schema == expected_schema

    def test_avd_schema_extend_invalid_schema(self):
        with pytest.raises(AvdValidationError):
            avdschema = AvdSchema()
            avdschema.extend_schema(INVALID_SCHEMA)

    @pytest.mark.parametrize("test_path", TEST_DATA_PATHS)
    def test_avd_schema_subschema_with_loaded_schema(self, test_path):
        try:
            avdschema = AvdSchema(combined_schema)
            subschema = avdschema.subschema(test_path)
        except Exception as e:  # pylint: disable=broad-exception-caught
            assert False, f"subschema(TEST_PATH) raised an exception: {e}"
        if len(test_path) == 0:
            assert subschema == EXPECTED_SUBSCHEMAS["_empty"]
        else:
            assert subschema == EXPECTED_SUBSCHEMAS[".".join(test_path)]

    def test_avd_schema_subschema_with_ref_to_store_schemas(self):
        test_schema = {"type": "dict", "keys": {}}
        for id in SCHEMA_PATHS:
            if id == "avd_meta_schema":
                continue
            test_schema["keys"][id] = {"type": "dict", "$ref": f"{id}#"}

        # For performance reasons $ref is no longer supported at runtime.
        # The $ref must be resolved before loading the schema.
        store = create_store()
        resolved_test_schema = AvdSchemaResolver("", store).resolve(test_schema)

        avdschema = AvdSchema(resolved_test_schema)
        for id in SCHEMA_PATHS:
            if id == "avd_meta_schema":
                continue
            subschema = avdschema.subschema([id])
            assert subschema.get("type") == "dict"
            assert subschema.get("keys") is not None

    @pytest.mark.parametrize("test_schema", UNIQUE_KEYS_SCHEMAS)
    @pytest.mark.parametrize("test_data", UNIQUE_KEYS_VALID_DATA)
    def test_avd_schema_validate_unique_keys_valid_data(self, test_schema, test_data):
        try:
            for validation_error in AvdSchema(test_schema).validate(test_data):
                assert False, f"Validation Error '{validation_error.message}' returned"
        except Exception as e:  # pylint: disable=broad-exception-caught
            assert False, f"AvdSchema(UNIQUE_KEYS_SCHEMAS).validate(UNIQUE_KEYS_VALID_DATA) raised an exception: {e}"

    @pytest.mark.parametrize("test_schema", UNIQUE_KEYS_SCHEMAS)
    @pytest.mark.parametrize("invalid_data", UNIQUE_KEYS_INVALID_DATA)
    def test_avd_schema_validate_unique_keys_invalid_data(self, test_schema, invalid_data):
        try:
            validation_errors = tuple(AvdSchema(test_schema).validate(invalid_data))
            if not validation_errors:
                assert False, "did NOT fail validation"
            for validation_error in validation_errors:
                assert isinstance(validation_error, AvdValidationError)
                assert validation_error.path.endswith((".key", ".nested_list_key"))

        except Exception as e:  # pylint: disable=broad-exception-caught
            assert False, f"AvdSchema(UNIQUE_KEYS_SCHEMAS).validate(UNIQUE_KEYS_INVALID_DATA) raised an exception: {e}"
