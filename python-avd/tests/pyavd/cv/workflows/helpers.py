# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from typing import Literal

from aristaproto import _DateTime

from pyavd._cv.api.arista.changecontrol.v1 import Change, ChangeControl, ChangeControlStatus, Flag
from pyavd._cv.api.arista.configlet.v1 import ConfigletAssignment, ConfigletAssignmentKey, MatchPolicy
from pyavd._cv.api.arista.tag.v2 import (
    CreatorType,
    ElementSubType,
    ElementType,
    Tag,
    TagAssignment,
    TagAssignmentKey,
    TagKey,
)
from pyavd._cv.api.fmp import RepeatedString
from pyavd._cv.workflows.models import CVManifest

DEFAULT_TIMESTAMP = _DateTime.fromisoformat("2025-10-03T00:00:00")

# === Mock Creation Functions ===
# These functions create instances of the API classes.


def create_grpc_container(
    container_id: str, name: str, description: str, query: str, configlet_ids: list[str] | None = None, child_ids: list[str] | None = None
) -> ConfigletAssignment:
    """Create a gRPC ConfigletAssignment (container) object."""
    return ConfigletAssignment(
        key=ConfigletAssignmentKey(configlet_assignment_id=container_id),
        display_name=name,
        description=description,
        configlet_ids=RepeatedString(values=configlet_ids or []),
        query=query,
        child_assignment_ids=RepeatedString(values=child_ids or []),
        match_policy=MatchPolicy.MATCH_ALL,
    )


def create_grpc_change_control(
    status: ChangeControlStatus = ChangeControlStatus.NOT_STARTED,
    approved: bool = False,
    error: str | None = None,
    name: str = "Test CC",
    notes: str = "Test Notes",
    time: _DateTime = DEFAULT_TIMESTAMP,
) -> ChangeControl:
    """Create a gRPC ChangeControl object."""
    change = Change(name=name, notes=notes, time=time)
    return ChangeControl(change=change, approve=Flag(value=approved), status=status, error=error)


# === Other Helper Functions ===


def generate_id(key: str) -> str:
    """Helper to consistently generate expected IDs for tests."""
    return CVManifest._generate_deterministic_id(key)


def get_tags_cv_state(tag_type: Literal["device", "interface", "all"]) -> list[Tag]:
    device_tags = [
        Tag(
            key=TagKey(
                workspace_id="", element_type=ElementType.DEVICE, label="device_tag_1", value="device_tag_1_value_2", element_sub_type=ElementSubType.DEVICE
            ),
            creator_type=CreatorType.USER,
        ),
        Tag(
            key=TagKey(
                workspace_id="", element_type=ElementType.DEVICE, label="device_tag_2", value="device_tag_2_value_1", element_sub_type=ElementSubType.DEVICE
            ),
            creator_type=CreatorType.USER,
        ),
        Tag(
            key=TagKey(
                workspace_id="", element_type=ElementType.DEVICE, label="mixed_tag_1", value="mixed_tag_1_value_2", element_sub_type=ElementSubType.DEVICE
            ),
            creator_type=CreatorType.USER,
        ),
        Tag(
            key=TagKey(
                workspace_id="", element_type=ElementType.DEVICE, label="mixed_tag_2", value="mixed_tag_2_value_1", element_sub_type=ElementSubType.DEVICE
            ),
            creator_type=CreatorType.USER,
        ),
        Tag(
            key=TagKey(workspace_id="", element_type=ElementType.DEVICE, label="K", value="V", element_sub_type=ElementSubType.DEVICE),
            creator_type=CreatorType.USER,
        ),
    ]
    interface_tags = [
        Tag(
            key=TagKey(
                workspace_id="",
                element_type=ElementType.INTERFACE,
                label="interface_tag_1",
                value="interface_tag_1_value_2",
                element_sub_type=ElementSubType.DEVICE,
            ),
            creator_type=CreatorType.USER,
        ),
        Tag(
            key=TagKey(
                workspace_id="",
                element_type=ElementType.INTERFACE,
                label="interface_tag_2",
                value="interface_tag_2_value_1",
                element_sub_type=ElementSubType.DEVICE,
            ),
            creator_type=CreatorType.USER,
        ),
        Tag(
            key=TagKey(
                workspace_id="", element_type=ElementType.INTERFACE, label="mixed_tag_1", value="mixed_tag_1_value_2", element_sub_type=ElementSubType.DEVICE
            ),
            creator_type=CreatorType.USER,
        ),
        Tag(
            key=TagKey(
                workspace_id="", element_type=ElementType.INTERFACE, label="mixed_tag_2", value="mixed_tag_2_value_1", element_sub_type=ElementSubType.DEVICE
            ),
            creator_type=CreatorType.USER,
        ),
        Tag(
            key=TagKey(workspace_id="", element_type=ElementType.INTERFACE, label="K", value="V", element_sub_type=ElementSubType.DEVICE),
            creator_type=CreatorType.USER,
        ),
    ]
    if tag_type == "device":
        return device_tags
    if tag_type == "interface":
        return interface_tags
    return device_tags + interface_tags


def get_tags_assignments_cv_state(tag_type: Literal["device", "interface", "all"]) -> list[TagAssignment]:
    device_tag_assignments = [
        TagAssignment(
            key=TagAssignmentKey(
                workspace_id="",
                element_type=ElementType.DEVICE,
                label="device_tag_1",
                value="device_tag_1_value_2",
                device_id="L2_serial",
                element_sub_type=ElementSubType.DEVICE,
            ),
            tag_creator_type=CreatorType.USER,
        ),
        TagAssignment(
            key=TagAssignmentKey(
                workspace_id="",
                element_type=ElementType.DEVICE,
                label="device_tag_1",
                value="device_tag_1_value_2",
                device_id="L3_serial",
                element_sub_type=ElementSubType.DEVICE,
            ),
            tag_creator_type=CreatorType.USER,
        ),
        TagAssignment(
            key=TagAssignmentKey(
                workspace_id="",
                element_type=ElementType.DEVICE,
                label="device_tag_2",
                value="device_tag_2_value_1",
                device_id="L3_serial",
                element_sub_type=ElementSubType.DEVICE,
            ),
            tag_creator_type=CreatorType.USER,
        ),
        TagAssignment(
            key=TagAssignmentKey(
                workspace_id="",
                element_type=ElementType.DEVICE,
                label="mixed_tag_1",
                value="mixed_tag_1_value_2",
                device_id="L2_serial",
                element_sub_type=ElementSubType.DEVICE,
            ),
            tag_creator_type=CreatorType.USER,
        ),
        TagAssignment(
            key=TagAssignmentKey(
                workspace_id="",
                element_type=ElementType.DEVICE,
                label="mixed_tag_1",
                value="mixed_tag_1_value_2",
                device_id="L3_serial",
                element_sub_type=ElementSubType.DEVICE,
            ),
            tag_creator_type=CreatorType.USER,
        ),
        TagAssignment(
            key=TagAssignmentKey(
                workspace_id="",
                element_type=ElementType.DEVICE,
                label="mixed_tag_2",
                value="mixed_tag_2_value_1",
                device_id="L3_serial",
                element_sub_type=ElementSubType.DEVICE,
            ),
            tag_creator_type=CreatorType.USER,
        ),
    ]
    interface_tag_assignments = [
        TagAssignment(
            key=TagAssignmentKey(
                workspace_id="",
                element_type=ElementType.INTERFACE,
                label="interface_tag_1",
                value="interface_tag_1_value_2",
                device_id="L2_serial",
                interface_id="Ethernet1",
                element_sub_type=ElementSubType.DEVICE,
            ),
            tag_creator_type=CreatorType.USER,
        ),
        TagAssignment(
            key=TagAssignmentKey(
                workspace_id="",
                element_type=ElementType.INTERFACE,
                label="interface_tag_1",
                value="interface_tag_1_value_2",
                device_id="L3_serial",
                interface_id="Ethernet1",
                element_sub_type=ElementSubType.DEVICE,
            ),
            tag_creator_type=CreatorType.USER,
        ),
        TagAssignment(
            key=TagAssignmentKey(
                workspace_id="",
                element_type=ElementType.INTERFACE,
                label="interface_tag_2",
                value="interface_tag_2_value_1",
                device_id="L3_serial",
                interface_id="Ethernet1",
                element_sub_type=ElementSubType.DEVICE,
            ),
            tag_creator_type=CreatorType.USER,
        ),
        TagAssignment(
            key=TagAssignmentKey(
                workspace_id="",
                element_type=ElementType.INTERFACE,
                label="mixed_tag_1",
                value="mixed_tag_1_value_2",
                device_id="L2_serial",
                interface_id="Ethernet1",
                element_sub_type=ElementSubType.DEVICE,
            ),
            tag_creator_type=CreatorType.USER,
        ),
        TagAssignment(
            key=TagAssignmentKey(
                workspace_id="",
                element_type=ElementType.INTERFACE,
                label="mixed_tag_1",
                value="mixed_tag_1_value_2",
                device_id="L3_serial",
                interface_id="Ethernet1",
                element_sub_type=ElementSubType.DEVICE,
            ),
            tag_creator_type=CreatorType.USER,
        ),
        TagAssignment(
            key=TagAssignmentKey(
                workspace_id="",
                element_type=ElementType.INTERFACE,
                label="mixed_tag_1",
                value="mixed_tag_1_value_2",
                device_id="L3_serial",
                interface_id="Ethernet1",
                element_sub_type=ElementSubType.DEVICE,
            ),
            tag_creator_type=CreatorType.USER,
        ),
        TagAssignment(
            key=TagAssignmentKey(
                workspace_id="",
                element_type=ElementType.INTERFACE,
                label="mixed_tag_2",
                value="mixed_tag_2_value_1",
                device_id="L3_serial",
                interface_id="Ethernet1",
                element_sub_type=ElementSubType.DEVICE,
            ),
            tag_creator_type=CreatorType.USER,
        ),
    ]
    if tag_type == "device":
        return device_tag_assignments
    if tag_type == "interface":
        return interface_tag_assignments
    return device_tag_assignments + interface_tag_assignments
