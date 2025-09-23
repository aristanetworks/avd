# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from typing import Any
from unittest.mock import MagicMock

import pytest
from ansible.errors import AnsibleActionFail
from ansible.utils.display import Display

from ansible_collections.arista.avd.plugins.plugin_utils.utils.avd_action_plugin import AvdActionPlugin


class TestAvdActionPlugin:
    """Test suite for the AvdActionPlugin base class."""

    def _plugin_factory(self, cls: type[AvdActionPlugin]) -> AvdActionPlugin:
        """Factory method to instantiate a plugin with mocks for testing."""
        # Create mock objects for the Ansible ActionBase constructor arguments
        mock_task = MagicMock()
        mock_task.args = {}
        mock_task.async_val = False
        mock_task.check_mode = False

        # Create a mock Display to capture all calls
        mock_display = MagicMock(spec=Display)
        mock_display.verbosity = 0

        # Instantiate the plugin class with a full set of mocks
        plugin_instance = cls(
            task=mock_task, connection=MagicMock(), play_context=MagicMock(), loader=MagicMock(), templar=MagicMock(), shared_loader_obj=MagicMock()
        )
        plugin_instance._display = mock_display

        return plugin_instance

    def test_run_success(self) -> None:
        """Tests a successful run of the plugin."""

        class ActionModule(AvdActionPlugin):
            def main(self, task_vars: dict[str, Any]) -> None:
                _unused = task_vars
                self.result["status"] = "success"

        plugin = self._plugin_factory(cls=ActionModule)

        result = plugin.run(task_vars={})

        assert result["status"] == "success"
        assert "failed" not in result

    def test_run_failure_recast_as_ansible_exception(self) -> None:
        """Tests that a generic exception in main() is recast as AnsibleActionFail."""

        class ActionModule(AvdActionPlugin):
            def main(self, task_vars: dict[str, Any]) -> None:
                _unused = task_vars
                msg = "Something went wrong"
                raise ValueError(msg)

        plugin = self._plugin_factory(ActionModule)

        with pytest.raises(AnsibleActionFail, match="Error during plugin execution: Something went wrong"):
            plugin.run(task_vars={})
