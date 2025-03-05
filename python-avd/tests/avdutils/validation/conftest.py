# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from pathlib import Path
from typing import cast

from avdutils._validation import init_store_from_fragments
from schema_tools.constants import SCHEMAS

init_store_from_fragments(
    eos_cli_config_gen=cast(Path, SCHEMAS["eos_cli_config_gen"].fragments_dir),
    eos_designs=cast(Path, SCHEMAS["eos_designs"].fragments_dir),
)
