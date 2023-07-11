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


def extend_range(one_range):
    regex = r"(\(\s*(?:\d*)(?:(?:\s*,\s*\d+)*(?:\s*,?\s*\d+\-\d+)*)*\s*\))|([0-9]+\-[0-9]+)"
    range_sr = re.search(regex, one_range)
    groups = range_sr.groups()
    start_index, end_index = range_sr.start(), range_sr.end()
    replaced_list = []
    if groups[0]:
        # To replace the values inside parenthesis, Ex. (2,3,4-6)
        ports_list = groups[0].replace("(", "").replace(")", "").split(",")
        for i in ports_list:
            replaced_list.append(one_range.replace(one_range[start_index:end_index], str(i), 1))
    elif groups[1]:
        # To replace the values of range, Ex. 4-6
        range_start, range_end = groups[1].split("-")
        for i in range(int(range_start), int(range_end) + 1):
            replaced_list.append(one_range.replace(one_range[start_index:end_index], str(i), 1))
    return replaced_list


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
        # Replacing "," inside () with "&" so that below for loop won't split it.
        range_to_expand = re.sub(r"\((.*?)\)", lambda match: match.group(0).replace(",", "&"), range_to_expand)
        # Unpack list in string
        for one_range in range_to_expand.split(","):
            # Changing "&" back to ",".
            one_range = re.sub(r"\((.*?)\)", lambda match: match.group(0).replace("&", ","), one_range)
            if one_range is None:
                continue
            regex = r"([A-Za-z]+\s*)?(.*)"
            sr = re.search(regex, one_range)
            try:
                prefix_group = sr.groups()
                if prefix_group[0]:
                    prefix = prefix_group[0]
                else:
                    one_range = prefix + one_range
                result.extend(range_expand(extend_range(one_range)))
            except AttributeError:
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
