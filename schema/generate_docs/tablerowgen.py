# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from abc import ABC
from typing import Generator

from pydantic import BaseModel

from ..metaschema.meta_schema_model import AvdSchemaBool, AvdSchemaDict, AvdSchemaInt, AvdSchemaList, AvdSchemaStr
from ..metaschema.resolvemodel import resolve_model


def get_table_rows(
    schema: AvdSchemaInt | AvdSchemaBool | AvdSchemaStr | AvdSchemaList | AvdSchemaDict,
    path: list[str] | None = None,
    render_table: str | None = None,
    parent_schema: AvdSchemaInt | AvdSchemaBool | AvdSchemaStr | AvdSchemaList | AvdSchemaDict | None = None,
    first_list_key: bool = False,
    inherited_table: str | None = None,
) -> Generator[TableRow]:
    """
    Detects schema type and yields TableRows using the relevant TableRowGen classes
    The function is called recursively inside the TableRowGen classes for passing children.
    """

    if isinstance(schema, AvdSchemaBool):
        doc_table_gen = TableRowGenBool()
    elif isinstance(schema, AvdSchemaDict):
        doc_table_gen = TableRowGenDict()
    elif isinstance(schema, AvdSchemaInt):
        doc_table_gen = TableRowGenInt()
    elif isinstance(schema, AvdSchemaList):
        doc_table_gen = TableRowGenList()
    elif isinstance(schema, AvdSchemaStr):
        doc_table_gen = TableRowGenStr()
    else:
        raise TypeError(f"Unknown type {type(schema)}\nschema {schema}\nparent_schema {parent_schema}")

    # Use the _resolved_model property which contains the model covering the fully resolved schema
    yield from doc_table_gen.get_table_rows(resolve_model(schema), path, render_table, parent_schema, first_list_key, inherited_table)


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
    Provides the method "get_table_rows" to build documentation tables
    """

    def get_table_rows(
        self,
        schema: AvdSchemaInt | AvdSchemaBool | AvdSchemaStr | AvdSchemaList | AvdSchemaDict,
        path: list[str] | None = None,
        render_table: str | None = None,
        parent_schema: AvdSchemaInt | AvdSchemaBool | AvdSchemaStr | AvdSchemaList | AvdSchemaDict | None = None,
        first_list_key: bool = False,
        inherited_table: str | None = None,
    ) -> Generator[TableRow]:
        self.schema = schema
        self.path = path or []
        self.parent_schema = parent_schema
        self.render_table = render_table
        self.first_list_key = first_list_key
        self.set_table(inherited_table)

        if path:
            if render_table and self.table != render_table:
                # Skip this field if table is set and it doesn't match the render_table.
                # print(f"skipping row for path {path} since schema table '{self.table}' does not match '{render_table}'")
                return

            yield TableRow(
                key=self.render_key(),
                type=self.render_type(),
                required=self.render_required(),
                default=self.render_default(),
                restrictions=self.render_restrictions(),
                description=self.render_description(),
            )

        yield from self.render_children()

    def set_table(self, inherited_table: str | None):
        if self.schema.documentation_options is not None:
            self.table = getattr(self.schema.documentation_options, "table", None) or inherited_table
        else:
            self.table = inherited_table

    def get_indentation(self) -> str:
        """
        Indentation is two spaces for dicts and 4 spaces for lists (so the hyphen will be indented 2)
        """
        indentation_count = (len(self.path) - 1) * 2 + self.path.count("[]") * 2
        i = "&nbsp;"  # Indentation character
        if self.first_list_key:
            return i * (indentation_count - 2) + "-" + i

        return i * indentation_count

    def get_key(self) -> str:
        """
        Get key from path
        """
        return self.path[-1]

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
        path = ".".join(self.path)
        return f'[<samp>{self.get_indentation()}{self.get_key()}</samp>](## "{path}"){self.get_deprecation_label()}'

    def render_type(self) -> str:
        """
        Renders markdown for "type" field including mouse-over and deprecation label with color.
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
        Should render markdown for "required" field including mouse-over and deprecation label with color.
        """
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

    def render_children(self) -> Generator:
        """Noop for classes without children. Overload in subclasses  for dict and list."""
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
        restrictions.extend((super().render_restrictions() or "").split("<br>"))

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
        restrictions.extend((super().render_restrictions() or "").split("<br>"))
        if self.schema.pattern is not None:
            restrictions.append(f"Pattern: {self.schema.pattern}")

        return "<br>".join(restrictions) or None


class TableRowGenList(TableRowGenBase):
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
        restrictions.extend((super().render_restrictions() or "").split("<br>"))

        return "<br>".join(restrictions) or None

    def render_children(self) -> Generator[TableRow]:
        """yields TableRow from each child class"""
        if not self.schema.items:
            return

        if getattr(self.schema.items, "keys", None):
            first_list_key = True
            for key, child_schema in self.schema.items.keys.items():
                yield from get_table_rows(
                    schema=child_schema,
                    path=self.path + ["[]", key],
                    render_table=self.render_table,
                    parent_schema=self.schema,
                    first_list_key=first_list_key,
                    inherited_table=self.table,
                )
                first_list_key = False
        else:
            type_str = rf"\<{self.schema.items.type}\>"
            yield from get_table_rows(
                schema=self.schema.items,
                path=self.path + [type_str],
                render_table=self.render_table,
                parent_schema=self.schema,
                first_list_key=True,
                inherited_table=self.table,
            )


class TableRowGenDict(TableRowGenBase):
    def render_required(self) -> str | None:
        """
        Render markdown for "required" field including mouse-over and deprecation label with color.
        """
        key = self.path[-1]
        if self.parent_schema and getattr(self.parent_schema, "primary_key", None) == key:
            return "Required, Unique"
        if self.schema.required:
            return "Required"

    def render_children(self) -> Generator[TableRow]:
        """yields TableRow from each child class"""

        if self.schema.documentation_options is not None and self.schema.documentation_options.hide_keys:
            # Skip generating table fields for children, if "hide_keys" is set.
            # print(f"Skipping path {self.path} since hide_keys is set")
            return

        if self.schema.keys:
            for key, child_schema in self.schema.keys.items():
                yield from get_table_rows(
                    schema=child_schema,
                    path=self.path + [key],
                    render_table=self.render_table,
                    parent_schema=self.schema,
                    inherited_table=self.table,
                )

        if self.schema.dynamic_keys:
            for key, child_schema in self.schema.dynamic_keys.items():
                yield from get_table_rows(
                    schema=child_schema,
                    path=self.path + [key],
                    render_table=self.render_table,
                    parent_schema=self.schema,
                    inherited_table=self.table,
                )
