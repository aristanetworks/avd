# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Source-template reporting helpers for the Jinja coverage plugin."""

from __future__ import annotations

from functools import lru_cache
from types import MappingProxyType
from typing import TYPE_CHECKING, Any

from .models import JINJA2_EXTENSIONS, SOURCE_EXIT, FileStamp, SourceTemplate, file_stamp

if TYPE_CHECKING:
    from collections.abc import Collection, Mapping
    from pathlib import Path


def source_template(filename: Path) -> SourceTemplate:
    """Return the cached source reporting model for one template."""
    if (stamp := file_stamp(filename)) is None:
        return SourceTemplate(
            reportable_lines=frozenset(),
            arc_endpoint_lines=frozenset(),
            possible_arcs=frozenset(),
            arc_aliases=MappingProxyType({}),
            no_branch_lines=frozenset(),
            tag_ranges=MappingProxyType({}),
        )

    return _source_template_cached(filename.resolve(), stamp)


@lru_cache(maxsize=4096)
def _source_template_cached(filename: Path, stamp: FileStamp) -> SourceTemplate:
    """
    Build the source-level model used by all reporting methods.

    The arc endpoint set is explicit so possible arc generation and recorded
    arc translation agree on which source lines can be branch endpoints.
    ``stamp`` participates only in cache invalidation.
    """
    reportable_lines = _find_reportable_jinja_lines_cached(filename, stamp)
    structural_control_label_lines = _find_structural_control_label_lines_cached(filename, stamp)
    arc_endpoint_lines = _arc_endpoint_lines(reportable_lines, structural_control_label_lines)
    possible_arcs = _find_possible_jinja_arcs_cached(filename, stamp, reportable_lines, arc_endpoint_lines)
    return SourceTemplate(
        reportable_lines=reportable_lines,
        arc_endpoint_lines=arc_endpoint_lines,
        possible_arcs=possible_arcs,
        arc_aliases=MappingProxyType(_find_jinja_arc_aliases_cached(filename, stamp, possible_arcs, reportable_lines)),
        no_branch_lines=_find_no_branch_jinja_lines_cached(filename, stamp),
        tag_ranges=MappingProxyType(source_tag_ranges(filename)),
    )


def _arc_endpoint_lines(reportable_lines: Collection[int], structural_control_label_lines: Collection[int] = ()) -> frozenset[int]:
    """
    Return source lines allowed as branch arc endpoints.

    Structural control labels are not executable lines, but they are useful
    source-level join points for branch coverage.
    """
    return frozenset(reportable_lines) | frozenset(structural_control_label_lines)


def translate_recorded_arc_endpoint(line: int, arc_endpoint_lines: Collection[int]) -> int | None:
    """Translate one recorded arc endpoint to a template branch endpoint."""
    if line < 0:
        return SOURCE_EXIT

    if line in arc_endpoint_lines:
        return line

    return None


def covered_multiline_tag_branch_arcs(
    recorded_arcs: tuple[tuple[int, int], ...],
    possible_arcs: Collection[tuple[int, int]],
    tag_ranges: Mapping[int, tuple[int, int]],
    reportable_lines: Collection[int],
) -> set[tuple[int, int]]:
    """Return source branch arcs covered by coverage.py's multiline range arcs."""
    recorded_arc_set = set(recorded_arcs)
    covered_branch_arcs: set[tuple[int, int]] = set()
    for from_line, to_line in possible_arcs:
        if from_line <= 0 or to_line <= 0:
            continue
        if to_line not in reportable_lines:
            continue

        tag_range = tag_ranges.get(from_line)
        if tag_range is None or tag_range[0] == tag_range[1]:
            continue

        start_line, end_line = tag_range
        if not all((line_number, line_number + 1) in recorded_arc_set for line_number in range(start_line, end_line)):
            continue

        if any(raw_to_line == to_line and raw_from_line not in reportable_lines for raw_from_line, raw_to_line in recorded_arcs):
            covered_branch_arcs.add((from_line, to_line))

    return covered_branch_arcs


def covered_structural_control_branch_arcs(
    recorded_arcs: tuple[tuple[int, int], ...],
    possible_arcs: Collection[tuple[int, int]],
    tag_ranges: Mapping[int, tuple[int, int]],
    reportable_lines: Collection[int],
) -> set[tuple[int, int]]:
    """
    Return branch arcs covered by jumps from multiline tags to structural labels.

    No-else ``if`` statements use the source ``endif`` line as the false branch
    target. Jinja may report the runtime jump from the last line in a multiline
    ``if`` tag to that ``endif`` label instead of from the first tag line.
    """
    recorded_arc_set = set(recorded_arcs)
    reportable_line_set = set(reportable_lines)
    covered_branch_arcs: set[tuple[int, int]] = set()
    for from_line, to_line in possible_arcs:
        if from_line <= 0 or to_line <= 0:
            continue
        if to_line in reportable_line_set:
            continue

        start_line, end_line = tag_ranges.get(from_line, (from_line, from_line))
        if any((line_number, to_line) in recorded_arc_set for line_number in range(start_line, end_line + 1)):
            covered_branch_arcs.add((from_line, to_line))

    return covered_branch_arcs


def covered_else_branch_arcs(
    recorded_arcs: tuple[tuple[int, int], ...],
    translated_arcs: set[tuple[int, int]],
    possible_arcs: Collection[tuple[int, int]],
    source_filename: Path,
    reportable_lines: Collection[int],
) -> set[tuple[int, int]]:
    """Return else branch arcs covered by generated arcs entering an else tag."""
    try:
        source = source_filename.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return set()

    else_lines = _control_statement_lines(source, names={"else"})
    executed_lines = {line for arc in translated_arcs for line in arc if line > 0}
    covered_else_arcs: set[tuple[int, int]] = set()
    for from_line, to_line in possible_arcs:
        if from_line not in executed_lines or to_line not in else_lines:
            continue

        if any(raw_to_line == to_line and raw_from_line not in reportable_lines for raw_from_line, raw_to_line in recorded_arcs):
            covered_else_arcs.add((from_line, to_line))

    return covered_else_arcs


def covered_generated_body_branch_arcs(
    recorded_arcs: tuple[tuple[int, int], ...],
    translated_arcs: set[tuple[int, int]],
    possible_arcs: Collection[tuple[int, int]],
    reportable_lines: Collection[int],
) -> set[tuple[int, int]]:
    """
    Return body branch arcs covered by generated code entering reportable body lines.

    Jinja compiles ``set`` and ``do`` statements, and sometimes static output,
    into generated Python lines that enter the source body line without a direct
    source-to-source arc. If the condition was evaluated and generated code
    reached the body line, credit the source branch body arc.
    """
    executed_lines = {line for arc in translated_arcs for line in arc if line > 0}
    executed_lines.update(raw_to_line for _raw_from_line, raw_to_line in recorded_arcs if raw_to_line in reportable_lines)
    covered_branch_arcs: set[tuple[int, int]] = set()
    for from_line, to_line in possible_arcs:
        if from_line not in executed_lines or to_line not in reportable_lines:
            continue

        if any(raw_to_line == to_line and raw_from_line not in reportable_lines for raw_from_line, raw_to_line in recorded_arcs):
            covered_branch_arcs.add((from_line, to_line))

    return covered_branch_arcs


def covered_adjacent_static_branch_arcs(
    recorded_arcs: tuple[tuple[int, int], ...],
    possible_arcs: Collection[tuple[int, int]],
    reportable_lines: Collection[int],
) -> set[tuple[int, int]]:
    """
    Return branch arcs covered by jumps from adjacent rendered output.

    Jinja sometimes records line events on the static output immediately before
    an ``if`` tag instead of on the generated ``if`` statement itself. In that
    shape, coverage sees an arc from the previous rendered line into the body
    when the condition is true, or around the body when it is false.
    """
    covered_branch_arcs: set[tuple[int, int]] = set()
    reportable_line_set = set(reportable_lines)
    recorded_line_set = {line for recorded_arc in recorded_arcs for line in recorded_arc if line > 0}
    possible_arcs_by_from_line: dict[int, set[int]] = {}
    for from_line, to_line in possible_arcs:
        if from_line > 0 and to_line > 0:
            possible_arcs_by_from_line.setdefault(from_line, set()).add(to_line)

    for from_line, to_lines in possible_arcs_by_from_line.items():
        if len(to_lines) < 2:
            continue

        previous_line = _previous_reportable_line(reportable_line_set, from_line)
        if previous_line is None or previous_line not in recorded_line_set:
            continue

        forward_targets = {to_line for to_line in to_lines if to_line > from_line}
        if not forward_targets:
            continue

        body_target = min(forward_targets)
        skipped_targets = to_lines - {body_target}
        first_skipped_target = min(skipped_targets) if skipped_targets else SOURCE_EXIT
        if body_target in recorded_line_set or any(
            raw_from_line == from_line and body_target <= raw_to_line < first_skipped_target for raw_from_line, raw_to_line in recorded_arcs
        ):
            covered_branch_arcs.add((from_line, body_target))

        predecessor_lines = {previous_line, from_line - 1}
        if not any(
            raw_from_line in predecessor_lines and (raw_to_line < from_line or raw_to_line >= first_skipped_target)
            for raw_from_line, raw_to_line in recorded_arcs
        ):
            continue

        for skipped_target in skipped_targets:
            covered_branch_arcs.add((from_line, skipped_target))

    return covered_branch_arcs


def _previous_reportable_line(reportable_lines: Collection[int], line_number: int) -> int | None:
    """Return the nearest reportable line before ``line_number``."""
    return next((line for line in sorted(reportable_lines, reverse=True) if line < line_number), None)


def find_reportable_jinja_lines(filename: Path) -> frozenset[int]:
    """Return reportable source lines for a Jinja template with file-stamp cache invalidation."""
    if (stamp := file_stamp(filename)) is None:
        return frozenset()

    return _find_reportable_jinja_lines_cached(filename.resolve(), stamp)


@lru_cache(maxsize=4096)
def _find_reportable_jinja_lines_cached(filename: Path, stamp: FileStamp) -> frozenset[int]:  # noqa: ARG001
    """
    Parse a Jinja template and identify lines that represent source behavior.

    Jinja's AST does not make static text output look like normal statements,
    so reportable lines are a union of AST nodes, static data tokens, and
    selected control-statement block starts. ``stamp`` participates only
    in cache invalidation.
    """
    try:
        source = filename.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return frozenset()

    try:
        from jinja2 import Environment, TemplateSyntaxError, nodes  # noqa: PLC0415
    except ImportError:
        return frozenset()

    environment = Environment(extensions=JINJA2_EXTENSIONS)  # noqa: S701
    try:
        parsed_template = environment.parse(source)
    except TemplateSyntaxError:
        return frozenset()

    ignored_nodes = (nodes.Output, nodes.Template)
    reportable_lines: set[int] = set()
    nodes_to_visit = list(parsed_template.iter_child_nodes())
    while nodes_to_visit:
        node = nodes_to_visit.pop()
        if isinstance(node, nodes.Stmt) and not isinstance(node, ignored_nodes):
            lineno = getattr(node, "lineno", None)
            if isinstance(lineno, int) and lineno > 0:
                reportable_lines.add(lineno)

        nodes_to_visit.extend(node.iter_child_nodes())

    reportable_lines.update(line_number for line_number, _line_text in static_template_lines(source))
    reportable_lines = _expand_tag_ranges(source, reportable_lines | _variable_statement_lines(source) | _control_statement_lines(source))
    return frozenset(reportable_lines)


@lru_cache(maxsize=4096)
def _find_structural_control_label_lines_cached(filename: Path, stamp: FileStamp) -> frozenset[int]:  # noqa: ARG001
    """Return structural control labels used only as branch arc endpoints."""
    try:
        source = filename.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return frozenset()

    return frozenset(_control_statement_lines(source, names={"endif"}))


def static_template_lines(source: str) -> tuple[tuple[int, str], ...]:
    """Return static-data lines from a Jinja source template."""
    try:
        from jinja2 import Environment  # noqa: PLC0415
    except ImportError:
        return ()

    environment = Environment(extensions=JINJA2_EXTENSIONS)  # noqa: S701
    source_lines = source.splitlines()
    static_lines: list[tuple[int, str]] = []
    try:
        tokens = environment.lex(source)
        for lineno, kind, value in tokens:
            if kind == "data":
                static_lines.extend(_numbered_static_lines(lineno, value, source_lines))
    except Exception:
        return ()

    return tuple(static_lines)


def source_tag_ranges(source_filename: Path) -> dict[int, tuple[int, int]]:
    """Return source line to full executable Jinja tag range mappings."""
    try:
        source = source_filename.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return {}

    return tag_ranges_by_line(source)


def _expand_tag_ranges(source: str, line_numbers: set[int]) -> set[int]:
    """Expand any line inside a Jinja tag to the full tag source range."""
    tag_ranges = tag_ranges_by_line(source)
    expanded_lines: set[int] = set()
    for line_number in line_numbers:
        start_line, end_line = tag_ranges.get(line_number, (line_number, line_number))
        expanded_lines.update(range(start_line, end_line + 1))

    return expanded_lines


def tag_ranges_by_line(source: str) -> dict[int, tuple[int, int]]:
    """Return line mappings for block and variable tags, including multiline tags."""
    try:
        from jinja2 import Environment  # noqa: PLC0415
    except ImportError:
        return {}

    environment = Environment(extensions=JINJA2_EXTENSIONS)  # noqa: S701
    tag_ranges: dict[int, tuple[int, int]] = {}
    tag_start_line: int | None = None
    end_kinds: set[str] = set()
    try:
        for lineno, kind, _value in environment.lex(source):
            if kind == "block_begin":
                tag_start_line = lineno
                end_kinds = {"block_end"}
                continue

            if kind == "variable_begin":
                tag_start_line = lineno
                end_kinds = {"variable_end"}
                continue

            if tag_start_line is not None and kind in end_kinds:
                tag_range = (tag_start_line, lineno)
                for line_number in range(tag_start_line, lineno + 1):
                    tag_ranges[line_number] = tag_range
                tag_start_line = None
                end_kinds = set()
    except Exception:
        return {}

    return tag_ranges


def else_branch_line_ranges(source_filename: Path) -> dict[int, tuple[int, int]]:
    """Return first else-body reportable line to else-tag range mappings."""
    try:
        source = source_filename.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return {}

    try:
        from jinja2 import Environment, TemplateSyntaxError, nodes  # noqa: PLC0415
    except ImportError:
        return {}

    environment = Environment(extensions=JINJA2_EXTENSIONS)  # noqa: S701
    try:
        parsed_template = environment.parse(source)
    except TemplateSyntaxError:
        return {}

    reportable_lines = find_reportable_jinja_lines(source_filename)
    tag_ranges = tag_ranges_by_line(source)
    else_lines = _control_statement_lines(source, names={"else"})
    else_branch_line_ranges: dict[int, tuple[int, int]] = {}
    for node in parsed_template.find_all((nodes.If, nodes.For)):
        if not node.else_:
            continue

        first_else_node_line = min(getattr(child_node, "lineno", 0) for child_node in node.else_)
        else_line = next((line for line in sorted(else_lines, reverse=True) if node.lineno < line <= first_else_node_line), None)
        if else_line is None:
            continue

        body_line = _first_reportable_line_in_nodes(reportable_lines, node.else_, after_line=_tag_end_line(else_line, tag_ranges))
        if body_line is not None:
            else_branch_line_ranges[body_line] = (else_line, body_line)

    return else_branch_line_ranges


def _variable_statement_lines(source: str) -> set[int]:
    """Return source lines for Jinja variable statements."""
    try:
        from jinja2 import Environment  # noqa: PLC0415
    except ImportError:
        return set()

    environment = Environment(extensions=JINJA2_EXTENSIONS)  # noqa: S701
    try:
        return {lineno for lineno, kind, _value in environment.lex(source) if kind == "variable_begin"}
    except Exception:
        return set()


def _control_statement_lines(source: str, names: set[str] | None = None) -> set[int]:
    """
    Return block-start lines for control statements that should be reportable.

    Jinja may attach a node line to the expression inside a block rather than
    to the ``{%`` line itself. Lexing preserves the block-start line, so this
    helper adds the source line for ``if``, ``elif``, and ``for`` statements.
    """
    names = names or {"if", "elif", "else", "for"}
    return {line_number for line_number, name in block_statement_lines(source) if name in names}


def if_endif_lines(source: str) -> dict[int, int]:
    """Return matching source ``endif`` lines for each ``if`` and ``elif`` line."""
    endif_lines_by_conditional_line: dict[int, int] = {}
    if_stack: list[list[int]] = []
    for block_lineno, block_name in block_statement_lines(source):
        if block_name == "if":
            if_stack.append([block_lineno])
        elif block_name == "elif" and if_stack:
            if_stack[-1].append(block_lineno)
        elif block_name == "endif" and if_stack:
            for conditional_line in if_stack.pop():
                endif_lines_by_conditional_line[conditional_line] = block_lineno

    return endif_lines_by_conditional_line


def block_statement_lines(source: str) -> tuple[tuple[int, str], ...]:
    """Return the first statement name and source line for each Jinja block."""
    try:
        from jinja2 import Environment  # noqa: PLC0415
    except ImportError:
        return ()

    environment = Environment(extensions=JINJA2_EXTENSIONS)  # noqa: S701
    block_statements: list[tuple[int, str]] = []
    in_block = False
    block_lineno = 0
    try:
        for lineno, kind, value in environment.lex(source):
            if kind == "block_begin":
                in_block = True
                block_lineno = lineno
            elif in_block and kind == "name":
                block_statements.append((block_lineno, value))
                in_block = False
            elif kind == "block_end":
                in_block = False
    except Exception:
        return ()

    return tuple(block_statements)


def _numbered_static_lines(start_lineno: int, value: str, source_lines: list[str]) -> list[tuple[int, str]]:
    """Split a Jinja static-data token into stripped source lines with line numbers."""
    numbered_lines: list[tuple[int, str]] = []
    line_number = start_lineno
    for line in value.splitlines(keepends=True):
        line_without_newline = line.removesuffix("\n").removesuffix("\r")
        stripped_line = line_without_newline.strip()
        if stripped_line or _source_line_is_blank(line_number, source_lines):
            numbered_lines.append((line_number, stripped_line))

        if line.endswith(("\n", "\r")):
            line_number += 1

    return numbered_lines


def _source_line_is_blank(line_number: int, source_lines: list[str]) -> bool:
    """Return whether a source line is whitespace-only."""
    return 0 < line_number <= len(source_lines) and not source_lines[line_number - 1].strip()


def rendered_static_lines(value: str) -> list[str]:
    """Return stripped rendered static lines, including intentional blank lines."""
    rendered_lines: list[str] = []
    for index, line in enumerate(value.splitlines(keepends=True)):
        line_without_newline = line.removesuffix("\n").removesuffix("\r")
        stripped_line = line_without_newline.strip()
        if stripped_line:
            rendered_lines.append(stripped_line)
        elif index > 0:
            rendered_lines.append("")

    return rendered_lines


def find_possible_jinja_arcs(source_filename: Path) -> frozenset[tuple[int, int]]:
    """Return possible source-level branch arcs for a template with file-stamp cache invalidation."""
    if (stamp := file_stamp(source_filename)) is None:
        return frozenset()

    reportable_lines = find_reportable_jinja_lines(source_filename)
    structural_control_label_lines = _find_structural_control_label_lines_cached(source_filename.resolve(), stamp)
    return _find_possible_jinja_arcs_cached(
        source_filename.resolve(),
        stamp,
        reportable_lines,
        _arc_endpoint_lines(reportable_lines, structural_control_label_lines),
    )


@lru_cache(maxsize=4096)
def _find_possible_jinja_arcs_cached(
    source_filename: Path,
    stamp: FileStamp,  # noqa: ARG001
    reportable_lines: frozenset[int],
    arc_endpoint_lines: frozenset[int],
) -> frozenset[tuple[int, int]]:
    """
    Parse supported Jinja control flow into possible source-level branch arcs.

    The model intentionally covers only common source constructs where a
    source-level branch is useful: ``if``/``elif``/``else`` and ``for`` with an
    explicit ``else``. ``stamp`` is used only for cache invalidation.
    """
    try:
        source = source_filename.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return frozenset()

    try:
        from jinja2 import Environment, TemplateSyntaxError, nodes  # noqa: PLC0415
    except ImportError:
        return frozenset()

    environment = Environment(extensions=JINJA2_EXTENSIONS)  # noqa: S701
    try:
        parsed_template = environment.parse(source)
    except TemplateSyntaxError:
        return frozenset()

    tag_ranges = tag_ranges_by_line(source)
    endif_lines_by_conditional_line = if_endif_lines(source)
    elif_node_ids = {id(elif_node) for if_node in parsed_template.find_all(nodes.If) for elif_node in if_node.elif_}
    arcs: set[tuple[int, int]] = set()
    for node in parsed_template.find_all((nodes.If, nodes.For)):
        if isinstance(node, nodes.If):
            if id(node) in elif_node_ids:
                continue
            _add_if_arcs(node, reportable_lines, arc_endpoint_lines, tag_ranges, endif_lines_by_conditional_line, arcs)
        elif isinstance(node, nodes.For):
            _add_for_arcs(node, reportable_lines, arc_endpoint_lines, tag_ranges, arcs)

    return frozenset(arcs)


def _add_if_arcs(
    node: Any,
    reportable_lines: Collection[int],
    arc_endpoint_lines: Collection[int],
    tag_ranges: Mapping[int, tuple[int, int]],
    endif_lines_by_conditional_line: Mapping[int, int],
    arcs: set[tuple[int, int]],
) -> None:
    """Add possible arcs from a Jinja ``if`` node and any ``elif`` nodes."""
    after_line = _next_reportable_line(reportable_lines, _node_end_lineno(node))
    conditional_nodes = [node, *node.elif_]
    for index, conditional_node in enumerate(conditional_nodes):
        conditional_end_line = _tag_end_line(conditional_node.lineno, tag_ranges)
        body_line = _first_reportable_line_in_nodes(
            reportable_lines,
            conditional_node.body,
            after_line=conditional_end_line,
        )
        false_line = _false_if_target(node, conditional_nodes, index, reportable_lines, endif_lines_by_conditional_line, after_line)

        _add_arc(arcs, conditional_node.lineno, body_line, arc_endpoint_lines)
        _add_arc(arcs, conditional_node.lineno, false_line, arc_endpoint_lines)


def _false_if_target(
    node: Any,
    conditional_nodes: list[Any],
    index: int,
    reportable_lines: Collection[int],
    endif_lines_by_conditional_line: Mapping[int, int],
    after_line: int,
) -> int | None:
    """Return the source line reached when one ``if`` or ``elif`` condition is false."""
    if index + 1 < len(conditional_nodes):
        return conditional_nodes[index + 1].lineno
    if node.else_:
        return _first_reportable_line_in_nodes(reportable_lines, node.else_)

    return endif_lines_by_conditional_line.get(conditional_nodes[index].lineno, after_line)


def _add_for_arcs(
    node: Any,
    reportable_lines: Collection[int],
    arc_endpoint_lines: Collection[int],
    tag_ranges: Mapping[int, tuple[int, int]],
    arcs: set[tuple[int, int]],
) -> None:
    """Add possible arcs from a Jinja ``for`` node to its body and explicit ``else`` block."""
    body_line = _first_reportable_line_in_nodes(reportable_lines, node.body, after_line=_tag_end_line(node.lineno, tag_ranges))

    _add_arc(arcs, node.lineno, body_line, arc_endpoint_lines)
    if node.else_:
        _add_arc(arcs, node.lineno, _first_reportable_line_in_nodes(reportable_lines, node.else_), arc_endpoint_lines)


@lru_cache(maxsize=4096)
def _find_jinja_arc_aliases_cached(
    source_filename: Path,
    stamp: FileStamp,  # noqa: ARG001
    possible_arcs: frozenset[tuple[int, int]],
    reportable_lines: frozenset[int],
) -> dict[tuple[int, int], tuple[int, int]]:
    """
    Return observed runtime arcs that should be normalized to source arcs.

    No-else ``if`` blocks use the source ``endif`` line as the canonical false
    branch target. When such an ``if`` is the last executed statement in a loop
    iteration, Jinja can record the false path as a jump back to the enclosing
    ``for`` line instead.
    """
    try:
        source = source_filename.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return {}

    try:
        from jinja2 import Environment, TemplateSyntaxError, nodes  # noqa: PLC0415
    except ImportError:
        return {}

    environment = Environment(extensions=JINJA2_EXTENSIONS)  # noqa: S701
    try:
        parsed_template = environment.parse(source)
    except TemplateSyntaxError:
        return {}

    possible_arc_set = set(possible_arcs)
    reportable_line_set = set(reportable_lines)
    endif_lines_by_conditional_line = if_endif_lines(source)
    aliases: dict[tuple[int, int], tuple[int, int]] = {}

    def visit_statements(statements: list[Any], enclosing_for_lines: tuple[int, ...] = ()) -> None:
        for statement in statements:
            if isinstance(statement, nodes.For):
                visit_statements(statement.body, (*enclosing_for_lines, statement.lineno))
                visit_statements(statement.else_, enclosing_for_lines)
                continue

            if isinstance(statement, nodes.If):
                _add_no_else_if_loop_backedge_aliases(
                    aliases,
                    statement,
                    enclosing_for_lines,
                    endif_lines_by_conditional_line,
                    possible_arc_set,
                    reportable_line_set,
                )
                for conditional_node in (statement, *statement.elif_):
                    visit_statements(conditional_node.body, enclosing_for_lines)

                visit_statements(statement.else_, enclosing_for_lines)

    visit_statements(parsed_template.body)
    return aliases


def _add_no_else_if_loop_backedge_aliases(
    aliases: dict[tuple[int, int], tuple[int, int]],
    node: Any,
    enclosing_for_lines: tuple[int, ...],
    endif_lines_by_conditional_line: Mapping[int, int],
    possible_arcs: set[tuple[int, int]],
    reportable_lines: set[int],
) -> None:
    """Add aliases from loop backedges to canonical no-else ``if`` false arcs."""
    if not enclosing_for_lines or node.elif_ or node.else_:
        return

    endif_line = endif_lines_by_conditional_line.get(node.lineno)
    if endif_line is None or endif_line in reportable_lines or (node.lineno, endif_line) not in possible_arcs:
        return

    canonical_arc = (node.lineno, endif_line)
    for for_line in enclosing_for_lines:
        aliases[(node.lineno, for_line)] = canonical_arc


def _first_reportable_line_in_nodes(reportable_lines: Collection[int], nodes, after_line: int = 0) -> int | None:  # noqa: ANN001
    """Return the first reportable line associated with a list of Jinja AST nodes."""
    if not nodes:
        return None

    start_line = min(getattr(node, "lineno", 0) for node in nodes)
    end_line = max(_node_end_lineno(node) for node in nodes)
    if line := next((line for line in sorted(reportable_lines) if line > after_line and start_line <= line <= end_line), None):
        return line

    return _next_reportable_line(reportable_lines, max(after_line, start_line - 1))


def _next_reportable_line(reportable_lines: Collection[int], line_number: int) -> int:
    """Return the next reportable line after ``line_number`` or the source-exit sentinel."""
    return next((line for line in sorted(reportable_lines) if line > line_number), SOURCE_EXIT)


def _tag_end_line(line_number: int, tag_ranges: Mapping[int, tuple[int, int]]) -> int:
    """Return the end line of the Jinja tag containing ``line_number``."""
    return tag_ranges.get(line_number, (line_number, line_number))[1]


def _node_end_lineno(node) -> int:  # noqa: ANN001
    """Return the greatest source line used by a Jinja AST node and its children."""
    node_lines = [getattr(node, "lineno", 0)]
    nodes_to_visit = list(node.iter_child_nodes())
    while nodes_to_visit:
        child_node = nodes_to_visit.pop()
        if isinstance((lineno := getattr(child_node, "lineno", None)), int):
            node_lines.append(lineno)
        nodes_to_visit.extend(child_node.iter_child_nodes())

    return max(node_lines)


def _add_arc(arcs: set[tuple[int, int]], from_line: int, to_line: int | None, arc_endpoint_lines: Collection[int]) -> None:
    """Add a branch arc when both endpoints belong to the source endpoint model."""
    if to_line is None or from_line == to_line:
        return

    if from_line not in arc_endpoint_lines or (to_line > 0 and to_line not in arc_endpoint_lines):
        return

    arcs.add((from_line, to_line))


def find_no_branch_jinja_lines(source_filename: Path) -> frozenset[int]:
    """Return source lines that should be excused from branch coverage with cache invalidation."""
    if (stamp := file_stamp(source_filename)) is None:
        return frozenset()

    return _find_no_branch_jinja_lines_cached(source_filename.resolve(), stamp)


@lru_cache(maxsize=4096)
def _find_no_branch_jinja_lines_cached(source_filename: Path, stamp: FileStamp) -> frozenset[int]:  # noqa: ARG001
    """
    Find top-level optional guards that should not count as partial branches.

    Many AVD templates wrap optional feature sections in a top-level ``if``
    without an ``elif`` or ``else``. Reporting the absent path as a missing
    branch creates broad noise, so these simple guards are marked no-branch.
    ``stamp`` is used only for cache invalidation.
    """
    try:
        source = source_filename.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return frozenset()

    try:
        from jinja2 import Environment, TemplateSyntaxError, nodes  # noqa: PLC0415
    except ImportError:
        return frozenset()

    environment = Environment(extensions=JINJA2_EXTENSIONS)  # noqa: S701
    try:
        parsed_template = environment.parse(source)
    except TemplateSyntaxError:
        return frozenset()

    return frozenset(node.lineno for node in parsed_template.body if isinstance(node, nodes.If) and not node.elif_ and not node.else_)
