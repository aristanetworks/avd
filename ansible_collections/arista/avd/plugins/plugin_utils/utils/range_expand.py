def expand_parentheses(range_sr: object, range_to_expand: str) -> list:
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


def expand_hyphen(range_sr: object, range_to_expand: str) -> list:
    """
    Expand the numbers in a string seperated by hyphen(-) to get continuous
    numbers using regular expressions and forms a new string with each numbers separately.

    Example
    -------
    "Eth2-4" -> ["Eth2", "Eth3", "Eth4"]

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
