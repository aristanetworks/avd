# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any
from unittest.mock import patch

from ansible.plugins.action import ActionBase

from ansible_collections.arista.avd.plugins.action import cv_workflow
from pyavd._cv.workflows.models import DeployToCvResult

if TYPE_CHECKING:
    from pyavd._cv.workflows.models import CVDeviceDeployment


async def simulate_deployment(device_deployments: list[CVDeviceDeployment], **kwargs: Any) -> DeployToCvResult:
    """Emit controlled diagnostics without opening a CloudVision connection."""
    case = kwargs["workspace"].name
    logging.getLogger("pyavd._cv").warning("CV_LOGGING_PROBE_pyavd_%s", case)
    logging.getLogger("urllib3.connectionpool").warning("CV_LOGGING_PROBE_urllib3_%s", case)
    logging.getLogger("grpclib.client").error("CV_LOGGING_PROBE_ERROR_%s", case)
    logging.getLogger("pyavd._cv").critical("CV_LOGGING_PROBE_CRITICAL_%s", case)
    failed = case.startswith("failure")
    config = device_deployments[0].eos_config
    assert config is not None
    return DeployToCvResult(
        failed=failed,
        warnings=[f"CV_WORKFLOW_WARNING_{case}"],
        errors=[ValueError("Workflow rejected deployment")] if failed else [],
        deployed_configs=[config],
    )


class ActionModule(ActionBase):
    """Run the production CV action, replacing only the remote deployment function."""

    def run(self, tmp: Any = None, task_vars: dict[str, Any] | None = None) -> dict[str, Any]:
        """Keep real argument validation, logging, serialization, and Ansible result handling."""
        action = cv_workflow.ActionModule(
            task=self._task,
            connection=self._connection,
            play_context=self._play_context,
            loader=self._loader,
            templar=self._templar,
            shared_loader_obj=self._shared_loader_obj,
        )
        action.ansible_name = "arista.avd.cv_workflow"
        with patch.object(cv_workflow, "deploy_to_cv", side_effect=simulate_deployment):
            return action.run(tmp=tmp, task_vars=task_vars)
