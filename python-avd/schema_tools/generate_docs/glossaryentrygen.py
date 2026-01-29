# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel

from .utils import render_schema_field

if TYPE_CHECKING:
    from collections.abc import Generator

    from schema_tools.metaschema.meta_schema_model import AvdSchemaField


class GlossaryEntry(BaseModel):
    """
    Dataclass for one glossary entry.

    Content is markdown formatted so it can be rendered directly.
    """

    term: str
    """The term/key name to display in the glossary"""
    type: str
    """Human-readable type (String, Integer, Boolean, List, Dictionary)"""
    path: str
    """Full path to the field (e.g., 'fabric.spine.nodes')"""
    description: str | None = None
    """Description of the field"""
    default: str | None = None
    """Default value if applicable"""
    valid_values: list[str | int | float | bool] | None = None
    """List of valid values if applicable"""
    deprecated: bool = False
    """Whether this field is deprecated"""

    def __str__(self) -> str:
        """Render as markdown."""
        lines = [f"### {self.term}\n"]

        if self.description:
            lines.append(f"{self.description}\n")

        return "\n".join(lines)


class GlossaryEntryGenBase:
    """
    Base class to be used with schema pydantic models.

    Provides the method "generate_glossary_entries" used to build glossary documentation.

    Sub-classed per schema type to generate type-specific documentation.
    """

    def generate_glossary_entries(
        self,
        schema: AvdSchemaField,
        target_table: str | None = None,
    ) -> Generator[GlossaryEntry]:
        """
        Yields GlossaryEntry for this schema field if the field should be included in the glossary.

        Recursively walks children if applicable (only for lists and dicts).

        If target_table is None, includes all fields (consolidated glossary).
        If target_table is set, only includes fields from that table.
        """
        self.schema = schema
        self.target_table = target_table

        # For consolidated glossary (target_table=None), include all fields
        # For table-specific glossary, use render_schema_field to filter by table
        should_render = target_table is None or render_schema_field(schema, target_table)

        if should_render:
            if schema._path and self._should_include_in_glossary():
                # Only render this field when there is a path (not the root dict)
                yield GlossaryEntry(
                    term=self.get_term(),
                    type=self.render_type(),
                    path=self.get_path(),
                    description=self.schema.description,
                    default=self.get_default(),
                    valid_values=self.get_valid_values(),
                    deprecated=self.schema.deprecation is not None and not self.schema.deprecation.removed,
                )

            yield from self.render_children()

    def _should_include_in_glossary(self) -> bool:
        """
        Determine if this field should be in the glossary.

        Only includes fields that explicitly have `glossary: true` in documentation_options.
        This makes the glossary opt-in only for actual data fields.
        """
        # Skip if no key (list items without keys)
        if not self.schema._key:
            return False

        # Only include if explicitly set to True
        if self.schema.documentation_options and self.schema.documentation_options.glossary is True:
            return True

        return False

    def get_term(self) -> str:
        """Returns the term to display in the glossary."""
        # Use display_name if available, otherwise format the key
        if self.schema.display_name:
            return self.schema.display_name

        # Convert key from snake_case to Title Case with spaces
        key = self.schema._key or f"<{self.schema.type}>"
        return key.replace("_", " ").title()

    def get_path(self) -> str:
        """Returns the full path to the field."""
        return ".".join(self.schema._path)

    def render_type(self) -> str:
        """Renders human-readable type."""
        type_converters = {
            "str": "String",
            "int": "Integer",
            "bool": "Boolean",
            "dict": "Dictionary",
            "list": "List",
        }
        return type_converters.get(self.schema.type, self.schema.type)

    def get_default(self) -> str | None:
        """Returns default value if applicable."""
        if hasattr(self.schema, "default") and self.schema.default is not None:
            # For complex defaults (lists/dicts), just indicate they exist
            if isinstance(self.schema.default, (list, dict)):
                return "See documentation"
            return str(self.schema.default)
        return None

    def get_valid_values(self) -> list[str | int | float | bool] | None:
        """Returns list of valid values if applicable."""
        if hasattr(self.schema, "valid_values") and self.schema.valid_values:
            # Cast to the expected type to handle variance
            return list(self.schema.valid_values)
        return None

    def render_children(self) -> Generator[GlossaryEntry]:
        """Noop for classes without children. Override in subclasses for dict and list."""
        yield from []


class GlossaryEntryGenBool(GlossaryEntryGenBase):
    """Glossary entry generator for boolean fields."""

    pass


class GlossaryEntryGenInt(GlossaryEntryGenBase):
    """Glossary entry generator for integer fields."""

    pass


class GlossaryEntryGenStr(GlossaryEntryGenBase):
    """Glossary entry generator for string fields."""

    pass


class GlossaryEntryGenList(GlossaryEntryGenBase):
    """Glossary entry generator for list fields."""

    def render_type(self) -> str:
        """Renders type with item type if available."""
        type_converters = {
            "str": "String",
            "int": "Integer",
            "bool": "Boolean",
            "dict": "Dictionary",
            "list": "List",
        }
        field_type = type_converters[self.schema.type]
        if self.schema.items:
            field_type += f", items: {type_converters[self.schema.items.type]}"
        return field_type

    def render_children(self) -> Generator[GlossaryEntry]:
        """Yields GlossaryEntry from each child class."""
        if not self.schema.items:
            return

        if getattr(self.schema.items, "keys", None):
            for child_schema in self.schema.items.keys.values():
                yield from child_schema._generate_glossary_entries(
                    target_table=self.target_table,
                )
        else:
            yield from self.schema.items._generate_glossary_entries(
                target_table=self.target_table,
            )


class GlossaryEntryGenDict(GlossaryEntryGenBase):
    """Glossary entry generator for dictionary fields."""

    def render_children(self) -> Generator[GlossaryEntry]:
        """Yields GlossaryEntry from each child class."""
        if self.schema.documentation_options and self.schema.documentation_options.hide_keys:
            # Skip generating glossary entries for children, if "hide_keys" is set.
            return

        if self.schema.dynamic_keys:
            for child_schema in self.schema.dynamic_keys.values():
                yield from child_schema._generate_glossary_entries(
                    target_table=self.target_table,
                )

        if self.schema.keys:
            for child_schema in self.schema.keys.values():
                yield from child_schema._generate_glossary_entries(
                    target_table=self.target_table,
                )


