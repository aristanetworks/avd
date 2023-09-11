# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from ..constants import STORE
from ..metaschema.meta_schema_model import AristaAvdSchema
from .tablerowgen import get_table_rows

TABLE_HEADER = [
    "| Variable | Type | Required | Default | Value Restrictions | Description |",
    "| -------- | ---- | -------- | ------- | ------------------ | ----------- |",
]


def get_table(schema_name: str, table_name: str | None = None) -> str:
    """
    Returns one markdown table either containing all keys of the given schema or only a subset if "table_name" is set.
    """
    if schema_name not in STORE:
        raise KeyError(f"Invalid schema name '{schema_name}'")

    pydantic_schema = AristaAvdSchema(**STORE[schema_name])
    lines = [*TABLE_HEADER]
    lines.extend(str(row) for row in get_table_rows(pydantic_schema, render_table=table_name))
    lines.append("")  # Add final newline
    return "\n".join(lines)
