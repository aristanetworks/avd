#!/usr/bin/env python
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

''' Class containing calls to CVP RESTful API.
'''
import os
# This import is for proper file IO handling support for both Python 2 and 3
# pylint: disable=redefined-builtin
from io import open

from ansible_collections.arista.cvp.plugins.module_utils.cv_client_errors import CvpApiError

try:
    from urllib import quote_plus as qplus
except (AttributeError, ImportError):
    from urllib.parse import quote_plus as qplus


class CvpApi(object):
    ''' CvpApi class contains calls to CVP 2018.2.x RESTful API.  The RESTful API
        parameters are passed in as parameters to the method.  The results of
        the RESTful API call are converted from json to a dict and returned.
        Where needed minimal processing is performed on the results.
        Any method that does a cv_client get or post call could raise the
        following errors:

        ConnectionError: A ConnectionError is raised if there was a network
            problem (e.g. DNS failure, refused connection, etc)
        CvpApiError: A CvpApiError is raised if there was a JSON error.
        CvpRequestError: A CvpRequestError is raised if the request is not
            properly constructed.
        CvpSessionLogOutError: A CvpSessionLogOutError is raised if
            reponse from server indicates session was logged out.
        HTTPError: A HTTPError is raised if there was an invalid HTTP response.
        ReadTimeout: A ReadTimeout is raised if there was a request
            timeout when reading from the connection.
        Timeout: A Timeout is raised if there was a request timeout.
        TooManyRedirects: A TooManyRedirects is raised if the request exceeds
            the configured number of maximum redirections
        ValueError: A ValueError is raised when there is no valid
            CVP session.  This occurs because the previous get or post request
            failed and no session could be established to a CVP node.  Destroy
            the class and re-instantiate.
    '''
    # pylint: disable=too-many-public-methods
    # pylint: disable=too-many-lines

    def __init__(self, clnt, request_timeout=30):
        ''' Initialize the class.

            Args:
                clnt (obj): A CvpClient object
        '''
        self.clnt = clnt
        self.log = clnt.log
        self.request_timeout = request_timeout

    def get_cvp_info(self):
        ''' Returns information about CVP.

            Returns:
                cvp_info (dict): CVP Information
        '''
        data = self.clnt.get('/cvpInfo/getCvpInfo.do',
                             timeout=self.request_timeout)
        return data

    # ~Device Related API Calls

    def get_inventory(self, start=0, end=0, provisioned="true", query=None):
        ''' Returns the a dict of the net elements known to CVP.

            Args:
                start (int): The first inventory entry to return.  Default is 0
                end (int): The last inventory entry to return.  Default is 0
                    which means to return all inventory entries.  Can be a
                    large number to indicate the last inventory entry.
                query (string): A value that can be used as a match to filter
                    returned inventory list. For example get all switches that
                    are running a specific version of EOS.
        '''
        self.log.debug('get_inventory: called')
        self.log.debug('2018 Inventory API Call')
        data = self.clnt.get('/inventory/devices?provisioned=%s' % provisioned,
                             timeout=self.request_timeout)
        for dev in data:
            dev['key'] = dev['systemMacAddress']
            dev['deviceInfo'] = dev['deviceStatus'] = dev['status']
            dev['isMLAGEnabled'] = dev['mlagEnabled']
            dev['isDANZEnabled'] = dev['danzEnabled']
            dev['parentContainerId'] = dev['parentContainerKey']
            dev['bootupTimeStamp'] = dev['bootupTimestamp']
            dev['internalBuildId'] = dev['internalBuild']
            if 'taskIdList' not in dev:
                dev['taskIdList'] = []
            if 'tempAction' not in dev:
                dev['tempAction'] = None
            dev['memTotal'] = 0
            dev['memFree'] = 0
            dev['sslConfigAvailable'] = False
            dev['sslEnabledByCVP'] = False
            dev['lastSyncUp'] = 0
            dev['type'] = 'netelement'
            dev['dcaKey'] = None
            parent_container = self.get_container_by_id(
                dev['parentContainerKey'])
            if parent_container is not None:
                dev['containerName'] = parent_container['name']
            else:
                dev['containerName'] = ''
        return data

    def get_net_element_info_by_device_id(self, device_id):
        ''' Return a dict of info about a device in CVP.

            Args:
                device_id (str): Device Id Key / System MAC.

            Returns:
                net element data (dict): Dict of info specific to the device
                    requested or None if the name requested doesn't exist.
        '''
        self.log.debug('Attempt to get net element data for %s' % device_id)
        try:
            element_info = self.clnt.get('/provisioning/getNetElementInfoById.do?netElementId=%s'
                                         % qplus(device_id), timeout=self.request_timeout)
        except CvpApiError as e:
            # Catch an invalid task_id error and return None
            if 'errorMessage' in str(e):
                self.log.debug('Device with id %s could not be found' % device_id)
                return None
                # pylint: disable=unreachable
                raise CvpApiError("get_net_element_info_by_device_id:%s" % e)
        return element_info

    def get_device_by_name(self, fqdn):
        ''' Returns the net element device dict for the devices fqdn name.

            Args:
                fqdn (str): Fully qualified domain name of the device.

            Returns:
                device (dict): The net element device dict for the device if
                    otherwise returns an empty hash.
        '''
        self.log.debug('get_device_by_name: fqdn: %s' % fqdn)
        data = self.get_inventory(start=0, end=0)
        if len(data) > 0:
            for netelement in data:
                if netelement['fqdn'] == fqdn:
                    device = netelement
                    break
            else:
                device = {}
        else:
            device = {}
        return device

    def get_device_configuration(self, device_mac):
        ''' Returns the running configuration for the device provided.

            Args:
                device_mac (str): Mac address of the device to get the running
                    configuration for.

            Returns:
                device (dict): The net element device dict for the device if
                    otherwise returns an empty hash.
        '''
        self.log.debug('get_device_configuration: device_mac: %s' % device_mac)
        data = self.clnt.get('/inventory/getInventoryConfiguration.do?'
                             'netElementId=%s' % device_mac,
                             timeout=self.request_timeout)
        running_config = ''
        if 'output' in data:
            running_config = data['output']
        return running_config

    def get_configlets_by_device_id(self, mac, start=0, end=0):
        ''' Returns the list of configlets applied to a device.

            Args:
                mac (str): Device mac address (i.e. device id)
                start (int): The first configlet entry to return.  Default is 0
                end (int): The last configlet entry to return.  Default is 0
                    which means to return all configlet entries.  Can be a
                    large number to indicate the last configlet entry.

            Returns:
                configlets (list): The list of configlets applied to the device
        '''
        self.log.debug('get_configlets_by_device: mac: %s' % mac)
        data = self.clnt.get('/provisioning/getConfigletsByNetElementId.do?'
                             'netElementId=%s&queryParam=&startIndex=%d&'
                             'endIndex=%d' % (mac, start, end),
                             timeout=self.request_timeout)
        return data['configletList']

    # pylint: disable=too-many-locals
    def update_configlets_on_device(self, app_name, device, add_configlets, del_configlets, create_task=True):
        ''' Remove the configlets from the device.

            Args:
                app_name (str): The application name to use in info field.
                device (dict): The switch device dict
                add_configlets (list): List of configlets name and key pairs
                del_configlets (list): List of configlet name and key pairs
                create_task (bool): Determines whether or not to execute a save
                    and create the tasks (if any)

            Returns:
                response (dict): A dict that contains a status and a list of
                    task ids created (if any).

                    Ex: {u'data': {u'status': u'success', u'taskIds': [u'35']}}
        '''
        self.log.debug('update_configlets_on_device - %s: add: %s delete: %s' %
                       (device['name'], add_configlets, del_configlets))
        # Allow for deviceId key name variations
        if 'systemMacAddress' not in device.keys() and 'key' in device.keys():
            device['systemMacAddress'] = device['key']
        if 'systemMacAddress' not in device.keys():
            raise KeyError("update_configlets: key or systemMacAddress not found in device object %s - %s" % (device['name'],
                                                                                                              device.keys()))

        # Get all the configlets assigned to the device.
        configlets = self.get_configlets_by_device_id(device['systemMacAddress'])

        # Get a list of the names and keys of the configlets.  Do not add
        # configlets that are on the delete list.
        add_names = []
        add_keys = []
        # If provsioning new device skip this
        if len(configlets) > 0:
            # Remove del_configlet from existing list
            for configlet in configlets:
                found = False
                for del_configlet in del_configlets:
                    if configlet['key'] == del_configlet['key']:
                        found = True
                if not found:
                    add_names.append(configlet['name'])
                    add_keys.append(configlet['key'])
            # Append list of new configlets to add
        for entry in add_configlets:
            add_names.append(entry['name'])
            add_keys.append(entry['key'])

        # Remove the names and keys of the configlets to keep and build a
        # list of the configlets to remove.
        del_names = []
        del_keys = []
        for entry in del_configlets:
            del_names.append(entry['name'])
            del_keys.append(entry['key'])

        info = '%s Configlet Update: on Device %s' % (app_name, device['name'])
        info_preview = '<b>Configlet Update:</b> on Device' + device['name']
        data = {'data': [{'info': info,
                          'infoPreview': info_preview,
                          'note': '',
                          'action': 'associate',
                          'nodeType': 'configlet',
                          'nodeId': '',
                          'configletList': add_keys,
                          'configletNamesList': add_names,
                          'ignoreConfigletNamesList': del_names,
                          'ignoreConfigletList': del_keys,
                          'configletBuilderList': [],
                          'configletBuilderNamesList': [],
                          'ignoreConfigletBuilderList': [],
                          'ignoreConfigletBuilderNamesList': [],
                          'toId': device['systemMacAddress'],
                          'toIdType': 'netelement',
                          'fromId': '',
                          'nodeName': '',
                          'fromName': '',
                          'toName': device['fqdn'],
                          'nodeIpAddress': device['ipAddress'],
                          'nodeTargetIpAddress': device['ipAddress'],
                          'childTasks': [],
                          'parentTask': ''}]}
        self.log.debug('update_configlets_on_device: saveTopology data:\n%s' % data['data'])
        url = ('/provisioning/addTempAction.do?'
               'format=topology&queryParam=&nodeId=root')
        try:
            self.clnt.post(url, data=data, timeout=self.request_timeout)
        except Exception as e:
            self.log.debug('Device %s : %s' % (device['fqdn'], e))
            raise Exception("update_configlets_on_device:%s" % e)
        configlets = []
        for configlet in self.get_configlets_by_device_id(device['systemMacAddress']):
            configlets.append(configlet['name'])
        if create_task:
            url = '/provisioning/v2/saveTopology.do'
            tasks = self.clnt.post(url, data=[], timeout=self.request_timeout)
        else:
            tasks = {}
        return tasks

    def update_imageBundle_on_device(self, app_name, device, add_imageBundle, del_imageBundle, create_task=True):
        ''' Remove the image bundle from the specified container.

            Args:
                app_name (str): The application name to use in info field.
                device (dict): The switch device dictionary.
                add_imageBundle (dict): name & key for imageBundle
                del_imageBundle (dict): name & key for imageBundle
                name (): name.
                id_type (): type.

            Returns:
                response (dict): A dict that contains a status and a list of
                    task ids created (if any).

                    Ex: {u'data': {u'status': u'success', u'taskIds': [u'32']}}
        '''
        # Allow for deviceId key name variations
        if 'systemMacAddress' not in device.keys() and 'key' in device.keys():
            device['systemMacAddress'] = device['key']
        if 'systemMacAddress' not in device.keys():
            raise KeyError("update_imageBundle: key or systemMacAddress not found in device object %s" % device['name'])
        if len(add_imageBundle) > 0 and len(del_imageBundle) > 0:
            raise Exception("Attempting to Delete and Add Imagebundles on %s" % device['name'])
        else:
            if 'key' in add_imageBundle.keys():
                self.log.debug('Attempt to update %s on %s' % (add_imageBundle['name'], device['name']))
                info = '%s Update image: %s on %s' % (app_name, add_imageBundle['name'], device['name'])
                del_imageBundle = {'key': '', 'name': ''}
            elif 'key' in del_imageBundle.keys():
                self.log.debug('Attempt to remove %s on %s' % (del_imageBundle['name'], device['name']))
                info = '%s Remove image: %s on %s' % (app_name, del_imageBundle['name'], device['name'])
                add_imageBundle = {'key': '', 'name': ''}
            else:
                raise Exception("imageBundle_key check: No imageBundle specified")
            info_preview = '<b>Image Update:</b> on Device' + device['name']
            data = {'data': [{'info': info,
                              'infoPreview': info_preview,
                              'note': '',
                              'action': 'associate',
                              'nodeType': 'imagebundle',
                              'nodeId': add_imageBundle['key'],
                              'nodeName': add_imageBundle['name'],
                              'toId': device['systemMacAddress'],
                              'toName': device['fqdn'],
                              'toIdType': 'netelement',
                              'fromId': '',
                              'fromName': '',
                              'ignoreNodeId': del_imageBundle['key'],
                              'ignoreNodeName': del_imageBundle['name'],
                              'childTasks': [],
                              'parentTask': ''}]}
            self.log.debug('update_imageBundles_on_device: saveTopology data:\n%s' % data['data'])
            url = ('/provisioning/addTempAction.do?'
                   'format=topology&queryParam=&nodeId=root')
            try:
                self.clnt.post(url, data=data, timeout=self.request_timeout)
            except Exception as e:
                # pylint: disable=unreachable
                raise Exception("update_imageBundle_on_device:%s" % e)
                self.log.debug('Device %s : %s' % (device['fqdn'], e))
            if create_task:
                url = '/provisioning/v2/saveTopology.do'
                tasks = self.clnt.post(url, data=[], timeout=self.request_timeout)
                return tasks

    def reset_device(self, app_name, device, create_task=True):
        ''' Reset device by moving it to the Undefined Container.

            Args:
                app_name (str): String to specify info/signifier of calling app
                device (dict): Device info
                container (dict): Container info
                create_task (bool): Determines whether or not to execute a save
                    and create the tasks (if any)

            Returns:
                response (dict): A dict that contains a status and a list of
                    task ids created (if any).

                    Ex: {u'data': {u'status': u'success', u'taskIds': []}}
        '''
        info = '%s Reseting device %s moving it to Undefined' % (app_name,
                                                                 device['fqdn'])
        self.log.debug('Attempting to Reset device %s moving it to Undefined'
                       % (device['fqdn']))
        # Allow for deviceId key name variations
        if 'systemMacAddress' not in device.keys() and 'key' in device.keys():
            device['systemMacAddress'] = device['key']
        if 'systemMacAddress' not in device.keys():
            raise KeyError("update_imageBundle: key or systemMacAddress not found in device object %s" % device['name'])
        # Allow for parentContainerId key name variations
        if 'parentContainerId' not in device.keys() and 'parentContainerKey' in device.keys():
            device['parentContainerId'] = device['parentContainerKey']
        if 'parentContainerId' not in device.keys():
            raise KeyError("parentContainerId not found in device object %s" % device['name'])
        data = {'data': [{'info': info,
                          'infoPreview': info,
                          'action': 'reset',
                          'nodeType': 'netelement',
                          'nodeId': device['systemMacAddress'],
                          'toId': 'undefined_container',
                          'fromId': device['parentContainerId'],
                          'nodeName': device['fqdn'],
                          'toName': 'Undefined',
                          'toIdType': 'container',
                          'childTasks': [],
                          'parentTask': ''}]}
        url = ('/provisioning/addTempAction.do?'
               'format=topology&queryParam=&nodeId=root')
        try:
            self.clnt.post(url, data=data, timeout=self.request_timeout)
        except CvpApiError as e:
            if any(txt in str(e) for txt in ['Data already exists', 'undefined container']):
                self.log.debug('Device %s already in container Undefined'
                               % device['fqdn'])
        except Exception as e:
            self.log.debug('Reset Device %s : %s' % (device['fqdn'], e))
            raise Exception("reset_device:%s" % e)
        if create_task:
            url = '/provisioning/v2/saveTopology.do'
            tasks = self.clnt.post(url, data=[], timeout=self.request_timeout)
            return tasks

    def provision_device(self, app_name, device, container, configlets, imageBundle, create_task=True):
        '''Move a device from the undefined container to a target container.
            Optionally apply device-specific configlets and an imageBundle.

            Args:
                device (dict): Device Info
                container (dict): Container Info
                configlets (list): list of dicts with configlet key/name pairs
                imageBundle (dict): imageBundle name and key to apply to device
                create_task (boolean): Create task for this device provisioning sequence.

            Returns:
                response (dict): A dict that contains a status and a list of
                    task ids created (if any).

                    Ex: {u'data': {u'status': u'success', u'taskIds': [u'32']}}
        '''
        info = 'Provision device %s to container %s' % (device['fqdn'], container['name'])
        self.log.debug(info)
        # Allow for deviceId key name variations
        if 'systemMacAddress' not in device.keys() and 'key' in device.keys():
            device['systemMacAddress'] = device['key']
        if 'systemMacAddress' not in device.keys():
            raise KeyError("update_imageBundle: key or systemMacAddress not found in device object %s" % device['name'])
        # Allow for parentContainerId key name variations
        if 'parentContainerId' not in device.keys() and 'parentContainerKey' in device.keys():
            device['parentContainerId'] = device['parentContainerKey']
        if 'parentContainerId' not in device.keys():
            raise KeyError("parentContainerId not found in device object %s" % device['name'])
        # Add action for moving device to specified container
        try:
            self.move_device_to_container('%s:provision_device' % app_name, device, container,
                                          create_task=False)
        except Exception as e:
            self.log.debug('Provision Device - move %s : %s' % (device['fqdn'], e))
            raise Exception("provsion_device-move_to_container:%s" % e)
        # Don't save configlet action if there is an image bundle to add
        if 'key' in imageBundle.keys():
            configlet_task = False
        elif create_task:
            configlet_task = True
        else:
            configlet_task = False
        try:
            created_tasks = self.update_configlets_on_device(app_name, device, configlets, [],
                                                             configlet_task)
        except Exception as e:
            self.log.debug('Provision Device - configlets %s : %s' % (device['fqdn'], e))
            raise Exception("provsion_device-update_configlets:%s" % e)
        # If configlet action created tasks then don't action imageBundles
        # Skip if no imageBundles specified
        if not configlet_task and 'key' in imageBundle.keys():
            try:
                created_tasks = self.update_imageBundle_on_device(app_name, device, imageBundle, {},
                                                                  create_task)
            except Exception as e:
                self.log.debug('Provision Device - imageBundle %s : %s' % (device['fqdn'], e))
                raise Exception("provsion_device-update_imageBundle:%s" % e)
        return created_tasks

    def apply_configlets_to_container(self, app_name, container, new_configlets, create_task=True):
        ''' Apply the configlets to the container.

            Args:
                app_name (str): The application name to use in info field.
                container (dict): The container dict
                new_configlets (list): List of configlet name and key pairs
                create_task (bool): Determines whether or not to execute a save
                    and create the tasks (if any)

            Returns:
                response (dict): A dict that contains a status and a list of
                    task ids created (if any).

                    Ex: {u'data': {u'status': u'success', u'taskIds': [u'32']}}
        '''
        self.log.debug('apply_configlets_to_container: container: %s names: %s' %
                       (container, new_configlets))
        # Get all the configlets assigned to the device.
        configlets = self.get_configlets_by_container_id(container['key'])

        # Get a list of the names and keys of the configlets
        # Static Configlets
        cnames = []
        ckeys = []
        # ConfigletBuilder Configlets
        bnames = []
        bkeys = []
        if len(configlets['configletList']) > 0:
            for configlet in configlets['configletList']:
                if configlet['type'] == 'Static':
                    cnames.append(configlet['name'])
                    ckeys.append(configlet['key'])
                elif configlet['type'] == 'Builder':
                    bnames.append(configlet['name'])
                    bkeys.append(configlet['key'])

        # Add the new configlets to the end of the arrays
        for entry in new_configlets:
            cnames.append(entry['name'])
            ckeys.append(entry['key'])

        info = '%s: Configlet Assign: to Container %s' % (app_name, container['name'])
        info_preview = '<b>Configlet Assign:</b> to Container' + container['name']
        data = {'data': [{'info': info,
                          'infoPreview': info_preview,
                          'note': '',
                          'action': 'associate',
                          'nodeType': 'configlet',
                          'nodeId': '',
                          'configletList': ckeys,
                          'configletNamesList': cnames,
                          'ignoreConfigletNamesList': [],
                          'ignoreConfigletList': [],
                          'configletBuilderList': bkeys,
                          'configletBuilderNamesList': bnames,
                          'ignoreConfigletBuilderList': [],
                          'ignoreConfigletBuilderNamesList': [],
                          'toId': container['key'],
                          'toIdType': 'container',
                          'fromId': '',
                          'nodeName': '',
                          'fromName': '',
                          'toName': container['name'],
                          'nodeIpAddress': '',
                          'nodeTargetIpAddress': '',
                          'childTasks': [],
                          'parentTask': ''}]}
        self.log.debug('apply_configlets_to_container: saveTopology data:\n%s' %
                       data['data'])
        self._add_temp_action(data)
        if create_task:
            return self._save_topology_v2([])
        else:
            return data

    # ~Configlet Related API Calls

    def get_configlet_by_name(self, name):
        ''' Returns the configlet with the specified name

            Args:
                name (str): Name of the configlet.  Can contain spaces.

            Returns:
                configlet (dict): The configlet dict.
        '''
        self.log.debug('get_configlets_by_name: name: %s' % name)
        return self.clnt.get('/configlet/getConfigletByName.do?name=%s'
                             % qplus(name), timeout=self.request_timeout)

    def get_configlets(self, start=0, end=0):
        ''' Returns a list of all defined configlets.

            Args:
                start (int): Start index for the pagination. Default is 0.
                end (int): End index for the pagination. If end index is 0
                    then all the records will be returned. Default is 0.
        '''
        self.log.debug('v2 Inventory API Call')
        # Get the actual configlet config using getConfigletByName
        configlets = self.clnt.get('/configlet/getConfiglets.do?'
                                   'startIndex=%d&endIndex=%d' % (start, end),
                                   timeout=self.request_timeout)
        if 'data' in configlets:
            for configlet in configlets['data']:
                full_cfglt_data = self.get_configlet_by_name(
                    configlet['name'])
                configlet['config'] = full_cfglt_data['config']
        return configlets

    def get_devices_by_configlet(self, configlet_name, start=0, end=0):
        ''' Returns a list of devices to which the named configlet is applied.

            Args:
                configlet_name (str): The name of the configlet to be queried.
                start (int): Start index for the pagination. Default is 0.
                end (int): End index for the pagination. If end index is 0
                    then all the records will be returned. Default is 0.
        '''
        return self.clnt.get('/configlet/getAppliedDevices.do?'
                             'configletName=%s&startIndex=%d&endIndex=%d'
                             % (configlet_name, start, end),
                             timeout=self.request_timeout)

    def get_containers_by_configlet(self, configlet_name, start=0, end=0):
        ''' Returns a list of containers to which the named
            configlet is applied.

            Args:
                configlet_name (str): The name of the configlet to be queried.
                start (int): Start index for the pagination. Default is 0.
                end (int): End index for the pagination. If end index is 0
                    then all the records will be returned. Default is 0.
        '''
        return self.clnt.get('/configlet/getAppliedContainers.do?'
                             'configletName=%s&startIndex=%d&endIndex=%d'
                             % (configlet_name, start, end),
                             timeout=self.request_timeout)

    def add_configlet(self, name, config):
        ''' Add a configlet and return the key for the configlet.

            Args:
                name (str): Configlet name
                config (str): Switch config statements

            Returns:
                key (str): The key for the configlet
        '''
        self.log.debug('add_configlet: name: %s config: %s' % (name, config))
        body = {'name': name, 'config': config}
        # Create the configlet
        self.clnt.post('/configlet/addConfiglet.do', data=body,
                       timeout=self.request_timeout)

        # Get the key for the configlet
        data = self.clnt.get('/configlet/getConfigletByName.do?name=%s'
                             % qplus(name), timeout=self.request_timeout)
        return data['key']

    def update_configlet(self, config, key, name, wait_task_ids=False):
        ''' Update a configlet.

            Args:
                config (str): Switch config statements
                key (str): Configlet key
                name (str): Configlet name
                wait_task_ids (boolean): Wait for task IDs to generate

            Returns:
                data (dict): Contains success or failure message
        '''
        self.log.debug('update_configlet: config: %s key: %s name: %s' %
                       (config, key, name))

        # Update the configlet
        body = {'config': config, 'key': key, 'name': name,
                'waitForTaskIds': wait_task_ids}
        return self.clnt.post('/configlet/updateConfiglet.do', data=body,
                              timeout=self.request_timeout)

    def delete_configlet(self, name, key):
        ''' Delete the configlet.

            Args:
                name (str): Configlet name
                key (str): Configlet key
        '''
        self.log.debug('delete_configlet: name: %s key: %s' % (name, key))
        body = [{'name': name, 'key': key}]
        # Delete the configlet
        self.clnt.post('/configlet/deleteConfiglet.do', data=body,
                       timeout=self.request_timeout)

    def add_note_to_configlet(self, key, note):
        ''' Add a note to a configlet.

            Args:
                key (str): Configlet key
                note (str): Note to be added to configlet.
        '''
        data = {
            'key': key,
            'note': note,
        }
        return self.clnt.post('/configlet/addNoteToConfiglet.do',
                              data=data, timeout=self.request_timeout)

    # ~Container Related API Calls

    # pylint: disable=too-many-arguments
    def _container_op(self, container_name, container_key, parent_name,
                      parent_key, operation):
        ''' Perform the operation on the container.

            Args:
                container_name (str): Container name
                container_key (str): Container key, can be empty for add.
                parent_name (str): Parent container name
                parent_key (str): Parent container key
                operation (str): Container operation 'add' or 'delete'.

            Returns:
                response (dict): A dict that contains a status and a list of
                    task ids created (if any).

                    Ex: {u'data': {u'status': u'success', u'taskIds': []}}
        '''
        msg = ('%s container %s under container %s' %
               (operation, container_name, parent_name))
        data = {'data': [{'info': msg,
                          'infoPreview': msg,
                          'action': operation,
                          'nodeType': 'container',
                          'nodeId': container_key,
                          'toId': '',
                          'fromId': '',
                          'nodeName': container_name,
                          'fromName': '',
                          'toName': '',
                          'childTasks': [],
                          'parentTask': '',
                          'toIdType': 'container'}]}
        if operation == 'add':
            data['data'][0]['toId'] = parent_key
            data['data'][0]['toName'] = parent_name
        elif operation == 'delete':
            data['data'][0]['fromId'] = parent_key
            data['data'][0]['fromName'] = parent_name

        # Perform the container operation
        self._add_temp_action(data)
        return self._save_topology_v2([])

    def _add_temp_action(self, data):
        ''' Adds temp action that requires a saveTopology call to take effect.

            Args:
                data (dict): a data dict with a specific format for the
                    desired action.

                    Base Ex: data = {'data': [{specific key/value pairs}]}
        '''
        url = ('/provisioning/addTempAction.do?'
               'format=topology&queryParam=&nodeId=root')
        self.clnt.post(url, data=data, timeout=self.request_timeout)

    def _save_topology_v2(self, data):
        ''' Confirms a previously created temp action.

            Args:
                data (list): a list that contains a dict with a specific
                    format for the desired action. Our primary use case is for
                    confirming existing temp actions so we most often send an
                    empty list to confirm an existing temp action.

            Returns:
                response (dict): A dict that contains a status and a list of
                    task ids created (if any).

                    Ex: {u'data': {u'status': u'success', u'taskIds': []}}
        '''
        url = '/provisioning/v2/saveTopology.do'
        return self.clnt.post(url, data=data, timeout=self.request_timeout)

    def get_configlets_by_netelement_id(self, d_id, start=0, end=0):
        ''' Returns a list of configlets applied to the given device.

            Args:
                d_id (str): The device ID (key) to query.
                start (int): Start index for the pagination. Default is 0.
                end (int): End index for the pagination. If end index is 0
                    then all the records will be returned. Default is 0.
        '''
        return self.clnt.get('/provisioning/getConfigletsByNetElementId.do?'
                             'netElementId=%s&startIndex=%d&endIndex=%d'
                             % (d_id, start, end),
                             timeout=self.request_timeout)

    def add_container(self, container_name, parent_name, parent_key):
        ''' Add the container to the specified parent.

            Args:
                container_name (str): Container name
                parent_name (str): Parent container name
                parent_key (str): Parent container key

            Returns:
                response (dict): A dict that contains a status and a list of
                    task ids created (if any).

                    Ex: {u'data': {u'status': u'success', u'taskIds': []}}
        '''
        self.log.debug('add_container: container: %s parent: %s parent_key: %s'
                       % (container_name, parent_name, parent_key))
        return self._container_op(container_name, 'new_container', parent_name,
                                  parent_key, 'add')

    def delete_container(self, container_name, container_key, parent_name,
                         parent_key):
        ''' Add the container to the specified parent.

            Args:
                container_name (str): Container name
                container_key (str): Container key
                parent_name (str): Parent container name
                parent_key (str): Parent container key

            Returns:
                response (dict): A dict that contains a status and a list of
                    task ids created (if any).

                    Ex: {u'data': {u'status': u'success', u'taskIds': []}}
        '''
        self.log.debug('delete_container: container: %s container_key: %s '
                       'parent: %s parent_key: %s' %
                       (container_name, container_key, parent_name,
                        parent_key))
        return self._container_op(container_name, container_key, parent_name,
                                  parent_key, 'delete')

    def get_containers(self, start=0, end=0):
        ''' Returns a list of all the containers.

            Args:
                start (int): Start index for the pagination.  Default is 0.
                end (int): End index for the pagination.  If end index is 0
                    then all the records will be returned.  Default is 0.

            Returns:
                containers (dict): The 'total' key contains the number of
                containers, the 'data' key contains a list of the containers
                with associated info.
        '''
        self.log.debug('Get list of containers')
        self.log.debug('v2 Inventory API Call')
        containers = self.clnt.get('/inventory/containers')
        for container in containers:
            container['name'] = container['Name']
            container['key'] = container['Key']
            full_cont_info = self.get_container_by_id(container['Key'])
            if (full_cont_info is not None and container['Key'] != 'root'):
                container['parentName'] = full_cont_info['parentName']
                full_parent_info = self.get_container_by_name(full_cont_info['parentName'])
                if full_parent_info is not None:
                    container['parentId'] = full_parent_info['key']
                else:
                    container['parentId'] = None
            else:
                container['parentName'] = None
                container['parentId'] = None
            container['type'] = None
            container['id'] = 21
            container['factoryId'] = 1
            container['userId'] = None
            container['childContainerId'] = None
        return {'data': containers, 'total': len(containers)}

    def get_container_by_name(self, name):
        ''' Returns a container that exactly matches the name.

            Args:
                name (str): String to search for in container names.

            Returns:
                container (dict): Container info in dictionary format or None
        '''
        self.log.debug('Get info for container %s' % name)
        containers = self.clnt.get('/provisioning/searchTopology.do?queryParam=%s'
                                   '&startIndex=0&endIndex=0' % qplus(name))
        if containers['total'] > 0 and containers['containerList']:
            for container in containers['containerList']:
                if container['name'] == name:
                    return container
        return None

    def get_container_by_id(self, key):
        ''' Returns a container for the given id.

            Args:
                key (str): String ID for container to find.

            Returns:
                container (dict): Container info in dictionary format or None
        '''
        self.log.debug('Get info for container %s' % key)
        return self.clnt.get('/provisioning/getContainerInfoById.do?'
                             'containerId=%s' % qplus(key))

    def get_devices_in_container(self, name):
        ''' Returns a dict of the devices under the named container.

            Args:
                name (str): The name of the container to get devices from
        '''
        self.log.debug('get_devices_in_container: called')
        devices = []
        container = self.get_container_by_name(name)
        if container:
            all_devices = self.get_inventory(0, 0, name)
            for device in all_devices:
                if device['parentContainerId'] == container['key']:
                    devices.append(device)
        return devices

    def get_devices_by_container_id(self, key):
        ''' Returns a dict of the devices under the named container.

            Args:
                key (str): The containerId of the container to get devices from
        '''
        self.log.debug('get_devices_in_container: by Id')
        devices = []
        all_elements = self.clnt.get('/provisioning/getNetElementList.do?'
                                     'nodeId=%s&startIndex=0&endIndex=0&ignoreAdd=false'
                                     % key, timeout=self.request_timeout)
        for device in all_elements["netElementList"]:
            devices.append(device)
        return devices

    def get_configlets_by_container_id(self, c_id, start=0, end=0):
        ''' Returns a list of configlets applied to the given container.

            Args:
                c_id (str): The container ID (key) to query.
                start (int): Start index for the pagination. Default is 0.
                end (int): End index for the pagination. If end index is 0
                    then all the records will be returned. Default is 0.
        '''
        return self.clnt.get('/provisioning/getConfigletsByContainerId.do?'
                             'containerId=%s&startIndex=%d&endIndex=%d'
                             % (c_id, start, end),
                             timeout=self.request_timeout)

    def get_image_bundle_by_container_id(self, c_id, start=0, end=0, scope='false'):
        ''' Returns a list of ImageBundles applied to the given container.

            Args:
                c_id (str): The container ID (key) to query.
                start (int): Start index for the pagination. Default is 0.
                end (int): End index for the pagination. If end index is 0
                    then all the records will be returned. Default is 0.
                scope (string) the session scope
        '''
        return self.clnt.get('/provisioning/getImageBundleByContainerId.do?'
                             'containerId=%s&startIndex=%d&endIndex=%d&sessionScope=%s'
                             % (c_id, start, end, scope),
                             timeout=self.request_timeout)

    def move_device_to_container(self, app_name, device, container, create_task=True):
        ''' Add the container to the specified parent.

            Args:
                app_name (str): String to specify info/signifier of calling app
                device (dict): Device info
                container (dict): Container info
                create_task (bool): Determines whether or not to execute a save
                    and create the tasks (if any)

            Returns:
                response (dict): A dict that contains a status and a list of
                    task ids created (if any).

                    Ex: {u'data': {u'status': u'success', u'taskIds': []}}
        '''
        info = '%s moving device %s to container %s' % (app_name,
                                                        device['fqdn'],
                                                        container['name'])
        self.log.debug('Attempting to move device %s to container %s'
                       % (device['fqdn'], container['name']))
        # Allow for deviceId key name variations
        if 'systemMacAddress' not in device.keys() and 'key' in device.keys():
            device['systemMacAddress'] = device['key']
        if 'systemMacAddress' not in device.keys():
            raise KeyError("update_imageBundle: key or systemMacAddress not found in device object %s" % device['name'])
        # Allow for parentContainerId key name variations
        if 'parentContainerId' not in device.keys() and 'parentContainerKey' in device.keys():
            device['parentContainerId'] = device['parentContainerKey']
        if 'parentContainerId' not in device.keys():
            raise KeyError("parentContainerId not found in device object %s" % device['name'])
        from_id = device['parentContainerId']
        data = {'data': [{'info': info,
                          'infoPreview': info,
                          'action': 'update',
                          'nodeType': 'netelement',
                          'nodeId': device['key'],
                          'toId': container['key'],
                          'fromId': from_id,
                          'nodeName': device['fqdn'],
                          'toName': container['name'],
                          'toIdType': 'container',
                          'childTasks': [],
                          'parentTask': ''}]}
        url = ('/provisioning/addTempAction.do?'
               'format=topology&queryParam=&nodeId=root')
        try:
            self.clnt.post(url, data=data, timeout=self.request_timeout)
        except CvpApiError as e:
            if any(txt in str(e) for txt in ['Data already exists']):
                self.log.debug('Device %s already in container %s'
                               % (device['fqdn'], container['name']))
        except Exception as e:
            self.log.debug('Move %s to %s : %s' % (device['name'], container['name'], e))
            raise Exception("move_device:%s" % e)
        if create_task:
            url = '/provisioning/v2/saveTopology.do'
            tasks = self.clnt.post(url, data=[], timeout=self.request_timeout)
            return tasks

    # ~Image Related API Calls

    def get_image_bundles(self, start=0, end=0):
        ''' Return a list of all image bundles.

            Args:
                start (int): Start index for the pagination.  Default is 0.
                end (int): End index for the pagination.  If end index is 0
                    then all the records will be returned.  Default is 0.

            Returns:
                image bundles (dict): The 'total' key contains the number of
                    image bundles, the 'data' key contains a list of image
                    bundles and their info.
        '''
        self.log.debug('Get image bundles that can be applied to devices or'
                       ' containers')
        return self.clnt.get('/image/getImageBundles.do?queryparam=&'
                             'startIndex=%d&endIndex=%d' % (start, end),
                             timeout=self.request_timeout)

    # ~Task Related API Calls

    def get_tasks(self, start=0, end=0):
        ''' Returns a list of all the tasks.

            Args:
                start (int): Start index for the pagination.  Default is 0.
                end (int): End index for the pagination.  If end index is 0
                    then all the records will be returned.  Default is 0.

            Returns:
                tasks (dict): The 'total' key contains the number of tasks,
                    the 'data' key contains a list of the tasks.
        '''
        self.log.debug('get_tasks:')
        return self.clnt.get('/task/getTasks.do?queryparam=&startIndex=%d&'
                             'endIndex=%d' % (start, end),
                             timeout=self.request_timeout)

    def get_tasks_by_status(self, status, start=0, end=0):
        ''' Returns a list of tasks with the given status.

            Args:
                status (str): Task status
                start (int): Start index for the pagination.  Default is 0.
                end (int): End index for the pagination.  If end index is 0
                    then all the records will be returned.  Default is 0.

            Returns:
                tasks (list): The list of tasks
        '''
        self.log.debug('get_tasks_by_status: status: %s' % status)
        data = self.clnt.get(
            '/task/getTasks.do?queryparam=%s&startIndex=%d&endIndex=%d' %
            (status, start, end), timeout=self.request_timeout)
        return data['data']

    def get_task_by_id(self, task_id):
        ''' Returns the current CVP Task status for the task with the specified
        TaskId.

        Args:
            task_id (int): CVP task identifier

        Returns:
            task (dict): The CVP task for the associated Id.  Returns None
                if the task_id was invalid.
        '''
        self.log.debug('get_task_by_id: task_id: %s' % task_id)
        try:
            task = self.clnt.get('/task/getTaskById.do?taskId=%s' % task_id,
                                 timeout=self.request_timeout)
        except CvpApiError as error:
            self.log.debug('Caught error: %s attempting to get task.' % error)
            # Catch an invalid task_id error and return None
            return None
        return task

    def add_note_to_task(self, task_id, note):
        ''' Add notes to the task.

            Args:
                task_id (str): Task ID
                note (str): Note to add to the task
        '''
        self.log.debug('add_note_to_task: task_id: %s note: %s' %
                       (task_id, note))
        data = {'workOrderId': task_id, 'note': note}
        self.clnt.post('/task/addNoteToTask.do', data=data,
                       timeout=self.request_timeout)

    def execute_task(self, task_id):
        ''' Execute the task.  Note that if the task has failed then inspect
            the task logs to determine why the task failed.  If you see:

              Failure response received from the netElement: Unauthorized User

            then it means that the netelement does not have the same user ID
            and/or password as the CVP user executing the task.

            Args:
                task_id (str): Task ID
        '''
        self.log.debug('execute_task: task_id: %s' % task_id)
        data = {'data': [task_id]}
        return self.clnt.post('/task/executeTask.do', data=data,
                              timeout=self.request_timeout)

    def cancel_task(self, task_id):
        ''' Cancel the task

            Args:
                task_id (str): Task ID
        '''
        self.log.debug('cancel_task: task_id: %s' % task_id)
        data = {'data': [task_id]}
        return self.clnt.post('/task/cancelTask.do', data=data,
                              timeout=self.request_timeout)
