# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from collections.abc import Hashable
from typing import Any, TypeVar

from pyavd._errors import AristaAvdInvalidInputsError, AristaAvdMissingVariableError

T = TypeVar("T")


class IndexedListCache:
    """
    Provides O(1) lookups for lists of dicts by caching index mappings.

    Usage:
        cache = IndexedListCache()
        item = cache.get_item(my_list, "name", "target_name")
    """

    def __init__(self) -> None:
        self._indices: dict[int, dict[str, dict[Hashable, int]]] = {}

    def get_item(
        self,
        list_of_dicts: list[dict],
        key: str,
        value: Hashable,
        default: T = None,
    ) -> dict | T:
        """Get item from list by key=value with O(1) lookup after first access."""
        list_id = id(list_of_dicts)

        # Build index on first access
        if list_id not in self._indices:
            self._indices[list_id] = {}

        if key not in self._indices[list_id]:
            # Build index for this key
            key_index: dict[Hashable, int] = {}
            for idx, item in enumerate(list_of_dicts):
                if isinstance(item, dict) and key in item:
                    item_key = item[key]
                    # Only index hashable values
                    if isinstance(item_key, Hashable):
                        key_index[item_key] = idx
            self._indices[list_id][key] = key_index

        # O(1) lookup
        idx = self._indices[list_id][key].get(value)
        if idx is not None:
            return list_of_dicts[idx]
        return default

    def invalidate(self, list_of_dicts: list[dict] | None = None) -> None:
        """Invalidate cache for a specific list or all lists."""
        if list_of_dicts is None:
            self._indices.clear()
        else:
            self._indices.pop(id(list_of_dicts), None)


# Global cache instance for get_item_cached
_list_cache = IndexedListCache()


def get_item_cached(list_of_dicts: list[dict], key: str, value: Hashable, default: T = None) -> dict | T:
    """Drop-in replacement for get_item() with O(1) lookups after first access."""
    return _list_cache.get_item(list_of_dicts, key, value, default)


def get_item(
    list_of_dicts: list,
    key: Any,
    value: Any,
    default: Any = None,
    *,
    required: bool = False,
    _case_sensitive: bool = False,
    var_name: str | None = None,
    custom_error_msg: str | None = None,
) -> Any:
    """
    Get one dictionary from a list of dictionaries by matching the given key and value.

    Returns the supplied default value or None if there is no match and "required" is False.

    Will return the first matching item if there are multiple matching items.

    Parameters
    ----------
    list_of_dicts : list(dict)
        List of Dictionaries to get list item from
    key : any
        Dictionary Key to match on
    value : any
        Value that must match
    default : any
        Default value returned if the key and value is not found
    required : bool
        Fail if there is no match
    case_sensitive : bool
        If the search value is a string, the comparison will ignore case by default (TODO)
    var_name : str
        String used for raising exception with the full variable name
    custom_error_msg : str
        Custom error message to raise when required is True and the value is not found

    Returns:
    -------
    any
        Dict or default value

    Raises:
    ------
    AristaAvdMissingVariableError
        If the key and value is not found and "required" == True
    """
    if var_name is None:
        var_name = key

    if (not isinstance(list_of_dicts, list)) or list_of_dicts == [] or value is None or key is None:
        if required is True:
            if custom_error_msg:
                raise AristaAvdInvalidInputsError(custom_error_msg)
            raise AristaAvdMissingVariableError(var_name)
        return default

    for list_item in list_of_dicts:
        if not isinstance(list_item, dict):
            # List item is not a dict as required. Skip this item
            continue
        if list_item.get(key) == value:
            # Match. Return this item
            return list_item

    # No Match
    if required is True:
        if custom_error_msg:
            raise AristaAvdInvalidInputsError(custom_error_msg)
        raise AristaAvdMissingVariableError(var_name)
    return default
