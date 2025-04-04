# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Unit tests for the action_plugin_vars module."""

import pytest
from ansible.playbook.task import Task
from ansible.vars.hostvars import HostVarsVars

from ansible_collections.arista.avd.plugins.plugin_utils.utils import ActionPluginVars

from .conftest import MinimalActionPlugin


class TestActionPluginVars:
    """Unit tests for the ActionPluginVars class."""

    def test_init(self, ansible_task: Task) -> None:
        """Test that initialization correctly sets all attributes."""
        action_plugin = MinimalActionPlugin(ansible_task)
        action_plugin_vars = ActionPluginVars(action_plugin)

        assert action_plugin_vars.action_plugin == action_plugin
        assert action_plugin_vars.task == ansible_task
        assert action_plugin_vars.play == ansible_task.get_play()
        assert action_plugin_vars.loader == ansible_task.get_loader()
        assert action_plugin_vars.variable_manager == ansible_task.get_variable_manager()
        assert action_plugin_vars.inventory == ansible_task.get_variable_manager()._inventory

    def test_get_raw_variables_valid_host(self, ansible_task: Task) -> None:
        """Test _get_raw_variables with a valid host."""
        action_plugin = MinimalActionPlugin(ansible_task)
        action_plugin_vars = ActionPluginVars(action_plugin)

        variables = action_plugin_vars._get_raw_variables("DC1-SPINE1")
        assert isinstance(variables, dict)

    def test_get_raw_variables_invalid_host(self, ansible_task: Task) -> None:
        """Test _get_raw_variables with an invalid host raises KeyError."""
        action_plugin = MinimalActionPlugin(ansible_task)
        action_plugin_vars = ActionPluginVars(action_plugin)

        with pytest.raises(KeyError, match="Host 'non-existent-host' not found in Ansible inventory."):
            action_plugin_vars._get_raw_variables("non-existent-host")

    def test_get_raw_variables_group_vars(self, ansible_task: Task) -> None:
        """Test _get_raw_variables with variable values from group_vars."""
        action_plugin = MinimalActionPlugin(ansible_task)
        action_plugin_vars = ActionPluginVars(action_plugin)

        variables = action_plugin_vars._get_raw_variables("DC1-SPINE1")
        assert "ansible_user" in variables
        assert variables["ansible_user"] == "ansible"

    def test_getitem(self, ansible_task: Task) -> None:
        """Test __getitem__ returns a HostVarsVars instance."""
        action_plugin = MinimalActionPlugin(ansible_task)
        action_plugin_vars = ActionPluginVars(action_plugin)

        variables = action_plugin_vars["DC1-SPINE1"]
        assert isinstance(variables, HostVarsVars)
        assert "ansible_user" in variables

    @pytest.mark.parametrize(
        ("ansible_task", "variable", "expected_value"),
        [
            # Scenario 1: Task variable takes precedence (task > block > play)
            pytest.param(
                {
                    "task_data": {"name": "Test Task", "vars": {"ansible_user": "task_user"}, "debug": {"msg": "Hello from Task"}},
                    "block_data": {
                        "name": "Test Block",
                        "vars": {"ansible_user": "block_user"},
                        "block": [{"name": "Task from Block", "debug": {"msg": "Hello from Block"}}],
                    },
                    "play_data": {
                        "name": "Test Play",
                        "hosts": "all",
                        "vars": {"ansible_user": "play_user"},
                        "tasks": [{"name": "Task from Play", "debug": {"msg": "Hello from Play"}}],
                    },
                },
                "ansible_user",
                "task_user",
                id="task_wins_precedence"
            ),
            # Scenario 2: Block variable takes precedence when no task var (block > play)
            pytest.param(
                {
                    "task_data": {
                        "name": "Test Task",
                        "vars": {},  # No ansible_user at task level
                        "debug": {"msg": "Hello from Task"},
                    },
                    "block_data": {
                        "name": "Test Block",
                        "vars": {"ansible_user": "block_user"},
                        "block": [{"name": "Task from Block", "debug": {"msg": "Hello from Block"}}],
                    },
                    "play_data": {
                        "name": "Test Play",
                        "hosts": "all",
                        "vars": {"ansible_user": "play_user"},
                        "tasks": [{"name": "Task from Play", "debug": {"msg": "Hello from Play"}}],
                    },
                },
                "ansible_user",
                "block_user",
                id="block_wins_precedence"
            ),
            # Scenario 3: Play variable is used when no task or block vars
            pytest.param(
                {
                    "task_data": {
                        "name": "Test Task",
                        "vars": {},  # No ansible_user at task level
                        "debug": {"msg": "Hello from Task"},
                    },
                    "block_data": {
                        "name": "Test Block",
                        "vars": {},  # No ansible_user at block level
                        "block": [{"name": "Task from Block", "debug": {"msg": "Hello from Block"}}],
                    },
                    "play_data": {
                        "name": "Test Play",
                        "hosts": "all",
                        "vars": {"ansible_user": "play_user"},
                        "tasks": [{"name": "Task from Play", "debug": {"msg": "Hello from Play"}}],
                    },
                },
                "ansible_user",
                "play_user",
                id="play_wins_precedence"
            ),
        ],
        indirect=["ansible_task"],
    )
    def test_variable_precedence(self, ansible_task: Task, variable: str, expected_value: str) -> None:
        """Test that variable precedence is correctly applied."""
        action_plugin = MinimalActionPlugin(ansible_task)
        action_plugin_vars = ActionPluginVars(action_plugin)

        variables = action_plugin_vars["DC1-SPINE1"]
        assert variables[variable] == expected_value
