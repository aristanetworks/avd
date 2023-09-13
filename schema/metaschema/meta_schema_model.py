# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from abc import ABC
from enum import Enum
from functools import cached_property
from typing import Annotated, Any, Generator, List, Literal

from pydantic import BaseModel, ConfigDict, Field, RootModel, constr

from schema.generate_docs.yamllinegen import YamlLine, YamlLineGenBase, YamlLineGenBool, YamlLineGenDict, YamlLineGenInt, YamlLineGenList, YamlLineGenStr

from ..generate_docs.tablerowgen import TableRow, TableRowGenBase, TableRowGenBool, TableRowGenDict, TableRowGenInt, TableRowGenList, TableRowGenStr
from .resolvemodel import resolve_model


class AvdSchemaBaseModel(BaseModel, ABC):
    class Deprecation(BaseModel):
        warning: bool = True
        """Emit deprecation warning if key is set"""
        new_key: str | None = None
        """Relative path to new key"""
        removed: bool | None = False
        """Support for this key has been removed"""
        remove_in_version: str | None = None
        """Version in which the key will be removed"""
        remove_after_date: str | None = None
        """Date after which the key will be removed in the next major version"""
        url: str | None = None
        """URL detailing the deprecation and migration guidelines"""

    model_config = ConfigDict(
        extra="forbid",
    )
    display_name: str | None = Field(None, pattern=r"^[^\n]+$")
    """Free text display name for forms and documentation (single line)"""
    description: Annotated[str, constr(min_length=1)] | None = None
    """Free text description for forms and documentation (multi line)"""
    required: bool | None = None
    """Key is required"""
    deprecation: Deprecation | None = None
    field_ref: str | None = Field(None, alias="$ref")
    """
    Reference to Sub Schema using JSON Path.
    Example 'eos_designs#/keys/mykey' will resolve the schema for 'mykey' under the root dictionary of the eos_designs schema
    """
    documentation_options: DocumentationOptions | None = None

    _table_row_generator: type[TableRowGenBase]
    _yaml_line_generator: type[YamlLineGenBase]
    _key: str | None = None
    _parent_schema: AvdSchemaField | None = None
    _is_primary_key: bool = False
    _is_first_list_key: bool = False

    @cached_property
    def _descendant_tables(self) -> set[str]:
        return set()

    @cached_property
    def _resolved_model(self) -> AvdSchemaField:
        return resolve_model(self)

    @property
    def _table(self) -> str | None:
        schema = self._resolved_model

        if schema.documentation_options is not None:
            return schema.documentation_options.table

    @property
    def _path(self) -> list[str]:
        if self._parent_schema is None:
            # The root dict
            return []

        if not self._key:
            # A list item
            return self._parent_schema._path + ["[]"]

        return self._parent_schema._path + [self._key]

    def generate_table_rows(
        self,
        target_table: str | None = None,
    ) -> Generator[TableRow]:
        """
        Yields "TableRow"s to be used in schema docs.
        The function is called recursively inside the YamlLineGen classes for passing children.

        Uses the resolve_model function to generate based on the the fully resolved schema.
        """
        yield from self._table_row_generator().generate_table_rows(
            schema=self._resolved_model,
            target_table=target_table,
        )

    def generate_yaml_lines(
        self,
        target_table: str | None = None,
    ) -> Generator[YamlLine]:
        """
        Yields "YamlLine"s to be used in schema docs.
        The function is called recursively inside the YamlLineGen classes for passing children.

        Uses the resolve_model function to generate based on the the fully resolved schema.
        """
        yield from self._yaml_line_generator().generate_yaml_lines(
            schema=self._resolved_model,
            target_table=target_table,
        )


class DocumentationOptions(BaseModel):
    """Special options used for generating documentation"""

    model_config = ConfigDict(
        extra="forbid",
    )
    table: str | None = None
    """
    Setting 'table' will allow for custom grouping of schema fields in the documentation.
    By default each root key has it's own table. By setting the same table-value on multiple keys, they will be merged to a single table.
    If 'table' is set on a 'child' key, all 'ancestor' keys are automatically included in the table so the full path is visible.
    The 'table' option is inherited to all child keys, unless specifically set on the child.
    """


class DocumentationOptionsDict(DocumentationOptions):
    """Special options used for generating documentation for dicts"""

    hide_keys: bool | None = None
    """
    Prevent keys of the dict from being displayed in the generated documentation.
    This is used for structured_config where we wish to avoid displaying the full eos_cli_config_gen schema everywhere.
    """


class AvdSchemaInt(AvdSchemaBaseModel):
    class ConvertType(str, Enum):
        bool = "bool"
        str = "str"
        float = "float"

    type: Literal["int"]
    convert_types: List[ConvertType] | None = None
    """List of types to auto-convert from. For 'int' auto-conversion is supported from 'bool' and 'str'"""
    default: int | None = None
    """Default value"""
    max: int | None = None
    min: int | None = None
    valid_values: List[int] | None = None
    """List of valid values"""
    dynamic_valid_values: str | None = None
    """
    Path to variable under the parent dictionary containing valid values.
    Variable path use dot-notation and variable path must be relative to the parent dictionary.
    If an element of the variable path is a list, every list item will be unpacked.
    Note that this is building the schema from values in the _data_ being validated!
    """

    _table_row_generator = TableRowGenInt
    _yaml_line_generator = YamlLineGenInt


class AvdSchemaBool(AvdSchemaBaseModel):
    class ConvertType(str, Enum):
        int = "int"
        str = "str"

    type: Literal["bool"]
    convert_types: List[ConvertType] | None = None
    """List of types to auto-convert from.\n\nFor 'bool' auto-conversion is supported from 'int' and 'str'"""
    default: bool | None = None
    """Default value"""
    valid_values: List[bool] | None = None
    """List of valid values"""
    dynamic_valid_values: str | None = None
    """
    Path to variable under the parent dictionary containing valid values.
    Variable path use dot-notation and variable path must be relative to the parent dictionary.
    If an element of the variable path is a list, every list item will be unpacked.
    Note that this is building the schema from values in the _data_ being validated!
    """

    _table_row_generator = TableRowGenBool
    _yaml_line_generator = YamlLineGenBool


class AvdSchemaStr(AvdSchemaBaseModel):
    class ConvertType(str, Enum):
        bool = "bool"
        int = "int"
        float = "float"

    class Format(str, Enum):
        ipv4 = "ipv4"
        ipv4_cidr = "ipv4_cidr"
        ipv6 = "ipv6"
        ipv6_cidr = "ipv6_cidr"
        ip = "ip"
        cidr = "cidr"
        mac = "mac"

    type: Literal["str"]
    convert_to_lower_case: bool | None = False
    """Convert string value to lower case before performing validation"""
    convert_types: List[ConvertType] | None = None
    """List of types to auto-convert from.\n\nFor 'str' auto-conversion is supported from 'bool' and 'int'"""
    default: str | None = None
    """Default value"""
    format: Format | None = None
    max_length: int | None = None
    min_length: int | None = None
    pattern: str | None = None
    """
    A regular expression which will be matched on the variable value.
    The regular expression should be valid according to the ECMA 262 dialect.
    Remember to use double escapes.
    """
    valid_values: List[str] | None = None
    """List of valid values"""
    dynamic_valid_values: str | None = None
    """
    Path to variable under the parent dictionary containing valid values.
    Variable path use dot-notation and variable path must be relative to the parent dictionary.
    If an element of the variable path is a list, every list item will be unpacked.
    Note that this is building the schema from values in the _data_ being validated!
    """

    _table_row_generator = TableRowGenStr
    _yaml_line_generator = YamlLineGenStr


class AvdSchemaList(AvdSchemaBaseModel):
    class ConvertType(str, Enum):
        dict = "dict"
        list = "list"
        str = "str"

    type: Literal["list"]
    convert_types: List[ConvertType] | None = None
    """
    List of types to auto-convert from.
    For 'list of dicts' auto-conversion is supported from 'dict' if 'primary_key' is set on the list schema.
    For other list item types conversion from dict will use the keys as list items.
    """
    default: List | None = None
    """Default value"""
    items: Annotated[AvdSchemaField, Field(discriminator="type")] | None = None
    """Schema for list items"""
    min_length: int | None = None
    max_length: int | None = None
    primary_key: str | None = Field(None, pattern=r"^[a-z][a-z0-9_]*$")
    """
    Name of a primary key in a list of dictionaries.
    The configured key is implicitly required and must have unique values between the list elements.
    """
    secondary_key: str | None = Field(None, pattern=r"^[a-z][a-z0-9_]*$")
    """Name of a secondary key, which is used with `convert_types:[dict]` in case of values not being dictionaries."""

    _table_row_generator = TableRowGenList
    _yaml_line_generator = YamlLineGenList

    @cached_property
    def _descendant_tables(self) -> set[str]:
        schema = self._resolved_model
        if schema.items is None:
            return set()

        descendant_tables = set()
        if schema.items._table:
            descendant_tables.add(schema.items._table)
        descendant_tables.update(schema.items._descendant_tables)

        return descendant_tables

    def model_post_init(self, __context: Any) -> None:
        """our update_child_info to set internal properties"""
        self.update_child_info()
        return super().model_post_init(__context)

    def update_child_info(self) -> None:
        """
        Set internal properties on child schema (if set):
            - _parent_schema
            - _is_first_list_key (except for dict)
        Set internal properties on grandchild schemas if child schema is a dict:
            - _is_primary_key
            - _is_first_list_key
        """
        if self.items is not None:
            self.items._parent_schema = self
            if isinstance(self.items, AvdSchemaDict) and self.items.keys:
                first_key = True
                for key, grandchildschema in self.items.keys.items():
                    if first_key:
                        grandchildschema._is_first_list_key = True
                        first_key = False

                    if self.primary_key and self.primary_key == key:
                        grandchildschema._is_primary_key = True
                        # No need to look any further if we found the primary key.
                        break
            else:
                self.items._is_first_list_key = True

            # if hasattr(self.items, "update_child_info"):
            #     self.items.update_child_info()


class AvdSchemaDict(AvdSchemaBaseModel):
    type: Literal["dict"]
    default: dict[str, Any] | None = None
    """Default value"""
    keys: dict[
        # TODO: Allowing upper case until we have deprecated and removed the remaining upper case vars.
        Annotated[str, constr(pattern=r"^[a-zA-Z][a-zA-Z0-9_]*$")],
        Annotated[AvdSchemaField, Field(discriminator="type")],
    ] | None = None
    """
    Dictionary of dictionary-keys in the format `{<keyname>: {<schema>}}`.
    `keyname` must use snake_case.
    `schema` is the schema for each key. This is a recursive schema, so the value must conform to AVD Schema.
    """
    dynamic_keys: dict[
        Annotated[str, constr(pattern=r"^[a-z][a-z0-9_.]*$")],
        Annotated[AvdSchemaField, Field(discriminator="type")],
    ] | None = None
    """
    Dictionary of dynamic dictionary-keys in the format `{<variable.path>: {<schema>}}`.
    `variable.path` is a variable path using dot-notation and pointing to a variable under the parent dictionary containing dictionary-keys.
    If an element of the variable path is a list, every list item will unpacked.
    `schema` is the schema for each key. This is a recursive schema, so the value must conform to AVD Schema.
    Note that this is building the schema from values in the _data_ being validated!
    """
    allow_other_keys: bool | None = False
    """Allow keys in the dictionary which are not defined in the schema."""
    documentation_options: DocumentationOptionsDict | None = None

    field_schema: str | None = Field(None, alias="$schema")
    field_id: str | None = Field(None, alias="$id")
    field_defs: FieldDefs | None = Field(None, alias="$defs")

    _table_row_generator = TableRowGenDict
    _yaml_line_generator = YamlLineGenDict

    @cached_property
    def _descendant_tables(self) -> set[str]:
        schema = self._resolved_model
        descendant_tables = set()
        if schema.keys:
            for childschema in schema.keys.values():
                if childschema._table:
                    descendant_tables.add(childschema._table)
                descendant_tables.update(childschema._descendant_tables)
        if schema.dynamic_keys:
            for childschema in schema.keys.values():
                if childschema._table:
                    descendant_tables.add(childschema._table)
                descendant_tables.update(childschema._descendant_tables)

        return descendant_tables

    def model_post_init(self, __context: Any) -> None:
        """our update_child_info to set internal properties"""
        self.update_child_info()
        return super().model_post_init(__context)

    def update_child_info(self) -> None:
        """
        Set internal properties on child schemas:
            - _key
            - _parent_schema
        """
        if self.keys is not None:
            for key, childschema in self.keys.items():
                childschema._key = key
                childschema._parent_schema = self
                # if hasattr(childschema, "update_child_info"):
                #     childschema.update_child_info()

        if self.dynamic_keys is not None:
            for key, childschema in self.dynamic_keys.items():
                childschema._key = f"<{key}>"
                childschema._parent_schema = self
                # if hasattr(childschema, "update_child_info"):
                #     childschema.update_child_info()


class FieldDefs(RootModel):
    root: dict[
        Annotated[str, constr(pattern=r"^[a-z][a-z0-9_]*$")],
        Annotated[AvdSchemaField, Field(discriminator="type")],
    ] = Field(...)
    """Storage for reusable schema fragments"""

    def __iter__(self):
        return iter(self.root)

    def __getitem__(self, item):
        return self.root[item]


class AristaAvdSchema(AvdSchemaDict):
    """Arista AVD Schema"""


AvdSchemaField = AvdSchemaInt | AvdSchemaBool | AvdSchemaStr | AvdSchemaList | AvdSchemaDict
"""Alias for any of the AvdSchema types"""
