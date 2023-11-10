# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
#
# def arista.avd.add_md_toc
#
from __future__ import absolute_import, division, print_function

__metaclass__ = type

import re
import sys
from io import StringIO

from jinja2.runtime import Undefined

try:
    import md_toc

    HAS_MD_TOC = True
except ImportError:
    HAS_MD_TOC = False

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
  - The filter is used in M(arista.avd.eos_designs) to create a table of contents for Fabric Documentation.
  - The filter is also used in M(arista.avd.eos_cli_config_gen) to create a table of contents for Device Documentation.
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

    if isinstance(md_input, Undefined) or md_input is None or HAS_MD_TOC is False:
        # Return None
        return

    # Generate TOC from variable
    with StringIO(md_input) as md:
        stdin = sys.stdin
        sys.stdin = md
        toc = md_toc.build_toc("-", keep_header_levels=toc_levels, skip_lines=skip_lines).rstrip()
        sys.stdin = stdin

    # Insert TOC between markers
    toc_marker = re.escape(toc_marker)
    toc_pattern = re.compile(rf"{toc_marker}[\S\s]*?{toc_marker}")

    return toc_pattern.sub(toc, md_input, count=1)


class FilterModule(object):
    def filters(self):
        return {
            "add_md_toc": add_md_toc,
        }
