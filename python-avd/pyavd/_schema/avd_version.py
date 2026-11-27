# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Versioned defaults for future behaviors shared by AVD Design and EOS Config."""

from __future__ import annotations

import re
from collections import ChainMap
from typing import TYPE_CHECKING

from pyavd._errors import AristaAvdInvalidInputsError

if TYPE_CHECKING:
    from collections.abc import MutableMapping
    from typing import Any

# Keep these versions aligned with the "Available from AVD" descriptions in the schemas.
FUTURE_SETTINGS = {
    "avd_design_future": {
        (6, 1, 0): ("remove_redundant_ipv4_unicast_for_peer_groups",),
        (6, 2, 0): (
            "accept_dhcp_default_route_for_mgmt_ip_dhcp",
            "configure_inband_mgmt_ipv6_vrf",
            "consistent_uplink_vlans",
            "fix_radius_server_group_tls",
            "only_configure_ipv6_inband_mgmt_prefix_list_when_used",
            "only_configure_mlag_vrfs_peer_group_when_used",
            "raise_for_port_channels_without_members",
            "raise_for_underlay_router_with_uplink_type_port_channel",
        ),
        (6, 3, 0): (
            "accept_dhcp_default_route_for_inband_mgmt_ip_dhcp",
            "only_configure_pvst_border_when_mode_is_mstp",
            "only_configure_route_map_connected_to_bgp_vrfs_when_used",
        ),
        (6, 4, 0): (
            "accept_ra_default_route_for_ipv6_mgmt_ip_auto_config",
            "fix_address_locking_dhcp_server_interfaces",
            "fix_match_ipv6_prefix_list_on_mlag_route_map",
        ),
        (6, 5, 0): (
            "allow_recursive_profile_inheritance",
            "fix_mlag_ibgp_peering_ipv6_pool",
            "fix_mlag_ibgp_peering_vrfs_address_families",
            "fix_virtual_source_nat_address_families",
            "sort_snmp_acls_and_local_interfaces_by_vrf",
            "only_configure_oob_mgmt_vrf_and_ipv4_static_routes_when_used",
        ),
        (6, 6, 0): ("configure_management_eapi_ipv4_acl_from_catalog",),
    },
    "eos_config_future": {
        (6, 1, 0): ("new_ip_radius_cli_order", "new_ip_tacacs_cli_order"),
        (6, 2, 0): ("always_render_ip_routing_separator", "only_render_mpls_rsvp_with_settings"),
        (6, 3, 0): ("render_monitor_layer1_without_enabled", "render_spanning_tree_portfast_edge"),
        (6, 4, 0): ("render_combined_separator_for_ipv6_hardware_and_unicast_routing", "only_render_separator_with_boot_secret_key"),
        (6, 5, 0): ("new_bgp_peer_group_cli_order",),
    },
}


def get_future_defaults(version: str, future_key: str) -> dict[str, bool]:
    """Get the flags introduced in or before the selected release."""
    if not isinstance(version, str) or re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", version) is None:
        msg = f"'avd_version' must be an AVD version string in 'major.minor.patch' format. Got {version!r}."
        raise AristaAvdInvalidInputsError(msg)
    selected_version = tuple(int(part) for part in version.split("."))
    return {flag: True for since, flags in FUTURE_SETTINGS[future_key].items() if since <= selected_version for flag in flags}


def with_avd_version(data: MutableMapping[str, Any], future_key: str) -> MutableMapping[str, Any]:
    """Overlay versioned defaults without modifying inputs or overriding explicit flags."""
    if (version := data.get("avd_version")) is None:
        return data
    defaults = get_future_defaults(version, future_key)
    if not defaults or (future_key in data and data[future_key] is None):
        return data
    return ChainMap({future_key: ChainMap(data.get(future_key, {}), defaults)}, data)
