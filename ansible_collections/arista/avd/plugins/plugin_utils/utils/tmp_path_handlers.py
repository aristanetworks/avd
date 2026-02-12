# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from pathlib import Path

TEMPLATED_DIR_NAME = "templated"
VALIDATED_DIR_NAME = "validated"

EOS_DESIGNS_FACTS_FILENAME = "eos_designs_facts.json"

AVD_TMP_DIR_MODE = 0o700


def _get_tmp_path(tmp_dir: str) -> Path:
    """
    Return a Path object for the given temporary directory.

    The directory will be created if missing with 700 permissions.

    Args:
        tmp_dir: Path to use as the temporary directory.

    Returns:
        Path object pointing to the temporary directory.
    """
    path = Path(tmp_dir)
    if not path.exists():
        try:
            path.mkdir(mode=AVD_TMP_DIR_MODE, parents=True, exist_ok=True)
        except OSError as e:
            msg = f"Unable to create temporary directory {path}: {e}"
            raise type(e)(msg) from e
    return path


def get_eos_designs_facts_path(tmp_dir: str, clean: bool = False) -> Path:
    """
    Return the Path object for the shared eos_designs facts file.

    This file contains facts for all devices in the fabric, written by `eos_designs_facts`
    and read by `eos_designs_structured_config`.

    The parent directory is created if it doesn't exist.

    Args:
        tmp_dir: Path to the eos_designs temporary directory.
        clean: If True, remove the file if it exists before returning.

    Returns:
        Path object pointing to the eos_designs facts JSON file.
    """
    tmp_path = _get_tmp_path(tmp_dir)
    eos_designs_facts_path = tmp_path / EOS_DESIGNS_FACTS_FILENAME

    # Clean file if requested.
    if eos_designs_facts_path.exists() and clean:
        eos_designs_facts_path.unlink()

    return eos_designs_facts_path


def get_tmp_paths(tmp_dir: str, clean: bool = False) -> tuple[Path, Path]:
    """
    Return the temporary paths for 'templated' and 'validated' directories to be used inside tmp_dir.

    This function ensures that the directories exist before returning.

    Args:
        tmp_dir: Path to use as the temporary directory.
        clean: If True, remove all files in the 'templated' and 'validated' directories before returning.

    Returns:
        A tuple of Path objects containing (templated_path, validated_path).
    """
    tmp_path = _get_tmp_path(tmp_dir)

    templated_path = tmp_path / TEMPLATED_DIR_NAME
    validated_path = tmp_path / VALIDATED_DIR_NAME

    # Ensure directories exist.
    # Clean files if requested.
    for path in [templated_path, validated_path]:
        if path.exists() and clean:
            for item in path.iterdir():
                if item.is_file():
                    item.unlink()
        else:
            path.mkdir(parents=True, exist_ok=True)

    return templated_path, validated_path
