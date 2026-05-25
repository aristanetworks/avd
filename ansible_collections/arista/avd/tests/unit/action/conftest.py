# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any
from unittest.mock import MagicMock

import pytest

if TYPE_CHECKING:
    from collections.abc import Callable, Generator


@pytest.fixture(autouse=True)
def reset_avd_logger() -> Generator[None, None, None]:
    logger = logging.getLogger("ansible_collections.arista.avd")
    original_propagate = logger.propagate
    original_handlers = logger.handlers[:]
    original_level = logger.level
    logger.propagate = True
    logger.handlers = []
    yield
    logger.propagate = original_propagate
    logger.handlers = original_handlers
    logger.setLevel(original_level)


@pytest.fixture
def action_module(request: pytest.FixtureRequest) -> Callable[..., Any]:
    """Factory fixture that builds the test module's ``ActionModule`` with mocked Ansible deps."""
    action_module_cls = request.module.ActionModule

    def _factory(task_args: dict | None = None) -> Any:
        mock_task = MagicMock()
        mock_task.args = task_args if task_args is not None else {}
        mock_task.async_val = False
        mock_task.check_mode = False
        return action_module_cls(
            task=mock_task,
            connection=MagicMock(),
            play_context=MagicMock(),
            loader=MagicMock(),
            templar=MagicMock(),
            shared_loader_obj=MagicMock(),
        )

    return _factory
