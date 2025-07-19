# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from abc import abstractmethod
from typing import Any

from ansible.errors import AnsibleActionFail
from ansible.plugins.action import ActionBase


class AvdActionPlugin(ActionBase):
    """Base class for AVD Ansible action plugins to provide common functionality."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the action plugin."""
        super().__init__(*args, **kwargs)
        self.result: dict[str, Any] = {}

    def run(self, tmp: Any = None, task_vars: dict[str, Any] | None = None) -> dict[str, Any]:
        """Ansible Action entry point."""
        if task_vars is None:
            task_vars = {}

        self.result = super().run(tmp, task_vars)
        del tmp  # tmp no longer has any effect

        try:
            return self.run_plugin(task_vars)
        except BaseException as exc:
            # Recast errors as AnsibleActionFail
            msg = f"Error during plugin execution: {exc}"
            raise AnsibleActionFail(msg) from exc

    @abstractmethod
    def run_plugin(self, task_vars: dict[str, Any]) -> dict[str, Any]:
        """This method must be implemented by child plugins with their core logic."""
