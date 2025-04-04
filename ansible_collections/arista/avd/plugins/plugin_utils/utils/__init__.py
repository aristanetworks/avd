# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from ansible_collections.arista.avd.plugins.plugin_utils.pyavd_wrappers import RaiseOnUse

from .action_plugin_vars import ActionPluginVars
from .anta_logging_filter import AntaLoggingFilter
from .avd_switch_facts_default_dict import AvdSwitchFactsDefaultDict
from .compile_searchpath import compile_searchpath
from .cprofile_decorator import cprofile
from .get_templar import get_templar
from .get_validated_path import get_validated_path
from .get_validated_value import get_validated_value
from .log_message import log_message
from .python_to_ansible_logging_handler import PythonToAnsibleContextFilter, PythonToAnsibleHandler
from .write_file import write_file
from .yaml_dumper import NoAliasDumper, YamlDumper
from .yaml_loader import YamlLoader

# TODO: The pyavd imports can be removed once validate_state has been moved to pyavd.
try:
    from pyavd._utils import default, get
except ImportError as e:
    default = get = RaiseOnUse(ImportError(f"The 'arista.avd' collection requires the 'pyavd' Python library. Got import error {e}"))

__all__ = [
    "ActionPluginVars",
    "AntaLoggingFilter",
    "AvdSwitchFactsDefaultDict",
    "NoAliasDumper",
    "PythonToAnsibleContextFilter",
    "PythonToAnsibleHandler",
    "YamlDumper",
    "YamlLoader",
    "compile_searchpath",
    "cprofile",
    "default",
    "get",
    "get_templar",
    "get_validated_path",
    "get_validated_value",
    "log_message",
    "write_file",
]
