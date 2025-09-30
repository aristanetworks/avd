# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import logging
from dataclasses import dataclass

from ansible.utils.display import Display

ANSIBLE_VERBOSITY_MAPPING: dict[int, dict[str, int]] = {
    0: {  # Verbosity: 0
        "ansible_collections.arista.avd": logging.WARNING,
        "pyavd": logging.WARNING,
        "schema_tools": logging.WARNING,
        "anta": logging.WARNING,
        "external_libs": logging.WARNING,
    },
    1: {  # Verbosity: -v
        "ansible_collections.arista.avd": logging.INFO,
        "pyavd": logging.INFO,
        "schema_tools": logging.INFO,
        "anta": logging.WARNING,
        "external_libs": logging.WARNING,
    },
    2: {  # Verbosity: -vv
        "ansible_collections.arista.avd": logging.INFO,
        "pyavd": logging.DEBUG,
        "schema_tools": logging.DEBUG,
        "anta": logging.WARNING,
        "external_libs": logging.WARNING,
    },
    3: {  # Verbosity: -vvv
        "ansible_collections.arista.avd": logging.DEBUG,
        "pyavd": logging.DEBUG,
        "schema_tools": logging.DEBUG,
        "anta": logging.INFO,
        "external_libs": logging.WARNING,
    },
    4: {  # Verbosity: -vvvv
        "ansible_collections.arista.avd": logging.DEBUG,
        "pyavd": logging.DEBUG,
        "schema_tools": logging.DEBUG,
        "anta": logging.DEBUG,
        "external_libs": logging.WARNING,
    },
    5: {  # Verbosity: -vvvvv
        "ansible_collections.arista.avd": logging.DEBUG,
        "pyavd": logging.DEBUG,
        "schema_tools": logging.DEBUG,
        "anta": logging.DEBUG,
        "external_libs": logging.INFO,
    },
    6: {  # Verbosity: -vvvvvv
        "ansible_collections.arista.avd": logging.DEBUG,
        "pyavd": logging.DEBUG,
        "schema_tools": logging.DEBUG,
        "anta": logging.DEBUG,
        "external_libs": logging.DEBUG,
    },
}
"""Map Ansible verbosity levels (0-6) to a dictionary of logger names and their desired logging level."""

EXTERNAL_LIB_LOGGERS = ["asyncio", "httpcore", "httpx", "requests", "urllib3"]
"""List of common third-party libraries whose log levels are managed collectively.

- `asyncio`: Python built-in asynchronous framework.
- `httpcore`, `httpx`: The HTTP client libraries used by ANTA.
- `requests`, `urllib3`: Used by the `cv_workflow` action plugin for authentication.

The `hpack` logger is intentionally omitted as it is too noisy. It is used by `grpclib`,
which is a dependency of `cv_workflow`.
"""


def get_avd_log_level(logger_name: str) -> int:
    """
    Calculate the logging level for a given logger based on Ansible verbosity.

    Args:
        logger_name: The name of the logger for which to find the level.
        verbosity: The verbosity level from Ansible Display object (0 for none, 1 for -v, etc.).

    Returns:
        The calculated logging level.
    """
    # Get the verbosity level from Ansible Display singleton object (0 for none, 1 for -v, etc.)
    verbosity = Display().verbosity

    # Any verbosity level set above 6 will be treated as 6
    max_defined_verbosity = max(ANSIBLE_VERBOSITY_MAPPING.keys())
    effective_verbosity = min(verbosity, max_defined_verbosity)

    level_map = ANSIBLE_VERBOSITY_MAPPING[effective_verbosity]

    # If the logger is not found, it is considered an external library
    return level_map.get(logger_name, level_map["external_libs"])


@dataclass(frozen=True)
class AvdLoggingConfig:
    """Configuration for the logging environment in AVD Ansible action plugins."""

    add_role_context: bool = False
    add_hostname_context: bool = False
    target_loggers: tuple[str, ...] = ("ansible_collections.arista.avd", "pyavd", "schema_tools")


@dataclass(frozen=True)
class LoggerState:
    """Dataclass to store logger parameters to be restored later."""

    level: int
    handlers: tuple[logging.Handler, ...]
    propagate: bool
