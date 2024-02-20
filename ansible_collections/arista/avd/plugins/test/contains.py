# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
#
# arista.avd.contains
from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible.errors import AnsibleError

try:
    from pyavd.j2tests.contains import contains

    HAS_PYAVD = True
except ImportError:
    HAS_PYAVD = False

DOCUMENTATION = r"""
---
name: contains
collection: arista.avd
author: Arista Ansible Team (@aristanetworks)
version_added: "2.0"
short_description: Test if a list contains one or more of the supplied values.
description:
  - The `arista.avd.contains` test will test if the passed list contains one or more of the supplied test_values.
  - The test accepts either a single test_value or a list of test_values.
positional: _input
options:
  _input:
    description: List of items to test.
    type: list
    required: true
  test_value:
    description: Single item or list of items to test for in value.
    default: None
"""

EXAMPLES = r"""
---
vars:
  mylist: ["test", "test2"]
  item_is_in_my_list: "{{ mylist is arista.avd.contains('test') }}"
  any_item_is_in_my_list: "{{ mylist is arista.avd.contains(['test2', 'test3']) }}"
  platform_settings: "{{ platform_settings | selectattr('platforms', 'arista.avd.contains', switch_platform) }}"
"""

RETURN = r"""
---
_value:
  description:
    - Returns `False` if either the passed value or the test_values are `Undefined` or `none`.
    - Returns `True` if the passed list contains one or more of the supplied test_values. `False` otherwise.
  type: boolean
"""


class TestModule(object):
    def tests(self):
        if not HAS_PYAVD:
            raise AnsibleError("The Python library 'pyavd' cound not be found. Please install using 'pip3 install'")
        return {
            "contains": contains,
        }
