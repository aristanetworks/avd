# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from importlib import import_module
from typing import Any, TypeAlias

LazyImports: TypeAlias = dict[str, tuple[str, str]]
"""Map exported attribute names to their defining module and attribute names."""


def get_lazy_attr(name: str, lazy_imports: LazyImports, namespace: dict[str, Any]) -> Any:
    """Import and cache one lazily re-exported package attribute."""
    try:
        module_name, attribute_name = lazy_imports[name]
    except KeyError as error:
        raise AttributeError(name) from error

    value = getattr(import_module(module_name), attribute_name)
    namespace[name] = value
    return value


def get_lazy_dir(lazy_imports: LazyImports, namespace: dict[str, Any]) -> list[str]:
    """Return package attributes including names that have not been imported yet."""
    return sorted(namespace.keys() | lazy_imports.keys())
