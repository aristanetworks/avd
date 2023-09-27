# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import absolute_import, division, print_function

__metaclass__ = type

from collections import ChainMap
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import get_context
from os import open as os_open

from ansible.errors import AnsibleActionFail
from ansible.plugins.action import ActionBase, display

from ansible_collections.arista.avd.plugins.plugin_utils.utils import get_templar, template

# Leveraging copy on write from fork
GLOBALS = {}


def opener(path, flags):
    return os_open(path, flags, 0o664)


# def _template_process(item: str, task_vars: dict, templatefile: str, dest_format_str: str, templar) -> dict:
def _template_process(item: str) -> dict:
    """
    This function runs as a separate fork.

    Perform Jinja templating and write output to a file.

    Parameters
    ----------
    item : str
        One string from the list of strings given to the module. Could be used as key in the template.
        Also used to build destination filename
    task_vars : dict
        Ansible task vars
    templatefile : str
        Filename of template file
    dest_format_str : str
        Format string used to build destination filename inserting item value
    templar : object
        Instance of Ansible templar

    Returns
    -------
    dict
        Ansible result dictionary with any errors caught during writing of the output file.
    """
    dest_format_str = GLOBALS["dest_format_str"]
    task_vars = GLOBALS["task_vars"]
    templatefile = GLOBALS["templatefile"]
    templar = GLOBALS["templar"]
    dest = str(dest_format_str).format(item=item)

    template_vars = ChainMap({"item": item}, task_vars)
    output = template(templatefile, template_vars, templar)

    result = {}
    try:
        with open(dest, "w", encoding="UTF-8", opener=opener) as file:
            file.write(output)
    except Exception as e:
        result["failed"] = True
        result["msg"] = str(e)
        result["exception"] = e

    return result


class ActionModule(ActionBase):
    """
    Arguments:
        template:
            Path to jinja2 template used for all items
        items:
            List of strings. Each list item is passed to 'dest_format_string' as 'item' and passed to templater as 'item'
        dest_format_str:
            Format string used to specify target file for each item. 'item' is the current item from 'items'
            Example: "mypath/{item}.md"
    """

    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = {}

        GLOBALS["task_vars"] = task_vars

        result = super().run(tmp, task_vars)
        del tmp  # tmp no longer has any effect

        # Validate Arguments
        templatefile = self._task.args["template"]
        if not isinstance(templatefile, str):
            raise AnsibleActionFail("The argument 'template' must be a string")
        GLOBALS["templatefile"] = templatefile

        items = self._task.args.get("items")
        if not isinstance(items, list):
            raise AnsibleActionFail("The argument 'items' must be a list")

        dest_format_str = self._task.args.get("dest_format_str")
        if not isinstance(dest_format_str, str):
            raise AnsibleActionFail("The argument 'dest_format_str' must be a string")
        GLOBALS["dest_format_str"] = dest_format_str

        forks = task_vars["ansible_forks"]

        # Get updated templar instance to be passed along to our simplified "templater"
        templar = get_templar(self, task_vars)
        GLOBALS["templar"] = templar

        context = get_context("fork")
        with ProcessPoolExecutor(max_workers=forks, mp_context=context) as executor:
            return_values = executor.map(
                _template_process,
                items,
            )

        for return_value in return_values:
            if isinstance(return_value, Exception):
                display.error(return_value)
                result["failed"] = True

        return result
