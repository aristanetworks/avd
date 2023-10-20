# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
name: generate_esi
collection: arista.avd
author: Arista Ansible Team (@aristanetworks)
version_added: "1.1"
short_description: Transforms short_esi C(0303:0202:0101) to EVPN ESI format C(0000:0000:0303:0202:0101)
description: Concatenates the given I(esi_prefix) and I(short_esi).
positional: _input
options:
  _input:
    description: Short ESI value as per AVD definition in eos_designs.
    type: string
    required: true
  esi_prefix:
    description: ESI prefix value. Will be concatenated with the I(short_esi).
    type: string
    default: "0000:0000:"
"""

EXAMPLES = r"""
---
esi: "{{ short_esi | arista.avd.generate_esi('deaf:beed:') }}"
"""

RETURN = r"""
---
_value:
  description: Concatenated string of I(esi_prefix) and I(short_esi) like C(0000:0000:0303:0202:0101)
  type: string
"""


def generate_esi(esi_short, esi_prefix="0000:0000:"):
    return esi_prefix + esi_short


class FilterModule(object):
    def filters(self):
        return {
            "generate_esi": generate_esi,
        }
