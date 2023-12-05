# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
#
# range_expand filter
#
from __future__ import absolute_import, division, print_function

__metaclass__ = type

import re

from ansible.errors import AnsibleFilterError

DOCUMENTATION = r"""
---
name: range_expand
collection: arista.avd
author: Arista Ansible Team (@aristanetworks)
version_added: "3.4.0"
short_description: Expand a range of interfaces or list of ranges and return as a list of strings.
description:
  - Provides the capabilities to expand a range of interfaces or list of ranges and return as a list of strings.
  - The filter supports VLANs, interfaces, modules, sub-interfaces, and ranges are expanded at all levels.
  - Within a single range, prefixes (ex. Ethernet, Eth, Po) are carried over to items without prefixes (see examples).
positional: _input
options:
  _input:
    description: Range as string or list of ranges.
    type: any
    required: true
"""

EXAMPLES = r"""
---
- "{{ 'Ethernet1' | range_expand }}"
# -> ["Ethernet1"]

- "{{ 'Ethernet1-2' | range_expand }}"
# -> ["Ethernet1", "Ethernet2"]

- "{{ 'Eth 3-5,7-8' | range_expand }}"
# -> ["Eth 3", "Eth 4", "Eth 5", "Eth 7", "Eth 8"]

- "{{ 'et2-6,po1-2' | range_expand }}"
# -> ["et2", "et3", "et4", "et5", "et6", "po1", "po2"]

- "{{ ['Ethernet1'] | range_expand }}"
# -> ["Ethernet1"]

- "{{ ['Ethernet 1-2', 'Eth3-5', '7-8'] | range_expand }}"
# -> ["Ethernet 1", "Ethernet 2", "Eth3", "Eth4", "Eth5", "7", "8"]

- "{{ ['Ethernet2-6', 'Port-channel1-2'] | range_expand }}"
# -> ["Ethernet2", "Ethernet3", "Ethernet4", "Ethernet5", "Ethernet6", "Port-channel1", "Port-channel2"]

- "{{ ['Ethernet1/1-2', 'Eth1-2/3-5,5/1-2'] | range_expand }}"
# -> ["Ethernet1/1", "Ethernet1/2", "Eth1/3", "Eth1/4", "Eth1/5", "Eth2/3", "Eth2/4", "Eth2/5", "Eth5/1", "Eth5/2"]

- "{{ ['Eth1.1,9-10.1', 'Eth2.2-3', 'Eth3/1-2.3-4'] | range_expand }}"
# -> ["Eth1.1", "Eth9.1", "Eth10.1", "Eth2.2", "Eth2.3", "Eth3/1.3", "Eth3/1.4", "Eth3/2.3", "Eth3/2.4"]

- "{{ '1-3' | range_expand }}"
# -> ["1", "2", "3"]

- "{{ ['1', '2', '3'] | range_expand }}"
# -> ["1", "2", "3"]

- "{{ 'vlan1-3' | range_expand }}"
# -> ["vlan1", "vlan2", "vlan3"]

- "{{ 'Et1-2/3-4/5-6' | range_expand }}"
# -> ["Et1/3/5", "Et1/3/6", "Et1/4/5", "Et1/4/6", "Et2/3/5", "Et2/3/6", "Et2/4/5", "Et2/4/6"]
"""

RETURN = r"""
---
_value:
  description: List of strings from all ranges.
  type: list
  elements: string
"""


def range_expand(range_to_expand):
    if not (isinstance(range_to_expand, list) or isinstance(range_to_expand, str)):
        raise AnsibleFilterError(f"value must be of type list or str, got {type(range_to_expand)}")

    result = []

    # If we got a list, unpack it and run this function recursively
    if isinstance(range_to_expand, list):
        for r in range_to_expand:
            result.extend(range_expand(r))

    # Must be a str now
    else:
        prefix = ""

        # Unpack list in string
        for one_range in range_to_expand.split(","):
            if one_range is None:
                continue

            # Find prefix (if any)
            regex = r"^(.*?)(((\d+)-)?(\d+)\/)?(((\d+)-)?(\d+)\/)?(((\d+)-)?(\d+))(\.((\d+)-)?(\d+))?"
            # Number of groups in this regex.
            regex_groups = 17
            # Groups one-by-one:
            # Group 1  (.*?)                                                                           matches prefix ex. Ethernet, Eth, Po, Port-Channel
            # Group 2       (((\d+)-)?(\d+)\/)?                                                        matches module(s) and slash ex. 12/, 1-3/
            # Group 3        ((\d+)-)?                                                                 matches first module and dash ex. 1-
            # Group 4         (\d+)                                                                    matches first module ex. 1
            # Group 5                 (\d+)                                                            matches last module ex. 12, 3
            # Group 6                          (((\d+)-)?(\d+)\/)?                                     matches parent interface(s) and slash ex. 47/, 1-48/
            # Group 7                           ((\d+)-)?                                              matches parent interface(s) and dash ex. 47-
            # Group 8                            (\d+)                                                 matches first parent interface ex. 1
            # Group 9                                    (\d+)                                         matches last parent interface ex. 47, 48
            # Group 10                                            (((\d+)-)?(\d+))                     matches (breakout) interface(s) ex. 1, 1-4, 1-48
            # Group 11                                             ((\d+)-)?                           matches first interfaces and dash ex. 1-, 1-
            # Group 12                                              (\d+)                              matches first interface
            # Group 13                                                      (\d+)                      matches last interface ex. 1, 4, 48
            # Group 14                                                            (\.((\d+)-)?(\d+))?  matches dot and sub-interface(s) ex. .141, .12-15
            # Group 15                                                               ((\d+)-)?         matches first sub-interface and dash ex. 12-
            # Group 16                                                                (\d+)            matches first sub-interface ex. 12
            # Group 17                                                                        (\d+)    matches last sub-interface ex. 141, 15
            # Remember that the groups() object is 0-based and the group numbers above are 1-based
            search_result = re.search(regex, one_range)
            if search_result:
                if len(search_result.groups()) == regex_groups:
                    groups = search_result.groups()
                    first_module = last_module = None
                    first_parent_interface = last_parent_interface = None
                    first_interface = last_interface = None
                    first_subinterface = last_subinterface = None
                    # Set prefix if found (otherwise use last set prefix)
                    if groups[0]:
                        prefix = groups[0]
                    if groups[4]:
                        last_module = int(groups[4])
                    if groups[3]:
                        first_module = int(groups[3])
                    else:
                        first_module = last_module
                    if groups[8]:
                        last_parent_interface = int(groups[8])
                    if groups[7]:
                        first_parent_interface = int(groups[7])
                    else:
                        first_parent_interface = last_parent_interface
                    if groups[12]:
                        last_interface = int(groups[12])
                    if groups[11]:
                        first_interface = int(groups[11])
                    else:
                        first_interface = last_interface
                    if groups[16]:
                        last_subinterface = int(groups[16])
                    if groups[15]:
                        first_subinterface = int(groups[15])
                    else:
                        first_subinterface = last_subinterface

                    def expand_subinterfaces(interface_string):
                        result = []
                        if last_subinterface is not None:
                            if first_subinterface > last_subinterface:
                                raise AnsibleFilterError(
                                    f"Range {one_range} could not be expanded because the first subinterface {first_subinterface} is larger than last"
                                    f" subinterface {last_subinterface} in the range."
                                )
                            for subinterface in range(first_subinterface, last_subinterface + 1):
                                result.append(f"{interface_string}.{subinterface}")
                        else:
                            result.append(interface_string)
                        return result

                    def expand_interfaces(interface_string):
                        result = []
                        if first_interface > last_interface:
                            raise AnsibleFilterError(
                                f"Range {one_range} could not be expanded because the first interface {first_interface} is larger than last interface"
                                f" {last_interface} in the range."
                            )
                        for interface in range(first_interface, last_interface + 1):
                            for res in expand_subinterfaces(f"{interface_string}{interface}"):
                                result.append(res)
                        return result

                    def expand_parent_interfaces(interface_string):
                        result = []
                        if last_parent_interface:
                            if first_parent_interface > last_parent_interface:
                                raise AnsibleFilterError(
                                    f"Range {one_range} could not be expanded because the first interface {first_parent_interface} is larger than last"
                                    f" interface {last_parent_interface} in the range."
                                )
                            for parent_interface in range(first_parent_interface, last_parent_interface + 1):
                                for res in expand_interfaces(f"{interface_string}{parent_interface}/"):
                                    result.append(res)
                        else:
                            for res in expand_interfaces(f"{interface_string}"):
                                result.append(res)
                        return result

                    def expand_module(interface_string):
                        result = []
                        if last_module:
                            if first_module > last_module:
                                raise AnsibleFilterError(
                                    f"Range {one_range} could not be expanded because the first module {first_module} is larger than last module"
                                    f" {last_module} in the range."
                                )
                            for module in range(first_module, last_module + 1):
                                for res in expand_parent_interfaces(f"{interface_string}{module}/"):
                                    result.append(res)
                        else:
                            for res in expand_parent_interfaces(f"{interface_string}"):
                                result.append(res)
                        return result

                    result.extend(expand_module(prefix))

                else:
                    raise AnsibleFilterError(f"Invalid range, got {one_range} and found {search_result.groups()}")

    return result


class FilterModule(object):
    def filters(self):
        return {
            "range_expand": range_expand,
        }
