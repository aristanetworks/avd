# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import json
import sys
from importlib import import_module
from pathlib import Path

import pytest

import pyavd._schema.models.avd_model
from schema_tools.generate_classes.class_src_gen import SrcGenInt
from schema_tools.generate_classes.src_generators import FieldSrc, FieldTypeHintSrc, FileSrc
from schema_tools.generate_classes.utils import generate_class_name
from schema_tools.metaschema.meta_schema_model import AristaAvdSchema, AvdSchemaInt
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
    with data_file.open(encoding="UTF-8") as file:
        return json.load(file)


# Loading from YAML to get the schema with $refs in it instead of the fully resolved schema stored in the .pickle files.
STORE = create_store(load_from_yaml=True)

sys.path.insert(0, str(Path(__file__).parent))


@pytest.mark.parametrize("schema_name", TEST_SCHEMAS_FROM_STORE)
def test_generate_class_src(schema_name: str) -> None:
    """
    Builds Python classes from the schemas in the schema store.

    Writes the resulting models to python files under artifacts/.
    """
    schema = AristaAvdSchema(_resolve_schema=schema_name, **STORE[schema_name])
    output_file = Path(__file__).parent.joinpath(f"artifacts/{schema_name}.py")
    schemasrc = schema._generate_class_src(class_name=generate_class_name(schema_name))
    src_file_contents = FileSrc(classes=[schemasrc.cls])
    with output_file.open(mode="w", encoding="UTF-8") as file:
        file.write(str(src_file_contents))


@pytest.mark.parametrize(("schema_name", "data_file"), TEST_DATA)
def test_import_and_load_model(schema_name: str, data_file: str | None, artifacts_path: Path) -> None:
    """Imports the generated Python classes and initializes them with data from the given data_file or no data."""
    module = import_module(f"artifacts.{schema_name}")
    class_name = generate_class_name(schema_name)
    cls = getattr(module, class_name)
    assert issubclass(cls, pyavd._schema.models.avd_model.AvdModel)

    data = {} if data_file is None else load_data_file(artifacts_path.joinpath(data_file))

    # Initialize the loaded class with data.
    model = cls._from_dict(data)

    assert isinstance(model, pyavd._schema.models.avd_model.AvdModel)


class TestSrcGenBase:
    def test_get_key_raises_runtime_error(self) -> None:
        schema = AvdSchemaInt(type="int")
        srcgen = SrcGenInt()
        srcgen.schema = schema
        with pytest.raises(RuntimeError, match=r"'get_key' was called when 'schema._key' is 'None'"):
            srcgen.get_key()

    def test_valid_key_raises_runtime_error(self) -> None:
        schema = AvdSchemaInt(type="int")
        srcgen = SrcGenInt()
        srcgen.schema = schema
        with pytest.raises(RuntimeError, match=r"'valid_key' was called when 'schema._key' is 'None'"):
            _ = srcgen.valid_key


class TestFieldSrc:
    def test_str_renders_none_after_undefined_type(self) -> None:
        field = FieldSrc(name="foo", field_type="str", type_hints=[FieldTypeHintSrc("str")])

        assert str(field) == "foo: str | UndefinedType | None = Undefined"

    def test_field_as_class_attr_does_not_render_undefined_type(self) -> None:
        field = FieldSrc(name="foo", field_type="str", type_hints=[FieldTypeHintSrc("str")])

        assert field.field_as_class_attr() == "foo: str | None"
