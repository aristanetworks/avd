# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
#
# natural_sort filter
#
from __future__ import absolute_import, division, print_function

__metaclass__ = type

import re

from jinja2.runtime import Undefined
from jinja2.utils import Namespace

DOCUMENTATION = r"""
---
name: natural_sort
collection: arista.avd
author: Arista Ansible Team (@aristanetworks)
version_added: "1.0.0"
short_description: Sort an input list with natural sorting.
description:
  - |-
      Provides the capability to sort a list or a dictionary of integers and strings that contain alphanumeric characters naturally.
      When leveraged on a dictionary, only the key value will be returned.
      An optional `sort_key` can be specified, to sort on content of certain key if the items are dictionaries.
  - The filter will return an empty list if the value parsed to M(arista.avd.natural_sort) is C(None) or C(undefined).
positional: _input
options:
  _input:
    description: List or dictionary
    type: any
    required: true
  sort_key:
    description: Key to sort on when sorting a list of dictionaries
    type: string
    version_added: "3.0.0"
"""

EXAMPLES = r"""
---
sorted_list: "{{ ['test19', 'test9'] | natural_sort }}" # -> ["test9", "test19"]
sorted_keys: "{{ {'test19': 'value', 'test9': 'value'} | natural_sort }}" # -> ["test9", "test19"]
sorted_on_name_key: "{{ [{'name': 'test19'}, {'name': 'test9'}] | natural_sort('name') }}" # -> [{"name": "test9"}, {"name": "test19"}]
empty_list_1: "{{ none | natural_sort }}" # -> []
empty_list_2: "{{ some_undefined_var | natural_sort }}" # -> []
"""

RETURN = r"""
---
_value:
  description: Sorted list if the input was a list. Sorted keys if the input was a dictionary. Empty list if the input value was C(None) or C(undefined).
  type: list
"""


def convert(text):
    return int(text) if text.isdigit() else text.lower()


def natural_sort(iterable, sort_key=None):
    if isinstance(iterable, Undefined) or iterable is None:
        return []

    def alphanum_key(key):
        if sort_key is not None and isinstance(key, dict):
            return [convert(c) for c in re.split("([0-9]+)", str(key.get(sort_key, key)))]
        elif sort_key is not None and isinstance(key, Namespace):
            return [convert(c) for c in re.split("([0-9]+)", getattr(key, sort_key))]
        else:
            return [convert(c) for c in re.split("([0-9]+)", str(key))]

    return sorted(iterable, key=alphanum_key)


class FilterModule(object):
    def filters(self):
        return {
            "natural_sort": natural_sort,
        }
