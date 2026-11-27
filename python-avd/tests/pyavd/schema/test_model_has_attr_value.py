# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import Any, ClassVar

import pytest

from pyavd._schema.models.avd_indexed_list import AvdIndexedList
from pyavd._schema.models.avd_list import AvdList
from pyavd._schema.models.avd_model import AvdModel
from pyavd._utils.undefined import Undefined


class SampleModel(AvdModel):
    """Minimal model covering scalars, defaults, nested models, lists, indexed lists, and raw dicts."""

    class IndexedItem(AvdModel):
        _fields: ClassVar[dict] = {"name": {"type": str}, "value": {"type": int}}

        name: str
        value: int | None

    class IndexedItems(AvdIndexedList[str, IndexedItem]):
        _primary_key: ClassVar[str] = "name"

    IndexedItems._item_type = IndexedItem

    class StringList(AvdList[str]):
        pass

    StringList._item_type = str

    class NestedModel(AvdModel):
        class LeafModel(AvdModel):
            _fields: ClassVar[dict] = {
                "flag": {"type": bool, "default": True},
                "count": {"type": int},
            }

            flag: bool
            count: int | None

        _fields: ClassVar[dict] = {
            "text": {"type": str},
            "flag": {"type": bool, "default": True},
            "leaf": {"type": LeafModel},
        }

        text: str | None
        flag: bool
        leaf: LeafModel

    _fields: ClassVar[dict] = {
        "flag_with_default": {"type": bool, "default": True},
        "int_val": {"type": int},
        "str_val": {"type": str},
        "nested": {"type": NestedModel},
        "str_list": {"type": StringList},
        "indexed_items": {"type": IndexedItems},
        "raw_dict": {"type": dict},
    }

    flag_with_default: bool
    int_val: int | None
    str_val: str | None
    nested: NestedModel
    str_list: StringList
    indexed_items: IndexedItems
    raw_dict: dict[str, Any]


@pytest.mark.parametrize(
    ("data", "field", "expected"),
    [
        # Scalars
        pytest.param({}, "flag_with_default", False, id="unset_scalar_with_default"),
        pytest.param({}, "int_val", False, id="unset_scalar"),
        pytest.param({"int_val": None}, "int_val", False, id="null_scalar"),
        pytest.param({"flag_with_default": True}, "flag_with_default", True, id="bool_true"),
        pytest.param({"flag_with_default": False}, "flag_with_default", True, id="bool_false"),
        pytest.param({"int_val": 0}, "int_val", True, id="int_zero"),
        pytest.param({"str_val": ""}, "str_val", True, id="empty_string"),
        pytest.param({"str_val": "routed"}, "str_val", True, id="non_empty_string"),
        # Nested AvdModel
        pytest.param({}, "nested", False, id="unset_nested_model"),
        pytest.param({"nested": None}, "nested", False, id="null_nested_model"),
        pytest.param({"nested": {}}, "nested", False, id="empty_nested_model"),
        pytest.param({"nested": {"text": None}}, "nested", False, id="nested_model_only_null_field"),
        pytest.param({"nested": {"leaf": None}}, "nested", False, id="nested_model_null_submodel"),
        pytest.param({"nested": {"leaf": {}}}, "nested", False, id="nested_model_empty_submodel"),
        pytest.param({"nested": {"leaf": {"count": None}}}, "nested", False, id="nested_model_deeply_null"),
        pytest.param({"nested": {"flag": False}}, "nested", True, id="nested_model_falsy_scalar"),
        pytest.param({"nested": {"leaf": {"count": 0}}}, "nested", True, id="nested_model_deeply_set_zero"),
        # AvdList
        pytest.param({}, "str_list", False, id="unset_list"),
        pytest.param({"str_list": None}, "str_list", False, id="null_list"),
        pytest.param({"str_list": []}, "str_list", False, id="empty_list"),
        pytest.param({"str_list": ["a"]}, "str_list", True, id="non_empty_list"),
        # AvdIndexedList
        pytest.param({}, "indexed_items", False, id="unset_indexed_list"),
        pytest.param({"indexed_items": None}, "indexed_items", False, id="null_indexed_list"),
        pytest.param({"indexed_items": []}, "indexed_items", False, id="empty_indexed_list"),
        pytest.param({"indexed_items": [{"name": "item1"}]}, "indexed_items", True, id="non_empty_indexed_list"),
        # Raw dict
        pytest.param({}, "raw_dict", False, id="unset_raw_dict"),
        pytest.param({"raw_dict": None}, "raw_dict", False, id="null_raw_dict"),
        pytest.param({"raw_dict": {}}, "raw_dict", False, id="empty_raw_dict"),
        pytest.param({"raw_dict": {"k": "v"}}, "raw_dict", True, id="non_empty_raw_dict"),
    ],
)
def test_has_attr_value(data: dict[str, Any], field: str, expected: bool) -> None:
    """Verify _has_attr_value across scalar, model, list, indexed list, and raw dict fields."""
    model = SampleModel._from_dict(data)
    assert model._has_attr_value(field) is expected
    assert model._has_data() is expected


def test_has_attr_value_does_not_materialize_defaults() -> None:
    """Calling _has_attr_value and _has_data must not trigger __getattr__ or store defaults."""
    model = SampleModel()

    assert model._has_data() is False
    for field in SampleModel._fields:
        assert model._has_attr_value(field) is False
        assert model._get_defined_attr(field) is Undefined


def test_has_attr_value_false_after_empty_model_materialized_by_getattr() -> None:
    """An empty nested model materialized via attribute access still reports no configured data."""
    model = SampleModel()
    _ = model.nested

    assert model._get_defined_attr("nested") is not Undefined
    assert model._has_attr_value("nested") is False
    assert model._has_data() is False


def test_has_attr_value_true_after_default_materialized_by_getattr() -> None:
    """Accessing a field with a schema default stores it on the model, so subsequent checks return True."""
    model = SampleModel()
    assert model._has_attr_value("flag_with_default") is False
    assert model._has_data() is False

    assert model.flag_with_default is True
    assert model._has_attr_value("flag_with_default") is True
    assert model._has_data() is True

    nested_model = SampleModel()
    assert nested_model._has_attr_value("nested") is False
    assert nested_model._has_data() is False

    assert nested_model.nested.flag is True
    assert nested_model.nested._has_attr_value("flag") is True
    assert nested_model.nested._has_data() is True
    assert nested_model._has_attr_value("nested") is True
    assert nested_model._has_data() is True


def test_has_attr_value_after_deepinherit_null_override() -> None:
    """Null overrides applied before _deepinherit clear inherited scalar, model, list, and indexed list fields."""
    profile = SampleModel._from_dict(
        {
            "str_val": "inherited",
            "nested": {"text": "from_profile"},
            "str_list": ["a"],
            "indexed_items": [{"name": "item1", "value": 1}],
        }
    )
    child = SampleModel._from_dict(
        {
            "str_val": None,
            "nested": None,
            "str_list": None,
            "indexed_items": None,
        }
    )
    child._deepinherit(profile)

    assert child._has_attr_value("str_val") is False
    assert child._has_attr_value("nested") is False
    assert child._has_attr_value("str_list") is False
    assert child._has_attr_value("indexed_items") is False
    assert child._has_data() is False


def test_has_data_ignores_custom_data_and_null_root() -> None:
    """_has_data returns False for _from_null() instances and models holding only _custom_data."""
    assert SampleModel._from_null()._has_data() is False
    assert SampleModel.StringList._from_null()._has_data() is False
    assert SampleModel.IndexedItems._from_null()._has_data() is False

    custom_only = SampleModel._from_dict({"_custom_key": "value"})
    assert custom_only._has_data() is False
