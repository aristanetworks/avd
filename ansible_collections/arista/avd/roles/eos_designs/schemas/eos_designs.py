# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

from pydantic import BaseModel, Field

from ansible_collections.arista.avd.roles.eos_cli_config_gen.schemas.eos_cli_config_gen import EosCliConfigGen


class EosDesigns(BaseModel):
    class BfdMultihop(BaseModel):
        interval: int = Field(default=None)
        min_rx: int = Field(default=None)
        multiplier: int = Field(default=None)

    class BgpGracefulRestart(BaseModel):
        enabled: bool = Field(default=False)
        restart_time: int = Field(default=300)

    class BgpPeerGroups(BaseModel):
        class Ipv4UnderlayPeers(BaseModel):
            name: str = Field(default="IPv4-UNDERLAY-PEERS")
            password: str | None = Field(default=None)
            bfd: bool = Field(default=False)
            structured_config: EosCliConfigGen.RouterBgp.PeerGroupsItem | None = Field(default=None)

        class MlagIpv4UnderlayPeer(BaseModel):
            name: str = Field(default="MLAG-IPv4-UNDERLAY-PEER")
            password: str | None = Field(default=None)
            bfd: bool = Field(default=False)
            structured_config: EosCliConfigGen.RouterBgp.PeerGroupsItem | None = Field(default=None)

        class EvpnOverlayPeers(BaseModel):
            name: str = Field(default="EVPN-OVERLAY-PEERS")
            password: str | None = Field(default=None)
            bfd: bool = Field(default=True)
            structured_config: EosCliConfigGen.RouterBgp.PeerGroupsItem | None = Field(default=None)

        class EvpnOverlayCore(BaseModel):
            name: str = Field(default="EVPN-OVERLAY-CORE")
            password: str | None = Field(default=None)
            bfd: bool = Field(default=True)
            structured_config: EosCliConfigGen.RouterBgp.PeerGroupsItem | None = Field(default=None)

        class MplsOverlayPeers(BaseModel):
            name: str = Field(default="MPLS-OVERLAY-PEERS")
            password: str | None = Field(default=None)
            bfd: bool = Field(default=True)
            structured_config: EosCliConfigGen.RouterBgp.PeerGroupsItem | None = Field(default=None)

        class RrOverlayPeers(BaseModel):
            name: str = Field(default="RR-OVERLAY-PEERS")
            password: str | None = Field(default=None)
            bfd: bool = Field(default=True)
            structured_config: EosCliConfigGen.RouterBgp.PeerGroupsItem | None = Field(default=None)

        class IpvpnGatewayPeers(BaseModel):
            name: str = Field(default="IPVPN-GATEWAY-PEERS")
            password: str | None = Field(default=None)
            bfd: bool = Field(default=True)
            structured_config: EosCliConfigGen.RouterBgp.PeerGroupsItem | None = Field(default=None)

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
                    interfaces: list[str] | None = Field(default=None)

                mode: str = Field(default="active")
                nodes_child_interfaces: list[NodesChildInterfacesItem] | None = Field(default=None)

            name: str | None = Field(default=None)
            id: int | None = Field(default=None)
            speed: str | None = Field(default=None)
            ip_pool: str | None = Field(default=None)
            subnet: str | None = Field(default=None)
            ip: list[str] | None = Field(default=None)
            ipv6_enable: bool = Field(default=False)
            nodes: list[str] | None = Field(default=None)
            interfaces: list[str] | None = Field(default=None)
            as_key: list[str] | None = Field(default=None, alias="as")
            descriptions: list[str] | None = Field(default=None)
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
                    interfaces: list[str] | None = Field(default=None)

                mode: str = Field(default="active")
                nodes_child_interfaces: list[NodesChildInterfacesItem] | None = Field(default=None)

            nodes: list[str] = Field(default=None)
            profile: str | None = Field(default=None)
            id: int | None = Field(default=None)
            speed: str | None = Field(default=None)
            ip_pool: str | None = Field(default=None)
            subnet: str | None = Field(default=None)
            ip: list[str] | None = Field(default=None)
            ipv6_enable: bool = Field(default=False)
            interfaces: list[str] | None = Field(default=None)
            as_key: list[str] | None = Field(default=None, alias="as")
            descriptions: list[str] | None = Field(default=None)
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

        p2p_links_ip_pools: list[P2pLinksIpPoolsItem] | None = Field(default=None)
        p2p_links_profiles: list[P2pLinksProfilesItem] | None = Field(default=None)
        p2p_links: list[P2pLinksItem] | None = Field(default=None)

    class DefaultInterfacesItem(BaseModel):
        types: list[str] = Field(default=None)
        platforms: list[str] = Field(default=None)
        uplink_interfaces: list[str] | None = Field(default=None)
        mlag_interfaces: list[str] | None = Field(default=None)
        downlink_interfaces: list[str] | None = Field(default=None)

    class DefaultNodeTypesItem(BaseModel):
        node_type: str | None = Field(default=None)
        match_hostnames: list[str] = Field(default=None)

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

    class EvpnHostflapDetection(BaseModel):
        enabled: bool = Field(default=True)
        threshold: int = Field(default=5)
        window: int = Field(default=180)
        expiry_timeout: int | None = Field(default=None)

    class FabricIpAddressing(BaseModel):
        class Mlag(BaseModel):
            algorithm: str = Field(default="first_id")

        mlag: Mlag | None = Field(default=None)

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
                    interfaces: list[str] | None = Field(default=None)

                mode: str = Field(default="active")
                nodes_child_interfaces: list[NodesChildInterfacesItem] | None = Field(default=None)

            name: str | None = Field(default=None)
            id: int | None = Field(default=None)
            speed: str | None = Field(default=None)
            ip_pool: str | None = Field(default=None)
            subnet: str | None = Field(default=None)
            ip: list[str] | None = Field(default=None)
            ipv6_enable: bool = Field(default=False)
            nodes: list[str] | None = Field(default=None)
            interfaces: list[str] | None = Field(default=None)
            as_key: list[str] | None = Field(default=None, alias="as")
            descriptions: list[str] | None = Field(default=None)
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
                    interfaces: list[str] | None = Field(default=None)

                mode: str = Field(default="active")
                nodes_child_interfaces: list[NodesChildInterfacesItem] | None = Field(default=None)

            nodes: list[str] = Field(default=None)
            profile: str | None = Field(default=None)
            id: int | None = Field(default=None)
            speed: str | None = Field(default=None)
            ip_pool: str | None = Field(default=None)
            subnet: str | None = Field(default=None)
            ip: list[str] | None = Field(default=None)
            ipv6_enable: bool = Field(default=False)
            interfaces: list[str] | None = Field(default=None)
            as_key: list[str] | None = Field(default=None, alias="as")
            descriptions: list[str] | None = Field(default=None)
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

        p2p_links_ip_pools: list[P2pLinksIpPoolsItem] | None = Field(default=None)
        p2p_links_profiles: list[P2pLinksProfilesItem] | None = Field(default=None)
        p2p_links: list[P2pLinksItem] | None = Field(default=None)

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
            designated_forwarder_preferences: list[str] | None = Field(default=None)
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

            mode: str | None = Field(default=None)
            channel_id: int | None = Field(default=None)
            description: str | None = Field(default=None)
            enabled: bool = Field(default=True)
            short_esi: str | None = Field(default=None)
            lacp_fallback: LacpFallback | None = Field(default=None)
            lacp_timer: LacpTimer | None = Field(default=None)
            subinterfaces: list[SubinterfacesItem] | None = Field(default=None)
            raw_eos_cli: str | None = Field(default=None)
            structured_config: EosCliConfigGen.PortChannelInterfacesItem | None = Field(default=None)

        switches: list[str] | None = Field(default=None)
        switch_ports: list[str] | None = Field(default=None)
        description: str | None = Field(default=None)
        speed: str | None = Field(default=None)
        profile: str | None = Field(default=None)
        enabled: bool = Field(default=True)
        mode: str | None = Field(default=None)
        mtu: int | None = Field(default=None)
        l2_mtu: int | None = Field(default=None)
        native_vlan: int | None = Field(default=None)
        native_vlan_tag: bool = Field(default=False)
        trunk_groups: list[str] | None = Field(default=None)
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
        poe: EosCliConfigGen.EthernetInterfacesItem.Poe | None = Field(default=None)
        storm_control: StormControl | None = Field(default=None)
        monitor_sessions: list[MonitorSessionsItem] | None = Field(default=None)
        ethernet_segment: EthernetSegment | None = Field(default=None)
        port_channel: PortChannel | None = Field(default=None)
        raw_eos_cli: str | None = Field(default=None)
        structured_config: EosCliConfigGen.EthernetInterfacesItem | None = Field(default=None)

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
        default_overlay_address_families: list[str] | None = Field(default=None)
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

        platforms: list[str] | None = Field(default=None)
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
            speed_groups: list[int] | None = Field(default=None)

        platform: str | None = Field(default=None)
        speeds: list[SpeedsItem] | None = Field(default=None)

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
            designated_forwarder_preferences: list[str] | None = Field(default=None)
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

            mode: str | None = Field(default=None)
            channel_id: int | None = Field(default=None)
            description: str | None = Field(default=None)
            enabled: bool = Field(default=True)
            short_esi: str | None = Field(default=None)
            lacp_fallback: LacpFallback | None = Field(default=None)
            lacp_timer: LacpTimer | None = Field(default=None)
            subinterfaces: list[SubinterfacesItem] | None = Field(default=None)
            raw_eos_cli: str | None = Field(default=None)
            structured_config: EosCliConfigGen.PortChannelInterfacesItem | None = Field(default=None)

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
        trunk_groups: list[str] | None = Field(default=None)
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
        poe: EosCliConfigGen.EthernetInterfacesItem.Poe | None = Field(default=None)
        storm_control: StormControl | None = Field(default=None)
        monitor_sessions: list[MonitorSessionsItem] | None = Field(default=None)
        ethernet_segment: EthernetSegment | None = Field(default=None)
        port_channel: PortChannel | None = Field(default=None)
        raw_eos_cli: str | None = Field(default=None)
        structured_config: EosCliConfigGen.EthernetInterfacesItem | None = Field(default=None)

    class Ptp(BaseModel):
        enabled: bool | None = Field(default=None)
        profile: str = Field(default="aes67-r16-2016")
        domain: EosCliConfigGen.Ptp.Domain | None = Field(default=None)
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
        users: list[UsersItem] | None = Field(default=None)

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
                message_digest_keys: list[MessageDigestKeysItem] | None = Field(default=None)

            class Bgp(BaseModel):
                structured_config: EosCliConfigGen.RouterBgp.VlansItem | None = Field(default=None)
                raw_eos_cli: str | None = Field(default=None)

            node: str | None = Field(default=None)
            name: str | None = Field(default=None)
            enabled: bool | None = Field(default=None)
            description: str | None = Field(default=None)
            ip_address: str | None = Field(default=None)
            ipv6_address: str | None = Field(default=None)
            ipv6_enable: bool | None = Field(default=None)
            ip_address_virtual: str | None = Field(default=None)
            ipv6_address_virtual: str | None = Field(default=None)
            ipv6_address_virtuals: list[str] | None = Field(default=None)
            ip_address_virtual_secondaries: list[str] | None = Field(default=None)
            ip_virtual_router_addresses: list[str] | None = Field(default=None)
            ipv6_virtual_router_addresses: list[str] | None = Field(default=None)
            ip_helpers: list[IpHelpersItem] | None = Field(default=None)
            vni_override: int | None = Field(default=None)
            rt_override: str | None = Field(default=None)
            rd_override: str | None = Field(default=None)
            tags: list[str] = Field(default=["all"])
            trunk_groups: list[str] | None = Field(default=None)
            evpn_l2_multicast: EvpnL2Multicast | None = Field(default=None)
            evpn_l3_multicast: EvpnL3Multicast | None = Field(default=None)
            igmp_snooping_enabled: bool | None = Field(default=None)
            igmp_snooping_querier: IgmpSnoopingQuerier | None = Field(default=None)
            vxlan: bool = Field(default=True)
            mtu: int | None = Field(default=None)
            ospf: Ospf | None = Field(default=None)
            bgp: Bgp | None = Field(default=None)
            raw_eos_cli: str | None = Field(default=None)
            structured_config: EosCliConfigGen.VlanInterfacesItem | None = Field(default=None)

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
            message_digest_keys: list[MessageDigestKeysItem] | None = Field(default=None)

        class Bgp(BaseModel):
            structured_config: EosCliConfigGen.RouterBgp.VlansItem | None = Field(default=None)
            raw_eos_cli: str | None = Field(default=None)

        profile: str | None = Field(default=None)
        parent_profile: str | None = Field(default=None)
        nodes: list[NodesItem] | None = Field(default=None)
        name: str | None = Field(default=None)
        enabled: bool | None = Field(default=None)
        description: str | None = Field(default=None)
        ip_address: str | None = Field(default=None)
        ipv6_address: str | None = Field(default=None)
        ipv6_enable: bool | None = Field(default=None)
        ip_address_virtual: str | None = Field(default=None)
        ipv6_address_virtual: str | None = Field(default=None)
        ipv6_address_virtuals: list[str] | None = Field(default=None)
        ip_address_virtual_secondaries: list[str] | None = Field(default=None)
        ip_virtual_router_addresses: list[str] | None = Field(default=None)
        ipv6_virtual_router_addresses: list[str] | None = Field(default=None)
        ip_helpers: list[IpHelpersItem] | None = Field(default=None)
        vni_override: int | None = Field(default=None)
        rt_override: str | None = Field(default=None)
        rd_override: str | None = Field(default=None)
        tags: list[str] = Field(default=["all"])
        trunk_groups: list[str] | None = Field(default=None)
        evpn_l2_multicast: EvpnL2Multicast | None = Field(default=None)
        evpn_l3_multicast: EvpnL3Multicast | None = Field(default=None)
        igmp_snooping_enabled: bool | None = Field(default=None)
        igmp_snooping_querier: IgmpSnoopingQuerier | None = Field(default=None)
        vxlan: bool = Field(default=True)
        mtu: int | None = Field(default=None)
        ospf: Ospf | None = Field(default=None)
        bgp: Bgp | None = Field(default=None)
        raw_eos_cli: str | None = Field(default=None)
        structured_config: EosCliConfigGen.VlanInterfacesItem | None = Field(default=None)

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
        nodes: list[NodesItem] | None = Field(default=None)
        groups: list[str] | None = Field(default=None)
        access_list_name: str | None = Field(default=None)

    class UplinkPtp(BaseModel):
        enable: bool = Field(default=False)

    avd_data_conversion_mode: str = Field(default="debug")
    avd_data_validation_mode: str = Field(default="warning")
    bfd_multihop: BfdMultihop = Field(default={"interval": 300, "min_rx": 300, "multiplier": 3})
    bgp_as: str | None = Field(default=None)
    bgp_default_ipv4_unicast: bool = Field(default=False)
    bgp_distance: EosCliConfigGen.RouterBgp.Distance | None = Field(default=None)
    bgp_ecmp: int = Field(default=4)
    bgp_graceful_restart: BgpGracefulRestart | None = Field(default=None)
    bgp_maximum_paths: int = Field(default=4)
    bgp_mesh_pes: bool = Field(default=False)
    bgp_peer_groups: BgpPeerGroups | None = Field(default=None)
    bgp_update_wait_install: EosCliConfigGen.RouterBgp.Updates.WaitInstall | None = Field(default=None)
    bgp_update_wait_for_convergence: EosCliConfigGen.RouterBgp.Updates.WaitForConvergence | None = Field(default=None)
    connected_endpoints_keys: list[ConnectedEndpointsKeysItem] = Field(
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
    custom_structured_configuration_prefix: list[str] = Field(default=["custom_structured_configuration_"])
    cvp_ingestauth_key: str | None = Field(default=None)
    cvp_instance_ip: str | None = Field(default=None)
    cvp_instance_ips: list[str] | None = Field(default=None)
    cvp_token_file: str | None = Field(default=None)
    dc_name: str | None = Field(default=None)
    default_igmp_snooping_enabled: bool = Field(default=True)
    default_interfaces: list[DefaultInterfacesItem] | None = Field(default=None)
    default_node_types: list[DefaultNodeTypesItem] | None = Field(default=None)
    design: Design | None = Field(default=None)
    enable_trunk_groups: bool = Field(default=False)
    eos_designs_custom_templates: list[EosDesignsCustomTemplatesItem] | None = Field(default=None)
    eos_designs_documentation: EosDesignsDocumentation | None = Field(default=None)
    event_handlers: EosCliConfigGen.EventHandlers | None = Field(default=None)
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
    hardware_counters: EosCliConfigGen.HardwareCounters | None = Field(default=None)
    internal_vlan_order: InternalVlanOrder = Field(default={"allocation": "ascending", "range": {"beginning": 1006, "ending": 1199}})
    ipv6_mgmt_destination_networks: list[str] | None = Field(default=None)
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
    local_users: EosCliConfigGen.LocalUsers | None = Field(default=None)
    mac_address_table: MacAddressTable | None = Field(default=None)
    management_eapi: ManagementEapi | None = Field(default=None)
    mgmt_destination_networks: list[str] | None = Field(default=None)
    mgmt_gateway: str | None = Field(default=None)
    mgmt_interface: str = Field(default="Management1")
    mgmt_interface_description: str = Field(default="oob_management")
    mgmt_interface_vrf: str = Field(default="MGMT")
    mgmt_vrf_routing: bool = Field(default=False)
    mlag_ibgp_peering_vrfs: MlagIbgpPeeringVrfs | None = Field(default=None)
    name_servers: list[str] | None = Field(default=None)
    network_ports: list[NetworkPortsItem] | None = Field(default=None)
    network_services_keys: list[NetworkServicesKeysItem] = Field(default=[{"name": "tenants"}])
    node_type_keys: list[NodeTypeKeysItem] | None = Field(default=None)
    only_local_vlan_trunk_groups: bool = Field(default=False)
    overlay_cvx_servers: list[str] | None = Field(default=None)
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
    platform_settings: list[PlatformSettingsItem] = Field(
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
    platform_speed_groups: list[PlatformSpeedGroupsItem] | None = Field(default=None)
    pod_name: str | None = Field(default=None)
    port_profiles: list[PortProfilesItem] | None = Field(default=None)
    ptp: Ptp | None = Field(default=None)
    ptp_profiles: list[PtpProfilesItem] = Field(
        default=[
            {"announce": {"interval": 0, "timeout": 3}, "delay_req": -3, "profile": "aes67-r16-2016", "sync_message": {"interval": -3}, "transport": "ipv4"},
            {"announce": {"interval": -2, "timeout": 3}, "delay_req": -4, "profile": "smpte2059-2", "sync_message": {"interval": -4}, "transport": "ipv4"},
            {"announce": {"interval": 2, "timeout": 3}, "delay_req": 0, "profile": "aes67", "sync_message": {"interval": 0}, "transport": "ipv4"},
        ]
    )
    queue_monitor_length: EosCliConfigGen.QueueMonitorLength | None = Field(default=None)
    redundancy: Redundancy | None = Field(default=None)
    serial_number: str | None = Field(default=None)
    shutdown_interfaces_towards_undeployed_peers: bool = Field(default=False)
    snmp_settings: SnmpSettings | None = Field(default=None)
    svi_profiles: list[SviProfilesItem] | None = Field(default=None)
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
    underlay_multicast_rps: list[UnderlayMulticastRpsItem] | None = Field(default=None)
    underlay_ospf_area: str = Field(default="0.0.0.0")
    underlay_ospf_bfd_enable: bool = Field(default=False)
    underlay_ospf_max_lsa: int = Field(default=12000)
    underlay_ospf_process_id: int = Field(default=100)
    underlay_rfc5549: bool = Field(default=False)
    underlay_routing_protocol: str | None = Field(default=None)
    uplink_ptp: UplinkPtp | None = Field(default=None)
    vtep_vvtep_ip: str | None = Field(default=None)
