# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import json
from pathlib import Path
from sys import path

import yaml

# Override global path to load schema from source instead of any installed version.
# Avoids to load from pyavd to avoid relying on pyavd vendor things being generated.
path.insert(0, str(Path(__file__).parents[3].joinpath("pyavd")))

from schema.metaschema.meta_schema_model import AristaAvdSchema
from schema.store import create_store


class NoAliasDumper(yaml.Dumper):
    """Dump YAML without generating aliases and anchors for reused ids"""

    def ignore_aliases(self, data):
        return True


raw_schema = create_store()["eos_designs"]


def test_pydantic_dump_matches_original_yaml():
    """
    Loads the schema _without_ resolving the $ref and then dumps the schema again as json.
    Then compares the input schema with the dumped schema.
    """
    pydantic_schema = AristaAvdSchema(resolve_schema=False, **raw_schema)

    dump_raw_schema = yaml.dump(raw_schema, Dumper=NoAliasDumper)
    dump_pydantic_schema = yaml.dump(json.loads(pydantic_schema.model_dump_json(by_alias=True, exclude_unset=True)), Dumper=NoAliasDumper)
    assert dump_raw_schema == dump_pydantic_schema
