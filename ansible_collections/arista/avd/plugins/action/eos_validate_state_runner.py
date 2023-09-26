# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import absolute_import, division, print_function

__metaclass__ = type

import logging

from ansible.errors import AnsibleActionFail
from ansible.plugins.action import ActionBase, display

from ansible_collections.arista.avd.plugins.plugin_utils.eos_validate_state_utils import get_anta_results
from ansible_collections.arista.avd.plugins.plugin_utils.utils import PythonToAnsibleContextFilter, PythonToAnsibleHandler

LOGGER = logging.getLogger("ansible_collections.arista.avd")
# ANTA 0.8.0 currently add some RichHandler to the root logger so need to disable propagation
LOGGER.propagate = False


class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        self._supports_check_mode = True

        if task_vars is None:
            task_vars = {}

        validation_result, new_module_args = self.validate_argument_spec(
            argument_spec={
                "logging_level": {"type": "str", "default": "WARNING"},
                "save_catalog": {"type": "bool", "defaut": False},
                "device_catalog_output_dir": {"type": "str"},
                "skipped_tests": {"type": "dict"},
            },
            required_if=[("save_catalog", True, ["device_catalog_output_dir"])],
        )

        result = super().run(tmp, task_vars)
        del tmp  # tmp no longer has any effect

        hostname = task_vars["inventory_hostname"]
        ansible_connection = self._connection

        # Handle logging
        setup_module_logging(hostname, result)

        # Get task arguments
        logging_level = new_module_args["logging_level"]
        save_catalog = new_module_args["save_catalog"]
        skipped_tests = new_module_args.get("skipped_tests", {})
        if save_catalog is True:
            eos_validate_state_dir = new_module_args["device_catalog_output_dir"]
            save_catalog_name = f"{eos_validate_state_dir}/{hostname}-catalog.yml"
        else:
            save_catalog_name = None

        # If we are running this task, it means "anta" is present in `ansible_run_tags`
        ansible_tags = {
            "ansible_run_tags": [tag for tag in task_vars.get("ansible_run_tags", []) if tag != "anta"],
            "ansible_skip_tags": task_vars.get("ansible_skip_tags", []),
        }

        # This is not all the hostvars, but just the Ansible Hostvars Manager object where we can retrieve hostvars for each host on-demand.
        hostvars = task_vars["hostvars"]

        try:
            anta_results = get_anta_results(
                device_name=hostname,
                hostvars=hostvars,
                connection=ansible_connection,
                logging_level=logging_level,
                skipped_tests=skipped_tests,
                ansible_tags=ansible_tags,
                save_catalog_name=save_catalog_name,
                # This convert Ansible Check Mode to dry_run
                dry_run=self._play_context.check_mode,
            )
        except Exception as error:
            raise AnsibleActionFail(message=str(error)) from error

        result["results"] = anta_results

        return result


def setup_module_logging(hostname: str, result: dict) -> None:
    """
    Create a Filter to add the hostname to generate logs,
    Add a Handler to copy the logs from the plugin into Ansible output based on their level

    Args:
      hostname (str): Current Inventory device being used to augment the logs with <hostname>
      result (dict): The ansible dictionary used for the results
    """
    python_to_ansible_filter = PythonToAnsibleContextFilter(hostname)
    python_to_ansible_handler = PythonToAnsibleHandler(result, display)
    python_to_ansible_handler.addFilter(python_to_ansible_filter)
    LOGGER.addHandler(python_to_ansible_handler)
    # TODO mechanism to manipulate the logger globally for pyavd
    # Keep debug to be able to see logs with `-v` and `-vvv`
    LOGGER.setLevel(logging.DEBUG)
