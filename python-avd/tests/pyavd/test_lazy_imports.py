# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import importlib
import subprocess
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
    ("module_name", "attribute_name", "expected_exception", "expected_message", "expected_cause"),
    [
        ("pyavd.missing_module", "missing_attribute", ModuleNotFoundError, "No module named 'pyavd.missing_module'", None),
        ("types", "missing_attribute", ImportError, "module 'types' has no attribute 'missing_attribute'", AttributeError),
    ],
)
def test_lazy_export_error_context(
    module_name: str,
    attribute_name: str,
    expected_exception: type[Exception],
    expected_message: str,
    expected_cause: type[Exception] | None,
) -> None:
    """Lazy import failures retain their message and include the export mapping on Python 3.11 and later."""
    lazy_imports = {"public_name": (module_name, attribute_name)}
    namespace = {"__name__": "test_package"}

    with pytest.raises(expected_exception) as exc_info:
        get_lazy_attr("public_name", lazy_imports, namespace)

    assert str(exc_info.value) == expected_message
    if expected_cause is None:
        assert exc_info.value.__cause__ is None
    else:
        assert isinstance(exc_info.value.__cause__, expected_cause)

    if sys.version_info >= (3, 11):
        assert exc_info.value.__notes__ == [f"Lazy export 'test_package.public_name' maps to attribute '{attribute_name}' in module '{module_name}'."]
    else:
        # TODO: Remove this branch once support for Python 3.10 is removed.
        assert not hasattr(exc_info.value, "__notes__")


def test_lazy_export_attribute_error_does_not_fall_back_to_submodule() -> None:
    """A broken same-named export must fail during a from-import instead of returning its submodule."""
    script = """
import pyavd

vars(pyavd)["_lazy_imports"]["get_device_config"] = ("pyavd.get_device_config", "missing_get_device_config")
from pyavd import get_device_config
get_device_config({})
"""

    result = subprocess.run([sys.executable, "-c", script], check=False, capture_output=True, text=True)  # noqa: S603

    assert result.returncode != 0
    assert "ImportError: module 'pyavd.get_device_config' has no attribute 'missing_get_device_config'" in result.stderr
    assert "'module' object is not callable" not in result.stderr
    note = "Lazy export 'pyavd.get_device_config' maps to attribute 'missing_get_device_config' in module 'pyavd.get_device_config'."
    if sys.version_info >= (3, 11):
        assert note in result.stderr
    else:
        # TODO: Remove this branch once support for Python 3.10 is removed.
        assert note not in result.stderr
