# Copyright (c) 2025-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Unit tests for the config processor."""

import sys
from pathlib import Path
from textwrap import dedent

import pytest

# Logic to find the 'processor.py' file using pathlib
# We need to go up 5 levels from this file to reach the collection root:
# 1. scripts/ -> 2. extensions/ -> 3. unit/ -> 4. tests/ -> 5. avd/
COLLECTION_ROOT = Path(__file__).resolve().parents[4]
SCRIPTS_DIR = COLLECTION_ROOT / "extensions" / "scripts"

# sys.path expects strings, so we convert the Path object
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.append(str(SCRIPTS_DIR))

import processor  # noqa: E402


# --- Helper to cleaner config definitions ---
def config(text: str) -> list[str]:
    """Removes common leading whitespace from every line in `text`, then splits into a list of lines."""
    return dedent(text).strip().splitlines()


@pytest.mark.parametrize(
    ("line", "pattern", "expected"),
    [
        ("vlan 11", "vlan 11", True),
        ("vlan 11 name foo", "vlan 11", True),
        ("vlan 1111", "vlan 11", False),
        ("interface Eth1", "interface Eth1", True),
        ("interface Eth1/1", "interface Eth1", False),
        ("   indent matches", "indent", False),
    ],
)
def test_is_strict_match(line: str, pattern: str, expected: bool) -> None:
    assert processor.is_strict_match(line, pattern) == expected


def test_extract_section() -> None:
    raw_config = config("""
        !
        vlan 10
           name Ten
        !
        vlan 20
           name Twenty
        !
    """)

    result = processor.extract_section(raw_config, "vlan 10")

    # We expect the greedy extraction (including trailing separator)
    expected = config("""
        vlan 10
           name Ten
        !
    """)

    assert result == expected

    result = processor.extract_section(raw_config, "vlan 20")
    expected = config("""
        vlan 20
           name Twenty
        !
    """)
    assert result == expected


def test_apply_filters_basic() -> None:
    block = config("""
        router bgp 65000
           no bgp default ipv4-unicast
           neighbor 1.1.1.1 remote-as 100
           neighbor 2.2.2.2 remote-as 200
    """)

    filters = ["neighbor 1.1.1.1"]
    result = processor.apply_filters(block, filters)

    expected = config("""
        router bgp 65000
           neighbor 1.1.1.1 remote-as 100
    """)
    assert result == expected


def test_apply_filters_nested_blocks() -> None:
    block = config("""
        router bgp 65000
           vrf RED
              rd 1:1
              route-target both 1:1
           vrf BLUE
              rd 2:2
    """)

    filters = ["vrf RED"]
    result = processor.apply_filters(block, filters)

    expected = config("""
        router bgp 65000
           vrf RED
              rd 1:1
              route-target both 1:1
    """)
    assert result == expected


def test_separator_logic() -> None:
    block = config("""
        router bgp 65000
           neighbor 1.1.1.1 remote-as 1
           !
           vrf KEEP_ME
              rd 1:1
           !
           vrf SKIP_ME
              rd 2:2
    """)

    filters = ["vrf KEEP_ME"]
    result = processor.apply_filters(block, filters)

    expected = config("""
        router bgp 65000
           !
           vrf KEEP_ME
              rd 1:1
    """)
    assert result == expected


def test_process_config_integration(tmp_path: Path) -> None:
    config_dir = tmp_path / "inputs"
    config_dir.mkdir()

    eos_file = config_dir / "device.cfg"
    eos_file.write_text(
        dedent("""
        vlan 10
           name Test
        !
        router bgp 65001
           neighbor 1.1.1.1 remote-as 100
           neighbor 2.2.2.2 remote-as 200
        !
    """).strip(),
        encoding="utf-8",
    )

    job_yaml = config_dir / "config.yml"
    job_yaml_content = f"""
    - file: "{eos_file}"
      sections:
        - header: "router bgp 65001"
          filters:
            - "neighbor 1.1.1.1"
      artifact: "result.cfg"
    """
    job_yaml.write_text(dedent(job_yaml_content), encoding="utf-8")

    output_dir = tmp_path / "artifacts"

    processor.process_config(str(job_yaml), str(output_dir))

    result_file = output_dir / "result.cfg"
    assert result_file.exists()

    content = result_file.read_text(encoding="utf-8")

    expected_content = dedent("""
        router bgp 65001
           neighbor 1.1.1.1 remote-as 100
        !
    """).strip()

    assert content.strip() == expected_content


def test_process_config_with_per_artifact_output_dir(tmp_path: Path) -> None:
    """Test that per-artifact output_dir overrides global output_dir."""
    config_dir = tmp_path / "inputs"
    config_dir.mkdir()

    eos_file = config_dir / "device.cfg"
    eos_file.write_text(
        dedent("""
        vlan 10
           name Test
        !
        router bgp 65001
           neighbor 1.1.1.1 remote-as 100
        !
    """).strip(),
        encoding="utf-8",
    )

    # Create two different output directories
    output_dir_1 = tmp_path / "artifacts1"
    output_dir_2 = tmp_path / "artifacts2"

    job_yaml = config_dir / "config.yml"
    job_yaml_content = f"""
    - file: "{eos_file}"
      sections:
        - header: "vlan 10"
      artifact: "vlan.cfg"
      output_dir: "{output_dir_1}"
    - file: "{eos_file}"
      sections:
        - header: "router bgp 65001"
      artifact: "bgp.cfg"
      output_dir: "{output_dir_2}"
    """
    job_yaml.write_text(dedent(job_yaml_content), encoding="utf-8")

    # Process without global output_dir
    processor.process_config(str(job_yaml))

    # Check that artifacts went to their respective directories
    vlan_file = output_dir_1 / "vlan.cfg"
    bgp_file = output_dir_2 / "bgp.cfg"

    assert vlan_file.exists()
    assert bgp_file.exists()

    vlan_content = vlan_file.read_text(encoding="utf-8")
    bgp_content = bgp_file.read_text(encoding="utf-8")

    assert "vlan 10" in vlan_content
    assert "router bgp 65001" in bgp_content


def test_process_config_with_base_path(tmp_path: Path) -> None:
    """Test that base_path is prepended to relative output_dir paths."""
    config_dir = tmp_path / "inputs"
    config_dir.mkdir()

    eos_file = config_dir / "device.cfg"
    eos_file.write_text(
        dedent("""
        vlan 10
           name Test
        !
        router bgp 65001
           neighbor 1.1.1.1 remote-as 100
        !
    """).strip(),
        encoding="utf-8",
    )

    # Create base path directory
    base_dir = tmp_path / "docs" / "howto"

    job_yaml = config_dir / "config.yml"
    job_yaml_content = f"""
    base_path: "{base_dir}"

    artifacts:
      - file: "{eos_file}"
        sections:
          - header: "vlan 10"
        artifact: "vlan.cfg"
        output_dir: "vlans/artifacts/"
      - file: "{eos_file}"
        sections:
          - header: "router bgp 65001"
        artifact: "bgp.cfg"
        output_dir: "bgp/artifacts/"
    """
    job_yaml.write_text(dedent(job_yaml_content), encoding="utf-8")

    # Process without global output_dir
    processor.process_config(str(job_yaml))

    # Check that artifacts went to base_path + output_dir
    vlan_file = base_dir / "vlans" / "artifacts" / "vlan.cfg"
    bgp_file = base_dir / "bgp" / "artifacts" / "bgp.cfg"

    assert vlan_file.exists(), f"Expected {vlan_file} to exist"
    assert bgp_file.exists(), f"Expected {bgp_file} to exist"

    vlan_content = vlan_file.read_text(encoding="utf-8")
    bgp_content = bgp_file.read_text(encoding="utf-8")

    assert "vlan 10" in vlan_content
    assert "router bgp 65001" in bgp_content
