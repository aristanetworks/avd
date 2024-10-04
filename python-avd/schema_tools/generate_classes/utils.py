# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

from .src_generators import FormatSrc, LowerSrc, MaxLenSrc, MaxSrc, MinLenSrc, MinSrc, PatternSrc, ValidValuesSrc

if TYPE_CHECKING:
    from schema_tools.metaschema.meta_schema_model import AvdSchemaField


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
        msg = "Schema tooling only works with fully qualified refs with '<schema>#<path>' like 'eos_cli_config_gen#/'"
        raise ValueError(msg)

    # Replacing ref with only the part after #
    ref_schema, ref = ref.split("#", maxsplit=1)

    base_class_elements = [generate_class_name(ref_schema)]

    ref_elements = ref.split("/")
    for ref_index, ref_element in enumerate(ref_elements):
        if ref_element in {"", "keys", "items"}:
            continue

        if len(ref_elements) > ref_index + 1 and ref_elements[ref_index + 1] == "items":
            class_name = generate_class_name(f"{ref_element}_Item")
        else:
            class_name = generate_class_name(ref_element)

        base_class_elements.append(class_name)

    return ".".join(base_class_elements)


def get_annotations_for_field(schema: AvdSchemaField) -> list[str]:
    annotations = []
    if schema.type == "str":
        if schema.convert_to_lower_case:
            # This *must* come first to ensure we lower the value before further validation.
            annotations.append(LowerSrc())
        if schema.min_length:
            annotations.append(MinLenSrc(schema.min_length))
        if schema.max_length:
            annotations.append(MaxLenSrc(schema.max_length))
        if schema.format:
            annotations.append(FormatSrc(schema.format))
        if schema.pattern:
            annotations.append(PatternSrc(schema.pattern))
        if schema.valid_values:
            annotations.append(ValidValuesSrc(schema.valid_values))

    elif schema.type == "int":
        if schema.min:
            annotations.append(MinSrc(schema.min))
        if schema.max:
            annotations.append(MaxSrc(schema.max))
        if schema.valid_values:
            annotations.append(ValidValuesSrc(schema.valid_values))
        # TODO: The rest...

    elif schema.type == "list":
        if schema.min_length:
            annotations.append(MinLenSrc(schema.min_length))
        if schema.max_length:
            annotations.append(MaxLenSrc(schema.max_length))
        # TODO: The rest...

    elif schema.type == "bool":
        if schema.valid_values:
            annotations.append(ValidValuesSrc(schema.valid_values))
        # TODO: The rest...

    # TODO: The rest...

    return annotations
