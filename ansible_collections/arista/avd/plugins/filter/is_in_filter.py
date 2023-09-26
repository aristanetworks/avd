# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
#
# device-filter filter
#
from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
name: is_in_filter
collection: arista.avd
author: Arista Ansible Team (@aristanetworks)
version_added: "1.1"
short_description: Returns V(True) if the input hostname matches the I(hostname_filter).
description:
  - The filter matches if any filter strings are found in the input hostname.
  - I(hostname_filter=["all"]) or I(hostname_filter=none) will match all hostnames.
positional: _input
options:
  _input:
    description: One hostname to match with I(hostname_filter).
    type: string
    required: true
  hostname_filter:
    description:
      - Filter as a list of strings or C(None).
    type: any
    required: true
"""

EXAMPLES = r"""
---
found_all_1: "{{ 'myhostname' | arista.avd.is_in_filter(['all']) }}"
found_all_2: "{{ 'myhostname' | arista.avd.is_in_filter(none) }}"
found_1: "{{ 'myhostname' | arista.avd.is_in_filter(['my']) }}"
found_2: "{{ 'myhostname' | arista.avd.is_in_filter(['hostname']) }}"
not_found_1: "{{ 'myhostname' | arista.avd.is_in_filter(['myhost1', 'MYhostname']) }}"
"""

RETURN = r"""
---
_value:
  description: V(True) if the input hostname matches the I(hostname_filter). Otherwise V(False)
  type: boolean
"""


class FilterModule(object):
    def is_in_filter(self, hostname, hostname_filter):
        if hostname_filter is None:
            hostname_filter = ["all"]
        if "all" in hostname_filter:
            return True
        elif any(element in hostname for element in hostname_filter):
            return True
        return False

    def filters(self):
        return {
            "is_in_filter": self.is_in_filter,
        }
