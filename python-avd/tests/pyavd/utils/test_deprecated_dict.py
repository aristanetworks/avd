# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from unittest import mock

from ansible_collections.arista.avd.plugins.plugin_utils.utils.deprecated_dict import DeprecatedDict


def test_get_emits_deprecation_once_and_returns_value() -> None:
    display = mock.MagicMock()
    d = DeprecatedDict({"interface": "Ethernet1"}, _display=display, _message="deprecated")

    assert d.get("interface") == "Ethernet1"
    assert d.get("missing", "fallback") == "fallback"

    display.deprecated.assert_called_once_with(
        msg="deprecated",
        version="7.0.0",
        collection_name="arista.avd",
        removed=False,
    )


def test_getitem_emits_deprecation_once_and_returns_value() -> None:
    display = mock.MagicMock()
    d = DeprecatedDict({"interface": "Ethernet1"}, _display=display, _message="deprecated")

    assert d["interface"] == "Ethernet1"
    assert d["interface"] == "Ethernet1"

    display.deprecated.assert_called_once()
