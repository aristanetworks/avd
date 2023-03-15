"""
Encrypt / Decrypt filters
"""
from __future__ import annotations

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError, AristaAvdMissingVariableError
from ansible_collections.arista.avd.plugins.plugin_utils.password_utils import cbc_decrypt, cbc_encrypt


##############
# OSPF
##############
def ospf_encrypt(password: str, key: str, auth_algo: str | None = None, key_id: str | None = None) -> str:
    """
    Encrypt a password.

    <key> should be the interface name e.g. "Ethernet1"

    The key is transformed to either::
        <key>_passwd for simple authentication
    or
        <key>_<auth_algo>Key_<key_id> for message digest keys

    Returns the encrypted password as a string
    """
    if not key:
        raise AristaAvdMissingVariableError("Key is required for OSPF encryption")

    if not password:
        raise AristaAvdMissingVariableError("Password is required for OSPF encryption")

    if not isinstance(password, str):
        raise AristaAvdError(f"Password MUST be of type 'str' but is of type {type(password)}")

    data = bytes(password, encoding="UTF-8")

    if auth_algo is not None and key_id is not None:
        # message digest authentication
        key_b = bytes(f"{key}_{auth_algo}Key_{key_id}", encoding="UTF-8")
    elif auth_algo is not None or key_id is not None:
        raise AristaAvdError("For OSPF message digest keys, both auth_algo and key_id are required")
    else:
        # None set - assumes simple authentication
        key_b = bytes(f"{key}_passwd", encoding="UTF-8")

    return cbc_encrypt(key_b, data).decode()


def ospf_decrypt(password: str, key: str, auth_algo: str | None = None, key_id: str | None = None) -> str:
    """
    Decrypt a password.

    <key> should be the interface name e.g. "Ethernet1"

    The key is transformed to either::
        <key>_passwd for simple authentication
    or
        <key>_<auth_algo>Key_<key_id> for message digest keys

    Returns the decrypted password as a string

    Raises AristaAvdError is decryption fails
    """
    if not key:
        raise AristaAvdMissingVariableError("Key is required for OSPF decryption")

    if not password:
        raise AristaAvdMissingVariableError("Password is required for OSPF decryption")

    if not isinstance(password, str):
        raise AristaAvdError(f"Password MUST be of type 'str' but is of type {type(password)}")

    data = bytes(password, encoding="UTF-8")

    if auth_algo is not None and key_id is not None:
        # message digest authentication
        key_b = bytes(f"{key}_{auth_algo}Key_{key_id}", encoding="UTF-8")
    elif auth_algo is not None or key_id is not None:
        raise AristaAvdError("For OSPF message digest keys, both auth_algo and key_id are required")
    else:
        # None set - assumes simple authentication
        key_b = bytes(f"{key}_passwd", encoding="UTF-8")

    try:
        return cbc_decrypt(key_b, data).decode()
    except Exception as exc:
        raise AristaAvdError("OSPF password decryption failed - check the input parameters") from exc


##############
# BGP
##############
def bgp_encrypt(password: str, key) -> str:
    """
    Encrypt a password. The key is either <PEER_GROUP_NAME>_passwd or <NEIGHBOR_IP>_passwd

    Returns the encrypted password as a string
    """
    if not key:
        raise AristaAvdMissingVariableError("Key is required for BGP encryption")

    if not password:
        raise AristaAvdMissingVariableError("Password is required for BGP encryption")

    if not isinstance(password, str):
        raise AristaAvdError(f"Password MUST be of type 'str' but is of type {type(password)}")

    data = bytes(password, encoding="UTF-8")
    key = bytes(f"{key}_passwd", encoding="UTF-8")

    return cbc_encrypt(key, data).decode()


def bgp_decrypt(password: str, key) -> str:
    """
    Decrypt a password. The key is either <PEER_GROUP_NAME>_passwd or <NEIGHBOR_IP>_passwd

    Returns the decrypted password as a string

    Raises AristaAvdError is decryption fails
    """
    if not key:
        raise AristaAvdMissingVariableError("Key is required for BGP decryption")

    if not password:
        raise AristaAvdMissingVariableError("Password is required for BGP decryption")

    if not isinstance(password, str):
        raise AristaAvdError(f"Password MUST be of type 'str' but is of type {type(password)}")

    data = bytes(password, encoding="UTF-8")
    key = bytes(f"{key}_passwd", encoding="UTF-8")

    try:
        return cbc_decrypt(key, data).decode()
    except Exception as exc:
        raise AristaAvdError("BGP password decryption failed - check the input parameters") from exc


##############
# GENERIC
##############
METHODS_DIR = {
    "bgp": (bgp_encrypt, bgp_decrypt),
    "ospf": (ospf_encrypt, ospf_decrypt),
}


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
    return encrypt_method(str(value), key=key, **kwargs)


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
    return decrypt_method(str(value), key=key, **kwargs)


class FilterModule(object):
    def filters(self):
        return {
            "encrypt": encrypt,
            "decrypt": decrypt,
        }
