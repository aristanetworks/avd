# Copyright (c) 2019-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import absolute_import, annotations, division, print_function

__metaclass__ = type

from functools import wraps
from typing import Callable

from ansible.errors import AnsibleFilterError, AnsibleUndefinedVariable
from ansible.module_utils.basic import to_native
from jinja2.exceptions import UndefinedError


class RaiseOnUse:
    """
    Class that will delay raises of errors until the instance is called.

    Used with Ansible try/except import logic to not fail on import of plugins, but instead fail on first use.
    """

    def __init__(self, exception: Exception):
        self.exception = exception

    def __call__(self, *args):
        raise self.exception


def wrap_filter(name: str) -> Callable:
    def wrap_filter_decorator(func: Callable | None) -> Callable:
        @wraps(func)
        def filter_wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except UndefinedError as e:
                raise AnsibleUndefinedVariable(f"Filter '{name}' failed: {to_native(e)}", orig_exc=e) from e
            except Exception as e:
                raise AnsibleFilterError(f"Filter '{name}' failed: {to_native(e)}", orig_exc=e) from e

        return filter_wrapper

    return wrap_filter_decorator
