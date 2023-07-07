from ansible_collections.arista.avd.plugins.plugin_utils.schema.avdschema import AvdSchema


class AvdToPydanticConverter:
    """
    This class will convert the proprietary AVD Schema to Pydantic Classes
    """

    def __init__(self, avdschema: AvdSchema):
        self.avdschema = avdschema

    def convert_schema(self, root_key="root") -> dict:
        header = [
            "from pydantic import BaseModel",
        ]
        footer = [""]
        class_name, output = self.generate_class(root_key, self.avdschema.resolved_schema, [])
        return "\n".join(header + output + footer)

    def generate_class_name(self, class_key: str, path: list) -> str:
        elements = path + [class_key]
        elements = [str(element).capitalize() for element in elements]
        return "".join(elements)

    def generate_class(self, class_key: str, schema: dict, path: list) -> tuple[str, list]:
        if schema.get("type") != "dict":
            # Ignore if not dict
            return None, []

        if (keys := schema.get("keys")) is None:
            # Avoid creating class without attributes
            return None, []

        # Insert two blank lines before each class
        output = ["", ""]

        class_name = self.generate_class_name(class_key, path)
        output.append(f"class {class_name}(BaseModel):")
        for key, subschema in keys.items():
            # generate_field will return the field string but may also create sub classes,
            # which must be added to the output above the class referring to it.
            field, prepend_output = self.generate_field(key, subschema, path + [class_key])
            output = prepend_output + output
            output.append(field)

        return class_name, output

    def generate_field(self, field_key: str, schema: dict, path: list) -> tuple[str, list]:
        field_type, prepend_output = self.generate_field_type(field_key, schema, path)
        defaultvalue = schema.get("default", None)
        if schema.get("required") is True or defaultvalue is not None:
            or_none = ""
        else:
            or_none = " | None"

        field = f"    {field_key}: {field_type}{or_none} = {self.to_text(defaultvalue)}"
        return field, prepend_output

    def generate_field_type(self, field_key: str, schema: dict, path: list) -> tuple[str, list]:
        schema_type = schema.get("type")
        if schema_type == "list" and "items" in schema:
            field_type, prepend_output = self.generate_field_type(f"{field_key}Item", schema["items"], path)
            return f"list[{field_type}]", prepend_output

        if schema_type == "dict" and "keys" in schema:
            return self.generate_class(field_key, schema, path)

        return schema_type, []

    def to_text(self, data) -> str:
        if isinstance(data, str):
            return f'"{data}"'

        if isinstance(data, list):
            return str(data).replace("'", '"')

        return str(data)
