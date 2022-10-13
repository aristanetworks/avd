"""
Encrypt / Decrypt filters
"""

from ansible_collections.arista.avd.plugins.plugin_utils.bgp_utils import cbc_decrypt, cbc_encrypt
from ansible_collections.arista.avd.plugins.plugin_utils.utils import AristaAvdError, AristaAvdMissingVariableError


##############
# BGP
##############
def _parse_bgp_input(input_dict: dict) -> (bytes, bytes, bool):
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


def bgp_encrypt(input_dict: dict) -> str:
    """
    Encrypt a password. The key is either <PEER_GROUP_NAME>_passwd or <NEIGHBOR_IP>_passwd

    Returns the encrypted password as a string
    """
    key, data, usebase64 = _parse_bgp_input(input_dict)
    return cbc_encrypt(key, data, usebase64).decode()


def bgp_decrypt(input_dict: dict) -> str:
    """
    Decrypt a password. The key is either <PEER_GROUP_NAME>_passwd or <NEIGHBOR_IP>_passwd

    Returns the decrypted password as a string

    Raises AristaAvdError is decryption fails
    """
    key, data, usebase64 = _parse_bgp_input(input_dict)
    try:
        return cbc_decrypt(key, data, usebase64).decode()
    except Exception as exc:
        raise AristaAvdError from exc


##############
# GENERIC
##############
METHODS_DIR = {"bgp": (bgp_encrypt, bgp_decrypt)}


def _get_type(input_dict: dict) -> str:
    """
    Get the type key out of the directory to lower case

    returns the type key from the input_dict

    """
    try:
        return input_dict["type"].lower()
    except KeyError as exc:
        raise AristaAvdMissingVariableError("type keyword must be present to use this filter") from exc


def encrypt(input_dict) -> str:
    """
    Umbrella function to execute the correct encrypt method based on the input type
    """
    passwd_type = _get_type(input_dict)
    try:
        encrypt_method = METHODS_DIR[passwd_type][0]
    except KeyError as exc:
        raise AristaAvdError("Type {passwd_type} is not supported for the encrypt filter") from exc
    return encrypt_method(input_dict)


def decrypt(input_dict) -> str:
    """
    Umbrella function to execute the correct decrypt method based on the input type
    """
    passwd_type = _get_type(input_dict)
    try:
        decrypt_method = METHODS_DIR[passwd_type][1]
    except KeyError as exc:
        raise AristaAvdError("Type {passwd_type} is not supported for the decrypt filter") from exc
    return decrypt_method(input_dict)


class FilterModule(object):
    def filters(self):
        return {
            "encrypt": encrypt,
            "decrypt": decrypt,
        }
