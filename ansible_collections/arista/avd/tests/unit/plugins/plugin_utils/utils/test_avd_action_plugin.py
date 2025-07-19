# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from unittest.mock import patch

import pytest
from ansible.errors import AnsibleActionFail

from ansible_collections.arista.avd.plugins.plugin_utils.utils import AvdActionPlugin


def test_run_success(avd_action_plugin_instance: AvdActionPlugin) -> None:
    """Tests that run() calls run_plugin() and returns its result on success."""
    task_vars = {"some_var": "some_value"}
    expected_result = {"status": "success", "changed": True}

    with patch.object(avd_action_plugin_instance, "run_plugin", return_value=expected_result) as mock_run_plugin:
        result = avd_action_plugin_instance.run(task_vars=task_vars)

        mock_run_plugin.assert_called_once_with(task_vars)
        assert all(item in result.items() for item in expected_result.items())


def test_run_failure(avd_action_plugin_instance: AvdActionPlugin) -> None:
    """Tests that run() catches an exception from run_plugin() and raises AnsibleActionFail."""
    task_vars = None
    original_exception = ValueError("Something went wrong inside the plugin")

    with patch.object(avd_action_plugin_instance, "run_plugin", side_effect=original_exception) as mock_run_plugin:
        with pytest.raises(AnsibleActionFail) as exc_info:
            avd_action_plugin_instance.run(task_vars=task_vars)

        mock_run_plugin.assert_called_once_with(task_vars)
        assert "Error during plugin execution" in str(exc_info.value)
        assert str(original_exception) in str(exc_info.value)
