# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from pyavd._errors import AvdDeprecationWarning
from pyavd._schema.avdschema import AvdSchema

# Only adding tests that are missing in coverage from other tests within the tests/pyavd/schema folder.


def test_convert_types_for_list_items() -> None:
    schema = {"type": "list", "items": {"type": "int", "convert_types": ["str"]}}
    avdschema = AvdSchema(schema=schema)
    data = ["123", 456]
    warnings = list(avdschema.convert(data))
    assert len(warnings) == 0
    assert data == [123, 456]


def test_convert_types_for_list_items_invalid() -> None:
    schema = {"type": "list", "items": {"type": "int", "convert_types": ["str"]}}
    avdschema = AvdSchema(schema=schema)
    data = ["not an int", 456]
    warnings = list(avdschema.convert(data))
    assert len(warnings) == 0
    assert data == ["not an int", 456]


def test_to_lower_case_for_list_items() -> None:
    schema = {"type": "list", "items": {"type": "str", "convert_to_lower_case": True}}
    avdschema = AvdSchema(schema=schema)
    data = ["FoO", "baR"]
    warnings = list(avdschema.convert(data))
    assert len(warnings) == 0
    assert data == ["foo", "bar"]


def test_no_support_for_other_keys_in_structured_config() -> None:
    schema = {
        "type": "dict",
        "keys": {
            "some_key": {
                "type": "dict",
                "keys": {
                    "structured_config": {
                        "type": "dict",
                        "keys": {
                            "some_valid_key": {"type": "bool"},
                        },
                        "allow_other_keys": True,
                    }
                },
            }
        },
        "allow_other_keys": True,
    }

    avdschema = AvdSchema(schema=schema)
    data = {
        "some_key": {
            "structured_config": {
                "invalid_key_generating_warning": True,
                "_ignored": True,
            },
        },
        "allowed_without_warning": True,
    }
    warnings = list(avdschema.convert(data))
    assert len(warnings) == 1
    assert str(warnings[0]) == (
        "The input data model 'some_key.structured_config.invalid_key_generating_warning' was removed. Use '_invalid_key_generating_warning' instead."
    )


def test_deprecation_with_new_key_and_url_and_conflict() -> None:
    schema = {
        "type": "dict",
        "keys": {
            "a": {
                "type": "bool",
                "deprecation": {
                    "warning": True,
                    "new_key": "b or c",
                    "url": "avd.arista.com",
                    "remove_in_version": "1.2.3",
                },
            },
        },
    }

    avdschema = AvdSchema(schema=schema)
    data = {"a": True, "b": True}
    warnings = list(avdschema.convert(data))
    assert len(warnings) == 1
    assert str(warnings[0]) == (
        "The input data model 'a' is deprecated and cannot be used in conjunction with the new data model 'b'. "
        "This usually happens when a data model has been updated and custom structured configuration still uses the old model. "
        "See avd.arista.com for details."
    )


def test_deprecation_with_warning_false() -> None:
    schema = {
        "type": "dict",
        "keys": {
            "a": {"type": "bool", "deprecation": {"warning": False}},
        },
    }

    avdschema = AvdSchema(schema=schema)
    data = {"a": True, "b": True}
    warnings = list(avdschema.convert(data))
    assert len(warnings) == 0


def test_deprecation_removed() -> None:
    schema = {
        "type": "dict",
        "keys": {
            "a": {
                "type": "bool",
                "deprecation": {
                    "warning": True,
                    "removed": True,
                },
            },
        },
    }

    avdschema = AvdSchema(schema=schema)
    data = {"a": True, "b": True}
    warnings = list(avdschema.convert(data))
    assert len(warnings) == 1
    assert str(warnings[0]) == ("The input data model 'a' was removed.")


def test_deprecation_remove_after_date() -> None:
    schema = {
        "type": "dict",
        "keys": {
            "a": {
                "type": "bool",
                "deprecation": {
                    "warning": True,
                    "remove_after_date": "Tomorrow",
                },
            },
        },
    }

    avdschema = AvdSchema(schema=schema)
    data = {"a": True, "b": True}
    warnings = list(avdschema.convert(data))
    assert len(warnings) == 1
    warning = warnings[0]
    assert str(warning) == ("The input data model 'a' is deprecated.")
    assert isinstance(warning, AvdDeprecationWarning)
    assert warning.date == "Tomorrow"


def test_deprecation_special_new_key() -> None:
    schema = {
        "type": "dict",
        "keys": {
            "a": {
                "type": "bool",
                "deprecation": {
                    "warning": True,
                    "remove_in_version": "1.2.3",
                    "new_key": "something with space without _or_",
                },
            },
        },
    }

    avdschema = AvdSchema(schema=schema)
    data = {"a": True, "b": True}
    warnings = list(avdschema.convert(data))
    assert len(warnings) == 1
    warning = warnings[0]
    assert str(warning) == "The input data model 'a' is deprecated. Use 'something with space without _or_' instead."
    assert isinstance(warning, AvdDeprecationWarning)
    assert warning.version == "1.2.3"


def test_deprecation_with_new_key_no_conflict() -> None:
    schema = {
        "type": "dict",
        "keys": {
            "a": {
                "type": "bool",
                "deprecation": {
                    "warning": True,
                    "new_key": "b",
                },
            },
        },
    }

    avdschema = AvdSchema(schema=schema)
    data = {"a": True}
    warnings = list(avdschema.convert(data))
    assert len(warnings) == 1
    assert str(warnings[0]) == "The input data model 'a' is deprecated. Use 'b' instead."
