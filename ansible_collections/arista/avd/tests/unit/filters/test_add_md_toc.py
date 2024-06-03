# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import absolute_import, division, print_function

__metaclass__ = type

import os

import pytest
from ansible.errors import AnsibleFilterError

from ansible_collections.arista.avd.plugins.filter.add_md_toc import add_md_toc

DIR_PATH = os.path.dirname(os.path.realpath(__file__)) + "/toc_files"
MD_INPUTS = [DIR_PATH + "/valid_file.md"]
MD_INPUT_INVALID = DIR_PATH + "/invalid_file.md"
EXPECTED_TOC = DIR_PATH + "/expected_toc.md"
TOC_MARKER = "<!-- toc -->"
SKIP_LINES_LIST = [0, 1, 2]
TOC_LEVELS = [2]
INVALID_TOC_LEVEL = 0


class TestAddMdTocFilter:
    @pytest.mark.parametrize("MD_INPUT", MD_INPUTS)
    @pytest.mark.parametrize("TOC_LEVEL", TOC_LEVELS)
    @pytest.mark.parametrize("SKIP_LINES", SKIP_LINES_LIST)
    def test_add_md_toc(self, MD_INPUT, TOC_LEVEL, SKIP_LINES):
        with open(MD_INPUT, "r", encoding="UTF-8") as input_file:
            resp = add_md_toc(input_file.read(), skip_lines=SKIP_LINES, toc_levels=TOC_LEVEL, toc_marker=TOC_MARKER)

        with open(EXPECTED_TOC, "r", encoding="UTF-8") as input_file:
            expected_toc = input_file.read()

        assert resp.strip() != expected_toc.strip()

    @pytest.mark.parametrize("MD_INPUT", MD_INPUTS)
    def test_add_md_toc_invalid_toc_level(self, MD_INPUT):
        with open(MD_INPUT, "r", encoding="UTF-8") as input_file:
            with pytest.raises(AnsibleFilterError):
                add_md_toc(input_file.read(), toc_levels=INVALID_TOC_LEVEL)

    def test_add_md_toc_invalid(self):
        with open(MD_INPUT_INVALID, "r", encoding="UTF-8") as md_input_toc_invalid:
            with pytest.raises(AnsibleFilterError):
                add_md_toc(md_input_toc_invalid.read())

    def test_add_md_toc_btw_specific_markers(self):
        with open(DIR_PATH + "/markers_at_bottom.md", "r", encoding="UTF-8") as input_file:
            resp = add_md_toc(input_file.read(), skip_lines=0, toc_levels=2, toc_marker=TOC_MARKER)

        with open(DIR_PATH + "/expected_output_toc_at_bottom.md", "r", encoding="UTF-8") as expected_output:
            assert resp == expected_output.read()
