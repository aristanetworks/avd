#!/usr/bin/python
# coding: utf-8 -*-
#
# FIXME: required to pass ansible-test
# GNU General Public License v3.0+
#
# Copyright 2019 Arista Networks AS-EMEA
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {
    'metadata_version': '1.0',
    'status': ['preview'],
    'supported_by': 'community'
}

import time
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection, ConnectionError
from ansible_collections.arista.cvp.plugins.module_utils.cv_client import CvpClient
from ansible_collections.arista.cvp.plugins.module_utils.cv_client_errors import CvpLoginError, CvpApiError

DOCUMENTATION = r'''
---
module: cv_task
version_added: "2.9"
author: EMEA AS Team (@aristanetworks)
short_description: Execute or Cancel CVP Tasks.
description: CloudVison Portal Task module
options:
  tasks:
    description: CVP taskIDs to act on
    required: True
    type: list
  wait:
    description: Time to wait for tasks to transition to 'Completed'
    required: False
    default: 0
    type: int
  state:
    description: action to carry out on the task
                 executed - execute tasks
                 cancelled - cancel tasks
    required: false
    default: executed
    type: str
    choices:
      - executed
      - cancelled
'''

EXAMPLES = '''
---
- name: Execute all tasks registered in cvp_configlets variable
  arista.cvp.cv_task:
    tasks: "{{ cvp_configlets.data.tasks }}"

- name: Cancel a list of pending tasks
  arista.cvp.cv_task:
    tasks: "{{ cvp_configlets.data.tasks }}"
    state: cancelled

# Execute all pending tasks and wait for completion for 60 seconds
# In order to get a list of all pending tasks, execute cv_facts first
- name: Update cvp facts
  arista.cvp.cv_facts:

- name: Execute all pending tasks and wait for completion for 60 seconds
  arista.cvp.cv_task:
    port: '{{cvp_port}}'
    tasks: "{{ tasks }}"
    wait: 60
'''


def connect(module):
    ''' Connects to CVP device using user provided credentials from playbook.
    :param module: Ansible module with parameters and client connection.
    :return: CvpClient object with connection instantiated.
    '''
    client = CvpClient()
    connection = Connection(module._socket_path)
    host = connection.get_option("host")
    port = connection.get_option("port")
    user = connection.get_option("remote_user")
    pswd = connection.get_option("password")
    try:
        client.connect([host],
                       user,
                       pswd,
                       protocol="https",
                       port=port,
                       )
    except CvpLoginError as e:
        module.fail_json(msg=str(e))

    return client


def get_id(task):
    return task.get("workOrderId")


def get_state(task):
    return task.get("workOrderUserDefinedStatus")


def execute_task(cvp, task_id):
    return cvp.execute_task(task_id)


def cancel_task(cvp, task_id):
    return cvp.cancel_task(task_id)


def apply_state(cvp, task, state):
    cvp.add_note_to_task(get_id(task), "Executed by Ansible")
    if state == "executed":
        return execute_task(cvp, get_id(task))
    elif state == "cancelled":
        return cancel_task(cvp, get_id(task))


def actionable(state):
    return state in ["Pending"]


def terminal(state):
    return state in ["Completed", "Cancelled"]


def state_is_different(task, target):
    return get_state(task) != target


def update_all_tasks(cvp, data):
    new_data = dict()
    for task_id in data.keys():
        new_data[task_id] = cvp.get_task_by_id(task_id)
    return new_data


def task_action(module):
    '''
    TODO.
    '''
    changed = False
    data = dict()
    warnings = list()

    tasks = module.params['tasks']
    state = module.params['state']
    wait = module.params['wait']
    cvp = module.client.api

    actionable_tasks = [t for t in tasks if actionable(get_state(t))]

    if len(actionable_tasks) == 0:
        warnings.append("No actionable tasks found on CVP")
        return changed, data, warnings

    for task in actionable_tasks:
        if state_is_different(task, state):
            apply_state(cvp, task, state)
            changed = True
            data[get_id(task)] = task

    start = time.time()
    now = time.time()
    while (now - start) < wait:
        data = update_all_tasks(cvp, data)
        if all([terminal(get_state(t)) for t in data.values()]):
            break
        now = time.time()

    if wait:
        for i, task in data.items():
            if not terminal(get_state(task)):
                warnings.append("Task {0} has not completed in {1} seconds".format(i, wait))

    return changed, data, warnings


def main():
    """ main entry point for module execution
    """
    argument_spec = dict(
        tasks=dict(required=True, type='list'),
        wait=dict(default=0, type='int'),
        state=dict(default='executed', choices=['executed', 'cancelled']))

    module = AnsibleModule(argument_spec=argument_spec,
                           supports_check_mode=False)

    result = dict(changed=False)

    # Connect to CVP instance
    module.client = connect(module)

    result['changed'], result['data'], warnings = task_action(module)

    if warnings:
        [module.warn(w) for w in warnings]

    module.exit_json(**result)


if __name__ == '__main__':
    main()
