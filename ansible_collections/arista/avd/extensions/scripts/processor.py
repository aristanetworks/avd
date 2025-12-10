# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import logging
import sys
from pathlib import Path

import yaml

# Configure Logging
logging.basicConfig(level=logging.INFO, format="%(message)s", stream=sys.stdout)
logger = logging.getLogger(__name__)


def load_file(filepath: str) -> list[str] | None:
    """Safely loads a text file using pathlib."""
    path = Path(filepath)

    if not path.exists():
        logger.error("ERROR: File not found: %s", filepath)
        return None

    with path.open("r", encoding="utf-8") as f:
        return f.read().splitlines()


def extract_section(lines: list[str], section_header: str) -> list[str]:
    """Extracts a specific configuration section based on indentation."""
    buffer: list[str] = []
    capture: bool = False

    for line in lines:
        stripped = line.strip()

        # Check start of section
        if line.startswith(section_header) and not capture:
            capture = True
            buffer.append(line)
            continue

        # Capture logic
        if capture:
            if not stripped:
                continue

            indent_level = len(line) - len(line.lstrip())

            # Stop if we hit a non-indented line that is NOT a comment/separator
            if indent_level == 0 and not line.startswith("!"):
                break

            buffer.append(line)

    return buffer


def process_config(config_path: str, output_dir: str) -> None:
    """Main logic to process the configuration and write artifacts."""
    # G004 Fixes
    logger.info("--- Loading Config: %s ---", config_path)
    logger.info("--- Output Directory: %s ---", output_dir)

    out_path = Path(output_dir)

    if not out_path.exists():
        out_path.mkdir(parents=True, exist_ok=True)

    cfg_path = Path(config_path)

    with cfg_path.open("r", encoding="utf-8") as f:
        jobs = yaml.safe_load(f)

    for job in jobs:
        target_file: str = job.get("file")
        sections_to_find: list[str] = job.get("sections", [])
        artifact_filename: str = job.get("artifact")

        full_output_path = out_path / artifact_filename

        logger.info("Processing target: %s", target_file)

        eos_lines = load_file(target_file)
        if not eos_lines:
            continue

        extracted_data: list[str] = []

        for header in sections_to_find:
            block = extract_section(eos_lines, header)

            if block:
                # Clean up trailing '!'s
                while block and block[-1].strip() == "!":
                    block.pop()

                extracted_data.extend(block)
                # Add exactly one separator after the clean block
                extracted_data.append("!")

        if extracted_data:
            with full_output_path.open("w", encoding="utf-8") as out:
                out.write("\n".join(extracted_data))
            logger.info("  > Saved to %s", full_output_path)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        logger.error("Usage: python3 processor.py <path_to_config.yml> <output_directory>")
        sys.exit(1)

    process_config(sys.argv[1], sys.argv[2])
