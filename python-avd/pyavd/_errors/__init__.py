# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

from pyavd._utils.json_path_to_string import json_path_to_string

if TYPE_CHECKING:
    from collections.abc import Sequence

    from pyavd_utils.validation import Violation
    from typing_extensions import Self


class AristaAvdError(Exception):
    host: str | None

    def __init__(self, *args: object, host: str | None = None) -> None:
        self.host = host
        super().__init__(*args or ("An Error has occurred in an arista.avd plugin",))

    @property
    def message(self) -> str:
        return str(self.args[0])

    def __str__(self) -> str:
        # args can be zeroed by raise_action_fail._clear_exception_chain to suppress duplicate messages in Ansible output.
        if not self.args:
            return ""
        return self.message

    def with_host(self, host: str) -> Self:
        new_error = type(self)(*self.args)
        new_error.__dict__.update(self.__dict__)
        new_error.host = host
        return new_error


class AristaAvdInvalidInputsError(AristaAvdError):
    def __init__(self, message: str, host: str | None = None) -> None:
        super().__init__(message, host=host)

    @property
    def message(self) -> str:
        msg = str(self.args[0])
        if self.host:
            return f"{msg.removesuffix('.')} for host '{self.host}'."
        return msg


class AristaAvdMissingVariableError(AristaAvdError):
    variable: str | None

    def __init__(self, variable: str | None = None, host: str | None = None) -> None:
        self.variable = variable
        super().__init__(variable, host=host)

    @property
    def message(self) -> str:
        msg = f"'{self.args[0]}' is required but was not found."
        if self.host:
            return f"{msg.removesuffix('.')} for host '{self.host}'."
        return msg


class AvdSchemaError(AristaAvdError):
    def __init__(self, message: str = "Schema Error", path: Sequence[str | int] | None = None) -> None:
        if path is not None:
            self.path = json_path_to_string(path)
        super().__init__(message, path)

    @property
    def message(self) -> str:
        msg = str(self.args[0])
        if self.args[1] is not None:
            return f"'Validation Error: {json_path_to_string(self.args[1])}': {msg}"
        return msg


class AvdValidationError(AristaAvdError):
    path: str
    violation: str

    def __init__(self, violation: str, path: Sequence[str | int]) -> None:
        self.violation = violation
        self.path = json_path_to_string(path)
        super().__init__(violation, path)

    @property
    def message(self) -> str:
        return f"Validation Error: [{json_path_to_string(self.args[1])}] {self.args[0]}"

    @classmethod
    def from_violation(cls, violation: Violation) -> Self:
        return cls(violation=violation.message, path=violation.path)


class AvdDeprecationWarning(AristaAvdError, DeprecationWarning):  # noqa: N818
    def __init__(
        self,
        key: Sequence[str | int],
        new_key: str | None = None,
        remove_in_version: str | None = None,
        remove_after_date: str | None = None,
        url: str | None = None,
        *,
        removed: bool = False,
        conflict: bool = False,
    ) -> None:
        self.path = json_path_to_string(key)
        self.version = remove_in_version
        self.date = remove_after_date
        self.removed = removed
        self.conflict = conflict

        if conflict and new_key:
            self.new_key_path = ".".join(item for item in [json_path_to_string(key[:-1]), new_key] if item)

        super().__init__(key, new_key, remove_in_version, remove_after_date, url)

    @property
    def message(self) -> str:
        key, new_key, url = self.args[0], self.args[1], self.args[4]
        path = json_path_to_string(key)
        parts = []

        if self.removed:
            parts.append(f"The input data model '{path}' was removed.")
        elif self.conflict and new_key:
            new_key_path = ".".join(item for item in [json_path_to_string(key[:-1]), new_key] if item)
            parts.append(
                f"The input data model '{path}' is deprecated and cannot be used in conjunction with the new data model '{new_key_path}'. "
                "This usually happens when a data model has been updated and custom structured configuration still uses the old model."
            )
        else:
            parts.append(f"The input data model '{path}' is deprecated.")

        if new_key and not self.conflict:
            parts.append(f"Use '{new_key}' instead.")

        if url:
            parts.append(f"See {url} for details.")

        return " ".join(parts)


class AristaAvdDuplicateDataError(AristaAvdError):
    def __init__(self, context: str, context_item_a: str, context_item_b: str, host: str | None = None) -> None:
        super().__init__(context, context_item_a, context_item_b, host=host)

    @property
    def message(self) -> str:
        msg = f"Found duplicate objects with conflicting data while generating configuration for {self.args[0]}. {self.args[1]} conflicts with {self.args[2]}."
        if self.host:
            return f"{msg.removesuffix('.')} for host '{self.host}'."
        return msg


class AristaAvdModelDeprecationWarning(DeprecationWarning):
    """
    Inherit Python DeprecationWarning class for AVD.

    TODO: Not ideal with AvdDeprecationWarning already inheriting from AristaAvdError
          but this is our legacy we have to live with for now.
    """
