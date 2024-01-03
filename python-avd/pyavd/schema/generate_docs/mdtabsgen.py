# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from textwrap import indent

from ..constants import LICENSE_HEADER
from ..metaschema.meta_schema_model import AristaAvdSchema
from .tablegen import get_table
from .yamlgen import get_yaml


def get_md_tabs(schema: AristaAvdSchema, target_table: str | None = None) -> str:
    """
    Generate the content of a markdown file with mkdocs tabs containing documentation
    of of the schema optionally filtered using "target_table".

    - Table tab contains a markdown table.
    - YAML tab contains a markdown code block with YAML.
    """
    return f"""\
<!--
{indent(LICENSE_HEADER, "  ~ ")}
  -->
=== "Table"

{indent(get_table(schema, target_table), "    ")}
=== "YAML"

{indent(get_yaml(schema, target_table), "    ")}\
"""
