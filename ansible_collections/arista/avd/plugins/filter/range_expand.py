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


def expand_parentheses(range_sr, one_range):
    groups = range_sr.groups()
    start_index, end_index = range_sr.start(), range_sr.end()
    replaced_list = []
    if groups[0]:
        # To replace the values inside parenthesis, Ex. (2,3,4-6)
        ports_list = groups[0].replace("(", "").replace(")", "").split(",")
        for i in ports_list:
            replaced_list.append(one_range.replace(one_range[start_index:end_index], str(i), 1))
    return replaced_list


def expand_hypen(range_sr, one_range):
    groups = range_sr.groups()
    start_index, end_index = range_sr.start(), range_sr.end()
    replaced_list = []
    if groups[0]:
        # To replace the values of range, Ex. 4-6
        range_start, range_end = groups[0].split("-")
        for i in range(int(range_start), int(range_end) + 1):
            replaced_list.append(one_range.replace(one_range[start_index:end_index], str(i), 1))
    return replaced_list


def range_expand(one_range, prefix=""):
    if not (isinstance(one_range, list) or isinstance(one_range, str)):
        raise AnsibleFilterError(f"value must be of type list or str, got {type(one_range)}")

    result = []

    # If we got a list, unpack it and run this function recursively
    if isinstance(one_range, list):
        for r in one_range:
            result.extend(range_expand(r, prefix))

    else:
        # Must be a str now
        if one_range is None:
            return

        regex = r"([A-Za-z]+\s*)?(.*)"
        sr = re.search(regex, one_range)

        prefix_group = sr.groups()
        if prefix_group[0]:
            prefix = prefix_group[0]
        else:
            one_range = prefix + one_range

        if re.search(r",(?![^(]*\))", one_range):
            # Split comma outside parentheses
            result.extend(range_expand(re.split(r",(?![^(]*\))", one_range), prefix))
        elif parentheses_sr := re.search(r"(\(\s*(?:\d+)(?:(?:\s*,\s*\d+)*(?:,?(?:\d+)?\-\d+)*)*\s*\))", one_range):
            # Expand parentheses
            result.extend(range_expand(expand_parentheses(parentheses_sr, one_range), prefix))
        elif hypen_sr := re.search(r"([0-9]+\-[0-9]+)", one_range):
            # Expand hypen
            result.extend(range_expand(expand_hypen(hypen_sr, one_range), prefix))
        else:
            if one_range:
                result.extend([one_range])
            else:
                result.extend(one_range)
    return result


class FilterModule(object):
    def filters(self):
        return {
            "range_expand": range_expand,
        }
