#!/usr/bin/env python3
# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import subprocess
from pathlib import Path
from sys import path

# Override global path to load schema from source instead of any installed version.
path.insert(0, str(Path(__file__).parents[1]))

from schema_tools.constants import PYTHON_CLASS_PATHS
from schema_tools.generate_classes.src_generators import FileSrc
from schema_tools.metaschema.meta_schema_model import AristaAvdSchema
from schema_tools.store import create_store

STORE = create_store(load_from_yaml=True)

for schema_name, python_class_path in PYTHON_CLASS_PATHS.items():
    if schema_name not in STORE:
        msg = f"Invalid schema name '{schema_name}'"
        raise KeyError(msg)

    schema = AristaAvdSchema(resolve_hide_keys=False, **STORE[schema_name])
    print(f"Building Python Classes from schema '{schema_name}'")
    schemasrc = schema._generate_class_src(class_name=schema_name)
    src_file_contents = FileSrc(classes=[schemasrc.cls])
    with python_class_path.open(mode="w", encoding="UTF-8") as file:
        file.write(str(src_file_contents))

    print(f"Running 'ruff' for Python class file '{python_class_path}'")
    subprocess.run(["ruff", "check", "--fix", str(python_class_path)], check=False)  # noqa: S603, S607
    subprocess.run(["ruff", "format", str(python_class_path)], check=False)  # noqa: S603, S607
