from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError, AvdSchemaError, AvdValidationError
from ansible_collections.arista.avd.plugins.plugin_utils.schema.avddataconverter import AvdDataConverter
from ansible_collections.arista.avd.plugins.plugin_utils.schema.avdschemaresolver import AvdSchemaResolver
from ansible_collections.arista.avd.plugins.plugin_utils.schema.avdvalidator import AVD_META_SCHEMA, AvdValidator

try:
    import jsonschema
except ImportError as imp_exc:
    JSONSCHEMA_IMPORT_ERROR = imp_exc
else:
    JSONSCHEMA_IMPORT_ERROR = None

try:
    from deepmerge import always_merger
except ImportError as imp_exc:
    DEEPMERGE_IMPORT_ERROR = imp_exc
else:
    DEEPMERGE_IMPORT_ERROR = None

DEFAULT_SCHEMA = {
    "type": "dict",
    "allow_other_keys": True,
}


class AvdSchema:
    def __init__(self, schema: dict = None):
        if JSONSCHEMA_IMPORT_ERROR:
            raise AristaAvdError('Python library "jsonschema" must be installed to use this plugin') from JSONSCHEMA_IMPORT_ERROR
        if DEEPMERGE_IMPORT_ERROR:
            raise AristaAvdError('Python library "deepmerge" must be installed to use this plugin') from DEEPMERGE_IMPORT_ERROR

        if not schema:
            schema = DEFAULT_SCHEMA
        self._schema_validator = jsonschema.Draft7Validator(AVD_META_SCHEMA)
        self.load_schema(schema)

    def validate_schema(self, schema: dict):
        validation_errors = self._schema_validator.iter_errors(schema)
        for validation_error in validation_errors:
            yield self._error_handler(validation_error)

    def load_schema(self, schema: dict):
        for validation_error in self.validate_schema(schema):
            # TODO: Find a way to wrap multiple schema errors in a single raise
            raise validation_error
        self._schema = schema
        try:
            self._validator = AvdValidator(schema)
            self._dataconverter = AvdDataConverter(schema)
            self._schemaresolver = AvdSchemaResolver(schema)
        except Exception as e:
            raise AristaAvdError("An error occured during creation of the validator") from e

    def extend_schema(self, schema: dict):
        for validation_error in self.validate_schema(schema):
            raise validation_error
        always_merger.merge(self._schema, schema)
        for validation_error in self.validate_schema(self._schema):
            raise validation_error

    def validate(self, data, schema: dict = None):
        if schema:
            for schema_validation_error in self.validate_schema(schema):
                yield schema_validation_error
                return

            validation_errors = self._validator.iter_errors(data, _schema=schema)
        else:
            validation_errors = self._validator.iter_errors(data)

        try:
            for validation_error in validation_errors:
                yield self._error_handler(validation_error)
        except Exception as error:
            yield self._error_handler(error)

    def convert(self, data, schema: dict = None):
        if schema:
            for schema_validation_error in self.validate_schema(schema):
                yield schema_validation_error
                return

            conversion_errors = self._dataconverter.iter_errors(data, _schema=schema)
        else:
            conversion_errors = self._dataconverter.iter_errors(data)

        try:
            for conversion_error in conversion_errors:
                yield self._error_handler(conversion_error)
        except Exception as error:
            yield self._error_handler(error)

    def resolve(self, resolved_schema: dict, schema: dict = None):
        """
        resolved_schema is a placeholder for the resulting schema where all $ref has been resolved recursively
        schema is the schema to resolve

        returns a Generator of resolve errors
        """
        if schema:
            for schema_validation_error in self.validate_schema(schema):
                yield schema_validation_error
                return

            resolved_schema.update(schema)
            resolve_errors = self._schemaresolver.iter_errors(resolved_schema, _schema=schema)
        else:
            resolved_schema.update(self._schema)
            resolve_errors = self._schemaresolver.iter_errors(resolved_schema)

        try:
            for resolve_error in resolve_errors:
                yield self._error_handler(resolve_error)
        except Exception as error:
            yield self._error_handler(error)

    def _error_handler(self, error: Exception):
        if isinstance(error, jsonschema.ValidationError):
            return AvdValidationError(error=error)
        if isinstance(error, jsonschema.SchemaError):
            return AvdSchemaError(error=error)
        return AvdSchemaError(str(error))

    def is_valid(self, data, schema: dict = None):
        if schema:
            for schema_validation_error in self.validate_schema(schema):
                # TODO: Find a way to wrap multiple schema errors in a single raise
                raise schema_validation_error
        try:
            if schema:
                return self._validator.is_valid(data, _schema=schema)
            return self._validator.is_valid(data)
        except Exception as error:
            # TODO: Find a way to wrap multiple schema errors in a single raise
            raise self._error_handler(error) from error

    def subschema(self, datapath: list, schema: dict = None):
        """
        Takes datapath elements as a list and returns the subschema for this datapath.
        Optionally the schema can be supplied. This is primarily used for recursive calls.

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

        if not schema:
            schema = self._schema

        for validation_error in self.validate_schema(schema):
            raise validation_error

        if len(datapath) == 0:
            return schema

        # More items in datapath, so we run recursively with subschema
        key = datapath[0]
        if not isinstance(key, str):
            raise AvdSchemaError(f"All datapath items must be strings. Got {type(key)}")

        if schema["type"] == "dict" and key in schema.get("keys", []):
            return self.subschema(datapath[1:], schema["keys"][key])

        if schema["type"] == "list" and key in schema.get("items", {}).get("keys", []):
            return self.subschema(datapath[1:], schema["items"]["keys"][key])

        # Falling through here in case the schema is not covering the requested datapath
        raise AvdSchemaError(f"The datapath '{datapath}' could not be found in the schema")
