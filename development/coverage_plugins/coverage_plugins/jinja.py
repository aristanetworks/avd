# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import ast
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import TYPE_CHECKING

from coverage import CoveragePlugin, FileReporter, FileTracer
from coverage.exceptions import ConfigError

if TYPE_CHECKING:
    from collections.abc import Iterable
    from types import FrameType

JINJA2_EXTENSIONS = ("jinja2.ext.loopcontrols", "jinja2.ext.do", "jinja2.ext.i18n")
SOURCE_EXIT = -1


@dataclass(frozen=True)
class CompiledTemplate:
    source_filename: str
    debug_map: tuple[tuple[int, int], ...]
    generated_line_map: dict[int, int]
    generated_line_ranges: dict[int, tuple[int, int]]


class JinjaTemplateCoveragePlugin(CoveragePlugin):
    def __init__(self, compiled_template_roots: Iterable[str | Path] | None = None) -> None:
        self.compiled_template_roots = _configured_compiled_template_roots(compiled_template_roots)

    def file_tracer(self, filename: str) -> JinjaTemplateFileTracer | None:
        compiled_filename = Path(filename).resolve()
        if compiled_filename.suffix != ".py":
            return None

        compiled_root = self._compiled_root_for(compiled_filename)
        if compiled_root is None:
            return None

        compiled_template = _parse_compiled_template(compiled_filename, compiled_root)
        if compiled_template is None:
            return None

        return JinjaTemplateFileTracer(compiled_template)

    def file_reporter(self, filename: str) -> JinjaTemplateFileReporter:
        return JinjaTemplateFileReporter(filename)

    def _compiled_root_for(self, filename: Path) -> Path | None:
        for compiled_root in self.compiled_template_roots:
            if filename.is_relative_to(compiled_root):
                return compiled_root
        return None


class JinjaTemplateFileTracer(FileTracer):
    def __init__(self, compiled_template: CompiledTemplate) -> None:
        self.compiled_template = compiled_template

    def source_filename(self) -> str:
        return self.compiled_template.source_filename

    def line_number_range(self, frame: FrameType) -> tuple[int, int]:
        generated_line = frame.f_lineno
        if line_range := self.compiled_template.generated_line_ranges.get(generated_line):
            return line_range

        if template_line := self.compiled_template.generated_line_map.get(generated_line):
            return template_line, template_line

        return -1, -1


class JinjaTemplateFileReporter(FileReporter):
    def lines(self) -> set[int]:
        return _find_reportable_jinja_lines(Path(self.filename))

    def translate_lines(self, lines: Iterable[int]) -> set[int]:
        reportable_lines = self.lines()
        return {line for line in lines if line in reportable_lines}

    def arcs(self) -> set[tuple[int, int]]:
        return _find_possible_jinja_arcs(Path(self.filename).resolve())

    def no_branch_lines(self) -> set[int]:
        return _find_no_branch_jinja_lines(Path(self.filename))

    def translate_arcs(self, arcs: Iterable[tuple[int, int]]) -> set[tuple[int, int]]:
        reportable_lines = self.lines()
        translated_arcs: set[tuple[int, int]] = set()
        for from_line, to_line in arcs:
            translated_from_line = _translate_recorded_arc_endpoint(from_line, reportable_lines)
            translated_to_line = _translate_recorded_arc_endpoint(to_line, reportable_lines)
            if translated_from_line is not None and translated_to_line is not None:
                translated_arcs.add((translated_from_line, translated_to_line))

        return translated_arcs

    def exit_counts(self) -> dict[int, int]:
        exit_counts: dict[int, int] = {}
        for from_line, to_line in self.arcs():
            if from_line > 0 and to_line != from_line:
                exit_counts[from_line] = exit_counts.get(from_line, 0) + 1

        return exit_counts


def coverage_init(reg, options) -> None:  # noqa: ANN001
    configured_roots = options.get("compiled_template_roots")
    if not configured_roots:
        msg = "coverage_plugins.jinja requires the compiled_template_roots coverage plugin option."
        raise ConfigError(msg)

    reg.add_file_tracer(JinjaTemplateCoveragePlugin(compiled_template_roots=configured_roots))


def _configured_compiled_template_roots(configured_roots: Iterable[str | Path] | str | Path | None) -> tuple[Path, ...]:
    if configured_roots is None:
        return ()

    if isinstance(configured_roots, (str, Path)):
        configured_roots = (configured_roots,)

    return tuple(Path(root).resolve() for root in configured_roots)


@lru_cache(maxsize=4096)
def _parse_compiled_template(compiled_filename: Path, compiled_root: Path) -> CompiledTemplate | None:
    try:
        tree = ast.parse(compiled_filename.read_text(encoding="utf-8"), filename=str(compiled_filename))
    except (OSError, SyntaxError, UnicodeDecodeError):
        return None

    constants = _module_string_constants(tree)
    template_name = constants.get("name")
    debug_info = constants.get("debug_info")
    if template_name is None or debug_info is None:
        return None

    source_filename = _resolve_template_source_filename(template_name, compiled_root)
    if source_filename is None:
        return None

    debug_map = _parse_debug_info(debug_info)
    generated_line_ranges = _generated_static_line_ranges(tree, source_filename)
    return CompiledTemplate(
        source_filename=str(source_filename),
        debug_map=debug_map,
        generated_line_map=dict(debug_map),
        generated_line_ranges=generated_line_ranges,
    )


def _translate_recorded_arc_endpoint(line: int, reportable_lines: set[int]) -> int | None:
    if line < 0:
        return SOURCE_EXIT

    if line in reportable_lines:
        return line

    return None


def _module_string_constants(tree: ast.Module) -> dict[str, str]:
    constants: dict[str, str] = {}
    for node in tree.body:
        if not isinstance(node, ast.Assign) or not isinstance(node.value, ast.Constant) or not isinstance(node.value.value, str):
            continue

        for target in node.targets:
            if isinstance(target, ast.Name):
                constants[target.id] = node.value.value

    return constants


def _resolve_template_source_filename(template_name: str, compiled_root: Path) -> Path | None:
    template_root = compiled_root.parent.resolve()
    source_filename = template_root.joinpath(*Path(template_name.replace("\\", "/")).parts).resolve()
    if not source_filename.is_relative_to(template_root) or not source_filename.is_file():
        return None

    return source_filename


def _parse_debug_info(debug_info: str) -> tuple[tuple[int, int], ...]:
    debug_map: list[tuple[int, int]] = []
    for pair in debug_info.split("&"):
        if not pair:
            continue

        try:
            template_line, generated_line = (int(value) for value in pair.split("=", 1))
        except ValueError:
            continue

        debug_map.append((generated_line, template_line))

    return tuple(sorted(debug_map))


@lru_cache(maxsize=4096)
def _find_reportable_jinja_lines(filename: Path) -> set[int]:
    try:
        source = filename.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return set()

    try:
        from jinja2 import Environment, TemplateSyntaxError, nodes  # noqa: PLC0415
    except ImportError:
        return set()

    environment = Environment(extensions=JINJA2_EXTENSIONS)  # noqa: S701
    try:
        parsed_template = environment.parse(source)
    except TemplateSyntaxError:
        return set()

    ignored_nodes = (nodes.Output, nodes.Template, nodes.TemplateData)
    reportable_lines: set[int] = set()
    nodes_to_visit = list(parsed_template.iter_child_nodes())
    while nodes_to_visit:
        node = nodes_to_visit.pop()
        if not isinstance(node, ignored_nodes):
            lineno = getattr(node, "lineno", None)
            if isinstance(lineno, int) and lineno > 0:
                reportable_lines.add(lineno)

        nodes_to_visit.extend(node.iter_child_nodes())

    reportable_lines.update(line_number for line_number, _line_text in _static_template_lines(source))
    reportable_lines.update(_control_statement_lines(source))
    return reportable_lines


def _generated_static_line_ranges(tree: ast.Module, source_filename: Path) -> dict[int, tuple[int, int]]:
    try:
        source = source_filename.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return {}

    source_static_lines = _static_template_lines(source)
    if not source_static_lines:
        return {}

    ranges: dict[int, tuple[int, int]] = {}
    source_index = 0
    yield_nodes = sorted(
        (node for node in ast.walk(tree) if isinstance(node, ast.Yield)),
        key=lambda node: node.lineno,
    )
    for node in yield_nodes:
        if not isinstance(node, ast.Yield) or not isinstance(node.value, ast.Constant) or not isinstance(node.value.value, str):
            continue

        rendered_lines = _non_whitespace_lines(node.value.value)
        if not rendered_lines:
            continue

        matched_line_numbers: list[int] = []
        next_source_index = source_index
        for rendered_line in rendered_lines:
            matched_index = _find_next_static_line(source_static_lines, rendered_line, next_source_index)
            if matched_index is None:
                matched_line_numbers.clear()
                break

            matched_line_numbers.append(source_static_lines[matched_index][0])
            next_source_index = matched_index + 1

        if matched_line_numbers and _is_contiguous_line_range(matched_line_numbers):
            ranges[node.lineno] = (matched_line_numbers[0], matched_line_numbers[-1])
            source_index = next_source_index

    return ranges


def _find_next_static_line(source_static_lines: tuple[tuple[int, str], ...], rendered_line: str, start_index: int) -> int | None:
    for index, (_line_number, source_line) in enumerate(source_static_lines[start_index:], start=start_index):
        if source_line == rendered_line:
            return index

    return None


def _static_template_lines(source: str) -> tuple[tuple[int, str], ...]:
    try:
        from jinja2 import Environment  # noqa: PLC0415
    except ImportError:
        return ()

    environment = Environment(extensions=JINJA2_EXTENSIONS)  # noqa: S701
    static_lines: list[tuple[int, str]] = []
    try:
        tokens = environment.lex(source)
        for lineno, kind, value in tokens:
            if kind == "data":
                static_lines.extend(_numbered_non_whitespace_lines(lineno, value))
    except Exception:
        return ()

    return tuple(static_lines)


def _control_statement_lines(source: str) -> set[int]:
    try:
        from jinja2 import Environment  # noqa: PLC0415
    except ImportError:
        return set()

    environment = Environment(extensions=JINJA2_EXTENSIONS)  # noqa: S701
    control_statement_lines: set[int] = set()
    in_block = False
    block_lineno = 0
    try:
        for lineno, kind, value in environment.lex(source):
            if kind == "block_begin":
                in_block = True
                block_lineno = lineno
                continue

            if kind == "block_end":
                in_block = False
                block_lineno = 0
                continue

            if in_block and kind == "name" and value in {"if", "elif", "for"}:
                control_statement_lines.add(block_lineno)
                in_block = False
    except Exception:
        return set()

    return control_statement_lines


def _numbered_non_whitespace_lines(start_lineno: int, value: str) -> list[tuple[int, str]]:
    numbered_lines: list[tuple[int, str]] = []
    line_number = start_lineno
    for line in value.splitlines(keepends=True):
        line_without_newline = line.removesuffix("\n").removesuffix("\r")
        stripped_line = line_without_newline.strip()
        if stripped_line:
            numbered_lines.append((line_number, stripped_line))

        if line.endswith(("\n", "\r")):
            line_number += 1

    return numbered_lines


def _non_whitespace_lines(value: str) -> list[str]:
    return [line.strip() for line in value.splitlines() if line.strip()]


def _is_contiguous_line_range(line_numbers: list[int]) -> bool:
    return line_numbers == list(range(line_numbers[0], line_numbers[-1] + 1))


@lru_cache(maxsize=4096)
def _find_possible_jinja_arcs(source_filename: Path) -> set[tuple[int, int]]:
    try:
        source = source_filename.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return set()

    try:
        from jinja2 import Environment, TemplateSyntaxError, nodes  # noqa: PLC0415
    except ImportError:
        return set()

    environment = Environment(extensions=JINJA2_EXTENSIONS)  # noqa: S701
    try:
        parsed_template = environment.parse(source)
    except TemplateSyntaxError:
        return set()

    reportable_lines = _find_reportable_jinja_lines(source_filename)
    arcs: set[tuple[int, int]] = set()
    for node in parsed_template.find_all((nodes.If, nodes.For)):
        if isinstance(node, nodes.If):
            _add_if_arcs(node, reportable_lines, arcs)
        elif isinstance(node, nodes.For):
            _add_for_arcs(node, reportable_lines, arcs)

    return arcs


def _add_if_arcs(node, reportable_lines: set[int], arcs: set[tuple[int, int]]) -> None:  # noqa: ANN001
    after_line = _next_reportable_line(reportable_lines, _node_end_lineno(node))
    conditional_nodes = [node, *node.elif_]
    for index, conditional_node in enumerate(conditional_nodes):
        body_line = _first_reportable_line_in_nodes(
            reportable_lines,
            conditional_node.body,
            after_line=conditional_node.lineno,
        )
        false_line = _false_if_target(node, conditional_nodes, index, reportable_lines, after_line)

        _add_arc(arcs, conditional_node.lineno, body_line)
        _add_arc(arcs, conditional_node.lineno, false_line)


def _false_if_target(node, conditional_nodes: list, index: int, reportable_lines: set[int], after_line: int) -> int | None:  # noqa: ANN001
    if index + 1 < len(conditional_nodes):
        return conditional_nodes[index + 1].lineno
    if node.else_:
        return _first_reportable_line_in_nodes(reportable_lines, node.else_)

    return after_line


def _add_for_arcs(node, reportable_lines: set[int], arcs: set[tuple[int, int]]) -> None:  # noqa: ANN001
    body_line = _first_reportable_line_in_nodes(reportable_lines, node.body, after_line=node.lineno)

    _add_arc(arcs, node.lineno, body_line)
    if node.else_:
        _add_arc(arcs, node.lineno, _first_reportable_line_in_nodes(reportable_lines, node.else_))


def _first_reportable_line_in_nodes(reportable_lines: set[int], nodes, after_line: int = 0) -> int | None:  # noqa: ANN001
    if not nodes:
        return None

    start_line = min(getattr(node, "lineno", 0) for node in nodes)
    end_line = max(_node_end_lineno(node) for node in nodes)
    if line := next((line for line in sorted(reportable_lines) if line > after_line and start_line <= line <= end_line), None):
        return line

    return _next_reportable_line(reportable_lines, max(after_line, start_line - 1))


def _next_reportable_line(reportable_lines: set[int], line_number: int) -> int:
    return next((line for line in sorted(reportable_lines) if line > line_number), SOURCE_EXIT)


def _node_end_lineno(node) -> int:  # noqa: ANN001
    node_lines = [getattr(node, "lineno", 0)]
    nodes_to_visit = list(node.iter_child_nodes())
    while nodes_to_visit:
        child_node = nodes_to_visit.pop()
        if isinstance((lineno := getattr(child_node, "lineno", None)), int):
            node_lines.append(lineno)
        nodes_to_visit.extend(child_node.iter_child_nodes())

    return max(node_lines)


def _add_arc(arcs: set[tuple[int, int]], from_line: int, to_line: int | None) -> None:
    if to_line is None or from_line == to_line:
        return

    arcs.add((from_line, to_line))


@lru_cache(maxsize=4096)
def _find_no_branch_jinja_lines(source_filename: Path) -> set[int]:
    try:
        source = source_filename.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return set()

    try:
        from jinja2 import Environment, TemplateSyntaxError, nodes  # noqa: PLC0415
    except ImportError:
        return set()

    environment = Environment(extensions=JINJA2_EXTENSIONS)  # noqa: S701
    try:
        parsed_template = environment.parse(source)
    except TemplateSyntaxError:
        return set()

    return {node.lineno for node in parsed_template.body if isinstance(node, nodes.If) and not node.elif_ and not node.else_}
