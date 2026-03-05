# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Any

from pyavd._utils import AVDTemplar

if TYPE_CHECKING:
    from ansible.plugins.action import ActionBase

from .compile_searchpath import compile_searchpath


def get_templar(action_plugin_instance: ActionBase, task_vars: dict[str, Any]) -> AVDTemplar:
    """
    Return a new AVDTemplar instance based on the action plugin instance.

    The templar is loaded with new searchpath based on
    ".ansible_search_path" from the given task_vars.

    Args:
        action_plugin_instance: The Ansible ActionBase plugin instance
        task_vars: Task variables containing ansible_search_path

    Returns:
        AVDTemplar instance with configured templar, loader, and searchpath
    """
    searchpath = compile_searchpath(task_vars.get("ansible_search_path", []))
    templar = action_plugin_instance._templar.copy_with_new_env(searchpath=searchpath)
    loader = action_plugin_instance._task.get_loader()
    return AVDTemplar(templar, loader, searchpath)
