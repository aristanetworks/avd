# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Literal
from uuid import uuid4


@dataclass
class CloudVision:
    servers: str | list[str]
    token: str
    verify_certs: bool = True


@dataclass
class CVChangeControl:
    name: str
    description: str | None = None
    id: str | None = None
    """ `id` should not be set on the request. It will be updated with the ID of the created Change Control. """
    change_control_template: CVChangeControlTemplate | None = None
    requested_state: Literal["pending approval", "approved", "submitted", "canceled"] = "pending approval"
    """
    The requested state for the Change Control.

    - `"pending approval"` (default): Leave the Change Control in "pending approval" state.
    - `"approved"`: Approve the Change Control but do not submit.
    - `"submitted"`: Approve and submit the workspace.
    - `"canceled"`: Create and cancel the workspace. Used for dry-run where no changes will be committed to CloudVision.
    """
    final_state: Literal["pending approval", "approved", "submitted", "failed", "canceled"] | None = None


@dataclass
class CVChangeControlTemplate:
    name: str
    id: str | None = None


@dataclass
class CVDeviceTag:
    label: str
    value: str
    device: Device | None = None


@dataclass
class CVInterfaceTag:
    label: str
    value: str
    device: Device | None = None
    interface: str | None = None
    """Must be set if device is set"""


@dataclass
class CVWorkspace:
    name: str = field(default_factory=lambda: f"AVD {datetime.now()}")
    description: str | None = None
    id: str = field(default_factory=lambda: f"ws-{uuid4()}")
    requested_state: Literal["pending", "built", "submitted", "abandoned", "deleted"] = "submitted"
    """
    The requested state for the Workspace.

    - `"pending"`: Leave the Workspace in pending state.
    - `"built"`: Build the Workspace but do not submit.
    - `"submitted"` (default): Build and submit the Workspace.
    - `"abandoned"`: Build and then abandon the Workspace. \
        Used for dry-run where no changes will be committed to CloudVision.
    - `"deleted"`: Build, abort and then delete the Workspace. \
        Used for dry-run where no changes will be committed to CloudVision and the temporary Workspace will be removed to avoid "clutter".
    """
    final_state: Literal["pending", "built", "submitted", "build failed", "abandoned", "deleted"] | None = None


@dataclass
class DeployChangeControlResult:
    failed: bool = False
    errors: list = field(default_factory=list)
    warnings: list = field(default_factory=list)
    change_control: CVChangeControl | None = None
    deployed_devices: list[Device] = field(default_factory=list)
    skipped_devices: list[Device] = field(default_factory=list)


@dataclass
class DeployToCvResult:
    failed: bool = False
    errors: list = field(default_factory=list)
    warnings: list = field(default_factory=list)
    workspace: CVWorkspace | None = CVWorkspace()
    change_control: CVChangeControl | None = None
    # deployed_devices: list[Device] = field(default_factory=list)
    deployed_configs: list[EosConfig] = field(default_factory=list)
    deployed_device_tags: list[CVDeviceTag] = field(default_factory=list)
    deployed_interface_tags: list[CVInterfaceTag] = field(default_factory=list)
    # skipped_devices: list[Device] = field(default_factory=list)
    skipped_configs: list[EosConfig] = field(default_factory=list)
    skipped_device_tags: list[CVDeviceTag] = field(default_factory=list)
    skipped_interface_tags: list[CVInterfaceTag] = field(default_factory=list)
    removed_configs: list[str] = field(default_factory=list)
    removed_device_tags: list[CVDeviceTag] = field(default_factory=list)
    removed_interface_tags: list[CVInterfaceTag] = field(default_factory=list)


@dataclass
class Device:
    hostname: str
    """
    Device hostname or intended hostname.
    `serial_number` or `system_mac_address` must be set if the hostname is not already configured on the device or
    if the hostname is not unique.
    """
    serial_number: str | None = None
    system_mac_address: str | None = None
    _cv_device_id: str | None = None
    """ Do not set this manually. """


@dataclass
class EosConfig:
    config: str
    device: Device
    config_name: str | None = None
    """ By default the hostname of the device is used as config_name """


@dataclass
class TimeOuts:
    """Timeouts in seconds"""

    workspace_build_timeout: float = 300.0
    change_control_creation_timeout: float = 300.0
