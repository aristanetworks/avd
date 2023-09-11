# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import json
from copy import deepcopy
from functools import lru_cache
from typing import TYPE_CHECKING

from deepmerge import always_merger

from ..constants import STORE

if TYPE_CHECKING:
    from .meta_schema_model import AvdSchemaBool, AvdSchemaDict, AvdSchemaInt, AvdSchemaList, AvdSchemaStr


def resolve_model(model: AvdSchemaInt | AvdSchemaBool | AvdSchemaStr | AvdSchemaList | AvdSchemaDict):
    if model.field_ref is None:
        return model

    model_schema = json.loads(model.model_dump_json(by_alias=True, exclude_unset=True))
    merged_schema = merge_schema_from_ref(model_schema)
    return model.__class__(**merged_schema)


def merge_schema_from_ref(schema: dict) -> dict:
    if "$ref" not in schema:
        return schema

    ref = schema.pop("$ref")
    ref_schema = merge_schema_from_ref(deepcopy(get_schema_from_ref(ref)))
    if ref_schema["type"] != schema["type"]:
        raise ValueError(
            f"Incompatible schema types from ref '{ref}' ref type '{ref_schema['type']}' schema type '{schema['type']}'\nschema: {schema}\nref_schema:"
            f" {ref_schema})"
        )

    merged_schema = always_merger.merge(ref_schema, schema)
    # if "documentation_options" in merged_schema:
    #     print(merged_schema["documentation_options"])
    return merged_schema


@lru_cache
def get_schema_from_ref(ref: str) -> dict:
    # print(f"Resolving ref '{ref}'")
    if "#" not in ref:
        raise ValueError("Missing # in ref")

    schema_name, ref = ref.split("#", maxsplit=1)
    if schema_name not in STORE:
        raise KeyError(f"Invalid schema name '{schema_name}'")

    schema = STORE[schema_name]
    path = ref.split("/")
    ref_schema = walk_schema(schema, path)
    if ref_schema is None:
        raise KeyError(f"Unable to resolve schema ref '{ref}' for schema '{schema_name}'")

    return ref_schema


def walk_schema(schema: dict, path: list[str]) -> dict:
    if not path:
        return schema

    step = path.pop(0)
    if step == "":
        # print(f"Ignoring empty step in path '{path}'")
        return walk_schema(schema, path)

    if step in schema:
        return walk_schema(schema[step], path)

    return None
