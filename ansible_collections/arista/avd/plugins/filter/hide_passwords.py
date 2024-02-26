# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
#
# arista.avd.hide_passwords filter
#
from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible.errors import AnsibleFilterError

try:
    from pyavd.j2filters.hide_passwords import hide_passwords

    HAS_PYAVD = True
except ImportError:
    HAS_PYAVD = False

DOCUMENTATION = r"""
name: hide_passwords
collection: arista.avd
author: Arista Ansible Team (@aristanetworks)
version_added: "4.0.0"
short_description: Replace a value by "<removed>"
description:
  - Replace the input data by "<removed>" if the hide_passwords parameter is true
positional: _input
options:
  _input:
    description: Value to replace.
    type: raw
    required: true
  hide_passwords:
    description: Flag to indicate whether or not the string should be replaced.
    type: bool
    required: true
"""

EXAMPLES = r"""
cli_with_hidden_password: "ip ospf authentication-key 7 {{ vlan_interface.ospf_authentication_key | arista.avd.hide_passwords(true) }}"
"""

RETURN = r"""
---
_value:
  description: The original input or '<removed>'
  type: string
"""


class FilterModule(object):
    def filters(self):
        if not HAS_PYAVD:
            raise AnsibleFilterError("The Python library 'pyavd' cound not be found. Please install using 'pip3 install'")
        return {
            "hide_passwords": hide_passwords,
        }
