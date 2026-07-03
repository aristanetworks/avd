# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path

from coverage import CoverageData

REPO_ROOT = Path(__file__).parents[3]
COVERAGE_PLUGIN_ROOT = REPO_ROOT / "development/coverage_plugins"


def _subprocess_env(*extra_python_paths: Path) -> dict[str, str]:
    env = os.environ.copy()
    env["PYTHONPATH"] = os.pathsep.join(str(path) for path in (COVERAGE_PLUGIN_ROOT, *extra_python_paths, env.get("PYTHONPATH", "")) if path)
    return env


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
        'core = "ctrace"\n'
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
        env=_subprocess_env(),
    )
    subprocess.run(  # noqa: S603
        [sys.executable, "-m", "coverage", "combine", "--rcfile", str(coverage_config), "--data-file", str(coverage_file)],
        check=True,
        cwd=tmp_path,
        env=_subprocess_env(),
    )
    shutil.rmtree(compiled_root)

    subprocess.run(  # noqa: S603
        [sys.executable, "-m", "coverage", "report", "--rcfile", str(coverage_config), "--data-file", str(coverage_file), "-m"],
        check=True,
        cwd=tmp_path,
        env=_subprocess_env(),
    )
    subprocess.run(  # noqa: S603
        [sys.executable, "-m", "coverage", "xml", "--rcfile", str(coverage_config), "--data-file", str(coverage_file), "-o", str(coverage_xml)],
        check=True,
        cwd=tmp_path,
        env=_subprocess_env(),
    )

    xml = coverage_xml.read_text(encoding="utf-8")
    assert "simple.j2" in xml
    assert "compiled_templates" not in xml


def test_configured_coverage_records_checked_in_templates(tmp_path: Path) -> None:
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

    env = _subprocess_env(REPO_ROOT, REPO_ROOT / "python-avd")
    env["COVERAGE_FILE"] = str(coverage_file)
    subprocess.run(  # noqa: S603
        [sys.executable, "-m", "coverage", "run", "--rcfile=pyproject.toml", str(script)],
        check=True,
        cwd=REPO_ROOT,
        env=env,
    )
    subprocess.run(  # noqa: S603
        [sys.executable, "-m", "coverage", "combine", "--rcfile=pyproject.toml"],
        check=True,
        cwd=REPO_ROOT,
        env=env,
    )
    coverage_xml = tmp_path / "coverage.xml"
    xml_result = subprocess.run(  # noqa: S603
        [sys.executable, "-m", "coverage", "xml", "--rcfile=pyproject.toml", "-o", str(coverage_xml)],
        check=False,
        cwd=REPO_ROOT,
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
