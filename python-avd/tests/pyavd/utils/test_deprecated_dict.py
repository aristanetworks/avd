# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import pytest

from pyavd._errors import AvdDeprecationWarning
from pyavd._utils.deprecated_dict import DeprecatedDict


def test_get_emits_deprecation_once_and_returns_value() -> None:
    deprecated_dict = DeprecatedDict({"interface": "Ethernet1"}, _message="deprecated")

    assert deprecated_dict.get("interface") == "Ethernet1"
    assert deprecated_dict.get("missing", "fallback") == "fallback"

    with pytest.warns(DeprecationWarning, msg="deprecated"):
        deprecated_dict.get("interface")
