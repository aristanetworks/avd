from __future__ import absolute_import, division, print_function

__metaclass__ = type

from collections import ChainMap
from concurrent.futures import ProcessPoolExecutor
from itertools import repeat
from multiprocessing import get_context
from os import open as os_open

from ansible.errors import AnsibleActionFail
from ansible.plugins.action import ActionBase, display

from ansible_collections.arista.avd.plugins.plugin_utils.utils import get_templar, template


def opener(path, flags):
    return os_open(path, flags, 0o664)


def _template_process(item, task_vars, templatefile, dest_format_str, templar):
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

        result = super().run(tmp, task_vars)
        del tmp  # tmp no longer has any effect

        # Validate Arguments
        templatefile = self._task.args["template"]
        if not isinstance(templatefile, str):
            raise AnsibleActionFail("The argument 'template' must be a string")

        items = self._task.args.get("items")
        if not isinstance(items, list):
            raise AnsibleActionFail("The argument 'items' must be a list")

        dest_format_str = self._task.args.get("dest_format_str")
        if not isinstance(dest_format_str, str):
            raise AnsibleActionFail("The argument 'dest_format_str' must be a string")

        forks = task_vars["ansible_forks"]

        # Get updated templar instance to be passed along to our simplified "templater"
        templar = get_templar(self, task_vars)

        context = get_context("fork")
        with ProcessPoolExecutor(max_workers=forks, mp_context=context) as executor:
            return_values = executor.map(
                _template_process,
                items,
                repeat(task_vars),
                repeat(templatefile),
                repeat(dest_format_str),
                repeat(templar),
            )

        for return_value in return_values:
            if isinstance(return_value, Exception):
                display.error(return_value)
                result["failed"] = True

        return result
