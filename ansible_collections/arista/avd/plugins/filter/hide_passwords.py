#
# arista.avd.hide_passwords filter
#
from __future__ import annotations

__metaclass__ = type

DOCUMENTATION = r"""
  name: hide_passwords
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
ip ospf authentication-key 7 {{ vlan_interface.ospf_authentication_key | arista.avd.hide_passwords(true) }}
"""

RETURN = r"""
  _value:
    description: The original input or '<removed>'
    type: string
"""


def hide_passwords(value: str, hide_passwords: bool = False) -> str:
    return "<removed>" if hide_passwords else value


class FilterModule(object):
    def filters(self):
        return {
            "hide_passwords": hide_passwords,
        }
