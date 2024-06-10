# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from itertools import count, groupby

from ansible.errors import AnsibleFilterError

def list_compress(list_to_compress: list) -> str:
    """
    Compresses a list of integers to a range string.
    Args:
        list_to_compress (list): List of integers.
    Returns:
        str: Compressed range string.

    Example when used as a jinja filter
    -------
    list1: "{{ [1,2,3,4,5] | arista.avd.list_compress }}" -> "1-5"
    list2: "{{ [1,2,3,7,8] | arista.avd.list_compress }}" -> "1-3,7-8"
    """
    if not isinstance(list_to_compress, list):
        raise AnsibleFilterError(f"Value must be of type list, got {type(list_to_compress)}")

    list_of_groups = (list(group) for key, group in groupby(sorted(list_to_compress), lambda element, iterator=count(): next(iterator) - element))
    
    return ",".join("-".join(map(str, (group[0], group[-1])[: len(group)])) for group in list_of_groups)
