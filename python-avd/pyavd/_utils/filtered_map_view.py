# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from collections.abc import Iterator, Mapping
from typing import Any


class FilteredMapView(Mapping):
    """
    A read-only mapping that filters out keys not in the allowed set.

    This is useful for creating a view of a mapping that only includes a subset of keys.
    """

    def __init__(self, data: Mapping, allowed_keys: set[Any]) -> None:
        """
        Create a new FilteredMapView.

        Args:
            data: The underlying mapping to filter.
            allowed_keys: A set of keys to allow.
        """
        self._data = data
        self._allowed_keys = allowed_keys

    def __getitem__(self, key: Any) -> Any:
        """
        Get the value for the given key.

        Raises:
            KeyError: If the key is not in the underlying data or not in the allowed keys.
        """
        if key not in self._allowed_keys:
            raise KeyError(key)
        return self._data[key]

    def __len__(self) -> int:
        """Return the number of items in the filtered mapping."""
        return sum(1 for _ in self)

    def __iter__(self) -> Iterator[Any]:
        """Return an iterator over the keys in the filtered mapping."""
        return (key for key in self._allowed_keys if key in self._data)

    def __repr__(self) -> str:
        """Return a string representation of the filtered mapping."""
        return f"FilteredMapView({self._data!r}, {self._allowed_keys!r})"
