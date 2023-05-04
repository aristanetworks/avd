"""
Encrypt / Decrypt filters
"""
from __future__ import annotations

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError, AristaAvdMissingVariableError
from ansible_collections.arista.avd.plugins.plugin_utils.password_utils import cbc_decrypt, cbc_encrypt


def _validate_password_and_key(password: str, key: str) -> None:
    """
    Validates the password and key values

    Raises AristaAvdMissingVariableError if one is missinge
    Raises AristaAvdError if Password is not a string
    """
    if not key:
        raise AristaAvdMissingVariableError("Key is required for encryption")

    if not password:
        raise AristaAvdMissingVariableError("Password is required for encryption")

    if not isinstance(password, str):
        raise AristaAvdError(f"Password MUST be of type 'str' but is of type {type(password)}")


##############
# OSPF
##############
def ospf_simple_encrypt(password: str, key: str) -> str:
    """
    Encrypt a password for OSPF simple authentication

    <key> should be the interface name e.g. "Ethernet1"

    The key is transformed to : <key>_passwd for simple authentication

    Returns the encrypted password as a string
    """
    _validate_password_and_key(password, key)

    data = bytes(password, encoding="UTF-8")
    key_b = bytes(f"{key}_passwd", encoding="UTF-8")

    return cbc_encrypt(key_b, data).decode()


def ospf_simple_decrypt(password: str, key: str) -> str:
    """
    Decrypt a password for OSPF simple authentication

    <key> should be the interface name e.g. "Ethernet1"

    The key is transformed to either: <key>_passwd for simple authentication

    Returns the decrypted password as a string

    Raises AristaAvdError is decryption fails
    """
    _validate_password_and_key(password, key)

    data = bytes(password, encoding="UTF-8")
    key_b = bytes(f"{key}_passwd", encoding="UTF-8")

    try:
        return cbc_decrypt(key_b, data).decode()
    except Exception as exc:
        raise AristaAvdError("OSPF password decryption failed - check the input parameters") from exc


OSPF_MESSAGE_DIGEST_HASH_ALGORITHMS = ["md5", "sha1", "sha256", "sha384", "sha512"]


def ospf_message_digest_encrypt(password: str, key: str, hash_algorithm: str | None = None, key_id: str | None = None) -> str:
    """
    Encrypt a password for Message Digest Keys

    <key> should be the interface name e.g. "Ethernet1"
    <hash_algorithm>  MUST be in  ["md5", "sha1", "sha256", "sha384", "sha512"]
    <key_id> MUST be set

    The key is transformed to either:: <key>_<hash_algorithm>Key_<key_id> for message digest keys

    Returns the encrypted password as a string
    """
    _validate_password_and_key(password, key)
    if hash_algorithm is None or key_id is None:
        raise AristaAvdMissingVariableError("For OSPF message digest keys, both hash_algorithm and key_id are required")
    if hash_algorithm not in OSPF_MESSAGE_DIGEST_HASH_ALGORITHMS:
        raise AristaAvdError(f"For OSPF message digest keys, `hash_algorithm` must be in {OSPF_MESSAGE_DIGEST_HASH_ALGORITHMS}")

    data = bytes(password, encoding="UTF-8")
    key_b = bytes(f"{key}_{hash_algorithm}Key_{key_id}", encoding="UTF-8")

    return cbc_encrypt(key_b, data).decode()


def ospf_message_digest_decrypt(password: str, key: str, hash_algorithm: str | None = None, key_id: str | None = None) -> str:
    """
    Decrypt a password for Message Digest Keys

    <key> should be the interface name e.g. "Ethernet1"
    <hash_algorithm>  MUST be in  ["md5", "sha1", "sha256", "sha384", "sha512"]
    <key_id> MUST be set

    The key is transformed to either:: <key>_<hash_algorithm>Key_<key_id> for message digest keys

    Returns the decrypted password as a string

    Raises AristaAvdError is decryption fails
    """
    _validate_password_and_key(password, key)
    if hash_algorithm is None or key_id is None:
        raise AristaAvdMissingVariableError("For OSPF message digest keys, both hash_algorithm and key_id are required")
    if hash_algorithm not in OSPF_MESSAGE_DIGEST_HASH_ALGORITHMS:
        raise AristaAvdError(f"For OSPF message digest keys, `hash_algorithm` must be in {OSPF_MESSAGE_DIGEST_HASH_ALGORITHMS}")

    data = bytes(password, encoding="UTF-8")
    key_b = bytes(f"{key}_{hash_algorithm}Key_{key_id}", encoding="UTF-8")

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
    _validate_password_and_key(password, key)

    data = bytes(password, encoding="UTF-8")
    key = bytes(f"{key}_passwd", encoding="UTF-8")

    return cbc_encrypt(key, data).decode()


def bgp_decrypt(password: str, key) -> str:
    """
    Decrypt a password. The key is either <PEER_GROUP_NAME>_passwd or <NEIGHBOR_IP>_passwd

    Returns the decrypted password as a string

    Raises AristaAvdError is decryption fails
    """
    _validate_password_and_key(password, key)

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
    "ospf_simple": (ospf_simple_encrypt, ospf_simple_decrypt),
    "ospf_message_digest": (ospf_message_digest_encrypt, ospf_message_digest_decrypt),
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
        raise AristaAvdError(f"Type {passwd_type} is not supported for the encrypt filter") from exc
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
        raise AristaAvdError(f"Type {passwd_type} is not supported for the decrypt filter") from exc
    return decrypt_method(str(value), key=key, **kwargs)


class FilterModule(object):
    def filters(self):
        return {
            "encrypt": encrypt,
            "decrypt": decrypt,
        }
