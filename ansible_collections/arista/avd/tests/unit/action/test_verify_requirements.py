# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

import logging
from importlib.metadata import PackageNotFoundError
from itertools import repeat
from pathlib import Path
from typing import NamedTuple
from unittest.mock import patch

import pytest

from ansible_collections.arista.avd.plugins.action.verify_requirements import (
    MIN_PYTHON_SUPPORTED_VERSION,
    _get_collection_version,
    _get_running_collection_version,
    _validate_ansible_collections,
    _validate_ansible_version,
    _validate_python_requirements,
    _validate_python_version,
)


class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: str
    serial: int


@pytest.mark.parametrize(
    ("mocked_version", "expected_return"),
    [
        ((2, 2, 2, "final", 0), False),
        ((MIN_PYTHON_SUPPORTED_VERSION[0], MIN_PYTHON_SUPPORTED_VERSION[1], 42, "final", 0), True),
        ((MIN_PYTHON_SUPPORTED_VERSION[0], MIN_PYTHON_SUPPORTED_VERSION[1] + 1, 42, "final", 0), True),
    ],
)
def test__validate_python_version(mocked_version: tuple[int, int, int, str, int], expected_return: bool) -> None:
    """TODO: - could add the expected stderr."""
    info = {}
    with patch("ansible_collections.arista.avd.plugins.action.verify_requirements.sys") as mocked_sys:
        mocked_sys.version_info = VersionInfo(*mocked_version)
        ret = _validate_python_version(info)
    assert ret == expected_return
    assert info["python_version_info"] == {
        "major": mocked_version[0],
        "minor": mocked_version[1],
        "micro": mocked_version[2],
        "releaselevel": mocked_version[3],
        "serial": mocked_version[4],
    }
    assert bool(info["python_path"])


def test__validate_python_version_deprecation_message() -> None:
    """Test to verify the deprecation message."""
    info: dict[str, str | int] = {}
    with (
        patch("ansible_collections.arista.avd.plugins.action.verify_requirements.DEPRECATE_MIN_PYTHON_SUPPORTED_VERSION", new=True),
        patch("ansible_collections.arista.avd.plugins.action.verify_requirements.sys") as mocked_sys,
    ):
        mocked_sys.version_info = VersionInfo(*MIN_PYTHON_SUPPORTED_VERSION, 42, "final", 0)
        with pytest.warns(DeprecationWarning, match="will drop support for Python version") as recorded_warnings:
            ret = _validate_python_version(info)
    assert ret is True
    assert info["python_version_info"] == {
        "major": MIN_PYTHON_SUPPORTED_VERSION[0],
        "minor": MIN_PYTHON_SUPPORTED_VERSION[1],
        "micro": 42,
        "releaselevel": "final",
        "serial": 0,
    }
    assert bool(info["python_path"])
    # Check for deprecation of PYTHON min version
    assert len(recorded_warnings) == 1


@pytest.mark.parametrize(
    ("n_reqs", "mocked_version", "requirement_version", "expected_return"),
    [
        pytest.param(
            1,
            "4.3",
            "4.2",
            True,
            id="valid version",
        ),
        pytest.param(
            1,
            "4.3",
            "4.2 # inline comment",
            True,
            id="requirement with inline comment",
        ),
        pytest.param(
            2,
            "4.0",
            "4.2",
            False,
            id="invalid version",
        ),
        pytest.param(
            1,
            None,
            "4.2",
            False,
            id="missing requirement",
        ),
        pytest.param(
            0,
            None,
            None,
            True,
            id="no requirement",
        ),
    ],
)
def test__validate_python_requirements(n_reqs: int, mocked_version: str | None, requirement_version: str | None, expected_return: bool) -> None:
    """
    Running with n_reqs requirements.

    TODO: - check the results
         - not testing for wrongly formatted requirements
    """
    result = {}
    requirements = list(repeat(f"test-dep>={requirement_version}", n_reqs))
    with patch("ansible_collections.arista.avd.plugins.action.verify_requirements.version") as patched_version:
        patched_version.return_value = mocked_version
        if mocked_version is None:
            patched_version.side_effect = PackageNotFoundError()
        ret = _validate_python_requirements(requirements, result)
        assert ret == expected_return


@pytest.mark.parametrize(
    ("running_from_source", "expected_return"),
    [
        pytest.param(False, True, id="pyavd - not running from source"),
        pytest.param(True, True, id="pyavd - running from source"),
    ],
)
def test__validate_python_requirements_pyavd(running_from_source: bool, expected_return: bool) -> None:
    """Testing behavior of the function for pyavd when running from source or not."""
    result = {}
    req = "pyavd==5.3.0"

    requirements = [req]

    with (
        patch("ansible_collections.arista.avd.plugins.action.verify_requirements.version") as patched_version,
        patch("ansible_collections.arista.avd.plugins.action.verify_requirements.RUNNING_FROM_SOURCE", running_from_source),
    ):
        patched_version.return_value = "5.3.0"
        ret = _validate_python_requirements(requirements, result)
        assert ret == expected_return
    python_req_result = result["python_requirements"]
    assert (
        len(python_req_result["valid"]) + len(python_req_result["mismatched"]) + len(python_req_result["not_found"]) + len(python_req_result["parsing_failed"])
        == 1
    )
    if running_from_source:
        assert python_req_result["valid"]["pyavd"]["installed"] == "running from source"
    else:
        assert python_req_result["valid"]["pyavd"]["installed"] == "5.3.0"


@pytest.mark.parametrize(
    ("metadata_file", "content"),
    [
        pytest.param("galaxy.yml", "version: 5.3.0\n", id="galaxy"),
        pytest.param("MANIFEST.json", '{"collection_info": {"version": "5.3.0"}}', id="manifest"),
    ],
)
def test__get_collection_version(metadata_file: str, content: str, tmp_path: Path) -> None:
    """Verify collection version is loaded from galaxy.yml or MANIFEST.json."""
    (tmp_path / metadata_file).write_text(content, encoding="UTF-8")

    assert _get_collection_version(str(tmp_path)) == "5.3.0"


def test__get_collection_version_rejects_unsafe_version(tmp_path: Path) -> None:
    """Verify collection version is validated before it can be logged."""
    (tmp_path / "MANIFEST.json").write_text('{"collection_info": {"version": "5.3.0\\nmalicious"}}', encoding="UTF-8")

    with pytest.raises(ValueError, match=r"Invalid collection version found in collection metadata: 5.3.0\nmalicious"):
        _get_collection_version(str(tmp_path))


@pytest.mark.parametrize(
    ("mocked_running_version", "expected_return"),
    [
        pytest.param("2.16", True, id="valid ansible version"),
        pytest.param("2.14.0", False, id="invalid ansible version"),
    ],
)
def test__validate_ansible_version(mocked_running_version: str, expected_return: bool) -> None:
    """TODO: - check that the requires_ansible is picked up from the correct place."""
    info = {}
    with patch(
        "ansible_collections.arista.avd.plugins.action.verify_requirements._get_collection_metadata",
        return_value={"requires_ansible": ">=2.16.0,<2.22.0"},
    ):
        ret = _validate_ansible_version("arista.avd", mocked_running_version, info)
    assert ret == expected_return


@pytest.mark.parametrize(
    ("n_reqs", "mocked_version", "requirement_version", "expected_return"),
    [
        pytest.param(1, "4.3", ">=4.2", True, id="valid version"),
        pytest.param(1, "4.3", None, True, id="no required version"),
        pytest.param(2, "4.0", ">=4.2", False, id="invalid version"),
        pytest.param(1, None, ">=4.2", False, id="missing requirement"),
        pytest.param(0, None, None, True, id="no requirement"),
    ],
)
def test__validate_ansible_collections(n_reqs: int, mocked_version: str | None, requirement_version: str | None, expected_return: bool) -> None:
    """
    Running with n_reqs requirements in the collection file.

    TODO: - check the results
         - not testing for wrongly formatted collection.yml file
    """
    result = {}

    # Create the metadata based on test input data
    metadata = {}
    if n_reqs > 0:
        metadata["collections"] = list(repeat({"name": "test-collection"}, n_reqs))
        if requirement_version is not None:
            for collection in metadata["collections"]:
                collection["version"] = requirement_version

    with (
        patch("ansible_collections.arista.avd.plugins.action.verify_requirements.Path.open"),
        patch("ansible_collections.arista.avd.plugins.action.verify_requirements.yaml.safe_load") as patched_safe_load,
        patch(
            "ansible_collections.arista.avd.plugins.action.verify_requirements._get_collection_path",
        ) as patched__get_collection_path,
        patch(
            "ansible_collections.arista.avd.plugins.action.verify_requirements._get_collection_version",
        ) as patched__get_collection_version,
        patch(
            "ansible_collections.arista.avd.plugins.action.verify_requirements.open",
        ),
    ):
        patched_safe_load.return_value = metadata
        patched__get_collection_path.return_value = "/collections/foo/bar"
        if mocked_version is None and n_reqs > 0:
            # First call is for arista.avd
            patched__get_collection_path.side_effect = ["/collections/foo/bar", ModuleNotFoundError()]
        patched__get_collection_version.return_value = mocked_version

        ret = _validate_ansible_collections("arista.avd", result)
        assert ret == expected_return


def test__get_running_collection_version_published_install_skips_git(tmp_path: Path, caplog: pytest.LogCaptureFixture) -> None:
    """Verify that when MANIFEST.json is present the collection metadata version is returned."""
    collection_path = tmp_path / "ansible_collections/arista/avd"
    collection_path.mkdir(parents=True)
    (collection_path / "MANIFEST.json").touch()
    result = {}
    with (
        patch("ansible_collections.arista.avd.plugins.action.verify_requirements._get_collection_path") as patched__get_collection_path,
        patch(
            "ansible_collections.arista.avd.plugins.action.verify_requirements._get_collection_version",
        ) as patched__get_collection_version,
        patch("ansible_collections.arista.avd.plugins.action.verify_requirements._get_git_command_output") as patched__get_git_command_output,
    ):
        patched__get_collection_path.return_value = str(collection_path)
        patched__get_collection_version.return_value = "42.0.0"

        with caplog.at_level(logging.DEBUG):
            _get_running_collection_version("dummy", result)

    assert result == {"collection": {"name": "dummy", "path": str(tmp_path / "ansible_collections"), "version": "42.0.0"}}
    patched__get_git_command_output.assert_not_called()
    assert "Published collection detected, returning collection version" in caplog.text


def test__get_running_collection_version_git_not_installed(tmp_path: Path, caplog: pytest.LogCaptureFixture) -> None:
    """Verify that when git is not found in PATH the function returns the collection metadata version."""
    collection_path = tmp_path / "ansible_collections/arista/avd"
    result = {}
    with (
        patch("ansible_collections.arista.avd.plugins.action.verify_requirements.RUNNING_FROM_SOURCE", new=True),
        patch("ansible_collections.arista.avd.plugins.action.verify_requirements._get_collection_path") as patched__get_collection_path,
        patch(
            "ansible_collections.arista.avd.plugins.action.verify_requirements._get_collection_version",
        ) as patched__get_collection_version,
        patch("ansible_collections.arista.avd.plugins.action.verify_requirements.Popen", side_effect=FileNotFoundError),
    ):
        patched__get_collection_path.return_value = str(collection_path)
        patched__get_collection_version.return_value = "42.0.0"

        with caplog.at_level(logging.DEBUG):
            _get_running_collection_version("dummy", result)

    assert result == {"collection": {"name": "dummy", "path": str(tmp_path / "ansible_collections"), "version": "42.0.0"}}
    assert "Could not find 'git' executable, returning collection version" in caplog.text


def test__get_running_collection_version_source_checkout_uses_git(tmp_path: Path) -> None:
    """Verify that an AVD source checkout uses git describe for the running collection version."""
    collection_path = tmp_path / "ansible_collections/arista/avd"
    result = {}
    with (
        patch("ansible_collections.arista.avd.plugins.action.verify_requirements.RUNNING_FROM_SOURCE", new=True),
        patch("ansible_collections.arista.avd.plugins.action.verify_requirements._get_collection_path") as patched__get_collection_path,
        patch(
            "ansible_collections.arista.avd.plugins.action.verify_requirements._get_collection_version",
        ) as patched__get_collection_version,
        patch("ansible_collections.arista.avd.plugins.action.verify_requirements._get_git_command_output") as patched__get_git_command_output,
    ):
        patched__get_collection_path.return_value = str(collection_path)
        patched__get_collection_version.return_value = "42.0.0"
        patched__get_git_command_output.return_value = "v42.0.1-1-gabcdef"

        _get_running_collection_version("dummy", result)

    assert result == {"collection": {"name": "dummy", "path": str(tmp_path / "ansible_collections"), "version": "v42.0.1-1-gabcdef"}}
    patched__get_git_command_output.assert_called_once_with(["git", "describe", "--tags"], str(collection_path))


def test__get_running_collection_version_not_running_from_source_skips_git(tmp_path: Path, caplog: pytest.LogCaptureFixture) -> None:
    """Verify that non-source collections use the collection metadata version."""
    customer_repo_path = tmp_path / "customer"
    collection_path = customer_repo_path / "collections/ansible_collections/arista/avd"
    result = {}
    with (
        patch("ansible_collections.arista.avd.plugins.action.verify_requirements.RUNNING_FROM_SOURCE", new=False),
        patch("ansible_collections.arista.avd.plugins.action.verify_requirements._get_collection_path") as patched__get_collection_path,
        patch(
            "ansible_collections.arista.avd.plugins.action.verify_requirements._get_collection_version",
        ) as patched__get_collection_version,
        patch("ansible_collections.arista.avd.plugins.action.verify_requirements._get_git_command_output") as patched__get_git_command_output,
    ):
        patched__get_collection_path.return_value = str(collection_path)
        patched__get_collection_version.return_value = "42.0.0"

        with caplog.at_level(logging.DEBUG):
            _get_running_collection_version("dummy", result)

    assert result == {"collection": {"name": "dummy", "path": str(customer_repo_path / "collections/ansible_collections"), "version": "42.0.0"}}
    patched__get_git_command_output.assert_not_called()
    assert "AVD is not running from source, returning collection version" in caplog.text
