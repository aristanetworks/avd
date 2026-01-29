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

    # Group by first letter
    grouped = defaultdict(list)
    for entry in sorted(entries, key=lambda e: e.term.lower()):
        first_letter = entry.term[0].upper()
        # Handle special characters
        if not first_letter.isalpha():
            first_letter = "#"
        grouped[first_letter].append(entry)

    # Build markdown
    lines = ["# Glossary\n"]

    # Add table of contents
    lines.append("## Table of Contents\n")
    for letter in sorted(grouped.keys()):
        lines.append(f"- [{letter}](#{letter.lower()})")
    lines.append("")

    # Add entries grouped by letter
    for letter in sorted(grouped.keys()):
        lines.append(f"## {letter}\n")
        for entry in grouped[letter]:
            lines.append(str(entry))
            lines.append("---\n")

    return "\n".join(lines)

