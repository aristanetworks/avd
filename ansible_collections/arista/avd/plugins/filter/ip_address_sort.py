# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

from ansible.errors import AnsibleFilterError

from ansible_collections.arista.avd.plugins.plugin_utils.pyavd_wrappers import RaiseOnUse, wrap_filter

PLUGIN_NAME = "arista.avd.ip_address_sort"

try:
    from pyavd.j2filters import ip_address_sort
except ImportError as e:
    ip_address_sort = RaiseOnUse(
        AnsibleFilterError(
            f"The '{PLUGIN_NAME}' plugin requires the 'pyavd' Python library. Got import error",
            orig_exc=e,
        ),
    )

try:
    from ansible.template import accept_args_markers
except ImportError:
    accept_args_markers = None

DOCUMENTATION = r"""
---
name: ip_address_sort
collection: arista.avd
author: Arista Ansible Team (@aristanetworks)
version_added: "6.5.0"
short_description: Sort a list by IP address.
description:
  - Sorts IPv4 and IPv6 addresses, with or without prefix lengths, numerically. IPv4 addresses are sorted before IPv6 addresses.
  - The filter returns an empty list if the input is `None` or `undefined`.
positional: _input
options:
  _input:
    description: List of IPv4 or IPv6 addresses with optional prefix lengths.
    type: list
    elements: any
    required: true
  sort_key:
    description: Key containing the IP address when sorting a list of dictionaries.
    type: string
"""

EXAMPLES = r"""
---
sorted_ipv4_addresses: "{{ ['192.0.2.10/24', '192.0.2.2'] | arista.avd.ip_address_sort }}" # -> ["192.0.2.2", "192.0.2.10/24"]
sorted_ipv6_addresses: "{{ ['2001:db8::10/64', '2001:db8::2'] | arista.avd.ip_address_sort }}" # -> ["2001:db8::2", "2001:db8::10/64"]
sorted_neighbors: >-
  {{
    [{'ip_address': '192.0.2.10'}, {'ip_address': '192.0.2.2'}]
    | arista.avd.ip_address_sort(sort_key='ip_address')
  }}
# -> [{"ip_address": "192.0.2.2"}, {"ip_address": "192.0.2.10"}]
"""

RETURN = r"""
---
_value:
  description: Input values sorted by IP version and numeric address.
  type: list
"""


class FilterModule:
    def filters(self) -> dict:
        wrapped_filter = wrap_filter(PLUGIN_NAME)(ip_address_sort)
        if accept_args_markers is not None:
            wrapped_filter = accept_args_markers(wrapped_filter)
        return {"ip_address_sort": wrapped_filter}
