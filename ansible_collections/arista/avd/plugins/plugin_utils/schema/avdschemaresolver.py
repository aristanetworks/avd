# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import absolute_import, annotations, division, print_function

__metaclass__ = type

from copy import deepcopy

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError
from ansible_collections.arista.avd.plugins.plugin_utils.merge import merge
from ansible_collections.arista.avd.plugins.plugin_utils.schema.refresolver import create_refresolver

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


def _keys(validator, keys: dict, resolved_schema: dict, schema: dict):
    # Resolve the child schemas
    for key, childschema in keys.items():
        if "$ref" in childschema:
            _ref_on_child(validator, childschema["$ref"], resolved_schema["keys"][key])
        yield from validator.descend(
            resolved_schema["keys"][key],
            resolved_schema["keys"][key],
            path=key,
            schema_path=key,
        )


def _dynamic_keys(validator, dynamic_keys: dict, resolved_schema: dict, schema: dict):
    # Resolve the child schemas
    for key, childschema in dynamic_keys.items():
        if "$ref" in childschema:
            _ref_on_child(validator, childschema["$ref"], resolved_schema["dynamic_keys"][key])
        yield from validator.descend(
            resolved_schema["dynamic_keys"][key],
            resolved_schema["dynamic_keys"][key],
            path=key,
            schema_path=key,
        )


def _items(validator, items: dict, resolved_schema: dict, schema: dict):
    # Resolve the child schema
    if "$ref" in items:
        _ref_on_child(validator, items["$ref"], resolved_schema["items"])
    yield from validator.descend(
        resolved_schema["items"],
        resolved_schema["items"],
        path=0,
        schema_path=0,
    )


def _ref_on_child(validator, ref, child_schema: dict):
    """
    This function resolves the $ref referenced schema,
    then merges with any schema defined at the same level

    In place update of supplied child_schema
    """
    scope, ref_schema = validator.resolver.resolve(ref)
    ref_schema = deepcopy(ref_schema)
    child_schema.pop("$ref", None)
    merge(child_schema, ref_schema, same_key_strategy="use_existing")
    # Resolve new refs inherited from the first ref.
    if "$ref" in child_schema:
        _ref_on_child(validator, child_schema["$ref"], child_schema)


class AvdSchemaResolver:
    def __new__(cls, schema, store):
        """
        AvdSchemaResolver is used to resolve $ref in AVD Schemas.

        It is used to generate full documentation covering all nested schemas.

        Since we return generators, we cannot also return the resolved schema.
        Instead we use the "instance" in jsonschema - the variable normally holding
        the data to be validated - called "resolved_schema" above.
        The "resolved_schema" must contain a copy of the original schema, and then
        the $ref resolver will merge in the resolved schema and do in-place update.
        """
        if JSONSCHEMA_IMPORT_ERROR:
            raise AristaAvdError('Python library "jsonschema" must be installed to use this plugin') from JSONSCHEMA_IMPORT_ERROR

        ValidatorClass = jsonschema.validators.create(
            meta_schema=store["avd_meta_schema"],
            validators={
                "items": _items,
                "keys": _keys,
                "dynamic_keys": _dynamic_keys,
            },
        )

        return ValidatorClass(schema, resolver=create_refresolver(schema, store))
