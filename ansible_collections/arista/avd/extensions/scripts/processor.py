# Copyright (c) 2025-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import logging
import sys
from pathlib import Path

import yaml

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


def is_strict_match(line: str, pattern: str) -> bool:
    """
    Checks if 'line' matches 'pattern' strictly.

    Match is valid if:
    1. line == pattern (Exact match)
    2. line starts with "pattern " (Pattern followed by space)
    """
    clean_line = line.rstrip()

    if clean_line == pattern:
        return True

    return clean_line.startswith(pattern + " ")


def extract_section(lines: list[str], section_header: str) -> list[str]:
    """Extracts a specific configuration section based on indentation."""
    buffer: list[str] = []
    capture: bool = False

    for line in lines:
        stripped = line.strip()

        if not capture:
            match = is_strict_match(line, section_header)
            if match:
                capture = True
                buffer.append(line)
                continue

        if capture:
            if not stripped:
                continue

            indent_level = len(line) - len(line.lstrip())

            # Stop if we hit a non-indented line that is NOT a comment
            if indent_level == 0 and not line.startswith("!"):
                break

            buffer.append(line)

    return buffer


def apply_filters(block: list[str], filters: list[str]) -> list[str]:
    """Filters a captured block hierarchically with strict matching."""
    if not block or not filters:
        return block

    filtered_block: list[str] = [block[0]]

    keep_barrier: int | None = None
    skip_barrier: int | None = None
    pending_separator: str | None = None

    for line in block[1:]:
        stripped_line = line.strip()

        # Preserve blank lines only if we are inside a kept block
        if not stripped_line:
            if keep_barrier is not None:
                filtered_block.append(line)
            continue

        current_indent = len(line) - len(line.lstrip())

        # 1. Skip Barrier Check
        if skip_barrier is not None:
            if current_indent > skip_barrier:
                continue
            skip_barrier = None

        # 2. Keep Barrier Check
        if keep_barrier is not None:
            if current_indent > keep_barrier:
                filtered_block.append(line)
                continue
            keep_barrier = None

        # 3. Special Handling for Separators (!)
        if stripped_line == "!":
            pending_separator = line
            continue

        # 4. Filter Check
        is_match = any(is_strict_match(stripped_line, f) for f in filters)

        if is_match:
            # Inject buffered separator if it exists
            if pending_separator:
                filtered_block.append(pending_separator)
                pending_separator = None

            filtered_block.append(line)
            keep_barrier = current_indent
        else:
            skip_barrier = current_indent
            pending_separator = None

    return filtered_block


def process_config(config_path: str, output_dir: str | None = None) -> None:
    logger.info("--- Loading Config: %s ---", config_path)

    cfg_path = Path(config_path)
    with cfg_path.open("r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    # Support both list format (legacy) and dict format with base_path
    if isinstance(config, list):
        jobs = config
        base_path = ""
    elif isinstance(config, dict):
        jobs = config.get("artifacts", [])
        base_path = config.get("base_path", "")
    else:
        logger.error("ERROR: Invalid config format. Expected list or dict.")
        return

    for job in jobs:
        target_file: str = job.get("file")
        sections_def: list[str | dict] = job.get("sections", [])
        artifact_filename: str = job.get("artifact")

        # Use job-specific output_dir if provided, otherwise use the global one
        job_output_dir: str | None = job.get("output_dir")
        final_output_dir: str | None = job_output_dir or output_dir

        if not final_output_dir:
            logger.error("ERROR: No output_dir specified for artifact '%s'", artifact_filename)
            continue

        # Prepend base_path if defined and output_dir is not absolute
        out_path = Path(base_path) / final_output_dir if base_path and not Path(final_output_dir).is_absolute() else Path(final_output_dir)
        if not out_path.exists():
            out_path.mkdir(parents=True, exist_ok=True)

        full_output_path = out_path / artifact_filename
        logger.info("Processing target: %s -> %s", target_file, full_output_path)

        eos_lines = load_file(target_file)
        if not eos_lines:
            continue

        extracted_data: list[str] = []

        for item in sections_def:
            if isinstance(item, str):
                header = item
                filters = []
            elif isinstance(item, dict):
                header = item.get("header")
                filters = item.get("filters", [])
            else:
                continue

            raw_block = extract_section(eos_lines, header)

            if raw_block:
                final_block = apply_filters(raw_block, filters) if filters else raw_block

                # Clean up any trailing separators that might have been left over
                while final_block and final_block[-1].strip() == "!":
                    final_block.pop()

                extracted_data.extend(final_block)
                extracted_data.append("!")

            else:
                logger.warning("  > Section '%s' not found.", header)

        if extracted_data:
            extracted_data[-1] = extracted_data[-1] + "\n"
            with full_output_path.open("w", encoding="utf-8") as out:
                out.write("\n".join(extracted_data))
            logger.info("  > Saved to %s", full_output_path)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        logger.error("Usage: python3 processor.py <config.yml> [output_dir]")
        logger.error("  If output_dir is not provided, each artifact must specify 'output_dir' in the config.")
        sys.exit(1)

    config_file = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) >= 3 else None

    process_config(config_file, output_dir)
