# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import warnings

import pytest

from pyavd._utils.deprecated_dict import DeprecatedDict


def test_get_emits_deprecation() -> None:
    deprecated_dict = DeprecatedDict({"interface": "Ethernet1"}, _message="deprecated")

    with pytest.deprecated_call(match="deprecated"):
        assert deprecated_dict["interface"] == "Ethernet1"


def test_deprecated_dict_warning_only_once_on_getitem() -> None:
    d = DeprecatedDict({"a": 1, "b": 2}, _message="Deprecated access")

    # First access triggers warning
    with pytest.deprecated_call():
        _ = d["a"]

    # Second access should NOT issue any warnings
    with warnings.catch_warnings():
        warnings.simplefilter("error", DeprecationWarning)
        assert d["b"] == 2
