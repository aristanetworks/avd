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

from ansible_collections.arista.avd.plugins.action.verify_requirements import _get_running_collection_version


def wrap_filter(name: str, pyavd_import_error: Exception | None) -> Callable:
    def wrap_filter_decorator(func: Callable | None) -> Callable:
        @wraps(func)
        def filter_wrapper(*args, **kwargs):
            if pyavd_import_error:
                result = {}
                _get_running_collection_version("arista.avd", result)
                version = result["collection"]["version"]
                raise AnsibleFilterError(
                    f"Filter '{name}' was not imported correctly. Check PyAVD is installed correctly with version '{version}' "
                    f"and that all PyAVD dependencies are also installed correctly. Got import error: '{to_native(pyavd_import_error)}'",
                    orig_exc=pyavd_import_error,
                )

            try:
                return func(*args, **kwargs)
            except UndefinedError as e:
                raise AnsibleUndefinedVariable(f"Filter '{name}' failed: {to_native(e)}", orig_exc=e) from e
            except Exception as e:
                raise AnsibleFilterError(f"Filter '{name}' failed: {to_native(e)}", orig_exc=e) from e

        return filter_wrapper

    return wrap_filter_decorator
