# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Validate authored AVD schema fragments against the generated metaschema."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from jsonschema_rs import Draft7Validator
from yaml import CSafeLoader, YAMLError
from yaml import load as yaml_load

REPO_ROOT = Path(__file__).resolve().parents[1]
METASCHEMA_FILE = REPO_ROOT / "python-avd/pyavd/_schema/avd_meta_schema.json"
SCHEMA_PATTERNS = (
    "python-avd/pyavd/*/schema/schema_fragments/*.yml",
    "schemas/*/schema_fragments/*.yml",
    "python-avd/pyavd/_eos_designs/eos_designs_facts/schema/eos_designs_facts.schema.yml",
)


def main() -> int:
    """Validate the schema files passed by pre-commit, reporting every error."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="+", type=Path)
    args = parser.parse_args()
    schema_files = args.files
    # Configuration changes can regenerate the metaschema earlier in the same pre-commit run.
    if any(path.resolve() in (METASCHEMA_FILE, REPO_ROOT / ".pre-commit-config.yaml") for path in schema_files):
        schema_files = sorted(path for pattern in SCHEMA_PATTERNS for path in REPO_ROOT.glob(pattern))
    validator = Draft7Validator(json.loads(METASCHEMA_FILE.read_text(encoding="UTF-8")))
    failed = False
    for schema_file in schema_files:
        try:
            schema = yaml_load(schema_file.read_text(encoding="UTF-8"), Loader=CSafeLoader)
        except YAMLError as error:
            print(f"{schema_file}: {error}", file=sys.stderr)
            failed = True
            continue
        for error in validator.iter_errors(schema):
            print(f"{schema_file}: {error}", file=sys.stderr)
            failed = True
    return int(failed)


if __name__ == "__main__":
    sys.exit(main())
