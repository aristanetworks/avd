# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from logging import INFO, getLogger
from os import environ
from typing import TYPE_CHECKING, Any
from unittest.mock import AsyncMock, MagicMock

import pytest

from pyavd._cv.client import CVClient
from pyavd._cv.client.models import CVTag, CVTagAssignment
from pyavd._cv.workflows.create_workspace_on_cv import create_workspace_on_cv
from pyavd._cv.workflows.deploy_tags_to_cv import deploy_tags_to_cv
from pyavd._cv.workflows.models import CVDevice, CVDeviceTag, CVInterfaceTag, CVWorkspace

from .helpers import get_tags_assignments_cv_state, get_tags_cv_state

if TYPE_CHECKING:
    from tests.pyavd.cv.mockery import CvEnvironment


LOGGER = getLogger(__name__)
WORKSPACE = CVWorkspace()


@pytest.fixture
def mock_cv_client() -> MagicMock:
    """Fixture to provide a mocked CVClient instance with AsyncMocks."""
    client = MagicMock()
    # Patch all required async methods with AsyncMock
    client.get_tags = AsyncMock()
    client.set_tags = AsyncMock()
    client.get_tag_assignments = AsyncMock()
    client.set_tag_assignments = AsyncMock()
    client.delete_tag_assignments = AsyncMock()
    return client


@pytest.fixture
def cv_tags_fixture() -> set[CVTag]:
    tags_qty = 20000
    return {CVTag(element_type="device", label=f"pytest-label-{tag_index}", value=f"pytest-value-{tag_index}") for tag_index in range(1, tags_qty + 1)}


@pytest.fixture
def cv_tag_assignments_fixture(cv_tags_fixture: set[CVTag]) -> set[CVTagAssignment]:
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
    ("strict", "expected_removed_tags", "delete_tag_assignments_call_count", "delete_tag_assignments_call_args"),
    [
        pytest.param(True, [], 0, {}, id="STRICT_TRUE"),
        pytest.param(False, [], 0, {}, id="STRICT_FALSE"),
    ],
)
async def test_deploy_tags_to_cv_new_device_tags(
    mock_cv_client: MagicMock,
    strict: bool,
    expected_removed_tags: list[CVDeviceTag | CVInterfaceTag],
    delete_tag_assignments_call_count: int,
    delete_tag_assignments_call_args: dict[str, Any],
) -> None:
    """Test creation and assignment of the new device tag+value pairs."""
    mock_cv_client.get_tags.return_value = get_tags_cv_state("device")
    mock_cv_client.get_tag_assignments.return_value = get_tags_assignments_cv_state("device")

    skipped_tags: list[CVDeviceTag | CVInterfaceTag] = []
    deployed_tags: list[CVDeviceTag | CVInterfaceTag] = []
    removed_tags: list[CVDeviceTag | CVInterfaceTag] = []

    designed_tags: list[CVDeviceTag | CVInterfaceTag] = [
        # New tag for non-existing device
        CVDeviceTag("K1", "V1", CVDevice("L0", "L0_serial", _exists_on_cv=False)),
        CVDeviceTag("device_tag_1", "device_tag_1_value_1", CVDevice("L1", "L1_serial", _exists_on_cv=True)),
        CVDeviceTag("mixed_tag_1", "mixed_tag_1_value_1", CVDevice("L1", "L1_serial", _exists_on_cv=True)),
    ]

    await deploy_tags_to_cv(designed_tags, WORKSPACE, strict, skipped_tags, deployed_tags, removed_tags, mock_cv_client)

    assert skipped_tags == [CVDeviceTag("K1", "V1", CVDevice("L0", "L0_serial", _exists_on_cv=False))]
    assert deployed_tags == [
        CVDeviceTag("device_tag_1", "device_tag_1_value_1", CVDevice("L1", "L1_serial", _exists_on_cv=True)),
        CVDeviceTag("mixed_tag_1", "mixed_tag_1_value_1", CVDevice("L1", "L1_serial", _exists_on_cv=True)),
    ]
    assert removed_tags == expected_removed_tags

    assert mock_cv_client.get_tags.call_count == 1
    get_tags_call_args: dict[str, Any] = {"workspace_id": WORKSPACE.id, "element_type": "device", "creator_type": "user"}
    for arg_key, arg_value in get_tags_call_args.items():
        assert mock_cv_client.get_tags.call_args[1][arg_key] == arg_value

    assert mock_cv_client.set_tags.call_count == 1
    set_tags_call_args: dict[str, Any] = {
        "workspace_id": WORKSPACE.id,
        "tags": {
            CVTag(element_type="device", label="device_tag_1", value="device_tag_1_value_1"),
            CVTag(element_type="device", label="mixed_tag_1", value="mixed_tag_1_value_1"),
        },
    }
    for arg_key, arg_value in set_tags_call_args.items():
        assert mock_cv_client.set_tags.call_args[1][arg_key] == arg_value

    assert mock_cv_client.get_tag_assignments.call_count == 1
    get_tag_assignments_call_args: dict[str, Any] = {"workspace_id": WORKSPACE.id, "element_type": "device", "creator_type": "user"}
    for arg_key, arg_value in get_tag_assignments_call_args.items():
        assert mock_cv_client.get_tag_assignments.call_args[1][arg_key] == arg_value

    assert mock_cv_client.set_tag_assignments.call_count == 1
    set_tag_assignments_call_args: dict[str, Any] = {
        "workspace_id": WORKSPACE.id,
        "tag_assignments": {
            CVTagAssignment(element_type="device", label="device_tag_1", value="device_tag_1_value_1", device_id="L1_serial", interface_id=None),
            CVTagAssignment(element_type="device", label="mixed_tag_1", value="mixed_tag_1_value_1", device_id="L1_serial", interface_id=None),
        },
    }
    for arg_key, arg_value in set_tag_assignments_call_args.items():
        assert mock_cv_client.set_tag_assignments.call_args[1][arg_key] == arg_value

    assert mock_cv_client.delete_tag_assignments.call_count == delete_tag_assignments_call_count
    for arg_key, arg_value in delete_tag_assignments_call_args.items():
        assert mock_cv_client.delete_tag_assignments.call_args[1][arg_key] == arg_value


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("strict", "expected_removed_tags", "delete_tag_assignments_call_count", "delete_tag_assignments_call_args"),
    [
        pytest.param(True, [], 0, {}, id="STRICT_TRUE"),
        pytest.param(False, [], 0, {}, id="STRICT_FALSE"),
    ],
)
async def test_deploy_tags_to_cv_unassigned_device_tags(
    mock_cv_client: MagicMock,
    strict: bool,
    expected_removed_tags: list[CVDeviceTag | CVInterfaceTag],
    delete_tag_assignments_call_count: int,
    delete_tag_assignments_call_args: dict[str, Any],
) -> None:
    """Test assignment of the existing device tag+value pairs."""
    mock_cv_client.get_tags.return_value = get_tags_cv_state("device")
    mock_cv_client.get_tag_assignments.return_value = get_tags_assignments_cv_state("device")

    skipped_tags: list[CVDeviceTag | CVInterfaceTag] = []
    deployed_tags: list[CVDeviceTag | CVInterfaceTag] = []
    removed_tags: list[CVDeviceTag | CVInterfaceTag] = []

    designed_tags: list[CVDeviceTag | CVInterfaceTag] = [
        CVDeviceTag("device_tag_1", "device_tag_1_value_2", CVDevice("L1", "L1_serial", _exists_on_cv=True)),
        CVDeviceTag("mixed_tag_1", "mixed_tag_1_value_2", CVDevice("L1", "L1_serial", _exists_on_cv=True)),
    ]

    await deploy_tags_to_cv(designed_tags, WORKSPACE, strict, skipped_tags, deployed_tags, removed_tags, mock_cv_client)

    assert not skipped_tags
    assert deployed_tags == [
        CVDeviceTag("device_tag_1", "device_tag_1_value_2", CVDevice("L1", "L1_serial", _exists_on_cv=True)),
        CVDeviceTag("mixed_tag_1", "mixed_tag_1_value_2", CVDevice("L1", "L1_serial", _exists_on_cv=True)),
    ]
    assert removed_tags == expected_removed_tags

    assert mock_cv_client.get_tags.call_count == 1
    get_tags_call_args: dict[str, Any] = {"workspace_id": WORKSPACE.id, "element_type": "device", "creator_type": "user"}
    for arg_key, arg_value in get_tags_call_args.items():
        assert mock_cv_client.get_tags.call_args[1][arg_key] == arg_value

    assert mock_cv_client.set_tags.call_count == 0

    assert mock_cv_client.get_tag_assignments.call_count == 1
    get_tag_assignments_call_args: dict[str, Any] = {"workspace_id": WORKSPACE.id, "element_type": "device", "creator_type": "user"}
    for arg_key, arg_value in get_tag_assignments_call_args.items():
        assert mock_cv_client.get_tag_assignments.call_args[1][arg_key] == arg_value

    assert mock_cv_client.set_tag_assignments.call_count == 1
    set_tag_assignments_call_args: dict[str, Any] = {
        "workspace_id": WORKSPACE.id,
        "tag_assignments": {
            CVTagAssignment(element_type="device", label="device_tag_1", value="device_tag_1_value_2", device_id="L1_serial", interface_id=None),
            CVTagAssignment(element_type="device", label="mixed_tag_1", value="mixed_tag_1_value_2", device_id="L1_serial", interface_id=None),
        },
    }
    for arg_key, arg_value in set_tag_assignments_call_args.items():
        assert mock_cv_client.set_tag_assignments.call_args[1][arg_key] == arg_value

    assert mock_cv_client.delete_tag_assignments.call_count == delete_tag_assignments_call_count
    for arg_key, arg_value in delete_tag_assignments_call_args.items():
        assert mock_cv_client.delete_tag_assignments.call_args[1][arg_key] == arg_value


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("strict", "expected_removed_tags", "delete_tag_assignments_call_count", "delete_tag_assignments_call_args"),
    [
        pytest.param(True, [], 0, {}, id="STRICT_TRUE"),
        pytest.param(False, [], 0, {}, id="STRICT_FALSE"),
    ],
)
async def test_deploy_tags_to_cv_assigned_device_tags(
    mock_cv_client: MagicMock,
    strict: bool,
    expected_removed_tags: list[CVDeviceTag | CVInterfaceTag],
    delete_tag_assignments_call_count: int,
    delete_tag_assignments_call_args: dict[str, Any],
) -> None:
    """Test attempt to assign already assigned device tag+value pairs."""
    mock_cv_client.get_tags.return_value = get_tags_cv_state("device")
    mock_cv_client.get_tag_assignments.return_value = get_tags_assignments_cv_state("device")

    skipped_tags: list[CVDeviceTag | CVInterfaceTag] = []
    deployed_tags: list[CVDeviceTag | CVInterfaceTag] = []
    removed_tags: list[CVDeviceTag | CVInterfaceTag] = []

    designed_tags: list[CVDeviceTag | CVInterfaceTag] = [
        CVDeviceTag("device_tag_1", "device_tag_1_value_2", CVDevice("L2", "L2_serial", _exists_on_cv=True)),
        CVDeviceTag("mixed_tag_1", "mixed_tag_1_value_2", CVDevice("L2", "L2_serial", _exists_on_cv=True)),
    ]

    await deploy_tags_to_cv(designed_tags, WORKSPACE, strict, skipped_tags, deployed_tags, removed_tags, mock_cv_client)

    assert not skipped_tags
    assert deployed_tags == [
        CVDeviceTag("device_tag_1", "device_tag_1_value_2", CVDevice("L2", "L2_serial", _exists_on_cv=True)),
        CVDeviceTag("mixed_tag_1", "mixed_tag_1_value_2", CVDevice("L2", "L2_serial", _exists_on_cv=True)),
    ]
    assert removed_tags == expected_removed_tags

    assert mock_cv_client.get_tags.call_count == 1
    get_tags_call_args: dict[str, Any] = {"workspace_id": WORKSPACE.id, "element_type": "device", "creator_type": "user"}
    for arg_key, arg_value in get_tags_call_args.items():
        assert mock_cv_client.get_tags.call_args[1][arg_key] == arg_value

    assert mock_cv_client.set_tags.call_count == 0

    assert mock_cv_client.get_tag_assignments.call_count == 1
    get_tag_assignments_call_args: dict[str, Any] = {"workspace_id": WORKSPACE.id, "element_type": "device", "creator_type": "user"}
    for arg_key, arg_value in get_tag_assignments_call_args.items():
        assert mock_cv_client.get_tag_assignments.call_args[1][arg_key] == arg_value

    assert mock_cv_client.set_tag_assignments.call_count == 0

    assert mock_cv_client.delete_tag_assignments.call_count == delete_tag_assignments_call_count
    for arg_key, arg_value in delete_tag_assignments_call_args.items():
        assert mock_cv_client.delete_tag_assignments.call_args[1][arg_key] == arg_value


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("strict", "expected_removed_tags", "delete_tag_assignments_call_count", "delete_tag_assignments_call_args"),
    [
        pytest.param(
            True,
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
    mock_cv_client.get_tags.return_value = get_tags_cv_state("device")
    mock_cv_client.get_tag_assignments.return_value = get_tags_assignments_cv_state("device")

    skipped_tags: list[CVDeviceTag | CVInterfaceTag] = []
    deployed_tags: list[CVDeviceTag | CVInterfaceTag] = []
    removed_tags: list[CVDeviceTag | CVInterfaceTag] = []

    designed_tags: list[CVDeviceTag | CVInterfaceTag] = [
        CVDeviceTag("device_tag_1", "device_tag_1_value_1", CVDevice("L3", "L3_serial", _exists_on_cv=True)),
        CVDeviceTag("device_tag_1", "device_tag_1_value_2", CVDevice("L3", "L3_serial", _exists_on_cv=True)),
        CVDeviceTag("mixed_tag_1", "mixed_tag_1_value_1", CVDevice("L3", "L3_serial", _exists_on_cv=True)),
    ]

    await deploy_tags_to_cv(designed_tags, WORKSPACE, strict, skipped_tags, deployed_tags, removed_tags, mock_cv_client)

    assert not skipped_tags
    assert deployed_tags == [
        CVDeviceTag("device_tag_1", "device_tag_1_value_1", CVDevice("L3", "L3_serial", _exists_on_cv=True)),
        CVDeviceTag("device_tag_1", "device_tag_1_value_2", CVDevice("L3", "L3_serial", _exists_on_cv=True)),
        CVDeviceTag("mixed_tag_1", "mixed_tag_1_value_1", CVDevice("L3", "L3_serial", _exists_on_cv=True)),
    ]
    assert removed_tags == expected_removed_tags

    assert mock_cv_client.get_tags.call_count == 1
    get_tags_call_args: dict[str, Any] = {"workspace_id": WORKSPACE.id, "element_type": "device", "creator_type": "user"}
    for arg_key, arg_value in get_tags_call_args.items():
        assert mock_cv_client.get_tags.call_args[1][arg_key] == arg_value

    assert mock_cv_client.set_tags.call_count == 1
    set_tags_call_args: dict[str, Any] = {
        "workspace_id": WORKSPACE.id,
        "tags": {
            CVTag(element_type="device", label="device_tag_1", value="device_tag_1_value_1"),
            CVTag(element_type="device", label="mixed_tag_1", value="mixed_tag_1_value_1"),
        },
    }
    for arg_key, arg_value in set_tags_call_args.items():
        assert mock_cv_client.set_tags.call_args[1][arg_key] == arg_value

    assert mock_cv_client.get_tag_assignments.call_count == 1
    get_tag_assignments_call_args: dict[str, Any] = {"workspace_id": WORKSPACE.id, "element_type": "device", "creator_type": "user"}
    for arg_key, arg_value in get_tag_assignments_call_args.items():
        assert mock_cv_client.get_tag_assignments.call_args[1][arg_key] == arg_value

    assert mock_cv_client.set_tag_assignments.call_count == 1
    set_tag_assignments_call_args: dict[str, Any] = {
        "workspace_id": WORKSPACE.id,
        "tag_assignments": {
            CVTagAssignment(element_type="device", label="device_tag_1", value="device_tag_1_value_1", device_id="L3_serial", interface_id=None),
            CVTagAssignment(element_type="device", label="mixed_tag_1", value="mixed_tag_1_value_1", device_id="L3_serial", interface_id=None),
        },
    }
    for arg_key, arg_value in set_tag_assignments_call_args.items():
        assert mock_cv_client.set_tag_assignments.call_args[1][arg_key] == arg_value

    assert mock_cv_client.delete_tag_assignments.call_count == delete_tag_assignments_call_count
    for arg_key, arg_value in delete_tag_assignments_call_args.items():
        assert mock_cv_client.delete_tag_assignments.call_args[1][arg_key] == arg_value


### interface tags ###
@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("strict", "expected_removed_tags", "delete_tag_assignments_call_count", "delete_tag_assignments_call_args"),
    [
        pytest.param(True, [], 0, {}, id="STRICT_TRUE"),
        pytest.param(False, [], 0, {}, id="STRICT_FALSE"),
    ],
)
async def test_deploy_tags_to_cv_new_interface_tags(
    mock_cv_client: MagicMock,
    strict: bool,
    expected_removed_tags: list[CVDeviceTag | CVInterfaceTag],
    delete_tag_assignments_call_count: int,
    delete_tag_assignments_call_args: dict[str, Any],
) -> None:
    """Test creation and assignment of the new interface tag+value pairs."""
    mock_cv_client.get_tags.return_value = get_tags_cv_state("interface")
    mock_cv_client.get_tag_assignments.return_value = get_tags_assignments_cv_state("interface")

    skipped_tags: list[CVDeviceTag | CVInterfaceTag] = []
    deployed_tags: list[CVDeviceTag | CVInterfaceTag] = []
    removed_tags: list[CVDeviceTag | CVInterfaceTag] = []

    designed_tags: list[CVDeviceTag | CVInterfaceTag] = [
        # New tag for non-existing device
        CVInterfaceTag("K1", "V1", CVDevice("L0", "L0_serial", _exists_on_cv=False), "Ethernet1"),
        CVInterfaceTag("interface_tag_1", "interface_tag_1_value_1", CVDevice("L1", "L1_serial", _exists_on_cv=True), "Ethernet1"),
        CVInterfaceTag("mixed_tag_1", "mixed_tag_1_value_1", CVDevice("L1", "L1_serial", _exists_on_cv=True), "Ethernet1"),
    ]

    await deploy_tags_to_cv(designed_tags, WORKSPACE, strict, skipped_tags, deployed_tags, removed_tags, mock_cv_client)

    assert skipped_tags == [CVInterfaceTag("K1", "V1", CVDevice("L0", "L0_serial", _exists_on_cv=False), "Ethernet1")]
    assert deployed_tags == [
        CVInterfaceTag("interface_tag_1", "interface_tag_1_value_1", CVDevice("L1", "L1_serial", _exists_on_cv=True), "Ethernet1"),
        CVInterfaceTag("mixed_tag_1", "mixed_tag_1_value_1", CVDevice("L1", "L1_serial", _exists_on_cv=True), "Ethernet1"),
    ]
    assert removed_tags == expected_removed_tags

    assert mock_cv_client.get_tags.call_count == 1
    get_tags_call_args: dict[str, Any] = {"workspace_id": WORKSPACE.id, "element_type": "interface", "creator_type": "user"}
    for arg_key, arg_value in get_tags_call_args.items():
        assert mock_cv_client.get_tags.call_args[1][arg_key] == arg_value

    assert mock_cv_client.set_tags.call_count == 1
    set_tags_call_args: dict[str, Any] = {
        "workspace_id": WORKSPACE.id,
        "tags": {
            CVTag(element_type="interface", label="interface_tag_1", value="interface_tag_1_value_1"),
            CVTag(element_type="interface", label="mixed_tag_1", value="mixed_tag_1_value_1"),
        },
    }
    for arg_key, arg_value in set_tags_call_args.items():
        assert mock_cv_client.set_tags.call_args[1][arg_key] == arg_value

    assert mock_cv_client.get_tag_assignments.call_count == 1
    get_tag_assignments_call_args: dict[str, Any] = {"workspace_id": WORKSPACE.id, "element_type": "interface", "creator_type": "user"}
    for arg_key, arg_value in get_tag_assignments_call_args.items():
        assert mock_cv_client.get_tag_assignments.call_args[1][arg_key] == arg_value

    assert mock_cv_client.set_tag_assignments.call_count == 1
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

    assert mock_cv_client.delete_tag_assignments.call_count == delete_tag_assignments_call_count
    for arg_key, arg_value in delete_tag_assignments_call_args.items():
        assert mock_cv_client.delete_tag_assignments.call_args[1][arg_key] == arg_value


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("strict", "expected_removed_tags", "delete_tag_assignments_call_count", "delete_tag_assignments_call_args"),
    [
        pytest.param(True, [], 0, {}, id="STRICT_TRUE"),
        pytest.param(False, [], 0, {}, id="STRICT_FALSE"),
    ],
)
async def test_deploy_tags_to_cv_unassigned_interface_tags(
    mock_cv_client: MagicMock,
    strict: bool,
    expected_removed_tags: list[CVDeviceTag | CVInterfaceTag],
    delete_tag_assignments_call_count: int,
    delete_tag_assignments_call_args: dict[str, Any],
) -> None:
    """Test assignment of the existing interface tag+value pairs."""
    mock_cv_client.get_tags.return_value = get_tags_cv_state("interface")
    mock_cv_client.get_tag_assignments.return_value = get_tags_assignments_cv_state("interface")

    skipped_tags: list[CVDeviceTag | CVInterfaceTag] = []
    deployed_tags: list[CVDeviceTag | CVInterfaceTag] = []
    removed_tags: list[CVDeviceTag | CVInterfaceTag] = []

    designed_tags: list[CVDeviceTag | CVInterfaceTag] = [
        CVInterfaceTag("interface_tag_1", "interface_tag_1_value_2", CVDevice("L1", "L1_serial", _exists_on_cv=True), "Ethernet1"),
        CVInterfaceTag("mixed_tag_1", "mixed_tag_1_value_2", CVDevice("L1", "L1_serial", _exists_on_cv=True), "Ethernet1"),
    ]

    await deploy_tags_to_cv(designed_tags, WORKSPACE, strict, skipped_tags, deployed_tags, removed_tags, mock_cv_client)

    assert not skipped_tags
    assert deployed_tags == [
        CVInterfaceTag("interface_tag_1", "interface_tag_1_value_2", CVDevice("L1", "L1_serial", _exists_on_cv=True), "Ethernet1"),
        CVInterfaceTag("mixed_tag_1", "mixed_tag_1_value_2", CVDevice("L1", "L1_serial", _exists_on_cv=True), "Ethernet1"),
    ]
    assert removed_tags == expected_removed_tags

    assert mock_cv_client.get_tags.call_count == 1
    get_tags_call_args: dict[str, Any] = {"workspace_id": WORKSPACE.id, "element_type": "interface", "creator_type": "user"}
    for arg_key, arg_value in get_tags_call_args.items():
        assert mock_cv_client.get_tags.call_args[1][arg_key] == arg_value

    assert mock_cv_client.set_tags.call_count == 0

    assert mock_cv_client.get_tag_assignments.call_count == 1
    get_tag_assignments_call_args: dict[str, Any] = {"workspace_id": WORKSPACE.id, "element_type": "interface", "creator_type": "user"}
    for arg_key, arg_value in get_tag_assignments_call_args.items():
        assert mock_cv_client.get_tag_assignments.call_args[1][arg_key] == arg_value

    assert mock_cv_client.set_tag_assignments.call_count == 1
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

    assert mock_cv_client.delete_tag_assignments.call_count == delete_tag_assignments_call_count
    for arg_key, arg_value in delete_tag_assignments_call_args.items():
        assert mock_cv_client.delete_tag_assignments.call_args[1][arg_key] == arg_value


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("strict", "expected_removed_tags", "delete_tag_assignments_call_count", "delete_tag_assignments_call_args"),
    [
        pytest.param(True, [], 0, {}, id="STRICT_TRUE"),
        pytest.param(False, [], 0, {}, id="STRICT_FALSE"),
    ],
)
async def test_deploy_tags_to_cv_assigned_interface_tags(
    mock_cv_client: MagicMock,
    strict: bool,
    expected_removed_tags: list[CVDeviceTag | CVInterfaceTag],
    delete_tag_assignments_call_count: int,
    delete_tag_assignments_call_args: dict[str, Any],
) -> None:
    """Test attempt to assign already assigned interface tag+value pairs."""
    mock_cv_client.get_tags.return_value = get_tags_cv_state("interface")
    mock_cv_client.get_tag_assignments.return_value = get_tags_assignments_cv_state("interface")

    skipped_tags: list[CVDeviceTag | CVInterfaceTag] = []
    deployed_tags: list[CVDeviceTag | CVInterfaceTag] = []
    removed_tags: list[CVDeviceTag | CVInterfaceTag] = []

    designed_tags: list[CVDeviceTag | CVInterfaceTag] = [
        CVInterfaceTag("interface_tag_1", "interface_tag_1_value_2", CVDevice("L2", "L2_serial", _exists_on_cv=True), "Ethernet1"),
        CVInterfaceTag("mixed_tag_1", "mixed_tag_1_value_2", CVDevice("L2", "L2_serial", _exists_on_cv=True), "Ethernet1"),
    ]

    await deploy_tags_to_cv(designed_tags, WORKSPACE, strict, skipped_tags, deployed_tags, removed_tags, mock_cv_client)

    assert not skipped_tags
    assert deployed_tags == [
        CVInterfaceTag("interface_tag_1", "interface_tag_1_value_2", CVDevice("L2", "L2_serial", _exists_on_cv=True), "Ethernet1"),
        CVInterfaceTag("mixed_tag_1", "mixed_tag_1_value_2", CVDevice("L2", "L2_serial", _exists_on_cv=True), "Ethernet1"),
    ]
    assert removed_tags == expected_removed_tags

    assert mock_cv_client.get_tags.call_count == 1
    get_tags_call_args: dict[str, Any] = {"workspace_id": WORKSPACE.id, "element_type": "interface", "creator_type": "user"}
    for arg_key, arg_value in get_tags_call_args.items():
        assert mock_cv_client.get_tags.call_args[1][arg_key] == arg_value

    assert mock_cv_client.set_tags.call_count == 0

    assert mock_cv_client.get_tag_assignments.call_count == 1
    get_tag_assignments_call_args: dict[str, Any] = {"workspace_id": WORKSPACE.id, "element_type": "interface", "creator_type": "user"}
    for arg_key, arg_value in get_tag_assignments_call_args.items():
        assert mock_cv_client.get_tag_assignments.call_args[1][arg_key] == arg_value

    assert mock_cv_client.set_tag_assignments.call_count == 0

    assert mock_cv_client.delete_tag_assignments.call_count == delete_tag_assignments_call_count
    for arg_key, arg_value in delete_tag_assignments_call_args.items():
        assert mock_cv_client.delete_tag_assignments.call_args[1][arg_key] == arg_value


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("strict", "expected_removed_tags", "delete_tag_assignments_call_count", "delete_tag_assignments_call_args"),
    [
        pytest.param(
            True,
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
    mock_cv_client.get_tags.return_value = get_tags_cv_state("interface")
    mock_cv_client.get_tag_assignments.return_value = get_tags_assignments_cv_state("interface")

    skipped_tags: list[CVDeviceTag | CVInterfaceTag] = []
    deployed_tags: list[CVDeviceTag | CVInterfaceTag] = []
    removed_tags: list[CVDeviceTag | CVInterfaceTag] = []

    designed_tags: list[CVDeviceTag | CVInterfaceTag] = [
        CVInterfaceTag("interface_tag_1", "interface_tag_1_value_1", CVDevice("L3", "L3_serial", _exists_on_cv=True), "Ethernet1"),
        CVInterfaceTag("interface_tag_1", "interface_tag_1_value_2", CVDevice("L3", "L3_serial", _exists_on_cv=True), "Ethernet1"),
        CVInterfaceTag("mixed_tag_1", "mixed_tag_1_value_1", CVDevice("L3", "L3_serial", _exists_on_cv=True), "Ethernet1"),
    ]

    await deploy_tags_to_cv(designed_tags, WORKSPACE, strict, skipped_tags, deployed_tags, removed_tags, mock_cv_client)

    assert not skipped_tags
    assert deployed_tags == [
        CVInterfaceTag("interface_tag_1", "interface_tag_1_value_1", CVDevice("L3", "L3_serial", _exists_on_cv=True), "Ethernet1"),
        CVInterfaceTag("interface_tag_1", "interface_tag_1_value_2", CVDevice("L3", "L3_serial", _exists_on_cv=True), "Ethernet1"),
        CVInterfaceTag("mixed_tag_1", "mixed_tag_1_value_1", CVDevice("L3", "L3_serial", _exists_on_cv=True), "Ethernet1"),
    ]
    assert removed_tags == expected_removed_tags

    assert mock_cv_client.get_tags.call_count == 1
    get_tags_call_args: dict[str, Any] = {"workspace_id": WORKSPACE.id, "element_type": "interface", "creator_type": "user"}
    for arg_key, arg_value in get_tags_call_args.items():
        assert mock_cv_client.get_tags.call_args[1][arg_key] == arg_value

    assert mock_cv_client.set_tags.call_count == 1
    set_tags_call_args: dict[str, Any] = {
        "workspace_id": WORKSPACE.id,
        "tags": {
            CVTag(element_type="interface", label="interface_tag_1", value="interface_tag_1_value_1"),
            CVTag(element_type="interface", label="mixed_tag_1", value="mixed_tag_1_value_1"),
        },
    }
    for arg_key, arg_value in set_tags_call_args.items():
        assert mock_cv_client.set_tags.call_args[1][arg_key] == arg_value

    assert mock_cv_client.get_tag_assignments.call_count == 1
    get_tag_assignments_call_args: dict[str, Any] = {"workspace_id": WORKSPACE.id, "element_type": "interface", "creator_type": "user"}
    for arg_key, arg_value in get_tag_assignments_call_args.items():
        assert mock_cv_client.get_tag_assignments.call_args[1][arg_key] == arg_value

    assert mock_cv_client.set_tag_assignments.call_count == 1
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

    assert mock_cv_client.delete_tag_assignments.call_count == delete_tag_assignments_call_count
    for arg_key, arg_value in delete_tag_assignments_call_args.items():
        assert mock_cv_client.delete_tag_assignments.call_args[1][arg_key] == arg_value


## Live TAGs tests ##
@pytest.mark.skipif(environ.get("CV_LIVE_TEST") is None, reason="CV_LIVE_TEST env variable is not set. Live cv_deploy tests are skipped.")
@pytest.mark.asyncio
@pytest.mark.filterwarnings("ignore:Unverified HTTPS request is being made to host")
async def test_deploy_tags_to_cv_message_splitting(
    caplog: pytest.LogCaptureFixture,
    cv_environment: CvEnvironment,
    cv_tags_fixture: set[CVTag],
    cv_tag_assignments_fixture: set[CVTagAssignment],
) -> None:
    """Test ability to gracefully push amount of Tags and Assignments which exceeds the message limit (1837788 vs. 1048576 max)."""
    with caplog.at_level(INFO):
        async with CVClient(
            servers=cv_environment.cv_server,
            token=cv_environment.cv_access_token,
            verify_certs=cv_environment.verify_certs,
        ) as cv_client:
            cv_tags = cv_tags_fixture
            cv_tag_assignments = cv_tag_assignments_fixture
            workspace = CVWorkspace(name="AVD_CI_PYTEST_TEST_DEPLOY_TAGS_TO_CV_MESSAGE_SPLITTING", requested_state="pending")
            try:
                # Create Workspace in pending state
                await create_workspace_on_cv(workspace=workspace, cv_client=cv_client)
                # Set tags
                await cv_client.set_tags(workspace_id=workspace.id, tags=cv_tags)
                # Confirm MAX message size
                assert "exceeded the max of 1048576 for" in next(iter(msg.message for msg in caplog.records if "Message size" in msg.message))
                # Clear logs before next async call
                caplog.clear()
                # Set tags assignments. Without building a Workspace it's OK that assignments reference non-existing device
                await cv_client.set_tag_assignments(workspace_id=workspace.id, tag_assignments=cv_tag_assignments)
                # Confirm MAX message size
                assert "exceeded the max of 1048576 for" in next(iter(msg.message for msg in caplog.records if "Message size" in msg.message))
            finally:
                try:
                    # Try to clean Workspace on all CVs to leave no traces
                    await cv_client.abandon_workspace(workspace_id=workspace.id)
                    await cv_client.delete_workspace(workspace_id=workspace.id)
                except Exception as e:
                    LOGGER.warning(
                        "The following exception faced while trying to abandon/clean Workspace %s on %s: %s", workspace.id, cv_environment.cv_server, e
                    )
