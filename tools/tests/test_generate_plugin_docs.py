# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Check the plugin renderer against committed pages and Ansible documentation formats."""

import importlib.util
from pathlib import Path

import pytest
import yaml
from ansible.plugins.loader import init_plugin_loader
from jinja2 import Environment, FileSystemLoader, Template

REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("generate_plugin_docs", REPOSITORY_ROOT / "tools/generate_plugin_docs.py")
assert SPEC is not None
assert SPEC.loader is not None
GENERATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(GENERATOR)

PLUGIN_GROUPS = {
    "modules": "Modules_and_action_plugins",
    "filter": "Filter_plugins",
    "lookup": "Lookup_plugins",
    "test": "Test_plugins",
    "vars": "Vars_plugins",
}
PLUGIN_SOURCES = sorted(
    source.relative_to(REPOSITORY_ROOT)
    for group in PLUGIN_GROUPS
    for source in (REPOSITORY_ROOT / "ansible_collections/arista/avd/plugins" / group).glob("*.py")
    if source.name != "deprecated_filters.py"
)


@pytest.fixture(scope="module")
def template() -> Template:
    """Load the same template and Ansible fragments used by the hook."""
    init_plugin_loader()
    environment = Environment(loader=FileSystemLoader(GENERATOR.TEMPLATE_PATH.parent), trim_blocks=True, autoescape=False)  # noqa: S701
    return environment.get_template(GENERATOR.TEMPLATE_PATH.name)


@pytest.mark.parametrize("source", PLUGIN_SOURCES, ids=str)
def test_committed_pages_are_unchanged(source: Path, template: Template) -> None:
    """Preserve every byte, including escaping, whitespace, and nested descriptions."""
    name, content = GENERATOR.render_plugin_docs(source, template)
    expected = REPOSITORY_ROOT / "docs/plugins" / PLUGIN_GROUPS[source.parent.name] / f"{name}.md"
    assert content.encode("UTF-8") == expected.read_bytes()


@pytest.mark.parametrize("extension", [".py", ".yml", ".yaml"])
def test_python_and_yaml_documentation(tmp_path: Path, template: Template, extension: str) -> None:
    """Read plugins without executing them and support equivalent YAML sidecars."""
    documentation = {
        "name": "arista.avd.sample",
        "author": "An author",
        "short_description": "Sample plugin",
        "description": "A <sample> plugin.",
        "options": {
            "parent": {
                "description": "Parent",
                "suboptions": {"child": {"description": "A <child>", "required": True, "default": False}},
            },
        },
    }
    returns = {"result": {"description": "Result", "contains": {"child": {"description": "A <result>"}}}}
    examples = "sample: '{{ value | arista.avd.sample }}'"
    source = tmp_path / f"sample{extension}"
    if extension == ".py":
        source.write_text(
            f"DOCUMENTATION = {yaml.safe_dump(documentation)!r}\nEXAMPLES = {examples!r}\nRETURN = {yaml.safe_dump(returns)!r}\n"
            "raise RuntimeError('The documentation generator must not execute the plugin')\n",
            encoding="UTF-8",
        )
    else:
        source.write_text(yaml.safe_dump({"DOCUMENTATION": documentation, "EXAMPLES": examples, "RETURN": returns}), encoding="UTF-8")

    name, content = GENERATOR.render_plugin_docs(source, template)

    assert name == "sample"
    assert "A &lt;sample&gt; plugin." in content
    assert "| <samp>&nbsp;&nbsp;&nbsp;&nbsp;child</samp> | any | True | False | - | A &lt;child&gt; |" in content
    assert "|     child | any | A &lt;result&gt; |" in content
    assert examples in content
    assert "- An author\n" in content


def test_missing_documentation_fails(tmp_path: Path, template: Template) -> None:
    """Do not silently leave an old generated page when documentation is missing."""
    source = tmp_path / "missing.py"
    source.write_text("# No documentation\n", encoding="UTF-8")

    with pytest.raises(ValueError, match="No DOCUMENTATION found"):
        GENERATOR.render_plugin_docs(source, template)
