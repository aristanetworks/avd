# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from copy import deepcopy
from typing import TYPE_CHECKING

from deepmerge import Merger

from .mergeonschema import MergeOnSchema

if TYPE_CHECKING:
    from ..._schema.avdschema import AvdSchema


def _strategy_keep(_config, _path, base, nxt):
    """prefer base, otherwise nxt"""
    if base is not None:
        return base
    return nxt


def _strategy_prepend_unique(_config, _path, base, nxt):
    """prepend nxt items without duplicates in base to base."""
    nxt_as_set = set(nxt)
    return nxt + [n for n in base if n not in nxt_as_set]


def _strategy_must_match(_config, path, base, nxt):
    if base != nxt:
        raise ValueError(f"Values of {'.'.join(path)} do not match: {base} != {nxt}")
    return base


MAP_ANSIBLE_LIST_MERGE_TO_DEEPMERGE_LIST_STRATEGY = {
    "replace": "override",
    "keep": _strategy_keep,
    "append": "append",
    "prepend": "prepend",
    "append_rp": "append_unique",
    "prepend_rp": _strategy_prepend_unique,
}


def merge(base, *nxt_list, recursive=True, list_merge="append", same_key_strategy="override", destructive_merge=True, schema: AvdSchema = None):
    """
    Merge two or more data sets using deepmerge

    Parameters
    ----------
    base : Any
        The base data set
    *nxt_list : *Any
        One or more data sets which are merged one by one onto the base data set
    recursive : bool, default=True
        Perform recursive merge of dicts or just override with nxt.
    list_merge : str, default="append"
        Valid values: "append, replace, keep, prepend, append_rp, prepend_rp"
    same_key_strategy : str, default="override"
        Valid values: "override", "use_existing"
        Controls how dictionary keys that are in both base and nxt are handled:
        - "override" means nxt value replace base value.
        - "use_existing" means base value is kept.
        - "must_match" means a ValueError will be raised if values are not matching.
    destructive_merge : bool, default=True
        To optimize performance the merge is done in-place and is destructive for both base and nxt data sets by default.
        Base will be in-place updated with objects from nxt and some objects in nxt will be modified during the merge.
        By setting "destructive_merge=False" both base and nxt data sets will be deep copied and no in-place merge
        will be happen. Instead the merge result will be returned.
    schema : AvdSchema, optional
        An instance of AvdSchema can be passed to merge, to allow merging lists of dictionaries using the "primary_key" defined in the schema.
    """

    if not destructive_merge:
        base = deepcopy(base)

    if list_merge not in MAP_ANSIBLE_LIST_MERGE_TO_DEEPMERGE_LIST_STRATEGY:
        raise ValueError(f"merge: 'list_merge' argument can only be equal to one of {list(MAP_ANSIBLE_LIST_MERGE_TO_DEEPMERGE_LIST_STRATEGY.keys())}")

    list_strategies = [MAP_ANSIBLE_LIST_MERGE_TO_DEEPMERGE_LIST_STRATEGY.get(list_merge, "append")]

    if list_merge != "replace" and schema is not None:
        # If list_merge is not "replace" and we have a schema, we prepend the list_strategies
        # with our schema based list merger "MergeOnSchema"
        # If "primary_key" is not set and equal, we will fallback to the supplied "list_merge" strategy
        merge_on_schema = MergeOnSchema(schema)
        list_strategies.insert(0, merge_on_schema.strategy)

    dict_strategies = ["merge" if recursive else "override"]

    if same_key_strategy == "must_match":
        same_key_strategy = _strategy_must_match

    merger = Merger(
        # List of tuples with strategies for each type
        [(list, list_strategies), (dict, dict_strategies), (set, ["union"])],
        # Fallback strategy applied to all other types
        [same_key_strategy],
        # Strategy for type conflict
        [same_key_strategy],
    )
    for nxt in nxt_list:
        if isinstance(nxt, list):
            for nxt_item in nxt:
                if not destructive_merge:
                    nxt_item = deepcopy(nxt_item)
                merger.merge(base, nxt_item)
        else:
            if not destructive_merge:
                nxt = deepcopy(nxt)
            merger.merge(base, nxt)

    return base
