from ansible.plugins.action import ActionBase
from ansible.template import Templar

from .compile_searchpath import compile_searchpath


def get_templar(action_plugin_instance: ActionBase, task_vars: dict) -> Templar:
    """
    Return a new instance of Ansible Templar Class based on the
    "._templar" from the given action_plugin_instance.
    The new instance is loaded with new searchpath based on
    ".ansible_search_path" from the given task_vars.
    """
    return action_plugin_instance._templar.copy_with_new_env(
        searchpath=compile_searchpath(task_vars.get("ansible_search_path", [])),
    )
