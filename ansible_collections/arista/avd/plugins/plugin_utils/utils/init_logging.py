# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import logging

from ansible.utils.display import Display

from .python_to_ansible_logging_handler import PythonToAnsibleHandler


def init_pyavd_logging() -> None:
    """Specify logger parameters for pyavd."""
    pyavd_logger = logging.getLogger("pyavd")
    schema_tools_logger = logging.getLogger("schema_tools")

    pyavd_handler = PythonToAnsibleHandler(None)
    pyavd_formatter = logging.Formatter("[pyavd] - %(message)s")
    pyavd_handler.setFormatter(pyavd_formatter)

    pyavd_logger.addHandler(pyavd_handler)
    schema_tools_logger.addHandler(pyavd_handler)

    verbosity = Display().verbosity
    if verbosity > 3:
        pyavd_logger.setLevel(logging.DEBUG)
        schema_tools_logger.setLevel(logging.DEBUG)
    elif verbosity > 0:
        pyavd_logger.setLevel(logging.INFO)
        schema_tools_logger.setLevel(logging.INFO)
    else:
        pyavd_logger.setLevel(logging.WARNING)
        schema_tools_logger.setLevel(logging.WARNING)
