# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import json
from pathlib import Path

import yaml
from jsonschema import validate

from ..meta_schema_model import AristaAvdSchema


class NoAliasDumper(yaml.Dumper):
    def ignore_aliases(self, data):
        return True


with open(Path(__file__).parents[3].joinpath("ansible_collections/arista/avd/roles/eos_designs/schemas/eos_designs.schema.yml"), encoding="UTF-8") as file:
    raw_schema = yaml.safe_load(file.read())


def test_pydantic_dump_matches_original_yaml():
    pydantic_schema = AristaAvdSchema(**raw_schema)

    dump_raw_schema = yaml.dump(raw_schema, Dumper=NoAliasDumper)
    dump_pydantic_schema = yaml.dump(json.loads(pydantic_schema.model_dump_json(by_alias=True, exclude_unset=True)), Dumper=NoAliasDumper)
    assert dump_raw_schema == dump_pydantic_schema


def test_dump_jsonschema():
    pydantic_schema = AristaAvdSchema(**raw_schema)
    # with open(Path(__file__).parent.joinpath("test.jsonschema.json"), mode="w", encoding="UTF-8") as file:
    #     file.write(json.dumps(pydantic_schema.model_json_schema(), indent=4))
    jsonschema = pydantic_schema.model_json_schema()
    validate(raw_schema, jsonschema)
