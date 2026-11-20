#!/usr/bin/env python3

# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Render Ansible plugin documentation with the existing AVD Markdown template."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

import yaml
from ansible.plugins.loader import fragment_loader, init_plugin_loader
from ansible.utils.plugin_docs import get_docstring
from jinja2 import Environment, FileSystemLoader, Template

REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
TEMPLATE_PATH = REPOSITORY_ROOT / "docs/templates/plugin-docs.j2"


def ensure_list(value: Any) -> list:
    """Normalize scalar documentation fields for the Markdown template."""
    return value if isinstance(value, list) else [value]


def normalize_descriptions(definitions: dict) -> None:
    """Normalize descriptions in nested parameter and return-value definitions."""
    for definition in definitions.values():
        if "description" in definition:
            definition["description"] = ensure_list(definition["description"])
        for key in ("suboptions", "contains"):
            if key in definition:
                normalize_descriptions(definition[key])


def render_plugin_docs(source: Path, template: Template) -> tuple[str, str]:
    """Read documentation without importing the plugin and render its Markdown."""
    # Ansible 2.19 and later require absolute paths for documentation source locations.
    doc, examples, returns, metadata = get_docstring(str(source.resolve()), fragment_loader)
    if not doc:
        msg = f"No DOCUMENTATION found in {source}"
        raise ValueError(msg)

    if isinstance(returns, str):
        returns = yaml.safe_load(returns)
    doc.update(examples=examples, returndocs=returns or {}, metadata=metadata)
    for key in ("author", "description"):
        if key in doc:
            doc[key] = ensure_list(doc[key])
    normalize_descriptions(doc.get("options", {}))
    normalize_descriptions(doc["returndocs"])

    if "module" in doc:
        doc["plugin_type"] = "module"
    else:
        doc["module"] = doc["name"].rsplit(".", 1)[-1]

    return doc["module"], template.render(doc)


def main() -> None:
    """Generate Markdown pages for the plugin files passed by pre-commit."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, help="Directory for generated Markdown pages")
    parser.add_argument("plugins", type=Path, nargs="+", help="Python plugins or YAML documentation files")
    args = parser.parse_args()

    init_plugin_loader()
    environment = Environment(loader=FileSystemLoader(TEMPLATE_PATH.parent), trim_blocks=True, autoescape=False)  # noqa: S701
    template = environment.get_template(TEMPLATE_PATH.name)
    args.output.mkdir(parents=True, exist_ok=True)
    for source in args.plugins:
        name, content = render_plugin_docs(source, template)
        output_path = args.output / f"{name}.md"
        if not output_path.exists() or output_path.read_text(encoding="UTF-8") != content:
            output_path.write_text(content, encoding="UTF-8")
            print(f"Updated {output_path}")


if __name__ == "__main__":
    main()
