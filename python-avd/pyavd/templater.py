# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import importlib.util
import logging
from pathlib import Path
from typing import TYPE_CHECKING, Any

from jinja2 import ChoiceLoader, Environment, FileSystemLoader, ModuleLoader, StrictUndefined, TemplateNotFound
from jinja2.compiler import generate

from .constants import JINJA2_EXTENSIONS, RUNNING_FROM_SRC

if TYPE_CHECKING:
    import os
    from collections.abc import MutableMapping, Sequence

    from jinja2 import Template

LOGGER = logging.getLogger(__name__)

# Constants for registered filters and tests - single source of truth
CUSTOM_FILTERS = [
    "add_md_toc",
    "decrypt",
    "default",
    "encrypt",
    "hide_passwords",
    "is_in_filter",
    "list_compress",
    "natural_sort",
    "range_expand",
    "snmp_hash",
    "status_render",
    "secure_hash",
]

CUSTOM_TESTS = [
    "defined",
    "contains",
]


class Undefined(StrictUndefined):
    """
    Allow nested checks for undefined instead of having to check on every level.

    Example "{% if var.key.subkey is arista.avd.undefined %}" is ok.

    Without this it we would have to test every level, like
    "{% if var is arista.avd.undefined or var.key is arista.avd.undefined or var.key.subkey is arista.avd.undefined %}"
    """

    def __getattr__(self, _name: str) -> Undefined:
        # Return original Undefined object to preserve the first failure context
        return self

    def __getitem__(self, _key: str) -> Undefined:
        # Return original Undefined object to preserve the first failure context
        return self

    def __repr__(self) -> str:
        return f"Undefined(hint={self._undefined_hint}, obj={self._undefined_obj}, name={self._undefined_name})"

    def __contains__(self, _item: int) -> Undefined:
        # Return original Undefined object to preserve the first failure context
        return self


class CustomModuleLoader(ModuleLoader):
    """Custom ModuleLoader that handles readable module names."""

    def __init__(self, path: str | Path) -> None:
        self.path = Path(path).resolve()
        super().__init__(path)

    def load(self, environment: Environment, name: str, globals: MutableMapping[str, Any] | None = None) -> Template:  # noqa: A002
        """Load template using the module name conversion."""
        # Convert template name to module name
        module_name = self._template_name_to_module_name(name)

        # Check if the module is already loaded/cached
        mod = getattr(self.module, module_name, None)

        if mod is None:
            # Build the file path directly
            module_file = self.path / f"{module_name}.py"

            if not module_file.exists():
                raise TemplateNotFound(name)

            # Load module directly from file path (no sys.path needed!)
            spec = importlib.util.spec_from_file_location(module_name, module_file)
            if spec is None or spec.loader is None:
                raise TemplateNotFound(name)

            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)

        # Create template from module dict
        return environment.template_class.from_module_dict(environment, mod.__dict__, globals if globals is not None else {})

    @staticmethod
    def _template_name_to_module_name(template_name: str) -> str:
        """Convert a template name to a module name."""
        normalized = Path(template_name.replace("\\", "/")).as_posix()
        return normalized.replace("/", "__").removesuffix(".j2").replace(".", "_").replace("-", "_")


class Templar:
    def __init__(self, precompiled_templates_path: str | Path, searchpaths: list[str | Path] | None = None) -> None:
        if not RUNNING_FROM_SRC:
            self.loader = CustomModuleLoader(precompiled_templates_path)

        else:
            searchpaths = searchpaths or []
            self.loader = ChoiceLoader(
                [
                    CustomModuleLoader(precompiled_templates_path),
                    FileSystemLoader(searchpaths),
                ],
            )

        # Accepting SonarLint issue: No autoescaping is ok, since we are not using this for a website, so XSS is not applicable.
        self.environment = Environment(  # NOSONAR # noqa: S701
            extensions=JINJA2_EXTENSIONS,
            loader=self.loader,
            undefined=Undefined,
            trim_blocks=True,
        )
        # Backward-compatible compilation for Jinja 3.0.0 to 3.1.x
        if not hasattr(self.environment, "concat"):
            self.environment.concat = "".join

        self.import_filters_and_tests()

    def import_filters_and_tests(self) -> None:
        import importlib  # noqa: PLC0415

        # Dynamically import and register filters from constants
        filters_module = importlib.import_module(".j2filters", package="pyavd")
        for filter_name in CUSTOM_FILTERS:
            filter_func = getattr(filters_module, filter_name)
            self.environment.filters[f"arista.avd.{filter_name}"] = filter_func

        # Dynamically import and register tests from constants
        for test_name in CUSTOM_TESTS:
            test_module = importlib.import_module(f".j2tests.{test_name}", package="pyavd")
            test_func = getattr(test_module, test_name)
            self.environment.tests[f"arista.avd.{test_name}"] = test_func

    def render_template_from_file(self, template_file: str, template_vars: dict) -> str:
        return self.environment.get_template(template_file).render(template_vars)

    def compile_templates_in_paths(self, precompiled_templates_path: str | Path, searchpaths: list[str | Path]) -> None:
        """
        Compile the Jinja2 templates in the path with readable module names.

        The FileSystemLoader tries to compile any file in the path no matter the extension so
        this uses a custom one.

        Parameters
        ----------
            searchpaths: The list of path to search templates in.
        """
        precompiled_path = Path(precompiled_templates_path)
        precompiled_path.mkdir(parents=True, exist_ok=True)

        self.environment.loader = ExtensionFileSystemLoader(searchpaths)

        # Get all templates
        templates = self.environment.loader.list_templates()

        # Track module names to detect collisions
        module_name_map: dict[str, str] = {}

        # Compile each template with a readable name
        for template_name in templates:
            # Get the template source
            source, filename, _uptodate = self.environment.loader.get_source(self.environment, template_name)

            # Parse and compile to Python source code
            try:
                code = self.environment.parse(source, template_name, filename)
                module_code = generate(code, self.environment, template_name, filename, defer_init=True)
            except Exception as exc:
                msg = f"Failed to compile template {template_name}"
                raise RuntimeError(msg) from exc

            if module_code is None:
                msg = f"Failed to generate code for template {template_name}"
                raise RuntimeError(msg)

            # Create a readable module name from template path
            module_name = CustomModuleLoader._template_name_to_module_name(template_name)

            # Check for module name collision
            if module_name in module_name_map:
                msg = (
                    f"Module name collision detected: templates '{module_name_map[module_name]}' and '{template_name}' "
                    f"both resolve to module name '{module_name}'. "
                    "Template names must be unique after normalization (replacing '/', '\\', '.', '-' with '_')."
                )
                raise ValueError(msg)
            module_name_map[module_name] = template_name

            # Write to file with proper module structure for ModuleLoader
            output_file = precompiled_path / f"{module_name}.py"
            output_file.parent.mkdir(parents=True, exist_ok=True)

            with output_file.open("w", encoding="utf-8") as f:
                # Write the generated code (already includes necessary imports and name)
                f.write(module_code)

        self.environment.loader = self.loader


class ExtensionFileSystemLoader(FileSystemLoader):
    """Custom Jinja2 loader that filters on extensions."""

    def __init__(
        self,
        searchpath: str | os.PathLike[str] | Sequence[str | os.PathLike[str]],
        encoding: str = "utf-8",
        followlinks: bool = False,
        extensions: list[str] | None = None,
    ) -> None:
        self.extensions = extensions or [".j2"]
        super().__init__(searchpath, encoding, followlinks)

    def list_templates(self) -> list[str]:
        """Filter found files from FileSystemLoader using extensions."""
        found = super().list_templates()
        return [file for file in found if Path(file).suffix in self.extensions]
