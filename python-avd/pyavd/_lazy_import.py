# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from importlib import import_module
from types import ModuleType
from typing import Any, TypeAlias

LazyImports: TypeAlias = dict[str, tuple[str, str]]
"""Map exported attribute names to their defining module and attribute names."""


class _LazyImportModule(ModuleType):
    """Module type preserving lazy exports that have the same name as a submodule."""

    def __getattribute__(self, name: str) -> Any:
        namespace = ModuleType.__getattribute__(self, "__dict__")
        lazy_imports: LazyImports = namespace["_lazy_imports"]
        if name in lazy_imports and (name not in namespace or isinstance(namespace[name], ModuleType)):
            return get_lazy_attr(name, lazy_imports, namespace)

        return ModuleType.__getattribute__(self, name)


def get_lazy_attr(name: str, lazy_imports: LazyImports, namespace: dict[str, Any]) -> Any:
    """Import and cache one lazily re-exported package attribute."""
    try:
        module_name, attribute_name = lazy_imports[name]
    except KeyError as error:
        raise AttributeError(name) from error

    try:
        value = getattr(import_module(module_name), attribute_name)
    except Exception as error:
        package_name = namespace.get("__name__", "<unknown>")
        note = f"Lazy export '{package_name}.{name}' maps to attribute '{attribute_name}' in module '{module_name}'."
        if isinstance(error, AttributeError):
            # AttributeError makes `from package import name` fall back to a same-named submodule, potentially returning the module instead.
            import_error = ImportError(str(error))
            # TODO: Call import_error.add_note directly once support for Python 3.10 is removed.
            if callable(add_note := getattr(import_error, "add_note", None)):
                add_note(note)
            raise import_error from error

        # TODO: Call error.add_note directly once support for Python 3.10 is removed.
        if callable(add_note := getattr(error, "add_note", None)):
            add_note(note)
        raise

    namespace[name] = value
    return value


def get_lazy_dir(lazy_imports: LazyImports, namespace: dict[str, Any]) -> list[str]:
    """Return package attributes including names that have not been imported yet."""
    return sorted(namespace.keys() | lazy_imports.keys())


def install_lazy_imports(lazy_imports: LazyImports, namespace: dict[str, Any], additional_exports: tuple[str, ...] = ()) -> None:
    """
    Install the runtime machinery for lazily re-exporting package attributes.

    This function must be called once from a package ``__init__.py`` after its
    ``LazyImports`` mapping has been defined, passing ``globals()`` as
    ``namespace``. It mutates that namespace by installing:

    - ``__all__`` containing ``additional_exports`` followed by the lazy names.
    - ``__getattr__`` to resolve, import, and cache missing lazy attributes.
    - ``__dir__`` to expose lazy names before their defining modules are loaded.
    - The private ``_lazy_imports`` mapping used by ``_LazyImportModule``.

    The package module is also changed to ``_LazyImportModule``. A normal
    module-level ``__getattr__`` only runs for missing attributes, which is not
    sufficient when an export has the same name as its defining submodule. For
    example, importing ``pyavd.j2filters.add_md_toc`` makes importlib assign the
    submodule object to ``pyavd.j2filters.add_md_toc``. The custom module type
    detects that module object and restores the documented lazy export instead.
    Resolved values are cached in the package namespace until importlib replaces
    one with another same-named submodule object.

    ``additional_exports`` are existing package attributes that should be
    included in ``__all__`` but are not lazy. Lazy mappings are expected to
    resolve to functions, classes, or other non-module attributes.

    Exceptions raised while importing the target module are preserved. A missing
    target attribute is raised as ``ImportError`` with the original
    ``AttributeError`` chained as its cause, preventing Python's from-import
    machinery from silently falling back to a same-named submodule.

    This runtime setup is invisible to static type checkers. Package initializers
    must still declare their lazy exports under ``TYPE_CHECKING`` so consumers
    receive the correct types and editor completions.

    Args:
        lazy_imports: Export name to defining module and attribute mappings.
        namespace: The calling package's global namespace, normally ``globals()``.
        additional_exports: Eager package attributes to prepend to ``__all__``.
    """

    def _getattr(name: str) -> Any:
        return get_lazy_attr(name, lazy_imports, namespace)

    def _dir() -> list[str]:
        return get_lazy_dir(lazy_imports, namespace)

    namespace["_lazy_imports"] = lazy_imports
    namespace["__all__"] = [*additional_exports, *lazy_imports]
    namespace["__getattr__"] = _getattr
    namespace["__dir__"] = _dir
    module = namespace["__name__"]
    import_module(module).__class__ = _LazyImportModule
