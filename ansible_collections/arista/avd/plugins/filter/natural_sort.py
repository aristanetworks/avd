#
# natural_sort filter
#
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import re
from jinja2.runtime import Undefined


def convert(text):
    return int(text) if text.isdigit() else text.lower()


class FilterModule(object):

    def natural_sort(self, iterable, sort_key=None):
        if isinstance(iterable, Undefined) or iterable is None:
            return list()

        def alphanum_key(key):
            if sort_key is not None and isinstance(key, dict):
                return [convert(c) for c in re.split('([0-9]+)', str(key.get(sort_key, key)))]
            else:
                return [convert(c) for c in re.split('([0-9]+)', str(key))]

        return sorted(iterable, key=alphanum_key)

    def filters(self):
        return {
            'natural_sort': self.natural_sort,
        }
