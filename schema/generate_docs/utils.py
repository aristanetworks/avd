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

    - Checks every root key for it's own table, and if not defined it adds a default table name using the key.
    - Scans every root key for decendant tables.
    """
    table_names = set()

    if schema.keys:
        for key, childschema in schema.keys.items():
            if childschema._table is not None:
                table_names.add(childschema._table)
            else:
                table_names.add(key.replace("_", "-"))
            table_names.update(childschema._descendant_tables)
    if schema.dynamic_keys:
        for key, childschema in schema.dynamic_keys.items():
            if childschema._table is not None:
                table_names.add(childschema._table)
            else:
                table_names.add(key.replace("_", "-"))
            table_names.update(childschema._descendant_tables)

    return table_names


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

    if schema._table and target_table != schema._table:
        # Target table mismatches specifically set table name.
        # print("mismatching table", target_table, schema._table)
        return False

    if not schema._table and len(schema._path) == 1 and schema._key and schema._key.replace("_", "-") != target_table:
        # This is a root key and the target_table mismatches a hyphen variant of the key name.
        # print("mismatching rootkey", target_table, schema._key.replace("_", "-"))
        return False

    if schema._descendant_tables and target_table not in schema._descendant_tables:
        # Some descendant key has the target_table set, so this one should be rendered to show the path.
        # print("no descendents", target_table, schema._descendant_tables)
        return False

    # Render the key if none of the above match.
    # The key is likely just a child of something else
    # print("allowed key", schema._key)
    return True
