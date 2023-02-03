from copy import deepcopy

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError
from ansible_collections.arista.avd.plugins.plugin_utils.schema.avdschema import AvdSchema

from .mergeonschema import MergeOnSchema

try:
    from deepmerge import Merger
except ImportError as imp_exc:
    DEEPMERGE_IMPORT_ERROR = imp_exc
else:
    DEEPMERGE_IMPORT_ERROR = None


def _strategy_keep(config, path, base, nxt):
    """prefer base, otherwise nxt"""
    if base is not None:
        return base
    return nxt


def _strategy_prepend_unique(config, path, base, nxt):
    """prepend nxt items without duplicates in base to base."""
    nxt_as_set = set(nxt)
    return nxt + [n for n in base if n not in nxt_as_set]


MAP_ANSIBLE_LIST_MERGE_TO_DEEPMERGE_LIST_STRATEGY = {
    "replace": "override",
    "keep": _strategy_keep,
    "append": "append",
    "prepend": "prepend",
    "append_rp": "append_unique",
    "prepend_rp": _strategy_prepend_unique,
}


def merge(base, *nxt_list, recursive=True, list_merge="append", destructive_merge=True, schema: AvdSchema = None):
    if DEEPMERGE_IMPORT_ERROR:
        raise AristaAvdError("AVD requires python deepmerge to be installed") from DEEPMERGE_IMPORT_ERROR

    if not destructive_merge:
        base = deepcopy(base)

    if list_merge not in MAP_ANSIBLE_LIST_MERGE_TO_DEEPMERGE_LIST_STRATEGY:
        raise AristaAvdError(f"merge: 'list_merge' argument can only be equal to one of {list(MAP_ANSIBLE_LIST_MERGE_TO_DEEPMERGE_LIST_STRATEGY.keys())}")

    list_strategies = [MAP_ANSIBLE_LIST_MERGE_TO_DEEPMERGE_LIST_STRATEGY.get(list_merge, "append")]

    if list_merge != "replace" and isinstance(schema, AvdSchema):
        # If list_merge is not "replace" and we have a valid schema, we prepend the list_strategies
        # with our schema based list merger "MergeOnSchema"
        # If "primary_key" is not set and equal, we will fallback to the supplied "list_merge" strategy
        merge_on_schema = MergeOnSchema(schema)
        list_strategies.insert(0, merge_on_schema.strategy)

    dict_strategies = ["merge" if recursive else "override"]

    merger = Merger(
        # List of tuples with strategies for each type
        [(list, list_strategies), (dict, dict_strategies), (set, ["union"])],
        # Fallback strategy applied to all other types
        ["override"],
        # Strategy for type conflict
        ["override"],
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
