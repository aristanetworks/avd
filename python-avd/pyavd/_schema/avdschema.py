# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from copy import deepcopy
from functools import cached_property

import jsonschema
from deepmerge import always_merger

from .._errors import AristaAvdError, AvdSchemaError, AvdValidationError
from .avddataconverter import AvdDataConverter
from .avdschemaresolver import AvdSchemaResolver
from .avdvalidator import AvdValidator
from .store import create_store

DEFAULT_SCHEMA = {
    "type": "dict",
    "allow_other_keys": True,
}


class AvdSchema:
    """
    AvdSchema takes either a schema as dict or the ID of a builtin schema.
    If none of them are set, a default "dummy" schema will be loaded.
    schema -> schema_id -> DEFAULT_SCHEMA

    Parameters
    ----------
    schema : dict
        AVD Schema as dictionary. Will be validated towards AVD_META_SCHEMA.
    schema_id : str
        ID of AVD Schema. Either 'eos_cli_config_gen' or 'eos_designs'
    load_store_from_yaml : bool
        Force loading the YAML schema files into the store. By default schemas are loaded from pickled files.
    """

    def __init__(self, schema: dict = None, schema_id: str = None, load_store_from_yaml=False):
        self.store = create_store(load_from_yaml=load_store_from_yaml)
        self._schema_validator = jsonschema.Draft7Validator(self.store["avd_meta_schema"])
        self.load_schema(schema, schema_id)

    def validate_schema(self, schema: dict):
        validation_errors = self._schema_validator.iter_errors(schema)
        for validation_error in validation_errors:
            yield self._error_handler(validation_error)

    def load_schema(self, schema: dict = None, schema_id: str = None):
        """
        Load schema from dict or the ID of a builtin schema.
        If none of them are set, a default "dummy" schema will be loaded.
        schema -> schema_id -> DEFAULT_SCHEMA

        Parameters
        ----------
        schema : dict, optional
            AVD Schema as dictionary. Will be validated towards AVD_META_SCHEMA.
        schema_id : str, optional
            ID of AVD Schema. Either 'eos_cli_config_gen' or 'eos_designs'
        """

        # Clear cached resolved_schema if any
        self.__dict__.pop("resolved_schema", None)

        if schema:
            # Validate the schema
            for validation_error in self.validate_schema(schema):
                # TODO: Find a way to wrap multiple schema errors in a single raise
                raise validation_error
        elif schema_id:
            if schema_id not in self.store:
                raise AristaAvdError(f"Schema id {schema_id} not found in store. Must be one of {self.store.keys()}")

            schema = self.store[schema_id]
        else:
            schema = DEFAULT_SCHEMA

        self._schema = schema
        try:
            self._validator = AvdValidator(schema, self.store)
            self._dataconverter = AvdDataConverter(self)
            self._schemaresolver = AvdSchemaResolver(schema, self.store)
        except Exception as e:
            raise AristaAvdError("An error occurred during creation of the validator") from e

    def extend_schema(self, schema: dict):
        # Clear cached resolved_schema if any
        self.__dict__.pop("resolved_schema", None)

        for validation_error in self.validate_schema(schema):
            raise validation_error
        always_merger.merge(self._schema, schema)
        for validation_error in self.validate_schema(self._schema):
            raise validation_error

    def validate(self, data):
        validation_errors = self._validator.iter_errors(data)

        try:
            for validation_error in validation_errors:
                yield self._error_handler(validation_error)
        except Exception as error:  # pylint: disable=broad-exception-caught
            yield self._error_handler(error)

    def convert(self, data):
        conversion_errors = self._dataconverter.convert_data(data, self._schema)

        try:
            for conversion_error in conversion_errors:
                yield self._error_handler(conversion_error)
        except Exception as error:  # pylint: disable=broad-exception-caught
            yield self._error_handler(error)

    @cached_property
    def resolved_schema(self):
        """
        Get fully resolved schema (where all $ref has been expanded recursively)
        _schemaresolver performs inplace update of the argument so we give it a copy of the existing schema.

        The resolved schema is cached on the instance of AvdSchema.
        """
        resolved_schema = deepcopy(self._schema)
        resolve_errors = self._schemaresolver.iter_errors(resolved_schema)
        for resolve_error in resolve_errors:
            if isinstance(resolve_error, Exception):
                # TODO: Raise multiple errors or abstract them
                raise self._error_handler(resolve_error)
        return resolved_schema

    def _error_handler(self, error: Exception):
        if isinstance(error, AristaAvdError):
            return error
        if isinstance(error, jsonschema.ValidationError):
            return AvdValidationError(error=error)
        if isinstance(error, jsonschema.SchemaError):
            return AvdSchemaError(error=error)
        return error

    def subschema(self, datapath: list):
        """
        Takes datapath elements as a list and returns the subschema for this datapath.

        Example
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
            raise AvdSchemaError(f"The datapath argument must be a list. Got {type(datapath)}")

        schema = self._schema

        def recursive_function(datapath, schema):
            """
            Walk through schema following the datapath
            """
            if len(datapath) == 0:
                return schema

            # More items in datapath, so we run recursively with recursive_function
            key = datapath[0]
            if not isinstance(key, str):
                raise AvdSchemaError(f"All datapath items must be strings. Got {type(key)}")

            if schema["type"] == "dict":
                if key in schema.get("keys", []):
                    return recursive_function(datapath[1:], schema["keys"][key])
                if key in schema.get("dynamic_keys", []):
                    return recursive_function(datapath[1:], schema["dynamic_keys"][key])

            if schema["type"] == "list" and key in schema.get("items", {}).get("keys", []):
                return recursive_function(datapath[1:], schema["items"]["keys"][key])

            # Falling through here in case the schema is not covering the requested datapath
            raise AvdSchemaError(f"The datapath '{datapath}' could not be found in the schema")

        return recursive_function(datapath, schema)
