# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import gzip
import json
from copy import deepcopy
from functools import lru_cache
from hashlib import sha1
from pathlib import Path
from pickle import HIGHEST_PROTOCOL
from pickle import dump as pickle_dump
from pickle import load as pickle_load

from yaml import CSafeLoader, load

from .avdschemaresolver import AvdSchemaResolver
from .constants import SCHEMAS, SCHEMA_STORE_GZ_FILE


@lru_cache
def create_store(*, load_from_yaml: bool = False, force_rebuild: bool = False) -> dict[str, dict]:
    """
    Create and return a schema store.

    A schema store is a dict of all our schemas like
    {
        "avd_meta_schema": {...avd meta schema as dict...},
        "eos_cli_config_gen": {...schema as dict...},
        "eos_designs": {...schema as dict...},
    }
    The function is cached to save time on multiple calls.

    If load_from_yaml is True it will read and return unresolved schemas from yml files.

    If force_rebuild is True or if this is the first time running AVD after changing schemas/upgrade/install
    the schema yml files will be read, fully resolved, saved as pickle to a file and returned in the
    store dict.
    """
    store = {}

    # Load from YAML if set. This is used by the tool that creates the pickle.
    if load_from_yaml:
        return _create_store_from_yaml()

    # Recompile schemas if needed and store in pickles for next time.
    if force_rebuild or _should_recompile_schemas():
        return _compile_schemas()

    # Load from Pickle.
    for schema_id, schema_paths in SCHEMAS.items():
        with Path(schema_paths.pickled_schema).open("rb") as file:
            store[schema_id] = pickle_load(file)  # noqa: S301

    return store


def _should_recompile_schemas() -> bool:
    """Returns true if pickled schemas should be recompiled."""
    # Check if any pickled schema is missing
    for schema_paths in SCHEMAS.values():
        if not schema_paths.pickled_schema.exists():
            return True

    # Check if any hash file is missing and if any stored hash does not match the hash of the schema file
    for schema_paths in SCHEMAS.values():
        hash_file = schema_paths.yaml_file.with_suffix(".sha1")
        if not hash_file.exists():
            return True

        existing_hash = hash_file.with_suffix(".sha1").read_text(encoding="UTF-8")
        new_hash = sha1(schema_paths.yaml_file.read_bytes(), usedforsecurity=False).hexdigest()  # NOSONAR
        if existing_hash != new_hash:
            return True

    return False


def _create_store_from_yaml() -> dict[str, dict]:
    """Returns a schema store loaded from yaml files with $ref."""
    store = {}
    for schema_id, schema_paths in SCHEMAS.items():
        with Path(schema_paths.yaml_file).open(encoding="UTF-8") as stream:
            store[schema_id] = load(stream=stream, Loader=CSafeLoader)
    return store


def load_combined_store_from_gz(*, gz_path: Path | None = None) -> dict[str, dict]:
    """
    Load the combined unresolved schema store produced by ``combine_schemas``.

    This is the same JSON document written to ``schemas.json.gz`` and compiled
    into ``schemas.rkyv`` for runtime validation. Tooling that needs unresolved
    cross-schema ``$ref`` markers (such as the Schema Explorer) should prefer
    this entry point over re-reading individual combined YAML files.
    """
    path = gz_path or SCHEMA_STORE_GZ_FILE
    if not path.is_file():
        msg = f"Combined schema store not found: {path}. Run schema build (combine_schemas) first."
        raise FileNotFoundError(msg)

    with gzip.open(path, "rt", encoding="UTF-8") as gz_file:
        store = json.load(gz_file)

    if not isinstance(store, dict):
        msg = f"Invalid combined schema store in {path}: expected a JSON object"
        raise TypeError(msg)

    return store


def load_unresolved_store(*, prefer_gz: bool = True) -> dict[str, dict]:
    """
    Return unresolved schemas for documentation tooling.

    Prefers ``schemas.json.gz`` when present and falls back to combined YAML.
    """
    if prefer_gz and SCHEMA_STORE_GZ_FILE.is_file():
        return load_combined_store_from_gz()
    return _create_store_from_yaml()


def neutralize_hidden_cross_schema_refs(node: dict, own_schema_id: str) -> None:
    """
    Strip cross-schema ``$ref`` only when ``documentation_options.hide_keys`` is set.

    Matches pyavd schema docs: ``hide_keys`` blocks inlining reused schema
    subtrees (for example ``structured_config`` → ``eos_cli_config_gen#``).
    Other cross-schema ``$ref`` values are left for ``AvdSchemaResolver`` so
    keys such as ``aaa_settings.authentication.login`` keep their children.

    Same-schema ``$ref`` is never modified here.
    """
    if not isinstance(node, dict):
        return

    doc_opts = node.get("documentation_options") or {}
    hide_keys = doc_opts.get("hide_keys")
    ref = node.get("$ref")
    if hide_keys and isinstance(ref, str) and "#" in ref:
        target_schema = ref.split("#", 1)[0]
        if target_schema and target_schema != own_schema_id:
            node["_cross_ref"] = ref
            node.pop("$ref", None)

    for child_key in ("keys", "dynamic_keys"):
        children = node.get(child_key)
        if isinstance(children, dict):
            for child in children.values():
                neutralize_hidden_cross_schema_refs(child, own_schema_id)
    if isinstance(node.get("items"), dict):
        neutralize_hidden_cross_schema_refs(node["items"], own_schema_id)
    defs = node.get("$defs")
    if isinstance(defs, dict):
        for child in defs.values():
            neutralize_hidden_cross_schema_refs(child, own_schema_id)


def _compile_schemas() -> dict:
    """
    Resolve full schemas and save as pickle files.

    Load schemas from yaml files
    create a temporary "store",
    resolve all $refs and save the resulting schemas as pickles.
    """
    schema_store = _create_store_from_yaml()

    # We rely on eos_cli_config_gen being before eos_designs,
    # so anything in eos_cli_config_gen can be resolved and $def popped before resolving from eos_designs.
    for schema_name in SCHEMAS:
        if schema_name == "avd_meta_schema":
            # Do not resolve $ref in the meta schema.
            resolved_schema = schema_store[schema_name]
        else:
            resolved_schema = _resolve_schema(schema_store[schema_name], schema_store)

            # Inplace update the schema store with the resolved variant without $def.
            # This is needed so eos_designs will not resolve to a schema with another $ref.
            schema_store[schema_name] = resolved_schema

    # Since all schemas are now fully resolved we can drop the $defs and write the pickle files.
    for schema_name, schema_paths in SCHEMAS.items():
        resolved_schema = schema_store[schema_name]
        if schema_name != "avd_meta_schema":
            # Do not drop $defs from the meta schema.
            resolved_schema.pop("$defs", None)

        # Update pickle file with binary version of the completely resolved schema.
        try:
            with schema_paths.pickled_schema.open("wb") as stream:
                pickle_dump(resolved_schema, stream, HIGHEST_PROTOCOL)

            # Update the .sha1 file with the new hash of the yaml schema file.
            schema_file = schema_paths.yaml_file
            new_hash = sha1(schema_file.read_bytes(), usedforsecurity=False).hexdigest()  # NOSONAR
            schema_file.with_suffix(".sha1").write_text(new_hash, encoding="UTF-8")
        except PermissionError:
            # Ignoring PermissionError so we can operate in read-only environments
            # (like "ansible-test units" containers).
            pass

    return schema_store


def _resolve_schema(schema: dict, store: dict) -> dict:
    """
    Get fully resolved schema (where all $ref has been expanded recursively).

    .schemaresolver performs inplace update of the argument so we give it a copy of the existing schema.
    """
    resolved_schema = deepcopy(schema)
    schemaresolver = AvdSchemaResolver(schema["$id"], store)
    schemaresolver.resolve(resolved_schema)
    return resolved_schema
