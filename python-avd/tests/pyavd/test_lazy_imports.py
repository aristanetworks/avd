# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import importlib
import sys
from types import ModuleType

import pytest

from pyavd._lazy_import import get_lazy_attr


@pytest.mark.parametrize(
    ("package_name", "submodule_name", "attribute_name"),
    [
        ("pyavd", "pyavd.get_device_doc", "get_device_doc"),
        ("pyavd.j2filters", "pyavd.j2filters.add_md_toc", "add_md_toc"),
    ],
)
def test_lazy_export_overrides_same_named_submodule(package_name: str, submodule_name: str, attribute_name: str) -> None:
    """Lazy package exports must take precedence when Python installs a same-named submodule."""
    package = importlib.import_module(package_name)
    submodule = importlib.import_module(submodule_name)
    assert isinstance(submodule, ModuleType)

    # Simulate importlib installing the imported submodule as an attribute on its parent package.
    vars(package)[attribute_name] = submodule

    assert getattr(package, attribute_name) is getattr(submodule, attribute_name)


@pytest.mark.parametrize(
    ("module_name", "attribute_name", "expected_exception", "expected_message"),
    [
        ("pyavd.missing_module", "missing_attribute", ModuleNotFoundError, "No module named 'pyavd.missing_module'"),
        ("types", "missing_attribute", AttributeError, "module 'types' has no attribute 'missing_attribute'"),
    ],
)
def test_lazy_export_error_context(module_name: str, attribute_name: str, expected_exception: type[Exception], expected_message: str) -> None:
    """Lazy import failures retain their original exception and message and include the export mapping on Python 3.11 and later."""
    lazy_imports = {"public_name": (module_name, attribute_name)}
    namespace = {"__name__": "test_package"}

    with pytest.raises(expected_exception) as exc_info:
        get_lazy_attr("public_name", lazy_imports, namespace)

    assert str(exc_info.value) == expected_message
    if sys.version_info >= (3, 11):
        assert exc_info.value.__notes__ == [f"Lazy export 'test_package.public_name' maps to attribute '{attribute_name}' in module '{module_name}'."]
    else:
        # TODO: Remove this branch once support for Python 3.10 is removed.
        assert not hasattr(exc_info.value, "__notes__")
