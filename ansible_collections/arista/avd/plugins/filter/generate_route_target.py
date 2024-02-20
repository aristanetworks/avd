# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible.errors import AnsibleFilterError

try:
    from pyavd.j2filters.generate_route_target import generate_route_target

    HAS_PYAVD = True
except ImportError:
    HAS_PYAVD = False

DOCUMENTATION = r"""
---
name: generate_route_target
collection: arista.avd
author: Arista Ansible Team (@aristanetworks)
version_added: "1.1"
short_description: Transforms short_esi `0303:0202:0101` to route-target format `03:03:02:02:01:01`
description: Removes `:` and inserts new `:` for each two characters.
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


class FilterModule(object):
    def filters(self):
        if not HAS_PYAVD:
            raise AnsibleFilterError("The Python library 'pyavd' cound not be found. Please install using 'pip3 install'")
        return {
            "generate_route_target": generate_route_target,
        }
