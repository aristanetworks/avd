# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from re import Match, search, split

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError


def expand_curly_brackets(range_sr: Match, range_to_expand: str) -> list:
    """
    Replace content inside curly brackets separated by commas(,) using regular
    expressions and forms a new string with each comma separated element.

    Example
    -------
    "Eth{1,2,3}" -> ["Eth1", "Eth2", "Eth3"]
    "Eth{1,2-4}" -> ["Eth1", "Eth2-4"]

    Parameters
    ----------
    range_sr :
        re.search() object
    range_to_expand :
        string to expand

    Returns
    -------
    list of replaced str
    """
    group = range_sr.group("curly_brackets")
    start_index, end_index = range_sr.start(), range_sr.end()
    replaced_list = []
    if group:
        # To replace the values inside curly brackets, Ex. (2,3,4-6)
        ports_list = group.replace("{", "").replace("}", "").split(",")
        for port in ports_list:
            replaced_list.append(range_to_expand.replace(range_to_expand[start_index:end_index], str(port), 1))
    return replaced_list


def expand_hyphen(range_sr: Match, range_to_expand: str) -> list:
    """
    Expand the numbers in a string seperated by hyphen(-) to get continuous
    numbers using regular expressions and forms a new string with each numbers separately.

    Example
    -------
    "Eth2-4" -> ["Eth2", "Eth3", "Eth4"],

    Parameters
    ----------
    range_sr :
        re.search object
    range_to_expand :
        string to expand

    Returns
    -------
    list of replaced str
    """
    group = range_sr.group("hyphen")
    start_index, end_index = range_sr.start(), range_sr.end()
    replaced_list = []
    if group:
        # To replace the values of range, Ex. 4-6
        range_start, range_end = group.split("-")
        for port_num in range(int(range_start), int(range_end) + 1):
            replaced_list.append(range_to_expand.replace(range_to_expand[start_index:end_index], str(port_num), 1))
    return replaced_list


def range_expand_utils(range_to_expand: str | list, prefix: str = "") -> list:
    """
    range_expand_utils recursively calls itself in order to expand the range in a
    string seperated by comma(,) or hyphen(-). It would also add a prefix to the
    number if it is not already present based on previous list element prefix (if present).

    Example
    -------
    "Eth2-4" -> ["Eth2", "Eth3", "Eth4"]
    "Eth{1,2,3}" -> ["Eth1", "Eth2", "Eth3"],
    "Ethernet{4,1-2}" -> ["Ethernet4", "Ethernet1", "Ethernet2"]

    Parameters
    ----------
    range_to_expand :
        str | list to expand
    prefix :
        string, dafault value = ""

    Returns
    -------
    list of expanded strings
    """
    if not (isinstance(range_to_expand, list) or isinstance(range_to_expand, str)):
        raise AristaAvdError(f"value must be of type list or str, got {type(range_to_expand)}")

    result = []

    # If we got a list, unpack it and run this function recursively
    if isinstance(range_to_expand, list):
        for one_range in range_to_expand:
            result.extend(range_expand_utils(one_range, prefix))

    else:
        # Must be a str now
        if range_to_expand is None:
            return

        regex = r"([A-Za-z]+\s*)?(.*)"
        sr = search(regex, range_to_expand)

        prefix_group = sr.groups()
        if prefix_group[0]:
            prefix = prefix_group[0]
        else:
            range_to_expand = prefix + range_to_expand

        regex_commas_outside_curly_brackets = r",(?![^{]*\})"
        # Above regex matches all the commas "," outside curly brackets.
        # Except the case where there is no opening curly bracket but closing curly bracket is present [Example: ",4}"]
        # It considers the comma inside the curly brackets whereas it is actually outside.

        regex_commas_inside_curly_brackets = r"(?P<curly_brackets>\{\s*\d+\s*(?:-\s*\d+\s*)?(?:,\s*\d+\s*(?:-\s*\d+\s*)?)*})"
        #     (\{} \})                                                                                  matches starting and ending of curly_brackets
        #     ?P<curly_brackets>                                                                        assigning name to the group.
        #     ?:                                                                                        only group but do not remember the grouped part
        #                                                           \s*\d+\s*                           matches 1 or more numbers and spaces before and
        #                                                                                                   after it, Ex. 1 or 21
        #                                                                    (?:-\s*\d+\s*)?            matches 0 or one apperance of hyphen followed by
        #                                                                                                   a number and spaces between them, Ex. -3 or - 4
        #                                                           (?:,\s*\d+\s*(?:-\s*\d+\s*)?)*      matches 0 or more apperance of comma followed by
        #                                                                                                   number and spaces in between, along with hyphen
        #                                                                                                       followed by a number and spaces between
        #                                                                                                           them, Ex. ,1 , 3-5,7-11
        #                                \{\s*\d+\s*(?:-\s*\d+\s*)?(?:,\s*\d+\s*(?:-\s*\d+\s*)?)*}      matches values similar to {1} or {1,2,3} or {1, 2-4}

        regex_hyphen_range = r"(?P<hyphen>(?<!-\s)(?<!-)(\d+\s*\-\s*\d+)(?!\s*-\s*))"
        #                       ?P<hyphen>                                                              assigning name to the group.
        #                                (?<!-\s)(?<!-)                                                 negative lookbehind for hyphen and hyphen with single
        #                                                                                                   space to avoid cases like 2-3-4-6 or 2 -3- 4
        #                                               (\d+\s*\-\s*\d+)                                matches number followed by hyphen followed by number
        #                                                                                                   and spaces between them, EX. 1-2 or 1 -3 or 66- 89
        #                                                               (?!\s*-\s*)                     negative lookahead for hyphen and spaces around it to
        #                                                                                                   avoid cases like 2-3-4-6 or 2 -3- 4

        search_result = search(f"{regex_commas_inside_curly_brackets}|{regex_hyphen_range}", range_to_expand)

        if search(regex_commas_outside_curly_brackets, range_to_expand):
            # Split by comma outside curly brackets
            result.extend(range_expand_utils(split(regex_commas_outside_curly_brackets, range_to_expand), prefix))
        elif search_result and search_result.group("curly_brackets"):
            # Expand curly brackets
            result.extend(range_expand_utils(expand_curly_brackets(search_result, range_to_expand), prefix))
        elif search_result and search_result.group("hyphen"):
            # Expand hyphen
            result.extend(range_expand_utils(expand_hyphen(search_result, range_to_expand), prefix))
        else:
            if range_to_expand:
                result.extend([range_to_expand])
    return result
