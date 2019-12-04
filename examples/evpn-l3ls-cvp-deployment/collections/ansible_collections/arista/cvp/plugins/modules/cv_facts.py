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

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection, ConnectionError
from ansible_collections.arista.cvp.plugins.module_utils.cv_client import CvpClient
from ansible_collections.arista.cvp.plugins.module_utils.cv_client_errors import CvpLoginError, CvpApiError

DOCUMENTATION = r'''
---
module: cv_facts
version_added: "2.9"
author: EMEA AS Team (@aristanetworks)
short_description: Collect facts from CloudVision Portal.
description:
  - Returns the list of devices, configlets, containers and images
'''

EXAMPLES = r'''
---
    # Collect CVP Facts as init process
- name: "Gather CVP facts from {{inventory_hostname}}"
  arista.cvp.cv_facts:
  register: cvp_facts

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


def cv_facts(module):
    ''' Connects to CVP device using user provided credentials from module.
    :param module: Ansible module with parameters and client connection.
    :return: CvpClient object with connection instantiated.
    '''
    facts = {}
    # Get version data for CVP
    facts['cvp_info'] = module.client.api.get_cvp_info()

    # Build required data for devices in CVP - Device Data, Config, Associated Container,
    # Associated Images, and Associated Configlets
    deviceField = {'hostname': 'name', 'fqdn': 'fqdn', 'complianceCode': 'complianceCode',
                   'complianceIndication': 'complianceIndication', 'version': 'version',
                   'ipAddress': 'ipAddress', 'systemMacAddress': 'key',
                   'parentContainerKey': 'parentContainerKey',
                   'streamingStatus': 'streamingStatus'}
    facts['devices'] = []

    # Get Inventory Data for All Devices
    inventory = module.client.api.get_inventory()
    # Reduce device data to required fields
    for device in inventory:
        deviceFacts = {}
        for field in device.keys():
            if field in deviceField:
                deviceFacts[deviceField[field]] = device[field]
        facts['devices'].append(deviceFacts)

    # Work through Devices list adding device specific information
    for device in facts['devices']:
        # Add designed config for device
        if device['streamingStatus'] == "active":
            device['config'] = module.client.api.get_device_configuration(device['key'])
        # Add parent container name
        container = module.client.api.get_container_by_id(device['parentContainerKey'])
        device['parentContainerName'] = container['name']
        # Add Device Specific Configlets
        configlets = module.client.api.get_configlets_by_device_id(device['key'])
        device['deviceSpecificConfiglets'] = []
        for configlet in configlets:
            if int(configlet['containerCount']) == 0:
                device['deviceSpecificConfiglets'].append(configlet['name'])
        # Add ImageBundle Info
        device['imageBundle'] = ""
        deviceInfo = module.client.api.get_net_element_info_by_device_id(device['key'])
        if "imageBundleMapper" in deviceInfo:
            # There should only be one ImageBudle but its id is not decernable
            # If the Image is applied directly to the device its type will be 'netelement'
            if len(deviceInfo['imageBundleMapper'].values()) > 0:
                if deviceInfo['imageBundleMapper'].values()[0]['type'] == 'netelement':
                    device['imageBundle'] = deviceInfo['bundleName']

    # Build required data for configlets in CVP - Configlet Name, Config, Associated Containers,
    # Associated Devices, and Configlet Type
    configletField = {'name': 'name', 'config': 'config', 'type': 'type', 'key': 'key'}
    facts['configlets'] = []

    # Get List of all configlets
    configlets = module.client.api.get_configlets()['data']
    # Reduce configlet data to required fields
    for configlet in configlets:
        configletFacts = {}
        for field in configlet.keys():
            if field in configletField:
                configletFacts[configletField[field]] = configlet[field]
        facts['configlets'].append(configletFacts)

    # Work through Configlet list adding Configlet specific information
    for configlet in facts['configlets']:
        # Add applied Devices
        configlet['devices'] = []
        applied_devices = module.client.api.get_devices_by_configlet(configlet['name'])
        for device in applied_devices['data']:
            configlet['devices'].append(device['hostName'])
        # Add applied Containers
        configlet['containers'] = []
        applied_containers = module.client.api.get_containers_by_configlet(configlet['name'])
        for container in applied_containers['data']:
            configlet['containers'].append(container['containerName'])

    # Build required data for containers in CVP - Container Name, parent container, Associated Configlets
    # Associated Devices, and Child Containers
    containerField = {'name': 'name', 'parentName': 'parentName', 'childContainerId': 'childContainerKey',
                      'key': 'key'}
    facts['containers'] = []

    # Get List of all Containers
    containers = module.client.api.get_containers()['data']
    # Reduce container data to required fields
    for container in containers:
        containerFacts = {}
        for field in container.keys():
            if field in containerField:
                containerFacts[containerField[field]] = container[field]
        facts['containers'].append(containerFacts)

    # Work through Container list adding Container specific information
    for container in facts['containers']:
        # Add applied Devices
        container['devices'] = []
        applied_devices = module.client.api.get_devices_by_container_id(container['key'])
        for device in applied_devices:
            container['devices'].append(device['fqdn'])
        # Add applied Configlets
        container['configlets'] = []
        applied_configlets = module.client.api.get_configlets_by_container_id(container['key'])['configletList']
        for configlet in applied_configlets:
            container['configlets'].append(configlet['name'])
        # Add applied Images
        container['imageBundle'] = ""
        applied_images = module.client.api.get_image_bundle_by_container_id(container['key'])['imageBundleList']
        if len(applied_images) > 0:
            container['imageBundle'] = applied_images[0]['name']

    # Build required data for images in CVP - Image Name, certified, Image Components
    imageField = {'name': 'name', 'isCertifiedImageBundle': 'certifified', 'imageIds': 'imageNames', 'key': 'key'}
    facts['imageBundles'] = []

    # Get List of all Image Bundles
    imageBundles = module.client.api.get_image_bundles()['data']
    # Reduce image data to required fields
    for imageBundle in imageBundles:
        imageBundleFacts = {}
        for field in imageBundle.keys():
            if field in imageField:
                imageBundleFacts[imageField[field]] = imageBundle[field]
        facts['imageBundles'].append(imageBundleFacts)

    # Build required data for tasks in CVP - work order Id, current task status, name
    # description
    tasksField = {'name': 'name', 'workOrderId': 'taskNo', 'workOrderState': 'status',
                  'currentTaskName': 'currentAction', 'description': 'description',
                  'workOrderUserDefinedStatus': 'displayedStutus', 'note': 'note',
                  'taskStatus': 'actionStatus'}
    facts['tasks'] = []

    # Get List of all Tasks
    tasks = module.client.api.get_tasks()['data']
    # Reduce task data to required fields
    for task in tasks:
        taskFacts = {}
        for field in task.keys():
            if field in tasksField:
                taskFacts[tasksField[field]] = task[field]
        facts['tasks'].append(taskFacts)

    return facts


def main():
    """ main entry point for module execution
    """
    argument_spec = dict()
    module = AnsibleModule(argument_spec=argument_spec,
                           supports_check_mode=True)

    result = dict(changed=False, ansible_facts={})

    module.client = connect(module)

    result['ansible_facts'] = cv_facts(module)
    result['changed'] = False

    module.exit_json(**result)


if __name__ == '__main__':
    main()
