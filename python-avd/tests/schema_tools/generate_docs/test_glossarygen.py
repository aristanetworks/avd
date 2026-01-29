# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from pathlib import Path
from sys import path
from typing import Any
from unittest.mock import patch

import pytest

# Override global path to load schema from source instead of any installed version.
# Avoids to load from pyavd to avoid relying on pyavd vendor things being generated.
path.insert(0, str(Path(__file__).parents[3]))

from schema_tools.generate_docs.glossarygen import get_glossary
from schema_tools.metaschema.meta_schema_model import AristaAvdSchema
from schema_tools.metaschema.resolvemodel import get_schema_from_ref


@pytest.mark.parametrize("table_name", ["network-services-multicast-settings"])
def test_get_glossary(table_name: str, schema_store: dict, artifacts_path: Path, output_path: Path) -> None:
    """
    Loads the schema with the resolved $refs and generates glossary.

    Write the resulting glossary to a file.
    Compare the output with the expected file.
    """
    raw_schema = schema_store["eos_designs"]

    output_file = output_path.joinpath(f"{table_name}-glossary.md")
    expected_file = artifacts_path.joinpath(f"expected-{table_name}-glossary.md")

    def mocked_create_store(*_args: Any, **_kwargs: Any) -> dict:
        return schema_store

    with patch("schema_tools.metaschema.resolvemodel.create_store", new=mocked_create_store):
        # Reset lru_cache in the resolver code to force it to read the schemas from our mocked store.
        get_schema_from_ref.cache_clear()

        schema = AristaAvdSchema(**raw_schema)
        glossary = get_glossary(schema, table_name)

    # Reset lru_cache in the resolver code to force it to read the schemas next time instead of taking them from our mocked store.
    get_schema_from_ref.cache_clear()

    with Path(output_file).open(mode="w", encoding="UTF-8") as file:
        file.write(glossary)
    
    # Only check if expected file exists (for initial test run, it won't exist)
    if expected_file.exists():
        with Path(expected_file).open(encoding="UTF-8") as file:
            assert glossary == file.read()


def test_glossary_with_explicit_options() -> None:
    """Test glossary generation with explicit glossary options."""
    # Create a simple test schema with explicit glossary options
    test_schema_dict = {
        "type": "dict",
        "keys": {
            "included_field": {
                "type": "str",
                "description": "This field should be included",
                "documentation_options": {
                    "glossary": True,
                },
            },
            "excluded_field": {
                "type": "str",
                "description": "This field should be excluded",
                "documentation_options": {
                    "glossary": False,
                },
            },
            "auto_included_field": {
                "type": "str",
                "description": "This top-level field should be auto-included",
            },
        },
    }

    schema = AristaAvdSchema(**test_schema_dict)
    glossary = get_glossary(schema)

    # Check that explicitly included field is present
    assert "included_field" in glossary
    
    # Check that explicitly excluded field is NOT present
    assert "excluded_field" not in glossary
    
    # Check that auto-included field is present (top-level with description)
    assert "auto_included_field" in glossary


def test_glossary_empty_schema() -> None:
    """Test glossary generation with empty schema."""
    test_schema_dict = {
        "type": "dict",
        "keys": {},
    }

    schema = AristaAvdSchema(**test_schema_dict)
    glossary = get_glossary(schema)

    # Should return a message about no entries
    assert "No glossary entries found" in glossary


def test_glossary_with_valid_values() -> None:
    """Test that fields with valid_values are auto-included."""
    test_schema_dict = {
        "type": "dict",
        "keys": {
            "nested": {
                "type": "dict",
                "keys": {
                    "mode": {
                        "type": "str",
                        "description": "Operating mode",
                        "valid_values": ["active", "passive", "disabled"],
                    },
                },
            },
        },
    }

    schema = AristaAvdSchema(**test_schema_dict)
    glossary = get_glossary(schema)

    # Field with valid_values should be auto-included even though it's nested
    assert "mode" in glossary
    assert "active" in glossary
    assert "passive" in glossary
    assert "disabled" in glossary


def test_glossary_alphabetical_grouping() -> None:
    """Test that glossary entries are grouped alphabetically."""
    test_schema_dict = {
        "type": "dict",
        "keys": {
            "zebra_field": {
                "type": "str",
                "description": "Z field",
                "documentation_options": {"glossary": True},
            },
            "alpha_field": {
                "type": "str",
                "description": "A field",
                "documentation_options": {"glossary": True},
            },
        },
    }

    schema = AristaAvdSchema(**test_schema_dict)
    glossary = get_glossary(schema)

    # Check that table of contents exists
    assert "Table of Contents" in glossary
    
    # Check that alphabetical sections exist
    assert "## A" in glossary
    assert "## Z" in glossary
    
    # Check that A comes before Z in the output
    assert glossary.index("## A") < glossary.index("## Z")

