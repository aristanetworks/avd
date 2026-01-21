# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from functools import lru_cache
from pathlib import Path
from pickle import load
from typing import Any

from pyavd._utils.run_once import run_once
from pyavd.constants import SCHEMA_STORE_GZ_FILE

from .constants import PICKLED_SCHEMAS


@lru_cache
def create_store(*, load_from_yaml: bool = False) -> dict[str, dict[str, Any]]:
    if load_from_yaml:
        msg = "'load_from_yaml' not supported for create_store under PyAVD"
        raise NotImplementedError(msg)
    store = {}
    for schema_id, schema_file in PICKLED_SCHEMAS.items():
        with Path(schema_file).open("rb") as file:
            store[schema_id] = load(file)  # noqa: S301

    return store


@run_once
def init_store() -> None:
    """
    Init the schema store in pyavd-utils.

    This should be called at least one time before each validation.
    The run_once decorator will ensure we only run this once and otherwise do a quick return on subsequent calls.

    TODO: Init from fragments when running from source.
    """
    from pyavd_utils.validation import init_store_from_file  # noqa: PLC0415

    init_store_from_file(SCHEMA_STORE_GZ_FILE)
