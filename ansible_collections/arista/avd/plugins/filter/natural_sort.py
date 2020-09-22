#
# natural_sort filter
#
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import re


def convert(text):
    return int(text) if text.isdigit() else text.lower()


def alphanum_key(key):
    return [convert(c) for c in re.split('([0-9]+)', str(key))]


class FilterModule(object):

    def natural_sort(self, iterable):
        return sorted(iterable, key=alphanum_key)

    def filters(self):
        return {
            'natural_sort': self.natural_sort,
        }
