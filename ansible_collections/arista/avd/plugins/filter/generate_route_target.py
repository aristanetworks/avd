# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible.errors import AnsibleFilterError

from ansible_collections.arista.avd.plugins.plugin_utils.pyavd_wrappers import RaiseOnUse, wrap_filter

PLUGIN_NAME = "arista.avd.generate_route_target"

try:
    from pyavd.j2filters import generate_route_target
except ImportError as e:
    generate_route_target = RaiseOnUse(
        AnsibleFilterError(
            f"The '{PLUGIN_NAME}' plugin requires the 'pyavd' Python library. Got import error",
            orig_exc=e,
        )
    )

DOCUMENTATION = r"""
---
name: generate_route_target
collection: arista.avd
author: Arista Ansible Team (@aristanetworks)
version_added: "1.1"
short_description: Transforms short_esi `0303:0202:0101` to route-target format `03:03:02:02:01:01`
description: Removes `:` and inserts new `:` for each two characters.
positional: _input
options:
  _input:
    description: Short ESI value as per AVD definition in eos_designs.
    type: string
    required: true
"""

EXAMPLES = r"""
---
rt: "{{ short_esi | arista.avd.generate_route_target }}"
"""

RETURN = r"""
---
_value:
  description: String based on route-target format like 03:03:02:02:01:01
  type: string
"""


class FilterModule(object):
    def filters(self):
        return {
            "generate_route_target": wrap_filter(PLUGIN_NAME)(generate_route_target),
        }
