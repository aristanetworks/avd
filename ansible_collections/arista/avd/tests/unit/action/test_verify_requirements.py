__metaclass__ = type

import importlib
from collections import namedtuple
from unittest.mock import patch

import pytest

from ansible_collections.arista.avd.plugins.action.verify_requirements import (
    MIN_PYTHON_SUPPORTED_VERSION,
    _validate_python_dependencies,
    _validate_python_version,
)


@pytest.mark.parametrize(
    "mocked_version, expected_return",
    [
        (
            (2, 2, 2, "final", 0),
            False,
        ),
        (
            (MIN_PYTHON_SUPPORTED_VERSION[0], MIN_PYTHON_SUPPORTED_VERSION[1], 42, "final", 0),
            True,
        ),
    ],
)
def test__validate_python_version(mocked_version, expected_return):
    """
    TODO - could add the expected stderr
    """
    result = {}
    version_info = namedtuple("version_info", "major minor micro releaselevel serial")
    with patch("ansible_collections.arista.avd.plugins.action.verify_requirements.sys") as mocked_sys:
        mocked_sys.version_info = version_info(*mocked_version)
        ret = _validate_python_version(result)
    assert ret == expected_return
    assert result["python_version_info"] == {
        "major": mocked_version[0],
        "minor": mocked_version[1],
        "micro": mocked_version[2],
        "releaselevel": mocked_version[3],
        "serial": mocked_version[4],
    }
    assert bool(result["python_path"])


@pytest.mark.parametrize(
    "n_deps, mocked_version, requirement_version, expected_return",
    [
        pytest.param(
            1,
            "4.3",
            "4.2",
            True,
            id="valid version",
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
            id="missing dependency",
        ),
        pytest.param(
            0,
            None,
            None,
            True,
            id="no dependency",
        ),
    ],
)
def test__validate_python_dependencies(n_deps, mocked_version, requirement_version, expected_return):
    """
    Running with n_deps dependencies

    TODO - check the results
         - not testing for wrongly formated dependencies
    """
    result = {}
    dependencies = [f"test-dep>={requirement_version}" for _ in range(n_deps)]  # pylint: disable=disallowed-name
    print(dependencies)
    with patch("ansible_collections.arista.avd.plugins.action.verify_requirements.importlib.metadata.version") as patched_version:
        patched_version.return_value = mocked_version
        if mocked_version is None:
            patched_version.side_effect = importlib.metadata.PackageNotFoundError()
        ret = _validate_python_dependencies(dependencies, result)
        assert ret == expected_return
