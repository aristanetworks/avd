#!/usr/bin/env python
# coding: utf-8 -*-
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


def strip_null_from_data(data, strip_values_tuple=(None,)):
    """
    strip_null_from_data Generic function to strip null entries regardless type of variable.

    Parameters
    ----------
    data : Any
        Data to look for null content to strip out

    Returns
    -------
    Any
        Cleaned data with no null.
    """
    if isinstance(data, dict):
        return strip_empties_from_dict(data, strip_values_tuple)
    elif isinstance(data, list):
        return strip_empties_from_list(data, strip_values_tuple)
    return data


def strip_empties_from_list(data, strip_values_tuple=(None, "", [], {},)):
    """
    strip_empties_from_list Remove entries with null value from a list

    Parameters
    ----------
    data : Any
        data to filter
    strip_values_tuple : tuple, optional
        Value to remove from data, by default (None, "", [], {},)

    Returns
    -------
    Any
        Cleaned list with no strip_values_tuple
    """
    new_data = []
    for v in data:
        if isinstance(v, dict):
            v = strip_empties_from_dict(v, strip_values_tuple)
        elif isinstance(v, list):
            v = strip_empties_from_list(v, strip_values_tuple)
        if v not in strip_values_tuple:
            new_data.append(v)
    return new_data


def strip_empties_from_dict(data, strip_values_tuple=(None, "", [], {},)):
    """
    strip_empties_from_dict Remove entries with null value from a dict

    Parameters
    ----------
    data : Any
        data to filter
    strip_values_tuple : tuple, optional
        Value to remove from data, by default (None, "", [], {},)

    Returns
    -------
    Any
        Cleaned dict with no strip_values_tuple
    """
    new_data = {}
    for k, v in data.items():
        if isinstance(v, dict):
            v = strip_empties_from_dict(v, strip_values_tuple)
        elif isinstance(v, list):
            v = strip_empties_from_list(v, strip_values_tuple)
        if v not in strip_values_tuple:
            new_data[k] = v
    return new_data
