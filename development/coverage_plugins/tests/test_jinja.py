# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import importlib.util
import shutil
from typing import TYPE_CHECKING, cast

import pytest
from coverage import Coverage
from coverage.exceptions import ConfigError
from coverage_plugins.jinja import JinjaTemplateCoveragePlugin, JinjaTemplateFileReporter, coverage_init
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


def test_file_tracer_resolves_source_filename_and_maps_generated_lines(tmp_path: Path) -> None:
    template_root = tmp_path / "j2templates"
    compiled_root = template_root / "compiled_templates"
    source_file = template_root / "nested/simple.j2"
    compiled_file = compiled_root / "nested__simple.py"

    source_file.parent.mkdir(parents=True)
    source_file.write_text("{% if enabled %}\n{{ value }}\n{% endif %}\n", encoding="utf-8")
    compiled_root.mkdir()
    compiled_file.write_text(
        "name = 'nested/simple.j2'\ndef root(context):\n    pass\ndebug_info = '1=10&2=15&3=30'\n",
        encoding="utf-8",
    )

    tracer = JinjaTemplateCoveragePlugin(compiled_template_roots=(compiled_root,)).file_tracer(str(compiled_file))

    assert tracer is not None
    assert tracer.source_filename() == str(source_file.resolve())
    assert tracer.line_number_range(_frame(9)) == (-1, -1)
    assert tracer.line_number_range(_frame(10)) == (1, 1)
    assert tracer.line_number_range(_frame(14)) == (-1, -1)
    assert tracer.line_number_range(_frame(15)) == (2, 2)
    assert tracer.line_number_range(_frame(99)) == (-1, -1)


def test_file_tracer_maps_blank_only_yield_after_jinja_pass(tmp_path: Path) -> None:
    template_root = tmp_path / "j2templates"
    compiled_root = template_root / "compiled_templates"
    source_file = template_root / "blank_pass.j2"
    compiled_file = compiled_root / "blank_pass.py"

    template_root.mkdir()
    compiled_root.mkdir()
    source_file.write_text("{% if items %}\n\n{% for item in items %}\n- {{ item }}\n{% endfor %}\n{% endif %}\n", encoding="utf-8")
    compiled_file.write_text(
        "name = 'blank_pass.j2'\n"
        "\n"
        "def root(context):\n"
        "    if context.get('items'):\n"
        "        pass\n"
        "        yield '\\n'\n"
        "        for item in context.get('items'):\n"
        "            yield '- '\n"
        "            yield str(item)\n"
        "debug_info = '1=4&3=7&4=8'\n",
        encoding="utf-8",
    )

    tracer = JinjaTemplateCoveragePlugin(compiled_template_roots=(compiled_root,)).file_tracer(str(compiled_file))

    assert tracer is not None
    assert tracer.line_number_range(_frame(6)) == (2, 2)


def test_file_tracer_maps_blank_only_yield_after_else_pass(tmp_path: Path) -> None:
    template_root = tmp_path / "j2templates"
    compiled_root = template_root / "compiled_templates"
    source_file = template_root / "blank_else.j2"
    compiled_file = compiled_root / "blank_else.py"

    template_root.mkdir()
    compiled_root.mkdir()
    source_file.write_text(
        "{% if enabled %}\ntrue\n{% else %}\n\n{% for item in items %}\n- {{ item }}\n{% endfor %}\n{% endif %}\n",
        encoding="utf-8",
    )
    compiled_file.write_text(
        "name = 'blank_else.j2'\n"
        "\n"
        "def root(context):\n"
        "    if context.get('enabled'):\n"
        "        yield 'true'\n"
        "    else:\n"
        "        pass\n"
        "        yield '\\n'\n"
        "        for item in context.get('items'):\n"
        "            yield '- '\n"
        "            yield str(item)\n"
        "debug_info = '1=4&2=5&5=9&6=10'\n",
        encoding="utf-8",
    )

    tracer = JinjaTemplateCoveragePlugin(compiled_template_roots=(compiled_root,)).file_tracer(str(compiled_file))

    assert tracer is not None
    assert tracer.line_number_range(_frame(8)) == (3, 4)


def test_file_tracer_without_compiled_template_roots_traces_no_files(tmp_path: Path) -> None:
    compiled_file = tmp_path / "compiled_templates/template.py"
    compiled_file.parent.mkdir()
    compiled_file.write_text("name = 'template.j2'\ndebug_info = '1=10'\n", encoding="utf-8")

    assert JinjaTemplateCoveragePlugin().file_tracer(str(compiled_file)) is None


def test_coverage_init_requires_compiled_template_roots() -> None:
    with pytest.raises(ConfigError, match="compiled_template_roots"):
        coverage_init(None, {})


def test_file_tracer_ignores_generated_scaffolding_between_mapped_lines(tmp_path: Path) -> None:
    template_root = tmp_path / "j2templates"
    compiled_root = template_root / "compiled_templates"
    source_file = template_root / "simple.j2"
    compiled_file = compiled_root / "simple.py"

    template_root.mkdir()
    compiled_root.mkdir()
    source_file.write_text("{% if enabled %}\ncovered\n{% endif %}\n", encoding="utf-8")
    compiled_file.write_text(
        "name = 'simple.j2'\n"
        "def root():\n"
        "    if 0: yield None\n"
        "    enabled = True\n"
        "    if enabled:\n"
        "        pass\n"
        "        yield 'covered'\n"
        "debug_info = '1=5'\n",
        encoding="utf-8",
    )

    tracer = JinjaTemplateCoveragePlugin(compiled_template_roots=(compiled_root,)).file_tracer(str(compiled_file))

    assert tracer is not None
    assert tracer.line_number_range(_frame(4)) == (-1, -1)
    assert tracer.line_number_range(_frame(5)) == (1, 1)
    assert tracer.line_number_range(_frame(6)) == (-1, -1)
    assert tracer.line_number_range(_frame(7)) == (2, 2)


def test_file_tracer_reloads_compiled_template_when_file_changes(tmp_path: Path) -> None:
    template_root = tmp_path / "j2templates"
    compiled_root = template_root / "compiled_templates"
    source_file = template_root / "simple.j2"
    compiled_file = compiled_root / "simple.py"

    template_root.mkdir()
    compiled_root.mkdir()
    source_file.write_text("{% if enabled %}\ncovered\n{% endif %}\n", encoding="utf-8")
    compiled_file.write_text("name = 'simple.j2'\ndef root():\n    pass\ndebug_info = '1=5'\n", encoding="utf-8")

    plugin = JinjaTemplateCoveragePlugin(compiled_template_roots=(compiled_root,))
    tracer = plugin.file_tracer(str(compiled_file))
    assert tracer is not None
    assert tracer.line_number_range(_frame(5)) == (1, 1)

    compiled_file.write_text("name = 'simple.j2'\ndef root():\n    pass\n    pass\ndebug_info = '2=7'\n", encoding="utf-8")

    tracer = plugin.file_tracer(str(compiled_file))
    assert tracer is not None
    assert tracer.line_number_range(_frame(5)) == (-1, -1)
    assert tracer.line_number_range(_frame(7)) == (2, 2)


def test_file_tracer_ignores_compiled_template_with_unresolved_source(tmp_path: Path) -> None:
    template_root = tmp_path / "j2templates"
    compiled_root = template_root / "compiled_templates"
    compiled_file = compiled_root / "missing.py"

    compiled_root.mkdir(parents=True)
    compiled_file.write_text("name = '../missing.j2'\ndebug_info = '1=10'\n", encoding="utf-8")

    assert JinjaTemplateCoveragePlugin(compiled_template_roots=(compiled_root,)).file_tracer(str(compiled_file)) is None


def test_file_reporter_lines_returns_reportable_jinja_lines(tmp_path: Path) -> None:
    source_file = tmp_path / "template.j2"
    source_file.write_text(
        "static text\n{% if enabled %}\nconditional static text\n{{ value }}\n{% endif %}\n{% set x = 1 %}\n{# comment #}\n",
        encoding="utf-8",
    )

    assert JinjaTemplateFileReporter(str(source_file)).lines() == {1, 2, 3, 4, 6}


def test_file_reporter_lines_expands_multiline_jinja_tags(tmp_path: Path) -> None:
    source_file = tmp_path / "template.j2"
    source_file.write_text(
        "{% if primary is defined\n      or secondary is defined\n      or fallback is defined %}\n{{ value |\n   default('fallback') }}\n{% endif %}\n",
        encoding="utf-8",
    )

    assert JinjaTemplateFileReporter(str(source_file)).lines() == {1, 2, 3, 4, 5}


def test_multiline_jinja_control_flow_arcs_target_body_after_tag(tmp_path: Path) -> None:
    source_file = tmp_path / "template.j2"
    source_file.write_text(
        "{% if primary is defined or\n"
        "      secondary is defined or\n"
        "      fallback is defined %}\n"
        "{% set value = 'covered' %}\n"
        "{% endif %}\n"
        "{% for item in items\n"
        "      if item.enabled %}\n"
        "{{ item.name }}\n"
        "{% else %}\n"
        "empty\n"
        "{% endfor %}\n",
        encoding="utf-8",
    )

    arcs = JinjaTemplateFileReporter(str(source_file)).arcs()

    assert (1, 4) in arcs
    assert (1, 3) not in arcs
    assert (6, 8) in arcs
    assert (6, 7) not in arcs


def test_reporter_translates_loop_backedge_to_no_else_endif_arc(tmp_path: Path) -> None:
    source_file = tmp_path / "template.j2"
    source_file.write_text(
        "{% for item in items %}\n{% if item.enabled %}\n{{ item.name }}\n{% endif %}\n{% endfor %}\n",
        encoding="utf-8",
    )

    reporter = JinjaTemplateFileReporter(str(source_file))

    assert reporter.arcs() == {(1, 2), (2, 3), (2, 4)}
    assert (2, 4) in reporter.translate_arcs([(2, 1)])


@pytest.mark.parametrize(
    ("source", "recorded_arc", "expected_arc"),
    [
        (
            "{% block content %}\n{% for item in items %}\n{% if item.enabled %}\n{{ item.name }}\n{% endif %}\n{% endfor %}\n{% endblock %}\n",
            (3, 2),
            (3, 5),
        ),
        (
            "{% call render_items() %}\n{% for item in items %}\n{% if item.enabled %}\n{{ item.name }}\n{% endif %}\n{% endfor %}\n{% endcall %}\n",
            (3, 2),
            (3, 5),
        ),
        (
            "{% filter upper %}\n{% for item in items %}\n{% if item.enabled %}\n{{ item.name }}\n{% endif %}\n{% endfor %}\n{% endfilter %}\n",
            (3, 2),
            (3, 5),
        ),
        (
            "{% with enabled = item.enabled %}\n{% for item in items %}\n{% if enabled %}\n{{ item.name }}\n{% endif %}\n{% endfor %}\n{% endwith %}\n",
            (3, 2),
            (3, 5),
        ),
        (
            "{% macro render_items(items) %}\n{% for item in items %}\n{% if item.enabled %}\n{{ item.name }}\n{% endif %}\n{% endfor %}\n{% endmacro %}\n",
            (3, 2),
            (3, 5),
        ),
    ],
)
def test_reporter_translates_loop_backedge_to_no_else_endif_arc_inside_wrapper(
    tmp_path: Path,
    source: str,
    recorded_arc: tuple[int, int],
    expected_arc: tuple[int, int],
) -> None:
    source_file = tmp_path / "template.j2"
    source_file.write_text(source, encoding="utf-8")

    assert expected_arc in JinjaTemplateFileReporter(str(source_file)).translate_arcs([recorded_arc])


def test_reporter_does_not_alias_macro_body_to_enclosing_loop(tmp_path: Path) -> None:
    source_file = tmp_path / "template.j2"
    source_file.write_text(
        "{% for item in items %}\n"
        "{% macro render_item(item) %}\n"
        "{% if item.enabled %}\n"
        "{{ item.name }}\n"
        "{% endif %}\n"
        "{% endmacro %}\n"
        "{{ render_item(item) }}\n"
        "{% endfor %}\n",
        encoding="utf-8",
    )

    assert (3, 5) not in JinjaTemplateFileReporter(str(source_file)).translate_arcs([(3, 1)])


def test_reporter_translates_loop_backedge_to_final_no_else_elif_endif_arc(tmp_path: Path) -> None:
    source_file = tmp_path / "template.j2"
    source_file.write_text(
        "{% for item in items %}\n"
        "{% if item.primary %}\n"
        "primary {{ item.name }}\n"
        "{% elif item.secondary %}\n"
        "secondary {{ item.name }}\n"
        "{% endif %}\n"
        "{% endfor %}\n",
        encoding="utf-8",
    )

    reporter = JinjaTemplateFileReporter(str(source_file))

    assert (4, 6) in reporter.translate_arcs([(4, 1)])
    assert (2, 6) not in reporter.translate_arcs([(2, 1)])
    assert (4, 6) not in reporter.translate_arcs([(4, 5)])


def test_reporter_does_not_alias_elif_chain_with_else_to_endif(tmp_path: Path) -> None:
    source_file = tmp_path / "template.j2"
    source_file.write_text(
        "{% for item in items %}\n"
        "{% if item.primary %}\n"
        "primary {{ item.name }}\n"
        "{% elif item.secondary %}\n"
        "secondary {{ item.name }}\n"
        "{% else %}\n"
        "fallback {{ item.name }}\n"
        "{% endif %}\n"
        "{% endfor %}\n",
        encoding="utf-8",
    )

    assert (4, 8) not in JinjaTemplateFileReporter(str(source_file)).translate_arcs([(4, 1)])


def test_reporter_does_not_infer_no_else_endif_arc_from_true_branch(tmp_path: Path) -> None:
    source_file = tmp_path / "template.j2"
    source_file.write_text(
        "{% for item in items %}\n{% if item.enabled %}\n{{ item.name }}\n{% endif %}\n{% endfor %}\n",
        encoding="utf-8",
    )

    assert (2, 4) not in JinjaTemplateFileReporter(str(source_file)).translate_arcs([(2, 3)])


def test_reporter_does_not_alias_no_else_endif_arc_outside_loop(tmp_path: Path) -> None:
    source_file = tmp_path / "template.j2"
    source_file.write_text("{% if enabled %}\n{{ name }}\n{% endif %}\n", encoding="utf-8")

    assert (1, 3) not in JinjaTemplateFileReporter(str(source_file)).translate_arcs([(1, -1)])


def test_file_tracer_maps_multiline_jinja_tags_to_full_source_range(tmp_path: Path) -> None:
    template_root = tmp_path / "j2templates"
    compiled_root = template_root / "compiled_templates"
    source_file = template_root / "template.j2"
    compiled_file = compiled_root / "template.py"

    template_root.mkdir()
    compiled_root.mkdir()
    source_file.write_text(
        "{% if primary is defined\n      or secondary is defined\n      or fallback is defined %}\n{{ value |\n   default('fallback') }}\n{% endif %}\n",
        encoding="utf-8",
    )
    compiled_file.write_text(
        "name = 'template.j2'\ndef root():\n    pass\ndebug_info = '1=10&4=20'\n",
        encoding="utf-8",
    )

    tracer = JinjaTemplateCoveragePlugin(compiled_template_roots=(compiled_root,)).file_tracer(str(compiled_file))

    assert tracer is not None
    assert tracer.line_number_range(_frame(10)) == (1, 3)
    assert tracer.line_number_range(_frame(20)) == (4, 5)


@pytest.mark.parametrize(
    ("spacer_values", "expected_executed", "expected_missing_branch_arcs"),
    [
        ([True], {1, 2, 3, 6}, {2: [4]}),
        ([False], {1, 2, 6}, {2: [3]}),
        ([True, False], {1, 2, 3, 6}, {}),
    ],
)
def test_coverage_tracks_conditional_blank_static_lines(
    tmp_path: Path,
    spacer_values: list[bool],
    expected_executed: set[int],
    expected_missing_branch_arcs: dict[int, list[int]],
) -> None:
    template_root = tmp_path / "j2templates"
    compiled_root = template_root / "compiled_templates"
    source_file = template_root / "blank_branch.j2"

    template_root.mkdir()
    compiled_root.mkdir()
    source_file.write_text(
        "{% if wrapper %}\n{% if spacer %}\n\n{% endif %}\n{% endif %}\nbody\n",
        encoding="utf-8",
    )

    Environment(loader=FileSystemLoader(template_root)).compile_templates(compiled_root, zip=None, ignore_errors=False)  # noqa: S701
    environment = Environment(loader=ModuleLoader(compiled_root))  # noqa: S701

    coverage = _coverage_for_template(tmp_path, template_root, compiled_root, branch=True)
    coverage.erase()
    coverage.start()
    for spacer in spacer_values:
        environment.get_template("blank_branch.j2").render(wrapper=True, spacer=spacer)
    coverage.stop()
    coverage.save()

    reporter = JinjaTemplateFileReporter(str(source_file))
    analysis = coverage._analyze(str(source_file.resolve()))

    assert reporter.lines() == {1, 2, 3, 6}
    assert set(analysis.executed) == expected_executed
    assert analysis.missing_branch_arcs() == expected_missing_branch_arcs
    assert analysis.branch_stats()[2] == (2, 2 if spacer_values == [True, False] else 1)


@pytest.mark.parametrize(
    ("items_values", "expected_executed", "expected_missing_branch_arcs"),
    [
        ([["leaf"]], {1, 2, 3, 4, 5, 9}, {2: [7]}),
        ([[]], {1, 2, 9}, {2: [3]}),
        ([["leaf"], []], {1, 2, 3, 4, 5, 9}, {}),
    ],
)
def test_coverage_tracks_conditional_blank_static_line_before_for(
    tmp_path: Path,
    items_values: list[list[str]],
    expected_executed: set[int],
    expected_missing_branch_arcs: dict[int, list[int]],
) -> None:
    template_root = tmp_path / "j2templates"
    compiled_root = template_root / "compiled_templates"
    source_file = template_root / "blank_before_for.j2"

    template_root.mkdir()
    compiled_root.mkdir()
    source_file.write_text(
        "{% if wrapper %}\n{% if items %}\n\n{% for item in items %}\n- {{ item }}\n{% endfor %}\n{% endif %}\n{% endif %}\nbody\n",
        encoding="utf-8",
    )

    Environment(loader=FileSystemLoader(template_root)).compile_templates(compiled_root, zip=None, ignore_errors=False)  # noqa: S701
    environment = Environment(loader=ModuleLoader(compiled_root))  # noqa: S701

    coverage = _coverage_for_template(tmp_path, template_root, compiled_root, branch=True)
    coverage.erase()
    coverage.start()
    for items in items_values:
        environment.get_template("blank_before_for.j2").render(wrapper=True, items=items)
    coverage.stop()
    coverage.save()

    analysis = coverage._analyze(str(source_file.resolve()))

    assert set(analysis.executed) == expected_executed
    assert analysis.missing_branch_arcs() == expected_missing_branch_arcs
    assert analysis.branch_stats()[2] == (2, 2 if items_values == [["leaf"], []] else 1)


@pytest.mark.parametrize(
    ("enabled_values", "expected_executed", "expected_missing_branch_arcs"),
    [
        ([True], {1, 2, 3, 6}, {2: [4]}),
        ([False], {1, 2, 6}, {2: [3]}),
        ([True, False], {1, 2, 3, 6}, {}),
    ],
)
def test_coverage_tracks_conditional_set_only_body(
    tmp_path: Path,
    enabled_values: list[bool],
    expected_executed: set[int],
    expected_missing_branch_arcs: dict[int, list[int]],
) -> None:
    template_root = tmp_path / "j2templates"
    compiled_root = template_root / "compiled_templates"
    source_file = template_root / "set_branch.j2"

    template_root.mkdir()
    compiled_root.mkdir()
    source_file.write_text(
        "{% if wrapper %}\n{% if enabled %}\n{% set value = 'yes' %}\n{% endif %}\n{% endif %}\n{{ value | default('-') }}\n",
        encoding="utf-8",
    )

    Environment(loader=FileSystemLoader(template_root)).compile_templates(compiled_root, zip=None, ignore_errors=False)  # noqa: S701
    environment = Environment(loader=ModuleLoader(compiled_root))  # noqa: S701

    coverage = _coverage_for_template(tmp_path, template_root, compiled_root, branch=True)
    coverage.erase()
    coverage.start()
    for enabled in enabled_values:
        environment.get_template("set_branch.j2").render(wrapper=True, enabled=enabled)
    coverage.stop()
    coverage.save()

    analysis = coverage._analyze(str(source_file.resolve()))

    assert set(analysis.executed) == expected_executed
    assert analysis.missing_branch_arcs() == expected_missing_branch_arcs
    assert analysis.branch_stats()[2] == (2, 2 if enabled_values == [True, False] else 1)


@pytest.mark.parametrize(
    ("enabled_values", "expected_executed", "expected_missing_branch_arcs"),
    [
        ([True], {1, 2, 3, 4, 7}, {3: [5]}),
        ([False], {1, 2, 3, 7}, {3: [4]}),
        ([True, False], {1, 2, 3, 4, 7}, {}),
    ],
)
def test_coverage_tracks_conditional_do_only_body(
    tmp_path: Path,
    enabled_values: list[bool],
    expected_executed: set[int],
    expected_missing_branch_arcs: dict[int, list[int]],
) -> None:
    template_root = tmp_path / "j2templates"
    compiled_root = template_root / "compiled_templates"
    source_file = template_root / "do_branch.j2"

    template_root.mkdir()
    compiled_root.mkdir()
    source_file.write_text(
        "{% set values = [] %}\n{% if wrapper %}\n{% if enabled %}\n{% do values.append('yes') %}\n{% endif %}\n{% endif %}\n{{ values | join(',') }}\n",
        encoding="utf-8",
    )

    Environment(loader=FileSystemLoader(template_root), extensions=["jinja2.ext.do"]).compile_templates(compiled_root, zip=None, ignore_errors=False)  # noqa: S701
    environment = Environment(loader=ModuleLoader(compiled_root), extensions=["jinja2.ext.do"])  # noqa: S701

    coverage = _coverage_for_template(tmp_path, template_root, compiled_root, branch=True)
    coverage.erase()
    coverage.start()
    for enabled in enabled_values:
        environment.get_template("do_branch.j2").render(wrapper=True, enabled=enabled)
    coverage.stop()
    coverage.save()

    analysis = coverage._analyze(str(source_file.resolve()))

    assert set(analysis.executed) == expected_executed
    assert analysis.missing_branch_arcs() == expected_missing_branch_arcs
    assert analysis.branch_stats()[3] == (2, 2 if enabled_values == [True, False] else 1)


def test_coverage_marks_multiline_jinja_tags_as_executed_ranges(tmp_path: Path) -> None:
    analysis = _analyze_rendered_template(
        tmp_path,
        "{% if primary is defined\n      or secondary is defined\n      or fallback is defined %}\n{{ value |\n   default('fallback') }}\n{% endif %}\n",
        {"primary": True, "value": "covered"},
    )

    assert set(analysis.executed) >= {1, 2, 3, 4, 5}


def test_coverage_marks_multiline_jinja_branch_body_arc_as_executed(tmp_path: Path) -> None:
    analysis = _analyze_rendered_template(
        tmp_path,
        "{% if wrapper %}\n"
        "{% if primary is defined or\n"
        "      secondary is defined or\n"
        "      fallback is defined %}\n"
        "{% set value = 'covered' %}\n"
        "{% endif %}\n"
        "{% endif %}\n",
        {"wrapper": True, "primary": True},
    )

    assert analysis.branch_stats()[2] == (2, 1)
    assert analysis.missing_branch_arcs() == {2: [6]}


def test_coverage_marks_multiline_no_else_false_arc_as_executed(tmp_path: Path) -> None:
    template_root = tmp_path / "j2templates"
    compiled_root = template_root / "compiled_templates"
    source_file = template_root / "template.j2"

    template_root.mkdir()
    compiled_root.mkdir()
    source_file.write_text(
        "{% if primary is defined or\n"
        "      secondary is defined or\n"
        "      fallback is defined %}\n"
        "{% set value = 'covered' %}\n"
        "{% endif %}\n"
        "{% for item in items %}\n"
        "{{ item }}\n"
        "{% endfor %}\n",
        encoding="utf-8",
    )

    Environment(loader=FileSystemLoader(template_root)).compile_templates(compiled_root, zip=None, ignore_errors=False)  # noqa: S701
    environment = Environment(loader=ModuleLoader(compiled_root))  # noqa: S701
    coverage = _coverage_for_template(tmp_path, template_root, compiled_root, branch=True)
    coverage.erase()
    coverage.start()
    environment.get_template("template.j2").render(primary=True, items=["leaf"])
    environment.get_template("template.j2").render(items=["leaf"])
    coverage.stop()
    coverage.save()

    analysis = coverage._analyze(str(source_file.resolve()))

    assert analysis.branch_stats()[1] == (2, 2)
    assert analysis.missing_branch_arcs() == {}


def test_coverage_marks_jinja_else_tag_as_executed_with_else_body(tmp_path: Path) -> None:
    analysis = _analyze_rendered_template(
        tmp_path,
        "{% if mode == 'a' %}\n{% set value = 'a' %}\n{% else %}\n{% set value = 'b' %}\n{% endif %}\n{{ value }}\n",
        {"mode": "b"},
    )

    assert set(analysis.executed) >= {1, 3, 4, 6}
    assert analysis.missing_branch_arcs() == {1: [2]}


def test_file_reporter_does_not_expose_cached_mutable_sets(tmp_path: Path) -> None:
    source_file = tmp_path / "template.j2"
    source_file.write_text("{% if enabled %}\nhello\n{% endif %}\n", encoding="utf-8")
    reporter = JinjaTemplateFileReporter(str(source_file))

    lines = reporter.lines()
    arcs = reporter.arcs()
    no_branch_lines = reporter.no_branch_lines()
    lines.clear()
    arcs.clear()
    no_branch_lines.clear()

    assert reporter.lines() == {1, 2}
    assert reporter.arcs() == {(1, 2), (1, 3)}
    assert reporter.no_branch_lines() == {1}


def test_coverage_records_compiled_execution_against_jinja_source(tmp_path: Path) -> None:
    template_root = tmp_path / "j2templates"
    compiled_root = template_root / "compiled_templates"
    source_file = template_root / "simple.j2"
    compiled_file = compiled_root / "simple.py"

    template_root.mkdir()
    compiled_root.mkdir()
    source_file.write_text("{% if enabled %}\n{{ value }}\n{% endif %}\n", encoding="utf-8")
    compiled_file.write_text(
        "name = 'simple.j2'\ndef root():\n    if 0: yield None\n    enabled = True\n    if enabled:\n        yield 'value'\ndebug_info = '1=4&2=6'\n",
        encoding="utf-8",
    )

    coverage = _coverage_for_template(tmp_path, template_root, compiled_root)
    coverage.erase()
    coverage.start()
    spec = importlib.util.spec_from_file_location("compiled_simple", compiled_file)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    list(module.root())
    coverage.stop()
    coverage.save()

    data = coverage.get_data()
    assert str(source_file.resolve()) in data.measured_files()
    assert data.file_tracer(str(source_file.resolve())) == "None.JinjaTemplateCoveragePlugin"
    assert data.lines(str(source_file.resolve())) == [1, 2]


def test_reporter_uses_jinja_source_for_branch_arcs(tmp_path: Path) -> None:
    template_root = tmp_path / "j2templates"
    compiled_root = template_root / "compiled_templates"
    source_file = template_root / "branch.j2"

    template_root.mkdir()
    compiled_root.mkdir()
    source_file.write_text(
        "{% if mode == 'a' %}\n"
        "alpha\n"
        "{% elif mode == 'b' %}\n"
        "bravo\n"
        "{% else %}\n"
        "charlie\n"
        "{% endif %}\n"
        "{% for item in items if item.enabled %}\n"
        "item {{ item.name }}\n"
        "{% else %}\n"
        "empty\n"
        "{% endfor %}\n",
        encoding="utf-8",
    )

    Environment(loader=FileSystemLoader(template_root)).compile_templates(compiled_root, zip=None, ignore_errors=False)  # noqa: S701

    compiled_file = next(compiled_root.glob("*.py"))
    tracer = JinjaTemplateCoveragePlugin(compiled_template_roots=(compiled_root,)).file_tracer(str(compiled_file))
    reporter = JinjaTemplateFileReporter(str(source_file))
    exit_counts = reporter.exit_counts()

    assert tracer is not None
    assert tracer.source_filename() == str(source_file.resolve())
    assert reporter.lines() == {1, 2, 3, 4, 5, 6, 8, 9, 10, 11}
    assert exit_counts[1] > 1
    assert exit_counts[3] > 1
    assert exit_counts[8] > 1


def test_for_loop_empty_branch_requires_template_else(tmp_path: Path) -> None:
    without_else = tmp_path / "without_else.j2"
    with_else = tmp_path / "with_else.j2"

    without_else.write_text("{% for item in items %}\nitem {{ item }}\n{% endfor %}\nafter\n", encoding="utf-8")
    with_else.write_text("{% for item in items %}\nitem {{ item }}\n{% else %}\nempty\n{% endfor %}\nafter\n", encoding="utf-8")

    assert JinjaTemplateFileReporter(str(without_else)).arcs() == {(1, 2)}
    assert JinjaTemplateFileReporter(str(with_else)).arcs() == {(1, 2), (1, 3)}


def test_nested_loop_cleanup_does_not_cover_loop_body_output(tmp_path: Path) -> None:
    template_root = tmp_path / "j2templates"
    compiled_root = template_root / "compiled_templates"
    source_file = template_root / "nested_loop.j2"

    template_root.mkdir()
    compiled_root.mkdir()
    source_file.write_text(
        "{% for parent in parents %}\n{% for child in parent.children %}\nchild {{ child }}\n{% endfor %}\nafter {{ parent.name }}\n{% endfor %}\n",
        encoding="utf-8",
    )

    Environment(loader=FileSystemLoader(template_root)).compile_templates(compiled_root, zip=None, ignore_errors=False)  # noqa: S701
    environment = Environment(loader=ModuleLoader(compiled_root))  # noqa: S701

    coverage = _coverage_for_template(tmp_path, template_root, compiled_root, branch=True)
    coverage.erase()
    coverage.start()
    environment.get_template("nested_loop.j2").render(parents=[{"name": "p1", "children": []}])
    coverage.stop()
    coverage.save()

    analysis = coverage._analyze(str(source_file.resolve()))

    assert 3 not in analysis.executed
    assert 5 in analysis.executed


def test_coverage_records_static_text_lines_from_compiled_template_execution(tmp_path: Path) -> None:
    template_root = tmp_path / "j2templates"
    compiled_root = template_root / "compiled_templates"
    source_file = template_root / "branch.j2"

    template_root.mkdir()
    compiled_root.mkdir()
    source_file.write_text(
        "{% if mode == 'a' %}\n"
        "alpha\n"
        "\n"
        "alpha details\n"
        "{% else %}\n"
        "bravo\n"
        "{% endif %}\n"
        "{% for item in items %}\n"
        "item {{ item }}\n"
        "{% else %}\n"
        "empty\n"
        "{% endfor %}\n",
        encoding="utf-8",
    )

    Environment(loader=FileSystemLoader(template_root)).compile_templates(compiled_root, zip=None, ignore_errors=False)  # noqa: S701
    environment = Environment(loader=ModuleLoader(compiled_root))  # noqa: S701

    coverage = _coverage_for_template(tmp_path, template_root, compiled_root, branch=True)
    coverage.erase()
    coverage.start()
    environment.get_template("branch.j2").render(mode="a", items=[])
    coverage.stop()
    coverage.save()

    source_filename = str(source_file.resolve())
    data = coverage.get_data()

    assert source_filename in data.measured_files()
    assert data.file_tracer(source_filename) == "None.JinjaTemplateCoveragePlugin"
    source_lines = data.lines(source_filename)
    assert source_lines is not None
    assert set(source_lines) >= {1, 2, 3, 4, 8, 11}
    assert 6 not in source_lines
    assert 9 not in source_lines
    assert data.arcs(source_filename)

    shutil.rmtree(compiled_root)

    analysis = coverage._analyze(source_filename)
    assert max(analysis.executed) <= len(source_file.read_text(encoding="utf-8").splitlines())
    assert 3 in analysis.executed
    assert 9 not in analysis.executed


def test_top_level_optional_guard_is_not_counted_as_missing_branch(tmp_path: Path) -> None:
    template_root = tmp_path / "j2templates"
    compiled_root = template_root / "compiled_templates"
    source_file = template_root / "optional.j2"

    template_root.mkdir()
    compiled_root.mkdir()
    source_file.write_text("{% if enabled %}\noptional output\n{% endif %}\n", encoding="utf-8")

    Environment(loader=FileSystemLoader(template_root)).compile_templates(compiled_root, zip=None, ignore_errors=False)  # noqa: S701
    environment = Environment(loader=ModuleLoader(compiled_root))  # noqa: S701

    coverage = _coverage_for_template(tmp_path, template_root, compiled_root, branch=True)
    coverage.erase()
    coverage.start()
    environment.get_template("optional.j2").render(enabled=True)
    coverage.stop()
    coverage.save()

    analysis = coverage._analyze(str(source_file.resolve()))

    assert analysis.no_branch == {1}
    assert not analysis.missing_branch_arcs()


def test_nested_optional_input_shape_reports_missing_inner_output(tmp_path: Path) -> None:
    analysis = _analyze_rendered_template(
        tmp_path,
        "{% if feature.enabled %}\nfeature\n{% if feature.optional %}\noptional\n{% endif %}\nafter\n{% endif %}\n",
        {"feature": {"enabled": True}},
    )

    assert 4 in analysis.missing
    assert analysis.missing_branch_arcs() == {3: [4]}


def test_optional_block_after_static_output_records_both_branches(tmp_path: Path) -> None:
    analysis = _analyze_rendered_template(
        tmp_path,
        "{% for item in items %}\nheading {{ item.name }}\n{% if item.enabled %}\noptional\n{% endif %}\n{% endfor %}\n",
        {"items": [{"name": "enabled", "enabled": True}, {"name": "disabled", "enabled": False}]},
    )

    assert not analysis.missing_branch_arcs()


def test_long_elif_chain_reports_unvisited_alternatives(tmp_path: Path) -> None:
    analysis = _analyze_rendered_template(
        tmp_path,
        "{% if mode == 'a' %}\nalpha\n{% elif mode == 'b' %}\nbravo\n{% elif mode == 'c' %}\ncharlie\n{% else %}\ndelta\n{% endif %}\n",
        {"mode": "a"},
    )

    assert analysis.missing_branch_arcs() == {1: [3], 3: [4, 5], 5: [6, 7]}


def test_final_no_else_elif_false_fallthrough_to_following_block_is_covered(tmp_path: Path) -> None:
    analysis = _analyze_rendered_template_contexts(
        tmp_path,
        "{% if wrapper %}\n"
        "{% if mode == 'a' %}\n"
        "alpha\n"
        "{% elif mode == 'b' %}\n"
        "bravo\n"
        "{% endif %}\n"
        "{% for item in items %}\n"
        "{{ item }}\n"
        "{% endfor %}\n"
        "{% endif %}\n",
        [
            {"wrapper": True, "mode": "a", "items": ["leaf"]},
            {"wrapper": True, "mode": "b", "items": ["leaf"]},
            {"wrapper": True, "mode": "c", "items": ["leaf"]},
        ],
    )

    assert not analysis.missing_branch_arcs()


def test_no_else_loop_guard_false_fallthrough_to_structural_label_is_covered(tmp_path: Path) -> None:
    analysis = _analyze_rendered_template_contexts(
        tmp_path,
        "{% if wrapper %}\n"
        "{% if config %}\n"
        "config\n"
        "{% endif %}\n"
        "{% for item in items %}\n"
        "{% set value = item.name %}\n"
        "{% if item.interval is defined or item.once is defined or item.interval is defined %}\n"
        "{% if item.once is defined %}\n"
        "{% set value = value ~ ' once' %}\n"
        "{% elif item.interval is defined %}\n"
        "{% set value = value ~ ' interval' %}\n"
        "{% endif %}\n"
        "{{ value }}\n"
        "{% endif %}\n"
        "{% endfor %}\n"
        "{% endif %}\n",
        [
            {
                "wrapper": True,
                "config": True,
                "items": [
                    {"name": "once", "once": True},
                    {"name": "interval", "interval": 10},
                    {"name": "skipped"},
                ],
            },
            {
                "wrapper": True,
                "config": False,
                "items": [],
            },
        ],
    )

    assert 7 not in analysis.missing_branch_arcs()


def test_variable_building_condition_reports_unvisited_assignment_branch(tmp_path: Path) -> None:
    analysis = _analyze_rendered_template(
        tmp_path,
        "{% if dangerous %}\n{% set prefix = 'dangerous ' %}\n{% else %}\n{% set prefix = '' %}\n{% endif %}\nvalue {{ prefix }}done\n",
        {"dangerous": False},
    )

    assert analysis.missing_branch_arcs() == {1: [2]}


def test_nested_loop_with_conditional_output_reports_unvisited_inner_output(tmp_path: Path) -> None:
    analysis = _analyze_rendered_template(
        tmp_path,
        "{% for parent in parents %}\n"
        "parent {{ parent.name }}\n"
        "{% for child in parent.children %}\n"
        "{% if child.enabled %}\n"
        "child {{ child.name }}\n"
        "{% endif %}\n"
        "{% endfor %}\n"
        "{% endfor %}\n",
        {"parents": [{"name": "p1", "children": [{"name": "c1", "enabled": False}]}]},
    )

    assert analysis.missing_branch_arcs() == {4: [5]}


def test_complex_expression_reports_missing_true_output_branch(tmp_path: Path) -> None:
    analysis = _analyze_rendered_template(
        tmp_path,
        "{% if wrapper %}\n{% if item.enabled and item.name is defined %}\nitem {{ item.name }}\n{% endif %}\nafter\n{% endif %}\n",
        {"wrapper": True, "item": {"enabled": False}},
    )

    assert analysis.missing_branch_arcs() == {2: [3]}
