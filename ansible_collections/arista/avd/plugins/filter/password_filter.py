"""
Encrypt / Decrypt filters
"""

from ansible_collections.arista.avd.plugins.plugin_utils.bgp_utils import cbc_decrypt, cbc_encrypt
from ansible_collections.arista.avd.plugins.plugin_utils.utils import AristaAvdError, AristaAvdMissingVariableError


##############
# BGP
##############
def bgp_encrypt(password, key=None, usebase64=True) -> str:
    """
    Encrypt a password. The key is either <PEER_GROUP_NAME>_passwd or <NEIGHBOR_IP>_passwd

    Returns the encrypted password as a string
    """
    if not key:
        raise AristaAvdMissingVariableError("Key is required for BGP encryption")

    data = bytes(password, encoding="utf-8")
    key = bytes(f"{key}_passwd", encoding="utf-8")

    return cbc_encrypt(key, data, usebase64).decode()


def bgp_decrypt(password, key=None, usebase64=True) -> str:
    """
    Decrypt a password. The key is either <PEER_GROUP_NAME>_passwd or <NEIGHBOR_IP>_passwd

    Returns the decrypted password as a string

    Raises AristaAvdError is decryption fails
    """
    if not key:
        raise AristaAvdMissingVariableError("Key is required for BGP decryption")

    data = bytes(password, encoding="utf-8")
    key = bytes(f"{key}_passwd", encoding="utf-8")

    try:
        return cbc_decrypt(key, data, usebase64).decode()
    except Exception as exc:
        raise AristaAvdError from exc


##############
# GENERIC
##############
METHODS_DIR = {"bgp": (bgp_encrypt, bgp_decrypt)}


def encrypt(value, passwd_type=None, key=None, **kwargs) -> str:
    """
    Umbrella function to execute the correct encrypt method based on the input type
    """
    if not passwd_type:
        raise AristaAvdMissingVariableError("type keyword must be present to use this test")
    try:
        encrypt_method = METHODS_DIR[passwd_type][0]
    except KeyError as exc:
        raise AristaAvdError("Type {passwd_type} is not supported for the encrypt filter") from exc
    return encrypt_method(value, key=key, **kwargs)


def decrypt(value, passwd_type=None, key=None, **kwargs) -> str:
    """
    Umbrella function to execute the correct decrypt method based on the input type
    """
    if not passwd_type:
        raise AristaAvdMissingVariableError("type keyword must be present to use this test")
    try:
        decrypt_method = METHODS_DIR[passwd_type][1]
    except KeyError as exc:
        raise AristaAvdError("Type {passwd_type} is not supported for the decrypt filter") from exc
    return decrypt_method(value, key=key, **kwargs)


class FilterModule(object):
    def filters(self):
        return {
            "encrypt": encrypt,
            "decrypt": decrypt,
        }
