#
# def arista.avd.is_valid
#
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from jinja2.runtime import Undefined

def is_valid(value):
    if isinstance(value, Undefined) or value is None:
        #Invalid value - return false
        return False
    else:
        #Valid value - return true
        return True

class FilterModule(object):
    def filters(self):
        return {
            'is_valid': is_valid,
        }
