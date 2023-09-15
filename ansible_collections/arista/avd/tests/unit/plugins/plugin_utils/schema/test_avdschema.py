# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import absolute_import, division, print_function

__metaclass__ = type

import os

import pytest
import yaml
from deepmerge import always_merger

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AvdValidationError
from ansible_collections.arista.avd.plugins.plugin_utils.schema.avdschema import DEFAULT_SCHEMA, AvdSchema
from ansible_collections.arista.avd.plugins.plugin_utils.schema.default_schemas import DEFAULT_SCHEMAS

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


class TestAvdSchema:
    def test_avd_schema_init_without_schema(self):
        avdschema = AvdSchema()
        assert isinstance(avdschema, AvdSchema)
        assert avdschema._schema == DEFAULT_SCHEMA

    @pytest.mark.parametrize("TEST_SCHEMA", VALID_TEST_SCHEMAS)
    def test_avd_schema_init_with_schema(self, TEST_SCHEMA):
        avdschema = AvdSchema(TEST_SCHEMA)
        assert isinstance(avdschema, AvdSchema)
        assert avdschema._schema == TEST_SCHEMA

    def test_avd_schema_init_with_invalid_schema(self):
        with pytest.raises(AvdValidationError):
            AvdSchema(INVALID_SCHEMA)

    @pytest.mark.parametrize("TEST_SCHEMA", VALID_TEST_SCHEMAS)
    def test_avd_schema_validate_schema(self, TEST_SCHEMA):
        try:
            for validation_error in AvdSchema().validate_schema(TEST_SCHEMA):
                assert False, f"Validation Error '{validation_error.message}' returned"
        except Exception as e:
            assert False, f"AvdSchema().validate_schema(TEST_SCHEMA) raised an exception: {e}"
        assert True

    def test_avd_schema_validate_invalid_schema(self):
        try:
            for validation_error in AvdSchema().validate_schema(INVALID_SCHEMA):
                assert isinstance(validation_error, AvdValidationError)
        except Exception as e:
            assert False, f"AvdSchema().validate_schema(INVALID_SCHEMA) raised an exception: {e}"

    @pytest.mark.parametrize("TEST_DATA", TEST_DATA_SETS)
    def test_avd_schema_validate_without_schema(self, TEST_DATA):
        try:
            for validation_error in AvdSchema().validate(TEST_DATA):
                pass
        except Exception as e:
            assert False, f"AvdSchema().validate(TEST_DATA) raised an exception: {e}"
        assert True

    @pytest.mark.parametrize("TEST_SCHEMA", VALID_TEST_SCHEMAS)
    @pytest.mark.parametrize("TEST_DATA", TEST_DATA_SETS)
    def test_avd_schema_validate_with_loaded_schema(self, TEST_SCHEMA, TEST_DATA):
        try:
            for validation_error in AvdSchema(TEST_SCHEMA).validate(TEST_DATA):
                assert False, f"Validation Error '{validation_error.message}' returned"
        except Exception as e:
            assert False, f"AvdSchema(TEST_SCHEMA).validate(TEST_DATA) raised an exception: {e}"
        assert True

    @pytest.mark.parametrize("INVALID_DATA", INVALID_ACL_DATA)
    def test_avd_schema_validate_with_invalid_data(self, INVALID_DATA):
        try:
            for validation_error in AvdSchema(combined_schema).validate(INVALID_DATA):
                assert isinstance(validation_error, AvdValidationError)
        except Exception as e:
            assert False, f"AvdSchema(combined_schema).validate(INVALID_DATA) raised an exception: {e}"

    def test_avd_schema_validate_with_missing_data(self):
        with pytest.raises(TypeError):
            AvdSchema().validate()

    @pytest.mark.parametrize("TEST_SCHEMA", VALID_TEST_SCHEMAS)
    def test_avd_schema_load_valid_schema(self, TEST_SCHEMA):
        try:
            avdschema = AvdSchema()
            avdschema.load_schema(TEST_SCHEMA)
        except Exception as e:
            assert False, f"load_schema(TEST_SCHEMA) raised an exception: {e}"
        assert avdschema._schema == TEST_SCHEMA

    def test_avd_schema_load_invalid_schema(self):
        with pytest.raises(AvdValidationError):
            avdschema = AvdSchema()
            avdschema.load_schema(INVALID_SCHEMA)

    @pytest.mark.parametrize("TEST_SCHEMA", VALID_TEST_SCHEMAS)
    def test_avd_schema_extend_valid_schema(self, TEST_SCHEMA):
        expected_schema = {}
        expected_schema = always_merger.merge(expected_schema, DEFAULT_SCHEMA)
        expected_schema = always_merger.merge(expected_schema, TEST_SCHEMA)
        try:
            avdschema = AvdSchema()
            avdschema.extend_schema(TEST_SCHEMA)
        except Exception as e:
            assert False, f"extend_schema(TEST_SCHEMA) raised an exception: {e}"
        assert avdschema._schema == expected_schema

    def test_avd_schema_extend_invalid_schema(self):
        with pytest.raises(AvdValidationError):
            avdschema = AvdSchema()
            avdschema.extend_schema(INVALID_SCHEMA)

    @pytest.mark.parametrize("TEST_PATH", TEST_DATA_PATHS)
    def test_avd_schema_subschema_with_loaded_schema(self, TEST_PATH):
        try:
            avdschema = AvdSchema(combined_schema)
            subschema = avdschema.subschema(TEST_PATH)
        except Exception as e:
            assert False, f"subschema(TEST_PATH) raised an exception: {e}"
        if len(TEST_PATH) == 0:
            assert subschema == EXPECTED_SUBSCHEMAS["_empty"]
        else:
            assert subschema == EXPECTED_SUBSCHEMAS[".".join(TEST_PATH)]

    def test_avd_schema_subschema_with_ref_to_store_schemas(self):
        test_schema = {"type": "dict", "keys": {}}
        for id in DEFAULT_SCHEMAS:
            if id == "avd_meta_schema":
                continue
            test_schema["keys"][id] = {"type": "dict", "$ref": f"{id}#/"}

        avdschema = AvdSchema(test_schema)
        for id in DEFAULT_SCHEMAS:
            if id == "avd_meta_schema":
                continue
            subschema = avdschema.subschema([id])
            assert subschema.get("type") == "dict"
            assert subschema.get("keys") is not None
