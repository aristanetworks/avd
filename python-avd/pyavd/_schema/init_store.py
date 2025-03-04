# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from avdutils._validation import init_store_from_fragments

from .constants import SCHEMA_YAML_FRAGMENTS

SCHEMA_STORE_INITIALIZED = False


def init_store() -> None:
    global SCHEMA_STORE_INITIALIZED  # noqa: PLW0603
    if SCHEMA_STORE_INITIALIZED:
        return

    init_store_from_fragments(
        eos_cli_config_gen=SCHEMA_YAML_FRAGMENTS["eos_cli_config_gen"],
        eos_designs=SCHEMA_YAML_FRAGMENTS["eos_designs"],
    )
    SCHEMA_STORE_INITIALIZED = True
