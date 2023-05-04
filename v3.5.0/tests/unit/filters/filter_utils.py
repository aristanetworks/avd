from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import re
from natsort import os_sorted


def convert_esi_short_to_route_target_format(esi_short):
    if esi_short is None or esi_short == "":
        return None
    esi = esi_short.replace(":", "")
    return ":".join(re.findall('..', esi))


def natural_sort(item_to_natural_sort):
    return os_sorted(item_to_natural_sort)
