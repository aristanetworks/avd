# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import Any
from unittest.mock import patch

from ansible.plugins.action import ActionBase

from ansible_collections.arista.avd.plugins.action import anta_workflow


async def simulate_runner(
    result_manager: anta_workflow.ResultManager,
    _inventory: anta_workflow.AntaInventory,
    _catalog: anta_workflow.AntaCatalog,
    **kwargs: Any,
) -> None:
    """Emit controlled results and diagnostics without opening an EOS connection."""
    if "workflow-error" in (kwargs.get("tags") or set()):
        anta_workflow.LOGGER.error("ANTA_WORKFLOW_PROBE_ERROR")
        return

    for status in ("success", "failure", "error"):
        result_manager.add(
            anta_workflow.TestResult(
                name="anta-leaf1",
                test=f"Probe{status.title()}",
                categories=["integration"],
                description=f"Simulated ANTA {status} result",
                result=status,
            )
        )


class ActionModule(ActionBase):
    """Run the production ANTA action, replacing only the remote test execution function."""

    def run(self, tmp: Any = None, task_vars: dict[str, Any] | None = None) -> dict[str, Any]:
        """Keep real validation, worker execution, logging, reports, and Ansible result handling."""
        action = anta_workflow.ActionModule(
            task=self._task,
            connection=self._connection,
            play_context=self._play_context,
            loader=self._loader,
            templar=self._templar,
            shared_loader_obj=self._shared_loader_obj,
        )
        action.ansible_name = "arista.avd.anta_workflow"
        with patch.object(anta_workflow, "anta_runner", new=simulate_runner):
            return action.run(tmp=tmp, task_vars=task_vars)
