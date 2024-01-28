# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import json
import sys
from importlib import import_module
from pathlib import Path
from unittest import mock

import pytest
from pydantic import BaseModel
from pytest_benchmark.fixture import BenchmarkFixture

# Override global path to load schema from source instead of any installed version.
sys.path.insert(0, str(Path(__file__).parents[3]))

import pyavd.schema.models
import pyavd.schema.types

from schema_tools.generate_pydantic.models import PydanticFileSrc
from schema_tools.generate_pydantic.utils import generate_class_name
from schema_tools.metaschema.meta_schema_model import AristaAvdSchema
from schema_tools.store import create_store

TEST_DATA = [
    # (schema_name: str, data_file: str | none)
    ("eos_cli_config_gen", None),
    ("eos_designs", None),
    ("eos_cli_config_gen", "ethernet-interfaces.json"),
    ("eos_designs", "DC1-BL1A.json"),
]

TEST_SCHEMAS_FROM_STORE = ["eos_cli_config_gen", "eos_designs"]


def load_data_file(data_file: Path) -> dict:
    with open(data_file, mode="r", encoding="UTF-8") as file:
        data = json.load(file)
    # keys = list(data.keys())
    # for key in keys:
    #     if str(key).startswith(("ansible_", "testdir", "playbook_", "groups", "inventory_", "root_dir", "group_names")):
    #         del data[key]
    return data


# Loading from YAML to get the schema with $refs in it instead of the fully resolved schema stored in the .pickle files.
STORE = create_store(load_from_yaml=True)

sys.path.insert(0, str(Path(__file__).parent))


@pytest.mark.parametrize("schema_name", TEST_SCHEMAS_FROM_STORE)
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


@pytest.mark.parametrize("schema_name,data_file", TEST_DATA)
def test_import_and_load_model(schema_name: str, data_file: str, artifacts_path: Path):
    """
    Imports the generated pydantic models and initializes them with no data.
    Assert that default values are hidden with "exclude_unset=True" and otherwise not.
    """
    with mock.patch.dict(sys.modules, {"artifacts.types": pyavd.schema.types, "artifacts.models": pyavd.schema.models}):
        module = import_module(f"artifacts.{schema_name}")
    class_name = generate_class_name(schema_name)
    Cls = getattr(module, class_name)
    assert issubclass(Cls, BaseModel)

    if data_file is None:
        data = {}
    else:
        data = load_data_file(artifacts_path.joinpath(data_file))

    # Initialize the loaded class with data.
    model = Cls(**data)

    assert isinstance(model, BaseModel)
    if data:
        # Data is a full data set, meaning it might include other stuff than what we cover in the model.
        # So we just check that we can dump something and it contains some keys.
        assert model.model_dump(by_alias=True, exclude_unset=True)
    else:
        # Data is empty so we can verify that nothing is dumped if input is empty
        assert model.model_dump(by_alias=True, exclude_unset=True) == data
    assert model.model_dump(by_alias=True) != data


@pytest.mark.parametrize("schema_name", TEST_SCHEMAS_FROM_STORE)
def test_benchmark_import(schema_name: str, benchmark: BenchmarkFixture):
    """
    Benchmark imports the generated pydantic models.
    """
    with mock.patch.dict(sys.modules, {"artifacts.types": pyavd.schema.types, "artifacts.models": pyavd.schema.models}):

        def importer(module):
            for schema_name in STORE.keys():
                if f"artifacts.{schema_name}" in sys.modules:
                    del sys.modules[f"artifacts.{schema_name}"]
            import_module(module)

        benchmark(importer, f"artifacts.{schema_name}")


@pytest.mark.parametrize("schema_name,data_file", TEST_DATA)
def test_benchmark_init(schema_name: str, data_file: str, artifacts_path: Path, benchmark: BenchmarkFixture):
    """
    Benchmark initialization of the generated pydantic models.
    """
    with mock.patch.dict(sys.modules, {"artifacts.types": pyavd.schema.types, "artifacts.models": pyavd.schema.models}):
        module = import_module(f"artifacts.{schema_name}")
    class_name = generate_class_name(schema_name)
    Cls = getattr(module, class_name)
    assert issubclass(Cls, BaseModel)

    if data_file is None:
        data = {}
    else:
        data = load_data_file(artifacts_path.joinpath(data_file))

    # Initialize the loaded class with data.
    benchmark(Cls, **data)
