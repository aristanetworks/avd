from __future__ import absolute_import, division, print_function

__metaclass__ = type

import copy
import json
import os

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

script_dir = os.path.dirname(__file__)
with open(f"{script_dir}/avd_meta_schema.json", "r", encoding="utf-8") as file:
    AVD_META_SCHEMA = json.load(file)


def _keys(validator, keys: dict, resolved_schema: dict, schema: dict):
    # Don't run resolver if $ref is part of the schema.
    # Instead $ref resolver will pop $ref and run all resolvers.
    if "$ref" in schema:
        return

    # Resolve the child schemas
    for key, childschema in keys.items():
        yield from validator.descend(
            resolved_schema["keys"][key],
            childschema,
            path=key,
            schema_path=key,
        )


def _dynamic_keys(validator, dynamic_keys: dict, resolved_schema: dict, schema: dict):
    # Don't run resolver if $ref is part of the schema.
    # Instead $ref resolver will pop $ref and run all resolvers.
    if "$ref" in schema:
        return

    # Resolve the child schemas
    for key, childschema in dynamic_keys.items():
        yield from validator.descend(
            resolved_schema["dynamic_keys"][key],
            childschema,
            path=key,
            schema_path=key,
        )


def _items(validator, items: dict, resolved_schema: dict, schema: dict):
    # Don't run resolver if $ref is part of the schema.
    # Instead $ref resolver will pop $ref and run all resolvers.
    if "$ref" in schema:
        return

    # Resolve the child schema
    yield from validator.descend(
        resolved_schema["items"],
        items,
        path=0,
        schema_path=0,
    )


def _ref(validator, ref, resolved_schema: dict, schema: dict):
    """
    This function resolves the $ref referenced schema,
    then merges with any schema defined at the same level
    Then performs other actions on the resolved+merged schema.

    Since this will run all resolve tasks on the same level,
    a check for $ref has been added to the other resolvers, to
    avoid duplicate resolving (and duplicate errors)

    This is the only function where the schema actully changes,
    so this is also where the resolved_schema is updated.
    """
    scope, resolved = validator.resolver.resolve(ref)
    validator.resolver.push_scope(scope)
    merged_schema = copy.deepcopy(resolved)
    always_merger.merge(merged_schema, schema)
    merged_schema.pop("$ref", None)

    resolved_schema.update(copy.deepcopy(merged_schema))

    try:
        yield from validator.descend(resolved_schema, merged_schema)
    finally:
        validator.resolver.pop_scope()


"""
AvdSchemaResolver is used to resolve $ref in AVD Schemas.

It is used to generate full documentation convering all nested schemas.

Since we return generators, we cannot return the resolved schema.
Instead we use the "instance" of jsonschema - the variable normally holding
the data to be validated - called "resolved_schema" above.
The "resolved_schema" must contain a copy of the original schema, and then
the $ref resolver will merge in the resolved schema and do in-place update.
"""
if JSONSCHEMA_IMPORT_ERROR or DEEPMERGE_IMPORT_ERROR:
    AvdSchemaResolver = None
else:
    AvdSchemaResolver = jsonschema.validators.create(
        meta_schema=AVD_META_SCHEMA,
        validators={
            "$ref": _ref,
            "items": _items,
            "keys": _keys,
            "dynamic_keys": _dynamic_keys,
        },
    )
