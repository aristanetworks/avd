# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from copy import deepcopy
from functools import lru_cache

from deepmerge import conservative_merger

from ..store import create_store


def merge_schema_from_ref(schema: dict) -> dict:
    """
    Returns a copy of the schema with any $ref resolved.

    If the referenced schema also has a $ref, that too will be resolved.

    Any child schemas will _not_ be resolved.
    """
    if "$ref" not in schema:
        return schema

    schema = deepcopy(schema)
    ref = schema.pop("$ref")
    ref_schema = merge_schema_from_ref(get_schema_from_ref(ref))
    if ref_schema["type"] != schema["type"]:
        # TODO: Consider if this should be a pyavd specific error
        raise ValueError(
            f"Incompatible schema types from ref '{ref}' ref type '{ref_schema['type']}' schema type '{schema['type']}'\nschema: {schema}\nref_schema:"
            f" {ref_schema})"
        )

    merged_schema = conservative_merger.merge(schema, ref_schema)
    return merged_schema


@lru_cache
def get_schema_from_ref(ref: str) -> dict:
    """
    Returns the schema found in the schema store using the given absolute ref.

    The ref is in the style "schema_name#/path/to/schema/element"
    """
    schema_store = create_store()

    if "#" not in ref:
        raise ValueError("Missing # in ref")

    schema_name, ref = ref.split("#", maxsplit=1)
    if schema_name not in schema_store:
        raise KeyError(f"Invalid schema name '{schema_name}'")

    schema = schema_store[schema_name]
    path = ref.split("/")
    ref_schema = walk_schema(schema, path)
    if ref_schema is None:
        raise KeyError(f"Unable to resolve schema ref '{ref}' for schema '{schema_name}'")

    return ref_schema


def walk_schema(schema: dict, path: list[str]) -> dict | None:
    """
    Paths the dictionary along the given path. Empty steps are ignored.

    If the path is invalid it will return None, sso the calling function can raise an error with the original schema ref.
    """
    if not path:
        return schema

    step = path.pop(0)
    if step == "":
        return walk_schema(schema, path)

    if step in schema:
        return walk_schema(schema[step], path)

    return None
