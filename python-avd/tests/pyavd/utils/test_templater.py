# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from jinja2 import TemplateNotFound

from pyavd.templater import CUSTOM_FILTERS, CUSTOM_TESTS, CustomModuleLoader, ExtensionFileSystemLoader, Templar, Undefined

if TYPE_CHECKING:
    from pathlib import Path


@pytest.fixture
def template_files(tmp_path: Path) -> dict[str, Path]:
    """Create temporary template files for testing."""
    template_dir = tmp_path / "templates"
    template_dir.mkdir()

    # Simple template
    simple_template = template_dir / "simple.j2"
    simple_template.write_text("Hello {{ name }}!")

    # Template with nested variable access
    nested_template = template_dir / "nested.j2"
    nested_template.write_text("Value: {{ data.nested.value }}")

    # Template with undefined check
    undefined_template = template_dir / "undefined.j2"
    undefined_template.write_text("{% if var.missing.key is arista.avd.defined %}defined{% else %}undefined{% endif %}")

    # Non-jinja file (should be ignored by ExtensionFileSystemLoader)
    non_jinja = template_dir / "readme.txt"
    non_jinja.write_text("This is not a template")

    # Subdirectory template
    subdir = template_dir / "subdir"
    subdir.mkdir()
    subdir_template = subdir / "sub.j2"
    subdir_template.write_text("Subdir: {{ value }}")

    return {
        "template_dir": template_dir,
        "simple": simple_template,
        "nested": nested_template,
        "undefined": undefined_template,
        "non_jinja": non_jinja,
        "subdir": subdir_template,
    }


@pytest.fixture
def precompiled_dir(tmp_path: Path) -> Path:
    """Create directory for precompiled templates."""
    precompiled = tmp_path / "precompiled"
    precompiled.mkdir()
    return precompiled


class TestUndefined:
    """Test the custom Undefined class."""

    def test_undefined_getattr_returns_self(self) -> None:
        """Test that accessing attributes on Undefined returns itself."""
        undef = Undefined()
        result = undef.some_attr
        assert isinstance(result, Undefined)
        assert result is undef

    def test_undefined_getitem_returns_self(self) -> None:
        """Test that accessing items on Undefined returns itself."""
        undef = Undefined()
        result = undef["some_key"]
        assert isinstance(result, Undefined)
        assert result is undef

    def test_undefined_contains_returns_self(self) -> None:
        """Test that contains check on Undefined returns itself."""
        undef = Undefined()
        result = undef.__contains__(1)
        assert isinstance(result, Undefined)
        assert result is undef

    def test_undefined_chained_access(self) -> None:
        """Test that chained access on Undefined preserves the original object."""
        undef = Undefined()
        result = undef.level1.level2.level3["key"]
        assert isinstance(result, Undefined)
        assert result is undef


class TestExtensionFileSystemLoader:
    """Test the ExtensionFileSystemLoader class."""

    def test_default_extensions(self, template_files: dict[str, Path]) -> None:
        """Test that default extensions filter is .j2."""
        loader = ExtensionFileSystemLoader(template_files["template_dir"])
        templates = loader.list_templates()

        # Should include .j2 files
        assert "simple.j2" in templates
        assert "nested.j2" in templates
        assert "subdir/sub.j2" in templates

        # Should exclude non-.j2 files
        assert "readme.txt" not in templates

    def test_custom_extensions(self, tmp_path: Path) -> None:
        """Test custom extensions filtering."""
        template_dir = tmp_path / "templates"
        template_dir.mkdir()

        (template_dir / "template.j2").write_text("j2 file")
        (template_dir / "template.jinja").write_text("jinja file")
        (template_dir / "template.txt").write_text("txt file")

        loader = ExtensionFileSystemLoader(template_dir, extensions=[".j2", ".jinja"])
        templates = loader.list_templates()

        assert "template.j2" in templates
        assert "template.jinja" in templates
        assert "template.txt" not in templates


class TestCustomModuleLoader:
    """Test the CustomModuleLoader class."""

    def test_template_name_to_module_name(self) -> None:
        """Test template name to module name conversion."""
        assert CustomModuleLoader._template_name_to_module_name("simple.j2") == "simple"
        assert CustomModuleLoader._template_name_to_module_name("path/to/template.j2") == "path__to__template"
        assert CustomModuleLoader._template_name_to_module_name("windows\\path\\template.j2") == "windows__path__template"
        assert CustomModuleLoader._template_name_to_module_name("file-name.j2") == "file_name"
        assert CustomModuleLoader._template_name_to_module_name("file.name.j2") == "file_name"

    def test_template_name_normalization_handles_redundant_separators(self) -> None:
        """Test that path normalization handles redundant separators."""
        # Redundant forward slashes
        assert CustomModuleLoader._template_name_to_module_name("foo//bar/baz.j2") == "foo__bar__baz"
        # Redundant backslashes
        assert CustomModuleLoader._template_name_to_module_name("foo\\\\bar\\baz.j2") == "foo__bar__baz"

    def test_template_name_normalization_cross_platform(self) -> None:
        """Test that path normalization produces consistent results across platforms."""
        # Windows-style path
        windows_result = CustomModuleLoader._template_name_to_module_name("templates\\config\\device.j2")
        # Unix-style path
        unix_result = CustomModuleLoader._template_name_to_module_name("templates/config/device.j2")

        # Both should produce the same module name
        assert windows_result == unix_result == "templates__config__device"

    def test_load_nonexistent_template_raises(self, precompiled_dir: Path) -> None:
        """Test that loading a non-existent template raises TemplateNotFound."""
        from jinja2 import Environment

        loader = CustomModuleLoader(precompiled_dir)
        env = Environment(loader=loader, autoescape=True)

        with pytest.raises(TemplateNotFound):
            loader.load(env, "nonexistent.j2")


class TestTemplar:
    """Test the Templar class."""

    def test_init_with_module_loader_only(self, precompiled_dir: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Test initialization with only module loader (RUNNING_FROM_SRC=False)."""
        monkeypatch.setattr("pyavd.templater.RUNNING_FROM_SRC", False)

        templar = Templar(precompiled_templates_path=precompiled_dir)

        assert isinstance(templar.loader, CustomModuleLoader)

    def test_init_with_choice_loader(self, precompiled_dir: Path, template_files: dict[str, Path], monkeypatch: pytest.MonkeyPatch) -> None:
        """Test initialization with ChoiceLoader (RUNNING_FROM_SRC=True)."""
        from jinja2 import ChoiceLoader

        monkeypatch.setattr("pyavd.templater.RUNNING_FROM_SRC", True)

        templar = Templar(precompiled_templates_path=precompiled_dir, searchpaths=[template_files["template_dir"]])

        assert isinstance(templar.loader, ChoiceLoader)

    def test_environment_has_custom_undefined(self, precompiled_dir: Path) -> None:
        """Test that environment uses custom Undefined class."""
        templar = Templar(precompiled_templates_path=precompiled_dir)

        assert templar.environment.undefined is Undefined

    def test_environment_has_filters(self, precompiled_dir: Path) -> None:
        """Test that environment has all custom filters registered."""
        templar = Templar(precompiled_templates_path=precompiled_dir)

        expected_filters = [f"arista.avd.{name}" for name in CUSTOM_FILTERS]

        for filter_name in expected_filters:
            assert filter_name in templar.environment.filters

    def test_environment_has_tests(self, precompiled_dir: Path) -> None:
        """Test that environment has all custom tests registered."""
        templar = Templar(precompiled_templates_path=precompiled_dir)

        expected_tests = [f"arista.avd.{name}" for name in CUSTOM_TESTS]

        for test_name in expected_tests:
            assert test_name in templar.environment.tests

    def test_render_template_from_file(self, precompiled_dir: Path, template_files: dict[str, Path], monkeypatch: pytest.MonkeyPatch) -> None:
        """Test rendering a template from file."""
        monkeypatch.setattr("pyavd.templater.RUNNING_FROM_SRC", True)

        templar = Templar(precompiled_templates_path=precompiled_dir, searchpaths=[template_files["template_dir"]])

        result = templar.render_template_from_file("simple.j2", {"name": "World"})

        assert result == "Hello World!"

    def test_render_nested_template(self, precompiled_dir: Path, template_files: dict[str, Path], monkeypatch: pytest.MonkeyPatch) -> None:
        """Test rendering a template with nested variable access."""
        monkeypatch.setattr("pyavd.templater.RUNNING_FROM_SRC", True)

        templar = Templar(precompiled_templates_path=precompiled_dir, searchpaths=[template_files["template_dir"]])

        result = templar.render_template_from_file("nested.j2", {"data": {"nested": {"value": 42}}})

        assert result == "Value: 42"

    def test_compile_templates_in_paths(self, precompiled_dir: Path, template_files: dict[str, Path]) -> None:
        """Test compiling templates to precompiled modules."""
        templar = Templar(precompiled_templates_path=precompiled_dir, searchpaths=[template_files["template_dir"]])

        # Compile templates
        templar.compile_templates_in_paths(precompiled_templates_path=precompiled_dir, searchpaths=[template_files["template_dir"]])

        # Verify compiled files exist
        assert (precompiled_dir / "simple.py").exists()
        assert (precompiled_dir / "nested.py").exists()
        assert (precompiled_dir / "undefined.py").exists()
        assert (precompiled_dir / "subdir__sub.py").exists()

        # Verify non-jinja files were not compiled
        assert not (precompiled_dir / "readme.py").exists()

    def test_compiled_templates_are_valid_python(self, precompiled_dir: Path, template_files: dict[str, Path]) -> None:
        """Test that compiled templates are valid Python modules."""
        templar = Templar(precompiled_templates_path=precompiled_dir, searchpaths=[template_files["template_dir"]])

        templar.compile_templates_in_paths(precompiled_templates_path=precompiled_dir, searchpaths=[template_files["template_dir"]])

        # Try to compile the generated Python file
        compiled_file = precompiled_dir / "simple.py"
        code = compiled_file.read_text()

        # Should not raise SyntaxError
        compile(code, str(compiled_file), "exec")

    def test_compile_templates_with_invalid_template(self, precompiled_dir: Path, tmp_path: Path) -> None:
        """Test that compilation fails gracefully with invalid template."""
        template_dir = tmp_path / "invalid_templates"
        template_dir.mkdir()

        # Create invalid template
        invalid_template = template_dir / "invalid.j2"
        invalid_template.write_text("{% for item in items %}{{ item }}")  # Missing {% endfor %}

        templar = Templar(precompiled_templates_path=precompiled_dir, searchpaths=[template_dir])

        with pytest.raises(RuntimeError, match=r"Failed to compile template invalid\.j2"):
            templar.compile_templates_in_paths(precompiled_templates_path=precompiled_dir, searchpaths=[template_dir])

    def test_render_from_compiled_template(self, precompiled_dir: Path, template_files: dict[str, Path], monkeypatch: pytest.MonkeyPatch) -> None:
        """Test rendering from a precompiled template."""
        # First compile the templates
        templar_compile = Templar(precompiled_templates_path=precompiled_dir, searchpaths=[template_files["template_dir"]])
        templar_compile.compile_templates_in_paths(precompiled_templates_path=precompiled_dir, searchpaths=[template_files["template_dir"]])

        # Now render using only the module loader (simulating non-dev environment)
        monkeypatch.setattr("pyavd.templater.RUNNING_FROM_SRC", False)
        templar_render = Templar(precompiled_templates_path=precompiled_dir)

        result = templar_render.render_template_from_file("simple.j2", {"name": "Compiled"})

        assert result == "Hello Compiled!"

    def test_backward_compatibility_concat(self, precompiled_dir: Path) -> None:
        """Test backward compatibility for Jinja 3.0.0 to 3.1.x concat attribute."""
        templar = Templar(precompiled_templates_path=precompiled_dir)

        # The concat attribute should be set
        assert hasattr(templar.environment, "concat")
        assert callable(templar.environment.concat)
        # Test that concat works like "".join
        assert templar.environment.concat(["a", "b", "c"]) == "abc"

    def test_compile_templates_collision_detection_dash_vs_underscore(self, precompiled_dir: Path, tmp_path: Path) -> None:
        """Test that collision is detected between templates with dashes and underscores."""
        template_dir = tmp_path / "collision_templates"
        template_dir.mkdir()

        # Create templates that would collide: aa-aa.j2 and aa_aa.j2
        (template_dir / "aa-aa.j2").write_text("Template with dashes")
        (template_dir / "aa_aa.j2").write_text("Template with underscores")

        templar = Templar(precompiled_templates_path=precompiled_dir, searchpaths=[template_dir])

        with pytest.raises(ValueError, match=r"Module name collision detected.*aa-aa\.j2.*aa_aa\.j2.*aa_aa"):
            templar.compile_templates_in_paths(precompiled_templates_path=precompiled_dir, searchpaths=[template_dir])

    def test_compile_templates_collision_detection_dot_vs_dash(self, precompiled_dir: Path, tmp_path: Path) -> None:
        """Test that collision is detected between templates with dots and dashes."""
        template_dir = tmp_path / "collision_templates"
        template_dir.mkdir()

        # Create templates that would collide: foo.bar.j2 and foo-bar.j2
        (template_dir / "foo.bar.j2").write_text("Template with dots")
        (template_dir / "foo-bar.j2").write_text("Template with dashes")

        templar = Templar(precompiled_templates_path=precompiled_dir, searchpaths=[template_dir])

        # The regex accepts either order of the template names since list_templates() order may vary
        with pytest.raises(ValueError, match=r"Module name collision detected.*foo[.-]bar\.j2.*foo[.-]bar\.j2.*foo_bar"):
            templar.compile_templates_in_paths(precompiled_templates_path=precompiled_dir, searchpaths=[template_dir])

    def test_compile_templates_no_collision_different_names(self, precompiled_dir: Path, tmp_path: Path) -> None:
        """Test that no collision is raised for genuinely different template names."""
        template_dir = tmp_path / "no_collision_templates"
        template_dir.mkdir()

        # Create templates with different names
        (template_dir / "template_one.j2").write_text("Template one")
        (template_dir / "template_two.j2").write_text("Template two")
        (template_dir / "my-config.j2").write_text("Config template")

        templar = Templar(precompiled_templates_path=precompiled_dir, searchpaths=[template_dir])

        # Should compile without error
        templar.compile_templates_in_paths(precompiled_templates_path=precompiled_dir, searchpaths=[template_dir])

        # Verify all templates were compiled
        assert (precompiled_dir / "template_one.py").exists()
        assert (precompiled_dir / "template_two.py").exists()
        assert (precompiled_dir / "my_config.py").exists()
