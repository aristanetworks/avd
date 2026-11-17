# Copyright (c) 2024-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import pytest
from data_merging_schema_class import DataMergingTestSchema

from pyavd._errors import AristaAvdDuplicateDataError

A_LIST = {"some_list": [1, 2]}
B_LIST = {"some_list": [2, 3, 4]}
UNIQUE_A_AND_B_LISTS = {"some_list": [1, 2, 3, 4]}

A_INDEXED_LIST = {"some_indexed_list": [{"name": "one", "some_int": 1}, {"name": "two", "some_int": 2}]}
B_INDEXED_LIST = {"some_indexed_list": [{"name": "two", "some_int": 2}, {"name": "three", "some_int": 3}, {"name": "four", "some_int": 4}]}
C_INDEXED_LIST = {"some_indexed_list": [{"name": "two", "some_int": 666}]}
UNIQUE_A_AND_B_INDEXED_LISTS = {
    "some_indexed_list": [{"name": "one", "some_int": 1}, {"name": "two", "some_int": 2}, {"name": "three", "some_int": 3}, {"name": "four", "some_int": 4}]
}

A_DICT = {"some_dict": {"some_nested_key": "blah"}}
C_DICT = {"some_dict": {"some_nested_key": "plop"}}

A = {"some_key": 42}
C = {"some_key": 666}


@pytest.mark.parametrize(
    ("a_data", "b_data", "expected"),
    [
        pytest.param({}, {}, {}, id="empty_data"),
        # Testing AvdList
        pytest.param(A_LIST, B_LIST, UNIQUE_A_AND_B_LISTS, id="list"),
        # Testing AvdIndexedList
        pytest.param(A_INDEXED_LIST, B_INDEXED_LIST, UNIQUE_A_AND_B_INDEXED_LISTS, id="indexed_list"),
        # Testing AvdModel
        pytest.param(A_DICT, A_DICT, A_DICT, id="dict"),
    ],
)
def test_data_combining_valid(
    a_data: dict,
    b_data: dict,
    expected: dict,
) -> None:
    a = DataMergingTestSchema._from_dict(a_data)
    b = DataMergingTestSchema._from_dict(b_data)
    a._combine(b)
    assert a._as_dict() == expected


@pytest.mark.parametrize(
    ("a_data", "c_data"),
    [
        pytest.param(A, C, id="conflict_in_top_level_key"),
        pytest.param(A_INDEXED_LIST, C_INDEXED_LIST, id="conflict_in_indexed_list"),
        pytest.param(A_DICT, C_DICT, id="conflict_in_nested_dict"),
    ],
)
def test_data_combining_conflict(
    a_data: dict,
    c_data: dict,
) -> None:
    a = DataMergingTestSchema._from_dict(a_data)
    c = DataMergingTestSchema._from_dict(c_data)
    with pytest.raises(AristaAvdDuplicateDataError, match=r"Found duplicate objects with conflicting data while generating configuration for"):
        a._combine(c)


@pytest.mark.parametrize(
    ("a_data", "key"),
    [
        pytest.param(A_LIST, "some_list", id="wrong_type_list"),
        pytest.param(A_INDEXED_LIST, "some_indexed_list", id="wrong_type_indexed_list"),
        pytest.param(A_DICT, "some_dict", id="wrong_type_model"),
    ],
)
def test_data_combining_wrong_type(
    a_data: dict,
    key: str,
) -> None:
    a = DataMergingTestSchema._from_dict(a_data)
    c = 42
    with pytest.raises(TypeError, match=r"Unable to combine type '<class 'int'>' into '"):
        getattr(a, key)._combine(c)


def test_data_combining_different_custom_data() -> None:
    a = DataMergingTestSchema._from_dict(A_DICT)
    b = DataMergingTestSchema._from_dict(A_DICT)
    # Injecting conflicting values in _custom_data
    a.some_dict._custom_data["my_awesome_key"] = "context_a"
    b.some_dict._custom_data["my_awesome_key"] = "context_b"
    with pytest.raises(AristaAvdDuplicateDataError, match="Found duplicate objects with conflicting data while generating configuration for SomeDict"):
        a._combine(b)
