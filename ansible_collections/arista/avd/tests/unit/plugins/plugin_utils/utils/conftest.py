# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Fixtures for testing the utils modules."""

import logging
from pathlib import Path
from unittest.mock import Mock

import pytest
from ansible.cli import Display
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
    """
    Build a dummy Ansible task with parametrized data.

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


def create_log_record(name: str, level: int, msg: str, unique_id: str | None = None, args: tuple = ()) -> logging.LogRecord:
    """Helper function to create a LogRecord, optionally adding unique_id."""
    record = logging.LogRecord(
        name=name,
        level=level,
        pathname="dummy_path",
        lineno=123,
        msg=msg,
        args=args,
        exc_info=None,
        func="dummy_func",
    )
    # Simulate the filter adding the unique_id *before* it reaches the handler
    if unique_id:
        record.unique_id = unique_id
    return record


@pytest.fixture
def mock_display() -> Mock:
    """Fixture for creating a mock Ansible Display object."""
    return Mock(spec=Display)
