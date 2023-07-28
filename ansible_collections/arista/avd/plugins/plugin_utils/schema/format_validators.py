from ipaddress import IPv4Address, IPv4Network, IPv6Address, IPv6Network
from re import error as re_error
from re import fullmatch

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError


def _validate_format_ipv4(instance: str, *args) -> bool:
    try:
        IPv4Address(instance)
        return True
    except ValueError:
        return False


def _validate_format_ipv6(instance: str, *args) -> bool:
    try:
        IPv6Address(instance)
        return True
    except ValueError:
        return False


def _validate_format_mac(instance: str, *args) -> bool:
    return fullmatch(r"([0-9a-f]{2}:){5}[0-9a-f]{2}", str(instance).lower()) is not None


def _validate_format_ipv4_cidr(instance: str, *args) -> bool:
    # Loose regex match to verify that the string looks like an ipv4 cidr
    if fullmatch(r"[0-9\.]{7,15}/[0-9]{1,2}", str(instance)) is None:
        return False
    try:
        IPv4Network(instance, strict=False)
        return True
    except ValueError:
        return False


def _validate_format_ipv6_cidr(instance: str, *args) -> bool:
    # Loose regex match to verify that the string looks like an ipv6 cidr
    if fullmatch(r"[0-9a-f:]{2,39}/[0-9]{1,3}", str(instance).lower()) is None:
        return False
    try:
        IPv6Network(instance, strict=False)
        return True
    except ValueError:
        return False


def _validate_format_regex(instance: str, *args) -> bool:
    # Join multiple args in the case where regex contain , since we split on , for args.
    regex = ",".join(args)
    try:
        return fullmatch(rf"{regex}", instance) is not None
    except re_error as e:
        raise AristaAvdError("Unable to validate format {test_format}: Invalid format string") from e


FORMAT_VALIDATORS = {
    "ipv4": _validate_format_ipv4,
    "ipv6": _validate_format_ipv6,
    "ipv4_cidr": _validate_format_ipv4_cidr,
    "ipv6_cidr": _validate_format_ipv6_cidr,
    "mac": _validate_format_mac,
    "regex": _validate_format_regex,
}
