# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from types import GenericAlias
from typing import Any, ClassVar


class ValidationAnnotation:
    _is_validation_annotation: ClassVar[bool] = True

    def __class_getitem__(cls, item: Any) -> GenericAlias:
        return GenericAlias(cls, item)


class Format(ValidationAnnotation):
    pass


class MaxLen(ValidationAnnotation):
    pass


class MinLen(ValidationAnnotation):
    pass


class Max(ValidationAnnotation):
    pass


class Min(ValidationAnnotation):
    pass


class Pattern(ValidationAnnotation):
    pass


class Lower:
    is_validation_type: ClassVar[bool] = True


class ValidValues(ValidationAnnotation):
    pass


class ValidationWarning(UserWarning):
    msg: str
    """Message"""
    path: list[str | int]
    """Data path to key that raised this warning"""

    @staticmethod
    def _path_to_str(path: list[str | int]) -> str:
        if not path:
            return ""

        string_elements = []
        for element in path:
            if isinstance(element, int):
                if string_elements:
                    # Add index to last element (to avoid the preceding dot)
                    string_elements[-1] += f"[{element}]"
                else:
                    string_elements = [f"[{element}]"]
                continue
            string_elements.append(element)
        return ".".join(string_elements)


class InvalidKey(ValidationWarning):
    def __init__(self, path: list[str | int] | None = None) -> None:
        self.path = path
        self.msg = f"Got invalid key '{self._path_to_str(path)}'"
        super().__init__(self.msg)


class InvalidType(ValidationWarning):
    def __init__(self, invalid_type: type, valid_type: type, path: list[str | int] | None = None) -> None:
        self.path = path
        self.msg = f"Got invalid type for '{self._path_to_str(path)}'. Expected '{valid_type}', got '{invalid_type}'."
        super().__init__(self.msg)


class InvalidValue(ValidationWarning):
    def __init__(self, value: Any, valid_values: tuple | str, path: list[str | int] | None = None) -> None:
        self.path = path
        if isinstance(valid_values, str):
            valid_values = (valid_values,)

        expected = " or ".join(str(valid_value) for valid_value in valid_values)
        self.msg = f"Got invalid value for '{self._path_to_str(path)}'. Expected '{expected}', got '{value}'"
        super().__init__(self.msg)


class InvalidLength(ValidationWarning):
    def __init__(self, length: int, valid_length: str, path: list[str | int] | None = None) -> None:
        self.path = path

        self.msg = f"Got invalid length for '{self._path_to_str(path)}'. Expected a length of {valid_length}, but the value had a length of '{length}'"
        super().__init__(self.msg)


class InvalidPattern(ValidationWarning):
    def __init__(self, value: Any, pattern: str, path: list[str | int] | None = None) -> None:
        self.path = path
        self.msg = f"Got invalid value for '{self._path_to_str(path)}'. Expected a value matching the pattern '{pattern}', got '{value}'"
        super().__init__(self.msg)


class MissingKey(ValidationWarning):
    def __init__(self, path: list[str | int] | None = None) -> None:
        self.path = path
        self.msg = f"Missing required key '{self._path_to_str(path)}'"
        super().__init__(self.msg)
