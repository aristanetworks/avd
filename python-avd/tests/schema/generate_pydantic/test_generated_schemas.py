# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from pathlib import Path
from sys import path

# Override global path to load schema from source instead of any installed version.
# Avoids to load from pyavd to avoid relying on pyavd vendor things being generated.
path.insert(0, str(Path(__file__).parents[3].joinpath("pyavd")))

# TODO:
# - Build a test schema in AVD Schema format execising all the schema variants and options in various combinations
# - Generate the pydantic schema from that and import.
# - Build positive and negative test cases for each combination using the pydantic schema.
