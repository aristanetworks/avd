#!/usr/bin/env python3
# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import subprocess
from pathlib import Path
from sys import path

# Override global path to load schema from source instead of any installed version.
# Avoids to load from pyavd to avoid relying on pyavd vendor things being generated.
path.insert(0, str(Path(__file__).parents[1].joinpath("pyavd")))

from schema.constants import SCHEMA_PATHS, STORE
from schema.generate_pydantic.models import PydanticFileSrc
from schema.metaschema.meta_schema_model import AristaAvdSchema

for schema_name, schema_path in SCHEMA_PATHS.items():
    if schema_name not in STORE:
        raise KeyError(f"Invalid schema name '{schema_name}'")

    schema = AristaAvdSchema(only_resolve_schema=schema_name, **STORE[schema_name])
    output_file = Path(__file__).parents[1].joinpath(f"pyavd/schema/{schema_name}.py")
    print(f"Building pydantic from schema '{schema_name}'")
    schemasrc = schema._generate_pydantic_src(class_name=schema_name)
    src_file_contents = PydanticFileSrc(classes=[schemasrc.cls])
    with open(output_file, mode="w", encoding="UTF-8") as file:
        file.write(str(src_file_contents))

    print(f"Running 'black' for pydantic model file '{output_file}'")
    subprocess.run(["black", str(output_file)], check=False)
