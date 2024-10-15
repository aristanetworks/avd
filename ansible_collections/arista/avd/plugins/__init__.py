# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from pathlib import Path

from .plugin_utils.utils.init_logging import init_pyavd_logging

PYTHON_AVD_PATH = Path(__file__).parents[4] / "python-avd"
RUNNING_FROM_SOURCE_PATH = PYTHON_AVD_PATH / "pyavd/running_from_src.txt"

init_pyavd_logging()

if RUNNING_FROM_SOURCE_PATH.exists():
    import sys

    from ansible.utils.display import Display

    display = Display()

    display.warning(f"AVD detected it is running from source, prepending the path to the source of pyavd '{str(PYTHON_AVD_PATH)}' to PATH to use it.")

    sys.path = [str(PYTHON_AVD_PATH), *sys.path]
