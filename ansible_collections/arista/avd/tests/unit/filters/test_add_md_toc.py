from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible_collections.arista.avd.plugins.filter.add_md_toc import add_md_toc
import pytest
import md_toc
import re
import os
from jinja2.runtime import Undefined


DIR_PATH = os.path.dirname(os.path.realpath(
    __file__)) + '/toc_files'
MD_INPUTS = [None, DIR_PATH + '/valid_file.md']
MD_INPUT_INVALID = DIR_PATH + '/invalid_file.md'
EXPECTED_TOC = DIR_PATH + '/expected_toc.md'
TOC_MARKER = '<!-- toc -->'
SKIP_LINES_LIST = [0, 1, 2]
TOC_LEVELS = [1, 2, 3]
INVALID_TOC_LEVEL = 0


class TestAddMdTocFilter():
    @pytest.mark.parametrize("MD_INPUT", MD_INPUTS)
    @pytest.mark.parametrize("TOC_LEVEL", TOC_LEVELS)
    @pytest.mark.parametrize("SKIP_LINES", SKIP_LINES_LIST)
    def test_add_md_toc(self, MD_INPUT, TOC_LEVEL, SKIP_LINES):
        if MD_INPUT is None or isinstance(MD_INPUT, Undefined):
            resp = add_md_toc(MD_INPUT)
            assert resp is None
        else:
            # Extract the TOC from the response
            with open(MD_INPUT, "r") as input_file:
                resp = add_md_toc(input_file.read(
                ), skip_lines=SKIP_LINES, toc_levels=TOC_LEVEL, toc_marker=TOC_MARKER)
            m = re.compile(
                r'(<avd_unit_test_tag_start>)([\S\s]*?)(<avd_unit_test_tag_end>)')
            toc_output = m.search(resp).group(2)

            # Generate TOC for input file
            toc_input = md_toc.build_toc(
                MD_INPUT, list_marker='-', keep_header_levels=TOC_LEVEL, skip_lines=SKIP_LINES)

            assert toc_output.strip() == toc_input.strip()

    @pytest.mark.parametrize("MD_INPUT", MD_INPUTS)
    def test_add_md_toc_invalid_toc_level(self, MD_INPUT):
        if(MD_INPUT is not None):
            with open(MD_INPUT, "r") as input_file:
                with pytest.raises(ValueError):
                    resp = add_md_toc(input_file.read(),
                                      toc_levels=INVALID_TOC_LEVEL)

    def test_add_md_toc_invalid(self):
        md_input_toc_invalid = open(MD_INPUT_INVALID, "r")
        resp = add_md_toc(md_input_toc_invalid.read())

        with open(EXPECTED_TOC, "r") as input_file:
            expected_toc = input_file.read()

        assert resp.strip() != expected_toc.strip()

    def test_add_md_toc_btw_specific_markers(self):
        with open(DIR_PATH + '/markers_at_bottom.md', "r") as input_file:
            resp = add_md_toc(input_file.read(), skip_lines=0,
                              toc_levels=2, toc_marker=TOC_MARKER)

        with open(DIR_PATH + '/expected_output_toc_at_bottom.md', "r") as expected_output:
            assert resp == expected_output.read()
