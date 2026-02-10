# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""
Export Excalidraw files to light and dark mode SVGs using Kroki API.

Prerequisites:
    pip install requests

Usage:
    python docs/scripts/export_excalidraw.py [input_dir]

If no input_dir is specified, defaults to docs/_media/excalidraw/
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

try:
    import requests
except ImportError:
    print("Error: requests is not installed")
    print("\nInstall it with:")
    print("  pip install requests")
    sys.exit(1)

KROKI_URL = "https://kroki.io/excalidraw/svg"


def export_excalidraw(file_path: Path, output_path: Path, *, dark_mode: bool = False) -> bool:
    """Export an Excalidraw file to SVG using Kroki API."""
    with file_path.open() as f:
        excalidraw_data: dict[str, Any] = json.load(f)

    # Filter out deleted elements to ensure proper bounding box calculation
    if "elements" in excalidraw_data:
        original_count = len(excalidraw_data["elements"])
        excalidraw_data["elements"] = [e for e in excalidraw_data["elements"] if not e.get("isDeleted", False)]
        filtered_count = len(excalidraw_data["elements"])
        if original_count != filtered_count:
            print(f"  (filtered {original_count - filtered_count} deleted elements)")

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

        with output_path.open("w") as f:
            f.write(svg_content)

    except requests.exceptions.RequestException as e:
        print(f"  ✗ Kroki API error: {e}")
        return False
    else:
        return True


def main() -> None:
    """Export all Excalidraw files to light and dark mode SVGs."""
    input_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("docs/_media/excalidraw")

    if not input_dir.exists():
        print(f"Error: Directory '{input_dir}' does not exist")
        sys.exit(1)

    excalidraw_files = list(input_dir.glob("*.excalidraw"))

    if not excalidraw_files:
        print(f"No .excalidraw files found in {input_dir}")
        sys.exit(0)

    print(f"Exporting {len(excalidraw_files)} Excalidraw files from: {input_dir}\n")

    # Create output directory
    output_dir = input_dir / "exported"
    output_dir.mkdir(exist_ok=True)

    success_count = 0
    for file_path in excalidraw_files:
        name = file_path.stem
        print(f"Processing: {file_path}")

        light_output = output_dir / f"{name}-light.svg"
        dark_output = output_dir / f"{name}-dark.svg"

        print(f"  -> Exporting light mode: {light_output}")
        light_ok = export_excalidraw(file_path, light_output, dark_mode=False)

        print(f"  -> Exporting dark mode: {dark_output}")
        dark_ok = export_excalidraw(file_path, dark_output, dark_mode=True)

        if light_ok and dark_ok:
            print("  ✓ Done\n")
            success_count += 1
        else:
            print("  ✗ Failed\n")

    print(f"Exported {success_count}/{len(excalidraw_files)} files successfully!")


if __name__ == "__main__":
    main()
