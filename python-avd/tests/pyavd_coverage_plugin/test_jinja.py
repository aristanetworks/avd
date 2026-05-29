# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import importlib.util
import os
import shutil
import subprocess
import sys
from pathlib import Path
from types import SimpleNamespace

from coverage import Coverage, CoverageData
from coverage_plugins.jinja import JinjaTemplateCoveragePlugin, JinjaTemplateFileReporter
from jinja2 import Environment, FileSystemLoader, ModuleLoader


def _analyze_rendered_template(tmp_path: Path, source: str, context: dict[str, object]) -> object:
    template_root = tmp_path / "j2templates"
    compiled_root = template_root / "compiled_templates"
    source_file = template_root / "template.j2"

    template_root.mkdir()
    compiled_root.mkdir()
    source_file.write_text(source, encoding="utf-8")

    Environment(loader=FileSystemLoader(template_root)).compile_templates(compiled_root, zip=None, ignore_errors=False)  # noqa: S701
    environment = Environment(loader=ModuleLoader(compiled_root))  # noqa: S701
    coverage = Coverage(
        config_file=False,
        data_file=str(tmp_path / ".coverage"),
        branch=True,
        source=[str(template_root), str(compiled_root)],
        plugins=[lambda reg: reg.add_file_tracer(JinjaTemplateCoveragePlugin(compiled_template_roots=(compiled_root,)))],
    )
    coverage.erase()
    coverage.start()
    environment.get_template("template.j2").render(**context)
    coverage.stop()
    coverage.save()

    return coverage._analyze(str(source_file.resolve()))


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
    assert tracer.line_number_range(SimpleNamespace(f_lineno=9)) == (-1, -1)
    assert tracer.line_number_range(SimpleNamespace(f_lineno=10)) == (1, 1)
    assert tracer.line_number_range(SimpleNamespace(f_lineno=14)) == (-1, -1)
    assert tracer.line_number_range(SimpleNamespace(f_lineno=15)) == (2, 2)
    assert tracer.line_number_range(SimpleNamespace(f_lineno=99)) == (-1, -1)


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
    assert tracer.line_number_range(SimpleNamespace(f_lineno=4)) == (-1, -1)
    assert tracer.line_number_range(SimpleNamespace(f_lineno=5)) == (1, 1)
    assert tracer.line_number_range(SimpleNamespace(f_lineno=6)) == (-1, -1)
    assert tracer.line_number_range(SimpleNamespace(f_lineno=7)) == (2, 2)


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

    coverage = Coverage(
        config_file=False,
        data_file=str(tmp_path / ".coverage"),
        source=[str(template_root), str(compiled_root)],
        plugins=[lambda reg: reg.add_file_tracer(JinjaTemplateCoveragePlugin(compiled_template_roots=(compiled_root,)))],
    )
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
    assert reporter.lines() == {1, 2, 3, 4, 6, 8, 9, 11}
    assert exit_counts[1] > 1
    assert exit_counts[3] > 1
    assert exit_counts[8] > 1


def test_for_loop_empty_branch_requires_template_else(tmp_path: Path) -> None:
    without_else = tmp_path / "without_else.j2"
    with_else = tmp_path / "with_else.j2"

    without_else.write_text("{% for item in items %}\nitem {{ item }}\n{% endfor %}\nafter\n", encoding="utf-8")
    with_else.write_text("{% for item in items %}\nitem {{ item }}\n{% else %}\nempty\n{% endfor %}\nafter\n", encoding="utf-8")

    assert JinjaTemplateFileReporter(str(without_else)).arcs() == {(1, 2)}
    assert JinjaTemplateFileReporter(str(with_else)).arcs() == {(1, 2), (1, 4)}


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

    coverage = Coverage(
        config_file=False,
        data_file=str(tmp_path / ".coverage"),
        branch=True,
        source=[str(template_root), str(compiled_root)],
        plugins=[lambda reg: reg.add_file_tracer(JinjaTemplateCoveragePlugin(compiled_template_roots=(compiled_root,)))],
    )
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
        "{% if mode == 'a' %}\nalpha\n{% else %}\nbravo\n{% endif %}\n{% for item in items %}\nitem {{ item }}\n{% else %}\nempty\n{% endfor %}\n",
        encoding="utf-8",
    )

    Environment(loader=FileSystemLoader(template_root)).compile_templates(compiled_root, zip=None, ignore_errors=False)  # noqa: S701
    environment = Environment(loader=ModuleLoader(compiled_root))  # noqa: S701

    coverage = Coverage(
        config_file=False,
        data_file=str(tmp_path / ".coverage"),
        branch=True,
        source=[str(template_root), str(compiled_root)],
        plugins=[lambda reg: reg.add_file_tracer(JinjaTemplateCoveragePlugin(compiled_template_roots=(compiled_root,)))],
    )
    coverage.erase()
    coverage.start()
    environment.get_template("branch.j2").render(mode="a", items=[])
    coverage.stop()
    coverage.save()

    source_filename = str(source_file.resolve())
    data = coverage.get_data()

    assert source_filename in data.measured_files()
    assert data.file_tracer(source_filename) == "None.JinjaTemplateCoveragePlugin"
    assert set(data.lines(source_filename)) >= {1, 2, 6, 9}
    assert 4 not in data.lines(source_filename)
    assert 7 not in data.lines(source_filename)
    assert data.arcs(source_filename)

    shutil.rmtree(compiled_root)

    analysis = coverage._analyze(source_filename)
    assert max(analysis.executed) <= len(source_file.read_text(encoding="utf-8").splitlines())
    assert 7 not in analysis.executed


def test_top_level_optional_guard_is_not_counted_as_missing_branch(tmp_path: Path) -> None:
    template_root = tmp_path / "j2templates"
    compiled_root = template_root / "compiled_templates"
    source_file = template_root / "optional.j2"

    template_root.mkdir()
    compiled_root.mkdir()
    source_file.write_text("{% if enabled %}\noptional output\n{% endif %}\n", encoding="utf-8")

    Environment(loader=FileSystemLoader(template_root)).compile_templates(compiled_root, zip=None, ignore_errors=False)  # noqa: S701
    environment = Environment(loader=ModuleLoader(compiled_root))  # noqa: S701

    coverage = Coverage(
        config_file=False,
        data_file=str(tmp_path / ".coverage"),
        branch=True,
        source=[str(template_root), str(compiled_root)],
        plugins=[lambda reg: reg.add_file_tracer(JinjaTemplateCoveragePlugin(compiled_template_roots=(compiled_root,)))],
    )
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
    assert not analysis.missing_branch_arcs()


def test_long_elif_chain_reports_unvisited_alternatives(tmp_path: Path) -> None:
    analysis = _analyze_rendered_template(
        tmp_path,
        "{% if mode == 'a' %}\nalpha\n{% elif mode == 'b' %}\nbravo\n{% elif mode == 'c' %}\ncharlie\n{% else %}\ndelta\n{% endif %}\n",
        {"mode": "a"},
    )

    assert analysis.missing_branch_arcs() == {1: [3], 3: [4, 5], 5: [6, 8]}


def test_variable_building_condition_reports_unvisited_assignment_branch(tmp_path: Path) -> None:
    analysis = _analyze_rendered_template(
        tmp_path,
        "{% if dangerous %}\n{% set prefix = 'dangerous ' %}\n{% else %}\n{% set prefix = '' %}\n{% endif %}\nvalue {{ prefix }}done\n",
        {"dangerous": False},
    )

    assert analysis.missing_branch_arcs() == {1: [2, 4]}


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

    assert analysis.missing_branch_arcs() == {4: [-1, 5]}


def test_complex_expression_reports_missing_true_output_branch(tmp_path: Path) -> None:
    analysis = _analyze_rendered_template(
        tmp_path,
        "{% if wrapper %}\n{% if item.enabled and item.name is defined %}\nitem {{ item.name }}\n{% endif %}\nafter\n{% endif %}\n",
        {"wrapper": True, "item": {"enabled": False}},
    )

    assert analysis.missing_branch_arcs() == {2: [3]}


def test_report_does_not_require_compiled_templates(tmp_path: Path) -> None:
    template_root = tmp_path / "j2templates"
    compiled_root = template_root / "compiled_templates"
    source_file = template_root / "simple.j2"
    coverage_file = tmp_path / ".coverage"
    coverage_xml = tmp_path / "coverage.xml"
    script = tmp_path / "render.py"
    coverage_config = tmp_path / "pyproject.toml"

    compiled_root.mkdir(parents=True)
    source_file.write_text("{% if enabled %}\nhello\n{% endif %}\n", encoding="utf-8")
    script.write_text(
        "from pathlib import Path\n"
        "from jinja2 import Environment, FileSystemLoader, ModuleLoader\n"
        "root = Path(__file__).parent / 'j2templates'\n"
        "compiled = root / 'compiled_templates'\n"
        "Environment(loader=FileSystemLoader(root)).compile_templates(compiled, zip=None, ignore_errors=False)\n"
        "Environment(loader=ModuleLoader(compiled)).get_template('simple.j2').render(enabled=True)\n",
        encoding="utf-8",
    )
    coverage_config.write_text(
        "[tool.coverage.run]\n"
        "branch = true\n"
        "parallel = true\n"
        'plugins = ["coverage_plugins.jinja"]\n'
        f'source_dirs = ["{template_root.as_posix()}"]\n'
        "[tool.coverage.coverage_plugins.jinja]\n"
        f'compiled_template_roots = ["{compiled_root.as_posix()}"]\n',
        encoding="utf-8",
    )

    subprocess.run(  # noqa: S603
        [sys.executable, "-m", "coverage", "run", "--rcfile", str(coverage_config), "--data-file", str(coverage_file), str(script)],
        check=True,
        cwd=tmp_path,
    )
    subprocess.run(  # noqa: S603
        [sys.executable, "-m", "coverage", "combine", "--rcfile", str(coverage_config), "--data-file", str(coverage_file)],
        check=True,
        cwd=tmp_path,
    )
    shutil.rmtree(compiled_root)

    subprocess.run(  # noqa: S603
        [sys.executable, "-m", "coverage", "report", "--rcfile", str(coverage_config), "--data-file", str(coverage_file), "-m"],
        check=True,
        cwd=tmp_path,
    )
    subprocess.run(  # noqa: S603
        [sys.executable, "-m", "coverage", "xml", "--rcfile", str(coverage_config), "--data-file", str(coverage_file), "-o", str(coverage_xml)],
        check=True,
        cwd=tmp_path,
    )

    xml = coverage_xml.read_text(encoding="utf-8")
    assert "simple.j2" in xml
    assert "compiled_templates" not in xml


def test_configured_coverage_records_checked_in_templates(tmp_path: Path) -> None:
    repo_root = Path(__file__).parents[3]
    coverage_file = tmp_path / ".coverage"
    script = tmp_path / "render_checked_in_template.py"
    script.write_text(
        "from pyavd.constants import EOS_CLI_CONFIG_GEN_JINJA2_PRECOMPILED_TEMPLATE_PATH\n"
        "from pyavd.templater import Templar\n"
        "Templar(EOS_CLI_CONFIG_GEN_JINJA2_PRECOMPILED_TEMPLATE_PATH).render_template_from_file(\n"
        "    'eos/banners.j2',\n"
        "    {'banners': {'login': 'hello'}},\n"
        ")\n",
        encoding="utf-8",
    )

    env = os.environ.copy()
    env["COVERAGE_FILE"] = str(coverage_file)
    env["PYTHONPATH"] = os.pathsep.join(path for path in (str(repo_root), str(repo_root / "python-avd"), env.get("PYTHONPATH", "")) if path)
    subprocess.run(  # noqa: S603
        [sys.executable, "-m", "coverage", "run", "--rcfile=pyproject.toml", str(script)],
        check=True,
        cwd=repo_root,
        env=env,
    )
    subprocess.run(
        [sys.executable, "-m", "coverage", "combine", "--rcfile=pyproject.toml"],
        check=True,
        cwd=repo_root,
        env=env,
    )
    coverage_xml = tmp_path / "coverage.xml"
    xml_result = subprocess.run(  # noqa: S603
        [sys.executable, "-m", "coverage", "xml", "--rcfile=pyproject.toml", "-o", str(coverage_xml)],
        check=False,
        cwd=repo_root,
        env=env,
    )
    assert xml_result.returncode in {0, 2}
    assert coverage_xml.is_file()

    data = CoverageData(basename=str(coverage_file))
    data.read()
    template_file = str(Path("python-avd/pyavd/_eos_cli_config_gen/j2templates/eos/banners.j2").resolve())
    compiled_file = str(Path("python-avd/pyavd/_eos_cli_config_gen/j2templates/compiled_templates/eos__banners.py").resolve())

    assert template_file in data.measured_files()
    assert data.file_tracer(template_file) == "coverage_plugins.jinja.JinjaTemplateCoveragePlugin"
    assert data.lines(template_file)
    assert compiled_file not in data.measured_files()

    assert 'filename="python-avd/pyavd/_eos_cli_config_gen/j2templates/eos/banners.j2"' in coverage_xml.read_text(encoding="utf-8")
