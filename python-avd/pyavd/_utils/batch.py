# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from itertools import islice
from typing import TYPE_CHECKING, TypeVar

if TYPE_CHECKING:
    from collections.abc import Generator, Iterable


T = TypeVar("T")
Batch_Type = type[list] | type[set] | type[tuple]


def batch(iterable: Iterable[T], size: int, batch_type: Batch_Type = list) -> Generator[list[T] | set[T] | tuple[T]]:
    """Returns a Generator of lists, sets or tuples containing 'size' items. The final yielded iterator may be shorter."""
    iterator = iter(iterable)
    while batch := list(islice(iterator, size)):
        yield batch_type(batch)
