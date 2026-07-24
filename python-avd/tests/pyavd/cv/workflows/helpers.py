# Copyright (c) 2025-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

from datetime import datetime

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

DEFAULT_TIMESTAMP = datetime.fromisoformat("2025-10-03T00:00:00")

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
    time: datetime = DEFAULT_TIMESTAMP,
) -> ChangeControl:
    """Create a gRPC ChangeControl object."""
    change = Change(name=name, notes=notes, time=time)
    return ChangeControl(change=change, approve=Flag(value=approved), status=status, error=error)


# === Tags Helper Functions ===


def _get_device_tag(label: str, value: str) -> Tag:
    """Return a single Device Tag."""
    return Tag(
        key=TagKey(workspace_id="", element_type=ElementType.DEVICE, label=label, value=value, element_sub_type=ElementSubType.DEVICE),
        creator_type=CreatorType.USER,
    )


def _get_interface_tag(label: str, value: str) -> Tag:
    """Return a single Interface Tag."""
    return Tag(
        key=TagKey(workspace_id="", element_type=ElementType.INTERFACE, label=label, value=value, element_sub_type=ElementSubType.DEVICE),
        creator_type=CreatorType.USER,
    )


def _get_device_tag_assignment(label: str, value: str, device_id: str) -> TagAssignment:
    """Return a single Device TagAssignment."""
    return TagAssignment(
        key=TagAssignmentKey(
            workspace_id="",
            element_type=ElementType.DEVICE,
            label=label,
            value=value,
            device_id=device_id,
            element_sub_type=ElementSubType.DEVICE,
        ),
        tag_creator_type=CreatorType.USER,
    )


def _get_interface_tag_assignment(label: str, value: str, device_id: str, interface_id: str = "Ethernet1") -> TagAssignment:
    """Return a single Interface TagAssignment."""
    return TagAssignment(
        key=TagAssignmentKey(
            workspace_id="",
            element_type=ElementType.INTERFACE,
            label=label,
            value=value,
            device_id=device_id,
            interface_id=interface_id,
            element_sub_type=ElementSubType.DEVICE,
        ),
        tag_creator_type=CreatorType.USER,
    )


def get_device_tags_cv_state() -> list[Tag]:
    label_value_map = [
        ("device_tag_1", "device_tag_1_value_2"),
        ("device_tag_2", "device_tag_2_value_1"),
        ("mixed_tag_1", "mixed_tag_1_value_2"),
        ("mixed_tag_2", "mixed_tag_2_value_1"),
        ("K", "V"),
    ]
    return [_get_device_tag(label, value) for label, value in label_value_map]


def get_interface_tags_cv_state() -> list[Tag]:
    label_value_map = [
        ("interface_tag_1", "interface_tag_1_value_2"),
        ("interface_tag_2", "interface_tag_2_value_1"),
        ("mixed_tag_1", "mixed_tag_1_value_2"),
        ("mixed_tag_2", "mixed_tag_2_value_1"),
        ("K", "V"),
    ]
    return [_get_interface_tag(label, value) for label, value in label_value_map]


def get_device_tag_assignments_cv_state() -> list[TagAssignment]:
    label_value_map = [
        ("device_tag_1", "device_tag_1_value_2", "L2_serial"),
        ("device_tag_1", "device_tag_1_value_2", "L3_serial"),
        ("device_tag_2", "device_tag_2_value_1", "L3_serial"),
        ("mixed_tag_1", "mixed_tag_1_value_2", "L2_serial"),
        ("mixed_tag_1", "mixed_tag_1_value_2", "L3_serial"),
        ("mixed_tag_2", "mixed_tag_2_value_1", "L3_serial"),
    ]
    return [_get_device_tag_assignment(label, value, device_id) for label, value, device_id in label_value_map]


def get_interface_tag_assignments_cv_state() -> list[TagAssignment]:
    label_value_map = [
        ("interface_tag_1", "interface_tag_1_value_2", "L2_serial"),
        ("interface_tag_1", "interface_tag_1_value_2", "L3_serial"),
        ("interface_tag_2", "interface_tag_2_value_1", "L3_serial"),
        ("mixed_tag_1", "mixed_tag_1_value_2", "L2_serial"),
        ("mixed_tag_1", "mixed_tag_1_value_2", "L3_serial"),
        ("mixed_tag_2", "mixed_tag_2_value_1", "L3_serial"),
    ]
    return [_get_interface_tag_assignment(label, value, device_id) for label, value, device_id in label_value_map]


# === Other Helper Functions ===


def generate_id(key: str) -> str:
    """Helper to consistently generate expected IDs for tests."""
    return CVManifest._generate_deterministic_id(key)
