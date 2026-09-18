# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from collections.abc import Iterable, Mapping
from functools import partial
from ipaddress import ip_interface
from typing import TYPE_CHECKING

from jinja2.runtime import Undefined
from jinja2.utils import Namespace

if TYPE_CHECKING:
    from typing import Any, TypeVar

    T = TypeVar("T")


def ip_address_sort(iterable: Iterable[T] | None, sort_key: str | None = None) -> list[T]:
    """
    Sort an iterable by IP address.

    Values may be IPv4 or IPv6 addresses with or without a prefix length. IPv4 addresses are sorted before IPv6 addresses.

    Args:
        iterable: Input iterable.
        sort_key: Key or attribute containing the IP address. Required for mappings and namespaces.

    Returns:
        list: Sorted iterable.

    Raises:
        ValueError: If a value is not a valid IP address, or if sort_key is not set for a mapping or namespace.
    """
    if isinstance(iterable, Undefined) or iterable is None:
        return []

    return sorted(iterable, key=partial(_ip_address_key, sort_key=sort_key))


def _ip_address_key(item: Any, sort_key: str | None = None) -> tuple[int, int]:
    """Return the IP version and numeric address used for sorting."""
    if isinstance(item, Mapping):
        if sort_key is None:
            msg = f"'ip_address_sort' requires 'sort_key' to be set when used for a Mapping: {item}"
            raise ValueError(msg)
        value = item[sort_key]
    elif isinstance(item, Namespace):
        if sort_key is None:
            msg = f"'ip_address_sort' requires 'sort_key' to be set when used for a Namespace: {item}"
            raise ValueError(msg)
        value = getattr(item, sort_key)
    else:
        value = item

    address = ip_interface(value)
    return address.version, int(address.ip)
