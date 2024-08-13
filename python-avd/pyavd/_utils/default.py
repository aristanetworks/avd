# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from typing import Any


def default(*values: Any) -> Any:
    """
    Accepts any number of arguments. Return the first value which is not None.

    Last resort is to return None.

    Parameters
    ----------
    *values : any
        One or more values to test

    Returns:
    -------
    any
        First value which is not None
    """
    for value in values:
        if value is not None:
            return value
    return None
