# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from pyavd._cv.client.exceptions import CVClientException, CVDecommissioningFailed
from pyavd._cv.workflows.create_workspace_on_cv import create_workspace_on_cv
from pyavd._cv.workflows.finalize_workspace_on_cv import finalize_workspace_on_cv
from pyavd._cv.workflows.models import CVWorkspace, DeployToCvResult

if TYPE_CHECKING:
    from pyavd._cv.client import CVClient


async def decommission_devices(
    cv_client: CVClient,
    device_ids: list[str],
    workspace: CVWorkspace | None = None,
    logger: logging.Logger | None = None,
) -> None:
    """
    Decommission devices on CloudVision using the new Studio aware decommissioning workflow.

    Args:
        cv_client: An active and authenticated CVClient instance.
        device_ids: List of device serial numbers to decommission.
        workspace: CloudVision Workspace to create/build/submit.
        logger: Logger instance.

    Returns:
        None.
    """
    if logger is None:
        logger = logging.getLogger(__name__)

    result = DeployToCvResult(workspace=workspace or CVWorkspace(), change_control=None)

    try:
        # Create a workspace
        await create_workspace_on_cv(workspace=result.workspace, cv_client=cv_client)

        try:
            # Decommission devices
            logger.info("Decommissioning devices %s in workspace %s", device_ids, result.workspace.id)
            await cv_client.set_topology_decommissions(device_ids=device_ids, workspace_id=result.workspace.id)
            logger.info("Getting the decommissioning status of all devices in workspace %s", result.workspace.id)
            # Check for device decommissioning status to be successful
            decommission_status = await cv_client.get_all_decommissions(device_ids=device_ids, workspace_id=result.workspace.id, state="success")
            if decommission_status.error != "":
                decommission_status.state = "failed"
                logger.info("decommission_status: %s", decommission_status)
                msg = f"Decommission failed during execution: {decommission_status.error}"
                raise CVDecommissioningFailed(msg)

            decommission_status.state = "success"

        except CVClientException as e:
            result.errors.append(e)
            result.failed = True

        # Build, submit or abandon Workspace. If failed, we always abandon.
        if result.failed:
            logger.warning("Abandoning workspace %s due to errors.", result.workspace.id)
            await cv_client.abandon_workspace(workspace_id=result.workspace.id)
            result.workspace.state = "abandoned"
            return result

        # Build and submit the workspace
        await finalize_workspace_on_cv(workspace=result.workspace, cv_client=cv_client)

    except CVClientException as e:
        result.errors.append(e)
        result.failed = True

    return result
