# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from contextlib import nullcontext as does_not_raise
from logging import getLogger
from os import environ

import pytest

from pyavd._cv.client import CVClient
from pyavd._cv.client.models import CVTag, CVTagAssignment
from pyavd._cv.workflows.create_workspace_on_cv import create_workspace_on_cv
from pyavd._cv.workflows.models import CVWorkspace

LOGGER = getLogger(__name__)


@pytest.fixture
def cv_tags_fixture() -> set[CVTag]:
    tags_qty = 20000
    return {CVTag(element_type="device", label=f"pytest-label-{tag_index}", value=f"pytest-value-{tag_index}") for tag_index in range(1, tags_qty + 1)}


@pytest.fixture
def cv_tag_assignments_fixture(cv_tags_fixture: set[CVTag]) -> set[CVTagAssignment]:
    device_id = "ABCDEFGHIGKLMNOP"
    return {CVTagAssignment(element_type=cv_tag.element_type, label=cv_tag.label, value=cv_tag.value, device_id=device_id) for cv_tag in cv_tags_fixture}


@pytest.mark.skipif(environ.get("CV_LIVE_TEST") is None, reason="CV_LIVE_TEST env variable is not set. Live cv_deploy tests are skipped.")
@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("targeted_cv", "verify_certs"),
    [
        pytest.param(
            {
                "cv_access_token": environ.get("CV_PRD_ACCESS_TOKEN", default=""),
                "cv_server": environ.get("CV_PRD_SERVER", default=""),
            },
            True,
            id="CVAAS_PRD",
        ),
        pytest.param(
            {
                "cv_access_token": environ.get("CV_STG_ACCESS_TOKEN", default=""),
                "cv_server": environ.get("CV_STG_SERVER", default=""),
            },
            True,
            id="CVAAS_STG",
        ),
        pytest.param(
            {
                "cv_access_token": environ.get("CV_ONPREM_ACCESS_TOKEN", default=""),
                "cv_server": environ.get("CV_ONPREM_SERVER", default=""),
            },
            False,
            id="CV_ONPREM",
        ),
    ],
)
@pytest.mark.filterwarnings("ignore:Unverified HTTPS request is being made to host")
async def test_deploy_tags_to_cv_message_splitting(
    targeted_cv: dict[str, str],
    verify_certs: bool,
    cv_tags_fixture: set[CVTag],
    cv_tag_assignments_fixture: set[CVTagAssignment],
) -> None:
    """Test ability to gracefully push amount of Tags and Assignments which exceeds the message limit (1837788 vs. 1048576 max)."""
    with does_not_raise():
        async with CVClient(
            servers=targeted_cv["cv_server"],
            token=targeted_cv["cv_access_token"],
            verify_certs=verify_certs,
        ) as cv_client:
            cv_tags = cv_tags_fixture
            cv_tag_assignments = cv_tag_assignments_fixture
            workspace = CVWorkspace(name="AVD_CI_PYTEST_TEST_DEPLOY_TAGS_TO_CV_MESSAGE_SPLITTING", requested_state="pending")
            try:
                # Create Workspace in pending state
                await create_workspace_on_cv(workspace=workspace, cv_client=cv_client)
                # Set tags
                await cv_client.set_tags(workspace_id=workspace.id, tags=cv_tags)
                # Set tags assignments. Without building a Workspace it's OK that assignments reference non-existing device
                await cv_client.set_tag_assignments(workspace_id=workspace.id, tag_assignments=cv_tag_assignments)
            finally:
                try:
                    # Try to clean Workspace on all CVs to leave no traces
                    await cv_client.abandon_workspace(workspace_id=workspace.id)
                    await cv_client.delete_workspace(workspace_id=workspace.id)
                except Exception as e:
                    LOGGER.warning(
                        "The following exception faced while trying to abandon/clean Workspace %s on %s: %s", workspace.id, targeted_cv["cv_server"], e
                    )
