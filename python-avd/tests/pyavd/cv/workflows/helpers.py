# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from pyavd._cv.api.arista.configlet.v1 import ConfigletAssignment, ConfigletAssignmentKey, MatchPolicy
from pyavd._cv.api.fmp import RepeatedString
from pyavd._cv.workflows.models import CVManifest

# === Mock Creation Functions ===
# These functions create instances of the api classes.


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


# === Other Helper Functions ===


def generate_id(key: str) -> str:
    """Helper to consistently generate expected IDs for tests."""
    return CVManifest._generate_deterministic_id(key)
