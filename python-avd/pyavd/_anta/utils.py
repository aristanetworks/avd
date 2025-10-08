# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Utility functions used by PyAVD for ANTA."""

from __future__ import annotations

from logging import getLogger
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from anta.catalog import AntaCatalog


LOGGER = getLogger(__name__)


def dump_anta_catalog(hostname: str, catalog: AntaCatalog, catalog_dir: str | Path) -> None:
    """
    Dump the ANTA catalog for a device to the provided catalog directory.

    The catalog will be saved as a JSON file named after the device: `<device>.json`.
    """
    catalog_path = Path(catalog_dir) / f"{hostname}.json"
    catalog_dump = catalog.dump()

    LOGGER.debug("<%s> Dumping ANTA catalog at %s", hostname, catalog_path)
    with catalog_path.open(mode="w", encoding="UTF-8") as stream:
        stream.write(catalog_dump.to_json())


def parse_tests(test_list: list[str]) -> dict[str, set[str]]:
    """
    Parse a list of test strings into a dictionary mapping test names to a set of peer names to filter.

    Args:
        test_list: A list of strings, where each string is a test name,
                   optionally with parenthesized, comma-separated peer names.

    Returns:
        A dictionary mapping each test name to a set of peer names to filter.
    """
    parsed_map = {}
    for item in test_list:
        name, paren, args = item.partition("(")
        name = name.strip()

        if not paren:
            # No parentheses, so no specific filters.
            parsed_map[name] = set()
            continue

        # If parentheses exist, process the arguments.
        filters_str = args.rstrip(")").strip()
        if filters_str:
            # Split the string by commas to get raw peer names.
            raw_peers = filters_str.split(",")

            # Clean each peer by stripping whitespace and quotes.
            cleaned_peers = (peer.strip().strip("'\"") for peer in raw_peers)

            # Create the final set, filtering out any empty strings that resulted from the cleaning process.
            parsed_map[name] = {peer for peer in cleaned_peers if peer}
        else:
            # Handles cases like "TestName()".
            parsed_map[name] = set()

    return parsed_map
