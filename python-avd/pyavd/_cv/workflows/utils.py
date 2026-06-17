# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from copy import deepcopy
from dataclasses import MISSING, fields, is_dataclass
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from dataclasses import Field

    from .models import CVDeviceDeployment, CVDeviceTag, CVEosConfig, CVInterfaceTag, CVPathfinderMetadata


def extract_from_device_deployments(
    device_deployments: list[CVDeviceDeployment],
) -> tuple[list[CVEosConfig], list[CVDeviceTag], list[CVInterfaceTag], list[CVPathfinderMetadata]]:
    """Extract configs, device tags, interface tags and pathfinder metadata from a list of CVDeviceDeployment objects."""
    configs: list[CVEosConfig] = []
    device_tags: list[CVDeviceTag] = []
    interface_tags: list[CVInterfaceTag] = []
    cv_pathfinder_metadata: list[CVPathfinderMetadata] = []
    for device_deployment in device_deployments:
        if device_deployment.eos_config is not None:
            configs.append(device_deployment.eos_config)
        device_tags.extend(device_deployment.device_tags)
        interface_tags.extend(device_deployment.interface_tags)
        if device_deployment.cv_pathfinder_metadata is not None:
            cv_pathfinder_metadata.append(device_deployment.cv_pathfinder_metadata)
    return configs, device_tags, interface_tags, cv_pathfinder_metadata


def get_result(obj: Any) -> Any:
    """
    Recursively convert workflow model objects into the JSON-compatible structure returned as part of the Ansible module result.

    For objects that implement `get_result()`, that method is called first so the object
    controls which fields are exposed (potentially a subset of the dataclass fields).
    Plain dataclasses without `get_result()` are expanded field-by-field.
    Collections (list, tuple, dict) are traversed recursively.
    All other values are returned as a deep copy.
    """
    if hasattr(obj, "get_result"):
        return get_result(obj.get_result())
    if is_dataclass(obj) and not isinstance(obj, type):
        return {f.name: get_result(getattr(obj, f.name)) for f in fields(obj)}
    if isinstance(obj, list):
        return [get_result(item) for item in obj]
    if isinstance(obj, tuple):
        return tuple(get_result(item) for item in obj)
    if isinstance(obj, dict):
        return {k: get_result(v) for k, v in obj.items()}
    return deepcopy(obj)


def _is_frozen_dataclass(obj: object) -> bool:
    """Return True if object is an instance of a frozen dataclass."""
    params = getattr(type(obj), "__dataclass_params__", None)
    return params is not None and params.frozen


def _reset_field(obj: object, f: Field[Any]) -> None:
    """Reset single dataclass field to its default."""
    value = getattr(obj, f.name)
    if value is not None and is_dataclass(value):
        if not _is_frozen_dataclass(value):
            if hasattr(value, "reset_mutable_fields"):
                value.reset_mutable_fields()
            else:
                reset_mutable_fields(value)
        # Frozen input-based objects (AvdWorkspace, AvdChangeControl) are kept as-is.
    elif f.default is not MISSING:
        setattr(obj, f.name, f.default)
    elif f.default_factory is not MISSING:
        setattr(obj, f.name, f.default_factory())


def reset_mutable_fields(obj: object) -> None:
    """
    Reset all mutable fields of a cv_deploy model/dataclass instance to their original defaults.

    Logic per field:
    - Non-frozen dataclass: call reset_mutable_fields.
    - Frozen dataclass: keep as is.
    - Field with a regular default: set to that default.
    - Field with a default_factory: call the factory.
    - Any other field: skip.
    """
    if not is_dataclass(obj) or isinstance(obj, type):
        return
    for f in fields(obj):
        _reset_field(obj, f)
