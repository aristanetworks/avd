#
# def arista.avd.default
#
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from jinja2.runtime import Undefined


def default(primary_value, *default_values):
    """
    default will test value if defined and is not none.

    Arista.avd.default will test value if defined and is not none. If true
    return value else test default_value1.
    Test of default_value1 if defined and is not none. If true return
    default_value1 else test default_value2.
    If we run out of default values we return none.

    Example
    -------
    priority: {{ switch.spanning_tree_priority | arista.avd.default("32768") }}

    Parameters
    ----------
    primary_value : any
        Ansible default value to look for

    Returns
    -------
    any
        Default value
    """
    if isinstance(primary_value, Undefined) or primary_value is None:
        # Invalid value - try defaults
        if len(default_values) >= 1:
            # Return the result of another loop
            return default(default_values[0], *default_values[1:])
        else:
            # Return None
            return
    else:
        # Return the valid value
        return primary_value


class FilterModule(object):
    def filters(self):
        return {
            'default': default,
        }
