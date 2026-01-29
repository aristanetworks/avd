# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from collections import defaultdict
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from schema_tools.metaschema.meta_schema_model import AristaAvdSchema


def get_glossary(schema: AristaAvdSchema, target_table: str | None = None) -> str:
    """
    Generate a glossary of schema fields.

    Returns markdown formatted glossary grouped alphabetically.

    Args:
        schema: The AristaAvdSchema to generate glossary from
        target_table: Optional filter to only include fields from a specific documentation table
    """
    entries = []

    # Collect all glossary entries
    for entry in schema._generate_glossary_entries(target_table=target_table):
        entries.append(entry)

    if not entries:
        return "# Glossary\n\nNo glossary entries found.\n"

    # Sort entries alphabetically
    sorted_entries = sorted(entries, key=lambda e: e.term.lower())

    # Build markdown
    lines = ["# Glossary\n"]

    # Add all entries without letter grouping
    for entry in sorted_entries:
        lines.append(str(entry))
        lines.append("---\n")

    return "\n".join(lines)

