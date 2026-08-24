# Copyright (c) 2024-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from typing import TYPE_CHECKING

from pyavd._lazy_import import LazyImports, install_lazy_imports

if TYPE_CHECKING:
    from .add_md_toc import add_md_toc as add_md_toc
    from .decrypt import decrypt as decrypt
    from .default import default as default
    from .encrypt import encrypt as encrypt
    from .hide_passwords import hide_passwords as hide_passwords
    from .is_in_filter import is_in_filter as is_in_filter
    from .list_compress import list_compress as list_compress
    from .natural_sort import natural_sort as natural_sort
    from .range_expand import range_expand as range_expand
    from .secure_hash import secure_hash as secure_hash
    from .snmp_hash import snmp_hash as snmp_hash
    from .status_render import status_render as status_render

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

install_lazy_imports(_LAZY_IMPORTS, globals())
