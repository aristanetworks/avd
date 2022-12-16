from __future__ import absolute_import, division, print_function

__metaclass__ = type

import copy

from ansible_collections.arista.avd.plugins.filter.convert_dicts import convert_dicts
from ansible_collections.arista.avd.plugins.plugin_utils.schema.avdvalidator import AVD_META_SCHEMA
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get_all

try:
    import jsonschema
    import jsonschema._types
    import jsonschema._validators
    import jsonschema.protocols
    import jsonschema.validators
except ImportError as imp_exc:
    JSONSCHEMA_IMPORT_ERROR = imp_exc
else:
    JSONSCHEMA_IMPORT_ERROR = None

try:
    from deepmerge import always_merger
except ImportError as imp_exc:
    DEEPMERGE_IMPORT_ERROR = imp_exc
else:
    DEEPMERGE_IMPORT_ERROR = None


def _keys(validator, keys: dict, instance: dict, schema: dict):
    """
    This function performs conversion on each key with the relevant subschema
    """
    if not validator.is_type(instance, "object"):
        return

    # Don't run validator if $ref is part of the schema.
    # Instead $ref validator will pop $ref and run all validators.
    if "$ref" in schema:
        return

    # We run through all the regular keys first, to ensure that all data has been converted
    # in case some of it is referenced in "dynamic_keys" below
    yield from _resolve_and_convert_keys(validator, keys, instance, schema)

    # Compile "dynamic_keys"
    dynamic_keys = {}
    schema_dynamic_keys = schema.get("dynamic_keys", {})
    for dynamic_key, childschema in schema_dynamic_keys.items():
        resolved_keys = get_all(instance, dynamic_key)
        for resolved_key in resolved_keys:
            dynamic_keys.setdefault(resolved_key, childschema)

    yield from _resolve_and_convert_keys(validator, dynamic_keys, instance, schema)


def _resolve_and_convert_keys(validator, keys: dict, instance: dict, schema: dict):
    """
    This function is run from _keys() and should not be run elsewhere

    First time with regular keys, and next with resolved dynamic_keys
    We run through all the regular keys first, to ensure that all data has been converted
    in case some of it is referenced in "dynamic_keys"
    """

    # Run over each child key and perform resolving of $ref, data conversion before
    # descending into conversion of the child schema
    for key, childschema in keys.items():
        if key not in instance:
            # Skip key since there is nothing to convert if the key is not set in instance
            continue

        # Resolve $ref, before running schema actions below which operates on the child schema
        if "$ref" in childschema:
            scope, resolved = validator.resolver.resolve(childschema["$ref"])
            # We are not allowed to modify the resolved schema directly, so we will create a new copy
            merged_childschema = copy.deepcopy(resolved)
            always_merger.merge(merged_childschema, childschema)
            merged_childschema.pop("$ref", None)
            childschema = merged_childschema

        # Perform type conversion of the instance data for the child key if required based on "convert_types"
        if "convert_types" in childschema:
            instance[key] = _convert_types(validator, childschema["convert_types"], instance[key], childschema)

        # Descend to the child schema with instance data for the child key.
        yield from validator.descend(
            instance[key],
            childschema,
            path=key,
            schema_path=key,
        )


def _items(validator, items: dict, instance: list, schema: dict):
    """
    This function performs conversion on each item with the items subschema
    """
    if not validator.is_type(instance, "array"):
        return

    # Don't run validator if $ref is part of the schema.
    # Instead $ref validator will pop $ref and run all validators.
    if "$ref" in schema:
        return

    # Resolve $ref for items, to support schema actions below which operates on the child schema
    if "$ref" in items:
        scope, resolved = validator.resolver.resolve(items["$ref"])
        merged_childschema = copy.deepcopy(resolved)
        always_merger.merge(merged_childschema, items)
        merged_childschema.pop("$ref", None)
        items = merged_childschema

    # Perform type conversion of instance items if required based on "convert_types"
    if "convert_types" in items:
        for index, instance_item in enumerate(instance):
            instance[index] = _convert_types(validator, items["convert_types"], instance_item, items)

    # Perform regular validation of child elements.
    # Using schema ["items"] to use the original schema instead of the $ref merged one.
    for index, instance_item in enumerate(instance):
        yield from validator.descend(
            instance=instance_item,
            schema=schema["items"],
            path=index,
        )


def _ref(validator, ref: str, instance, schema: dict):
    """
    This function resolves the $ref referenced schema,
    then merges with any schema defined at the same level
    Then performs validation on the resolved+merged schema.

    Since this will run all validation tasks on the same level,
    a check for $ref has been added to the other validators, to
    avoid duplicate validation (and duplicate errors)
    """
    scope, resolved = validator.resolver.resolve(ref)
    validator.resolver.push_scope(scope)
    merged_schema = copy.deepcopy(resolved)
    always_merger.merge(merged_schema, schema)
    merged_schema.pop("$ref", None)
    try:
        yield from validator.descend(instance, merged_schema)
    finally:
        validator.resolver.pop_scope()


def _convert_types(validator, convert_types: list, instance, schema: dict):
    """
    This function performs type conversion if necessary on a single data instance.
    It is invoked for child keys during "keys" conversion and for child items during
    "items" conversion
    Returns the converted value is returned to the calling converter.
    Any conversion errors are ignored and the original value is returned
    """
    schema_type = schema.get("type")

    simple_converters = {
        "str": str,
        "int": int,
        "bool": bool,
    }

    # For simple conversions, skip conversion if the value is of the correct type
    if validator.is_type(instance, schema_type) and schema_type in simple_converters:
        return instance

    for convert_type in convert_types:
        if validator.is_type(instance, convert_type):
            if schema_type in simple_converters:
                try:
                    converted_instance = simple_converters[schema_type](instance)
                except Exception:
                    # Ignore errors and return original
                    converted_instance = instance
                    pass
                return converted_instance
            elif convert_type in ["dict", "list"] and schema_type == "list" and "primary_key" in schema:
                try:
                    converted_instance = convert_dicts(
                        instance,
                        schema["primary_key"],
                        secondary_key=schema.get("secondary_key"),
                    )
                except Exception:
                    # Ignore errors and return original
                    converted_instance = instance
                    pass
                return converted_instance
            elif convert_type == "dict" and schema_type == "list":
                try:
                    converted_instance = list(instance)
                except Exception:
                    # Ignore errors and return original
                    converted_instance = instance
                    pass
                return converted_instance
    return instance


def _is_float(validator, instance):
    return isinstance(instance, float)


"""
AvdDataConverter is used to convert AVD Data Types based on schema options.
We have extra type checkers not covered by the AVD_META_SCHEMA (array, boolean etc)
since the same TypeChecker is used by the converters themselves.
"""
if JSONSCHEMA_IMPORT_ERROR or DEEPMERGE_IMPORT_ERROR:
    AvdDataConverter = None
else:
    AvdDataConverter = jsonschema.validators.create(
        meta_schema=AVD_META_SCHEMA,
        validators={"$ref": _ref, "items": _items, "keys": _keys},
        type_checker=jsonschema.TypeChecker(
            {
                "any": jsonschema._types.is_any,
                "array": jsonschema._types.is_array,
                "boolean": jsonschema._types.is_bool,
                "integer": jsonschema._types.is_integer,
                "object": jsonschema._types.is_object,
                "null": jsonschema._types.is_null,
                "None": jsonschema._types.is_null,
                "number": jsonschema._types.is_number,
                "string": jsonschema._types.is_string,
                "dict": jsonschema._types.is_object,
                "str": jsonschema._types.is_string,
                "bool": jsonschema._types.is_bool,
                "list": jsonschema._types.is_array,
                "int": jsonschema._types.is_integer,
                "float": _is_float,
            }
        ),
    )
