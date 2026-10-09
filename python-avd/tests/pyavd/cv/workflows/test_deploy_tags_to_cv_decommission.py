# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from pyavd._cv.workflows.deploy_tags_to_cv import deploy_tags_to_cv
from pyavd._cv.workflows.models import AvdDevice, CVDevice, CVDeviceTag, CVInterfaceTag, CVWorkspace

if TYPE_CHECKING:
    from unittest.mock import MagicMock

WORKSPACE = CVWorkspace()


def _deploy_device(hostname: str, serial: str) -> CVDevice:
    return CVDevice(avd_device=AvdDevice(hostname=hostname), serial_number=serial, exists_on_cv=True, action="deploy")


def _decommission_device(hostname: str, serial: str) -> CVDevice:
    return CVDevice(avd_device=AvdDevice(hostname=hostname), serial_number=serial, exists_on_cv=True, action="decommission")


def _missing_decommission_device(hostname: str, serial: str) -> CVDevice:
    return CVDevice(avd_device=AvdDevice(hostname=hostname), serial_number=serial, exists_on_cv=False, action="decommission")


# === Decommission device tags are added to skipped ===


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "tag",
    [
        pytest.param(CVDeviceTag("role", "leaf", _decommission_device("leaf1", "SN_DECOM")), id="DEVICE_TAG_EXISTING"),
        pytest.param(CVDeviceTag("role", "leaf", _missing_decommission_device("leaf1", "SN_DECOM")), id="DEVICE_TAG_MISSING"),
        pytest.param(CVInterfaceTag("link_type", "P2P", _decommission_device("leaf1", "SN_DECOM"), interface="Ethernet1"), id="INTERFACE_TAG_EXISTING"),
        pytest.param(CVInterfaceTag("link_type", "P2P", _missing_decommission_device("leaf1", "SN_DECOM"), interface="Ethernet1"), id="INTERFACE_TAG_MISSING"),
    ],
)
async def test_decommission_device_tags_added_to_skipped(mock_cv_client: MagicMock, tag: CVDeviceTag | CVInterfaceTag) -> None:
    """Test that tags for decommission devices are added to skipped_tags and not sent to CV."""
    skipped_tags: list = []
    strict = False

    await deploy_tags_to_cv([tag], WORKSPACE, strict, skipped_tags, [], [], mock_cv_client)

    assert skipped_tags == [tag]
    mock_cv_client.get_tags.assert_not_called()
    mock_cv_client.set_tags.assert_not_called()
    mock_cv_client.set_tag_assignments.assert_not_called()
    mock_cv_client.delete_tag_assignments.assert_not_called()


@pytest.mark.asyncio
async def test_decommission_tags_excluded_while_deploy_tags_processed(mock_cv_client: MagicMock) -> None:
    """Test that in a mixed list deploy device tags are processed normally while decommission device tags are added to skipped."""
    deploy_device = _deploy_device("leaf2", "SN_DEPLOY")
    decommission_device = _decommission_device("leaf1", "SN_DECOM")
    deploy_tag = CVDeviceTag("role", "leaf", deploy_device)
    decommission_tag = CVDeviceTag("role", "leaf", decommission_device)
    mock_cv_client.get_tags.return_value = []
    mock_cv_client.get_tag_assignments.return_value = []
    skipped_tags: list = []
    deployed_tags: list = []
    strict = False

    await deploy_tags_to_cv([deploy_tag, decommission_tag], WORKSPACE, strict, skipped_tags, deployed_tags, [], mock_cv_client)

    assert deployed_tags == [deploy_tag]
    assert skipped_tags == [decommission_tag]
