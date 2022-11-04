import json
import os

from ansible_collections.arista.avd.plugins.plugin_utils.schema.avdschema import AvdSchema
from ansible_collections.arista.avd.plugins.plugin_utils.schema.key_to_display_name import key_to_display_name

script_dir = os.path.dirname(__file__)
with open(f"{script_dir}/avd_meta_schema.json", "r", encoding="utf-8") as file:
    AVD_META_SCHEMA = json.load(file)


class AvdToJsonSchemaConverter:
    """
    This class will convert the proprietary AVD Schema to JSON Schema

    A few keywords are converted as part of another keyword, simply because
    of the way JSON Schema is organized compared to AVD Schema.
    - "required"
    - "primary_key"
    - "allow_other_keys"

    Some features of AVD Schema are not supported by JSON Schema:
    - Enforcing uniqueness of "primary_key" in list of dicts
    - "dynamic_keys" based on values of data
    - "dynamic_valid_values" based on values of data
    - Most options under str "format"
    """

    def __init__(self, avdschema: AvdSchema):
        self.avdschema = avdschema
        self.converters = {
            "display_name": self.convert_display_name,
            "description": self.convert_description,
            "$ref": self.convert_ref,
            "type": self.convert_type,
            "max": self.convert_max,
            "min": self.convert_min,
            "valid_values": self.convert_valid_values,
            "format": self.convert_format,
            "max_length": self.convert_max_length,
            "min_length": self.convert_min_length,
            "pattern": self.convert_pattern,
            "default": self.convert_default,
            "items": self.convert_items,
            "keys": self.convert_keys,
            # "dynamic_keys": self.convert_dynamic_keys,
        }

    def convert_schema(self, schema: dict = None) -> dict:
        if schema is None:
            schema = self.avdschema._schema

        output = {}
        for word in schema:
            if word not in self.converters:
                # Ignore unsupported keys
                continue

            output.update(self.converters[word](schema[word], schema))

        return output

    def convert_type(self, type: str, parent_schema: dict) -> dict:
        TYPE_MAP = {
            "str": "string",
            "int": "integer",
            "bool": "boolean",
            "list": "array",
            "dict": "object",
        }
        return {"type": TYPE_MAP[type]}

    def convert_keys(self, keys: dict, parent_schema: dict) -> dict:
        output = {"properties": {}}
        required = []
        for key in keys:
            output["properties"][key] = self.convert_schema(keys[key])

            # Add an auto-generated title in case one is not set
            if "title" not in output["properties"][key]:
                output["properties"][key]["title"] = key_to_display_name(str(key))

            if keys[key].get("required") is True:
                required.append(key)

        if required:
            output["required"] = required

        output["additionalProperties"] = parent_schema.get("allow_other_keys", False)

        return output

    def convert_max(self, max: int, parent_schema: dict) -> dict:
        return {"maximum": max}

    def convert_min(self, min: int, parent_schema: dict) -> dict:
        return {"minimum": min}

    def convert_valid_values(self, valid_values: list, parent_schema: dict) -> dict:
        return {"enum": valid_values}

    def convert_format(self, format: str, parent_schema: dict) -> dict:
        FORMAT_MAP = {
            "ipv4": "ipv4",
            "ipv4_cidr": None,
            "ipv6": "ipv6",
            "ipv6_cidr": None,
            "ip": None,
            "cidr": None,
            "mac": None,
        }
        if (newformat := FORMAT_MAP[format]) is None:
            return {}

        return {"format": newformat}

    def convert_max_length(self, max: int, parent_schema: dict) -> dict:
        vartype = parent_schema["type"]
        if vartype == "str":
            return {"maxLength": max}
        if vartype == "list":
            return {"maxItems": max}
        return {}

    def convert_min_length(self, min: int, parent_schema: dict) -> dict:
        vartype = parent_schema["type"]
        if vartype == "str":
            return {"minLength": min}
        if vartype == "list":
            return {"minItems": min}
        return {}

    def convert_pattern(self, pattern: str, parent_schema: dict) -> dict:
        return {"pattern": pattern}

    def convert_default(self, default, parent_schema: dict) -> dict:
        return {"default": default}

    def convert_items(self, items: dict, parent_schema: dict) -> dict:
        output = {
            "items": self.convert_schema(items),
        }
        if (primary_key := parent_schema.get("primary_key")) and items.get("type") == "dict":
            output["items"].setdefault("required", [])
            if primary_key not in output["items"]["required"]:
                output["items"]["required"].append(primary_key)
        return output

    def convert_display_name(self, display_name: str, parent_schema: dict) -> dict:
        return {"title": display_name}

    def convert_description(self, description: str, parent_schema: dict) -> dict:
        return {"description": description}

    def convert_ref(self, ref: str, parent_schema: dict) -> dict:
        return {"$ref": ref}
