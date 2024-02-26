# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
#
# list_compress filter
#
from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible.errors import AnsibleFilterError

try:
    from pyavd.j2filters.list_compress import list_compress

    HAS_PYAVD = True
except ImportError:
    HAS_PYAVD = False

DOCUMENTATION = r"""
---
name: list_compress
collection: arista.avd
author: Arista Ansible Team (@aristanetworks)
version_added: "1.0"
short_description: Compress a list of integers to a range string.
description:
  - Provides the capability to generate a string representing ranges of VLANs or VNIs.
positional: _input
options:
  _input:
    description: List of integers to compress into a range.
    type: list
    elements: integer
    required: true
"""

EXAMPLES = r"""
---
list1: "{{ [1,2,3,4,5] | arista.avd.list_compress }}" # -> "1-5"
list2: "{{ [1,2,3,7,8] | arista.avd.list_compress }}" # -> "1-3,7-8"
"""

RETURN = r"""
---
_value:
  description: Range string like "1-3,7-8"
  type: string
"""


class FilterModule(object):
    def filters(self):
        if not HAS_PYAVD:
            raise AnsibleFilterError("The Python library 'pyavd' cound not be found. Please install using 'pip3 install'")
        return {
            "list_compress": list_compress,
        }
