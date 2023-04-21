from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
    name: global_vars
    version_added: "4.0.0"
    short_description: Variable plugins to allow loading global_vars with less precedence than group_vars or host_vars
    requirements:
        - Should run at the 'inventory' stage (default) before all other
    description:
        - Loads variables from a variable file present in ansible.cfg and inject them in the 'all' group
        - Files are restricted by extension to one of .yaml, .json, .yml or no extension.
        - Hidden (starting with '.') and backup (ending with '~') files and directories are ignored.
        - Only applies to inventory sources that are existing paths.
    options:
      paths:
        required: true
        type: list
        elements: string
        ini:
          - key: paths
            section: vars_global_vars
        env:
          - name: ARISTA_AVD_GLOBAL_VARS_PATHS
        description:
          - List of relative paths, relative  to the inventory file.
          - If path is a directory, all the valid files inside are loaded in alphabetical order.
          - If the environment variable is set, it takes precedence over ansible.cfg.
      stage:
        default: inventory
        choices: ["inventory"]
        description:
          - The stage during which executing the plugin. It could be 'inventory' or 'task'
          - Given the expected usage of this plugin at the beginning of the run. It is hardcoded to 'inventory'
      _valid_extensions:
        default: [".yml", ".yaml", ".json"]
        description:
          - "Check all of these extensions when looking for 'variable' files which should be YAML or JSON or vaulted versions of these."
          - 'This affects vars_files, include_vars, inventory and vars plugins among others.'
        ini:
          - key: yaml_valid_extensions
            section: defaults
        type: list
        elements: string
"""

OTHER = """
# To enable the global_variable plugin in `ansible.cfg`
[defaults]
vars_plugins_enabled = arista.avd.global_vars, host_group_vars

[vars_global_vars]
paths = ../../relative/path/to/my/global/vars/file/or/dir
"""


import os

from ansible.errors import AnsibleParserError
from ansible.inventory.group import Group
from ansible.inventory.host import Host
from ansible.module_utils._text import to_bytes, to_native, to_text
from ansible.plugins.vars import BaseVarsPlugin
from ansible.utils.vars import combine_vars

FOUND: list[str] = []


class VarsModule(BaseVarsPlugin):
    def find_variable_source(self, path, loader):
        """
        Return the source files from which to load data,
        if the path is a directory - lookup vars file inside
        """
        global_vars_paths = self.get_option("paths")

        found_files = []
        for g_path in global_vars_paths:
            b_opath = os.path.realpath(to_bytes(os.path.join(path, g_path)))
            opath = to_text(b_opath)
            try:
                if not os.path.exists(b_opath):
                    # file does not exist, skip it
                    self._display.vvv(f"Path: {opath} does not exist - skipping")
                    continue
                self._display.vvv(f"Adding Path: {opath} to global variables")
                if os.path.isdir(b_opath):
                    # THIS NEEDS TO BE FIXED
                    name = "test"
                    found_files.extend(loader.find_vars_files(opath, name))
                else:
                    found_files.append(b_opath)

            except Exception as e:
                raise AnsibleParserError(to_native(e)) from e

        return found_files

    def get_vars(self, loader, path, entities, cache=True):
        """
        Return global variables for the `all` group in the inventory file
        """
        global FOUND
        if not isinstance(entities, list):
            entities = [entities]

        if not FOUND:
            FOUND = self.find_variable_source(path, loader)

        variables = {}
        for entity in entities:
            if not isinstance(entity, (Host, Group)):
                # Changed the error message because the TYPE_REGEX of ansible was triggering
                # unidiomatic-typecheck because of the `or` word before the type  call...
                raise AnsibleParserError(f"Supplied entity is of type {type(entity)} but must be of type Host or Group instead")
            if entity.name != "all":
                continue

            print(entity.name, path)

            for path in FOUND:
                if new_data := loader.load_from_file(path, cache=True, unsafe=True):
                    variables = combine_vars(variables, new_data)

        return variables
