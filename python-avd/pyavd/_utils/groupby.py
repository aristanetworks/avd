# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from collections.abc import Iterator
from itertools import groupby as itergroupby
from typing import Any, TypeVar

T = TypeVar("T")


def groupby(list_of_dictionaries: list, key: str) -> Iterator:
    """Group list of dictionaries by key."""

    def getkey(dictionary: dict) -> Any:
        return dictionary.get(key)

    sorted_list = sorted(list_of_dictionaries, key=getkey)
    return itergroupby(sorted_list, getkey)


def groupby_obj(list_of_objects: list[T], attr: str, skip_singles: bool = False) -> Iterator[tuple[Any, Iterator[T]]]:
    """Group list of object by attribute."""

    def getkey(obj: object) -> Any:
        return getattr(obj, attr, None)

    sorted_list = sorted(list_of_objects, key=getkey)
    if skip_singles:
        for key, group in itergroupby(sorted_list, key=getkey):
            group_list = list(group)
            if len(group_list) > 1:
                yield key, iter(group_list)
    else:
        yield from itergroupby(sorted_list, getkey)
