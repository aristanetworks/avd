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
    Tests can pass ``ansible_name`` to model plugin metadata normally injected by Ansible's plugin loader.
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
        if ansible_name is not None:
            module.ansible_name = ansible_name
        return module

    return _factory
