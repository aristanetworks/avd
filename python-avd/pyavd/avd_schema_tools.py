# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Generator

if TYPE_CHECKING:
    from ._errors import AvdDeprecationWarning
    from .validation_result import ValidationResult


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
        # pylint: disable=import-outside-toplevel
        from ._schema.avdschema import AvdSchema

        # pylint: enable=import-outside-toplevel

        self.avdschema = AvdSchema(schema=schema, schema_id=schema_id)

    def convert_data(self, data: dict) -> list[AvdDeprecationWarning]:
        """
        Convert data according to the schema (convert_types)
        The data conversion is done in-place (updating the original "data" dict).

        Args:
            data:
                Input variables which should be converted according to the schema.

        Returns:
            List of AvdDeprecationWarnings
        """
        from ._errors import AvdConversionWarning, AvdDeprecationWarning  # pylint: disable=import-outside-toplevel

        # avdschema.convert returns a Generator, so we have to iterate through it to perform the actual conversions.
        exceptions: Generator = self.avdschema.convert(data)

        result = []
        for exception in exceptions:
            # Ignore conversions
            if isinstance(exception, AvdConversionWarning):
                continue

            # Store but continue for deprecations
            if isinstance(exception, AvdDeprecationWarning):
                result.append(exception)
                continue

            # Raise on other exceptions
            if isinstance(exception, Exception):
                raise exception

        return result

    def validate_data(self, data: dict) -> ValidationResult:
        """
        Validate data according to the schema

        Args:
            data:
                Input variables which are to be validated according to the schema.

        Returns:
            Validation result object with any validation errors or deprecation warnings.
        """
        # pylint: disable=import-outside-toplevel
        from ._errors import AvdConversionWarning, AvdDeprecationWarning, AvdValidationError
        from .validation_result import ValidationResult

        # pylint: enable=import-outside-toplevel

        result = ValidationResult(failed=False)

        # avdschema.validate returns a Generator, so we have to iterate through it to perform the actual validations.
        exceptions: Generator = self.avdschema.validate(data)
        for exception in exceptions:
            # Ignore conversions
            if isinstance(exception, AvdConversionWarning):
                continue

            # Store and fail but continue for validation errors
            if isinstance(exception, AvdValidationError):
                result.validation_errors.append(exception)
                result.failed = True
                continue

            # Store but continue for deprecations
            if isinstance(exception, AvdDeprecationWarning):
                result.deprecation_warnings.append(exception)
                continue

            # Raise on other exceptions
            if isinstance(exception, Exception):
                raise exception

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
        self.convert_data(data)
        res = self.validate_data(data)
        return {"failed": res.failed, "errors": res.validation_errors}
