# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from unittest.mock import MagicMock

import pytest

from ansible_collections.arista.avd.plugins.action.set_vars import ActionModule


def _action_module(args: dict) -> ActionModule:
    task = MagicMock()
    task.args = args
    return ActionModule(
        task=task,
        connection=MagicMock(),
        play_context=MagicMock(),
        loader=MagicMock(),
        templar=MagicMock(),
        shared_loader_obj=MagicMock(),
    )


@pytest.mark.parametrize(
    "args",
    [
        pytest.param({}, id="empty args"),
        pytest.param({"foo": "bar"}, id="single key"),
        pytest.param({"foo": "bar", "baz": 42, "nested": {"a": [1, 2, 3]}}, id="multiple keys with nested values"),
    ],
)
def test_run_returns_args_as_ansible_facts(args: dict) -> None:
    """Verify run() returns task args under the ansible_facts key."""
    action = _action_module(args)
    result = action.run(task_vars={"existing": "value"})
    assert result == {"ansible_facts": args}


def test_run_with_none_task_vars() -> None:
    """Verify run() handles task_vars=None without raising."""
    args = {"foo": "bar"}
    action = _action_module(args)
    result = action.run(task_vars=None)
    assert result == {"ansible_facts": args}


def test_run_default_task_vars() -> None:
    """Verify run() works with default arguments."""
    args = {"key": "value"}
    action = _action_module(args)
    result = action.run()
    assert result == {"ansible_facts": args}


def test_run_does_not_mutate_task_args() -> None:
    """Verify run() returns a reference to the original task args without modifying them."""
    args = {"foo": "bar"}
    action = _action_module(args)
    result = action.run(task_vars={})
    assert result["ansible_facts"] is args
