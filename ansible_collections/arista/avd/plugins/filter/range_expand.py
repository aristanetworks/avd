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

from ansible_collections.arista.avd.plugins.plugin_utils.utils.range_expand import expand_hyphen, expand_parentheses


def range_expand(range_to_expand, prefix=""):
    if not (isinstance(range_to_expand, list) or isinstance(range_to_expand, str)):
        raise AnsibleFilterError(f"value must be of type list or str, got {type(range_to_expand)}")

    result = []

    # If we got a list, unpack it and run this function recursively
    if isinstance(range_to_expand, list):
        for one_range in range_to_expand:
            result.extend(range_expand(one_range, prefix))

    else:
        # Must be a str now
        if range_to_expand is None:
            return

        regex = r"([A-Za-z]+\s*)?(.*)"
        sr = re.search(regex, range_to_expand)

        prefix_group = sr.groups()
        if prefix_group[0]:
            prefix = prefix_group[0]
        else:
            range_to_expand = prefix + range_to_expand

        regex_commas_outside_parentheses = r",(?![^(]*\))"
        # Above regex matches all the commas "," outside parentheses.
        # Except the case where there is no opening parentheses but closing parentheses is present [Example: ",4)"]
        # It considers the comma inside the parentheses whereas it is actually outside.

        regex_commas_inside_parentheses = r"(\(\s*(?:\d+)(?:(?:\s*,\s*\d+)*(?:,?(?:\d+)?\-\d+)*)*\s*\))"
        #                           (\( \))                                                              matches starting and ending of parentheses
        #                           ?:                                                                   only group but do not remember the grouped part
        #                                         (?:\d+)                                                matches 1 or more numbers Ex. 1, 21
        #                                                   (?:\s*,\s*\d+)*                              matches 0 or more apperance of "," and one
        #                                                                                                             or more numbers Ex. ,2,23
        #                                                                  (?:,?\d+\-\d+)*               matches 0 or more apperance of "," and one or more
        #                                                                                                             numbers with range (-) Ex. ,2-4
        #                                         (?:\d+)(?:(?:\s*,\s*\d+)*(?:,?\d+\-\d+)*)*             matches values similar to 1 or 1,2,3 or 1,2-4
        #                                   (\(\s*(?:\d+)(?:(?:\s*,\s*\d+)*(?:,?\d+\-\d+)*)*\s*\))       matches values similar to 1 or 1,2,3 or 1,2-4

        regex_hyphen_range = r"([0-9]+\-[0-9]+)"
        #                      ([0-9]+\-[0-9]+)                                                          matches range outside parentheses Ex. 1-5 or 33-46

        if re.search(regex_commas_outside_parentheses, range_to_expand):
            # Split comma outside parentheses
            result.extend(range_expand(re.split(regex_commas_outside_parentheses, range_to_expand), prefix))
        elif parentheses_sr := re.search(regex_commas_inside_parentheses, range_to_expand):
            # Expand parentheses
            result.extend(range_expand(expand_parentheses(parentheses_sr, range_to_expand), prefix))
        elif hyphen_sr := re.search(regex_hyphen_range, range_to_expand):
            # Expand hyphen
            result.extend(range_expand(expand_hyphen(hyphen_sr, range_to_expand), prefix))
        else:
            if range_to_expand:
                result.extend([range_to_expand])
    return result


class FilterModule(object):
    def filters(self):
        return {
            "range_expand": range_expand,
        }
