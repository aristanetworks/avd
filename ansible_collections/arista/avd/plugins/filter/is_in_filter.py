#
# device-filter filter
#
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from jinja2 import TemplateError
from itertools import count, groupby
from ansible.errors import AnsibleFilterError
import re


class FilterModule(object):

    def is_in_filter(self, hostname, hostname_filter):
        if hostname_filter is None:
            hostname_filter = ["all"]
        if "all" in hostname_filter:
            return True
        elif any(element in hostname for element in hostname_filter):
            return True
        return False

    def filters(self):
        return {
            'is_in_filter': self.is_in_filter,
        }
