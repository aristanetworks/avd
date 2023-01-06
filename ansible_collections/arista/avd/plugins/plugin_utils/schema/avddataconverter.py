from __future__ import annotations

from typing import Generator

from ansible_collections.arista.avd.plugins.filter.convert_dicts import convert_dicts
from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError, AvdConversionWarning
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get_all

SCHEMA_TO_PY_TYPE_MAP = {
    "str": str,
    "int": int,
    "bool": bool,
    "float": float,
    "dict": dict,
    "list": list,
}
SIMPLE_CONVERTERS = {
    "str": str,
    "int": int,
    "bool": bool,
}


class AvdDataConverter:
    """
    AvdDataConverter is used to convert AVD Data Types based on schema options.
    """

    def __init__(self, avdschema):
        self._avdschema = avdschema

        self.converters = {
            "items": self.convert_items,
            "keys": self.convert_keys,
        }

    def convert_data(self, data, schema: dict = None, path: list = None) -> Generator:
        if schema is None:
            # Get fully resolved schema (where all $ref has been expanded recursively)
            # Performs inplace update of the argument so we give an empty dict.
            # By default it will resolve the full schema
            schema = {}
            resolve_errors = self._avdschema.resolve(schema)
            for resolve_error in resolve_errors:
                if isinstance(resolve_error, Exception):
                    raise AristaAvdError(resolve_error)

        if path is None:
            path = []

        for key, converter in self.converters.items():
            if key not in schema:
                # Ignore keys not in schema
                continue

            # Converters will do inplace update of data. Any returns will be yielded conversion messages.
            yield from converter(schema[key], data, schema, path)

    def convert_keys(self, keys: dict, data: dict, schema: dict, path: list):
        """
        This function performs conversion on each key with the relevant subschema
        """
        if not isinstance(data, dict):
            return

        # We run through all the regular keys first, to ensure that all data has been converted
        # in case some of it is referenced in "dynamic_keys" below
        for key, childschema in keys.items():
            if key not in data:
                # Skip key since there is nothing to convert if the key is not set in data
                continue

            # Perform type conversion of the data for the child key if required based on "convert_types"
            if "convert_types" in childschema:
                yield from self.convert_types(childschema["convert_types"], data, key, childschema, path + [key])

            yield from self.convert_data(data[key], childschema, path + [key])

        # Compile "dynamic_keys"
        dynamic_keys = {}
        schema_dynamic_keys = schema.get("dynamic_keys", {})
        for dynamic_key, childschema in schema_dynamic_keys.items():
            resolved_keys = get_all(data, dynamic_key)
            for resolved_key in resolved_keys:
                dynamic_keys.setdefault(resolved_key, childschema)

        for key, childschema in dynamic_keys.items():
            if key not in data:
                # Skip key since there is nothing to convert if the key is not set in data
                continue

            # Perform type conversion of the data for the child key if required based on "convert_types"
            if "convert_types" in childschema:
                yield from self.convert_types(childschema["convert_types"], data, key, childschema, path + [key])

            # Dive in to child keys/schemas
            yield from self.convert_data(data[key], childschema, path + [key])

    def convert_items(self, items: dict, data: list, schema: dict, path: list):
        """
        This function performs conversion on each item with the items subschema
        """
        if not isinstance(data, list):
            return

        for index, item in enumerate(data):
            # Perform type conversion of the items data if required based on "convert_types"
            if "convert_types" in items:
                yield from self.convert_types(items["convert_types"], data, index, items, path + [f"[{index}]"])

            # Dive in to child items/schema
            yield from self.convert_data(item, items, path + [f"[{index}]"])

    def convert_types(self, convert_types: list, data: dict | list, index: str | int, schema: dict, path: list):
        """
        This function performs type conversion if necessary on a single data instance.
        It is invoked for child keys during "keys" conversion and for child items during
        "items" conversion

        "data" is either the parent dict or the parent list.
        "index" is either the key of the parent dict or the index of the parent list.

        Conversion is performed in-place using the provided "data" and "index"

        Yields AvdConversionWarning and/or AvdDeprecationWarning except for simple str/int/bool conversions

        Any conversion errors are ignored and the original value is returned
        """
        schema_type = schema.get("type")

        # Get value from input data
        value = data[index]

        # For simple conversions, skip conversion if the value is of the correct type
        if schema_type in SIMPLE_CONVERTERS and isinstance(value, SCHEMA_TO_PY_TYPE_MAP.get(schema_type)):
            return

        # Prepare string for var path used in warning messages.
        path_str = ".".join(path)

        for convert_type in convert_types:
            if isinstance(value, SCHEMA_TO_PY_TYPE_MAP.get(convert_type)):
                if schema_type in SIMPLE_CONVERTERS:
                    try:
                        data[index] = SIMPLE_CONVERTERS[schema_type](value)
                    except Exception:
                        # Ignore errors
                        return

                elif convert_type in ["dict", "list"] and schema_type == "list" and "primary_key" in schema:
                    try:
                        data[index] = convert_dicts(value, schema["primary_key"], secondary_key=schema.get("secondary_key"))
                    except Exception:
                        # Ignore errors
                        return

                    yield AvdConversionWarning(key=path_str, oldtype=convert_type, newtype=schema_type)

                elif convert_type == "dict" and schema_type == "list":
                    try:
                        data[index] = list(value)
                    except Exception:
                        # Ignore errors
                        return

                    yield AvdConversionWarning(key=path_str, oldtype=convert_type, newtype=schema_type)
