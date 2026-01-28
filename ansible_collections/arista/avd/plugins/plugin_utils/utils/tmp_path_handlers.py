# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import tempfile
from functools import cache
from pathlib import Path
from typing import Literal

from ansible import constants as ansible_constants

TEMPLATED_DIR_NAME = "templated"
VALIDATED_DIR_NAME = "validated"

EOS_DESIGNS_FACTS_FILENAME = "eos_designs_facts.json"

AVD_TMP_DIR_MODE = 0o700


def get_tmp_path(avd_tmp_dir: str | None = None) -> Path:
    """
    Return a Path object for the AVD temporary directory.

    The directory will be created if missing with 700 permissions.

    The location is determined in the following order:
    1. If `avd_tmp_dir` is provided, use it directly.
    2. An "arista_avd" subdirectory under Ansible "local_tmp" directory (cleaned up by Ansible after the play).
    3. Fall back to "arista_avd_<random>" directory under the system temp directory.

    Args:
        avd_tmp_dir: Optional path to use as the AVD temporary directory.

    Returns:
        Path object pointing to the AVD temporary directory.
    """
    if avd_tmp_dir is not None:
        tmp_path = Path(avd_tmp_dir)
        _create_avd_tmp_dir(tmp_path)
        return tmp_path

    # Return the same tmp_path as last time unless Ansible cleaned it up in the meanwhile. Ansible maintains a separate local_tmp folder per play.
    tmp_path = _cached_tmp_path()
    if not tmp_path.exists():
        _cached_tmp_path.cache_clear()
        return _cached_tmp_path()
    return tmp_path


def _create_avd_tmp_dir(path: Path) -> None:
    """
    Create the AVD temporary directory with 700 permissions if it doesn't exist.

    Args:
        path: The directory path to create.

    Raises:
        OSError: If directory creation fails.
    """
    if path.exists():
        return

    try:
        path.mkdir(mode=AVD_TMP_DIR_MODE, parents=True)
    except OSError as e:
        msg = f"Unable to create AVD temporary directory {path}: {e}"
        raise type(e)(msg) from e


@cache
def _cached_tmp_path() -> Path:
    """Create and return a new tmp_path. Cached for next time."""
    if hasattr(ansible_constants, "DEFAULT_LOCAL_TMP"):
        # If using Ansible tmp dir, append our subdir to keep things organized.
        tmp_path = Path(ansible_constants.DEFAULT_LOCAL_TMP) / "arista_avd"
    else:
        tmp_path = Path(tempfile.mkdtemp(prefix="arista_avd_"))

    _create_avd_tmp_dir(tmp_path)
    return tmp_path


def get_eos_designs_facts_path(avd_tmp_dir: str | None = None) -> Path:
    """
    Return the Path object for the shared eos_designs facts file.

    This file contains facts for all devices in the fabric, written by `eos_designs_facts`
    and read by `eos_designs_structured_config`.

    The parent directory is created if it doesn't exist.

    Args:
        avd_tmp_dir: Optional path to use as the AVD temporary directory.

    Returns:
        Path object pointing to the eos_designs facts JSON file.
    """
    base_tmp_path = get_tmp_path(avd_tmp_dir)
    eos_designs_path = base_tmp_path / "eos_designs"

    # Ensure directory exist.
    eos_designs_path.mkdir(parents=True, exist_ok=True)

    return eos_designs_path / EOS_DESIGNS_FACTS_FILENAME


def get_role_tmp_paths(role_name: Literal["eos_designs", "eos_cli_config_gen"], avd_tmp_dir: str | None = None) -> tuple[Path, Path]:
    """
    Return the temporary paths for 'templated' and 'validated' directories to be used by a specific Ansible role.

    This function ensures that the directories exist before returning.

    Args:
        role_name: The role name. Either 'eos_designs' or 'eos_cli_config_gen'.
        avd_tmp_dir: Optional path to use as the AVD temporary directory.

    Returns:
        A tuple of Path objects containing (templated_path, validated_path).
    """
    base_tmp_path = get_tmp_path(avd_tmp_dir)
    role_path = base_tmp_path / role_name

    templated_path = role_path / TEMPLATED_DIR_NAME
    validated_path = role_path / VALIDATED_DIR_NAME

    # Ensure directories exist. parents=True handles the creation of the 'role_name' intermediate dir if needed.
    templated_path.mkdir(parents=True, exist_ok=True)
    validated_path.mkdir(parents=True, exist_ok=True)

    return templated_path, validated_path
