# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
#
# def arista.avd.add_md_toc
#
from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
name: add_md_toc
collection: arista.avd
author: Arista Ansible Team (@aristanetworks)
version_added: "3.2"
requirements:
  - md_toc
short_description: Parse the input Markdown and add a Table of Contents between the toc_markers.
description:
  - The filter is used in `arista.avd.eos_designs` to create a table of contents for Fabric Documentation.
  - The filter is also used in `arista.avd.eos_cli_config_gen` to create a table of contents for Device Documentation.
positional: _input
options:
  _input:
    description: Markdown to process.
    type: string
    required: true
  skip_lines:
    type: integer
    description: Skip the first x lines when parsing the input Markdown.
    default: 0
  toc_levels:
    type: integer
    description: How many levels of headings will be included in the TOC.
    default: 3
  toc_marker:
    type: string
    description: TOC will be inserted or updated between two of markers in the input Markdown.
    default: "<!-- toc -->"
"""

EXAMPLES = r"""
---
tasks:
- name: Generate fabric documentation
  tags: [build, provision, documentation]
  run_once: true
  delegate_to: localhost
  check_mode: no
  copy:
    content: "{{ lookup('template','documentation/fabric-documentation.j2') | arista.avd.add_md_toc(skip_lines=3) }}"
    dest: "{{ fabric_dir }}/{{ fabric_name }}-documentation.md"
    mode: 0664
"""

RETURN = r"""
---
_value:
  description: Markdown with TOC inserted between the toc_markers.
  type: string
"""

import re
from unicodedata import normalize

from ansible.errors import AnsibleFilterError

HEADING_PATTERN = re.compile(r"#+ ")


def add_md_toc(md_input, skip_lines=0, toc_levels=3, toc_marker="<!-- toc -->"):
    """
    add_md_toc will parse the input MarkDown and add a TOC between the toc_markers

    Example
    -------
    copy:
        content: "{{ lookup('template','eos-device-documentation.j2') | arista.avd.add_md_toc(skip_lines=3) }}"
        dest: "{{ devices_dir }}/{{ inventory_hostname }}.md"
        mode: 0664

    Parameters
    ----------
    md_input: str
        MarkDown which will be processed

    skip_lines: int, optional
        Skip first x lines when parsing MD file
        default: 0

    toc_levels: int, optional
        How many levels of headings will be included in the TOC (Default:3)
        default: 3

    toc_marker: str, optional
        TOC will be inserted or updated between two of these markers in the MD file
        default: '<!-- toc -->'


    Returns
    -------
    str
        MD with added TOC
    """

    if not isinstance(skip_lines, int):
        raise AnsibleFilterError(f"add_md_toc 'skip_lines' argument must be an integer. Got '{skip_lines}'({type(skip_lines)}).")

    if not isinstance(toc_levels, int) or toc_levels < 1:
        raise AnsibleFilterError(f"add_md_toc 'toc_levels' argument must be >0. Got '{toc_levels}'({type(skip_lines)}).")

    if not isinstance(toc_marker, str) or not toc_marker:
        raise AnsibleFilterError(f"add_md_toc 'toc_marker' argument must be a non-empty string. Got '{toc_marker}'({type(skip_lines)}).")

    if not isinstance(md_input, str):
        raise AnsibleFilterError(f"add_md_toc expects a string. Got {type(md_input)}.")

    md_lines = md_input.split("\n")
    toc_marker_positions = []
    toc_lines = []

    # all_anchor_ids is used to hold anchors for the full MD document even if we are skipping lines or levels for the TOC.
    all_anchor_ids = []

    # toc_level_offset ensures we start the TOC at the lowest level within the unskipped lines.
    toc_level_offset = 99

    for line_num, line in enumerate(md_lines):
        if line == toc_marker:
            # Register line number or the TOC marker.
            toc_marker_positions.append(line_num)
            continue
        if re.match(HEADING_PATTERN, line):
            # This is a heading.
            # First get info for this line, including building an anchor and adding this anchor to all_anchor_ids.
            # This is important, since skipped headings will still be associated with an anchor-id during parsing of the final MarkDown file.
            level, text, anchor_id = _get_line_info(line, all_anchor_ids)

            # Do not create a TOC line if we are skipping or at a deeper level than we want.
            if line_num < skip_lines or level > toc_levels:
                continue

            # Create the TOC line
            toc_level_offset = min(toc_level_offset, level)
            prefix = ("  " * (level - toc_level_offset)) + "- "
            toc_lines.append(f"{prefix}[{text}](#{anchor_id})")

    if len(toc_marker_positions) != 2:
        raise AnsibleFilterError(
            f"add_md_toc expects exactly two occurrences of the toc marker '{toc_marker}' on their own lines. Found {len(toc_marker_positions)} occurrences."
        )

    return "\n".join(md_lines[0 : toc_marker_positions[0]] + toc_lines + md_lines[toc_marker_positions[1] + 1 :])


def _get_line_info(line, all_anchor_ids):
    """
    Split heading and return level, text and anchor_id.
    Since we know the line is already a heading, we can assume correct formatting.
    """
    pounds, text = line.split(" ", maxsplit=1)
    level = len(pounds)
    anchor_id = _get_anchor_id(text, all_anchor_ids)

    return level, text, anchor_id


def _get_anchor_id(text, all_anchor_ids):
    """
    Returns a unique anchor_id after adding it to 'all_anchor_ids'.
    The logic here follow the auto-id generation algorithm of the MarkDown spec.
    """
    tmp_anchor_id = normalize("NFKD", text).encode("ascii", "ignore")
    tmp_anchor_id = re.sub(r"[^\w\s-]", "", tmp_anchor_id.decode("ascii")).strip().lower()
    tmp_anchor_id = re.sub(r"[-\s]+", "-", tmp_anchor_id)

    anchor_id = tmp_anchor_id
    counter = 0
    while anchor_id in all_anchor_ids:
        counter += 1
        anchor_id = f"{tmp_anchor_id}-{counter}"
    all_anchor_ids.append(anchor_id)
    return anchor_id


class FilterModule(object):
    def filters(self):
        return {
            "add_md_toc": add_md_toc,
        }
