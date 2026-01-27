# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .api.schemas import EOSConfig


def get_device_config_tree(structured_config: EOSConfig | dict) -> dict[str, dict]:
    """
    Render eos_cli_config_gen templates and return a nested dict representing the CLI.

    Args:
        structured_config:
            EOSConfig instance or dictionary with the validated structured configuration.

    Returns:
        Device configuration as a nested dict under a single 'default' key.
    """
    from .get_device_config import get_device_config  # noqa: PLC0415

    full_cli = get_device_config(structured_config)

    # Convert the full CLI into a nested dictionary
    return {"default": _cli_to_tree(full_cli)}


def _cli_to_tree(cli: str) -> dict[str, dict]:
    """
    Convert EOS CLI text into a nested dictionary using indentation.

    Each command becomes a key in the dictionary, and subcommands are nested dictionaries.
    """
    tree: dict[str, dict] = {}
    stack: list[tuple[int, dict[str, dict]]] = [(0, tree)]

    for line in cli.splitlines():
        stripped = line.lstrip()

        # Ignore empty lines and comments
        if not stripped or stripped.startswith("!"):
            continue

        indent = len(line) - len(stripped)

        # Pop stack until we find the correct parent based on indentation
        while stack and indent <= stack[-1][0]:
            stack.pop()

        parent = stack[-1][1] if stack else tree
        parent[stripped] = {}
        stack.append((indent, parent[stripped]))

    return tree
