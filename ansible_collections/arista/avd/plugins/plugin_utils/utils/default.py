def default(*values):
    """
    Accepts any number of arguments. Return the first value which is not None

    Last resort is to return None.

    Parameters
    ----------
    *values : any
        One or more values to test

    Returns
    -------
    any
        First value which is not None
    """

    for value in values:
        if value is not None:
            return value
    return None
