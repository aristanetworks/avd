# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

from contextlib import AbstractContextManager
from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from jinja2.utils import Namespace

from pyavd.j2filters.natural_sort import _alphanum_key, _convert, natural_sort


class TestNaturalSortFilter:
    @pytest.mark.parametrize(
        ("item_to_convert", "converted_item", "ignore_case"),
        [
            pytest.param("100", 100, True),
            pytest.param("200", 200, True),
            pytest.param("ABC", "abc", True),
            pytest.param("ABC", "ABC", False),
        ],
    )
    def test_convert(self, item_to_convert: str, converted_item: int | str, ignore_case: bool) -> None:
        resp = _convert(item_to_convert, ignore_case)
        assert resp == converted_item

    @pytest.mark.parametrize(
        ("item_to_natural_sort", "sort_key", "strict", "ignore_case", "default_value", "sorted_list", "expected_raise"),
        [
            pytest.param(None, None, False, True, None, [], does_not_raise(), id="None"),
            pytest.param([], None, False, True, None, [], does_not_raise(), id="empty-list"),
            pytest.param({}, "", False, True, None, [], does_not_raise(), id="empty-dict"),
            pytest.param("", "", False, True, None, [], does_not_raise(), id="empty-string"),
            pytest.param("access_list", None, False, True, None, ["_", "a", "c", "c", "e", "i", "l", "s", "s", "s", "t"], does_not_raise(), id="string-input"),
            pytest.param(
                ["1,2,3,4", "11,2,3,4", "5.6.7.8"],  # NOSONAR, IP is just test data
                None,
                False,
                True,
                None,
                ["1,2,3,4", "5.6.7.8", "11,2,3,4"],  # NOSONAR, IP is just test data
                does_not_raise(),
                id="list-of-integers",
            ),
            pytest.param({"a1": 123, "a10": 333, "a2": 2, "a11": 4456}, None, False, True, None, ["a1", "a2", "a10", "a11"], does_not_raise(), id="dict"),
            pytest.param(
                [
                    {"name": "ACL-10", "counters_per_entry": True},
                    {"name": "ACL-01", "counters_per_entry": True},
                    {"name": "ACL-05", "counters_per_entry": False},
                ],
                "name",
                False,
                True,
                None,
                [
                    {"name": "ACL-01", "counters_per_entry": True},
                    {"name": "ACL-05", "counters_per_entry": False},
                    {"name": "ACL-10", "counters_per_entry": True},
                ],
                does_not_raise(),
                id="list-of-dict-with-sort-key",
            ),
            pytest.param(
                [
                    {"name": "ACL-10", "counters_per_entry": True},
                    {"sequence_numbers": {"sequence": 10}},
                    {"counters_per_entry": False},
                    {"name": "ACL-05", "counters_per_entry": False},
                ],
                "name",
                False,
                True,
                None,
                [
                    {"name": "ACL-05", "counters_per_entry": False},
                    {"name": "ACL-10", "counters_per_entry": True},
                    {"counters_per_entry": False},
                    {"sequence_numbers": {"sequence": 10}},
                ],
                does_not_raise(),
                id="list-of-dict-with-sort-key-some-entries-dont-have-the-key",
            ),
            pytest.param(
                [
                    {"sequence_numbers": {"sequence": 10}},
                    {"counters_per_entry": False},
                    {"action": "action_command"},
                ],
                "name",
                False,
                True,
                None,
                [
                    {"action": "action_command"},
                    {"counters_per_entry": False},
                    {"sequence_numbers": {"sequence": 10}},
                ],
                does_not_raise(),
                id="list-of-dict-with-sort-key-all-entries-dont-have-the-key",
            ),
            pytest.param(
                [
                    {"name": "default"},
                    {"name": "D"},
                    {"name": "E"},
                ],
                "name",
                False,
                True,
                None,
                [
                    {"name": "D"},
                    {"name": "default"},
                    {"name": "E"},
                ],
                does_not_raise(),
                id="list-of-dict-with-sort-key-ignore-case",
            ),
            pytest.param(
                [
                    {"name": "default"},
                    {"name": "D"},
                    {"name": "E"},
                ],
                "name",
                False,
                False,
                None,
                [
                    {"name": "D"},
                    {"name": "E"},
                    {"name": "default"},
                ],
                does_not_raise(),
                id="list-of-dict-with-sort-key-respect-case",
            ),
            pytest.param(
                [
                    {"name": "ACL-10", "counters_per_entry": True},
                    {"counters_per_entry": False},
                    {"name": "ACL-05", "counters_per_entry": False},
                ],
                "name",
                True,
                True,
                None,
                None,
                pytest.raises(Exception, match="Missing key 'name' in item to sort "),
                id="list-of-dict-with-sort-key-strict-mode",
            ),
            pytest.param(
                [
                    {"name": "ACL-10", "counters_per_entry": True},
                    {"counters_per_entry": False},
                    {"name": "ACL-05", "counters_per_entry": False},
                ],
                "name",
                True,
                True,
                "ACL-00",
                [
                    {"counters_per_entry": False},
                    {"name": "ACL-05", "counters_per_entry": False},
                    {"name": "ACL-10", "counters_per_entry": True},
                ],
                does_not_raise(),
                id="list-of-dict-with-sort-key-strict-mode-and-default-value",
            ),
        ],
    )
    def test_natural_sort(
        self,
        item_to_natural_sort: Any,
        sort_key: str | None,
        strict: bool,
        ignore_case: bool,
        default_value: Any,
        sorted_list: list | None,
        expected_raise: AbstractContextManager,
    ) -> None:
        with expected_raise:
            resp = natural_sort(item_to_natural_sort, sort_key, strict=strict, ignore_case=ignore_case, default_value=default_value)
            assert resp == sorted_list

    def test_natural_sort_namespaces_basic(self) -> None:
        """Test basic natural sorting with Namespace objects."""
        n1 = Namespace(name="ACL-10", counters_per_entry=True)
        n2 = Namespace(name="ACL-01", counters_per_entry=True)
        n3 = Namespace(name="ACL-05", counters_per_entry=False)

        # Execute
        resp = natural_sort([n1, n2, n3], sort_key="name")

        # Assert identity and order
        assert resp == [n2, n3, n1]
        assert resp[0].name == "ACL-01"
        assert resp[2].name == "ACL-10"

    def test_natural_sort_namespaces_missing_keys(self) -> None:
        """Test sorting when some Namespaces are missing the sort_key (non-strict)."""
        n1 = Namespace(name="ACL-10", counters_per_entry=True)
        n2 = Namespace(sequence_numbers={"sequence": 10})  # Missing 'name'
        n3 = Namespace(counters_per_entry=False)  # Missing 'name'
        n4 = Namespace(name="ACL-05", counters_per_entry=False)

        # Execute
        resp = natural_sort([n1, n2, n3, n4], sort_key="name", strict=False)

        # Based on AVD logic: items with valid keys sort first,
        # then items where the key is missing (defaulting to the item itself).
        # Expected identity order: n4 (ACL-05), n1 (ACL-10), n3, n2
        assert resp == [n4, n1, n3, n2]

    def test_natural_sort_namespaces_all_missing_key(self) -> None:
        """Test sorting when NO Namespaces have the sort_key (non-strict)."""
        # Setup
        n1 = Namespace(sequence_numbers={"sequence": 10})
        n2 = Namespace(counters_per_entry=False)
        n3 = Namespace(action="action_command")

        # Execute
        # Since all are missing the key and default_value is None,
        # they sort based on the items themselves.
        resp = natural_sort([n1, n2, n3], sort_key="name", strict=False, ignore_case=True)

        # Based on your param, the expected order is n3, n2, n1
        # This usually happens if the fallback sorts by the string representation
        # of the objects or their internal data.
        assert resp == [n3, n2, n1]
        assert resp[0].action == "action_command"
        assert resp[1].counters_per_entry is False
        assert resp[2].sequence_numbers["sequence"] == 10

    def test_natural_sort_namespaces_strict_error(self) -> None:
        """Test that strict mode correctly raises AttributeError for Namespaces."""
        n1 = Namespace(counters_per_entry=False)

        # The optimized function raises AttributeError for Namespaces
        msg = "Missing attribute 'name' in item to sort"
        with pytest.raises(KeyError, match=msg):
            natural_sort([n1], sort_key="name", strict=True)

    def test_natural_sort_namespaces_ignore_case(self) -> None:
        """Test natural sorting for Namespaces with ignore_case=True."""
        # Setup
        n1 = Namespace(name="default")
        n2 = Namespace(name="D")
        n3 = Namespace(name="E")

        # Execute
        resp = natural_sort([n1, n2, n3], sort_key="name", ignore_case=True, strict=False)

        # Assert - Expected order: D, default, E
        assert resp == [n2, n1, n3]
        assert resp[0].name == "D"
        assert resp[1].name == "default"
        assert resp[2].name == "E"

    def test_natural_sort_namespaces_respect_case(self) -> None:
        """Test natural sorting for Namespaces with ignore_case=False (case-sensitive)."""
        # Setup
        n1 = Namespace(name="default")
        n2 = Namespace(name="D")
        n3 = Namespace(name="E")

        # Execute
        resp = natural_sort([n1, n2, n3], sort_key="name", ignore_case=False, strict=False)

        # Assert - Expected order: D, E, default
        assert resp == [n2, n3, n1]
        assert resp[0].name == "D"
        assert resp[1].name == "E"
        assert resp[2].name == "default"

    def test_natural_sort_namespaces_with_default(self) -> None:
        """Test sorting using a default_value when the sort_key is missing."""
        n1 = Namespace(name="ACL-10")
        n2 = Namespace(counters_per_entry=False)  # Missing 'name'
        n3 = Namespace(name="ACL-05")

        # Providing "ACL-00" as default means n2 should sort to the front
        resp = natural_sort([n1, n2, n3], sort_key="name", default_value="ACL-00", strict=True)

        assert resp == [n2, n3, n1]
        assert n2.counters_per_entry is False

    def test_natural_sort_as_ip_address(self) -> None:
        """Test numeric sorting of IPv4 and IPv6 addresses."""
        addresses = ["11:22:33:44:55:66:77:77", "::ffff:192.1.56.10", "::1", "192.0.2.10", "192.0.2.2"]

        assert natural_sort(addresses, sort_as_ip_address=True) == [
            "192.0.2.2",
            "192.0.2.10",
            "::1",
            "::ffff:192.1.56.10",
            "11:22:33:44:55:66:77:77",
        ]

    def test_natural_sort_mapping_as_ip_address(self) -> None:
        """Test numeric IP address sorting using a mapping key."""
        entries = [
            {"address": "11:22:33:44:55:66:77:77"},
            {"address": "::ffff:192.1.56.10"},
        ]

        assert natural_sort(entries, sort_key="address", sort_as_ip_address=True) == list(reversed(entries))

    def test_natural_sort_namespace_as_ip_address(self) -> None:
        """Test numeric IP address sorting using a Namespace attribute."""
        high_address = Namespace(address="11:22:33:44:55:66:77:77")
        low_address = Namespace(address="::ffff:192.1.56.10")

        assert natural_sort([high_address, low_address], sort_key="address", sort_as_ip_address=True) == [low_address, high_address]

    def test_natural_sort_as_ip_address_invalid_address(self) -> None:
        """Test that invalid IP addresses raise ValueError."""
        with pytest.raises(ValueError, match="does not appear to be an IPv4 or IPv6 address"):
            natural_sort(["invalid"], sort_as_ip_address=True)

    def test__alphanum_key_failure_mapping(self) -> None:
        with pytest.raises(ValueError, match=r"'natural_sort' requires 'sort_key' to be set when used for a Mapping:"):
            # trying to get a key for a dict without sort_key
            _alphanum_key(item={"name": "blah"})

    def test__alphanum_key_failure_namespace(self) -> None:
        with pytest.raises(ValueError, match=r"'natural_sort' requires 'sort_key' to be set when used for a Namespace:"):
            # trying to get a key for a dict without sort_key
            _alphanum_key(item=Namespace(name="blah"))
