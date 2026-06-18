# Copyright (c) 2024-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import sys
from importlib.metadata import PackageNotFoundError
from typing import TYPE_CHECKING
from unittest.mock import Mock, patch

from pyavd._cv.client import CVClient
from pyavd._cv.workflows.models import CloudVision

if TYPE_CHECKING:
    from collections.abc import Callable


def _cloudvision() -> CloudVision:
    return CloudVision(servers=("127.0.0.1",), token="token", username=None, password=None)  # noqa: S106


def _mock_version(versions: dict[str, str]) -> Callable:
    """Return a side_effect callable for patching `version()`."""

    def _version(pkg: str) -> str:
        v = versions.get(pkg)
        if v is None:
            raise PackageNotFoundError(pkg)
        return v

    return _version


ALL_VERSIONS = {
    "pyavd": "6.1.0",
    "aristaproto": "0.1.4",
    "grpcio": "1.81.1",
    "requests": "2.32.5",
}

OPTIONAL_DEPS = ["grpcio", "requests", "ansible-core"]


def test_cv_client_get_user_agent_python_version_unavailable() -> None:
    """Test that user-agent string is built when Python version is unavailable."""
    expected_user_agent = "pyavd/6.1.0 aristaproto/0.1.4 grpcio/1.81.1 requests/2.32.5"

    # Mock requests' Response
    mocked_requests_response = Mock()
    mocked_requests_response.raise_for_status.return_value = None
    mocked_requests_response.json.return_value = {"version": "CVaaS"}

    # Mock requests' API get method
    mocked_requests_get = Mock(return_value=mocked_requests_response)

    with (
        patch("pyavd._cv.client.version", side_effect=_mock_version(ALL_VERSIONS)),
        patch("pyavd._cv.client.platform.python_version", return_value=""),
        patch("pyavd._cv.client.get", mocked_requests_get),
    ):
        cv_client = CVClient(cloudvision=_cloudvision())
        cv_client_user_agent = cv_client._user_agent
        cv_client._init_version()

    assert cv_client_user_agent == expected_user_agent

    http_headers = mocked_requests_get.call_args.kwargs["headers"]
    assert "User-Agent" in http_headers
    assert http_headers["User-Agent"] == expected_user_agent


def test_cv_client_get_user_agent_all_packages_available() -> None:
    """Test that user-agent string includes all packages when all are available."""
    expected_user_agent = "python/3.12.2 pyavd/6.1.0 aristaproto/0.1.4 grpcio/1.81.1 requests/2.32.5"

    # Mock requests' Response
    mocked_requests_response = Mock()
    mocked_requests_response.raise_for_status.return_value = None
    mocked_requests_response.json.return_value = {"version": "CVaaS"}

    # Mock requests' API get method
    mocked_requests_get = Mock(return_value=mocked_requests_response)

    with (
        patch("pyavd._cv.client.version", side_effect=_mock_version(ALL_VERSIONS)),
        patch("pyavd._cv.client.platform.python_version", return_value="3.12.2"),
        patch("pyavd._cv.client.get", mocked_requests_get),
    ):
        cv_client = CVClient(cloudvision=_cloudvision())
        cv_client_user_agent = cv_client._user_agent
        cv_client._init_version()

    assert cv_client_user_agent == expected_user_agent

    http_headers = mocked_requests_get.call_args.kwargs["headers"]
    assert "User-Agent" in http_headers
    assert http_headers["User-Agent"] == expected_user_agent


def test_cv_client_get_user_agent_pyavd_metadata_missing_falls_back_to_version_attr() -> None:
    """Test falling back to pyavd.__version__ when importlib.metadata.version can not fetch pyavd version."""
    expected_user_agent = "python/3.12.2 pyavd/6.100.0 aristaproto/0.1.4 grpcio/1.81.1 requests/2.32.5"

    # Mock requests' Response
    mocked_requests_response = Mock()
    mocked_requests_response.raise_for_status.return_value = None
    mocked_requests_response.json.return_value = {"version": "CVaaS"}

    # Mock requests' API get method
    mocked_requests_get = Mock(return_value=mocked_requests_response)

    versions = {**ALL_VERSIONS, "pyavd": None}

    with (
        patch("pyavd._cv.client.version", side_effect=_mock_version(versions)),
        patch("pyavd.__version__", "6.100.0"),
        patch("pyavd._cv.client.platform.python_version", return_value="3.12.2"),
        patch("pyavd._cv.client.get", mocked_requests_get),
    ):
        cv_client = CVClient(cloudvision=_cloudvision())
        cv_client_user_agent = cv_client._user_agent
        cv_client._init_version()

    assert cv_client_user_agent == expected_user_agent

    http_headers = mocked_requests_get.call_args.kwargs["headers"]
    assert "User-Agent" in http_headers
    assert http_headers["User-Agent"] == expected_user_agent


def test_cv_client_get_user_agent_pyavd_unavailable() -> None:
    """Test that user-agent string excludes pyavd when its version can not be found."""
    expected_user_agent = "python/3.12.2 aristaproto/0.1.4 grpcio/1.81.1 requests/2.32.5"

    # Mock requests' Response
    mocked_requests_response = Mock()
    mocked_requests_response.raise_for_status.return_value = None
    mocked_requests_response.json.return_value = {"version": "CVaaS"}

    # Mock requests' API get method
    mocked_requests_get = Mock(return_value=mocked_requests_response)

    versions = {**ALL_VERSIONS, "pyavd": None}

    with (
        patch("pyavd._cv.client.version", side_effect=_mock_version(versions)),
        patch("pyavd._cv.client.platform.python_version", return_value="3.12.2"),
        patch("pyavd._cv.client.get", mocked_requests_get),
        # Simulate failed import. This must be done after all pyavd-related patched above.
        patch.dict(sys.modules, {"pyavd": None}),
    ):
        cv_client = CVClient(cloudvision=_cloudvision())
        cv_client_user_agent = cv_client._user_agent
        cv_client._init_version()

    assert cv_client_user_agent == expected_user_agent

    http_headers = mocked_requests_get.call_args.kwargs["headers"]
    assert "User-Agent" in http_headers
    assert http_headers["User-Agent"] == expected_user_agent


def test_cv_client_get_user_agent_optional_dependency_missing() -> None:
    """Test that user-agent string omits a missing optional dependency."""
    expected_user_agent = "python/3.12.2 pyavd/6.1.0 grpcio/1.81.1 requests/2.32.5"

    versions = {k: v for k, v in ALL_VERSIONS.items() if k != "aristaproto"}

    # Mock requests' Response
    mocked_requests_response = Mock()
    mocked_requests_response.raise_for_status.return_value = None
    mocked_requests_response.json.return_value = {"version": "CVaaS"}

    # Mock requests' API get method
    mocked_requests_get = Mock(return_value=mocked_requests_response)

    with (
        patch("pyavd._cv.client.version", side_effect=_mock_version(versions)),
        patch("pyavd._cv.client.platform.python_version", return_value="3.12.2"),
        patch("pyavd._cv.client.get", mocked_requests_get),
    ):
        cv_client = CVClient(cloudvision=_cloudvision())
        cv_client_user_agent = cv_client._user_agent
        cv_client._init_version()

    assert cv_client_user_agent == expected_user_agent

    http_headers = mocked_requests_get.call_args.kwargs["headers"]
    assert "User-Agent" in http_headers
    assert http_headers["User-Agent"] == expected_user_agent


def test_cv_client_get_user_agent_no_optional_dependencies() -> None:
    """Test that user-agent string contains only pyavd when no optional dependencies are available."""
    expected_user_agent = "python/3.12.2 pyavd/6.1.0"

    versions = {"pyavd": "6.1.0"}

    # Mock requests' Response
    mocked_requests_response = Mock()
    mocked_requests_response.raise_for_status.return_value = None
    mocked_requests_response.json.return_value = {"version": "CVaaS"}

    # Mock requests' API get method
    mocked_requests_get = Mock(return_value=mocked_requests_response)

    with (
        patch("pyavd._cv.client.version", side_effect=_mock_version(versions)),
        patch("pyavd._cv.client.platform.python_version", return_value="3.12.2"),
        patch("pyavd._cv.client.get", mocked_requests_get),
    ):
        cv_client = CVClient(cloudvision=_cloudvision())
        cv_client_user_agent = cv_client._user_agent
        cv_client._init_version()

    assert cv_client_user_agent == expected_user_agent

    http_headers = mocked_requests_get.call_args.kwargs["headers"]
    assert "User-Agent" in http_headers
    assert http_headers["User-Agent"] == expected_user_agent
