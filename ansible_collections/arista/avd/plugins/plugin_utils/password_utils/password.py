# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""
Used by Encrypt / Decrypt filters
"""
from __future__ import annotations

import random

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


##############
# ISIS
##############
_ISIS_MODE_MAP = {
    "none": "noAuth",
    "text": "clearText",
    "md5": "md5",
    "sha": "sha",
    "sha-1": "sha_1",
    "sha-224": "sha_224",
    "sha-256": "sha_256",
    "sha-384": "sha_384",
    "sha-512": "sha_512",
}


def _validate_isis_args(password: str, key: str, mode: str):
    if not password:
        raise AristaAvdError("Password is required for encryption/decryption")

    if not isinstance(password, str):
        raise AristaAvdError(f"Password MUST be of type 'str' but is of type {type(password)}")

    if not isinstance(key, str):
        raise AristaAvdError(f"Key MUST be of type 'str' but is of type {type(key)}")

    if not isinstance(mode, str):
        raise AristaAvdError(f"Mode MUST be a string with one of the following options: {list(_ISIS_MODE_MAP)}. Got '{mode}'.")

    if not mode:
        raise AristaAvdError("Mode is required for encryption/decryption")


def _get_isis_key(key: str, mode: str) -> bytes:
    return bytes(f"{key}_{_ISIS_MODE_MAP[mode]}", encoding="UTF-8")


def isis_encrypt(password: str, key: str, mode: str) -> str:
    """
    Encrypt a password for ISIS authentication.

    Args:
        password: Password as string
        key: ISIS instance name as string.
        mode: 'none', 'text', 'md5' or 'sha' or for shared-secret mode 'sha-1', 'sha-224', 'sha-256', 'sha-384', 'sha-512'.

    Returns the encrypted password as a string.
    """
    _validate_isis_args(password, key, mode)

    data = bytes(password, encoding="UTF-8")

    return cbc_encrypt(_get_isis_key(key, mode), data).decode()


def isis_decrypt(password: str, key: str, mode: str) -> str:
    """
    Decrypt a password for ISIS authentication.

    <key> ISIS instance name.
    <mode> 'none', 'text', 'md5' or 'sha' or for shared-secret mode 'sha-1', 'sha-224', 'sha-256', 'sha-384', 'sha-512'.

    Returns the decrypted password as a string.

    Raises AristaAvdError is decryption fails
    """
    _validate_isis_args(password, key, mode)

    data = bytes(password, encoding="UTF-8")

    try:
        return cbc_decrypt(_get_isis_key(key, mode), data).decode()
    except Exception as exc:
        raise AristaAvdError("ISIS password decryption failed - check the input parameters") from exc


###############
# Simple type 7
###############
SIMPLE_7_SEED = b"dsfd;kfoA,.iyewrkldJKDHSUBsgvca69834ncxv9873254k;fg87"


def simple_7_decrypt(data: str) -> str:
    """
    Decrypt (deobfuscate) a password from insecure type-7.

    Args:
        data: The encrypted password

    Returns the decrypted password as a string.
    """
    salt = int(data[0:2])
    secret = bytearray.fromhex(data[2:])
    return bytes(char ^ (SIMPLE_7_SEED[(salt + i) % 53]) for i, char in enumerate(secret)).decode("UTF-8")


def simple_7_encrypt(data: str, salt: int | None = None) -> str:
    """
    Encrypt (obfuscate) a password with insecure type-7.

    Args:
        data: The clear text password
        salt: Optionally a number within the range 0-15. If not set, a random salt will be used.

    Returns the encrypted password as a string.
    """
    if salt is None:
        salt = random.randint(0, 15)
    cleartext = data.encode("UTF-8")
    return f"{salt:02}" + bytearray(char ^ (SIMPLE_7_SEED[(salt + i) % 53]) for i, char in enumerate(cleartext)).hex().upper()
