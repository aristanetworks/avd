# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import absolute_import, division, print_function

__metaclass__ = type

import pytest
from pyavd.j2filters.status_render import status_render

STATE_STRINGS = [("PASS", "github", ":white_check_mark:"), ("FAIL", "test", "FAIL")]


class TestMarkdownRenderingFilter:
    @pytest.mark.parametrize("state_string, rendering, markdown_code", STATE_STRINGS)
    def test_status_render_valid(self, state_string, rendering, markdown_code):
        resp = status_render(state_string, rendering)
        assert resp == markdown_code
