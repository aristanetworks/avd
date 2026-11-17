# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Validate authored AVD schema fragments against the generated metaschema."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import TYPE_CHECKING

from jsonschema_rs import Draft202012Validator, ValidationError
from yaml import CSafeLoader, YAMLError
from yaml import load as yaml_load

if TYPE_CHECKING:
    from collections.abc import Iterator

REPO_ROOT = Path(__file__).resolve().parents[1]
METASCHEMA_FILE = REPO_ROOT / "python-avd/pyavd/_schema/avd_meta_schema.json"
SCHEMA_PATTERNS = (
    "python-avd/pyavd/*/schema/schema_fragments/*.yml",
    "schemas/*/schema_fragments/*.yml",
    "python-avd/pyavd/_eos_designs/eos_designs_facts/schema/eos_designs_facts.schema.yml",
)


def leaf_errors(error: ValidationError) -> Iterator[ValidationError]:
    """Yield relevant nested errors instead of a summary containing the entire schema fragment."""
    branches = getattr(error.kind, "context", None)
    if not branches:
        yield error
        return
    # Ignore mismatched types at this location, not type errors in descendants.
    matching = [branch for branch in branches if not any(sub.instance_path == [*error.instance_path, "type"] for sub in branch)] or branches
    nested = [sub for branch in matching for sub in branch]
    if not nested:
        yield error
        return
    for sub in nested:
        yield from leaf_errors(sub)


def main() -> int:
    """Validate the schema files passed by pre-commit, reporting every error."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="+", type=Path)
    args = parser.parse_args()
    schema_files = args.files
    # Configuration changes can regenerate the metaschema earlier in the same pre-commit run.
    if any(path.resolve() in (METASCHEMA_FILE, REPO_ROOT / ".pre-commit-config.yaml") for path in schema_files):
        schema_files = sorted(path for pattern in SCHEMA_PATTERNS for path in REPO_ROOT.glob(pattern))
    # TODO: Override formats["regex"] with pyavd-utils-gen's is_valid_avd_regex_pattern once available
    # to check compatibility with AVD's runtime regex compiler instead of JSON Schema regex syntax alone.
    # https://github.com/aristanetworks/pyavd-utils/pull/364
    validator = Draft202012Validator(json.loads(METASCHEMA_FILE.read_text(encoding="UTF-8")), validate_formats=True)
    failed = False
    for schema_file in schema_files:
        try:
            schema = yaml_load(schema_file.read_text(encoding="UTF-8"), Loader=CSafeLoader)
        except YAMLError as error:
            print(f"{schema_file}: {error}", file=sys.stderr)
            failed = True
            continue
        reported: set[tuple[str, str]] = set()
        for error in validator.iter_errors(schema):
            failed = True
            for leaf in leaf_errors(error):
                pointer = "".join(f"/{str(part).replace('~', '~0').replace('/', '~1')}" for part in leaf.instance_path)
                diagnostic = (pointer, leaf.message)
                if diagnostic in reported:
                    continue
                reported.add(diagnostic)
                message = leaf.message.replace("\r", r"\r").replace("\n", r"\n")
                print(f"{schema_file}: {pointer or '<root>'}: {message}", file=sys.stderr)
    return int(failed)


if __name__ == "__main__":
    sys.exit(main())
