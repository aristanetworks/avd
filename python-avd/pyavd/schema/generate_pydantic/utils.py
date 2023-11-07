# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

from .models import StrConvertSrc

if TYPE_CHECKING:
    from ..metaschema.meta_schema_model import AvdSchemaField


def generate_class_name(class_key: str) -> str:
    """
    Generate ClassName in from class_key.

    "some_key_using_snake_case" => "SomeKeyUsingSnakeCase"
    """
    return "".join(element.capitalize() for element in class_key.split("_"))


def generate_class_name_from_ref(ref: str) -> str:
    """
    Generate ClassName in from a schema ref.

    "eos_cli_config_gen#/keys/ethernet_interfaces/items" => "EosCliConfigGen.EthernetInterfacesItem"
    "eos_cli_config_gen#/keys/router_bgp/keys/vlans/items => "EosCliConfigGen.RouterBgp.VlansItem"
    """

    if "#" not in ref:
        raise ValueError("Schema tooling only works with fully qualified refs with '<schema>#<path>' like 'eos_cli_config_gen#/'")

    # Replacing ref with only the part after #
    ref_schema, ref = ref.split("#", maxsplit=1)

    base_class_elements = [generate_class_name(ref_schema)]

    ref_elements = ref.split("/")
    for ref_index, ref_element in enumerate(ref_elements):
        if ref_element in {"", "keys", "items"}:
            continue

        if len(ref_elements) > ref_index + 1 and ref_elements[ref_index + 1] == "items":
            ref_element = f"{ref_element}_Item"

        base_class_elements.append(generate_class_name(ref_element))

    return ".".join(base_class_elements)


def get_type_hints_for_field(schema: AvdSchemaField):
    """
    Return list of type hints to apply for the given schema field.

    Kept here instead of in the PydanticSrcGen* since we sometimes need to find the hint for a child schema.

    TODO: Figure out how to get valid_values implemented in combination with convert_to_lower_case
    """
    if schema.type == "str":
        if schema.convert_types and schema.convert_to_lower_case:
            raise NotImplementedError("schema options 'convert_types' and 'convert_to_lower_case' cannot be combined")

        if schema.convert_to_lower_case:
            return ["StrToLowerCase"]
        if not schema.convert_types:
            # TODO: Change default behavior for strings to always convert from int
            return ["str"]
        if "int" in schema.convert_types and "float" in schema.convert_types:
            return ["StrAcceptingIntFloat"]
        if "float" in schema.convert_types:
            return ["StrAcceptingFloat"]
        return ["StrAcceptingInt"]

    if schema.type == "list":
        if schema.items is None:
            return ["list[Any]"]
        return [f"list[{' | '.join(get_type_hints_for_field(schema.items))}]"]

    return [schema.type]


def get_imports_from_type_hints(type_hints: list[str]) -> set[str] | None:
    """
    Returns a set with Python import statements needed for the given type hints.
    """
    imports = set()
    types_in_types_file = [
        "StrToLowerCase",
        "StrAcceptingIntFloat",
        "StrAcceptingFloat",
        "StrAcceptingInt",
    ]
    types_from_typing = ["Any", "Annotated"]
    type_hints_set = set()

    # Expand any list[<hint> | <hint>]
    for type_hint in type_hints:
        if type_hint.startswith("Annotated["):
            type_hints_set.add("Annotated")
        type_hints_set.update(type_hint.removeprefix("list[").removeprefix("Annotated[").removesuffix("]").split(" | "))

    for type_hint in type_hints_set:
        if type_hint in types_in_types_file:
            imports.add(f"from .types import {type_hint}")
        elif type_hint in types_from_typing:
            imports.add(f"from typing import {type_hint}")
    return imports or None


def get_annotations_for_field(schema: AvdSchemaField) -> list[StrConvertSrc]:
    if schema.type != "str":
        return []

    annotations = []
    annotation = StrConvertSrc(
        convert_types=schema.convert_types,
        to_lower=schema.convert_to_lower_case,
    )
    if annotation:
        annotations.append(annotation)

    return annotations
