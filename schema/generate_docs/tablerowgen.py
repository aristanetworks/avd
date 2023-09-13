# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from abc import ABC
from typing import TYPE_CHECKING, Generator

from pydantic import BaseModel

from .utils import render_schema_field

if TYPE_CHECKING:
    from ..metaschema.meta_schema_model import AvdSchemaField


class TableRow(BaseModel):
    """
    Dataclass for one table row.
    Content is markdown formatted so it can be rendered directly.
    """

    key: str
    type: str
    required: str | None = None
    default: str | None = None
    restrictions: str | None = None
    description: str | None = None

    def __str__(self):
        return f"| {self.key} | {self.type} | {self.required or ''} | {self.default or ''} | {self.restrictions or ''} | {self.description or ''} |"


class TableRowGenBase(ABC):
    """
    Base class to be used with schema pydantic models.
    Provides the method "generate_table_rows" to build documentation tables
    """

    def generate_table_rows(
        self,
        schema: AvdSchemaField,
        target_table: str | None = None,
    ) -> Generator[TableRow]:
        self.schema = schema
        self.target_table = target_table

        if render_schema_field(target_table, schema):
            if schema._path:
                # Only render this field when there is a path (not the root dict), but always render children.

                yield TableRow(
                    key=self.render_key(),
                    type=self.render_type(),
                    required=self.render_required(),
                    default=self.render_default(),
                    restrictions=self.render_restrictions(),
                    description=self.render_description(),
                )

            yield from self.render_children()

    def get_indentation(self) -> str:
        """
        Indentation is two spaces for dicts and 4 spaces for lists (so the hyphen will be indented 2)
        """
        indentation_count = len(self.schema._path) * 2 - 2
        if not self.schema._key:
            # this is a flat list item so path is one shorter than for dict. So we add 2 to the indentation
            indentation_count += 2

        i = "&nbsp;"  # Indentation character
        if self.schema._is_first_list_key:
            return i * (indentation_count - 2) + "-" + " "  # Using space as last indentation to match legacy behavior

        return i * indentation_count

    def get_deprecation_label(self) -> str | None:
        if self.schema.deprecation is None:
            return ""

        if self.schema.deprecation.removed:
            label = "removed"
        else:
            label = "deprecated"

        return f' <span style="color:red">{label}</span>'

    def get_deprecation_description(self) -> str | None:
        if self.schema.deprecation is None:
            return ""

        descriptions = []
        if self.schema.deprecation.removed:
            descriptions.append("This key was removed.")
            removed_verb = "was"
        else:
            descriptions.append("This key is deprecated.")
            removed_verb = "will be"

        if self.schema.deprecation.remove_in_version is not None:
            descriptions.append(f"Support {removed_verb} removed in AVD version {self.schema.deprecation.remove_in_version}.")
        elif self.schema.deprecation.remove_after_date is not None:
            descriptions.append(f"Support {removed_verb} removed in the first major AVD version released after {self.schema.deprecation.remove_after_date}.")
        elif self.schema.deprecation.removed:
            descriptions.append("Support was removed in AVD.")

        if self.schema.deprecation.new_key is not None:
            descriptions.append(f"Use <samp>{self.schema.deprecation.new_key}</samp> instead.")

        if self.schema.deprecation.url is not None:
            descriptions.append(f"See [here]({self.schema.deprecation.url}) for details.")

        description = " ".join(descriptions)
        return f'<span style="color:red">{description}</span>'

    def render_key(self) -> str:
        """
        Renders markdown for "key" field including mouse-over and deprecation label with color.
        """
        path = ".".join(self.schema._path)
        if self.schema._key:
            key = self.schema._key
        else:
            key = f"&lt;{self.schema.type}&gt;"

        return f'[<samp>{self.get_indentation()}{key}</samp>](## "{path}"){self.get_deprecation_label()}'

    def render_type(self) -> str:
        """
        Renders markdown for "type" field.
        """
        type_converters = {
            "str": "String",
            "int": "Integer",
            "bool": "Boolean",
            "dict": "Dictionary",
            "list": "List",
        }
        return type_converters[self.schema.type]

    def render_required(self) -> str | None:
        """
        Render markdown for "required" field.
        """
        if self.schema._is_primary_key:
            return "Required, Unique"
        if self.schema.required:
            return "Required"

    def render_default(self) -> str | None:
        """
        Should render markdown for "default" field.
        """
        if self.schema.default is not None:
            if isinstance(self.schema.default, (list, dict)) and len(self.schema.default) > 1:
                return "See (+) on YAML tab"

            return f"`{self.schema.default}`"

    def render_description(self) -> str | None:
        """
        Renders markdown for "description" field including deprecation text with color.
        """
        descriptions = []
        if self.schema.description:
            descriptions.append(self.schema.description.replace("\n", "<br>"))
        if deprecation := self.get_deprecation_description():
            descriptions.append(deprecation)
        return " ".join(descriptions) or None

    def render_children(self) -> Generator[TableRow]:
        """Noop for classes without children. Overload in subclasses for dict and list."""
        yield from []

    def render_restrictions(self) -> str | None:
        """
        Renders markdown for "restrictions" field as a multiline text compatible with a markdown table cell.

        Only covers generic restrictions. Should be overloaded in type specific subclasses.
        """
        restrictions = []
        valid_values = []
        if getattr(self.schema, "dynamic_valid_values", None) is not None:
            valid_values.append(f"<value(s) of {self.schema.dynamic_valid_values}>")

        if getattr(self.schema, "valid_values", None) is not None:
            valid_values.extend(self.schema.valid_values)

        if valid_values:
            restrictions.append("Valid Values:")
            restrictions.extend(f"- <code>{valid_value}</code>" for valid_value in valid_values)

        return "<br>".join(restrictions) or None


class TableRowGenBool(TableRowGenBase):
    pass


class TableRowGenInt(TableRowGenBase):
    def render_restrictions(self) -> str | None:
        """
        Renders markdown for "restrictions" field as a multiline text compatible with a markdown table cell.

        Leverages common restrictions from base class.
        """
        restrictions = []
        if self.schema.min is not None:
            restrictions.append(f"Min: {self.schema.min}")
        if self.schema.max is not None:
            restrictions.append(f"Max: {self.schema.max}")

        if base_restrictions := super().render_restrictions():
            restrictions.extend(base_restrictions.split("<br>"))

        return "<br>".join(restrictions) or None


class TableRowGenStr(TableRowGenBase):
    def render_restrictions(self) -> str | None:
        """
        Renders markdown for "restrictions" field as a multiline text compatible with a markdown table cell.

        Leverages common restrictions from base class.
        """
        restrictions = []
        if self.schema.min_length is not None:
            restrictions.append(f"Min Length: {self.schema.min_length}")
        if self.schema.max_length is not None:
            restrictions.append(f"Max Length: {self.schema.max_length}")
        if self.schema.format is not None:
            restrictions.append(f"Format: {self.schema.format}")

        if base_restrictions := super().render_restrictions():
            restrictions.extend(base_restrictions.split("<br>"))

        if self.schema.pattern is not None:
            restrictions.append(f"Pattern: {self.schema.pattern}")

        return "<br>".join(restrictions) or None


class TableRowGenList(TableRowGenBase):
    def render_type(self) -> str:
        """
        Renders markdown for "type" field.
        """
        type_converters = {
            "str": "String",
            "int": "Integer",
            "bool": "Boolean",
            "dict": "Dictionary",
            "list": "List",
        }
        field_type = type_converters[self.schema.type]
        if self.schema.items is not None:
            field_type += f", items: {type_converters[self.schema.items.type]}"

        return field_type

    def render_restrictions(self) -> str | None:
        """
        Renders markdown for "restrictions" field as a multiline text compatible with a markdown table cell.

        Leverages common restrictions from base class.
        """
        restrictions = []
        if self.schema.min_length is not None:
            restrictions.append(f"Min Length: {self.schema.min_length}")
        if self.schema.max_length is not None:
            restrictions.append(f"Max Length: {self.schema.max_length}")

        if base_restrictions := super().render_restrictions():
            restrictions.extend(base_restrictions.split("<br>"))

        return "<br>".join(restrictions) or None

    def render_children(self) -> Generator[TableRow]:
        """yields TableRow from each child class"""
        if not self.schema.items:
            return

        if getattr(self.schema.items, "keys", None):
            for child_schema in self.schema.items.keys.values():
                yield from child_schema.generate_table_rows(
                    target_table=self.target_table,
                )
        else:
            yield from self.schema.items.generate_table_rows(
                target_table=self.target_table,
            )


class TableRowGenDict(TableRowGenBase):
    def render_children(self) -> Generator[TableRow]:
        """yields TableRow from each child class"""

        if self.schema.documentation_options is not None and self.schema.documentation_options.hide_keys:
            # Skip generating table fields for children, if "hide_keys" is set.
            # print(f"Skipping path {self.path} since hide_keys is set")
            return

        if self.schema.keys:
            for child_schema in self.schema.keys.values():
                yield from child_schema.generate_table_rows(
                    target_table=self.target_table,
                )

        if self.schema.dynamic_keys:
            for child_schema in self.schema.dynamic_keys.values():
                yield from child_schema.generate_table_rows(
                    target_table=self.target_table,
                )
