# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from typing import Any

from ansible_collections.arista.avd.plugins.plugin_utils.utils.avd_action_plugin import AVDActionPlugin, AVDLoggingConfig


class ActionModule(AVDActionPlugin):
    _logging_config = AVDLoggingConfig(add_hostname_context=True)

    def main(self, _task_vars: dict[str, Any]) -> None:
        """Set task arguments as ansible_facts."""
        self.result["ansible_facts"] = self._task.args
