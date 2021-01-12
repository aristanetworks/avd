#
# natural_sort filter
#
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import re
from jinja2.runtime import Undefined


def convert(text):
    return int(text) if text.isdigit() else text.lower()


def alphanum_key(key):
    return [convert(c) for c in re.split('([0-9]+)', str(key))]


class FilterModule(object):

    def natural_sort(self, iterable):
        if isinstance(iterable, Undefined) or iterable is None:
            return list()
        return sorted(iterable, key=alphanum_key)

    def filters(self):
        return {
            'natural_sort': self.natural_sort,
        }
