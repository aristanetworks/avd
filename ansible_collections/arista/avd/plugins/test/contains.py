#
# arista.avd.contains
#
# Example:
# A is [1, 2]
# B is [3, 4]
# C is [2, 3]
#
# Jinja test examples:
# {% if A is arista.avd.contains(B) %}  =>  false
# {% if B is arista.avd.contains(C) %}  =>  true
# {% if C is arista.avd.contains(A) %}  =>  true
# {% if C is arista.avd.contains(B) %}  =>  true
#
# {% if A is arista.avd.contains(0) %}  =>  false
# {% if B is arista.avd.contains(1) %}  =>  false
# {% if C is arista.avd.contains(2) %}  =>  true
# {% if D is arista.avd.contains(3) %}  =>  false <- Protecting against undefined gracefully.

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from jinja2.runtime import Undefined


def contains(value, test_value=None):
    """
    contains - Ansible test plugin to test if a list contains one or more elements

    Arista.avd.contains will test value and argument if defined and is not none and return false if any one them doesn't pass.
    Test value can be one value or a list of values to test for.

    Example:
    1. Test for one element in list
    {% if switch.vlans is arista.avd.contains(123) %}
    ...
    {% endif %}
    2. Test for multiple elements in list
    {% if switch.vlans is arista.avd.contains([123, 456]) %}
    ...
    {% endif %}

    Parameters
    ----------
    value : any
        List to test
    test_value : single item or list of items
        Value(s) to test for in value

    Returns
    -------
    boolean
        True if variable matches criteria, False in other cases.
    """
    if isinstance(value, Undefined) or value is None or not isinstance(value, list):
        # Invalid value - return false
        return False
    elif isinstance(test_value, Undefined) or value is None:
        # Invalid value - return false
        return False
    elif isinstance(test_value, list) and not set(value).isdisjoint(test_value):
        # test_value is list so test if value and test_value has any common items
        return True
    elif test_value in value:
        # Test if test_value is in value
        return True
    else:
        return False


class TestModule(object):
    def tests(self):
        return {
            'contains': contains,
        }
