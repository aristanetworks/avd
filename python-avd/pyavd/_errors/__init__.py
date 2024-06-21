# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import jsonschema


class AristaAvdError(Exception):
    def __init__(self, message="An Error has occurred in an arista.avd plugin"):
        self.message = message
        super().__init__(self.message)

    def _json_path_to_string(self, json_path):
        path = ""
        for index, elem in enumerate(json_path):
            if isinstance(elem, int):
                path += "[" + str(elem) + "]"
            else:
                if index == 0:
                    path += elem
                    continue
                path += "." + elem
        return path


class AristaAvdMissingVariableError(AristaAvdError):
    pass


class AvdSchemaError(AristaAvdError):
    def __init__(self, message="Schema Error", error=None):
        if isinstance(error, jsonschema.SchemaError):
            self.message = f"'Schema Error: {self._json_path_to_string(error.absolute_path)}': {error.message}"
        else:
            self.message = message
        super().__init__(self.message)


class AvdValidationError(AristaAvdError):
    def __init__(self, message: str = "Schema Error", error=None):
        if isinstance(error, (jsonschema.ValidationError)):
            self.path = self._json_path_to_string(error.absolute_path)
            self.message = f"'Validation Error: {self.path}': {error.message}"
        else:
            self.message = message
        super().__init__(self.message)


class AvdConversionWarning(AristaAvdError):
    def __init__(self, message: str = "Data was converted to conform to schema", key=None, oldtype="unknown", newtype="unknown"):
        if key is not None:
            self.path = self._json_path_to_string(key)
            self.message = f"'Data Type Converted: {self.path} from '{oldtype}' to '{newtype}'"
        else:
            self.message = message
        super().__init__(self.message)


class AvdDeprecationWarning(AristaAvdError):
    def __init__(self, key, new_key=None, remove_in_version=None, remove_after_date=None, url=None, removed=False):
        messages = []
        self.path = self._json_path_to_string(key)

        if removed:
            messages.append(f"The input data model '{self.path}' was removed.")
        else:
            messages.append(f"The input data model '{self.path}' is deprecated.")

        self.version = remove_in_version
        self.date = remove_after_date
        self.removed = removed

        if new_key is not None:
            messages.append(f"Use '{new_key}' instead.")

        if url is not None:
            messages.append(f"See {url} for details.")

        self.message = " ".join(messages)
        super().__init__(self.message)


class AristaAvdDuplicateDataError(AristaAvdError):
    def __init__(self, context: str, context_item_a: str, context_item_b: str):
        self.message = (
            f"Found duplicate objects with conflicting data while generating configuration for {context}. {context_item_a} conflicts with {context_item_b}."
        )
        super().__init__(self.message)
