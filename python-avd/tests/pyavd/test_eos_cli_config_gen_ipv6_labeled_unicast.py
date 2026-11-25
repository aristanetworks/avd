# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Tests for router BGP IPv6 labeled-unicast support."""

from pyavd import get_device_config, get_device_doc, validate_structured_config


def test_router_bgp_ipv6_labeled_unicast_is_validated_and_rendered() -> None:
    """Validate and render the IPv6 labeled-unicast address family."""
    structured_config = {
        "router_bgp": {
            "as": 65100,
            "peer_groups": [
                {
                    "name": "MPLS-OVERLAY-PEERS",
                    "remote_as": 65000,
                }
            ],
            "address_family_ipv6_labeled_unicast": {
                "peer_groups": [
                    {
                        "name": "MPLS-OVERLAY-PEERS",
                        "activate": True,
                        "maximum_advertised_routes": {"limit": 1200, "warning_limit": {"percent": 10}},
                    }
                ],
                "neighbors": [
                    {
                        "ip_address": "2001:db8::1",
                        "activate": True,
                        "next_hop_self": True,
                        "maximum_advertised_routes": {"limit": 1000, "warning_limit": {"count": 0}},
                    }
                ],
                "networks": [{"prefix": "2001:db8:1::/64", "route_map": "RM-V6-LU"}],
                "next_hops": [{"ip_address": "2001:db8::2", "lfib_backup_ip_forwarding": True}],
            },
        }
    }

    result = validate_structured_config(structured_config)
    assert result.validated_data is not None, result.validation_result

    config = get_device_config(result.validated_data)
    documentation = get_device_doc(result.validated_data)

    assert "address-family ipv6 labeled-unicast" in config
    assert "neighbor MPLS-OVERLAY-PEERS maximum-advertised-routes 1200 warning-limit 10 percent" in config
    assert "neighbor 2001:db8::1 maximum-advertised-routes 1000 warning-limit 0" in config
    assert "neighbor MPLS-OVERLAY-PEERS activate" in config
    assert "neighbor 2001:db8::1 next-hop-self" in config
    assert "network 2001:db8:1::/64 route-map RM-V6-LU" in config
    assert "next-hop 2001:db8::2 originate lfib-backup ip-forwarding" in config
    assert "Router BGP IPv6 Labeled Unicast" in documentation
