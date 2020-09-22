#!/usr/bin/python
# -*- coding: utf-8 -*-
#
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

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.0.0',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = r'''
---
module: inventory_to_container
version_added: "2.9"
author: Ansible Arista Team (@aristanetworks)
short_description: Transform information from inventory to arista.cvp collection
description:
  - Transform information from ansible inventory to be able to
  - provision CloudVision Platform using arista.cvp collection and
  - its specific data structure.
options:
  inventory:
    description: YAML inventory file
    required: true
    type: str
  container_root:
    description: Ansible group name to consider to be Root of our topology.
    required: true
    type: str
  configlet_dir:
    description: Directory where intended configurations are located.
    required: false
    type: str
  configlet_prefix:
    description: Prefix to put on configlet.
    required: false
    type: str
  destination:
    description: Optional path to save variable.
    required: false
    type: str
  device_filter:
    description: Filter to apply intended mode on a set of configlet.
                 If not used, then module only uses ADD mode. device_filter
                 list devices that can be modified or deleted based
                 on configlets entries.
    required: false
    default: ['all']
    type: list
'''

EXAMPLES = r'''
- name: generate intented variables
  inventory_to_container:
    inventory: 'inventory.yml'
    container_root: 'DC1_FABRIC'
    configlet_dir: 'intended_configs'
    configlet_prefix: 'AVD'
    device_filter: ['DC1-LE']
    # destination: 'generated_vars/{{inventory_hostname}}.yml'
  register: CVP_VARS

- name: 'Collecting facts from CVP {{inventory_hostname}}.'
  arista.cvp.cv_facts:
  register: CVP_FACTS

- name: 'Create configlets on CVP {{inventory_hostname}}.'
  arista.cvp.cv_configlet:
    cvp_facts: "{{CVP_FACTS.ansible_facts}}"
    configlets: "{{CVP_VARS.CVP_CONFIGLETS}}"
    configlet_filter: ["AVD"]

- name: "Building Container topology on {{inventory_hostname}}"
  arista.cvp.cv_container:
    topology: '{{CVP_VARS.CVP_TOPOLOGY}}'
    cvp_facts: '{{CVP_FACTS.ansible_facts}}'
    save_topology: true
'''

import glob
import os
import traceback
from ansible.module_utils.basic import AnsibleModule
TREELIB_IMP_ERR = None
try:
    from treelib import Tree
    HAS_TREELIB = True
except ImportError:
    HAS_TREELIB = False
    TREELIB_IMP_ERR = traceback.format_exc()
YAML_IMP_ERR = None
try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False
    YAML_IMP_ERR = traceback.format_exc()


# Root container on CloudVision.
# Shall not be changed unless CloudVision changes it in the core.
CVP_ROOT_CONTAINER = 'Tenant'


def is_in_filter(hostname_filter=None, hostname="eos"):
    """
    Check if device is part of the filter or not.

    Parameters
    ----------
    hostname_filter : list, optional
        Device filter, by default ['all']
    hostname : str
        Device hostname to compare against filter.

    Returns
    -------
    boolean
        True if device hostname is part of filter. False if not.
    """

    # W102 Workaround to avoid list as default value.
    if hostname_filter is None:
        hostname_filter = ["all"]

    if "all" in hostname_filter:
        return True
    elif any(element in hostname for element in hostname_filter):
        return True
    return False


def isIterable(testing_object=None):
    """
    Test if an object is iterable or not.

    Test if an object is iterable or not. If yes return True, else return False.

    Parameters
    ----------
    testing_object : any, optional
        Object to test if it is iterable or not, by default None
    """
    try:
        some_object_iterator = iter(testing_object)  # noqa # pylint: disable=unused-variable
        return True
    except TypeError as te:  # noqa # pylint: disable=unused-variable
        return False


def isLeaf(tree, nid):
    """
    Test if NodeID is a leaf with no nid attached to it.

    Parameters
    ----------
    tree : treelib.Tree
        Tree where NID is defined.
    nid : treelib.Node
        NodeID to test.

    Returns
    -------
    boolean
        True if node is a leaf, false in other situation
    """
    if len(tree.is_branch(nid)) == 0:
        return True
    else:
        return False


def get_configlet(src_folder=str(), prefix='AVD', extension='cfg', device_filter=None):
    """
    Get available configlets to deploy to CVP.

    Parameters
    ----------
    src_folder : str, optional
        Path where to find configlet, by default str()
    prefix : str, optional
        Prefix to append to configlet name, by default 'AVD'
    extension : str, optional
        File extension to lookup configlet file, by default 'cfg'
    device_filter: list, optional
        List of filter to compare device configlet and to select only a subset of configlet.

    Returns
    -------
    dict
        Dictionary of configlets found in source folder.
    """
    # W102 Workaround to avoid list as default value.
    if device_filter is None:
        device_filter = ["all"]

    src_configlets = glob.glob(src_folder + '/*.' + extension)
    configlets = dict()
    for file in src_configlets:
        # Build structure only if configlet match device_filter.
        if is_in_filter(hostname=os.path.splitext(os.path.basename(file))[0], hostname_filter=device_filter):
            if prefix != 'none':
                name = prefix + '_' + os.path.splitext(os.path.basename(file))[0]
            else:
                name = os.path.splitext(os.path.basename(file))[0]
            with open(file, 'r') as file:
                data = file.read()
            configlets[name] = data
    return configlets


def serialize(dict_inventory, parent_container=None, tree_topology=None):
    """
    Build a tree topology from inventory.

    Parameters
    ----------
    dict_inventory : dict
        Inventory YAML content.
    parent_container : str, optional
        Registration of container N-1 for recursive function, by default None
    tree_topology : treelib.Tree, optional
        Tree topology built over iteration, by default None

    Returns
    -------
    treelib.Tree
        complete container tree topology.
    """
    if isIterable(dict_inventory):
        # Working with ROOT container for Fabric
        if tree_topology is None:
            # initiate tree topology and add ROOT under Tenant
            tree_topology = Tree()
            tree_topology.create_node("Tenant", "Tenant")
            parent_container = 'Tenant'

        # Recursive Inventory read
        for k1, v1 in dict_inventory.items():
            # Read a leaf
            if isIterable(v1) and 'children' not in v1:
                tree_topology.create_node(k1, k1, parent=parent_container)
            # If subgroup has kids
            if isIterable(v1) and 'children' in v1:
                tree_topology.create_node(k1, k1, parent=parent_container)
                serialize(
                    dict_inventory=v1['children'],
                    parent_container=k1,
                    tree_topology=tree_topology
                )
            elif k1 == 'children' and isIterable(v1):
                # Extract sub-group information
                for k2, v2 in v1.items():
                    # Add subgroup to tree
                    tree_topology.create_node(k2, k2, parent=parent_container)
                    serialize(
                        dict_inventory=v2,
                        parent_container=k2,
                        tree_topology=tree_topology
                    )
        return tree_topology


def get_devices(dict_inventory, search_container=None, devices=None, device_filter=None):
    """
    Get devices attached to a container.

    Parameters
    ----------
    dict_inventory : dict
        Inventory YAML content.
    search_container : str, optional
        Container to look for, by default None
    devices : str, optional
        List of found devices attached to container, by default list()
    device_filter: list, optional
        List of filter to compare device name and to select only a subset of devices.

    Returns
    -------
    list
        List of found devices.
    """
    # W102 Workaround to avoid list as default value.
    if device_filter is None:
        device_filter = ["all"]

    for k1, v1 in dict_inventory.items():
        # Read a leaf
        if k1 == search_container and 'hosts' in v1:
            for dev, data in v1['hosts'].items():
                if is_in_filter(
                    hostname_filter=device_filter,
                    hostname=dev
                ):
                    devices.append(dev)
        # If subgroup has kids
        if isIterable(v1) and 'children' in v1:
            get_devices(
                dict_inventory=v1['children'],
                search_container=search_container,
                devices=devices,
                device_filter=device_filter
            )
        elif k1 == 'children' and isIterable(v1):
            # Extract sub-group information
            for k2, v2 in v1.items():
                get_devices(
                    dict_inventory=v2,
                    search_container=search_container,
                    devices=devices,
                    device_filter=device_filter
                )
    return devices


def get_containers(inventory_content, parent_container, module):
    """
    get_containers - Build Container topology to build on CoudVision.

    Parameters
    ----------
    inventory_content : dict
        Inventory loaded using a YAML input.
    parent_container : string
        Root of tree lookup
    module : AnsibleModule
        Ansible Module

    Returns
    -------
    JSON
        CVP Container structure to use with cv_container.
    """
    serialized_inventory = serialize(dict_inventory=inventory_content)
    tree_dc = serialized_inventory.subtree(parent_container)
    container_list = [tree_dc[node].tag for node in tree_dc.expand_tree()]
    container_json = {}
    for container in container_list:
        data = dict()
        if container != CVP_ROOT_CONTAINER:
            parent = tree_dc.parent(container)
            if container == parent_container:
                data['parent_container'] = CVP_ROOT_CONTAINER
            elif parent.tag != CVP_ROOT_CONTAINER:
                if isLeaf(tree=tree_dc, nid=container):
                    devices = get_devices(dict_inventory=inventory_content,
                                          search_container=container,
                                          devices=list(),
                                          device_filter=module.params['device_filter'])
                    data['devices'] = devices
                data['parent_container'] = parent.tag
            container_json[container] = data
    return container_json


def main():
    """ Main entry point for module execution."""
    argument_spec = dict(
        inventory=dict(type='str', required=True),
        container_root=dict(type='str', required=True),
        configlet_dir=dict(type='str', required=False),
        configlet_prefix=dict(type='str', required=False),
        destination=dict(type='str', required=False),
        device_filter=dict(type="list", default="all")
    )

    module = AnsibleModule(argument_spec=argument_spec,
                           supports_check_mode=False)
    result = dict(changed=False)

    # Build cv_container structure from YAML inventory.
    if (module.params['inventory'] is not None and
            module.params['container_root'] is not None):
        # "ansible-avd/examples/evpn-l3ls-cvp-deployment/inventory.yml"
        inventory_file = module.params['inventory']
        parent_container = module.params['container_root']
        # Build containers & devices topology
        inventory_content = str()
        with open(inventory_file, 'r') as stream:
            try:
                inventory_content = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
        result['CVP_TOPOLOGY'] = get_containers(inventory_content=inventory_content,
                                                parent_container=parent_container,
                                                module=module)

    # If set, build configlet topology
    if module.params['configlet_dir'] is not None:
        result['CVP_CONFIGLETS'] = get_configlet(src_folder=module.params['configlet_dir'],
                                                 prefix=module.params['configlet_prefix'],
                                                 device_filter=module.params['device_filter'])

    # Write vars to file if set by user
    if module.params['destination'] is not None:
        with open(module.params['destination'], 'w') as file:
            yaml.dump(result, file)

    module.exit_json(**result)


if __name__ == '__main__':
    main()
