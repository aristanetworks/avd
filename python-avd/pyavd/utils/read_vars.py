# Copyright (c) 2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from json import load as json_load
from pathlib import Path

from .yaml import yaml_load


def read_vars(filename: Path | str):
    if not isinstance(filename, Path):
        filename = Path(filename)

    with filename.open(mode="r", encoding="UTF-8") as stream:
        if filename.suffix in [".yml", ".yaml"]:
            return yaml_load(stream)
        elif filename.suffix == ".json":
            return json_load(stream)
        else:
            raise NotImplementedError(f"Unsupported file suffix for file '{filename}'")
