#
# range_expand filter
#
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from itertools import count, groupby
import re
from ansible.errors import AnsibleFilterError


class FilterModule(object):

    def range_expand(self, range_to_expand):
        if not (isinstance(range_to_expand, list) or isinstance(range_to_expand, str)):
            raise AnsibleFilterError(f"value must be of type list or str, got {type(range_to_expand)}")

        result = []

        # If we got a list, unpack it and run this function recursively
        if isinstance(range_to_expand, list):
            for r in range_to_expand:
                result.extend(self.range_expand(r))

        # Must be a str now
        else:
            prefix = ""

            # Unpack list in string
            for one_range in range_to_expand.split(','):

                # Find prefix (if any)
                regex = r"^(.*?)(((\d+)-)?(\d+)\/)?(((\d+)-)?(\d+))(\.((\d+)-)?(\d+))?"
                # Groups one-by-one:
                # Group 1  (.*?)                                                        matches prefix ex. Ethernet, Eth, Po, Port-Channel
                # Group 2       (((\d+)-)?(\d+)\/)?                                     matches module(s) and slash ex. 12/, 1-3/
                # Group 3        ((\d+)-)?                                              matches first module and dash ex. 1-
                # Group 4         (\d+)                                                 matches first module ex. 1
                # Group 5                 (\d+)                                         matches last module ex. 12, 3
                # Group 6                          (((\d+)-)?(\d+))                     matches interface(s) ex. 47, 1-48
                # Group 7                           ((\d+)-)?                           matches first interfaces and dash ex. 1-
                # Group 8                            (\d+)                              matches first interface
                # Group 9                                    (\d+)                      matches last interface ex. 47, 48
                # Group 10                                         (\.((\d+)-)?(\d+))?  matches dot and sub-interface(s) ex. .141, .12-15
                # Group 11                                            ((\d+)-)?         matches first sub-interface and dash ex. 12-
                # Group 12                                             (\d+)            matches first sub-interface ex. 12
                # Group 13                                                     (\d+)    matches last sub-interface ex. 141, 15
                # Remember that the groups() object is 0-based and the group numbers above are 1-based
                search_result = re.search(regex, one_range)
                if search_result and len(search_result.groups()) == 13:
                    groups = search_result.groups()
                    first_module = last_module = first_interface = last_interface = first_subinterface = last_subinterface = None
                    # Set prefix if found (otherwise use last set prefix)
                    if groups[0]:
                        prefix = groups[0]
                    if groups[4]:
                        last_module = int(groups[4])
                    if groups[3]:
                        first_module = int(groups[3])
                    else:
                        first_module = last_module
                    if groups[8]:
                        last_interface = int(groups[8])
                    if groups[7]:
                        first_interface = int(groups[7])
                    else:
                        first_interface = last_interface
                    if groups[12]:
                        last_subinterface = int(groups[12])
                    if groups[11]:
                        first_subinterface = int(groups[11])
                    else:
                        first_subinterface = last_subinterface

                    # expand modules if found
                    if last_module:
                        for module in range(first_module, last_module + 1):

                            # expand interfaces
                            for interface in range(first_interface, last_interface + 1):

                                # expand sub-interfaces if found
                                if last_subinterface:
                                    for subinterface in range(first_subinterface, last_subinterface + 1):
                                        result.append(f"{prefix}{module}/{interface}.{subinterface}")
                                else:
                                    result.append(f"{prefix}{module}/{interface}")
                    else:
                        # expand interfaces
                        for interface in range(first_interface, last_interface + 1):

                            # expand sub-interfaces if found
                            if last_subinterface:
                                for subinterface in range(first_subinterface, last_subinterface + 1):
                                    result.append(f"{prefix}{interface}.{subinterface}")
                            else:
                                result.append(f"{prefix}{interface}")
                else:
                    raise AnsibleFilterError(f"Invalid range, got {one_range} and found {search_result.groups()}")
        return result

    def filters(self):
        return {
            'range_expand': self.range_expand,
        }
