# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from typing import Any, Generator

from .validation_result import ValidationResult
from .vendor.errors import AvdConversionWarning, AvdDeprecationWarning, AvdValidationError
from .vendor.schema.avdschema import AvdSchema


class AvdSchemaTools:
    """
    Tools that wrap the various schema components for easy use
    """

    def __init__(self, schema: dict = None, schema_id: str = None) -> None:
        """
        Convert data according to the schema (convert_types)
        The data conversion is done in-place (updating the original "data" dict).

        Args:
            schema_id:
                Name of AVD Schema to use for conversion and validation.
        """
        self.avdschema = AvdSchema(schema=schema, schema_id=schema_id)

    def _exceptions_handler(self, exceptions: Generator[Exception, Any, None], result: ValidationResult):
        """
        Sort the given exceptions and update the result object.
        Unknown exceptions will be raised.
        """
        for exception in exceptions:
            if isinstance(exception, AvdConversionWarning):
                result.conversion_warnings.append(exception)
                continue

            if isinstance(exception, AvdValidationError):
                result.validation_errors.append(exception)
                result.failed = True
                continue

            if isinstance(exception, AvdDeprecationWarning):
                result.deprecation_warnings.append(exception)
                continue

            if isinstance(exception, Exception):
                raise exception

    def convert_data(self, data: dict, result: None | ValidationResult = None) -> list[AvdDeprecationWarning]:
        """
        Convert data according to the schema (convert_types)
        The data conversion is done in-place (updating the original "data" dict).

        Args:
            data:
                Input variables which should be converted according to the schema.
            result:
                Result object to update if given. Otherwise a new object will be created and returned.

        Returns:
            Validation result object with any validation errors, conversion warnings or deprecation warnings.
        """
        result = result or ValidationResult(failed=False)

        # avdschema.convert returns a Generator, so we have to iterate through it to perform the actual conversions.
        self._exceptions_handler(self.avdschema.convert(data), result)

        return result

    def validate_data(self, data: dict, result: ValidationResult) -> ValidationResult:
        """
        Validate data according to the schema

        Args:
            data:
                Input variables which are to be validated according to the schema.
            result:
                Result object to update if given. Otherwise a new object will be created and returned.

        Returns:
            Validation result object with any validation errors, conversion warnings or deprecation warnings.
        """
        result = result or ValidationResult(failed=False)

        # avdschema.validate returns a Generator, so we have to iterate through it to perform the actual validations.
        self._exceptions_handler(self.avdschema.validate(data), result)

        return result

    def convert_and_validate_data(self, data: dict) -> dict:
        """
        Convert and validate data according to the schema

        Returns dictionary to be compatible with Ansible plugin. Called from vendored "get_structured_config".

        Args:
            data:
                Input variables which are to be validated according to the schema.

        Returns
            dict :
                failed : bool
                    True if data is invalid. Otherwise False.
                errors : list[Exception]
                    Any data validation issues.
        """
        result = ValidationResult(failed=False)
        self.convert_data(data, result)
        self.validate_data(data, result)
        return {"failed": result.failed, "errors": result.validation_errors}
