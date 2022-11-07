from __future__ import absolute_import, division, print_function

from typing import Generator

__metaclass__ = type

from ansible_collections.arista.avd.plugins.filter.convert_dicts import convert_dicts
from ansible_collections.arista.avd.plugins.plugin_utils.schema.errors import AristaAvdError, AvdConversion
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get_all

SCHEMA_TO_PY_TYPE_MAP = {
    "str": str,
    "int": int,
    "bool": bool,
    "float": float,
    "dict": dict,
    "list": list,
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
                oldtype = type(data[key]).__name__
                data[key] = self.convert_types(childschema["convert_types"], data[key], childschema, path + [key])
                newtype = type(data[key]).__name__
                if oldtype != newtype:
                    path_str = ".".join(path + [key])
                    yield AvdConversion(key=path_str, oldtype=oldtype, newtype=newtype)

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
                oldtype = type(data[key]).__name__
                data[key] = self.convert_types(childschema["convert_types"], data[key], childschema, path + [key])
                newtype = type(data[key]).__name__
                if oldtype != newtype:
                    path_str = ".".join(path + [key])
                    yield AvdConversion(key=path_str, oldtype=oldtype, newtype=newtype)

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
                oldtype = type(data[index]).__name__
                data[index] = self.convert_types(items["convert_types"], data[index], items, path + [f"[{index}]"])
                newtype = type(data[index]).__name__
                if oldtype != newtype:
                    path_str = ".".join(path + [f"[{index}]"])
                    yield AvdConversion(key=path_str, oldtype=oldtype, newtype=newtype)

            # Dive in to child items/schema
            yield from self.convert_data(item, items, path + [f"[{index}]"])

    def convert_types(self, convert_types: list, data, schema: dict, path: list):
        """
        This function performs type convertion if necessary on a single data instance.
        It is invoked for child keys during "keys" conversion and for child items during
        "items" conversion
        Returns the converted value is returned to the calling converter.
        Any convertion errors are ignored and the original value is returned
        """
        schema_type = schema.get("type")

        simple_converters = {
            "str": str,
            "int": int,
            "bool": bool,
        }

        # For simple conversions, skip conversion if the value is of the correct type
        if schema_type in simple_converters and isinstance(data, SCHEMA_TO_PY_TYPE_MAP.get(schema_type)):
            return data

        for convert_type in convert_types:
            if isinstance(data, SCHEMA_TO_PY_TYPE_MAP.get(convert_type)):
                if schema_type in simple_converters:
                    try:
                        return simple_converters[schema_type](data)
                    except Exception:
                        # Ignore errors and return original
                        return data

                elif convert_type in ["dict", "list"] and schema_type == "list" and "primary_key" in schema:
                    try:
                        return convert_dicts(data, schema["primary_key"], secondary_key=schema.get("secondary_key"))
                    except Exception:
                        # Ignore errors and return original
                        return data

                elif convert_type == "dict" and schema_type == "list":
                    try:
                        return list(data)
                    except Exception:
                        # Ignore errors and return original
                        return data

        return data
