from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.action.include_vars import ActionModule as IncludeVarsActionModule


class ActionModule(IncludeVarsActionModule):
    '''
    This class is wrapping the builtin action plugin "include_vars" 1:1.
    We need this to avoid the Ansible behavior of injecting variables from
    "include_vars" with special precedence.

    Since Ansible uses the task name (fqcn) to detect if it is "include_vars"
    or some other module returning "ansible_facts", we only need to provide
    a different name, to avoid the builtin behavior.

    If we did not have this, we would have no way of overriding included_vars
    with structured_config or the automatic input variable conversion.

    Ref. https://github.com/ansible/ansible/blob/v2.13.3/lib/ansible/plugins/strategy/__init__.py#L738
    '''
    def run(self, tmp=None, task_vars=None):
        return super().run(tmp, task_vars)
