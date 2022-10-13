#
# arista.avd.bgp_valid_password
#
# Jinja test examples:
# {% if bgp_password is arista.avd.bgp_valid_password(neighbor_or_peer_group_name) %}  =>  True / False

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from jinja2.runtime import Undefined

from ansible_collections.arista.avd.plugins.plugin_utils.bgp_utils import cbc_check_password
from ansible_collections.arista.avd.plugins.plugin_utils.utils import AristaAvdError


def bgp_valid_password(value, key):
    """
    bgp_valid_password - Ansible Test

    Validate if a given password (value) is decryptable against the key

    Parameters
    ----------
    value : str
        The encrypted password
    key : str
        Either the Neighbor IP or the Peer Group Name for which the password was encrypted.
        The function will add the `_passwd` suffix itself.

    Returns
    -------
    boolean
        True if the password is decryptable

    Raises:
    -------
    AristaAvdError if the password is not decryptable

    """
    if isinstance(value, Undefined) or value is None or not isinstance(value, str):
        # Invalid value - return false
        return False
    elif isinstance(key, Undefined) or value is None or not isinstance(key, str):
        # Invalid value - return false
        return False
    b_key = bytes(f"{key}_passwd", encoding="utf-8")
    b_value = bytes(value, encoding="utf-8")
    if cbc_check_password(b_key, b_value) is True:
        return True

    raise AristaAvdError(f"The BGP encrypted password {value} cannot be decrypted for {key}!")


class TestModule(object):
    def tests(self):
        return {
            "bgp_valid_password": bgp_valid_password,
        }
