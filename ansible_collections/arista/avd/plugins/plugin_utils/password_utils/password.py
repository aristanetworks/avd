# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""
Used by Encrypt / Decrypt filters
"""
from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError, AristaAvdMissingVariableError

from .password_utils import cbc_decrypt, cbc_encrypt


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


def ospf_message_digest_encrypt(password: str, key: str, hash_algorithm: str = None, key_id: str = None) -> str:
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


def ospf_message_digest_decrypt(password: str, key: str, hash_algorithm: str = None, key_id: str = None) -> str:
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
