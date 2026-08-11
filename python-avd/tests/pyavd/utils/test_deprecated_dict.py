# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import warnings

import pytest

from pyavd._utils.deprecated_dict import DeprecatedDict


def test_get_emits_deprecation_once() -> None:
    deprecated_dict = DeprecatedDict(
        {"interface": "Ethernet1", "type": "sometype"},
        _deprecated_dict_key="link",
        _new_keys={"interface": "interface", "type": "link_type"},
        _remove_in_version="7.0.0",
    )

    # Warn on first __get_item__ for a key.
    with pytest.deprecated_call(match="deprecated"):
        assert deprecated_dict["type"] == "sometype"

    # No warning on second access - here using get() for the same key.
    with warnings.catch_warnings():
        warnings.simplefilter("error", DeprecationWarning)
        assert deprecated_dict.get("type") == "sometype"

    # Warn on first get() for another key.
    with pytest.deprecated_call(match="deprecated"):
        assert deprecated_dict.get("type") == "sometype"
        assert deprecated_dict["interface"] == "Ethernet1"

    # No warning on second access - here using __get_item__ for the other key.
    with warnings.catch_warnings():
        warnings.simplefilter("error", DeprecationWarning)
        assert deprecated_dict["interface"] == "Ethernet1"
