def unique(in_list):
    """
    Return list of unique items from the in_list

    Parameters
    ----------
    in_list : list

    Returns
    -------
    list
        Unique list items
    """

    list_set = set(in_list)
    return list(list_set)
