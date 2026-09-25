# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from ansible.plugins.action import ActionBase

if TYPE_CHECKING:
    from ansible.executor.task_vars import TaskVars


class ActionModule(ActionBase):
    """Warn about or reject legacy unprefixed role variables."""

    TRANSFERS_FILES = False

    def run(self, tmp: str | None = None, task_vars: TaskVars | None = None) -> dict[str, Any]:
        """Inspect task and host variables without templating their values."""
        del tmp
        result = super().run(task_vars=task_vars)
        task_vars = task_vars or {}

        role_name = self._task.args.get("role_name")
        aliases = self._task.args.get("aliases")
        mode = self._task.args.get("mode", "warning")

        if not isinstance(role_name, str) or not role_name:
            return {**result, "failed": True, "msg": "'role_name' must be a non-empty string."}
        if not isinstance(aliases, Mapping) or not all(isinstance(key, str) and isinstance(value, str) for key, value in aliases.items()):
            return {**result, "failed": True, "msg": "'aliases' must be a dictionary mapping legacy variable names to canonical variable names."}
        if mode not in {"warning", "error", "silent"}:
            return {**result, "failed": True, "msg": "'mode' must be one of: warning, error, silent."}

        hostvars = task_vars.get("hostvars", {})
        host_variable_scopes: list[Mapping[str, Any]] = []
        if isinstance(hostvars, Mapping):
            host_variable_scopes.extend(host_vars for host_vars in hostvars.values() if isinstance(host_vars, Mapping))

        current_host_vars: Mapping[str, Any] = {}
        inventory_hostname = task_vars.get("inventory_hostname")
        if isinstance(hostvars, Mapping) and isinstance(inventory_hostname, str):
            candidate_host_vars = hostvars.get(inventory_hostname, {})
            if isinstance(candidate_host_vars, Mapping):
                current_host_vars = candidate_host_vars

        used_aliases = sorted(
            (legacy_name, canonical_name)
            for legacy_name, canonical_name in aliases.items()
            if (legacy_name in task_vars and canonical_name not in task_vars)
            or (
                not (canonical_name in task_vars and canonical_name not in current_host_vars)
                and any(legacy_name in variables and canonical_name not in variables for variables in host_variable_scopes)
            )
        )
        result["changed"] = False
        result["legacy_aliases"] = [alias[0] for alias in used_aliases]

        if not used_aliases or mode == "silent":
            return result

        alias_text = ", ".join(f"'{legacy_name}' -> '{canonical_name}'" for legacy_name, canonical_name in used_aliases)
        message = f"The {role_name} role is using legacy variable aliases: {alias_text}. Update to the role-prefixed variable names."
        if mode == "error":
            return {**result, "failed": True, "msg": message}

        self._display.warning(message)
        return result
