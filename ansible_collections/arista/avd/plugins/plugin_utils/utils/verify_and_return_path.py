# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from pathlib import Path


def verify_and_return_path(path_input: str | Path) -> Path:
    """Verify if the given path exists in the file system and returns the Path object.

    Args:
    ----
    path_input (str or Path): A string or Path object representing a file system path.

    Returns:
    -------
    Path: The verified file system path as a Path object.

    Raises:
    ------
    TypeError: If the input is not a string or Path object.
    FileNotFoundError: If the path does not exist.
    """
    if not isinstance(path_input, (str, Path)):
        msg = f"Input path {path_input} must be a string or a Path object."
        raise TypeError(msg)
    path = Path(path_input)
    if path.exists():
        return path
    msg = f"The path {path} does not exist"
    raise FileNotFoundError(msg)
