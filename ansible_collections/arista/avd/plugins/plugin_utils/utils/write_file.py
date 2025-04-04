# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from pathlib import Path


def write_file(content: str, filename: str, file_mode: str = "0o664", dir_mode: str = "0o775", track_changes: bool = True) -> bool:
    """
    This function writes the file only if the content has changed.

    Parameters
    ----------
        content: The content to write
        filename: Target filename
        file_mode: The permissions to set on the file if creating it. Permissions for existing files are not changed.
        dir_mode: The permissions to set on a directory if creating it. Permissions for existing directories are not changed.
        track_changes: Read the file first to check if it already contains the correct data.

    Returns:
    -------
        bool: Indicate if the content of the file has changed.
    """
    path = Path(filename)
    if not path.exists():
        # Create parent dirs automatically.
        path.parent.mkdir(mode=int(dir_mode, 8), parents=True, exist_ok=True)
        # Touch file
        path.touch(mode=int(file_mode, 8))
    elif track_changes and path.read_text(encoding="UTF-8") == content:
        return False

    path.write_text(content, encoding="UTF-8")
    return True
