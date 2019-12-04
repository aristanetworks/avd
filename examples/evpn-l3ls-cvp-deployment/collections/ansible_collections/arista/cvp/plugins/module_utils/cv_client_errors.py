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

''' CVP Restful API client exception classes
'''


class CvpClientError(Exception):
    ''' CVP Restful API client error
    '''
    def __init__(self, msg):
        Exception.__init__(self)
        self.msg = msg

    def __str__(self):
        return self.msg


class CvpApiError(CvpClientError):
    ''' Error encountered related to the CVP API request.
    '''
    def __init__(self, msg):
        CvpClientError.__init__(self, msg)


class CvpLoginError(CvpClientError):
    ''' Error encountered trying to login into CVP.
    '''
    def __init__(self, msg):
        CvpClientError.__init__(self, msg)


class CvpRequestError(CvpClientError):
    ''' CVP request not properly constructed.
    '''
    def __init__(self, msg):
        CvpClientError.__init__(self, msg)


class CvpSessionLogOutError(CvpClientError):
    ''' Current CVP session has been logged out.
    '''
    def __init__(self, msg):
        CvpClientError.__init__(self, msg)
