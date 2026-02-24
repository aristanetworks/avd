# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import pytest

from pyavd._utils.filtered_map_view import FilteredMapView


def test_filtered_map_view() -> None:
    data = {"a": 1, "b": 2, "c": 3}
    view = FilteredMapView(data, {"b"})
    assert len(view) == 1
    assert list(view) == ["b"]
    assert view["b"] == 2
    with pytest.raises(KeyError):
        view["a"]
