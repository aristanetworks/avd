from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

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
            Short ESI value as per AVD definition in eos_designs

        Returns
        -------
        str
            String based on route-target format like 03:03:02:02:01:01
        """
        if esi_short is None:
            return None
        delimiter = ':'
        esi = esi_short.replace(delimiter, "")
        esi_split = re.findall('..', esi)
        return delimiter.join(esi_split)

    def filters(self):
        return {
            'generate_route_target': self.generate_route_target,
            'generate_lacp_id': self.generate_lacp_id,
            'generate_esi': self.generate_esi,
        }
