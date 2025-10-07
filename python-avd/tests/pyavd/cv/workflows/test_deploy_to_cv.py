# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import tempfile
from contextlib import nullcontext as does_not_raise
from logging import INFO
from typing import TYPE_CHECKING
from unittest.mock import patch

import pytest

from pyavd._cv.workflows.deploy_to_cv import deploy_to_cv
from pyavd._cv.workflows.models import CloudVision, CVEosConfig, CVWorkspace
from tests.pyavd.cv.constants import (
    MOCKED_WORKSPACE_DESCRIPTION,
    MOCKED_WORKSPACE_ID,
    MOCKED_WORKSPACE_NAME,
    MOCKED_WORKSPACE_REQUEST_ID_BUILD_SUCCESS,
    MOCKED_WORKSPACE_REQUEST_ID_SUBMIT_SUCCESS,
    MOCKED_WORKSPACE_REQUESTED_STATE_SUBMITTED,
)
from tests.pyavd.cv.mockery import mocked_cvdevices

if TYPE_CHECKING:
    from pyavd._cv.client import CVClient


@pytest.mark.asyncio
@pytest.mark.parametrize("cv_client", [{"static_recording": True, "cv_version": "CVaaS"}], ids=["CV_CLIENT_STATIC_RECORDINGS"], indirect=True)
@pytest.mark.parametrize(("workspace_force_submission"), [pytest.param(False, id="UNFORCED"), pytest.param(True, id="FORCED")])
async def test_deploy_to_cv(
    caplog: pytest.LogCaptureFixture,
    cv_client: CVClient,
    workspace_force_submission: bool,
) -> None:
    """
    Test full functionality of the deploy_to_cv by building and submitting (both forced and unforced) Workspace with a single streaming device.

    Exact test steps:
    -   description: Fethc Workspace status
        request: 'WorkspaceRequest(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'), time=None)'
        targeted_file: 'arista.workspace.v1.WorkspaceService/GetOne/www.cv-prod-us-central1-c.arista.io/a996cf0f4bc694971e5d4069f481faaba80f68b2.json'

    -   description: Create Workspace
        request: 'WorkspaceConfigSetRequest(value=WorkspaceConfig(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'),
            display_name='MOCKED_WS_NAME', description='MOCKED_WS_DESCRIPTION'))'
        targeted_file: 'arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/ce73310ec5154d57ac888fc8f93d69893962d804.json'

    -   description: Fetch device status
        request: 'DeviceStreamRequest(partial_eq_filter=[Device(key=DeviceKey(device_id=None), hostname='avd-ci-leaf2', system_mac_address=None)],
            time=TimeBounds(start=None, end=None))'
        targeted_file: 'arista.inventory.v1.DeviceService/GetAll/www.cv-prod-us-central1-c.arista.io/effc85b759a4d35ba98ae7c22bcef828c070752d.json'

    -   description: Fetch I&T Studio inputs
        request: 'InputsStreamRequest(partial_eq_filter=[Inputs(key=InputsKey(studio_id='TOPOLOGY', workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'))],
            time=None)'
        targeted_file: 'arista.studio.v1.InputsService/GetAll/www.cv-prod-us-central1-c.arista.io/0ab698a68a7f9f86eeda70fba362f57cb2f07fc4.json'

    -   description: Create configlet
        request: 'ConfigletConfigSetSomeRequest(values=[ConfigletConfig(key=ConfigletKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e',
            configlet_id='avd-B51AA89B6E51E89E1422107EDE3A9438'), display_name='TEST_CONFIGLET_NAME', description='Configuration created and
            uploaded by AVD for avd-ci-leaf2', body='alias test test')])'
        targeted_file: 'arista.configlet.v1.ConfigletConfigService/SetSome/www.cv-prod-us-central1-c.arista.io/9928854663237cf59f5710079cb64befccffd7cc.json'

    -   description: Fetch Configlet assignments
        request: 'ConfigletAssignmentStreamRequest(partial_eq_filter=[ConfigletAssignment(key=ConfigletAssignmentKey(workspace_id=
            'ws-cbf7c7ea-a57c-481d-b96b-97c12856395e', configlet_assignment_id='avd-configlets'))], time=TimeBounds(start=None, end=None))'
        targeted_file: 'arista.configlet.v1.ConfigletAssignmentService/GetAll/www.cv-prod-us-central1-c.arista.io/0462b04aed494937b07702371f123831a4e81036.json'

    -   description: Fetch configlets assignments
        request: Too long. Please consult JSON file for details.
        targeted_file: 'arista.configlet.v1.ConfigletAssignmentService/GetAll/www.cv-prod-us-central1-c.arista.io/15b2c867c1abf9b0d425ca76fa4327294c18c376.json'

    -   description: Build Workspace
        request: 'WorkspaceConfigSetRequest(value=WorkspaceConfig(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'),
            request=Request.START_BUILD, request_params=RequestParams(request_id='req-914310f3-08dd-4239-bd42-6d78bf781229')))'
        targeted_file: 'arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/1fdd6fcd02728621447eeb8a1d8c9cbfdd9201c9.json'

    -   description: Fetch build results
        request: 'WorkspaceStreamRequest(partial_eq_filter=[Workspace(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'))])'
        targeted_file: 'arista.workspace.v1.WorkspaceService/Subscribe/www.cv-prod-us-central1-c.arista.io/1560c66d73da2be39448d710f15853fb124b2548.json'

    -   description: Submit Workspace (UNFORCED use case)
        request: 'WorkspaceConfigSetRequest(value=WorkspaceConfig(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'),
            request=Request.SUBMIT, request_params=RequestParams(request_id='req-b8f4e511-58de-4afe-99f0-b75abf980131')))'
        targeted_file: 'arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/ba83e98eab07691e8b079958618ab2973822bfe8.json'

    -   description: Submit Workspace (FORCED use case)
        request: 'WorkspaceConfigSetRequest(value=WorkspaceConfig(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'),
            request=Request.SUBMIT_FORCE, request_params=RequestParams(request_id='req-b8f4e511-58de-4afe-99f0-b75abf980131')))'
        targeted_file: 'arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/47049c8a6b520f110540f81bcd892ba0e4954908.json'

    -   description: Fetch submit results
        request: 'WorkspaceStreamRequest(partial_eq_filter=[Workspace(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'))])'
        targeted_file: 'arista.workspace.v1.WorkspaceService/Subscribe/www.cv-prod-us-central1-c.arista.io/1560c66d73da2be39448d710f15853fb124b2548.json'
    """
    with (
        caplog.at_level(INFO),
        does_not_raise(),
        patch(
            "pyavd._cv.client.workspace.uuid4",
            side_effect=[
                MOCKED_WORKSPACE_REQUEST_ID_BUILD_SUCCESS["id"].removeprefix("req-"),
                MOCKED_WORKSPACE_REQUEST_ID_SUBMIT_SUCCESS["id"].removeprefix("req-"),
            ],
        ),
        patch("pyavd._cv.workflows.deploy_to_cv.CVClient", return_value=cv_client),
        tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", delete=True) as temp_configlet_file,
    ):
        temp_configlet_file.write("alias test test")
        temp_configlet_file.flush()

        result = await deploy_to_cv(
            cloudvision=CloudVision(
                servers="",
                token=None,
                username=None,
                password=None,
                verify_certs=False,
                proxy_host=None,
                proxy_port=None,
                proxy_username=None,
                proxy_password=None,
            ),
            workspace=CVWorkspace(
                name=MOCKED_WORKSPACE_NAME,
                description=MOCKED_WORKSPACE_DESCRIPTION,
                id=MOCKED_WORKSPACE_ID,
                requested_state=MOCKED_WORKSPACE_REQUESTED_STATE_SUBMITTED,
                force=workspace_force_submission,
            ),
            configs=[
                CVEosConfig(
                    file=temp_configlet_file.name, device=next(iter(mocked_cvdevices(hostnames=["avd-ci-leaf2"]))), configlet_name="TEST_CONFIGLET_NAME"
                )
            ],
        )

    # Assess result
    assert not result.failed

    # Assert number of returned warnings
    assert len(result.warnings) == 0

    # Assert number of returned errors
    assert len(result.errors) == 0

    # Assert returned workspace object
    assert result.workspace.name == MOCKED_WORKSPACE_NAME
    assert result.workspace.description == MOCKED_WORKSPACE_DESCRIPTION
    assert result.workspace.id == MOCKED_WORKSPACE_ID
    assert result.workspace.requested_state == MOCKED_WORKSPACE_REQUESTED_STATE_SUBMITTED
    assert result.workspace.force == workspace_force_submission
    assert result.workspace.state == MOCKED_WORKSPACE_REQUESTED_STATE_SUBMITTED
