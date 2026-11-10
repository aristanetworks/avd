# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Any

from ansible.vars.hostvars import HostVarsVars

from ansible_collections.arista.avd.plugins.plugin_utils.constants import ANSIBLE_ABOVE_2_19

# Remove once we drop ansible-core <2.20; ansible-test then pins coverage >=7.10.1.
if TYPE_CHECKING:  # pragma: no cover
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.plugins.action import ActionBase
    from ansible.vars.manager import VariableManager


class ActionPluginVars:
    """Provides access to Ansible host variables resolved for the current action plugin context."""

    def __init__(self, action_plugin: ActionBase) -> None:
        """
        Initializes the accessor with an Ansible action plugin instance to capture context.

        Args:
            action_plugin: The Ansible ActionBase plugin instance currently executing.
        """
        self.action_plugin: ActionBase = action_plugin
        self.task: Task = action_plugin._task
        self.play: Play = self.task.get_play()
        self.loader: DataLoader = self.task.get_loader()
        self.variable_manager: VariableManager = self.task.get_variable_manager()
        self.inventory: InventoryManager = self.variable_manager._inventory

    def __getitem__(self, hostname: str) -> HostVarsVars:
        """
        Provides dictionary-like access to a host's variables, processed for templates.

        Args:
            hostname: The name of the host.

        Returns:
            A HostVarsVars object wrapping the host's variables for templating.

        Raises:
            KeyError: If the hostname is not found.
        """
        variables = self._get_raw_variables(hostname)

        # TODO: Cleanup once our oldest supported ansible-core version is 2.19. Gotta love breaking signatures.
        if not ANSIBLE_ABOVE_2_19:
            return HostVarsVars(variables=variables, loader=self.loader)  # pyright: ignore[reportCallIssue]

        return HostVarsVars(variables=variables, loader=self.loader, host=hostname)  # pyright: ignore[reportCallIssue]

    def _get_raw_variables(self, hostname: str) -> dict[str, Any]:
        """
        Retrieves the raw variables for a specific host using the captured context.

        Args:
            hostname: The name of the host for which to retrieve variables.

        Returns:
            A dictionary containing the host's variables.

        Raises:
            KeyError: If the specified hostname is not found in the inventory.
        """
        host = self.inventory.get_host(hostname)
        if host is None:
            msg = f"Host '{hostname}' not found in Ansible inventory."
            raise KeyError(msg)

        return self.variable_manager.get_vars(
            play=self.play,
            host=host,
            task=self.task,
            include_hostvars=False,
        )
