# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from pathlib import Path
from typing import Literal

TEMPLATED_DIR_NAME = "templated"
VALIDATED_DIR_NAME = "validated"

EOS_DESIGNS_FACTS_FILENAME = "eos_designs_facts.json"

AVD_TMP_DIR_MODE = 0o700


def _get_base_tmp_path(tmp_dir: str) -> Path:
    """
    Return a Path object for the base AVD temporary directory.

    The directory will be created if missing with 700 permissions.

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


def get_eos_designs_facts_path(tmp_dir: str, clean: bool = False) -> Path:
    """
    Return the Path object for the shared eos_designs facts file.

    This file contains facts for all devices in the fabric, written by `eos_designs_facts`
    and read by `eos_designs_structured_config`.

    The parent directory is created if it doesn't exist.

    Args:
        tmp_dir: Path to use as the AVD temporary directory.
        clean: If True, remove the file if it exists before returning.

    Returns:
        Path object pointing to the eos_designs facts JSON file.
    """
    base_tmp_path = _get_base_tmp_path(tmp_dir)
    eos_designs_path = base_tmp_path / "eos_designs"
    eos_designs_facts_path = eos_designs_path / EOS_DESIGNS_FACTS_FILENAME

    # Ensure directory exists.
    # Clean file if requested.
    if eos_designs_facts_path.exists() and clean:
        eos_designs_facts_path.unlink()
    else:
        eos_designs_path.mkdir(parents=True, exist_ok=True)

    return eos_designs_facts_path


def get_role_tmp_paths(role_name: Literal["eos_designs", "eos_cli_config_gen"], tmp_dir: str, clean: bool = False) -> tuple[Path, Path]:
    """
    Return the temporary paths for 'templated' and 'validated' directories to be used by a specific Ansible role.

    This function ensures that the directories exist before returning.

    Args:
        role_name: The role name. Either 'eos_designs' or 'eos_cli_config_gen'.
        tmp_dir: Path to use as the AVD temporary directory.
        clean: If True, remove all files in the role's temporary directory before returning.

    Returns:
        A tuple of Path objects containing (templated_path, validated_path).
    """
    base_tmp_path = _get_base_tmp_path(tmp_dir)
    role_path = base_tmp_path / role_name

    templated_path = role_path / TEMPLATED_DIR_NAME
    validated_path = role_path / VALIDATED_DIR_NAME

    # Ensure directories exist. parents=True handles the creation of the 'role_name' intermediate dir if needed.
    # Clean if requested.
    for path in [templated_path, validated_path]:
        if path.exists() and clean:
            for file in path.iterdir():
                file.unlink()
        else:
            path.mkdir(parents=True, exist_ok=True)

    return templated_path, validated_path
