from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import ipaddress


class FilterModule(object):

    def net(self, val):
        try:
            return ipaddress.ip_network(val, strict=True)
        except ValueError:
            return

    def subnet(self, val):
        if self.validate(val):
            return ipaddress.ip_network(val, strict=False)
        return

    def netmask(self, val):
        valid_subnet = self.subnet(val)
        if valid_subnet:
            return valid_subnet.netmask

    def prefix(self, val):
        valid_subnet = self.subnet(val)
        if valid_subnet:
            return valid_subnet.prefixlen
        return

    def size(self, val):
        valid_subnet = self.subnet(val)
        if valid_subnet:
            return 2**(valid_subnet.max_prefixlen - valid_subnet.prefixlen)
        return

    def network(self, val):
        valid_subnet = self.subnet(val)
        if valid_subnet:
            return valid_subnet.network_address
        return

    def address(self, val):
        try:
            if isinstance(val, str) and '/' in val:
                try:
                    ipaddress.ip_network(val, strict=True)
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

    def defaultattr(self, input_val, ip_address):
        try:
            input_val_int = int(input_val)
            if self.size(ip_address) == 1:
                return ip_address
            else:
                max_ips = self.size(ip_address)
                if input_val_int < max_ips:
                    network_address = ipaddress.ip_network(ip_address, strict=False)
                    calc_ip = str(network_address.network_address + input_val_int)
                    prefix = network_address.prefixlen
                    return f'{calc_ip}/{prefix}'
                else:
                    return
        except ValueError:
            subnet_a = self.subnet(input_val)
            subnet_b = ipaddress.ip_network(ip_address, strict=False)
            if subnet_a and subnet_a.version == subnet_b.version and subnet_b.subnet_of(subnet_a):
                return ip_address
            else:
                return

    def ipaddr(self, ip_addresses, method='validate'):
        result = None
        if type(ip_addresses) in (str, int):
            try:
                result = getattr(self, method)(ip_addresses)
            except (TypeError, AttributeError):
                if self.validate(ip_addresses):
                    result = self.defaultattr(method, str(self.validate(ip_addresses)))
            if result is not None:
                result = str(result)
        elif type(ip_addresses) is list:
            result = []
            for ip_address in ip_addresses:
                result.append(self.ipaddr(ip_address, method=method))

        return result

    def ipmath(self, ip_addresses, add_val):
        result = None
        if type(ip_addresses) in (str, int) and self.validate(ip_addresses):
            result = str(self.validate(ip_addresses) + int(add_val)).split('/', maxsplit=1)[0]
        elif type(ip_addresses) is list:
            result = []
            for ip_address in ip_addresses:
                result.append(self.ipmath(ip_address, add_val))

        return result

    def filters(self):
        return {
            'ipaddr': self.ipaddr,
            'ipmath': self.ipmath,
        }
