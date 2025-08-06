# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from unittest.mock import Mock

from ansible_collections.arista.avd.plugins.plugin_utils.utils import DeprecatedDict


def test__deprecated_dict(mock_display: Mock) -> None:
    """Test to verify that DeprecatedDict emits a deprecation warning on first access."""
    test_dict = {"test_key1": "test_value_1", "test_key2": "test_value_2"}

    # Testing with __getitem__
    deprecated_dict = DeprecatedDict(test_dict, _display=mock_display, _message="This dict is deprecated")
    mock_display.assert_not_called()
    _unused = deprecated_dict["test_key1"]
    deprecated_method: Mock = mock_display.deprecated
    deprecated_method.assert_called_once_with(msg="This dict is deprecated", version="6.0.0", collection_name="arista.avd", removed=False)
    _unused = deprecated_dict["test_key1"]
    _unused = deprecated_dict["test_key2"]
    deprecated_method.assert_called_once_with(msg="This dict is deprecated", version="6.0.0", collection_name="arista.avd", removed=False)

    mock_display.reset_mock()
    # Testing with .get()
    deprecated_dict = DeprecatedDict(test_dict, _display=mock_display, _message="This dict is deprecated")
    mock_display.assert_not_called()
    _unused = deprecated_dict.get("test_key1")
    deprecated_method: Mock = mock_display.deprecated
    deprecated_method.assert_called_once_with(msg="This dict is deprecated", version="6.0.0", collection_name="arista.avd", removed=False)
    _unused = deprecated_dict.get("test_key1")
    _unused = deprecated_dict.get("test_key2")
    deprecated_method.assert_called_once_with(msg="This dict is deprecated", version="6.0.0", collection_name="arista.avd", removed=False)
