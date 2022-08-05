import copy
from ansible_collections.arista.avd.plugins.module_utils.utils import AristaAvdError
try:
    import deepmerge
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
    "prepend_rp": _strategy_prepend_unique
}


def merge(base, *nxt_list, recursive=True, list_merge="append", destructive_merge=True):
    if not destructive_merge:
        base = copy.deepcopy(base)

    if list_merge not in MAP_ANSIBLE_LIST_MERGE_TO_DEEPMERGE_LIST_STRATEGY:
        raise AristaAvdError(f"merge: 'list_merge' argument can only be equal to one of {list(MAP_ANSIBLE_LIST_MERGE_TO_DEEPMERGE_LIST_STRATEGY.keys())}")

    list_strategy = MAP_ANSIBLE_LIST_MERGE_TO_DEEPMERGE_LIST_STRATEGY.get(list_merge, "append")

    dict_strategy = "merge" if recursive else "override"

    merger = deepmerge.Merger(
        # List of tuples with strategies for each type
        [
            (list, [list_strategy]),
            (dict, [dict_strategy]),
            (set, ["union"])
        ],
        # Fallback strategy applied to all other types
        ["override"],
        # Strategy for type conflict
        ["override"]
    )
    for nxt in nxt_list:
        if isinstance(nxt, list):
            for nxt_item in nxt:
                merger.merge(base, nxt_item)
        else:
            merger.merge(base, nxt)

    return base
