# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""
Coverage.py plugin mapping generated Jinja module execution to source templates.

The reporting model is intentionally source-level and heuristic: it maps only
lines and arcs it can associate with template behavior instead of assigning
generated scaffolding to the nearest template line.
"""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

from coverage import CoveragePlugin, FileReporter, FileTracer
from coverage.exceptions import ConfigError

from .compiled_parser import parse_compiled_template
from .source_template import (
    covered_else_branch_arcs,
    covered_multiline_tag_branch_arcs,
    source_template,
    translate_recorded_arc_endpoint,
)

if TYPE_CHECKING:
    from collections.abc import Iterable
    from types import FrameType

    from .models import CompiledTemplate

JINJA2_EXTENSIONS = ("jinja2.ext.loopcontrols", "jinja2.ext.do", "jinja2.ext.i18n")
SOURCE_EXIT = -1
FileStamp = tuple[int, int]


class JinjaTemplateCoveragePlugin(CoveragePlugin):
    """Coverage.py file tracer plugin for generated Jinja modules."""

    def __init__(self, compiled_template_roots: Iterable[str | Path] | None = None) -> None:
        """Store normalized directories containing generated Jinja Python modules."""
        self.compiled_template_roots = _configured_compiled_template_roots(compiled_template_roots)

    def file_tracer(self, filename: str) -> JinjaTemplateFileTracer | None:
        """Return a tracer for generated Jinja modules under configured compiled-template roots."""
        compiled_filename = Path(filename).resolve()
        if compiled_filename.suffix != ".py":
            return None

        compiled_root = self._compiled_root_for(compiled_filename)
        if compiled_root is None:
            return None

        compiled_template = parse_compiled_template(compiled_filename, compiled_root)
        if compiled_template is None:
            return None

        return JinjaTemplateFileTracer(compiled_template)

    def file_reporter(self, filename: str) -> JinjaTemplateFileReporter:
        """Return the reporter used by coverage.py when generating reports for a source template."""
        return JinjaTemplateFileReporter(filename)

    def _compiled_root_for(self, filename: Path) -> Path | None:
        """Find the configured compiled-template root containing ``filename``."""
        for compiled_root in self.compiled_template_roots:
            if filename.is_relative_to(compiled_root):
                return compiled_root
        return None


class JinjaTemplateFileTracer(FileTracer):
    """Map executed generated Python frame lines to source Jinja template lines."""

    def __init__(self, compiled_template: CompiledTemplate) -> None:
        """Keep the precomputed source mapping for one compiled template module."""
        self.compiled_template = compiled_template

    def source_filename(self) -> str:
        """Tell coverage.py which source file should receive execution data."""
        return self.compiled_template.source_filename

    def line_number_range(self, frame: FrameType) -> tuple[int, int]:
        """Translate the current generated Python frame line to a source template line range."""
        generated_line = frame.f_lineno
        if line_range := self.compiled_template.generated_line_ranges.get(generated_line):
            return line_range

        return -1, -1


class JinjaTemplateFileReporter(FileReporter):
    """Describe executable lines and branch arcs for a source Jinja template."""

    def lines(self) -> set[int]:
        """Return source template lines that should be treated as executable statements."""
        return set(source_template(Path(self.filename)).reportable_lines)

    def translate_lines(self, lines: Iterable[int]) -> set[int]:
        """Drop recorded lines that are not reportable source template lines."""
        reportable_lines = self.lines()
        return {line for line in lines if line in reportable_lines}

    def arcs(self) -> set[tuple[int, int]]:
        """Return possible source-level branch arcs for supported Jinja control flow."""
        return set(source_template(Path(self.filename)).possible_arcs)

    def no_branch_lines(self) -> set[int]:
        """Return lines that should not be treated as missing branch coverage."""
        return set(source_template(Path(self.filename)).no_branch_lines)

    def translate_arcs(self, arcs: Iterable[tuple[int, int]]) -> set[tuple[int, int]]:
        """Drop recorded arcs whose endpoints are not reportable source template lines."""
        recorded_arcs = tuple(arcs)
        template = source_template(Path(self.filename))
        translated_arcs: set[tuple[int, int]] = set()
        for from_line, to_line in recorded_arcs:
            translated_from_line = translate_recorded_arc_endpoint(from_line, template.arc_endpoint_lines)
            translated_to_line = translate_recorded_arc_endpoint(to_line, template.arc_endpoint_lines)
            if translated_from_line is not None and translated_to_line is not None:
                translated_arcs.add((translated_from_line, translated_to_line))

        possible_arcs = template.possible_arcs
        source_filename = Path(self.filename)
        translated_arcs.update(
            covered_multiline_tag_branch_arcs(recorded_arcs, possible_arcs, template.tag_ranges, template.reportable_lines),
        )
        translated_arcs.update(
            covered_else_branch_arcs(recorded_arcs, translated_arcs, possible_arcs, source_filename, template.reportable_lines),
        )
        return translated_arcs

    def exit_counts(self) -> dict[int, int]:
        """Return the number of possible exits from each reportable source template line."""
        exit_counts: dict[int, int] = {}
        for from_line, to_line in self.arcs():
            if from_line > 0 and to_line != from_line:
                exit_counts[from_line] = exit_counts.get(from_line, 0) + 1

        return exit_counts


def coverage_init(reg, options) -> None:  # noqa: ANN001
    """Register the plugin with coverage.py using options from ``[tool.coverage.coverage_plugins.jinja]``."""
    configured_roots = options.get("compiled_template_roots")
    if not configured_roots:
        msg = "coverage_plugins.jinja requires the compiled_template_roots coverage plugin option."
        raise ConfigError(msg)

    reg.add_file_tracer(JinjaTemplateCoveragePlugin(compiled_template_roots=configured_roots))


def _configured_compiled_template_roots(configured_roots: Iterable[str | Path] | str | Path | None) -> tuple[Path, ...]:
    """Normalize the configured compiled-template roots to absolute ``Path`` objects."""
    if configured_roots is None:
        return ()

    if isinstance(configured_roots, (str, Path)):
        configured_roots = (configured_roots,)

    return tuple(Path(root).resolve() for root in configured_roots)
