# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from enum import Enum
from typing import Annotated, Any, List, Literal

from pydantic import BaseModel, ConfigDict, Field, RootModel, constr


class FieldRef(RootModel):
    root: str
    (
        "Reference to Sub Schema using JSON Schema resolver. "
        "Example '#/keys/mykey' will resolve the schema for 'mykey' under the root dictionary of the current schema"
    )

    def __str__(self):
        return self.root.__str__()


class Deprecation(BaseModel):
    warning: bool = True
    "Emit deprecation warning if key is set"
    new_key: str | None = None
    "Relative path to new key"
    removed: bool | None = False
    "Support for this key has been removed"
    remove_in_version: str | None = None
    "Version in which the key will be removed"
    remove_after_date: str | None = None
    "Date after which the key will be removed in the next major version"
    url: str | None = None
    "URL detailing the deprecation and migration guidelines"


class DisplayName(RootModel):
    "Free text display name for forms and documentation (single line)"
    root: Annotated[str, constr(pattern=r"^[^\n]+$")]

    def __str__(self):
        return self.root.__str__()


class DynamicValidValues(RootModel):
    (
        "Path to variable under the parent dictionary containing valid values. "
        "Variable path use dot-notation and variable path must be relative to the parent dictionary. "
        "If an element of the variable path is a list, every list item will be unpacked. "
        "Note that this is building the schema from values in the _data_ being validated!"
    )
    root: str

    def __str__(self):
        return self.root.__str__()


class Required(RootModel):
    "Key is required"
    root: bool

    def __str__(self):
        return self.root.__str__()

    def __bool__(self):
        return self.root.__bool__()


class DocumentationOptions(BaseModel):
    "Special options used for generating documentation"
    model_config = ConfigDict(
        extra="forbid",
    )
    table: str | None = None
    (
        "Setting 'table' will allow for custom grouping of schema fields in the documentation."
        "By default each root key has it's own table. By setting the same table-value on multiple keys, they will be merged to a single table."
        "If 'table' is set on a 'child' key, all 'ancestor' keys are automatically included in the table so the full path is visible. "
        "The 'table' option is inherited to all child keys, unless specifically set on the child."
    )


class DocumentationOptionsDict(DocumentationOptions):
    "Special options used for generating documentation for dicts"
    hide_keys: bool | None = None
    (
        "Prevent keys of the dict from being displayed in the generated documentation.\n\n"
        "This is used for structured_config where we wish to avoid displaying the full "
        "eos_cli_config_gen schema everywhere."
    )


class AvdSchemaInt(BaseModel):
    class ConvertType(str, Enum):
        bool = "bool"
        str = "str"
        float = "float"

    model_config = ConfigDict(
        extra="forbid",
    )
    type: Literal["int"]
    convert_types: List[ConvertType] | None = None
    "List of types to auto-convert from. For 'int' auto-conversion is supported from 'bool' and 'str'"
    default: int | None = None
    "Default value"
    max: int | None = None
    min: int | None = None
    valid_values: List[int] | None = None
    "List of valid values"
    display_name: DisplayName | None = None
    description: Annotated[str, constr(min_length=1)] | None = None
    "Free text description for forms and documentation (multi line)"
    required: Required | None = None
    dynamic_valid_values: DynamicValidValues | None = None
    deprecation: Deprecation | None = None
    field_ref: FieldRef | None = Field(None, alias="$ref")
    documentation_options: DocumentationOptions | None = None


class AvdSchemaBool(BaseModel):
    class ConvertType(str, Enum):
        int = "int"
        str = "str"

    model_config = ConfigDict(
        extra="forbid",
    )
    type: Literal["bool"]
    convert_types: List[ConvertType] | None = None
    "List of types to auto-convert from.\n\nFor 'bool' auto-conversion is supported from 'int' and 'str'"
    default: bool | None = None
    "Default value"
    valid_values: List[bool] | None = None
    "List of valid values"
    display_name: DisplayName | None = None
    description: Annotated[str, constr(min_length=1)] | None = None
    "Free text description for forms and documentation (multi line)"
    required: Required | None = None
    dynamic_valid_values: DynamicValidValues | None = None
    deprecation: Deprecation | None = None
    field_ref: FieldRef | None = Field(None, alias="$ref")
    documentation_options: DocumentationOptions | None = None


class AvdSchemaStr(BaseModel):
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

    model_config = ConfigDict(
        extra="forbid",
    )
    type: Literal["str"]
    convert_to_lower_case: bool | None = False
    "Convert string value to lower case before performing validation"
    convert_types: List[ConvertType] | None = None
    "List of types to auto-convert from.\n\nFor 'str' auto-conversion is supported from 'bool' and 'int'"
    default: str | None = None
    "Default value"
    format: Format | None = None
    max_length: int | None = None
    min_length: int | None = None
    pattern: str | None = None
    (
        "A regular expression which will be matched on the variable value.\n\n"
        "The regular expression should be valid according to the ECMA 262 dialect.\n\n"
        "Remember to use double escapes."
    )
    valid_values: List[str] | None = None
    "List of valid values"
    display_name: DisplayName | None = None
    description: Annotated[str, constr(min_length=1)] | None = None
    "Free text description for forms and documentation (multi line)"
    required: Required | None = None
    dynamic_valid_values: DynamicValidValues | None = None
    deprecation: Deprecation | None = None
    field_ref: FieldRef | None = Field(None, alias="$ref")
    documentation_options: DocumentationOptions | None = None


class AvdSchemaList(BaseModel):
    class ConvertType(str, Enum):
        dict = "dict"
        list = "list"
        str = "str"

    model_config = ConfigDict(
        extra="forbid",
    )
    type: Literal["list"]
    convert_types: List[ConvertType] | None = None
    (
        "List of types to auto-convert from. "
        "For 'list of dicts' auto-conversion is supported from 'dict' if 'primary_key' is set on the list schema. "
        "For other list item types conversion from dict will use the keys as list items."
    )
    default: List | None = None
    "Default value"
    items: Annotated[AvdSchemaInt | AvdSchemaBool | AvdSchemaStr | AvdSchemaList | AvdSchemaDict, Field(discriminator="type")] | None = None
    "Schema for list items"
    min_length: int | None = None
    max_length: int | None = None
    primary_key: Annotated[str, constr(pattern=r"^[a-z][a-z0-9_]*$")] | None = None
    "Name of a primary key in a list of dictionaries. The configured key is implicitly required and must have unique values between the list elements."
    secondary_key: Annotated[str, constr(pattern=r"^[a-z][a-z0-9_]*$")] | None = None
    "Name of a secondary key, which is used with `convert_types:[dict]` in case of values not being dictionaries."
    display_name: DisplayName | None = None
    description: Annotated[str, constr(min_length=1)] | None = None
    "Free text description for forms and documentation (multi line)"
    required: Required | None = None
    deprecation: Deprecation | None = None
    field_ref: FieldRef | None = Field(None, alias="$ref")
    documentation_options: DocumentationOptions | None = None


class AvdSchemaDict(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    type: Literal["dict"]
    default: dict[str, Any] | None = None
    "Default value"
    keys: dict[
        # TODO: Allowing upper case until we have deprecated and removed the remaining upper case vars.
        Annotated[str, constr(pattern=r"^[a-zA-Z][a-zA-Z0-9_]*$")],
        Annotated[AvdSchemaInt | AvdSchemaBool | AvdSchemaStr | AvdSchemaList | AvdSchemaDict, Field(discriminator="type")],
    ] | None = None
    (
        "Dictionary of dictionary-keys in the format `{<keyname>: {<schema>}}`. "
        "`keyname` must use snake_case. "
        "`schema` is the schema for each key. This is a recursive schema, so the value must conform to AVD Schema."
    )
    dynamic_keys: dict[
        Annotated[str, constr(pattern=r"^[a-z][a-z0-9_.]*$")],
        Annotated[AvdSchemaInt | AvdSchemaBool | AvdSchemaStr | AvdSchemaList | AvdSchemaDict, Field(discriminator="type")],
    ] | None = None
    (
        "Dictionary of dynamic dictionary-keys in the format `{<variable.path>: {<schema>}}`. "
        "`variable.path` is a variable path using dot-notation and pointing to a variable under the parent dictionary containing dictionary-keys. "
        "If an element of the variable path is a list, every list item will unpacked. "
        "`schema` is the schema for each key. This is a recursive schema, so the value must conform to AVD Schema. "
        "Note that this is building the schema from values in the _data_ being validated!"
    )
    allow_other_keys: bool | None = False
    "Allow keys in the dictionary which are not defined in the schema."
    display_name: DisplayName | None = None
    description: Annotated[str, constr(min_length=1)] | None = None
    "Free text description for forms and documentation (multi line)"
    required: Required | None = None
    deprecation: Deprecation | None = None
    field_ref: FieldRef | None = Field(None, alias="$ref")
    documentation_options: DocumentationOptionsDict | None = None
    field_schema: str | None = Field(None, alias="$schema")
    field_id: str | None = Field(None, alias="$id")
    field_defs: FieldDefs | None = Field(None, alias="$defs")


class FieldDefs(RootModel):
    root: dict[
        Annotated[str, constr(pattern=r"^[a-z][a-z0-9_]*$")],
        Annotated[AvdSchemaInt | AvdSchemaBool | AvdSchemaStr | AvdSchemaList | AvdSchemaDict, Field(discriminator="type")],
    ] = Field(...)
    "Storage for reusable schema fragments"

    def __iter__(self):
        return iter(self.root)

    def __getitem__(self, item):
        return self.root[item]

    def __getattr__(self, item):
        return self.root.__getattr__(item)


class AristaAvdSchema(AvdSchemaDict):
    "Arista AVD Schema"
