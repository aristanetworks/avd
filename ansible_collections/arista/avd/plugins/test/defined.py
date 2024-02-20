# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
#
# arista.avd.defined
from __future__ import absolute_import, division, print_function

__metaclass__ = type

import logging

from ansible.errors import AnsibleError
from ansible.utils.display import Display

from ansible_collections.arista.avd.plugins.plugin_utils.utils import PythonToAnsibleHandler

try:
    from pyavd.j2tests.defined import defined

    HAS_PYAVD = True
except ImportError:
    HAS_PYAVD = False

LOGGER = logging.getLogger("ansible_collections.arista.avd")
LOGGING_LEVELS = ["DEBUG", "INFO", "ERROR", "WARNING", "CRITICAL"]

DOCUMENTATION = r"""
---
name: defined
collection: arista.avd
author: Arista Ansible Team (@aristanetworks)
version_added: "2.0"
short_description: Test if the value is not `Undefined` or `None`.
description:
  - The `arista.avd.defined` test returns `False` if the passed value is `Undefined` or `None`. Else it will return `True`.
  - The `arista.avd.defined` test also accepts an optional `test_value` argument to test if the value equals this.
  - The optional `var_type` argument can also be used to test if the variable is of the expected type.
  - Optionally, the test can emit warnings or errors if the test fails.
  - Compared to the built-in `is defined` test, this test will also test for `None` and can even test for a specific value or class.
positional: _input
options:
  _input:
    description: Value to test
    required: true
  test_value:
    description: Value to match for in addition to defined and not none
    default: None
  var_type:
    type: string
    description: Type or Class to test for
    choices: ['float', 'int', 'str', 'list', 'dict', 'tuple', 'bool']
  fail_action:
    type: string
    description: Optional action if a test fails to emit a Warning or Error
    choices: ['warning', 'error']
  var_name:
    type: string
    description: Optional string to use as a variable name in warning or error messages
"""

EXAMPLES = r"""
# Test if "my_var" is defined and not none:
is_defined_and_not_none: "{{ my_var is arista.avd.defined }}"

# Test if "my_var" is defined, not none and has value "something"
is_defined_and_set_to_something: "{{ my_var is arista.avd.defined('something') }}"

# Test if "my_var" is defined and if not print a warning message with the variable name
test_result: "{{ my_dict.my_list[12].my_var is arista.avd.defined(fail_action='warning', var_name='my_dict.my_list[12].my_var' }}"
# Output >>> [WARNING]: my_dict.my_list[12].my_var was expected but not set. Output may be incorrect or incomplete!
"""

RETURN = r"""
---
_value:
  description:
    - Returns `False` if the passed value is `Undefined` or `None` or if any of the optional checks fail. Otherwise `True`.
  type: boolean
"""


def setup_module_logging(result: dict) -> None:
    """
    Add a Handler to copy the logs from the plugin into Ansible output based on their level

    Parameters:
        result: The dictionary used for the ansible module results
    """
    python_to_ansible_handler = PythonToAnsibleHandler(result, Display())
    LOGGER.addHandler(python_to_ansible_handler)
    # TODO mechanism to manipulate the logger globally for pyavd
    # Keep debug to be able to see logs with `-v` and `-vvv`
    LOGGER.setLevel(logging.DEBUG)


class TestModule(object):
    def tests(self):
        if not HAS_PYAVD:
            raise AnsibleError("The Python library 'pyavd' cound not be found. Please install using 'pip3 install'")
        setup_module_logging({})
        return {
            "defined": defined,
        }
