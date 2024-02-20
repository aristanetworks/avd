# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
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

import logging

from jinja2.runtime import Undefined

from ..errors import AristaAvdError


def defined(value, test_value=None, var_type=None, fail_action=None, var_name=None):
    """
    defined - Ansible test plugin to test if a variable is defined and not none

    Arista.avd.defined will test value if defined and is not none and return true or false.
    If test_value is supplied, the value must also pass == test_value to return true.
    If var_type is supplied, the value must also be of the specified class/type
    If fail_action is 'warning' a warning will be emitted on failure.
    If fail_action is 'error' an error will be emitted on failure and the task will fail.
    If var_name is supplied it will be used in the warning and error messages to ease troubleshooting.

    Examples:
    1. Test if var is defined and not none:
    {% if spanning_tree is arista.avd.defined %}
    ...
    {% endif %}

    2. Test if variable is defined, not none and has value "something"
    {% if extremely_long_variable_name is arista.avd.defined("something") %}
    ...
    {% endif %}

    3. Test if variable is defined and of not print a warning message with the variable name
    {% if my_dict.my_list[12].my_var is arista.avd.defined(fail_action='warning', var_name='my_dict.my_list[12].my_var' %}

    Parameters
    ----------
    value : any
        Value to test from ansible
    test_value : any, optional
        Value to test in addition of defined and not none, by default None
    var_type : ['float', 'int', 'str', 'list', 'dict', 'tuple', 'bool'], optional
        Type or Class to test for
    fail_action : ['warning', 'error'], optional
        Optional action if test fails to emit a Warning or Error
    var_name : <string>, optional
        Optional string to use as variable name in warning or error messages

    Returns
    -------
    boolean
        True if variable matches criteria, False in other cases.
    """
    if isinstance(value, Undefined) or value is None:
        # Invalid value - return false
        if str(fail_action).lower() == "warning":
            if var_name is not None:
                logging.warning("%s was expected but not set. Output may be incorrect or incomplete!", var_name)
            else:
                logging.warning("A variable was expected but not set. Output may be incorrect or incomplete!")
        elif str(fail_action).lower() == "error":
            if var_name is not None:
                raise AristaAvdError(f"{var_name} was expected but not set!")
            else:
                raise AristaAvdError("A variable was expected but not set!")

        return False

    elif test_value is not None and value != test_value:
        # Valid value but not matching the optional argument
        if str(fail_action).lower() == "warning":
            if var_name is not None:
                logging.warning("%s was set to %s but we expected %s. Output may be incorrect or incomplete!", var_name, value, test_value)
            else:
                logging.warning("A variable was set to %s but we expected %s. Output may be incorrect or incomplete!", value, test_value)
        elif str(fail_action).lower() == "error":
            if var_name is not None:
                raise AristaAvdError(f"{var_name} was set to {value} but we expected {test_value}!")
            else:
                raise AristaAvdError(f"A variable was set to {value} but we expected {test_value}!")

        return False
    elif str(var_type).lower() in ["float", "int", "str", "list", "dict", "tuple", "bool"] and str(var_type).lower() != type(value).__name__:
        # Invalid class - return false
        expected_type = str(var_type).lower()
        actual_type = type(value).__name__
        if str(fail_action).lower() == "warning":
            if var_name is not None:
                logging.warning("%s was a %s but we expected a %s. Output may be incorrect or incomplete!", var_name, actual_type, expected_type)
            else:
                logging.warning("A variable was a %s but we expected a %s. Output may be incorrect or incomplete!", actual_type, expected_type)
        elif str(fail_action).lower() == "error":
            if var_name is not None:
                raise AristaAvdError(f"{var_name} was a {actual_type} but we expected a {expected_type}!")
            else:
                raise AristaAvdError(f"A variable was a {actual_type} but we expected a {expected_type}!")

        return False
    else:
        # Valid value and is matching optional argument if provided - return true
        return True
