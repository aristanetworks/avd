# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
#
# arista.avd.hide_passwords filter
#
__metaclass__ = type

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError

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


def hide_passwords(value: str, hide_passwords: bool = False) -> str:
    if not isinstance(hide_passwords, bool):
        raise AristaAvdError(f"{hide_passwords} in hide_passwords filter is not of type bool")
    return "<removed>" if hide_passwords else value


class FilterModule(object):
    def filters(self):
        return {
            "hide_passwords": hide_passwords,
        }
