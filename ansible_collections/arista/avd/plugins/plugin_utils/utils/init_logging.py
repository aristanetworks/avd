# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import logging

from .python_to_ansible_logging_handler import PythonToAnsibleHandler


def init_pyavd_logging() -> None:
    """Specify logger parameters for pyavd."""
    pyavd_logger = logging.getLogger("pyavd")
    pyavd_handler = PythonToAnsibleHandler(None)
    pyavd_formatter = logging.Formatter("[pyavd] - %(message)s")
    pyavd_handler.setFormatter(pyavd_formatter)
    pyavd_logger.addHandler(pyavd_handler)
    pyavd_logger.setLevel(logging.INFO)
