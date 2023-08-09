# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
#
# range_expand filter
#
from __future__ import absolute_import, division, print_function

from ansible.errors import AnsibleFilterError

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError
from ansible_collections.arista.avd.plugins.plugin_utils.utils.range_expand import range_expand_utils

__metaclass__ = type


def range_expand(range_to_expand):
    try:
        return range_expand_utils(range_to_expand, prefix="")
    except AristaAvdError as exc:
        raise AnsibleFilterError(exc) from exc


class FilterModule(object):
    def filters(self):
        return {
            "range_expand": range_expand,
        }
