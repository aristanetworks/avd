# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from logging import getLogger
from typing import TYPE_CHECKING

from pyavd._cv.client.exceptions import CVClientException
from pyavd._cv.workflows.create_workspace_on_cv import create_workspace_on_cv
from pyavd._cv.workflows.finalize_workspace_on_cv import finalize_workspace_on_cv
from pyavd._cv.workflows.models import CVWorkspace, DeployToCvResult

if TYPE_CHECKING:
    from pyavd._cv.client import CVClient

LOGGER = getLogger(__name__)


async def decommission_devices(
    cv_client: CVClient,
    device_ids: list[str],
    workspace: CVWorkspace | None = None,
) -> DeployToCvResult:
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
    result = DeployToCvResult(workspace=workspace or CVWorkspace(), change_control=None)

    try:
        # 1. Create a workspace
        await create_workspace_on_cv(workspace=result.workspace, cv_client=cv_client)

        try:
            # 2. Decommission devices
            LOGGER.info("Decommissioning devices %s in workspace %s", device_ids, result.workspace.id)
            await cv_client.decommission_device(device_ids=device_ids, workspace_id=result.workspace.id)
        except CVClientException as e:
            result.errors.append(e)
            result.failed = True

        # Build, submit or abandon Workspace. If failed, we always abandon.
        if result.failed:
            LOGGER.warning("Abandoning workspace %s due to errors.", result.workspace.id)
            await cv_client.abandon_workspace(workspace_id=result.workspace.id)
            result.workspace.state = "abandoned"
            return result

        # 3. Build and submit the workspace
        LOGGER.info("Building and submitting workspace...")
        await finalize_workspace_on_cv(workspace=result.workspace, cv_client=cv_client)

    except CVClientException as e:
        result.errors.append(e)
        result.failed = True

    return result
