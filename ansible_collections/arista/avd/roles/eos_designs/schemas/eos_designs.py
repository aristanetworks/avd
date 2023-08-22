# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

from pydantic import BaseModel, Field


class EosDesigns(BaseModel):
    class BfdMultihop(BaseModel):
        interval: int = Field(default=None)
        min_rx: int = Field(default=None)
        multiplier: int = Field(default=None)

    class BgpDistance(BaseModel):
        external_routes: int = Field(default=None)
        internal_routes: int = Field(default=None)
        local_routes: int = Field(default=None)

    class BgpGracefulRestart(BaseModel):
        enabled: bool = Field(default=False)
        restart_time: int = Field(default=300)

    class BgpPeerGroups(BaseModel):
        class Ipv4UnderlayPeers(BaseModel):
            class StructuredConfig(BaseModel):
                class AsPath(BaseModel):
                    remote_as_replace_out: bool | None = Field(default=None)
                    prepend_own_disabled: bool | None = Field(default=None)

                class RemovePrivateAs(BaseModel):
                    enabled: bool | None = Field(default=None)
                    all: bool | None = Field(default=None)
                    replace_as: bool | None = Field(default=None)

                class RemovePrivateAsIngress(BaseModel):
                    enabled: bool | None = Field(default=None)
                    replace_as: bool | None = Field(default=None)

                class DefaultOriginate(BaseModel):
                    enabled: bool | None = Field(default=None)
                    always: bool | None = Field(default=None)
                    route_map: str | None = Field(default=None)

                class LinkBandwidth(BaseModel):
                    enabled: bool | None = Field(default=None)
                    default: str | None = Field(default=None)

                class AllowasIn(BaseModel):
                    enabled: bool | None = Field(default=None)
                    times: int | None = Field(default=None)

                class RibInPrePolicyRetain(BaseModel):
                    enabled: bool | None = Field(default=None)
                    all: bool | None = Field(default=None)

                name: str | None = Field(default=None)
                type: str | None = Field(default=None)
                remote_as: str | None = Field(default=None)
                local_as: str | None = Field(default=None)
                description: str | None = Field(default=None)
                shutdown: bool | None = Field(default=None)
                as_path: AsPath | None = Field(default=None)
                remove_private_as: RemovePrivateAs | None = Field(default=None)
                remove_private_as_ingress: RemovePrivateAsIngress | None = Field(default=None)
                peer_filter: str | None = Field(default=None)
                next_hop_unchanged: bool | None = Field(default=None)
                update_source: str | None = Field(default=None)
                route_reflector_client: bool | None = Field(default=None)
                bfd: bool | None = Field(default=None)
                ebgp_multihop: int | None = Field(default=None)
                next_hop_self: bool | None = Field(default=None)
                password: str | None = Field(default=None)
                passive: bool | None = Field(default=None)
                default_originate: DefaultOriginate | None = Field(default=None)
                send_community: str | None = Field(default=None)
                maximum_routes: int | None = Field(default=None)
                maximum_routes_warning_limit: str | None = Field(default=None)
                maximum_routes_warning_only: bool | None = Field(default=None)
                link_bandwidth: LinkBandwidth | None = Field(default=None)
                allowas_in: AllowasIn | None = Field(default=None)
                weight: int | None = Field(default=None)
                timers: str | None = Field(default=None)
                rib_in_pre_policy_retain: RibInPrePolicyRetain | None = Field(default=None)
                route_map_in: str | None = Field(default=None)
                route_map_out: str | None = Field(default=None)
                bgp_listen_range_prefix: str | None = Field(default=None)
                session_tracker: str | None = Field(default=None)

            name: str = Field(default="IPv4-UNDERLAY-PEERS")
            password: str | None = Field(default=None)
            bfd: bool = Field(default=False)
            structured_config: StructuredConfig | None = Field(default=None)

        class MlagIpv4UnderlayPeer(BaseModel):
            class StructuredConfig(BaseModel):
                class AsPath(BaseModel):
                    remote_as_replace_out: bool | None = Field(default=None)
                    prepend_own_disabled: bool | None = Field(default=None)

                class RemovePrivateAs(BaseModel):
                    enabled: bool | None = Field(default=None)
                    all: bool | None = Field(default=None)
                    replace_as: bool | None = Field(default=None)

                class RemovePrivateAsIngress(BaseModel):
                    enabled: bool | None = Field(default=None)
                    replace_as: bool | None = Field(default=None)

                class DefaultOriginate(BaseModel):
                    enabled: bool | None = Field(default=None)
                    always: bool | None = Field(default=None)
                    route_map: str | None = Field(default=None)

                class LinkBandwidth(BaseModel):
                    enabled: bool | None = Field(default=None)
                    default: str | None = Field(default=None)

                class AllowasIn(BaseModel):
                    enabled: bool | None = Field(default=None)
                    times: int | None = Field(default=None)

                class RibInPrePolicyRetain(BaseModel):
                    enabled: bool | None = Field(default=None)
                    all: bool | None = Field(default=None)

                name: str | None = Field(default=None)
                type: str | None = Field(default=None)
                remote_as: str | None = Field(default=None)
                local_as: str | None = Field(default=None)
                description: str | None = Field(default=None)
                shutdown: bool | None = Field(default=None)
                as_path: AsPath | None = Field(default=None)
                remove_private_as: RemovePrivateAs | None = Field(default=None)
                remove_private_as_ingress: RemovePrivateAsIngress | None = Field(default=None)
                peer_filter: str | None = Field(default=None)
                next_hop_unchanged: bool | None = Field(default=None)
                update_source: str | None = Field(default=None)
                route_reflector_client: bool | None = Field(default=None)
                bfd: bool | None = Field(default=None)
                ebgp_multihop: int | None = Field(default=None)
                next_hop_self: bool | None = Field(default=None)
                password: str | None = Field(default=None)
                passive: bool | None = Field(default=None)
                default_originate: DefaultOriginate | None = Field(default=None)
                send_community: str | None = Field(default=None)
                maximum_routes: int | None = Field(default=None)
                maximum_routes_warning_limit: str | None = Field(default=None)
                maximum_routes_warning_only: bool | None = Field(default=None)
                link_bandwidth: LinkBandwidth | None = Field(default=None)
                allowas_in: AllowasIn | None = Field(default=None)
                weight: int | None = Field(default=None)
                timers: str | None = Field(default=None)
                rib_in_pre_policy_retain: RibInPrePolicyRetain | None = Field(default=None)
                route_map_in: str | None = Field(default=None)
                route_map_out: str | None = Field(default=None)
                bgp_listen_range_prefix: str | None = Field(default=None)
                session_tracker: str | None = Field(default=None)

            name: str = Field(default="MLAG-IPv4-UNDERLAY-PEER")
            password: str | None = Field(default=None)
            bfd: bool = Field(default=False)
            structured_config: StructuredConfig | None = Field(default=None)

        class EvpnOverlayPeers(BaseModel):
            class StructuredConfig(BaseModel):
                class AsPath(BaseModel):
                    remote_as_replace_out: bool | None = Field(default=None)
                    prepend_own_disabled: bool | None = Field(default=None)

                class RemovePrivateAs(BaseModel):
                    enabled: bool | None = Field(default=None)
                    all: bool | None = Field(default=None)
                    replace_as: bool | None = Field(default=None)

                class RemovePrivateAsIngress(BaseModel):
                    enabled: bool | None = Field(default=None)
                    replace_as: bool | None = Field(default=None)

                class DefaultOriginate(BaseModel):
                    enabled: bool | None = Field(default=None)
                    always: bool | None = Field(default=None)
                    route_map: str | None = Field(default=None)

                class LinkBandwidth(BaseModel):
                    enabled: bool | None = Field(default=None)
                    default: str | None = Field(default=None)

                class AllowasIn(BaseModel):
                    enabled: bool | None = Field(default=None)
                    times: int | None = Field(default=None)

                class RibInPrePolicyRetain(BaseModel):
                    enabled: bool | None = Field(default=None)
                    all: bool | None = Field(default=None)

                name: str | None = Field(default=None)
                type: str | None = Field(default=None)
                remote_as: str | None = Field(default=None)
                local_as: str | None = Field(default=None)
                description: str | None = Field(default=None)
                shutdown: bool | None = Field(default=None)
                as_path: AsPath | None = Field(default=None)
                remove_private_as: RemovePrivateAs | None = Field(default=None)
                remove_private_as_ingress: RemovePrivateAsIngress | None = Field(default=None)
                peer_filter: str | None = Field(default=None)
                next_hop_unchanged: bool | None = Field(default=None)
                update_source: str | None = Field(default=None)
                route_reflector_client: bool | None = Field(default=None)
                bfd: bool | None = Field(default=None)
                ebgp_multihop: int | None = Field(default=None)
                next_hop_self: bool | None = Field(default=None)
                password: str | None = Field(default=None)
                passive: bool | None = Field(default=None)
                default_originate: DefaultOriginate | None = Field(default=None)
                send_community: str | None = Field(default=None)
                maximum_routes: int | None = Field(default=None)
                maximum_routes_warning_limit: str | None = Field(default=None)
                maximum_routes_warning_only: bool | None = Field(default=None)
                link_bandwidth: LinkBandwidth | None = Field(default=None)
                allowas_in: AllowasIn | None = Field(default=None)
                weight: int | None = Field(default=None)
                timers: str | None = Field(default=None)
                rib_in_pre_policy_retain: RibInPrePolicyRetain | None = Field(default=None)
                route_map_in: str | None = Field(default=None)
                route_map_out: str | None = Field(default=None)
                bgp_listen_range_prefix: str | None = Field(default=None)
                session_tracker: str | None = Field(default=None)

            name: str = Field(default="EVPN-OVERLAY-PEERS")
            password: str | None = Field(default=None)
            bfd: bool = Field(default=True)
            structured_config: StructuredConfig | None = Field(default=None)

        class EvpnOverlayCore(BaseModel):
            class StructuredConfig(BaseModel):
                class AsPath(BaseModel):
                    remote_as_replace_out: bool | None = Field(default=None)
                    prepend_own_disabled: bool | None = Field(default=None)

                class RemovePrivateAs(BaseModel):
                    enabled: bool | None = Field(default=None)
                    all: bool | None = Field(default=None)
                    replace_as: bool | None = Field(default=None)

                class RemovePrivateAsIngress(BaseModel):
                    enabled: bool | None = Field(default=None)
                    replace_as: bool | None = Field(default=None)

                class DefaultOriginate(BaseModel):
                    enabled: bool | None = Field(default=None)
                    always: bool | None = Field(default=None)
                    route_map: str | None = Field(default=None)

                class LinkBandwidth(BaseModel):
                    enabled: bool | None = Field(default=None)
                    default: str | None = Field(default=None)

                class AllowasIn(BaseModel):
                    enabled: bool | None = Field(default=None)
                    times: int | None = Field(default=None)

                class RibInPrePolicyRetain(BaseModel):
                    enabled: bool | None = Field(default=None)
                    all: bool | None = Field(default=None)

                name: str | None = Field(default=None)
                type: str | None = Field(default=None)
                remote_as: str | None = Field(default=None)
                local_as: str | None = Field(default=None)
                description: str | None = Field(default=None)
                shutdown: bool | None = Field(default=None)
                as_path: AsPath | None = Field(default=None)
                remove_private_as: RemovePrivateAs | None = Field(default=None)
                remove_private_as_ingress: RemovePrivateAsIngress | None = Field(default=None)
                peer_filter: str | None = Field(default=None)
                next_hop_unchanged: bool | None = Field(default=None)
                update_source: str | None = Field(default=None)
                route_reflector_client: bool | None = Field(default=None)
                bfd: bool | None = Field(default=None)
                ebgp_multihop: int | None = Field(default=None)
                next_hop_self: bool | None = Field(default=None)
                password: str | None = Field(default=None)
                passive: bool | None = Field(default=None)
                default_originate: DefaultOriginate | None = Field(default=None)
                send_community: str | None = Field(default=None)
                maximum_routes: int | None = Field(default=None)
                maximum_routes_warning_limit: str | None = Field(default=None)
                maximum_routes_warning_only: bool | None = Field(default=None)
                link_bandwidth: LinkBandwidth | None = Field(default=None)
                allowas_in: AllowasIn | None = Field(default=None)
                weight: int | None = Field(default=None)
                timers: str | None = Field(default=None)
                rib_in_pre_policy_retain: RibInPrePolicyRetain | None = Field(default=None)
                route_map_in: str | None = Field(default=None)
                route_map_out: str | None = Field(default=None)
                bgp_listen_range_prefix: str | None = Field(default=None)
                session_tracker: str | None = Field(default=None)

            name: str = Field(default="EVPN-OVERLAY-CORE")
            password: str | None = Field(default=None)
            bfd: bool = Field(default=True)
            structured_config: StructuredConfig | None = Field(default=None)

        class MplsOverlayPeers(BaseModel):
            class StructuredConfig(BaseModel):
                class AsPath(BaseModel):
                    remote_as_replace_out: bool | None = Field(default=None)
                    prepend_own_disabled: bool | None = Field(default=None)

                class RemovePrivateAs(BaseModel):
                    enabled: bool | None = Field(default=None)
                    all: bool | None = Field(default=None)
                    replace_as: bool | None = Field(default=None)

                class RemovePrivateAsIngress(BaseModel):
                    enabled: bool | None = Field(default=None)
                    replace_as: bool | None = Field(default=None)

                class DefaultOriginate(BaseModel):
                    enabled: bool | None = Field(default=None)
                    always: bool | None = Field(default=None)
                    route_map: str | None = Field(default=None)

                class LinkBandwidth(BaseModel):
                    enabled: bool | None = Field(default=None)
                    default: str | None = Field(default=None)

                class AllowasIn(BaseModel):
                    enabled: bool | None = Field(default=None)
                    times: int | None = Field(default=None)

                class RibInPrePolicyRetain(BaseModel):
                    enabled: bool | None = Field(default=None)
                    all: bool | None = Field(default=None)

                name: str | None = Field(default=None)
                type: str | None = Field(default=None)
                remote_as: str | None = Field(default=None)
                local_as: str | None = Field(default=None)
                description: str | None = Field(default=None)
                shutdown: bool | None = Field(default=None)
                as_path: AsPath | None = Field(default=None)
                remove_private_as: RemovePrivateAs | None = Field(default=None)
                remove_private_as_ingress: RemovePrivateAsIngress | None = Field(default=None)
                peer_filter: str | None = Field(default=None)
                next_hop_unchanged: bool | None = Field(default=None)
                update_source: str | None = Field(default=None)
                route_reflector_client: bool | None = Field(default=None)
                bfd: bool | None = Field(default=None)
                ebgp_multihop: int | None = Field(default=None)
                next_hop_self: bool | None = Field(default=None)
                password: str | None = Field(default=None)
                passive: bool | None = Field(default=None)
                default_originate: DefaultOriginate | None = Field(default=None)
                send_community: str | None = Field(default=None)
                maximum_routes: int | None = Field(default=None)
                maximum_routes_warning_limit: str | None = Field(default=None)
                maximum_routes_warning_only: bool | None = Field(default=None)
                link_bandwidth: LinkBandwidth | None = Field(default=None)
                allowas_in: AllowasIn | None = Field(default=None)
                weight: int | None = Field(default=None)
                timers: str | None = Field(default=None)
                rib_in_pre_policy_retain: RibInPrePolicyRetain | None = Field(default=None)
                route_map_in: str | None = Field(default=None)
                route_map_out: str | None = Field(default=None)
                bgp_listen_range_prefix: str | None = Field(default=None)
                session_tracker: str | None = Field(default=None)

            name: str = Field(default="MPLS-OVERLAY-PEERS")
            password: str | None = Field(default=None)
            bfd: bool = Field(default=True)
            structured_config: StructuredConfig | None = Field(default=None)

        class RrOverlayPeers(BaseModel):
            class StructuredConfig(BaseModel):
                class AsPath(BaseModel):
                    remote_as_replace_out: bool | None = Field(default=None)
                    prepend_own_disabled: bool | None = Field(default=None)

                class RemovePrivateAs(BaseModel):
                    enabled: bool | None = Field(default=None)
                    all: bool | None = Field(default=None)
                    replace_as: bool | None = Field(default=None)

                class RemovePrivateAsIngress(BaseModel):
                    enabled: bool | None = Field(default=None)
                    replace_as: bool | None = Field(default=None)

                class DefaultOriginate(BaseModel):
                    enabled: bool | None = Field(default=None)
                    always: bool | None = Field(default=None)
                    route_map: str | None = Field(default=None)

                class LinkBandwidth(BaseModel):
                    enabled: bool | None = Field(default=None)
                    default: str | None = Field(default=None)

                class AllowasIn(BaseModel):
                    enabled: bool | None = Field(default=None)
                    times: int | None = Field(default=None)

                class RibInPrePolicyRetain(BaseModel):
                    enabled: bool | None = Field(default=None)
                    all: bool | None = Field(default=None)

                name: str | None = Field(default=None)
                type: str | None = Field(default=None)
                remote_as: str | None = Field(default=None)
                local_as: str | None = Field(default=None)
                description: str | None = Field(default=None)
                shutdown: bool | None = Field(default=None)
                as_path: AsPath | None = Field(default=None)
                remove_private_as: RemovePrivateAs | None = Field(default=None)
                remove_private_as_ingress: RemovePrivateAsIngress | None = Field(default=None)
                peer_filter: str | None = Field(default=None)
                next_hop_unchanged: bool | None = Field(default=None)
                update_source: str | None = Field(default=None)
                route_reflector_client: bool | None = Field(default=None)
                bfd: bool | None = Field(default=None)
                ebgp_multihop: int | None = Field(default=None)
                next_hop_self: bool | None = Field(default=None)
                password: str | None = Field(default=None)
                passive: bool | None = Field(default=None)
                default_originate: DefaultOriginate | None = Field(default=None)
                send_community: str | None = Field(default=None)
                maximum_routes: int | None = Field(default=None)
                maximum_routes_warning_limit: str | None = Field(default=None)
                maximum_routes_warning_only: bool | None = Field(default=None)
                link_bandwidth: LinkBandwidth | None = Field(default=None)
                allowas_in: AllowasIn | None = Field(default=None)
                weight: int | None = Field(default=None)
                timers: str | None = Field(default=None)
                rib_in_pre_policy_retain: RibInPrePolicyRetain | None = Field(default=None)
                route_map_in: str | None = Field(default=None)
                route_map_out: str | None = Field(default=None)
                bgp_listen_range_prefix: str | None = Field(default=None)
                session_tracker: str | None = Field(default=None)

            name: str = Field(default="RR-OVERLAY-PEERS")
            password: str | None = Field(default=None)
            bfd: bool = Field(default=True)
            structured_config: StructuredConfig | None = Field(default=None)

        class IpvpnGatewayPeers(BaseModel):
            class StructuredConfig(BaseModel):
                class AsPath(BaseModel):
                    remote_as_replace_out: bool | None = Field(default=None)
                    prepend_own_disabled: bool | None = Field(default=None)

                class RemovePrivateAs(BaseModel):
                    enabled: bool | None = Field(default=None)
                    all: bool | None = Field(default=None)
                    replace_as: bool | None = Field(default=None)

                class RemovePrivateAsIngress(BaseModel):
                    enabled: bool | None = Field(default=None)
                    replace_as: bool | None = Field(default=None)

                class DefaultOriginate(BaseModel):
                    enabled: bool | None = Field(default=None)
                    always: bool | None = Field(default=None)
                    route_map: str | None = Field(default=None)

                class LinkBandwidth(BaseModel):
                    enabled: bool | None = Field(default=None)
                    default: str | None = Field(default=None)

                class AllowasIn(BaseModel):
                    enabled: bool | None = Field(default=None)
                    times: int | None = Field(default=None)

                class RibInPrePolicyRetain(BaseModel):
                    enabled: bool | None = Field(default=None)
                    all: bool | None = Field(default=None)

                name: str | None = Field(default=None)
                type: str | None = Field(default=None)
                remote_as: str | None = Field(default=None)
                local_as: str | None = Field(default=None)
                description: str | None = Field(default=None)
                shutdown: bool | None = Field(default=None)
                as_path: AsPath | None = Field(default=None)
                remove_private_as: RemovePrivateAs | None = Field(default=None)
                remove_private_as_ingress: RemovePrivateAsIngress | None = Field(default=None)
                peer_filter: str | None = Field(default=None)
                next_hop_unchanged: bool | None = Field(default=None)
                update_source: str | None = Field(default=None)
                route_reflector_client: bool | None = Field(default=None)
                bfd: bool | None = Field(default=None)
                ebgp_multihop: int | None = Field(default=None)
                next_hop_self: bool | None = Field(default=None)
                password: str | None = Field(default=None)
                passive: bool | None = Field(default=None)
                default_originate: DefaultOriginate | None = Field(default=None)
                send_community: str | None = Field(default=None)
                maximum_routes: int | None = Field(default=None)
                maximum_routes_warning_limit: str | None = Field(default=None)
                maximum_routes_warning_only: bool | None = Field(default=None)
                link_bandwidth: LinkBandwidth | None = Field(default=None)
                allowas_in: AllowasIn | None = Field(default=None)
                weight: int | None = Field(default=None)
                timers: str | None = Field(default=None)
                rib_in_pre_policy_retain: RibInPrePolicyRetain | None = Field(default=None)
                route_map_in: str | None = Field(default=None)
                route_map_out: str | None = Field(default=None)
                bgp_listen_range_prefix: str | None = Field(default=None)
                session_tracker: str | None = Field(default=None)

            name: str = Field(default="IPVPN-GATEWAY-PEERS")
            password: str | None = Field(default=None)
            bfd: bool = Field(default=True)
            structured_config: StructuredConfig | None = Field(default=None)

        ipv4_underlay_peers: Ipv4UnderlayPeers | None = Field(default=None)
        mlag_ipv4_underlay_peer: MlagIpv4UnderlayPeer | None = Field(default=None)
        evpn_overlay_peers: EvpnOverlayPeers | None = Field(default=None)
        evpn_overlay_core: EvpnOverlayCore | None = Field(default=None)
        mpls_overlay_peers: MplsOverlayPeers | None = Field(default=None)
        rr_overlay_peers: RrOverlayPeers | None = Field(default=None)
        ipvpn_gateway_peers: IpvpnGatewayPeers | None = Field(default=None)

    class ConnectedEndpointsKeysItem(BaseModel):
        key: str | None = Field(default=None)
        type: str | None = Field(default=None)
        description: str | None = Field(default=None)

    class CoreInterfaces(BaseModel):
        class P2pLinksIpPoolsItem(BaseModel):
            name: str | None = Field(default=None)
            ipv4_pool: str | None = Field(default=None)
            prefix_size: int = Field(default=31)

        class P2pLinksProfilesItem(BaseModel):
            class Ptp(BaseModel):
                enabled: bool = Field(default=False)

            class PortChannel(BaseModel):
                class NodesChildInterfacesItem(BaseModel):
                    node: str | None = Field(default=None)
                    interfaces: str | None = Field(default=None)

                mode: str = Field(default="active")
                nodes_child_interfaces: NodesChildInterfacesItem | None = Field(default=None)

            name: str | None = Field(default=None)
            id: int | None = Field(default=None)
            speed: str | None = Field(default=None)
            ip_pool: str | None = Field(default=None)
            subnet: str | None = Field(default=None)
            ip: str | None = Field(default=None)
            ipv6_enable: bool = Field(default=False)
            nodes: str | None = Field(default=None)
            interfaces: str | None = Field(default=None)
            as_key: str | None = Field(default=None, alias="as")
            descriptions: str | None = Field(default=None)
            include_in_underlay_protocol: bool = Field(default=True)
            isis_hello_padding: bool = Field(default=False)
            isis_metric: int | None = Field(default=None)
            isis_circuit_type: str | None = Field(default=None)
            isis_authentication_mode: str | None = Field(default=None)
            isis_authentication_key: str | None = Field(default=None)
            mpls_ip: bool | None = Field(default=None)
            mpls_ldp: bool | None = Field(default=None)
            mtu: int | None = Field(default=None)
            bfd: bool = Field(default=False)
            ptp: Ptp | None = Field(default=None)
            sflow: bool | None = Field(default=None)
            qos_profile: str | None = Field(default=None)
            macsec_profile: str | None = Field(default=None)
            port_channel: PortChannel | None = Field(default=None)
            raw_eos_cli: str | None = Field(default=None)
            structured_config: dict | None = Field(default=None)

        class P2pLinksItem(BaseModel):
            class Ptp(BaseModel):
                enabled: bool = Field(default=False)

            class PortChannel(BaseModel):
                class NodesChildInterfacesItem(BaseModel):
                    node: str | None = Field(default=None)
                    interfaces: str | None = Field(default=None)

                mode: str = Field(default="active")
                nodes_child_interfaces: NodesChildInterfacesItem | None = Field(default=None)

            nodes: str = Field(default=None)
            profile: str | None = Field(default=None)
            id: int | None = Field(default=None)
            speed: str | None = Field(default=None)
            ip_pool: str | None = Field(default=None)
            subnet: str | None = Field(default=None)
            ip: str | None = Field(default=None)
            ipv6_enable: bool = Field(default=False)
            interfaces: str | None = Field(default=None)
            as_key: str | None = Field(default=None, alias="as")
            descriptions: str | None = Field(default=None)
            include_in_underlay_protocol: bool = Field(default=True)
            isis_hello_padding: bool = Field(default=False)
            isis_metric: int | None = Field(default=None)
            isis_circuit_type: str | None = Field(default=None)
            isis_authentication_mode: str | None = Field(default=None)
            isis_authentication_key: str | None = Field(default=None)
            mpls_ip: bool | None = Field(default=None)
            mpls_ldp: bool | None = Field(default=None)
            mtu: int | None = Field(default=None)
            bfd: bool = Field(default=False)
            ptp: Ptp | None = Field(default=None)
            sflow: bool | None = Field(default=None)
            qos_profile: str | None = Field(default=None)
            macsec_profile: str | None = Field(default=None)
            port_channel: PortChannel | None = Field(default=None)
            raw_eos_cli: str | None = Field(default=None)
            structured_config: dict | None = Field(default=None)

        p2p_links_ip_pools: P2pLinksIpPoolsItem | None = Field(default=None)
        p2p_links_profiles: P2pLinksProfilesItem | None = Field(default=None)
        p2p_links: P2pLinksItem | None = Field(default=None)

    class DefaultInterfacesItem(BaseModel):
        types: str = Field(default=None)
        platforms: str = Field(default=None)
        uplink_interfaces: str | None = Field(default=None)
        mlag_interfaces: str | None = Field(default=None)
        downlink_interfaces: str | None = Field(default=None)

    class DefaultNodeTypesItem(BaseModel):
        node_type: str | None = Field(default=None)
        match_hostnames: str = Field(default=None)

    class Design(BaseModel):
        type: str = Field(default="l3ls-evpn")

    class EosDesignsCustomTemplatesItem(BaseModel):
        class Options(BaseModel):
            list_merge: str = Field(default="append_rp")
            strip_empty_keys: bool = Field(default=True)

        template: str = Field(default=None)
        options: Options | None = Field(default=None)

    class EosDesignsDocumentation(BaseModel):
        connected_endpoints: bool = Field(default=False)

    class EventHandlersItem(BaseModel):
        name: str | None = Field(default=None)
        action_type: str | None = Field(default=None)
        action: str | None = Field(default=None)
        delay: int | None = Field(default=None)
        trigger: str | None = Field(default=None)
        regex: str | None = Field(default=None)
        asynchronous: bool = Field(default=False)

    class EvpnHostflapDetection(BaseModel):
        enabled: bool = Field(default=True)
        threshold: int = Field(default=5)
        window: int = Field(default=180)
        expiry_timeout: int | None = Field(default=None)

    class FabricIpAddressing(BaseModel):
        class Mlag(BaseModel):
            algorithm: str = Field(default="first_id")

        mlag: Mlag | None = Field(default=None)

    class HardwareCounters(BaseModel):
        class FeaturesItem(BaseModel):
            name: str | None = Field(default=None)
            direction: str | None = Field(default=None)
            address_type: str | None = Field(default=None)
            layer3: bool | None = Field(default=None)
            vrf: str | None = Field(default=None)
            prefix: str | None = Field(default=None)
            units_packets: bool | None = Field(default=None)

        features: FeaturesItem | None = Field(default=None)

    class InternalVlanOrder(BaseModel):
        class Range(BaseModel):
            beginning: int = Field(default=None)
            ending: int = Field(default=None)

        allocation: str = Field(default=None)
        range: Range | None = Field(default=None)

    class IsisTiLfa(BaseModel):
        enabled: bool = Field(default=False)
        protection: str | None = Field(default=None)
        local_convergence_delay: int = Field(default=10000)

    class L3Edge(BaseModel):
        class P2pLinksIpPoolsItem(BaseModel):
            name: str | None = Field(default=None)
            ipv4_pool: str | None = Field(default=None)
            prefix_size: int = Field(default=31)

        class P2pLinksProfilesItem(BaseModel):
            class Ptp(BaseModel):
                enabled: bool = Field(default=False)

            class PortChannel(BaseModel):
                class NodesChildInterfacesItem(BaseModel):
                    node: str | None = Field(default=None)
                    interfaces: str | None = Field(default=None)

                mode: str = Field(default="active")
                nodes_child_interfaces: NodesChildInterfacesItem | None = Field(default=None)

            name: str | None = Field(default=None)
            id: int | None = Field(default=None)
            speed: str | None = Field(default=None)
            ip_pool: str | None = Field(default=None)
            subnet: str | None = Field(default=None)
            ip: str | None = Field(default=None)
            ipv6_enable: bool = Field(default=False)
            nodes: str | None = Field(default=None)
            interfaces: str | None = Field(default=None)
            as_key: str | None = Field(default=None, alias="as")
            descriptions: str | None = Field(default=None)
            include_in_underlay_protocol: bool = Field(default=True)
            isis_hello_padding: bool = Field(default=False)
            isis_metric: int | None = Field(default=None)
            isis_circuit_type: str | None = Field(default=None)
            isis_authentication_mode: str | None = Field(default=None)
            isis_authentication_key: str | None = Field(default=None)
            mpls_ip: bool | None = Field(default=None)
            mpls_ldp: bool | None = Field(default=None)
            mtu: int | None = Field(default=None)
            bfd: bool = Field(default=False)
            ptp: Ptp | None = Field(default=None)
            sflow: bool | None = Field(default=None)
            qos_profile: str | None = Field(default=None)
            macsec_profile: str | None = Field(default=None)
            port_channel: PortChannel | None = Field(default=None)
            raw_eos_cli: str | None = Field(default=None)
            structured_config: dict | None = Field(default=None)

        class P2pLinksItem(BaseModel):
            class Ptp(BaseModel):
                enabled: bool = Field(default=False)

            class PortChannel(BaseModel):
                class NodesChildInterfacesItem(BaseModel):
                    node: str | None = Field(default=None)
                    interfaces: str | None = Field(default=None)

                mode: str = Field(default="active")
                nodes_child_interfaces: NodesChildInterfacesItem | None = Field(default=None)

            nodes: str = Field(default=None)
            profile: str | None = Field(default=None)
            id: int | None = Field(default=None)
            speed: str | None = Field(default=None)
            ip_pool: str | None = Field(default=None)
            subnet: str | None = Field(default=None)
            ip: str | None = Field(default=None)
            ipv6_enable: bool = Field(default=False)
            interfaces: str | None = Field(default=None)
            as_key: str | None = Field(default=None, alias="as")
            descriptions: str | None = Field(default=None)
            include_in_underlay_protocol: bool = Field(default=True)
            isis_hello_padding: bool = Field(default=False)
            isis_metric: int | None = Field(default=None)
            isis_circuit_type: str | None = Field(default=None)
            isis_authentication_mode: str | None = Field(default=None)
            isis_authentication_key: str | None = Field(default=None)
            mpls_ip: bool | None = Field(default=None)
            mpls_ldp: bool | None = Field(default=None)
            mtu: int | None = Field(default=None)
            bfd: bool = Field(default=False)
            ptp: Ptp | None = Field(default=None)
            sflow: bool | None = Field(default=None)
            qos_profile: str | None = Field(default=None)
            macsec_profile: str | None = Field(default=None)
            port_channel: PortChannel | None = Field(default=None)
            raw_eos_cli: str | None = Field(default=None)
            structured_config: dict | None = Field(default=None)

        p2p_links_ip_pools: P2pLinksIpPoolsItem | None = Field(default=None)
        p2p_links_profiles: P2pLinksProfilesItem | None = Field(default=None)
        p2p_links: P2pLinksItem | None = Field(default=None)

    class LocalUsersItem(BaseModel):
        name: str | None = Field(default=None)
        disabled: bool | None = Field(default=None)
        privilege: int | None = Field(default=None)
        role: str | None = Field(default=None)
        sha512_password: str | None = Field(default=None)
        no_password: bool | None = Field(default=None)
        ssh_key: str | None = Field(default=None)
        shell: str | None = Field(default=None)

    class MacAddressTable(BaseModel):
        aging_time: int | None = Field(default=None)

    class ManagementEapi(BaseModel):
        enable_http: bool = Field(default=False)
        enable_https: bool = Field(default=True)
        default_services: bool | None = Field(default=None)

    class MlagIbgpPeeringVrfs(BaseModel):
        base_vlan: int = Field(default=3000)

    class NetworkPortsItem(BaseModel):
        class Flowcontrol(BaseModel):
            received: str | None = Field(default=None)

        class Ptp(BaseModel):
            enabled: bool = Field(default=False)
            endpoint_role: str = Field(default="follower")
            profile: str = Field(default="aes67-r16-2016")

        class LinkTracking(BaseModel):
            enabled: bool | None = Field(default=None)
            name: str | None = Field(default=None)

        class Dot1x(BaseModel):
            class Pae(BaseModel):
                mode: str | None = Field(default=None)

            class AuthenticationFailure(BaseModel):
                action: str | None = Field(default=None)
                allow_vlan: int | None = Field(default=None)

            class HostMode(BaseModel):
                mode: str | None = Field(default=None)
                multi_host_authenticated: bool | None = Field(default=None)

            class MacBasedAuthentication(BaseModel):
                enabled: bool | None = Field(default=None)
                always: bool | None = Field(default=None)
                host_mode_common: bool | None = Field(default=None)

            class Timeout(BaseModel):
                idle_host: int | None = Field(default=None)
                quiet_period: int | None = Field(default=None)
                reauth_period: str | None = Field(default=None)
                reauth_timeout_ignore: bool | None = Field(default=None)
                tx_period: int | None = Field(default=None)

            port_control: str | None = Field(default=None)
            port_control_force_authorized_phone: bool | None = Field(default=None)
            reauthentication: bool | None = Field(default=None)
            pae: Pae | None = Field(default=None)
            authentication_failure: AuthenticationFailure | None = Field(default=None)
            host_mode: HostMode | None = Field(default=None)
            mac_based_authentication: MacBasedAuthentication | None = Field(default=None)
            timeout: Timeout | None = Field(default=None)
            reauthorization_request_limit: int | None = Field(default=None)

        class Poe(BaseModel):
            class Reboot(BaseModel):
                action: str | None = Field(default=None)

            class LinkDown(BaseModel):
                action: str | None = Field(default=None)
                power_off_delay: int | None = Field(default=None)

            class Shutdown(BaseModel):
                action: str | None = Field(default=None)

            class Limit(BaseModel):
                class_key: int | None = Field(default=None, alias="class")
                watts: str | None = Field(default=None)
                fixed: bool | None = Field(default=None)

            disabled: bool = Field(default=False)
            priority: str | None = Field(default=None)
            reboot: Reboot | None = Field(default=None)
            link_down: LinkDown | None = Field(default=None)
            shutdown: Shutdown | None = Field(default=None)
            limit: Limit | None = Field(default=None)
            negotiation_lldp: bool | None = Field(default=None)
            legacy_detect: bool | None = Field(default=None)

        class StormControl(BaseModel):
            class All(BaseModel):
                level: str | None = Field(default=None)
                unit: str = Field(default="percent")

            class Broadcast(BaseModel):
                level: str | None = Field(default=None)
                unit: str = Field(default="percent")

            class Multicast(BaseModel):
                level: str | None = Field(default=None)
                unit: str = Field(default="percent")

            class UnknownUnicast(BaseModel):
                level: str | None = Field(default=None)
                unit: str = Field(default="percent")

            all: All | None = Field(default=None)
            broadcast: Broadcast | None = Field(default=None)
            multicast: Multicast | None = Field(default=None)
            unknown_unicast: UnknownUnicast | None = Field(default=None)

        class MonitorSessionsItem(BaseModel):
            class SourceSettings(BaseModel):
                class AccessGroup(BaseModel):
                    type: str | None = Field(default=None)
                    name: str | None = Field(default=None)
                    priority: int | None = Field(default=None)

                direction: str | None = Field(default=None)
                access_group: AccessGroup | None = Field(default=None)

            class SessionSettings(BaseModel):
                class AccessGroup(BaseModel):
                    type: str | None = Field(default=None)
                    name: str | None = Field(default=None)

                class Truncate(BaseModel):
                    enabled: bool | None = Field(default=None)
                    size: int | None = Field(default=None)

                encapsulation_gre_metadata_tx: bool | None = Field(default=None)
                header_remove_size: int | None = Field(default=None)
                access_group: AccessGroup | None = Field(default=None)
                rate_limit_per_ingress_chip: str | None = Field(default=None)
                rate_limit_per_egress_chip: str | None = Field(default=None)
                sample: int | None = Field(default=None)
                truncate: Truncate | None = Field(default=None)

            name: str = Field(default=None)
            role: str | None = Field(default=None)
            source_settings: SourceSettings | None = Field(default=None)
            session_settings: SessionSettings | None = Field(default=None)

        class EthernetSegment(BaseModel):
            short_esi: str = Field(default=None)
            redundancy: str | None = Field(default=None)
            designated_forwarder_algorithm: str | None = Field(default=None)
            designated_forwarder_preferences: str | None = Field(default=None)
            dont_preempt: bool | None = Field(default=None)

        class PortChannel(BaseModel):
            class LacpFallback(BaseModel):
                mode: str | None = Field(default=None)
                timeout: int | None = Field(default=None)

            class LacpTimer(BaseModel):
                mode: str | None = Field(default=None)
                multiplier: int | None = Field(default=None)

            class SubinterfacesItem(BaseModel):
                class EncapsulationVlan(BaseModel):
                    client_dot1q: int | None = Field(default=None)

                number: int | None = Field(default=None)
                short_esi: str | None = Field(default=None)
                vlan_id: int | None = Field(default=None)
                encapsulation_vlan: EncapsulationVlan | None = Field(default=None)

            class StructuredConfig(BaseModel):
                class Logging(BaseModel):
                    class Event(BaseModel):
                        link_status: bool | None = Field(default=None)

                    event: Event | None = Field(default=None)

                class EncapsulationVlan(BaseModel):
                    class Client(BaseModel):
                        class Dot1q(BaseModel):
                            vlan: int | None = Field(default=None)
                            outer: int | None = Field(default=None)
                            inner: int | None = Field(default=None)

                        dot1q: Dot1q | None = Field(default=None)
                        unmatched: bool | None = Field(default=None)

                    class Network(BaseModel):
                        class Dot1q(BaseModel):
                            vlan: int | None = Field(default=None)
                            outer: int | None = Field(default=None)
                            inner: int | None = Field(default=None)

                        dot1q: Dot1q | None = Field(default=None)
                        client: bool | None = Field(default=None)

                    client: Client | None = Field(default=None)
                    network: Network | None = Field(default=None)

                class LinkTrackingGroupsItem(BaseModel):
                    name: str | None = Field(default=None)
                    direction: str | None = Field(default=None)

                class Phone(BaseModel):
                    trunk: str | None = Field(default=None)
                    vlan: int | None = Field(default=None)

                class L2Protocol(BaseModel):
                    encapsulation_dot1q_vlan: int | None = Field(default=None)
                    forwarding_profile: str | None = Field(default=None)

                class Qos(BaseModel):
                    trust: str | None = Field(default=None)
                    dscp: int | None = Field(default=None)
                    cos: int | None = Field(default=None)

                class Bfd(BaseModel):
                    echo: bool | None = Field(default=None)
                    interval: int | None = Field(default=None)
                    min_rx: int | None = Field(default=None)
                    multiplier: int | None = Field(default=None)

                class ServicePolicy(BaseModel):
                    class Pbr(BaseModel):
                        input: str | None = Field(default=None)

                    class Qos(BaseModel):
                        input: str = Field(default=None)

                    pbr: Pbr | None = Field(default=None)
                    qos: Qos | None = Field(default=None)

                class Mpls(BaseModel):
                    class Ldp(BaseModel):
                        interface: bool | None = Field(default=None)
                        igp_sync: bool | None = Field(default=None)

                    ip: bool | None = Field(default=None)
                    ldp: Ldp | None = Field(default=None)

                class VlanTranslationsItem(BaseModel):
                    from_key: str | None = Field(default=None, alias="from")
                    to: int | None = Field(default=None)
                    direction: str = Field(default="both")

                class Shape(BaseModel):
                    rate: str | None = Field(default=None)

                class StormControl(BaseModel):
                    class All(BaseModel):
                        level: str | None = Field(default=None)
                        unit: str = Field(default="percent")

                    class Broadcast(BaseModel):
                        level: str | None = Field(default=None)
                        unit: str = Field(default="percent")

                    class Multicast(BaseModel):
                        level: str | None = Field(default=None)
                        unit: str = Field(default="percent")

                    class UnknownUnicast(BaseModel):
                        level: str | None = Field(default=None)
                        unit: str = Field(default="percent")

                    all: All | None = Field(default=None)
                    broadcast: Broadcast | None = Field(default=None)
                    multicast: Multicast | None = Field(default=None)
                    unknown_unicast: UnknownUnicast | None = Field(default=None)

                class TrafficPolicy(BaseModel):
                    input: str | None = Field(default=None)
                    output: str | None = Field(default=None)

                class EvpnEthernetSegment(BaseModel):
                    class DesignatedForwarderElection(BaseModel):
                        algorithm: str | None = Field(default=None)
                        preference_value: int | None = Field(default=None)
                        dont_preempt: bool = Field(default=False)
                        hold_time: int | None = Field(default=None)
                        subsequent_hold_time: int | None = Field(default=None)
                        candidate_reachability_required: bool | None = Field(default=None)

                    class Mpls(BaseModel):
                        shared_index: int | None = Field(default=None)
                        tunnel_flood_filter_time: int | None = Field(default=None)

                    identifier: str | None = Field(default=None)
                    redundancy: str | None = Field(default=None)
                    designated_forwarder_election: DesignatedForwarderElection | None = Field(default=None)
                    mpls: Mpls | None = Field(default=None)
                    route_target: str | None = Field(default=None)

                class Ptp(BaseModel):
                    class Announce(BaseModel):
                        interval: int | None = Field(default=None)
                        timeout: int | None = Field(default=None)

                    class SyncMessage(BaseModel):
                        interval: int | None = Field(default=None)

                    enable: bool | None = Field(default=None)
                    announce: Announce | None = Field(default=None)
                    delay_req: int | None = Field(default=None)
                    delay_mechanism: str | None = Field(default=None)
                    sync_message: SyncMessage | None = Field(default=None)
                    role: str | None = Field(default=None)
                    vlan: str | None = Field(default=None)
                    transport: str | None = Field(default=None)

                class IpNat(BaseModel):
                    class Destination(BaseModel):
                        class DynamicItem(BaseModel):
                            access_list: str | None = Field(default=None)
                            comment: str | None = Field(default=None)
                            pool_name: str = Field(default=None)
                            priority: int | None = Field(default=None)

                        class StaticItem(BaseModel):
                            access_list: str | None = Field(default=None)
                            comment: str | None = Field(default=None)
                            direction: str | None = Field(default=None)
                            group: int | None = Field(default=None)
                            original_ip: str | None = Field(default=None)
                            original_port: int | None = Field(default=None)
                            priority: int | None = Field(default=None)
                            protocol: str | None = Field(default=None)
                            translated_ip: str = Field(default=None)
                            translated_port: int | None = Field(default=None)

                        dynamic: DynamicItem | None = Field(default=None)
                        static: StaticItem | None = Field(default=None)

                    class Source(BaseModel):
                        class DynamicItem(BaseModel):
                            access_list: str | None = Field(default=None)
                            comment: str | None = Field(default=None)
                            nat_type: str = Field(default=None)
                            pool_name: str | None = Field(default=None)
                            priority: int | None = Field(default=None)

                        class StaticItem(BaseModel):
                            access_list: str | None = Field(default=None)
                            comment: str | None = Field(default=None)
                            direction: str | None = Field(default=None)
                            group: int | None = Field(default=None)
                            original_ip: str | None = Field(default=None)
                            original_port: int | None = Field(default=None)
                            priority: int | None = Field(default=None)
                            protocol: str | None = Field(default=None)
                            translated_ip: str = Field(default=None)
                            translated_port: int | None = Field(default=None)

                        dynamic: DynamicItem | None = Field(default=None)
                        static: StaticItem | None = Field(default=None)

                    destination: Destination | None = Field(default=None)
                    source: Source | None = Field(default=None)

                class Ipv6NdPrefixesItem(BaseModel):
                    ipv6_prefix: str | None = Field(default=None)
                    valid_lifetime: str | None = Field(default=None)
                    preferred_lifetime: str | None = Field(default=None)
                    no_autoconfig_flag: bool | None = Field(default=None)

                class Pim(BaseModel):
                    class Ipv4(BaseModel):
                        dr_priority: int | None = Field(default=None)
                        sparse_mode: bool | None = Field(default=None)

                    ipv4: Ipv4 | None = Field(default=None)

                class OspfMessageDigestKeysItem(BaseModel):
                    id: int | None = Field(default=None)
                    hash_algorithm: str | None = Field(default=None)
                    key: str | None = Field(default=None)

                class FlowTracker(BaseModel):
                    sampled: str | None = Field(default=None)

                class Bgp(BaseModel):
                    session_tracker: str | None = Field(default=None)

                class Sflow(BaseModel):
                    class Egress(BaseModel):
                        enable: bool | None = Field(default=None)
                        unmodified_enable: bool | None = Field(default=None)

                    enable: bool | None = Field(default=None)
                    egress: Egress | None = Field(default=None)

                name: str | None = Field(default=None)
                description: str | None = Field(default=None)
                logging: Logging | None = Field(default=None)
                shutdown: bool | None = Field(default=None)
                l2_mtu: int | None = Field(default=None)
                vlans: str | None = Field(default=None)
                snmp_trap_link_change: bool | None = Field(default=None)
                type: str | None = Field(default=None)
                encapsulation_dot1q_vlan: int | None = Field(default=None)
                vrf: str | None = Field(default=None)
                encapsulation_vlan: EncapsulationVlan | None = Field(default=None)
                vlan_id: int | None = Field(default=None)
                mode: str | None = Field(default=None)
                native_vlan: int | None = Field(default=None)
                native_vlan_tag: bool = Field(default=False)
                link_tracking_groups: LinkTrackingGroupsItem | None = Field(default=None)
                phone: Phone | None = Field(default=None)
                l2_protocol: L2Protocol | None = Field(default=None)
                mtu: int | None = Field(default=None)
                mlag: int | None = Field(default=None)
                trunk_groups: str | None = Field(default=None)
                lacp_fallback_timeout: int = Field(default=90)
                lacp_fallback_mode: str | None = Field(default=None)
                qos: Qos | None = Field(default=None)
                bfd: Bfd | None = Field(default=None)
                service_policy: ServicePolicy | None = Field(default=None)
                mpls: Mpls | None = Field(default=None)
                trunk_private_vlan_secondary: bool | None = Field(default=None)
                pvlan_mapping: str | None = Field(default=None)
                vlan_translations: VlanTranslationsItem | None = Field(default=None)
                shape: Shape | None = Field(default=None)
                storm_control: StormControl | None = Field(default=None)
                ip_proxy_arp: bool | None = Field(default=None)
                isis_enable: str | None = Field(default=None)
                isis_passive: bool | None = Field(default=None)
                isis_metric: int | None = Field(default=None)
                isis_network_point_to_point: bool | None = Field(default=None)
                isis_circuit_type: str | None = Field(default=None)
                isis_hello_padding: bool | None = Field(default=None)
                isis_authentication_mode: str | None = Field(default=None)
                isis_authentication_key: str | None = Field(default=None)
                traffic_policy: TrafficPolicy | None = Field(default=None)
                evpn_ethernet_segment: EvpnEthernetSegment | None = Field(default=None)
                esi: str | None = Field(default=None)
                rt: str | None = Field(default=None)
                lacp_id: str | None = Field(default=None)
                spanning_tree_bpdufilter: str | None = Field(default=None)
                spanning_tree_bpduguard: str | None = Field(default=None)
                spanning_tree_guard: str | None = Field(default=None)
                spanning_tree_portfast: str | None = Field(default=None)
                vmtracer: bool | None = Field(default=None)
                ptp: Ptp | None = Field(default=None)
                ip_address: str | None = Field(default=None)
                ip_nat: IpNat | None = Field(default=None)
                ipv6_enable: bool | None = Field(default=None)
                ipv6_address: str | None = Field(default=None)
                ipv6_address_link_local: str | None = Field(default=None)
                ipv6_nd_ra_disabled: bool | None = Field(default=None)
                ipv6_nd_managed_config_flag: bool | None = Field(default=None)
                ipv6_nd_prefixes: Ipv6NdPrefixesItem | None = Field(default=None)
                access_group_in: str | None = Field(default=None)
                access_group_out: str | None = Field(default=None)
                ipv6_access_group_in: str | None = Field(default=None)
                ipv6_access_group_out: str | None = Field(default=None)
                mac_access_group_in: str | None = Field(default=None)
                mac_access_group_out: str | None = Field(default=None)
                pim: Pim | None = Field(default=None)
                service_profile: str | None = Field(default=None)
                ospf_network_point_to_point: bool | None = Field(default=None)
                ospf_area: str | None = Field(default=None)
                ospf_cost: int | None = Field(default=None)
                ospf_authentication: str | None = Field(default=None)
                ospf_authentication_key: str | None = Field(default=None)
                ospf_message_digest_keys: OspfMessageDigestKeysItem | None = Field(default=None)
                flow_tracker: FlowTracker | None = Field(default=None)
                bgp: Bgp | None = Field(default=None)
                peer: str | None = Field(default=None)
                peer_interface: str | None = Field(default=None)
                peer_type: str | None = Field(default=None)
                sflow: Sflow | None = Field(default=None)
                eos_cli: str | None = Field(default=None)

            mode: str | None = Field(default=None)
            channel_id: int | None = Field(default=None)
            description: str | None = Field(default=None)
            enabled: bool = Field(default=True)
            short_esi: str | None = Field(default=None)
            lacp_fallback: LacpFallback | None = Field(default=None)
            lacp_timer: LacpTimer | None = Field(default=None)
            subinterfaces: SubinterfacesItem | None = Field(default=None)
            raw_eos_cli: str | None = Field(default=None)
            structured_config: StructuredConfig | None = Field(default=None)

        class StructuredConfig(BaseModel):
            class Phone(BaseModel):
                trunk: str | None = Field(default=None)
                vlan: int | None = Field(default=None)

            class L2Protocol(BaseModel):
                encapsulation_dot1q_vlan: int | None = Field(default=None)
                forwarding_profile: str | None = Field(default=None)

            class AddressLocking(BaseModel):
                ipv4: bool | None = Field(default=None)
                ipv6: bool | None = Field(default=None)

            class Flowcontrol(BaseModel):
                received: str | None = Field(default=None)

            class FlowTracker(BaseModel):
                sampled: str | None = Field(default=None)

            class ErrorCorrectionEncoding(BaseModel):
                enabled: bool = Field(default=True)
                fire_code: bool | None = Field(default=None)
                reed_solomon: bool | None = Field(default=None)

            class LinkTrackingGroupsItem(BaseModel):
                name: str | None = Field(default=None)
                direction: str | None = Field(default=None)

            class EvpnEthernetSegment(BaseModel):
                class DesignatedForwarderElection(BaseModel):
                    algorithm: str | None = Field(default=None)
                    preference_value: int | None = Field(default=None)
                    dont_preempt: bool | None = Field(default=None)
                    hold_time: int | None = Field(default=None)
                    subsequent_hold_time: int | None = Field(default=None)
                    candidate_reachability_required: bool | None = Field(default=None)

                class Mpls(BaseModel):
                    shared_index: int | None = Field(default=None)
                    tunnel_flood_filter_time: int | None = Field(default=None)

                identifier: str | None = Field(default=None)
                redundancy: str | None = Field(default=None)
                designated_forwarder_election: DesignatedForwarderElection | None = Field(default=None)
                mpls: Mpls | None = Field(default=None)
                route_target: str | None = Field(default=None)

            class EncapsulationVlan(BaseModel):
                class Client(BaseModel):
                    class Dot1q(BaseModel):
                        vlan: int | None = Field(default=None)
                        outer: int | None = Field(default=None)
                        inner: int | None = Field(default=None)

                    dot1q: Dot1q | None = Field(default=None)
                    unmatched: bool | None = Field(default=None)

                class Network(BaseModel):
                    class Dot1q(BaseModel):
                        vlan: int | None = Field(default=None)
                        outer: int | None = Field(default=None)
                        inner: int | None = Field(default=None)

                    dot1q: Dot1q | None = Field(default=None)
                    client: bool | None = Field(default=None)

                client: Client | None = Field(default=None)
                network: Network | None = Field(default=None)

            class IpHelpersItem(BaseModel):
                ip_helper: str | None = Field(default=None)
                source_interface: str | None = Field(default=None)
                vrf: str | None = Field(default=None)

            class IpNat(BaseModel):
                class Destination(BaseModel):
                    class DynamicItem(BaseModel):
                        access_list: str | None = Field(default=None)
                        comment: str | None = Field(default=None)
                        pool_name: str = Field(default=None)
                        priority: int | None = Field(default=None)

                    class StaticItem(BaseModel):
                        access_list: str | None = Field(default=None)
                        comment: str | None = Field(default=None)
                        direction: str | None = Field(default=None)
                        group: int | None = Field(default=None)
                        original_ip: str | None = Field(default=None)
                        original_port: int | None = Field(default=None)
                        priority: int | None = Field(default=None)
                        protocol: str | None = Field(default=None)
                        translated_ip: str = Field(default=None)
                        translated_port: int | None = Field(default=None)

                    dynamic: DynamicItem | None = Field(default=None)
                    static: StaticItem | None = Field(default=None)

                class Source(BaseModel):
                    class DynamicItem(BaseModel):
                        access_list: str | None = Field(default=None)
                        comment: str | None = Field(default=None)
                        nat_type: str = Field(default=None)
                        pool_name: str | None = Field(default=None)
                        priority: int | None = Field(default=None)

                    class StaticItem(BaseModel):
                        access_list: str | None = Field(default=None)
                        comment: str | None = Field(default=None)
                        direction: str | None = Field(default=None)
                        group: int | None = Field(default=None)
                        original_ip: str | None = Field(default=None)
                        original_port: int | None = Field(default=None)
                        priority: int | None = Field(default=None)
                        protocol: str | None = Field(default=None)
                        translated_ip: str = Field(default=None)
                        translated_port: int | None = Field(default=None)

                    dynamic: DynamicItem | None = Field(default=None)
                    static: StaticItem | None = Field(default=None)

                destination: Destination | None = Field(default=None)
                source: Source | None = Field(default=None)

            class Ipv6NdPrefixesItem(BaseModel):
                ipv6_prefix: str | None = Field(default=None)
                valid_lifetime: str | None = Field(default=None)
                preferred_lifetime: str | None = Field(default=None)
                no_autoconfig_flag: bool | None = Field(default=None)

            class Ipv6DhcpRelayDestinationsItem(BaseModel):
                address: str | None = Field(default=None)
                vrf: str | None = Field(default=None)
                local_interface: str | None = Field(default=None)
                source_address: str | None = Field(default=None)
                link_address: str | None = Field(default=None)

            class Multicast(BaseModel):
                class Ipv4(BaseModel):
                    class BoundariesItem(BaseModel):
                        boundary: str | None = Field(default=None)
                        out: bool | None = Field(default=None)

                    boundaries: BoundariesItem | None = Field(default=None)
                    static: bool | None = Field(default=None)

                class Ipv6(BaseModel):
                    class BoundariesItem(BaseModel):
                        boundary: str | None = Field(default=None)

                    boundaries: BoundariesItem | None = Field(default=None)
                    static: bool | None = Field(default=None)

                ipv4: Ipv4 | None = Field(default=None)
                ipv6: Ipv6 | None = Field(default=None)

            class OspfMessageDigestKeysItem(BaseModel):
                id: int | None = Field(default=None)
                hash_algorithm: str | None = Field(default=None)
                key: str | None = Field(default=None)

            class Pim(BaseModel):
                class Ipv4(BaseModel):
                    dr_priority: int | None = Field(default=None)
                    sparse_mode: bool | None = Field(default=None)

                ipv4: Ipv4 | None = Field(default=None)

            class MacSecurity(BaseModel):
                profile: str | None = Field(default=None)

            class ChannelGroup(BaseModel):
                id: int | None = Field(default=None)
                mode: str | None = Field(default=None)

            class Poe(BaseModel):
                class Reboot(BaseModel):
                    action: str | None = Field(default=None)

                class LinkDown(BaseModel):
                    action: str | None = Field(default=None)
                    power_off_delay: int | None = Field(default=None)

                class Shutdown(BaseModel):
                    action: str | None = Field(default=None)

                class Limit(BaseModel):
                    class_key: int | None = Field(default=None, alias="class")
                    watts: str | None = Field(default=None)
                    fixed: bool | None = Field(default=None)

                disabled: bool = Field(default=False)
                priority: str | None = Field(default=None)
                reboot: Reboot | None = Field(default=None)
                link_down: LinkDown | None = Field(default=None)
                shutdown: Shutdown | None = Field(default=None)
                limit: Limit | None = Field(default=None)
                negotiation_lldp: bool | None = Field(default=None)
                legacy_detect: bool | None = Field(default=None)

            class Ptp(BaseModel):
                class Announce(BaseModel):
                    interval: int | None = Field(default=None)
                    timeout: int | None = Field(default=None)

                class SyncMessage(BaseModel):
                    interval: int | None = Field(default=None)

                enable: bool | None = Field(default=None)
                announce: Announce | None = Field(default=None)
                delay_req: int | None = Field(default=None)
                delay_mechanism: str | None = Field(default=None)
                sync_message: SyncMessage | None = Field(default=None)
                role: str | None = Field(default=None)
                vlan: str | None = Field(default=None)
                transport: str | None = Field(default=None)

            class StormControl(BaseModel):
                class All(BaseModel):
                    level: str | None = Field(default=None)
                    unit: str = Field(default="percent")

                class Broadcast(BaseModel):
                    level: str | None = Field(default=None)
                    unit: str = Field(default="percent")

                class Multicast(BaseModel):
                    level: str | None = Field(default=None)
                    unit: str = Field(default="percent")

                class UnknownUnicast(BaseModel):
                    level: str | None = Field(default=None)
                    unit: str = Field(default="percent")

                all: All | None = Field(default=None)
                broadcast: Broadcast | None = Field(default=None)
                multicast: Multicast | None = Field(default=None)
                unknown_unicast: UnknownUnicast | None = Field(default=None)

            class Logging(BaseModel):
                class Event(BaseModel):
                    link_status: bool | None = Field(default=None)
                    congestion_drops: bool | None = Field(default=None)
                    spanning_tree: bool | None = Field(default=None)
                    storm_control: bool | None = Field(default=None)

                event: Event | None = Field(default=None)

            class Lldp(BaseModel):
                transmit: bool | None = Field(default=None)
                receive: bool | None = Field(default=None)
                ztp_vlan: int | None = Field(default=None)

            class VlanTranslationsItem(BaseModel):
                from_key: str | None = Field(default=None, alias="from")
                to: int | None = Field(default=None)
                direction: str = Field(default="both")

            class Dot1x(BaseModel):
                class Pae(BaseModel):
                    mode: str | None = Field(default=None)

                class AuthenticationFailure(BaseModel):
                    action: str | None = Field(default=None)
                    allow_vlan: int | None = Field(default=None)

                class HostMode(BaseModel):
                    mode: str | None = Field(default=None)
                    multi_host_authenticated: bool | None = Field(default=None)

                class MacBasedAuthentication(BaseModel):
                    enabled: bool | None = Field(default=None)
                    always: bool | None = Field(default=None)
                    host_mode_common: bool | None = Field(default=None)

                class Timeout(BaseModel):
                    idle_host: int | None = Field(default=None)
                    quiet_period: int | None = Field(default=None)
                    reauth_period: str | None = Field(default=None)
                    reauth_timeout_ignore: bool | None = Field(default=None)
                    tx_period: int | None = Field(default=None)

                class Unauthorized(BaseModel):
                    access_vlan_membership_egress: bool | None = Field(default=None)
                    native_vlan_membership_egress: bool | None = Field(default=None)

                class Eapol(BaseModel):
                    class AuthenticationFailureFallbackMba(BaseModel):
                        enabled: bool | None = Field(default=None)
                        timeout: int | None = Field(default=None)

                    disabled: bool | None = Field(default=None)
                    authentication_failure_fallback_mba: AuthenticationFailureFallbackMba | None = Field(default=None)

                port_control: str | None = Field(default=None)
                port_control_force_authorized_phone: bool | None = Field(default=None)
                reauthentication: bool | None = Field(default=None)
                pae: Pae | None = Field(default=None)
                authentication_failure: AuthenticationFailure | None = Field(default=None)
                host_mode: HostMode | None = Field(default=None)
                mac_based_authentication: MacBasedAuthentication | None = Field(default=None)
                timeout: Timeout | None = Field(default=None)
                reauthorization_request_limit: int | None = Field(default=None)
                unauthorized: Unauthorized | None = Field(default=None)
                eapol: Eapol | None = Field(default=None)

            class Shape(BaseModel):
                rate: str | None = Field(default=None)

            class Qos(BaseModel):
                trust: str | None = Field(default=None)
                dscp: int | None = Field(default=None)
                cos: int | None = Field(default=None)

            class PriorityFlowControl(BaseModel):
                class PrioritiesItem(BaseModel):
                    priority: int | None = Field(default=None)
                    no_drop: bool | None = Field(default=None)

                enabled: bool | None = Field(default=None)
                priorities: PrioritiesItem | None = Field(default=None)

            class Bfd(BaseModel):
                echo: bool | None = Field(default=None)
                interval: int | None = Field(default=None)
                min_rx: int | None = Field(default=None)
                multiplier: int | None = Field(default=None)

            class ServicePolicy(BaseModel):
                class Pbr(BaseModel):
                    input: str | None = Field(default=None)

                class Qos(BaseModel):
                    input: str = Field(default=None)

                pbr: Pbr | None = Field(default=None)
                qos: Qos | None = Field(default=None)

            class Mpls(BaseModel):
                class Ldp(BaseModel):
                    interface: bool | None = Field(default=None)
                    igp_sync: bool | None = Field(default=None)

                ip: bool | None = Field(default=None)
                ldp: Ldp | None = Field(default=None)

            class LacpTimer(BaseModel):
                mode: str | None = Field(default=None)
                multiplier: int | None = Field(default=None)

            class Transceiver(BaseModel):
                class Media(BaseModel):
                    override: str | None = Field(default=None)

                media: Media | None = Field(default=None)

            class TrafficPolicy(BaseModel):
                input: str | None = Field(default=None)
                output: str | None = Field(default=None)

            class Bgp(BaseModel):
                session_tracker: str | None = Field(default=None)

            class Sflow(BaseModel):
                class Egress(BaseModel):
                    enable: bool | None = Field(default=None)
                    unmodified_enable: bool | None = Field(default=None)

                enable: bool | None = Field(default=None)
                egress: Egress | None = Field(default=None)

            name: str | None = Field(default=None)
            description: str | None = Field(default=None)
            shutdown: bool | None = Field(default=None)
            load_interval: int | None = Field(default=None)
            speed: str | None = Field(default=None)
            mtu: int | None = Field(default=None)
            l2_mtu: int | None = Field(default=None)
            vlans: str | None = Field(default=None)
            native_vlan: int | None = Field(default=None)
            native_vlan_tag: bool | None = Field(default=None)
            mode: str | None = Field(default=None)
            phone: Phone | None = Field(default=None)
            l2_protocol: L2Protocol | None = Field(default=None)
            trunk_groups: str | None = Field(default=None)
            type: str | None = Field(default=None)
            snmp_trap_link_change: bool | None = Field(default=None)
            address_locking: AddressLocking | None = Field(default=None)
            flowcontrol: Flowcontrol | None = Field(default=None)
            vrf: str | None = Field(default=None)
            flow_tracker: FlowTracker | None = Field(default=None)
            error_correction_encoding: ErrorCorrectionEncoding | None = Field(default=None)
            link_tracking_groups: LinkTrackingGroupsItem | None = Field(default=None)
            evpn_ethernet_segment: EvpnEthernetSegment | None = Field(default=None)
            encapsulation_dot1q_vlan: int | None = Field(default=None)
            encapsulation_vlan: EncapsulationVlan | None = Field(default=None)
            vlan_id: int | None = Field(default=None)
            ip_address: str | None = Field(default=None)
            ip_address_secondaries: str | None = Field(default=None)
            ip_helpers: IpHelpersItem | None = Field(default=None)
            ip_nat: IpNat | None = Field(default=None)
            ipv6_enable: bool | None = Field(default=None)
            ipv6_address: str | None = Field(default=None)
            ipv6_address_link_local: str | None = Field(default=None)
            ipv6_nd_ra_disabled: bool | None = Field(default=None)
            ipv6_nd_managed_config_flag: bool | None = Field(default=None)
            ipv6_nd_prefixes: Ipv6NdPrefixesItem | None = Field(default=None)
            ipv6_dhcp_relay_destinations: Ipv6DhcpRelayDestinationsItem | None = Field(default=None)
            access_group_in: str | None = Field(default=None)
            access_group_out: str | None = Field(default=None)
            ipv6_access_group_in: str | None = Field(default=None)
            ipv6_access_group_out: str | None = Field(default=None)
            mac_access_group_in: str | None = Field(default=None)
            mac_access_group_out: str | None = Field(default=None)
            multicast: Multicast | None = Field(default=None)
            ospf_network_point_to_point: bool | None = Field(default=None)
            ospf_area: str | None = Field(default=None)
            ospf_cost: int | None = Field(default=None)
            ospf_authentication: str | None = Field(default=None)
            ospf_authentication_key: str | None = Field(default=None)
            ospf_message_digest_keys: OspfMessageDigestKeysItem | None = Field(default=None)
            pim: Pim | None = Field(default=None)
            mac_security: MacSecurity | None = Field(default=None)
            channel_group: ChannelGroup | None = Field(default=None)
            isis_enable: str | None = Field(default=None)
            isis_passive: bool | None = Field(default=None)
            isis_metric: int | None = Field(default=None)
            isis_network_point_to_point: bool | None = Field(default=None)
            isis_circuit_type: str | None = Field(default=None)
            isis_hello_padding: bool | None = Field(default=None)
            isis_authentication_mode: str | None = Field(default=None)
            isis_authentication_key: str | None = Field(default=None)
            poe: Poe | None = Field(default=None)
            ptp: Ptp | None = Field(default=None)
            profile: str | None = Field(default=None)
            storm_control: StormControl | None = Field(default=None)
            logging: Logging | None = Field(default=None)
            lldp: Lldp | None = Field(default=None)
            trunk_private_vlan_secondary: bool | None = Field(default=None)
            pvlan_mapping: str | None = Field(default=None)
            vlan_translations: VlanTranslationsItem | None = Field(default=None)
            dot1x: Dot1x | None = Field(default=None)
            service_profile: str | None = Field(default=None)
            shape: Shape | None = Field(default=None)
            qos: Qos | None = Field(default=None)
            spanning_tree_bpdufilter: str | None = Field(default=None)
            spanning_tree_bpduguard: str | None = Field(default=None)
            spanning_tree_guard: str | None = Field(default=None)
            spanning_tree_portfast: str | None = Field(default=None)
            vmtracer: bool | None = Field(default=None)
            priority_flow_control: PriorityFlowControl | None = Field(default=None)
            bfd: Bfd | None = Field(default=None)
            service_policy: ServicePolicy | None = Field(default=None)
            mpls: Mpls | None = Field(default=None)
            lacp_timer: LacpTimer | None = Field(default=None)
            lacp_port_priority: int | None = Field(default=None)
            transceiver: Transceiver | None = Field(default=None)
            ip_proxy_arp: bool | None = Field(default=None)
            traffic_policy: TrafficPolicy | None = Field(default=None)
            bgp: Bgp | None = Field(default=None)
            peer: str | None = Field(default=None)
            peer_interface: str | None = Field(default=None)
            peer_type: str | None = Field(default=None)
            sflow: Sflow | None = Field(default=None)
            port_profile: str | None = Field(default=None)
            eos_cli: str | None = Field(default=None)

        switches: str | None = Field(default=None)
        switch_ports: str | None = Field(default=None)
        description: str | None = Field(default=None)
        speed: str | None = Field(default=None)
        profile: str | None = Field(default=None)
        enabled: bool = Field(default=True)
        mode: str | None = Field(default=None)
        mtu: int | None = Field(default=None)
        l2_mtu: int | None = Field(default=None)
        native_vlan: int | None = Field(default=None)
        native_vlan_tag: bool = Field(default=False)
        trunk_groups: str | None = Field(default=None)
        vlans: str | None = Field(default=None)
        spanning_tree_portfast: str | None = Field(default=None)
        spanning_tree_bpdufilter: str | None = Field(default=None)
        spanning_tree_bpduguard: str | None = Field(default=None)
        flowcontrol: Flowcontrol | None = Field(default=None)
        qos_profile: str | None = Field(default=None)
        ptp: Ptp | None = Field(default=None)
        sflow: bool | None = Field(default=None)
        link_tracking: LinkTracking | None = Field(default=None)
        dot1x: Dot1x | None = Field(default=None)
        poe: Poe | None = Field(default=None)
        storm_control: StormControl | None = Field(default=None)
        monitor_sessions: MonitorSessionsItem | None = Field(default=None)
        ethernet_segment: EthernetSegment | None = Field(default=None)
        port_channel: PortChannel | None = Field(default=None)
        raw_eos_cli: str | None = Field(default=None)
        structured_config: StructuredConfig | None = Field(default=None)

    class NetworkServicesKeysItem(BaseModel):
        name: str | None = Field(default=None)

    class NodeTypeKeysItem(BaseModel):
        class NetworkServices(BaseModel):
            l1: bool = Field(default=False)
            l2: bool = Field(default=False)
            l3: bool = Field(default=False)

        class IpAddressing(BaseModel):
            python_module: str | None = Field(default=None)
            python_class_name: str | None = Field(default=None)
            router_id: str | None = Field(default=None)
            router_id_ipv6: str | None = Field(default=None)
            mlag_ip_primary: str | None = Field(default=None)
            mlag_ip_secondary: str | None = Field(default=None)
            mlag_l3_ip_primary: str | None = Field(default=None)
            mlag_l3_ip_secondary: str | None = Field(default=None)
            mlag_ibgp_peering_ip_primary: str | None = Field(default=None)
            mlag_ibgp_peering_ip_secondary: str | None = Field(default=None)
            p2p_uplinks_ip: str | None = Field(default=None)
            p2p_uplinks_peer_ip: str | None = Field(default=None)
            vtep_ip_mlag: str | None = Field(default=None)
            vtep_ip: str | None = Field(default=None)

        class InterfaceDescriptions(BaseModel):
            python_module: str | None = Field(default=None)
            python_class_name: str | None = Field(default=None)
            underlay_ethernet_interfaces: str | None = Field(default=None)
            underlay_port_channel_interfaces: str | None = Field(default=None)
            mlag_ethernet_interfaces: str | None = Field(default=None)
            mlag_port_channel_interfaces: str | None = Field(default=None)
            connected_endpoints_ethernet_interfaces: str | None = Field(default=None)
            connected_endpoints_port_channel_interfaces: str | None = Field(default=None)
            overlay_loopback_interface: str | None = Field(default=None)
            vtep_loopback_interface: str | None = Field(default=None)

        key: str | None = Field(default=None)
        type: str | None = Field(default=None)
        connected_endpoints: bool = Field(default=False)
        default_evpn_role: str = Field(default="none")
        default_ptp_priority1: int = Field(default=127)
        default_underlay_routing_protocol: str = Field(default="ebgp")
        default_overlay_routing_protocol: str = Field(default="ebgp")
        default_mpls_overlay_role: str | None = Field(default=None)
        default_overlay_address_families: str | None = Field(default=None)
        default_evpn_encapsulation: str | None = Field(default=None)
        mlag_support: bool = Field(default=False)
        network_services: NetworkServices | None = Field(default=None)
        underlay_router: bool = Field(default=True)
        uplink_type: str = Field(default="p2p")
        vtep: bool = Field(default=False)
        mpls_lsr: bool = Field(default=False)
        ip_addressing: IpAddressing | None = Field(default=None)
        interface_descriptions: InterfaceDescriptions | None = Field(default=None)

    class OverlayRdType(BaseModel):
        admin_subfield: str = Field(default="overlay_loopback_ip")
        admin_subfield_offset: str | None = Field(default=None)
        vrf_admin_subfield: str | None = Field(default=None)
        vrf_admin_subfield_offset: str | None = Field(default=None)
        vlan_assigned_number_subfield: str = Field(default="mac_vrf_id")

    class OverlayRtType(BaseModel):
        admin_subfield: str = Field(default="vrf_id")
        vrf_admin_subfield: str = Field(default="vrf_id")
        vlan_assigned_number_subfield: str = Field(default="mac_vrf_id")

    class PlatformSettingsItem(BaseModel):
        class ReloadDelay(BaseModel):
            mlag: int | None = Field(default=None)
            non_mlag: int | None = Field(default=None)

        class FeatureSupport(BaseModel):
            queue_monitor_length_notify: bool = Field(default=True)
            interface_storm_control: bool = Field(default=True)
            poe: bool = Field(default=False)
            bgp_update_wait_install: bool = Field(default=True)
            bgp_update_wait_for_convergence: bool = Field(default=True)

        platforms: str | None = Field(default=None)
        trident_forwarding_table_partition: str | None = Field(default=None)
        reload_delay: ReloadDelay | None = Field(default=None)
        tcam_profile: str | None = Field(default=None)
        lag_hardware_only: bool | None = Field(default=None)
        feature_support: FeatureSupport | None = Field(default=None)
        management_interface: str = Field(default="Management1")
        raw_eos_cli: str | None = Field(default=None)

    class PlatformSpeedGroupsItem(BaseModel):
        class SpeedsItem(BaseModel):
            speed: str | None = Field(default=None)
            speed_groups: int | None = Field(default=None)

        platform: str | None = Field(default=None)
        speeds: SpeedsItem | None = Field(default=None)

    class PortProfilesItem(BaseModel):
        class Flowcontrol(BaseModel):
            received: str | None = Field(default=None)

        class Ptp(BaseModel):
            enabled: bool = Field(default=False)
            endpoint_role: str = Field(default="follower")
            profile: str = Field(default="aes67-r16-2016")

        class LinkTracking(BaseModel):
            enabled: bool | None = Field(default=None)
            name: str | None = Field(default=None)

        class Dot1x(BaseModel):
            class Pae(BaseModel):
                mode: str | None = Field(default=None)

            class AuthenticationFailure(BaseModel):
                action: str | None = Field(default=None)
                allow_vlan: int | None = Field(default=None)

            class HostMode(BaseModel):
                mode: str | None = Field(default=None)
                multi_host_authenticated: bool | None = Field(default=None)

            class MacBasedAuthentication(BaseModel):
                enabled: bool | None = Field(default=None)
                always: bool | None = Field(default=None)
                host_mode_common: bool | None = Field(default=None)

            class Timeout(BaseModel):
                idle_host: int | None = Field(default=None)
                quiet_period: int | None = Field(default=None)
                reauth_period: str | None = Field(default=None)
                reauth_timeout_ignore: bool | None = Field(default=None)
                tx_period: int | None = Field(default=None)

            port_control: str | None = Field(default=None)
            port_control_force_authorized_phone: bool | None = Field(default=None)
            reauthentication: bool | None = Field(default=None)
            pae: Pae | None = Field(default=None)
            authentication_failure: AuthenticationFailure | None = Field(default=None)
            host_mode: HostMode | None = Field(default=None)
            mac_based_authentication: MacBasedAuthentication | None = Field(default=None)
            timeout: Timeout | None = Field(default=None)
            reauthorization_request_limit: int | None = Field(default=None)

        class Poe(BaseModel):
            class Reboot(BaseModel):
                action: str | None = Field(default=None)

            class LinkDown(BaseModel):
                action: str | None = Field(default=None)
                power_off_delay: int | None = Field(default=None)

            class Shutdown(BaseModel):
                action: str | None = Field(default=None)

            class Limit(BaseModel):
                class_key: int | None = Field(default=None, alias="class")
                watts: str | None = Field(default=None)
                fixed: bool | None = Field(default=None)

            disabled: bool = Field(default=False)
            priority: str | None = Field(default=None)
            reboot: Reboot | None = Field(default=None)
            link_down: LinkDown | None = Field(default=None)
            shutdown: Shutdown | None = Field(default=None)
            limit: Limit | None = Field(default=None)
            negotiation_lldp: bool | None = Field(default=None)
            legacy_detect: bool | None = Field(default=None)

        class StormControl(BaseModel):
            class All(BaseModel):
                level: str | None = Field(default=None)
                unit: str = Field(default="percent")

            class Broadcast(BaseModel):
                level: str | None = Field(default=None)
                unit: str = Field(default="percent")

            class Multicast(BaseModel):
                level: str | None = Field(default=None)
                unit: str = Field(default="percent")

            class UnknownUnicast(BaseModel):
                level: str | None = Field(default=None)
                unit: str = Field(default="percent")

            all: All | None = Field(default=None)
            broadcast: Broadcast | None = Field(default=None)
            multicast: Multicast | None = Field(default=None)
            unknown_unicast: UnknownUnicast | None = Field(default=None)

        class MonitorSessionsItem(BaseModel):
            class SourceSettings(BaseModel):
                class AccessGroup(BaseModel):
                    type: str | None = Field(default=None)
                    name: str | None = Field(default=None)
                    priority: int | None = Field(default=None)

                direction: str | None = Field(default=None)
                access_group: AccessGroup | None = Field(default=None)

            class SessionSettings(BaseModel):
                class AccessGroup(BaseModel):
                    type: str | None = Field(default=None)
                    name: str | None = Field(default=None)

                class Truncate(BaseModel):
                    enabled: bool | None = Field(default=None)
                    size: int | None = Field(default=None)

                encapsulation_gre_metadata_tx: bool | None = Field(default=None)
                header_remove_size: int | None = Field(default=None)
                access_group: AccessGroup | None = Field(default=None)
                rate_limit_per_ingress_chip: str | None = Field(default=None)
                rate_limit_per_egress_chip: str | None = Field(default=None)
                sample: int | None = Field(default=None)
                truncate: Truncate | None = Field(default=None)

            name: str = Field(default=None)
            role: str | None = Field(default=None)
            source_settings: SourceSettings | None = Field(default=None)
            session_settings: SessionSettings | None = Field(default=None)

        class EthernetSegment(BaseModel):
            short_esi: str = Field(default=None)
            redundancy: str | None = Field(default=None)
            designated_forwarder_algorithm: str | None = Field(default=None)
            designated_forwarder_preferences: str | None = Field(default=None)
            dont_preempt: bool | None = Field(default=None)

        class PortChannel(BaseModel):
            class LacpFallback(BaseModel):
                mode: str | None = Field(default=None)
                timeout: int | None = Field(default=None)

            class LacpTimer(BaseModel):
                mode: str | None = Field(default=None)
                multiplier: int | None = Field(default=None)

            class SubinterfacesItem(BaseModel):
                class EncapsulationVlan(BaseModel):
                    client_dot1q: int | None = Field(default=None)

                number: int | None = Field(default=None)
                short_esi: str | None = Field(default=None)
                vlan_id: int | None = Field(default=None)
                encapsulation_vlan: EncapsulationVlan | None = Field(default=None)

            class StructuredConfig(BaseModel):
                class Logging(BaseModel):
                    class Event(BaseModel):
                        link_status: bool | None = Field(default=None)

                    event: Event | None = Field(default=None)

                class EncapsulationVlan(BaseModel):
                    class Client(BaseModel):
                        class Dot1q(BaseModel):
                            vlan: int | None = Field(default=None)
                            outer: int | None = Field(default=None)
                            inner: int | None = Field(default=None)

                        dot1q: Dot1q | None = Field(default=None)
                        unmatched: bool | None = Field(default=None)

                    class Network(BaseModel):
                        class Dot1q(BaseModel):
                            vlan: int | None = Field(default=None)
                            outer: int | None = Field(default=None)
                            inner: int | None = Field(default=None)

                        dot1q: Dot1q | None = Field(default=None)
                        client: bool | None = Field(default=None)

                    client: Client | None = Field(default=None)
                    network: Network | None = Field(default=None)

                class LinkTrackingGroupsItem(BaseModel):
                    name: str | None = Field(default=None)
                    direction: str | None = Field(default=None)

                class Phone(BaseModel):
                    trunk: str | None = Field(default=None)
                    vlan: int | None = Field(default=None)

                class L2Protocol(BaseModel):
                    encapsulation_dot1q_vlan: int | None = Field(default=None)
                    forwarding_profile: str | None = Field(default=None)

                class Qos(BaseModel):
                    trust: str | None = Field(default=None)
                    dscp: int | None = Field(default=None)
                    cos: int | None = Field(default=None)

                class Bfd(BaseModel):
                    echo: bool | None = Field(default=None)
                    interval: int | None = Field(default=None)
                    min_rx: int | None = Field(default=None)
                    multiplier: int | None = Field(default=None)

                class ServicePolicy(BaseModel):
                    class Pbr(BaseModel):
                        input: str | None = Field(default=None)

                    class Qos(BaseModel):
                        input: str = Field(default=None)

                    pbr: Pbr | None = Field(default=None)
                    qos: Qos | None = Field(default=None)

                class Mpls(BaseModel):
                    class Ldp(BaseModel):
                        interface: bool | None = Field(default=None)
                        igp_sync: bool | None = Field(default=None)

                    ip: bool | None = Field(default=None)
                    ldp: Ldp | None = Field(default=None)

                class VlanTranslationsItem(BaseModel):
                    from_key: str | None = Field(default=None, alias="from")
                    to: int | None = Field(default=None)
                    direction: str = Field(default="both")

                class Shape(BaseModel):
                    rate: str | None = Field(default=None)

                class StormControl(BaseModel):
                    class All(BaseModel):
                        level: str | None = Field(default=None)
                        unit: str = Field(default="percent")

                    class Broadcast(BaseModel):
                        level: str | None = Field(default=None)
                        unit: str = Field(default="percent")

                    class Multicast(BaseModel):
                        level: str | None = Field(default=None)
                        unit: str = Field(default="percent")

                    class UnknownUnicast(BaseModel):
                        level: str | None = Field(default=None)
                        unit: str = Field(default="percent")

                    all: All | None = Field(default=None)
                    broadcast: Broadcast | None = Field(default=None)
                    multicast: Multicast | None = Field(default=None)
                    unknown_unicast: UnknownUnicast | None = Field(default=None)

                class TrafficPolicy(BaseModel):
                    input: str | None = Field(default=None)
                    output: str | None = Field(default=None)

                class EvpnEthernetSegment(BaseModel):
                    class DesignatedForwarderElection(BaseModel):
                        algorithm: str | None = Field(default=None)
                        preference_value: int | None = Field(default=None)
                        dont_preempt: bool = Field(default=False)
                        hold_time: int | None = Field(default=None)
                        subsequent_hold_time: int | None = Field(default=None)
                        candidate_reachability_required: bool | None = Field(default=None)

                    class Mpls(BaseModel):
                        shared_index: int | None = Field(default=None)
                        tunnel_flood_filter_time: int | None = Field(default=None)

                    identifier: str | None = Field(default=None)
                    redundancy: str | None = Field(default=None)
                    designated_forwarder_election: DesignatedForwarderElection | None = Field(default=None)
                    mpls: Mpls | None = Field(default=None)
                    route_target: str | None = Field(default=None)

                class Ptp(BaseModel):
                    class Announce(BaseModel):
                        interval: int | None = Field(default=None)
                        timeout: int | None = Field(default=None)

                    class SyncMessage(BaseModel):
                        interval: int | None = Field(default=None)

                    enable: bool | None = Field(default=None)
                    announce: Announce | None = Field(default=None)
                    delay_req: int | None = Field(default=None)
                    delay_mechanism: str | None = Field(default=None)
                    sync_message: SyncMessage | None = Field(default=None)
                    role: str | None = Field(default=None)
                    vlan: str | None = Field(default=None)
                    transport: str | None = Field(default=None)

                class IpNat(BaseModel):
                    class Destination(BaseModel):
                        class DynamicItem(BaseModel):
                            access_list: str | None = Field(default=None)
                            comment: str | None = Field(default=None)
                            pool_name: str = Field(default=None)
                            priority: int | None = Field(default=None)

                        class StaticItem(BaseModel):
                            access_list: str | None = Field(default=None)
                            comment: str | None = Field(default=None)
                            direction: str | None = Field(default=None)
                            group: int | None = Field(default=None)
                            original_ip: str | None = Field(default=None)
                            original_port: int | None = Field(default=None)
                            priority: int | None = Field(default=None)
                            protocol: str | None = Field(default=None)
                            translated_ip: str = Field(default=None)
                            translated_port: int | None = Field(default=None)

                        dynamic: DynamicItem | None = Field(default=None)
                        static: StaticItem | None = Field(default=None)

                    class Source(BaseModel):
                        class DynamicItem(BaseModel):
                            access_list: str | None = Field(default=None)
                            comment: str | None = Field(default=None)
                            nat_type: str = Field(default=None)
                            pool_name: str | None = Field(default=None)
                            priority: int | None = Field(default=None)

                        class StaticItem(BaseModel):
                            access_list: str | None = Field(default=None)
                            comment: str | None = Field(default=None)
                            direction: str | None = Field(default=None)
                            group: int | None = Field(default=None)
                            original_ip: str | None = Field(default=None)
                            original_port: int | None = Field(default=None)
                            priority: int | None = Field(default=None)
                            protocol: str | None = Field(default=None)
                            translated_ip: str = Field(default=None)
                            translated_port: int | None = Field(default=None)

                        dynamic: DynamicItem | None = Field(default=None)
                        static: StaticItem | None = Field(default=None)

                    destination: Destination | None = Field(default=None)
                    source: Source | None = Field(default=None)

                class Ipv6NdPrefixesItem(BaseModel):
                    ipv6_prefix: str | None = Field(default=None)
                    valid_lifetime: str | None = Field(default=None)
                    preferred_lifetime: str | None = Field(default=None)
                    no_autoconfig_flag: bool | None = Field(default=None)

                class Pim(BaseModel):
                    class Ipv4(BaseModel):
                        dr_priority: int | None = Field(default=None)
                        sparse_mode: bool | None = Field(default=None)

                    ipv4: Ipv4 | None = Field(default=None)

                class OspfMessageDigestKeysItem(BaseModel):
                    id: int | None = Field(default=None)
                    hash_algorithm: str | None = Field(default=None)
                    key: str | None = Field(default=None)

                class FlowTracker(BaseModel):
                    sampled: str | None = Field(default=None)

                class Bgp(BaseModel):
                    session_tracker: str | None = Field(default=None)

                class Sflow(BaseModel):
                    class Egress(BaseModel):
                        enable: bool | None = Field(default=None)
                        unmodified_enable: bool | None = Field(default=None)

                    enable: bool | None = Field(default=None)
                    egress: Egress | None = Field(default=None)

                name: str | None = Field(default=None)
                description: str | None = Field(default=None)
                logging: Logging | None = Field(default=None)
                shutdown: bool | None = Field(default=None)
                l2_mtu: int | None = Field(default=None)
                vlans: str | None = Field(default=None)
                snmp_trap_link_change: bool | None = Field(default=None)
                type: str | None = Field(default=None)
                encapsulation_dot1q_vlan: int | None = Field(default=None)
                vrf: str | None = Field(default=None)
                encapsulation_vlan: EncapsulationVlan | None = Field(default=None)
                vlan_id: int | None = Field(default=None)
                mode: str | None = Field(default=None)
                native_vlan: int | None = Field(default=None)
                native_vlan_tag: bool = Field(default=False)
                link_tracking_groups: LinkTrackingGroupsItem | None = Field(default=None)
                phone: Phone | None = Field(default=None)
                l2_protocol: L2Protocol | None = Field(default=None)
                mtu: int | None = Field(default=None)
                mlag: int | None = Field(default=None)
                trunk_groups: str | None = Field(default=None)
                lacp_fallback_timeout: int = Field(default=90)
                lacp_fallback_mode: str | None = Field(default=None)
                qos: Qos | None = Field(default=None)
                bfd: Bfd | None = Field(default=None)
                service_policy: ServicePolicy | None = Field(default=None)
                mpls: Mpls | None = Field(default=None)
                trunk_private_vlan_secondary: bool | None = Field(default=None)
                pvlan_mapping: str | None = Field(default=None)
                vlan_translations: VlanTranslationsItem | None = Field(default=None)
                shape: Shape | None = Field(default=None)
                storm_control: StormControl | None = Field(default=None)
                ip_proxy_arp: bool | None = Field(default=None)
                isis_enable: str | None = Field(default=None)
                isis_passive: bool | None = Field(default=None)
                isis_metric: int | None = Field(default=None)
                isis_network_point_to_point: bool | None = Field(default=None)
                isis_circuit_type: str | None = Field(default=None)
                isis_hello_padding: bool | None = Field(default=None)
                isis_authentication_mode: str | None = Field(default=None)
                isis_authentication_key: str | None = Field(default=None)
                traffic_policy: TrafficPolicy | None = Field(default=None)
                evpn_ethernet_segment: EvpnEthernetSegment | None = Field(default=None)
                esi: str | None = Field(default=None)
                rt: str | None = Field(default=None)
                lacp_id: str | None = Field(default=None)
                spanning_tree_bpdufilter: str | None = Field(default=None)
                spanning_tree_bpduguard: str | None = Field(default=None)
                spanning_tree_guard: str | None = Field(default=None)
                spanning_tree_portfast: str | None = Field(default=None)
                vmtracer: bool | None = Field(default=None)
                ptp: Ptp | None = Field(default=None)
                ip_address: str | None = Field(default=None)
                ip_nat: IpNat | None = Field(default=None)
                ipv6_enable: bool | None = Field(default=None)
                ipv6_address: str | None = Field(default=None)
                ipv6_address_link_local: str | None = Field(default=None)
                ipv6_nd_ra_disabled: bool | None = Field(default=None)
                ipv6_nd_managed_config_flag: bool | None = Field(default=None)
                ipv6_nd_prefixes: Ipv6NdPrefixesItem | None = Field(default=None)
                access_group_in: str | None = Field(default=None)
                access_group_out: str | None = Field(default=None)
                ipv6_access_group_in: str | None = Field(default=None)
                ipv6_access_group_out: str | None = Field(default=None)
                mac_access_group_in: str | None = Field(default=None)
                mac_access_group_out: str | None = Field(default=None)
                pim: Pim | None = Field(default=None)
                service_profile: str | None = Field(default=None)
                ospf_network_point_to_point: bool | None = Field(default=None)
                ospf_area: str | None = Field(default=None)
                ospf_cost: int | None = Field(default=None)
                ospf_authentication: str | None = Field(default=None)
                ospf_authentication_key: str | None = Field(default=None)
                ospf_message_digest_keys: OspfMessageDigestKeysItem | None = Field(default=None)
                flow_tracker: FlowTracker | None = Field(default=None)
                bgp: Bgp | None = Field(default=None)
                peer: str | None = Field(default=None)
                peer_interface: str | None = Field(default=None)
                peer_type: str | None = Field(default=None)
                sflow: Sflow | None = Field(default=None)
                eos_cli: str | None = Field(default=None)

            mode: str | None = Field(default=None)
            channel_id: int | None = Field(default=None)
            description: str | None = Field(default=None)
            enabled: bool = Field(default=True)
            short_esi: str | None = Field(default=None)
            lacp_fallback: LacpFallback | None = Field(default=None)
            lacp_timer: LacpTimer | None = Field(default=None)
            subinterfaces: SubinterfacesItem | None = Field(default=None)
            raw_eos_cli: str | None = Field(default=None)
            structured_config: StructuredConfig | None = Field(default=None)

        class StructuredConfig(BaseModel):
            class Phone(BaseModel):
                trunk: str | None = Field(default=None)
                vlan: int | None = Field(default=None)

            class L2Protocol(BaseModel):
                encapsulation_dot1q_vlan: int | None = Field(default=None)
                forwarding_profile: str | None = Field(default=None)

            class AddressLocking(BaseModel):
                ipv4: bool | None = Field(default=None)
                ipv6: bool | None = Field(default=None)

            class Flowcontrol(BaseModel):
                received: str | None = Field(default=None)

            class FlowTracker(BaseModel):
                sampled: str | None = Field(default=None)

            class ErrorCorrectionEncoding(BaseModel):
                enabled: bool = Field(default=True)
                fire_code: bool | None = Field(default=None)
                reed_solomon: bool | None = Field(default=None)

            class LinkTrackingGroupsItem(BaseModel):
                name: str | None = Field(default=None)
                direction: str | None = Field(default=None)

            class EvpnEthernetSegment(BaseModel):
                class DesignatedForwarderElection(BaseModel):
                    algorithm: str | None = Field(default=None)
                    preference_value: int | None = Field(default=None)
                    dont_preempt: bool | None = Field(default=None)
                    hold_time: int | None = Field(default=None)
                    subsequent_hold_time: int | None = Field(default=None)
                    candidate_reachability_required: bool | None = Field(default=None)

                class Mpls(BaseModel):
                    shared_index: int | None = Field(default=None)
                    tunnel_flood_filter_time: int | None = Field(default=None)

                identifier: str | None = Field(default=None)
                redundancy: str | None = Field(default=None)
                designated_forwarder_election: DesignatedForwarderElection | None = Field(default=None)
                mpls: Mpls | None = Field(default=None)
                route_target: str | None = Field(default=None)

            class EncapsulationVlan(BaseModel):
                class Client(BaseModel):
                    class Dot1q(BaseModel):
                        vlan: int | None = Field(default=None)
                        outer: int | None = Field(default=None)
                        inner: int | None = Field(default=None)

                    dot1q: Dot1q | None = Field(default=None)
                    unmatched: bool | None = Field(default=None)

                class Network(BaseModel):
                    class Dot1q(BaseModel):
                        vlan: int | None = Field(default=None)
                        outer: int | None = Field(default=None)
                        inner: int | None = Field(default=None)

                    dot1q: Dot1q | None = Field(default=None)
                    client: bool | None = Field(default=None)

                client: Client | None = Field(default=None)
                network: Network | None = Field(default=None)

            class IpHelpersItem(BaseModel):
                ip_helper: str | None = Field(default=None)
                source_interface: str | None = Field(default=None)
                vrf: str | None = Field(default=None)

            class IpNat(BaseModel):
                class Destination(BaseModel):
                    class DynamicItem(BaseModel):
                        access_list: str | None = Field(default=None)
                        comment: str | None = Field(default=None)
                        pool_name: str = Field(default=None)
                        priority: int | None = Field(default=None)

                    class StaticItem(BaseModel):
                        access_list: str | None = Field(default=None)
                        comment: str | None = Field(default=None)
                        direction: str | None = Field(default=None)
                        group: int | None = Field(default=None)
                        original_ip: str | None = Field(default=None)
                        original_port: int | None = Field(default=None)
                        priority: int | None = Field(default=None)
                        protocol: str | None = Field(default=None)
                        translated_ip: str = Field(default=None)
                        translated_port: int | None = Field(default=None)

                    dynamic: DynamicItem | None = Field(default=None)
                    static: StaticItem | None = Field(default=None)

                class Source(BaseModel):
                    class DynamicItem(BaseModel):
                        access_list: str | None = Field(default=None)
                        comment: str | None = Field(default=None)
                        nat_type: str = Field(default=None)
                        pool_name: str | None = Field(default=None)
                        priority: int | None = Field(default=None)

                    class StaticItem(BaseModel):
                        access_list: str | None = Field(default=None)
                        comment: str | None = Field(default=None)
                        direction: str | None = Field(default=None)
                        group: int | None = Field(default=None)
                        original_ip: str | None = Field(default=None)
                        original_port: int | None = Field(default=None)
                        priority: int | None = Field(default=None)
                        protocol: str | None = Field(default=None)
                        translated_ip: str = Field(default=None)
                        translated_port: int | None = Field(default=None)

                    dynamic: DynamicItem | None = Field(default=None)
                    static: StaticItem | None = Field(default=None)

                destination: Destination | None = Field(default=None)
                source: Source | None = Field(default=None)

            class Ipv6NdPrefixesItem(BaseModel):
                ipv6_prefix: str | None = Field(default=None)
                valid_lifetime: str | None = Field(default=None)
                preferred_lifetime: str | None = Field(default=None)
                no_autoconfig_flag: bool | None = Field(default=None)

            class Ipv6DhcpRelayDestinationsItem(BaseModel):
                address: str | None = Field(default=None)
                vrf: str | None = Field(default=None)
                local_interface: str | None = Field(default=None)
                source_address: str | None = Field(default=None)
                link_address: str | None = Field(default=None)

            class Multicast(BaseModel):
                class Ipv4(BaseModel):
                    class BoundariesItem(BaseModel):
                        boundary: str | None = Field(default=None)
                        out: bool | None = Field(default=None)

                    boundaries: BoundariesItem | None = Field(default=None)
                    static: bool | None = Field(default=None)

                class Ipv6(BaseModel):
                    class BoundariesItem(BaseModel):
                        boundary: str | None = Field(default=None)

                    boundaries: BoundariesItem | None = Field(default=None)
                    static: bool | None = Field(default=None)

                ipv4: Ipv4 | None = Field(default=None)
                ipv6: Ipv6 | None = Field(default=None)

            class OspfMessageDigestKeysItem(BaseModel):
                id: int | None = Field(default=None)
                hash_algorithm: str | None = Field(default=None)
                key: str | None = Field(default=None)

            class Pim(BaseModel):
                class Ipv4(BaseModel):
                    dr_priority: int | None = Field(default=None)
                    sparse_mode: bool | None = Field(default=None)

                ipv4: Ipv4 | None = Field(default=None)

            class MacSecurity(BaseModel):
                profile: str | None = Field(default=None)

            class ChannelGroup(BaseModel):
                id: int | None = Field(default=None)
                mode: str | None = Field(default=None)

            class Poe(BaseModel):
                class Reboot(BaseModel):
                    action: str | None = Field(default=None)

                class LinkDown(BaseModel):
                    action: str | None = Field(default=None)
                    power_off_delay: int | None = Field(default=None)

                class Shutdown(BaseModel):
                    action: str | None = Field(default=None)

                class Limit(BaseModel):
                    class_key: int | None = Field(default=None, alias="class")
                    watts: str | None = Field(default=None)
                    fixed: bool | None = Field(default=None)

                disabled: bool = Field(default=False)
                priority: str | None = Field(default=None)
                reboot: Reboot | None = Field(default=None)
                link_down: LinkDown | None = Field(default=None)
                shutdown: Shutdown | None = Field(default=None)
                limit: Limit | None = Field(default=None)
                negotiation_lldp: bool | None = Field(default=None)
                legacy_detect: bool | None = Field(default=None)

            class Ptp(BaseModel):
                class Announce(BaseModel):
                    interval: int | None = Field(default=None)
                    timeout: int | None = Field(default=None)

                class SyncMessage(BaseModel):
                    interval: int | None = Field(default=None)

                enable: bool | None = Field(default=None)
                announce: Announce | None = Field(default=None)
                delay_req: int | None = Field(default=None)
                delay_mechanism: str | None = Field(default=None)
                sync_message: SyncMessage | None = Field(default=None)
                role: str | None = Field(default=None)
                vlan: str | None = Field(default=None)
                transport: str | None = Field(default=None)

            class StormControl(BaseModel):
                class All(BaseModel):
                    level: str | None = Field(default=None)
                    unit: str = Field(default="percent")

                class Broadcast(BaseModel):
                    level: str | None = Field(default=None)
                    unit: str = Field(default="percent")

                class Multicast(BaseModel):
                    level: str | None = Field(default=None)
                    unit: str = Field(default="percent")

                class UnknownUnicast(BaseModel):
                    level: str | None = Field(default=None)
                    unit: str = Field(default="percent")

                all: All | None = Field(default=None)
                broadcast: Broadcast | None = Field(default=None)
                multicast: Multicast | None = Field(default=None)
                unknown_unicast: UnknownUnicast | None = Field(default=None)

            class Logging(BaseModel):
                class Event(BaseModel):
                    link_status: bool | None = Field(default=None)
                    congestion_drops: bool | None = Field(default=None)
                    spanning_tree: bool | None = Field(default=None)
                    storm_control: bool | None = Field(default=None)

                event: Event | None = Field(default=None)

            class Lldp(BaseModel):
                transmit: bool | None = Field(default=None)
                receive: bool | None = Field(default=None)
                ztp_vlan: int | None = Field(default=None)

            class VlanTranslationsItem(BaseModel):
                from_key: str | None = Field(default=None, alias="from")
                to: int | None = Field(default=None)
                direction: str = Field(default="both")

            class Dot1x(BaseModel):
                class Pae(BaseModel):
                    mode: str | None = Field(default=None)

                class AuthenticationFailure(BaseModel):
                    action: str | None = Field(default=None)
                    allow_vlan: int | None = Field(default=None)

                class HostMode(BaseModel):
                    mode: str | None = Field(default=None)
                    multi_host_authenticated: bool | None = Field(default=None)

                class MacBasedAuthentication(BaseModel):
                    enabled: bool | None = Field(default=None)
                    always: bool | None = Field(default=None)
                    host_mode_common: bool | None = Field(default=None)

                class Timeout(BaseModel):
                    idle_host: int | None = Field(default=None)
                    quiet_period: int | None = Field(default=None)
                    reauth_period: str | None = Field(default=None)
                    reauth_timeout_ignore: bool | None = Field(default=None)
                    tx_period: int | None = Field(default=None)

                class Unauthorized(BaseModel):
                    access_vlan_membership_egress: bool | None = Field(default=None)
                    native_vlan_membership_egress: bool | None = Field(default=None)

                class Eapol(BaseModel):
                    class AuthenticationFailureFallbackMba(BaseModel):
                        enabled: bool | None = Field(default=None)
                        timeout: int | None = Field(default=None)

                    disabled: bool | None = Field(default=None)
                    authentication_failure_fallback_mba: AuthenticationFailureFallbackMba | None = Field(default=None)

                port_control: str | None = Field(default=None)
                port_control_force_authorized_phone: bool | None = Field(default=None)
                reauthentication: bool | None = Field(default=None)
                pae: Pae | None = Field(default=None)
                authentication_failure: AuthenticationFailure | None = Field(default=None)
                host_mode: HostMode | None = Field(default=None)
                mac_based_authentication: MacBasedAuthentication | None = Field(default=None)
                timeout: Timeout | None = Field(default=None)
                reauthorization_request_limit: int | None = Field(default=None)
                unauthorized: Unauthorized | None = Field(default=None)
                eapol: Eapol | None = Field(default=None)

            class Shape(BaseModel):
                rate: str | None = Field(default=None)

            class Qos(BaseModel):
                trust: str | None = Field(default=None)
                dscp: int | None = Field(default=None)
                cos: int | None = Field(default=None)

            class PriorityFlowControl(BaseModel):
                class PrioritiesItem(BaseModel):
                    priority: int | None = Field(default=None)
                    no_drop: bool | None = Field(default=None)

                enabled: bool | None = Field(default=None)
                priorities: PrioritiesItem | None = Field(default=None)

            class Bfd(BaseModel):
                echo: bool | None = Field(default=None)
                interval: int | None = Field(default=None)
                min_rx: int | None = Field(default=None)
                multiplier: int | None = Field(default=None)

            class ServicePolicy(BaseModel):
                class Pbr(BaseModel):
                    input: str | None = Field(default=None)

                class Qos(BaseModel):
                    input: str = Field(default=None)

                pbr: Pbr | None = Field(default=None)
                qos: Qos | None = Field(default=None)

            class Mpls(BaseModel):
                class Ldp(BaseModel):
                    interface: bool | None = Field(default=None)
                    igp_sync: bool | None = Field(default=None)

                ip: bool | None = Field(default=None)
                ldp: Ldp | None = Field(default=None)

            class LacpTimer(BaseModel):
                mode: str | None = Field(default=None)
                multiplier: int | None = Field(default=None)

            class Transceiver(BaseModel):
                class Media(BaseModel):
                    override: str | None = Field(default=None)

                media: Media | None = Field(default=None)

            class TrafficPolicy(BaseModel):
                input: str | None = Field(default=None)
                output: str | None = Field(default=None)

            class Bgp(BaseModel):
                session_tracker: str | None = Field(default=None)

            class Sflow(BaseModel):
                class Egress(BaseModel):
                    enable: bool | None = Field(default=None)
                    unmodified_enable: bool | None = Field(default=None)

                enable: bool | None = Field(default=None)
                egress: Egress | None = Field(default=None)

            name: str | None = Field(default=None)
            description: str | None = Field(default=None)
            shutdown: bool | None = Field(default=None)
            load_interval: int | None = Field(default=None)
            speed: str | None = Field(default=None)
            mtu: int | None = Field(default=None)
            l2_mtu: int | None = Field(default=None)
            vlans: str | None = Field(default=None)
            native_vlan: int | None = Field(default=None)
            native_vlan_tag: bool | None = Field(default=None)
            mode: str | None = Field(default=None)
            phone: Phone | None = Field(default=None)
            l2_protocol: L2Protocol | None = Field(default=None)
            trunk_groups: str | None = Field(default=None)
            type: str | None = Field(default=None)
            snmp_trap_link_change: bool | None = Field(default=None)
            address_locking: AddressLocking | None = Field(default=None)
            flowcontrol: Flowcontrol | None = Field(default=None)
            vrf: str | None = Field(default=None)
            flow_tracker: FlowTracker | None = Field(default=None)
            error_correction_encoding: ErrorCorrectionEncoding | None = Field(default=None)
            link_tracking_groups: LinkTrackingGroupsItem | None = Field(default=None)
            evpn_ethernet_segment: EvpnEthernetSegment | None = Field(default=None)
            encapsulation_dot1q_vlan: int | None = Field(default=None)
            encapsulation_vlan: EncapsulationVlan | None = Field(default=None)
            vlan_id: int | None = Field(default=None)
            ip_address: str | None = Field(default=None)
            ip_address_secondaries: str | None = Field(default=None)
            ip_helpers: IpHelpersItem | None = Field(default=None)
            ip_nat: IpNat | None = Field(default=None)
            ipv6_enable: bool | None = Field(default=None)
            ipv6_address: str | None = Field(default=None)
            ipv6_address_link_local: str | None = Field(default=None)
            ipv6_nd_ra_disabled: bool | None = Field(default=None)
            ipv6_nd_managed_config_flag: bool | None = Field(default=None)
            ipv6_nd_prefixes: Ipv6NdPrefixesItem | None = Field(default=None)
            ipv6_dhcp_relay_destinations: Ipv6DhcpRelayDestinationsItem | None = Field(default=None)
            access_group_in: str | None = Field(default=None)
            access_group_out: str | None = Field(default=None)
            ipv6_access_group_in: str | None = Field(default=None)
            ipv6_access_group_out: str | None = Field(default=None)
            mac_access_group_in: str | None = Field(default=None)
            mac_access_group_out: str | None = Field(default=None)
            multicast: Multicast | None = Field(default=None)
            ospf_network_point_to_point: bool | None = Field(default=None)
            ospf_area: str | None = Field(default=None)
            ospf_cost: int | None = Field(default=None)
            ospf_authentication: str | None = Field(default=None)
            ospf_authentication_key: str | None = Field(default=None)
            ospf_message_digest_keys: OspfMessageDigestKeysItem | None = Field(default=None)
            pim: Pim | None = Field(default=None)
            mac_security: MacSecurity | None = Field(default=None)
            channel_group: ChannelGroup | None = Field(default=None)
            isis_enable: str | None = Field(default=None)
            isis_passive: bool | None = Field(default=None)
            isis_metric: int | None = Field(default=None)
            isis_network_point_to_point: bool | None = Field(default=None)
            isis_circuit_type: str | None = Field(default=None)
            isis_hello_padding: bool | None = Field(default=None)
            isis_authentication_mode: str | None = Field(default=None)
            isis_authentication_key: str | None = Field(default=None)
            poe: Poe | None = Field(default=None)
            ptp: Ptp | None = Field(default=None)
            profile: str | None = Field(default=None)
            storm_control: StormControl | None = Field(default=None)
            logging: Logging | None = Field(default=None)
            lldp: Lldp | None = Field(default=None)
            trunk_private_vlan_secondary: bool | None = Field(default=None)
            pvlan_mapping: str | None = Field(default=None)
            vlan_translations: VlanTranslationsItem | None = Field(default=None)
            dot1x: Dot1x | None = Field(default=None)
            service_profile: str | None = Field(default=None)
            shape: Shape | None = Field(default=None)
            qos: Qos | None = Field(default=None)
            spanning_tree_bpdufilter: str | None = Field(default=None)
            spanning_tree_bpduguard: str | None = Field(default=None)
            spanning_tree_guard: str | None = Field(default=None)
            spanning_tree_portfast: str | None = Field(default=None)
            vmtracer: bool | None = Field(default=None)
            priority_flow_control: PriorityFlowControl | None = Field(default=None)
            bfd: Bfd | None = Field(default=None)
            service_policy: ServicePolicy | None = Field(default=None)
            mpls: Mpls | None = Field(default=None)
            lacp_timer: LacpTimer | None = Field(default=None)
            lacp_port_priority: int | None = Field(default=None)
            transceiver: Transceiver | None = Field(default=None)
            ip_proxy_arp: bool | None = Field(default=None)
            traffic_policy: TrafficPolicy | None = Field(default=None)
            bgp: Bgp | None = Field(default=None)
            peer: str | None = Field(default=None)
            peer_interface: str | None = Field(default=None)
            peer_type: str | None = Field(default=None)
            sflow: Sflow | None = Field(default=None)
            port_profile: str | None = Field(default=None)
            eos_cli: str | None = Field(default=None)

        profile: str | None = Field(default=None)
        parent_profile: str | None = Field(default=None)
        speed: str | None = Field(default=None)
        description: str | None = Field(default=None)
        enabled: bool = Field(default=True)
        mode: str | None = Field(default=None)
        mtu: int | None = Field(default=None)
        l2_mtu: int | None = Field(default=None)
        native_vlan: int | None = Field(default=None)
        native_vlan_tag: bool = Field(default=False)
        trunk_groups: str | None = Field(default=None)
        vlans: str | None = Field(default=None)
        spanning_tree_portfast: str | None = Field(default=None)
        spanning_tree_bpdufilter: str | None = Field(default=None)
        spanning_tree_bpduguard: str | None = Field(default=None)
        flowcontrol: Flowcontrol | None = Field(default=None)
        qos_profile: str | None = Field(default=None)
        ptp: Ptp | None = Field(default=None)
        sflow: bool | None = Field(default=None)
        link_tracking: LinkTracking | None = Field(default=None)
        dot1x: Dot1x | None = Field(default=None)
        poe: Poe | None = Field(default=None)
        storm_control: StormControl | None = Field(default=None)
        monitor_sessions: MonitorSessionsItem | None = Field(default=None)
        ethernet_segment: EthernetSegment | None = Field(default=None)
        port_channel: PortChannel | None = Field(default=None)
        raw_eos_cli: str | None = Field(default=None)
        structured_config: StructuredConfig | None = Field(default=None)

    class Ptp(BaseModel):
        enabled: bool | None = Field(default=None)
        profile: str = Field(default="aes67-r16-2016")
        domain: int | None = Field(default=None)
        auto_clock_identity: bool = Field(default=True)

    class PtpProfilesItem(BaseModel):
        class Announce(BaseModel):
            interval: int | None = Field(default=None)
            timeout: int | None = Field(default=None)

        class SyncMessage(BaseModel):
            interval: int | None = Field(default=None)

        profile: str | None = Field(default=None)
        announce: Announce | None = Field(default=None)
        delay_req: int | None = Field(default=None)
        sync_message: SyncMessage | None = Field(default=None)
        transport: str | None = Field(default=None)

    class QueueMonitorLength(BaseModel):
        class DefaultThresholds(BaseModel):
            high: int = Field(default=None)
            low: int | None = Field(default=None)

        class Cpu(BaseModel):
            class Thresholds(BaseModel):
                high: int = Field(default=None)
                low: int | None = Field(default=None)

            thresholds: Thresholds | None = Field(default=None)

        enabled: bool = Field(default=None)
        notifying: bool | None = Field(default=None)
        default_thresholds: DefaultThresholds | None = Field(default=None)
        log: int | None = Field(default=None)
        cpu: Cpu | None = Field(default=None)

    class Redundancy(BaseModel):
        protocol: str | None = Field(default=None)

    class SnmpSettings(BaseModel):
        class UsersItem(BaseModel):
            name: str | None = Field(default=None)
            group: str | None = Field(default=None)
            version: str | None = Field(default=None)
            auth: str | None = Field(default=None)
            auth_passphrase: str | None = Field(default=None)
            priv: str | None = Field(default=None)
            priv_passphrase: str | None = Field(default=None)

        contact: str | None = Field(default=None)
        location: bool = Field(default=False)
        compute_local_engineid: bool = Field(default=False)
        compute_local_engineid_source: str = Field(default="hostname_and_ip")
        compute_v3_user_localized_key: bool = Field(default=False)
        users: UsersItem | None = Field(default=None)

    class SviProfilesItem(BaseModel):
        class NodesItem(BaseModel):
            class IpHelpersItem(BaseModel):
                ip_helper: str | None = Field(default=None)
                source_interface: str | None = Field(default=None)
                source_vrf: str | None = Field(default=None)

            class EvpnL2Multicast(BaseModel):
                enabled: bool | None = Field(default=None)

            class EvpnL3Multicast(BaseModel):
                enabled: bool | None = Field(default=None)

            class IgmpSnoopingQuerier(BaseModel):
                enabled: bool | None = Field(default=None)
                source_address: str | None = Field(default=None)
                version: int | None = Field(default=None)

            class Ospf(BaseModel):
                class MessageDigestKeysItem(BaseModel):
                    id: int | None = Field(default=None)
                    hash_algorithm: str = Field(default="sha512")
                    key: str | None = Field(default=None)

                enabled: bool | None = Field(default=None)
                point_to_point: bool = Field(default=True)
                area: str = Field(default="0")
                cost: int | None = Field(default=None)
                authentication: str | None = Field(default=None)
                simple_auth_key: str | None = Field(default=None)
                message_digest_keys: MessageDigestKeysItem | None = Field(default=None)

            class Bgp(BaseModel):
                class StructuredConfig(BaseModel):
                    class RdEvpnDomain(BaseModel):
                        domain: str | None = Field(default=None)
                        rd: str | None = Field(default=None)

                    class RouteTargets(BaseModel):
                        class ImportEvpnDomainsItem(BaseModel):
                            domain: str | None = Field(default=None)
                            route_target: str | None = Field(default=None)

                        class ExportEvpnDomainsItem(BaseModel):
                            domain: str | None = Field(default=None)
                            route_target: str | None = Field(default=None)

                        class ImportExportEvpnDomainsItem(BaseModel):
                            domain: str | None = Field(default=None)
                            route_target: str | None = Field(default=None)

                        both: str | None = Field(default=None)
                        import_key: str | None = Field(default=None, alias="import")
                        export: str | None = Field(default=None)
                        import_evpn_domains: ImportEvpnDomainsItem | None = Field(default=None)
                        export_evpn_domains: ExportEvpnDomainsItem | None = Field(default=None)
                        import_export_evpn_domains: ImportExportEvpnDomainsItem | None = Field(default=None)

                    id: int | None = Field(default=None)
                    tenant: str | None = Field(default=None)
                    rd: str | None = Field(default=None)
                    rd_evpn_domain: RdEvpnDomain | None = Field(default=None)
                    eos_cli: str | None = Field(default=None)
                    route_targets: RouteTargets | None = Field(default=None)
                    redistribute_routes: str | None = Field(default=None)
                    no_redistribute_routes: str | None = Field(default=None)

                structured_config: StructuredConfig | None = Field(default=None)
                raw_eos_cli: str | None = Field(default=None)

            class StructuredConfig(BaseModel):
                class IpHelpersItem(BaseModel):
                    ip_helper: str | None = Field(default=None)
                    source_interface: str | None = Field(default=None)
                    vrf: str | None = Field(default=None)

                class IpNat(BaseModel):
                    class Destination(BaseModel):
                        class DynamicItem(BaseModel):
                            access_list: str | None = Field(default=None)
                            comment: str | None = Field(default=None)
                            pool_name: str = Field(default=None)
                            priority: int | None = Field(default=None)

                        class StaticItem(BaseModel):
                            access_list: str | None = Field(default=None)
                            comment: str | None = Field(default=None)
                            direction: str | None = Field(default=None)
                            group: int | None = Field(default=None)
                            original_ip: str | None = Field(default=None)
                            original_port: int | None = Field(default=None)
                            priority: int | None = Field(default=None)
                            protocol: str | None = Field(default=None)
                            translated_ip: str = Field(default=None)
                            translated_port: int | None = Field(default=None)

                        dynamic: DynamicItem | None = Field(default=None)
                        static: StaticItem | None = Field(default=None)

                    class Source(BaseModel):
                        class DynamicItem(BaseModel):
                            access_list: str | None = Field(default=None)
                            comment: str | None = Field(default=None)
                            nat_type: str = Field(default=None)
                            pool_name: str | None = Field(default=None)
                            priority: int | None = Field(default=None)

                        class StaticItem(BaseModel):
                            access_list: str | None = Field(default=None)
                            comment: str | None = Field(default=None)
                            direction: str | None = Field(default=None)
                            group: int | None = Field(default=None)
                            original_ip: str | None = Field(default=None)
                            original_port: int | None = Field(default=None)
                            priority: int | None = Field(default=None)
                            protocol: str | None = Field(default=None)
                            translated_ip: str = Field(default=None)
                            translated_port: int | None = Field(default=None)

                        dynamic: DynamicItem | None = Field(default=None)
                        static: StaticItem | None = Field(default=None)

                    destination: Destination | None = Field(default=None)
                    source: Source | None = Field(default=None)

                class Ipv6NdPrefixesItem(BaseModel):
                    ipv6_prefix: str | None = Field(default=None)
                    valid_lifetime: str | None = Field(default=None)
                    preferred_lifetime: str | None = Field(default=None)
                    no_autoconfig_flag: bool | None = Field(default=None)

                class Ipv6DhcpRelayDestinationsItem(BaseModel):
                    address: str | None = Field(default=None)
                    vrf: str | None = Field(default=None)
                    local_interface: str | None = Field(default=None)
                    source_address: str | None = Field(default=None)
                    link_address: str | None = Field(default=None)

                class Multicast(BaseModel):
                    class Ipv4(BaseModel):
                        class BoundariesItem(BaseModel):
                            boundary: str | None = Field(default=None)
                            out: bool | None = Field(default=None)

                        class SourceRouteExport(BaseModel):
                            enabled: bool = Field(default=None)
                            administrative_distance: int | None = Field(default=None)

                        boundaries: BoundariesItem | None = Field(default=None)
                        source_route_export: SourceRouteExport | None = Field(default=None)
                        static: bool | None = Field(default=None)

                    class Ipv6(BaseModel):
                        class BoundariesItem(BaseModel):
                            boundary: str | None = Field(default=None)

                        class SourceRouteExport(BaseModel):
                            enabled: bool = Field(default=None)
                            administrative_distance: int | None = Field(default=None)

                        boundaries: BoundariesItem | None = Field(default=None)
                        source_route_export: SourceRouteExport | None = Field(default=None)
                        static: bool | None = Field(default=None)

                    ipv4: Ipv4 | None = Field(default=None)
                    ipv6: Ipv6 | None = Field(default=None)

                class OspfMessageDigestKeysItem(BaseModel):
                    id: int | None = Field(default=None)
                    hash_algorithm: str | None = Field(default=None)
                    key: str | None = Field(default=None)

                class Pim(BaseModel):
                    class Ipv4(BaseModel):
                        dr_priority: int | None = Field(default=None)
                        sparse_mode: bool | None = Field(default=None)
                        local_interface: str | None = Field(default=None)

                    ipv4: Ipv4 | None = Field(default=None)

                class VrrpIdsItem(BaseModel):
                    class Advertisement(BaseModel):
                        interval: int | None = Field(default=None)

                    class Preempt(BaseModel):
                        class Delay(BaseModel):
                            minimum: int | None = Field(default=None)
                            reload: int | None = Field(default=None)

                        enabled: bool = Field(default=None)
                        delay: Delay | None = Field(default=None)

                    class Timers(BaseModel):
                        class Delay(BaseModel):
                            reload: int | None = Field(default=None)

                        delay: Delay | None = Field(default=None)

                    class TrackedObjectItem(BaseModel):
                        name: str | None = Field(default=None)
                        decrement: int | None = Field(default=None)
                        shutdown: bool | None = Field(default=None)

                    class Ipv4(BaseModel):
                        address: str = Field(default=None)
                        version: int | None = Field(default=None)

                    class Ipv6(BaseModel):
                        address: str = Field(default=None)

                    id: int | None = Field(default=None)
                    priority_level: int | None = Field(default=None)
                    advertisement: Advertisement | None = Field(default=None)
                    preempt: Preempt | None = Field(default=None)
                    timers: Timers | None = Field(default=None)
                    tracked_object: TrackedObjectItem | None = Field(default=None)
                    ipv4: Ipv4 | None = Field(default=None)
                    ipv6: Ipv6 | None = Field(default=None)

                class Vrrp(BaseModel):
                    virtual_router: str | None = Field(default=None)
                    priority: int | None = Field(default=None)
                    advertisement_interval: int | None = Field(default=None)
                    preempt_delay_minimum: int | None = Field(default=None)
                    ipv4: str | None = Field(default=None)
                    ipv6: str | None = Field(default=None)

                class IpAttachedHostRouteExport(BaseModel):
                    enabled: bool = Field(default=None)
                    distance: int | None = Field(default=None)

                class Bfd(BaseModel):
                    echo: bool | None = Field(default=None)
                    interval: int | None = Field(default=None)
                    min_rx: int | None = Field(default=None)
                    multiplier: int | None = Field(default=None)

                class ServicePolicy(BaseModel):
                    class Pbr(BaseModel):
                        input: str | None = Field(default=None)

                    pbr: Pbr | None = Field(default=None)

                name: str | None = Field(default=None)
                description: str | None = Field(default=None)
                shutdown: bool | None = Field(default=None)
                vrf: str | None = Field(default=None)
                arp_aging_timeout: int | None = Field(default=None)
                arp_cache_dynamic_capacity: int | None = Field(default=None)
                arp_gratuitous_accept: bool | None = Field(default=None)
                arp_monitor_mac_address: bool | None = Field(default=None)
                ip_proxy_arp: bool | None = Field(default=None)
                ip_directed_broadcast: bool | None = Field(default=None)
                ip_address: str | None = Field(default=None)
                ip_address_secondaries: str | None = Field(default=None)
                ip_virtual_router_addresses: str | None = Field(default=None)
                ip_address_virtual: str | None = Field(default=None)
                ip_address_virtual_secondaries: str | None = Field(default=None)
                ip_igmp: bool | None = Field(default=None)
                ip_igmp_version: int | None = Field(default=None)
                ip_helpers: IpHelpersItem | None = Field(default=None)
                ip_nat: IpNat | None = Field(default=None)
                ipv6_enable: bool | None = Field(default=None)
                ipv6_address: str | None = Field(default=None)
                ipv6_address_virtual: str | None = Field(default=None)
                ipv6_address_virtuals: str | None = Field(default=None)
                ipv6_address_link_local: str | None = Field(default=None)
                ipv6_virtual_router_address: str | None = Field(default=None)
                ipv6_virtual_router_addresses: str | None = Field(default=None)
                ipv6_nd_ra_disabled: bool | None = Field(default=None)
                ipv6_nd_managed_config_flag: bool | None = Field(default=None)
                ipv6_nd_prefixes: Ipv6NdPrefixesItem | None = Field(default=None)
                ipv6_dhcp_relay_destinations: Ipv6DhcpRelayDestinationsItem | None = Field(default=None)
                access_group_in: str | None = Field(default=None)
                access_group_out: str | None = Field(default=None)
                ipv6_access_group_in: str | None = Field(default=None)
                ipv6_access_group_out: str | None = Field(default=None)
                multicast: Multicast | None = Field(default=None)
                ospf_network_point_to_point: bool | None = Field(default=None)
                ospf_area: str | None = Field(default=None)
                ospf_cost: int | None = Field(default=None)
                ospf_authentication: str | None = Field(default=None)
                ospf_authentication_key: str | None = Field(default=None)
                ospf_message_digest_keys: OspfMessageDigestKeysItem | None = Field(default=None)
                pim: Pim | None = Field(default=None)
                isis_enable: str | None = Field(default=None)
                isis_passive: bool | None = Field(default=None)
                isis_metric: int | None = Field(default=None)
                isis_network_point_to_point: bool | None = Field(default=None)
                mtu: int | None = Field(default=None)
                no_autostate: bool | None = Field(default=None)
                vrrp_ids: VrrpIdsItem | None = Field(default=None)
                vrrp: Vrrp | None = Field(default=None)
                ip_attached_host_route_export: IpAttachedHostRouteExport | None = Field(default=None)
                bfd: Bfd | None = Field(default=None)
                service_policy: ServicePolicy | None = Field(default=None)
                pvlan_mapping: str | None = Field(default=None)
                tenant: str | None = Field(default=None)
                tags: str | None = Field(default=None)
                type: str | None = Field(default=None)
                eos_cli: str | None = Field(default=None)

            node: str | None = Field(default=None)
            name: str | None = Field(default=None)
            enabled: bool | None = Field(default=None)
            description: str | None = Field(default=None)
            ip_address: str | None = Field(default=None)
            ipv6_address: str | None = Field(default=None)
            ipv6_enable: bool | None = Field(default=None)
            ip_address_virtual: str | None = Field(default=None)
            ipv6_address_virtual: str | None = Field(default=None)
            ipv6_address_virtuals: str | None = Field(default=None)
            ip_address_virtual_secondaries: str | None = Field(default=None)
            ip_virtual_router_addresses: str | None = Field(default=None)
            ipv6_virtual_router_addresses: str | None = Field(default=None)
            ip_helpers: IpHelpersItem | None = Field(default=None)
            vni_override: int | None = Field(default=None)
            rt_override: str | None = Field(default=None)
            rd_override: str | None = Field(default=None)
            tags: str = Field(default=["all"])
            trunk_groups: str | None = Field(default=None)
            evpn_l2_multicast: EvpnL2Multicast | None = Field(default=None)
            evpn_l3_multicast: EvpnL3Multicast | None = Field(default=None)
            igmp_snooping_enabled: bool | None = Field(default=None)
            igmp_snooping_querier: IgmpSnoopingQuerier | None = Field(default=None)
            vxlan: bool = Field(default=True)
            mtu: int | None = Field(default=None)
            ospf: Ospf | None = Field(default=None)
            bgp: Bgp | None = Field(default=None)
            raw_eos_cli: str | None = Field(default=None)
            structured_config: StructuredConfig | None = Field(default=None)

        class IpHelpersItem(BaseModel):
            ip_helper: str | None = Field(default=None)
            source_interface: str | None = Field(default=None)
            source_vrf: str | None = Field(default=None)

        class EvpnL2Multicast(BaseModel):
            enabled: bool | None = Field(default=None)

        class EvpnL3Multicast(BaseModel):
            enabled: bool | None = Field(default=None)

        class IgmpSnoopingQuerier(BaseModel):
            enabled: bool | None = Field(default=None)
            source_address: str | None = Field(default=None)
            version: int | None = Field(default=None)

        class Ospf(BaseModel):
            class MessageDigestKeysItem(BaseModel):
                id: int | None = Field(default=None)
                hash_algorithm: str = Field(default="sha512")
                key: str | None = Field(default=None)

            enabled: bool | None = Field(default=None)
            point_to_point: bool = Field(default=True)
            area: str = Field(default="0")
            cost: int | None = Field(default=None)
            authentication: str | None = Field(default=None)
            simple_auth_key: str | None = Field(default=None)
            message_digest_keys: MessageDigestKeysItem | None = Field(default=None)

        class Bgp(BaseModel):
            class StructuredConfig(BaseModel):
                class RdEvpnDomain(BaseModel):
                    domain: str | None = Field(default=None)
                    rd: str | None = Field(default=None)

                class RouteTargets(BaseModel):
                    class ImportEvpnDomainsItem(BaseModel):
                        domain: str | None = Field(default=None)
                        route_target: str | None = Field(default=None)

                    class ExportEvpnDomainsItem(BaseModel):
                        domain: str | None = Field(default=None)
                        route_target: str | None = Field(default=None)

                    class ImportExportEvpnDomainsItem(BaseModel):
                        domain: str | None = Field(default=None)
                        route_target: str | None = Field(default=None)

                    both: str | None = Field(default=None)
                    import_key: str | None = Field(default=None, alias="import")
                    export: str | None = Field(default=None)
                    import_evpn_domains: ImportEvpnDomainsItem | None = Field(default=None)
                    export_evpn_domains: ExportEvpnDomainsItem | None = Field(default=None)
                    import_export_evpn_domains: ImportExportEvpnDomainsItem | None = Field(default=None)

                id: int | None = Field(default=None)
                tenant: str | None = Field(default=None)
                rd: str | None = Field(default=None)
                rd_evpn_domain: RdEvpnDomain | None = Field(default=None)
                eos_cli: str | None = Field(default=None)
                route_targets: RouteTargets | None = Field(default=None)
                redistribute_routes: str | None = Field(default=None)
                no_redistribute_routes: str | None = Field(default=None)

            structured_config: StructuredConfig | None = Field(default=None)
            raw_eos_cli: str | None = Field(default=None)

        class StructuredConfig(BaseModel):
            class IpHelpersItem(BaseModel):
                ip_helper: str | None = Field(default=None)
                source_interface: str | None = Field(default=None)
                vrf: str | None = Field(default=None)

            class IpNat(BaseModel):
                class Destination(BaseModel):
                    class DynamicItem(BaseModel):
                        access_list: str | None = Field(default=None)
                        comment: str | None = Field(default=None)
                        pool_name: str = Field(default=None)
                        priority: int | None = Field(default=None)

                    class StaticItem(BaseModel):
                        access_list: str | None = Field(default=None)
                        comment: str | None = Field(default=None)
                        direction: str | None = Field(default=None)
                        group: int | None = Field(default=None)
                        original_ip: str | None = Field(default=None)
                        original_port: int | None = Field(default=None)
                        priority: int | None = Field(default=None)
                        protocol: str | None = Field(default=None)
                        translated_ip: str = Field(default=None)
                        translated_port: int | None = Field(default=None)

                    dynamic: DynamicItem | None = Field(default=None)
                    static: StaticItem | None = Field(default=None)

                class Source(BaseModel):
                    class DynamicItem(BaseModel):
                        access_list: str | None = Field(default=None)
                        comment: str | None = Field(default=None)
                        nat_type: str = Field(default=None)
                        pool_name: str | None = Field(default=None)
                        priority: int | None = Field(default=None)

                    class StaticItem(BaseModel):
                        access_list: str | None = Field(default=None)
                        comment: str | None = Field(default=None)
                        direction: str | None = Field(default=None)
                        group: int | None = Field(default=None)
                        original_ip: str | None = Field(default=None)
                        original_port: int | None = Field(default=None)
                        priority: int | None = Field(default=None)
                        protocol: str | None = Field(default=None)
                        translated_ip: str = Field(default=None)
                        translated_port: int | None = Field(default=None)

                    dynamic: DynamicItem | None = Field(default=None)
                    static: StaticItem | None = Field(default=None)

                destination: Destination | None = Field(default=None)
                source: Source | None = Field(default=None)

            class Ipv6NdPrefixesItem(BaseModel):
                ipv6_prefix: str | None = Field(default=None)
                valid_lifetime: str | None = Field(default=None)
                preferred_lifetime: str | None = Field(default=None)
                no_autoconfig_flag: bool | None = Field(default=None)

            class Ipv6DhcpRelayDestinationsItem(BaseModel):
                address: str | None = Field(default=None)
                vrf: str | None = Field(default=None)
                local_interface: str | None = Field(default=None)
                source_address: str | None = Field(default=None)
                link_address: str | None = Field(default=None)

            class Multicast(BaseModel):
                class Ipv4(BaseModel):
                    class BoundariesItem(BaseModel):
                        boundary: str | None = Field(default=None)
                        out: bool | None = Field(default=None)

                    class SourceRouteExport(BaseModel):
                        enabled: bool = Field(default=None)
                        administrative_distance: int | None = Field(default=None)

                    boundaries: BoundariesItem | None = Field(default=None)
                    source_route_export: SourceRouteExport | None = Field(default=None)
                    static: bool | None = Field(default=None)

                class Ipv6(BaseModel):
                    class BoundariesItem(BaseModel):
                        boundary: str | None = Field(default=None)

                    class SourceRouteExport(BaseModel):
                        enabled: bool = Field(default=None)
                        administrative_distance: int | None = Field(default=None)

                    boundaries: BoundariesItem | None = Field(default=None)
                    source_route_export: SourceRouteExport | None = Field(default=None)
                    static: bool | None = Field(default=None)

                ipv4: Ipv4 | None = Field(default=None)
                ipv6: Ipv6 | None = Field(default=None)

            class OspfMessageDigestKeysItem(BaseModel):
                id: int | None = Field(default=None)
                hash_algorithm: str | None = Field(default=None)
                key: str | None = Field(default=None)

            class Pim(BaseModel):
                class Ipv4(BaseModel):
                    dr_priority: int | None = Field(default=None)
                    sparse_mode: bool | None = Field(default=None)
                    local_interface: str | None = Field(default=None)

                ipv4: Ipv4 | None = Field(default=None)

            class VrrpIdsItem(BaseModel):
                class Advertisement(BaseModel):
                    interval: int | None = Field(default=None)

                class Preempt(BaseModel):
                    class Delay(BaseModel):
                        minimum: int | None = Field(default=None)
                        reload: int | None = Field(default=None)

                    enabled: bool = Field(default=None)
                    delay: Delay | None = Field(default=None)

                class Timers(BaseModel):
                    class Delay(BaseModel):
                        reload: int | None = Field(default=None)

                    delay: Delay | None = Field(default=None)

                class TrackedObjectItem(BaseModel):
                    name: str | None = Field(default=None)
                    decrement: int | None = Field(default=None)
                    shutdown: bool | None = Field(default=None)

                class Ipv4(BaseModel):
                    address: str = Field(default=None)
                    version: int | None = Field(default=None)

                class Ipv6(BaseModel):
                    address: str = Field(default=None)

                id: int | None = Field(default=None)
                priority_level: int | None = Field(default=None)
                advertisement: Advertisement | None = Field(default=None)
                preempt: Preempt | None = Field(default=None)
                timers: Timers | None = Field(default=None)
                tracked_object: TrackedObjectItem | None = Field(default=None)
                ipv4: Ipv4 | None = Field(default=None)
                ipv6: Ipv6 | None = Field(default=None)

            class Vrrp(BaseModel):
                virtual_router: str | None = Field(default=None)
                priority: int | None = Field(default=None)
                advertisement_interval: int | None = Field(default=None)
                preempt_delay_minimum: int | None = Field(default=None)
                ipv4: str | None = Field(default=None)
                ipv6: str | None = Field(default=None)

            class IpAttachedHostRouteExport(BaseModel):
                enabled: bool = Field(default=None)
                distance: int | None = Field(default=None)

            class Bfd(BaseModel):
                echo: bool | None = Field(default=None)
                interval: int | None = Field(default=None)
                min_rx: int | None = Field(default=None)
                multiplier: int | None = Field(default=None)

            class ServicePolicy(BaseModel):
                class Pbr(BaseModel):
                    input: str | None = Field(default=None)

                pbr: Pbr | None = Field(default=None)

            name: str | None = Field(default=None)
            description: str | None = Field(default=None)
            shutdown: bool | None = Field(default=None)
            vrf: str | None = Field(default=None)
            arp_aging_timeout: int | None = Field(default=None)
            arp_cache_dynamic_capacity: int | None = Field(default=None)
            arp_gratuitous_accept: bool | None = Field(default=None)
            arp_monitor_mac_address: bool | None = Field(default=None)
            ip_proxy_arp: bool | None = Field(default=None)
            ip_directed_broadcast: bool | None = Field(default=None)
            ip_address: str | None = Field(default=None)
            ip_address_secondaries: str | None = Field(default=None)
            ip_virtual_router_addresses: str | None = Field(default=None)
            ip_address_virtual: str | None = Field(default=None)
            ip_address_virtual_secondaries: str | None = Field(default=None)
            ip_igmp: bool | None = Field(default=None)
            ip_igmp_version: int | None = Field(default=None)
            ip_helpers: IpHelpersItem | None = Field(default=None)
            ip_nat: IpNat | None = Field(default=None)
            ipv6_enable: bool | None = Field(default=None)
            ipv6_address: str | None = Field(default=None)
            ipv6_address_virtual: str | None = Field(default=None)
            ipv6_address_virtuals: str | None = Field(default=None)
            ipv6_address_link_local: str | None = Field(default=None)
            ipv6_virtual_router_address: str | None = Field(default=None)
            ipv6_virtual_router_addresses: str | None = Field(default=None)
            ipv6_nd_ra_disabled: bool | None = Field(default=None)
            ipv6_nd_managed_config_flag: bool | None = Field(default=None)
            ipv6_nd_prefixes: Ipv6NdPrefixesItem | None = Field(default=None)
            ipv6_dhcp_relay_destinations: Ipv6DhcpRelayDestinationsItem | None = Field(default=None)
            access_group_in: str | None = Field(default=None)
            access_group_out: str | None = Field(default=None)
            ipv6_access_group_in: str | None = Field(default=None)
            ipv6_access_group_out: str | None = Field(default=None)
            multicast: Multicast | None = Field(default=None)
            ospf_network_point_to_point: bool | None = Field(default=None)
            ospf_area: str | None = Field(default=None)
            ospf_cost: int | None = Field(default=None)
            ospf_authentication: str | None = Field(default=None)
            ospf_authentication_key: str | None = Field(default=None)
            ospf_message_digest_keys: OspfMessageDigestKeysItem | None = Field(default=None)
            pim: Pim | None = Field(default=None)
            isis_enable: str | None = Field(default=None)
            isis_passive: bool | None = Field(default=None)
            isis_metric: int | None = Field(default=None)
            isis_network_point_to_point: bool | None = Field(default=None)
            mtu: int | None = Field(default=None)
            no_autostate: bool | None = Field(default=None)
            vrrp_ids: VrrpIdsItem | None = Field(default=None)
            vrrp: Vrrp | None = Field(default=None)
            ip_attached_host_route_export: IpAttachedHostRouteExport | None = Field(default=None)
            bfd: Bfd | None = Field(default=None)
            service_policy: ServicePolicy | None = Field(default=None)
            pvlan_mapping: str | None = Field(default=None)
            tenant: str | None = Field(default=None)
            tags: str | None = Field(default=None)
            type: str | None = Field(default=None)
            eos_cli: str | None = Field(default=None)

        profile: str | None = Field(default=None)
        parent_profile: str | None = Field(default=None)
        nodes: NodesItem | None = Field(default=None)
        name: str | None = Field(default=None)
        enabled: bool | None = Field(default=None)
        description: str | None = Field(default=None)
        ip_address: str | None = Field(default=None)
        ipv6_address: str | None = Field(default=None)
        ipv6_enable: bool | None = Field(default=None)
        ip_address_virtual: str | None = Field(default=None)
        ipv6_address_virtual: str | None = Field(default=None)
        ipv6_address_virtuals: str | None = Field(default=None)
        ip_address_virtual_secondaries: str | None = Field(default=None)
        ip_virtual_router_addresses: str | None = Field(default=None)
        ipv6_virtual_router_addresses: str | None = Field(default=None)
        ip_helpers: IpHelpersItem | None = Field(default=None)
        vni_override: int | None = Field(default=None)
        rt_override: str | None = Field(default=None)
        rd_override: str | None = Field(default=None)
        tags: str = Field(default=["all"])
        trunk_groups: str | None = Field(default=None)
        evpn_l2_multicast: EvpnL2Multicast | None = Field(default=None)
        evpn_l3_multicast: EvpnL3Multicast | None = Field(default=None)
        igmp_snooping_enabled: bool | None = Field(default=None)
        igmp_snooping_querier: IgmpSnoopingQuerier | None = Field(default=None)
        vxlan: bool = Field(default=True)
        mtu: int | None = Field(default=None)
        ospf: Ospf | None = Field(default=None)
        bgp: Bgp | None = Field(default=None)
        raw_eos_cli: str | None = Field(default=None)
        structured_config: StructuredConfig | None = Field(default=None)

    class TrunkGroups(BaseModel):
        class Mlag(BaseModel):
            name: str = Field(default="MLAG")

        class MlagL3(BaseModel):
            name: str = Field(default="LEAF_PEER_L3")

        class Uplink(BaseModel):
            name: str = Field(default="UPLINK")

        mlag: Mlag | None = Field(default=None)
        mlag_l3: MlagL3 | None = Field(default=None)
        uplink: Uplink | None = Field(default=None)

    class UnderlayMulticastAnycastRp(BaseModel):
        mode: str = Field(default="pim")

    class UnderlayMulticastRpsItem(BaseModel):
        class NodesItem(BaseModel):
            name: str | None = Field(default=None)
            loopback_number: int = Field(default=None)
            description: str = Field(default="PIM RP")

        rp: str | None = Field(default=None)
        nodes: NodesItem | None = Field(default=None)
        groups: str | None = Field(default=None)
        access_list_name: str | None = Field(default=None)

    class UplinkPtp(BaseModel):
        enable: bool = Field(default=False)

    avd_data_conversion_mode: str = Field(default="debug")
    avd_data_validation_mode: str = Field(default="warning")
    bfd_multihop: BfdMultihop = Field(default={"interval": 300, "min_rx": 300, "multiplier": 3})
    bgp_as: str | None = Field(default=None)
    bgp_default_ipv4_unicast: bool = Field(default=False)
    bgp_distance: BgpDistance | None = Field(default=None)
    bgp_ecmp: int = Field(default=4)
    bgp_graceful_restart: BgpGracefulRestart | None = Field(default=None)
    bgp_maximum_paths: int = Field(default=4)
    bgp_mesh_pes: bool = Field(default=False)
    bgp_peer_groups: BgpPeerGroups | None = Field(default=None)
    bgp_update_wait_install: bool | None = Field(default=None)
    bgp_update_wait_for_convergence: bool | None = Field(default=None)
    connected_endpoints_keys: ConnectedEndpointsKeysItem = Field(
        default=[
            {"key": "servers", "type": "server", "description": "Server"},
            {"key": "firewalls", "type": "firewall", "description": "Firewall"},
            {"key": "routers", "type": "router", "description": "Router"},
            {"key": "load_balancers", "type": "load_balancer", "description": "Load Balancer"},
            {"key": "storage_arrays", "type": "storage_array", "description": "Storage Array"},
            {"key": "cpes", "type": "cpe", "description": "CPE"},
            {"key": "workstations", "type": "workstation", "description": "Workstation"},
            {"key": "access_points", "type": "access_point", "description": "Access Point"},
            {"key": "phones", "type": "phone", "description": "Phone"},
            {"key": "printers", "type": "printer", "description": "Printer"},
            {"key": "cameras", "type": "camera", "description": "Camera"},
            {"key": "generic_devices", "type": "generic_device", "description": "Generic Device"},
        ]
    )
    core_interfaces: CoreInterfaces | None = Field(default=None)
    custom_structured_configuration_list_merge: str = Field(default="append_rp")
    custom_structured_configuration_prefix: str = Field(default=["custom_structured_configuration_"])
    cvp_ingestauth_key: str | None = Field(default=None)
    cvp_instance_ip: str | None = Field(default=None)
    cvp_instance_ips: str | None = Field(default=None)
    cvp_token_file: str | None = Field(default=None)
    dc_name: str | None = Field(default=None)
    default_igmp_snooping_enabled: bool = Field(default=True)
    default_interfaces: DefaultInterfacesItem | None = Field(default=None)
    default_node_types: DefaultNodeTypesItem | None = Field(default=None)
    design: Design | None = Field(default=None)
    enable_trunk_groups: bool = Field(default=False)
    eos_designs_custom_templates: EosDesignsCustomTemplatesItem | None = Field(default=None)
    eos_designs_documentation: EosDesignsDocumentation | None = Field(default=None)
    event_handlers: EventHandlersItem | None = Field(default=None)
    evpn_ebgp_gateway_inter_domain: bool | None = Field(default=None)
    evpn_ebgp_gateway_multihop: int = Field(default=15)
    evpn_ebgp_multihop: int = Field(default=3)
    evpn_hostflap_detection: EvpnHostflapDetection | None = Field(default=None)
    evpn_import_pruning: bool = Field(default=False)
    evpn_multicast: bool = Field(default=False)
    evpn_overlay_bgp_rtc: bool = Field(default=False)
    evpn_prevent_readvertise_to_server: bool = Field(default=False)
    evpn_short_esi_prefix: str = Field(default="0000:0000:")
    evpn_vlan_aware_bundles: bool = Field(default=False)
    fabric_evpn_encapsulation: str = Field(default="vxlan")
    fabric_ip_addressing: FabricIpAddressing | None = Field(default=None)
    fabric_name: str = Field(default=None)
    hardware_counters: HardwareCounters | None = Field(default=None)
    internal_vlan_order: InternalVlanOrder = Field(default={"allocation": "ascending", "range": {"beginning": 1006, "ending": 1199}})
    ipv6_mgmt_destination_networks: str | None = Field(default=None)
    ipv6_mgmt_gateway: str | None = Field(default=None)
    is_deployed: bool = Field(default=True)
    isis_advertise_passive_only: bool = Field(default=False)
    isis_area_id: str = Field(default="49.0001")
    isis_default_circuit_type: str = Field(default="level-2")
    isis_default_is_type: str = Field(default="level-2")
    isis_default_metric: int = Field(default=50)
    isis_maximum_paths: int | None = Field(default=None)
    isis_ti_lfa: IsisTiLfa | None = Field(default=None)
    l3_edge: L3Edge | None = Field(default=None)
    local_users: LocalUsersItem | None = Field(default=None)
    mac_address_table: MacAddressTable | None = Field(default=None)
    management_eapi: ManagementEapi | None = Field(default=None)
    mgmt_destination_networks: str | None = Field(default=None)
    mgmt_gateway: str | None = Field(default=None)
    mgmt_interface: str = Field(default="Management1")
    mgmt_interface_description: str = Field(default="oob_management")
    mgmt_interface_vrf: str = Field(default="MGMT")
    mgmt_vrf_routing: bool = Field(default=False)
    mlag_ibgp_peering_vrfs: MlagIbgpPeeringVrfs | None = Field(default=None)
    name_servers: str | None = Field(default=None)
    network_ports: NetworkPortsItem | None = Field(default=None)
    network_services_keys: NetworkServicesKeysItem = Field(default=[{"name": "tenants"}])
    node_type_keys: NodeTypeKeysItem | None = Field(default=None)
    only_local_vlan_trunk_groups: bool = Field(default=False)
    overlay_cvx_servers: str | None = Field(default=None)
    overlay_her_flood_list_per_vni: bool = Field(default=False)
    overlay_her_flood_list_scope: str = Field(default="fabric")
    overlay_loopback_description: str | None = Field(default=None)
    overlay_mlag_rfc5549: bool = Field(default=False)
    overlay_rd_type: OverlayRdType | None = Field(default=None)
    overlay_routing_protocol: str = Field(default="ebgp")
    overlay_routing_protocol_address_family: str = Field(default="ipv4")
    overlay_rt_type: OverlayRtType | None = Field(default=None)
    p2p_uplinks_mtu: int = Field(default=9214)
    p2p_uplinks_qos_profile: str | None = Field(default=None)
    platform_settings: PlatformSettingsItem = Field(
        default=[
            {"platforms": ["default"], "feature_support": {"queue_monitor_length_notify": False}, "reload_delay": {"mlag": 300, "non_mlag": 330}},
            {
                "platforms": ["7050X3", "720XP", "722XP"],
                "feature_support": {"queue_monitor_length_notify": False},
                "reload_delay": {"mlag": 300, "non_mlag": 330},
                "trident_forwarding_table_partition": "flexible exact-match 16384 l2-shared 98304 l3-shared 131072",
            },
            {
                "platforms": ["7280R", "7280R2", "7020R"],
                "lag_hardware_only": True,
                "reload_delay": {"mlag": 900, "non_mlag": 1020},
                "tcam_profile": "vxlan-routing",
            },
            {"platforms": ["7280R3"], "reload_delay": {"mlag": 900, "non_mlag": 1020}},
            {
                "platforms": ["7500R", "7500R2"],
                "lag_hardware_only": True,
                "management_interface": "Management0",
                "reload_delay": {"mlag": 900, "non_mlag": 1020},
                "tcam_profile": "vxlan-routing",
            },
            {"platforms": ["7500R3", "7800R3"], "management_interface": "Management0", "reload_delay": {"mlag": 900, "non_mlag": 1020}},
            {"platforms": ["7368X4"], "management_interface": "Management0", "reload_delay": {"mlag": 300, "non_mlag": 330}},
            {
                "platforms": ["7300X3"],
                "management_interface": "Management0",
                "reload_delay": {"mlag": 1200, "non_mlag": 1320},
                "trident_forwarding_table_partition": "flexible exact-match 16384 l2-shared 98304 l3-shared 131072",
            },
            {
                "platforms": ["VEOS", "VEOS-LAB", "vEOS", "vEOS-lab"],
                "feature_support": {
                    "bgp_update_wait_for_convergence": False,
                    "bgp_update_wait_install": False,
                    "interface_storm_control": False,
                    "queue_monitor_length_notify": False,
                },
                "reload_delay": {"mlag": 300, "non_mlag": 330},
            },
            {
                "platforms": ["CEOS", "cEOS", "ceos", "cEOSLab"],
                "feature_support": {
                    "bgp_update_wait_for_convergence": False,
                    "bgp_update_wait_install": False,
                    "interface_storm_control": False,
                    "queue_monitor_length_notify": False,
                },
                "management_interface": "Management0",
                "reload_delay": {"mlag": 300, "non_mlag": 330},
            },
        ]
    )
    platform_speed_groups: PlatformSpeedGroupsItem | None = Field(default=None)
    pod_name: str | None = Field(default=None)
    port_profiles: PortProfilesItem | None = Field(default=None)
    ptp: Ptp | None = Field(default=None)
    ptp_profiles: PtpProfilesItem = Field(
        default=[
            {"announce": {"interval": 0, "timeout": 3}, "delay_req": -3, "profile": "aes67-r16-2016", "sync_message": {"interval": -3}, "transport": "ipv4"},
            {"announce": {"interval": -2, "timeout": 3}, "delay_req": -4, "profile": "smpte2059-2", "sync_message": {"interval": -4}, "transport": "ipv4"},
            {"announce": {"interval": 2, "timeout": 3}, "delay_req": 0, "profile": "aes67", "sync_message": {"interval": 0}, "transport": "ipv4"},
        ]
    )
    queue_monitor_length: QueueMonitorLength | None = Field(default=None)
    redundancy: Redundancy | None = Field(default=None)
    serial_number: str | None = Field(default=None)
    shutdown_interfaces_towards_undeployed_peers: bool = Field(default=False)
    snmp_settings: SnmpSettings | None = Field(default=None)
    svi_profiles: SviProfilesItem | None = Field(default=None)
    system_mac_address: str | None = Field(default=None)
    terminattr_disable_aaa: bool = Field(default=False)
    terminattr_ingestexclude: str = Field(default="/Sysdb/cell/1/agent,/Sysdb/cell/2/agent")
    terminattr_ingestgrpcurl_port: int = Field(default=9910)
    terminattr_smashexcludes: str = Field(default="ale,flexCounter,hardware,kni,pulse,strata")
    timezone: str | None = Field(default=None)
    trunk_groups: TrunkGroups | None = Field(default=None)
    type: str | None = Field(default=None)
    underlay_filter_peer_as: bool = Field(default=False)
    underlay_filter_redistribute_connected: bool = Field(default=True)
    underlay_ipv6: bool = Field(default=False)
    underlay_isis_instance_name: str | None = Field(default=None)
    underlay_multicast: bool = Field(default=False)
    underlay_multicast_anycast_rp: UnderlayMulticastAnycastRp | None = Field(default=None)
    underlay_multicast_rps: UnderlayMulticastRpsItem | None = Field(default=None)
    underlay_ospf_area: str = Field(default="0.0.0.0")
    underlay_ospf_bfd_enable: bool = Field(default=False)
    underlay_ospf_max_lsa: int = Field(default=12000)
    underlay_ospf_process_id: int = Field(default=100)
    underlay_rfc5549: bool = Field(default=False)
    underlay_routing_protocol: str | None = Field(default=None)
    uplink_ptp: UplinkPtp | None = Field(default=None)
    vtep_vvtep_ip: str | None = Field(default=None)
