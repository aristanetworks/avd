# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

import json
import logging
import sys
from importlib.metadata import PackageNotFoundError
from itertools import repeat
from pathlib import Path
from typing import TYPE_CHECKING, NamedTuple
from unittest.mock import MagicMock, patch

import pytest

from ansible_collections.arista.avd.plugins.action.verify_requirements import (
    MIN_PYTHON_SUPPORTED_VERSION,
    ActionModule,
    _check_requirement,
    _get_collection_version,
    _get_git_command_output,
    _get_running_collection_version,
    _validate_ansible_collections,
    _validate_ansible_version,
    _validate_python_requirements,
    _validate_python_version,
    check_running_from_source,
)

if TYPE_CHECKING:
    from collections.abc import Callable

    from ansible.plugins.action import ActionBase

MODULE_PATH = "ansible_collections.arista.avd.plugins.action.verify_requirements"
DEFAULT_TASK_VARS = {
    "ansible_version": {"string": "2.16.0"},
    "ansible_collection_name": "arista.avd",
}


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
    ("mocked_running_version", "deprecated_version", "expected_return"),
    [
        pytest.param(
            "2.16",
            False,
            True,
            id="valid ansible version",
        ),
        pytest.param(
            "2.14.0",
            True,
            False,
            id="invalid ansible version",
        ),
    ],
)
def test__validate_ansible_version(mocked_running_version: str, deprecated_version: bool, expected_return: bool) -> None:
    """TODO: - check that the requires_ansible is picked up from the correct place."""
    info = {}
    result = {}  # As in ansible module result
    ret = _validate_ansible_version("arista.avd", mocked_running_version, info)
    assert ret == expected_return
    if expected_return is True and deprecated_version is True:
        # Check for depreecation of old Ansible versions (Not used right now)
        assert len(result["deprecations"]) == 1


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


# ---------------------------------------------------------------------------
# Short-circuit prevention
# ---------------------------------------------------------------------------


def test__validate_python_requirements_short_circuits_on_first_failure() -> None:
    """Due to the `valid = valid and ...` pattern, only the first failing requirement is evaluated."""
    result = {}
    requirements = ["first-dep>=1.0", "second-dep>=1.0"]
    checked_names: list[str] = []

    def recording_check(req: object, requirements_dict: dict) -> bool:
        checked_names.append(req.name)  # type: ignore[attr-defined]
        requirements_dict["mismatched"][req.name] = {"installed": "0.1", "required_version": ">=1.0"}  # type: ignore[attr-defined]
        return False

    with patch(f"{MODULE_PATH}._check_requirement", side_effect=recording_check):
        ret = _validate_python_requirements(requirements, result)

    assert ret is False
    assert checked_names == ["first-dep"]


# ---------------------------------------------------------------------------
# Duplicate installed-distribution metadata
# ---------------------------------------------------------------------------


def test__check_requirement_duplicate_dist_alternate_satisfies() -> None:
    """When multiple dists exist and an alternate version satisfies the requirement, result is valid."""
    mock_req = MagicMock()
    mock_req.name = "test-dep"
    mock_req.specifier.contains.side_effect = lambda v: v == "4.3"
    mock_req.specifier.__len__ = MagicMock(return_value=1)
    mock_req.specifier.__str__ = MagicMock(return_value=">=4.2")

    requirements_dict: dict = {"valid": {}, "mismatched": {}, "not_found": {}, "parsing_failed": []}

    mock_dist_old = MagicMock()
    mock_dist_old.version = "4.0"
    mock_dist_new = MagicMock()
    mock_dist_new.version = "4.3"

    with (
        patch(f"{MODULE_PATH}.version", return_value="4.0"),
        patch(f"{MODULE_PATH}.Distribution") as mock_dist_cls,
    ):
        mock_dist_cls.discover.return_value = [mock_dist_old, mock_dist_new]
        ret = _check_requirement(mock_req, requirements_dict)

    assert ret is True
    assert "test-dep" in requirements_dict["valid"]
    entry = requirements_dict["valid"]["test-dep"]
    assert entry["installed"] == "4.0"
    assert set(entry["detected_versions"]) == {"4.0", "4.3"}
    assert entry["valid_versions"] == ["4.3"]
    assert "test-dep" not in requirements_dict["mismatched"]


def test__check_requirement_duplicate_dist_none_satisfies() -> None:
    """
    When multiple dists exist and none satisfies the requirement, result is placed in mismatched.

    Note: the function returns True in this case (falls through to `return True`) — a known
    false-positive: the requirement is not met but no failure is signalled.
    """
    mock_req = MagicMock()
    mock_req.name = "test-dep"
    mock_req.specifier.contains.return_value = False
    mock_req.specifier.__len__ = MagicMock(return_value=1)
    mock_req.specifier.__str__ = MagicMock(return_value=">=4.2")

    requirements_dict: dict = {"valid": {}, "mismatched": {}, "not_found": {}, "parsing_failed": []}

    mock_dist1 = MagicMock()
    mock_dist1.version = "4.0"
    mock_dist2 = MagicMock()
    mock_dist2.version = "3.9"

    with (
        patch(f"{MODULE_PATH}.version", return_value="4.0"),
        patch(f"{MODULE_PATH}.Distribution") as mock_dist_cls,
    ):
        mock_dist_cls.discover.return_value = [mock_dist1, mock_dist2]
        ret = _check_requirement(mock_req, requirements_dict)

    assert ret is True
    assert "test-dep" in requirements_dict["mismatched"]
    entry = requirements_dict["mismatched"]["test-dep"]
    assert entry["installed"] == "4.0"
    assert entry["valid_versions"] is None
    assert set(entry["detected_versions"]) == {"4.0", "3.9"}
    assert "test-dep" not in requirements_dict["valid"]


# ---------------------------------------------------------------------------
# _get_git_command_output direct tests
# ---------------------------------------------------------------------------


def test__get_git_command_output_success() -> None:
    """Successful git command returns stripped decoded output."""
    mock_process = MagicMock()
    mock_process.communicate.return_value = (b"v5.3.0-1-gabcdef\n", b"")
    mock_process.returncode = 0

    with patch(f"{MODULE_PATH}.Popen") as mock_popen:
        mock_popen.return_value.__enter__.return_value = mock_process
        mock_popen.return_value.__exit__.return_value = False
        result = _get_git_command_output(["git", "describe", "--tags"], "/some/path")

    assert result == "v5.3.0-1-gabcdef"


def test__get_git_command_output_nonzero_exit() -> None:
    """Non-zero return code results in None."""
    mock_process = MagicMock()
    mock_process.communicate.return_value = (b"", b"")
    mock_process.returncode = 128

    with patch(f"{MODULE_PATH}.Popen") as mock_popen:
        mock_popen.return_value.__enter__.return_value = mock_process
        mock_popen.return_value.__exit__.return_value = False
        result = _get_git_command_output(["git", "describe", "--tags"], "/some/path")

    assert result is None


def test__get_git_command_output_stderr() -> None:
    """Stderr output results in None even when returncode is 0."""
    mock_process = MagicMock()
    mock_process.communicate.return_value = (b"v5.3.0\n", b"fatal: not a git repository\n")
    mock_process.returncode = 0

    with patch(f"{MODULE_PATH}.Popen") as mock_popen:
        mock_popen.return_value.__enter__.return_value = mock_process
        mock_popen.return_value.__exit__.return_value = False
        result = _get_git_command_output(["git", "describe", "--tags"], "/some/path")

    assert result is None


def test__get_git_command_output_missing_executable(caplog: pytest.LogCaptureFixture) -> None:
    """FileNotFoundError when git is absent results in None and logs a debug message."""
    with (
        patch(f"{MODULE_PATH}.Popen", side_effect=FileNotFoundError),
        caplog.at_level(logging.DEBUG),
    ):
        result = _get_git_command_output(["git", "describe", "--tags"], "/some/path")

    assert result is None
    assert "Could not find 'git' executable" in caplog.text


# ---------------------------------------------------------------------------
# check_running_from_source
# ---------------------------------------------------------------------------


def test_check_running_from_source_not_from_source() -> None:
    """Returns False immediately when not running from source."""
    with patch(f"{MODULE_PATH}.RUNNING_FROM_SOURCE", new=False):
        result = check_running_from_source()

    assert result is False


@pytest.mark.parametrize(
    ("schemas_recompiled", "templates_recompiled", "expected_return"),
    [
        pytest.param(True, True, True, id="both-recompiled"),
        pytest.param(True, False, True, id="schemas-only"),
        pytest.param(False, True, True, id="templates-only"),
        pytest.param(False, False, False, id="neither-recompiled"),
    ],
)
def test_check_running_from_source_rebuild_combinations(
    schemas_recompiled: bool,
    templates_recompiled: bool,
    expected_return: bool,
) -> None:
    """check_running_from_source returns True only when schemas or templates were recompiled."""
    mock_check_schemas = MagicMock(return_value=schemas_recompiled)
    mock_rebuild_schemas = MagicMock()
    mock_check_templates = MagicMock(return_value=templates_recompiled)
    mock_recompile_templates = MagicMock()

    mock_check_schemas_mod = MagicMock()
    mock_check_schemas_mod.check_schemas = mock_check_schemas
    mock_check_schemas_mod.rebuild_schemas = mock_rebuild_schemas

    mock_compile_templates_mod = MagicMock()
    mock_compile_templates_mod.check_templates = mock_check_templates
    mock_compile_templates_mod.recompile_templates = mock_recompile_templates

    with (
        patch(f"{MODULE_PATH}.RUNNING_FROM_SOURCE", new=True),
        patch(f"{MODULE_PATH}.DISPLAY"),
        patch.dict(
            sys.modules,
            {
                "schema_tools": MagicMock(),
                "schema_tools.check_schemas": mock_check_schemas_mod,
                "schema_tools.compile_templates": mock_compile_templates_mod,
            },
        ),
    ):
        result = check_running_from_source()

    assert result is expected_return
    if schemas_recompiled:
        mock_rebuild_schemas.assert_called_once()
    else:
        mock_rebuild_schemas.assert_not_called()
    if templates_recompiled:
        mock_recompile_templates.assert_called_once()
    else:
        mock_recompile_templates.assert_not_called()


# ---------------------------------------------------------------------------
# _get_collection_version edge cases
# ---------------------------------------------------------------------------


def test__get_collection_version_missing_both_files(tmp_path: Path) -> None:
    """When both galaxy.yml and MANIFEST.json are absent, FileNotFoundError is raised."""
    with pytest.raises(FileNotFoundError):
        _get_collection_version(str(tmp_path))


def test__get_collection_version_malformed_manifest(tmp_path: Path) -> None:
    """When MANIFEST.json contains invalid JSON, json.JSONDecodeError is raised."""
    (tmp_path / "MANIFEST.json").write_text("this is not valid json", encoding="UTF-8")
    with pytest.raises(json.JSONDecodeError):
        _get_collection_version(str(tmp_path))


def test__get_collection_version_versionless_metadata(tmp_path: Path) -> None:
    """When galaxy.yml has no 'version' key, KeyError is raised."""
    (tmp_path / "galaxy.yml").write_text("name: test-collection\n", encoding="UTF-8")
    with pytest.raises(KeyError):
        _get_collection_version(str(tmp_path))


# ---------------------------------------------------------------------------
# Isolated ActionModule.main() tests
# ---------------------------------------------------------------------------


def _mock_get_running_collection_version(collection_name: str, result: dict) -> None:
    result["collection"] = {"name": collection_name, "version": "5.3.0", "path": "/collections/ansible_collections"}


def test_action_module_main_missing_packaging(action_module: "Callable[..., ActionBase]") -> None:
    """When HAS_PACKAGING is False, main() raises ImportError."""
    module = action_module(ActionModule, task_args={"requirements": []})
    with patch(f"{MODULE_PATH}.HAS_PACKAGING", new=False), pytest.raises(ImportError, match="packaging is required"):
        module.main(task_vars=DEFAULT_TASK_VARS)


def test_action_module_main_validator_failure(action_module: "Callable[..., ActionBase]") -> None:
    """When a validator returns False, result['failed'] is True and the error message is set."""
    module = action_module(ActionModule, task_args={"requirements": []})

    with (
        patch(f"{MODULE_PATH}._get_running_collection_version", side_effect=_mock_get_running_collection_version),
        patch(f"{MODULE_PATH}.check_running_from_source", return_value=False),
        patch(f"{MODULE_PATH}._validate_python_version", return_value=False),
        patch(f"{MODULE_PATH}._validate_python_requirements", return_value=True),
        patch(f"{MODULE_PATH}._validate_ansible_version", return_value=True),
        patch(f"{MODULE_PATH}._validate_ansible_collections", return_value=True),
        patch(f"{MODULE_PATH}.DISPLAY"),
        patch(f"{MODULE_PATH}.RUNNING_FROM_SOURCE", new=False),
    ):
        module.main(task_vars=DEFAULT_TASK_VARS)

    assert module.result["failed"] is True
    assert module.result.get("msg") == "If it is a false positive, set 'avd_ignore_requirements=True'."


def test_action_module_main_source_changes(action_module: "Callable[..., ActionBase]") -> None:
    """When check_running_from_source returns True, result['changed'] is True."""
    module = action_module(ActionModule, task_args={"requirements": []})

    with (
        patch(f"{MODULE_PATH}._get_running_collection_version", side_effect=_mock_get_running_collection_version),
        patch(f"{MODULE_PATH}.check_running_from_source", return_value=True),
        patch(f"{MODULE_PATH}._validate_python_version", return_value=True),
        patch(f"{MODULE_PATH}._validate_python_requirements", return_value=True),
        patch(f"{MODULE_PATH}._validate_ansible_version", return_value=True),
        patch(f"{MODULE_PATH}._validate_ansible_collections", return_value=True),
        patch(f"{MODULE_PATH}.DISPLAY"),
        patch(f"{MODULE_PATH}.RUNNING_FROM_SOURCE", new=False),
    ):
        module.main(task_vars=DEFAULT_TASK_VARS)

    assert module.result.get("changed") is True
    assert module.result["failed"] is False


def test_action_module_main_success(action_module: "Callable[..., ActionBase]") -> None:
    """When all validators pass and avd_ignore_requirements is False, result['failed'] is False."""
    module = action_module(ActionModule, task_args={"requirements": ["test-dep>=1.0"]})

    with (
        patch(f"{MODULE_PATH}._get_running_collection_version", side_effect=_mock_get_running_collection_version),
        patch(f"{MODULE_PATH}.check_running_from_source", return_value=False),
        patch(f"{MODULE_PATH}._validate_python_version", return_value=True),
        patch(f"{MODULE_PATH}._validate_python_requirements", return_value=True),
        patch(f"{MODULE_PATH}._validate_ansible_version", return_value=True),
        patch(f"{MODULE_PATH}._validate_ansible_collections", return_value=True),
        patch(f"{MODULE_PATH}.DISPLAY"),
        patch(f"{MODULE_PATH}.RUNNING_FROM_SOURCE", new=False),
    ):
        module.main(task_vars=DEFAULT_TASK_VARS)

    assert module.result["failed"] is False
    assert "msg" not in module.result
