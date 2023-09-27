# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
#
# def arista.avd.default
#
from __future__ import absolute_import, division, print_function

__metaclass__ = type

from jinja2.runtime import Undefined

DOCUMENTATION = r"""
---
name: default
collection: arista.avd
author: Arista Ansible Team (@aristanetworks)
version_added: "2.0"
short_description: Returns input value if defined and is not none. Otherwise, return default value.
description: |-
  The M(arista.avd.default) filter can provide the same essential capability as the built-in C(default) filter.
  It will return the input value only if it's valid and, if not, provide a default value instead.
  Our custom filter requires a value to be C(not undefined) and C(not None) to pass through.
  Furthermore, the filter allows multiple default values as arguments, which will undergo the same validation until we find a valid default value.
  As a last resort, the filter will return C(None).
positional: _input
options:
  _input:
    description: Default value to check. Will be returned untouched if C(not undefined) and C(not None).
    type: any
    required: true
  default_values:
    type: any
    description: One or more default values will be tested individually, and the first valid value will be used.
"""

EXAMPLES = r"""
---
myvalue: "{{ variable | arista.avd.default(default_value_1, default_value_2) }}"
"""

RETURN = r"""
---
_value:
  description: Input value if C(not undefined) and C(not None). Otherwise, return the first defined default value or C(None).
  type: any
"""


def default(primary_value, *default_values):
    """
    default will test value if defined and is not none.

    Arista.avd.default will test value if defined and is not none. If true
    return value else test default_value1.
    Test of default_value1 if defined and is not none. If true return
    default_value1 else test default_value2.
    If we run out of default values we return none.

    Example
    -------
    priority: {{ spanning_tree_priority | arista.avd.default("32768") }}

    Parameters
    ----------
    primary_value : any
        Ansible default value to look for

    Returns
    -------
    any
        Default value
    """
    if isinstance(primary_value, Undefined) or primary_value is None:
        # Invalid value - try defaults
        if len(default_values) >= 1:
            # Return the result of another loop
            return default(default_values[0], *default_values[1:])
        else:
            # Return None
            return
    else:
        # Return the valid value
        return primary_value


class FilterModule(object):
    def filters(self):
        return {
            "default": default,
        }
