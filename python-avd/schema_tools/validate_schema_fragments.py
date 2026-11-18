# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Validate authored AVD schema fragments against the generated metaschema."""

from __future__ import annotations

import json
import logging
from typing import TYPE_CHECKING

from jsonschema_rs import Draft202012Validator, ValidationError
from yaml import CSafeLoader, YAMLError
from yaml import load as yaml_load

from .constants import SCHEMAS

if TYPE_CHECKING:
    from collections.abc import Iterator

LOGGER = logging.getLogger(__name__)


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


def validate_schema_fragments() -> None:
    """Validate all authored schemas, reporting every error before aborting the build."""
    LOGGER.info("Validating schema fragments against the metaschema")
    schema_files = sorted(
        path
        for schema_name, schema_paths in SCHEMAS.items()
        if schema_name != "avd_meta_schema"
        for path in (schema_paths.fragments_dir.glob("*.yml") if schema_paths.fragments_dir else [schema_paths.yaml_file])
    )
    # TODO: Override formats["regex"] with pyavd-utils-gen's is_valid_avd_regex_pattern once available
    # to check compatibility with AVD's runtime regex compiler instead of JSON Schema regex syntax alone.
    # https://github.com/aristanetworks/pyavd-utils/pull/364
    metaschema_file = SCHEMAS["avd_meta_schema"].yaml_file
    validator = Draft202012Validator(json.loads(metaschema_file.read_text(encoding="UTF-8")), validate_formats=True)
    failed = False
    for schema_file in schema_files:
        try:
            schema = yaml_load(schema_file.read_text(encoding="UTF-8"), Loader=CSafeLoader)
        except YAMLError as error:
            LOGGER.error("%s: %s", schema_file, error)  # noqa: TRY400 - Keep the diagnostic free of a traceback.
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
                LOGGER.error("%s: %s: %s", schema_file, pointer or "<root>", message)
    if failed:
        msg = "Schema fragment validation failed. See the source filenames and diagnostics above."
        raise ValueError(msg)
