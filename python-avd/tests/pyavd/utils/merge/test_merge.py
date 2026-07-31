# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from pathlib import Path
from unittest.mock import MagicMock

import pytest
import yaml
from deepmerge.strategy.core import STRATEGY_END

from pyavd._utils import merge
from pyavd._utils.merge.mergeonschema import MergeOnSchema

script_dir = Path(__file__).parent
with Path(script_dir, "acl1.yml").open(encoding="utf-8") as data_file:
    acl1 = yaml.load(data_file, Loader=yaml.SafeLoader)
with Path(script_dir, "acl2.yml").open(encoding="utf-8") as data_file:
    acl2 = yaml.load(data_file, Loader=yaml.SafeLoader)
with Path(script_dir, "acl_merged.yml").open(encoding="utf-8") as data_file:
    acl_merged = yaml.load(data_file, Loader=yaml.SafeLoader)


class TestMerge:
    @pytest.mark.parametrize("schema_name", ["eos_config", "eos_cli_config_gen"])
    def test_merge_of_lists_with_primary_keys(self, schema_name: str) -> None:
        """Merge list items by primary key using both public and internal EOS config schema names."""
        merge_result = merge({}, acl1, acl2, schema_name=schema_name, destructive_merge=False)
        assert merge_result == acl_merged

    @pytest.mark.parametrize("schema_name", [None, "eos_config"])
    def test_list_merge_replace(self, schema_name: str | None) -> None:
        """Replace lists without schema-based merging, even when a valid schema name is supplied."""
        merge_result = {}
        merge(merge_result, acl1, acl2, list_merge="replace", schema_name=schema_name)
        assert merge_result == acl2

    def test_unsupported_schema_name_raises(self) -> None:
        """Reject unsupported schema names before attempting schema-store lookups."""
        with pytest.raises(ValueError, match="Unsupported schema name 'invalid_schema'"):
            merge({}, acl1, acl2, schema_name="invalid_schema")


class TestMergeOnSchema:
    def test_get_primary_key_without_schema_name_returns_none(self) -> None:
        """Return no primary key when MergeOnSchema is created without a schema name."""
        assert MergeOnSchema()._get_primary_key(["access_lists"]) is None

    def test_strategy_without_schema_name_returns_strategy_end(self) -> None:
        """Fall through to the next list strategy when no schema name is configured."""
        assert MergeOnSchema().strategy(MagicMock(), [], [], []) is STRATEGY_END

    def test_strategy_without_primary_key_returns_strategy_end(self) -> None:
        """Fall through to the next list strategy when the schema path has no primary key."""
        merge_on_schema = MergeOnSchema("eos_config")
        merge_on_schema.get_list_primary_key = MagicMock(return_value=None)

        assert merge_on_schema.strategy(MagicMock(), ["not_a_list_with_primary_key"], [], []) is STRATEGY_END

    def test_strategy_skips_items_without_matching_primary_key(self) -> None:
        """Only merge dict list items with matching primary-key values and leave the rest for fallback strategies."""
        merge_on_schema = MergeOnSchema("eos_config")
        merge_on_schema.get_list_primary_key = MagicMock(return_value="name")
        config = MagicMock()
        config.value_strategy.return_value = {"name": "base", "value": "merged"}
        base = [{}, {"name": "base"}]
        nxt = [{}, {"name": "new"}, {"name": "base", "value": "next"}]

        assert merge_on_schema.strategy(config, ["access_lists"], base, nxt) is STRATEGY_END
        assert base == [{}, {"name": "base", "value": "merged"}]
        assert nxt == [{}, {"name": "new"}]
        config.value_strategy.assert_called_once_with(["access_lists", "1"], {"name": "base"}, {"name": "base", "value": "next"})

    def test_strategy_returns_base_when_all_next_items_are_merged(self) -> None:
        """Return the updated base immediately when every next item was merged by schema primary key."""
        merge_on_schema = MergeOnSchema("eos_config")
        merge_on_schema.get_list_primary_key = MagicMock(return_value="name")
        config = MagicMock()
        config.value_strategy.return_value = {"name": "base", "value": "merged"}
        base = [{"name": "base"}]
        nxt = [{"name": "base", "value": "next"}]

        assert merge_on_schema.strategy(config, ["access_lists"], base, nxt) is base
        assert base == [{"name": "base", "value": "merged"}]

    def test_get_primary_key_wraps_pyavd_utils_error(self) -> None:
        """Wrap pyavd-utils schema lookup errors with schema name and path context."""
        merge_on_schema = MergeOnSchema("eos_config")
        merge_on_schema.get_list_primary_key = MagicMock(side_effect=ValueError("lookup failed"))

        with pytest.raises(RuntimeError, match=r"Unable to get the primary key for schema 'eos_config' at schema path \['access_lists'\]"):
            merge_on_schema._get_primary_key(["access_lists"])

    def test_strategy_wraps_merge_error(self) -> None:
        """Wrap errors raised while deep-merging matching list items."""
        merge_on_schema = MergeOnSchema("eos_config")
        merge_on_schema.get_list_primary_key = MagicMock(return_value="name")
        config = MagicMock()
        config.value_strategy.side_effect = ValueError("merge failed")

        with pytest.raises(RuntimeError, match="An issue occurred while trying to do schema-based deepmerge"):
            merge_on_schema.strategy(config, ["access_lists"], [{"name": "base"}], [{"name": "base"}])

    def test_strategy_wraps_remaining_items_cleanup_error(self) -> None:
        """Wrap errors raised while removing already-merged items from the fallback merge input."""

        class ListWithFailingDelete(list):
            def __delitem__(self, index: int) -> None:
                msg = f"Cannot delete index {index}"
                raise ValueError(msg)

        merge_on_schema = MergeOnSchema("eos_config")
        merge_on_schema.get_list_primary_key = MagicMock(return_value="name")
        config = MagicMock()
        config.value_strategy.return_value = {"name": "base", "value": "merged"}
        nxt = ListWithFailingDelete([{"name": "base"}, {"name": "new"}])

        with pytest.raises(RuntimeError, match="An issue occurred after schema-based deepmerge"):
            merge_on_schema.strategy(config, ["access_lists"], [{"name": "base"}], nxt)
