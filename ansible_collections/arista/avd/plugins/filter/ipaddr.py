from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import ipaddress
from jinja2.runtime import Undefined


class FilterModule(object):

    def net(self, val, version=None):
        if isinstance(val, int) or '/' not in val:
            return
        try:
            network_address = ipaddress.ip_network(val, strict=True)
            if isinstance(version, int) and network_address.version != version:
                return
            return network_address
        except ValueError:
            return

    def subnet(self, val, version=None):
        if self.validate(val, version):
            return ipaddress.ip_network(val, strict=False)
        return

    def netmask(self, val, version=None):
        valid_subnet = self.subnet(val, version)
        if valid_subnet:
            return valid_subnet.netmask
        return

    def prefix(self, val, version=None):
        valid_subnet = self.subnet(val, version)
        if valid_subnet:
            return valid_subnet.prefixlen
        return

    def size(self, val, version=None):
        valid_subnet = self.subnet(val, version)
        if valid_subnet:
            return 2**(valid_subnet.max_prefixlen - valid_subnet.prefixlen)
        return

    def network(self, val, version=None):
        valid_subnet = self.subnet(val, version)
        if valid_subnet:
            return valid_subnet.network_address
        return

    def address(self, val, version=None):
        try:
            if isinstance(val, str) and '/' in val:
                try:
                    if ipaddress.ip_network(val, strict=True):
                        return
                except ValueError:
                    ip = ipaddress.ip_interface(val).ip
            else:
                ip = ipaddress.ip_address(val)
            if isinstance(version, int) and ip.version != version:
                return
            return ip
        except ValueError:
            return

    def validate(self, val, version=None):
        try:
            if isinstance(val, str) and '/' in val:
                ip = ipaddress.ip_interface(val)
            else:
                ip = ipaddress.ip_address(val)
            if isinstance(version, int) and ip.version != version:
                return
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

    def ipaddr(self, ip_addresses, method='validate', version=None):
        result = None
        if isinstance(ip_addresses, (Undefined, bool)) or ip_addresses in (None, '', []):
            return

        if isinstance(ip_addresses, list):
            result = []
            for ip_address in ip_addresses:
                if single_entry := self.ipaddr(ip_address, method=method, version=version):
                    result.append(single_entry)
        else:
            if not isinstance(ip_addresses, (str, int)):
                ip_addresses = str(ip_addresses)
            try:
                result = getattr(self, method)(ip_addresses, version=version)
            except (TypeError, AttributeError):
                if self.validate(ip_addresses):
                    result = self.defaultattr(method, str(self.validate(ip_addresses, version)))
            if result is not None and not isinstance(result, int):
                result = str(result)

        return result

    def ipmath(self, ip_addresses, add_val):
        result = None
        if isinstance(ip_addresses, (Undefined, bool)) or ip_addresses in (None, '', []):
            return
        if isinstance(ip_addresses, list):
            result = []
            for ip_address in ip_addresses:
                if self.ipmath(ip_address, add_val):
                    result.append(self.ipmath(ip_address, add_val))
        else:
            if not isinstance(ip_addresses, (str, int)):
                ip_addresses = str(ip_addresses)
            if self.validate(ip_addresses):
                result = str(self.validate(ip_addresses) + int(add_val)).split('/', maxsplit=1)[0]

        return result

    def ipv4(self, ip_addresses, method='validate'):
        return self.ipaddr(ip_addresses=ip_addresses, method=method, version=4)

    def ipv6(self, ip_addresses, method='validate'):
        return self.ipaddr(ip_addresses=ip_addresses, method=method, version=6)

    def filters(self):
        return {
            'ipaddr': self.ipaddr,
            'ipmath': self.ipmath,
            'ipv4': self.ipv4,
            'ipv6': self.ipv6,
        }
