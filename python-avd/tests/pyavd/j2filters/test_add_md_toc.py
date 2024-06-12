# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import absolute_import, division, print_function

__metaclass__ = type

from pathlib import Path

import pytest
from pyavd.j2filters.add_md_toc import add_md_toc

DIR_PATH = Path(__file__).parent / "toc_files"
MD_INPUTS = [DIR_PATH / "valid_file.md"]
MD_INPUT_INVALID = DIR_PATH / "invalid_file.md"
EXPECTED_TOC = DIR_PATH / "expected_toc.md"
TOC_MARKER = "<!-- toc -->"
SKIP_LINES_LIST = [0, 1, 2]
TOC_LEVELS = [2]
INVALID_TOC_LEVEL = 0


class TestAddMdTocFilter:
    """Class to test add_md_toc filter."""

    @pytest.mark.parametrize("md_input", MD_INPUTS)
    @pytest.mark.parametrize("toc_level", TOC_LEVELS)
    @pytest.mark.parametrize("skip_lines", SKIP_LINES_LIST)
    def test_add_md_toc(self, md_input, toc_level, skip_lines):
        """Test add_md_toc success scenarii."""
        with open(md_input, "r", encoding="UTF-8") as input_file:
            resp = add_md_toc(input_file.read(), skip_lines=skip_lines, toc_levels=toc_level, toc_marker=TOC_MARKER)

        with open(EXPECTED_TOC, "r", encoding="UTF-8") as input_file:
            expected_toc = input_file.read()

        assert resp.strip() != expected_toc.strip()

    @pytest.mark.parametrize("md_input", MD_INPUTS)
    def test_add_md_toc_invalid_toc_level(self, md_input):
        """Test add_md_toc with invalid toc level."""
        with open(md_input, "r", encoding="UTF-8") as input_file:
            with pytest.raises(TypeError):
                add_md_toc(input_file.read(), toc_levels=INVALID_TOC_LEVEL)

    def test_add_md_toc_invalid(self):
        """Test add_md_toc with invalid input file."""
        with open(MD_INPUT_INVALID, "r", encoding="UTF-8") as md_input_toc_invalid:
            with pytest.raises(ValueError, match="add_md_toc expects exactly two occurrences of the toc marker"):
                add_md_toc(md_input_toc_invalid.read())

    def test_add_md_toc_btw_specific_markers(self):
        with open(DIR_PATH / "markers_at_bottom.md", "r", encoding="UTF-8") as input_file:
            resp = add_md_toc(input_file.read(), skip_lines=0, toc_levels=2, toc_marker=TOC_MARKER)

        with open(DIR_PATH / "expected_output_toc_at_bottom.md", "r", encoding="UTF-8") as expected_output:
            assert resp == expected_output.read()
