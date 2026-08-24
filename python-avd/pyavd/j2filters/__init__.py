# Copyright (c) 2024-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from typing import TYPE_CHECKING, Any

from pyavd._lazy_import import LazyImports, get_lazy_attr, get_lazy_dir

if TYPE_CHECKING:
    from .add_md_toc import add_md_toc
    from .decrypt import decrypt
    from .default import default
    from .encrypt import encrypt
    from .hide_passwords import hide_passwords
    from .is_in_filter import is_in_filter
    from .list_compress import list_compress
    from .natural_sort import natural_sort
    from .range_expand import range_expand
    from .secure_hash import secure_hash
    from .snmp_hash import snmp_hash
    from .status_render import status_render

__all__ = [
    "add_md_toc",
    "decrypt",
    "default",
    "encrypt",
    "hide_passwords",
    "is_in_filter",
    "list_compress",
    "natural_sort",
    "range_expand",
    "secure_hash",
    "snmp_hash",
    "status_render",
]

_LAZY_IMPORTS: LazyImports = {
    "add_md_toc": ("pyavd.j2filters.add_md_toc", "add_md_toc"),
    "decrypt": ("pyavd.j2filters.decrypt", "decrypt"),
    "default": ("pyavd.j2filters.default", "default"),
    "encrypt": ("pyavd.j2filters.encrypt", "encrypt"),
    "hide_passwords": ("pyavd.j2filters.hide_passwords", "hide_passwords"),
    "is_in_filter": ("pyavd.j2filters.is_in_filter", "is_in_filter"),
    "list_compress": ("pyavd.j2filters.list_compress", "list_compress"),
    "natural_sort": ("pyavd.j2filters.natural_sort", "natural_sort"),
    "range_expand": ("pyavd.j2filters.range_expand", "range_expand"),
    "secure_hash": ("pyavd.j2filters.secure_hash", "secure_hash"),
    "snmp_hash": ("pyavd.j2filters.snmp_hash", "snmp_hash"),
    "status_render": ("pyavd.j2filters.status_render", "status_render"),
}


def __getattr__(name: str) -> Any:
    return get_lazy_attr(name, _LAZY_IMPORTS, globals())


def __dir__() -> list[str]:
    return get_lazy_dir(_LAZY_IMPORTS, globals())
