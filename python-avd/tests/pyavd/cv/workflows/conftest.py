# Copyright (c) 2025-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from dataclasses import dataclass
from os import environ
from unittest.mock import AsyncMock, MagicMock

import pytest


@pytest.fixture
def mock_cv_client() -> MagicMock:
    """Fixture to provide a mocked CVClient instance with AsyncMocks."""
    client = MagicMock()
    # Patch all required async methods with AsyncMock
    client.get_change_control = AsyncMock()
    client.set_change_control = AsyncMock()
    client.approve_change_control = AsyncMock()
    client.start_change_control = AsyncMock()
    client.wait_for_change_control_state = AsyncMock()

    client.get_configlet_containers = AsyncMock()
    client.set_configlet_containers = AsyncMock()
    client.get_configlets = AsyncMock()
    client.set_configlets_from_files = AsyncMock()
    client.delete_configlets = AsyncMock()
    client.get_studio_inputs_with_path = AsyncMock()
    client.set_studio_inputs = AsyncMock()
    client.delete_configlet_container = AsyncMock()

    client.get_tags = AsyncMock()
    client.set_tags = AsyncMock()
    client.get_tag_assignments = AsyncMock()
    client.set_tag_assignments = AsyncMock()
    client.delete_tag_assignments = AsyncMock()

    return client


@dataclass
class CvEnvironment:
    id: str
    cv_server: str
    cv_access_token: str
    verify_certs: bool


@pytest.fixture(scope="session", params=["PRD", "STG", "ONPREM"])
def cv_environment(request: pytest.FixtureRequest) -> CvEnvironment:
    """
    Fixture that loads environment variables and returns a CvEnvironment dataclass instance.

    Raises:
        pytest.UsageError if environment variables required for testing specific CloudVision environment are not set.
    """
    env_prefix: str = request.param

    cv_server = environ.get(f"CV_{env_prefix}_SERVER")
    cv_access_token = environ.get(f"CV_{env_prefix}_ACCESS_TOKEN")

    err_msg = (
        "Mandatory environment variable '{missing_variable}' for CV_{env_prefix} is missing or is set to an empty string. "
        "Please properly set all required env variables to run tests against CV_{env_prefix} environment."
    )
    if not cv_server or cv_server.strip() == "":
        msg = err_msg.format(missing_variable=f"CV_{env_prefix}_SERVER", env_prefix=env_prefix)
        raise pytest.UsageError(msg)
    if not cv_access_token or cv_access_token.strip() == "":
        msg = err_msg.format(missing_variable=f"CV_{env_prefix}_ACCESS_TOKEN", env_prefix=env_prefix)
        raise pytest.UsageError(msg)

    verify_certs: bool = env_prefix != "ONPREM"

    return CvEnvironment(
        id=f"CVAAS_{env_prefix}",
        cv_server=cv_server.strip(),
        cv_access_token=cv_access_token.strip(),
        verify_certs=verify_certs,
    )
