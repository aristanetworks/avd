# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from keyword import iskeyword

from ansible_collections.arista.avd.plugins.plugin_utils.schema.avdschema import AvdSchema


class AvdToPydanticConverter:
    """
    This class will convert the proprietary AVD Schema to Pydantic v2 Classes
    """

    INDENTATION = "    "

    def __init__(self, avdschema: AvdSchema):
        self.avdschema = avdschema

    def convert_schema(self, root_key) -> dict:
        self.root_key = root_key
        class_name, output = self.generate_class(root_key, self.avdschema.resolved_schema)

        header = (
            "# Copyright (c) 2023 Arista Networks, Inc.\n"
            "# Use of this source code is governed by the Apache License 2.0\n"
            "# that can be found in the LICENSE file.\n\n"
            "from pydantic import BaseModel, Field\n"
            "\n\n"
        )
        return header + output + "\n"

    def generate_class_name(self, class_key: str) -> str:
        return "".join(str(element).capitalize() for element in class_key.split("_"))

    def generate_base_class(self, ref: str | None) -> str:
        if ref is None:
            return "BaseModel"

        base_class_elements = []

        if ":" in ref:
            # Replacing ref with only the part after :
            schema, ref = ref.split(":", maxsplit=1)
        else:
            schema = self.root_key

        base_class_elements = [self.generate_class_name(schema)]

        def recursive_function(_ref: str, add_item: bool = False):
            if not _ref:
                return

            for ref_index, ref_element in enumerate(_ref.split("/")):
                if ref_element in ["keys", "$defs"]:
                    recursive_function("/".join(_ref[ref_index + 1]))
                elif ref_element == "items":
                    recursive_function("/".join(_ref[ref_index + 1], add_item=True))
                elif add_item:
                    base_class_elements.append(self.generate_class_name(f"{ref_element}_Item"))
                    recursive_function("/".join(_ref[ref_index + 1]))
                else:
                    base_class_elements.append(self.generate_class_name(ref_element))
                    recursive_function("/".join(_ref[ref_index + 1]))

    def indent_block(self, block: str) -> str:
        return "\n".join(f"{self.INDENTATION}{line}".rstrip() for line in f"{block}".splitlines())

    def generate_class(self, class_key: str, schema: dict) -> tuple[str, str]:
        if schema.get("type") != "dict":
            # Ignore if not dict
            return None, ""

        if (keys := schema.get("keys")) is None:
            # Avoid creating class without attributes
            return None, ""

        subclasses = []
        fields = []

        class_name = self.generate_class_name(class_key)
        base_class = self.generate_base_class(schema.get("$ref"))

        output = f"class {class_name}({base_class}):\n"
        for key, subschema in keys.items():
            # generate_field will return the field string but may also create sub classes,
            # which must be added to the output above the attributes referring to it.
            field, subclass = self.generate_field(key, subschema)
            if subclass:
                subclasses.append(self.indent_block(subclass))
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
        if iskeyword(field_key):
            field_args["alias"] = field_key
            field_key = f"{field_key}_key"

        # Render field_args
        field_args_str = ", ".join(f"""{key}={self.to_text(value)}""" for key, value in field_args.items())

        # Render field
        field = f"""{self.INDENTATION}{field_key}: {field_type}{or_none} = Field({field_args_str})"""

        return field, subclass

    def generate_field_type(self, field_key: str, schema: dict) -> tuple[str, str]:
        schema_type = schema.get("type")
        if schema_type == "list" and "items" in schema:
            return self.generate_field_type(f"{field_key}_Item", schema["items"])

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
