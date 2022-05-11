from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import ipaddress

class FilterModule(object):

    def net(self, val):
        if self.validate(val):
            return ipaddress.ip_network(val, strict = False)
        return

    def netmask(self, val):
        valid_subnet = self.net(val)
        if valid_subnet:
            return valid_subnet.netmask

    def prefix(self, val):
        valid_subnet = self.net(val)
        if valid_subnet:
            return valid_subnet.prefixlen
        return

    def size(self, val):
        valid_subnet = self.net(val)
        if valid_subnet:
            return 2**(valid_subnet.max_prefixlen-valid_subnet.prefixlen)
        return

    def network(self, val):
        valid_subnet = self.net(val)
        if valid_subnet:
            return valid_subnet.network_address
        return

    def address(self, val):
        try:
            if isinstance(val, str) and '/' in val:
                try:
                    ipaddress.ip_network(val)
                    return
                except ValueError:
                    ip = ipaddress.ip_interface(val).ip
            else:
                ip = ipaddress.ip_address(val)
            return ip
        except ValueError:
            return

    def validate(self, val):
        try:
            if isinstance(val, str) and '/' in val:
                ip = ipaddress.ip_interface(val)
            else:
                ip = ipaddress.ip_address(val)
            return ip
        except ValueError:
            return

    def ipaddr(self, ip_addresses, method = 'validate'):
        result = None
        if type(ip_addresses) in (str,int):
            result = getattr(self, method)(ip_addresses)
            if result is not None:
                result = str(result)
        elif type(ip_addresses) is list:
            result = []
            for ip_address in ip_addresses:
                result.append(self.ipaddr(ip_address, method = method))

        return result

    def ipmath(self, ip_addresses, add_val):
        result = None
        if type(ip_addresses) in (str, int) and self.validate(ip_addresses):
            result = str(self.validate(ip_addresses) + int(add_val)).split('/')[0]
        elif type(ip_addresses) is list:
            result = []
            for ip_address in ip_addresses:
                result.append(self.ipmath(ip_address, add_val))

        return result

    def filters(self):
        return {
            'ipaddr': self.ipaddr,
        }
