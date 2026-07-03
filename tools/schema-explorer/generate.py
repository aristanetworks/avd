# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
r"""
Build the AVD Schema Explorer for the docs site.

Two responsibilities:

1. Generate a ``schema.sqlite`` by loading the eos_designs and
   eos_cli_config_gen schemas through pyavd's ``schema_tools`` resolver, so
   ``dynamic_keys`` placeholders and same-schema ``$ref`` blocks are fully
   expanded. Cross-schema ``$ref`` (e.g. ``eos_cli_config_gen#/...`` from
   inside ``eos_designs``) is stripped before resolution and surfaced as a
   ``cross_ref`` column on the leaf row, so the SQLite stays small instead
   of materializing the entire ``eos_cli_config_gen`` tree under every
   ``structured_config``.
2. Copy the static SPA assets (``static/index.html``, ``static/css/``,
   ``static/js/``) alongside the SQLite into ``--site-dir`` so MkDocs picks
   up a self-contained Schema Explorer page.

Source lives at ``tools/schema-explorer/``; build output goes to
``tools/schema-explorer/build/`` (gitignored). ``mkdocs_hook.py`` copies the
built tree into ``<site_dir>/_assets/schema-explorer/`` on every
``mkdocs build``, so nothing generated lives under the source-controlled
``docs/`` tree. The standalone SPA is reachable at
``/_assets/schema-explorer/index.html``; embedded views are dropped into
any docs page via the ``<schema-explorer>`` custom element.

Usage:
    python tools/schema-explorer/generate.py \\
        --avd-root <repo-root> \\
        --site-dir tools/schema-explorer/build
"""

from __future__ import annotations

import argparse
import json
import shutil
import sqlite3
import sys
import time
from copy import deepcopy
from pathlib import Path

SCHEMA_IDS = ("eos_designs", "eos_cli_config_gen")
HERE = Path(__file__).resolve().parent
STATIC_DIR = HERE / "static"


def _path_depth(key_path: str) -> int:
    """
    Count path segments, treating ``<...>`` placeholders as one segment.

    AVD's dynamic_keys placeholders (e.g. ``<node_type_keys.key>``) contain a
    literal dot, so a naive ``key_path.split(".")`` over-counts depth.
    """
    depth = 1
    in_placeholder = False
    for char in key_path:
        if char == "<":
            in_placeholder = True
        elif char == ">":
            in_placeholder = False
        elif char == "." and not in_placeholder:
            depth += 1
    return depth


def _strip_cross_schema_refs(node: dict, own_schema_id: str) -> None:
    """
    Strip any ``$ref`` that targets a different schema.

    Without this step the resolver would materialize the entire
    ``eos_cli_config_gen`` tree under every ``structured_config`` key in
    ``eos_designs`` — about 155 k duplicated rows. We instead emit a single
    leaf row with a ``cross_ref`` annotation pointing at the other module so
    consumers can link out.

    Same-schema ``$ref`` (e.g. ``eos_designs#/$defs/node_type``) is left intact
    so the resolver expands it normally — that is how dynamic_keys subtrees
    get filled in.
    """
    if not isinstance(node, dict):
        return
    ref = node.get("$ref")
    if isinstance(ref, str) and "#" in ref:
        target_schema = ref.split("#", 1)[0]
        if target_schema and target_schema != own_schema_id:
            node["_cross_ref"] = ref
            node.pop("$ref", None)
    for child_key in ("keys", "dynamic_keys"):
        children = node.get(child_key)
        if isinstance(children, dict):
            for child in children.values():
                _strip_cross_schema_refs(child, own_schema_id)
    if isinstance(node.get("items"), dict):
        _strip_cross_schema_refs(node["items"], own_schema_id)
    defs = node.get("$defs")
    if isinstance(defs, dict):
        for child in defs.values():
            _strip_cross_schema_refs(child, own_schema_id)


def _load_resolved_store(avd_root: Path) -> dict[str, dict]:
    """
    Load both AVD schemas as resolved dicts.

    ``dynamic_keys`` subtrees and same-schema ``$ref``s are expanded;
    cross-schema ``$ref``s (e.g. ``eos_cli_config_gen#/...`` from inside
    ``eos_designs``) are left as leaf annotations to keep the SQLite small.
    """
    python_avd = avd_root / "python-avd"
    if not python_avd.is_dir():
        msg = f"python-avd/ not found under {avd_root}"
        raise FileNotFoundError(msg)
    sys.path.insert(0, str(python_avd))

    from schema_tools.avdschemaresolver import AvdSchemaResolver
    from schema_tools.store import create_store

    raw_store = create_store(load_from_yaml=True)
    # Strip cross-schema $refs in-place across the whole store first, so that
    # when the resolver pulls in $defs subtrees (e.g. eos_designs#/$defs/node_type
    # which itself contains $ref: eos_cli_config_gen#/... under structured_config)
    # those references are already neutralized.
    for schema_id in SCHEMA_IDS:
        _strip_cross_schema_refs(raw_store[schema_id], own_schema_id=schema_id)
    # eos_cli_config_gen must be resolved first so any same-schema $refs
    # within it are settled before eos_designs is processed.
    for schema_id in ("eos_cli_config_gen", "eos_designs"):
        resolved = deepcopy(raw_store[schema_id])
        AvdSchemaResolver(resolved["$id"], raw_store).resolve(resolved)
        raw_store[schema_id] = resolved
    return raw_store


def _flatten(
    keys: dict,
    module: str,
    prefix: str = "",
    parent: str = "",
    inherited_doc_table: str = "",
    list_primary_key: str = "",
    list_primary_key_unique: bool = False,
) -> list[dict]:
    rows: list[dict] = []
    for key_name, props in keys.items():
        if not isinstance(props, dict):
            continue
        key_path = f"{prefix}{key_name}" if prefix else key_name
        var_type = props.get("type", "")
        description = (props.get("description") or "").strip()
        is_primary_key = bool(list_primary_key and key_name == list_primary_key)
        required = 1 if props.get("required") or is_primary_key else 0
        unique = 1 if is_primary_key and list_primary_key_unique else 0
        default = props.get("default")
        default_value = json.dumps(default) if default is not None else None
        depth_value = _path_depth(key_path)

        deprec = props.get("deprecation") or {}
        removed = 1 if deprec.get("removed") else 0
        deprecated = 1 if (deprec.get("warning") and not removed) else 0

        if deprec:
            var_type = f"{var_type}(deprecated)" if var_type else "deprecated"

        doc_opts = props.get("documentation_options") or {}
        doc_table = doc_opts.get("table") or inherited_doc_table
        # Match pyavd's docs convention: a root key with no explicit
        # documentation_options.table defaults to its own name with
        # underscores → hyphens and any <...> markers stripped. This is what
        # eos_cli_config_gen relies on (it almost never sets `table:` itself).
        if not doc_table and not parent:
            doc_table = key_name.replace("<", "").replace(">", "").replace("_", "-")

        constraints: dict = {}
        for k in ("valid_values", "min", "max", "min_length", "max_length", "pattern", "format", "convert_types"):
            if k in props:
                constraints[k] = props[k]
        items = props.get("items")
        if var_type == "list" and isinstance(items, dict):
            item_constraints = {}
            if items.get("type"):
                item_constraints["type"] = items["type"]
            for k in ("valid_values", "min", "max", "min_length", "max_length", "pattern", "format", "convert_types"):
                if k in items:
                    item_constraints[k] = items[k]
            if item_constraints:
                constraints["items"] = item_constraints

        rows.append(
            {
                "module": module,
                "key_path": key_path,
                "var_type": var_type,
                "description": description,
                "default_value": default_value,
                "required": required,
                "unique": unique,
                "parent_path": parent,
                "depth": depth_value,
                "doc_table": doc_table,
                "deprecated": deprecated,
                "removed": removed,
                "cross_ref": props.get("_cross_ref"),
                "constraints": json.dumps(constraints) if constraints else None,
            }
        )

        if isinstance(props.get("keys"), dict):
            rows.extend(_flatten(props["keys"], module, prefix=key_path + ".", parent=key_path, inherited_doc_table=doc_table))

        # dynamic_keys: variable-name placeholders rendered as <name> in the
        # path, matching the convention used by pyavd's schema_tools docs.
        if isinstance(props.get("dynamic_keys"), dict):
            for dyn_name, dyn_schema in props["dynamic_keys"].items():
                if not isinstance(dyn_schema, dict):
                    continue
                dyn_key = f"<{dyn_name}>"
                rows.extend(_flatten({dyn_key: dyn_schema}, module, prefix=key_path + ".", parent=key_path, inherited_doc_table=doc_table))

        if isinstance(items, dict):
            if isinstance(items.get("keys"), dict):
                rows.extend(
                    _flatten(
                        items["keys"],
                        module,
                        prefix=key_path + "[].",
                        parent=key_path,
                        inherited_doc_table=doc_table,
                        list_primary_key=props.get("primary_key") or "",
                        list_primary_key_unique=props.get("allow_duplicate_primary_key") is not True,
                    ),
                )
            if isinstance(items.get("dynamic_keys"), dict):
                for dyn_name, dyn_schema in items["dynamic_keys"].items():
                    if not isinstance(dyn_schema, dict):
                        continue
                    dyn_key = f"<{dyn_name}>"
                    rows.extend(_flatten({dyn_key: dyn_schema}, module, prefix=key_path + "[].", parent=key_path, inherited_doc_table=doc_table))

    return rows


def flatten_schema(data: dict, module: str) -> list[dict]:
    rows: list[dict] = []
    if isinstance(data.get("keys"), dict):
        rows.extend(_flatten(data["keys"], module))
    if isinstance(data.get("dynamic_keys"), dict):
        for dyn_name, dyn_schema in data["dynamic_keys"].items():
            if not isinstance(dyn_schema, dict):
                continue
            dyn_key = f"<{dyn_name}>"
            rows.extend(_flatten({dyn_key: dyn_schema}, module))
    return rows


def _create_schema(conn: sqlite3.Connection) -> None:
    conn.execute("""
        CREATE TABLE schema_vars (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            module TEXT NOT NULL,
            key_path TEXT NOT NULL,
            var_type TEXT,
            description TEXT,
            default_value TEXT,
            required INTEGER DEFAULT 0,
            unique_key INTEGER DEFAULT 0,
            parent_path TEXT,
            depth INTEGER DEFAULT 0,
            doc_table TEXT DEFAULT '',
            deprecated INTEGER DEFAULT 0,
            removed INTEGER DEFAULT 0,
            cross_ref TEXT,
            constraints TEXT
        )
    """)
    conn.execute("CREATE UNIQUE INDEX idx_schema_unique ON schema_vars(module, key_path)")
    conn.execute("CREATE INDEX idx_schema_search ON schema_vars(key_path, module)")
    conn.execute("CREATE INDEX idx_schema_parent ON schema_vars(module, parent_path)")
    conn.execute("CREATE INDEX idx_schema_doc_table ON schema_vars(module, doc_table)")
    conn.execute("""
        CREATE TABLE schema_meta (
            module TEXT NOT NULL,
            loaded_at INTEGER,
            var_count INTEGER,
            PRIMARY KEY (module)
        )
    """)


def build(avd_root: Path, out: Path) -> dict[str, int]:
    if out.parent.exists():
        shutil.rmtree(out.parent)
    out.parent.mkdir(parents=True, exist_ok=True)

    print(f"  loading schemas from {avd_root}/python-avd")
    store = _load_resolved_store(avd_root)

    tmp_out = out.with_suffix(out.suffix + ".tmp")
    if tmp_out.exists():
        tmp_out.unlink()

    conn = sqlite3.connect(str(tmp_out))
    try:
        _create_schema(conn)
        counts: dict[str, int] = {}
        loaded_at = int(time.time())

        for module in SCHEMA_IDS:
            data = store[module]
            print(f"  flattening {module}")
            rows = flatten_schema(data, module)
            conn.executemany(
                """INSERT INTO schema_vars
                   (module, key_path, var_type, description, default_value,
                    required, unique_key, parent_path, depth, doc_table, deprecated,
                    removed, cross_ref, constraints)
                   VALUES (:module, :key_path, :var_type, :description,
                           :default_value, :required, :unique, :parent_path, :depth,
                           :doc_table, :deprecated, :removed,
                           :cross_ref, :constraints)""",
                rows,
            )
            conn.execute(
                "INSERT INTO schema_meta (module, loaded_at, var_count) VALUES (?, ?, ?)",
                (module, loaded_at, len(rows)),
            )
            counts[module] = len(rows)
            print(f"    {len(rows)} variables")
        conn.commit()
        tmp_out.replace(out)
        return counts
    finally:
        conn.close()
        if tmp_out.exists():
            tmp_out.unlink()


def _copy_static_assets(site_dir: Path) -> None:
    """Copy index.html / css/ / js/ from ``static/`` into ``site_dir``."""
    if not STATIC_DIR.is_dir():
        msg = f"Static asset dir not found: {STATIC_DIR}"
        raise FileNotFoundError(msg)
    site_dir.mkdir(parents=True, exist_ok=True)
    for entry in STATIC_DIR.iterdir():
        target = site_dir / entry.name
        if entry.is_dir():
            if target.exists():
                shutil.rmtree(target)
            shutil.copytree(entry, target)
        else:
            shutil.copy2(entry, target)
    print(f"  copied static assets → {site_dir}")


def main() -> int:
    parser = argparse.ArgumentParser(description=(__doc__ or "").strip().splitlines()[0])
    parser.add_argument("--avd-root", type=Path, required=True, help="Path to the avd repo root (the directory containing python-avd/)")
    parser.add_argument(
        "--site-dir",
        type=Path,
        required=True,
        help="Output directory for the built explorer (e.g. tools/schema-explorer/build). "
        "Static assets are copied here and the SQLite is written under "
        "data/schema.sqlite.",
    )
    args = parser.parse_args()

    site_dir = args.site_dir.resolve()
    print("Building Schema Explorer")
    _copy_static_assets(site_dir)

    sqlite_out = site_dir / "data" / "schema.sqlite"
    counts = build(args.avd_root.resolve(), sqlite_out)
    total = sum(counts.values())
    print(f"Wrote {sqlite_out} ({total} variables across {len(counts)} modules)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
