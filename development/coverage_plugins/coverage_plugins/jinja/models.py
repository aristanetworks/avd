# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Shared models for the Jinja coverage plugin."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Mapping
    from pathlib import Path

JINJA2_EXTENSIONS = ("jinja2.ext.loopcontrols", "jinja2.ext.do", "jinja2.ext.i18n")
SOURCE_EXIT = -1
FileStamp = tuple[int, int]


@dataclass(frozen=True)
class CompiledTemplate:
    """Parsed mapping metadata for one compiled Jinja Python module."""

    source_filename: str
    debug_map: tuple[tuple[int, int], ...]
    generated_line_ranges: Mapping[int, tuple[int, int]]


@dataclass(frozen=True)
class SourceTemplate:
    """Cached source-level reporting model for one Jinja template."""

    reportable_lines: frozenset[int]
    arc_endpoint_lines: frozenset[int]
    possible_arcs: frozenset[tuple[int, int]]
    no_branch_lines: frozenset[int]
    tag_ranges: Mapping[int, tuple[int, int]]


def file_stamp(filename: Path) -> FileStamp | None:
    """Return the file metadata used to invalidate path-keyed caches."""
    try:
        stat_result = filename.stat()
    except OSError:
        return None

    return stat_result.st_mtime_ns, stat_result.st_size
