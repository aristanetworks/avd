# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import re
from logging import DEBUG
from typing import TYPE_CHECKING
from unittest.mock import AsyncMock, patch

import pytest

from pyavd._cv.workflows.deploy_configs_to_cv import STATIC_CONFIGLET_STUDIO_ID, get_existing_device_container_ids_from_root_container
from tests.pyavd.cv.constants import MOCKED_WORKSPACE_ID

if TYPE_CHECKING:
    from pyavd._cv.client import CVClient


@pytest.mark.asyncio
@pytest.mark.parametrize("cv_client", [{"static_recording": True, "cv_version": "CVaaS"}], ids=["CV_CLIENT_STATIC_RECORDINGS"], indirect=True)
async def test_get_existing_device_container_ids_from_root_container_new_root_container(caplog: pytest.LogCaptureFixture, cv_client: CVClient) -> None:
    """
    Test creation of the new AVD root level container and adding it to configletAssignmentRoots.

    Exact test steps:
    -   description: Try to get AVD root container and its child assignments
        request: 'ConfigletAssignmentStreamRequest(partial_eq_filter=[ConfigletAssignment(key=ConfigletAssignmentKe
            (workspace_id='bfb16595-a8b0-428e-9f08-93e6a5f32973', configlet_assignment_id='new-avd-configlets'))], time=TimeBounds(start=None, end=None))'
        targeted_file: 'arista.configlet.v1.ConfigletAssignmentService/GetAll/www.cv-prod-us-central1-c.arista.io/9cd6ccdbef8b06210430e4703d73c2779fbf95bd.json'

    -   description: Create new AVD root container
        request: 'ConfigletAssignmentConfigSetRequest(value=ConfigletAssignmentConfig(key=ConfigletAssignmentKey
            (workspace_id='bfb16595-a8b0-428e-9f08-93e6a5f32973', configlet_assignment_id='new-avd-configlets'), display_name='AVD Configurations',
            description='Configurations created and uploaded by AVD', configlet_ids=RepeatedString(values=None), query='device:*',
            match_policy=MatchPolicy.MATCH_ALL, child_assignment_ids=RepeatedString(values=None)))'
        targeted_file: 'api_recordings/arista.configlet.v1.ConfigletAssignmentConfigService/Set/www.cv-prod-us-central1-c.arista.io/
            463edcd078578add345597aed1ebffb61b47bd47.json'

    -   description: Get current configletAssignmentRoots
        request: 'InputsRequest(key=InputsKey(studio_id='studio-static-configlet', workspace_id='bfb16595-a8b0-428e-9f08-93e6a5f32973',
            path=RepeatedString(values=['configletAssignmentRoots'])), time=None)'
        targeted_file: 'arista.studio.v1.InputsService/GetOne/www.cv-prod-us-central1-c.arista.io/218b79449463543915f8e63e66bdbbbd249333d3.json'

    -   description: Get current configletAssignmentRoots
        request: 'InputsConfigStreamRequest(partial_eq_filter=InputsConfig(key=InputsKey(studio_id='studio-static-configlet',
            workspace_id='bfb16595-a8b0-428e-9f08-93e6a5f32973', path=RepeatedString(values=['configletAssignmentRoots'])), remove=True), time=None)'
        targeted_file: 'arista.studio.v1.InputsConfigService/GetAll/www.cv-prod-us-central1-c.arista.io/1fbe2ebb45ada87974e6a6228efcce717950d89d.json'

    -   description: Get current configletAssignmentRoots
        request: 'InputsRequest(key=InputsKey(studio_id='studio-static-configlet', workspace_id='',
            path=RepeatedString(values=['configletAssignmentRoots'])), time=None)'
        targeted_file: 'arista.studio.v1.InputsService/GetOne/www.cv-prod-us-central1-c.arista.io/b45e9b96ea9c215914828995f6c62354ae80296f.json'

    -   description: Insert new AVD root container to the head of the configletAssignmentRoots
        request: 'InputsConfigSetRequest(value=InputsConfig(key=InputsKey(studio_id='studio-static-configlet',
            workspace_id='bfb16595-a8b0-428e-9f08-93e6a5f32973', path=RepeatedString(values=['configletAssignmentRoots'])), inputs='["new-avd-configlets",
            "avd_1cb9aa2e-4c10-5fe1-9503-78a6ba3160ab", "avd-configlets", "RECONCILE_TREE_KEY"]'))'
        targeted_file: 'arista.studio.v1.InputsConfigService/Set/www.cv-prod-us-central1-c.arista.io/54759f4b303d5407d1465eb7f647ca33cfb829f5.json'
    """
    # Mock original CVClient methods to assert them later.
    cv_client.get_configlet_containers = AsyncMock(wraps=cv_client.get_configlet_containers)
    cv_client.set_configlet_container = AsyncMock(wraps=cv_client.set_configlet_container)
    cv_client.get_studio_inputs_with_path = AsyncMock(wraps=cv_client.get_studio_inputs_with_path)
    cv_client.set_studio_inputs = AsyncMock(wraps=cv_client.set_studio_inputs)

    mocked_avd_root_container_id = "new-avd-configlets"

    with (
        caplog.at_level(DEBUG),
        patch("pyavd._cv.workflows.deploy_configs_to_cv.CONFIGLET_CONTAINER_ID", mocked_avd_root_container_id),
    ):
        child_assignment_ids: list = await get_existing_device_container_ids_from_root_container(
            workspace_id=MOCKED_WORKSPACE_ID,
            cv_client=cv_client,
        )

    cv_client.get_configlet_containers.assert_called_once_with(workspace_id=MOCKED_WORKSPACE_ID, container_ids=[mocked_avd_root_container_id])

    cv_client.set_configlet_container.assert_called_once_with(
        workspace_id=MOCKED_WORKSPACE_ID,
        container_id=mocked_avd_root_container_id,
        display_name="AVD Configurations",
        description="Configurations created and uploaded by AVD",
        query="device:*",
    )

    cv_client.get_studio_inputs_with_path.assert_called_once_with(
        studio_id=STATIC_CONFIGLET_STUDIO_ID,
        workspace_id=MOCKED_WORKSPACE_ID,
        input_path=["configletAssignmentRoots"],
        default_value=[],
    )

    cv_client.set_studio_inputs.assert_called_once_with(
        studio_id=STATIC_CONFIGLET_STUDIO_ID,
        workspace_id=MOCKED_WORKSPACE_ID,
        input_path=["configletAssignmentRoots"],
        inputs=["new-avd-configlets", "avd_1cb9aa2e-4c10-5fe1-9503-78a6ba3160ab", "avd-configlets", "RECONCILE_TREE_KEY"],
    )

    expected_log_messages: list[re.Pattern] = [
        re.compile(r"get_or_create_configlet_root_container: Got AVD root container\? False"),
        re.compile(r"deploy_configs_to_cv: Creating AVD root container 'new-avd-configlets'"),
        re.compile(r"deploy_configs_to_cv: Found 3 root containers"),
        re.compile(r"deploy_configs_to_cv: AVD root container not assigned as root container in Static Config Studio. Inserting AVD container at the top"),
    ]
    for expected_log_message in expected_log_messages:
        assert any(re.search(expected_log_message, str(record.message)) for record in caplog.records)

    assert child_assignment_ids == []
