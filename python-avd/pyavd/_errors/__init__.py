# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.


class AristaAvdError(Exception):
    def __init__(self, message: str = "An Error has occurred in an arista.avd plugin") -> None:
        self.message = message
        super().__init__(self.message)

    def _json_path_to_string(self, json_path: list[str | int]) -> str:
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
    def __init__(self, message: str = "Schema Error", path: list[str | int] | None = None) -> None:
        if path is not None:
            self.path = self._json_path_to_string(path)
            message = f"'Validation Error: {self.path}': {message}"
        super().__init__(message)


class AvdValidationError(AristaAvdError):
    def __init__(self, message: str = "Schema Error", path: list[str | int] | None = None) -> None:
        if path is not None:
            self.path = self._json_path_to_string(path)
            message = f"'Validation Error: {self.path}': {message}"
        super().__init__(message)


class AvdDeprecationWarning(AristaAvdError):  # noqa: N818
    def __init__(
        self,
        key: str,
        new_key: str | None = None,
        remove_in_version: str | None = None,
        remove_after_date: str | None = None,
        url: str | None = None,
        *,
        removed: bool = False,
    ) -> None:
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
    def __init__(self, context: str, context_item_a: str, context_item_b: str) -> None:
        self.message = (
            f"Found duplicate objects with conflicting data while generating configuration for {context}. {context_item_a} conflicts with {context_item_b}."
        )
        super().__init__(self.message)
