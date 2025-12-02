# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, cast

import pytest

from pyavd_utils.validation import init_store_from_fragments

if TYPE_CHECKING:
    from pathlib import Path


@pytest.fixture(scope="package")
def init_store() -> None:
    from schema_tools.constants import SCHEMAS

    init_store_from_fragments(
        eos_cli_config_gen=cast("Path", SCHEMAS["eos_cli_config_gen"].fragments_dir),
        eos_designs=cast("Path", SCHEMAS["eos_designs"].fragments_dir),
    )
