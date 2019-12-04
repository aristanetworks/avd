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

''' RESTful API Client class for Cloudvision(R) Portal

This module provides a RESTful API client for Cloudvision(R) Portal (CVP)
which can be used for building applications that work with Arista CVP.

When the class is instantiated the logging is configured.  Either syslog,
file logging, both, or none can be enabled.  If neither syslog nor filename is
specified then no logging will be performed.

This class supports creating a connection to a CVP node and then issuing
subsequent GET and POST requests to CVP.  A GET or POST request will be
automatically retried on the same node if the request receives a
requests.exceptions.Timeout or ReadTimeout error.  A GET or POST request will
be automatically retried on the same node if the request receives a
CvpSessionLogOutError.  For this case a login will be performed before the
request is retried.  For either case, the maximum number of times a request
will be retried on the same node is specified by the class attribute
NUM_RETRY_REQUESTS.

If more than one CVP node is specified when creating a connection, and a GET
or POST request that receives a requests.exceptions.ConnectionError,
requests.exceptions.HTTPError, or a requests.exceptions.TooManyRedirects will
be retried on the next CVP node in the list.  If a GET or POST request that
receives a requests.exceptions.Timeout or CvpSessionLogOutError and the retries
on the same node exceed NUM_RETRY_REQUESTS, then the request will be retried
on the next node on the list.

If any of the errors persists across all nodes then the GET or POST request
will fail and the last error that occurred will be raised.

The class provides connect, get, and post methods that allow the user to make
direct RESTful API calls to CVP.

Example:

    >>> from cv_client import CvpClient
    >>> clnt = CvpClient()
    >>> clnt.connect(['cvp1', 'cvp2', 'cvp3'], 'cvp_user', 'cvp_word')
    >>> result = clnt.get('/cvpInfo/getCvpInfo.do')
    >>> print result
    {u'version': u'2016.1.0'}
    >>>

The class provides a wrapper function around the CVP RESTful API operations.
Each API method takes the RESTful API parameters as method parameters to the
operation method.  The API class was added to the client class because the
API functions are required when using the CVP RESTful API and placing them
in this library avoids duplicating the calls in every application that uses
this class.

Example:

    >>> from cv_client import CvpClient
    >>> clnt = CvpClient()
    >>> clnt.connect(['cvp1', 'cvp2', 'cvp3'], 'cvp_user', 'cvp_word')
    >>> result = clnt.api.get_cvp_info()
    >>> print result
    {u'version': u'2016.1.0'}
    >>>
'''

import re
import json
import logging
import inspect
import traceback
from logging.handlers import SysLogHandler
from itertools import cycle
from ansible_collections.arista.cvp.plugins.module_utils.cv_client_errors import CvpApiError, CvpLoginError, CvpRequestError, CvpSessionLogOutError
REQUESTS_IMP_ERR = None
try:
    import requests
    from requests.exceptions import ConnectionError, HTTPError, Timeout, ReadTimeout, TooManyRedirects
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False
    REQUESTS_IMP_ERR = traceback.format_exc()


class CvpClient(object):
    ''' Use this class to create a persistent connection to CVP.
    '''
    # pylint: disable=too-many-instance-attributes
    # Maximum number of times to retry a get or post to the same
    # CVP node.
    NUM_RETRY_REQUESTS = 3

    def __init__(self, logger='cv_apiClient', syslog=False, filename=None,
                 log_level='INFO'):
        ''' Initialize the client and configure logging.  Either syslog, file
            logging, both, or none can be enabled.  If neither syslog
            nor filename is specified then no logging will be performed.

            Args:
                logger (str): The name assigned to the logger.
                syslog (bool): If True enable logging to syslog. Default is
                    False.
                filename (str): Log to the file specified by filename. Default
                    is None.
                log_level (str): Log level to use for logger. Default is INFO.
        '''
        self.apiVersion = None
        self.api = None
        self.authdata = None
        self.cert = False
        self.connect_timeout = None
        self.cookies = None
        self.error_msg = ''
        self.node_cnt = None
        self.node_pool = None
        self.nodes = None
        self.port = None
        self.protocol = None
        self.session = None
        self.url_prefix = None
        self.version = None
        self._last_used_node = None

        # Save proper headers
        self.headers = {'Accept': 'application/json',
                        'Content-Type': 'application/json'}

        self.log = logging.getLogger(logger)
        self.set_log_level(log_level)
        if syslog:
            # Enables sending logging messages to the local syslog server.
            self.log.addHandler(SysLogHandler())
        if filename:
            # Enables sending logging messages to a file.
            self.log.addHandler(logging.FileHandler(filename))
        if syslog is False and filename is None:
            # Not logging so use the null handler
            self.log.addHandler(logging.NullHandler())

    @property
    def last_used_node(self):
        ''' Returns the node that the last request was sent to regardless of
            whether the request was successful or not.

            Returns:
                String identifying the node that the last request was sent to.
        '''
        return self._last_used_node

    def set_log_level(self, log_level='INFO'):
        ''' Set log level for logger. Defaults to INFO if no level passed in or
            if an invalid level is passed in.

            Args:
                log_level (str): Log level to use for logger. Default is INFO.
        '''
        log_level = log_level.upper()
        if log_level not in ['NOTSET', 'DEBUG', 'INFO',
                             'WARNING', 'ERROR', 'CRITICAL']:
            log_level = 'INFO'
        self.log.setLevel(getattr(logging, log_level))

    def _set_apiVersion(self, init=False):
        '''
        Use client information to retrive CVP Info and get CVP Version
        assumption made that get CVP Info API request has not changed.
        :param: init - Boolean, True if intialising module, false if checking.
        :return: required cv_api version
        '''
        self.apiVersion = None
        self.apiName = None
        self.errorMessage = []
        self.cvpInfo = self.get('/cvpInfo/getCvpInfo.do')
        if 'version' in self.cvpInfo:
            self.cvpVersion = self.cvpInfo['version']
            self.splitVersion = self.cvpVersion.split('.')
            # Expect version string to be at least two long
            # Ex: 2018.2
            # Ex: 2018.1.4
            # Ex: 2017.2
            if len(self.splitVersion) > 2:
                # Set apiversion to major CVP release
                if int(self.splitVersion[0]) == 2017:
                    self.log.info('Setting API version to 2017')
                    self.apiVersion = '2017'
                    self.apiName = 'cv_api2017'
                    if init:
                        pass
                elif int(self.splitVersion[0]) == 2018:
                    self.log.info('Setting API version to 2018')
                    self.apiVersion = '2018'
                    self.apiName = 'cv_api2018'
                    if init:
                        from ansible_collections.arista.cvp.plugins.module_utils.cv_api2018 import CvpApi
                elif int(self.splitVersion[0]) == 2019:
                    self.log.info('Setting API version to 2019')
                    self.apiVersion = '2019'
                    self.apiName = 'cv_api2019'
                    if init:
                        from ansible_collections.arista.cvp.plugins.module_utils.cv_api2019 import CvpApi
                else:
                    self.log.error('Unable to set API version')
            else:
                # If version is shorter than 2 elements for some reason default
                self.log.error('Version has less than 2 elements. CVP Version Format Error')
            if self.apiVersion is not None and init:
                self.log.info('Importing API library: %s', inspect.getfile(CvpApi))
                self.api = CvpApi(self)

        return {'apiVersion': self.apiVersion, 'apiName': self.apiName}

    def connect(self, nodes, username, password, connect_timeout=10,
                protocol='https', port=None, cert=False):
        ''' Login to CVP and get a session ID and cookie.  Currently
            certificates are not verified if the https protocol is specified. A
            warning may be printed out from the requests module for this case.

            Args:
                nodes (list): A list of hostname/IP addresses for CVP nodes
                username (str): The CVP username
                password (str): The CVP password
                connect_timeout (int): The number of seconds to wait for a
                    connection.
                protocol (str): The protocol to use to connect to CVP.
                    THIS PARAMETER IS NOT USED AND WILL BE DEPRECATED.
                    ONLY INCLUDED TO NOT BREAK EXISTING CODE THAT HAS PROTOCOL
                    SPECIFIED IN CONNECTION.
                port (int): The TCP port of the endpoint for the connection.
                    If this keyword is not specified, the default value is
                    automatically determined by the transport type.
                    (http=80, https=443)
                cert (str or boolean): Path to a cert file used for a https
                    connection or boolean with default False. If a cert is
                    provided then the connection will not attempt to fallback
                    to http. The False default sets the request to not verify
                    the servers TLS certificate.

            Raises:
                CvpLoginError: A CvpLoginError is raised if a connection
                    could not be established to any of the nodes.
                TypeError: A TypeError is raised if the nodes argument is not
                    a list.
                ValueError: A ValueError is raised if a port is not specified
                    and the protocol is not http or https.
        '''
        # pylint: disable=too-many-arguments
        if not isinstance(nodes, list):
            raise TypeError('nodes argument must be a list')

        self.cert = cert
        self.nodes = nodes
        self.node_cnt = len(nodes)
        self.node_pool = cycle(nodes)
        self.authdata = {'userId': username, 'password': password}
        self.connect_timeout = connect_timeout
        # protocol is deprecated and not used.
        self.protocol = protocol
        self.port = port
        self._create_session(all_nodes=True)
        # Verify that we can connect to at least one node
        if not self.session:
            raise CvpLoginError(self.error_msg)
        else:
            # Instantiate the CvpApi class
            self.apiVersion = self._set_apiVersion(True)

    def _create_session(self, all_nodes=False):
        ''' Login to CVP and get a session ID and user information.
            If the all_nodes parameter is True then try creating a session
            with each CVP node.  If False, then try creating a session with
            each node except the one currently connected to.
        '''
        num_nodes = self.node_cnt
        if not all_nodes and num_nodes > 1:
            num_nodes -= 1

        self.error_msg = '\n'
        for x in range(0, num_nodes):
            host = next(self.node_pool)
            self.url_prefix = ('https://%s:%d/web' % (host, self.port or 443))
            error = self._reset_session()
            if error and not self.cert:
                self.log.warning('Failed to connect over https. Potentially'
                                 ' due to an old version of CVP. Attempting'
                                 ' fallback to http. Error: %s', error)
                # Attempt http fallback if no cert file is provided. The
                # intention here is that a user providing a cert file
                # forces https.
                self.url_prefix = ('http://%s:%d/web'
                                   % (host, self.port or 80))
                error = self._reset_session()
            if error is None:
                break
            self.error_msg += '%s: %s\n' % (host, error)

    def _reset_session(self):
        ''' Get a new request session and try logging into the current
            CVP node. If the login succeeded None will be returned and
            self.session will be valid. If the login failed then an
            exception error will be returned and self.session will
            be set to None.
        '''
        self.session = requests.Session()
        return_error = None
        try:
            self._login()
        except (ConnectionError, CvpApiError, CvpRequestError,
                CvpSessionLogOutError, HTTPError, ReadTimeout, Timeout,
                TooManyRedirects) as error:
            self.log.error(error)
            # Use outer scope var for return to handle
            # Python 3 UnboundLocalError
            return_error = error
            # Any error that occurs during login is a good reason not to use
            # this CVP node.
            self.session = None
        return return_error

    def _is_good_response(self, response, prefix):
        ''' Check for errors in a response from a GET or POST request.
            The response argument contains a response object from a GET or POST
            request.  The prefix argument contains the prefix to put into the
            error message.

            Raises:
                CvpApiError: A CvpApiError is raised if there was a JSON error.
                CvpRequestError: A CvpRequestError is raised if the request
                    is not properly constructed.
                CvpSessionLogOutError: A CvpSessionLogOutError is raised if
                    response from server indicates session was logged out.
        '''
        if not response.ok:
            msg = '%s: Request Error: %s' % (prefix, response.reason)
            self.log.error(msg)
            if 'Unauthorized' in response.reason:
                # Check for Unauthorized User error because this is how
                # CVP responds to a logged out users requests in 2018
                # and beyond.
                raise CvpApiError(msg)
            else:
                raise CvpRequestError(msg)

        if 'LOG OUT MESSAGE' in response.text:
            msg = ('%s: Request Error: session logged out' % prefix)
            raise CvpSessionLogOutError(msg)

        if 'errorCode' in response.text:
            joutput = response.json()
            if 'errorMessage' in joutput:
                err_msg = joutput['errorMessage']
            else:
                if 'errors' in joutput:
                    error_list = joutput['errors']
                else:
                    error_list = [joutput['errorCode']]
                # Build the error message from all the errors.
                err_msg = error_list[0]
                for idx in range(1, len(error_list)):
                    err_msg = '%s\n%s' % (err_msg, error_list[idx])

            msg = ('%s: Request Error: %s' % (prefix, err_msg))
            self.log.error(msg)
            raise CvpApiError(msg)

    def _login(self):
        ''' Make a POST request to CVP login authentication.
            An error can be raised from the post method call or the
            _is_good_response method call.  Any errors raised would be a good
            reason not to use this host.

            Raises:
                ConnectionError: A ConnectionError is raised if there was a
                    network problem (e.g. DNS failure, refused connection, etc)
                CvpApiError: A CvpApiError is raised if there was a JSON error.
                CvpRequestError: A CvpRequestError is raised if the request
                    is not properly constructed.
                CvpSessionLogOutError: A CvpSessionLogOutError is raised if
                    reponse from server indicates session was logged out.
                HTTPError: A HTTPError is raised if there was an invalid HTTP
                    response.
                ReadTimeout: A ReadTimeout is raised if there was a request
                    timeout when reading from the connection.
                Timeout: A Timeout is raised if there was a request timeout.
                TooManyRedirects: A TooManyRedirects is raised if the request
                    exceeds the configured number of maximum redirections
                ValueError: A ValueError is raised when there is no valid
                    CVP session.  This occurs because the previous get or post
                    request failed and no session could be established to a
                    CVP node.  Destroy the class and re-instantiate.
        '''
        # Remove any previous session id from the headers
        self.headers.pop('APP_SESSION_ID', None)
        url = self.url_prefix + '/login/authenticate.do'
        response = self.session.post(url,
                                     data=json.dumps(self.authdata),
                                     headers=self.headers,
                                     timeout=self.connect_timeout,
                                     verify=self.cert)
        self._is_good_response(response, 'Authenticate: %s' % url)

        self.cookies = response.cookies
        self.headers['APP_SESSION_ID'] = response.json()['sessionId']

    def logout(self):
        '''

        :return:
        '''
        response = self.session.post('/login/logout.do')
        if response['data'] == 'success':
            self.log.info('User logged out.')
            self.session = None
        else:
            err = 'Error trying to logout %s' % response
            self.log.error(err)

    def _make_request(self, req_type, url, timeout, data=None,
                      files=None):
        ''' Make a GET or POST request to CVP.  If the request call raises a
            timeout or CvpSessionLogOutError then the request will be retried
            on the same CVP node.  Otherwise the request will be tried on the
            next CVP node.

            Args:
                req_type (str): Either 'GET' or 'POST'.
                url (str): Portion of request URL that comes after the host.
                timeout (int): Number of seconds the client will wait between
                    bytes sent from the server.
                data (dict): Dict of key/value pairs to pass as parameters into
                    the request. Default is None.
                files (dict): Dict of file name to files for upload. Currently
                    only used for adding images to CVP. Default is None.

            Returns:
                The JSON response.

            Raises:
                ConnectionError: A ConnectionError is raised if there was a
                    network problem (e.g. DNS failure, refused connection, etc)
                CvpApiError: A CvpApiError is raised if there was a JSON error.
                CvpRequestError: A CvpRequestError is raised if the request
                    is not properly constructed.
                CvpSessionLogOutError: A CvpSessionLogOutError is raised if
                    reponse from server indicates session was logged out.
                HTTPError: A HTTPError is raised if there was an invalid HTTP
                    response.
                ReadTimeout: A ReadTimeout is raised if there was a request
                    timeout when reading from the connection.
                Timeout: A Timeout is raised if there was a request timeout.
                TooManyRedirects: A TooManyRedirects is raised if the request
                    exceeds the configured number of maximum redirections
                ValueError: A ValueError is raised when there is no valid
                    CVP session.  This occurs because the previous get or post
                    request failed and no session could be established to a
                    CVP node.  Destroy the class and re-instantiate.
        '''
        # pylint: disable=too-many-branches
        # pylint: disable=too-many-statements
        # pylint: disable=too-many-arguments
        # pylint: disable=raising-bad-type
        if not self.session:
            raise ValueError('No valid session to CVP node')
        # Keep note of which node is handling this request.
        self._last_used_node = re.match('http[s]?://(.*):',
                                        self.url_prefix).group(1)
        # Retry the request for the number of nodes.
        response = None
        for node_num in range(self.node_cnt):
            # Set full URL based on current node
            full_url = self.url_prefix + url
            try:
                response = self._send_request(req_type, full_url, timeout,
                                              data, files)
            except CvpApiError as error:
                # If this is not an Unauthorized CvpApiError raise the error
                if 'Unauthorized' not in error.msg:
                    raise error
                # If this is the final CVP node raise error
                if node_num + 1 == self.node_cnt:
                    raise error
                # Create a new session to retry on another CVP node.
                self._create_session()
                # Verify that we can connect to at least one node
                # otherwise raise the last error
                if not self.session:
                    raise error
                continue
            except (ConnectionError, HTTPError, TooManyRedirects, ReadTimeout,
                    Timeout, CvpSessionLogOutError) as error:
                # If this is the final CVP node raise error
                if node_num + 1 == self.node_cnt:
                    raise error
                # Create a new session to retry on another CVP node.
                self._create_session()
                # Verify that we can connect to at least one node
                # otherwise raise the last error
                if not self.session:
                    raise error
                continue
            break
        if response:
            return response.json()

    def _send_request(self, req_type, full_url, timeout, data=None,
                      files=None):
        ''' Make a GET or POST request to CVP.  If the request call raises a
            timeout or CvpSessionLogOutError then the request will be retried
            on the same CVP node.  Otherwise the request will be tried on the
            next CVP node.

            Args:
                req_type (str): Either 'GET' or 'POST'.
                full_url (str): Portion of request URL that comes after the
                    host.
                timeout (int): Number of seconds the client will wait between
                    bytes sent from the server.
                data (dict): Dict of key/value pairs to pass as parameters into
                    the request. Default is None.
                files (dict): Dict of file name to files for upload. Currently
                    only used for adding images to CVP. Default is None.

            Returns:
                The JSON response.

            Raises:
                ConnectionError: A ConnectionError is raised if there was a
                    network problem (e.g. DNS failure, refused connection, etc)
                CvpApiError: A CvpApiError is raised if there was a JSON error.
                CvpRequestError: A CvpRequestError is raised if the request
                    is not properly constructed.
                CvpSessionLogOutError: A CvpSessionLogOutError is raised if
                    reponse from server indicates session was logged out.
                HTTPError: A HTTPError is raised if there was an invalid HTTP
                    response.
                ReadTimeout: A ReadTimeout is raised if there was a request
                    timeout when reading from the connection.
                Timeout: A Timeout is raised if there was a request timeout.
                TooManyRedirects: A TooManyRedirects is raised if the request
                    exceeds the configured number of maximum redirections
                ValueError: A ValueError is raised when there is no valid
                    CVP session.  This occurs because the previous get or post
                    request failed and no session could be established to a
                    CVP node.  Destroy the class and re-instantiate.
        '''
        # pylint: disable=too-many-branches
        # pylint: disable=too-many-statements
        # pylint: disable=too-many-arguments
        # pylint: disable=raising-bad-type
        # For get or post requests apply both the connect and read timeout.
        timeout = (self.connect_timeout, timeout)
        for req_try in range(self.NUM_RETRY_REQUESTS):
            try:
                if req_type == 'GET':
                    response = self.session.get(full_url,
                                                cookies=self.cookies,
                                                headers=self.headers,
                                                timeout=timeout,
                                                verify=self.cert)
                else:
                    if files is None:
                        response = self.session.post(full_url,
                                                     cookies=self.cookies,
                                                     data=json.dumps(data),
                                                     headers=self.headers,
                                                     timeout=timeout,
                                                     verify=self.cert)
                    else:
                        fhs = dict()
                        fhs['Accept'] = self.headers['Accept']
                        fhs['APP_SESSION_ID'] = self.headers['APP_SESSION_ID']
                        response = self.session.post(full_url,
                                                     cookies=self.cookies,
                                                     headers=fhs,
                                                     timeout=timeout,
                                                     verify=self.cert,
                                                     files=files)
            except (ConnectionError, HTTPError, TooManyRedirects) as error:
                # Any of these errors is a good reason to try another CVP node
                self.log.error(error)
                raise error
            except (ReadTimeout, Timeout) as error:
                self.log.debug(error)
                # If there was a timeout and this is not the final try,
                # retry this request to the same node. If this is the final
                # try raise the error so another CVP node can be tried
                if req_try + 1 == self.NUM_RETRY_REQUESTS:
                    raise error
                continue

            try:
                self._is_good_response(response, '%s: %s ' %
                                       (req_type, full_url))
            except CvpSessionLogOutError as error:
                self.log.debug(error)
                # Retry the request to the same node if there was a CVP session
                # logout. Reset the session which will login. If a valid
                # session comes back then clear the error so this request will
                # be retried on the same node.
                if req_try + 1 == self.NUM_RETRY_REQUESTS:
                    raise error
                else:
                    self._reset_session()
                    if not self.session:
                        raise error
                    continue
            except CvpApiError as error:
                self.log.debug(error)
                if 'Unauthorized' in error.msg:
                    # Retry the request to the same node if there was an
                    # Unauthorized User error because this is how CVP responds
                    # to a logged out users requests in 2017.1 and beyond.
                    # Reset the session which will login. If a valid
                    # session comes back then clear the error so this request
                    # will be retried on the same node.
                    if req_try + 1 == self.NUM_RETRY_REQUESTS:
                        raise error
                    else:
                        self._reset_session()
                        if not self.session:
                            raise error
                        continue
                else:
                    # pylint: disable=raising-bad-type
                    raise error
            return response

    def get(self, url, timeout=30):
        ''' Make a GET request to CVP.  If the request call raises an error
            or if the JSON response contains a CVP session related error then
            retry the request on another CVP node.

            Args:
                url (str): Portion of request URL that comes after the host.
                timeout (int): Number of seconds the client will wait between
                    bytes sent from the server.  Default value is 30 seconds.

            Returns:
                The JSON response.

            Raises:
                ConnectionError: A ConnectionError is raised if there was a
                    network problem (e.g. DNS failure, refused connection, etc)
                CvpApiError: A CvpApiError is raised if there was a JSON error.
                CvpRequestError: A CvpRequestError is raised if the request
                    is not properly constructed.
                CvpSessionLogOutError: A CvpSessionLogOutError is raised if
                    reponse from server indicates session was logged out.
                HTTPError: A HTTPError is raised if there was an invalid HTTP
                    response.
                ReadTimeout: A ReadTimeout is raised if there was a request
                    timeout when reading from the connection.
                Timeout: A Timeout is raised if there was a request timeout.
                TooManyRedirects: A TooManyRedirects is raised if the request
                    exceeds the configured number of maximum redirections
                ValueError: A ValueError is raised when there is no valid
                    CVP session.  This occurs because the previous get or post
                    request failed and no session could be established to a
                    CVP node.  Destroy the class and re-instantiate.
        '''
        return self._make_request('GET', url, timeout)

    def post(self, url, data=None, files=None, timeout=30):
        ''' Make a POST request to CVP.  If the request call raises an error
            or if the JSON response contains a CVP session related error then
            retry the request on another CVP node.

            Args:
                url (str): Portion of request URL that comes after the host.
                data (dict): Dict of key/value pairs to pass as parameters into
                    the request. Default is None.
                files (dict): Dict of file name to files for upload. Currently
                    only used for adding images to CVP. Default is None.
                timeout (int): Number of seconds the client will wait between
                    bytes sent from the server.  Default value is 30 seconds.

            Returns:
                The JSON response.

            Raises:
                ConnectionError: A ConnectionError is raised if there was a
                    network problem (e.g. DNS failure, refused connection, etc)
                CvpApiError: A CvpApiError is raised if there was a JSON error.
                CvpRequestError: A CvpRequestError is raised if the request
                    is not properly constructed.
                CvpSessionLogOutError: A CvpSessionLogOutError is raised if
                    reponse from server indicates session was logged out.
                HTTPError: A HTTPError is raised if there was an invalid HTTP
                    response.
                ReadTimeout: A ReadTimeout is raised if there was a request
                    timeout when reading from the connection.
                Timeout: A Timeout is raised if there was a request timeout.
                TooManyRedirects: A TooManyRedirects is raised if the request
                    exceeds the configured number of maximum redirections
                ValueError: A ValueError is raised when there is no valid
                    CVP session.  This occurs because the previous get or post
                    request failed and no session could be established to a
                    CVP node.  Destroy the class and re-instantiate.
        '''
        return self._make_request('POST', url, timeout, data=data, files=files)
