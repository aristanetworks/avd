# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = r"""
---
name: status_render
collection: arista.avd
author: Arista Ansible Team (@aristanetworks)
version_added: "1.1.1"
short_description: Convert Text to EMOJI code.
description:
  - Returns the input value unless I(rendering) is set to "github".
  - Returns C(:x:) if input status string is C(FAIL) and I(rendering) is set to "github".
  - Returns C(:white_check_mark:) if input status string is C(PASS) and I(rendering) is set to "github".
positional: _input
options:
  _input:
    description: Text to convert to EMOJI.
    type: string
    required: true
  rendering:
    description: Markdown Flavor to use for Emoji rendering. Only "github" is supported.
    type: string
    required: true
"""

RETURN = r"""
---
_value:
  description: Input value or GitHub Markdown emoji code.
  type: string
"""


class FilterModule(object):
    # STATIC EMOJI CODE
    GH_CODE = {}
    # Github MD code for Emoji checked box
    GH_CODE["PASS"] = ":white_check_mark:"
    # GH MD code for Emoji Fail
    GH_CODE["FAIL"] = ":x:"

    def status_render(self, state_string, rendering):
        """
        status_render Convert Text to EMOJI code

        Parameters
        ----------
        state_string : str
            Text to convert in EMOJI
        rendering : string
            Markdown Flavor to use for Emoji rendering.

        Returns
        -------
        str
            Value to render in markdown
        """
        if rendering == "github":
            return self.GH_CODE[state_string.upper()]
        else:
            return state_string

    def filters(self):
        return {"status_render": self.status_render}
