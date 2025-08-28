# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.


class AristaAvdError(Exception):
    host: str | None

    def __init__(self, message: str = "An Error has occurred in an arista.avd plugin", host: str | None = None) -> None:
        self.host = host
        self.message = message
        super().__init__(self.message)

    def _json_path_to_string(self, json_path: list[str | int]) -> str:
        path = ""
        for index, elem in enumerate(json_path):
            if isinstance(elem, int):
                path += f"[{elem}]"
            else:
                if index == 0:
                    path += elem
                    continue
                path += f".{elem}"
        return path


class AristaAvdInvalidInputsError(AristaAvdError):
    host: str | None

    def __init__(self, message: str, host: str | None = None) -> None:
        super().__init__(message, host=host)


class AristaAvdMissingVariableError(AristaAvdError):
    variable: str | None
    host: str | None

    def __init__(self, variable: str | None = None, host: str | None = None) -> None:
        """Fact host message is used only if host is set as well."""
        self.variable = variable
        self.host = host
        host_msg = f" for host '{host}'" if host else ""
        message = f"'{variable}' is required but was not found{host_msg}."
        super().__init__(message, host=host)


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
        key: list[str | int],
        new_key: str | None = None,
        remove_in_version: str | None = None,
        remove_after_date: str | None = None,
        url: str | None = None,
        *,
        removed: bool = False,
        conflict: bool = False,
    ) -> None:
        messages = []
        self.path = self._json_path_to_string(key)
        self.version = remove_in_version
        self.date = remove_after_date
        self.removed = removed
        self.conflict = conflict

        if removed:
            messages.append(f"The input data model '{self.path}' was removed.")
        elif conflict and new_key:
            self.new_key_path = ".".join(item for item in [self._json_path_to_string(key[:-1]), new_key] if item)
            messages.append(
                f"The input data model '{self.path}' is deprecated and cannot be used in conjunction with the new data model '{self.new_key_path}'. "
                "This usually happens when a data model has been updated and custom structured configuration still uses the old model."
            )
        else:
            messages.append(f"The input data model '{self.path}' is deprecated.")

        if new_key and not conflict:
            messages.append(f"Use '{new_key}' instead.")

        if url:
            messages.append(f"See {url} for details.")

        self.message = " ".join(messages)
        super().__init__(self.message)

    def _as_validation_error(self) -> AvdValidationError:
        """Converting AvdDeprecationWarning to AvdValidationError."""
        return AvdValidationError(message=self.message, path=self.path.split("."))


class AristaAvdDuplicateDataError(AristaAvdError):
    def __init__(self, context: str, context_item_a: str, context_item_b: str, host: str | None = None) -> None:
        self.message = (
            f"Found duplicate objects with conflicting data while generating configuration for {context}. {context_item_a} conflicts with {context_item_b}."
        )
        super().__init__(self.message, host=host)


class AristaAvdModelDeprecationWarning(DeprecationWarning):
    """
    Inherit Python DeprecationWarning class for AVD.

    TODO: Not ideal with AvdDeprecationWarning already inheriting from AristaAvdError
          but this is our legacy we have to live with for now.
    """
