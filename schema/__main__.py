# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from pathlib import Path
from textwrap import indent

from .generate_docs.tablegen import get_table

with open(Path(__file__).parent.joinpath("test.md"), mode="w", encoding="UTF-8") as file:
    file.write(
        """\
<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

"""
    )
    file.write(indent(get_table("eos_designs", "bgp-settings"), "    "))
