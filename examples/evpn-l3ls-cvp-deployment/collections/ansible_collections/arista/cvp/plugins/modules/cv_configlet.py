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

# Required by Ansible and CVP
import re
import traceback
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.arista.cvp.plugins.module_utils.cv_client import CvpClient
from ansible_collections.arista.cvp.plugins.module_utils.cv_client_errors import CvpLoginError, CvpApiError
from ansible.module_utils.connection import Connection, ConnectionError
from time import sleep
# Required by compare function
# FUZZYWUZZY_IMP_ERR = None
# try:
#     from fuzzywuzzy import fuzz  # Library that uses Levenshtein Distance to calculate the differences between strings.
#     HAS_FUZZYWUZZY = True
# except ImportError:
#     HAS_TREELIB = False
#     FUZZYWUZZY_IMP_ERR = traceback.format_exc()
DIFFLIB_IMP_ERR = None
try:
    import difflib
    HAS_DIFFLIB = True
except ImportError:
    HAS_DIFFLIB = False
    DIFFLIB_IMP_ERR = traceback.format_exc()


DOCUMENTATION = r'''
---
module: cv_configlet
version_added: "2.9"
author: EMEA AS Team (@aristanetworks)
short_description: Create, Delete, or Update CloudVision Portal Configlets.
description:
  - CloudVison Portal Configlet compares the list of configlets and config in
  - configlets against cvp-facts then adds, deletes, or updates
  - them as appropriate.
  - If a configlet is in cvp_facts but not in configlets it will be deleted.
  - If a configlet is in configlets but not in cvp_facts it will be created.
  - If a configlet is in both configlets and cvp_facts it configuration will
  - be compared and updated with the version in configlets
  - if the two are different.
options:
  configlets:
    description: List of configlets to managed on CVP server.
    required: true
    type: dict
  cvp_facts:
    description: Facts extracted from CVP servers using cv_facts module
    required: true
    type: dict
  configlet_filter:
    description: Filter to apply intended mode on a set of configlet.
                 If not used, then module only uses ADD mode. configlet_filter
                 list configlets that can be modified or deleted based
                 on configlets entries.
    required: false
    default: ['none']
    type: list
  state:
    description: 
        - If absent, configlets will be removed from CVP if they are not binded
        - to either a container or a device.
        - If present, configlets will be created or updated.
    required: false
    default: 'present'
    type: string
'''

EXAMPLES = r'''
---
- name: Test cv_configlet_v2
  hosts: cvp
  connection: local
  gather_facts: no
  vars:
    configlet_list:
      Test_Configlet: "! This is a Very First Testing Configlet\n!"
      Test_DYNAMIC_Configlet: "{{ lookup('file', 'templates/configlet_'+inventory_hostname+'.txt') }}"
  tasks:
    - name: 'Collecting facts from CVP {{inventory_hostname}}.'
      tags:
        - always
      cv_facts:
      register: cvp_facts

    - name: 'Create configlets on CVP {{inventory_hostname}}.'
      tags:
        - provision
      cv_configlet:
        cvp_facts: "{{cvp_facts.ansible_facts}}"
        configlets: "{{configlet_list}}"
        configlet_filter: ["New", "Test","base-chk","base-firewall"]
      register: cvp_configlet
'''


def compare(fromText, toText, lines=10):
    """ Compare text string in 'fromText' with 'toText' and produce
        diffRatio - a score as a float in the range [0, 1] 2.0*M / T
          T is the total number of elements in both sequences,
          M is the number of matches.
          Score - 1.0 if the sequences are identical, and 0.0 if they have nothing in common.
        unified diff list
          Code	Meaning
          '- '	line unique to sequence 1
          '+ '	line unique to sequence 2
          '  '	line common to both sequences
          '? '	line not present in either input sequence
    """
    fromlines = fromText.splitlines(1)
    tolines = toText.splitlines(1)
    diff = list(difflib.unified_diff(fromlines, tolines, n=lines))
    textComp = difflib.SequenceMatcher(None, fromText, toText)
    diffRatio = round(textComp.quick_ratio() * 100, 2)
    return [diffRatio, diff]


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


def configlet_action(module):
    ''' Compare configlets in "configlets" with configlets in "cvp_facts"
    if configlet exists in "cvp_facts" check config, if changed update
    if configlet does not exist in "cvp_facts" add to CVP
    if configlet in "cvp_facts" but not in "configlets" remove from CVP if
    not applied to a device or container.
    :param module: Ansible module with parameters and client connection.
    :return: data: dict of module actions and taskIDs
    '''
    # If any configlet changed updated 'changed' flag
    changed = False
    # Compare configlets against cvp_facts-configlets
    keep_configlet = []  # configlets with no changes
    delete_configlet = []  # configlets to delete from CVP
    deleted = []
    update_configlet = []  # configlets with config changes
    updated = []
    new_configlet = []  # configlets to add to CVP
    new = []
    taskList = []  # Tasks that have a pending status after function runs

    for configlet in module.params['cvp_facts']['configlets']:
        # Only deal with Static configlets not Configletbuilders or
        # their derived configlets
        # Include only configlets that match filter elements "all" will
        # include all configlets.
        if configlet['type'] == 'Static':
            if re.search(r"\ball\b", str(module.params['configlet_filter'])) or (
               any(element in configlet['name'] for element in module.params['configlet_filter'])):
                if configlet['name'] in module.params['configlets']:
                    if module.params['state'] == 'present':
                        ansible_configlet = module.params['configlets'][configlet['name']]
                        configlet_compare = compare(configlet['config'], ansible_configlet)
                        # compare function returns a floating point number
                        if configlet_compare[0] == 100.0:
                            keep_configlet.append(configlet)
                        else:
                            update_configlet.append({'data': configlet, 'config': ansible_configlet})
                    elif module.params['state'] == 'absent':
                        delete_configlet.append(configlet)
                else:
                    delete_configlet.append(configlet)
    # Look for new configlets, if a configlet is not CVP assume it is to be created
    for ansible_configlet in module.params['configlets']:
        found = False
        for cvp_configlet in module.params['cvp_facts']['configlets']:
            if str(ansible_configlet) == str(cvp_configlet['name']):
                found = True
        if not found:
            new_configlet.append({'name': str(ansible_configlet),
                                  'config': str(module.params['configlets'][ansible_configlet])})

    # Only execute this section if ansible check_mode is false
    if not module.check_mode:
        # delete any configlets as required
        if len(delete_configlet) > 0:
            for configlet in delete_configlet:
                try:
                    delete_resp = module.client.api.delete_configlet(configlet['name'], configlet['key'])
                except Exception as error:
                    errorMessage = re.split(':', str(error))[-1]
                    message = "Configlet %s cannot be deleted - %s" % (configlet['name'], errorMessage)
                    deleted.append({configlet['name']: message})
                else:
                    if "error" in str(delete_resp).lower():
                        message = "Configlet %s cannot be deleted - %s" % (configlet['name'], delete_resp['errorMessage'])
                        deleted.append({configlet['name']: message})
                    else:
                        changed = True
                        deleted.append({configlet['name']: "success"})

        # Update any configlets as required
        if len(update_configlet) > 0:
            for configlet in update_configlet:
                try:
                    update_resp = module.client.api.update_configlet(configlet['config'],
                                                                     configlet['data']['key'],
                                                                     configlet['data']['name'])
                except Exception as error:
                    errorMessage = re.split(':', str(error))[-1]
                    message = "Configlet %s cannot be updated - %s" % (configlet['name'], errorMessage)
                    updated.append({configlet['name']: message})
                else:
                    if "errorMessage" in str(update_resp):
                        message = "Configlet %s cannot be updated - %s" % (configlet['name'], update_resp['errorMessage'])
                        updated.append({configlet['data']['name']: message})
                    else:
                        module.client.api.add_note_to_configlet(configlet['data']['key'], "## Managed by Ansible ##")
                        changed = True
                        updated.append({configlet['data']['name']: "success"})

        # Add any new configlets as required
        if len(new_configlet) > 0:
            for configlet in new_configlet:
                try:
                    new_resp = module.client.api.add_configlet(configlet['name'], configlet['config'])
                except Exception as error:
                    errorMessage = re.split(':', str(error))[-1]
                    message = "Configlet %s cannot be created - %s" % (configlet['name'], errorMessage)
                    new.append({configlet['name']: message})
                else:
                    if "errorMessage" in str(new_resp):
                        message = "Configlet %s cannot be created - %s" % (configlet['name'], new_resp['errorMessage'])
                        new.append({configlet['name']: message})
                    else:
                        module.client.api.add_note_to_configlet(new_resp, "## Managed by Ansible ##")
                        changed = True
                        new.append({configlet['name']: "success"})

        # Get any Pending Tasks in CVP
        if changed:
            # Allow CVP to generate Tasks
            sleep(10)
            # Build required data for tasks in CVP - work order Id, current task status, name
            # description
            tasksField = {'workOrderId': 'workOrderId', 'workOrderState': 'workOrderState',
                          'currentTaskName': 'currentTaskName', 'description': 'description',
                          'workOrderUserDefinedStatus': 'workOrderUserDefinedStatus', 'note': 'note',
                          'taskStatus': 'taskStatus', 'workOrderDetails': 'workOrderDetails'}
            tasks = module.client.api.get_tasks_by_status('Pending')
            # Reduce task data to required fields
            for task in tasks:
                taskFacts = {}
                for field in task.keys():
                    if field in tasksField:
                        taskFacts[tasksField[field]] = task[field]
                taskList.append(taskFacts)
        data = {'new': new, 'updated': updated, 'deleted': deleted, 'tasks': taskList}
    else:
        for configlet in new_configlet:
            new.append({configlet['name']: "checked"})
        for configlet in update_configlet:
            updated.append({configlet['data']['name']: "checked"})
        for configlet in delete_configlet:
            deleted.append({configlet['name']: "checked"})
        data = {'new': new, 'updated': updated, 'deleted': deleted, 'tasks': taskList}
    return [changed, data]


def main():
    """ main entry point for module execution
    """
    argument_spec = dict(
        configlets=dict(type='dict', required=True),
        cvp_facts=dict(type='dict', required=True),
        configlet_filter=dict(type='list', default='none'),
        state=dict(type='str',
                   choices=['present', 'absent'],
                   default='present',
                   required=False))

    module = AnsibleModule(argument_spec=argument_spec,
                           supports_check_mode=True)

    if not HAS_DIFFLIB:
        module.fail_json(msg='difflib required for this module')

    result = dict(changed=False, data={})
    messages = dict(issues=False)
    # Connect to CVP instance
    module.client = connect(module)

    # Pass module params to configlet_action to act on configlet
    result['changed'], result['data'] = configlet_action(module)
    module.exit_json(**result)


if __name__ == '__main__':
    main()
