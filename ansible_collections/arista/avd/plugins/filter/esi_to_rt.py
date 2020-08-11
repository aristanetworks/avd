from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from jinja2 import TemplateError
from ansible.errors import AnsibleFilterError
import re


class FilterModule(object):

    def esi_to_rt(self, esi):
        delimiter = ':'
        if ":" in esi:
            esi = esi.replace(delimiter, "")
        esi_split = re.findall('..', esi)
        rt = ""
        loop_cpt = 0
        for esi_section in esi_split:
            loop_cpt += 1
            rt = rt + str(esi_section)
            if loop_cpt < len(esi_split):
                rt = rt + str(delimiter)
        return rt

    def filters(self):
        return {
            'esi_to_rt': self.esi_to_rt,
        }
