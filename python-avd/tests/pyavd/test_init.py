# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import importlib
import importlib.util
import sys
import warnings
from unittest.mock import patch

import pytest

import pyavd


@pytest.mark.parametrize("python_minor", [10, 11, 12, 13, 14])
def test_python_version_deprecation_on_import(python_minor: int) -> None:
    """Importing PyAVD warns only on Python 3.10, including when other tests already imported it."""
    spec = importlib.util.spec_from_file_location("pyavd", pyavd.__file__)
    assert spec is not None
    assert spec.loader is not None
    package = importlib.util.module_from_spec(spec)

    # Execute the real initializer in an isolated module without reloading the shared PyAVD package.
    with (
        patch.dict(sys.modules, {"pyavd": package}),
        patch.object(sys, "version_info", (3, python_minor, 42, "final", 0)),
        warnings.catch_warnings(record=True) as recorded_warnings,
    ):
        warnings.simplefilter("always", DeprecationWarning)
        spec.loader.exec_module(package)
        # A subsequent normal import uses the cached package and must not warn again.
        assert importlib.import_module("pyavd") is package

    if python_minor != 10:
        assert not recorded_warnings
        return

    assert len(recorded_warnings) == 1
    assert recorded_warnings[0].category is DeprecationWarning
    message = str(recorded_warnings[0].message)
    assert "Python 3.10 has reached end of life and no longer receives security updates." in message
    assert "AVD will drop support for Python version 3.10 in a future major release." in message
    assert "Please upgrade to a newer Python version supported by AVD." in message
    assert "https://avd.arista.com/stable/docs/installation/collection-installation.html#ansible-collection-installation" in message
