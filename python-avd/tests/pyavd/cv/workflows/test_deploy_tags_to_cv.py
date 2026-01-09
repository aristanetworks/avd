# Copyright (c) 2024-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from logging import getLogger
from typing import TYPE_CHECKING, Any

import pytest

from pyavd._cv.client.models import CVTag, CVTagAssignment
from pyavd._cv.workflows.deploy_tags_to_cv import deploy_tags_to_cv
from pyavd._cv.workflows.models import CVDevice, CVDeviceTag, CVInterfaceTag, CVWorkspace

from .helpers import get_device_tag_assignments_cv_state, get_device_tags_cv_state, get_interface_tag_assignments_cv_state, get_interface_tags_cv_state

if TYPE_CHECKING:
    from unittest.mock import MagicMock


LOGGER = getLogger(__name__)
WORKSPACE = CVWorkspace()


@pytest.fixture
def cv_tags_fixture() -> set[CVTag]:
    """Return 20K 'CVTag' objects to test message size limits of the CloudVision Tag-related APIs."""
    tags_qty = 20000
    return {CVTag(element_type="device", label=f"pytest-label-{tag_index}", value=f"pytest-value-{tag_index}") for tag_index in range(1, tags_qty + 1)}


@pytest.fixture
def cv_tag_assignments_fixture(cv_tags_fixture: set[CVTag]) -> set[CVTagAssignment]:
    """Return 20K 'CVTagAssignment' objects to test message size limits of the CloudVision Tag-related APIs."""
    device_id = "ABCDEFGHIGKLMNOP"
    return {CVTagAssignment(element_type=cv_tag.element_type, label=cv_tag.label, value=cv_tag.value, device_id=device_id) for cv_tag in cv_tags_fixture}


## Offline TAGs tests ##
@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("strict"),
    [
        pytest.param(True, id="STRICT_TRUE"),
        pytest.param(False, id="STRICT_FALSE"),
    ],
)
async def test_deploy_tags_to_cv_no_tags(
    mock_cv_client: MagicMock,
    strict: bool,
) -> None:
    """Test use case with empty TAGs list."""
    assert await deploy_tags_to_cv([], CVWorkspace(), strict, [], [], [], mock_cv_client) is None


@pytest.mark.asyncio
@pytest.mark.parametrize(("strict"), [pytest.param(True, id="STRICT_TRUE"), pytest.param(False, id="STRICT_FALSE")])
@pytest.mark.parametrize(
    ("tags"),
    [
        pytest.param([CVDeviceTag("K1", "V1", CVDevice("L1", _exists_on_cv=False))], id="ONE_DEVICE_TAG_ONE_DEVICE"),
        pytest.param(
            [CVDeviceTag("K1", "V1", CVDevice("L1", _exists_on_cv=False)), CVDeviceTag("K1", "V1", CVDevice("L2", _exists_on_cv=False))],
            id="ONE_DEVICE_TAG_MULTIPLE_DEVICES",
        ),
        pytest.param(
            [
                CVDeviceTag("K1", "V1", CVDevice("L1", _exists_on_cv=False)),
                CVDeviceTag("K1", "V1", CVDevice("L2", _exists_on_cv=False)),
                CVDeviceTag("K2", "V2", CVDevice("L1", _exists_on_cv=False)),
                CVDeviceTag("K2", "V2", CVDevice("L2", _exists_on_cv=False)),
            ],
            id="MULTIPLE_DEVICE_TAGS_MULTIPLE_DEVICES",
        ),
        pytest.param([CVInterfaceTag("K1", "V1", CVDevice("L1", _exists_on_cv=False), interface="Ethernet1")], id="ONE_INTERFACE_TAG_ONE_DEVICE"),
        pytest.param(
            [
                CVInterfaceTag("K1", "V1", CVDevice("L1", _exists_on_cv=False), interface="Ethernet1"),
                CVInterfaceTag("K1", "V1", CVDevice("L2", _exists_on_cv=False), interface="Ethernet1"),
            ],
            id="ONE_INTERFACE_TAG_MULTIPLE_DEVICES",
        ),
        pytest.param(
            [
                CVInterfaceTag("K1", "V1", CVDevice("L1", _exists_on_cv=False), interface="Ethernet1"),
                CVInterfaceTag("K1", "V1", CVDevice("L2", _exists_on_cv=False), interface="Ethernet1"),
                CVInterfaceTag("K2", "V2", CVDevice("L1", _exists_on_cv=False), interface="Ethernet1"),
                CVInterfaceTag("K2", "V2", CVDevice("L2", _exists_on_cv=False), interface="Ethernet1"),
            ],
            id="MULTIPLE_INTERFACE_TAGS_MULTIPLE_DEVICES",
        ),
    ],
)
async def test_deploy_tags_to_cv_no_existing_devices(mock_cv_client: MagicMock, strict: bool, tags: list[CVDeviceTag | CVInterfaceTag]) -> None:
    """Test use case with TAGs targeting non-existing devices."""
    assert await deploy_tags_to_cv(tags, CVWorkspace(), strict, [], [], [], mock_cv_client) is None


### device tags ###
@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("strict"),
    [
        pytest.param(True, id="STRICT_TRUE"),
        pytest.param(False, id="STRICT_FALSE"),
    ],
)
async def test_deploy_tags_to_cv_new_device_tags(
    mock_cv_client: MagicMock,
    strict: bool,
) -> None:
    """Test creation and assignment of the new device tag+value pairs."""
    # Mock state of the Tags and their assignments on the CloudVision side
    mock_cv_client.get_tags.return_value = get_device_tags_cv_state()
    mock_cv_client.get_tag_assignments.return_value = get_device_tag_assignments_cv_state()

    skipped_tags: list[CVDeviceTag | CVInterfaceTag] = []
    deployed_tags: list[CVDeviceTag | CVInterfaceTag] = []
    removed_tags: list[CVDeviceTag | CVInterfaceTag] = []

    designed_tags: list[CVDeviceTag | CVInterfaceTag] = [
        # New interface Tag for non-existing device
        CVDeviceTag("K1", "V1", CVDevice("L0", "L0_serial", _exists_on_cv=False)),
        # Assigning new device Tags to L1 (has no Tags assigned yet)
        CVDeviceTag("device_tag_1", "device_tag_1_value_1", CVDevice("L1", "L1_serial", _exists_on_cv=True)),
        CVDeviceTag("mixed_tag_1", "mixed_tag_1_value_1", CVDevice("L1", "L1_serial", _exists_on_cv=True)),
    ]

    await deploy_tags_to_cv(designed_tags, WORKSPACE, strict, skipped_tags, deployed_tags, removed_tags, mock_cv_client)

    # Assert that we skipped Tag assignment for non-existing device
    assert skipped_tags == [CVDeviceTag("K1", "V1", CVDevice("L0", "L0_serial", _exists_on_cv=False))]
    # Assert that all device Tags for L1 were deployed
    assert deployed_tags == [
        CVDeviceTag("device_tag_1", "device_tag_1_value_1", CVDevice("L1", "L1_serial", _exists_on_cv=True)),
        CVDeviceTag("mixed_tag_1", "mixed_tag_1_value_1", CVDevice("L1", "L1_serial", _exists_on_cv=True)),
    ]
    # Assert that deployment did not delete any other Tags from CloudVision
    assert not removed_tags

    # Assert that we only called `get_tags` once
    assert mock_cv_client.get_tags.call_count == 1
    # Assert that we called 'get_tags' to fetch 'device' Tags of a type 'user'
    get_tags_call_args: dict[str, Any] = {"workspace_id": WORKSPACE.id, "element_type": "device", "creator_type": "user"}
    for arg_key, arg_value in get_tags_call_args.items():
        assert mock_cv_client.get_tags.call_args[1][arg_key] == arg_value

    # Assert that we only called `set_tags` once
    assert mock_cv_client.set_tags.call_count == 1
    # Assert that we called 'set_tags' to only set Tags that we needed
    set_tags_call_args: dict[str, Any] = {
        "workspace_id": WORKSPACE.id,
        "tags": {
            CVTag(element_type="device", label="device_tag_1", value="device_tag_1_value_1"),
            CVTag(element_type="device", label="mixed_tag_1", value="mixed_tag_1_value_1"),
        },
    }
    for arg_key, arg_value in set_tags_call_args.items():
        assert mock_cv_client.set_tags.call_args[1][arg_key] == arg_value

    # Assert that we only called `get_tag_assignments` once
    assert mock_cv_client.get_tag_assignments.call_count == 1
    # Assert that we called 'get_tag_assignments' to fetch assignments for 'device' Tags of a type 'user'
    get_tag_assignments_call_args: dict[str, Any] = {"workspace_id": WORKSPACE.id, "element_type": "device", "creator_type": "user"}
    for arg_key, arg_value in get_tag_assignments_call_args.items():
        assert mock_cv_client.get_tag_assignments.call_args[1][arg_key] == arg_value

    # Assert that we only called `set_tag_assignments` once
    assert mock_cv_client.set_tag_assignments.call_count == 1
    # Assert that we called 'set_tag_assignments' to only set Tag assignments that we needed
    set_tag_assignments_call_args: dict[str, Any] = {
        "workspace_id": WORKSPACE.id,
        "tag_assignments": {
            CVTagAssignment(element_type="device", label="device_tag_1", value="device_tag_1_value_1", device_id="L1_serial", interface_id=None),
            CVTagAssignment(element_type="device", label="mixed_tag_1", value="mixed_tag_1_value_1", device_id="L1_serial", interface_id=None),
        },
    }
    for arg_key, arg_value in set_tag_assignments_call_args.items():
        assert mock_cv_client.set_tag_assignments.call_args[1][arg_key] == arg_value

    # Assert that no calls were made to delete Tag assignments
    mock_cv_client.delete_tag_assignments.assert_not_called()


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("strict"),
    [
        pytest.param(True, id="STRICT_TRUE"),
        pytest.param(False, id="STRICT_FALSE"),
    ],
)
async def test_deploy_tags_to_cv_unassigned_device_tags(
    mock_cv_client: MagicMock,
    strict: bool,
) -> None:
    """Test assignment of the existing device tag+value pairs."""
    # Mock state of the Tags and their assignments on the CloudVision side
    mock_cv_client.get_tags.return_value = get_device_tags_cv_state()
    mock_cv_client.get_tag_assignments.return_value = get_device_tag_assignments_cv_state()

    skipped_tags: list[CVDeviceTag | CVInterfaceTag] = []
    deployed_tags: list[CVDeviceTag | CVInterfaceTag] = []
    removed_tags: list[CVDeviceTag | CVInterfaceTag] = []

    # Try to assign Tags (label+value pair) already assigned to L2 to new device L1
    designed_tags: list[CVDeviceTag | CVInterfaceTag] = [
        CVDeviceTag("device_tag_1", "device_tag_1_value_2", CVDevice("L1", "L1_serial", _exists_on_cv=True)),
        CVDeviceTag("mixed_tag_1", "mixed_tag_1_value_2", CVDevice("L1", "L1_serial", _exists_on_cv=True)),
    ]

    await deploy_tags_to_cv(designed_tags, WORKSPACE, strict, skipped_tags, deployed_tags, removed_tags, mock_cv_client)

    # Assert that none of the Tags were skipped
    assert not skipped_tags
    # Assert that all device Tags for L1 were deployed
    assert deployed_tags == [
        CVDeviceTag("device_tag_1", "device_tag_1_value_2", CVDevice("L1", "L1_serial", _exists_on_cv=True)),
        CVDeviceTag("mixed_tag_1", "mixed_tag_1_value_2", CVDevice("L1", "L1_serial", _exists_on_cv=True)),
    ]
    # Assert that deployment did not delete any other Tags from CloudVision
    assert not removed_tags

    # Assert that we only called `get_tags` once
    assert mock_cv_client.get_tags.call_count == 1
    # Assert that we called 'get_tags' to fetch 'device' Tags of a type 'user'
    get_tags_call_args: dict[str, Any] = {"workspace_id": WORKSPACE.id, "element_type": "device", "creator_type": "user"}
    for arg_key, arg_value in get_tags_call_args.items():
        assert mock_cv_client.get_tags.call_args[1][arg_key] == arg_value

    # Assert that we did no call `set_tags` (as those Tags are already present and assigned to L2)
    assert mock_cv_client.set_tags.call_count == 0

    # Assert that we only called `get_tag_assignments` once
    assert mock_cv_client.get_tag_assignments.call_count == 1
    # Assert that we called 'get_tag_assignments' to fetch assignments for 'device' Tags of a type 'user'
    get_tag_assignments_call_args: dict[str, Any] = {"workspace_id": WORKSPACE.id, "element_type": "device", "creator_type": "user"}
    for arg_key, arg_value in get_tag_assignments_call_args.items():
        assert mock_cv_client.get_tag_assignments.call_args[1][arg_key] == arg_value

    # Assert that we only called `set_tag_assignments` once
    assert mock_cv_client.set_tag_assignments.call_count == 1
    # Assert that we called 'set_tag_assignments' to only set Tag assignments that we needed
    set_tag_assignments_call_args: dict[str, Any] = {
        "workspace_id": WORKSPACE.id,
        "tag_assignments": {
            CVTagAssignment(element_type="device", label="device_tag_1", value="device_tag_1_value_2", device_id="L1_serial", interface_id=None),
            CVTagAssignment(element_type="device", label="mixed_tag_1", value="mixed_tag_1_value_2", device_id="L1_serial", interface_id=None),
        },
    }
    for arg_key, arg_value in set_tag_assignments_call_args.items():
        assert mock_cv_client.set_tag_assignments.call_args[1][arg_key] == arg_value

    # Assert that no calls were made to delete Tag assignments
    mock_cv_client.delete_tag_assignments.assert_not_called()


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "strict",
    [
        pytest.param(True, id="STRICT_TRUE"),
        pytest.param(False, id="STRICT_FALSE"),
    ],
)
async def test_deploy_tags_to_cv_assigned_device_tags(
    mock_cv_client: MagicMock,
    strict: bool,
) -> None:
    """Test attempt to assign already assigned device tag+value pairs."""
    mock_cv_client.get_tags.return_value = get_device_tags_cv_state()
    mock_cv_client.get_tag_assignments.return_value = get_device_tag_assignments_cv_state()

    skipped_tags: list[CVDeviceTag | CVInterfaceTag] = []
    deployed_tags: list[CVDeviceTag | CVInterfaceTag] = []
    removed_tags: list[CVDeviceTag | CVInterfaceTag] = []

    # Try to assign Tags (label+value pair) that are already assigned to L2
    designed_tags: list[CVDeviceTag | CVInterfaceTag] = [
        CVDeviceTag("device_tag_1", "device_tag_1_value_2", CVDevice("L2", "L2_serial", _exists_on_cv=True)),
        CVDeviceTag("mixed_tag_1", "mixed_tag_1_value_2", CVDevice("L2", "L2_serial", _exists_on_cv=True)),
    ]

    await deploy_tags_to_cv(designed_tags, WORKSPACE, strict, skipped_tags, deployed_tags, removed_tags, mock_cv_client)

    # Assert that none of the Tags were skipped
    assert not skipped_tags
    # Assert that all device Tags for L2 were deployed
    assert deployed_tags == [
        CVDeviceTag("device_tag_1", "device_tag_1_value_2", CVDevice("L2", "L2_serial", _exists_on_cv=True)),
        CVDeviceTag("mixed_tag_1", "mixed_tag_1_value_2", CVDevice("L2", "L2_serial", _exists_on_cv=True)),
    ]
    # Assert that deployment did not delete any other Tags from CloudVision
    assert not removed_tags

    # Assert that we only called `get_tags` once
    assert mock_cv_client.get_tags.call_count == 1
    # Assert that we called 'get_tags' to fetch 'device' Tags of a type 'user'
    get_tags_call_args: dict[str, Any] = {"workspace_id": WORKSPACE.id, "element_type": "device", "creator_type": "user"}
    for arg_key, arg_value in get_tags_call_args.items():
        assert mock_cv_client.get_tags.call_args[1][arg_key] == arg_value

    # Assert that we have not called 'set_tags' (as all designed Tags are already assigned to target device)
    assert mock_cv_client.set_tags.call_count == 0

    # Assert that we only called `get_tag_assignments` once
    assert mock_cv_client.get_tag_assignments.call_count == 1
    # Assert that we called 'get_tag_assignments' to fetch assignment of 'device' Tags of a type 'user'
    get_tag_assignments_call_args: dict[str, Any] = {"workspace_id": WORKSPACE.id, "element_type": "device", "creator_type": "user"}
    for arg_key, arg_value in get_tag_assignments_call_args.items():
        assert mock_cv_client.get_tag_assignments.call_args[1][arg_key] == arg_value

    # Assert that we did no call `set_tags` (as those Tags are already present and assigned to L2)
    mock_cv_client.set_tag_assignments.assert_not_called()

    # Assert that no calls were made to delete Tag assignments
    mock_cv_client.delete_tag_assignments.assert_not_called()


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("strict", "expected_removed_tags", "delete_tag_assignments_call_count", "delete_tag_assignments_call_args"),
    [
        pytest.param(
            True,
            # We expect 'strict' mode to unassociate all other assigned user Tags of the same type from the targeted device
            [
                CVDeviceTag("device_tag_2", "device_tag_2_value_1", CVDevice("L3", "L3_serial", _exists_on_cv=True)),
                CVDeviceTag("mixed_tag_1", "mixed_tag_1_value_2", CVDevice("L3", "L3_serial", _exists_on_cv=True)),
                CVDeviceTag("mixed_tag_2", "mixed_tag_2_value_1", CVDevice("L3", "L3_serial", _exists_on_cv=True)),
            ],
            1,
            {
                "workspace_id": WORKSPACE.id,
                "tag_assignments": {
                    CVTagAssignment(element_type="device", label="device_tag_2", value="device_tag_2_value_1", device_id="L3_serial", interface_id=None),
                    CVTagAssignment(element_type="device", label="mixed_tag_1", value="mixed_tag_1_value_2", device_id="L3_serial", interface_id=None),
                    CVTagAssignment(element_type="device", label="mixed_tag_2", value="mixed_tag_2_value_1", device_id="L3_serial", interface_id=None),
                },
            },
            id="STRICT_TRUE",
        ),
        pytest.param(
            False,
            # We expect 'non-strict' mode to only unassociate user Tags (from targeted device) if they share the same label with Tags being assigned
            [CVDeviceTag("mixed_tag_1", "mixed_tag_1_value_2", CVDevice("L3", "L3_serial", _exists_on_cv=True))],
            1,
            {
                "workspace_id": WORKSPACE.id,
                "tag_assignments": {
                    CVTagAssignment(element_type="device", label="mixed_tag_1", value="mixed_tag_1_value_2", device_id="L3_serial", interface_id=None),
                },
            },
            id="STRICT_FALSE",
        ),
    ],
)
async def test_deploy_tags_to_cv_all_device_tags(
    mock_cv_client: MagicMock,
    strict: bool,
    expected_removed_tags: list[CVDeviceTag | CVInterfaceTag],
    delete_tag_assignments_call_count: int,
    delete_tag_assignments_call_args: dict[str, Any],
) -> None:
    """Generic test case covering all actions including removal of device tags and their assignments."""
    mock_cv_client.get_tags.return_value = get_device_tags_cv_state()
    mock_cv_client.get_tag_assignments.return_value = get_device_tag_assignments_cv_state()

    skipped_tags: list[CVDeviceTag | CVInterfaceTag] = []
    deployed_tags: list[CVDeviceTag | CVInterfaceTag] = []
    removed_tags: list[CVDeviceTag | CVInterfaceTag] = []

    designed_tags: list[CVDeviceTag | CVInterfaceTag] = [
        # New Tag assignment for L3
        CVDeviceTag("device_tag_1", "device_tag_1_value_1", CVDevice("L3", "L3_serial", _exists_on_cv=True)),
        # Already existing Tag assignment for L3
        CVDeviceTag("device_tag_1", "device_tag_1_value_2", CVDevice("L3", "L3_serial", _exists_on_cv=True)),
        # New Tag assignment for L3
        CVDeviceTag("mixed_tag_1", "mixed_tag_1_value_1", CVDevice("L3", "L3_serial", _exists_on_cv=True)),
    ]

    await deploy_tags_to_cv(designed_tags, WORKSPACE, strict, skipped_tags, deployed_tags, removed_tags, mock_cv_client)

    # Assert that none of the Tags were skipped
    assert not skipped_tags
    # Assert that all device Tags for L3 were deployed
    assert deployed_tags == [
        CVDeviceTag("device_tag_1", "device_tag_1_value_1", CVDevice("L3", "L3_serial", _exists_on_cv=True)),
        CVDeviceTag("device_tag_1", "device_tag_1_value_2", CVDevice("L3", "L3_serial", _exists_on_cv=True)),
        CVDeviceTag("mixed_tag_1", "mixed_tag_1_value_1", CVDevice("L3", "L3_serial", _exists_on_cv=True)),
    ]
    # Assert that in 'strict' mode we removed/unassociated all other Tags and in 'non-strict' mode we only removed Tags that share the same label with designed
    assert removed_tags == expected_removed_tags

    # Assert that we only called `get_tags` once
    assert mock_cv_client.get_tags.call_count == 1
    # Assert that we called 'get_tags' to fetch 'device' Tags of a type 'user'
    get_tags_call_args: dict[str, Any] = {"workspace_id": WORKSPACE.id, "element_type": "device", "creator_type": "user"}
    for arg_key, arg_value in get_tags_call_args.items():
        assert mock_cv_client.get_tags.call_args[1][arg_key] == arg_value

    # Assert that we only called `set_tags` once
    assert mock_cv_client.set_tags.call_count == 1
    # Assert that we called 'set_tags' to only set Tags that were missing on the targeted device
    set_tags_call_args: dict[str, Any] = {
        "workspace_id": WORKSPACE.id,
        "tags": {
            CVTag(element_type="device", label="device_tag_1", value="device_tag_1_value_1"),
            CVTag(element_type="device", label="mixed_tag_1", value="mixed_tag_1_value_1"),
        },
    }
    for arg_key, arg_value in set_tags_call_args.items():
        assert mock_cv_client.set_tags.call_args[1][arg_key] == arg_value

    # Assert that we only called `get_tag_assignments` once
    assert mock_cv_client.get_tag_assignments.call_count == 1
    # Assert that we called 'get_tag_assignments' to fetch assignments for 'device' Tags of a type 'user'
    get_tag_assignments_call_args: dict[str, Any] = {"workspace_id": WORKSPACE.id, "element_type": "device", "creator_type": "user"}
    for arg_key, arg_value in get_tag_assignments_call_args.items():
        assert mock_cv_client.get_tag_assignments.call_args[1][arg_key] == arg_value

    # Assert that we only called `set_tag_assignments` once
    assert mock_cv_client.set_tag_assignments.call_count == 1
    # Assert that we called 'set_tag_assignments' to only set Tag assignments that we needed
    set_tag_assignments_call_args: dict[str, Any] = {
        "workspace_id": WORKSPACE.id,
        "tag_assignments": {
            CVTagAssignment(element_type="device", label="device_tag_1", value="device_tag_1_value_1", device_id="L3_serial", interface_id=None),
            CVTagAssignment(element_type="device", label="mixed_tag_1", value="mixed_tag_1_value_1", device_id="L3_serial", interface_id=None),
        },
    }
    for arg_key, arg_value in set_tag_assignments_call_args.items():
        assert mock_cv_client.set_tag_assignments.call_args[1][arg_key] == arg_value

    # Assert that in 'strict' mode we unassign all other user Tags and in 'non-strict' mode we only unassign Tags sharing the same label with designed Tags
    assert mock_cv_client.delete_tag_assignments.call_count == delete_tag_assignments_call_count
    for arg_key, arg_value in delete_tag_assignments_call_args.items():
        assert mock_cv_client.delete_tag_assignments.call_args[1][arg_key] == arg_value


### interface tags ###
@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("strict"),
    [
        pytest.param(True, id="STRICT_TRUE"),
        pytest.param(False, id="STRICT_FALSE"),
    ],
)
async def test_deploy_tags_to_cv_new_interface_tags(
    mock_cv_client: MagicMock,
    strict: bool,
) -> None:
    """Test creation and assignment of the new interface tag+value pairs."""
    # Mock state of the Tags and their assignments on the CloudVision side
    mock_cv_client.get_tags.return_value = get_interface_tags_cv_state()
    mock_cv_client.get_tag_assignments.return_value = get_interface_tag_assignments_cv_state()

    skipped_tags: list[CVDeviceTag | CVInterfaceTag] = []
    deployed_tags: list[CVDeviceTag | CVInterfaceTag] = []
    removed_tags: list[CVDeviceTag | CVInterfaceTag] = []

    designed_tags: list[CVDeviceTag | CVInterfaceTag] = [
        # New interface Tag for non-existing device
        CVInterfaceTag("K1", "V1", CVDevice("L0", "L0_serial", _exists_on_cv=False), "Ethernet1"),
        # Assigning new interface Tags to L1 (has no Tags assigned yet)
        CVInterfaceTag("interface_tag_1", "interface_tag_1_value_1", CVDevice("L1", "L1_serial", _exists_on_cv=True), "Ethernet1"),
        CVInterfaceTag("mixed_tag_1", "mixed_tag_1_value_1", CVDevice("L1", "L1_serial", _exists_on_cv=True), "Ethernet1"),
    ]

    await deploy_tags_to_cv(designed_tags, WORKSPACE, strict, skipped_tags, deployed_tags, removed_tags, mock_cv_client)

    # Assert that we skipped Tag assignment for non-existing device
    assert skipped_tags == [CVInterfaceTag("K1", "V1", CVDevice("L0", "L0_serial", _exists_on_cv=False), "Ethernet1")]
    # Assert that all interface Tags for L1 were deployed
    assert deployed_tags == [
        CVInterfaceTag("interface_tag_1", "interface_tag_1_value_1", CVDevice("L1", "L1_serial", _exists_on_cv=True), "Ethernet1"),
        CVInterfaceTag("mixed_tag_1", "mixed_tag_1_value_1", CVDevice("L1", "L1_serial", _exists_on_cv=True), "Ethernet1"),
    ]
    # Assert that deployment did not delete any other Tags from CloudVision
    assert not removed_tags

    # Assert that we only called `get_tags` once
    assert mock_cv_client.get_tags.call_count == 1
    # Assert that we called 'get_tags' to fetch 'interface' Tags of a type 'user'
    get_tags_call_args: dict[str, Any] = {"workspace_id": WORKSPACE.id, "element_type": "interface", "creator_type": "user"}
    for arg_key, arg_value in get_tags_call_args.items():
        assert mock_cv_client.get_tags.call_args[1][arg_key] == arg_value

    # Assert that we only called `set_tags` once
    assert mock_cv_client.set_tags.call_count == 1
    # Assert that we called 'set_tags' to only set Tags that we needed
    set_tags_call_args: dict[str, Any] = {
        "workspace_id": WORKSPACE.id,
        "tags": {
            CVTag(element_type="interface", label="interface_tag_1", value="interface_tag_1_value_1"),
            CVTag(element_type="interface", label="mixed_tag_1", value="mixed_tag_1_value_1"),
        },
    }
    for arg_key, arg_value in set_tags_call_args.items():
        assert mock_cv_client.set_tags.call_args[1][arg_key] == arg_value

    # Assert that we only called `get_tag_assignments` once
    assert mock_cv_client.get_tag_assignments.call_count == 1
    # Assert that we called 'get_tag_assignments' to fetch assignments for 'interface' Tags of a type 'user'
    get_tag_assignments_call_args: dict[str, Any] = {"workspace_id": WORKSPACE.id, "element_type": "interface", "creator_type": "user"}
    for arg_key, arg_value in get_tag_assignments_call_args.items():
        assert mock_cv_client.get_tag_assignments.call_args[1][arg_key] == arg_value

    # Assert that we only called `set_tag_assignments` once
    assert mock_cv_client.set_tag_assignments.call_count == 1
    # Assert that we called 'set_tag_assignments' to only set Tag assignments that we needed
    set_tag_assignments_call_args: dict[str, Any] = {
        "workspace_id": WORKSPACE.id,
        "tag_assignments": {
            CVTagAssignment(
                element_type="interface", label="interface_tag_1", value="interface_tag_1_value_1", device_id="L1_serial", interface_id="Ethernet1"
            ),
            CVTagAssignment(element_type="interface", label="mixed_tag_1", value="mixed_tag_1_value_1", device_id="L1_serial", interface_id="Ethernet1"),
        },
    }
    for arg_key, arg_value in set_tag_assignments_call_args.items():
        assert mock_cv_client.set_tag_assignments.call_args[1][arg_key] == arg_value

    # Assert that no calls were made to delete Tag assignments
    mock_cv_client.delete_tag_assignments.assert_not_called()


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("strict"),
    [
        pytest.param(True, id="STRICT_TRUE"),
        pytest.param(False, id="STRICT_FALSE"),
    ],
)
async def test_deploy_tags_to_cv_unassigned_interface_tags(
    mock_cv_client: MagicMock,
    strict: bool,
) -> None:
    """Test assignment of the existing interface tag+value pairs."""
    # Mock state of the Tags and their assignments on the CloudVision side
    mock_cv_client.get_tags.return_value = get_interface_tags_cv_state()
    mock_cv_client.get_tag_assignments.return_value = get_interface_tag_assignments_cv_state()

    skipped_tags: list[CVDeviceTag | CVInterfaceTag] = []
    deployed_tags: list[CVDeviceTag | CVInterfaceTag] = []
    removed_tags: list[CVDeviceTag | CVInterfaceTag] = []

    # Try to assign Tags (label+value pair) already assigned to L2 to new device L1
    designed_tags: list[CVDeviceTag | CVInterfaceTag] = [
        CVInterfaceTag("interface_tag_1", "interface_tag_1_value_2", CVDevice("L1", "L1_serial", _exists_on_cv=True), "Ethernet1"),
        CVInterfaceTag("mixed_tag_1", "mixed_tag_1_value_2", CVDevice("L1", "L1_serial", _exists_on_cv=True), "Ethernet1"),
    ]

    await deploy_tags_to_cv(designed_tags, WORKSPACE, strict, skipped_tags, deployed_tags, removed_tags, mock_cv_client)

    # Assert that none of the Tags were skipped
    assert not skipped_tags
    # Assert that all interface Tags for L1 were deployed
    assert deployed_tags == [
        CVInterfaceTag("interface_tag_1", "interface_tag_1_value_2", CVDevice("L1", "L1_serial", _exists_on_cv=True), "Ethernet1"),
        CVInterfaceTag("mixed_tag_1", "mixed_tag_1_value_2", CVDevice("L1", "L1_serial", _exists_on_cv=True), "Ethernet1"),
    ]
    # Assert that deployment did not delete any other Tags from CloudVision
    assert not removed_tags

    # Assert that we only called `get_tags` once
    assert mock_cv_client.get_tags.call_count == 1
    # Assert that we called 'get_tags' to fetch 'interface' Tags of a type 'user'
    get_tags_call_args: dict[str, Any] = {"workspace_id": WORKSPACE.id, "element_type": "interface", "creator_type": "user"}
    for arg_key, arg_value in get_tags_call_args.items():
        assert mock_cv_client.get_tags.call_args[1][arg_key] == arg_value

    # Assert that we did no call `set_tags` (as those Tags are already present and assigned to L2)
    assert mock_cv_client.set_tags.call_count == 0

    # Assert that we only called `get_tag_assignments` once
    assert mock_cv_client.get_tag_assignments.call_count == 1
    # Assert that we called 'get_tag_assignments' to fetch assignments for 'interface' Tags of a type 'user'
    get_tag_assignments_call_args: dict[str, Any] = {"workspace_id": WORKSPACE.id, "element_type": "interface", "creator_type": "user"}
    for arg_key, arg_value in get_tag_assignments_call_args.items():
        assert mock_cv_client.get_tag_assignments.call_args[1][arg_key] == arg_value

    # Assert that we only called `set_tag_assignments` once
    assert mock_cv_client.set_tag_assignments.call_count == 1
    # Assert that we called 'set_tag_assignments' to only set Tag assignments that we needed
    set_tag_assignments_call_args: dict[str, Any] = {
        "workspace_id": WORKSPACE.id,
        "tag_assignments": {
            CVTagAssignment(
                element_type="interface", label="interface_tag_1", value="interface_tag_1_value_2", device_id="L1_serial", interface_id="Ethernet1"
            ),
            CVTagAssignment(element_type="interface", label="mixed_tag_1", value="mixed_tag_1_value_2", device_id="L1_serial", interface_id="Ethernet1"),
        },
    }
    for arg_key, arg_value in set_tag_assignments_call_args.items():
        assert mock_cv_client.set_tag_assignments.call_args[1][arg_key] == arg_value

    # Assert that no calls were made to delete Tag assignments
    mock_cv_client.delete_tag_assignments.assert_not_called()


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("strict"),
    [
        pytest.param(True, id="STRICT_TRUE"),
        pytest.param(False, id="STRICT_FALSE"),
    ],
)
async def test_deploy_tags_to_cv_assigned_interface_tags(
    mock_cv_client: MagicMock,
    strict: bool,
) -> None:
    """Test attempt to assign already assigned interface tag+value pairs."""
    mock_cv_client.get_tags.return_value = get_interface_tags_cv_state()
    mock_cv_client.get_tag_assignments.return_value = get_interface_tag_assignments_cv_state()

    skipped_tags: list[CVDeviceTag | CVInterfaceTag] = []
    deployed_tags: list[CVDeviceTag | CVInterfaceTag] = []
    removed_tags: list[CVDeviceTag | CVInterfaceTag] = []

    # Try to assign Tags (label+value pair) that are already assigned to L2
    designed_tags: list[CVDeviceTag | CVInterfaceTag] = [
        CVInterfaceTag("interface_tag_1", "interface_tag_1_value_2", CVDevice("L2", "L2_serial", _exists_on_cv=True), "Ethernet1"),
        CVInterfaceTag("mixed_tag_1", "mixed_tag_1_value_2", CVDevice("L2", "L2_serial", _exists_on_cv=True), "Ethernet1"),
    ]

    await deploy_tags_to_cv(designed_tags, WORKSPACE, strict, skipped_tags, deployed_tags, removed_tags, mock_cv_client)

    # Assert that none of the Tags were skipped
    assert not skipped_tags
    # Assert that all device Tags for L2 were deployed
    assert deployed_tags == [
        CVInterfaceTag("interface_tag_1", "interface_tag_1_value_2", CVDevice("L2", "L2_serial", _exists_on_cv=True), "Ethernet1"),
        CVInterfaceTag("mixed_tag_1", "mixed_tag_1_value_2", CVDevice("L2", "L2_serial", _exists_on_cv=True), "Ethernet1"),
    ]
    # Assert that deployment did not delete any other Tags from CloudVision
    assert not removed_tags

    # Assert that we only called `get_tags` once
    assert mock_cv_client.get_tags.call_count == 1
    # Assert that we called 'get_tags' to fetch 'interface' Tags of a type 'user'
    get_tags_call_args: dict[str, Any] = {"workspace_id": WORKSPACE.id, "element_type": "interface", "creator_type": "user"}
    for arg_key, arg_value in get_tags_call_args.items():
        assert mock_cv_client.get_tags.call_args[1][arg_key] == arg_value

    # Assert that we have not called 'set_tags' (as all designed Tags are already assigned to target device)
    assert mock_cv_client.set_tags.call_count == 0

    # Assert that we only called `get_tag_assignments` once
    assert mock_cv_client.get_tag_assignments.call_count == 1
    # Assert that we called 'get_tag_assignments' to fetch assignment of 'interface' Tags of a type 'user'
    get_tag_assignments_call_args: dict[str, Any] = {"workspace_id": WORKSPACE.id, "element_type": "interface", "creator_type": "user"}
    for arg_key, arg_value in get_tag_assignments_call_args.items():
        assert mock_cv_client.get_tag_assignments.call_args[1][arg_key] == arg_value

    # Assert that we did no call `set_tags` (as those Tags are already present and assigned to L2)
    mock_cv_client.set_tag_assignments.assert_not_called()

    # Assert that no calls were made to delete Tag assignments
    mock_cv_client.delete_tag_assignments.assert_not_called()


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("strict", "expected_removed_tags", "delete_tag_assignments_call_count", "delete_tag_assignments_call_args"),
    [
        pytest.param(
            True,
            # We expect 'strict' mode to unassociate all other assigned user Tags of the same type from the targeted device
            [
                CVInterfaceTag("interface_tag_2", "interface_tag_2_value_1", CVDevice("L3", "L3_serial", _exists_on_cv=True), "Ethernet1"),
                CVInterfaceTag("mixed_tag_1", "mixed_tag_1_value_2", CVDevice("L3", "L3_serial", _exists_on_cv=True), "Ethernet1"),
                CVInterfaceTag("mixed_tag_2", "mixed_tag_2_value_1", CVDevice("L3", "L3_serial", _exists_on_cv=True), "Ethernet1"),
            ],
            1,
            {
                "workspace_id": WORKSPACE.id,
                "tag_assignments": {
                    CVTagAssignment(
                        element_type="interface", label="interface_tag_2", value="interface_tag_2_value_1", device_id="L3_serial", interface_id="Ethernet1"
                    ),
                    CVTagAssignment(
                        element_type="interface", label="mixed_tag_1", value="mixed_tag_1_value_2", device_id="L3_serial", interface_id="Ethernet1"
                    ),
                    CVTagAssignment(
                        element_type="interface", label="mixed_tag_2", value="mixed_tag_2_value_1", device_id="L3_serial", interface_id="Ethernet1"
                    ),
                },
            },
            id="STRICT_TRUE",
        ),
        pytest.param(
            False,
            # We expect 'non-strict' mode to only unassociate user Tags (from targeted device) if they share the same label with Tags being assigned
            [CVInterfaceTag("mixed_tag_1", "mixed_tag_1_value_2", CVDevice("L3", "L3_serial", _exists_on_cv=True), "Ethernet1")],
            1,
            {
                "workspace_id": WORKSPACE.id,
                "tag_assignments": {
                    CVTagAssignment(
                        element_type="interface", label="mixed_tag_1", value="mixed_tag_1_value_2", device_id="L3_serial", interface_id="Ethernet1"
                    ),
                },
            },
            id="STRICT_FALSE",
        ),
    ],
)
async def test_deploy_tags_to_cv_all_interface_tags(
    mock_cv_client: MagicMock,
    strict: bool,
    expected_removed_tags: list[CVDeviceTag | CVInterfaceTag],
    delete_tag_assignments_call_count: int,
    delete_tag_assignments_call_args: dict[str, Any],
) -> None:
    """Generic test case covering all actions including removal of interface tags and their assignments."""
    mock_cv_client.get_tags.return_value = get_interface_tags_cv_state()
    mock_cv_client.get_tag_assignments.return_value = get_interface_tag_assignments_cv_state()

    skipped_tags: list[CVDeviceTag | CVInterfaceTag] = []
    deployed_tags: list[CVDeviceTag | CVInterfaceTag] = []
    removed_tags: list[CVDeviceTag | CVInterfaceTag] = []

    designed_tags: list[CVDeviceTag | CVInterfaceTag] = [
        # New Tag assignment for L3
        CVInterfaceTag("interface_tag_1", "interface_tag_1_value_1", CVDevice("L3", "L3_serial", _exists_on_cv=True), "Ethernet1"),
        # Already existing Tag assignment for L3
        CVInterfaceTag("interface_tag_1", "interface_tag_1_value_2", CVDevice("L3", "L3_serial", _exists_on_cv=True), "Ethernet1"),
        # New Tag assignment for L3
        CVInterfaceTag("mixed_tag_1", "mixed_tag_1_value_1", CVDevice("L3", "L3_serial", _exists_on_cv=True), "Ethernet1"),
    ]

    await deploy_tags_to_cv(designed_tags, WORKSPACE, strict, skipped_tags, deployed_tags, removed_tags, mock_cv_client)

    # Assert that none of the Tags were skipped
    assert not skipped_tags
    # Assert that all interface Tags for L3 were deployed
    assert deployed_tags == [
        CVInterfaceTag("interface_tag_1", "interface_tag_1_value_1", CVDevice("L3", "L3_serial", _exists_on_cv=True), "Ethernet1"),
        CVInterfaceTag("interface_tag_1", "interface_tag_1_value_2", CVDevice("L3", "L3_serial", _exists_on_cv=True), "Ethernet1"),
        CVInterfaceTag("mixed_tag_1", "mixed_tag_1_value_1", CVDevice("L3", "L3_serial", _exists_on_cv=True), "Ethernet1"),
    ]
    # Assert that in 'strict' mode we removed/unassociated all other Tags and in 'non-strict' mode we only removed Tags that share the same label with designed
    assert removed_tags == expected_removed_tags

    # Assert that we only called `get_tags` once
    assert mock_cv_client.get_tags.call_count == 1
    # Assert that we called 'get_tags' to fetch 'interface' Tags of a type 'user'
    get_tags_call_args: dict[str, Any] = {"workspace_id": WORKSPACE.id, "element_type": "interface", "creator_type": "user"}
    for arg_key, arg_value in get_tags_call_args.items():
        assert mock_cv_client.get_tags.call_args[1][arg_key] == arg_value

    # Assert that we only called `set_tags` once
    assert mock_cv_client.set_tags.call_count == 1
    # Assert that we called 'set_tags' to only set Tags that were missing on the targeted device
    set_tags_call_args: dict[str, Any] = {
        "workspace_id": WORKSPACE.id,
        "tags": {
            CVTag(element_type="interface", label="interface_tag_1", value="interface_tag_1_value_1"),
            CVTag(element_type="interface", label="mixed_tag_1", value="mixed_tag_1_value_1"),
        },
    }
    for arg_key, arg_value in set_tags_call_args.items():
        assert mock_cv_client.set_tags.call_args[1][arg_key] == arg_value

    # Assert that we only called `get_tag_assignments` once
    assert mock_cv_client.get_tag_assignments.call_count == 1
    # Assert that we called 'get_tag_assignments' to fetch assignments for 'interface' Tags of a type 'user'
    get_tag_assignments_call_args: dict[str, Any] = {"workspace_id": WORKSPACE.id, "element_type": "interface", "creator_type": "user"}
    for arg_key, arg_value in get_tag_assignments_call_args.items():
        assert mock_cv_client.get_tag_assignments.call_args[1][arg_key] == arg_value

    # Assert that we only called `set_tag_assignments` once
    assert mock_cv_client.set_tag_assignments.call_count == 1
    # Assert that we called 'set_tag_assignments' to only set Tag assignments that we needed
    set_tag_assignments_call_args: dict[str, Any] = {
        "workspace_id": WORKSPACE.id,
        "tag_assignments": {
            CVTagAssignment(
                element_type="interface", label="interface_tag_1", value="interface_tag_1_value_1", device_id="L3_serial", interface_id="Ethernet1"
            ),
            CVTagAssignment(element_type="interface", label="mixed_tag_1", value="mixed_tag_1_value_1", device_id="L3_serial", interface_id="Ethernet1"),
        },
    }
    for arg_key, arg_value in set_tag_assignments_call_args.items():
        assert mock_cv_client.set_tag_assignments.call_args[1][arg_key] == arg_value

    # Assert that in 'strict' mode we unassign all other user Tags and in 'non-strict' mode we only unassign Tags sharing the same label with designed Tags
    assert mock_cv_client.delete_tag_assignments.call_count == delete_tag_assignments_call_count
    for arg_key, arg_value in delete_tag_assignments_call_args.items():
        assert mock_cv_client.delete_tag_assignments.call_args[1][arg_key] == arg_value
