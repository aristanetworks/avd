# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Add explicit false-path line events to generated templates used for coverage."""

from __future__ import annotations

import argparse
import ast
from pathlib import Path
from typing import TYPE_CHECKING, cast

from coverage import Coverage

from . import _configured_compiled_template_roots
from .compiled_parser import _module_string_constants, _parse_debug_info, parse_compiled_template
from .source_template import block_statement_lines, if_endif_lines, source_template

if TYPE_CHECKING:
    from collections.abc import Iterable


def instrument_compiled_templates(compiled_root: Path) -> int:
    """
    Instrument terminal no-else guards in generated root functions, before import.

    A condition-to-function-exit arc alone cannot distinguish a false condition
    from an exception evaluating that condition. An explicit generated ``else:
    pass`` gives the false path its own line event without evaluating anything
    extra or changing the rendered output. Its debug mapping credits only the
    matching source ``endif``. Uninstrumented exit arcs remain uninterpreted.

    Only generated modules are rewritten. Repeating this operation is a no-op.
    Loops, macros, blocks, and generated cleanup continuations are left alone.
    """
    count = 0
    for compiled_filename in sorted(compiled_root.glob("*.py")):
        compiled_template = parse_compiled_template(compiled_filename, compiled_root)
        if compiled_template is None:
            continue

        source_filename = Path(compiled_template.source_filename)
        generated_source = compiled_filename.read_text(encoding="utf-8")
        instrumented_source = _instrument_module(generated_source, source_filename)
        if instrumented_source != generated_source:
            compiled_filename.write_text(instrumented_source, encoding="utf-8")
            # A same-second cached bytecode file can otherwise hide the added events.
            for cached_file in (compiled_root / "__pycache__").glob(f"{compiled_filename.stem}.*.pyc"):
                cached_file.unlink()
            count += 1

    return count


def _instrument_module(generated_source: str, source_filename: Path) -> str:
    """Insert false-path passes and shift every original debug-info mapping."""
    tree = ast.parse(generated_source)
    constants = _module_string_constants(tree)
    if "debug_info" not in constants:
        return generated_source

    debug_assignment = next(
        (
            node
            for node in tree.body
            if isinstance(node, ast.Assign) and any(isinstance(target, ast.Name) and target.id == "debug_info" for target in node.targets)
        ),
        None,
    )
    if debug_assignment is None or debug_assignment.end_lineno != debug_assignment.lineno:
        return generated_source

    debug_map = _parse_debug_info(constants["debug_info"])
    source_lines_by_generated_line = dict(debug_map)
    source = source_filename.read_text(encoding="utf-8")
    template = source_template(source_filename)
    endif_lines = if_endif_lines(source)
    control_lines = [line for line, name in block_statement_lines(source) if name in {"if", "elif"}]
    insertions: dict[int, list[tuple[int, int]]] = {}

    def visit_tail(statements: list[ast.stmt]) -> None:
        if not statements or not isinstance(statement := statements[-1], ast.If):
            return

        # Descend only through root-function conditional arms. A loop backedge,
        # nested function return, or cleanup statement is a different continuation.
        visit_tail(statement.body)
        visit_tail(statement.orelse)
        source_line = source_lines_by_generated_line.get(statement.lineno)
        endif_line = endif_lines.get(source_line) if source_line is not None else None
        if (
            statement.orelse
            or source_line is None
            or endif_line is None
            or statement.end_lineno is None
            or endif_line in template.reportable_lines
            or (source_line, endif_line) not in template.possible_arcs
            or control_lines.count(source_line) != 1
        ):
            return

        tag_end = template.tag_ranges.get(source_line, (source_line, source_line))[1]
        if not any(origin == source_line and tag_end < target < endif_line for origin, target in template.possible_arcs):
            return

        insertions.setdefault(statement.end_lineno, []).append((statement.col_offset, endif_line))

    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == "root":
            visit_tail(node.body)

    if not insertions:
        return generated_source

    generated_lines = generated_source.splitlines(keepends=True)
    instrumented_lines: list[str] = []
    shifted_line_numbers: dict[int, int] = {}
    added_debug_map: list[tuple[int, int]] = []
    for old_line, text in enumerate(generated_lines, start=1):
        shifted_line_numbers[old_line] = len(instrumented_lines) + 1
        instrumented_lines.append(text)
        # Inner terminal guards close before their enclosing terminal guards.
        for indentation, endif_line in sorted(insertions.get(old_line, ()), reverse=True):
            instrumented_lines.append(f"{' ' * indentation}else:\n")
            instrumented_lines.append(f"{' ' * (indentation + 4)}pass\n")
            added_debug_map.append((len(instrumented_lines), endif_line))

    shifted_debug_map = [(shifted_line_numbers[generated_line], source_line) for generated_line, source_line in debug_map]
    debug_info = "&".join(f"{source_line}={generated_line}" for generated_line, source_line in sorted([*shifted_debug_map, *added_debug_map]))
    instrumented_lines[shifted_line_numbers[debug_assignment.lineno] - 1] = f"debug_info = {debug_info!r}\n"
    instrumented_source = "".join(instrumented_lines)
    ast.parse(instrumented_source)
    return instrumented_source


def main() -> None:
    """Instrument the roots configured for the Jinja plugin in a coverage config."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rcfile", default="pyproject.toml")
    args = parser.parse_args()
    coverage = Coverage(config_file=args.rcfile)
    options = coverage.config.plugin_options.get("coverage_plugins.jinja", {})
    configured_roots = options.get("compiled_template_roots")
    if not configured_roots:
        parser.error("coverage_plugins.jinja requires compiled_template_roots in the coverage config")
    roots = _configured_compiled_template_roots(
        cast("Iterable[str | Path] | str | Path", configured_roots),
        cast("str | None", options.get("package")),
    )
    for root in roots:
        if not root.is_dir():
            parser.error(f"compiled template root does not exist: {root}")
        print(f"Instrumented {instrument_compiled_templates(root)} templates in {root}")  # noqa: T201


if __name__ == "__main__":
    main()
