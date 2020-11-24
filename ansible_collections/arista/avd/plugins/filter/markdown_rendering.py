from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from jinja2 import TemplateError
from ansible.errors import AnsibleFilterError
import re


class FilterModule(object):
    # STATIC EMOJI CODE
    GH_CODE = dict()
    # Github MD code for Emoji checked box
    GH_CODE['PASS'] = ':white_check_mark:'
    # GH MD code for Emoji Fail
    GH_CODE['FAIL'] = ':x:'

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
        if rendering == 'github':
            return self.GH_CODE[state_string.upper()]
        else:
            return state_string

    def filters(self):
        return {
            'status_render': self.status_render
        }
