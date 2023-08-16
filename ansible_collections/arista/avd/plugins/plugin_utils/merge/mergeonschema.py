# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError, AvdSchemaError

if TYPE_CHECKING:
    from ansible_collections.arista.avd.plugins.plugin_utils.schema.avdschema import AvdSchema

try:
    from deepmerge import STRATEGY_END
except ImportError as imp_exc:
    DEEPMERGE_IMPORT_ERROR = imp_exc
else:
    DEEPMERGE_IMPORT_ERROR = None


class MergeOnSchema:
    """
    MergeOnSchema provides the method "strategy" to be used as
    list merge strategy with the deepmerge library.

    The class is needed to allow a schema to be passed along to the method.
    """

    def __init__(self, schema: AvdSchema = None):
        if DEEPMERGE_IMPORT_ERROR:
            raise AristaAvdError("AVD requires python deepmerge to be installed") from DEEPMERGE_IMPORT_ERROR

        self.schema = schema

    def strategy(self, config, path: list, base: list, nxt: list):
        """
        The argument "config" should be an instance of deepmerge.Merger,
        but Ansible sanity test breaks type hinting with imported libs
        """
        # Skip if no schema is supplied
        if not self.schema:
            return STRATEGY_END

        # Skip if we cannot load subschema for path
        try:
            schema = self.schema.subschema(path)
        except AvdSchemaError:
            return STRATEGY_END

        # Skip if the schema for this list is not having "primary_key"
        if "primary_key" not in schema:
            return STRATEGY_END

        primary_key = schema["primary_key"]

        # "merged_nxt_indexes" will contain a list of indexes in nxt that we merged.
        # These will be removed from nxt before passing on to the next strategy.
        merged_nxt_indexes = []

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
                base[base_index] = config.value_strategy(path, base_item, nxt_item)

        # If all nxt items got merged, we can just return the updated base.
        if len(merged_nxt_indexes) == len(nxt):
            return base

        # Since some nxt items were not merged, we pass along a reduced nxt to the next strategy.
        # Reverse to avoid changing indexes when removing from nxt.
        merged_nxt_indexes.reverse()
        for merged_nxt_index in merged_nxt_indexes:
            del nxt[merged_nxt_index]

        # Since we did inplace updates of both nxt and base, we return STRATEGY_END
        # so deepmerge will run the next strategy on the remaining nxt items.
        return STRATEGY_END
