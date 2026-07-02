# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Compiled-template reporting helpers for the Jinja coverage plugin."""

from __future__ import annotations

import ast
from functools import lru_cache
from pathlib import Path
from types import MappingProxyType
from typing import TYPE_CHECKING

from .models import CompiledTemplate, FileStamp, file_stamp
from .source_template import block_statement_lines, else_branch_line_ranges, if_endif_lines, rendered_static_lines, source_tag_ranges, static_template_lines

if TYPE_CHECKING:
    from collections.abc import Mapping


def parse_compiled_template(compiled_filename: Path, compiled_root: Path) -> CompiledTemplate | None:
    """
    Resolve and parse a compiled Jinja Python module with stamp-based cache invalidation.

    The mapping result depends on both the generated Python module and the
    source ``.j2`` template. The wrapper reads file stamps first and passes
    those stamps into cached helpers so edits to either file invalidate the
    cached mapping.
    """
    compiled_filename = compiled_filename.resolve()
    compiled_root = compiled_root.resolve()
    if (compiled_stamp := file_stamp(compiled_filename)) is None:
        return None

    source_filename = _resolve_compiled_template_source_filename(compiled_filename, compiled_root, compiled_stamp)
    if source_filename is None:
        return None

    if (source_stamp := file_stamp(source_filename)) is None:
        return None

    return _parse_compiled_template_cached(compiled_filename, source_filename.resolve(), compiled_stamp, source_stamp)


@lru_cache(maxsize=4096)
def _parse_compiled_template_cached(
    compiled_filename: Path,
    source_filename: Path,
    compiled_stamp: FileStamp,  # noqa: ARG001
    source_stamp: FileStamp,  # noqa: ARG001
) -> CompiledTemplate | None:
    """
    Build immutable line mappings for one compiled template.

    ``compiled_stamp`` and ``source_stamp`` are intentionally unused inside the
    function body. They are part of the cache key so repeated tracing of the
    same generated module is cheap, while file rewrites still invalidate stale
    mappings.
    """
    try:
        tree = ast.parse(compiled_filename.read_text(encoding="utf-8"), filename=str(compiled_filename))
    except (OSError, SyntaxError, UnicodeDecodeError):
        return None

    constants = _module_string_constants(tree)
    debug_info = constants.get("debug_info")
    if debug_info is None:
        return None

    debug_map = _parse_debug_info(debug_info)
    generated_line_ranges = _generated_line_ranges(tree, source_filename, debug_map)
    return CompiledTemplate(
        source_filename=str(source_filename),
        debug_map=debug_map,
        generated_line_ranges=MappingProxyType(generated_line_ranges),
    )


@lru_cache(maxsize=4096)
def _resolve_compiled_template_source_filename(compiled_filename: Path, compiled_root: Path, compiled_stamp: FileStamp) -> Path | None:  # noqa: ARG001
    """
    Read a compiled module's ``name`` constant and resolve it to a source template path.

    The generated Jinja module records the original template name in a module
    constant. ``compiled_stamp`` is included only as cache invalidation input.
    """
    try:
        tree = ast.parse(compiled_filename.read_text(encoding="utf-8"), filename=str(compiled_filename))
    except (OSError, SyntaxError, UnicodeDecodeError):
        return None

    constants = _module_string_constants(tree)
    template_name = constants.get("name")
    if template_name is None or constants.get("debug_info") is None:
        return None

    return _resolve_template_source_filename(template_name, compiled_root)


def _generated_line_ranges(tree: ast.Module, source_filename: Path, debug_map: tuple[tuple[int, int], ...]) -> dict[int, tuple[int, int]]:
    """Return generated-line mappings for Jinja tag ranges and static output ranges."""
    tag_ranges = source_tag_ranges(source_filename)
    else_line_ranges = else_branch_line_ranges(source_filename)
    generated_line_ranges = {generated_line: tag_ranges.get(template_line, (template_line, template_line)) for generated_line, template_line in debug_map}
    generated_line_ranges.update(_generated_static_line_ranges(tree, source_filename, debug_map))
    generated_line_ranges.update(_generated_endif_line_ranges(tree, source_filename, debug_map, generated_line_ranges))
    for generated_line, (start_line, end_line) in generated_line_ranges.items():
        if else_branch_range := else_line_ranges.get(start_line):
            generated_line_ranges[generated_line] = (else_branch_range[0], end_line)

    return generated_line_ranges


def _generated_endif_line_ranges(
    tree: ast.Module,
    source_filename: Path,
    debug_map: tuple[tuple[int, int], ...],
    existing_line_ranges: Mapping[int, tuple[int, int]],
) -> dict[int, tuple[int, int]]:
    """Map generated post-if statements to the matching source ``endif`` label."""
    try:
        source = source_filename.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return {}

    endif_lines_by_conditional_line = if_endif_lines(source)
    if not endif_lines_by_conditional_line:
        return {}

    source_lines_by_generated_line = dict(debug_map)
    endif_ranges: dict[int, tuple[int, int]] = {}

    def visit_statements(statements: list[ast.stmt]) -> None:
        for index, statement in enumerate(statements):
            source_line = source_lines_by_generated_line.get(statement.lineno) if isinstance(statement, ast.If) else None
            if source_line is not None and (endif_line := endif_lines_by_conditional_line.get(source_line)) is not None and index + 1 < len(statements):
                next_generated_line = statements[index + 1].lineno
                existing_start_line, existing_end_line = existing_line_ranges.get(next_generated_line, (endif_line, endif_line))
                endif_ranges[next_generated_line] = (min(endif_line, existing_start_line), max(endif_line, existing_end_line))

            for _field_name, value in ast.iter_fields(statement):
                if isinstance(value, list) and value and all(isinstance(item, ast.stmt) for item in value):
                    visit_statements(value)

    visit_statements(tree.body)
    return endif_ranges


def _module_string_constants(tree: ast.Module) -> dict[str, str]:
    """Return top-level string assignments from a compiled Jinja module AST."""
    constants: dict[str, str] = {}
    for node in tree.body:
        if not isinstance(node, ast.Assign) or not isinstance(node.value, ast.Constant) or not isinstance(node.value.value, str):
            continue

        for target in node.targets:
            if isinstance(target, ast.Name):
                constants[target.id] = node.value.value

    return constants


def _resolve_template_source_filename(template_name: str, compiled_root: Path) -> Path | None:
    """
    Resolve a Jinja template name from a compiled module to an existing source file.

    The source template root is the parent of the configured
    ``compiled_templates`` directory. The resolved path must stay within that
    root to avoid trusting arbitrary paths from generated module constants.
    """
    template_root = compiled_root.parent.resolve()
    source_filename = template_root.joinpath(*Path(template_name.replace("\\", "/")).parts).resolve()
    if not source_filename.is_relative_to(template_root) or not source_filename.is_file():
        return None

    return source_filename


def _parse_debug_info(debug_info: str) -> tuple[tuple[int, int], ...]:
    """Parse Jinja's ``debug_info`` string into ``(generated_line, template_line)`` pairs."""
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


def _generated_static_line_ranges(tree: ast.Module, source_filename: Path, debug_map: tuple[tuple[int, int], ...]) -> dict[int, tuple[int, int]]:
    """
    Map generated ``yield 'static text'`` lines back to source template ranges.

    Jinja ``debug_info`` does not reliably credit static output text to source
    lines. This function uses generated literal-yield nodes as runtime evidence
    and matches their rendered lines back to the static text tokens in the source
    template. Whitespace-only static lines are included since documentation
    templates intentionally render blank lines for Markdown structure.
    """
    try:
        source = source_filename.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return {}

    source_static_lines = static_template_lines(source)
    if not source_static_lines:
        return {}

    ranges: dict[int, tuple[int, int]] = {}
    source_index = 0
    blank_only_yield_lines = _blank_only_yield_lines_by_generated_line(tree, source, source_static_lines, debug_map)
    yield_nodes = sorted(
        (node for node in ast.walk(tree) if isinstance(node, ast.Yield)),
        key=lambda node: node.lineno,
    )
    for node in yield_nodes:
        if not isinstance(node, ast.Yield) or not isinstance(node.value, ast.Constant) or not isinstance(node.value.value, str):
            continue

        rendered_lines = rendered_static_lines(node.value.value)
        if not rendered_lines:
            if not node.value.value.strip() and (line_number := blank_only_yield_lines.get(node.lineno)) is not None:
                ranges[node.lineno] = (line_number, line_number)
                if (matched_index := _find_static_line_index(source_static_lines, line_number, source_index)) is not None:
                    source_index = matched_index + 1

            continue

        matched_line_numbers: list[int] = []
        next_source_index = source_index
        if (
            node.value.value.startswith(("\n", "\r"))
            and rendered_lines[0]
            and next_source_index < len(source_static_lines)
            and not source_static_lines[next_source_index][1]
        ):
            matched_line_numbers.append(source_static_lines[next_source_index][0])
            next_source_index += 1

        for rendered_line in rendered_lines:
            matched_index = _find_next_static_line(source_static_lines, rendered_line, next_source_index)
            if matched_index is None:
                if rendered_line:
                    matched_line_numbers.clear()
                    break

                continue

            matched_line_numbers.append(source_static_lines[matched_index][0])
            next_source_index = matched_index + 1

        if matched_line_numbers:
            ranges[node.lineno] = (matched_line_numbers[0], matched_line_numbers[-1])
            source_index = next_source_index

    return ranges


def _blank_only_yield_lines_by_generated_line(
    tree: ast.Module,
    source: str,
    source_static_lines: tuple[tuple[int, str], ...],
    debug_map: tuple[tuple[int, int], ...],
) -> dict[int, int]:
    """Return generated yield lines that should be credited to blank-only source lines."""
    source_lines_by_generated_line = dict(debug_map)
    first_blank_source_line_by_block_line = _first_blank_source_line_before_next_block(source, source_static_lines)
    else_line_by_conditional_line = _else_line_by_conditional_line(source)
    blank_only_yield_lines: dict[int, int] = {}
    for node in ast.walk(tree):
        if not isinstance(node, ast.If):
            continue

        source_line = source_lines_by_generated_line.get(node.lineno)
        if source_line is None:
            continue

        _add_blank_only_yield_line(blank_only_yield_lines, node.body, source_line, first_blank_source_line_by_block_line)
        if else_line := else_line_by_conditional_line.get(source_line):
            _add_blank_only_yield_line(blank_only_yield_lines, node.orelse, else_line, first_blank_source_line_by_block_line)

    return blank_only_yield_lines


def _add_blank_only_yield_line(
    blank_only_yield_lines: dict[int, int],
    statements: list[ast.stmt],
    source_line: int,
    first_blank_source_line_by_block_line: dict[int, int],
) -> None:
    """Add the first blank-only yield generated for one control-flow body."""
    if source_line not in first_blank_source_line_by_block_line or not statements:
        return

    first_statement = next((statement for statement in statements if not isinstance(statement, ast.Pass)), None)
    if (
        isinstance(first_statement, ast.Expr)
        and isinstance(first_statement.value, ast.Yield)
        and isinstance(first_statement.value.value, ast.Constant)
        and isinstance(first_statement.value.value.value, str)
        and not first_statement.value.value.value.strip()
    ):
        blank_only_yield_lines[first_statement.value.lineno] = first_blank_source_line_by_block_line[source_line]


def _first_blank_source_line_before_next_block(source: str, source_static_lines: tuple[tuple[int, str], ...]) -> dict[int, int]:
    """Return the first blank static source line immediately inside a control-flow body."""
    block_lines = block_statement_lines(source)
    blank_static_lines = [line_number for line_number, line_text in source_static_lines if not line_text]
    blank_source_lines_by_block_line: dict[int, int] = {}
    for block_line, block_name in block_lines:
        if block_name not in {"if", "elif", "else"}:
            continue

        next_block_line = next((line_number for line_number, _name in block_lines if line_number > block_line), None)
        blank_line = next((line_number for line_number in blank_static_lines if line_number > block_line), None)
        if blank_line is not None and (next_block_line is None or blank_line < next_block_line):
            blank_source_lines_by_block_line[block_line] = blank_line

    return blank_source_lines_by_block_line


def _else_line_by_conditional_line(source: str) -> dict[int, int]:
    """Return matching source ``else`` lines for ``if`` and ``elif`` conditions."""
    else_lines_by_conditional_line: dict[int, int] = {}
    conditional_line_stack: list[int] = []
    for block_line, block_name in block_statement_lines(source):
        if block_name == "if":
            conditional_line_stack.append(block_line)
        elif block_name == "elif" and conditional_line_stack:
            conditional_line_stack[-1] = block_line
        elif block_name == "else" and conditional_line_stack:
            else_lines_by_conditional_line[conditional_line_stack[-1]] = block_line
        elif block_name == "endif" and conditional_line_stack:
            conditional_line_stack.pop()

    return else_lines_by_conditional_line


def _find_static_line_index(source_static_lines: tuple[tuple[int, str], ...], line_number: int, start_index: int) -> int | None:
    """Find a source static line by source line number."""
    for index, (source_line_number, _source_line) in enumerate(source_static_lines[start_index:], start=start_index):
        if source_line_number == line_number:
            return index

    return None


def _find_next_static_line(source_static_lines: tuple[tuple[int, str], ...], rendered_line: str, start_index: int) -> int | None:
    """Find the next source static line matching one rendered static output line."""
    for index, (_line_number, source_line) in enumerate(source_static_lines[start_index:], start=start_index):
        if source_line == rendered_line:
            return index

    return None
