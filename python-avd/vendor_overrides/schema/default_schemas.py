# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from pathlib import Path

pyavd_dir = Path(__file__).parents[2]

DEFAULT_PICKLED_SCHEMAS = {
    "avd_meta_schema": pyavd_dir.joinpath("vendor", "schemas", "avd_meta_schema.pickle"),
    "eos_cli_config_gen": pyavd_dir.joinpath("vendor", "schemas", "eos_cli_config_gen.schema.pickle"),
    "eos_designs": pyavd_dir.joinpath("vendor", "schemas", "eos_designs.schema.pickle"),
}
