# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Fixtures for testing the utils modules."""

from pathlib import Path

import logging
import pytest

from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from ansible.playbook.block import Block
from ansible.playbook.play import Play
from ansible.playbook.task import Task
from ansible.vars.manager import VariableManager

TESTS_PATH = Path(__file__).parents[4]
DEFAULT_INVENTORY_PATH = TESTS_PATH / "inventory/inventory.yml"

DEFAULT_PLAY_DATA = {"name": "Test Play", "hosts": "all", "tasks": [{"name": "Task from Play", "debug": {"msg": "Hello from Play"}}]}

DEFAULT_BLOCK_DATA = {"name": "Test Block", "block": [{"name": "Task from Block", "debug": {"msg": "Hello from Block"}}]}

DEFAULT_TASK_DATA = {"name": "Test Task", "debug": {"msg": "Hello from Task"}}


class MinimalActionPlugin:
    """Minimal Ansible action plugin for testing."""

    def __init__(self, task: Task) -> None:
        """Initialize with a dummy Ansible task."""
        self._task = task


@pytest.fixture
def ansible_task(request: pytest.FixtureRequest) -> Task:
    """Build a dummy Ansible task with parametrized data.

    Parameters can be specified using indirect parametrization:

    ```python
    @pytest.mark.parametrize("ansible_task", [
        {"task_data": {...}, "block_data": {...}, "play_data": {...}, "inventory_path": Path(...)}
    ], indirect=True)
    ```
    """
    # Get parameters or use defaults
    params = getattr(request, "param", {})
    inventory_path = params.get("inventory_path", DEFAULT_INVENTORY_PATH)
    task_data = params.get("task_data", DEFAULT_TASK_DATA)
    block_data = params.get("block_data", DEFAULT_BLOCK_DATA)
    play_data = params.get("play_data", DEFAULT_PLAY_DATA)

    # Setup Ansible objects
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=[inventory_path.as_posix()])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    # Load play, block, and task
    play = Play.load(play_data, variable_manager=variable_manager, loader=loader)
    block = Block.load(block_data, play, variable_manager=variable_manager, loader=loader)
    return Task.load(task_data, block, variable_manager=variable_manager, loader=loader)


@pytest.fixture
def anta_record() -> logging.LogRecord:
    """Create a log record from an ANTA library."""
    return logging.LogRecord(
        name="anta.runner",
        level=logging.INFO,
        pathname="",
        lineno=0,
        msg="Hello from ANTA",
        args=(),
        exc_info=None
    )


@pytest.fixture
def non_anta_record() -> logging.LogRecord:
    """Create a log record from a non-ANTA library."""
    return logging.LogRecord(
        name="pyavd",
        level=logging.INFO,
        pathname="",
        lineno=0,
        msg="Hello from PyAVD",
        args=(),
        exc_info=None
    )


@pytest.fixture
def warning_record() -> logging.LogRecord:
    """Create a warning log record from an ANTA library."""
    return logging.LogRecord(
        name="anta.runner",
        level=logging.WARNING,
        pathname="",
        lineno=0,
        msg="Warning from ANTA",
        args=(),
        exc_info=None
    )
