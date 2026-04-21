# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from pyavd._errors import AristaAvdError


class PathIndexedListKey:
    """Models an AvdIndexList Key."""

    def __init__(self, index: int, primary_key: str, value: str) -> None:
        """
        Initialize the object.

        Args:
            index: Index of the instance in the AvdIndexedList
            value: Value of the primary_key in the AvdIndexedList
            primary_key: Name of the primary key in the AvdIndexedList
        """
        self.index: int = index
        self.primary_key: str = primary_key
        self.value: str = value

    def __str__(self) -> str:
        """String representation."""
        return f"[{self.primary_key}={self.value}]"


class InputPath:
    """Representation of a Path in the AVD data tree."""

    path_elements: tuple[int | str | PathIndexedListKey, ...]

    def __init__(self, *args: int | str | PathIndexedListKey) -> None:
        """
        An ordered list of path elements.

        TODO: technically it should not be possible to have:
        * two ints in a row
        * two PathIndexedListKey in a row
        * an int following a PathIndexedListKey
        * a PathIndexedListKey following an int
        """
        self.path_elements = args

    def __str__(self) -> str:
        """String representation."""
        result = ""
        add_dot = False
        for element in self.path_elements:
            if isinstance(element, str):
                result += "." if add_dot else ""
                result += f"{element}"
            elif isinstance(element, bool):
                # bool are int..
                msg = f"Wrong element type '{type(element)}' in InputPath."
                raise AristaAvdError(msg)
            elif isinstance(element, int):
                result += f"[{element}]"
            elif isinstance(element, PathIndexedListKey):
                result += f"{element!s}"
            else:
                msg = f"Wrong element type '{type(element)}' in InputPath."
                raise AristaAvdError(msg)
            add_dot = True

        return result

    @property
    def parent(self) -> InputPath:
        """Returns a new InputPath object representing the parent path."""
        if len(self.path_elements) > 0:
            return InputPath(*self.path_elements[:-1])
        return _EMPTY_PATH

    def create_descendant(self, *args: int | str | PathIndexedListKey) -> InputPath:
        """Creates a descendant of this InputPath instance."""
        return InputPath(*self.path_elements, *args)


_EMPTY_PATH = InputPath()
