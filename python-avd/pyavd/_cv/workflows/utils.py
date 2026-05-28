# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
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
