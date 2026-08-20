# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from pathlib import Path
from unittest.mock import MagicMock

import pytest

from ansible_collections.arista.avd.plugins.plugin_utils.utils import LazyJsonFileMapping


def test_lazy_json_file_mapping_loads_once_on_first_access() -> None:
    """The JSON file is loaded once on first access and the loaded mapping remains mutable."""
    file_handler = MagicMock()
    file_handler.load_json.return_value = {"key": "value"}
    file_path = Path("validated/device.json")

    data = LazyJsonFileMapping(file_handler, file_path)

    file_handler.load_json.assert_not_called()

    assert data["key"] == "value"
    file_handler.load_json.assert_called_once_with(file_path)

    data["other_key"] = "other_value"
    del data["key"]

    assert dict(data) == {"other_key": "other_value"}
    file_handler.load_json.assert_called_once_with(file_path)


def test_lazy_json_file_mapping_rejects_non_mapping_json() -> None:
    """A JSON value that is not an object cannot satisfy the mapping contract."""
    file_handler = MagicMock()
    file_handler.load_json.return_value = []
    file_path = Path("validated/device.json")
    data = LazyJsonFileMapping(file_handler, file_path)

    with pytest.raises(TypeError, match=r"Expected a JSON object in 'validated/device.json'\."):
        len(data)
