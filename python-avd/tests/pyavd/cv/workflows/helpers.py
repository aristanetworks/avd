# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from dataclasses import dataclass, field
from enum import Enum

from pyavd._cv.workflows.models import CVManifest

# === Mock CVClient gRPC Data Structures ===
# These classes mimic the gRPC response objects.


class MockMatchPolicy(Enum):
    UNSPECIFIED = 0
    MATCH_FIRST = 1
    MATCH_ALL = 2


@dataclass
class MockRepeatedString:
    values: list[str] = field(default_factory=list)


@dataclass
class MockAssignmentKey:
    configlet_assignment_id: str


@dataclass
class MockConfigletKey:
    configlet_id: str


@dataclass
class MockConfiglet:
    key: MockConfigletKey
    display_name: str


@dataclass
class MockConfigletAssignment:
    key: MockAssignmentKey
    display_name: str
    description: str
    configlet_ids: MockRepeatedString
    query: str
    child_assignment_ids: MockRepeatedString
    match_policy: MockMatchPolicy


# === Mock Creation Functions ===
# These functions create instances of the mock classes above.


def create_mock_grpc_configlet(configlet_id: str, name: str) -> MockConfiglet:
    """Create a mock gRPC Configlet object using our dataclass."""
    return MockConfiglet(key=MockConfigletKey(configlet_id=configlet_id), display_name=name)


def create_mock_grpc_container(
    container_id: str, name: str, description: str, query: str, configlet_ids: list[str] | None = None, child_ids: list[str] | None = None
) -> MockConfigletAssignment:
    """Create a mock gRPC ConfigletAssignment (container) object using our dataclass."""
    return MockConfigletAssignment(
        key=MockAssignmentKey(configlet_assignment_id=container_id),
        display_name=name,
        description=description,
        configlet_ids=MockRepeatedString(values=configlet_ids or []),
        query=query,
        child_assignment_ids=MockRepeatedString(values=child_ids or []),
        match_policy=MockMatchPolicy.MATCH_ALL,
    )


# === Other Helper Functions ===


def generate_id(key: str) -> str:
    """Helper to consistently generate expected IDs for tests."""
    return CVManifest._generate_deterministic_id(key)
