# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Used by Encrypt / Decrypt filters."""

from __future__ import annotations

from typing import Any, Literal

from pyavd_utils.passwords import cbc_decrypt, cbc_encrypt, simple_7_decrypt, simple_7_encrypt


def _validate_password_and_key(password: Any, key: str) -> None:
    """
    Validates the password and key values.

    Args:
        password (str): The password to validate.
        key (str): The key to validate.

    Raises:
        ValueError: If the key or password is missing.
        TypeError: If the password is not of type `str`.
    """
    if not key:
        msg = "Key is required for encryption"
        raise ValueError(msg)

    if not password:
        msg = "Password is required for encryption"
        raise ValueError(msg)

    if not isinstance(password, str):
        msg = f"Password MUST be of type 'str' but is of type {type(password)}"
        raise TypeError(msg)


##############
# OSPF
##############
def ospf_simple_encrypt(password: str, key: str) -> str:
    """
    Encrypt a password for OSPF simple authentication.

    Args:
        password (str): The password to be encrypted.
        key (str): The interface name, e.g., "Ethernet1".

    Returns:
        str: The encrypted password as a base64-encoded string.

    Raises:
        ValueError: If the key or password is missing.
        TypeError: If the password is not of type `str`.
    """
    _validate_password_and_key(password, key)
    return cbc_encrypt(f"{key}_passwd", password)


def ospf_simple_decrypt(password: str, key: str) -> str:
    """
    Decrypt a password for OSPF simple authentication.

    Args:
        password (str): The encrypted password to be decrypted.
        key (str): The interface name, e.g., "Ethernet1".

    Returns:
        str: The decrypted password as a string.

    Raises:
        ValueError: If decryption fails.
        ValueError: If the key or password is missing.
        TypeError: If the password is not of type `str`.
    """
    _validate_password_and_key(password, key)

    try:
        return cbc_decrypt(f"{key}_passwd", password)
    except Exception as exc:
        msg = "OSPF password decryption failed - check the input parameters"
        raise ValueError(msg) from exc


OSPF_MESSAGE_DIGEST_HASH_ALGORITHMS = ["md5", "sha1", "sha256", "sha384", "sha512"]


def ospf_message_digest_encrypt(password: str, key: str, hash_algorithm: str | None = None, key_id: str | None = None) -> str:
    """
    Encrypt a password for Message Digest Keys.

    Args:
        password (str): The password to be encrypted.
        key (str): The interface name, e.g., "Ethernet1".
        hash_algorithm (str, optional): The hash algorithm to use. Must be one of ["md5", "sha1", "sha256", "sha384", "sha512"].
        key_id (str, optional): The key ID to use.

    Returns:
        str: The encrypted password as a base64-encoded string.

    Raises:
        ValueError: If `hash_algorithm` or `key_id` is not provided.
        ValueError: If `hash_algorithm` is not one of the allowed values.
        ValueError: If the key or password is missing.
        TypeError: If the password is not of type `str`.
    """
    _validate_password_and_key(password, key)
    if hash_algorithm is None or key_id is None:
        msg = "For OSPF message digest keys, both hash_algorithm and key_id are required"
        raise ValueError(msg)
    if hash_algorithm not in OSPF_MESSAGE_DIGEST_HASH_ALGORITHMS:
        msg = f"For OSPF message digest keys, `hash_algorithm` must be in {OSPF_MESSAGE_DIGEST_HASH_ALGORITHMS}"
        raise ValueError(msg)

    return cbc_encrypt(f"{key}_{hash_algorithm}Key_{key_id}", password)


def ospf_message_digest_decrypt(password: str, key: str, hash_algorithm: str | None = None, key_id: str | None = None) -> str:
    """
    Decrypt a password for Message Digest Keys.

    Args:
        password (str): The encrypted password to be decrypted.
        key (str): The interface name, e.g., "Ethernet1".
        hash_algorithm (str, optional): The hash algorithm used for encryption. Must be one of ["md5", "sha1", "sha256", "sha384", "sha512"].
        key_id (str, optional): The key ID used for encryption.

    Returns:
        str: The decrypted password as a string.

    Raises:
        ValueError: If `hash_algorithm` or `key_id` is not provided.
        ValueError: If `hash_algorithm` is not one of the allowed values.
        ValueError: If decryption fails.
        ValueError: If the key or password is missing.
        TypeError: If the password is not of type `str`.
    """
    _validate_password_and_key(password, key)
    if hash_algorithm is None or key_id is None:
        msg = "For OSPF message digest keys, both hash_algorithm and key_id are required"
        raise ValueError(msg)
    if hash_algorithm not in OSPF_MESSAGE_DIGEST_HASH_ALGORITHMS:
        msg = f"For OSPF message digest keys, `hash_algorithm` must be in {OSPF_MESSAGE_DIGEST_HASH_ALGORITHMS}"
        raise ValueError(msg)

    try:
        return cbc_decrypt(f"{key}_{hash_algorithm}Key_{key_id}", password)
    except Exception as exc:
        msg = "OSPF password decryption failed - check the input parameters"
        raise ValueError(msg) from exc


##############
# BGP
##############
def bgp_encrypt(password: str, key: str) -> str:
    """
    Encrypts a password for BGP (Border Gateway Protocol) authentication.

    Args:
        password (str): The password to be encrypted.
        key (str): The key used for encryption, derived from either <PEER_GROUP_NAME> or <NEIGHBOR_IP>.

    Returns:
        str: The encrypted password as a base64-encoded string.

    Raises:
        ValueError: If the key or password is missing.
        TypeError: If the password is not of type `str`.
    """
    _validate_password_and_key(password, key)
    return cbc_encrypt(f"{key}_passwd", password)


def bgp_decrypt(password: str, key: str) -> str:
    """
    Decrypts a password for BGP (Border Gateway Protocol) authentication.

    Args:
        password (str): The encrypted password to be decrypted.
        key (str): The key used for decryption, derived from either <PEER_GROUP_NAME> or <NEIGHBOR_IP>.

    Returns:
        str: The decrypted password as a string.

    Raises:
        ValueError: If decryption fails.
        ValueError: If the key or password is missing.
        TypeError: If the password is not of type `str`.
    """
    _validate_password_and_key(password, key)

    try:
        return cbc_decrypt(f"{key}_passwd", password)
    except Exception as exc:
        msg = "BGP password decryption failed - check the input parameters"
        raise ValueError(msg) from exc


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


def _validate_isis_args(password: str, key: str, mode: str) -> None:
    """
    Validates the arguments for ISIS (Intermediate System to Intermediate System) encryption/decryption.

    Args:
        password (str): The password to be encrypted/decrypted.
        key (str): The key used for encryption/decryption.
        mode (str): The mode of operation for encryption/decryption, which should be one of the options in `_ISIS_MODE_MAP`.

    Raises:
        ValueError: If `password` is empty or missing.
        TypeError: If `password` is not of type `str`.
        TypeError: If `key` is not of type `str`.
        TypeError: If `mode` is not of type `str` or is not one of the valid options in `_ISIS_MODE_MAP`.
        ValueError: If `mode` is empty or missing.
    """
    if not password:
        msg = "Password is required for encryption/decryption"
        raise ValueError(msg)

    if not isinstance(password, str):
        msg = f"Password MUST be of type 'str' but is of type {type(password)}"
        raise TypeError(msg)

    if not isinstance(key, str):
        msg = f"Key MUST be of type 'str' but is of type {type(key)}"
        raise TypeError(msg)

    if not isinstance(mode, str):
        msg = f"Mode MUST be a string with one of the following options: {list(_ISIS_MODE_MAP)}. Got '{mode}'."
        raise TypeError(msg)

    if not mode:
        msg = "Mode is required for encryption/decryption"
        raise ValueError(msg)


def _get_isis_key(key: str, mode: str) -> str:
    return f"{key}_{_ISIS_MODE_MAP[mode]}"


def isis_encrypt(password: str, key: str, mode: str) -> str:
    """
    Encrypt a password for ISIS authentication.

    Args:
        password: Password as string
        key: ISIS instance name as string.
        mode: 'none', 'text', 'md5' or 'sha' or for shared-secret mode 'sha-1', 'sha-224', 'sha-256', 'sha-384', 'sha-512'.

    Returns:
        str: The encrypted password as a string.
    """
    _validate_isis_args(password, key, mode)
    return cbc_encrypt(_get_isis_key(key, mode), password)


def isis_decrypt(password: str, key: str, mode: str) -> str:
    """
    Decrypt a password for ISIS authentication.

    Args:
        password (str): The encrypted password to be decrypted.
        key (str): The ISIS instance name used to derive the decryption key.
        mode (str): Specifies the decryption mode. Can be one of:
            - 'none': No encryption.
            - 'text': Plain text (no decryption needed, but processed accordingly).
            - 'md5': MD5 hash decryption.
            - 'sha': SHA-1 hash decryption.
            - 'sha-1', 'sha-224', 'sha-256', 'sha-384', 'sha-512': Various SHA hash decryptions.

    Returns:
        str: The decrypted password as a string.

    Raises:
        ValueError: If decryption fails for any reason.
    """
    _validate_isis_args(password, key, mode)

    try:
        return cbc_decrypt(_get_isis_key(key, mode), password)
    except Exception as exc:
        msg = "ISIS password decryption failed - check the input parameters"
        raise ValueError(msg) from exc


########
# Radius
########
def radius_encrypt(password: str, salt: Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) -> str:
    """
    Encrypt (obfuscate) a Radius key with insecure type-7.

    Args:
        password: The clear text Radius key.
        salt: A number within the range 0-15.

    Returns:
        str: The encrypted Radius key as a string.
    """
    if not isinstance(password, str) or not password:
        msg = "Password MUST be a string with at least 1 character."
        raise ValueError(msg)

    if not isinstance(salt, int) or salt < 0 or salt > 15:
        msg = "Salt MUST be an integer within the range 0-15."
        raise ValueError(msg)

    return simple_7_encrypt(password, salt)


def radius_decrypt(password: str) -> str:
    """
    Decrypt (deobfuscate) a Radius key from insecure type-7.

    Args:
        password: The encrypted Radius key to be decrypted.

    Returns:
        str: The decrypted Radius key as a string.
    """
    if not isinstance(password, str) or not password:
        msg = "Password MUST be a string with at least 1 character."
        raise ValueError(msg)

    return simple_7_decrypt(password)


########
# Tacacs
########
def tacacs_encrypt(password: str, salt: Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) -> str:
    """
    Encrypt (obfuscate) a Tacacs key with insecure type-7.

    Args:
        password: The clear text Tacacs key.
        salt: A number within the range 0-15.

    Returns:
        str: The encrypted Tacacs key as a string.
    """
    if not isinstance(password, str) or not password:
        msg = "Password MUST be a string with at least 1 character."
        raise ValueError(msg)

    if not isinstance(salt, int) or salt < 0 or salt > 15:
        msg = "Salt MUST be an integer within the range 0-15."
        raise ValueError(msg)

    return simple_7_encrypt(password, salt)


def tacacs_decrypt(password: str) -> str:
    """
    Decrypt (deobfuscate) a Tacacs key from insecure type-7.

    Args:
        password: The encrypted Tacacs key to be decrypted.

    Returns:
        str: The decrypted Tacacs key as a string.
    """
    if not isinstance(password, str) or not password:
        msg = "Password MUST be a string with at least 1 character."
        raise ValueError(msg)

    return simple_7_decrypt(password)


########
# NTP
########
# TODO: discuss with @Claus to merge the functions between tacacs, ntp and -soon- radius
# probably can move the salt check in simple_7_xxx and use only one function
def ntp_encrypt(password: str, salt: Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) -> str:
    """
    Encrypt (obfuscate) an NTP key with insecure type-7.

    Args:
        password: The clear text NTP key.
        salt: A number within the range 0-15.

    Returns:
        str: The encrypted NTP key as a string.
    """
    if not isinstance(password, str) or not password:
        msg = "Password MUST be a string with at least 1 character."
        raise ValueError(msg)

    if not isinstance(salt, int) or salt < 0 or salt > 15:
        msg = "Salt MUST be an integer within the range 0-15."
        raise ValueError(msg)

    return simple_7_encrypt(password, salt)


def ntp_decrypt(password: str) -> str:
    """
    Decrypt (deobfuscate) a NTP key from insecure type-7.

    Args:
        password: The encrypted NTP key to be decrypted.

    Returns:
        str: The decrypted NTP key as a string.
    """
    if not isinstance(password, str) or not password:
        msg = "Password MUST be a string with at least 1 character."
        raise ValueError(msg)

    return simple_7_decrypt(password)
