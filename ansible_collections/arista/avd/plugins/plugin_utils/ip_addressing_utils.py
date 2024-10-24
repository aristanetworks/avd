import ipaddress

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError


def get_ip_from_range(ip_offset: int, ip_ranges: list) -> str:
    """
    get_ip_from_range returns IPs from the given ranges.

    Parameters
    ----------
    ip_offset : int starts from 1
    ip_ranges : list of IP ranges in tuples, ex: [("10.10.10.0", "10.10.10.11")]

    Returns
    -------
    IPv4 address
    """

    org_ip_offset = ip_offset
    total_no_ips_available = 0

    for ip_range in ip_ranges:
        if ip_offset == 0:
            raise AristaAvdError("ip_offset should start from 1")
        else:
            ip_offset -= 1

        start_ip = ipaddress.IPv4Address(ip_range[0])
        end_ip = ipaddress.IPv4Address(ip_range[1])
        len_ip_range = int(end_ip) - int(start_ip)
        total_no_ips_available += len_ip_range + 1

        if len_ip_range < 0:
            raise AristaAvdError(f"Provided ip_range {ip_range} is not in ascending order")

        if ip_offset > len_ip_range:
            ip_offset = ip_offset - len_ip_range
        else:
            break

    if org_ip_offset > total_no_ips_available:  # ip_offset starts from 1
        raise AristaAvdError(f"ip_offset value {org_ip_offset} is larger than the defined ip range, total number of ips available {total_no_ips_available}")

    return str(ipaddress.IPv4Address(ip_range[0]) + ip_offset)
