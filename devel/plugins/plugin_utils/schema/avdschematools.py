from __future__ import annotations

from typing import Generator

from ansible.errors import AnsibleActionFail
from ansible.utils.display import Display

from ansible_collections.arista.avd.plugins.plugin_utils.errors.errors import AvdDeprecationWarning
from ansible_collections.arista.avd.plugins.plugin_utils.schema.avdschema import AristaAvdError, AvdSchema

VALID_CONVERSION_MODES = ["disabled", "error", "warning", "info", "debug", "quiet"]
DEFAULT_CONVERSION_MODE = "debug"
VALID_VALIDATION_MODES = ["disabled", "error", "warning", "info", "debug"]
DEFAULT_VALIDATION_MODE = "warning"


class AvdSchemaTools:
    """
    Tools that wrap the various schema components for easy reuse in Ansible plugins
    """

    def __init__(
        self,
        hostname: str,
        ansible_display: Display,
        schema: dict = None,
        schema_id: str = None,
        conversion_mode: str = None,
        validation_mode: str = None,
        plugin_name: str = None,
    ) -> None:
        self._set_schema(schema, schema_id)
        self.hostname = hostname
        self.ansible_display = ansible_display
        self.plugin_name = plugin_name
        self._set_conversion_mode(conversion_mode)
        self._set_validation_mode(validation_mode)

    def _set_schema(self, schema: dict | None, schema_id: str | None) -> None:
        if schema is None and schema_id is None:
            raise AnsibleActionFail("Either argument 'schema' or 'schema_id' must be set")

        try:
            self.avdschema = AvdSchema(schema=schema, schema_id=schema_id)
        except AristaAvdError as e:
            raise AnsibleActionFail("Invalid Schema!") from e

    def _set_conversion_mode(self, conversion_mode: str | None) -> None:
        if conversion_mode is None:
            conversion_mode = DEFAULT_CONVERSION_MODE

        if not isinstance(conversion_mode, str):
            raise AnsibleActionFail("The argument 'conversion_mode' must be a string")

        if conversion_mode not in VALID_CONVERSION_MODES:
            raise AnsibleActionFail(f"Invalid value '{conversion_mode}' for the argument 'conversion_mode'. Must be one of {VALID_CONVERSION_MODES}")

        self.conversion_mode = conversion_mode

    def _set_validation_mode(self, validation_mode: str | None) -> None:
        if validation_mode is None:
            validation_mode = DEFAULT_VALIDATION_MODE

        if not isinstance(validation_mode, str):
            raise AnsibleActionFail("The argument 'validation_mode' must be a string")

        if validation_mode not in VALID_VALIDATION_MODES:
            raise AnsibleActionFail(f"Invalid value '{validation_mode}' for the argument 'validation_mode'. Must be one of {VALID_VALIDATION_MODES}")

        self.validation_mode = validation_mode

    def convert_data(self, data: dict) -> list[str]:
        """
        Convert data according to the schema (convert_types)
        The data conversion is done in-place (updating the original "data" dict).

        Returns list[str] with one conversion summary message if any conversions were performed
        """
        if self.conversion_mode == "disabled":
            return []

        result_messages = []

        # avd_schema.convert returns a generator, which we iterate through in handle_exceptions to perform the actual conversions.
        exceptions = self.avdschema.convert(data)
        if conversion_counter := self.handle_validation_exceptions(exceptions, self.conversion_mode):
            if self.conversion_mode == "error":
                result_messages.append(f"{conversion_counter} errors raised during conversion of input vars.")
            else:
                result_messages.append(f"{conversion_counter} data conversions done to conform to schema.")
            if self.conversion_mode == "debug":
                result_messages.append("Run with -v to see details")

        return result_messages

    def validate_data(self, data: dict) -> list:
        """
        Validate data according to the schema

        Returns list[str] with one validation summary message if any validation errors was found
        """
        if self.validation_mode == "disabled":
            return []

        result_messages = []

        # avd_schema.validate returns a generator, which we iterate through in handle_exceptions to perform the actual conversions.
        exceptions = self.avdschema.validate(data)
        if validation_counter := self.handle_validation_exceptions(exceptions, self.validation_mode):
            result_messages.append(f"{validation_counter} errors found during schema validation of input vars.")
            if self.validation_mode == "debug":
                result_messages.append("Run with -v to see details")

        return result_messages

    def convert_and_validate_data(self, data: dict) -> dict:
        """
        Convert & Validate data according to the schema

        Calls conversion and validation methods and gather resulting messages

        Returns dict which can contain either or both of the following keys:
        - failed: <bool>
        - msg: <str with concatenated summarys messages from conversion and validation>

        The return value should be applied on Ansible Action "result" dictionary
        """
        result = {}
        result_messages = []

        # Perform data conversions
        result_messages.extend(self.convert_data(data))
        if result_messages:
            if self.conversion_mode == "error":
                result["failed"] = True

        # Perform validation
        validation_messages = self.validate_data(data)
        if validation_messages:
            result_messages.extend(validation_messages)
            if self.validation_mode == "error":
                result["failed"] = True

        if result_messages:
            result["msg"] = " ".join(result_messages)

        return result

    def handle_validation_exceptions(self, exceptions: Generator, mode: str) -> int:
        """
        Iterate through the Generator of exceptions.
        This method is actually where the content of the generator gets executed.

        It displays various messages depending on the `mode` parameter

        Returns:
        - counter: <int> the number of AristaAvdError in the exceptions Generator
        """
        counter = 0
        for exception in exceptions:
            if not isinstance(exception, AristaAvdError):
                continue

            if isinstance(exception, AvdDeprecationWarning):
                # Deprecation warnings are not subject to "conversion_mode".
                # Instead we display using Ansible's deprecation notices.
                message = f"[{self.hostname}]: {exception}"
                self.ansible_display.deprecated(
                    msg=message,
                    version=exception.version,
                    date=exception.date,
                    collection_name=self.plugin_name,
                    removed=exception.removed,
                )
                continue

            counter += 1
            if mode == "quiet":
                continue
            message = f"[{self.hostname}]: {exception}"
            if mode == "error":
                self.ansible_display.error(message, False)
            elif mode == "info":
                self.ansible_display.display(message)
            elif mode == "debug":
                self.ansible_display.v(message)
            else:
                # mode == "warning"
                self.ansible_display.warning(message, False)
        return counter
