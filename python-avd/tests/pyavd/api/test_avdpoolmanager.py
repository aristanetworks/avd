# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any
from unittest import mock

import pytest
from yaml import safe_dump

from pyavd._eos_designs.schema import EosDesigns
from pyavd._eos_designs.shared_utils import SharedUtils
from pyavd._schema.store import create_store
from pyavd.api.pool_manager import PoolManager
from pyavd.api.pool_manager.base_classes import FILE_HEADER, Pool

# Load schema from pickled file into lru_cache before we start mocking the file open.
create_store(load_from_yaml=False)

DUMMYDIR = "mydir"
""" Files will be mocked throughout. This will be the fake directory under which the data folder holding the pool files will be created. """

TESTHOST1 = {"inventory_hostname": "testhost1", "fabric_name": "pool_manager_tests", "type": "l2leaf", "l2leaf": {"defaults": {}}}
TESTHOST2 = {"inventory_hostname": "testhost2", "fabric_name": "pool_manager_tests", "type": "l2leaf", "l2leaf": {"defaults": {}}}
TESTHOST3 = {"inventory_hostname": "testhost3", "fabric_name": "pool_manager_tests", "type": "l2leaf", "pod_name": "POD1", "l2leaf": {"defaults": {}}}
TESTHOST4 = {
    "inventory_hostname": "testhost4",
    "fabric_name": "pool_manager_tests",
    "type": "l2leaf",
    "pod_name": "POD1",
    "dc_name": "DC1",
    "l2leaf": {"defaults": {}},
}


def get_assignment(hostvars: dict, node_id: int) -> dict[str, int]:
    return {f"hostname={hostvars['inventory_hostname']}": node_id}


def get_pool(hostvars: dict, assignments: list[dict[str, int]] | None = None) -> dict[str, dict[str, int]]:
    pool_key = f"fabric_name={hostvars['fabric_name']}"
    if "dc_name" in hostvars:
        pool_key += f"/dc_name={hostvars['dc_name']}"
    if "pod_name" in hostvars:
        pool_key += f"/pod_name={hostvars['pod_name']}"
    pool_key += f"/type={hostvars['type']}"
    return {
        pool_key: {key: value for assignment in assignments or [] for key, value in assignment.items()},
    }


def get_data(pools: list[dict[str, dict[str, int]]] | None = None) -> dict[str, dict[str, dict[str, int]]]:
    return {"node_id_pools": {key: value for pool in pools or {} for key, value in pool.items()}}


BASIC_DATA = get_data([get_pool(TESTHOST1, [get_assignment(TESTHOST1, 1)])])
""" Basic data set. Works for simple scenarios with one host. """


def get_file_content(data: dict) -> str:
    """Computed file content either to be used for mock_file_content or expected file content."""
    return f"{FILE_HEADER}{safe_dump(data, sort_keys=False)}"


@pytest.mark.parametrize(
    ("hostvars_list", "expected_ids", "mock_file_data", "expected_data", "requested_ids"),
    [
        pytest.param(
            # File exists but is empty. Request id for testhost1, get 1 back.
            # After saving the file contains BASIC_DATA.
            [TESTHOST1],
            [1],
            "",
            BASIC_DATA,
            None,  # requested_ids
            id="empty_file_add_testhost1",
        ),
        pytest.param(
            # File does not exist. Request id for testhost1, get 1 back.
            # After saving the file contains BASIC_DATA.
            [TESTHOST1],
            [1],
            None,
            BASIC_DATA,
            None,  # requested_ids
            id="no_file_add_testhost1",
        ),
        pytest.param(
            # File has BASIC_DATA. Request id for testhost1, get 1 back.
            # After saving the file contains BASIC_DATA.
            [TESTHOST1],
            [1],
            BASIC_DATA,
            BASIC_DATA,
            None,  # requested_ids
            id="keep_testhost1",
        ),
        pytest.param(
            # File has BASIC_DATA. Request ids for testhost1 & 2, get 1 & 2 back.
            # After saving the file contains both IDs since both were active.
            [TESTHOST1, TESTHOST2],
            [1, 2],
            BASIC_DATA,
            get_data([get_pool(TESTHOST1, [get_assignment(TESTHOST1, 1), get_assignment(TESTHOST2, 2)])]),
            None,  # requested_ids
            id="keep_testhost1_add_testhost2",
        ),
        pytest.param(
            # File has BASIC_DATA. Request ids for testhost2 & 1 (reversed order), get 2 & 1 back.
            # After saving the file contains both IDs since both were active.
            [TESTHOST2, TESTHOST1],
            [2, 1],
            BASIC_DATA,
            get_data([get_pool(TESTHOST1, [get_assignment(TESTHOST1, 1), get_assignment(TESTHOST2, 2)])]),
            None,  # requested_ids
            id="add_testhost2_keep_testhost1",
        ),
        pytest.param(
            # File has BASIC_DATA. Request id for testhost2, get 2 back.
            # After saving the file contains only id 2 since id 1 was never requested, so it is deemed stale.
            [TESTHOST2],
            [2],
            BASIC_DATA,
            get_data([get_pool(TESTHOST2, [get_assignment(TESTHOST2, 2)])]),
            None,  # requested_ids
            id="add_testhost2_remove_testhost1",
        ),
        pytest.param(
            # File has id2 only. Request id for testhost2 get 2 back.
            # After saving the file contains id 2.
            [TESTHOST2],
            [2],
            get_data([get_pool(TESTHOST2, [get_assignment(TESTHOST2, 2)])]),
            get_data([get_pool(TESTHOST2, [get_assignment(TESTHOST2, 2)])]),
            None,  # requested_ids
            id="keep_testhost2",
        ),
        pytest.param(
            # File has id2 only. Request id for testhost1 & 2, get 1 & 2 back.
            # After saving the file contains id 1 and 2.
            [TESTHOST1, TESTHOST2],
            [1, 2],
            get_data([get_pool(TESTHOST2, [get_assignment(TESTHOST2, 2)])]),
            get_data([get_pool(TESTHOST1, [get_assignment(TESTHOST1, 1), get_assignment(TESTHOST2, 2)])]),
            None,  # requested_ids
            id="add_testhost1_remove_testhost2",
        ),
        pytest.param(
            # File has BASIC_DATA. Request id for testhost3 get 1 back.
            # After saving the file contains a new pool with id 1 for testhost3 since id 1 was never requested, so it is deemed stale.
            [TESTHOST3],
            [1],
            BASIC_DATA,
            get_data([get_pool(TESTHOST3, [get_assignment(TESTHOST3, 1)])]),
            None,  # requested_ids
            id="add_pool_with_testhost2_remove_pool_with_testhost1",
        ),
        pytest.param(
            # File has pool for testhost3 with id 1. Request id for testhost1 & 3, get 1 & 1 back.
            # After saving the file contains two pools with id 1 in each.
            [TESTHOST1, TESTHOST3],
            [1, 1],
            get_data([get_pool(TESTHOST3, [get_assignment(TESTHOST3, 1)])]),
            get_data([get_pool(TESTHOST3, [get_assignment(TESTHOST3, 1)]), get_pool(TESTHOST1, [get_assignment(TESTHOST1, 1)])]),
            None,  # requested_ids
            id="add_pool_with_testhost1_keep_pool_with_testhost3",
        ),
        pytest.param(
            # No file. Request id for testhost4-1 (reversed) and get 1,1,1,2 back.
            # After saving the file contains three pools. First one with 1-2 and 1 in the other two.
            # Notice input is reversed but output is sorted on pool keys (DC1 before None).
            # Also notice testhost2 has id 1 and testhost1 has id 2
            [TESTHOST4, TESTHOST3, TESTHOST2, TESTHOST1],
            [1, 1, 1, 2],
            None,
            get_data(
                [
                    get_pool(TESTHOST4, [get_assignment(TESTHOST4, 1)]),
                    get_pool(TESTHOST3, [get_assignment(TESTHOST3, 1)]),
                    get_pool(TESTHOST1, [get_assignment(TESTHOST2, 1), get_assignment(TESTHOST1, 2)]),
                ]
            ),
            None,  # requested_ids
            id="no_file_add_three_pools_and_four_hosts",
        ),
        pytest.param(
            # File has BASIC_DATA where testhost has id 1. Request the specific id 1 for testhost1, get 1 back.
            # After saving the file contains BASIC_DATA.
            [TESTHOST1],
            [1],
            BASIC_DATA,
            BASIC_DATA,
            [1],  # requested_ids
            id="keep_testhost1",
        ),
        pytest.param(
            # File has BASIC_DATA where testhost has id 1. Request the specific id 66 for testhost1, get 66 back.
            # After saving the file contains testhost1 with id 66.
            [TESTHOST1],
            [66],
            BASIC_DATA,
            get_data([get_pool(TESTHOST1, [get_assignment(TESTHOST1, 66)])]),
            [66],  # requested_ids
            id="keep_testhost1",
        ),
        pytest.param(
            # File has BASIC_DATA where testhost has id 1. Request the specific id 1 for testhost2, get 2 back.
            # After saving the file contains testhost1 with id 1 and testhost2 with 2.
            [TESTHOST1, TESTHOST2],
            [1, 2],
            BASIC_DATA,
            get_data([get_pool(TESTHOST1, [get_assignment(TESTHOST1, 1), get_assignment(TESTHOST2, 2)])]),
            [None, 1],  # requested_ids
            id="keep_testhost1",
        ),
    ],
)
def test_avdpoolmanager_pool(
    hostvars_list: list[dict], expected_ids: list[int], mock_file_data: dict, expected_data: dict, requested_ids: list[int | None] | None
) -> None:
    """
    Test PoolManager.

    Args:
        hostvars_list: Request ID for each host in this list.
        expected_ids: Expected answer on get_id for each host.
        mock_file_data: Initial file data. None for missing file.
        expected_data: File data after saving to file.
        requested_ids: Request this specific ID per host. Index must match hostvars_list.
    """
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
        pool_manager = PoolManager(Path(DUMMYDIR))

        for index, hostvars in enumerate(hostvars_list):
            requested_id = requested_ids[index] if requested_ids else None
            _hostvars = hostvars.copy()
            hostname = _hostvars.pop("inventory_hostname")
            shared_utils = SharedUtils(hostname=hostname, hostvars=_hostvars, inputs=EosDesigns._from_dict(hostvars), templar=object(), peer_facts={})
            # Get the id of the host from hostvars. If not, a new data set will be created.
            assert pool_manager.get_assignment("node_id_pools", shared_utils, requested_id) == expected_ids[index]

        mocked_exists.assert_called_once()
        if file_exists:
            mocked_open.assert_called_once()
            _args, kwargs = mocked_open.call_args
            assert "mode" in kwargs
            assert kwargs["mode"] == "r"
        else:
            mocked_open.assert_not_called()

        assert pool_manager.save_updated_pools() is expected_write

        if not file_exists:
            # If the mocked file does not exists check that it was created together with the parent dir.
            mocked_mkdir: mock.MagicMock = mocked_parent.return_value.mkdir
            mocked_mkdir.assert_called_once_with(exist_ok=True, mode=509, parents=True)
            mocked_touch.assert_called_once()

        if expected_write:
            mocked_open.assert_called()
            _args, kwargs = mocked_open.call_args_list[-1]
            assert "mode" in kwargs
            assert kwargs["mode"] == "w"
            mocked_file_write.assert_called_once_with(get_file_content(expected_data))
        else:
            mocked_open.assert_called_once()
            _args, kwargs = mocked_open.call_args
            assert "mode" in kwargs
            assert kwargs["mode"] == "r"
            mocked_file_write.assert_not_called()


@dataclass
class DummySharedUtils:
    fabric_name: str
    type: str
    dc_name: str | None = None
    pod_name: str | None = None
    inputs: object | None = None


@pytest.mark.parametrize(
    ("mock_file_data", "shared_utils", "expected_exception"),
    [
        pytest.param(
            {"node_id_pools": "test"},
            DummySharedUtils(fabric_name="Test", type="test"),
            TypeError("Invalid type '<class 'str'>'. Expected a dict."),
            id="invalid_pools_type",
        ),
        pytest.param(
            {"node_id_pools": {123: {}}},
            DummySharedUtils(fabric_name="Test", type="test"),
            TypeError("Invalid type for pool key '<class 'int'>'. Expected a str."),
            id="invalid_pool_key_type",
        ),
        pytest.param(
            {"node_id_pools": {"fabric_name=fabric/dc_name=dc/pod_name=pod/type=mytype": None}},
            DummySharedUtils(fabric_name="Test", type="test"),
            TypeError("assignments"),
            id="missing_pool_assignments",
        ),
        pytest.param(
            {"node_id_pools": {"fabric_name=fabric/dc_name=dc/pod_name=pod/type=mytype": "foo"}},
            DummySharedUtils(fabric_name="Test", type="test"),
            TypeError("Invalid type for pool assignments '<class 'str'>'. Expected a dict."),
            id="invalid_pool_assignments_type",
        ),
        pytest.param(
            {"node_id_pools": {"fabric_name=fabric/dc_name=dc/pod_name=pod/type=mytype": ["foo"]}},
            DummySharedUtils(fabric_name="Test", type="test"),
            TypeError("Invalid type for pool assignments '<class 'list'>'. Expected a dict."),
            id="invalid_pool_assignment_type",
        ),
        pytest.param(
            {"node_id_pools": {"fabric_name=fabric/dc_name=dc/pod_name=pod/type=mytype": {123: 123}}},
            DummySharedUtils(fabric_name="Test", type="test"),
            TypeError("Invalid type for assignment key '<class 'int'>'. Expected a str."),
            id="invalid_pool_assignment_key",
        ),
        pytest.param(
            {
                "node_id_pools": {
                    "fabric_name=fabric/dc_name=dc/pod_name=pod/type=mytype": {"hostname=myhost": "foo"},
                }
            },
            DummySharedUtils(fabric_name="Test", type="test"),
            TypeError("Invalid type for assignment 'value' '<class 'str'>'. Expected a int."),
            id="invalid_pool_assignment_value",
        ),
    ],
)
def test_avdpoolmanager_load_data_negative(mock_file_data: dict, shared_utils: DummySharedUtils, expected_exception: Exception) -> None:
    with (
        mock.patch.object(Path, "exists", mock.Mock()),
        mock.patch.object(Path, "open", mock.mock_open(read_data=get_file_content(mock_file_data))),
        mock.patch.object(Path, "parent", mock.PropertyMock(mkdir=mock.MagicMock())),
        mock.patch.object(Path, "touch", mock.Mock()),
    ):
        shared_utils.inputs = mock.MagicMock()
        pool_manager = PoolManager(Path(DUMMYDIR))
        with pytest.raises(type(expected_exception), match=str(expected_exception)):
            pool_manager.get_pool("node_id_pools", shared_utils)


@pytest.mark.parametrize(
    ("mock_file_data", "expected_exception"),
    [
        pytest.param("not_a_dict", TypeError("Invalid type for 'pool' '<class 'str'>'. Expected a dict."), id="Wrong data format"),
        pytest.param(
            {"pool_key": "pool_key_not_a_dict"}, TypeError("Invalid type for 'pool_key' '<class 'str'>'. Expected a dict."), id="Wrong data format for pool_key"
        ),
        pytest.param(
            {"pool_key": {}, "assignments": "not_a_list"},
            TypeError("Invalid type for 'assignments' '<class 'str'>'. Expected a list."),
            id="Wrong data format for assignments",
        ),
        pytest.param(
            {"pool_key": {}, "assignments": ["not_a_dict"]},
            TypeError("Invalid assignment type '<class 'str'>'. Expected a dict."),
            id="Wrong data format for one assignment",
        ),
        pytest.param(
            {"pool_key": {}, "assignments": [{"key": "not_a_dict"}]},
            TypeError("Invalid type for assignment 'key' '<class 'str'>'. Expected a dict."),
            id="Wrong data format for one assignment key",
        ),
        pytest.param(
            {"pool_key": {}, "assignments": [{"key": {}, "value": "not_an_int"}]},
            TypeError("Invalid type for assignment 'value' '<class 'str'>'. Expected a int."),
            id="Wrong data format for one assignment value",
        ),
    ],
)
def test_avdpoolmanager_load_old_format_negative(mock_file_data: dict[str, Any] | str, expected_exception: Exception) -> None:
    # mocking value_type for collection for the last test
    mocked_collection = mock.MagicMock()
    mocked_collection.value_type = int
    with pytest.raises(type(expected_exception), match=str(expected_exception)):
        Pool.load_old_format(mock_file_data, mocked_collection)


def test_avdpoolmanager_upgrade_old_data() -> None:
    hostvars = TESTHOST3.copy()
    hostname = hostvars.pop("inventory_hostname")

    file_data_in_old_format = {
        "node_id_pools": [
            {
                "pool_key": {"fabric_name": hostvars["fabric_name"], "dc_name": None, "pod_name": hostvars["pod_name"], "type": hostvars["type"]},
                "assignments": [{"key": {"hostname": hostname}, "value": 123}],
            }
        ]
    }
    expected_data_in_new_format = get_data([get_pool(TESTHOST3, [get_assignment(TESTHOST3, 123)])])

    with (
        mock.patch.object(Path, "exists", mock.Mock(return_value=True)) as mocked_exists,
        mock.patch.object(Path, "open", mock.mock_open(read_data=get_file_content(file_data_in_old_format))) as mocked_open,
        mock.patch.object(Path, "parent", mock.PropertyMock(mkdir=mock.MagicMock())) as _mocked_parent,
        mock.patch.object(Path, "touch", mock.Mock()) as _mocked_touch,
    ):
        mocked_open: mock.MagicMock
        mocked_file_write: mock.MagicMock = mocked_open.return_value.write

        # Initialize pool_manager and feed to shared_utils.
        pool_manager = PoolManager(Path(DUMMYDIR))

        shared_utils = SharedUtils(hostname=hostname, hostvars=hostvars, inputs=EosDesigns._from_dict(hostvars), templar=None, peer_facts={})
        # Get the id of the host from hostvars. If not, a new data set will be created.
        assert pool_manager.get_assignment("node_id_pools", shared_utils) == 123

        mocked_exists.assert_called_once()
        mocked_open.assert_called_once()
        _args, kwargs = mocked_open.call_args
        assert "mode" in kwargs
        assert kwargs["mode"] == "r"

        assert pool_manager.save_updated_pools() is True

        mocked_open.assert_called()
        _args, kwargs = mocked_open.call_args_list[-1]
        assert "mode" in kwargs
        assert kwargs["mode"] == "w"
        mocked_file_write.assert_called_once_with(get_file_content(expected_data_in_new_format))
