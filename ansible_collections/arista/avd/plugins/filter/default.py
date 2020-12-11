#
# def arista.avd.default
#
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from jinja2.runtime import Undefined

def default(primary_value, *default_values ):
    if isinstance(primary_value, Undefined) or primary_value is None:
        #Invalid value - try defaults
        if len(default_values) >= 1:
            #Return the result of another loop
            return default(default_values[0],*default_values[1:])
        else:
            #Return None
            return
    else:
        #Return the valid value
        return primary_value

class FilterModule(object):
    def filters(self):
        return {
            'default': default,
        }
