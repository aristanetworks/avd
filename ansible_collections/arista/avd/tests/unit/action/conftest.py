# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import importlib
import logging
from typing import TYPE_CHECKING, Any
from unittest.mock import MagicMock

import pytest

if TYPE_CHECKING:
    from collections.abc import Callable, Generator

    from ansible.plugins.action import ActionBase


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
def action_module(request: pytest.FixtureRequest) -> Callable[..., ActionBase]:
    """
    Factory fixture that builds the test module's ``ActionModule`` with mocked Ansible deps.

    Resolves the plugin's ``ActionModule`` class from the ``MODULE_PATH`` constant defined
    in the calling test file, so the import can stay under ``TYPE_CHECKING``.
    """
    action_module_cls = importlib.import_module(request.module.MODULE_PATH).ActionModule

    # Some plugin modules (e.g. eos_cli_config_gen) mutate the AVD logger at import time.
    # Re-apply the clean state ``reset_avd_logger`` set up, in case the import undid it.
    avd_logger = logging.getLogger("ansible_collections.arista.avd")
    avd_logger.propagate = True
    avd_logger.handlers = []

    def _factory(task_args: dict | None = None) -> ActionBase:
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
