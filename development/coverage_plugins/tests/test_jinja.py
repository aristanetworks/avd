# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import importlib
import sys
from typing import TYPE_CHECKING

import pytest
from coverage.exceptions import ConfigError
from coverage_plugins.jinja import JinjaTemplateCoveragePlugin, JinjaTemplateFileReporter, coverage_init
from jinja_helpers import _frame

if TYPE_CHECKING:
    from pathlib import Path


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


def test_package_relative_roots_are_discovered_without_importing_package(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    package_name = "coverage_test_package"
    package_root = tmp_path / package_name
    compiled_root = package_root / "j2templates/compiled_templates"
    source_file = package_root / "j2templates/simple.j2"
    package_root.mkdir()
    (package_root / "__init__.py").write_text("raise AssertionError('package must not be imported')\n", encoding="utf-8")
    compiled_root.mkdir(parents=True)
    source_file.write_text("hello\n", encoding="utf-8")
    monkeypatch.syspath_prepend(str(tmp_path))
    importlib.invalidate_caches()
    sys.modules.pop(package_name, None)

    plugin = JinjaTemplateCoveragePlugin(compiled_template_roots=("j2templates/compiled_templates",), package=package_name)

    assert plugin.compiled_template_roots == (compiled_root.resolve(),)
    assert list(plugin.find_executable_files(str(package_root))) == [str(source_file.resolve())]
    assert not list(plugin.find_executable_files(str(tmp_path / "other")))
    assert package_name not in sys.modules


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
