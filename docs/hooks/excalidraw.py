# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""
MkDocs hook for Excalidraw integration with light/dark mode support.

This hook processes special Excalidraw image references in markdown and
automatically exports them to SVG files with light and dark mode variants.

Usage in markdown:
    ![Alt text](path/to/diagram.excalidraw)

The hook will automatically export the .excalidraw file to SVG files:
    path/to/exported/diagram_light.svg
    path/to/exported/diagram_dark.svg

These will be rendered as two images that show/hide based on the current theme.

The export uses the Kroki API (https://kroki.io) to convert Excalidraw JSON to SVG.
"""

from __future__ import annotations

import json
import logging
import re
from pathlib import Path
from typing import Any

try:
    import requests
except ImportError:
    requests = None  # type: ignore[assignment]

log = logging.getLogger("mkdocs.hooks.excalidraw")

KROKI_URL = "https://kroki.io/excalidraw/svg"

# Pattern to match markdown image references to .excalidraw files
# Matches: ![alt text](path/to/file.excalidraw) or ![alt text](path/to/file.excalidraw "title")
EXCALIDRAW_PATTERN = re.compile(r"!\[([^\]]*)\]\(([^)]+\.excalidraw)(?:\s+\"([^\"]*)\")?\)")


def export_excalidraw_to_svg(excalidraw_file: Path, output_path: Path, *, dark_mode: bool = False) -> bool:
    """Export an Excalidraw file to SVG using Kroki API."""
    if requests is None:
        log.error("requests library is not installed. Cannot export Excalidraw files.")
        log.error("Install it with: pip install requests")
        return False

    try:
        with excalidraw_file.open() as f:
            excalidraw_data: dict[str, Any] = json.load(f)
    except (OSError, json.JSONDecodeError):
        log.exception("Failed to read Excalidraw file %s", excalidraw_file)
        return False

    # Filter out deleted elements to ensure proper bounding box calculation
    if "elements" in excalidraw_data:
        original_count = len(excalidraw_data["elements"])
        excalidraw_data["elements"] = [e for e in excalidraw_data["elements"] if not e.get("isDeleted", False)]
        filtered_count = len(excalidraw_data["elements"])
        if original_count != filtered_count:
            log.debug("Filtered %d deleted elements from %s", original_count - filtered_count, excalidraw_file.name)

    # Set the theme in appState for Excalidraw's native dark mode
    if "appState" not in excalidraw_data:
        excalidraw_data["appState"] = {}

    excalidraw_data["appState"]["theme"] = "dark" if dark_mode else "light"
    excalidraw_data["appState"]["exportBackground"] = False  # Transparent background
    excalidraw_data["appState"]["exportWithDarkMode"] = dark_mode

    # Convert to JSON string
    json_str = json.dumps(excalidraw_data)

    # Send to Kroki API via POST
    try:
        response = requests.post(
            KROKI_URL,
            json={"diagram_source": json_str},
            headers={"Content-Type": "application/json"},
            timeout=30,
        )
        response.raise_for_status()

        svg_content = response.text

        # Create output directory if needed
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with output_path.open("w") as f:
            f.write(svg_content)

    except requests.exceptions.RequestException:
        log.exception("Kroki API error while exporting %s", excalidraw_file)
        return False
    except OSError:
        log.exception("Failed to write SVG file %s", output_path)
        return False
    else:
        log.info("Exported %s to %s", excalidraw_file.name, output_path)
        return True


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
        light_path = exported_dir / f"{base_name}_light.svg"
        dark_path = exported_dir / f"{base_name}_dark.svg"

        # Check if the exported SVGs exist on disk
        page_src_path = Path(page.file.src_path).parent
        docs_dir = Path(config["docs_dir"])

        # Resolve the path relative to the current page
        check_base = docs_dir / excalidraw_path.lstrip("/") if excalidraw_path.startswith("/") else docs_dir / page_src_path / excalidraw_path

        check_base = check_base.resolve()
        exported_dir_abs = check_base.parent / "exported"
        light_file = exported_dir_abs / f"{base_name}_light.svg"
        dark_file = exported_dir_abs / f"{base_name}_dark.svg"

        # Check if we need to export (file doesn't exist or is older than source)
        needs_export = False
        if not light_file.exists() or not dark_file.exists():
            needs_export = True
            log.info("SVG files missing for %s, will export", check_base.name)
        elif check_base.exists():
            # Check if source is newer than exported files
            source_mtime = check_base.stat().st_mtime
            if light_file.stat().st_mtime < source_mtime or dark_file.stat().st_mtime < source_mtime:
                needs_export = True
                log.info("Source file %s is newer than exported SVGs, will re-export", check_base.name)

        # Export if needed
        if needs_export and check_base.exists():
            log.info("Exporting %s to SVG files", check_base)
            export_excalidraw_to_svg(check_base, light_file, dark_mode=False)
            export_excalidraw_to_svg(check_base, dark_file, dark_mode=True)
        elif not check_base.exists():
            log.warning("Excalidraw source file not found: %s (referenced from %s)", check_base, page.file.src_path)

        # Final check - warn if SVG files still don't exist after export attempt
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
