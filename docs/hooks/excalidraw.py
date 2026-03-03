# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""
MkDocs hook for Excalidraw integration with light/dark mode support.

This hook processes special Excalidraw image references in markdown and
generates the appropriate HTML with both light and dark mode variants.

Usage in markdown:
    ![Alt text](path/to/diagram.excalidraw)

The hook expects pre-exported SVG files with -light.svg and -dark.svg suffixes
in an 'exported/' subdirectory relative to the .excalidraw file:
    path/to/exported/diagram-light.svg
    path/to/exported/diagram-dark.svg

These will be rendered as two images that show/hide based on the current theme.
"""

from __future__ import annotations

import logging
import re
from pathlib import Path
from typing import Any

log = logging.getLogger("mkdocs.hooks.excalidraw")

# Pattern to match markdown image references to .excalidraw files
# Matches: ![alt text](path/to/file.excalidraw) or ![alt text](path/to/file.excalidraw "title")
EXCALIDRAW_PATTERN = re.compile(r"!\[([^\]]*)\]\(([^)]+\.excalidraw)(?:\s+\"([^\"]*)\")?\)")


def on_page_markdown(markdown: str, page: Any, config: Any, files: Any, **kwargs: Any) -> str:  # noqa: ARG001
    """Process markdown content and replace .excalidraw image references with light/dark mode image pairs."""
    # Check if there are any .excalidraw references in this page
    if ".excalidraw" in markdown:
        log.info("Processing Excalidraw references in: %s", page.file.src_path)

    def replace_excalidraw(match: re.Match) -> str:  # type: ignore[type-arg]
        alt_text = match.group(1)
        excalidraw_path = match.group(2)
        title = match.group(3) or alt_text

        # Use pathlib to parse the excalidraw path
        excalidraw_file = Path(excalidraw_path)
        base_name = excalidraw_file.stem  # Removes .excalidraw extension

        # Build paths to exported/ subdirectory using pathlib
        exported_dir = excalidraw_file.parent / "exported"
        light_path = exported_dir / f"{base_name}-light.svg"
        dark_path = exported_dir / f"{base_name}-dark.svg"

        # Check if the exported SVGs exist on disk
        page_src_path = Path(page.file.src_path).parent
        docs_dir = Path(config["docs_dir"])

        # Resolve the path relative to the current page
        check_base = docs_dir / excalidraw_path.lstrip("/") if excalidraw_path.startswith("/") else docs_dir / page_src_path / excalidraw_path

        check_base = check_base.resolve()
        light_file = check_base.parent / "exported" / f"{base_name}-light.svg"
        dark_file = check_base.parent / "exported" / f"{base_name}-dark.svg"

        # Warn if SVG files don't exist
        if not light_file.exists():
            log.warning("Excalidraw light mode SVG not found: %s (referenced from %s)", light_file, page.file.src_path)
        if not dark_file.exists():
            log.warning("Excalidraw dark mode SVG not found: %s (referenced from %s)", dark_file, page.file.src_path)

        # Generate markdown with Material's #only-light and #only-dark fragments
        # Using two separate image tags that show/hide based on theme
        title_attr = f' "{title}"' if title else ""

        # Convert Path objects to POSIX-style strings for markdown URLs
        result = f"![{alt_text}]({light_path.as_posix()}#only-light{title_attr})\n![{alt_text}]({dark_path.as_posix()}#only-dark{title_attr})"

        log.debug("Replaced Excalidraw reference: %s -> light/dark SVGs", excalidraw_path)

        return result

    # Replace all .excalidraw image references
    return EXCALIDRAW_PATTERN.sub(replace_excalidraw, markdown)
