# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from textwrap import indent

from ..metaschema.meta_schema_model import AristaAvdSchema
from .tablegen import get_table
from .yamlgen import get_yaml


def get_md_tabs(schema: AristaAvdSchema, target_table: str | None = None) -> str:
    return f"""\
<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

{indent(get_table(schema, target_table), "    ")}
=== "YAML"

{indent(get_yaml(schema, target_table), "    ")}\
"""
