from re import Match, search, split

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError


def expand_parentheses(range_sr: Match, range_to_expand: str) -> list:
    """
    Replace content inside parentheses separated by commas(,) using regular
    expressions and forms a new string with each comma separated element.

    Example
    -------
    "Eth(1,2,3)" -> ["Eth1", "Eth2", "Eth3"]
    "Eth(1,2-4)" -> ["Eth1", "Eth2-4"]

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
    groups = range_sr.groups()
    start_index, end_index = range_sr.start(), range_sr.end()
    replaced_list = []
    if groups[0]:
        # To replace the values inside parenthesis, Ex. (2,3,4-6)
        ports_list = groups[0].replace("(", "").replace(")", "").split(",")
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
    groups = range_sr.groups()
    start_index, end_index = range_sr.start(), range_sr.end()
    replaced_list = []
    if groups[0]:
        # To replace the values of range, Ex. 4-6
        range_start, range_end = groups[0].split("-")
        for port_num in range(int(range_start), int(range_end) + 1):
            replaced_list.append(range_to_expand.replace(range_to_expand[start_index:end_index], str(port_num), 1))
    return replaced_list


def range_expand_utils(range_to_expand: str or list, prefix: str = "") -> list:
    """
    range_expand_utils recursively calls itself in order to expand the range in a
    string seperated by comma(,) or hyphen(-). It would also add a prefix to the
    number if it is not already present based on previous list element prefix (if present).

    Example
    -------
    "Eth2-4" -> ["Eth2", "Eth3", "Eth4"]
    "Eth(1,2,3)" -> ["Eth1", "Eth2", "Eth3"],
    "Ethernet(4,1-2)" -> ["Ethernet4", "Ethernet1", "Ethernet2"]

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

        if search(regex_commas_outside_parentheses, range_to_expand):
            # Split comma outside parentheses
            result.extend(range_expand_utils(split(regex_commas_outside_parentheses, range_to_expand), prefix))
        elif parentheses_sr := search(regex_commas_inside_parentheses, range_to_expand):
            # Expand parentheses
            result.extend(range_expand_utils(expand_parentheses(parentheses_sr, range_to_expand), prefix))
        elif hyphen_sr := search(regex_hyphen_range, range_to_expand):
            # Expand hyphen
            result.extend(range_expand_utils(expand_hyphen(hyphen_sr, range_to_expand), prefix))
        else:
            if range_to_expand:
                result.extend([range_to_expand])
    return result
