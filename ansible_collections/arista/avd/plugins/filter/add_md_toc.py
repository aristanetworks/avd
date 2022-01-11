#
# def arista.avd.add_md_toc
#
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from jinja2.runtime import Undefined
from io import StringIO
import sys
import re
try:
    import md_toc
    HAS_MD_TOC = True
except ImportError:
    HAS_MD_TOC = False


def add_md_toc(md_input, skip_lines=0, toc_levels=2, toc_marker='<!-- toc -->'):
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
        How many levels of headings will be included in the TOC (Default:2)
        default: 2

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
        toc = md_toc.build_toc('-', keep_header_levels=toc_levels, skip_lines=skip_lines)
        sys.stdin = stdin

    # Insert TOC between markers
    toc_marker = re.escape(toc_marker)
    toc_pattern = re.compile(fr"{toc_marker}[\S\s]*?{toc_marker}")

    return toc_pattern.sub(toc, md_input, count=1)


class FilterModule(object):
    def filters(self):
        return {
            'add_md_toc': add_md_toc,
        }
