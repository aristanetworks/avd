# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
name: generate_lacp_id
collection: arista.avd
author: Arista Ansible Team (@aristanetworks)
version_added: "1.1"
short_description: Transforms short_esi C(0303:0202:0101) to LACP ID format C(0303.0202.0101)
description: Replaces C(:) with C(.)
positional: _input
options:
  _input:
    description: Short ESI value as per AVD definition in eos_designs.
    type: string
    required: true
"""

EXAMPLES = r"""
---
lacp_id: "{{ short_esi | arista.avd.generate_lacp_id }}"
"""

RETURN = r"""
---
_value:
  description: String based on LACP ID format like 0303.0202.0101
  type: string
"""


def generate_lacp_id(esi_short):
    return esi_short.replace(":", ".")


class FilterModule(object):
    def filters(self):
        return {
            "generate_lacp_id": generate_lacp_id,
        }
