from typing import Generator

from .vendor.errors import AvdConversionWarning, AvdDeprecationWarning
from .vendor.schema.avdschema import AvdSchema

IGNORE_EXCEPTIONS = (AvdDeprecationWarning, AvdConversionWarning)


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

    def convert_data(self, data: dict) -> dict:
        """
        Convert data according to the schema (convert_types)
        The data conversion is done in-place (updating the original "data" dict).

        Args:
            data:
                Input variables which should be converted according to the schema.

        Returns
            dict :
                failed : bool
                    True if Conversion failed. Otherwise False.
                errors : list[Exception]
                    Any errors raised during variable conversion
        """
        result = {"failed": False, "errors": []}

        # avdschema.convert returns a Generator, so we have to iterate through it to perform the actual conversions.
        exceptions: Generator = self.avdschema.convert(data)
        for exception in exceptions:
            # Ignore conversions and deprecations
            if exception is None or isinstance(exception, IGNORE_EXCEPTIONS):
                continue

            result["errors"].append(exception)
            result["failed"] = True

        return result

    def validate_data(self, data: dict) -> dict:
        """
        Validate data according to the schema

        Args:
            data:
                Input variables which are to be validated according to the schema.

        Returns
            dict :
                failed : bool
                    True if data is invalid. Otherwise False.
                errors : list[Exception]
                    Any errors raised during validation.
                    This will contain errors raised as well as data validation issues.
        """
        result = {"failed": False, "errors": []}

        # avdschema.validate returns a Generator, so we have to iterate through it to perform the actual validations.
        exceptions: Generator = self.avdschema.validate(data)
        for exception in exceptions:
            # Ignore conversions and deprecations
            if exception is None or isinstance(exception, IGNORE_EXCEPTIONS):
                continue

            result["errors"].append(exception)
            result["failed"] = True

        return result

    def convert_and_validate_data(self, data: dict) -> dict:
        """
        Convert and validate data according to the schema

        Args:
            data:
                Input variables which are to be validated according to the schema.

        Returns
            dict :
                failed : bool
                    True if Conversion failed or data is invalid. Otherwise False.
                errors : list[Exception]
                    Any errors raised during variable conversion and validation
                    This will contain errors raised as well as data validation issues.
        """
        result = self.convert_data(data)
        if result["failed"]:
            return result

        result = self.validate_data(data)
        return result
