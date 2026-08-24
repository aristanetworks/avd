# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import importlib
from types import ModuleType

import pytest


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
