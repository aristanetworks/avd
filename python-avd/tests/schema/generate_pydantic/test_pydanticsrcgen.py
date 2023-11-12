# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import json
import sys
from importlib import import_module
from pathlib import Path
from unittest import mock

import pytest
from pydantic import BaseModel

# Override global path to load schema from source instead of any installed version.
sys.path.insert(0, str(Path(__file__).parents[3]))

import pyavd.schema.models
import pyavd.schema.types
from pyavd.schema.constants import STORE
from pyavd.schema.generate_pydantic.models import PydanticFileSrc
from pyavd.schema.generate_pydantic.utils import generate_class_name
from pyavd.schema.metaschema.meta_schema_model import AristaAvdSchema

TEST_DATA = [
    ("eos_cli_config_gen", "ethernet-interfaces.json"),
    ("eos_designs", "DC1-BL1A.json"),
]


def load_data_file(data_file: Path) -> dict:
    with open(data_file, mode="r", encoding="UTF-8") as file:
        data = json.load(file)
    # keys = list(data.keys())
    # for key in keys:
    #     if str(key).startswith(("ansible_", "testdir", "playbook_", "groups", "inventory_", "root_dir", "group_names")):
    #         del data[key]
    return data


@pytest.mark.parametrize("schema_name", STORE.keys())
def test_generate_pydantic_src(schema_name: str):
    """
    Builds pydantic models from the schemas in the schema store.
    Writes the resulting models to python files under artifacts/.
    """
    schema = AristaAvdSchema(only_resolve_schema=schema_name, **STORE[schema_name])
    output_file = Path(__file__).parent.joinpath(f"artifacts/{schema_name}.py")
    print(f"Building pydantic from schema {schema_name}")
    schemasrc = schema._generate_pydantic_src(class_name=schema_name)
    src_file_contents = PydanticFileSrc(classes=[schemasrc.cls])
    with open(output_file, mode="w", encoding="UTF-8") as file:
        file.write(str(src_file_contents))


@pytest.mark.parametrize("schema_name", STORE.keys())
def test_load_model_without_data(schema_name: str):
    """
    Imports the generated pydantic models and initializes them with no data.
    Assert that default values are hidden with "exclude_unset=True" and otherwise not.
    """
    with mock.patch.dict(sys.modules, {"artifacts.types": pyavd.schema.types, "artifacts.models": pyavd.schema.models}):
        module = import_module(f"artifacts.{schema_name}")
    class_name = generate_class_name(schema_name)
    Cls = getattr(module, class_name)
    assert issubclass(Cls, BaseModel)

    # Initialize the loaded class without data.
    model: BaseModel = Cls()

    assert isinstance(model, BaseModel)
    assert model.model_dump(by_alias=True, exclude_unset=True) == {}
    assert model.model_dump(by_alias=True) != {}


@pytest.mark.parametrize("schema_name,data_file", TEST_DATA)
def test_load_model_with_data(schema_name: str, data_file: str, artifacts_path: Path):
    """
    Imports the generated pydantic models and initializes them with no data.
    Assert that default values are hidden with "exclude_unset=True" and otherwise not.
    """
    with mock.patch.dict(sys.modules, {"artifacts.types": pyavd.schema.types, "artifacts.models": pyavd.schema.models}):
        module = import_module(f"artifacts.{schema_name}")
    class_name = generate_class_name(schema_name)
    Cls = getattr(module, class_name)
    assert issubclass(Cls, BaseModel)

    data = load_data_file(artifacts_path.joinpath(data_file))

    # Initialize the loaded class with data.
    model: BaseModel = Cls(**data)

    assert isinstance(model, BaseModel)
    assert model.model_dump(by_alias=True, exclude_unset=True)
