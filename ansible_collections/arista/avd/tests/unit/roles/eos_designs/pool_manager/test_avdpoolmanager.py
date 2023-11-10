# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from pathlib import Path
from unittest import mock

import pytest
from yaml import safe_dump

from ansible_collections.arista.avd.plugins.plugin_utils.eos_designs_shared_utils import SharedUtils
from ansible_collections.arista.avd.roles.eos_designs.python_modules.pool_manager import AvdPoolManager
from ansible_collections.arista.avd.roles.eos_designs.python_modules.pool_manager.avdpoolmanager import FILE_HEADER

DUMMYDIR = "mydir"
""" Files will be mocked throughout. This will be the fake directory under which the data folder holding the pool files will be created. """

TESTHOST1 = {"inventory_hostname": "testhost1", "fabric_name": "pool_manager_tests", "type": "l2leaf"}
TESTHOST2 = {"inventory_hostname": "testhost2", "fabric_name": "pool_manager_tests", "type": "l2leaf"}
TESTHOST3 = {"inventory_hostname": "testhost3", "fabric_name": "pool_manager_tests", "type": "l2leaf", "pod_name": "POD1"}
TESTHOST4 = {"inventory_hostname": "testhost4", "fabric_name": "pool_manager_tests", "type": "l2leaf", "pod_name": "POD1", "dc_name": "DC1"}


def get_assignment(hostvars: dict, id: int):
    return {"hostname": hostvars["inventory_hostname"], "id": id}


def get_pool(hostvars: dict, assignments: list[dict] = None):
    return {
        "fabric_name": hostvars.get("fabric_name"),
        "dc_name": hostvars.get("dc_name"),
        "pod_name": hostvars.get("pod_name"),
        "type": hostvars.get("type"),
        "id_assignments": assignments or [],
    }


def get_data(pools: list[dict] = None) -> dict:
    return {"id_pools": pools or []}


BASIC_DATA = get_data([get_pool(TESTHOST1, [get_assignment(TESTHOST1, 1)])])
""" Basic data set. Works for simple scenarios with one host. """


def get_file_content(data: dict) -> str:
    """Computed file content either to be used for mock_file_content or expected file content."""
    return f"{FILE_HEADER}{safe_dump(data)}"


TESTS = [
    # (
    #     id: str,                     # Short description used as pytest id
    #     hostvars_list: list[dict],   # We will ask for IDs for each host.
    #     expected_ids: list[int],     # Expected answer on get_id for each host.
    #     mock_file_data: str | None,  # Initial file data. None for missing file.
    #     expected_data: str,          # File data after saving to file.
    # )
    (
        # File exists but is empty. Request id for testhost1, get 1 back.
        # After saving the file contains BASIC_DATA.
        "empty_file_add_testhost1",
        [TESTHOST1],
        [1],
        "",
        BASIC_DATA,
    ),
    (
        # File does not exist. Request id for testhost1, get 1 back.
        # After saving the file contains BASIC_DATA.
        "no_file_add_testhost1",
        [TESTHOST1],
        [1],
        None,
        BASIC_DATA,
    ),
    (
        # File has BASIC_DATA. Request id for testhost1, get 1 back.
        # After saving the file contains BASIC_DATA.
        "keep_testhost1",
        [TESTHOST1],
        [1],
        BASIC_DATA,
        BASIC_DATA,
    ),
    (
        # File has BASIC_DATA. Request ids for testhost1 & 2, get 1 & 2 back.
        # After saving the file contains both IDs since both were active.
        "keep_testhost1_add_testhost2",
        [TESTHOST1, TESTHOST2],
        [1, 2],
        BASIC_DATA,
        get_data([get_pool(TESTHOST1, [get_assignment(TESTHOST1, 1), get_assignment(TESTHOST2, 2)])]),
    ),
    (
        # File has BASIC_DATA. Request ids for testhost2 & 1 (reversed order), get 2 & 1 back.
        # After saving the file contains both IDs since both were active.
        "add_testhost2_keep_testhost1",
        [TESTHOST2, TESTHOST1],
        [2, 1],
        BASIC_DATA,
        get_data([get_pool(TESTHOST1, [get_assignment(TESTHOST1, 1), get_assignment(TESTHOST2, 2)])]),
    ),
    (
        # File has BASIC_DATA. Request id for testhost2, get 2 back.
        # After saving the file contains only id 2 since id 1 was never requested, so it is deemed stale.
        "add_testhost2_remove_testhost1",
        [TESTHOST2],
        [2],
        BASIC_DATA,
        get_data([get_pool(TESTHOST2, [get_assignment(TESTHOST2, 2)])]),
    ),
    (
        # File has id2 only. Request id for testhost2 get 2 back.
        # After saving the file contains id 2.
        "keep_testhost2",
        [TESTHOST2],
        [2],
        get_data([get_pool(TESTHOST2, [get_assignment(TESTHOST2, 2)])]),
        get_data([get_pool(TESTHOST2, [get_assignment(TESTHOST2, 2)])]),
    ),
    (
        # File has id2 only. Request id for testhost1 & 2, get 1 & 2 back.
        # After saving the file contains id 1 and 2.
        "add_testhost1_remove_testhost2",
        [TESTHOST1, TESTHOST2],
        [1, 2],
        get_data([get_pool(TESTHOST2, [get_assignment(TESTHOST2, 2)])]),
        get_data([get_pool(TESTHOST1, [get_assignment(TESTHOST1, 1), get_assignment(TESTHOST2, 2)])]),
    ),
    (
        # File has BASIC_DATA. Request id for testhost3 get 1 back.
        # After saving the file contains a new pool with id 1 for testhost3 since id 1 was never requested, so it is deemed stale.
        "add_pool_with_testhost2_remove_pool_with_testhost1",
        [TESTHOST3],
        [1],
        BASIC_DATA,
        get_data([get_pool(TESTHOST3, [get_assignment(TESTHOST3, 1)])]),
    ),
    (
        # File has pool for testhost3 with id 1. Request id for testhost1 & 3, get 1 & 1 back.
        # After saving the file contains two pools with id 1 in each.
        "add_pool_with_testhost1_keep_pool_with_testhost3",
        [TESTHOST1, TESTHOST3],
        [1, 1],
        get_data([get_pool(TESTHOST3, [get_assignment(TESTHOST3, 1)])]),
        get_data([get_pool(TESTHOST1, [get_assignment(TESTHOST1, 1)]), get_pool(TESTHOST3, [get_assignment(TESTHOST3, 1)])]),
    ),
    (
        # No file. Request id for testhost4-1 (reversed) and get 1,1,1,2 back.
        # After saving the file contains three pools. First one with 1-2 and 1 in the other two.
        # Notice input is reversed but output is sorted on pool keys (DC1 before None).
        # Also notice testhost2 has id 1 and testhost1 has id 2
        "no_file_add_three_pools_and_four_hosts",
        [TESTHOST4, TESTHOST3, TESTHOST2, TESTHOST1],
        [1, 1, 1, 2],
        None,
        get_data(
            [
                get_pool(TESTHOST4, [get_assignment(TESTHOST4, 1)]),
                get_pool(TESTHOST1, [get_assignment(TESTHOST2, 1), get_assignment(TESTHOST1, 2)]),
                get_pool(TESTHOST3, [get_assignment(TESTHOST3, 1)]),
            ]
        ),
    ),
]


def get_id(value) -> str:
    return value if isinstance(value, str) else ""


@pytest.mark.parametrize(("id", "hostvars_list", "expected_ids", "mock_file_data", "expected_data"), TESTS, ids=get_id)
def test_avdpoolmanager_pool(id: str, hostvars_list: list[dict], expected_ids: list[int], mock_file_data: str, expected_data: dict):
    file_exists = mock_file_data is not None
    expected_write = mock_file_data != expected_data
    with (
        mock.patch.object(Path, "exists", mock.Mock(return_value=file_exists)) as mocked_exists,
        mock.patch.object(Path, "open", mock.mock_open(read_data=get_file_content(mock_file_data))) as mocked_open,
        mock.patch.object(Path, "parent", mock.PropertyMock(mkdir=mock.MagicMock())) as mocked_parent,
        mock.patch.object(Path, "touch", mock.Mock()) as mocked_touch,
    ):
        mocked_open: mock.MagicMock
        mocked_file_write: mock.MagicMock = mocked_open.return_value.write

        # Initialize pool_manager and feed to shared_utils.
        pool_manager = AvdPoolManager(DUMMYDIR)

        for index, hostvars in enumerate(hostvars_list):
            shared_utils = SharedUtils(hostvars, object())
            # Get the id of the host from hostvars. If not, a new data set will be created.
            assert pool_manager.get_id(shared_utils) == expected_ids[index]

        mocked_exists.assert_called_once()
        if not file_exists:
            # If the mocked file does not exists check that it was created together with the parent dir.
            mocked_mkdir: mock.MagicMock = mocked_parent.return_value.mkdir
            mocked_mkdir.assert_called_once_with(exist_ok=True, mode=509, parents=True)
            mocked_touch.assert_called_once()

        mocked_open.assert_called_once_with(mode="r", encoding="UTF-8", errors=None)

        assert pool_manager.save_updated_pools() is None

        if expected_write:
            mocked_open.assert_called_with(mode="w", encoding="UTF-8", errors=None)
            mocked_file_write.assert_called_once_with(get_file_content(expected_data))
        else:
            mocked_open.assert_called_with(mode="r", encoding="UTF-8", errors=None)
            mocked_file_write.assert_not_called()
