# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible.errors import AnsibleFilterError

try:
    from pyavd.j2filters.generate_lacp_id import generate_lacp_id

    HAS_PYAVD = True
except ImportError:
    HAS_PYAVD = False

DOCUMENTATION = r"""
---
name: generate_lacp_id
collection: arista.avd
author: Arista Ansible Team (@aristanetworks)
version_added: "1.1"
short_description: Transforms short_esi `0303:0202:0101` to LACP ID format `0303.0202.0101`
description: Replaces `:` with `.`
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


class FilterModule(object):
    def filters(self):
        if not HAS_PYAVD:
            raise AnsibleFilterError("The Python library 'pyavd' cound not be found. Please install using 'pip3 install'")
        return {
            "generate_lacp_id": generate_lacp_id,
        }
