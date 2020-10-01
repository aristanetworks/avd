from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from jinja2 import TemplateError
from ansible.errors import AnsibleFilterError
import re


class FilterModule(object):

    def generate_esi(self, esi_short, esi_prefix='0000:0000:'):
        return esi_prefix + esi_short

    def generate_lacp_id(self, esi_short):
        return esi_short.replace(':', '.')

    def generate_route_target(self, esi_short):
        """
        generate_route_target Transform 3 octets ESI like 0303:0202:0101 to route-target

        Parameters
        ----------
        esi : str
            Short ESI value as per AVD definition in eos_l3ls_evpn

        Returns
        -------
        str
            String based on route-target format like 03:03:02:02:01:01
        """
        delimiter = ':'
        esi = esi_short.replace(delimiter, "")
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
            'generate_route_target': self.generate_route_target,
            'generate_lacp_id': self.generate_lacp_id,
            'generate_esi': self.generate_esi,
        }
