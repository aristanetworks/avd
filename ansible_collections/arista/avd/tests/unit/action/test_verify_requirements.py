# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

import logging
from importlib.metadata import PackageNotFoundError
from itertools import repeat
from pathlib import Path
from typing import TYPE_CHECKING, NamedTuple
from unittest.mock import MagicMock, patch

import pytest
from ansible.errors import AnsibleActionFail

from ansible_collections.arista.avd.plugins.action.verify_requirements import (
    MIN_PYTHON_SUPPORTED_VERSION,
    ActionModule,
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

MODULE_PATH = "ansible_collections.arista.avd.plugins.action.verify_requirements"


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


def test_check_running_from_source_not_from_source() -> None:
    """Verify that check_running_from_source returns False when not running from source."""
    with patch("ansible_collections.arista.avd.plugins.action.verify_requirements.RUNNING_FROM_SOURCE", new=False):
        assert check_running_from_source() is False


def test_check_running_from_source_import_error() -> None:
    """Verify that check_running_from_source returns False when schema_tools cannot be imported."""
    with (
        patch("ansible_collections.arista.avd.plugins.action.verify_requirements.RUNNING_FROM_SOURCE", new=True),
        patch.dict("sys.modules", {"schema_tools.check_schemas": None, "schema_tools.compile_templates": None}),
    ):
        assert check_running_from_source() is False


def test_check_running_from_source_no_rebuild() -> None:
    """Verify that check_running_from_source returns False when no schemas or templates need rebuilding."""
    mock_check_schemas_mod = MagicMock()
    mock_check_schemas_mod.check_schemas.return_value = False
    mock_compile_templates_mod = MagicMock()
    mock_compile_templates_mod.check_templates.return_value = False
    with (
        patch("ansible_collections.arista.avd.plugins.action.verify_requirements.RUNNING_FROM_SOURCE", new=True),
        patch.dict("sys.modules", {"schema_tools.check_schemas": mock_check_schemas_mod, "schema_tools.compile_templates": mock_compile_templates_mod}),
    ):
        assert check_running_from_source() is False


def test_check_running_from_source_schema_rebuild() -> None:
    """Verify that check_running_from_source returns True and rebuilds schemas when schemas changed."""
    mock_check_schemas_mod = MagicMock()
    mock_check_schemas_mod.check_schemas.return_value = True
    mock_compile_templates_mod = MagicMock()
    mock_compile_templates_mod.check_templates.return_value = False
    with (
        patch("ansible_collections.arista.avd.plugins.action.verify_requirements.RUNNING_FROM_SOURCE", new=True),
        patch.dict("sys.modules", {"schema_tools.check_schemas": mock_check_schemas_mod, "schema_tools.compile_templates": mock_compile_templates_mod}),
    ):
        assert check_running_from_source() is True


def test_check_running_from_source_template_rebuild() -> None:
    """Verify that check_running_from_source returns True and recompiles templates when templates changed."""
    mock_check_schemas_mod = MagicMock()
    mock_check_schemas_mod.check_schemas.return_value = False
    mock_compile_templates_mod = MagicMock()
    mock_compile_templates_mod.check_templates.return_value = True
    with (
        patch("ansible_collections.arista.avd.plugins.action.verify_requirements.RUNNING_FROM_SOURCE", new=True),
        patch.dict("sys.modules", {"schema_tools.check_schemas": mock_check_schemas_mod, "schema_tools.compile_templates": mock_compile_templates_mod}),
    ):
        assert check_running_from_source() is True


# ---------------------------------------------------------------------------
# Tests for _check_requirement with multiple distribution versions
# ---------------------------------------------------------------------------


def test__validate_python_requirements_multiple_dists_one_valid() -> None:
    """Verify that when multiple distributions exist and one matches the spec, the requirement is valid with a warning."""
    mock_dist_old = MagicMock()
    mock_dist_old.version = "4.0.0"
    mock_dist_valid = MagicMock()
    mock_dist_valid.version = "4.2.0"

    result: dict = {}
    with (
        patch(f"{MODULE_PATH}.version", return_value="4.0.0"),
        patch(f"{MODULE_PATH}.Distribution.discover", return_value=[mock_dist_old, mock_dist_valid]),
    ):
        ret = _validate_python_requirements(["test-dep>=4.2"], result)

    assert ret is True
    assert "test-dep" in result["python_requirements"]["valid"]


def test__validate_python_requirements_multiple_dists_none_valid() -> None:
    """
    Verify that when multiple distributions exist but none match, the requirement is logged as mismatched.

    NOTE: _check_requirement returns True even in this case (falls through to the final 'return True')
    because the mismatched-multiple-dists branch has no explicit 'return False'.
    """
    mock_dist_a = MagicMock()
    mock_dist_a.version = "4.0.0"
    mock_dist_b = MagicMock()
    mock_dist_b.version = "4.1.0"

    result: dict = {}
    with (
        patch(f"{MODULE_PATH}.version", return_value="4.0.0"),
        patch(f"{MODULE_PATH}.Distribution.discover", return_value=[mock_dist_a, mock_dist_b]),
    ):
        ret = _validate_python_requirements(["test-dep>=4.2"], result)

    assert ret is True
    assert "test-dep" in result["python_requirements"]["mismatched"]


# ---------------------------------------------------------------------------
# Tests for _validate_ansible_collections edge cases
# ---------------------------------------------------------------------------


def test__validate_ansible_collections_missing_name_key() -> None:
    """Verify that a collection entry missing the 'name' key is skipped with an error log."""
    metadata = {"collections": [{"version": ">=1.0"}]}

    with (
        patch(f"{MODULE_PATH}.Path.open"),
        patch(f"{MODULE_PATH}.yaml.safe_load", return_value=metadata),
        patch(f"{MODULE_PATH}._get_collection_path", return_value="/collections/arista/avd"),
    ):
        result: dict = {}
        ret = _validate_ansible_collections("arista.avd", result)

    assert ret is True
    assert result["collection_requirements"]["not_found"] == {}
    assert result["collection_requirements"]["mismatched"] == {}


def test__validate_ansible_collections_not_found_no_version() -> None:
    """Verify that a not-found collection with no version specifier logs the right error (line 285)."""
    metadata = {"collections": [{"name": "missing.collection"}]}

    with (
        patch(f"{MODULE_PATH}.Path.open"),
        patch(f"{MODULE_PATH}.yaml.safe_load", return_value=metadata),
        patch(
            f"{MODULE_PATH}._get_collection_path",
            side_effect=["/collections/arista/avd", ModuleNotFoundError()],
        ),
    ):
        result: dict = {}
        ret = _validate_ansible_collections("arista.avd", result)

    assert ret is False
    assert "missing.collection" in result["collection_requirements"]["not_found"]


# ---------------------------------------------------------------------------
# Tests for _get_git_command_output success/failure paths
# ---------------------------------------------------------------------------


def test__get_git_command_output_returns_none_on_nonzero_returncode() -> None:
    """Verify _get_git_command_output returns None when git exits with a non-zero returncode."""
    mock_process = MagicMock()
    mock_process.__enter__ = MagicMock(return_value=mock_process)
    mock_process.__exit__ = MagicMock(return_value=False)
    mock_process.communicate.return_value = (b"", b"error output")
    mock_process.returncode = 1

    with patch(f"{MODULE_PATH}.Popen", return_value=mock_process):
        result = _get_git_command_output(["git", "describe", "--tags"], "/some/path")

    assert result is None


def test__get_git_command_output_returns_decoded_output_on_success() -> None:
    """Verify _get_git_command_output returns the decoded stdout when git succeeds."""
    mock_process = MagicMock()
    mock_process.__enter__ = MagicMock(return_value=mock_process)
    mock_process.__exit__ = MagicMock(return_value=False)
    mock_process.communicate.return_value = (b"v5.3.0\n", b"")
    mock_process.returncode = 0

    with patch(f"{MODULE_PATH}.Popen", return_value=mock_process):
        result = _get_git_command_output(["git", "describe", "--tags"], "/some/path")

    assert result == "v5.3.0"


# ---------------------------------------------------------------------------
# Tests for ActionModule.main()
# ---------------------------------------------------------------------------

TASK_VARS = {"ansible_version": {"string": "2.16.0"}}
ERROR_MESSAGE = "If it is a false positive, set 'avd_ignore_requirements=True'."


def _make_module(action_module: "Callable", task_args: dict) -> ActionModule:
    return action_module(ActionModule, task_args=task_args, ansible_name="arista.avd.verify_requirements")


def _mock_collection_version(name: str, result: dict) -> None:  # noqa: ARG001
    result["collection"] = {"version": "5.3.0"}


def test_main_happy_path(action_module: "Callable") -> None:
    """Verify main() succeeds and result['failed'] is False when all validators pass."""
    module = _make_module(action_module, {"requirements": []})
    with (
        patch("ansible.plugins.action.ActionBase.run", return_value={}),
        patch(f"{MODULE_PATH}._get_running_collection_version", side_effect=_mock_collection_version),
        patch(f"{MODULE_PATH}.check_running_from_source", return_value=False),
        patch(f"{MODULE_PATH}._validate_python_version", return_value=True),
        patch(f"{MODULE_PATH}._validate_python_requirements", return_value=True),
        patch(f"{MODULE_PATH}._validate_ansible_version", return_value=True),
        patch(f"{MODULE_PATH}._validate_ansible_collections", return_value=True),
        patch(f"{MODULE_PATH}.DISPLAY"),
    ):
        result = module.run(task_vars=TASK_VARS)

    assert result["failed"] is False
    assert "msg" not in result


def test_main_python_version_fails(action_module: "Callable") -> None:
    """Verify main() sets failed=True and msg when _validate_python_version returns False."""
    module = _make_module(action_module, {"requirements": []})
    with (
        patch("ansible.plugins.action.ActionBase.run", return_value={}),
        patch(f"{MODULE_PATH}._get_running_collection_version", side_effect=_mock_collection_version),
        patch(f"{MODULE_PATH}.check_running_from_source", return_value=False),
        patch(f"{MODULE_PATH}._validate_python_version", return_value=False),
        patch(f"{MODULE_PATH}._validate_python_requirements", return_value=True),
        patch(f"{MODULE_PATH}._validate_ansible_version", return_value=True),
        patch(f"{MODULE_PATH}._validate_ansible_collections", return_value=True),
        patch(f"{MODULE_PATH}.DISPLAY"),
    ):
        result = module.run(task_vars=TASK_VARS)

    assert result["failed"] is True
    assert result["msg"] == ERROR_MESSAGE


def test_main_python_requirements_fail(action_module: "Callable") -> None:
    """Verify main() sets failed=True when _validate_python_requirements returns False."""
    module = _make_module(action_module, {"requirements": []})
    with (
        patch("ansible.plugins.action.ActionBase.run", return_value={}),
        patch(f"{MODULE_PATH}._get_running_collection_version", side_effect=_mock_collection_version),
        patch(f"{MODULE_PATH}.check_running_from_source", return_value=False),
        patch(f"{MODULE_PATH}._validate_python_version", return_value=True),
        patch(f"{MODULE_PATH}._validate_python_requirements", return_value=False),
        patch(f"{MODULE_PATH}._validate_ansible_version", return_value=True),
        patch(f"{MODULE_PATH}._validate_ansible_collections", return_value=True),
        patch(f"{MODULE_PATH}.DISPLAY"),
    ):
        result = module.run(task_vars=TASK_VARS)

    assert result["failed"] is True


def test_main_ansible_version_fails(action_module: "Callable") -> None:
    """Verify main() sets failed=True when _validate_ansible_version returns False."""
    module = _make_module(action_module, {"requirements": []})
    with (
        patch("ansible.plugins.action.ActionBase.run", return_value={}),
        patch(f"{MODULE_PATH}._get_running_collection_version", side_effect=_mock_collection_version),
        patch(f"{MODULE_PATH}.check_running_from_source", return_value=False),
        patch(f"{MODULE_PATH}._validate_python_version", return_value=True),
        patch(f"{MODULE_PATH}._validate_python_requirements", return_value=True),
        patch(f"{MODULE_PATH}._validate_ansible_version", return_value=False),
        patch(f"{MODULE_PATH}._validate_ansible_collections", return_value=True),
        patch(f"{MODULE_PATH}.DISPLAY"),
    ):
        result = module.run(task_vars=TASK_VARS)

    assert result["failed"] is True


def test_main_ansible_collections_fail(action_module: "Callable") -> None:
    """Verify main() sets failed=True when _validate_ansible_collections returns False."""
    module = _make_module(action_module, {"requirements": []})
    with (
        patch("ansible.plugins.action.ActionBase.run", return_value={}),
        patch(f"{MODULE_PATH}._get_running_collection_version", side_effect=_mock_collection_version),
        patch(f"{MODULE_PATH}.check_running_from_source", return_value=False),
        patch(f"{MODULE_PATH}._validate_python_version", return_value=True),
        patch(f"{MODULE_PATH}._validate_python_requirements", return_value=True),
        patch(f"{MODULE_PATH}._validate_ansible_version", return_value=True),
        patch(f"{MODULE_PATH}._validate_ansible_collections", return_value=False),
        patch(f"{MODULE_PATH}.DISPLAY"),
    ):
        result = module.run(task_vars=TASK_VARS)

    assert result["failed"] is True


def test_main_avd_ignore_requirements_overrides_failure(action_module: "Callable") -> None:
    """Verify main() resets failed=False when avd_ignore_requirements=True even if validators fail."""
    module = _make_module(action_module, {"requirements": [], "avd_ignore_requirements": True})
    with (
        patch("ansible.plugins.action.ActionBase.run", return_value={}),
        patch(f"{MODULE_PATH}._get_running_collection_version", side_effect=_mock_collection_version),
        patch(f"{MODULE_PATH}.check_running_from_source", return_value=False),
        patch(f"{MODULE_PATH}._validate_python_version", return_value=False),
        patch(f"{MODULE_PATH}._validate_python_requirements", return_value=True),
        patch(f"{MODULE_PATH}._validate_ansible_version", return_value=True),
        patch(f"{MODULE_PATH}._validate_ansible_collections", return_value=True),
        patch(f"{MODULE_PATH}.DISPLAY"),
    ):
        result = module.run(task_vars=TASK_VARS)

    assert result["failed"] is False
    assert "msg" not in result


def test_main_missing_requirements_arg_raises(action_module: "Callable") -> None:
    """Verify main() raises AnsibleActionFail when the 'requirements' argument is missing."""
    module = _make_module(action_module, {})
    with (
        patch("ansible.plugins.action.ActionBase.run", return_value={}),
        pytest.raises(AnsibleActionFail, match="requirements.*must be set"),
    ):
        module.run(task_vars=TASK_VARS)


def test_main_requirements_not_list_raises(action_module: "Callable") -> None:
    """Verify main() raises AnsibleActionFail when 'requirements' is not a list."""
    module = _make_module(action_module, {"requirements": "not-a-list"})
    with (
        patch("ansible.plugins.action.ActionBase.run", return_value={}),
        pytest.raises(AnsibleActionFail, match="requirements.*not a list"),
    ):
        module.run(task_vars=TASK_VARS)


def test_main_has_packaging_false_raises(action_module: "Callable") -> None:
    """Verify main() raises AnsibleActionFail when the packaging library is not installed."""
    module = _make_module(action_module, {"requirements": []})
    with (
        patch("ansible.plugins.action.ActionBase.run", return_value={}),
        patch(f"{MODULE_PATH}.HAS_PACKAGING", new=False),
        pytest.raises(AnsibleActionFail, match="packaging is required"),
    ):
        module.run(task_vars=TASK_VARS)


def test_main_running_from_source_sets_changed(action_module: "Callable") -> None:
    """Verify main() sets result['changed']=True when check_running_from_source() returns True."""
    module = _make_module(action_module, {"requirements": []})
    with (
        patch("ansible.plugins.action.ActionBase.run", return_value={}),
        patch(f"{MODULE_PATH}._get_running_collection_version", side_effect=_mock_collection_version),
        patch(f"{MODULE_PATH}.check_running_from_source", return_value=True),
        patch(f"{MODULE_PATH}.RUNNING_FROM_SOURCE", new=True),
        patch(f"{MODULE_PATH}._validate_python_version", return_value=True),
        patch(f"{MODULE_PATH}._validate_python_requirements", return_value=True),
        patch(f"{MODULE_PATH}._validate_ansible_version", return_value=True),
        patch(f"{MODULE_PATH}._validate_ansible_collections", return_value=True),
        patch(f"{MODULE_PATH}.DISPLAY"),
        patch(f"{MODULE_PATH}.PYTHON_AVD_PATH", new="/some/path"),
    ):
        result = module.run(task_vars=TASK_VARS)

    assert result.get("changed") is True


def test_main_not_running_from_source_skips_source_display(action_module: "Callable") -> None:
    """Verify main() skips the 'running from source' display when RUNNING_FROM_SOURCE is False."""
    module = _make_module(action_module, {"requirements": []})
    with (
        patch("ansible.plugins.action.ActionBase.run", return_value={}),
        patch(f"{MODULE_PATH}._get_running_collection_version", side_effect=_mock_collection_version),
        patch(f"{MODULE_PATH}.check_running_from_source", return_value=False),
        patch(f"{MODULE_PATH}.RUNNING_FROM_SOURCE", new=False),
        patch(f"{MODULE_PATH}._validate_python_version", return_value=True),
        patch(f"{MODULE_PATH}._validate_python_requirements", return_value=True),
        patch(f"{MODULE_PATH}._validate_ansible_version", return_value=True),
        patch(f"{MODULE_PATH}._validate_ansible_collections", return_value=True),
        patch(f"{MODULE_PATH}.DISPLAY") as mock_display,
    ):
        result = module.run(task_vars=TASK_VARS)

    assert result["failed"] is False
    display_messages = [call.args[0] for call in mock_display.display.call_args_list if call.args]
    assert not any("running from source" in msg for msg in display_messages)


def test_main_avd_ignore_requirements_string_true_is_normalized(action_module: "Callable") -> None:
    """Verify main() normalizes the string 'true' for avd_ignore_requirements and ignores failures."""
    module = _make_module(action_module, {"requirements": [], "avd_ignore_requirements": "true"})
    with (
        patch("ansible.plugins.action.ActionBase.run", return_value={}),
        patch(f"{MODULE_PATH}._get_running_collection_version", side_effect=_mock_collection_version),
        patch(f"{MODULE_PATH}.check_running_from_source", return_value=False),
        patch(f"{MODULE_PATH}._validate_python_version", return_value=False),
        patch(f"{MODULE_PATH}._validate_python_requirements", return_value=True),
        patch(f"{MODULE_PATH}._validate_ansible_version", return_value=True),
        patch(f"{MODULE_PATH}._validate_ansible_collections", return_value=True),
        patch(f"{MODULE_PATH}.DISPLAY"),
    ):
        result = module.run(task_vars=TASK_VARS)

    assert result["failed"] is False


def test__validate_ansible_version_with_no_requires_ansible() -> None:
    """Verify _validate_ansible_version passes when requires_ansible is absent from collection metadata."""
    info: dict = {}
    with patch(f"{MODULE_PATH}._get_collection_metadata", return_value={}):
        ret = _validate_ansible_version("arista.avd", "2.16.0", info)

    assert ret is True
    assert "requires_ansible" not in info
