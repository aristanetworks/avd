# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

from dataclasses import fields, is_dataclass
from typing import Any


def normalize_yaml_data(data: Any) -> Any:
    """Recursively normalize data for YAML output, honoring dataclass field YAML key aliases."""
    if is_dataclass(data):
        return {
            str(dataclass_field.metadata.get("yaml_key", dataclass_field.name)): normalize_yaml_data(getattr(data, dataclass_field.name))
            for dataclass_field in fields(data)
        }
    if isinstance(data, dict):
        return {str(key): normalize_yaml_data(value) for key, value in data.items()}
    if isinstance(data, tuple | list):
        return [normalize_yaml_data(value) for value in data]
    return data
