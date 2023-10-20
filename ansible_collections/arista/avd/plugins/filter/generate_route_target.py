# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import absolute_import, division, print_function

__metaclass__ = type

import re

DOCUMENTATION = r"""
---
name: generate_route_target
collection: arista.avd
author: Arista Ansible Team (@aristanetworks)
version_added: "1.1"
short_description: Transforms short_esi C(0303:0202:0101) to route-target format C(03:03:02:02:01:01)
description: Removes C(:) and inserts new C(:) for each two characters.
positional: _input
options:
  _input:
    description: Short ESI value as per AVD definition in eos_designs.
    type: string
    required: true
"""

EXAMPLES = r"""
---
rt: "{{ short_esi | arista.avd.generate_route_target }}"
"""

RETURN = r"""
---
_value:
  description: String based on route-target format like 03:03:02:02:01:01
  type: string
"""


def generate_route_target(esi_short):
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
    delimiter = ":"
    esi = esi_short.replace(delimiter, "")
    esi_split = re.findall("..", esi)
    return delimiter.join(esi_split)


class FilterModule(object):
    def filters(self):
        return {
            "generate_route_target": generate_route_target,
        }
