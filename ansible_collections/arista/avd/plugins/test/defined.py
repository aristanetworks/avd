#
# arista.avd.defined
#
# Example:
# A is undefined
# B is none
# C is "c"
# D is "d"
#
# Jinja test examples:
# {% if A is arista.avd.defined %}  =>  false
# {% if B is arista.avd.defined %}  =>  false
# {% if C is arista.avd.defined %}  =>  true
# {% if D is arista.avd.defined %}  =>  true
#
# {% if A is arista.avd.defined("c") %}  =>  false
# {% if B is arista.avd.defined("c") %}  =>  false
# {% if C is arista.avd.defined("c") %}  =>  true
# {% if D is arista.avd.defined("c") %}  =>  false

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from jinja2.runtime import Undefined


def defined(value, test_value=None):
    """
    defined - Ansible test plugin to test if a variable is defined and not none

    Arista.avd.defined will test value if defined and is not none and return true or false.
    If test_value is supplied, the value must also pass == test_value to return true.

    Example:
    1. Test if var is defined and not none:
    {% if spanning_tree is arista.avd.defined %}
    ...
    {% endif %}
    2. Test if variable is defined, not none and has value "something"
    {% if extremely_long_variable_name is arista.avd.defined("something") %}
    ...
    {% endif %}

    Parameters
    ----------
    value : any
        Value to test from ansible
    test_value : any, optional
        value to test in addition of defined and not none, by default None

    Returns
    -------
    boolean
        True if variable matches criteria, False in other cases.
    """
    if isinstance(value, Undefined) or value is None:
        # Invalid value - return false
        return False
    elif test_value is not None and value != test_value:
        # Valid value but not matching the optional argument
        return False
    else:
        # Valid value and is matching optional argument if provided - return true
        return True


class TestModule(object):
    def tests(self):
        return {
            'defined': defined,
        }
