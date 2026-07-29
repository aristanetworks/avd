# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from deepmerge.merger import Merger

from deepmerge.strategy.core import STRATEGY_END
from pyavd_utils.schema_store import get_list_primary_key

VALID_SCHEMA_NAMES = frozenset(("eos_config", "eos_cli_config_gen"))
PYAVD_UTILS_SCHEMA_NAME: Literal["eos_config"] = "eos_config"


class MergeOnSchema:
    """
    MergeOnSchema provides the method "strategy" to be used as list merge strategy with the deepmerge library.

    The class is needed to allow a schema to be passed along to the method.
    """

    def __init__(self, schema_name: str | None = None) -> None:
        if schema_name is not None and schema_name not in VALID_SCHEMA_NAMES:
            msg = f"Unsupported schema name '{schema_name}'. Expected one of {sorted(VALID_SCHEMA_NAMES)}."
            raise ValueError(msg)

        self.schema_name = schema_name
        self.get_list_primary_key = get_list_primary_key

        if self.schema_name:
            from pyavd._schema.store import init_store  # noqa: PLC0415

            init_store()

    def _get_primary_key(self, path: list) -> str | None:
        if not self.schema_name:
            return None

        try:
            return self.get_list_primary_key(PYAVD_UTILS_SCHEMA_NAME, [str(path_item) for path_item in path])
        except Exception as error:
            msg = f"Unable to get the primary key for schema '{self.schema_name}' at schema path {path}."
            raise RuntimeError(msg) from error

    def strategy(self, config: Merger, path: list, base: list, nxt: list) -> object:
        """Custom strategy to merge lists on schema primary key."""
        # Skip if no schema_name is supplied
        if not self.schema_name:
            return STRATEGY_END

        # Skip if the schema for this list is not having "primary_key"
        if not (primary_key := self._get_primary_key(path)):
            return STRATEGY_END

        # "merged_nxt_indexes" will contain a list of indexes in nxt that we merged.
        # These will be removed from nxt before passing on to the next strategy.
        merged_nxt_indexes = []

        try:
            # Nested iterations over nxt and base.
            for nxt_index, nxt_item in enumerate(nxt):
                # Skipping items if they are not dicts or don't have primary_key
                if not (isinstance(nxt_item, dict) and primary_key in nxt_item):
                    continue

                for base_index, base_item in enumerate(base):
                    # Skipping items if they are not dicts or don't have primary_key
                    if not (isinstance(base_item, dict) and primary_key in base_item):
                        continue

                    # Skipping items primary_keys don't match.
                    if base_item[primary_key] != nxt_item[primary_key]:
                        continue

                    # Perform regular dict merge on the matching items.
                    merged_nxt_indexes.append(nxt_index)
                    merge_path = [*path, str(base_index)]
                    base[base_index] = config.value_strategy(merge_path, base_item, nxt_item)

        except Exception as e:
            msg = f"An issue occurred while trying to do schema-based deepmerge for the schema path {path} using primary key '{primary_key}'"
            raise RuntimeError(msg) from e
        # If all nxt items got merged, we can just return the updated base.
        if len(merged_nxt_indexes) == len(nxt):
            return base

        try:
            # Since some nxt items were not merged, we pass along a reduced nxt to the next strategy.
            # Reverse to avoid changing indexes when removing from nxt.
            merged_nxt_indexes.sort(reverse=True)
            for merged_nxt_index in merged_nxt_indexes:
                del nxt[merged_nxt_index]

        except Exception as e:
            msg = (
                f"An issue occurred after schema-based deepmerge for the schema path {path} using primary key '{primary_key}', "
                f"while preparing remaining items with to be merged with regular strategies. Merged indexes were {merged_nxt_indexes}"
            )
            raise RuntimeError(msg) from e
        return STRATEGY_END
