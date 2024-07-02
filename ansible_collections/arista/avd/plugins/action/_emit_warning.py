# Copyright (c) 2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Temporary file to emit a warning."""

from ansible.plugins.action import ActionBase
from ansible.utils.display import Display

display = Display()

__metaclass__ = type


class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = {}

        result = super().run(tmp, task_vars)
        del tmp

        if self._task.args:
            message = self._task.args.get("message")

            display.warning(message)

        return result
