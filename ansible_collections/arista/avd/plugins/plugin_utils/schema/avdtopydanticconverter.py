# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from keyword import iskeyword
from textwrap import indent

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AvdSchemaError
from ansible_collections.arista.avd.plugins.plugin_utils.schema.avdschema import AvdSchema, AvdSchemaResolver


class AvdToPydanticConverter:
    """
    This class will convert the proprietary AVD Schema to Pydantic v2 Classes
    """

    INDENTATION = "    "

    def __init__(self, avdschema: AvdSchema):
        avdschema._schemaresolver = AvdSchemaResolver(avdschema._schema, avdschema.store, recursive=False)
        self.avdschema = avdschema

    def convert_schema(self, root_key) -> dict:
        self.root_key = root_key

        class_name, output = self.generate_class(root_key, self.avdschema.resolved_schema)

        header = (
            "# Copyright (c) 2023 Arista Networks, Inc.\n"
            "# Use of this source code is governed by the Apache License 2.0\n"
            "# that can be found in the LICENSE file.\n\n"
            "from pydantic import BaseModel, Field\n"
        )
        if class_name == "EosDesigns":
            header += "\nfrom ansible_collections.arista.avd.roles.eos_cli_config_gen.schemas.eos_cli_config_gen import EosCliConfigGen\n"

        return header + "\n\n" + output + "\n"

    def generate_class_name(self, class_key: str) -> str:
        prefix = ""
        if class_key.startswith("_"):
            prefix = "_"
        return prefix + "".join(str(element).capitalize() for element in class_key.split("_"))

    def generate_class_name_from_ref(self, ref: str) -> str:
        base_class_elements = []

        if "#" in ref:
            # Replacing ref with only the part after #
            ref_schema, ref = ref.split("#", maxsplit=1)
            if ref_schema and ref_schema != self.root_key:
                base_class_elements.append(self.generate_class_name(ref_schema))

        add_internal = False
        ref_elements = ref.split("/")
        for ref_index, ref_element in enumerate(ref_elements):
            if ref_element in {"", "keys", "items"}:
                continue

            if ref_element == "$defs":
                add_internal = True
                continue

            if len(ref_elements) > ref_index + 1 and ref_elements[ref_index + 1] == "items":
                ref_element = f"{ref_element}_Item"

            if add_internal:
                add_internal = False
                ref_element = f"_{ref_element}"

            base_class_elements.append(self.generate_class_name(ref_element))

        return ".".join(base_class_elements)

    def generate_class(self, class_key: str, schema: dict) -> tuple[str, str]:
        if schema.get("type") != "dict":
            # Ignore if not dict
            return None, ""

        keys: dict = schema.get("keys", {})
        if not keys:
            # Avoid creating class without attributes
            return None, ""

        subclasses = []
        fields = []

        class_name = self.generate_class_name(class_key)
        base_class = "BaseModel"

        output = f"class {class_name}({base_class}):\n"

        for key, subschema in keys.items():
            # generate_field will return the field string but may also create sub classes,
            # which must be added to the output above the attributes referring to it.
            field, subclass = self.generate_field(key, subschema)
            if subclass:
                subclasses.append(indent(subclass, self.INDENTATION))
                # Insert an extra blank line after each subclass
                subclasses.append("")
            if field:
                fields.append(field)

        output = output + "\n".join(subclasses + fields)

        return class_name, output

    def generate_field(self, field_key: str, schema: dict) -> tuple[str, str]:
        if schema.get("deprecation", {}).get("removed"):
            # Ignore removed keys
            return "", ""

        field_type, subclass = self.generate_field_type(field_key, schema)

        field_args = {}

        # Set default value
        field_args["default"] = schema.get("default", None)
        if schema.get("required") is True or field_args["default"] is not None:
            or_none = ""
        else:
            or_none = " | None"

        # Set alias for reserved keywords
        if iskeyword(field_key) or not field_key.islower():
            field_args["alias"] = field_key
            field_key = f"{field_key}_key"

        # Render field_args
        field_args_str = ", ".join(f"""{key}={self.to_text(value)}""" for key, value in field_args.items())

        # Render field
        field = f"""{self.INDENTATION}{field_key}: {field_type}{or_none} = Field({field_args_str})"""

        return field, subclass

    def generate_field_type(self, field_key: str, schema: dict) -> tuple[str, str]:
        if "$ref" in schema:
            # If this field resolves a ref from another schema, there is no need to build a local class.
            # Instead we just point to that other schema.
            if not schema["$ref"].startswith(("#", self.root_key)):
                return self.generate_class_name_from_ref(schema["$ref"]), None

            schema = self.resolve_schema(schema)
            if "$ref" in schema:
                raise AvdSchemaError(f"Unresolved $ref in '{schema}'")

        schema_type = schema.get("type")
        if schema_type == "list" and "items" in schema:
            items_type, subclass = self.generate_field_type(f"{field_key}_Item", schema["items"])
            return f"list[{items_type}]", subclass

        if schema_type == "dict" and "keys" in schema:
            return self.generate_class(field_key, schema)

        return schema_type, None

    def to_text(self, data) -> str:
        if isinstance(data, str):
            return f'"{data}"'

        if isinstance(data, list):
            return str(data).replace("'", '"')

        if isinstance(data, dict):
            return str(data).replace("'", '"')

        return str(data)

    def resolve_schema(self, schema: dict) -> dict:
        avdschema = AvdSchema(schema)
        avdschema._schemaresolver = AvdSchemaResolver(avdschema._schema, avdschema.store, recursive=False)
        return avdschema.resolved_schema
