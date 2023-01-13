from __future__ import absolute_import, division, print_function

__metaclass__ = type
# from ansible_collections.arista.avd.roles.eos_designs.python_modules.ip_addressing.avdipaddressing import AvdIpAddressing
from ansible_collections.arista.avd.plugins.plugin_utils.ip_addressing_utils import _ip

(pool, prefixlen, subnet_offset, ip_offset) = ("1.2.3.4/24", 32, 1, 0)


class TestAvdIpAddressing:
    def test_ip_with_default_values(self):
        resp = _ip(pool, prefixlen, subnet_offset, ip_offset)
        assert resp == "1.2.3.1"
