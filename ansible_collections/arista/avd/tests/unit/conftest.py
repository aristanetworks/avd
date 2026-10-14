# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Any
from unittest.mock import MagicMock

import pytest

if TYPE_CHECKING:
    from collections.abc import Callable

    from ansible.plugins.action import ActionBase


@pytest.fixture
def action_module() -> Callable[..., ActionBase]:
    """
    Factory that builds an ActionModule instance with mocked Ansible plumbing.

    Each test passes the specific ``ActionModule`` class under test.
    The plugin name is inferred for AVD action plugins and defaults to ``pytest_action_plugin`` for synthetic test classes.
    Tests can override it with ``ansible_name``.
    """

    def _factory(action_module_cls: type[ActionBase], task_args: dict[str, Any] | None = None, *, ansible_name: str | None = None) -> ActionBase:
        mock_task = MagicMock()
        mock_task.args = task_args or {}
        mock_task.async_val = False
        mock_task.check_mode = False
        module = action_module_cls(
            task=mock_task,
            connection=MagicMock(),
            play_context=MagicMock(),
            loader=MagicMock(),
            templar=MagicMock(),
            shared_loader_obj=MagicMock(),
        )
        # Ansible 2.18 and earlier have no default ansible_name; the plugin loader normally sets it.
        # Ansible 2.19+ defaults it to None, masking missing loader metadata when tests construct plugins directly.
        # Supply a valid name on every version to model a loaded plugin.
        if ansible_name is None:
            if action_module_cls.__module__.startswith("ansible_collections.arista.avd.plugins.action."):
                ansible_name = f"arista.avd.{action_module_cls.__module__.rsplit('.', 1)[-1]}"
            else:
                ansible_name = "pytest_action_plugin"
        module.ansible_name = ansible_name
        return module

    return _factory
