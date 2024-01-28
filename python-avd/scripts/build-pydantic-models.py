#!/usr/bin/env python3
# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import subprocess
from pathlib import Path
from sys import path

# Override global path to load schema from source instead of any installed version.
path.insert(0, str(Path(__file__).parents[1]))

from schema_tools.constants import PYDANTIC_MODEL_PATHS
from schema_tools.generate_pydantic.models import PydanticFileSrc
from schema_tools.metaschema.meta_schema_model import AristaAvdSchema
from schema_tools.store import create_store

STORE = create_store(load_from_yaml=True)

for schema_name, pydantic_model_path in PYDANTIC_MODEL_PATHS.items():
    if schema_name not in STORE:
        raise KeyError(f"Invalid schema name '{schema_name}'")

    schema = AristaAvdSchema(only_resolve_schema=schema_name, **STORE[schema_name])
    print(f"Building pydantic from schema '{schema_name}'")
    schemasrc = schema._generate_pydantic_src(class_name=schema_name)
    src_file_contents = PydanticFileSrc(classes=[schemasrc.cls])
    with open(pydantic_model_path, mode="w", encoding="UTF-8") as file:
        file.write(str(src_file_contents))

    print(f"Running 'black' for pydantic model file '{pydantic_model_path}'")
    subprocess.run(["black", str(pydantic_model_path)], check=False)
