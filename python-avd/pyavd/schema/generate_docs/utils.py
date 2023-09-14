# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..metaschema.meta_schema_model import AristaAvdSchema, AvdSchemaField


def list_tables(schema: AristaAvdSchema) -> set[str]:
    """
    Returns list of tables to render.
    """
    return schema._descendant_tables


def render_schema_field(target_table: str | None, schema: AvdSchemaField) -> bool:
    """Returns boolean indicating whether this field should be rendered in the targeted table"""
    if not schema._path:
        # Always render the root dict. Actually the root dict will not be rendered as a field, but we need this to render the children.
        return True

    if target_table is None:
        # Always render a field if there is no target table.
        # Without a target table all keys should be included.
        # print("no target_table")
        return True

    if target_table in schema._descendant_tables:
        # Always render the field if a descendant field has the target table
        # print("descending table found", schema._key)
        return True

    if schema._is_primary_key:
        # Always render the field if it is the primary key in a list of dicts.
        # print("primary_key found", schema._key)
        return True

    if schema._table and target_table != schema._table:
        # Target table mismatches specifically set table name.
        # print("mismatching table", target_table, schema._table)
        return False

    # Render the key if none of the above match.
    # The key is likely just a child of something else
    # print("allowed key", schema._key)
    return True
