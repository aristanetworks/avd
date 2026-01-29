# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

from yaml import load as yaml_load

try:
    from yaml import CSafeLoader as SafeLoader
except ImportError:
    from yaml import SafeLoader

if TYPE_CHECKING:
    from schema_tools.metaschema.meta_schema_model import AristaAvdSchema


class CustomGlossaryEntry:
    """Simple class to represent a custom glossary entry from YAML file."""

    def __init__(self, term: str, description: str) -> None:
        self.term = term
        self.description = description

    def __str__(self) -> str:
        """Render as markdown."""
        lines = [f"### {self.term}\n"]
        if self.description:
            lines.append(f"{self.description}\n")
        return "\n".join(lines)


def load_custom_glossary_entries(custom_glossary_path: Path) -> list[CustomGlossaryEntry]:
    """
    Load custom glossary entries from a YAML file.

    Args:
        custom_glossary_path: Path to the custom glossary YAML file

    Returns:
        List of CustomGlossaryEntry objects

    Expected YAML format:
        - term: "Term Name"
          description: |
            Description text
    """
    if not custom_glossary_path.exists():
        return []

    with custom_glossary_path.open(mode="r", encoding="UTF-8") as file:
        data = yaml_load(file, Loader=SafeLoader)

    if not data or not isinstance(data, list):
        return []

    custom_entries = []
    for item in data:
        if isinstance(item, dict) and "term" in item and "description" in item:
            custom_entries.append(CustomGlossaryEntry(term=item["term"], description=item["description"]))

    return custom_entries


def get_consolidated_glossary(schemas: dict[str, AristaAvdSchema], custom_glossary_path: Path | None = None) -> str:
    """
    Generate a consolidated glossary from multiple schemas and custom entries.

    Args:
        schemas: Dictionary mapping schema names to AristaAvdSchema objects
        custom_glossary_path: Optional path to custom glossary YAML file
    """
    all_entries = []

    # Collect entries from all schemas
    for schema_name, schema in schemas.items():
        for entry in schema._generate_glossary_entries(target_table=None):
            all_entries.append(entry)

    # Load and merge custom glossary entries
    if custom_glossary_path:
        custom_entries = load_custom_glossary_entries(custom_glossary_path)
        all_entries.extend(custom_entries)

    if not all_entries:
        return "# Glossary\n\nNo glossary entries found.\n"

    # Sort entries alphabetically by term
    sorted_entries = sorted(all_entries, key=lambda e: e.term.lower())

    # Build markdown
    lines = ["# Glossary\n"]

    # Add all entries
    for entry in sorted_entries:
        lines.append(str(entry))

    return "\n".join(lines)


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

    return "\n".join(lines)
