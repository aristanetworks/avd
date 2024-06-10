# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import re

from jinja2.runtime import Undefined
from jinja2.utils import Namespace


def convert(text: str) -> int | str:
    """
    Converts the string to an integer if it is a digit, otherwise converts it to lower case.
    Args:
        text (str): Input string.
    Returns:
        int | str: Converted string.
    """
    return int(text) if text.isdigit() else text.lower()


def natural_sort(iterable: list | dict | str | None, sort_key: str | None = None) -> list:
    """
    Sorts an iterable in a natural (alphanumeric) order.
    Args:
        iterable (list | dict | str | None): Input iterable.
        sort_key (str | None, optional): Key to sort by, defaults to None.
    Returns:
        list: Sorted iterable.
    """
    if isinstance(iterable, Undefined) or iterable is None:
        return []

    def alphanum_key(key):
        pattern = r"(\d+)"
        if sort_key is not None and isinstance(key, dict):
            return [convert(c) for c in re.split(pattern, str(key.get(sort_key, key)))]
        if sort_key is not None and isinstance(key, Namespace):
            return [convert(c) for c in re.split(pattern, getattr(key, sort_key))]
        return [convert(c) for c in re.split(pattern, str(key))]

    return sorted(iterable, key=alphanum_key)
