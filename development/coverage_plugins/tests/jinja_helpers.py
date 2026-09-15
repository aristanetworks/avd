# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, cast

from coverage import Coverage
from coverage_plugins.jinja import JinjaTemplateCoveragePlugin
from jinja2 import Environment, FileSystemLoader, ModuleLoader

if TYPE_CHECKING:
    from pathlib import Path
    from types import FrameType

    from coverage.results import Analysis


class _FakeFrame:
    def __init__(self, f_lineno: int) -> None:
        self.f_lineno = f_lineno


def _frame(line_number: int) -> FrameType:
    return cast("FrameType", _FakeFrame(line_number))


def _coverage_for_template(tmp_path: Path, template_root: Path, compiled_root: Path, *, branch: bool = False) -> Coverage:
    coverage = Coverage(
        config_file=False,
        data_file=str(tmp_path / ".coverage"),
        branch=branch,
        source=[str(template_root), str(compiled_root)],
        plugins=[lambda reg: reg.add_file_tracer(JinjaTemplateCoveragePlugin(compiled_template_roots=(compiled_root,)))],
    )
    coverage.config.core = "ctrace"
    return coverage


def _analyze_rendered_template(tmp_path: Path, source: str, context: dict[str, object]) -> Analysis:
    return _analyze_rendered_template_contexts(tmp_path, source, [context])


def _analyze_rendered_template_contexts(tmp_path: Path, source: str, contexts: list[dict[str, object]]) -> Analysis:
    template_root = tmp_path / "j2templates"
    compiled_root = template_root / "compiled_templates"
    source_file = template_root / "template.j2"

    template_root.mkdir()
    compiled_root.mkdir()
    source_file.write_text(source, encoding="utf-8")

    Environment(loader=FileSystemLoader(template_root)).compile_templates(compiled_root, zip=None, ignore_errors=False)  # noqa: S701
    environment = Environment(loader=ModuleLoader(compiled_root))  # noqa: S701
    coverage = _coverage_for_template(tmp_path, template_root, compiled_root, branch=True)
    coverage.erase()
    coverage.start()
    for context in contexts:
        environment.get_template("template.j2").render(**context)
    coverage.stop()
    coverage.save()

    return cast("Analysis", coverage._analyze(str(source_file.resolve())))
