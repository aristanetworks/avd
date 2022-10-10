"""
bgp_encrypt / bgp_decrypt filters
"""

from ansible_collections.arista.avd.plugins.plugin_utils.bgp_utils import cbc_decrypt, cbc_encrypt
from ansible_collections.arista.avd.plugins.plugin_utils.utils import AristaAvdError, AristaAvdMissingVariableError


def bgp_encrypt(input_dict: dict) -> bytes:
    """
    Encrypt a password. The key is either <PEER_GROUP_NAME>_passwd or <NEIGHBOR_IP>_passwd

    Returns the encrypted password as a string
    """
    key, data, usebase64 = _parse_input(input_dict)
    return cbc_encrypt(key, data, usebase64).decode()


def bgp_decrypt(input_dict: dict) -> bytes:
    """
    Decrypt a password. The key is either <PEER_GROUP_NAME>_passwd or <NEIGHBOR_IP>_passwd

    Returns the decrypted password as a string
    """
    key, data, usebase64 = _parse_input(input_dict)
    try:
        return cbc_decrypt(key, data, usebase64).decode()
    except Exception as exc:
        raise AristaAvdError from exc


def _parse_input(input_dict: dict) -> (bytes, bytes, bool):
    """
    Verify that the necessary input paramaters are present

    The key (either neighbor IP or BGP peer group is augmented with _passwd as is expected in the encrypt and decrypt functions on EOS

    returns a tuple (key, password, usebase64) to be used in bgp_encrypt and bgp_decrypt
    """
    try:
        key = input_dict["key"]
        password = bytes(input_dict["password"], encoding="utf-8")
    except KeyError as exc:
        raise AristaAvdMissingVariableError() from exc
    key = bytes(f"{key}_passwd", encoding="utf-8")

    usebase64 = input_dict.get("use_base64", True)

    return key, password, usebase64


class FilterModule(object):
    def filters(self):
        return {
            "bgp_encrypt": bgp_encrypt,
            "bgp_decrypt": bgp_decrypt,
        }
