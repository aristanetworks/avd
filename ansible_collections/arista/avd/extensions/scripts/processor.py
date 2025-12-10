# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import sys
import yaml
import logging
from pathlib import Path
from typing import List, Optional, Union, Dict

# Configure Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(message)s',
    stream=sys.stdout
)
logger = logging.getLogger(__name__)

def load_file(filepath: str) -> Optional[List[str]]:
    """Safely loads a text file using pathlib."""
    path = Path(filepath)
    if not path.exists():
        logger.error("ERROR: File not found: %s", filepath)
        return None
    with path.open("r", encoding="utf-8") as f:
        return f.read().splitlines()

def extract_section(lines: List[str], section_header: str) -> List[str]:
    """Extracts a specific configuration section based on indentation."""
    buffer: List[str] = []
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

            # Stop if we hit a non-indented line that is NOT a comment
            if indent_level == 0 and not line.startswith("!"):
                break

            buffer.append(line)

    return buffer

def apply_filters(block: List[str], filters: List[str]) -> List[str]:
    """
    Filters a captured block hierarchically.
    - If a line matches a filter: Keep it, and auto-keep all its children.
    - If a line fails filter: Skip it, and auto-skip all its children.
    """
    if not block or not filters:
        return block

    # Always keep the main header (e.g., 'router bgp...')
    filtered_block: List[str] = [block[0]]

    # State tracking
    keep_barrier: Optional[int] = None
    skip_barrier: Optional[int] = None

    # Iterate content lines (skipping the header at index 0)
    for line in block[1:]:
        stripped_line = line.strip()

        # If blank line, preserve if we are in a 'keep' block, otherwise skip?
        # Usually safer to skip unless we are strictly keeping children.
        if not stripped_line:
            if keep_barrier is not None:
                filtered_block.append(line)
            continue

        current_indent = len(line) - len(line.lstrip())

        # 1. Check if we are stuck in a "Skip Block" (children of a rejected parent)
        if skip_barrier is not None:
            if current_indent > skip_barrier:
                continue # Strictly skip this child
            else:
                # We have returned to the parent level or higher
                skip_barrier = None

        # 2. Check if we are inside a "Keep Block" (children of an accepted parent)
        if keep_barrier is not None:
            if current_indent > keep_barrier:
                filtered_block.append(line) # Automatically keep child
                continue
            else:
                # We have returned to the parent level or higher
                keep_barrier = None

        # 3. Decision Time: We are at a new "node" in the config tree
        # Check if this line matches any user filter
        is_match = any(stripped_line.startswith(f) for f in filters)

        if is_match:
            filtered_block.append(line)
            keep_barrier = current_indent # Capture all children of this line
        else:
            skip_barrier = current_indent # Ignore all children of this line

    return filtered_block

def process_config(config_path: str, output_dir: str) -> None:
    logger.info("--- Loading Config: %s ---", config_path)

    out_path = Path(output_dir)
    if not out_path.exists():
        out_path.mkdir(parents=True, exist_ok=True)

    cfg_path = Path(config_path)
    with cfg_path.open("r", encoding="utf-8") as f:
        jobs = yaml.safe_load(f)

    for job in jobs:
        target_file: str = job.get('file')
        # Sections can now be a list of Strings OR Dictionaries
        sections_def: List[Union[str, Dict]] = job.get('sections', [])
        artifact_filename: str = job.get('artifact')

        full_output_path = out_path / artifact_filename
        logger.info("Processing target: %s", target_file)

        eos_lines = load_file(target_file)
        if not eos_lines:
            continue

        extracted_data: List[str] = []

        for item in sections_def:
            # Determine if this is a simple string or a complex filter dict
            if isinstance(item, str):
                header = item
                filters = []
            elif isinstance(item, dict):
                header = item.get('header')
                filters = item.get('filters', [])
            else:
                logger.warning("Skipping invalid section definition: %s", item)
                continue

            # 1. Extract the full block first
            raw_block = extract_section(eos_lines, header)

            if raw_block:
                # 2. Apply filters if they exist
                if filters:
                    logger.info("  > Filtering block '%s' with %d filters", header, len(filters))
                    final_block = apply_filters(raw_block, filters)
                else:
                    final_block = raw_block

                # 3. Cleanup trailing '!'
                while final_block and final_block[-1].strip() == "!":
                    final_block.pop()

                extracted_data.extend(final_block)
                extracted_data.append("!")
            else:
                logger.warning("  > Section '%s' not found.", header)

        if extracted_data:
            with full_output_path.open("w", encoding="utf-8") as out:
                out.write("\n".join(extracted_data))
            logger.info("  > Saved to %s", full_output_path)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        logger.error("Usage: python3 processor.py <config.yml> <output_dir>")
        sys.exit(1)

    process_config(sys.argv[1], sys.argv[2])
