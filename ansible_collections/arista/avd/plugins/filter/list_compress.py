# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
#
# list_compress filter
#
from __future__ import absolute_import, division, print_function

__metaclass__ = type

from itertools import count, groupby

from ansible.errors import AnsibleFilterError

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


def list_compress(list_to_compress):
    if not isinstance(list_to_compress, list):
        raise AnsibleFilterError(f"value must be of type list, got {type(list_to_compress)}")
    G = (list(x) for y, x in groupby(sorted(list_to_compress), lambda x, c=count(): next(c) - x))
    return ",".join("-".join(map(str, (g[0], g[-1])[: len(g)])) for g in G)


class FilterModule(object):
    def filters(self):
        return {
            "list_compress": list_compress,
        }
