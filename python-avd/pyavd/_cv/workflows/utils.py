# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from copy import deepcopy
from dataclasses import fields, is_dataclass
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from pyavd._cv.api.arista.changecontrol.v1 import ChangeControl
    from pyavd._cv.client import CVClient

    from .models import CVChangeControl, CVDeviceDeployment, CVDeviceTag, CVEosConfig, CVInterfaceTag, CVPathfinderMetadata


async def update_change_control_details_on_cv(change_control: CVChangeControl, cv_client: CVClient) -> tuple[ChangeControl, bool]:
    """Update Change Control details when needed and return the current CloudVision object and change status."""
    cv_change_control = await cv_client.get_change_control(change_control_id=change_control.id)
    changed = False

    if change_control.name is None:
        change_control.name = cv_change_control.change.name
    if change_control.description is None:
        change_control.description = cv_change_control.change.notes

    # TODO: Add CC template

    if change_control.name != cv_change_control.change.name or change_control.description != cv_change_control.change.notes:
        await cv_client.set_change_control(change_control_id=change_control.id, name=change_control.name, description=change_control.description)
        changed = True
        # Update the local copy to get the exact "last updated" timestamp needed for approval.
        cv_change_control = await cv_client.get_change_control(change_control_id=change_control.id)

    return cv_change_control, changed


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
