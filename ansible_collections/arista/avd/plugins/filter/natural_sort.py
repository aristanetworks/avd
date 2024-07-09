# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
#
# natural_sort filter
#
from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible.errors import AnsibleFilterError

from ansible_collections.arista.avd.plugins.plugin_utils.pyavd_wrappers import RaiseOnUse, wrap_filter

PLUGIN_NAME = "arista.avd.natural_sort"

try:
    from pyavd.j2filters import natural_sort
except ImportError as e:
    natural_sort = RaiseOnUse(
        AnsibleFilterError(
            f"The '{PLUGIN_NAME}' plugin requires the 'pyavd' Python library. Got import error",
            orig_exc=e,
        )
    )

DOCUMENTATION = r"""
---
name: natural_sort
collection: arista.avd
author: Arista Ansible Team (@aristanetworks)
version_added: "1.0.0"
short_description: Sort an input list with natural sorting.
description:
  - |-
      Provides the capability to sort a list or a dictionary of integers and strings that contain alphanumeric characters naturally.
      When leveraged on a dictionary, only the key value will be returned.
      An optional `sort_key` can be specified, to sort on content of certain key if the items are dictionaries.
  - The filter will return an empty list if the value parsed to `arista.avd.natural_sort` is `None` or `undefined`.
positional: _input
options:
  _input:
    description: List or dictionary
    type: any
    required: true
  sort_key:
    description: Key to sort on when sorting a list of dictionaries
    type: string
    version_added: "3.0.0"
"""

EXAMPLES = r"""
---
sorted_list: "{{ ['test19', 'test9'] | natural_sort }}" # -> ["test9", "test19"]
sorted_keys: "{{ {'test19': 'value', 'test9': 'value'} | natural_sort }}" # -> ["test9", "test19"]
sorted_on_name_key: "{{ [{'name': 'test19'}, {'name': 'test9'}] | natural_sort('name') }}" # -> [{"name": "test9"}, {"name": "test19"}]
empty_list_1: "{{ none | natural_sort }}" # -> []
empty_list_2: "{{ some_undefined_var | natural_sort }}" # -> []
"""

RETURN = r"""
---
_value:
  description: Sorted list if the input was a list. Sorted keys if the input was a dictionary. Empty list if the input value was `None` or `undefined`.
  type: list
"""


class FilterModule(object):
    def filters(self):
        return {
            "natural_sort": wrap_filter(PLUGIN_NAME)(natural_sort),
        }
