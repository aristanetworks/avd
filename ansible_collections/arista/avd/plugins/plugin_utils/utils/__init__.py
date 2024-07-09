# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from ansible_collections.arista.avd.plugins.plugin_utils.pyavd_wrappers import RaiseOnUse

from .compile_searchpath import compile_searchpath
from .cprofile_decorator import cprofile
from .get_templar import get_templar
from .get_validated_path import get_validated_path
from .get_validated_value import get_validated_value
from .log_message import log_message
from .python_to_ansible_logging_handler import PythonToAnsibleContextFilter, PythonToAnsibleHandler
from .yaml_dumper import NoAliasDumper, YamlDumper
from .yaml_loader import YamlLoader

# TODO: AVD5.0.0 Some utils are exposed in custom modules code, so we will need to keep it here until 5.0
try:
    from pyavd._utils import get, template, template_var
except ImportError as e:
    get = template = template_var = RaiseOnUse(ImportError(f"The 'arista.avd' collection requires the 'pyavd' Python library. Got import error {e}"))

__all__ = [
    "compile_searchpath",
    "get_templar",
    "log_message",
    "PythonToAnsibleContextFilter",
    "PythonToAnsibleHandler",
    "NoAliasDumper",
    "get_validated_path",
    "get_validated_value",
    "cprofile",
    "YamlDumper",
    "YamlLoader",
    "get",
    "template",
    "template_var",
]
