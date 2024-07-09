# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from asyncio import gather
from logging import getLogger

from ..._utils import batch
from ..client import CVClient
from .models import CVStudioInputs, DeployToCvResult

LOGGER = getLogger(__name__)

CONFIGLET_ID_PREFIX = "avd-"
CONFIGLET_NAME_PREFIX = "AVD_"
CONFIGLET_CONTAINER_ID = f"{CONFIGLET_ID_PREFIX}configlets"
STATIC_CONFIGLET_STUDIO_ID = "studio-static-configlet"


def get_studio_id(studio_input: CVStudioInputs) -> str:
    return studio_input.studio_id


# TODO: Cleanup if we decide to live with the limitation of overlapping inputs in favor of performance.
# async def set_multiple_studio_inputs_on_one_studio(workspace_id: str, studio_inputs: list[CVStudioInputs], cv_client: CVClient) -> None:
#     """
#     Setting multiple CVStudioInputs on the same studio one by one to avoid race conditions when updating overlapping
#     """
#     for studio_input in studio_inputs:
#         await cv_client.set_studio_inputs(
#             studio_id=studio_input.studio_id, workspace_id=workspace_id, inputs=studio_input.inputs, input_path=studio_input.input_path
#         )


async def deploy_studio_inputs_to_cv(studio_inputs: list[CVStudioInputs], result: DeployToCvResult, cv_client: CVClient) -> None:
    """
    Deploy given Studio Inputs.

    It is not supported to deploy overlapping studio inputs for the same studio.
    """

    LOGGER.info("deploy_studio_inputs_to_cv: %s", len(studio_inputs))

    if not studio_inputs:
        return

    # TODO: Cleanup if we decide to live with the limitation of overlapping inputs in favor of performance.
    # grouped_by_studio_id = groupby(sorted(studio_inputs, get_studio_id), get_studio_id)

    studio_inputs_coroutines = []
    # TODO: Cleanup if we decide to live with the limitation of overlapping inputs in favor of performance.
    # for studio_id, studio_inputs_for_one_studio in grouped_by_studio_id:
    #     studio_inputs_coroutines.append(
    #         set_multiple_studio_inputs_on_one_studio(workspace_id=result.workspace.id, studio_inputs=studio_inputs_for_one_studio, cv_client=cv_client)
    #     )

    for studio_input in studio_inputs:
        studio_inputs_coroutines.append(
            cv_client.set_studio_inputs(
                studio_id=studio_input.studio_id, workspace_id=result.workspace.id, inputs=studio_input.inputs, input_path=studio_input.input_path
            )
        )

    # Deploy studio inputs in parallel in batches of 20.
    LOGGER.info("deploy_studio_inputs_to_cv: Deploying %s Studio Inputs in batches of 20.", len(studio_inputs_coroutines))
    for index, coroutines in enumerate(batch(studio_inputs_coroutines, 20), start=1):
        LOGGER.info("deploy_studio_inputs_to_cv: Batch %s", index)
        await gather(*coroutines)

    result.deployed_studio_inputs.extend(studio_inputs)
