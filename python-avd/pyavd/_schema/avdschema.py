# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Any

import jsonschema
from deepmerge import always_merger

from pyavd._errors import AristaAvdError, AvdSchemaError

from .avddataconverter import AvdDataConverter
from .avdvalidator import AvdValidator
from .store import create_store

if TYPE_CHECKING:
    from collections.abc import Generator

DEFAULT_SCHEMA = {
    "type": "dict",
    "allow_other_keys": True,
}


class AvdSchema:
    """
    AvdSchema takes either a schema as dict or the ID of a builtin schema.

    If none of them are set, a default "dummy" schema will be loaded.
    schema -> schema_id -> DEFAULT_SCHEMA.

    Parameters
    ----------
    schema : dict
        AVD Schema as dictionary. Will be validated towards AVD_META_SCHEMA.
    schema_id : str
        ID of AVD Schema. Either 'eos_cli_config_gen' or 'eos_designs'
    load_store_from_yaml : bool
        Force loading the YAML schema files into the store. By default schemas are loaded from pickled files.
    """

    def __init__(self, schema: dict | None = None, schema_id: str | None = None, load_store_from_yaml: bool = False) -> None:
        self.store = create_store(load_from_yaml=load_store_from_yaml)
        self._schema_validator = jsonschema.Draft7Validator(self.store["avd_meta_schema"])
        self.load_schema(schema, schema_id)

    def validate_schema(self, schema: dict) -> Generator:
        validation_errors = self._schema_validator.iter_errors(schema)
        for validation_error in validation_errors:
            yield AvdSchemaError(error=validation_error)

    def load_schema(self, schema: dict | None = None, schema_id: str | None = None) -> None:
        """
        Load schema from dict or the ID of a builtin schema.

        If none of them are set, a default "dummy" schema will be loaded.
        schema -> schema_id -> DEFAULT_SCHEMA.

        Parameters
        ----------
        schema : dict, optional
            AVD Schema as dictionary. Will be validated towards AVD_META_SCHEMA.
        schema_id : str, optional
            ID of AVD Schema. Either 'eos_cli_config_gen' or 'eos_designs'
        """
        if schema:
            # Validate the schema
            for validation_error in self.validate_schema(schema):
                # TODO: Find a way to wrap multiple schema errors in a single raise
                raise validation_error
        elif schema_id:
            if schema_id not in self.store:
                msg = f"Schema id {schema_id} not found in store. Must be one of {self.store.keys()}"
                raise AristaAvdError(msg)

            schema = self.store[schema_id]
        else:
            schema = DEFAULT_SCHEMA

        self._schema = schema
        try:
            self._validator = AvdValidator(schema)
            self._dataconverter = AvdDataConverter(schema)
        except Exception as e:
            msg = "An error occurred during creation of the validator"
            raise AristaAvdError(msg) from e

    def extend_schema(self, schema: dict) -> None:
        for validation_error in self.validate_schema(schema):
            raise validation_error
        always_merger.merge(self._schema, schema)
        for validation_error in self.validate_schema(self._schema):
            raise validation_error

    def validate(self, data: Any) -> Generator:
        yield from self._validator.validate(data)

    def convert(self, data: Any) -> Generator:
        yield from self._dataconverter.convert_data(data)

    def subschema(self, datapath: list) -> dict:
        """
        Takes datapath elements as a list and returns the subschema for this datapath.

        Example:
        -------
        Data model:
        a:
          b:
            - c: 1
            - c: 2

        Schema:
        a:
          type: dict
          keys:
            b:
              type: list
              primary_key: c
              items:
                type: dict
                keys:
                  c:
                    type: str

        subschema(['a', 'b'])
        >> {"type": "list", "primary_key": "c", "items": {"type": "dict", "keys": {"c": {"type": "str"}}}}

        subschema(['a', 'b', 'c'])
        >> {"type": "str"}

        subschema(['a', 'b', 'c', 'd'])
        >> raises AvdSchemaError

        subschema([])
        >> self._schema (the loaded schema)

        subschema([], <myschema>)
        >> <myschema>

        subschema(None)
        >> raises AvdSchemaError

        subschema(['a'], <invalid_schema>)
        >> raises AvdSchemaError
        """
        if not isinstance(datapath, list):
            msg = f"The datapath argument must be a list. Got {type(datapath)}"
            raise AvdSchemaError(msg)

        schema = self._schema

        def recursive_function(datapath: list, schema: dict) -> dict:
            """Walk through schema following the datapath."""
            if len(datapath) == 0:
                return schema

            # More items in datapath, so we run recursively with recursive_function
            key = datapath[0]
            if not isinstance(key, str):
                msg = f"All datapath items must be strings. Got {type(key)}"
                raise AvdSchemaError(msg)

            if schema["type"] == "dict":
                if key in schema.get("keys", []):
                    return recursive_function(datapath[1:], schema["keys"][key])
                if key in schema.get("dynamic_keys", []):
                    return recursive_function(datapath[1:], schema["dynamic_keys"][key])

            if schema["type"] == "list" and key in schema.get("items", {}).get("keys", []):
                return recursive_function(datapath[1:], schema["items"]["keys"][key])

            # Falling through here in case the schema is not covering the requested datapath
            msg = f"The datapath '{datapath}' could not be found in the schema"
            raise AvdSchemaError(msg)

        return recursive_function(datapath, schema)
