# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import re

from jinja2.runtime import Undefined
from jinja2.utils import Namespace


def convert(text: str) -> int | str:
    return int(text) if text.isdigit() else text.lower()


def natural_sort(iterable, sort_key=None):
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
