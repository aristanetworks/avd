# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from pathlib import Path
from sys import path

import pytest

# Override global path to load schema from source instead of any installed version.
# Avoids to load from pyavd to avoid relying on pyavd vendor things being generated.
path.insert(0, str(Path(__file__).parents[3].joinpath("pyavd")))

from schema.constants import STORE
from schema.generate_docs.mdtabsgen import get_md_tabs
from schema.metaschema.meta_schema_model import AristaAvdSchema

raw_schema = STORE["eos_designs"]


@pytest.mark.parametrize("table_name", ["network-services-multicast-settings"])
def test_get_md_tabs(table_name: str):
    """
    Loads the schema with the resolved $refs and generated md_tabs.
    Write the resulting md_tabs to a file.
    Compare the output with the expected file.
    """
    output_file = Path(__file__).parent.joinpath(f"{table_name}.md")
    expected_file = Path(__file__).parent.joinpath(f"expected-{table_name}.md")

    schema = AristaAvdSchema(resolve_schema=True, **raw_schema)
    md_tabs = get_md_tabs(schema, table_name)
    with open(output_file, mode="w", encoding="UTF-8") as file:
        file.write(md_tabs)
    with open(expected_file, mode="r", encoding="UTF-8") as file:
        assert md_tabs == file.read()
