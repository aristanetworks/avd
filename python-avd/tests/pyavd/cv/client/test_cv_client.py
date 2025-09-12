# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import tempfile
from contextlib import AbstractContextManager
from contextlib import nullcontext as does_not_raise
from logging import INFO, getLogger
from os import environ
from typing import TYPE_CHECKING, Any
from unittest.mock import patch

import pytest

from pyavd._cv.workflows.deploy_to_cv import deploy_to_cv
from pyavd._cv.workflows.models import CloudVision, CVDevice, CVEosConfig, CVWorkspace
from tests.pyavd.cv.constants import (
    MOCKED_WORKSPACE_DESCRIPTION,
    MOCKED_WORKSPACE_ID,
    MOCKED_WORKSPACE_NAME,
    MOCKED_WORKSPACE_REQUEST_ID_BUILD_SUCCESS,
    MOCKED_WORKSPACE_REQUEST_ID_SUBMIT_SUCCESS,
    MOCKED_WORKSPACE_REQUESTED_STATE_SUBMITTED,
)

if TYPE_CHECKING:
    from pyavd._cv.client import CVClient


LOGGER = getLogger(__name__)

# Environment variables
# TODO: avoid having a default server and instead run tests to all recorded servers in offline mode.
CV_SERVER = environ.get("CV_SERVER") or "www.cv-prod-us-central1-c.arista.io"
CV_TOKEN = environ.get("CV_ACCESS_TOKEN")
RECORDING = environ.get("RECORDING")

ExpectedExceptionContext = AbstractContextManager[pytest.ExceptionInfo | None]


def _mocked_cvdevices(hostnames: list[str] | None = None, device_count: int | None = None) -> list[CVDevice]:
    """
    Generate mocked CVDevice instances.

    Parameters:
        hostnames (list[str]): List of device hostnames.
        device_count (int): Number of CVDevice instances to generate.

    Returns:
        list[CVDevice]: List of CVDevice instances.
    """
    if hostnames:
        return [CVDevice(item) for item in hostnames]
    if device_count:
        return [CVDevice(str(item), str(item), str(item)) for item in range(device_count)]
    return [CVDevice(str(item), str(item), str(item)) for item in range(1000000)]


@pytest.mark.asyncio
async def test_get_inventory_devices(cv_client: CVClient) -> None:
    result = await cv_client.get_inventory_devices()
    assert len(result) > 0


@pytest.mark.asyncio
async def test_get_inventory_devices_with_filter(cv_client: CVClient) -> None:
    result = await cv_client.get_inventory_devices([(None, None, "avd-ci-spine1")])
    assert len(result) == 1
    assert hasattr(result[0], "hostname")
    assert result[0].hostname == "avd-ci-spine1"


@pytest.mark.asyncio
@pytest.mark.parametrize("cv_client", [{"static_recording": True, "cv_version": "CVaaS"}], ids=["CV_CLIENT_STATIC_RECORDINGS"], indirect=True)
@pytest.mark.parametrize(
    ("mocked_cvdevices"),
    [
        # mocked API response: tests/pyavd/cv/mocked_api_recordings/arista.inventory.v1.DeviceService/GetAll/www.cv-prod-us-central1-c.arista.io/\\
        # effc85b759a4d35ba98ae7c22bcef828c070752d.json
        pytest.param(_mocked_cvdevices(hostnames=["avd-ci-leaf2"]), id="SINGLE_STREAMING_DEVICE"),
    ],
)
@pytest.mark.parametrize(("workspace_force_submission"), [pytest.param(False, id="UNFORCED"), pytest.param(True, id="FORCED")])
@pytest.mark.parametrize(
    (
        "workspace",
        "expected",
    ),
    [
        pytest.param(
            {
                "id": MOCKED_WORKSPACE_ID,
                "name": MOCKED_WORKSPACE_NAME,
                "description": MOCKED_WORKSPACE_DESCRIPTION,
                "requested_state": MOCKED_WORKSPACE_REQUESTED_STATE_SUBMITTED,
                "build_request_id": MOCKED_WORKSPACE_REQUEST_ID_BUILD_SUCCESS,
                "submit_request_id": MOCKED_WORKSPACE_REQUEST_ID_SUBMIT_SUCCESS,
            },
            {
                "result_warnings_qty": 0,
                "result_errors_qty": 0,
                "exception": does_not_raise(),
                "execution_failed": False,
            },
            id="SUBMIT_SUCCESS",
        ),
    ],
)
async def test_deploy_to_cv(
    caplog: pytest.LogCaptureFixture,
    cv_client: CVClient,
    mocked_cvdevices: list[CVDevice],
    workspace: dict[str, Any],
    expected: dict[str, Any],
    workspace_force_submission: bool,
) -> None:
    """
    Test building and submitting Workspace with single streaming device.

    Build request:
        WorkspaceConfigSetRequest(value=WorkspaceConfig(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'),
        request=Request.START_BUILD, request_params=RequestParams(request_id='req-914310f3-08dd-4239-bd42-6d78bf781229')))
    Recorded build response:
        tests/pyavd/cv/mocked_api_recordings/arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/
        1fdd6fcd02728621447eeb8a1d8c9cbfdd9201c9.json
    Submit request:
        WorkspaceConfigSetRequest(value=WorkspaceConfig(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'),
        request=Request.SUBMIT, request_params=RequestParams(request_id='req-b8f4e511-58de-4afe-99f0-b75abf980131')))
    Recorded submit responses:
        tests/pyavd/cv/mocked_api_recordings/arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/
        ba83e98eab07691e8b079958618ab2973822bfe8.json
    """
    with (
        caplog.at_level(INFO),
        expected["exception"],
        patch(
            "pyavd._cv.client.workspace.uuid4",
            side_effect=[workspace["build_request_id"]["id"].removeprefix("req-"), workspace["submit_request_id"]["id"].removeprefix("req-")],
        ),
        patch("pyavd._cv.workflows.deploy_to_cv.CVClient", return_value=cv_client),
        tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", delete=True) as temp_configlet_file,
    ):
        temp_configlet_file.write("alias test test")
        temp_configlet_file.flush()

        result = await deploy_to_cv(
            cloudvision=CloudVision(
                servers="",
                token="",
                username="",
                password="",
            ),
            workspace=CVWorkspace(
                name=workspace["name"],
                description=workspace["description"],
                id=workspace["id"],
                requested_state=workspace["requested_state"],
                force=workspace_force_submission,
            ),
            configs=[CVEosConfig(file=temp_configlet_file.name, device=next(iter(mocked_cvdevices)), configlet_name="TEST_CONFIGLET_NAME")],
        )

    # Assess result
    assert result.failed == expected["execution_failed"]

    # Assert number of returned warnings
    assert len(result.warnings) == expected["result_warnings_qty"]

    # Assert number of returned errors
    assert len(result.errors) == expected["result_errors_qty"]

    # Assert returned workspace object
    assert result.workspace.name == workspace["name"]
    assert result.workspace.description == workspace["description"]
    assert result.workspace.id == workspace["id"]
    assert result.workspace.requested_state == workspace["requested_state"]
    assert result.workspace.force == workspace_force_submission
    assert result.workspace.state == workspace["requested_state"]
