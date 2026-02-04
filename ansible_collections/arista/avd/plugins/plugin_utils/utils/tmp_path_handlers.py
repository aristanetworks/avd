# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

from pathlib import Path
from typing import Literal

TEMPLATED_DIR_NAME = "templated"
VALIDATED_DIR_NAME = "validated"

EOS_DESIGNS_FACTS_FILENAME = "eos_designs_facts.json"

AVD_TMP_DIR_MODE = 0o700


def _get_tmp_path(tmp_dir: str) -> Path:
    """
    Return a Path object for the AVD temporary directory.

    The directory will be created with 700 permissions if it doesn't exist.

    Args:
        tmp_dir: Path to use as the AVD temporary directory.

    Returns:
        Path object pointing to the AVD temporary directory.
    """
    path = Path(tmp_dir)
    if not path.exists():
        try:
            path.mkdir(mode=AVD_TMP_DIR_MODE, parents=True)
        except OSError as e:
            msg = f"Unable to create AVD temporary directory {path}: {e}"
            raise type(e)(msg) from e
    return path


def get_eos_designs_facts_path(tmp_dir: str) -> Path:
    """
    Return the Path object for the shared eos_designs facts file.

    This file contains facts for all devices in the fabric, written by `eos_designs_facts`
    and read by `eos_designs_structured_config`.

    The parent directory is created if it doesn't exist.

    Args:
        tmp_dir: Path to use as the AVD temporary directory.

    Returns:
        Path object pointing to the eos_designs facts JSON file.
    """
    tmp_path = _get_tmp_path(tmp_dir)
    eos_designs_path = tmp_path / "eos_designs"

    # Ensure directory exist.
    eos_designs_path.mkdir(parents=True, exist_ok=True)

    return eos_designs_path / EOS_DESIGNS_FACTS_FILENAME


def get_role_tmp_paths(role_name: Literal["eos_designs", "eos_cli_config_gen"], tmp_dir: str) -> tuple[Path, Path]:
    """
    Return the temporary paths for 'templated' and 'validated' directories to be used by a specific Ansible role.

    This function ensures that the directories exist before returning.

    Args:
        role_name: The role name. Either 'eos_designs' or 'eos_cli_config_gen'.
        tmp_dir: Path to use as the AVD temporary directory.

    Returns:
        A tuple of Path objects containing (templated_path, validated_path).
    """
    tmp_path = _get_tmp_path(tmp_dir)
    role_path = tmp_path / role_name

    templated_path = role_path / TEMPLATED_DIR_NAME
    validated_path = role_path / VALIDATED_DIR_NAME

    # Ensure directories exist. parents=True handles the creation of the 'role_name' intermediate dir if needed.
    templated_path.mkdir(parents=True, exist_ok=True)
    validated_path.mkdir(parents=True, exist_ok=True)

    return templated_path, validated_path
