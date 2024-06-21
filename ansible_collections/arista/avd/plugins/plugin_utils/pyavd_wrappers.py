# Copyright (c) 2019-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import absolute_import, annotations, division, print_function

__metaclass__ = type

import warnings
from functools import partial, wraps
from typing import Callable, Literal

from ansible.errors import AnsibleFilterError, AnsibleInternalError, AnsibleTemplateError, AnsibleUndefinedVariable
from ansible.module_utils.basic import to_native
from ansible.utils.display import Display
from jinja2.exceptions import UndefinedError

display = Display()


class RaiseOnUse:
    """
    Class that will delay raises of errors until the instance is called.

    Used with Ansible try/except import logic to not fail on import of plugins, but instead fail on first use.
    """

    def __init__(self, exception: Exception):
        self.exception = exception

    def __call__(self, *args, **kwargs):
        raise self.exception


def wrap_plugin(plugin_type: Literal["filter", "test"], name: str) -> Callable:
    plugin_map = {
        "filter": AnsibleFilterError,
        "test": AnsibleTemplateError,
    }

    if plugin_type not in plugin_map:
        raise AnsibleInternalError(f"Wrong plugin type {plugin_type} passed to wrap_plugin.")

    def wrap_plugin_decorator(func: Callable) -> Callable:
        @wraps(func)
        def plugin_wrapper(*args, **kwargs):
            """Wrapper function for plugins.

            NOTE: if the same warning is raised multiple times, Ansible Display() will print only one
            """
            try:
                with warnings.catch_warnings(record=True) as w:
                    result = func(*args, **kwargs)
                    if w:
                        for warning in w:
                            display.warning(str(warning.message))
                return result
            except UndefinedError as e:
                raise AnsibleUndefinedVariable(f"{plugin_type.capitalize()} '{name}' failed: {to_native(e)}", orig_exc=e) from e
            except Exception as e:
                raise plugin_map[plugin_type](f"{plugin_type.capitalize()} '{name}' failed: {to_native(e)}", orig_exc=e) from e

        return plugin_wrapper

    return wrap_plugin_decorator


wrap_filter = partial(wrap_plugin, "filter")
wrap_test = partial(wrap_plugin, "test")
