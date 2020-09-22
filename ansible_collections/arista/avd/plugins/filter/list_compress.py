#
# list_compress filter
#
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from itertools import count, groupby
from ansible.errors import AnsibleFilterError


class FilterModule(object):

    def list_compress(self, list_to_compress):
        if not isinstance(list_to_compress, list):
            raise AnsibleFilterError('value must be of type list, got %s' % type(list_to_compress))
        G = (list(x) for y, x in groupby(sorted(list_to_compress), lambda x, c=count(): next(c) - x))
        return (",".join("-".join(map(str, (g[0], g[-1])[:len(g)])) for g in G))

    def filters(self):
        return {
            'list_compress': self.list_compress,
        }
