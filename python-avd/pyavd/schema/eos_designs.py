# Copyright (c) 2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field
from typing_extensions import Annotated

from .eos_cli_config_gen import EosCliConfigGen
from .models import AvdDictBaseModel, AvdEosDesignsRootDictBaseModel
from .types import IntConvert, StrConvert


class EosDesigns(AvdEosDesignsRootDictBaseModel):
    model_config = ConfigDict(defer_build=True)

    class ApplicationClassification(EosCliConfigGen.ApplicationTrafficRecognition, BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        pass

    class BfdMultihop(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        interval: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=50, le=60000)
        min_rx: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=50, le=60000)
        multiplier: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=3, le=50)

    class BgpDistance(EosCliConfigGen.RouterBgp.Distance, BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        pass

    class BgpGracefulRestart(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        enabled: bool = False
        """
        Enable or disable graceful-restart for all BGP peers.
        """
        restart_time: Annotated[int, IntConvert(convert_types=(str))] | None = Field(300, ge=1, le=3600)
        """
        Restart time in seconds.
        """

    class BgpPeerGroups(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Ipv4UnderlayPeers(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class StructuredConfig(EosCliConfigGen.RouterBgp.PeerGroupsItem, BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                pass

            name: str | None = "IPv4-UNDERLAY-PEERS"
            """
            Name of peer group.
            """
            password: str | None = None
            """
            Type 7 encrypted password.
            """
            bfd: bool | None = False
            structured_config: StructuredConfig | None = None
            """
            Custom structured config added under router_bgp.peer_groups.[name=<name>] for eos_cli_config_gen.
            """

        class MlagIpv4UnderlayPeer(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class StructuredConfig(EosCliConfigGen.RouterBgp.PeerGroupsItem, BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                pass

            name: str | None = "MLAG-IPv4-UNDERLAY-PEER"
            """
            Name of peer group.
            """
            password: str | None = None
            """
            Type 7 encrypted password.
            """
            bfd: bool | None = False
            structured_config: StructuredConfig | None = None
            """
            Custom structured config added under router_bgp.peer_groups.[name=<name>] for eos_cli_config_gen.
            """

        class EvpnOverlayPeers(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class StructuredConfig(EosCliConfigGen.RouterBgp.PeerGroupsItem, BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                pass

            name: str | None = "EVPN-OVERLAY-PEERS"
            """
            Name of peer group.
            """
            password: str | None = None
            """
            Type 7 encrypted password.
            """
            bfd: bool | None = True
            structured_config: StructuredConfig | None = None
            """
            Custom structured config added under router_bgp.peer_groups.[name=<name>] for eos_cli_config_gen.
            """

        class EvpnOverlayCore(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class StructuredConfig(EosCliConfigGen.RouterBgp.PeerGroupsItem, BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                pass

            name: str | None = "EVPN-OVERLAY-CORE"
            """
            Name of peer group.
            """
            password: str | None = None
            """
            Type 7 encrypted password.
            """
            bfd: bool | None = True
            structured_config: StructuredConfig | None = None
            """
            Custom structured config added under router_bgp.peer_groups.[name=<name>] for eos_cli_config_gen.
            """

        class MplsOverlayPeers(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class StructuredConfig(EosCliConfigGen.RouterBgp.PeerGroupsItem, BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                pass

            name: str | None = "MPLS-OVERLAY-PEERS"
            """
            Name of peer group.
            """
            password: str | None = None
            """
            Type 7 encrypted password.
            """
            bfd: bool | None = True
            structured_config: StructuredConfig | None = None
            """
            Custom structured config added under router_bgp.peer_groups.[name=<name>] for eos_cli_config_gen.
            """

        class RrOverlayPeers(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class StructuredConfig(EosCliConfigGen.RouterBgp.PeerGroupsItem, BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                pass

            name: str | None = "RR-OVERLAY-PEERS"
            """
            Name of peer group.
            """
            password: str | None = None
            """
            Type 7 encrypted password.
            """
            bfd: bool | None = True
            structured_config: StructuredConfig | None = None
            """
            Custom structured config added under router_bgp.peer_groups.[name=<name>] for eos_cli_config_gen.
            """

        class IpvpnGatewayPeers(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class StructuredConfig(EosCliConfigGen.RouterBgp.PeerGroupsItem, BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                pass

            name: str | None = "IPVPN-GATEWAY-PEERS"
            """
            Name of peer group.
            """
            password: str | None = None
            """
            Type 7 encrypted password.
            """
            bfd: bool | None = True
            structured_config: StructuredConfig | None = None
            """
            Custom structured config added under router_bgp.peer_groups.[name=<name>] for eos_cli_config_gen.
            """

        class WanOverlayPeers(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class BfdTimers(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                interval: Annotated[int, IntConvert(convert_types=(str))] = Field(1000, ge=50, le=60000)
                """
                Interval in milliseconds.
                """
                min_rx: Annotated[int, IntConvert(convert_types=(str))] = Field(1000, ge=50, le=60000)
                """
                Rate in milliseconds.
                """
                multiplier: Annotated[int, IntConvert(convert_types=(str))] = Field(10, ge=3, le=50)

            class StructuredConfig(EosCliConfigGen.RouterBgp.PeerGroupsItem, BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                pass

            name: str | None = "WAN-OVERLAY-PEERS"
            """
            Name of peer group.
            """
            password: str | None = None
            """
            Type 7 encrypted password.
            """
            bfd: bool | None = True
            bfd_timers: BfdTimers | None = None
            """
            Specify the BFD timers to override the default values.
            It is recommended to keep BFD total timeout longer than the DPS
            timeout.
            The Default BFD timeout is 10 x 1 seconds and the default DPS timeout is 5 x 1 seconds.
            """
            listen_range_prefixes: list[str] | None = None
            """
            Only used for nodes where `wan_role` is `server` like AutoVPN RRs and Pathfinders.
            For clients, AVD will raise an error
            if the Loopback0 IP is not in any listen range.
            """
            ttl_maximum_hops: Annotated[int, IntConvert(convert_types=(str))] | None = 1
            structured_config: StructuredConfig | None = None
            """
            Custom structured config added under router_bgp.peer_groups.[name=<name>] for eos_cli_config_gen.
            """

        class WanRrOverlayPeers(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class BfdTimers(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                interval: Annotated[int, IntConvert(convert_types=(str))] = Field(1000, ge=50, le=60000)
                """
                Interval in milliseconds.
                """
                min_rx: Annotated[int, IntConvert(convert_types=(str))] = Field(1000, ge=50, le=60000)
                """
                Rate in milliseconds.
                """
                multiplier: Annotated[int, IntConvert(convert_types=(str))] = Field(10, ge=3, le=50)

            class StructuredConfig(EosCliConfigGen.RouterBgp.PeerGroupsItem, BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                pass

            name: str | None = "WAN-RR-OVERLAY-PEERS"
            """
            Name of peer group.
            """
            password: str | None = None
            """
            Type 7 encrypted password.
            """
            bfd: bool | None = True
            bfd_timers: BfdTimers | None = None
            """
            Specify the BFD timers to override the default values.
            It is recommended to keep BFD total timeout longer than the DPS
            timeout.
            The Default BFD timeout is 10 x 1 seconds and the default DPS timeout is 5 x 1 seconds.
            """
            ttl_maximum_hops: Annotated[int, IntConvert(convert_types=(str))] | None = 1
            structured_config: StructuredConfig | None = None
            """
            Custom structured config added under router_bgp.peer_groups.[name=<name>] for eos_cli_config_gen.
            """

        ipv4_underlay_peers: Ipv4UnderlayPeers | None = None
        mlag_ipv4_underlay_peer: MlagIpv4UnderlayPeer | None = None
        evpn_overlay_peers: EvpnOverlayPeers | None = None
        evpn_overlay_core: EvpnOverlayCore | None = None
        mpls_overlay_peers: MplsOverlayPeers | None = None
        rr_overlay_peers: RrOverlayPeers | None = None
        ipvpn_gateway_peers: IpvpnGatewayPeers | None = None
        wan_overlay_peers: WanOverlayPeers | None = None
        wan_rr_overlay_peers: WanRrOverlayPeers | None = None
        """
        Configuration options for the peer-group created to peer between AutoVPN RRs or CV Pathfinders.
        """

    class ConnectedEndpointsKeysItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        key: str = None
        type: str | None = None
        """
        Type used for documentation.
        """
        description: str | None = None
        """
        Description used for documentation.
        """

    class CoreInterfaces(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class P2pLinksIpPoolsItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str = None
            """
            P2P pool name.
            """
            ipv4_pool: str | None = None
            """
            IPv4 address/Mask.
            """
            prefix_size: Annotated[int, IntConvert(convert_types=(str))] | None = Field(31, ge=8, le=31)
            """
            Subnet mask size.
            """

        class P2pLinksProfilesItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Ptp(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                enabled: bool | None = False
                """
                Enable PTP.
                """

            class PortChannel(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class NodesChildInterfacesItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    node: str = None
                    interfaces: list[str] | None = None
                    """
                    List of node interfaces. Ex.- [ 'node1 interface1', 'node1 interface2' ].
                    """
                    channel_id: Annotated[int, IntConvert(convert_types=(str))] | None = None
                    """
                    Port-Channel ID. If no channel_id is specified, an id is generated from the first switch port in the port channel.
                    """

                mode: str | None = "active"
                nodes_child_interfaces: list[NodesChildInterfacesItem] | None = None

            name: str = None
            """
            P2P profile name. Any variable supported under `p2p_links` can be inherited from a profile.
            """
            id: Annotated[int, IntConvert(convert_types=(str))] | None = None
            """
            Unique id per subnet_summary. Used to calculate ip addresses.
            Required with ip_pool. ID starting from 1.
            """
            speed: str | None = None
            """
            Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`.
            """
            ip_pool: str | None = None
            """
            P2P pool name. IP Pool defined under p2p_links_ip_pools. A /31 will be taken from the pool per P2P link.
            """
            subnet: str | None = None
            """
            IPv4 address/Mask. Subnet used on this P2P link.
            """
            ip: list[str] | None = None
            """
            Specific IP addresses used on this P2P link.
            """
            ipv6_enable: bool | None = False
            """
            Allows turning on ipv6 for the link or profile (also autodetected based on underlay_rfc5549 and
            include_in_underlay_protocol).
            """
            nodes: list[str] | None = None
            """
            Nodes where this link should be configured.
            """
            interfaces: list[str] | None = None
            """
            Interfaces where this link should be configured and Required unless using port-channels.
            """
            field_as: list[Annotated[str, StrConvert(convert_types=(int))]] | None = Field(None, alias="as")
            """
            AS numbers for BGP.
            Required with bgp peering.
            """
            descriptions: list[str] | None = None
            """
            Interface description.
            """
            include_in_underlay_protocol: bool | None = True
            """
            Add this interface to underlay routing protocol.
            """
            isis_hello_padding: bool | None = False
            isis_metric: Annotated[int, IntConvert(convert_types=(str))] | None = None
            isis_circuit_type: Literal["level-1", "level-2", "level-1-2"] | None = None
            isis_authentication_mode: Literal["md5", "text"] | None = None
            isis_authentication_key: str | None = None
            """
            Type-7 encrypted password.
            """
            mpls_ip: bool | None = None
            """
            MPLS parameters. Default value is true if switch.mpls_lsr is true.
            """
            mpls_ldp: bool | None = None
            """
            MPLS parameters. Default value is true for ldp underlay variants, otherwise false.
            """
            mtu: Annotated[int, IntConvert(convert_types=(str))] | None = None
            """
            MTU for this P2P link. Default value same as p2p_uplinks_mtu.
            """
            bfd: bool | None = False
            """
            Enable BFD (only considered for BGP).
            """
            ptp: Ptp | None = None
            """
            PTP parameters.
            """
            sflow: bool | None = None
            """
            Enable sFlow. Overrides `fabric_sflow` setting.
            """
            qos_profile: str | None = None
            """
            QOS service profile.
            """
            macsec_profile: str | None = None
            """
            MAC security profile.
            """
            port_channel: PortChannel | None = None
            """
            Port-channel parameters.
            """
            raw_eos_cli: str | None = None
            """
            EOS CLI rendered directly on the point-to-point interface in the final EOS configuration.
            """
            routing_protocol: Literal["ebgp"] | None = None
            """
            Enables deviation of the routing protocol used on this link from the fabric underlay default.
            - ebgp: Enforce plain IPv4
            BGP peering
            """
            structured_config: dict | None = None
            """
            Custom structured config for interfaces
            Note! The content of this dictionary is _not_ validated by the schema, since it
            can be either ethernet_interfaces or port_channel_interfaces.
            """

        class P2pLinksItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Ptp(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                enabled: bool | None = False
                """
                Enable PTP.
                """

            class PortChannel(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class NodesChildInterfacesItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    node: str = None
                    interfaces: list[str] | None = None
                    """
                    List of node interfaces. Ex.- [ 'node1 interface1', 'node1 interface2' ].
                    """
                    channel_id: Annotated[int, IntConvert(convert_types=(str))] | None = None
                    """
                    Port-Channel ID. If no channel_id is specified, an id is generated from the first switch port in the port channel.
                    """

                mode: str | None = "active"
                nodes_child_interfaces: list[NodesChildInterfacesItem] | None = None

            nodes: list[str] = None
            """
            Nodes where this link should be configured.
            """
            profile: str | None = None
            """
            P2P profile name. Profile defined under p2p_profiles.
            """
            id: Annotated[int, IntConvert(convert_types=(str))] | None = None
            """
            Unique id per subnet_summary. Used to calculate ip addresses.
            Required with ip_pool. ID starting from 1.
            """
            speed: str | None = None
            """
            Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`.
            """
            ip_pool: str | None = None
            """
            P2P pool name. IP Pool defined under p2p_links_ip_pools. A /31 will be taken from the pool per P2P link.
            """
            subnet: str | None = None
            """
            IPv4 address/Mask. Subnet used on this P2P link.
            """
            ip: list[str] | None = None
            """
            Specific IP addresses used on this P2P link.
            """
            ipv6_enable: bool | None = False
            """
            Allows turning on ipv6 for the link or profile (also autodetected based on underlay_rfc5549 and
            include_in_underlay_protocol).
            """
            interfaces: list[str] | None = None
            """
            Interfaces where this link should be configured and Required unless using port-channels.
            """
            field_as: list[Annotated[str, StrConvert(convert_types=(int))]] | None = Field(None, alias="as")
            """
            AS numbers for BGP.
            Required with bgp peering.
            """
            descriptions: list[str] | None = None
            """
            Interface description.
            """
            include_in_underlay_protocol: bool | None = True
            """
            Add this interface to underlay routing protocol.
            """
            isis_hello_padding: bool | None = False
            isis_metric: Annotated[int, IntConvert(convert_types=(str))] | None = None
            isis_circuit_type: Literal["level-1", "level-2", "level-1-2"] | None = None
            isis_authentication_mode: Literal["md5", "text"] | None = None
            isis_authentication_key: str | None = None
            """
            Type-7 encrypted password.
            """
            mpls_ip: bool | None = None
            """
            MPLS parameters. Default value is true if switch.mpls_lsr is true.
            """
            mpls_ldp: bool | None = None
            """
            MPLS parameters. Default value is true for ldp underlay variants, otherwise false.
            """
            mtu: Annotated[int, IntConvert(convert_types=(str))] | None = None
            """
            MTU for this P2P link. Default value same as p2p_uplinks_mtu.
            """
            bfd: bool | None = False
            """
            Enable BFD (only considered for BGP).
            """
            ptp: Ptp | None = None
            """
            PTP parameters.
            """
            sflow: bool | None = None
            """
            Enable sFlow. Overrides `fabric_sflow` setting.
            """
            qos_profile: str | None = None
            """
            QOS service profile.
            """
            macsec_profile: str | None = None
            """
            MAC security profile.
            """
            port_channel: PortChannel | None = None
            """
            Port-channel parameters.
            """
            raw_eos_cli: str | None = None
            """
            EOS CLI rendered directly on the point-to-point interface in the final EOS configuration.
            """
            routing_protocol: Literal["ebgp"] | None = None
            """
            Enables deviation of the routing protocol used on this link from the fabric underlay default.
            - ebgp: Enforce plain IPv4
            BGP peering
            """
            structured_config: dict | None = None
            """
            Custom structured config for interfaces
            Note! The content of this dictionary is _not_ validated by the schema, since it
            can be either ethernet_interfaces or port_channel_interfaces.
            """

        p2p_links_ip_pools: list[P2pLinksIpPoolsItem] | None = None
        p2p_links_profiles: list[P2pLinksProfilesItem] | None = None
        p2p_links: list[P2pLinksItem] | None = None

    class CvPathfinderRegionsItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class SitesItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str = None
            """
            The site name.
            """
            description: str | None = None
            id: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=1, le=10000)
            """
            The site ID must be unique within a zone.
            Given that all the sites are placed in a zone named after the region, the site
            ID must be unique within a region.
            """
            location: str | None = None
            """
            Location as a sring is resolved on Cloudvision.
            """
            site_contact: str | None = None
            site_after_hours_contact: str | None = None

        name: str = None
        """
        The region name.
        """
        description: str | None = None
        id: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=1, le=255)
        """
        The region ID must be unique for the whole WAN deployment.
        """
        sites: list[SitesItem] | None = None
        """
        All sites are placed in a default zone "<region_name>-ZONE" with ID 1.
        """

    class CvTopologyItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class InterfacesItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str = None
            neighbor: str | None = None
            neighbor_interface: str | None = None

        hostname: str = None
        platform: str = None
        interfaces: list[InterfacesItem] = None

    class DefaultInterfacesItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        types: list[str] = None
        """
        List of node type keys.
        """
        platforms: list[str] = None
        """
        List of platform families.
        This is defined as a Python regular expression that matches the full platform type.
        """
        uplink_interfaces: list[str] | None = None
        """
        List of uplink interfaces or uplink interface ranges.
        """
        mlag_interfaces: list[str] | None = None
        """
        List of MLAG interfaces or MLAG interface ranges.
        """
        downlink_interfaces: list[str] | None = None
        """
        List of downlink interfaces or downlink interface ranges.
        """

    class DefaultNodeTypesItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        node_type: str = None
        """
        Resulting node type when regex matches.
        """
        match_hostnames: list[str] = None
        """
        Regular expressions to match against hostnames.
        """

    class Design(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        type: Literal["l3ls-evpn", "mpls", "l2ls"] | None = "l3ls-evpn"
        """
        By setting the design.type variable, the default node-types and templates described in these documents will be used.
        """

    class EosDesignsCustomTemplatesItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Options(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            list_merge: str | None = "append_rp"
            """
            Merge strategy for lists.
            """
            strip_empty_keys: bool | None = True
            """
            Filter out keys from the generated output if value is null/none/undefined.
            """

        template: str = None
        """
        Template file.
        """
        options: Options | None = None
        """
        Template options.
        """

    class EosDesignsDocumentation(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        connected_endpoints: bool | None = False
        """
        Generate fabric-wide documentation for connected endpoints.
        """

    class EventHandlersItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        name: str = None
        """
        Event Handler Name
        """
        action_type: Literal["bash", "increment", "log"] | None = None
        action: str | None = None
        """
        Command to execute
        """
        delay: Annotated[int, IntConvert(convert_types=(str))] | None = None
        """
        Event-handler delay in seconds
        """
        trigger: Literal["on-boot", "on-logging", "on-startup-config"] | None = None
        """
        Configure event trigger condition.
        """
        regex: str | None = None
        """
        Regular expression to use for searching log messages. Required for on-logging trigger
        """
        asynchronous: bool | None = False
        """
        Set the action to be non-blocking.
        """

    class EvpnHostflapDetection(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        enabled: bool | None = True
        """
        If set to false it will disable EVPN host-flap detection.
        """
        threshold: Annotated[int, IntConvert(convert_types=(str))] | None = 5
        """
        Minimum number of MAC moves that indicate a MAC duplication issue.
        """
        window: Annotated[int, IntConvert(convert_types=(str))] | None = 180
        """
        Time (in seconds) to detect a MAC duplication issue.
        """
        expiry_timeout: Annotated[int, IntConvert(convert_types=(str))] | None = None
        """
        Time (in seconds) to purge a MAC duplication issue.
        """

    class EvpnVlanBundlesItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Bgp(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            raw_eos_cli: str | None = None
            """
            EOS cli commands rendered on router_bgp.vlans-aware-bundle.
            """

        name: Annotated[str, StrConvert(convert_types=(int))] = None
        """
        Specify an EVPN vlan-aware-bundle name.
        EVPN vlan-aware-bundles group L2 VLANs and define common settings.
        """
        id: Annotated[int, IntConvert(convert_types=(str))] = None
        """
        "id" may be used for vlan-aware-bundle RD/RT ID so it should not overlap with l2vlan IDs which are not part of this
        bundle.
        See "overlay_rd_type" and "overlay_rt_type" for details.
        """
        rt_override: Annotated[str, StrConvert(convert_types=(int))] | None = None
        """
        By default the MAC VRF bundle RT will be derived from mac_vrf_id_base + bundle_id.
        The rt_override allows us to override
        this value and statically define it.
        rt_override will default to vni_override if set.

        rt_override supports two formats:
        - A single number which will be used in the RT fields instead of mac_vrf_id/mac_vrf_vni (see 'overlay_rt_type' for
        details).
          - A full RT string with colon seperator which will override the full RT.
        """
        rd_override: Annotated[str, StrConvert(convert_types=(int))] | None = None
        """
        By default the MAC VRF bundle RD will be derived from mac_vrf_id_base + bundle_id.
        The rt_override allows us to override
        this value and statically define it.
        rd_override will default to rt_override or vni_override if set.

        rd_override
        supports two formats:
          - A single number which will be used in the RD assigned number field instead of
        mac_vrf_id/mac_vrf_vni (see 'overlay_rd_type' for details).
          - A full RD string with colon seperator which will
        override the full RD.
        """
        evpn_l2_multi_domain: bool | None = None
        """
        Explicitly extend VLAN-Aware Bundle to remote EVPN domains.
        Overrides `<network_services_key>.[].evpn_l2_multi_domain`.
        """
        bgp: Bgp | None = None

    class FabricIpAddressing(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Mlag(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            algorithm: Literal["first_id", "odd_id", "same_subnet"] | None = "first_id"
            """
            This variable defines the Multi-chassis Link Aggregation (MLAG) algorithm used.
            Each MLAG link will have a /31¹ subnet
            with each subnet allocated from the relevant MLAG pool via a calculated offset.
            The offset is calculated using one of
            the following algorithms:
              - first_id: `(mlag_primary_id - 1) * 2` where `mlag_primary_id` is the ID of the first node
            defined under the node_group.
                This allocation method will skip every other /31¹ subnet making it less space
            efficient than `odd_id`.
              - odd_id: `(odd_id - 1) / 2`. Requires the node_group to have a node with an odd ID and a
            node with an even ID.
              - same_subnet: the offset will always be zero.
                This allocation method will cause every MLAG
            link to be addressed with the same /31¹ subnet.
            ¹ The prefix length is configurable with a default of /31.
            """
            ipv4_prefix_length: Annotated[int, IntConvert(convert_types=(str))] | None = Field(31, ge=1, le=31)
            """
            IPv4 prefix length used for MLAG peer-vlan and L3 point-to-point SVIs over the MLAG peer-link.
            """

        class P2pUplinks(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            ipv4_prefix_length: Annotated[int, IntConvert(convert_types=(str))] | None = Field(31, ge=1, le=31)
            """
            IPv4 prefix length used for L3 point-to-point uplinks.
            """

        mlag: Mlag | None = None
        p2p_uplinks: P2pUplinks | None = None

    class FabricSflow(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        uplinks: bool | None = None
        """
        Enable sFlow on all fabric uplinks.
        """
        downlinks: bool | None = None
        """
        Enable sFlow on all fabric downlinks.
        """
        endpoints: bool | None = None
        """
        Enable sFlow on all endpoints ports.
        """
        l3_edge: bool | None = None
        """
        Enable sFlow on all p2p_links defined under l3_edge.
        """
        core_interfaces: bool | None = None
        """
        Enable sFlow on all p2p_links defined under core_interfaces.
        """
        mlag_interfaces: bool | None = None
        """
        Enable sFlow on all MLAG peer interfaces.
        """

    class FlowTrackingSettings(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class RecordExport(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            on_inactive_timeout: Annotated[int, IntConvert(convert_types=(str))] | None = Field(70000, ge=3000, le=900000)
            """
            Flow record inactive export timeout in milliseconds.
            """
            on_interval: Annotated[int, IntConvert(convert_types=(str))] | None = Field(300000, ge=1000, le=36000000)
            """
            Flow record export interval in milliseconds.
            """

        class Exporter(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str | None = "CV-TELEMETRY"
            """
            Exporter Name.
            """
            template_interval: Annotated[int, IntConvert(convert_types=(str))] | None = Field(3600000, ge=5000, le=3600000)
            """
            Template interval in milliseconds.
            """

        flow_tracker_name: str | None = "FLOW-TRACKER"
        """
        Flow Tracker Name.
        """
        record_export: RecordExport | None = None
        exporter: Exporter | None = None

    class GenerateCvTags(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class InterfaceTagsItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str = None
            """
            Tag name to be assigned to generated tags.
            """
            data_path: str | None = None
            """
            Structured config field/key path to be used to find the value for the tag. Dot notation is supported to reference values
            inside dictionaries.
            For Example: 'data_path: channel_group.id' would set the tag with the value of the channel id of
            the interface. If there is no channel id, the tag is not created.
            `data_path` is ignored if `value` is set.
            """
            value: str | None = None
            """
            Value to be assigned to the tag.
            """

        class DeviceTagsItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str = None
            """
            Tag name to be assigned to generated tags.
            """
            data_path: str | None = None
            """
            Structured config field/key path to be used to find the value for the tag. Dot notation is supported to reference values
            inside dictionaries.
            For Example: 'data_path: router_bfd.multihop.interval' would set the tag with the value of the
            interval for multihop bfd. If this value is not specified in the structured config, the tag is not created.
            `data_path`
            is ignored if `value` is set.
            """
            value: str | None = None
            """
            Value to be assigned to the tag.
            """

        topology_hints: bool | None = False
        """
        Enable the generation of CloudVision Topology Tags (hints).
        """
        interface_tags: list[InterfaceTagsItem] | None = None
        """
        List of interface tags that should be generated.
        """
        device_tags: list[DeviceTagsItem] | None = None
        """
        List of device tags that should be generated.
        """

    class HardwareCounters(EosCliConfigGen.HardwareCounters, BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        pass

    class InternalVlanOrder(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Range(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            beginning: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=2, le=4094)
            """
            First VLAN ID.
            """
            ending: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=2, le=4094)
            """
            Last VLAN ID.
            """

        allocation: Literal["ascending", "descending"] = None
        range: Range | None = None

    class Ipv4AclsItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class EntriesItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            source: str | None = None
            """
            This field supports substitution of the fields "interface_ip" and "peer_ip".
            Alternatively it can be set with a static
            value of "any", "<ip>/<mask>" or "<ip>".
            "<ip>" without a mask means host.
            Required except for remarks.
            """
            destination: str | None = None
            """
            This field supports substitution of the fields "interface_ip" and "peer_ip".
            Alternatively it can be set with a static
            value of "any", "<ip>/<mask>" or "<ip>".
            "<ip>" without a mask means host.
            Required except for remarks.
            """
            sequence: Annotated[int, IntConvert(convert_types=(str))] | None = None
            """
            ACL entry sequence number.
            """
            remark: str | None = None
            """
            Comment up to 100 characters.
            If remark is defined, other keys in the ACL entry will be ignored.
            """
            action: Literal["permit", "deny"] | None = None
            """
            ACL action.
            Required except for remarks.
            """
            protocol: str | None = None
            """
            "ip", "tcp", "udp", "icmp" or other protocol name or number.
            Required except for remarks.
            """
            source_ports_match: Literal["eq", "gt", "lt", "neq", "range"] | None = "eq"
            source_ports: list[Annotated[str, StrConvert(convert_types=(int))]] | None = None
            destination_ports_match: Literal["eq", "gt", "lt", "neq", "range"] | None = "eq"
            destination_ports: list[Annotated[str, StrConvert(convert_types=(int))]] | None = None
            tcp_flags: list[str] | None = None
            fragments: bool | None = None
            """
            Match non-head fragment packets.
            """
            log: bool | None = None
            """
            Log matches against this rule.
            """
            ttl: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=255)
            """
            TTL value
            """
            ttl_match: Literal["eq", "gt", "lt", "neq"] | None = "eq"
            icmp_type: Annotated[str, StrConvert(convert_types=(int))] | None = None
            """
            Message type name/number for ICMP packets.
            """
            icmp_code: Annotated[str, StrConvert(convert_types=(int))] | None = None
            """
            Message code for ICMP packets.
            """
            nexthop_group: str | None = None
            """
            nexthop-group name.
            """
            tracked: bool | None = None
            """
            Match packets in existing ICMP/UDP/TCP connections.
            """
            dscp: Annotated[str, StrConvert(convert_types=(int))] | None = None
            """
            DSCP value or name.
            """
            vlan_number: Annotated[int, IntConvert(convert_types=(str))] | None = None
            vlan_inner: bool | None = False
            vlan_mask: str | None = None
            """
            0x000-0xFFF VLAN mask.
            """

        name: Annotated[str, StrConvert(convert_types=(int))] = None
        """
        Access-list name.
        When using substitution for any fields, the interface name will be appended to the ACL name.
        """
        entries: list[EntriesItem] = None
        """
        ACL Entries.
        """
        counters_per_entry: bool | None = None

    class IsisTiLfa(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        enabled: bool | None = False
        protection: Literal["link", "node"] | None = None
        local_convergence_delay: Annotated[int, IntConvert(convert_types=(str))] | None = 10000
        """
        Local convergence delay in milliseconds.
        """

    class L3Edge(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class P2pLinksIpPoolsItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str = None
            """
            P2P pool name.
            """
            ipv4_pool: str | None = None
            """
            IPv4 address/Mask.
            """
            prefix_size: Annotated[int, IntConvert(convert_types=(str))] | None = Field(31, ge=8, le=31)
            """
            Subnet mask size.
            """

        class P2pLinksProfilesItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Ptp(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                enabled: bool | None = False
                """
                Enable PTP.
                """

            class PortChannel(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class NodesChildInterfacesItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    node: str = None
                    interfaces: list[str] | None = None
                    """
                    List of node interfaces. Ex.- [ 'node1 interface1', 'node1 interface2' ].
                    """
                    channel_id: Annotated[int, IntConvert(convert_types=(str))] | None = None
                    """
                    Port-Channel ID. If no channel_id is specified, an id is generated from the first switch port in the port channel.
                    """

                mode: str | None = "active"
                nodes_child_interfaces: list[NodesChildInterfacesItem] | None = None

            name: str = None
            """
            P2P profile name. Any variable supported under `p2p_links` can be inherited from a profile.
            """
            id: Annotated[int, IntConvert(convert_types=(str))] | None = None
            """
            Unique id per subnet_summary. Used to calculate ip addresses.
            Required with ip_pool. ID starting from 1.
            """
            speed: str | None = None
            """
            Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`.
            """
            ip_pool: str | None = None
            """
            P2P pool name. IP Pool defined under p2p_links_ip_pools. A /31 will be taken from the pool per P2P link.
            """
            subnet: str | None = None
            """
            IPv4 address/Mask. Subnet used on this P2P link.
            """
            ip: list[str] | None = None
            """
            Specific IP addresses used on this P2P link.
            """
            ipv6_enable: bool | None = False
            """
            Allows turning on ipv6 for the link or profile (also autodetected based on underlay_rfc5549 and
            include_in_underlay_protocol).
            """
            nodes: list[str] | None = None
            """
            Nodes where this link should be configured.
            """
            interfaces: list[str] | None = None
            """
            Interfaces where this link should be configured and Required unless using port-channels.
            """
            field_as: list[Annotated[str, StrConvert(convert_types=(int))]] | None = Field(None, alias="as")
            """
            AS numbers for BGP.
            Required with bgp peering.
            """
            descriptions: list[str] | None = None
            """
            Interface description.
            """
            include_in_underlay_protocol: bool | None = True
            """
            Add this interface to underlay routing protocol.
            """
            isis_hello_padding: bool | None = False
            isis_metric: Annotated[int, IntConvert(convert_types=(str))] | None = None
            isis_circuit_type: Literal["level-1", "level-2", "level-1-2"] | None = None
            isis_authentication_mode: Literal["md5", "text"] | None = None
            isis_authentication_key: str | None = None
            """
            Type-7 encrypted password.
            """
            mpls_ip: bool | None = None
            """
            MPLS parameters. Default value is true if switch.mpls_lsr is true.
            """
            mpls_ldp: bool | None = None
            """
            MPLS parameters. Default value is true for ldp underlay variants, otherwise false.
            """
            mtu: Annotated[int, IntConvert(convert_types=(str))] | None = None
            """
            MTU for this P2P link. Default value same as p2p_uplinks_mtu.
            """
            bfd: bool | None = False
            """
            Enable BFD (only considered for BGP).
            """
            ptp: Ptp | None = None
            """
            PTP parameters.
            """
            sflow: bool | None = None
            """
            Enable sFlow. Overrides `fabric_sflow` setting.
            """
            qos_profile: str | None = None
            """
            QOS service profile.
            """
            macsec_profile: str | None = None
            """
            MAC security profile.
            """
            port_channel: PortChannel | None = None
            """
            Port-channel parameters.
            """
            raw_eos_cli: str | None = None
            """
            EOS CLI rendered directly on the point-to-point interface in the final EOS configuration.
            """
            routing_protocol: Literal["ebgp"] | None = None
            """
            Enables deviation of the routing protocol used on this link from the fabric underlay default.
            - ebgp: Enforce plain IPv4
            BGP peering
            """
            structured_config: dict | None = None
            """
            Custom structured config for interfaces
            Note! The content of this dictionary is _not_ validated by the schema, since it
            can be either ethernet_interfaces or port_channel_interfaces.
            """

        class P2pLinksItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Ptp(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                enabled: bool | None = False
                """
                Enable PTP.
                """

            class PortChannel(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class NodesChildInterfacesItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    node: str = None
                    interfaces: list[str] | None = None
                    """
                    List of node interfaces. Ex.- [ 'node1 interface1', 'node1 interface2' ].
                    """
                    channel_id: Annotated[int, IntConvert(convert_types=(str))] | None = None
                    """
                    Port-Channel ID. If no channel_id is specified, an id is generated from the first switch port in the port channel.
                    """

                mode: str | None = "active"
                nodes_child_interfaces: list[NodesChildInterfacesItem] | None = None

            nodes: list[str] = None
            """
            Nodes where this link should be configured.
            """
            profile: str | None = None
            """
            P2P profile name. Profile defined under p2p_profiles.
            """
            id: Annotated[int, IntConvert(convert_types=(str))] | None = None
            """
            Unique id per subnet_summary. Used to calculate ip addresses.
            Required with ip_pool. ID starting from 1.
            """
            speed: str | None = None
            """
            Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`.
            """
            ip_pool: str | None = None
            """
            P2P pool name. IP Pool defined under p2p_links_ip_pools. A /31 will be taken from the pool per P2P link.
            """
            subnet: str | None = None
            """
            IPv4 address/Mask. Subnet used on this P2P link.
            """
            ip: list[str] | None = None
            """
            Specific IP addresses used on this P2P link.
            """
            ipv6_enable: bool | None = False
            """
            Allows turning on ipv6 for the link or profile (also autodetected based on underlay_rfc5549 and
            include_in_underlay_protocol).
            """
            interfaces: list[str] | None = None
            """
            Interfaces where this link should be configured and Required unless using port-channels.
            """
            field_as: list[Annotated[str, StrConvert(convert_types=(int))]] | None = Field(None, alias="as")
            """
            AS numbers for BGP.
            Required with bgp peering.
            """
            descriptions: list[str] | None = None
            """
            Interface description.
            """
            include_in_underlay_protocol: bool | None = True
            """
            Add this interface to underlay routing protocol.
            """
            isis_hello_padding: bool | None = False
            isis_metric: Annotated[int, IntConvert(convert_types=(str))] | None = None
            isis_circuit_type: Literal["level-1", "level-2", "level-1-2"] | None = None
            isis_authentication_mode: Literal["md5", "text"] | None = None
            isis_authentication_key: str | None = None
            """
            Type-7 encrypted password.
            """
            mpls_ip: bool | None = None
            """
            MPLS parameters. Default value is true if switch.mpls_lsr is true.
            """
            mpls_ldp: bool | None = None
            """
            MPLS parameters. Default value is true for ldp underlay variants, otherwise false.
            """
            mtu: Annotated[int, IntConvert(convert_types=(str))] | None = None
            """
            MTU for this P2P link. Default value same as p2p_uplinks_mtu.
            """
            bfd: bool | None = False
            """
            Enable BFD (only considered for BGP).
            """
            ptp: Ptp | None = None
            """
            PTP parameters.
            """
            sflow: bool | None = None
            """
            Enable sFlow. Overrides `fabric_sflow` setting.
            """
            qos_profile: str | None = None
            """
            QOS service profile.
            """
            macsec_profile: str | None = None
            """
            MAC security profile.
            """
            port_channel: PortChannel | None = None
            """
            Port-channel parameters.
            """
            raw_eos_cli: str | None = None
            """
            EOS CLI rendered directly on the point-to-point interface in the final EOS configuration.
            """
            routing_protocol: Literal["ebgp"] | None = None
            """
            Enables deviation of the routing protocol used on this link from the fabric underlay default.
            - ebgp: Enforce plain IPv4
            BGP peering
            """
            structured_config: dict | None = None
            """
            Custom structured config for interfaces
            Note! The content of this dictionary is _not_ validated by the schema, since it
            can be either ethernet_interfaces or port_channel_interfaces.
            """

        p2p_links_ip_pools: list[P2pLinksIpPoolsItem] | None = None
        p2p_links_profiles: list[P2pLinksProfilesItem] | None = None
        p2p_links: list[P2pLinksItem] | None = None

    class L3InterfaceProfilesItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class StaticRoutesItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            prefix: str = None
            """
            IPv4_network/Mask
            """

        class StructuredConfig(EosCliConfigGen.EthernetInterfacesItem, BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            pass

        profile: str = None
        """
        L3 interface profile name. Any variable supported under `l3_interfaces` can be inherited from a profile.
        """
        name: str | None = Field(None, pattern=r"Ethernet[\d/]+(.[\d]+)?")
        """
        Ethernet interface name like 'Ethernet2' or subinterface name like 'Ethernet2.42'
        For a subinterface, the parent
        physical interface is automatically created.
        """
        description: str | None = None
        """
        Interface description.
        If not set a default description will be configured with '[<peer>[ <peer_interface>]]'
        """
        ip_address: str | None = None
        """
        Node IPv4 address/Mask or 'dhcp'.
        """
        dhcp_ip: str | None = None
        """
        When the `ip_address` is `dhcp`, this optional field allows to indicate the expected
        IPv4 address (without mask) to be
        allocated on the interface if known.
        This is not rendered in the configuration but can be used for substitution of
        'interface_ip' in the Access-list
        set under `ipv4_acl_in` and `ipv4_acl_out`.
        """
        public_ip: str | None = None
        """
        Node IPv4 address (no mask).

        This is used to get the public IP (if known) when the device is behind NAT.
        This is only
        used for `wan_rr` routers (AutoVPN RRs and Pathfinders) to determine the Public IP
        with the following preference:
        `wan_route_servers.path_groups.interfaces.ip_address`
              -> `l3_interfaces.public_ip`
                  ->
        `l3_interfaces.ip_address`

        The determined Public IP is used by WAN routers when peering with this interface.
        """
        encapsulation_dot1q_vlan: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=4094)
        """
        For subinterfaces the dot1q vlan is derived from the interface name by default, but can also be specified.
        """
        dhcp_accept_default_route: bool | None = True
        """
        Accept a default route from DHCP if `ip_address` is set to `dhcp`.
        """
        enabled: bool | None = True
        """
        Enable or Shutdown the interface.
        """
        speed: str | None = None
        """
        Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`.
        """
        peer: str | None = None
        """
        The peer device name. Used for description and documentation
        """
        peer_interface: str | None = None
        """
        The peer device interface. Used for description and documentation
        """
        peer_ip: str | None = None
        """
        The peer device IPv4 address (no mask). Used as default route gateway if `set_default_route` is true and `ip` is an IP
        address.
        """
        ipv4_acl_in: Annotated[str, StrConvert(convert_types=(int))] | None = None
        """
        Name of the IPv4 access-list to be assigned in the ingress direction.
        The access-list must be defined under `ipv4_acls`.
        Required for all WAN interfaces (`wan_carrier` is set) unless the carrier is marked as 'trusted' under `wan_carriers`.
        """
        ipv4_acl_out: Annotated[str, StrConvert(convert_types=(int))] | None = None
        """
        Name of the IPv4 Access-list to be assigned in the egress direction.
        The access-list must be defined under `ipv4_acls`.
        """
        static_routes: list[StaticRoutesItem] | None = Field(None, min_length=1)
        """
        Configure IPv4 static routes pointing to `peer_ip`.
        """
        qos_profile: str | None = None
        """
        QOS service profile.
        """
        wan_carrier: str | None = None
        """
        The WAN carrier this interface is connected to.
        This is used to infer the path-groups in which this interface should be
        configured.
        Unless the carrier is marked as 'trusted' under `wan_carriers`, `ipv4_acl_in` is also required on all WAN
        interfaces.
        """
        wan_circuit_id: Annotated[str, StrConvert(convert_types=(int))] | None = None
        """
        The WAN circuit ID for this interface.
        This is not rendered in the configuration but used for WAN designs.
        """
        connected_to_pathfinder: bool | None = True
        """
        For a WAN interface (`wan_carrier` is set), allow to disable the static tunnel towards Pathfinders.
        """
        raw_eos_cli: str | None = None
        """
        EOS CLI rendered directly on the interface in the final EOS configuration.
        """
        structured_config: StructuredConfig | None = None
        """
        Custom structured config for the Ethernet interface.
        """

    class LocalUsersItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        name: str = None
        """
        Username
        """
        disabled: bool | None = None
        """
        If true, the user will be removed and all other settings are ignored.
        Useful for removing the default "admin" user.
        """
        privilege: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=15)
        """
        Initial privilege level with local EXEC authorization.
        """
        role: str | None = None
        """
        EOS RBAC Role to be assigned to the user such as "network-admin" or "network-operator"
        """
        sha512_password: str | None = None
        """
        SHA512 Hash of Password
        Must be the hash of the password. By default EOS salts the password with the username, so the
        simplest is to generate the hash on an EOS device using the same username.
        """
        no_password: bool | None = None
        """
        If set a password will not be configured for this user. "sha512_password" MUST not be defined for this user.
        """
        ssh_key: str | None = None
        secondary_ssh_key: str | None = None
        shell: Literal["/bin/bash", "/bin/sh", "/sbin/nologin"] | None = None
        """
        Specify shell for the user
        """

    class MacAddressTable(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        aging_time: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=1000000)
        """
        Aging time in seconds 10-1000000.
        Enter 0 to disable aging.
        """

    class ManagementEapi(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        enable_http: bool | None = False
        enable_https: bool | None = True
        default_services: bool | None = None

    class MlagIbgpPeeringVrfs(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        base_vlan: Annotated[int, IntConvert(convert_types=(str))] | None = Field(3000, ge=1, le=4093)

    class NetworkPortsItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Flowcontrol(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            received: Literal["received", "send", "on"] | None = None

        class Ptp(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            enabled: bool | None = False
            endpoint_role: Literal["bmca", "default", "follower"] | None = "follower"
            profile: Literal["aes67", "aes67-r16-2016", "smpte2059-2"] | None = "aes67-r16-2016"

        class LinkTracking(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            enabled: bool | None = None
            name: str | None = None
            """
            Tracking group name.
            The default group name is taken from fabric variable of the switch, `link_tracking.groups[0].name`
            with default value being "LT_GROUP1".
            Optional if default link_tracking settings are configured on the node.
            """

        class Dot1x(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Pae(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                mode: Literal["authenticator"] | None = None

            class AuthenticationFailure(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                action: Literal["allow", "drop"] | None = None
                allow_vlan: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=4094)

            class HostMode(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                mode: Literal["multi-host", "single-host"] | None = None
                multi_host_authenticated: bool | None = None

            class MacBasedAuthentication(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                enabled: bool | None = None
                always: bool | None = None
                host_mode_common: bool | None = None

            class Timeout(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                idle_host: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=10, le=65535)
                quiet_period: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)
                reauth_period: Annotated[str, StrConvert(convert_types=(int))] | None = None
                """
                Range 60-4294967295 or "server".
                """
                reauth_timeout_ignore: bool | None = None
                tx_period: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)

            class Unauthorized(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                access_vlan_membership_egress: bool | None = None
                native_vlan_membership_egress: bool | None = None

            port_control: Literal["auto", "force-authorized", "force-unauthorized"] | None = None
            port_control_force_authorized_phone: bool | None = None
            reauthentication: bool | None = None
            pae: Pae | None = None
            authentication_failure: AuthenticationFailure | None = None
            host_mode: HostMode | None = None
            mac_based_authentication: MacBasedAuthentication | None = None
            timeout: Timeout | None = None
            reauthorization_request_limit: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=10)
            unauthorized: Unauthorized | None = None

        class Poe(EosCliConfigGen.EthernetInterfacesItem.Poe, BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            pass

        class StormControl(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class All(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                level: Annotated[str, StrConvert(convert_types=(int, float))] | None = None
                """
                Configure maximum storm-control level.
                """
                unit: Literal["percent", "pps"] | None = "percent"
                """
                Optional variable and is hardware dependent.
                """

            class Broadcast(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                level: Annotated[str, StrConvert(convert_types=(int, float))] | None = None
                """
                Configure maximum storm-control level.
                """
                unit: Literal["percent", "pps"] | None = "percent"
                """
                Optional variable and is hardware dependent.
                """

            class Multicast(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                level: Annotated[str, StrConvert(convert_types=(int, float))] | None = None
                """
                Configure maximum storm-control level.
                """
                unit: Literal["percent", "pps"] | None = "percent"
                """
                Optional variable and is hardware dependent.
                """

            class UnknownUnicast(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                level: Annotated[str, StrConvert(convert_types=(int, float))] | None = None
                """
                Configure maximum storm-control level.
                """
                unit: Literal["percent", "pps"] | None = "percent"
                """
                Optional variable and is hardware dependent.
                """

            all: All | None = None
            broadcast: Broadcast | None = None
            multicast: Multicast | None = None
            unknown_unicast: UnknownUnicast | None = None

        class MonitorSessionsItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class SourceSettings(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class AccessGroup(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    type: Literal["ip", "ipv6", "mac"] | None = None
                    name: str | None = None
                    """
                    ACL name.
                    """
                    priority: Annotated[int, IntConvert(convert_types=(str))] | None = None

                direction: Literal["rx", "tx", "both"] | None = None
                access_group: AccessGroup | None = None

            class SessionSettings(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class AccessGroup(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    type: Literal["ip", "ipv6", "mac"] | None = None
                    name: str | None = None
                    """
                    ACL name.
                    """

                class Truncate(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    enabled: bool | None = None
                    size: Annotated[int, IntConvert(convert_types=(str))] | None = None
                    """
                    Size in bytes
                    """

                encapsulation_gre_metadata_tx: bool | None = None
                header_remove_size: Annotated[int, IntConvert(convert_types=(str))] | None = None
                """
                Number of bytes to remove from header.
                """
                access_group: AccessGroup | None = None
                rate_limit_per_ingress_chip: str | None = None
                """
                Ratelimit and unit as string.
                Examples:
                  "100000 bps"
                  "100 kbps"
                  "10 mbps"
                """
                rate_limit_per_egress_chip: str | None = None
                """
                Ratelimit and unit as string.
                Examples:
                  "100000 bps"
                  "100 kbps"
                  "10 mbps"
                """
                sample: Annotated[int, IntConvert(convert_types=(str))] | None = None
                truncate: Truncate | None = None

            name: str = None
            """
            Session name.
            """
            role: Literal["source", "destination"] | None = None
            source_settings: SourceSettings | None = None
            session_settings: SessionSettings | None = None
            """
            Session settings are defined per session name.
            Different session_settings for the same session name will be
            combined/merged.
            """

        class EthernetSegment(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            short_esi: str = None
            """
            In format xxxx:xxxx:xxxx or "auto".
            Define a manual short-esi (be careful using this on profiles) or set the value to
            "auto" to automatically generate the value.
            Please see the notes under "EVPN A/A ESI dual and single-attached endpoint
            scenarios" before setting `short_esi: auto`.
            """
            redundancy: Literal["all-active", "single-active"] | None = None
            """
            If omitted, Port-Channels use the EOS default of all-active.
            If omitted, Ethernet interfaces are configured as single-
            active.
            """
            designated_forwarder_algorithm: Literal["auto", "modulus", "preference"] | None = None
            """
            Configure DF algorithm and preferences.
            - auto: Use preference-based algorithm and assign preference based on position
            of device in the 'switches' list,
              e.g., assuming a list of three switches, this would assign a preference of 200 to
            the first switch, 100 to the 2nd, and 0 to the third.
            - preference: Set preference for each switch manually using
            designated_forwarder_preferences key.
            - modulus: Use the default modulus-based algorithm.
            If omitted, Port-Channels use
            the EOS default of modulus.
            If omitted, Ethernet interfaces default to the 'auto' mechanism detailed above.
            """
            designated_forwarder_preferences: list[Annotated[int, IntConvert(convert_types=(str))]] | None = None
            """
            Manual preference as described above, required only for preference algorithm.
            """
            dont_preempt: bool | None = None
            """
            Disable preemption for single-active forwarding when auto/manual DF preference is configured.
            """

        class PortChannel(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class LacpFallback(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Individual(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    profile: str | None = None
                    """
                    Port-profile name to inherit configuration.
                    """

                mode: Literal["static", "individual"] | None = None
                """
                Either static or individual mode is supported.
                If the mode is set to "individual" the "individual.profile" setting must
                be defined.
                """
                individual: Individual | None = None
                """
                Define parameters for port-channel member interfaces. Applies only if LACP fallback is set to "individual".
                """
                timeout: Annotated[int, IntConvert(convert_types=(str))] | None = None
                """
                Timeout in seconds. EOS default is 90 seconds.
                """

            class LacpTimer(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                mode: Literal["normal", "fast"] | None = None
                """
                LACP mode for interface members.
                """
                multiplier: Annotated[int, IntConvert(convert_types=(str))] | None = None
                """
                Number of LACP BPDUs lost before deeming the peer down. EOS default is 3.
                """

            class SubinterfacesItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class EncapsulationVlan(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    client_dot1q: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=4094)

                number: Annotated[int, IntConvert(convert_types=(str))] | None = None
                """
                Subinterface number
                """
                short_esi: str | None = None
                """
                In format xxxx:xxxx:xxxx or "auto"
                Required for multihomed port-channels with subinterfaces
                """
                vlan_id: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=4094)
                """
                VLAN ID to bridge.
                Default is subinterface number.
                """
                encapsulation_vlan: EncapsulationVlan | None = None
                """
                Client VLAN ID encapsulation.
                Default is subinterface number.
                """

            class StructuredConfig(EosCliConfigGen.PortChannelInterfacesItem, BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                pass

            mode: Literal["active", "passive", "on"] | None = None
            """
            Port-Channel Mode.
            """
            channel_id: Annotated[int, IntConvert(convert_types=(str))] | None = None
            """
            Port-Channel ID.
            If no channel_id is specified, an id is generated from the first switch port in the port channel.
            """
            description: str | None = None
            """
            By default the description is built leveraging `<peer>` name or `adapter.description` when defined.
            When this key is
            defined, it will append its content to the physical port description.
            """
            enabled: bool | None = True
            """
            Port-Channel administrative state.
            Setting to false will set port to 'shutdown' in intended configuration.
            """
            short_esi: str | None = None
            """
            In format xxxx:xxxx:xxxx or "auto".
            """
            lacp_fallback: LacpFallback | None = None
            """
            LACP fallback configuration.
            """
            lacp_timer: LacpTimer | None = None
            """
            LACP timer configuration. Applies only when Port-channel mode is not "on".
            """
            subinterfaces: list[SubinterfacesItem] | None = None
            """
            Port-Channel L2 Subinterfaces
            Subinterfaces are only supported on routed port-channels, which means they cannot be
            configured on MLAG port-channels.
            Setting short_esi: auto generates the short_esi automatically using a hash of
            configuration elements.
            Please see the notes under "EVPN A/A ESI dual-attached endpoint scenario" before setting
            short_esi: auto.
            """
            raw_eos_cli: str | None = None
            """
            EOS CLI rendered directly on the port-channel interface in the final EOS configuration.
            """
            structured_config: StructuredConfig | None = None
            """
            Custom structured config added under port_channel_interfaces.[name=<interface>] for eos_cli_config_gen.
            """

        class StructuredConfig(EosCliConfigGen.EthernetInterfacesItem, BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            pass

        switches: list[str] | None = None
        """
        Regex matching the full hostname of one or more switches.
        The regular expression must match the full hostname.
        """
        switch_ports: list[str] | None = None
        """
        List of ranges using AVD range_expand syntax.
        For example:

        switch_ports:
          - Ethernet1
          - Ethernet2-48

        All
        switch_ports ranges are expanded into individual port configurations.

        For more details and examples of the
        `range_expand` syntax, see the [`arista.avd.range_expand`
        documentation](../../../docs/plugins/Filter_plugins/range_expand.md).
        """
        description: str | None = None
        """
        Description to be used on all ports.
        """
        speed: str | None = None
        """
        Set adapter speed in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`.
        If not
        specified speed will be auto.
        """
        profile: str | None = None
        """
        Port-profile name to inherit configuration.
        """
        enabled: bool | None = True
        """
        Administrative state, setting to false will set the port to 'shutdown' in the intended configuration.
        """
        mode: Literal["access", "dot1q-tunnel", "trunk", "trunk phone"] | None = None
        """
        Interface mode.
        """
        mtu: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=68, le=65535)
        l2_mtu: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=68, le=65535)
        """
        "l2_mtu" should only be defined for platforms supporting the "l2 mtu" CLI
        """
        l2_mru: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=68, le=65535)
        """
        "l2_mru" should only be defined for platforms supporting the "l2 mru" CLI
        """
        native_vlan: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=4094)
        """
        Native VLAN for a trunk port.
        If both `native_vlan` and `native_vlan_tag`, `native_vlan_tag` takes precedence.
        """
        native_vlan_tag: bool | None = False
        """
        If both `native_vlan` and `native_vlan_tag`, `native_vlan_tag` takes precedence.
        """
        phone_vlan: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=4094)
        """
        Phone VLAN for a mode `trunk phone` port.
        Requires `mode: trunk phone` to be set.
        """
        phone_trunk_mode: Literal["tagged", "untagged", "tagged phone", "untagged phone"] | None = None
        """
        Specify if the phone traffic is tagged or untagged.
        If both data and phone traffic are untagged, MAC-Based VLAN
        Assignment (MBVA) is used, if supported by the model of switch.
        """
        trunk_groups: list[str] | None = None
        """
        Required with `enable_trunk_groups: true`.
        Trunk Groups are used for limiting VLANs on trunk ports to VLANs with the
        same Trunk Group.
        """
        vlans: Annotated[str, StrConvert(convert_types=(int))] | None = None
        """
        Interface VLANs - if not set, the EOS default is that all VLANs are allowed for trunk ports, and VLAN 1 will be used for
        access ports.
        """
        spanning_tree_portfast: Literal["edge", "network"] | None = None
        spanning_tree_bpdufilter: Annotated[Literal["enabled", "disabled", "True", "False", "true", "false"], StrConvert(convert_types=(bool))] | None = None
        spanning_tree_bpduguard: Annotated[Literal["enabled", "disabled", "True", "False", "true", "false"], StrConvert(convert_types=(bool))] | None = None
        flowcontrol: Flowcontrol | None = None
        qos_profile: str | None = None
        """
        QOS profile name
        """
        ptp: Ptp | None = None
        """
        The global PTP profile parameters will be applied to all connected endpoints where `ptp` is manually enabled.
        `ptp role
        master` is set to ensure control over the PTP topology.
        """
        sflow: bool | None = None
        """
        Configures sFlow on the interface. Overrides `fabric_sflow` setting.
        """
        link_tracking: LinkTracking | None = None
        """
        Configure the downstream interfaces of a respective Link Tracking Group.
        If `port_channel` is defined in an adapter,
        then the port-channel interface is configured to be the downstream.
        Else all the ethernet interfaces will be configured
        as downstream -> to configure single-active EVPN multihomed networks.
        """
        dot1x: Dot1x | None = None
        """
        802.1x
        """
        poe: Poe | None = None
        """
        Power Over Ethernet settings applied on port. Only configured if platform supports PoE.
        """
        storm_control: StormControl | None = None
        """
        Storm control settings applied on port toward the endpoint.
        """
        monitor_sessions: list[MonitorSessionsItem] | None = None
        """
        Used to define switchports as source or destination for monitoring sessions.
        """
        ethernet_segment: EthernetSegment | None = None
        """
        Settings for all or single-active EVPN multihoming.
        """
        port_channel: PortChannel | None = None
        """
        Used for port-channel adapter.
        """
        validate_state: bool | None = None
        """
        Set to false to disable interface validation by the `eos_validate_state` role.
        """
        raw_eos_cli: str | None = None
        """
        EOS CLI rendered directly on the ethernet interface in the final EOS configuration.
        """
        structured_config: StructuredConfig | None = None
        """
        Custom structured config added under ethernet_interfaces.[name=<interface>] for eos_cli_config_gen.
        """

    class NetworkServicesKeysItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        name: str = None

    class NodeTypeKeysItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class NetworkServices(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            l1: bool | None = False
            """
            ??
            """
            l2: bool | None = False
            """
            Vlans
            """
            l3: bool | None = False
            """
            VRFs, SVIs (if l2 is true).
            Only supported with underlay_router.
            """

        class IpAddressing(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            python_module: str | None = None
            """
            Custom Python Module to import for IP addressing.
            """
            python_class_name: str | None = None
            """
            Name of Custom Python Class to import for IP addressing.
            """
            router_id: str | None = None
            """
            Path to Custom J2 template.
            """
            router_id_ipv6: str | None = None
            """
            Path to Custom J2 template.
            """
            mlag_ip_primary: str | None = None
            """
            Path to Custom J2 template.
            """
            mlag_ip_secondary: str | None = None
            """
            Path to Custom J2 template.
            """
            mlag_l3_ip_primary: str | None = None
            """
            Path to Custom J2 template.
            """
            mlag_l3_ip_secondary: str | None = None
            """
            Path to Custom J2 template.
            """
            mlag_ibgp_peering_ip_primary: str | None = None
            """
            Path to Custom J2 template.
            """
            mlag_ibgp_peering_ip_secondary: str | None = None
            """
            Path to Custom J2 template.
            """
            p2p_uplinks_ip: str | None = None
            """
            Path to Custom J2 template.
            """
            p2p_uplinks_peer_ip: str | None = None
            """
            Path to Custom J2 template.
            """
            vtep_ip_mlag: str | None = None
            """
            Path to Custom J2 template.
            """
            vtep_ip: str | None = None
            """
            Path to Custom J2 template.
            """

        class InterfaceDescriptions(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            python_module: str | None = None
            """
            Custom Python Module to import for interface descriptions.
            """
            python_class_name: str | None = None
            """
            Name of Custom Python Class to import for interface descriptions.
            """
            underlay_ethernet_interfaces: str | None = None
            """
            Path to Custom J2 template.
            """
            underlay_port_channel_interfaces: str | None = None
            """
            Path to Custom J2 template.
            """
            mlag_ethernet_interfaces: str | None = None
            """
            Path to Custom J2 template.
            """
            mlag_port_channel_interfaces: str | None = None
            """
            Path to Custom J2 template.
            """
            connected_endpoints_ethernet_interfaces: str | None = None
            """
            Path to Custom J2 template.
            """
            connected_endpoints_port_channel_interfaces: str | None = None
            """
            Path to Custom J2 template.
            """
            overlay_loopback_interface: str | None = None
            """
            Path to Custom J2 template.
            """
            vtep_loopback_interface: str | None = None
            """
            Path to Custom J2 template.
            """

        key: str = None
        type: str | None = None
        """
        Type value matching this node_type_key.
        """
        connected_endpoints: bool | None = False
        """
        Are endpoints connected to this node type.
        """
        default_evpn_role: Literal["none", "client", "server"] | None = "none"
        """
        Default evpn_role. Can be overridden in topology vars.
        """
        default_ptp_priority1: int | None = Field(127, ge=0, le=255)
        """
        Default PTP priority 1
        """
        default_underlay_routing_protocol: (
            Annotated[Literal["ebgp", "ospf", "ospf-ldp", "isis", "isis-sr", "isis-ldp", "isis-sr-ldp", "none"], StrConvert(to_lower=True)] | None
        ) = "ebgp"
        """
        Set the default underlay routing_protocol.
        Can be overridden by setting "underlay_routing_protocol" host/group_vars.
        """
        default_overlay_routing_protocol: Annotated[Literal["ebgp", "ibgp", "her", "cvx", "none"], StrConvert(to_lower=True)] | None = "ebgp"
        """
        Set the default overlay routing_protocol.
        Can be overridden by setting "overlay_routing_protocol" host/group_vars.
        """
        default_mpls_overlay_role: Literal["client", "server", "none"] | None = None
        """
        Set the default mpls overlay role.
        Acting role in overlay control plane.
        """
        default_overlay_address_families: list[Annotated[str, StrConvert(to_lower=True)]] | None = None
        """
        Set the default overlay address families.
        """
        default_evpn_encapsulation: Annotated[Literal["mpls", "vxlan"], StrConvert(to_lower=True)] | None = None
        """
        Set the default evpn encapsulation.
        """
        default_wan_role: Literal["client", "server"] | None = None
        """
        Set the default WAN role.

        This is used both for AutoVPN and Pathfinder designs.
        That means if `wan_mode` root key is
        set to `autovpn` or `cv-pathfinder`.
        `server` indicates that the router is a route-reflector.

        Only supported if
        `overlay_routing_protocol` is set to `ibgp`.
        """
        mlag_support: bool | None = False
        """
        Can this node type support mlag.
        """
        network_services: NetworkServices | None = None
        """
        Will network services be deployed on this node type.
        """
        underlay_router: bool | None = True
        """
        Is this node type a L3 device.
        """
        uplink_type: Literal["p2p", "port-channel", "p2p-vrfs", "lan"] | None = "p2p"
        """
        `uplink_type` must be `p2p`, `p2p-vrfs` or `lan` if `vtep` or `underlay_router` is true.

        For `p2p-vrfs`, the uplinks
        are configured as L3 interfaces with a subinterface for each VRF
        in `network_services` present on both the uplink and
        the downlink switch.
        The subinterface ID is the `vrf_id`.
        'underlay_router' and 'network_services.l3' must be set to
        true.
        VRF `default` is always configured on the physical interface using the underlay routing protocol.
        All
        subinterfaces use the same IP address as the physical interface.
        Multicast is not supported.
        Only BGP is supported for
        subinterfaces.

        For `lan`, a single uplink interface is supported and will be configured as an L3 Interface with
        subinterfaces for each SVI defined under the VRFs in `network_services` as long as the uplink switch also
        has the VLAN
        permitted by tag/tenant filtering.
        """
        vtep: bool | None = False
        """
        Is this switch an EVPN VTEP.
        """
        mpls_lsr: bool | None = False
        """
        Is this switch an MPLS LSR.
        """
        ip_addressing: IpAddressing | None = None
        """
        Override ip_addressing templates.
        """
        interface_descriptions: InterfaceDescriptions | None = None
        """
        Override interface_descriptions templates
        If description templates use Jinja2, they have to strip whitespaces using {%-
        -%} on any code blocks.
        """
        cv_tags_topology_type: Literal["leaf", "spine", "core", "edge"] | None = None
        """
        PREVIEW: This key is currently not supported
        Type that CloudVision should use when generating the Topology.
        """

    class NtpSettings(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class ServersItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str | None = None
            """
            IP or hostname e.g., 2.2.2.55, ie.pool.ntp.org
            """
            burst: bool | None = None
            iburst: bool | None = None
            key: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)
            maxpoll: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=3, le=17)
            """
            Value of maxpoll between 3 - 17 (Logarithmic)
            """
            minpoll: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=3, le=17)
            """
            Value of minpoll between 3 - 17 (Logarithmic)
            """
            version: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=4)

        class AuthenticationKeysItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            id: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=1, le=65534)
            """
            Key identifier
            """
            hash_algorithm: Literal["md5", "sha1"] | None = None
            key: str | None = None
            """
            Obfuscated key
            """
            key_type: Annotated[Literal["0", "7", "8a"], StrConvert(convert_types=(int))] | None = None

        server_vrf: str | None = None
        """
        EOS only supports NTP servers in one VRF, so this VRF is used for all NTP servers and one local-interface.
        -
        `use_mgmt_interface_vrf` will configure the NTP server(s) under the VRF set with `mgmt_interface_vrf` and set the
        `mgmt_interface` as NTP local-interface.
          An error will be raised if `mgmt_ip` or `ipv6_mgmt_ip` are not configured for
        the device.
        - `use_inband_mgmt_vrf` will configure the NTP server(s) under the VRF set with `inband_mgmt_vrf` and set
        the `inband_mgmt_interface` as NTP local-interface.
          An error will be raised if inband management is not configured for
        the device.
        - Any other string will be used directly as the VRF name but local interface must be set with
        `custom_structured_configuration_ntp` if needed.
        If not set, the VRF is automatically picked up from the global setting
        `default_mgmt_method`.
        """
        servers: list[ServersItem] | None = None
        """
        The first server is always set as "preferred".
        """
        authenticate: bool | None = None
        authenticate_servers_only: bool | None = None
        authentication_keys: list[AuthenticationKeysItem] | None = None
        trusted_keys: Annotated[str, StrConvert(convert_types=(int))] | None = None
        """
        List of trusted-keys as string ex. 10-12,15
        """

    class OverlayRdType(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        admin_subfield: Annotated[str, StrConvert(convert_types=(int))] | None = "overlay_loopback_ip"
        """
        The method for deriving RD Administrator subfield (first part of RD):
        - 'overlay_loopback_ip' means the IP address of
        Loopback0.
        - 'vtep_loopback' means the IP address of the VTEP loopback interface.
        - 'bgp_as' means the AS number of the
        device.
        - 'switch_id' means the 'id' value of the device.
        - Any <IPv4 Address> without mask.
        - Integer between
        <0-65535>.
        - Integer between <0-4294967295>.
        """
        admin_subfield_offset: Annotated[str, StrConvert(convert_types=(int))] | None = None
        """
        Offset can only be used if admin_subfield is an integer between <0-4294967295> or 'switch_id'.
        Total value of
        admin_subfield + admin_subfield_offset must be <= 4294967295.
        """
        vrf_admin_subfield: Annotated[str, StrConvert(convert_types=(int))] | None = None
        """
        The method for deriving RD Administrator subfield (first part of RD) for VRF services:
        - 'overlay_loopback_ip' means the
        IP address of Loopback0.
        - 'vtep_loopback' means the IP address of the VTEP loopback interface.
        - 'bgp_as' means the AS
        number of the device.
        - 'switch_id' means the 'id' value of the device.
        - Any <IPv4 Address> without mask.
        - Integer
        between <0-65535>.
        - Integer between <0-4294967295>.

        'vrf_admin_subfield' takes precedence for VRF RDs if set.
        Otherwise the 'admin_subfield' value will be used.
        """
        vrf_admin_subfield_offset: Annotated[str, StrConvert(convert_types=(int))] | None = None
        """
        Offset can only be used if 'vrf_admin_subfield' is an integer between <0-4294967295> or 'switch_id'.
        Total value of
        'vrf_admin_subfield' + 'vrf_admin_subfield_offset' must be <= 4294967295.
        """
        vlan_assigned_number_subfield: Literal["mac_vrf_id", "mac_vrf_vni", "vlan_id"] | None = "mac_vrf_id"
        """
        The method for deriving RD Assigned Number subfield for VLAN services (second part of RD):
        - 'mac_vrf_id' means
        `(mac_vrf_id_base or mac_vrf_vni_base) + vlan_id`.
        - 'mac_vrf_vni' means `(mac_vrf_vni_base or mac_vrf_id_base) +
        vlan_id`.
        - 'vlan_id' will only use the 'vlan_id' and ignores all base values.

        These methods can be overridden per VLAN
        if either 'rd_override', 'rt_override' or 'vni_override' is set (preferred in this order).
        """

    class OverlayRtType(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        admin_subfield: Annotated[str, StrConvert(convert_types=(int))] | None = "vrf_id"
        """
        The method for deriving RT Administrator subfield (first part of RT):
        - 'vrf_id' means `(mac_vrf_id_base or
        mac_vrf_vni_base) + vlan_id` for VLANs, `(vrf_id or vrf_vni)` for VRFs and `id` for bundles defined under
        'evpn_vlan_bundles'.
        - 'vrf_vni' means `(mac_vrf_vni_base or mac_vrf_id_base) + vlan_id` for VLANs, `(vrf_vni or
        vrf_id)` for VRFs and `id` for bundles defined under 'evpn_vlan_bundles'.
        - 'id' means `vlan_id` for VLANs, `(vrf_id or
        vrf_vni)` for VRFs and `id` for bundles defined under 'evpn_vlan_bundles'.
        - 'bgp_as' means the AS number of the device.
        - Integer between <0-65535>.
        - Integer between <0-4294967295>.

        The 'vrf_id' and 'vrf_vni' methods can be overridden per
        VLAN if either 'rt_override' or 'vni_override' is set (preferred in this order).
        The 'vrf_id', 'vrf_vni' and 'id'
        methods can be overridden per bundle defined under `evpn_vlan_bundles` using 'rt_override'.
        """
        vrf_admin_subfield: Annotated[str, StrConvert(convert_types=(int))] | None = "vrf_id"
        """
        The method for deriving RT Administrator subfield (first part of RT) for VRF services:
        - 'id' means `(vrf_id or
        vrf_vni)`.
        - 'vrf_id' means `(vrf_id or vrf_vni)`.
        - 'vrf_vni' means `(vrf_vni or vrf_id)`.
        - 'bgp_as' means the AS
        number of the device.
        - Integer between <0-65535>.
        - Integer between <0-4294967295>.

        'vrf_admin_subfield' takes
        precedence for VRF RDs if set. Otherwise the 'admin_subfield' value will be used.
        """
        vlan_assigned_number_subfield: Literal["mac_vrf_id", "mac_vrf_vni", "vlan_id"] | None = "mac_vrf_id"
        """
        The method for deriving RT Assigned Number subfield for VLAN services (second part of RT):
        - 'mac_vrf_id' means
        `(mac_vrf_id_base or mac_vrf_vni_base) + vlan_id`.
        - 'mac_vrf_vni' means `(mac_vrf_vni_base or mac_vrf_id_base) +
        vlan_id`.
        - 'vlan_id' will only use the 'vlan_id' and ignores all base values.

        These methods can be overridden per VLAN
        if either 'rt_override' or 'vni_override' is set (preferred in this order).
        """

    class PlatformSettingsItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class ReloadDelay(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            mlag: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=86400)
            """
            In seconds.
            """
            non_mlag: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=86400)
            """
            In seconds.
            """

        class FeatureSupport(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            queue_monitor_length_notify: bool | None = True
            interface_storm_control: bool | None = True
            poe: bool | None = False
            per_interface_mtu: bool | None = True
            """
            Support for configuration of per interface MTU for p2p links, MLAG SVIs and Network Services.
            Effectively this means
            that all settings regarding interface MTU will be ignored if this is false.
            Platforms without support for per interface
            MTU can use a single default interface MTU setting. Set this via "default_interface_mtu"
            """
            bgp_update_wait_install: bool | None = True
            """
            Disables FIB updates and route advertisement when the BGP instance is initiated until the BGP convergence state is
            reached.
            Can be overridden by setting "bgp_update_wait_install" host/group_vars.
            """
            bgp_update_wait_for_convergence: bool | None = True
            """
            Do not advertise reachability to a prefix until that prefix has been installed in hardware.
            This will eliminate any
            temporary black holes due to a BGP speaker advertising reachability to a prefix that may not yet be installed into the
            forwarding plane.
            Can be overridden by setting "bgp_update_wait_for_convergence" host/group_vars.
            """

        platforms: list[Annotated[str, StrConvert(convert_types=(int))]] | None = None
        trident_forwarding_table_partition: str | None = None
        """
        Only applied when evpn_multicast is true.
        """
        reload_delay: ReloadDelay | None = None
        tcam_profile: str | None = None
        lag_hardware_only: bool | None = None
        default_interface_mtu: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=68, le=65535)
        """
        Default interface MTU configured on EOS under "interface defaults".
        Takes precedence over the root key
        "default_interface_mtu".
        """
        feature_support: FeatureSupport | None = None
        management_interface: str | None = "Management1"
        raw_eos_cli: str | None = None
        """
        EOS CLI rendered directly on the root level of the final EOS configuration.
        """

    class PlatformSpeedGroupsItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class SpeedsItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            speed: str = None
            speed_groups: list[Annotated[str, StrConvert(convert_types=(int))]] | None = None

        platform: Annotated[str, StrConvert(convert_types=(int))] = None
        speeds: list[SpeedsItem] | None = None

    class PortProfilesItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Flowcontrol(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            received: Literal["received", "send", "on"] | None = None

        class Ptp(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            enabled: bool | None = False
            endpoint_role: Literal["bmca", "default", "follower"] | None = "follower"
            profile: Literal["aes67", "aes67-r16-2016", "smpte2059-2"] | None = "aes67-r16-2016"

        class LinkTracking(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            enabled: bool | None = None
            name: str | None = None
            """
            Tracking group name.
            The default group name is taken from fabric variable of the switch, `link_tracking.groups[0].name`
            with default value being "LT_GROUP1".
            Optional if default link_tracking settings are configured on the node.
            """

        class Dot1x(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Pae(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                mode: Literal["authenticator"] | None = None

            class AuthenticationFailure(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                action: Literal["allow", "drop"] | None = None
                allow_vlan: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=4094)

            class HostMode(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                mode: Literal["multi-host", "single-host"] | None = None
                multi_host_authenticated: bool | None = None

            class MacBasedAuthentication(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                enabled: bool | None = None
                always: bool | None = None
                host_mode_common: bool | None = None

            class Timeout(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                idle_host: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=10, le=65535)
                quiet_period: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)
                reauth_period: Annotated[str, StrConvert(convert_types=(int))] | None = None
                """
                Range 60-4294967295 or "server".
                """
                reauth_timeout_ignore: bool | None = None
                tx_period: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)

            class Unauthorized(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                access_vlan_membership_egress: bool | None = None
                native_vlan_membership_egress: bool | None = None

            port_control: Literal["auto", "force-authorized", "force-unauthorized"] | None = None
            port_control_force_authorized_phone: bool | None = None
            reauthentication: bool | None = None
            pae: Pae | None = None
            authentication_failure: AuthenticationFailure | None = None
            host_mode: HostMode | None = None
            mac_based_authentication: MacBasedAuthentication | None = None
            timeout: Timeout | None = None
            reauthorization_request_limit: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=10)
            unauthorized: Unauthorized | None = None

        class Poe(EosCliConfigGen.EthernetInterfacesItem.Poe, BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            pass

        class StormControl(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class All(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                level: Annotated[str, StrConvert(convert_types=(int, float))] | None = None
                """
                Configure maximum storm-control level.
                """
                unit: Literal["percent", "pps"] | None = "percent"
                """
                Optional variable and is hardware dependent.
                """

            class Broadcast(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                level: Annotated[str, StrConvert(convert_types=(int, float))] | None = None
                """
                Configure maximum storm-control level.
                """
                unit: Literal["percent", "pps"] | None = "percent"
                """
                Optional variable and is hardware dependent.
                """

            class Multicast(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                level: Annotated[str, StrConvert(convert_types=(int, float))] | None = None
                """
                Configure maximum storm-control level.
                """
                unit: Literal["percent", "pps"] | None = "percent"
                """
                Optional variable and is hardware dependent.
                """

            class UnknownUnicast(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                level: Annotated[str, StrConvert(convert_types=(int, float))] | None = None
                """
                Configure maximum storm-control level.
                """
                unit: Literal["percent", "pps"] | None = "percent"
                """
                Optional variable and is hardware dependent.
                """

            all: All | None = None
            broadcast: Broadcast | None = None
            multicast: Multicast | None = None
            unknown_unicast: UnknownUnicast | None = None

        class MonitorSessionsItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class SourceSettings(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class AccessGroup(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    type: Literal["ip", "ipv6", "mac"] | None = None
                    name: str | None = None
                    """
                    ACL name.
                    """
                    priority: Annotated[int, IntConvert(convert_types=(str))] | None = None

                direction: Literal["rx", "tx", "both"] | None = None
                access_group: AccessGroup | None = None

            class SessionSettings(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class AccessGroup(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    type: Literal["ip", "ipv6", "mac"] | None = None
                    name: str | None = None
                    """
                    ACL name.
                    """

                class Truncate(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    enabled: bool | None = None
                    size: Annotated[int, IntConvert(convert_types=(str))] | None = None
                    """
                    Size in bytes
                    """

                encapsulation_gre_metadata_tx: bool | None = None
                header_remove_size: Annotated[int, IntConvert(convert_types=(str))] | None = None
                """
                Number of bytes to remove from header.
                """
                access_group: AccessGroup | None = None
                rate_limit_per_ingress_chip: str | None = None
                """
                Ratelimit and unit as string.
                Examples:
                  "100000 bps"
                  "100 kbps"
                  "10 mbps"
                """
                rate_limit_per_egress_chip: str | None = None
                """
                Ratelimit and unit as string.
                Examples:
                  "100000 bps"
                  "100 kbps"
                  "10 mbps"
                """
                sample: Annotated[int, IntConvert(convert_types=(str))] | None = None
                truncate: Truncate | None = None

            name: str = None
            """
            Session name.
            """
            role: Literal["source", "destination"] | None = None
            source_settings: SourceSettings | None = None
            session_settings: SessionSettings | None = None
            """
            Session settings are defined per session name.
            Different session_settings for the same session name will be
            combined/merged.
            """

        class EthernetSegment(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            short_esi: str = None
            """
            In format xxxx:xxxx:xxxx or "auto".
            Define a manual short-esi (be careful using this on profiles) or set the value to
            "auto" to automatically generate the value.
            Please see the notes under "EVPN A/A ESI dual and single-attached endpoint
            scenarios" before setting `short_esi: auto`.
            """
            redundancy: Literal["all-active", "single-active"] | None = None
            """
            If omitted, Port-Channels use the EOS default of all-active.
            If omitted, Ethernet interfaces are configured as single-
            active.
            """
            designated_forwarder_algorithm: Literal["auto", "modulus", "preference"] | None = None
            """
            Configure DF algorithm and preferences.
            - auto: Use preference-based algorithm and assign preference based on position
            of device in the 'switches' list,
              e.g., assuming a list of three switches, this would assign a preference of 200 to
            the first switch, 100 to the 2nd, and 0 to the third.
            - preference: Set preference for each switch manually using
            designated_forwarder_preferences key.
            - modulus: Use the default modulus-based algorithm.
            If omitted, Port-Channels use
            the EOS default of modulus.
            If omitted, Ethernet interfaces default to the 'auto' mechanism detailed above.
            """
            designated_forwarder_preferences: list[Annotated[int, IntConvert(convert_types=(str))]] | None = None
            """
            Manual preference as described above, required only for preference algorithm.
            """
            dont_preempt: bool | None = None
            """
            Disable preemption for single-active forwarding when auto/manual DF preference is configured.
            """

        class PortChannel(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class LacpFallback(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Individual(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    profile: str | None = None
                    """
                    Port-profile name to inherit configuration.
                    """

                mode: Literal["static", "individual"] | None = None
                """
                Either static or individual mode is supported.
                If the mode is set to "individual" the "individual.profile" setting must
                be defined.
                """
                individual: Individual | None = None
                """
                Define parameters for port-channel member interfaces. Applies only if LACP fallback is set to "individual".
                """
                timeout: Annotated[int, IntConvert(convert_types=(str))] | None = None
                """
                Timeout in seconds. EOS default is 90 seconds.
                """

            class LacpTimer(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                mode: Literal["normal", "fast"] | None = None
                """
                LACP mode for interface members.
                """
                multiplier: Annotated[int, IntConvert(convert_types=(str))] | None = None
                """
                Number of LACP BPDUs lost before deeming the peer down. EOS default is 3.
                """

            class SubinterfacesItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class EncapsulationVlan(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    client_dot1q: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=4094)

                number: Annotated[int, IntConvert(convert_types=(str))] | None = None
                """
                Subinterface number
                """
                short_esi: str | None = None
                """
                In format xxxx:xxxx:xxxx or "auto"
                Required for multihomed port-channels with subinterfaces
                """
                vlan_id: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=4094)
                """
                VLAN ID to bridge.
                Default is subinterface number.
                """
                encapsulation_vlan: EncapsulationVlan | None = None
                """
                Client VLAN ID encapsulation.
                Default is subinterface number.
                """

            class StructuredConfig(EosCliConfigGen.PortChannelInterfacesItem, BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                pass

            mode: Literal["active", "passive", "on"] | None = None
            """
            Port-Channel Mode.
            """
            channel_id: Annotated[int, IntConvert(convert_types=(str))] | None = None
            """
            Port-Channel ID.
            If no channel_id is specified, an id is generated from the first switch port in the port channel.
            """
            description: str | None = None
            """
            By default the description is built leveraging `<peer>` name or `adapter.description` when defined.
            When this key is
            defined, it will append its content to the physical port description.
            """
            enabled: bool | None = True
            """
            Port-Channel administrative state.
            Setting to false will set port to 'shutdown' in intended configuration.
            """
            short_esi: str | None = None
            """
            In format xxxx:xxxx:xxxx or "auto".
            """
            lacp_fallback: LacpFallback | None = None
            """
            LACP fallback configuration.
            """
            lacp_timer: LacpTimer | None = None
            """
            LACP timer configuration. Applies only when Port-channel mode is not "on".
            """
            subinterfaces: list[SubinterfacesItem] | None = None
            """
            Port-Channel L2 Subinterfaces
            Subinterfaces are only supported on routed port-channels, which means they cannot be
            configured on MLAG port-channels.
            Setting short_esi: auto generates the short_esi automatically using a hash of
            configuration elements.
            Please see the notes under "EVPN A/A ESI dual-attached endpoint scenario" before setting
            short_esi: auto.
            """
            raw_eos_cli: str | None = None
            """
            EOS CLI rendered directly on the port-channel interface in the final EOS configuration.
            """
            structured_config: StructuredConfig | None = None
            """
            Custom structured config added under port_channel_interfaces.[name=<interface>] for eos_cli_config_gen.
            """

        class StructuredConfig(EosCliConfigGen.EthernetInterfacesItem, BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            pass

        profile: str = None
        """
        Port profile name.
        """
        parent_profile: str | None = None
        """
        Parent profile is optional.
        Port_profiles can refer to another port_profile to inherit settings in up to two levels
        (adapter->profile->parent_profile).
        """
        speed: str | None = None
        """
        Set adapter speed in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`.
        If not
        specified speed will be auto.
        """
        description: str | None = None
        """
        By default the description is built leveraging `<peer>_<peer_interface>`.
        When set this key will overide the default
        value on the physical ports.
        """
        enabled: bool | None = True
        """
        Administrative state, setting to false will set the port to 'shutdown' in the intended configuration.
        """
        mode: Literal["access", "dot1q-tunnel", "trunk", "trunk phone"] | None = None
        """
        Interface mode.
        """
        mtu: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=68, le=65535)
        l2_mtu: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=68, le=65535)
        """
        "l2_mtu" should only be defined for platforms supporting the "l2 mtu" CLI
        """
        l2_mru: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=68, le=65535)
        """
        "l2_mru" should only be defined for platforms supporting the "l2 mru" CLI
        """
        native_vlan: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=4094)
        """
        Native VLAN for a trunk port.
        If both `native_vlan` and `native_vlan_tag`, `native_vlan_tag` takes precedence.
        """
        native_vlan_tag: bool | None = False
        """
        If both `native_vlan` and `native_vlan_tag`, `native_vlan_tag` takes precedence.
        """
        phone_vlan: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=4094)
        """
        Phone VLAN for a mode `trunk phone` port.
        Requires `mode: trunk phone` to be set.
        """
        phone_trunk_mode: Literal["tagged", "untagged", "tagged phone", "untagged phone"] | None = None
        """
        Specify if the phone traffic is tagged or untagged.
        If both data and phone traffic are untagged, MAC-Based VLAN
        Assignment (MBVA) is used, if supported by the model of switch.
        """
        trunk_groups: list[str] | None = None
        """
        Required with `enable_trunk_groups: true`.
        Trunk Groups are used for limiting VLANs on trunk ports to VLANs with the
        same Trunk Group.
        """
        vlans: Annotated[str, StrConvert(convert_types=(int))] | None = None
        """
        Interface VLANs - if not set, the EOS default is that all VLANs are allowed for trunk ports, and VLAN 1 will be used for
        access ports.
        """
        spanning_tree_portfast: Literal["edge", "network"] | None = None
        spanning_tree_bpdufilter: Annotated[Literal["enabled", "disabled", "True", "False", "true", "false"], StrConvert(convert_types=(bool))] | None = None
        spanning_tree_bpduguard: Annotated[Literal["enabled", "disabled", "True", "False", "true", "false"], StrConvert(convert_types=(bool))] | None = None
        flowcontrol: Flowcontrol | None = None
        qos_profile: str | None = None
        """
        QOS profile name
        """
        ptp: Ptp | None = None
        """
        The global PTP profile parameters will be applied to all connected endpoints where `ptp` is manually enabled.
        `ptp role
        master` is set to ensure control over the PTP topology.
        """
        sflow: bool | None = None
        """
        Configures sFlow on the interface. Overrides `fabric_sflow` setting.
        """
        link_tracking: LinkTracking | None = None
        """
        Configure the downstream interfaces of a respective Link Tracking Group.
        If `port_channel` is defined in an adapter,
        then the port-channel interface is configured to be the downstream.
        Else all the ethernet interfaces will be configured
        as downstream -> to configure single-active EVPN multihomed networks.
        """
        dot1x: Dot1x | None = None
        """
        802.1x
        """
        poe: Poe | None = None
        """
        Power Over Ethernet settings applied on port. Only configured if platform supports PoE.
        """
        storm_control: StormControl | None = None
        """
        Storm control settings applied on port toward the endpoint.
        """
        monitor_sessions: list[MonitorSessionsItem] | None = None
        """
        Used to define switchports as source or destination for monitoring sessions.
        """
        ethernet_segment: EthernetSegment | None = None
        """
        Settings for all or single-active EVPN multihoming.
        """
        port_channel: PortChannel | None = None
        """
        Used for port-channel adapter.
        """
        validate_state: bool | None = None
        """
        Set to false to disable interface validation by the `eos_validate_state` role.
        """
        raw_eos_cli: str | None = None
        """
        EOS CLI rendered directly on the ethernet interface in the final EOS configuration.
        """
        structured_config: StructuredConfig | None = None
        """
        Custom structured config added under ethernet_interfaces.[name=<interface>] for eos_cli_config_gen.
        """

    class Ptp(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        enabled: bool | None = None
        profile: Literal["aes67", "smpte2059-2", "aes67-r16-2016"] | None = "aes67-r16-2016"
        domain: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=255)
        auto_clock_identity: bool | None = True

    class PtpProfilesItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Announce(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            interval: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=-7, le=4)
            timeout: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=2, le=255)

        class SyncMessage(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            interval: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=-7, le=3)

        profile: str | None = None
        """
        PTP profile.
        """
        announce: Announce | None = None
        """
        PTP announce interval.
        """
        delay_req: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=-7, le=8)
        sync_message: SyncMessage | None = None
        """
        PTP sync message interval.
        """
        transport: Literal["ipv4"] | None = None

    class QueueMonitorLength(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class DefaultThresholds(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            high: Annotated[int, IntConvert(convert_types=(str))] = None
            """
            Default high threshold for Ethernet Interfaces.
            """
            low: Annotated[int, IntConvert(convert_types=(str))] | None = None
            """
            Default low threshold for Ethernet Interfaces.
            Low threshold support is platform dependent.
            """

        class Cpu(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Thresholds(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                high: Annotated[int, IntConvert(convert_types=(str))] = None
                low: Annotated[int, IntConvert(convert_types=(str))] | None = None

            thresholds: Thresholds | None = None

        enabled: bool = None
        notifying: bool | None = None
        """
        If True, `eos_designs` will configure `queue-monitor length notifying` according to the
        `platform_settings.[].feature_support.queue_monitor_length_notify` setting.
        """
        default_thresholds: DefaultThresholds | None = None
        log: Annotated[int, IntConvert(convert_types=(str))] | None = None
        """
        Logging interval in seconds
        """
        cpu: Cpu | None = None
        tx_latency: bool | None = None
        """
        Enable tx-latency mode
        """

    class Redundancy(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        protocol: Literal["sso", "rpr"] | None = None

    class SflowSettings(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class DestinationsItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            destination: str = None
            """
            sFlow destination name or IP address.
            """
            port: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)
            """
            UDP Port number. The default port number for sFlow is 6343.
            """
            vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
            """
            If not set, the VRF is automatically picked up from the global setting `default_mgmt_method`.
            The value of `vrf` will be
            interpreted according to these rules:
            - `use_mgmt_interface_vrf` will configure the sFlow destination under the VRF set
            with `mgmt_interface_vrf` and set the `mgmt_interface` as sFlow source-interface.
              An error will be raised if `mgmt_ip`
            or `ipv6_mgmt_ip` are not configured for the device.
            - `use_inband_mgmt_vrf` will configure the sFlow destination under
            the VRF set with `inband_mgmt_vrf` and set the `inband_mgmt_interface` as sFlow source-interface.
              An error will be
            raised if inband management is not configured for the device.
            - Any other string will be used directly as the VRF name.
            Remember to set the `sflow_settings.vrfs[].source_interface` if needed.
            """

        class VrfsItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: Annotated[str, StrConvert(convert_types=(int))] = None
            """
            VRF name.
            """
            source_interface: str | None = None
            """
            Source interface to use for sFlow destinations in this VRF.
            If set for the VRFs defined by `mgmt_interface_vrf` or
            `inband_mgmt_vrf`, this setting will take precedence.
            """

        destinations: list[DestinationsItem] | None = None
        vrfs: list[VrfsItem] | None = None

    class SnmpSettings(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class VrfsItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: Annotated[str, StrConvert(convert_types=(int))] = None
            """
            VRF name
            """
            enable: bool | None = None

        class UsersItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str | None = None
            """
            Username
            """
            group: str | None = None
            """
            Group name
            """
            version: Literal["v1", "v2c", "v3"] | None = None
            auth: Literal["md5", "sha", "sha256", "sha384", "sha512"] | None = None
            auth_passphrase: str | None = None
            """
            Cleartext passphrase so the recommendation is to use vault. Requires 'auth' to be set.
            """
            priv: Literal["des", "aes", "aes192", "aes256"] | None = None
            priv_passphrase: str | None = None
            """
            Cleartext passphrase so the recommendation is to use vault. Requires 'priv' to be set.
            """

        class HostsItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class UsersItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                username: str | None = None
                authentication_level: Literal["auth", "noauth", "priv"] | None = None

            host: str | None = None
            """
            Host IP address or name
            """
            vrf: Annotated[str, StrConvert(convert_types=(int, int))] | None = None
            """
            VRF Name.
            Can be used in combination with "use_mgmt_interface_vrf" and "use_inband_mgmt_vrf" to configure the SNMP host
            under multiple VRFs.
            """
            use_mgmt_interface_vrf: bool | None = None
            """
            Configure the SNMP host under the VRF set with "mgmt_interface_vrf". Ignored if 'mgmt_ip' or 'ipv6_mgmt_ip' are not
            configured for the device, so if the host is only configured with this VRF, the host will not be configured at all. Can
            be used in combination with "vrf" and "use_inband_mgmt_vrf" to configure the SNMP host under multiple VRFs.
            """
            use_inband_mgmt_vrf: bool | None = None
            """
            Configure the SNMP host under the VRF set with "inband_mgmt_vrf". Ignored if inband management is not configured for the
            device, so if the host is only configured with this VRF, the host will not be configured at all. Can be used in
            combination with "vrf" and "use_mgmt_interface_vrf" to configure the SNMP host under multiple VRFs.
            """
            version: Annotated[Literal["1", "2c", "3"], StrConvert(convert_types=(int))] | None = None
            community: str | None = None
            """
            Community name
            """
            users: list[UsersItem] | None = None

        class CommunitiesItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class AccessListIpv4(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                name: str | None = None
                """
                IPv4 access list name
                """

            class AccessListIpv6(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                name: str | None = None
                """
                IPv6 access list name
                """

            name: str = None
            """
            Community name
            """
            access: Literal["ro", "rw"] | None = None
            access_list_ipv4: AccessListIpv4 | None = None
            access_list_ipv6: AccessListIpv6 | None = None
            view: str | None = None

        class Ipv4AclsItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str | None = None
            """
            IPv4 access list name
            """
            vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None

        class Ipv6AclsItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str | None = None
            """
            IPv6 access list name
            """
            vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None

        class ViewsItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str | None = None
            """
            SNMP view name
            """
            mib_family_name: str | None = None
            included: bool | None = None
            field_MIB_family_name: str | None = Field(None, alias="MIB_family_name")

        class GroupsItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str | None = None
            """
            Group name
            """
            version: Literal["v1", "v2c", "v3"] | None = None
            authentication: Literal["auth", "noauth", "priv"] | None = None
            read: str | None = None
            """
            Read view
            """
            write: str | None = None
            """
            Write view
            """
            notify: str | None = None
            """
            Notify view
            """

        class Traps(EosCliConfigGen.SnmpServer.Traps, BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            pass

        contact: str | None = None
        """
        SNMP contact.
        """
        location: bool | None = False
        """
        Set SNMP location. Formatted as "<fabric_name> <dc_name> <pod_name> <switch_rack> <inventory_hostname>".
        """
        vrfs: list[VrfsItem] | None = None
        """
        Enable/disable SNMP for one or more VRFs.
        Can be used in combination with "enable_mgmt_interface_vrf" and
        "enable_inband_mgmt_vrf".
        """
        enable_mgmt_interface_vrf: bool | None = None
        """
        Enable/disable SNMP for the VRF set with "mgmt_interface_vrf".
        Ignored if 'mgmt_ip' or 'ipv6_mgmt_ip' are not configured
        for the device.
        Can be used in combination with "vrfs" and "enable_inband_mgmt_vrf".
        """
        enable_inband_mgmt_vrf: bool | None = None
        """
        Enable/disable SNMP for the VRF set with "inband_mgmt_vrf".
        Ignored if inband management is not configured for the
        device.
        Can be used in combination with "vrfs" and "enable_mgmt_interface_vrf".
        """
        compute_local_engineid: bool | None = False
        """
        Generate a local engineId for SNMP using the 'compute_local_engineid_source' method.
        """
        compute_local_engineid_source: Literal["hostname_and_ip", "system_mac"] | None = "hostname_and_ip"
        """
        `compute_local_engineid_source` supports:
        - `hostname_and_ip` generate a local engineId for SNMP by hashing via SHA1
        the string generated via the concatenation of the hostname plus the management IP.
          {{ inventory_hostname }} + {{
        switch.mgmt_ip }}.
        - `system_mac` generate the switch default engine id for AVD usage.
          To use this,
        `system_mac_address` MUST be set for the device.
          The formula is f5717f + system_mac_address + 00.
        """
        compute_v3_user_localized_key: bool | None = False
        """
        Requires compute_local_engineid to be `true`.
        If enabled, the SNMPv3 passphrases for auth and priv are transformed using
        RFC 2574, matching the value they would take in EOS CLI.
        The algorithm requires a local engineId, which is unknown to
        AVD, hence the necessity to generate one beforehand.
        """
        users: list[UsersItem] | None = None
        """
        Configuration of local SNMP users.
        Configuration of remote SNMP users are currently only possible using
        `structured_config`.
        """
        hosts: list[HostsItem] | None = None
        communities: list[CommunitiesItem] | None = None
        ipv4_acls: list[Ipv4AclsItem] | None = None
        ipv6_acls: list[Ipv6AclsItem] | None = None
        views: list[ViewsItem] | None = None
        groups: list[GroupsItem] | None = None
        traps: Traps | None = None

    class SourceInterfaces(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class DomainLookup(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            mgmt_interface: bool | None = None
            """
            Configure an IP Domain Lookup source-interface with the interface set by `mgmt_interface` for the VRF set by
            `mgmt_interface_vrf`.
            `mgmt_interface` is typically the out-of-band Management interface, and can be set under the node
            settings, platform settings or as a group/host var.
            """
            inband_mgmt_interface: bool | None = None
            """
            Configure an IP Domain Lookup source-interface with the interface set by `inband_mgmt_interface` for the VRF set by
            `inband_mgmt_vrf`.
            `inband_mgmt_interface` is typically a loopback or SVI interface, and can be set under the node
            settings.
            """

        class HttpClient(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            mgmt_interface: bool | None = None
            """
            Configure an IP HTTP Client source-interface with the interface set by `mgmt_interface` for the VRF set by
            `mgmt_interface_vrf`.
            `mgmt_interface` is typically the out-of-band Management interface, and can be set under the node
            settings, platform settings or as a group/host var.
            """
            inband_mgmt_interface: bool | None = None
            """
            Configure an IP HTTP Client source-interface with the interface set by `inband_mgmt_interface` for the VRF set by
            `inband_mgmt_vrf`.
            `inband_mgmt_interface` is typically a loopback or SVI interface, and can be set under the node
            settings.
            """

        class Radius(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            mgmt_interface: bool | None = None
            """
            Configure an IP Radius source-interface with the interface set by `mgmt_interface` for the VRF set by
            `mgmt_interface_vrf`.
            `mgmt_interface` is typically the out-of-band Management interface, and can be set under the node
            settings, platform settings or as a group/host var.
            """
            inband_mgmt_interface: bool | None = None
            """
            Configure an IP Radius source-interface with the interface set by `inband_mgmt_interface` for the VRF set by
            `inband_mgmt_vrf`.
            `inband_mgmt_interface` is typically a loopback or SVI interface, and can be set under the node
            settings.
            """

        class Snmp(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            mgmt_interface: bool | None = None
            """
            Configure a SNMP local-interface with the interface set by `mgmt_interface` for the VRF set by `mgmt_interface_vrf`.
            `mgmt_interface` is typically the out-of-band Management interface, and can be set under the node settings, platform
            settings or as a group/host var.
            """
            inband_mgmt_interface: bool | None = None
            """
            Configure a SNMP local-interface with the interface set by `inband_mgmt_interface` for the VRF set by `inband_mgmt_vrf`.
            `inband_mgmt_interface` is typically a loopback or SVI interface, and can be set under the node settings.
            """

        class SshClient(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            mgmt_interface: bool | None = None
            """
            Configure an IP SSH Client source-interface with the interface set by `mgmt_interface` for the VRF set by
            `mgmt_interface_vrf`.
            `mgmt_interface` is typically the out-of-band Management interface, and can be set under the node
            settings, platform settings or as a group/host var.
            """
            inband_mgmt_interface: bool | None = None
            """
            Configure an IP SSH Client source-interface with the interface set by `inband_mgmt_interface` for the VRF set by
            `inband_mgmt_vrf`.
            `inband_mgmt_interface` is typically a loopback or SVI interface, and can be set under the node
            settings.
            """

        class Tacacs(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            mgmt_interface: bool | None = None
            """
            Configure an IP Tacacs source-interface with the interface set by `mgmt_interface` for the VRF set by
            `mgmt_interface_vrf`.
            `mgmt_interface` is typically the out-of-band Management interface, and can be set under the node
            settings, platform settings or as a group/host var.
            """
            inband_mgmt_interface: bool | None = None
            """
            Configure an IP Tacacs source-interface with the interface set by `inband_mgmt_interface` for the VRF set by
            `inband_mgmt_vrf`.
            `inband_mgmt_interface` is typically a loopback or SVI interface, and can be set under the node
            settings.
            """

        domain_lookup: DomainLookup | None = None
        """
        IP Domain Lookup source-interfaces.
        """
        http_client: HttpClient | None = None
        """
        IP HTTP Client source-interfaces.
        """
        radius: Radius | None = None
        """
        IP Radius source-interfaces.
        """
        snmp: Snmp | None = None
        """
        SNMP local-interfaces.
        """
        ssh_client: SshClient | None = None
        """
        IP SSH Client source-interfaces.
        """
        tacacs: Tacacs | None = None
        """
        IP Tacacs source-interfaces.
        """

    class SviProfilesItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class NodesItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class IpHelpersItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                ip_helper: str = None
                """
                IPv4 DHCP server IP
                """
                source_interface: str | None = None
                """
                Interface name to originate DHCP relay packets to DHCP server.
                """
                source_vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
                """
                VRF to originate DHCP relay packets to DHCP server. If not set, EOS uses the VRF on the SVI.
                """

            class EvpnL2Multicast(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                enabled: bool | None = None

            class EvpnL3Multicast(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                enabled: bool | None = None

            class IgmpSnoopingQuerier(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                enabled: bool | None = None
                """
                Will be enabled automatically if evpn_l2_multicast is enabled.
                """
                source_address: str | None = None
                """
                IPv4_address
                If not set, IP address of "Loopback0" will be used.
                """
                version: Annotated[Literal[1, 2, 3], IntConvert(convert_types=(str))] | None = None
                """
                IGMP Version (By default EOS uses IGMP version 2 for IGMP querier).
                """

            class Ospf(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class MessageDigestKeysItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    id: Annotated[int, IntConvert(convert_types=(str))] | None = None
                    hash_algorithm: Literal["md5", "sha1", "sha256", "sha384", "sha512"] | None = "sha512"
                    key: str | None = None
                    """
                    Type 7 encrypted key.
                    """

                enabled: bool | None = None
                point_to_point: bool | None = True
                area: Annotated[str, StrConvert(convert_types=(int))] | None = "0"
                """
                OSPF area ID.
                """
                cost: Annotated[int, IntConvert(convert_types=(str))] | None = None
                """
                OSPF link cost.
                """
                authentication: Literal["simple", "message-digest"] | None = None
                simple_auth_key: str | None = None
                """
                Password used with simple authentication.
                """
                message_digest_keys: list[MessageDigestKeysItem] | None = None

            class Bgp(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class StructuredConfig(EosCliConfigGen.RouterBgp.VlansItem, BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    pass

                structured_config: StructuredConfig | None = None
                """
                Structured configuration and EOS CLI commands rendered on router_bgp.vlans.[id=<vlan>]
                This configuration will not be
                applied to vlan aware bundles
                """
                raw_eos_cli: str | None = None
                """
                EOS CLI rendered directly on the Router BGP, VLAN definition in the final EOS configuration.
                """

            class StructuredConfig(EosCliConfigGen.VlanInterfacesItem, BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                pass

            node: str = None
            """
            l3_leaf inventory hostname
            """
            name: str | None = None
            """
            VLAN name
            """
            enabled: bool | None = None
            """
            Enable or disable interface
            """
            description: str | None = None
            """
            SVI description. By default set to VLAN name.
            """
            ip_address: str | None = None
            """
            IPv4_address/Mask. Usually set under "nodes" to have unique IPv4 addresses per node.
            """
            ipv6_address: str | None = None
            """
            IPv6_address/Mask. Usually set under "nodes" to have unique IPv6 addresses per node.
            """
            ipv6_enable: bool | None = None
            """
            Explicitly enable/disable link-local IPv6 addressing.
            """
            ip_address_virtual: str | None = None
            """
            IPv4_address/Mask
            IPv4 VXLAN Anycast IP address
            Conserves IP addresses in VXLAN deployments as it doesn't require unique
            IP addresses on each node.
            """
            ipv6_address_virtual: str | None = None
            """
            IPv6_address/Mask
            ipv6 address virtuals to configure VXLAN Anycast IP address (Optional)
            If both "ipv6_address_virtual"
            and "ipv6_address_virtuals" are set, all addresses will be configured
            """
            ipv6_address_virtuals: list[str] | None = None
            """
            IPv6 VXLAN Anycast IP addresses
            Conserves IPv6 addresses in VXLAN deployments as it doesn't require unique IPv6
            addresses on each node.
            """
            ip_address_virtual_secondaries: list[str] | None = None
            """
            Secondary IPv4 VXLAN Anycast IP addresses
            """
            ip_virtual_router_addresses: list[str] | None = None
            """
            IPv4 VARP addresses.
            Requires an IP address to be configured on the SVI.
            If ip_address_virtual is also set,
            ip_virtual_router_addresses will take precedence
            _if_ there is an ip_address configured for the node.
            """
            ipv6_virtual_router_addresses: list[str] | None = None
            """
            IPv6 VARP addresses.
            Requires an IPv6 address to be configured on the SVI.
            If ipv6_address_virtuals is also set,
            ipv6_virtual_router_addresses will take precedence
            _if_ there is an ipv6_address configured for the node.
            """
            ip_helpers: list[IpHelpersItem] | None = None
            """
            IP helper for DHCP relay
            """
            vni_override: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=16777215)
            """
            By default the VNI will be derived from "mac_vrf_vni_base".
            The vni_override allows us to override this value and
            statically define it (optional).
            """
            rt_override: Annotated[str, StrConvert(convert_types=(int))] | None = None
            """
            By default the MAC VRF RT will be derived from mac_vrf_id_base + vlan_id.
            The rt_override allows us to override this
            value and statically define it.
            rt_override will default to vni_override if set.

            rt_override supports two formats:
              -
            A single number which will be used in the RT fields instead of mac_vrf_id/mac_vrf_vni (see 'overlay_rt_type' for
            details).
              - A full RT string with colon seperator which will override the full RT.
            """
            rd_override: Annotated[str, StrConvert(convert_types=(int))] | None = None
            """
            By default the MAC VRF RD will be derived from mac_vrf_id_base + vlan_id.
            The rt_override allows us to override this
            value and statically define it.
            rd_override will default to rt_override or vni_override if set.

            rd_override supports
            two formats:
              - A single number which will be used in the RD assigned number field instead of mac_vrf_id/mac_vrf_vni
            (see 'overlay_rd_type' for details).
              - A full RD string with colon seperator which will override the full RD.
            """
            trunk_groups: list[str] | None = None
            evpn_l2_multicast: EvpnL2Multicast | None = None
            """
            Explicitly enable or disable evpn_l2_multicast to override setting of
            `<network_services_key>.[].evpn_l2_multicast.enabled`.
            When evpn_l2_multicast.enabled is set to true for a vlan or a
            tenant, "igmp snooping" and "igmp snooping querier" will always be enabled, overriding those individual settings.
            Requires `evpn_multicast` to also be set to `true`.
            """
            evpn_l3_multicast: EvpnL3Multicast | None = None
            """
            Explicitly enable or disable evpn_l3_multicast to override setting of
            `<network_services_key>.[].evpn_l3_multicast.enabled` and `<network_services_key>.[].vrfs.[].evpn_l3_multicast.enabled`.
            Requires `evpn_multicast` to also be set to `true`.
            """
            igmp_snooping_enabled: bool | None = None
            """
            Enable IGMP Snooping (Enabled by default on EOS).
            """
            igmp_snooping_querier: IgmpSnoopingQuerier | None = None
            vxlan: bool | None = True
            """
            Extend this SVI over VXLAN.
            """
            spanning_tree_priority: Annotated[int, IntConvert(convert_types=(str))] | None = None
            """
            Setting spanning-tree priority per VLAN is only supported with `spanning_tree_mode: rapid-pvst` under node type
            settings.
            The default priority for rapid-PVST is set under the node type settings with `spanning_tree_priority`
            (default=32768).
            """
            mtu: Annotated[int, IntConvert(convert_types=(str))] | None = None
            """
            Interface MTU.
            """
            ospf: Ospf | None = None
            """
            OSPF interface configuration.
            """
            bgp: Bgp | None = None
            raw_eos_cli: str | None = None
            """
            EOS CLI rendered directly on the VLAN interface in the final EOS configuration.
            """
            structured_config: StructuredConfig | None = None
            """
            Custom structured config added under vlan_interfaces.[name=<interface>] for eos_cli_config_gen.
            """

        class IpHelpersItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            ip_helper: str = None
            """
            IPv4 DHCP server IP
            """
            source_interface: str | None = None
            """
            Interface name to originate DHCP relay packets to DHCP server.
            """
            source_vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
            """
            VRF to originate DHCP relay packets to DHCP server. If not set, EOS uses the VRF on the SVI.
            """

        class EvpnL2Multicast(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            enabled: bool | None = None

        class EvpnL3Multicast(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            enabled: bool | None = None

        class IgmpSnoopingQuerier(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            enabled: bool | None = None
            """
            Will be enabled automatically if evpn_l2_multicast is enabled.
            """
            source_address: str | None = None
            """
            IPv4_address
            If not set, IP address of "Loopback0" will be used.
            """
            version: Annotated[Literal[1, 2, 3], IntConvert(convert_types=(str))] | None = None
            """
            IGMP Version (By default EOS uses IGMP version 2 for IGMP querier).
            """

        class Ospf(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class MessageDigestKeysItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                id: Annotated[int, IntConvert(convert_types=(str))] | None = None
                hash_algorithm: Literal["md5", "sha1", "sha256", "sha384", "sha512"] | None = "sha512"
                key: str | None = None
                """
                Type 7 encrypted key.
                """

            enabled: bool | None = None
            point_to_point: bool | None = True
            area: Annotated[str, StrConvert(convert_types=(int))] | None = "0"
            """
            OSPF area ID.
            """
            cost: Annotated[int, IntConvert(convert_types=(str))] | None = None
            """
            OSPF link cost.
            """
            authentication: Literal["simple", "message-digest"] | None = None
            simple_auth_key: str | None = None
            """
            Password used with simple authentication.
            """
            message_digest_keys: list[MessageDigestKeysItem] | None = None

        class Bgp(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class StructuredConfig(EosCliConfigGen.RouterBgp.VlansItem, BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                pass

            structured_config: StructuredConfig | None = None
            """
            Structured configuration and EOS CLI commands rendered on router_bgp.vlans.[id=<vlan>]
            This configuration will not be
            applied to vlan aware bundles
            """
            raw_eos_cli: str | None = None
            """
            EOS CLI rendered directly on the Router BGP, VLAN definition in the final EOS configuration.
            """

        class StructuredConfig(EosCliConfigGen.VlanInterfacesItem, BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            pass

        profile: str = None
        """
        Profile name
        """
        parent_profile: str | None = None
        """
        Parent SVI profile name to apply.
        svi_profiles can refer to another svi_profile to inherit settings in up to two levels
        (svi -> svi_profile -> svi_parent_profile).
        """
        nodes: list[NodesItem] | None = None
        """
        Define node specific configuration, such as unique IP addresses.
        Any keys set here will be merged onto the SVI config,
        except `structured_config` keys which will replace the `structured_config` set on SVI level.
        """
        name: str | None = None
        """
        VLAN name
        """
        enabled: bool | None = None
        """
        Enable or disable interface
        """
        description: str | None = None
        """
        SVI description. By default set to VLAN name.
        """
        ip_address: str | None = None
        """
        IPv4_address/Mask. Usually set under "nodes" to have unique IPv4 addresses per node.
        """
        ipv6_address: str | None = None
        """
        IPv6_address/Mask. Usually set under "nodes" to have unique IPv6 addresses per node.
        """
        ipv6_enable: bool | None = None
        """
        Explicitly enable/disable link-local IPv6 addressing.
        """
        ip_address_virtual: str | None = None
        """
        IPv4_address/Mask
        IPv4 VXLAN Anycast IP address
        Conserves IP addresses in VXLAN deployments as it doesn't require unique
        IP addresses on each node.
        """
        ipv6_address_virtual: str | None = None
        """
        IPv6_address/Mask
        ipv6 address virtuals to configure VXLAN Anycast IP address (Optional)
        If both "ipv6_address_virtual"
        and "ipv6_address_virtuals" are set, all addresses will be configured
        """
        ipv6_address_virtuals: list[str] | None = None
        """
        IPv6 VXLAN Anycast IP addresses
        Conserves IPv6 addresses in VXLAN deployments as it doesn't require unique IPv6
        addresses on each node.
        """
        ip_address_virtual_secondaries: list[str] | None = None
        """
        Secondary IPv4 VXLAN Anycast IP addresses
        """
        ip_virtual_router_addresses: list[str] | None = None
        """
        IPv4 VARP addresses.
        Requires an IP address to be configured on the SVI.
        If ip_address_virtual is also set,
        ip_virtual_router_addresses will take precedence
        _if_ there is an ip_address configured for the node.
        """
        ipv6_virtual_router_addresses: list[str] | None = None
        """
        IPv6 VARP addresses.
        Requires an IPv6 address to be configured on the SVI.
        If ipv6_address_virtuals is also set,
        ipv6_virtual_router_addresses will take precedence
        _if_ there is an ipv6_address configured for the node.
        """
        ip_helpers: list[IpHelpersItem] | None = None
        """
        IP helper for DHCP relay
        """
        vni_override: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=16777215)
        """
        By default the VNI will be derived from "mac_vrf_vni_base".
        The vni_override allows us to override this value and
        statically define it (optional).
        """
        rt_override: Annotated[str, StrConvert(convert_types=(int))] | None = None
        """
        By default the MAC VRF RT will be derived from mac_vrf_id_base + vlan_id.
        The rt_override allows us to override this
        value and statically define it.
        rt_override will default to vni_override if set.

        rt_override supports two formats:
          -
        A single number which will be used in the RT fields instead of mac_vrf_id/mac_vrf_vni (see 'overlay_rt_type' for
        details).
          - A full RT string with colon seperator which will override the full RT.
        """
        rd_override: Annotated[str, StrConvert(convert_types=(int))] | None = None
        """
        By default the MAC VRF RD will be derived from mac_vrf_id_base + vlan_id.
        The rt_override allows us to override this
        value and statically define it.
        rd_override will default to rt_override or vni_override if set.

        rd_override supports
        two formats:
          - A single number which will be used in the RD assigned number field instead of mac_vrf_id/mac_vrf_vni
        (see 'overlay_rd_type' for details).
          - A full RD string with colon seperator which will override the full RD.
        """
        trunk_groups: list[str] | None = None
        evpn_l2_multicast: EvpnL2Multicast | None = None
        """
        Explicitly enable or disable evpn_l2_multicast to override setting of
        `<network_services_key>.[].evpn_l2_multicast.enabled`.
        When evpn_l2_multicast.enabled is set to true for a vlan or a
        tenant, "igmp snooping" and "igmp snooping querier" will always be enabled, overriding those individual settings.
        Requires `evpn_multicast` to also be set to `true`.
        """
        evpn_l3_multicast: EvpnL3Multicast | None = None
        """
        Explicitly enable or disable evpn_l3_multicast to override setting of
        `<network_services_key>.[].evpn_l3_multicast.enabled` and `<network_services_key>.[].vrfs.[].evpn_l3_multicast.enabled`.
        Requires `evpn_multicast` to also be set to `true`.
        """
        igmp_snooping_enabled: bool | None = None
        """
        Enable IGMP Snooping (Enabled by default on EOS).
        """
        igmp_snooping_querier: IgmpSnoopingQuerier | None = None
        vxlan: bool | None = True
        """
        Extend this SVI over VXLAN.
        """
        spanning_tree_priority: Annotated[int, IntConvert(convert_types=(str))] | None = None
        """
        Setting spanning-tree priority per VLAN is only supported with `spanning_tree_mode: rapid-pvst` under node type
        settings.
        The default priority for rapid-PVST is set under the node type settings with `spanning_tree_priority`
        (default=32768).
        """
        mtu: Annotated[int, IntConvert(convert_types=(str))] | None = None
        """
        Interface MTU.
        """
        ospf: Ospf | None = None
        """
        OSPF interface configuration.
        """
        bgp: Bgp | None = None
        raw_eos_cli: str | None = None
        """
        EOS CLI rendered directly on the VLAN interface in the final EOS configuration.
        """
        structured_config: StructuredConfig | None = None
        """
        Custom structured config added under vlan_interfaces.[name=<interface>] for eos_cli_config_gen.
        """

    class TrunkGroups(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Mlag(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str | None = "MLAG"

        class MlagL3(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str | None = "LEAF_PEER_L3"

        class Uplink(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str | None = "UPLINK"

        mlag: Mlag | None = None
        """
        Trunk Group used for MLAG VLAN (Typically VLAN 4094).
        """
        mlag_l3: MlagL3 | None = None
        """
        Trunk Group used for MLAG L3 peering VLAN and for VRF L3 peering VLANs (Typically VLAN 4093).
        """
        uplink: Uplink | None = None
        """
        Trunk Group used on L2 Leaf switches when "enable_trunk_groups" is set.
        """

    class UnderlayMulticastAnycastRp(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        mode: Literal["pim", "msdp"] | None = "pim"

    class UnderlayMulticastRpsItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class NodesItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str = None
            """
            Hostname.
            """
            loopback_number: Annotated[int, IntConvert(convert_types=(str))] = None
            description: str | None = "PIM RP"
            """
            Interface description.
            """

        rp: str = None
        """
        RP IPv4 address.
        """
        nodes: list[NodesItem] | None = None
        """
        List of nodes where a Loopback interface with the RP address will be configured.
        """
        groups: list[str] | None = None
        """
        List of groups to associate with the RP address set in 'rp'.
        If access_list_name is set, a standard access-list will be
        configured matching these groups.
        Otherwise the groups are configured directly on the RP command.
        """
        access_list_name: Annotated[str, StrConvert(convert_types=(int))] | None = None
        """
        Name of standard Access-List.
        """

    class UplinkPtp(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        enable: bool | None = False

    class WanCarriersItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        name: str = None
        """
        Carrier name.
        """
        description: str | None = None
        """
        Additional information about the carrier for documentation purposes.
        """
        path_group: str = None
        """
        The path-group to which this carrier belongs.
        """
        trusted: bool | None = False
        """
        Set this to `true` to mark this carrier as "trusted".
        WAN interfaces require an inbound access-list to be set unless the
        carrier is "trusted".
        """

    class WanHa(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        lan_ha_path_group_name: str | None = "LAN_HA"
        """
        When WAN HA is enabled for a site if `wan_mode: cv-pathfinder`, a default path-group is injected to form DPS tunnels
        over LAN.
        This key allows to overwrite the default LAN HA path-group name.
        """

    class WanIpsecProfiles(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class ControlPlane(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            ike_policy_name: str | None = "CP-IKE-POLICY"
            """
            Name of the IKE policy.
            """
            sa_policy_name: str | None = "CP-SA-POLICY"
            """
            Name of the SA policy.
            """
            profile_name: str | None = "CP-PROFILE"
            """
            Name of the IPSec profile.
            """
            shared_key: str = None
            """
            The IPSec shared key.
            This variable is sensitive and SHOULD be configured using some vault mechanism.
            """

        class DataPlane(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            ike_policy_name: str | None = "DP-IKE-POLICY"
            """
            Name of the IKE policy.
            """
            sa_policy_name: str | None = "DP-SA-POLICY"
            """
            Name of the SA policy.
            """
            profile_name: str | None = "DP-PROFILE"
            """
            Name of the IPSec profile.
            """
            shared_key: str = None
            """
            The type 7 encrypted IPSec shared key.
            This variable is sensitive and should be configured using some vault mechanism.
            """

        control_plane: ControlPlane = None
        data_plane: DataPlane | None = None
        """
        If `data_plane` is not defined, `control_plane` information is used for both.
        """

    class WanPathGroupsItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Ipsec(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            dynamic_peers: bool | None = True
            """
            Enable IPSec for dynamic peers.
            """
            static_peers: bool | None = True
            """
            Enable IPSec for static peers.
            """

        class ImportPathGroupsItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            remote: str | None = None
            """
            Remote path-group to import.
            """
            local: str | None = None
            """
            Optional, if not set, the path-group `name` is used as local.
            """

        class DpsKeepalive(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            interval: Annotated[str, StrConvert(convert_types=(int))] | None = None
            """
            Interval in milliseconds. Valid values are 50-60000 | "auto"

            When auto, the interval and failure_threshold are
            automatically determined based on
            path state.
            """
            failure_threshold: Annotated[int, IntConvert(convert_types=(str))] | None = Field(5, ge=2, le=100)
            """
            Failure threshold in number of lost keep-alive messages.
            """

        name: str = None
        """
        Path-group name.
        """
        id: Annotated[int, IntConvert(convert_types=(str))] = None
        """
        Path-group id.
        Required until an auto ID algorithm is implemented.
        """
        description: str | None = None
        """
        Additional information about the path-group for documentation purposes.
        """
        ipsec: Ipsec | None = None
        """
        Configuration of IPSec at the path-group level.
        """
        import_path_groups: list[ImportPathGroupsItem] | None = None
        """
        List of path-groups to import in this path-group.
        """
        default_preference: Annotated[str, StrConvert(convert_types=(int))] | None = "preferred"
        """
        Preference value used when a preference is not given for a path-group in the `wan_virtual_topologies.policies` input or
        when
        the path-group is used in an auto generated policy except if `excluded_from_default_policy` is set to `true.

        Valid
        values are 1-65535 | "preferred" | "alternate".

        `preferred` is converted to priority 1.
        `alternate` is converted to
        priority 2.
        """
        excluded_from_default_policy: bool | None = False
        """
        When set to `true`, the path-group is excluded from AVD auto generated policies.
        """
        dps_keepalive: DpsKeepalive | None = None
        """
        Period between the transmission of consecutive keepalive messages, and failure threshold.
        """

    class WanRouteServersItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class PathGroupsItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class InterfacesItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                name: str = None
                """
                Interface name.
                """
                public_ip: str | None = None
                """
                The public IPv4 address (without mask) of the Route Reflector for this path-group.
                """

            name: str = None
            """
            Path-group name.
            """
            interfaces: list[InterfacesItem] = Field(None, min_length=1)

        hostname: str = None
        """
        Route-Reflector hostname.
        """
        vtep_ip: str | None = None
        """
        Route-Reflector VTEP IP Address. This is usually the IP address under `interface Dps1`.
        """
        path_groups: list[PathGroupsItem] | None = None
        """
        Path-groups through which the Route Reflector/Pathfinder is reached.
        """

    class WanVirtualTopologies(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class VrfsItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: Annotated[str, StrConvert(convert_types=(int))] = None
            """
            VRF name.
            """
            policy: str | None = "DEFAULT-POLICY"
            """
            Name of the policy to apply to this VRF.
            AVD will auto generate a default policy DEFAULT-POLICY and apply it to the
            VRF(s)
            where the `policy` key is not set.
            It is possible to overwrite the default policy for all VRFs using it
            by
            redefining it in the `wan_virtual_topologies.policies` list using the
            default name `DEFAULT-POLICY`.
            """
            wan_vni: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=1, le=255)
            """
            Required for VRFs carried over AutoVPN or CV Pathfinder WAN.

            A VRF can have different VNIs between the Datacenters and
            the WAN.
            Note that if no VRF default is configured for WAN, AVD will automatically inject the VRF default with
            `wan_vni`
            set to `1`.
            In addition either `vrf_id` or `vrf_vni` must be set to enforce consistent route-targets across domains.
            """

        class ControlPlaneVirtualTopology(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Constraints(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                jitter: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=10000)
                """
                Jitter requirement for this load balance policy in milliseconds.
                """
                latency: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=10000)
                """
                One way delay requirement for this load balance policy in milliseconds.
                """
                loss_rate: Annotated[str, StrConvert(convert_types=(int, float))] | None = Field(None, pattern=r"^\d+(\.\d{1,2})?$")
                """
                Loss Rate requirement in percentage for this load balance policy.
                Value between 0.00 and 100.00.
                """

            class PathGroupsItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                names: list[str] = Field(None, min_length=1)
                """
                List of path-group names.
                """
                preference: Annotated[str, StrConvert(convert_types=(int))] | None = None
                """
                Valid values are 1-65535 | "preferred" | "alternate".

                "preferred" is converted to priority 1.
                "alternate" is converted
                to priority 2.

                If not set, each path-group in `names` will be attributed its `default_preference`.
                """

            name: str | None = None
            """
            Optional name, if not set `CONTROL-PLANE-PROFILE` is used.
            """
            application_profile: str | None = "APP-PROFILE-CONTROL-PLANE"
            """
            The application profile to use for control plane traffic.

            The application profile should be defined under
            `application_classification.application_profiles`.
            If not defined AVD will auto generate an application profile using
            the provided name or the default value.

            If not overwritten elsewhere, the application profile is generated matching one
            application matching the control plane traffic either sourced from or destined to the WAN route servers.
            """
            traffic_class: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=7)
            """
            Set traffic-class for matched traffic.
            """
            dscp: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=63)
            """
            Set DSCP for matched traffic.
            """
            lowest_hop_count: bool | None = False
            """
            Prefer paths with lowest hop-count.
            Only applicable for `wan_mode: "cv-pathfinder"`.
            """
            constraints: Constraints | None = None
            path_groups: list[PathGroupsItem] | None = Field(None, min_length=1)

        class PoliciesItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class ApplicationVirtualTopologiesItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Constraints(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    jitter: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=10000)
                    """
                    Jitter requirement for this load balance policy in milliseconds.
                    """
                    latency: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=10000)
                    """
                    One way delay requirement for this load balance policy in milliseconds.
                    """
                    loss_rate: Annotated[str, StrConvert(convert_types=(int, float))] | None = Field(None, pattern=r"^\d+(\.\d{1,2})?$")
                    """
                    Loss Rate requirement in percentage for this load balance policy.
                    Value between 0.00 and 100.00.
                    """

                class PathGroupsItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    names: list[str] = Field(None, min_length=1)
                    """
                    List of path-group names.
                    """
                    preference: Annotated[str, StrConvert(convert_types=(int))] | None = None
                    """
                    Valid values are 1-65535 | "preferred" | "alternate".

                    "preferred" is converted to priority 1.
                    "alternate" is converted
                    to priority 2.

                    If not set, each path-group in `names` will be attributed its `default_preference`.
                    """

                application_profile: str = None
                """
                The application profile to use for this virtual topology. It must be a defined
                `application_classification.application_profile`.
                """
                name: str | None = None
                """
                Optional name, if not set `<policy_name>-<application_profile>` is used.
                """
                id: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=2, le=253)
                """
                ID of the AVT in each VRFs. ID must be unique across all virtual topologies in a policy.
                ID 1 is reserved for the
                default_virtual_toplogy.
                ID 254 is reserved for the control_plane_virtual_topology.

                `id` is required when `wan_mode` is
                'cv-pathfinder'.
                """
                traffic_class: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=7)
                """
                Set traffic-class for matched traffic.
                """
                dscp: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=63)
                """
                Set DSCP for matched traffic.
                """
                lowest_hop_count: bool | None = False
                """
                Prefer paths with lowest hop-count.
                Only applicable for `wan_mode: "cv-pathfinder"`.
                """
                constraints: Constraints | None = None
                path_groups: list[PathGroupsItem] | None = Field(None, min_length=1)

            class DefaultVirtualTopology(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Constraints(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    jitter: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=10000)
                    """
                    Jitter requirement for this load balance policy in milliseconds.
                    """
                    latency: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=10000)
                    """
                    One way delay requirement for this load balance policy in milliseconds.
                    """
                    loss_rate: Annotated[str, StrConvert(convert_types=(int, float))] | None = Field(None, pattern=r"^\d+(\.\d{1,2})?$")
                    """
                    Loss Rate requirement in percentage for this load balance policy.
                    Value between 0.00 and 100.00.
                    """

                class PathGroupsItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    names: list[str] = Field(None, min_length=1)
                    """
                    List of path-group names.
                    """
                    preference: Annotated[str, StrConvert(convert_types=(int))] | None = None
                    """
                    Valid values are 1-65535 | "preferred" | "alternate".

                    "preferred" is converted to priority 1.
                    "alternate" is converted
                    to priority 2.

                    If not set, each path-group in `names` will be attributed its `default_preference`.
                    """

                name: str | None = None
                """
                Optional name, if not set `<policy_name>-DEFAULT` is used.
                """
                drop_unmatched: bool | None = False
                """
                When set, no `catch-all` match is configured for the policy and unmatched traffic is dropped.
                """
                traffic_class: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=7)
                """
                Set traffic-class for matched traffic.
                """
                dscp: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=63)
                """
                Set DSCP for matched traffic.
                """
                lowest_hop_count: bool | None = False
                """
                Prefer paths with lowest hop-count.
                Only applicable for `wan_mode: "cv-pathfinder"`.
                """
                constraints: Constraints | None = None
                path_groups: list[PathGroupsItem] | None = Field(None, min_length=1)

            name: str = None
            """
            Name of the AVT policy.
            """
            application_virtual_topologies: list[ApplicationVirtualTopologiesItem] | None = None
            """
            List of application specific virtual topologies.
            """
            default_virtual_topology: DefaultVirtualTopology = None
            """
            Default match for the policy.
            If no default match should be configured, set `drop_unmatched` to `true`.
            Otherwise, in CV
            Pathfinder mode, a default AVT profile will be configured with ID 1.
            """

        vrfs: list[VrfsItem] | None = None
        """
        Map a VRF that exists in network_services to an AVT policy.
        """
        control_plane_virtual_topology: ControlPlaneVirtualTopology | None = None
        """
        Always injected into the default VRF policy as the first entry.

        By default, if no path-groups are specified, all
        locally available path-groups
        are used in the generated load-balance policy.
        ID is hardcoded to 254 for the AVT profile
        in CV Pathfinder mode.
        """
        policies: list[PoliciesItem] | None = None
        """
        List of virtual toplogies policies.

        For AutoVPN, each item in the list creates:
          * one policy with:
              * one
        `match` entry per `application_virtual_topologies` item
                they are indexed using `10 * <list_index>` where
        `list_index` starts at `1`.
              * one `default-match`
          * one load-balance policy per `application_virtual_topologies`
        and one for the `default_virtual_topology`.
          * if the policy is associated with the default VRF, a special control-
        plane rule is injected
            in the policy with index `1` referring to a control-plane load-balance policy as defined
        under
            `control_plane_virtual_topology` or if not set, the default one.

        For CV Pathfinder, each item in the list
        creates:
          * one policy with:
              * one `match` entry per `application_virtual_topologies` item ordered as in the
        data.
              * one last match entry for the `default` application-profile using `default_virtual_topology` information.
        * one profile per `application_virtual_topologies` item.
          * one profile for the `default_virtual_topology`.
          * one
        load-balance policy per `application_virtual_topologies`.
          * one load_balance policy for the
        `default_virtual_topology`.
          * if the policy is associated with the default VRF, a special control-plane profile is
        configured
            and injected first in the policy assigned to the `default` VRF. This profile points to a
            control-
        plane load-balance policy as defined under `control_plane_virtual_topology` or if not set, the default one.
        """

    class CustomStructuredConfiguration(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        key: str
        """
        Complete key including prefix
        """
        value: EosCliConfigGen
        """
        Structured config including the suffix part of the key.
        """

    class DynamicKeys(BaseModel):
        """
        Data models for dynamic keys
        """

        model_config = ConfigDict(defer_build=True, extra="forbid")

        class DynamicConnectedEndpointsKeys(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class ConnectedEndpointsKeysKeyItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class AdaptersItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class Flowcontrol(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        received: Literal["received", "send", "on"] | None = None

                    class Ptp(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        enabled: bool | None = False
                        endpoint_role: Literal["bmca", "default", "follower"] | None = "follower"
                        profile: Literal["aes67", "aes67-r16-2016", "smpte2059-2"] | None = "aes67-r16-2016"

                    class LinkTracking(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        enabled: bool | None = None
                        name: str | None = None
                        """
                        Tracking group name.
                        The default group name is taken from fabric variable of the switch, `link_tracking.groups[0].name`
                        with default value being "LT_GROUP1".
                        Optional if default link_tracking settings are configured on the node.
                        """

                    class Dot1x(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        class Pae(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            mode: Literal["authenticator"] | None = None

                        class AuthenticationFailure(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            action: Literal["allow", "drop"] | None = None
                            allow_vlan: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=4094)

                        class HostMode(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            mode: Literal["multi-host", "single-host"] | None = None
                            multi_host_authenticated: bool | None = None

                        class MacBasedAuthentication(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            enabled: bool | None = None
                            always: bool | None = None
                            host_mode_common: bool | None = None

                        class Timeout(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            idle_host: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=10, le=65535)
                            quiet_period: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)
                            reauth_period: Annotated[str, StrConvert(convert_types=(int))] | None = None
                            """
                            Range 60-4294967295 or "server".
                            """
                            reauth_timeout_ignore: bool | None = None
                            tx_period: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)

                        class Unauthorized(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            access_vlan_membership_egress: bool | None = None
                            native_vlan_membership_egress: bool | None = None

                        port_control: Literal["auto", "force-authorized", "force-unauthorized"] | None = None
                        port_control_force_authorized_phone: bool | None = None
                        reauthentication: bool | None = None
                        pae: Pae | None = None
                        authentication_failure: AuthenticationFailure | None = None
                        host_mode: HostMode | None = None
                        mac_based_authentication: MacBasedAuthentication | None = None
                        timeout: Timeout | None = None
                        reauthorization_request_limit: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=10)
                        unauthorized: Unauthorized | None = None

                    class Poe(EosCliConfigGen.EthernetInterfacesItem.Poe, BaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        pass

                    class StormControl(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        class All(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            level: Annotated[str, StrConvert(convert_types=(int, float))] | None = None
                            """
                            Configure maximum storm-control level.
                            """
                            unit: Literal["percent", "pps"] | None = "percent"
                            """
                            Optional variable and is hardware dependent.
                            """

                        class Broadcast(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            level: Annotated[str, StrConvert(convert_types=(int, float))] | None = None
                            """
                            Configure maximum storm-control level.
                            """
                            unit: Literal["percent", "pps"] | None = "percent"
                            """
                            Optional variable and is hardware dependent.
                            """

                        class Multicast(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            level: Annotated[str, StrConvert(convert_types=(int, float))] | None = None
                            """
                            Configure maximum storm-control level.
                            """
                            unit: Literal["percent", "pps"] | None = "percent"
                            """
                            Optional variable and is hardware dependent.
                            """

                        class UnknownUnicast(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            level: Annotated[str, StrConvert(convert_types=(int, float))] | None = None
                            """
                            Configure maximum storm-control level.
                            """
                            unit: Literal["percent", "pps"] | None = "percent"
                            """
                            Optional variable and is hardware dependent.
                            """

                        all: All | None = None
                        broadcast: Broadcast | None = None
                        multicast: Multicast | None = None
                        unknown_unicast: UnknownUnicast | None = None

                    class MonitorSessionsItem(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        class SourceSettings(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            class AccessGroup(AvdDictBaseModel):
                                model_config = ConfigDict(defer_build=True, extra="forbid")

                                type: Literal["ip", "ipv6", "mac"] | None = None
                                name: str | None = None
                                """
                                ACL name.
                                """
                                priority: Annotated[int, IntConvert(convert_types=(str))] | None = None

                            direction: Literal["rx", "tx", "both"] | None = None
                            access_group: AccessGroup | None = None

                        class SessionSettings(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            class AccessGroup(AvdDictBaseModel):
                                model_config = ConfigDict(defer_build=True, extra="forbid")

                                type: Literal["ip", "ipv6", "mac"] | None = None
                                name: str | None = None
                                """
                                ACL name.
                                """

                            class Truncate(AvdDictBaseModel):
                                model_config = ConfigDict(defer_build=True, extra="forbid")

                                enabled: bool | None = None
                                size: Annotated[int, IntConvert(convert_types=(str))] | None = None
                                """
                                Size in bytes
                                """

                            encapsulation_gre_metadata_tx: bool | None = None
                            header_remove_size: Annotated[int, IntConvert(convert_types=(str))] | None = None
                            """
                            Number of bytes to remove from header.
                            """
                            access_group: AccessGroup | None = None
                            rate_limit_per_ingress_chip: str | None = None
                            """
                            Ratelimit and unit as string.
                            Examples:
                              "100000 bps"
                              "100 kbps"
                              "10 mbps"
                            """
                            rate_limit_per_egress_chip: str | None = None
                            """
                            Ratelimit and unit as string.
                            Examples:
                              "100000 bps"
                              "100 kbps"
                              "10 mbps"
                            """
                            sample: Annotated[int, IntConvert(convert_types=(str))] | None = None
                            truncate: Truncate | None = None

                        name: str = None
                        """
                        Session name.
                        """
                        role: Literal["source", "destination"] | None = None
                        source_settings: SourceSettings | None = None
                        session_settings: SessionSettings | None = None
                        """
                        Session settings are defined per session name.
                        Different session_settings for the same session name will be
                        combined/merged.
                        """

                    class EthernetSegment(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        short_esi: str = None
                        """
                        In format xxxx:xxxx:xxxx or "auto".
                        Define a manual short-esi (be careful using this on profiles) or set the value to
                        "auto" to automatically generate the value.
                        Please see the notes under "EVPN A/A ESI dual and single-attached endpoint
                        scenarios" before setting `short_esi: auto`.
                        """
                        redundancy: Literal["all-active", "single-active"] | None = None
                        """
                        If omitted, Port-Channels use the EOS default of all-active.
                        If omitted, Ethernet interfaces are configured as single-
                        active.
                        """
                        designated_forwarder_algorithm: Literal["auto", "modulus", "preference"] | None = None
                        """
                        Configure DF algorithm and preferences.
                        - auto: Use preference-based algorithm and assign preference based on position
                        of device in the 'switches' list,
                          e.g., assuming a list of three switches, this would assign a preference of 200 to
                        the first switch, 100 to the 2nd, and 0 to the third.
                        - preference: Set preference for each switch manually using
                        designated_forwarder_preferences key.
                        - modulus: Use the default modulus-based algorithm.
                        If omitted, Port-Channels use
                        the EOS default of modulus.
                        If omitted, Ethernet interfaces default to the 'auto' mechanism detailed above.
                        """
                        designated_forwarder_preferences: list[Annotated[int, IntConvert(convert_types=(str))]] | None = None
                        """
                        Manual preference as described above, required only for preference algorithm.
                        """
                        dont_preempt: bool | None = None
                        """
                        Disable preemption for single-active forwarding when auto/manual DF preference is configured.
                        """

                    class PortChannel(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        class LacpFallback(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            class Individual(AvdDictBaseModel):
                                model_config = ConfigDict(defer_build=True, extra="forbid")

                                profile: str | None = None
                                """
                                Port-profile name to inherit configuration.
                                """

                            mode: Literal["static", "individual"] | None = None
                            """
                            Either static or individual mode is supported.
                            If the mode is set to "individual" the "individual.profile" setting must
                            be defined.
                            """
                            individual: Individual | None = None
                            """
                            Define parameters for port-channel member interfaces. Applies only if LACP fallback is set to "individual".
                            """
                            timeout: Annotated[int, IntConvert(convert_types=(str))] | None = None
                            """
                            Timeout in seconds. EOS default is 90 seconds.
                            """

                        class LacpTimer(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            mode: Literal["normal", "fast"] | None = None
                            """
                            LACP mode for interface members.
                            """
                            multiplier: Annotated[int, IntConvert(convert_types=(str))] | None = None
                            """
                            Number of LACP BPDUs lost before deeming the peer down. EOS default is 3.
                            """

                        class SubinterfacesItem(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            class EncapsulationVlan(AvdDictBaseModel):
                                model_config = ConfigDict(defer_build=True, extra="forbid")

                                client_dot1q: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=4094)

                            number: Annotated[int, IntConvert(convert_types=(str))] | None = None
                            """
                            Subinterface number
                            """
                            short_esi: str | None = None
                            """
                            In format xxxx:xxxx:xxxx or "auto"
                            Required for multihomed port-channels with subinterfaces
                            """
                            vlan_id: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=4094)
                            """
                            VLAN ID to bridge.
                            Default is subinterface number.
                            """
                            encapsulation_vlan: EncapsulationVlan | None = None
                            """
                            Client VLAN ID encapsulation.
                            Default is subinterface number.
                            """

                        class StructuredConfig(EosCliConfigGen.PortChannelInterfacesItem, BaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            pass

                        mode: Literal["active", "passive", "on"] | None = None
                        """
                        Port-Channel Mode.
                        """
                        channel_id: Annotated[int, IntConvert(convert_types=(str))] | None = None
                        """
                        Port-Channel ID.
                        If no channel_id is specified, an id is generated from the first switch port in the port channel.
                        """
                        description: str | None = None
                        """
                        By default the description is built leveraging `<peer>` name or `adapter.description` when defined.
                        When this key is
                        defined, it will append its content to the physical port description.
                        """
                        enabled: bool | None = True
                        """
                        Port-Channel administrative state.
                        Setting to false will set port to 'shutdown' in intended configuration.
                        """
                        short_esi: str | None = None
                        """
                        In format xxxx:xxxx:xxxx or "auto".
                        """
                        lacp_fallback: LacpFallback | None = None
                        """
                        LACP fallback configuration.
                        """
                        lacp_timer: LacpTimer | None = None
                        """
                        LACP timer configuration. Applies only when Port-channel mode is not "on".
                        """
                        subinterfaces: list[SubinterfacesItem] | None = None
                        """
                        Port-Channel L2 Subinterfaces
                        Subinterfaces are only supported on routed port-channels, which means they cannot be
                        configured on MLAG port-channels.
                        Setting short_esi: auto generates the short_esi automatically using a hash of
                        configuration elements.
                        Please see the notes under "EVPN A/A ESI dual-attached endpoint scenario" before setting
                        short_esi: auto.
                        """
                        raw_eos_cli: str | None = None
                        """
                        EOS CLI rendered directly on the port-channel interface in the final EOS configuration.
                        """
                        structured_config: StructuredConfig | None = None
                        """
                        Custom structured config added under port_channel_interfaces.[name=<interface>] for eos_cli_config_gen.
                        """

                    class StructuredConfig(EosCliConfigGen.EthernetInterfacesItem, BaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        pass

                    switch_ports: list[str] = None
                    """
                    List of switch interfaces.
                    The lists `endpoint_ports`, `switch_ports`, and `switches` must have the same length.
                    """
                    switches: list[str] = None
                    """
                    List of switches.
                    The lists `endpoint_ports`, `switch_ports`, and `switches` must have the same length.
                    """
                    endpoint_ports: list[str] | None = None
                    """
                    Endpoint ports is used for description, required unless `description` or `descriptions` is set.
                    The lists
                    `endpoint_ports`, `switch_ports`, `descriptions` and `switches` must have the same length.
                    Each list item is one
                    switchport.
                    """
                    descriptions: list[Any] | None = None
                    """
                    Unique description per port. When set, takes priority over description.
                    """
                    speed: str | None = None
                    """
                    Set adapter speed in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`.
                    If not
                    specified speed will be auto.
                    """
                    description: str | None = None
                    """
                    By default the description is built leveraging `<peer>_<peer_interface>`.
                    When set this key will overide the default
                    value on the physical ports.
                    """
                    profile: str | None = None
                    """
                    Port-profile name to inherit configuration.
                    """
                    enabled: bool | None = True
                    """
                    Administrative state, setting to false will set the port to 'shutdown' in the intended configuration.
                    """
                    mode: Literal["access", "dot1q-tunnel", "trunk", "trunk phone"] | None = None
                    """
                    Interface mode.
                    """
                    mtu: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=68, le=65535)
                    l2_mtu: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=68, le=65535)
                    """
                    "l2_mtu" should only be defined for platforms supporting the "l2 mtu" CLI
                    """
                    l2_mru: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=68, le=65535)
                    """
                    "l2_mru" should only be defined for platforms supporting the "l2 mru" CLI
                    """
                    native_vlan: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=4094)
                    """
                    Native VLAN for a trunk port.
                    If both `native_vlan` and `native_vlan_tag`, `native_vlan_tag` takes precedence.
                    """
                    native_vlan_tag: bool | None = False
                    """
                    If both `native_vlan` and `native_vlan_tag`, `native_vlan_tag` takes precedence.
                    """
                    phone_vlan: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=4094)
                    """
                    Phone VLAN for a mode `trunk phone` port.
                    Requires `mode: trunk phone` to be set.
                    """
                    phone_trunk_mode: Literal["tagged", "untagged", "tagged phone", "untagged phone"] | None = None
                    """
                    Specify if the phone traffic is tagged or untagged.
                    If both data and phone traffic are untagged, MAC-Based VLAN
                    Assignment (MBVA) is used, if supported by the model of switch.
                    """
                    trunk_groups: list[str] | None = None
                    """
                    Required with `enable_trunk_groups: true`.
                    Trunk Groups are used for limiting VLANs on trunk ports to VLANs with the
                    same Trunk Group.
                    """
                    vlans: Annotated[str, StrConvert(convert_types=(int))] | None = None
                    """
                    Interface VLANs - if not set, the EOS default is that all VLANs are allowed for trunk ports, and VLAN 1 will be used for
                    access ports.
                    """
                    spanning_tree_portfast: Literal["edge", "network"] | None = None
                    spanning_tree_bpdufilter: (
                        Annotated[Literal["enabled", "disabled", "True", "False", "true", "false"], StrConvert(convert_types=(bool))] | None
                    ) = None
                    spanning_tree_bpduguard: (
                        Annotated[Literal["enabled", "disabled", "True", "False", "true", "false"], StrConvert(convert_types=(bool))] | None
                    ) = None
                    flowcontrol: Flowcontrol | None = None
                    qos_profile: str | None = None
                    """
                    QOS profile name
                    """
                    ptp: Ptp | None = None
                    """
                    The global PTP profile parameters will be applied to all connected endpoints where `ptp` is manually enabled.
                    `ptp role
                    master` is set to ensure control over the PTP topology.
                    """
                    sflow: bool | None = None
                    """
                    Configures sFlow on the interface. Overrides `fabric_sflow` setting.
                    """
                    link_tracking: LinkTracking | None = None
                    """
                    Configure the downstream interfaces of a respective Link Tracking Group.
                    If `port_channel` is defined in an adapter,
                    then the port-channel interface is configured to be the downstream.
                    Else all the ethernet interfaces will be configured
                    as downstream -> to configure single-active EVPN multihomed networks.
                    """
                    dot1x: Dot1x | None = None
                    """
                    802.1x
                    """
                    poe: Poe | None = None
                    """
                    Power Over Ethernet settings applied on port. Only configured if platform supports PoE.
                    """
                    storm_control: StormControl | None = None
                    """
                    Storm control settings applied on port toward the endpoint.
                    """
                    monitor_sessions: list[MonitorSessionsItem] | None = None
                    """
                    Used to define switchports as source or destination for monitoring sessions.
                    """
                    ethernet_segment: EthernetSegment | None = None
                    """
                    Settings for all or single-active EVPN multihoming.
                    """
                    port_channel: PortChannel | None = None
                    """
                    Used for port-channel adapter.
                    """
                    validate_state: bool | None = None
                    """
                    Set to false to disable interface validation by the `eos_validate_state` role.
                    """
                    raw_eos_cli: str | None = None
                    """
                    EOS CLI rendered directly on the ethernet interface in the final EOS configuration.
                    """
                    structured_config: StructuredConfig | None = None
                    """
                    Custom structured config added under ethernet_interfaces.[name=<interface>] for eos_cli_config_gen.
                    """

                name: str = None
                """
                Endpoint name will be used in the switchport description.
                """
                rack: str | None = None
                """
                Rack is used for documentation purposes only.
                """
                adapters: list[AdaptersItem] | None = None
                """
                A list of adapters, group by adapters leveraging the same port-profile.
                """

            key: str
            """
            Key used as dynamic key
            """
            value: list[ConnectedEndpointsKeysKeyItem] | None = Field(None, title="Connected Endpoints")
            """
            Value of dynamic key
            """

        class DynamicNetworkServicesKeys(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class NetworkServicesKeysNameItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class BgpPeerGroupsItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class AsPath(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        remote_as_replace_out: bool | None = None
                        """
                        Replace AS number with local AS number
                        """
                        prepend_own_disabled: bool | None = None
                        """
                        Disable prepending own AS number to AS path
                        """

                    class RemovePrivateAs(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        enabled: bool | None = None
                        all: bool | None = None
                        replace_as: bool | None = None

                    class RemovePrivateAsIngress(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        enabled: bool | None = None
                        replace_as: bool | None = None

                    class BfdTimers(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        interval: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=50, le=60000)
                        """
                        Interval in milliseconds.
                        """
                        min_rx: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=50, le=60000)
                        """
                        Rate in milliseconds.
                        """
                        multiplier: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=3, le=50)

                    class DefaultOriginate(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        enabled: bool | None = None
                        always: bool | None = None
                        route_map: str | None = None
                        """
                        Route-map name
                        """

                    class LinkBandwidth(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        enabled: bool | None = None
                        default: str | None = None
                        """
                        nn.nn(K|M|G) link speed in bits/second
                        """

                    class AllowasIn(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        enabled: bool | None = None
                        times: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=10)
                        """
                        Number of local ASNs allowed in a BGP update
                        """

                    class RibInPrePolicyRetain(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        enabled: bool | None = None
                        all: bool | None = None

                    name: str = None
                    """
                    BGP peer group name.
                    """
                    nodes: list[str] | None = None
                    """
                    Nodes is required to restrict configuration of BGP neighbors to certain nodes in the network.
                    If not set the peer-group
                    is created on devices which have a bgp_peer mapped to the corresponding peer_group.
                    """
                    type: str | None = None
                    """
                    Key only used for documentation or validation purposes
                    """
                    remote_as: Annotated[str, StrConvert(convert_types=(int))] | None = None
                    """
                    BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
                    For asdot notation in YAML inputs, the value
                    must be put in quotes, to prevent it from being interpreted as a float number.
                    """
                    local_as: Annotated[str, StrConvert(convert_types=(int))] | None = None
                    """
                    BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
                    For asdot notation in YAML inputs, the value
                    must be put in quotes, to prevent it from being interpreted as a float number.
                    """
                    description: str | None = None
                    shutdown: bool | None = None
                    as_path: AsPath | None = None
                    """
                    BGP AS-PATH options
                    """
                    remove_private_as: RemovePrivateAs | None = None
                    """
                    Remove private AS numbers in outbound AS path
                    """
                    remove_private_as_ingress: RemovePrivateAsIngress | None = None
                    peer_filter: str | None = None
                    """
                    Peer-filter name
                    note: `bgp_listen_range_prefix` and `peer_filter` should not be mixed with
                    the new `listen_ranges` key
                    above to avoid conflicts.
                    """
                    next_hop_unchanged: bool | None = None
                    update_source: str | None = None
                    """
                    IP address or interface name
                    """
                    route_reflector_client: bool | None = None
                    bfd: bool | None = None
                    """
                    Enable BFD.
                    """
                    bfd_timers: BfdTimers | None = None
                    """
                    Override default BFD timers. BFD must be enabled with `bfd: true`.
                    """
                    ebgp_multihop: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=255)
                    """
                    Time-to-live in range of hops
                    """
                    next_hop_self: bool | None = None
                    password: str | None = None
                    passive: bool | None = None
                    default_originate: DefaultOriginate | None = None
                    send_community: str | None = None
                    """
                    'all' or a combination of 'standard', 'extended', 'large' and 'link-bandwidth (w/options)'
                    """
                    maximum_routes: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=4294967294)
                    """
                    Maximum number of routes (0 means unlimited)
                    """
                    maximum_routes_warning_limit: Annotated[str, StrConvert(convert_types=(int))] | None = None
                    """
                    Maximum number of routes after which a warning is issued (0 means never warn) or
                    Percentage of maximum number of routes
                    at which to warn ("<1-100> percent")
                    """
                    maximum_routes_warning_only: bool | None = None
                    link_bandwidth: LinkBandwidth | None = None
                    allowas_in: AllowasIn | None = None
                    weight: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=65535)
                    timers: str | None = None
                    """
                    BGP Keepalive and Hold Timer values in seconds as string "<0-3600> <0-3600>"
                    """
                    rib_in_pre_policy_retain: RibInPrePolicyRetain | None = None
                    route_map_in: str | None = None
                    """
                    Inbound route-map name
                    """
                    route_map_out: str | None = None
                    """
                    Outbound route-map name
                    """
                    bgp_listen_range_prefix: str | None = None
                    """
                    IP prefix range
                    note: `bgp_listen_range_prefix` and `peer_filter` should not be mixed with
                    the new `listen_ranges` key
                    above to avoid conflicts.
                    """
                    session_tracker: str | None = None
                    ttl_maximum_hops: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=254)
                    """
                    Maximum number of hops.
                    """

                class EvpnL2Multicast(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    enabled: bool | None = None
                    underlay_l2_multicast_group_ipv4_pool: str | None = None
                    """
                    IPv4_address/Mask
                    """
                    underlay_l2_multicast_group_ipv4_pool_offset: Annotated[int, IntConvert(convert_types=(str))] | None = None

                class EvpnL3Multicast(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class EvpnPegItem(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        nodes: list[str] | None = None
                        """
                        A description will be applied to all nodes with RP addresses configured if not set.
                        """
                        transit: bool | None = None
                        """
                        Enable EVPN PEG transit mode.
                        """

                    enabled: bool | None = None
                    evpn_underlay_l3_multicast_group_ipv4_pool: str = None
                    """
                    IPv4_address/Mask
                    """
                    evpn_underlay_l3_multicast_group_ipv4_pool_offset: Annotated[int, IntConvert(convert_types=(str))] | None = None
                    evpn_peg: list[EvpnPegItem] | None = None
                    """
                    For each group of nodes, allow configuration of EVPN PEG options.
                    The first group of settings where the device's
                    hostname is present in the 'nodes' list will be used.
                    """

                class PimRpAddressesItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    rps: list[str] | None = Field(None, min_length=1)
                    """
                    List of Rendevouz Points.
                    """
                    nodes: list[str] | None = None
                    """
                    Restrict configuration to specific nodes.
                    Configuration Will be applied to all nodes if not set.
                    """
                    groups: list[str] | None = None
                    access_list_name: Annotated[str, StrConvert(convert_types=(int))] | None = None
                    """
                    List of groups to associate with the RP address set in 'rp'.
                    If access_list_name is set, a standard access-list will be
                    configured matching these groups.
                    Otherwise the groups are configured directly on the RP command.
                    """

                class IgmpSnoopingQuerier(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    enabled: bool | None = None
                    """
                    Will be enabled automatically if "evpn_l2_multicast" is enabled.
                    """
                    source_address: str | None = None
                    """
                    Default IP address of Loopback0
                    """
                    version: Annotated[Literal[1, 2, 3], IntConvert(convert_types=(str))] | None = 2

                class VrfsItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class IpHelpersItem(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        ip_helper: str = None
                        """
                        IPv4 DHCP server IP.
                        """
                        source_interface: str | None = None
                        """
                        Interface name.
                        """
                        source_vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
                        """
                        VRF to originate DHCP relay packets to DHCP server. If not set, uses current VRF.
                        """

                    class VtepDiagnostic(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        class LoopbackIpPoolsItem(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            pod: str | None = None
                            """
                            POD name.
                            """
                            ipv4_pool: str | None = None
                            """
                            IPv4_address/Mask.
                            """

                        loopback: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=2, le=2100)
                        """
                        Loopback interface number, required when vtep_diagnotics defined.
                        """
                        loopback_description: str | None = None
                        """
                        Provide a custom description for loopback interface.
                        """
                        loopback_ip_range: str | None = None
                        """
                        IPv4_address/Mask.
                        Loopback ip range, a unique ip is derived from this ranged and assignedto each l3 leaf based on it's
                        unique id.
                        Loopback is not created unless loopback_ip_range or loopback_ip_pools are set.
                        """
                        loopback_ip_pools: list[LoopbackIpPoolsItem] | None = None
                        """
                        For inventories with multiple PODs a loopback range can be set per POD to avoid overlaps.
                        This only takes effect when
                        loopback_ip_range is not defined, ptional (loopback is not created unless loopback_ip_range or loopback_ip_pools are
                        set).
                        """

                    class Ospf(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        class RedistributeBgp(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            enabled: bool | None = True
                            route_map: str | None = None
                            """
                            Route-map name.
                            """

                        class RedistributeConnected(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            enabled: bool | None = False
                            route_map: str | None = None
                            """
                            Route-map name.
                            """

                        enabled: bool | None = None
                        process_id: Annotated[int, IntConvert(convert_types=(str))] | None = None
                        """
                        If not set, "vrf_id" will be used.
                        """
                        router_id: str | None = None
                        """
                        If not set, switch router_id will be used.
                        """
                        max_lsa: Annotated[int, IntConvert(convert_types=(str))] | None = None
                        bfd: bool | None = False
                        redistribute_bgp: RedistributeBgp | None = None
                        redistribute_connected: RedistributeConnected | None = None
                        nodes: list[str] | None = None

                    class EvpnL3Multicast(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        class EvpnPegItem(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            nodes: list[str] | None = None
                            """
                            Restrict configuration to specific nodes.
                            Will apply to all nodes with RP addresses configured if not set.
                            """
                            transit: bool | None = False
                            """
                            Enable EVPN PEG transit mode.
                            """

                        enabled: bool | None = None
                        evpn_peg: list[EvpnPegItem] | None = None
                        """
                        For each group of nodes, allow configuration of EVPN PEG features.
                        """

                    class PimRpAddressesItem(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        rps: list[str] | None = None
                        """
                        A minimum of one RP must be specified.
                        """
                        nodes: list[str] | None = None
                        """
                        Restrict configuration to specific nodes.
                        Configuration Will be applied to all nodes if not set.
                        """
                        groups: list[str] | None = None
                        access_list_name: Annotated[str, StrConvert(convert_types=(int))] | None = None
                        """
                        List of groups to associate with the RP addresses set in 'rps'.
                        If access_list_name is set, a standard access-list will
                        be configured matching these groups.
                        Otherwise the groups are configured directly on the RP command.
                        """

                    class SvisItem(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        class NodesItem(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            class IpHelpersItem(AvdDictBaseModel):
                                model_config = ConfigDict(defer_build=True, extra="forbid")

                                ip_helper: str = None
                                """
                                IPv4 DHCP server IP
                                """
                                source_interface: str | None = None
                                """
                                Interface name to originate DHCP relay packets to DHCP server.
                                """
                                source_vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
                                """
                                VRF to originate DHCP relay packets to DHCP server. If not set, EOS uses the VRF on the SVI.
                                """

                            class EvpnL2Multicast(AvdDictBaseModel):
                                model_config = ConfigDict(defer_build=True, extra="forbid")

                                enabled: bool | None = None

                            class EvpnL3Multicast(AvdDictBaseModel):
                                model_config = ConfigDict(defer_build=True, extra="forbid")

                                enabled: bool | None = None

                            class IgmpSnoopingQuerier(AvdDictBaseModel):
                                model_config = ConfigDict(defer_build=True, extra="forbid")

                                enabled: bool | None = None
                                """
                                Will be enabled automatically if evpn_l2_multicast is enabled.
                                """
                                source_address: str | None = None
                                """
                                IPv4_address
                                If not set, IP address of "Loopback0" will be used.
                                """
                                version: Annotated[Literal[1, 2, 3], IntConvert(convert_types=(str))] | None = None
                                """
                                IGMP Version (By default EOS uses IGMP version 2 for IGMP querier).
                                """

                            class Ospf(AvdDictBaseModel):
                                model_config = ConfigDict(defer_build=True, extra="forbid")

                                class MessageDigestKeysItem(AvdDictBaseModel):
                                    model_config = ConfigDict(defer_build=True, extra="forbid")

                                    id: Annotated[int, IntConvert(convert_types=(str))] | None = None
                                    hash_algorithm: Literal["md5", "sha1", "sha256", "sha384", "sha512"] | None = "sha512"
                                    key: str | None = None
                                    """
                                    Type 7 encrypted key.
                                    """

                                enabled: bool | None = None
                                point_to_point: bool | None = True
                                area: Annotated[str, StrConvert(convert_types=(int))] | None = "0"
                                """
                                OSPF area ID.
                                """
                                cost: Annotated[int, IntConvert(convert_types=(str))] | None = None
                                """
                                OSPF link cost.
                                """
                                authentication: Literal["simple", "message-digest"] | None = None
                                simple_auth_key: str | None = None
                                """
                                Password used with simple authentication.
                                """
                                message_digest_keys: list[MessageDigestKeysItem] | None = None

                            class Bgp(AvdDictBaseModel):
                                model_config = ConfigDict(defer_build=True, extra="forbid")

                                class StructuredConfig(EosCliConfigGen.RouterBgp.VlansItem, BaseModel):
                                    model_config = ConfigDict(defer_build=True, extra="forbid")

                                    pass

                                structured_config: StructuredConfig | None = None
                                """
                                Structured configuration and EOS CLI commands rendered on router_bgp.vlans.[id=<vlan>]
                                This configuration will not be
                                applied to vlan aware bundles
                                """
                                raw_eos_cli: str | None = None
                                """
                                EOS CLI rendered directly on the Router BGP, VLAN definition in the final EOS configuration.
                                """

                            class StructuredConfig(EosCliConfigGen.VlanInterfacesItem, BaseModel):
                                model_config = ConfigDict(defer_build=True, extra="forbid")

                                pass

                            node: str = None
                            """
                            l3_leaf inventory hostname
                            """
                            tags: list[Annotated[str, StrConvert(convert_types=(int))]] | None = Field(["all"], validate_default=True)
                            """
                            Tags leveraged for networks services filtering.
                            Tags are matched against "filter.tags" defined under node type settings.
                            Tags are also matched against the "node_group" name under node type settings.
                            """
                            name: str | None = None
                            """
                            VLAN name
                            """
                            enabled: bool | None = None
                            """
                            Enable or disable interface
                            """
                            description: str | None = None
                            """
                            SVI description. By default set to VLAN name.
                            """
                            ip_address: str | None = None
                            """
                            IPv4_address/Mask. Usually set under "nodes" to have unique IPv4 addresses per node.
                            """
                            ipv6_address: str | None = None
                            """
                            IPv6_address/Mask. Usually set under "nodes" to have unique IPv6 addresses per node.
                            """
                            ipv6_enable: bool | None = None
                            """
                            Explicitly enable/disable link-local IPv6 addressing.
                            """
                            ip_address_virtual: str | None = None
                            """
                            IPv4_address/Mask
                            IPv4 VXLAN Anycast IP address
                            Conserves IP addresses in VXLAN deployments as it doesn't require unique
                            IP addresses on each node.
                            """
                            ipv6_address_virtual: str | None = None
                            """
                            IPv6_address/Mask
                            ipv6 address virtuals to configure VXLAN Anycast IP address (Optional)
                            If both "ipv6_address_virtual"
                            and "ipv6_address_virtuals" are set, all addresses will be configured
                            """
                            ipv6_address_virtuals: list[str] | None = None
                            """
                            IPv6 VXLAN Anycast IP addresses
                            Conserves IPv6 addresses in VXLAN deployments as it doesn't require unique IPv6
                            addresses on each node.
                            """
                            ip_address_virtual_secondaries: list[str] | None = None
                            """
                            Secondary IPv4 VXLAN Anycast IP addresses
                            """
                            ip_virtual_router_addresses: list[str] | None = None
                            """
                            IPv4 VARP addresses.
                            Requires an IP address to be configured on the SVI.
                            If ip_address_virtual is also set,
                            ip_virtual_router_addresses will take precedence
                            _if_ there is an ip_address configured for the node.
                            """
                            ipv6_virtual_router_addresses: list[str] | None = None
                            """
                            IPv6 VARP addresses.
                            Requires an IPv6 address to be configured on the SVI.
                            If ipv6_address_virtuals is also set,
                            ipv6_virtual_router_addresses will take precedence
                            _if_ there is an ipv6_address configured for the node.
                            """
                            ip_helpers: list[IpHelpersItem] | None = None
                            """
                            IP helper for DHCP relay
                            """
                            vni_override: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=16777215)
                            """
                            By default the VNI will be derived from "mac_vrf_vni_base".
                            The vni_override allows us to override this value and
                            statically define it (optional).
                            """
                            rt_override: Annotated[str, StrConvert(convert_types=(int))] | None = None
                            """
                            By default the MAC VRF RT will be derived from mac_vrf_id_base + vlan_id.
                            The rt_override allows us to override this
                            value and statically define it.
                            rt_override will default to vni_override if set.

                            rt_override supports two formats:
                              -
                            A single number which will be used in the RT fields instead of mac_vrf_id/mac_vrf_vni (see 'overlay_rt_type' for
                            details).
                              - A full RT string with colon seperator which will override the full RT.
                            """
                            rd_override: Annotated[str, StrConvert(convert_types=(int))] | None = None
                            """
                            By default the MAC VRF RD will be derived from mac_vrf_id_base + vlan_id.
                            The rt_override allows us to override this
                            value and statically define it.
                            rd_override will default to rt_override or vni_override if set.

                            rd_override supports
                            two formats:
                              - A single number which will be used in the RD assigned number field instead of mac_vrf_id/mac_vrf_vni
                            (see 'overlay_rd_type' for details).
                              - A full RD string with colon seperator which will override the full RD.
                            """
                            trunk_groups: list[str] | None = None
                            evpn_l2_multicast: EvpnL2Multicast | None = None
                            """
                            Explicitly enable or disable evpn_l2_multicast to override setting of
                            `<network_services_key>.[].evpn_l2_multicast.enabled`.
                            When evpn_l2_multicast.enabled is set to true for a vlan or a
                            tenant, "igmp snooping" and "igmp snooping querier" will always be enabled, overriding those individual settings.
                            Requires `evpn_multicast` to also be set to `true`.
                            """
                            evpn_l3_multicast: EvpnL3Multicast | None = None
                            """
                            Explicitly enable or disable evpn_l3_multicast to override setting of
                            `<network_services_key>.[].evpn_l3_multicast.enabled` and `<network_services_key>.[].vrfs.[].evpn_l3_multicast.enabled`.
                            Requires `evpn_multicast` to also be set to `true`.
                            """
                            igmp_snooping_enabled: bool | None = None
                            """
                            Enable IGMP Snooping (Enabled by default on EOS).
                            """
                            igmp_snooping_querier: IgmpSnoopingQuerier | None = None
                            vxlan: bool | None = True
                            """
                            Extend this SVI over VXLAN.
                            """
                            spanning_tree_priority: Annotated[int, IntConvert(convert_types=(str))] | None = None
                            """
                            Setting spanning-tree priority per VLAN is only supported with `spanning_tree_mode: rapid-pvst` under node type
                            settings.
                            The default priority for rapid-PVST is set under the node type settings with `spanning_tree_priority`
                            (default=32768).
                            """
                            mtu: Annotated[int, IntConvert(convert_types=(str))] | None = None
                            """
                            Interface MTU.
                            """
                            ospf: Ospf | None = None
                            """
                            OSPF interface configuration.
                            """
                            bgp: Bgp | None = None
                            raw_eos_cli: str | None = None
                            """
                            EOS CLI rendered directly on the VLAN interface in the final EOS configuration.
                            """
                            structured_config: StructuredConfig | None = None
                            """
                            Custom structured config added under vlan_interfaces.[name=<interface>] for eos_cli_config_gen.
                            """

                        class IpHelpersItem(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            ip_helper: str = None
                            """
                            IPv4 DHCP server IP
                            """
                            source_interface: str | None = None
                            """
                            Interface name to originate DHCP relay packets to DHCP server.
                            """
                            source_vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
                            """
                            VRF to originate DHCP relay packets to DHCP server. If not set, EOS uses the VRF on the SVI.
                            """

                        class EvpnL2Multicast(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            enabled: bool | None = None

                        class EvpnL3Multicast(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            enabled: bool | None = None

                        class IgmpSnoopingQuerier(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            enabled: bool | None = None
                            """
                            Will be enabled automatically if evpn_l2_multicast is enabled.
                            """
                            source_address: str | None = None
                            """
                            IPv4_address
                            If not set, IP address of "Loopback0" will be used.
                            """
                            version: Annotated[Literal[1, 2, 3], IntConvert(convert_types=(str))] | None = None
                            """
                            IGMP Version (By default EOS uses IGMP version 2 for IGMP querier).
                            """

                        class Ospf(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            class MessageDigestKeysItem(AvdDictBaseModel):
                                model_config = ConfigDict(defer_build=True, extra="forbid")

                                id: Annotated[int, IntConvert(convert_types=(str))] | None = None
                                hash_algorithm: Literal["md5", "sha1", "sha256", "sha384", "sha512"] | None = "sha512"
                                key: str | None = None
                                """
                                Type 7 encrypted key.
                                """

                            enabled: bool | None = None
                            point_to_point: bool | None = True
                            area: Annotated[str, StrConvert(convert_types=(int))] | None = "0"
                            """
                            OSPF area ID.
                            """
                            cost: Annotated[int, IntConvert(convert_types=(str))] | None = None
                            """
                            OSPF link cost.
                            """
                            authentication: Literal["simple", "message-digest"] | None = None
                            simple_auth_key: str | None = None
                            """
                            Password used with simple authentication.
                            """
                            message_digest_keys: list[MessageDigestKeysItem] | None = None

                        class Bgp(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            class StructuredConfig(EosCliConfigGen.RouterBgp.VlansItem, BaseModel):
                                model_config = ConfigDict(defer_build=True, extra="forbid")

                                pass

                            structured_config: StructuredConfig | None = None
                            """
                            Structured configuration and EOS CLI commands rendered on router_bgp.vlans.[id=<vlan>]
                            This configuration will not be
                            applied to vlan aware bundles
                            """
                            raw_eos_cli: str | None = None
                            """
                            EOS CLI rendered directly on the Router BGP, VLAN definition in the final EOS configuration.
                            """

                        class StructuredConfig(EosCliConfigGen.VlanInterfacesItem, BaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            pass

                        id: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=1, le=4096)
                        """
                        SVI interface id and VLAN id.
                        """
                        name: str = None
                        """
                        VLAN name.
                        """
                        profile: str | None = None
                        """
                        SVI profile name to apply.
                        SVI can refer to one svi_profile which again can refer to another svi_profile to inherit
                        settings in up to two levels (svi -> svi_profile -> svi_parent_profile).
                        """
                        tags: list[Annotated[str, StrConvert(convert_types=(int))]] | None = Field(["all"], validate_default=True)
                        """
                        Tags leveraged for networks services filtering.
                        Tags are matched against "filter.tags" defined under node type settings.
                        Tags are also matched against the "node_group" name under node type settings.
                        """
                        evpn_vlan_bundle: str | None = None
                        """
                        Name of a bundle defined under 'evpn_vlan_bundles' to inherit configuration.
                        To use this option the common
                        "evpn_vlan_aware_bundles" option must be set to true.
                        """
                        nodes: list[NodesItem] | None = None
                        """
                        Define node specific configuration, such as unique IP addresses.
                        Any keys set here will be merged onto the SVI config,
                        except `structured_config` keys which will replace the `structured_config` set on SVI level.
                        """
                        enabled: bool | None = None
                        """
                        Enable or disable interface
                        """
                        description: str | None = None
                        """
                        SVI description. By default set to VLAN name.
                        """
                        ip_address: str | None = None
                        """
                        IPv4_address/Mask. Usually set under "nodes" to have unique IPv4 addresses per node.
                        """
                        ipv6_address: str | None = None
                        """
                        IPv6_address/Mask. Usually set under "nodes" to have unique IPv6 addresses per node.
                        """
                        ipv6_enable: bool | None = None
                        """
                        Explicitly enable/disable link-local IPv6 addressing.
                        """
                        ip_address_virtual: str | None = None
                        """
                        IPv4_address/Mask
                        IPv4 VXLAN Anycast IP address
                        Conserves IP addresses in VXLAN deployments as it doesn't require unique
                        IP addresses on each node.
                        """
                        ipv6_address_virtual: str | None = None
                        """
                        IPv6_address/Mask
                        ipv6 address virtuals to configure VXLAN Anycast IP address (Optional)
                        If both "ipv6_address_virtual"
                        and "ipv6_address_virtuals" are set, all addresses will be configured
                        """
                        ipv6_address_virtuals: list[str] | None = None
                        """
                        IPv6 VXLAN Anycast IP addresses
                        Conserves IPv6 addresses in VXLAN deployments as it doesn't require unique IPv6
                        addresses on each node.
                        """
                        ip_address_virtual_secondaries: list[str] | None = None
                        """
                        Secondary IPv4 VXLAN Anycast IP addresses
                        """
                        ip_virtual_router_addresses: list[str] | None = None
                        """
                        IPv4 VARP addresses.
                        Requires an IP address to be configured on the SVI.
                        If ip_address_virtual is also set,
                        ip_virtual_router_addresses will take precedence
                        _if_ there is an ip_address configured for the node.
                        """
                        ipv6_virtual_router_addresses: list[str] | None = None
                        """
                        IPv6 VARP addresses.
                        Requires an IPv6 address to be configured on the SVI.
                        If ipv6_address_virtuals is also set,
                        ipv6_virtual_router_addresses will take precedence
                        _if_ there is an ipv6_address configured for the node.
                        """
                        ip_helpers: list[IpHelpersItem] | None = None
                        """
                        IP helper for DHCP relay
                        """
                        vni_override: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=16777215)
                        """
                        By default the VNI will be derived from "mac_vrf_vni_base".
                        The vni_override allows us to override this value and
                        statically define it (optional).
                        """
                        rt_override: Annotated[str, StrConvert(convert_types=(int))] | None = None
                        """
                        By default the MAC VRF RT will be derived from mac_vrf_id_base + vlan_id.
                        The rt_override allows us to override this
                        value and statically define it.
                        rt_override will default to vni_override if set.

                        rt_override supports two formats:
                          -
                        A single number which will be used in the RT fields instead of mac_vrf_id/mac_vrf_vni (see 'overlay_rt_type' for
                        details).
                          - A full RT string with colon seperator which will override the full RT.
                        """
                        rd_override: Annotated[str, StrConvert(convert_types=(int))] | None = None
                        """
                        By default the MAC VRF RD will be derived from mac_vrf_id_base + vlan_id.
                        The rt_override allows us to override this
                        value and statically define it.
                        rd_override will default to rt_override or vni_override if set.

                        rd_override supports
                        two formats:
                          - A single number which will be used in the RD assigned number field instead of mac_vrf_id/mac_vrf_vni
                        (see 'overlay_rd_type' for details).
                          - A full RD string with colon seperator which will override the full RD.
                        """
                        trunk_groups: list[str] | None = None
                        evpn_l2_multicast: EvpnL2Multicast | None = None
                        """
                        Explicitly enable or disable evpn_l2_multicast to override setting of
                        `<network_services_key>.[].evpn_l2_multicast.enabled`.
                        When evpn_l2_multicast.enabled is set to true for a vlan or a
                        tenant, "igmp snooping" and "igmp snooping querier" will always be enabled, overriding those individual settings.
                        Requires `evpn_multicast` to also be set to `true`.
                        """
                        evpn_l3_multicast: EvpnL3Multicast | None = None
                        """
                        Explicitly enable or disable evpn_l3_multicast to override setting of
                        `<network_services_key>.[].evpn_l3_multicast.enabled` and `<network_services_key>.[].vrfs.[].evpn_l3_multicast.enabled`.
                        Requires `evpn_multicast` to also be set to `true`.
                        """
                        igmp_snooping_enabled: bool | None = None
                        """
                        Enable IGMP Snooping (Enabled by default on EOS).
                        """
                        igmp_snooping_querier: IgmpSnoopingQuerier | None = None
                        vxlan: bool | None = True
                        """
                        Extend this SVI over VXLAN.
                        """
                        spanning_tree_priority: Annotated[int, IntConvert(convert_types=(str))] | None = None
                        """
                        Setting spanning-tree priority per VLAN is only supported with `spanning_tree_mode: rapid-pvst` under node type
                        settings.
                        The default priority for rapid-PVST is set under the node type settings with `spanning_tree_priority`
                        (default=32768).
                        """
                        mtu: Annotated[int, IntConvert(convert_types=(str))] | None = None
                        """
                        Interface MTU.
                        """
                        ospf: Ospf | None = None
                        """
                        OSPF interface configuration.
                        """
                        bgp: Bgp | None = None
                        raw_eos_cli: str | None = None
                        """
                        EOS CLI rendered directly on the VLAN interface in the final EOS configuration.
                        """
                        structured_config: StructuredConfig | None = None
                        """
                        Custom structured config added under vlan_interfaces.[name=<interface>] for eos_cli_config_gen.
                        """

                    class L3InterfacesItem(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        class Ospf(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            class MessageDigestKeysItem(AvdDictBaseModel):
                                model_config = ConfigDict(defer_build=True, extra="forbid")

                                id: Annotated[int, IntConvert(convert_types=(str))] | None = None
                                hash_algorithm: Literal["md5", "sha1", "sha256", "sha384", "sha512"] | None = "sha512"
                                key: str | None = None
                                """
                                Key password.
                                """

                            enabled: bool | None = None
                            point_to_point: bool | None = False
                            area: Annotated[str, StrConvert(convert_types=(int))] | None = "0"
                            """
                            OSPF area ID.
                            """
                            cost: Annotated[int, IntConvert(convert_types=(str))] | None = None
                            """
                            OSPF link cost.
                            """
                            authentication: Literal["simple", "message-digest"] | None = None
                            simple_auth_key: str | None = None
                            """
                            Password used with simple authentication.
                            """
                            message_digest_keys: list[MessageDigestKeysItem] | None = None

                        class Pim(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            enabled: bool | None = None

                        class StructuredConfig(EosCliConfigGen.EthernetInterfacesItem, BaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            pass

                        interfaces: list[str] | None = None
                        encapsulation_dot1q_vlan: list[Annotated[int, IntConvert(convert_types=(str))]] | None = None
                        """
                        For sub-interfaces the dot1q vlan is derived from the interface name by default, but can also be specified.
                        """
                        ip_addresses: list[str] | None = None
                        nodes: list[str] | None = None
                        description: str | None = None
                        descriptions: list[str] | None = None
                        """
                        "descriptions" has precedence over "description".
                        """
                        enabled: bool | None = None
                        mtu: Annotated[int, IntConvert(convert_types=(str))] | None = None
                        ospf: Ospf | None = None
                        """
                        OSPF interface configuration.
                        """
                        pim: Pim | None = None
                        """
                        Enable PIM sparse-mode on the interface; requires "evpn_l3_multicast" to be enabled on the VRF/Tenant
                        Enabling this
                        implicitly makes the device a PIM External Gateway (PEG) in EVPN designs only.
                        At least one RP address must be
                        configured for EVPN PEG to be configured.
                        """
                        structured_config: StructuredConfig | None = None
                        """
                        Custom structured config added under ethernet_interfaces.[name=<interface>] for eos_cli_config_gen.
                        """
                        raw_eos_cli: str | None = None
                        """
                        EOS CLI rendered directly on the Ethernet interface in the final EOS configuration.
                        """

                    class LoopbacksItem(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        class Ospf(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            enabled: bool | None = False
                            area: Annotated[str, StrConvert(convert_types=(int))] | None = "0"
                            """
                            OSPF area ID.
                            """

                        node: str = None
                        loopback: int = Field(None, ge=0, le=8191)
                        ip_address: str = None
                        description: str | None = None
                        enabled: bool | None = True
                        ospf: Ospf | None = None
                        """
                        OSPF interface configuration.
                        """
                        raw_eos_cli: str | None = None
                        """
                        EOS CLI rendered directly on the Loopback interface in the final EOS configuration.
                        """

                    class StaticRoutesItem(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        destination_address_prefix: str | None = None
                        """
                        IPv4_address.
                        """
                        gateway: str | None = None
                        """
                        IPv4_address.
                        """
                        track_bfd: bool | None = None
                        """
                        Track next-hop using BFD.
                        """
                        distance: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=255)
                        tag: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=4294967295)
                        name: str | None = None
                        """
                        description.
                        """
                        metric: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=4294967295)
                        interface: str | None = None
                        nodes: list[str] | None = None

                    class Ipv6StaticRoutesItem(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        destination_address_prefix: str | None = None
                        """
                        IPv6_address.
                        """
                        gateway: str | None = None
                        track_bfd: bool | None = None
                        """
                        Track next-hop using BFD.
                        """
                        distance: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=255)
                        tag: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=4294967295)
                        name: str | None = None
                        """
                        description.
                        """
                        metric: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=4294967295)
                        interface: str | None = None
                        nodes: list[str] | None = None

                    class BgpPeersItem(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        class DefaultOriginate(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            always: bool | None = None

                        ip_address: str = None
                        """
                        IPv4_address or IPv6_address.
                        """
                        peer_group: str | None = None
                        """
                        Peer group name.
                        """
                        remote_as: Annotated[str, StrConvert(convert_types=(int))] | None = None
                        """
                        BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
                        For asdot notation in YAML inputs, the value
                        must be put in quotes, to prevent it from being interpreted as a float number.
                        """
                        description: str | None = None
                        password: str | None = None
                        """
                        Encrypted password.
                        """
                        send_community: str | None = None
                        """
                        'all' or a combination of 'standard', 'extended', 'large' and 'link-bandwidth (w/options)'.
                        """
                        next_hop_self: bool | None = None
                        timers: str | None = None
                        """
                        BGP Keepalive and Hold Timer values in seconds as string <0-3600> <0-3600>.
                        """
                        maximum_routes: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=4294967294)
                        """
                        Maximum number of routes (0 means unlimited).
                        """
                        maximum_routes_warning_only: bool | None = None
                        default_originate: DefaultOriginate | None = None
                        update_source: str | None = None
                        ebgp_multihop: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=255)
                        """
                        Time-to-live in range of hops.
                        """
                        nodes: list[str] | None = None
                        """
                        Nodes is required to restrict configuration of BGP neighbors to certain nodes in the network.
                        """
                        set_ipv4_next_hop: str | None = None
                        """
                        IPv4_address
                        Next hop settings can be either ipv4 or ipv6 for one neighbor, this will be applied by a uniquely generated
                        route-map per neighbor.
                        Next hop takes precedence over route_map_out.
                        """
                        set_ipv6_next_hop: str | None = None
                        """
                        IPv6_address
                        Next hop settings can be either ipv4 or ipv6 for one neighbor, this will be applied by a uniquely generated
                        route-map per neighbor.
                        Next hop takes precedence over route_map_out.
                        """
                        route_map_out: str | None = None
                        """
                        Route-map name.
                        """
                        route_map_in: str | None = None
                        """
                        Route-map name.
                        """
                        prefix_list_in: str | None = None
                        """
                        Inbound prefix list name.
                        The prefix-list will be associated under the IPv4 or IPv6 address family based on the IP
                        address.
                        """
                        prefix_list_out: str | None = None
                        """
                        Outbound prefix list name.
                        The prefix-list will be associated under the IPv4 or IPv6 address family based on the IP
                        address.
                        """
                        local_as: Annotated[str, StrConvert(convert_types=(int))] | None = None
                        """
                        Local BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
                        For asdot notation in YAML inputs, the
                        value must be put in quotes, to prevent it from being interpreted as a float number.
                        """
                        weight: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=65535)
                        bfd: bool | None = None
                        shutdown: bool | None = None

                    class Bgp(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        class StructuredConfig(EosCliConfigGen.RouterBgp.VrfsItem, BaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            pass

                        raw_eos_cli: str | None = None
                        """
                        EOS CLI rendered directly on the Router BGP, VRF definition in the final EOS configuration.
                        """
                        structured_config: StructuredConfig | None = None
                        """
                        Custom structured config added under router_bgp.vrfs.[name=<vrf>] for eos_cli_config_gen.
                        """

                    class BgpPeerGroupsItem(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        class AsPath(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            remote_as_replace_out: bool | None = None
                            """
                            Replace AS number with local AS number
                            """
                            prepend_own_disabled: bool | None = None
                            """
                            Disable prepending own AS number to AS path
                            """

                        class RemovePrivateAs(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            enabled: bool | None = None
                            all: bool | None = None
                            replace_as: bool | None = None

                        class RemovePrivateAsIngress(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            enabled: bool | None = None
                            replace_as: bool | None = None

                        class BfdTimers(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            interval: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=50, le=60000)
                            """
                            Interval in milliseconds.
                            """
                            min_rx: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=50, le=60000)
                            """
                            Rate in milliseconds.
                            """
                            multiplier: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=3, le=50)

                        class DefaultOriginate(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            enabled: bool | None = None
                            always: bool | None = None
                            route_map: str | None = None
                            """
                            Route-map name
                            """

                        class LinkBandwidth(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            enabled: bool | None = None
                            default: str | None = None
                            """
                            nn.nn(K|M|G) link speed in bits/second
                            """

                        class AllowasIn(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            enabled: bool | None = None
                            times: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=10)
                            """
                            Number of local ASNs allowed in a BGP update
                            """

                        class RibInPrePolicyRetain(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            enabled: bool | None = None
                            all: bool | None = None

                        name: str | None = None
                        """
                        BGP peer group name.
                        """
                        nodes: list[str] | None = None
                        """
                        Nodes is required to restrict configuration of BGP neighbors to certain nodes in the network.
                        If not set the peer-group
                        is created on devices which have a bgp_peer mapped to the corresponding peer_group.
                        """
                        type: str | None = None
                        """
                        Key only used for documentation or validation purposes
                        """
                        remote_as: Annotated[str, StrConvert(convert_types=(int))] | None = None
                        """
                        BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
                        For asdot notation in YAML inputs, the value
                        must be put in quotes, to prevent it from being interpreted as a float number.
                        """
                        local_as: Annotated[str, StrConvert(convert_types=(int))] | None = None
                        """
                        BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
                        For asdot notation in YAML inputs, the value
                        must be put in quotes, to prevent it from being interpreted as a float number.
                        """
                        description: str | None = None
                        shutdown: bool | None = None
                        as_path: AsPath | None = None
                        """
                        BGP AS-PATH options
                        """
                        remove_private_as: RemovePrivateAs | None = None
                        """
                        Remove private AS numbers in outbound AS path
                        """
                        remove_private_as_ingress: RemovePrivateAsIngress | None = None
                        peer_filter: str | None = None
                        """
                        Peer-filter name
                        note: `bgp_listen_range_prefix` and `peer_filter` should not be mixed with
                        the new `listen_ranges` key
                        above to avoid conflicts.
                        """
                        next_hop_unchanged: bool | None = None
                        update_source: str | None = None
                        """
                        IP address or interface name
                        """
                        route_reflector_client: bool | None = None
                        bfd: bool | None = None
                        """
                        Enable BFD.
                        """
                        bfd_timers: BfdTimers | None = None
                        """
                        Override default BFD timers. BFD must be enabled with `bfd: true`.
                        """
                        ebgp_multihop: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=255)
                        """
                        Time-to-live in range of hops
                        """
                        next_hop_self: bool | None = None
                        password: str | None = None
                        passive: bool | None = None
                        default_originate: DefaultOriginate | None = None
                        send_community: str | None = None
                        """
                        'all' or a combination of 'standard', 'extended', 'large' and 'link-bandwidth (w/options)'
                        """
                        maximum_routes: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=4294967294)
                        """
                        Maximum number of routes (0 means unlimited)
                        """
                        maximum_routes_warning_limit: Annotated[str, StrConvert(convert_types=(int))] | None = None
                        """
                        Maximum number of routes after which a warning is issued (0 means never warn) or
                        Percentage of maximum number of routes
                        at which to warn ("<1-100> percent")
                        """
                        maximum_routes_warning_only: bool | None = None
                        link_bandwidth: LinkBandwidth | None = None
                        allowas_in: AllowasIn | None = None
                        weight: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=65535)
                        timers: str | None = None
                        """
                        BGP Keepalive and Hold Timer values in seconds as string "<0-3600> <0-3600>"
                        """
                        rib_in_pre_policy_retain: RibInPrePolicyRetain | None = None
                        route_map_in: str | None = None
                        """
                        Inbound route-map name
                        """
                        route_map_out: str | None = None
                        """
                        Outbound route-map name
                        """
                        bgp_listen_range_prefix: str | None = None
                        """
                        IP prefix range
                        note: `bgp_listen_range_prefix` and `peer_filter` should not be mixed with
                        the new `listen_ranges` key
                        above to avoid conflicts.
                        """
                        session_tracker: str | None = None
                        ttl_maximum_hops: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=254)
                        """
                        Maximum number of hops.
                        """

                    class AdditionalRouteTargetsItem(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        type: Literal["import", "export"] | None = None
                        address_family: str | None = None
                        route_target: str | None = None
                        nodes: list[str] | None = None
                        """
                        Nodes is required to restrict configuration of BGP neighbors to certain nodes in the network.
                        """

                    class StructuredConfig(EosCliConfigGen, BaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        pass

                    name: Annotated[str, StrConvert(convert_types=(int))] = None
                    address_families: list[str] | None = None
                    description: str | None = None
                    """
                    VRF description.
                    """
                    vrf_vni: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=16777215)
                    """
                    Required if "vrf_id" is not set.
                    The VRF VNI range is not limited, but if vrf_id is not set, "vrf_vni" is used for
                    calculating MLAG iBGP peering vlan id.
                    "vrf_vni" may also be used for VRF RD/RT ID. See "overlay_rd_type" and
                    "overlay_rt_type" for details.
                    See "mlag_ibgp_peering_vrfs.base_vlan" for details.
                    If vrf_vni > 10000 make sure to
                    adjust "mac_vrf_vni_base" accordingly to avoid overlap.
                    """
                    vrf_id: Annotated[int, IntConvert(convert_types=(str))] | None = None
                    """
                    Required if "vrf_vni" is not set.
                    "vrf_id" is used as default value for "vrf_vni" and "ospf.process_id" unless those are
                    set.
                    "vrf_id" may also be used for VRF RD/RT ID. See "overlay_rd_type" and "overlay_rt_type" for details.
                    "vrf_id" is
                    preferred over "vrf_vni" for MLAG iBGP peering vlan, see "mlag_ibgp_peering_vrfs.base_vlan" for details.
                    """
                    rd_override: Annotated[str, StrConvert(convert_types=(int))] | None = None
                    """
                    By default, the VRF RD will be derived from the pattern defined in `overlay_rd_type`.
                    The rd_override allows us to
                    override this value and statically define it.

                    rd_override supports two formats:
                      - A single number will be used in the
                    RD assigned number subfield (second part of the RD).
                      - A full RD string with colon seperator which will override the
                    full RD.
                    """
                    rt_override: Annotated[str, StrConvert(convert_types=(int))] | None = None
                    """
                    By default, the VRF RT will be derived from the pattern defined in `overlay_rt_type`.
                    The rt_override allows us to
                    override this value and statically define it.

                    rt_override supports two formats:
                      - A single number will be used in the
                    RT assigned number subfield (second part of the RT).
                      - A full RT string with colon seperator which will override the
                    full RT.
                    """
                    mlag_ibgp_peering_ipv4_pool: str | None = None
                    """
                    IPv4_address/Mask
                    The subnet used for iBGP peering in the VRF.
                    Each MLAG pair will be assigned a subnet based on the ID
                    of the primary MLAG switch.
                    If not set, "mlag_peer_l3_ipv4_pool" or "mlag_peer_ipv4_pool" will be used.
                    """
                    ip_helpers: list[IpHelpersItem] | None = None
                    """
                    IP helper for DHCP relay.
                    """
                    enable_mlag_ibgp_peering_vrfs: bool | None = None
                    """
                    MLAG iBGP peering per VRF.
                    By default an iBGP peering is configured per VRF between MLAG peers on separate VLANs.
                    Setting `enable_mlag_ibgp_peering_vrfs: false` under a VRF will change this default and/or override the tenant-wide
                    setting.
                    """
                    redistribute_mlag_ibgp_peering_vrfs: bool | None = True
                    """
                    Redistribute the connected subnet for the MLAG iBGP peering per VRF into overlay BGP.
                    By default the iBGP peering subnet
                    is redistributed into the overlay routing protocol per VRF.
                    Setting `redistribute_mlag_ibgp_peering_vrfs: false` under a
                    VRF will change this default and/or override the tenant-wide setting.
                    """
                    mlag_ibgp_peering_vlan: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=4096)
                    """
                    Manually define the VLAN used on the MLAG pair for the iBGP session.
                    By default this parameter is calculated using the
                    following formula: `<mlag_ibgp_peering_vrfs.base_vlan>` + `<vrf_id>` - 1.
                    """
                    vtep_diagnostic: VtepDiagnostic | None = None
                    """
                    Enable VTEP Network diagnostics.
                    This will create a loopback with virtual source-nat enable to perform diagnostics from
                    the switch.
                    """
                    ospf: Ospf | None = None
                    """
                    Router OSPF configuration.
                    This will create an OSPF routing instance in the tenant VRF. If there is no nodes definition,
                    the OSPF instance will be
                    created on all leafs where the VRF is deployed. This will also cause automatic OSPF
                    redistribution into BGP unless
                    explicitly turned off with "redistribute_ospf: false".
                    """
                    redistribute_ospf: bool | None = True
                    """
                    Non-selectively enabling or disabling redistribute ospf inside the VRF.
                    """
                    evpn_l3_multicast: EvpnL3Multicast | None = None
                    """
                    Explicitly enable or disable evpn_l3_multicast to override setting of
                    `<network_services_key>.[].evpn_l3_multicast.enabled`.
                    Allow override of `<network_services_key>.[].evpn_l3_multicast`
                    node_settings.
                    Requires `evpn_multicast` to also be set to `true`.
                    """
                    pim_rp_addresses: list[PimRpAddressesItem] | None = None
                    """
                    For each group of nodes, allow configuration of RP Addresses & associated groups.
                    """
                    evpn_l2_multi_domain: bool | None = None
                    """
                    Explicitly extend all VLANs/VLAN-Aware Bundles inside the VRF to remote EVPN domains.
                    Overrides
                    `<network_services_key>.[].evpn_l2_multi_domain`.
                    """
                    svis: list[SvisItem] | None = None
                    """
                    List of SVIs.
                    This will create both the L3 SVI and L2 VLAN based on filters applied to the node.
                    """
                    l3_interfaces: list[L3InterfacesItem] | None = None
                    """
                    List of L3 interfaces.
                    This will create IP routed interface inside VRF. Length of interfaces, nodes and ip_addresses
                    must match.
                    """
                    loopbacks: list[LoopbacksItem] | None = None
                    """
                    List of Loopback interfaces.
                    This will create Loopback interfaces inside the VRF.
                    """
                    static_routes: list[StaticRoutesItem] | None = None
                    """
                    List of static routes for v4 and/or v6.
                    This will create static routes inside the tenant VRF.
                    If nodes are not
                    specified, all l3leafs that carry the VRF will also be applied the static routes.
                    If a node has a static route in the
                    VRF, redistribute static will be automatically enabled in that VRF.
                    This automatic behavior can be overridden non-
                    selectively with the redistribute_static knob for the VRF.
                    """
                    ipv6_static_routes: list[Ipv6StaticRoutesItem] | None = None
                    redistribute_static: bool | None = None
                    """
                    Non-selectively enabling or disabling redistribute static inside the VRF.
                    """
                    bgp_peers: list[BgpPeersItem] | None = None
                    """
                    List of BGP peer definitions.
                    This will configure BGP neighbors inside the tenant VRF for peering with external devices.
                    The configured peer will automatically be activated for ipv4 or ipv6 address family based on the ip address.
                    Note, only
                    ipv4 and ipv6 address families are currently supported in eos_designs.
                    For other address families, use custom_structured
                    configuration with eos_cli_config_gen.
                    """
                    bgp: Bgp | None = None
                    bgp_peer_groups: list[BgpPeerGroupsItem] | None = None
                    """
                    List of BGP peer groups definitions.
                    This will configure BGP peer groups to be used inside the tenant VRF for peering
                    with external devices.
                    Since BGP peer groups are configured at higher BGP level, shared between VRFs,
                    peer_group names
                    should not overlap between VRFs.
                    """
                    additional_route_targets: list[AdditionalRouteTargetsItem] | None = None
                    """
                    Configuration of extra route-targets for this VRF. Useful for route-leaking or gateway between address families.
                    """
                    raw_eos_cli: str | None = None
                    """
                    EOS CLI rendered directly on the root level of the final EOS configuration.
                    """
                    structured_config: StructuredConfig | None = None
                    """
                    Custom structured config for eos_cli_config_gen.
                    """

                class L2vlansItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class EvpnL2Multicast(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        enabled: bool | None = None

                    class IgmpSnoopingQuerier(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        enabled: bool | None = None
                        """
                        Will be enabled automatically if evpn_l2_multicast is enabled.
                        """
                        source_address: str | None = None
                        """
                        IPv4_address
                        If not set, IP address of "Loopback0" will be used.
                        """
                        version: Annotated[Literal[1, 2, 3], IntConvert(convert_types=(str))] | None = 2

                    class Bgp(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        class StructuredConfig(EosCliConfigGen.RouterBgp.VlansItem, BaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            pass

                        structured_config: StructuredConfig | None = None
                        """
                        Custom structured config added under router_bgp.vlans.[id=<vlan>] for eos_cli_config_gen.
                        This configuration will not be
                        applied to vlan aware bundles.
                        """
                        raw_eos_cli: str | None = None
                        """
                        EOS cli commands rendered on router_bgp.vlans.
                        This configuration will not be applied to vlan aware bundles.
                        """

                    id: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=1, le=4094)
                    """
                    VLAN ID
                    """
                    vni_override: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=16777215)
                    """
                    By default the VNI will be derived from mac_vrf_vni_base.
                    The vni_override, allows to override this value and statically
                    define it.
                    """
                    rt_override: Annotated[str, StrConvert(convert_types=(int))] | None = None
                    """
                    By default the MAC VRF RT will be derived from mac_vrf_id_base + vlan_id.
                    The rt_override allows us to override this
                    value and statically define it.
                    rt_override will default to vni_override if set.

                    rt_override supports two formats:
                      -
                    A single number which will be used in the RT fields instead of mac_vrf_id/mac_vrf_vni (see 'overlay_rt_type' for
                    details).
                      - A full RT string with colon seperator which will override the full RT.
                    """
                    rd_override: Annotated[str, StrConvert(convert_types=(int))] | None = None
                    """
                    By default the MAC VRF RD will be derived from mac_vrf_id_base + vlan_id.
                    The rt_override allows us to override this
                    value and statically define it.
                    rd_override will default to rt_override or vni_override if set.

                    rd_override supports
                    two formats:
                      - A single number which will be used in the RD assigned number field instead of mac_vrf_id/mac_vrf_vni
                    (see 'overlay_rd_type' for details).
                      - A full RD string with colon seperator which will override the full RD.
                    """
                    name: str = None
                    """
                    VLAN name
                    """
                    tags: list[str] | None = None
                    """
                    Tags leveraged for networks services filtering.
                    Tags are matched against filter.tags defined under node type settings.
                    Tags are also matched against the node_group name under node type settings.
                    """
                    vxlan: bool | None = True
                    """
                    Extend this L2VLAN over VXLAN.
                    """
                    spanning_tree_priority: Annotated[int, IntConvert(convert_types=(str))] | None = None
                    """
                    Setting spanning-tree priority per VLAN is only supported with `spanning_tree_mode: rapid-pvst` under node type
                    settings.
                    The default priority for rapid-PVST is set under the node type settings with `spanning_tree_priority`
                    (default=32768).
                    """
                    evpn_vlan_bundle: str | None = None
                    """
                    Name of a bundle defined under 'evpn_vlan_bundles' to inherit configuration.
                    To use this option the common
                    "evpn_vlan_aware_bundles" option must be set to true.
                    """
                    trunk_groups: list[str] | None = None
                    evpn_l2_multicast: EvpnL2Multicast | None = None
                    """
                    Explicitly enable or disable evpn_l2_multicast to override setting of
                    `<network_services_key>.[].evpn_l2_multicast.enabled`.
                    When evpn_l2_multicast.enabled is set to true for a vlan or a
                    tenant, igmp snooping and igmp snooping querier will always be enabled, overriding those individual settings.
                    Requires
                    `evpn_multicast` to also be set to `true`.
                    """
                    igmp_snooping_enabled: bool | None = True
                    """
                    Activate or deactivate IGMP snooping.
                    """
                    igmp_snooping_querier: IgmpSnoopingQuerier | None = None
                    """
                    Enable igmp snooping querier, by default using IP address of Loopback 0.
                    When enabled, igmp snooping querier will only
                    be configured on l3 devices, i.e., uplink_type: p2p.
                    """
                    bgp: Bgp | None = None

                class PointToPointServicesItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class SubinterfacesItem(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        number: Annotated[int, IntConvert(convert_types=(str))] = None
                        """
                        Subinterface number
                        """

                    class EndpointsItem(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        class PortChannel(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            mode: Literal["active", "on"] | None = None
                            short_esi: str | None = None

                        id: Annotated[int, IntConvert(convert_types=(str))] = None
                        """
                        Pseudowire ID on this endpoint.
                        """
                        nodes: list[str] = Field(None, min_length=1)
                        """
                        Usually one node. With ESI multihoming we support two nodes per pseudowire endpoint
                        """
                        interfaces: list[str] = Field(None, min_length=1)
                        """
                        Interfaces patched to the pseudowire on this endpoints.
                        The list of interfaces is mapped to the list of nodes, so they
                        must have the same length.
                        """
                        port_channel: PortChannel | None = None

                    name: str = None
                    """
                    Pseudowire name
                    """
                    type: Literal["vpws-pseudowire"] | None = "vpws-pseudowire"
                    subinterfaces: list[SubinterfacesItem] | None = None
                    """
                    Subinterfaces will create subinterfaces and additional pseudowires/patch panel config for each endpoint.
                    """
                    endpoints: list[EndpointsItem] | None = Field(None, min_length=2, max_length=2)
                    """
                    Pseudowire terminating endpoints. Must have exactly two items.
                    """
                    lldp_disable: bool | None = None
                    """
                    Disable LLDP RX/TX on port mode pseudowire services.
                    """

                name: str = None
                """
                Specify a tenant name.
                Tenant provide a construct to group L3 VRFs and L2 VLANs.
                Networks services can be filtered by
                tenant name.
                """
                mac_vrf_vni_base: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=16770000)
                """
                Base number for MAC VRF VXLAN Network Identifier (required with VXLAN).
                VXLAN VNI is derived from the base number with
                simple addition.
                i.e. mac_vrf_vni_base = 10000, svi 100 = VNI 10100, svi 300 = VNI 10300.
                """
                mac_vrf_id_base: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=16770000)
                """
                If not set, "mac_vrf_vni_base" will be used.
                Base number for MAC VRF RD/RT ID (Required unless mac_vrf_vni_base is set)
                ID is derived from the base number with simple addition.
                i.e. mac_vrf_id_base = 10000, svi 100 = RD/RT 10100, svi 300 =
                RD/RT 10300.
                """
                vlan_aware_bundle_number_base: Annotated[int, IntConvert(convert_types=(str))] | None = 0
                """
                Base number for VLAN aware bundle RD/RT.
                The "Assigned Number" part of RD/RT is derived from vrf_vni +
                vlan_aware_bundle_number_base.
                """
                pseudowire_rt_base: Annotated[int, IntConvert(convert_types=(str))] | None = None
                """
                Pseudowire RT base, used to generate route targets for VPWS services.
                Avoid overlapping route target spaces between
                different services.
                """
                enable_mlag_ibgp_peering_vrfs: bool | None = None
                """
                MLAG iBGP peering per VRF.
                By default an iBGP peering is configured per VRF between MLAG peers on separate VLANs.
                Setting `enable_mlag_ibgp_peering_vrfs` false under a tenant will change this default to prevent configuration of these
                peerings and VLANs for all VRFs in the tenant.
                This setting can be overridden per VRF.
                """
                redistribute_mlag_ibgp_peering_vrfs: bool | None = True
                """
                Redistribute the connected subnet for the MLAG iBGP peering per VRF into overlay BGP.
                By default the iBGP peering subnet
                is redistributed into the overlay routing protocol per VRF.
                Setting `redistribute_mlag_ibgp_peering_vrfs: false` under a
                tenant will change this default to prevent redistribution of these subnets for all VRFs in the tenant.
                This setting can
                be overridden per VRF.
                """
                bgp_peer_groups: list[BgpPeerGroupsItem] | None = None
                """
                List of BGP peer groups definitions.
                This will configure BGP peer groups to be used inside the tenant VRF for peering
                with external devices.
                Since BGP peer groups are configured at higher BGP level, shared between VRFs,
                peer_group names
                should not overlap between VRFs.
                """
                evpn_l2_multicast: EvpnL2Multicast | None = None
                """
                Enable EVPN L2 Multicast for all SVIs and l2vlans within Tenant.
                - Multicast group binding is created only for Multicast
                traffic. BULL traffic will use ingress-replication.
                - Configures binding between VXLAN, VLAN, and multicast group IPv4
                address using the following formula:
                  < evpn_l2_multicast.underlay_l2_multicast_group_ipv4_pool > + < vlan_id - 1 > + <
                evpn_l2_multicast.underlay_l2_multicast_group_ipv4_pool_offset >.
                - The recommendation is to assign a /20 block within
                the 232.0.0.0/8 Source-Specific Multicast range.
                - Enables `redistribute igmp` on the router bgp MAC VRF.
                - When
                evpn_l2_multicast.enabled is true for a VLAN or a tenant, "igmp snooping" and "igmp snooping querier" will always be
                enabled - overriding those individual settings.
                - Requires `evpn_multicast` to also be set to `true`.
                """
                evpn_l3_multicast: EvpnL3Multicast | None = None
                """
                Enable L3 Multicast for all SVIs and l3vlans within Tenant.
                - In the evpn-l3ls design type, this enables L3 EVPN
                Multicast (aka OISM)'.
                - Multicast group binding for VRF is created only for Multicast traffic. BULL traffic will use
                ingress-replication.
                - Configures binding between VXLAN, VLAN, and multicast group IPv4 address using the following
                formula:
                  < l3_multicast.evpn_underlay_l3_multicast_group_ipv4_pool > + < vrf_vni - 1 > + <
                l3_multicast.evpn_underlay_l3_multicast_group_ipv4_pool_offset >.
                - The recommendation is to assign a /20 block within
                the 232.0.0.0/8 Source-Specific Multicast range.
                - If enabled on an SVI using the anycast default gateway feature, a
                diagnostic loopback (see below) MUST be configured to source IGMP traffic.
                - Enables `evpn multicast` on the router bgp
                VRF.
                - When enabled on an SVI:
                     - If switch is part of an MLAG pair, enables "pim ipv4 sparse-mode" on the SVI.
                - If switch is standalone or A-A MH, enables "ip igmp" on the SVI.
                     - If "ip address virtual" is configured, enables
                "pim ipv4 local-interface" and uses the diagnostic Loopback defined in the VRF
                - Requires `evpn_multicast` to also be
                set to `true`.
                """
                pim_rp_addresses: list[PimRpAddressesItem] | None = None
                """
                For each group of nodes, allow configuration of RP Addresses & associated groups.
                """
                igmp_snooping_querier: IgmpSnoopingQuerier | None = None
                """
                Enable IGMP snooping querier for each SVI/l2vlan within tenant, by default using IP address of Loopback 0.
                When enabled,
                IGMP snooping querier will only be configured on L3 devices, i.e., uplink_type: p2p.
                """
                evpn_l2_multi_domain: bool | None = True
                """
                Explicitly extend all VLANs/VLAN-Aware Bundles inside the tenant to remote EVPN domains.
                """
                vrfs: list[VrfsItem] | None = None
                """
                VRFs will only be configured on a node if any of the underlying objects like `svis` or `l3_interfaces` apply to the
                node.

                It is recommended to only define a VRF in one Tenant. If the same VRF name is used across multiple tenants and
                those tenants
                are accepted by `filter.tenants` on the node, any object set under the duplicate VRFs must either be
                unique or be an exact match.

                VRF "default" is partially supported under network-services. Currently the supported
                options for "default" vrf are route-target,
                route-distinguisher settings, structured_config, raw_eos_cli in bgp and SVIs
                are the only supported interface type.
                Vlan-aware-bundles are supported as well inside default vrf. OSPF is not
                supported currently.
                """
                l2vlans: list[L2vlansItem] | None = None
                """
                Define L2 network services organized by vlan id.
                """
                point_to_point_services: list[PointToPointServicesItem] | None = None
                """
                Point to point services (pseudowires).
                Only supported for node types with "network_services.l1: true".
                By default this
                is only set for node type "pe" with "design.type: mpls"
                """

            key: str
            """
            Key used as dynamic key
            """
            value: list[NetworkServicesKeysNameItem] | None = Field(None, title="Network Services")
            """
            Value of dynamic key
            """

        class DynamicNodeTypeKeys(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class NodeTypeKeysKey(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Defaults(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class LinkTracking(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        class GroupsItem(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            name: str | None = None
                            """
                            Tracking group name.
                            """
                            recovery_delay: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=3600)
                            """
                            default -> platform_settings_mlag_reload_delay -> 300.
                            """
                            links_minimum: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=100000)

                        enabled: bool | None = False
                        groups: list[GroupsItem] | None = Field([{"name": "LT_GROUP1"}], validate_default=True)
                        """
                        Link Tracking Groups.
                        By default a single group named "LT_GROUP1" is defined with default values.
                        Any groups defined
                        under "groups" will replace the default.
                        """

                    class LacpPortIdRange(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        enabled: bool | None = False
                        size: Annotated[int, IntConvert(convert_types=(str))] | None = 128
                        """
                        Recommended size > = number of ports in the switch.
                        """
                        offset: Annotated[int, IntConvert(convert_types=(str))] | None = 0
                        """
                        Offset is used to avoid overlapping port-id ranges of different switches.
                        Useful when a "connected-endpoint" is
                        connected to switches in different "node_groups".
                        """

                    class StructuredConfig(EosCliConfigGen, BaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        pass

                    class UplinkPtp(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        enable: bool | None = False

                    class UplinkMacsec(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        profile: str | None = None

                    class MlagPortChannelStructuredConfig(EosCliConfigGen.PortChannelInterfacesItem, BaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        pass

                    class MlagPeerVlanStructuredConfig(EosCliConfigGen.VlanInterfacesItem, BaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        pass

                    class MlagPeerL3VlanStructuredConfig(EosCliConfigGen.VlanInterfacesItem, BaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        pass

                    class Filter(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        tenants: list[str] | None = Field(["all"], validate_default=True)
                        """
                        Limit configured Network Services to those defined under these Tenants. Set to ['all'] for all Tenants (default).
                        This
                        list also limits Tenants included by `always_include_vrfs_in_tenants`.
                        """
                        tags: list[str] | None = Field(["all"], validate_default=True)
                        """
                        Limit configured VLANs to those matching the given tags. Set to ['all'] for all VLANs (default).
                        """
                        allow_vrfs: list[Annotated[str, StrConvert(convert_types=(int))]] | None = Field(["all"], validate_default=True)
                        """
                        Limit configured Network Services to those defined under these VRFs. Set to ['all'] for all VRFs (default).
                        This list
                        also limits VRFs included by `always_include_vrfs_in_tenants`.
                        """
                        deny_vrfs: list[Annotated[str, StrConvert(convert_types=(int))]] | None = Field(["all"], validate_default=True)
                        """
                        Prevent configuration of Network Services defined under these VRFs.
                        This list prevents the given VRFs to be included by
                        any other filtering mechanism.
                        """
                        always_include_vrfs_in_tenants: list[str] | None = None
                        """
                        List of tenants where VRFs will be configured even if VLANs are not included in tags.
                        Useful for L3 "border" leaf.
                        """
                        only_vlans_in_use: bool | None = False
                        """
                        Only configure VLANs, SVIs, VRFs in use by connected endpoints or downstream L2 switches.
                        Note! This feature only
                        considers configuration managed by eos_designs.
                        This excludes structured_config, custom_structured_configuration_,
                        raw_eos_cli, eos_cli, custom templates, configlets etc.
                        """

                    class EvpnGateway(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        class RemotePeersItem(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            hostname: str | None = None
                            """
                            Hostname of remote EVPN GW server.
                            """
                            ip_address: str | None = None
                            """
                            Peering IP of remote Route Server.
                            """
                            bgp_as: Annotated[str, StrConvert(convert_types=(int, float))] | None = None
                            """
                            Remote Route Server's BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
                            For asdot notation in
                            YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number.
                            """

                        class EvpnL2(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            enabled: bool | None = False

                        class EvpnL3(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            enabled: bool | None = False
                            inter_domain: bool | None = True

                        remote_peers: list[RemotePeersItem] | None = None
                        """
                        Define remote peers of the EVPN VXLAN Gateway.
                        If the hostname can be found in the inventory, ip_address and BGP ASN
                        will be automatically populated. Manual override takes precedence.
                        If the peer's hostname can not be found in the
                        inventory, ip_address and bgp_as must be defined.
                        """
                        evpn_l2: EvpnL2 | None = None
                        """
                        Enable EVPN Gateway functionality for route-types 2 (MAC-IP) and 3 (IMET).
                        """
                        evpn_l3: EvpnL3 | None = None
                        """
                        Enable EVPN Gateway functionality for route-type 5 (IP-PREFIX).
                        """

                    class IpvpnGateway(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        class RemotePeersItem(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            hostname: str = None
                            """
                            Hostname of remote IPVPN Peer.
                            """
                            ip_address: str = None
                            """
                            Peering IP of remote IPVPN Peer.
                            """
                            bgp_as: Annotated[str, StrConvert(convert_types=(int, float))] = None
                            """
                            Remote IPVPN Peer's BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
                            For asdot notation in
                            YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number.
                            """

                        enabled: bool = None
                        evpn_domain_id: str | None = "65535:1"
                        """
                        Domain ID to assign to EVPN address family for use with D-path. Format <nn>:<nn>.
                        """
                        ipvpn_domain_id: str | None = "65535:2"
                        """
                        Domain ID to assign to IPVPN address families for use with D-path. Format <nn>:<nn>.
                        """
                        enable_d_path: bool | None = True
                        """
                        Enable D-path for use with BGP bestpath selection algorithm.
                        """
                        maximum_routes: Annotated[int, IntConvert(convert_types=(str))] | None = 0
                        """
                        Maximum routes to accept from IPVPN remote peers.
                        """
                        local_as: Annotated[str, StrConvert(convert_types=(int))] | None = "none"
                        """
                        Local BGP AS applied to peering with IPVPN remote peers.
                        BGP AS <1-4294967295> or AS number in asdot notation
                        "<1-65535>.<0-65535>".
                        For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being
                        interpreted as a float number.
                        """
                        address_families: list[str] | None = Field(["vpn-ipv4"], validate_default=True)
                        """
                        IPVPN address families to enable for remote peers.
                        """
                        remote_peers: list[RemotePeersItem] | None = None

                    class Ptp(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        class Dscp(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            general_messages: Annotated[int, IntConvert(convert_types=(str))] | None = None
                            event_messages: Annotated[int, IntConvert(convert_types=(str))] | None = None

                        class Monitor(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            class Threshold(AvdDictBaseModel):
                                model_config = ConfigDict(defer_build=True, extra="forbid")

                                class Drop(AvdDictBaseModel):
                                    model_config = ConfigDict(defer_build=True, extra="forbid")

                                    offset_from_master: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=1000000000)
                                    mean_path_delay: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=1000000000)

                                offset_from_master: Annotated[int, IntConvert(convert_types=(str))] | None = Field(250, ge=0, le=1000000000)
                                mean_path_delay: Annotated[int, IntConvert(convert_types=(str))] | None = Field(1500, ge=0, le=1000000000)
                                drop: Drop | None = None

                            class MissingMessage(AvdDictBaseModel):
                                model_config = ConfigDict(defer_build=True, extra="forbid")

                                class Intervals(AvdDictBaseModel):
                                    model_config = ConfigDict(defer_build=True, extra="forbid")

                                    announce: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=2, le=255)
                                    follow_up: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=2, le=255)
                                    sync: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=2, le=255)

                                class SequenceIds(AvdDictBaseModel):
                                    model_config = ConfigDict(defer_build=True, extra="forbid")

                                    enabled: bool | None = True
                                    announce: Annotated[int, IntConvert(convert_types=(str))] | None = Field(3, ge=2, le=255)
                                    delay_resp: Annotated[int, IntConvert(convert_types=(str))] | None = Field(3, ge=2, le=255)
                                    follow_up: Annotated[int, IntConvert(convert_types=(str))] | None = Field(3, ge=2, le=255)
                                    sync: Annotated[int, IntConvert(convert_types=(str))] | None = Field(3, ge=2, le=255)

                                intervals: Intervals | None = None
                                sequence_ids: SequenceIds | None = None

                            enabled: bool | None = True
                            threshold: Threshold | None = None
                            missing_message: MissingMessage | None = None

                        enabled: bool | None = False
                        profile: Literal["aes67", "smpte2059-2", "aes67-r16-2016"] | None = "aes67-r16-2016"
                        mlag: bool | None = False
                        """
                        Configure PTP on the MLAG peer-link port-channel when PTP is enabled. By default PTP will not be configured on the MLAG
                        peer-link port-channel.
                        """
                        domain: Annotated[int, IntConvert(convert_types=(str))] | None = Field(127, ge=0, le=255)
                        priority1: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=255)
                        """
                        default -> automatically set based on node_type.
                        """
                        priority2: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=255)
                        """
                        default -> (node_id modulus 256).
                        """
                        auto_clock_identity: bool | None = True
                        """
                        If you prefer to have PTP clock identity be the system MAC-address of the switch, which is the default EOS behaviour,
                        simply disable the automatic PTP clock identity.
                        default -> (clock_identity_prefix = 00:1C:73 (default)) + (PTP priority
                        1 as HEX) + ":00:" + (PTP priority 2 as HEX).
                        """
                        clock_identity_prefix: str | None = None
                        """
                        PTP clock idetentiy 3-byte prefix. i.e. "01:02:03".
                        By default the 3-byte prefix is "00:1C:73".
                        This can be overridden
                        if auto_clock_identity is set to true (which is the default).
                        """
                        clock_identity: str | None = None
                        """
                        Set PTP clock identity manually. 6-byte value i.e. "01:02:03:04:05:06".
                        """
                        source_ip: str | None = None
                        """
                        By default in EOS, PTP packets are sourced with an IP address from the routed port or from the relevant SVI, which is
                        the recommended behaviour.
                        This can be set manually if required, for example, to a value of "10.1.2.3".
                        """
                        mode: Literal["boundary"] | None = "boundary"
                        mode_one_step: bool | None = False
                        ttl: Annotated[int, IntConvert(convert_types=(str))] | None = None
                        forward_unicast: bool | None = False
                        """
                        Enable PTP unicast forwarding.
                        """
                        dscp: Dscp | None = None
                        monitor: Monitor | None = None

                    class WanHa(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        enabled: bool | None = True
                        """
                        Enable / Disable auto CV-Pathfinder HA, when two nodes are defined in the same node_group.
                        """
                        ipsec: bool | None = True
                        """
                        Enable / Disable IPsec over HA path-group when HA is enabled.
                        """

                    class L3InterfacesItem(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        class StaticRoutesItem(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            prefix: str = None
                            """
                            IPv4_network/Mask
                            """

                        class StructuredConfig(EosCliConfigGen.EthernetInterfacesItem, BaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            pass

                        profile: str | None = None
                        """
                        L3 interface profile name. Profile defined under `l3_interface_profiles`.
                        """
                        name: str = Field(None, pattern=r"Ethernet[\d/]+(.[\d]+)?")
                        """
                        Ethernet interface name like 'Ethernet2' or subinterface name like 'Ethernet2.42'
                        For a subinterface, the parent
                        physical interface is automatically created.
                        """
                        description: str | None = None
                        """
                        Interface description.
                        If not set a default description will be configured with '[<peer>[ <peer_interface>]]'
                        """
                        ip_address: str | None = None
                        """
                        Node IPv4 address/Mask or 'dhcp'.
                        """
                        dhcp_ip: str | None = None
                        """
                        When the `ip_address` is `dhcp`, this optional field allows to indicate the expected
                        IPv4 address (without mask) to be
                        allocated on the interface if known.
                        This is not rendered in the configuration but can be used for substitution of
                        'interface_ip' in the Access-list
                        set under `ipv4_acl_in` and `ipv4_acl_out`.
                        """
                        public_ip: str | None = None
                        """
                        Node IPv4 address (no mask).

                        This is used to get the public IP (if known) when the device is behind NAT.
                        This is only
                        used for `wan_rr` routers (AutoVPN RRs and Pathfinders) to determine the Public IP
                        with the following preference:
                        `wan_route_servers.path_groups.interfaces.ip_address`
                              -> `l3_interfaces.public_ip`
                                  ->
                        `l3_interfaces.ip_address`

                        The determined Public IP is used by WAN routers when peering with this interface.
                        """
                        encapsulation_dot1q_vlan: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=4094)
                        """
                        For subinterfaces the dot1q vlan is derived from the interface name by default, but can also be specified.
                        """
                        dhcp_accept_default_route: bool | None = True
                        """
                        Accept a default route from DHCP if `ip_address` is set to `dhcp`.
                        """
                        enabled: bool | None = True
                        """
                        Enable or Shutdown the interface.
                        """
                        speed: str | None = None
                        """
                        Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`.
                        """
                        peer: str | None = None
                        """
                        The peer device name. Used for description and documentation
                        """
                        peer_interface: str | None = None
                        """
                        The peer device interface. Used for description and documentation
                        """
                        peer_ip: str | None = None
                        """
                        The peer device IPv4 address (no mask). Used as default route gateway if `set_default_route` is true and `ip` is an IP
                        address.
                        """
                        ipv4_acl_in: Annotated[str, StrConvert(convert_types=(int))] | None = None
                        """
                        Name of the IPv4 access-list to be assigned in the ingress direction.
                        The access-list must be defined under `ipv4_acls`.
                        Required for all WAN interfaces (`wan_carrier` is set) unless the carrier is marked as 'trusted' under `wan_carriers`.
                        """
                        ipv4_acl_out: Annotated[str, StrConvert(convert_types=(int))] | None = None
                        """
                        Name of the IPv4 Access-list to be assigned in the egress direction.
                        The access-list must be defined under `ipv4_acls`.
                        """
                        static_routes: list[StaticRoutesItem] | None = Field(None, min_length=1)
                        """
                        Configure IPv4 static routes pointing to `peer_ip`.
                        """
                        qos_profile: str | None = None
                        """
                        QOS service profile.
                        """
                        wan_carrier: str | None = None
                        """
                        The WAN carrier this interface is connected to.
                        This is used to infer the path-groups in which this interface should be
                        configured.
                        Unless the carrier is marked as 'trusted' under `wan_carriers`, `ipv4_acl_in` is also required on all WAN
                        interfaces.
                        """
                        wan_circuit_id: Annotated[str, StrConvert(convert_types=(int))] | None = None
                        """
                        The WAN circuit ID for this interface.
                        This is not rendered in the configuration but used for WAN designs.
                        """
                        connected_to_pathfinder: bool | None = True
                        """
                        For a WAN interface (`wan_carrier` is set), allow to disable the static tunnel towards Pathfinders.
                        """
                        raw_eos_cli: str | None = None
                        """
                        EOS CLI rendered directly on the interface in the final EOS configuration.
                        """
                        structured_config: StructuredConfig | None = None
                        """
                        Custom structured config for the Ethernet interface.
                        """

                    id: Annotated[int, IntConvert(convert_types=(str))] | None = None
                    """
                    Unique identifier used for IP addressing and other algorithms.
                    """
                    platform: Annotated[str, StrConvert(convert_types=(int))] | None = None
                    """
                    Arista platform family.
                    """
                    mac_address: str | None = None
                    """
                    Leverage to document management interface mac address.
                    """
                    system_mac_address: str | None = None
                    """
                    System MAC Address in this following format: "xx:xx:xx:xx:xx:xx".
                    Set to the same MAC address as available in "show
                    version" on the device.
                    "system_mac_address" can also be set directly as a hostvar.
                    If both are set, the setting under
                    node type settings takes precedence.
                    """
                    serial_number: str | None = None
                    """
                    Set to the Serial Number of the device.
                    Only used for documentation purpose in the fabric documentation and part of the
                    structured_config.
                    "serial_number" can also be set directly as a hostvar.
                    If both are set, the setting under node type
                    settings takes precedence.
                    """
                    rack: str | None = None
                    """
                    Rack that the switch is located in (only used in snmp_settings location).
                    """
                    mgmt_ip: str | None = None
                    """
                    Node management interface IPv4 address.
                    """
                    ipv6_mgmt_ip: str | None = None
                    """
                    Node management interface IPv6 address.
                    """
                    mgmt_interface: str | None = None
                    """
                    Management Interface Name.
                    Default -> platform_management_interface -> mgmt_interface -> "Management1".
                    """
                    link_tracking: LinkTracking | None = None
                    """
                    This configures the Link Tracking Group on a switch as well as adds the p2p-uplinks of the switch as the upstream
                    interfaces.
                    Useful in EVPN multhoming designs.
                    """
                    lacp_port_id_range: LacpPortIdRange | None = None
                    """
                    This will generate the "lacp port-id range", "begin" and "end" values based on node "id" and the number of nodes in the
                    "node_group".
                    Unique LACP port-id ranges are recommended for EVPN Multihoming designs.
                    """
                    always_configure_ip_routing: bool | None = False
                    """
                    Force configuration of "ip routing" even on L2 devices.
                    Use this to retain behavior of AVD versions below 4.0.0.
                    """
                    raw_eos_cli: str | None = None
                    """
                    EOS CLI rendered directly on the root level of the final EOS configuration.
                    """
                    structured_config: StructuredConfig | None = None
                    """
                    Custom structured config for eos_cli_config_gen.
                    """
                    uplink_type: Literal["p2p", "port-channel", "p2p-vrfs", "lan"] | None = "p2p"
                    """
                    Override the default `uplink_type` set at the `node_type_key` level.
                    `uplink_type` must be "p2p" if `vtep` or
                    `underlay_router` is true for the `node_type_key` definition.
                    """
                    uplink_ipv4_pool: str | None = None
                    """
                    IPv4 subnet to use to connect to uplink switches.
                    """
                    uplink_interfaces: list[str] | None = None
                    """
                    Local uplink interfaces
                    Each list item supports range syntax that can be expanded into a list of interfaces.
                    If
                    uplink_interfaces is not defined, platform-specific defaults (defined under default_interfaces) will be used instead.
                    Please note that default_interfaces are not defined by default, you should define these yourself.
                    """
                    uplink_switch_interfaces: list[str] | None = None
                    """
                    Interfaces located on uplink switches.
                    """
                    uplink_switches: list[str] | None = None
                    uplink_interface_speed: str | None = None
                    """
                    Set point-to-Point interface speed and will apply to uplink interfaces on both ends.
                    (Uplink switch interface speed can
                    be overridden with `uplink_switch_interface_speed`).
                    Speed should be set in the format `<interface_speed>` or `forced
                    <interface_speed>` or `auto <interface_speed>`.
                    """
                    uplink_switch_interface_speed: str | None = None
                    """
                    Set point-to-Point interface speed for the uplink switch interface only.
                    Speed should be set in the format
                    `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`.
                    """
                    max_uplink_switches: Annotated[int, IntConvert(convert_types=(str))] | None = None
                    """
                    Maximum number of uplink switches.
                    Changing this value may change IP Addressing on uplinks.
                    Can be used to reserve IP
                    space for future expansions.
                    """
                    max_parallel_uplinks: Annotated[int, IntConvert(convert_types=(str))] | None = None
                    """
                    Number of parallel links towards uplink switches.
                    Changing this value may change interface naming on uplinks (and
                    corresponding downlinks).
                    Can be used to reserve interfaces for future parallel uplinks.
                    """
                    uplink_bfd: bool | None = False
                    """
                    Enable bfd on uplink interfaces.
                    """
                    uplink_native_vlan: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=4094)
                    """
                    Only applicable to switches with layer-2 port-channel uplinks.
                    A suspended (disabled) vlan will be created in both ends
                    of the link unless the vlan is defined under network services.
                    By default the uplink will not have a native_vlan
                    configured, so EOS defaults to vlan 1.
                    """
                    uplink_ptp: UplinkPtp | None = None
                    """
                    Enable PTP on all infrastructure links.
                    """
                    uplink_macsec: UplinkMacsec | None = None
                    """
                    Enable MacSec on all uplinks.
                    """
                    uplink_port_channel_id: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=999999)
                    """
                    Only applicable for L2 switches with `uplink_type: port-channel`.
                    By default the uplink Port-channel ID will be set to
                    the number of the lowest member interface defined under `uplink_interfaces`.
                    For example:
                      member ports [ Eth22, Eth23
                    ] -> ID 22
                      member ports [ Eth11/1, Eth22/1 ] -> ID 111
                    For MLAG port-channels ID will be based on the lowest member
                    interface on the first MLAG switch.
                    This option overrides the default behavior and statically sets the local Port-
                    channel ID.
                    Note! Make sure the ID is unique and does not overlap with autogenerated Port-channel IDs in the Network
                    Services.
                    Note! For MLAG pairs the ID must be between 1 and 2000 and both MLAG switches must have the same value.
                    """
                    uplink_switch_port_channel_id: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=999999)
                    """
                    Only applicable for L2 switches with `uplink_type: port-channel`.
                    By default the uplink switch Port-channel ID will be
                    set to the number of the first interface defined under `uplink_switch_interfaces`.
                    For example:
                      member ports [ Eth22,
                    Eth23 ] -> ID 22
                      member ports [ Eth11/1, Eth22/1 ] -> ID 111
                    For MLAG port-channels ID will be based on the lowest
                    member interface on the first MLAG switch.
                    This option overrides the default behavior and statically sets the Port-
                    channel ID on the uplink switch.
                    Note! Make sure the ID is unique and does not overlap with autogenerated Port-channel
                    IDs in the Network Services.
                    Note! For MLAG pairs the ID must be between 1 and 2000 and both MLAG switches must have the
                    same value.
                    """
                    uplink_structured_config: dict | None = None
                    """
                    Custom structured config applied to "uplink_interfaces", and "uplink_switch_interfaces".
                    When uplink_type == "p2p",
                    custom structured config added under ethernet_interfaces.[name=<interface>] for eos_cli_config_gen overrides the
                    settings on the ethernet interface level.
                    When uplink_type == "port-channel", custom structured config added under
                    port_channel_interfaces.[name=<interface>] for eos_cli_config_gen overrides the settings on the port-channel interface
                    level.
                    "uplink_structured_config" is applied after "structured_config", so it can override "structured_config" defined
                    on node-level.
                    Note! The content of this dictionary is _not_ validated by the schema, since it can be either
                    ethernet_interfaces or port_channel_interfaces.
                    """
                    mlag_port_channel_structured_config: MlagPortChannelStructuredConfig | None = None
                    """
                    Custom structured config applied to MLAG peer link port-channel id.
                    Added under
                    port_channel_interfaces.[name=<interface>] for eos_cli_config_gen.
                    Overrides the settings on the port-channel interface
                    level.
                    "mlag_port_channel_structured_config" is applied after "structured_config", so it can override
                    "structured_config" defined on node-level.
                    """
                    mlag_peer_vlan_structured_config: MlagPeerVlanStructuredConfig | None = None
                    """
                    Custom structured config applied to MLAG Peer Link (control link) SVI interface id.
                    Added under
                    vlan_interfaces.[name=<interface>] for eos_cli_config_gen.
                    Overrides the settings on the vlan interface level.
                    "mlag_peer_vlan_structured_config" is applied after "structured_config", so it can override "structured_config" defined
                    on node-level.
                    """
                    mlag_peer_l3_vlan_structured_config: MlagPeerL3VlanStructuredConfig | None = None
                    """
                    Custom structured config applied to MLAG underlay L3 peering SVI interface id.
                    Added under
                    vlan_interfaces.[name=<interface>] for eos_cli_config_gen.
                    Overrides the settings on the vlan interface level.
                    "mlag_peer_l3_vlan_structured_config" is applied after "structured_config", so it can override "structured_config"
                    defined on node-level.
                    """
                    short_esi: str | None = None
                    """
                    short_esi only valid for l2leaf devices using port-channel uplink.
                    Setting short_esi to "auto" generates the short_esi
                    automatically using a hash of configuration elements.
                    < 0000:0000:0000 | auto >.
                    """
                    isis_system_id_prefix: str | None = Field(None, pattern=r"[0-9a-f]{4}\.[0-9a-f]{4}")
                    """
                    (4.4 hexadecimal).
                    """
                    isis_maximum_paths: Annotated[int, IntConvert(convert_types=(str))] | None = None
                    """
                    Number of path to configure in ECMP for ISIS.
                    """
                    is_type: Literal["level-1-2", "level-1", "level-2"] | None = "level-2"
                    node_sid_base: Annotated[int, IntConvert(convert_types=(str))] | None = 0
                    """
                    Node-SID base for isis-sr underlay variants. Combined with node id to generate ISIS-SR node-SID.
                    """
                    loopback_ipv4_pool: str | None = None
                    """
                    IPv4 subnet for Loopback0 allocation.
                    """
                    vtep_loopback_ipv4_pool: str | None = None
                    """
                    IPv4 subnet for VTEP-Loopback allocation.
                    """
                    loopback_ipv4_offset: Annotated[int, IntConvert(convert_types=(str))] | None = 0
                    """
                    Offset all assigned loopback IP addresses.
                    Required when the < loopback_ipv4_pool > is same for 2 different node_types
                    (like spine and l3leaf) to avoid over-lapping IPs.
                    For example, set the minimum offset
                    l3leaf.defaults.loopback_ipv4_offset: < total # spine switches > or vice versa.
                    """
                    loopback_ipv6_pool: str | None = None
                    """
                    IPv6 subnet for Loopback0 allocation.
                    """
                    loopback_ipv6_offset: Annotated[int, IntConvert(convert_types=(str))] | None = 0
                    """
                    Offset all assigned loopback IPv6 addresses.
                    Required when the < loopback_ipv6_pool > is same for 2 different node_types
                    (like spine and l3leaf) to avoid overlapping IPs.
                    For example, set the minimum offset
                    l3leaf.defaults.loopback_ipv6_offset: < total # spine switches > or vice versa.
                    """
                    vtep: bool | None = None
                    """
                    Node is configured as a VTEP when applicable based on 'overlay_routing_protocol'.
                    Overrides VTEP setting inherited from
                    node_type_keys.
                    """
                    vtep_loopback: str | None = Field(None, pattern=r"Loopback[\d/]+")
                    """
                    Set VXLAN source interface.
                    """
                    bgp_as: Annotated[str, StrConvert(convert_types=(int, float))] | None = None
                    """
                    BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
                    For asdot notation in YAML inputs, the value
                    must be put in quotes, to prevent it from being interpreted as a float number.
                    Required with eBGP.
                    """
                    bgp_defaults: list[str] | None = None
                    """
                    List of EOS commands to apply to BGP daemon.
                    """
                    evpn_role: Literal["client", "server", "none"] | None = None
                    """
                    Acting role in EVPN control plane.
                    Default is set in node_type definition from node_type_keys.
                    """
                    evpn_route_servers: list[str] | None = None
                    """
                    List of nodes acting as EVPN Route-Servers / Route-Reflectors.
                    """
                    evpn_services_l2_only: bool | None = False
                    """
                    Possibility to prevent configuration of Tenant VRFs and SVIs.
                    Override node definition "network_services_l3" from
                    node_type_keys.
                    This allows support for centralized routing.
                    """
                    filter: Filter | None = None
                    """
                    Filter L3 and L2 network services based on tenant and tags (and operation filter).
                    If filter is not defined it will
                    default to all.
                    """
                    igmp_snooping_enabled: bool | None = True
                    """
                    Activate or deactivate IGMP snooping on device level.
                    """
                    evpn_gateway: EvpnGateway | None = None
                    """
                    Node is acting as EVPN Multi-Domain Gateway.
                    New BGP peer-group is generated between EVPN GWs in different domains or
                    between GWs and Route Servers.
                    Name can be changed under "bgp_peer_groups.evpn_overlay_core" variable.
                    L3 rechability
                    for different EVPN GWs must be already in place, it is recommended to use DCI & L3 Edge if Route Servers and GWs are not
                    defined under the same Ansible inventory.
                    """
                    ipvpn_gateway: IpvpnGateway | None = None
                    """
                    Node is acting as IP-VPN Gateway for EVPN to MPLS-IP-VPN Interworking. The BGP peer group used for this is
                    "bgp_peer_groups.ipvpn_gateway_peers".
                    L3 Reachability is required for this to work, the preferred method to establish
                    underlay connectivity is to use core_interfaces.
                    """
                    mlag: bool | None = True
                    """
                    Enable / Disable auto MLAG, when two nodes are defined in node group.
                    """
                    mlag_dual_primary_detection: bool | None = False
                    """
                    Enable / Disable MLAG dual primary detection.
                    """
                    mlag_ibgp_origin_incomplete: bool | None = True
                    """
                    Set origin of routes received from MLAG iBGP peer to incomplete.
                    The purpose is to optimize routing for leaf loopbacks
                    from spine perspective and
                    avoid suboptimal routing via peerlink for control plane traffic.
                    """
                    mlag_interfaces: list[str] | None = None
                    """
                    Each list item supports range syntax that can be expanded into a list of interfaces.
                    Required when MLAG leafs are
                    present in the topology.
                    """
                    mlag_interfaces_speed: str | None = None
                    """
                    Set MLAG interface speed.
                    Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto
                    <interface_speed>`.
                    """
                    mlag_peer_l3_vlan: Annotated[int, IntConvert(convert_types=(str, bool))] | None = Field(4093, ge=0, le=4094)
                    """
                    Underlay L3 peering SVI interface id.
                    If set to 0 or the same vlan as mlag_peer_vlan, the mlag_peer_vlan will be used
                    for L3 peering.
                    """
                    mlag_peer_l3_ipv4_pool: str | None = None
                    """
                    IP address pool used for MLAG underlay L3 peering. IP is derived from the node id.
                    Required when MLAG leafs present in
                    topology and they are using a separate L3 peering VLAN.
                    """
                    mlag_peer_vlan: Annotated[int, IntConvert(convert_types=(str))] | None = Field(4094, ge=1, le=4094)
                    """
                    MLAG Peer Link (control link) SVI interface id.
                    """
                    mlag_peer_link_allowed_vlans: str | None = None
                    mlag_peer_ipv4_pool: str | None = None
                    """
                    IP address pool used for MLAG Peer Link (control link). IP is derived from the node id.
                    Required when MLAG leafs present
                    in topology.
                    """
                    mlag_port_channel_id: Annotated[int, IntConvert(convert_types=(str))] | None = None
                    """
                    If not set, the mlag port-channel id is generated based on the digits of the first interface present in
                    'mlag_interfaces'.
                    Valid port-channel id numbers are < 1-2000 > for EOS < 4.25.0F and < 1 - 999999 > for EOS >= 4.25.0F.
                    """
                    mlag_domain_id: str | None = None
                    """
                    MLAG Domain ID. If not set the node group name (Set with "group" key) will be used.
                    """
                    spanning_tree_mode: Literal["mstp", "rstp", "rapid-pvst", "none"] | None = None
                    spanning_tree_priority: Annotated[int, IntConvert(convert_types=(str))] | None = 32768
                    """
                    Spanning-tree priority configured for the selected mode.
                    For `rapid-pvst` the priority can also be set per VLAN under
                    network services.
                    """
                    spanning_tree_root_super: bool | None = False
                    virtual_router_mac_address: str | None = None
                    """
                    Virtual router mac address for anycast gateway.
                    """
                    inband_mgmt_interface: str | None = None
                    """
                    Pointer to interface used for inband management.
                    All configuration must be done using other data models like network
                    services or structured_config.
                    'inband_mgmt_interface' is only used to refer to this interface as source in various
                    management protocol settings (future feature).

                    On L2 switches, this defaults to Vlan<inband_mgmt_vlan> if either
                    'inband_mgmt_subnet' or 'inband_mgmt_ip' is set.
                    """
                    inband_mgmt_vlan: Annotated[int, IntConvert(convert_types=(str))] | None = 4092
                    """
                    VLAN number used for inband management on L2 switches (switches using port-channel trunks as uplinks).
                    When using
                    'inband_mgmt_subnet' the VLAN and SVIs will be created automatically on this switch as well as all 'uplink_switches'.
                    When using 'inband_mgmt_ip' the VLAN and SVI will only be created on this device and added to uplink trunk. The VLAN and
                    SVI on the parent switches must be created using network services data models.
                    """
                    inband_mgmt_subnet: str | None = None
                    """
                    Optional IP subnet assigned to inband management SVIs on L2 switches (switches using port-channels as uplinks).
                    Parent
                    l3leafs will have SVI with "ip virtual-router" and host-route injection based on ARP.
                    This allows all l3leafs to reuse
                    the same subnet across multiple racks without VXLAN extension.
                    SVI IP address will be assigned as follows:
                    virtual-
                    router: <subnet> + 1
                    l3leaf A      : <subnet> + 2 (same IP on all l3leaf A)
                    l3leaf B      : <subnet> + 3 (same IP on all
                    l3leaf B)
                    l2leafs       : <subnet> + 3 + <l2leaf id>
                    GW on l2leafs : <subnet> + 1
                    Assign range larger than total l2leafs
                    + 5

                    Setting is ignored if 'inband_mgmt_ip' is set.

                    This setting is applicable to L2 switches (switches using port-
                    channel trunks as uplinks).
                    """
                    inband_mgmt_ip: str | None = None
                    """
                    IP address assigned to the inband management interface set with 'inband_mgmt_vlan'.
                    This overrides 'inband_mgmt_subnet',
                    hence all behavior of 'inband_mgmt_subnet' is removed.

                    If this is set the VLAN and SVI will only be created on the L2
                    switch and added to uplink trunk.
                    The VLAN and SVI on the parent switches must be created using network services data
                    models.

                    This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).
                    """
                    inband_mgmt_gateway: str | None = None
                    """
                    Default gateway configured in the 'inband_mgmt_vrf' when using 'inband_mgmt_ip'. Otherwise gateway is derived from
                    'inband_mgmt_subnet' if set.

                    This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).
                    """
                    inband_mgmt_ipv6_address: str | None = None
                    """
                    IPv6 address assigned to the inband management interface set with 'inband_mgmt_vlan'.
                    This overrides
                    'inband_mgmt_ipv6_subnet', hence the configuration of 'inband_mgmt_ipv6_subnet' is ignored.

                    If this is set the VLAN and
                    SVI will only be created on the L2 switch and added to uplink trunk.
                    The VLAN and SVI on the parent switches must be
                    created using network services data models.

                    This setting is applicable to L2 switches (switches using port-channel
                    trunks as uplinks).
                    """
                    inband_mgmt_ipv6_subnet: str | None = None
                    """
                    Optional IPv6 prefix assigned to inband management SVIs on L2 switches (switches using port-channels as uplinks).
                    Parent
                    l3leafs will have SVI with "ipv6 virtual-router" and host-route injection based on ARP.
                    This allows all l3leafs to reuse
                    the same subnet across multiple racks without VXLAN extension.
                    SVI IP address will be assigned as follows:
                    virtual-
                    router: <subnet> + 1
                    l3leaf A      : <subnet> + 2 (same IP on all l3leaf A)
                    l3leaf B      : <subnet> + 3 (same IP on all
                    l3leaf B)
                    l2leafs       : <subnet> + 3 + <l2leaf id>
                    GW on l2leafs : <subnet> + 1
                    Assign range larger than total l2leafs
                    + 5

                    Setting is ignored if 'inband_mgmt_ipv6_address' is set.

                    This setting is applicable to L2 switches (switches using
                    port-channel trunks as uplinks).
                    """
                    inband_mgmt_ipv6_gateway: str | None = None
                    """
                    Default gateway configured in the 'inband_mgmt_vrf'.
                    Used when `inband_mgmt_ipv6_address` is set.
                    Ignored when
                    'inband_mgmt_ipv6_subnet' is set (first IP in subnet used as gateway).

                    This setting is applicable to L2 switches
                    (switches using port-channel trunks as uplinks).
                    """
                    inband_mgmt_description: str | None = "Inband Management"
                    """
                    Description configured on the Inband Management SVI.

                    This setting is only applied on the devices where it is set, it
                    does not automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-
                    group/node-type as needed.
                    """
                    inband_mgmt_vlan_name: str | None = "Inband Management"
                    """
                    Name configured on the Inband Management VLAN.
                    This setting is only applied on the devices where it is set, it does not
                    automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-group/node-
                    type as needed.
                    """
                    inband_mgmt_vrf: Annotated[str, StrConvert(convert_types=(int))] | None = "default"
                    """
                    VRF configured on the Inband Management Interface.
                    The VRF is created if not already created by other means.
                    This
                    setting is only applied on the devices where it is set, it does not automatically affect any parent/child devices
                    configuration, so it must be set on each applicable node/node-group/node-type as needed.
                    """
                    inband_mgmt_mtu: int | None = 1500
                    """
                    MTU configured on the Inband Management Interface.
                    This setting is only applied on the devices where it is set, it does
                    not automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-
                    group/node-type as needed.
                    """
                    inband_ztp: bool | None = False
                    """
                    Enable to configure upstream device with proper configuration to allow downstream devices to ZTP inband.
                    This setting
                    also requires that the `inband_mgmt_vlan` is set for the node.
                    """
                    inband_ztp_lacp_fallback_delay: int | None = Field(30, ge=0, le=300)
                    """
                    Set the LACP fallback timeout of the upstream device's port-channel towards the downstream inband ZTP node.
                    This setting
                    also requires that `inband_ztp` is set for the node.
                    """
                    inband_management_subnet: str | None = None
                    """
                    Optional IP subnet assigned to inband management SVIs on L2 switches (switches using port-channels as uplinks).
                    Parent
                    l3leafs will have SVI with "ip virtual-router" and host-route injection based on ARP.
                    This allows all l3leafs to reuse
                    the same subnet across multiple racks without VXLAN extension.
                    SVI IP address will be assigned as follows:
                    virtual-
                    router: <subnet> + 1
                    l3leaf A      : <subnet> + 2 (same IP on all l3leaf A)
                    l3leaf B      : <subnet> + 3 (same IP on all
                    l3leaf B)
                    l2leafs       : <subnet> + 3 + <l2leaf id>
                    GW on l2leafs : <subnet> + 1
                    Assign range larger than total l2leafs
                    + 5

                    Setting is ignored if 'inband_mgmt_ip' is set.

                    This setting is applicable to L2 switches (switches using port-
                    channel trunks as uplinks).
                    """
                    inband_management_vlan: Annotated[int, IntConvert(convert_types=(str))] | None = 4092
                    """
                    VLAN number used for inband management on L2 switches (switches using port-channel trunks as uplinks).
                    When using
                    'inband_mgmt_subnet' the VLAN and SVIs will be created automatically on this switch as well as all 'uplink_switches'.
                    When using 'inband_mgmt_ip' the VLAN and SVI will only be created on this device and added to uplink trunk. The VLAN and
                    SVI on the parent switches must be created using network services data models.
                    """
                    mpls_overlay_role: Literal["client", "server", "none"] | None = None
                    """
                    Set the default mpls overlay role.
                    Acting role in overlay control plane.
                    """
                    overlay_address_families: list[str] | None = None
                    """
                    Set the default overlay address families.
                    """
                    mpls_route_reflectors: list[str] | None = None
                    """
                    List of inventory hostname acting as MPLS route-reflectors.
                    """
                    bgp_cluster_id: Annotated[str, StrConvert(convert_types=(int))] | None = None
                    """
                    Set BGP cluster id.
                    """
                    ptp: Ptp | None = None
                    wan_role: Literal["client", "server"] | None = None
                    """
                    Override the default WAN role.

                    This is used both for AutoVPN and Pathfinder designs.
                    That means if `wan_mode` root key
                    is set to `autovpn` or `cv-pathfinder`.
                    `server` indicates that the router is a route-reflector.

                    Only supported if
                    `overlay_routing_protocol` is set to `ibgp`.
                    """
                    cv_pathfinder_transit_mode: Literal["region", "zone"] | None = None
                    """
                    Configure the transit mode for a WAN client for CV Pathfinder designs
                    only when the `wan_mode` root key is set to
                    `cv_pathfinder`.

                    'zone' is currently not supported.
                    """
                    cv_pathfinder_region: str | None = None
                    """
                    The CV Pathfinder region name.
                    This key is required for WAN routers but optional for pathfinders.
                    The region name must
                    be defined under 'cv_pathfinder_regions'.
                    """
                    cv_pathfinder_site: str | None = None
                    """
                    The CV Pathfinder site name.
                    This key is required for WAN routers but ignored for pathfinders.
                    The site name must be
                    defined for the relevant region under 'cv_pathfinder_regions'.
                    """
                    wan_ha: WanHa | None = None
                    """
                    PREVIEW: This key is currently not supported

                    The key is supported only if `wan_mode` == `cv-pathfinder`.
                    AutoVPN
                    support is still to be determined.

                    Maximum 2 devices supported by group for HA.
                    """
                    dps_mss_ipv4: Annotated[str, StrConvert(convert_types=(int))] | None = "auto"
                    """
                    IPv4 MSS value configured under "router path-selection" on WAN Devices.
                    """
                    l3_interfaces: list[L3InterfacesItem] | None = None
                    """
                    L3 Interfaces to configure on the node.
                    Used to define the node for WAN interfaces when `wan_carrier` is set.
                    """
                    data_plane_cpu_allocation_max: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=128)
                    """
                    Set the maximum number of CPU used for the data plane.
                    This setting is useful on virtual Route Reflectors and
                    Pathfinders where more CPU cores should be allocated for control plane.
                    """

                class NodeGroupsItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class NodesItem(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        class LinkTracking(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            class GroupsItem(AvdDictBaseModel):
                                model_config = ConfigDict(defer_build=True, extra="forbid")

                                name: str | None = None
                                """
                                Tracking group name.
                                """
                                recovery_delay: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=3600)
                                """
                                default -> platform_settings_mlag_reload_delay -> 300.
                                """
                                links_minimum: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=100000)

                            enabled: bool | None = False
                            groups: list[GroupsItem] | None = Field([{"name": "LT_GROUP1"}], validate_default=True)
                            """
                            Link Tracking Groups.
                            By default a single group named "LT_GROUP1" is defined with default values.
                            Any groups defined
                            under "groups" will replace the default.
                            """

                        class LacpPortIdRange(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            enabled: bool | None = False
                            size: Annotated[int, IntConvert(convert_types=(str))] | None = 128
                            """
                            Recommended size > = number of ports in the switch.
                            """
                            offset: Annotated[int, IntConvert(convert_types=(str))] | None = 0
                            """
                            Offset is used to avoid overlapping port-id ranges of different switches.
                            Useful when a "connected-endpoint" is
                            connected to switches in different "node_groups".
                            """

                        class StructuredConfig(EosCliConfigGen, BaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            pass

                        class UplinkPtp(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            enable: bool | None = False

                        class UplinkMacsec(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            profile: str | None = None

                        class MlagPortChannelStructuredConfig(EosCliConfigGen.PortChannelInterfacesItem, BaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            pass

                        class MlagPeerVlanStructuredConfig(EosCliConfigGen.VlanInterfacesItem, BaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            pass

                        class MlagPeerL3VlanStructuredConfig(EosCliConfigGen.VlanInterfacesItem, BaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            pass

                        class Filter(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            tenants: list[str] | None = Field(["all"], validate_default=True)
                            """
                            Limit configured Network Services to those defined under these Tenants. Set to ['all'] for all Tenants (default).
                            This
                            list also limits Tenants included by `always_include_vrfs_in_tenants`.
                            """
                            tags: list[str] | None = Field(["all"], validate_default=True)
                            """
                            Limit configured VLANs to those matching the given tags. Set to ['all'] for all VLANs (default).
                            """
                            allow_vrfs: list[Annotated[str, StrConvert(convert_types=(int))]] | None = Field(["all"], validate_default=True)
                            """
                            Limit configured Network Services to those defined under these VRFs. Set to ['all'] for all VRFs (default).
                            This list
                            also limits VRFs included by `always_include_vrfs_in_tenants`.
                            """
                            deny_vrfs: list[Annotated[str, StrConvert(convert_types=(int))]] | None = Field(["all"], validate_default=True)
                            """
                            Prevent configuration of Network Services defined under these VRFs.
                            This list prevents the given VRFs to be included by
                            any other filtering mechanism.
                            """
                            always_include_vrfs_in_tenants: list[str] | None = None
                            """
                            List of tenants where VRFs will be configured even if VLANs are not included in tags.
                            Useful for L3 "border" leaf.
                            """
                            only_vlans_in_use: bool | None = False
                            """
                            Only configure VLANs, SVIs, VRFs in use by connected endpoints or downstream L2 switches.
                            Note! This feature only
                            considers configuration managed by eos_designs.
                            This excludes structured_config, custom_structured_configuration_,
                            raw_eos_cli, eos_cli, custom templates, configlets etc.
                            """

                        class EvpnGateway(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            class RemotePeersItem(AvdDictBaseModel):
                                model_config = ConfigDict(defer_build=True, extra="forbid")

                                hostname: str | None = None
                                """
                                Hostname of remote EVPN GW server.
                                """
                                ip_address: str | None = None
                                """
                                Peering IP of remote Route Server.
                                """
                                bgp_as: Annotated[str, StrConvert(convert_types=(int, float))] | None = None
                                """
                                Remote Route Server's BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
                                For asdot notation in
                                YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number.
                                """

                            class EvpnL2(AvdDictBaseModel):
                                model_config = ConfigDict(defer_build=True, extra="forbid")

                                enabled: bool | None = False

                            class EvpnL3(AvdDictBaseModel):
                                model_config = ConfigDict(defer_build=True, extra="forbid")

                                enabled: bool | None = False
                                inter_domain: bool | None = True

                            remote_peers: list[RemotePeersItem] | None = None
                            """
                            Define remote peers of the EVPN VXLAN Gateway.
                            If the hostname can be found in the inventory, ip_address and BGP ASN
                            will be automatically populated. Manual override takes precedence.
                            If the peer's hostname can not be found in the
                            inventory, ip_address and bgp_as must be defined.
                            """
                            evpn_l2: EvpnL2 | None = None
                            """
                            Enable EVPN Gateway functionality for route-types 2 (MAC-IP) and 3 (IMET).
                            """
                            evpn_l3: EvpnL3 | None = None
                            """
                            Enable EVPN Gateway functionality for route-type 5 (IP-PREFIX).
                            """

                        class IpvpnGateway(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            class RemotePeersItem(AvdDictBaseModel):
                                model_config = ConfigDict(defer_build=True, extra="forbid")

                                hostname: str = None
                                """
                                Hostname of remote IPVPN Peer.
                                """
                                ip_address: str = None
                                """
                                Peering IP of remote IPVPN Peer.
                                """
                                bgp_as: Annotated[str, StrConvert(convert_types=(int, float))] = None
                                """
                                Remote IPVPN Peer's BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
                                For asdot notation in
                                YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number.
                                """

                            enabled: bool = None
                            evpn_domain_id: str | None = "65535:1"
                            """
                            Domain ID to assign to EVPN address family for use with D-path. Format <nn>:<nn>.
                            """
                            ipvpn_domain_id: str | None = "65535:2"
                            """
                            Domain ID to assign to IPVPN address families for use with D-path. Format <nn>:<nn>.
                            """
                            enable_d_path: bool | None = True
                            """
                            Enable D-path for use with BGP bestpath selection algorithm.
                            """
                            maximum_routes: Annotated[int, IntConvert(convert_types=(str))] | None = 0
                            """
                            Maximum routes to accept from IPVPN remote peers.
                            """
                            local_as: Annotated[str, StrConvert(convert_types=(int))] | None = "none"
                            """
                            Local BGP AS applied to peering with IPVPN remote peers.
                            BGP AS <1-4294967295> or AS number in asdot notation
                            "<1-65535>.<0-65535>".
                            For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being
                            interpreted as a float number.
                            """
                            address_families: list[str] | None = Field(["vpn-ipv4"], validate_default=True)
                            """
                            IPVPN address families to enable for remote peers.
                            """
                            remote_peers: list[RemotePeersItem] | None = None

                        class Ptp(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            class Dscp(AvdDictBaseModel):
                                model_config = ConfigDict(defer_build=True, extra="forbid")

                                general_messages: Annotated[int, IntConvert(convert_types=(str))] | None = None
                                event_messages: Annotated[int, IntConvert(convert_types=(str))] | None = None

                            class Monitor(AvdDictBaseModel):
                                model_config = ConfigDict(defer_build=True, extra="forbid")

                                class Threshold(AvdDictBaseModel):
                                    model_config = ConfigDict(defer_build=True, extra="forbid")

                                    class Drop(AvdDictBaseModel):
                                        model_config = ConfigDict(defer_build=True, extra="forbid")

                                        offset_from_master: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=1000000000)
                                        mean_path_delay: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=1000000000)

                                    offset_from_master: Annotated[int, IntConvert(convert_types=(str))] | None = Field(250, ge=0, le=1000000000)
                                    mean_path_delay: Annotated[int, IntConvert(convert_types=(str))] | None = Field(1500, ge=0, le=1000000000)
                                    drop: Drop | None = None

                                class MissingMessage(AvdDictBaseModel):
                                    model_config = ConfigDict(defer_build=True, extra="forbid")

                                    class Intervals(AvdDictBaseModel):
                                        model_config = ConfigDict(defer_build=True, extra="forbid")

                                        announce: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=2, le=255)
                                        follow_up: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=2, le=255)
                                        sync: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=2, le=255)

                                    class SequenceIds(AvdDictBaseModel):
                                        model_config = ConfigDict(defer_build=True, extra="forbid")

                                        enabled: bool | None = True
                                        announce: Annotated[int, IntConvert(convert_types=(str))] | None = Field(3, ge=2, le=255)
                                        delay_resp: Annotated[int, IntConvert(convert_types=(str))] | None = Field(3, ge=2, le=255)
                                        follow_up: Annotated[int, IntConvert(convert_types=(str))] | None = Field(3, ge=2, le=255)
                                        sync: Annotated[int, IntConvert(convert_types=(str))] | None = Field(3, ge=2, le=255)

                                    intervals: Intervals | None = None
                                    sequence_ids: SequenceIds | None = None

                                enabled: bool | None = True
                                threshold: Threshold | None = None
                                missing_message: MissingMessage | None = None

                            enabled: bool | None = False
                            profile: Literal["aes67", "smpte2059-2", "aes67-r16-2016"] | None = "aes67-r16-2016"
                            mlag: bool | None = False
                            """
                            Configure PTP on the MLAG peer-link port-channel when PTP is enabled. By default PTP will not be configured on the MLAG
                            peer-link port-channel.
                            """
                            domain: Annotated[int, IntConvert(convert_types=(str))] | None = Field(127, ge=0, le=255)
                            priority1: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=255)
                            """
                            default -> automatically set based on node_type.
                            """
                            priority2: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=255)
                            """
                            default -> (node_id modulus 256).
                            """
                            auto_clock_identity: bool | None = True
                            """
                            If you prefer to have PTP clock identity be the system MAC-address of the switch, which is the default EOS behaviour,
                            simply disable the automatic PTP clock identity.
                            default -> (clock_identity_prefix = 00:1C:73 (default)) + (PTP priority
                            1 as HEX) + ":00:" + (PTP priority 2 as HEX).
                            """
                            clock_identity_prefix: str | None = None
                            """
                            PTP clock idetentiy 3-byte prefix. i.e. "01:02:03".
                            By default the 3-byte prefix is "00:1C:73".
                            This can be overridden
                            if auto_clock_identity is set to true (which is the default).
                            """
                            clock_identity: str | None = None
                            """
                            Set PTP clock identity manually. 6-byte value i.e. "01:02:03:04:05:06".
                            """
                            source_ip: str | None = None
                            """
                            By default in EOS, PTP packets are sourced with an IP address from the routed port or from the relevant SVI, which is
                            the recommended behaviour.
                            This can be set manually if required, for example, to a value of "10.1.2.3".
                            """
                            mode: Literal["boundary"] | None = "boundary"
                            mode_one_step: bool | None = False
                            ttl: Annotated[int, IntConvert(convert_types=(str))] | None = None
                            forward_unicast: bool | None = False
                            """
                            Enable PTP unicast forwarding.
                            """
                            dscp: Dscp | None = None
                            monitor: Monitor | None = None

                        class WanHa(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            enabled: bool | None = True
                            """
                            Enable / Disable auto CV-Pathfinder HA, when two nodes are defined in the same node_group.
                            """
                            ipsec: bool | None = True
                            """
                            Enable / Disable IPsec over HA path-group when HA is enabled.
                            """

                        class L3InterfacesItem(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            class StaticRoutesItem(AvdDictBaseModel):
                                model_config = ConfigDict(defer_build=True, extra="forbid")

                                prefix: str = None
                                """
                                IPv4_network/Mask
                                """

                            class StructuredConfig(EosCliConfigGen.EthernetInterfacesItem, BaseModel):
                                model_config = ConfigDict(defer_build=True, extra="forbid")

                                pass

                            profile: str | None = None
                            """
                            L3 interface profile name. Profile defined under `l3_interface_profiles`.
                            """
                            name: str = Field(None, pattern=r"Ethernet[\d/]+(.[\d]+)?")
                            """
                            Ethernet interface name like 'Ethernet2' or subinterface name like 'Ethernet2.42'
                            For a subinterface, the parent
                            physical interface is automatically created.
                            """
                            description: str | None = None
                            """
                            Interface description.
                            If not set a default description will be configured with '[<peer>[ <peer_interface>]]'
                            """
                            ip_address: str | None = None
                            """
                            Node IPv4 address/Mask or 'dhcp'.
                            """
                            dhcp_ip: str | None = None
                            """
                            When the `ip_address` is `dhcp`, this optional field allows to indicate the expected
                            IPv4 address (without mask) to be
                            allocated on the interface if known.
                            This is not rendered in the configuration but can be used for substitution of
                            'interface_ip' in the Access-list
                            set under `ipv4_acl_in` and `ipv4_acl_out`.
                            """
                            public_ip: str | None = None
                            """
                            Node IPv4 address (no mask).

                            This is used to get the public IP (if known) when the device is behind NAT.
                            This is only
                            used for `wan_rr` routers (AutoVPN RRs and Pathfinders) to determine the Public IP
                            with the following preference:
                            `wan_route_servers.path_groups.interfaces.ip_address`
                                  -> `l3_interfaces.public_ip`
                                      ->
                            `l3_interfaces.ip_address`

                            The determined Public IP is used by WAN routers when peering with this interface.
                            """
                            encapsulation_dot1q_vlan: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=4094)
                            """
                            For subinterfaces the dot1q vlan is derived from the interface name by default, but can also be specified.
                            """
                            dhcp_accept_default_route: bool | None = True
                            """
                            Accept a default route from DHCP if `ip_address` is set to `dhcp`.
                            """
                            enabled: bool | None = True
                            """
                            Enable or Shutdown the interface.
                            """
                            speed: str | None = None
                            """
                            Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`.
                            """
                            peer: str | None = None
                            """
                            The peer device name. Used for description and documentation
                            """
                            peer_interface: str | None = None
                            """
                            The peer device interface. Used for description and documentation
                            """
                            peer_ip: str | None = None
                            """
                            The peer device IPv4 address (no mask). Used as default route gateway if `set_default_route` is true and `ip` is an IP
                            address.
                            """
                            ipv4_acl_in: Annotated[str, StrConvert(convert_types=(int))] | None = None
                            """
                            Name of the IPv4 access-list to be assigned in the ingress direction.
                            The access-list must be defined under `ipv4_acls`.
                            Required for all WAN interfaces (`wan_carrier` is set) unless the carrier is marked as 'trusted' under `wan_carriers`.
                            """
                            ipv4_acl_out: Annotated[str, StrConvert(convert_types=(int))] | None = None
                            """
                            Name of the IPv4 Access-list to be assigned in the egress direction.
                            The access-list must be defined under `ipv4_acls`.
                            """
                            static_routes: list[StaticRoutesItem] | None = Field(None, min_length=1)
                            """
                            Configure IPv4 static routes pointing to `peer_ip`.
                            """
                            qos_profile: str | None = None
                            """
                            QOS service profile.
                            """
                            wan_carrier: str | None = None
                            """
                            The WAN carrier this interface is connected to.
                            This is used to infer the path-groups in which this interface should be
                            configured.
                            Unless the carrier is marked as 'trusted' under `wan_carriers`, `ipv4_acl_in` is also required on all WAN
                            interfaces.
                            """
                            wan_circuit_id: Annotated[str, StrConvert(convert_types=(int))] | None = None
                            """
                            The WAN circuit ID for this interface.
                            This is not rendered in the configuration but used for WAN designs.
                            """
                            connected_to_pathfinder: bool | None = True
                            """
                            For a WAN interface (`wan_carrier` is set), allow to disable the static tunnel towards Pathfinders.
                            """
                            raw_eos_cli: str | None = None
                            """
                            EOS CLI rendered directly on the interface in the final EOS configuration.
                            """
                            structured_config: StructuredConfig | None = None
                            """
                            Custom structured config for the Ethernet interface.
                            """

                        name: str = None
                        """
                        The Node Name is used as "hostname".
                        """
                        id: Annotated[int, IntConvert(convert_types=(str))] | None = None
                        """
                        Unique identifier used for IP addressing and other algorithms.
                        """
                        platform: Annotated[str, StrConvert(convert_types=(int))] | None = None
                        """
                        Arista platform family.
                        """
                        mac_address: str | None = None
                        """
                        Leverage to document management interface mac address.
                        """
                        system_mac_address: str | None = None
                        """
                        System MAC Address in this following format: "xx:xx:xx:xx:xx:xx".
                        Set to the same MAC address as available in "show
                        version" on the device.
                        "system_mac_address" can also be set directly as a hostvar.
                        If both are set, the setting under
                        node type settings takes precedence.
                        """
                        serial_number: str | None = None
                        """
                        Set to the Serial Number of the device.
                        Only used for documentation purpose in the fabric documentation and part of the
                        structured_config.
                        "serial_number" can also be set directly as a hostvar.
                        If both are set, the setting under node type
                        settings takes precedence.
                        """
                        rack: str | None = None
                        """
                        Rack that the switch is located in (only used in snmp_settings location).
                        """
                        mgmt_ip: str | None = None
                        """
                        Node management interface IPv4 address.
                        """
                        ipv6_mgmt_ip: str | None = None
                        """
                        Node management interface IPv6 address.
                        """
                        mgmt_interface: str | None = None
                        """
                        Management Interface Name.
                        Default -> platform_management_interface -> mgmt_interface -> "Management1".
                        """
                        link_tracking: LinkTracking | None = None
                        """
                        This configures the Link Tracking Group on a switch as well as adds the p2p-uplinks of the switch as the upstream
                        interfaces.
                        Useful in EVPN multhoming designs.
                        """
                        lacp_port_id_range: LacpPortIdRange | None = None
                        """
                        This will generate the "lacp port-id range", "begin" and "end" values based on node "id" and the number of nodes in the
                        "node_group".
                        Unique LACP port-id ranges are recommended for EVPN Multihoming designs.
                        """
                        always_configure_ip_routing: bool | None = False
                        """
                        Force configuration of "ip routing" even on L2 devices.
                        Use this to retain behavior of AVD versions below 4.0.0.
                        """
                        raw_eos_cli: str | None = None
                        """
                        EOS CLI rendered directly on the root level of the final EOS configuration.
                        """
                        structured_config: StructuredConfig | None = None
                        """
                        Custom structured config for eos_cli_config_gen.
                        """
                        uplink_type: Literal["p2p", "port-channel", "p2p-vrfs", "lan"] | None = "p2p"
                        """
                        Override the default `uplink_type` set at the `node_type_key` level.
                        `uplink_type` must be "p2p" if `vtep` or
                        `underlay_router` is true for the `node_type_key` definition.
                        """
                        uplink_ipv4_pool: str | None = None
                        """
                        IPv4 subnet to use to connect to uplink switches.
                        """
                        uplink_interfaces: list[str] | None = None
                        """
                        Local uplink interfaces
                        Each list item supports range syntax that can be expanded into a list of interfaces.
                        If
                        uplink_interfaces is not defined, platform-specific defaults (defined under default_interfaces) will be used instead.
                        Please note that default_interfaces are not defined by default, you should define these yourself.
                        """
                        uplink_switch_interfaces: list[str] | None = None
                        """
                        Interfaces located on uplink switches.
                        """
                        uplink_switches: list[str] | None = None
                        uplink_interface_speed: str | None = None
                        """
                        Set point-to-Point interface speed and will apply to uplink interfaces on both ends.
                        (Uplink switch interface speed can
                        be overridden with `uplink_switch_interface_speed`).
                        Speed should be set in the format `<interface_speed>` or `forced
                        <interface_speed>` or `auto <interface_speed>`.
                        """
                        uplink_switch_interface_speed: str | None = None
                        """
                        Set point-to-Point interface speed for the uplink switch interface only.
                        Speed should be set in the format
                        `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`.
                        """
                        max_uplink_switches: Annotated[int, IntConvert(convert_types=(str))] | None = None
                        """
                        Maximum number of uplink switches.
                        Changing this value may change IP Addressing on uplinks.
                        Can be used to reserve IP
                        space for future expansions.
                        """
                        max_parallel_uplinks: Annotated[int, IntConvert(convert_types=(str))] | None = None
                        """
                        Number of parallel links towards uplink switches.
                        Changing this value may change interface naming on uplinks (and
                        corresponding downlinks).
                        Can be used to reserve interfaces for future parallel uplinks.
                        """
                        uplink_bfd: bool | None = False
                        """
                        Enable bfd on uplink interfaces.
                        """
                        uplink_native_vlan: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=4094)
                        """
                        Only applicable to switches with layer-2 port-channel uplinks.
                        A suspended (disabled) vlan will be created in both ends
                        of the link unless the vlan is defined under network services.
                        By default the uplink will not have a native_vlan
                        configured, so EOS defaults to vlan 1.
                        """
                        uplink_ptp: UplinkPtp | None = None
                        """
                        Enable PTP on all infrastructure links.
                        """
                        uplink_macsec: UplinkMacsec | None = None
                        """
                        Enable MacSec on all uplinks.
                        """
                        uplink_port_channel_id: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=999999)
                        """
                        Only applicable for L2 switches with `uplink_type: port-channel`.
                        By default the uplink Port-channel ID will be set to
                        the number of the lowest member interface defined under `uplink_interfaces`.
                        For example:
                          member ports [ Eth22, Eth23
                        ] -> ID 22
                          member ports [ Eth11/1, Eth22/1 ] -> ID 111
                        For MLAG port-channels ID will be based on the lowest member
                        interface on the first MLAG switch.
                        This option overrides the default behavior and statically sets the local Port-
                        channel ID.
                        Note! Make sure the ID is unique and does not overlap with autogenerated Port-channel IDs in the Network
                        Services.
                        Note! For MLAG pairs the ID must be between 1 and 2000 and both MLAG switches must have the same value.
                        """
                        uplink_switch_port_channel_id: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=999999)
                        """
                        Only applicable for L2 switches with `uplink_type: port-channel`.
                        By default the uplink switch Port-channel ID will be
                        set to the number of the first interface defined under `uplink_switch_interfaces`.
                        For example:
                          member ports [ Eth22,
                        Eth23 ] -> ID 22
                          member ports [ Eth11/1, Eth22/1 ] -> ID 111
                        For MLAG port-channels ID will be based on the lowest
                        member interface on the first MLAG switch.
                        This option overrides the default behavior and statically sets the Port-
                        channel ID on the uplink switch.
                        Note! Make sure the ID is unique and does not overlap with autogenerated Port-channel
                        IDs in the Network Services.
                        Note! For MLAG pairs the ID must be between 1 and 2000 and both MLAG switches must have the
                        same value.
                        """
                        uplink_structured_config: dict | None = None
                        """
                        Custom structured config applied to "uplink_interfaces", and "uplink_switch_interfaces".
                        When uplink_type == "p2p",
                        custom structured config added under ethernet_interfaces.[name=<interface>] for eos_cli_config_gen overrides the
                        settings on the ethernet interface level.
                        When uplink_type == "port-channel", custom structured config added under
                        port_channel_interfaces.[name=<interface>] for eos_cli_config_gen overrides the settings on the port-channel interface
                        level.
                        "uplink_structured_config" is applied after "structured_config", so it can override "structured_config" defined
                        on node-level.
                        Note! The content of this dictionary is _not_ validated by the schema, since it can be either
                        ethernet_interfaces or port_channel_interfaces.
                        """
                        mlag_port_channel_structured_config: MlagPortChannelStructuredConfig | None = None
                        """
                        Custom structured config applied to MLAG peer link port-channel id.
                        Added under
                        port_channel_interfaces.[name=<interface>] for eos_cli_config_gen.
                        Overrides the settings on the port-channel interface
                        level.
                        "mlag_port_channel_structured_config" is applied after "structured_config", so it can override
                        "structured_config" defined on node-level.
                        """
                        mlag_peer_vlan_structured_config: MlagPeerVlanStructuredConfig | None = None
                        """
                        Custom structured config applied to MLAG Peer Link (control link) SVI interface id.
                        Added under
                        vlan_interfaces.[name=<interface>] for eos_cli_config_gen.
                        Overrides the settings on the vlan interface level.
                        "mlag_peer_vlan_structured_config" is applied after "structured_config", so it can override "structured_config" defined
                        on node-level.
                        """
                        mlag_peer_l3_vlan_structured_config: MlagPeerL3VlanStructuredConfig | None = None
                        """
                        Custom structured config applied to MLAG underlay L3 peering SVI interface id.
                        Added under
                        vlan_interfaces.[name=<interface>] for eos_cli_config_gen.
                        Overrides the settings on the vlan interface level.
                        "mlag_peer_l3_vlan_structured_config" is applied after "structured_config", so it can override "structured_config"
                        defined on node-level.
                        """
                        short_esi: str | None = None
                        """
                        short_esi only valid for l2leaf devices using port-channel uplink.
                        Setting short_esi to "auto" generates the short_esi
                        automatically using a hash of configuration elements.
                        < 0000:0000:0000 | auto >.
                        """
                        isis_system_id_prefix: str | None = Field(None, pattern=r"[0-9a-f]{4}\.[0-9a-f]{4}")
                        """
                        (4.4 hexadecimal).
                        """
                        isis_maximum_paths: Annotated[int, IntConvert(convert_types=(str))] | None = None
                        """
                        Number of path to configure in ECMP for ISIS.
                        """
                        is_type: Literal["level-1-2", "level-1", "level-2"] | None = "level-2"
                        node_sid_base: Annotated[int, IntConvert(convert_types=(str))] | None = 0
                        """
                        Node-SID base for isis-sr underlay variants. Combined with node id to generate ISIS-SR node-SID.
                        """
                        loopback_ipv4_pool: str | None = None
                        """
                        IPv4 subnet for Loopback0 allocation.
                        """
                        vtep_loopback_ipv4_pool: str | None = None
                        """
                        IPv4 subnet for VTEP-Loopback allocation.
                        """
                        loopback_ipv4_offset: Annotated[int, IntConvert(convert_types=(str))] | None = 0
                        """
                        Offset all assigned loopback IP addresses.
                        Required when the < loopback_ipv4_pool > is same for 2 different node_types
                        (like spine and l3leaf) to avoid over-lapping IPs.
                        For example, set the minimum offset
                        l3leaf.defaults.loopback_ipv4_offset: < total # spine switches > or vice versa.
                        """
                        loopback_ipv6_pool: str | None = None
                        """
                        IPv6 subnet for Loopback0 allocation.
                        """
                        loopback_ipv6_offset: Annotated[int, IntConvert(convert_types=(str))] | None = 0
                        """
                        Offset all assigned loopback IPv6 addresses.
                        Required when the < loopback_ipv6_pool > is same for 2 different node_types
                        (like spine and l3leaf) to avoid overlapping IPs.
                        For example, set the minimum offset
                        l3leaf.defaults.loopback_ipv6_offset: < total # spine switches > or vice versa.
                        """
                        vtep: bool | None = None
                        """
                        Node is configured as a VTEP when applicable based on 'overlay_routing_protocol'.
                        Overrides VTEP setting inherited from
                        node_type_keys.
                        """
                        vtep_loopback: str | None = Field(None, pattern=r"Loopback[\d/]+")
                        """
                        Set VXLAN source interface.
                        """
                        bgp_as: Annotated[str, StrConvert(convert_types=(int, float))] | None = None
                        """
                        BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
                        For asdot notation in YAML inputs, the value
                        must be put in quotes, to prevent it from being interpreted as a float number.
                        Required with eBGP.
                        """
                        bgp_defaults: list[str] | None = None
                        """
                        List of EOS commands to apply to BGP daemon.
                        """
                        evpn_role: Literal["client", "server", "none"] | None = None
                        """
                        Acting role in EVPN control plane.
                        Default is set in node_type definition from node_type_keys.
                        """
                        evpn_route_servers: list[str] | None = None
                        """
                        List of nodes acting as EVPN Route-Servers / Route-Reflectors.
                        """
                        evpn_services_l2_only: bool | None = False
                        """
                        Possibility to prevent configuration of Tenant VRFs and SVIs.
                        Override node definition "network_services_l3" from
                        node_type_keys.
                        This allows support for centralized routing.
                        """
                        filter: Filter | None = None
                        """
                        Filter L3 and L2 network services based on tenant and tags (and operation filter).
                        If filter is not defined it will
                        default to all.
                        """
                        igmp_snooping_enabled: bool | None = True
                        """
                        Activate or deactivate IGMP snooping on device level.
                        """
                        evpn_gateway: EvpnGateway | None = None
                        """
                        Node is acting as EVPN Multi-Domain Gateway.
                        New BGP peer-group is generated between EVPN GWs in different domains or
                        between GWs and Route Servers.
                        Name can be changed under "bgp_peer_groups.evpn_overlay_core" variable.
                        L3 rechability
                        for different EVPN GWs must be already in place, it is recommended to use DCI & L3 Edge if Route Servers and GWs are not
                        defined under the same Ansible inventory.
                        """
                        ipvpn_gateway: IpvpnGateway | None = None
                        """
                        Node is acting as IP-VPN Gateway for EVPN to MPLS-IP-VPN Interworking. The BGP peer group used for this is
                        "bgp_peer_groups.ipvpn_gateway_peers".
                        L3 Reachability is required for this to work, the preferred method to establish
                        underlay connectivity is to use core_interfaces.
                        """
                        mlag: bool | None = True
                        """
                        Enable / Disable auto MLAG, when two nodes are defined in node group.
                        """
                        mlag_dual_primary_detection: bool | None = False
                        """
                        Enable / Disable MLAG dual primary detection.
                        """
                        mlag_ibgp_origin_incomplete: bool | None = True
                        """
                        Set origin of routes received from MLAG iBGP peer to incomplete.
                        The purpose is to optimize routing for leaf loopbacks
                        from spine perspective and
                        avoid suboptimal routing via peerlink for control plane traffic.
                        """
                        mlag_interfaces: list[str] | None = None
                        """
                        Each list item supports range syntax that can be expanded into a list of interfaces.
                        Required when MLAG leafs are
                        present in the topology.
                        """
                        mlag_interfaces_speed: str | None = None
                        """
                        Set MLAG interface speed.
                        Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto
                        <interface_speed>`.
                        """
                        mlag_peer_l3_vlan: Annotated[int, IntConvert(convert_types=(str, bool))] | None = Field(4093, ge=0, le=4094)
                        """
                        Underlay L3 peering SVI interface id.
                        If set to 0 or the same vlan as mlag_peer_vlan, the mlag_peer_vlan will be used
                        for L3 peering.
                        """
                        mlag_peer_l3_ipv4_pool: str | None = None
                        """
                        IP address pool used for MLAG underlay L3 peering. IP is derived from the node id.
                        Required when MLAG leafs present in
                        topology and they are using a separate L3 peering VLAN.
                        """
                        mlag_peer_vlan: Annotated[int, IntConvert(convert_types=(str))] | None = Field(4094, ge=1, le=4094)
                        """
                        MLAG Peer Link (control link) SVI interface id.
                        """
                        mlag_peer_link_allowed_vlans: str | None = None
                        mlag_peer_ipv4_pool: str | None = None
                        """
                        IP address pool used for MLAG Peer Link (control link). IP is derived from the node id.
                        Required when MLAG leafs present
                        in topology.
                        """
                        mlag_port_channel_id: Annotated[int, IntConvert(convert_types=(str))] | None = None
                        """
                        If not set, the mlag port-channel id is generated based on the digits of the first interface present in
                        'mlag_interfaces'.
                        Valid port-channel id numbers are < 1-2000 > for EOS < 4.25.0F and < 1 - 999999 > for EOS >= 4.25.0F.
                        """
                        mlag_domain_id: str | None = None
                        """
                        MLAG Domain ID. If not set the node group name (Set with "group" key) will be used.
                        """
                        spanning_tree_mode: Literal["mstp", "rstp", "rapid-pvst", "none"] | None = None
                        spanning_tree_priority: Annotated[int, IntConvert(convert_types=(str))] | None = 32768
                        """
                        Spanning-tree priority configured for the selected mode.
                        For `rapid-pvst` the priority can also be set per VLAN under
                        network services.
                        """
                        spanning_tree_root_super: bool | None = False
                        virtual_router_mac_address: str | None = None
                        """
                        Virtual router mac address for anycast gateway.
                        """
                        inband_mgmt_interface: str | None = None
                        """
                        Pointer to interface used for inband management.
                        All configuration must be done using other data models like network
                        services or structured_config.
                        'inband_mgmt_interface' is only used to refer to this interface as source in various
                        management protocol settings (future feature).

                        On L2 switches, this defaults to Vlan<inband_mgmt_vlan> if either
                        'inband_mgmt_subnet' or 'inband_mgmt_ip' is set.
                        """
                        inband_mgmt_vlan: Annotated[int, IntConvert(convert_types=(str))] | None = 4092
                        """
                        VLAN number used for inband management on L2 switches (switches using port-channel trunks as uplinks).
                        When using
                        'inband_mgmt_subnet' the VLAN and SVIs will be created automatically on this switch as well as all 'uplink_switches'.
                        When using 'inband_mgmt_ip' the VLAN and SVI will only be created on this device and added to uplink trunk. The VLAN and
                        SVI on the parent switches must be created using network services data models.
                        """
                        inband_mgmt_subnet: str | None = None
                        """
                        Optional IP subnet assigned to inband management SVIs on L2 switches (switches using port-channels as uplinks).
                        Parent
                        l3leafs will have SVI with "ip virtual-router" and host-route injection based on ARP.
                        This allows all l3leafs to reuse
                        the same subnet across multiple racks without VXLAN extension.
                        SVI IP address will be assigned as follows:
                        virtual-
                        router: <subnet> + 1
                        l3leaf A      : <subnet> + 2 (same IP on all l3leaf A)
                        l3leaf B      : <subnet> + 3 (same IP on all
                        l3leaf B)
                        l2leafs       : <subnet> + 3 + <l2leaf id>
                        GW on l2leafs : <subnet> + 1
                        Assign range larger than total l2leafs
                        + 5

                        Setting is ignored if 'inband_mgmt_ip' is set.

                        This setting is applicable to L2 switches (switches using port-
                        channel trunks as uplinks).
                        """
                        inband_mgmt_ip: str | None = None
                        """
                        IP address assigned to the inband management interface set with 'inband_mgmt_vlan'.
                        This overrides 'inband_mgmt_subnet',
                        hence all behavior of 'inband_mgmt_subnet' is removed.

                        If this is set the VLAN and SVI will only be created on the L2
                        switch and added to uplink trunk.
                        The VLAN and SVI on the parent switches must be created using network services data
                        models.

                        This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).
                        """
                        inband_mgmt_gateway: str | None = None
                        """
                        Default gateway configured in the 'inband_mgmt_vrf' when using 'inband_mgmt_ip'. Otherwise gateway is derived from
                        'inband_mgmt_subnet' if set.

                        This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).
                        """
                        inband_mgmt_ipv6_address: str | None = None
                        """
                        IPv6 address assigned to the inband management interface set with 'inband_mgmt_vlan'.
                        This overrides
                        'inband_mgmt_ipv6_subnet', hence the configuration of 'inband_mgmt_ipv6_subnet' is ignored.

                        If this is set the VLAN and
                        SVI will only be created on the L2 switch and added to uplink trunk.
                        The VLAN and SVI on the parent switches must be
                        created using network services data models.

                        This setting is applicable to L2 switches (switches using port-channel
                        trunks as uplinks).
                        """
                        inband_mgmt_ipv6_subnet: str | None = None
                        """
                        Optional IPv6 prefix assigned to inband management SVIs on L2 switches (switches using port-channels as uplinks).
                        Parent
                        l3leafs will have SVI with "ipv6 virtual-router" and host-route injection based on ARP.
                        This allows all l3leafs to reuse
                        the same subnet across multiple racks without VXLAN extension.
                        SVI IP address will be assigned as follows:
                        virtual-
                        router: <subnet> + 1
                        l3leaf A      : <subnet> + 2 (same IP on all l3leaf A)
                        l3leaf B      : <subnet> + 3 (same IP on all
                        l3leaf B)
                        l2leafs       : <subnet> + 3 + <l2leaf id>
                        GW on l2leafs : <subnet> + 1
                        Assign range larger than total l2leafs
                        + 5

                        Setting is ignored if 'inband_mgmt_ipv6_address' is set.

                        This setting is applicable to L2 switches (switches using
                        port-channel trunks as uplinks).
                        """
                        inband_mgmt_ipv6_gateway: str | None = None
                        """
                        Default gateway configured in the 'inband_mgmt_vrf'.
                        Used when `inband_mgmt_ipv6_address` is set.
                        Ignored when
                        'inband_mgmt_ipv6_subnet' is set (first IP in subnet used as gateway).

                        This setting is applicable to L2 switches
                        (switches using port-channel trunks as uplinks).
                        """
                        inband_mgmt_description: str | None = "Inband Management"
                        """
                        Description configured on the Inband Management SVI.

                        This setting is only applied on the devices where it is set, it
                        does not automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-
                        group/node-type as needed.
                        """
                        inband_mgmt_vlan_name: str | None = "Inband Management"
                        """
                        Name configured on the Inband Management VLAN.
                        This setting is only applied on the devices where it is set, it does not
                        automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-group/node-
                        type as needed.
                        """
                        inband_mgmt_vrf: Annotated[str, StrConvert(convert_types=(int))] | None = "default"
                        """
                        VRF configured on the Inband Management Interface.
                        The VRF is created if not already created by other means.
                        This
                        setting is only applied on the devices where it is set, it does not automatically affect any parent/child devices
                        configuration, so it must be set on each applicable node/node-group/node-type as needed.
                        """
                        inband_mgmt_mtu: int | None = 1500
                        """
                        MTU configured on the Inband Management Interface.
                        This setting is only applied on the devices where it is set, it does
                        not automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-
                        group/node-type as needed.
                        """
                        inband_ztp: bool | None = False
                        """
                        Enable to configure upstream device with proper configuration to allow downstream devices to ZTP inband.
                        This setting
                        also requires that the `inband_mgmt_vlan` is set for the node.
                        """
                        inband_ztp_lacp_fallback_delay: int | None = Field(30, ge=0, le=300)
                        """
                        Set the LACP fallback timeout of the upstream device's port-channel towards the downstream inband ZTP node.
                        This setting
                        also requires that `inband_ztp` is set for the node.
                        """
                        inband_management_subnet: str | None = None
                        """
                        Optional IP subnet assigned to inband management SVIs on L2 switches (switches using port-channels as uplinks).
                        Parent
                        l3leafs will have SVI with "ip virtual-router" and host-route injection based on ARP.
                        This allows all l3leafs to reuse
                        the same subnet across multiple racks without VXLAN extension.
                        SVI IP address will be assigned as follows:
                        virtual-
                        router: <subnet> + 1
                        l3leaf A      : <subnet> + 2 (same IP on all l3leaf A)
                        l3leaf B      : <subnet> + 3 (same IP on all
                        l3leaf B)
                        l2leafs       : <subnet> + 3 + <l2leaf id>
                        GW on l2leafs : <subnet> + 1
                        Assign range larger than total l2leafs
                        + 5

                        Setting is ignored if 'inband_mgmt_ip' is set.

                        This setting is applicable to L2 switches (switches using port-
                        channel trunks as uplinks).
                        """
                        inband_management_vlan: Annotated[int, IntConvert(convert_types=(str))] | None = 4092
                        """
                        VLAN number used for inband management on L2 switches (switches using port-channel trunks as uplinks).
                        When using
                        'inband_mgmt_subnet' the VLAN and SVIs will be created automatically on this switch as well as all 'uplink_switches'.
                        When using 'inband_mgmt_ip' the VLAN and SVI will only be created on this device and added to uplink trunk. The VLAN and
                        SVI on the parent switches must be created using network services data models.
                        """
                        mpls_overlay_role: Literal["client", "server", "none"] | None = None
                        """
                        Set the default mpls overlay role.
                        Acting role in overlay control plane.
                        """
                        overlay_address_families: list[str] | None = None
                        """
                        Set the default overlay address families.
                        """
                        mpls_route_reflectors: list[str] | None = None
                        """
                        List of inventory hostname acting as MPLS route-reflectors.
                        """
                        bgp_cluster_id: Annotated[str, StrConvert(convert_types=(int))] | None = None
                        """
                        Set BGP cluster id.
                        """
                        ptp: Ptp | None = None
                        wan_role: Literal["client", "server"] | None = None
                        """
                        Override the default WAN role.

                        This is used both for AutoVPN and Pathfinder designs.
                        That means if `wan_mode` root key
                        is set to `autovpn` or `cv-pathfinder`.
                        `server` indicates that the router is a route-reflector.

                        Only supported if
                        `overlay_routing_protocol` is set to `ibgp`.
                        """
                        cv_pathfinder_transit_mode: Literal["region", "zone"] | None = None
                        """
                        Configure the transit mode for a WAN client for CV Pathfinder designs
                        only when the `wan_mode` root key is set to
                        `cv_pathfinder`.

                        'zone' is currently not supported.
                        """
                        cv_pathfinder_region: str | None = None
                        """
                        The CV Pathfinder region name.
                        This key is required for WAN routers but optional for pathfinders.
                        The region name must
                        be defined under 'cv_pathfinder_regions'.
                        """
                        cv_pathfinder_site: str | None = None
                        """
                        The CV Pathfinder site name.
                        This key is required for WAN routers but ignored for pathfinders.
                        The site name must be
                        defined for the relevant region under 'cv_pathfinder_regions'.
                        """
                        wan_ha: WanHa | None = None
                        """
                        PREVIEW: This key is currently not supported

                        The key is supported only if `wan_mode` == `cv-pathfinder`.
                        AutoVPN
                        support is still to be determined.

                        Maximum 2 devices supported by group for HA.
                        """
                        dps_mss_ipv4: Annotated[str, StrConvert(convert_types=(int))] | None = "auto"
                        """
                        IPv4 MSS value configured under "router path-selection" on WAN Devices.
                        """
                        l3_interfaces: list[L3InterfacesItem] | None = None
                        """
                        L3 Interfaces to configure on the node.
                        Used to define the node for WAN interfaces when `wan_carrier` is set.
                        """
                        data_plane_cpu_allocation_max: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=128)
                        """
                        Set the maximum number of CPU used for the data plane.
                        This setting is useful on virtual Route Reflectors and
                        Pathfinders where more CPU cores should be allocated for control plane.
                        """

                    class LinkTracking(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        class GroupsItem(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            name: str | None = None
                            """
                            Tracking group name.
                            """
                            recovery_delay: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=3600)
                            """
                            default -> platform_settings_mlag_reload_delay -> 300.
                            """
                            links_minimum: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=100000)

                        enabled: bool | None = False
                        groups: list[GroupsItem] | None = Field([{"name": "LT_GROUP1"}], validate_default=True)
                        """
                        Link Tracking Groups.
                        By default a single group named "LT_GROUP1" is defined with default values.
                        Any groups defined
                        under "groups" will replace the default.
                        """

                    class LacpPortIdRange(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        enabled: bool | None = False
                        size: Annotated[int, IntConvert(convert_types=(str))] | None = 128
                        """
                        Recommended size > = number of ports in the switch.
                        """
                        offset: Annotated[int, IntConvert(convert_types=(str))] | None = 0
                        """
                        Offset is used to avoid overlapping port-id ranges of different switches.
                        Useful when a "connected-endpoint" is
                        connected to switches in different "node_groups".
                        """

                    class StructuredConfig(EosCliConfigGen, BaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        pass

                    class UplinkPtp(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        enable: bool | None = False

                    class UplinkMacsec(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        profile: str | None = None

                    class MlagPortChannelStructuredConfig(EosCliConfigGen.PortChannelInterfacesItem, BaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        pass

                    class MlagPeerVlanStructuredConfig(EosCliConfigGen.VlanInterfacesItem, BaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        pass

                    class MlagPeerL3VlanStructuredConfig(EosCliConfigGen.VlanInterfacesItem, BaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        pass

                    class Filter(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        tenants: list[str] | None = Field(["all"], validate_default=True)
                        """
                        Limit configured Network Services to those defined under these Tenants. Set to ['all'] for all Tenants (default).
                        This
                        list also limits Tenants included by `always_include_vrfs_in_tenants`.
                        """
                        tags: list[str] | None = Field(["all"], validate_default=True)
                        """
                        Limit configured VLANs to those matching the given tags. Set to ['all'] for all VLANs (default).
                        """
                        allow_vrfs: list[Annotated[str, StrConvert(convert_types=(int))]] | None = Field(["all"], validate_default=True)
                        """
                        Limit configured Network Services to those defined under these VRFs. Set to ['all'] for all VRFs (default).
                        This list
                        also limits VRFs included by `always_include_vrfs_in_tenants`.
                        """
                        deny_vrfs: list[Annotated[str, StrConvert(convert_types=(int))]] | None = Field(["all"], validate_default=True)
                        """
                        Prevent configuration of Network Services defined under these VRFs.
                        This list prevents the given VRFs to be included by
                        any other filtering mechanism.
                        """
                        always_include_vrfs_in_tenants: list[str] | None = None
                        """
                        List of tenants where VRFs will be configured even if VLANs are not included in tags.
                        Useful for L3 "border" leaf.
                        """
                        only_vlans_in_use: bool | None = False
                        """
                        Only configure VLANs, SVIs, VRFs in use by connected endpoints or downstream L2 switches.
                        Note! This feature only
                        considers configuration managed by eos_designs.
                        This excludes structured_config, custom_structured_configuration_,
                        raw_eos_cli, eos_cli, custom templates, configlets etc.
                        """

                    class EvpnGateway(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        class RemotePeersItem(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            hostname: str | None = None
                            """
                            Hostname of remote EVPN GW server.
                            """
                            ip_address: str | None = None
                            """
                            Peering IP of remote Route Server.
                            """
                            bgp_as: Annotated[str, StrConvert(convert_types=(int, float))] | None = None
                            """
                            Remote Route Server's BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
                            For asdot notation in
                            YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number.
                            """

                        class EvpnL2(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            enabled: bool | None = False

                        class EvpnL3(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            enabled: bool | None = False
                            inter_domain: bool | None = True

                        remote_peers: list[RemotePeersItem] | None = None
                        """
                        Define remote peers of the EVPN VXLAN Gateway.
                        If the hostname can be found in the inventory, ip_address and BGP ASN
                        will be automatically populated. Manual override takes precedence.
                        If the peer's hostname can not be found in the
                        inventory, ip_address and bgp_as must be defined.
                        """
                        evpn_l2: EvpnL2 | None = None
                        """
                        Enable EVPN Gateway functionality for route-types 2 (MAC-IP) and 3 (IMET).
                        """
                        evpn_l3: EvpnL3 | None = None
                        """
                        Enable EVPN Gateway functionality for route-type 5 (IP-PREFIX).
                        """

                    class IpvpnGateway(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        class RemotePeersItem(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            hostname: str = None
                            """
                            Hostname of remote IPVPN Peer.
                            """
                            ip_address: str = None
                            """
                            Peering IP of remote IPVPN Peer.
                            """
                            bgp_as: Annotated[str, StrConvert(convert_types=(int, float))] = None
                            """
                            Remote IPVPN Peer's BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
                            For asdot notation in
                            YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number.
                            """

                        enabled: bool = None
                        evpn_domain_id: str | None = "65535:1"
                        """
                        Domain ID to assign to EVPN address family for use with D-path. Format <nn>:<nn>.
                        """
                        ipvpn_domain_id: str | None = "65535:2"
                        """
                        Domain ID to assign to IPVPN address families for use with D-path. Format <nn>:<nn>.
                        """
                        enable_d_path: bool | None = True
                        """
                        Enable D-path for use with BGP bestpath selection algorithm.
                        """
                        maximum_routes: Annotated[int, IntConvert(convert_types=(str))] | None = 0
                        """
                        Maximum routes to accept from IPVPN remote peers.
                        """
                        local_as: Annotated[str, StrConvert(convert_types=(int))] | None = "none"
                        """
                        Local BGP AS applied to peering with IPVPN remote peers.
                        BGP AS <1-4294967295> or AS number in asdot notation
                        "<1-65535>.<0-65535>".
                        For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being
                        interpreted as a float number.
                        """
                        address_families: list[str] | None = Field(["vpn-ipv4"], validate_default=True)
                        """
                        IPVPN address families to enable for remote peers.
                        """
                        remote_peers: list[RemotePeersItem] | None = None

                    class Ptp(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        class Dscp(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            general_messages: Annotated[int, IntConvert(convert_types=(str))] | None = None
                            event_messages: Annotated[int, IntConvert(convert_types=(str))] | None = None

                        class Monitor(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            class Threshold(AvdDictBaseModel):
                                model_config = ConfigDict(defer_build=True, extra="forbid")

                                class Drop(AvdDictBaseModel):
                                    model_config = ConfigDict(defer_build=True, extra="forbid")

                                    offset_from_master: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=1000000000)
                                    mean_path_delay: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=1000000000)

                                offset_from_master: Annotated[int, IntConvert(convert_types=(str))] | None = Field(250, ge=0, le=1000000000)
                                mean_path_delay: Annotated[int, IntConvert(convert_types=(str))] | None = Field(1500, ge=0, le=1000000000)
                                drop: Drop | None = None

                            class MissingMessage(AvdDictBaseModel):
                                model_config = ConfigDict(defer_build=True, extra="forbid")

                                class Intervals(AvdDictBaseModel):
                                    model_config = ConfigDict(defer_build=True, extra="forbid")

                                    announce: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=2, le=255)
                                    follow_up: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=2, le=255)
                                    sync: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=2, le=255)

                                class SequenceIds(AvdDictBaseModel):
                                    model_config = ConfigDict(defer_build=True, extra="forbid")

                                    enabled: bool | None = True
                                    announce: Annotated[int, IntConvert(convert_types=(str))] | None = Field(3, ge=2, le=255)
                                    delay_resp: Annotated[int, IntConvert(convert_types=(str))] | None = Field(3, ge=2, le=255)
                                    follow_up: Annotated[int, IntConvert(convert_types=(str))] | None = Field(3, ge=2, le=255)
                                    sync: Annotated[int, IntConvert(convert_types=(str))] | None = Field(3, ge=2, le=255)

                                intervals: Intervals | None = None
                                sequence_ids: SequenceIds | None = None

                            enabled: bool | None = True
                            threshold: Threshold | None = None
                            missing_message: MissingMessage | None = None

                        enabled: bool | None = False
                        profile: Literal["aes67", "smpte2059-2", "aes67-r16-2016"] | None = "aes67-r16-2016"
                        mlag: bool | None = False
                        """
                        Configure PTP on the MLAG peer-link port-channel when PTP is enabled. By default PTP will not be configured on the MLAG
                        peer-link port-channel.
                        """
                        domain: Annotated[int, IntConvert(convert_types=(str))] | None = Field(127, ge=0, le=255)
                        priority1: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=255)
                        """
                        default -> automatically set based on node_type.
                        """
                        priority2: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=255)
                        """
                        default -> (node_id modulus 256).
                        """
                        auto_clock_identity: bool | None = True
                        """
                        If you prefer to have PTP clock identity be the system MAC-address of the switch, which is the default EOS behaviour,
                        simply disable the automatic PTP clock identity.
                        default -> (clock_identity_prefix = 00:1C:73 (default)) + (PTP priority
                        1 as HEX) + ":00:" + (PTP priority 2 as HEX).
                        """
                        clock_identity_prefix: str | None = None
                        """
                        PTP clock idetentiy 3-byte prefix. i.e. "01:02:03".
                        By default the 3-byte prefix is "00:1C:73".
                        This can be overridden
                        if auto_clock_identity is set to true (which is the default).
                        """
                        clock_identity: str | None = None
                        """
                        Set PTP clock identity manually. 6-byte value i.e. "01:02:03:04:05:06".
                        """
                        source_ip: str | None = None
                        """
                        By default in EOS, PTP packets are sourced with an IP address from the routed port or from the relevant SVI, which is
                        the recommended behaviour.
                        This can be set manually if required, for example, to a value of "10.1.2.3".
                        """
                        mode: Literal["boundary"] | None = "boundary"
                        mode_one_step: bool | None = False
                        ttl: Annotated[int, IntConvert(convert_types=(str))] | None = None
                        forward_unicast: bool | None = False
                        """
                        Enable PTP unicast forwarding.
                        """
                        dscp: Dscp | None = None
                        monitor: Monitor | None = None

                    class WanHa(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        enabled: bool | None = True
                        """
                        Enable / Disable auto CV-Pathfinder HA, when two nodes are defined in the same node_group.
                        """
                        ipsec: bool | None = True
                        """
                        Enable / Disable IPsec over HA path-group when HA is enabled.
                        """

                    class L3InterfacesItem(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        class StaticRoutesItem(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            prefix: str = None
                            """
                            IPv4_network/Mask
                            """

                        class StructuredConfig(EosCliConfigGen.EthernetInterfacesItem, BaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            pass

                        profile: str | None = None
                        """
                        L3 interface profile name. Profile defined under `l3_interface_profiles`.
                        """
                        name: str = Field(None, pattern=r"Ethernet[\d/]+(.[\d]+)?")
                        """
                        Ethernet interface name like 'Ethernet2' or subinterface name like 'Ethernet2.42'
                        For a subinterface, the parent
                        physical interface is automatically created.
                        """
                        description: str | None = None
                        """
                        Interface description.
                        If not set a default description will be configured with '[<peer>[ <peer_interface>]]'
                        """
                        ip_address: str | None = None
                        """
                        Node IPv4 address/Mask or 'dhcp'.
                        """
                        dhcp_ip: str | None = None
                        """
                        When the `ip_address` is `dhcp`, this optional field allows to indicate the expected
                        IPv4 address (without mask) to be
                        allocated on the interface if known.
                        This is not rendered in the configuration but can be used for substitution of
                        'interface_ip' in the Access-list
                        set under `ipv4_acl_in` and `ipv4_acl_out`.
                        """
                        public_ip: str | None = None
                        """
                        Node IPv4 address (no mask).

                        This is used to get the public IP (if known) when the device is behind NAT.
                        This is only
                        used for `wan_rr` routers (AutoVPN RRs and Pathfinders) to determine the Public IP
                        with the following preference:
                        `wan_route_servers.path_groups.interfaces.ip_address`
                              -> `l3_interfaces.public_ip`
                                  ->
                        `l3_interfaces.ip_address`

                        The determined Public IP is used by WAN routers when peering with this interface.
                        """
                        encapsulation_dot1q_vlan: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=4094)
                        """
                        For subinterfaces the dot1q vlan is derived from the interface name by default, but can also be specified.
                        """
                        dhcp_accept_default_route: bool | None = True
                        """
                        Accept a default route from DHCP if `ip_address` is set to `dhcp`.
                        """
                        enabled: bool | None = True
                        """
                        Enable or Shutdown the interface.
                        """
                        speed: str | None = None
                        """
                        Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`.
                        """
                        peer: str | None = None
                        """
                        The peer device name. Used for description and documentation
                        """
                        peer_interface: str | None = None
                        """
                        The peer device interface. Used for description and documentation
                        """
                        peer_ip: str | None = None
                        """
                        The peer device IPv4 address (no mask). Used as default route gateway if `set_default_route` is true and `ip` is an IP
                        address.
                        """
                        ipv4_acl_in: Annotated[str, StrConvert(convert_types=(int))] | None = None
                        """
                        Name of the IPv4 access-list to be assigned in the ingress direction.
                        The access-list must be defined under `ipv4_acls`.
                        Required for all WAN interfaces (`wan_carrier` is set) unless the carrier is marked as 'trusted' under `wan_carriers`.
                        """
                        ipv4_acl_out: Annotated[str, StrConvert(convert_types=(int))] | None = None
                        """
                        Name of the IPv4 Access-list to be assigned in the egress direction.
                        The access-list must be defined under `ipv4_acls`.
                        """
                        static_routes: list[StaticRoutesItem] | None = Field(None, min_length=1)
                        """
                        Configure IPv4 static routes pointing to `peer_ip`.
                        """
                        qos_profile: str | None = None
                        """
                        QOS service profile.
                        """
                        wan_carrier: str | None = None
                        """
                        The WAN carrier this interface is connected to.
                        This is used to infer the path-groups in which this interface should be
                        configured.
                        Unless the carrier is marked as 'trusted' under `wan_carriers`, `ipv4_acl_in` is also required on all WAN
                        interfaces.
                        """
                        wan_circuit_id: Annotated[str, StrConvert(convert_types=(int))] | None = None
                        """
                        The WAN circuit ID for this interface.
                        This is not rendered in the configuration but used for WAN designs.
                        """
                        connected_to_pathfinder: bool | None = True
                        """
                        For a WAN interface (`wan_carrier` is set), allow to disable the static tunnel towards Pathfinders.
                        """
                        raw_eos_cli: str | None = None
                        """
                        EOS CLI rendered directly on the interface in the final EOS configuration.
                        """
                        structured_config: StructuredConfig | None = None
                        """
                        Custom structured config for the Ethernet interface.
                        """

                    group: str = None
                    """
                    The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.
                    The Node Group Name is also used for peer
                    description on downstream switches' uplinks.
                    """
                    nodes: list[NodesItem] | None = None
                    """
                    Define variables per node.
                    """
                    id: Annotated[int, IntConvert(convert_types=(str))] | None = None
                    """
                    Unique identifier used for IP addressing and other algorithms.
                    """
                    platform: Annotated[str, StrConvert(convert_types=(int))] | None = None
                    """
                    Arista platform family.
                    """
                    mac_address: str | None = None
                    """
                    Leverage to document management interface mac address.
                    """
                    system_mac_address: str | None = None
                    """
                    System MAC Address in this following format: "xx:xx:xx:xx:xx:xx".
                    Set to the same MAC address as available in "show
                    version" on the device.
                    "system_mac_address" can also be set directly as a hostvar.
                    If both are set, the setting under
                    node type settings takes precedence.
                    """
                    serial_number: str | None = None
                    """
                    Set to the Serial Number of the device.
                    Only used for documentation purpose in the fabric documentation and part of the
                    structured_config.
                    "serial_number" can also be set directly as a hostvar.
                    If both are set, the setting under node type
                    settings takes precedence.
                    """
                    rack: str | None = None
                    """
                    Rack that the switch is located in (only used in snmp_settings location).
                    """
                    mgmt_ip: str | None = None
                    """
                    Node management interface IPv4 address.
                    """
                    ipv6_mgmt_ip: str | None = None
                    """
                    Node management interface IPv6 address.
                    """
                    mgmt_interface: str | None = None
                    """
                    Management Interface Name.
                    Default -> platform_management_interface -> mgmt_interface -> "Management1".
                    """
                    link_tracking: LinkTracking | None = None
                    """
                    This configures the Link Tracking Group on a switch as well as adds the p2p-uplinks of the switch as the upstream
                    interfaces.
                    Useful in EVPN multhoming designs.
                    """
                    lacp_port_id_range: LacpPortIdRange | None = None
                    """
                    This will generate the "lacp port-id range", "begin" and "end" values based on node "id" and the number of nodes in the
                    "node_group".
                    Unique LACP port-id ranges are recommended for EVPN Multihoming designs.
                    """
                    always_configure_ip_routing: bool | None = False
                    """
                    Force configuration of "ip routing" even on L2 devices.
                    Use this to retain behavior of AVD versions below 4.0.0.
                    """
                    raw_eos_cli: str | None = None
                    """
                    EOS CLI rendered directly on the root level of the final EOS configuration.
                    """
                    structured_config: StructuredConfig | None = None
                    """
                    Custom structured config for eos_cli_config_gen.
                    """
                    uplink_type: Literal["p2p", "port-channel", "p2p-vrfs", "lan"] | None = "p2p"
                    """
                    Override the default `uplink_type` set at the `node_type_key` level.
                    `uplink_type` must be "p2p" if `vtep` or
                    `underlay_router` is true for the `node_type_key` definition.
                    """
                    uplink_ipv4_pool: str | None = None
                    """
                    IPv4 subnet to use to connect to uplink switches.
                    """
                    uplink_interfaces: list[str] | None = None
                    """
                    Local uplink interfaces
                    Each list item supports range syntax that can be expanded into a list of interfaces.
                    If
                    uplink_interfaces is not defined, platform-specific defaults (defined under default_interfaces) will be used instead.
                    Please note that default_interfaces are not defined by default, you should define these yourself.
                    """
                    uplink_switch_interfaces: list[str] | None = None
                    """
                    Interfaces located on uplink switches.
                    """
                    uplink_switches: list[str] | None = None
                    uplink_interface_speed: str | None = None
                    """
                    Set point-to-Point interface speed and will apply to uplink interfaces on both ends.
                    (Uplink switch interface speed can
                    be overridden with `uplink_switch_interface_speed`).
                    Speed should be set in the format `<interface_speed>` or `forced
                    <interface_speed>` or `auto <interface_speed>`.
                    """
                    uplink_switch_interface_speed: str | None = None
                    """
                    Set point-to-Point interface speed for the uplink switch interface only.
                    Speed should be set in the format
                    `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`.
                    """
                    max_uplink_switches: Annotated[int, IntConvert(convert_types=(str))] | None = None
                    """
                    Maximum number of uplink switches.
                    Changing this value may change IP Addressing on uplinks.
                    Can be used to reserve IP
                    space for future expansions.
                    """
                    max_parallel_uplinks: Annotated[int, IntConvert(convert_types=(str))] | None = None
                    """
                    Number of parallel links towards uplink switches.
                    Changing this value may change interface naming on uplinks (and
                    corresponding downlinks).
                    Can be used to reserve interfaces for future parallel uplinks.
                    """
                    uplink_bfd: bool | None = False
                    """
                    Enable bfd on uplink interfaces.
                    """
                    uplink_native_vlan: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=4094)
                    """
                    Only applicable to switches with layer-2 port-channel uplinks.
                    A suspended (disabled) vlan will be created in both ends
                    of the link unless the vlan is defined under network services.
                    By default the uplink will not have a native_vlan
                    configured, so EOS defaults to vlan 1.
                    """
                    uplink_ptp: UplinkPtp | None = None
                    """
                    Enable PTP on all infrastructure links.
                    """
                    uplink_macsec: UplinkMacsec | None = None
                    """
                    Enable MacSec on all uplinks.
                    """
                    uplink_port_channel_id: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=999999)
                    """
                    Only applicable for L2 switches with `uplink_type: port-channel`.
                    By default the uplink Port-channel ID will be set to
                    the number of the lowest member interface defined under `uplink_interfaces`.
                    For example:
                      member ports [ Eth22, Eth23
                    ] -> ID 22
                      member ports [ Eth11/1, Eth22/1 ] -> ID 111
                    For MLAG port-channels ID will be based on the lowest member
                    interface on the first MLAG switch.
                    This option overrides the default behavior and statically sets the local Port-
                    channel ID.
                    Note! Make sure the ID is unique and does not overlap with autogenerated Port-channel IDs in the Network
                    Services.
                    Note! For MLAG pairs the ID must be between 1 and 2000 and both MLAG switches must have the same value.
                    """
                    uplink_switch_port_channel_id: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=999999)
                    """
                    Only applicable for L2 switches with `uplink_type: port-channel`.
                    By default the uplink switch Port-channel ID will be
                    set to the number of the first interface defined under `uplink_switch_interfaces`.
                    For example:
                      member ports [ Eth22,
                    Eth23 ] -> ID 22
                      member ports [ Eth11/1, Eth22/1 ] -> ID 111
                    For MLAG port-channels ID will be based on the lowest
                    member interface on the first MLAG switch.
                    This option overrides the default behavior and statically sets the Port-
                    channel ID on the uplink switch.
                    Note! Make sure the ID is unique and does not overlap with autogenerated Port-channel
                    IDs in the Network Services.
                    Note! For MLAG pairs the ID must be between 1 and 2000 and both MLAG switches must have the
                    same value.
                    """
                    uplink_structured_config: dict | None = None
                    """
                    Custom structured config applied to "uplink_interfaces", and "uplink_switch_interfaces".
                    When uplink_type == "p2p",
                    custom structured config added under ethernet_interfaces.[name=<interface>] for eos_cli_config_gen overrides the
                    settings on the ethernet interface level.
                    When uplink_type == "port-channel", custom structured config added under
                    port_channel_interfaces.[name=<interface>] for eos_cli_config_gen overrides the settings on the port-channel interface
                    level.
                    "uplink_structured_config" is applied after "structured_config", so it can override "structured_config" defined
                    on node-level.
                    Note! The content of this dictionary is _not_ validated by the schema, since it can be either
                    ethernet_interfaces or port_channel_interfaces.
                    """
                    mlag_port_channel_structured_config: MlagPortChannelStructuredConfig | None = None
                    """
                    Custom structured config applied to MLAG peer link port-channel id.
                    Added under
                    port_channel_interfaces.[name=<interface>] for eos_cli_config_gen.
                    Overrides the settings on the port-channel interface
                    level.
                    "mlag_port_channel_structured_config" is applied after "structured_config", so it can override
                    "structured_config" defined on node-level.
                    """
                    mlag_peer_vlan_structured_config: MlagPeerVlanStructuredConfig | None = None
                    """
                    Custom structured config applied to MLAG Peer Link (control link) SVI interface id.
                    Added under
                    vlan_interfaces.[name=<interface>] for eos_cli_config_gen.
                    Overrides the settings on the vlan interface level.
                    "mlag_peer_vlan_structured_config" is applied after "structured_config", so it can override "structured_config" defined
                    on node-level.
                    """
                    mlag_peer_l3_vlan_structured_config: MlagPeerL3VlanStructuredConfig | None = None
                    """
                    Custom structured config applied to MLAG underlay L3 peering SVI interface id.
                    Added under
                    vlan_interfaces.[name=<interface>] for eos_cli_config_gen.
                    Overrides the settings on the vlan interface level.
                    "mlag_peer_l3_vlan_structured_config" is applied after "structured_config", so it can override "structured_config"
                    defined on node-level.
                    """
                    short_esi: str | None = None
                    """
                    short_esi only valid for l2leaf devices using port-channel uplink.
                    Setting short_esi to "auto" generates the short_esi
                    automatically using a hash of configuration elements.
                    < 0000:0000:0000 | auto >.
                    """
                    isis_system_id_prefix: str | None = Field(None, pattern=r"[0-9a-f]{4}\.[0-9a-f]{4}")
                    """
                    (4.4 hexadecimal).
                    """
                    isis_maximum_paths: Annotated[int, IntConvert(convert_types=(str))] | None = None
                    """
                    Number of path to configure in ECMP for ISIS.
                    """
                    is_type: Literal["level-1-2", "level-1", "level-2"] | None = "level-2"
                    node_sid_base: Annotated[int, IntConvert(convert_types=(str))] | None = 0
                    """
                    Node-SID base for isis-sr underlay variants. Combined with node id to generate ISIS-SR node-SID.
                    """
                    loopback_ipv4_pool: str | None = None
                    """
                    IPv4 subnet for Loopback0 allocation.
                    """
                    vtep_loopback_ipv4_pool: str | None = None
                    """
                    IPv4 subnet for VTEP-Loopback allocation.
                    """
                    loopback_ipv4_offset: Annotated[int, IntConvert(convert_types=(str))] | None = 0
                    """
                    Offset all assigned loopback IP addresses.
                    Required when the < loopback_ipv4_pool > is same for 2 different node_types
                    (like spine and l3leaf) to avoid over-lapping IPs.
                    For example, set the minimum offset
                    l3leaf.defaults.loopback_ipv4_offset: < total # spine switches > or vice versa.
                    """
                    loopback_ipv6_pool: str | None = None
                    """
                    IPv6 subnet for Loopback0 allocation.
                    """
                    loopback_ipv6_offset: Annotated[int, IntConvert(convert_types=(str))] | None = 0
                    """
                    Offset all assigned loopback IPv6 addresses.
                    Required when the < loopback_ipv6_pool > is same for 2 different node_types
                    (like spine and l3leaf) to avoid overlapping IPs.
                    For example, set the minimum offset
                    l3leaf.defaults.loopback_ipv6_offset: < total # spine switches > or vice versa.
                    """
                    vtep: bool | None = None
                    """
                    Node is configured as a VTEP when applicable based on 'overlay_routing_protocol'.
                    Overrides VTEP setting inherited from
                    node_type_keys.
                    """
                    vtep_loopback: str | None = Field(None, pattern=r"Loopback[\d/]+")
                    """
                    Set VXLAN source interface.
                    """
                    bgp_as: Annotated[str, StrConvert(convert_types=(int, float))] | None = None
                    """
                    BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
                    For asdot notation in YAML inputs, the value
                    must be put in quotes, to prevent it from being interpreted as a float number.
                    Required with eBGP.
                    """
                    bgp_defaults: list[str] | None = None
                    """
                    List of EOS commands to apply to BGP daemon.
                    """
                    evpn_role: Literal["client", "server", "none"] | None = None
                    """
                    Acting role in EVPN control plane.
                    Default is set in node_type definition from node_type_keys.
                    """
                    evpn_route_servers: list[str] | None = None
                    """
                    List of nodes acting as EVPN Route-Servers / Route-Reflectors.
                    """
                    evpn_services_l2_only: bool | None = False
                    """
                    Possibility to prevent configuration of Tenant VRFs and SVIs.
                    Override node definition "network_services_l3" from
                    node_type_keys.
                    This allows support for centralized routing.
                    """
                    filter: Filter | None = None
                    """
                    Filter L3 and L2 network services based on tenant and tags (and operation filter).
                    If filter is not defined it will
                    default to all.
                    """
                    igmp_snooping_enabled: bool | None = True
                    """
                    Activate or deactivate IGMP snooping on device level.
                    """
                    evpn_gateway: EvpnGateway | None = None
                    """
                    Node is acting as EVPN Multi-Domain Gateway.
                    New BGP peer-group is generated between EVPN GWs in different domains or
                    between GWs and Route Servers.
                    Name can be changed under "bgp_peer_groups.evpn_overlay_core" variable.
                    L3 rechability
                    for different EVPN GWs must be already in place, it is recommended to use DCI & L3 Edge if Route Servers and GWs are not
                    defined under the same Ansible inventory.
                    """
                    ipvpn_gateway: IpvpnGateway | None = None
                    """
                    Node is acting as IP-VPN Gateway for EVPN to MPLS-IP-VPN Interworking. The BGP peer group used for this is
                    "bgp_peer_groups.ipvpn_gateway_peers".
                    L3 Reachability is required for this to work, the preferred method to establish
                    underlay connectivity is to use core_interfaces.
                    """
                    mlag: bool | None = True
                    """
                    Enable / Disable auto MLAG, when two nodes are defined in node group.
                    """
                    mlag_dual_primary_detection: bool | None = False
                    """
                    Enable / Disable MLAG dual primary detection.
                    """
                    mlag_ibgp_origin_incomplete: bool | None = True
                    """
                    Set origin of routes received from MLAG iBGP peer to incomplete.
                    The purpose is to optimize routing for leaf loopbacks
                    from spine perspective and
                    avoid suboptimal routing via peerlink for control plane traffic.
                    """
                    mlag_interfaces: list[str] | None = None
                    """
                    Each list item supports range syntax that can be expanded into a list of interfaces.
                    Required when MLAG leafs are
                    present in the topology.
                    """
                    mlag_interfaces_speed: str | None = None
                    """
                    Set MLAG interface speed.
                    Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto
                    <interface_speed>`.
                    """
                    mlag_peer_l3_vlan: Annotated[int, IntConvert(convert_types=(str, bool))] | None = Field(4093, ge=0, le=4094)
                    """
                    Underlay L3 peering SVI interface id.
                    If set to 0 or the same vlan as mlag_peer_vlan, the mlag_peer_vlan will be used
                    for L3 peering.
                    """
                    mlag_peer_l3_ipv4_pool: str | None = None
                    """
                    IP address pool used for MLAG underlay L3 peering. IP is derived from the node id.
                    Required when MLAG leafs present in
                    topology and they are using a separate L3 peering VLAN.
                    """
                    mlag_peer_vlan: Annotated[int, IntConvert(convert_types=(str))] | None = Field(4094, ge=1, le=4094)
                    """
                    MLAG Peer Link (control link) SVI interface id.
                    """
                    mlag_peer_link_allowed_vlans: str | None = None
                    mlag_peer_ipv4_pool: str | None = None
                    """
                    IP address pool used for MLAG Peer Link (control link). IP is derived from the node id.
                    Required when MLAG leafs present
                    in topology.
                    """
                    mlag_port_channel_id: Annotated[int, IntConvert(convert_types=(str))] | None = None
                    """
                    If not set, the mlag port-channel id is generated based on the digits of the first interface present in
                    'mlag_interfaces'.
                    Valid port-channel id numbers are < 1-2000 > for EOS < 4.25.0F and < 1 - 999999 > for EOS >= 4.25.0F.
                    """
                    mlag_domain_id: str | None = None
                    """
                    MLAG Domain ID. If not set the node group name (Set with "group" key) will be used.
                    """
                    spanning_tree_mode: Literal["mstp", "rstp", "rapid-pvst", "none"] | None = None
                    spanning_tree_priority: Annotated[int, IntConvert(convert_types=(str))] | None = 32768
                    """
                    Spanning-tree priority configured for the selected mode.
                    For `rapid-pvst` the priority can also be set per VLAN under
                    network services.
                    """
                    spanning_tree_root_super: bool | None = False
                    virtual_router_mac_address: str | None = None
                    """
                    Virtual router mac address for anycast gateway.
                    """
                    inband_mgmt_interface: str | None = None
                    """
                    Pointer to interface used for inband management.
                    All configuration must be done using other data models like network
                    services or structured_config.
                    'inband_mgmt_interface' is only used to refer to this interface as source in various
                    management protocol settings (future feature).

                    On L2 switches, this defaults to Vlan<inband_mgmt_vlan> if either
                    'inband_mgmt_subnet' or 'inband_mgmt_ip' is set.
                    """
                    inband_mgmt_vlan: Annotated[int, IntConvert(convert_types=(str))] | None = 4092
                    """
                    VLAN number used for inband management on L2 switches (switches using port-channel trunks as uplinks).
                    When using
                    'inband_mgmt_subnet' the VLAN and SVIs will be created automatically on this switch as well as all 'uplink_switches'.
                    When using 'inband_mgmt_ip' the VLAN and SVI will only be created on this device and added to uplink trunk. The VLAN and
                    SVI on the parent switches must be created using network services data models.
                    """
                    inband_mgmt_subnet: str | None = None
                    """
                    Optional IP subnet assigned to inband management SVIs on L2 switches (switches using port-channels as uplinks).
                    Parent
                    l3leafs will have SVI with "ip virtual-router" and host-route injection based on ARP.
                    This allows all l3leafs to reuse
                    the same subnet across multiple racks without VXLAN extension.
                    SVI IP address will be assigned as follows:
                    virtual-
                    router: <subnet> + 1
                    l3leaf A      : <subnet> + 2 (same IP on all l3leaf A)
                    l3leaf B      : <subnet> + 3 (same IP on all
                    l3leaf B)
                    l2leafs       : <subnet> + 3 + <l2leaf id>
                    GW on l2leafs : <subnet> + 1
                    Assign range larger than total l2leafs
                    + 5

                    Setting is ignored if 'inband_mgmt_ip' is set.

                    This setting is applicable to L2 switches (switches using port-
                    channel trunks as uplinks).
                    """
                    inband_mgmt_ip: str | None = None
                    """
                    IP address assigned to the inband management interface set with 'inband_mgmt_vlan'.
                    This overrides 'inband_mgmt_subnet',
                    hence all behavior of 'inband_mgmt_subnet' is removed.

                    If this is set the VLAN and SVI will only be created on the L2
                    switch and added to uplink trunk.
                    The VLAN and SVI on the parent switches must be created using network services data
                    models.

                    This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).
                    """
                    inband_mgmt_gateway: str | None = None
                    """
                    Default gateway configured in the 'inband_mgmt_vrf' when using 'inband_mgmt_ip'. Otherwise gateway is derived from
                    'inband_mgmt_subnet' if set.

                    This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).
                    """
                    inband_mgmt_ipv6_address: str | None = None
                    """
                    IPv6 address assigned to the inband management interface set with 'inband_mgmt_vlan'.
                    This overrides
                    'inband_mgmt_ipv6_subnet', hence the configuration of 'inband_mgmt_ipv6_subnet' is ignored.

                    If this is set the VLAN and
                    SVI will only be created on the L2 switch and added to uplink trunk.
                    The VLAN and SVI on the parent switches must be
                    created using network services data models.

                    This setting is applicable to L2 switches (switches using port-channel
                    trunks as uplinks).
                    """
                    inband_mgmt_ipv6_subnet: str | None = None
                    """
                    Optional IPv6 prefix assigned to inband management SVIs on L2 switches (switches using port-channels as uplinks).
                    Parent
                    l3leafs will have SVI with "ipv6 virtual-router" and host-route injection based on ARP.
                    This allows all l3leafs to reuse
                    the same subnet across multiple racks without VXLAN extension.
                    SVI IP address will be assigned as follows:
                    virtual-
                    router: <subnet> + 1
                    l3leaf A      : <subnet> + 2 (same IP on all l3leaf A)
                    l3leaf B      : <subnet> + 3 (same IP on all
                    l3leaf B)
                    l2leafs       : <subnet> + 3 + <l2leaf id>
                    GW on l2leafs : <subnet> + 1
                    Assign range larger than total l2leafs
                    + 5

                    Setting is ignored if 'inband_mgmt_ipv6_address' is set.

                    This setting is applicable to L2 switches (switches using
                    port-channel trunks as uplinks).
                    """
                    inband_mgmt_ipv6_gateway: str | None = None
                    """
                    Default gateway configured in the 'inband_mgmt_vrf'.
                    Used when `inband_mgmt_ipv6_address` is set.
                    Ignored when
                    'inband_mgmt_ipv6_subnet' is set (first IP in subnet used as gateway).

                    This setting is applicable to L2 switches
                    (switches using port-channel trunks as uplinks).
                    """
                    inband_mgmt_description: str | None = "Inband Management"
                    """
                    Description configured on the Inband Management SVI.

                    This setting is only applied on the devices where it is set, it
                    does not automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-
                    group/node-type as needed.
                    """
                    inband_mgmt_vlan_name: str | None = "Inband Management"
                    """
                    Name configured on the Inband Management VLAN.
                    This setting is only applied on the devices where it is set, it does not
                    automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-group/node-
                    type as needed.
                    """
                    inband_mgmt_vrf: Annotated[str, StrConvert(convert_types=(int))] | None = "default"
                    """
                    VRF configured on the Inband Management Interface.
                    The VRF is created if not already created by other means.
                    This
                    setting is only applied on the devices where it is set, it does not automatically affect any parent/child devices
                    configuration, so it must be set on each applicable node/node-group/node-type as needed.
                    """
                    inband_mgmt_mtu: int | None = 1500
                    """
                    MTU configured on the Inband Management Interface.
                    This setting is only applied on the devices where it is set, it does
                    not automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-
                    group/node-type as needed.
                    """
                    inband_ztp: bool | None = False
                    """
                    Enable to configure upstream device with proper configuration to allow downstream devices to ZTP inband.
                    This setting
                    also requires that the `inband_mgmt_vlan` is set for the node.
                    """
                    inband_ztp_lacp_fallback_delay: int | None = Field(30, ge=0, le=300)
                    """
                    Set the LACP fallback timeout of the upstream device's port-channel towards the downstream inband ZTP node.
                    This setting
                    also requires that `inband_ztp` is set for the node.
                    """
                    inband_management_subnet: str | None = None
                    """
                    Optional IP subnet assigned to inband management SVIs on L2 switches (switches using port-channels as uplinks).
                    Parent
                    l3leafs will have SVI with "ip virtual-router" and host-route injection based on ARP.
                    This allows all l3leafs to reuse
                    the same subnet across multiple racks without VXLAN extension.
                    SVI IP address will be assigned as follows:
                    virtual-
                    router: <subnet> + 1
                    l3leaf A      : <subnet> + 2 (same IP on all l3leaf A)
                    l3leaf B      : <subnet> + 3 (same IP on all
                    l3leaf B)
                    l2leafs       : <subnet> + 3 + <l2leaf id>
                    GW on l2leafs : <subnet> + 1
                    Assign range larger than total l2leafs
                    + 5

                    Setting is ignored if 'inband_mgmt_ip' is set.

                    This setting is applicable to L2 switches (switches using port-
                    channel trunks as uplinks).
                    """
                    inband_management_vlan: Annotated[int, IntConvert(convert_types=(str))] | None = 4092
                    """
                    VLAN number used for inband management on L2 switches (switches using port-channel trunks as uplinks).
                    When using
                    'inband_mgmt_subnet' the VLAN and SVIs will be created automatically on this switch as well as all 'uplink_switches'.
                    When using 'inband_mgmt_ip' the VLAN and SVI will only be created on this device and added to uplink trunk. The VLAN and
                    SVI on the parent switches must be created using network services data models.
                    """
                    mpls_overlay_role: Literal["client", "server", "none"] | None = None
                    """
                    Set the default mpls overlay role.
                    Acting role in overlay control plane.
                    """
                    overlay_address_families: list[str] | None = None
                    """
                    Set the default overlay address families.
                    """
                    mpls_route_reflectors: list[str] | None = None
                    """
                    List of inventory hostname acting as MPLS route-reflectors.
                    """
                    bgp_cluster_id: Annotated[str, StrConvert(convert_types=(int))] | None = None
                    """
                    Set BGP cluster id.
                    """
                    ptp: Ptp | None = None
                    wan_role: Literal["client", "server"] | None = None
                    """
                    Override the default WAN role.

                    This is used both for AutoVPN and Pathfinder designs.
                    That means if `wan_mode` root key
                    is set to `autovpn` or `cv-pathfinder`.
                    `server` indicates that the router is a route-reflector.

                    Only supported if
                    `overlay_routing_protocol` is set to `ibgp`.
                    """
                    cv_pathfinder_transit_mode: Literal["region", "zone"] | None = None
                    """
                    Configure the transit mode for a WAN client for CV Pathfinder designs
                    only when the `wan_mode` root key is set to
                    `cv_pathfinder`.

                    'zone' is currently not supported.
                    """
                    cv_pathfinder_region: str | None = None
                    """
                    The CV Pathfinder region name.
                    This key is required for WAN routers but optional for pathfinders.
                    The region name must
                    be defined under 'cv_pathfinder_regions'.
                    """
                    cv_pathfinder_site: str | None = None
                    """
                    The CV Pathfinder site name.
                    This key is required for WAN routers but ignored for pathfinders.
                    The site name must be
                    defined for the relevant region under 'cv_pathfinder_regions'.
                    """
                    wan_ha: WanHa | None = None
                    """
                    PREVIEW: This key is currently not supported

                    The key is supported only if `wan_mode` == `cv-pathfinder`.
                    AutoVPN
                    support is still to be determined.

                    Maximum 2 devices supported by group for HA.
                    """
                    dps_mss_ipv4: Annotated[str, StrConvert(convert_types=(int))] | None = "auto"
                    """
                    IPv4 MSS value configured under "router path-selection" on WAN Devices.
                    """
                    l3_interfaces: list[L3InterfacesItem] | None = None
                    """
                    L3 Interfaces to configure on the node.
                    Used to define the node for WAN interfaces when `wan_carrier` is set.
                    """
                    data_plane_cpu_allocation_max: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=128)
                    """
                    Set the maximum number of CPU used for the data plane.
                    This setting is useful on virtual Route Reflectors and
                    Pathfinders where more CPU cores should be allocated for control plane.
                    """

                class NodesItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class LinkTracking(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        class GroupsItem(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            name: str | None = None
                            """
                            Tracking group name.
                            """
                            recovery_delay: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=3600)
                            """
                            default -> platform_settings_mlag_reload_delay -> 300.
                            """
                            links_minimum: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=100000)

                        enabled: bool | None = False
                        groups: list[GroupsItem] | None = Field([{"name": "LT_GROUP1"}], validate_default=True)
                        """
                        Link Tracking Groups.
                        By default a single group named "LT_GROUP1" is defined with default values.
                        Any groups defined
                        under "groups" will replace the default.
                        """

                    class LacpPortIdRange(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        enabled: bool | None = False
                        size: Annotated[int, IntConvert(convert_types=(str))] | None = 128
                        """
                        Recommended size > = number of ports in the switch.
                        """
                        offset: Annotated[int, IntConvert(convert_types=(str))] | None = 0
                        """
                        Offset is used to avoid overlapping port-id ranges of different switches.
                        Useful when a "connected-endpoint" is
                        connected to switches in different "node_groups".
                        """

                    class StructuredConfig(EosCliConfigGen, BaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        pass

                    class UplinkPtp(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        enable: bool | None = False

                    class UplinkMacsec(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        profile: str | None = None

                    class MlagPortChannelStructuredConfig(EosCliConfigGen.PortChannelInterfacesItem, BaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        pass

                    class MlagPeerVlanStructuredConfig(EosCliConfigGen.VlanInterfacesItem, BaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        pass

                    class MlagPeerL3VlanStructuredConfig(EosCliConfigGen.VlanInterfacesItem, BaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        pass

                    class Filter(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        tenants: list[str] | None = Field(["all"], validate_default=True)
                        """
                        Limit configured Network Services to those defined under these Tenants. Set to ['all'] for all Tenants (default).
                        This
                        list also limits Tenants included by `always_include_vrfs_in_tenants`.
                        """
                        tags: list[str] | None = Field(["all"], validate_default=True)
                        """
                        Limit configured VLANs to those matching the given tags. Set to ['all'] for all VLANs (default).
                        """
                        allow_vrfs: list[Annotated[str, StrConvert(convert_types=(int))]] | None = Field(["all"], validate_default=True)
                        """
                        Limit configured Network Services to those defined under these VRFs. Set to ['all'] for all VRFs (default).
                        This list
                        also limits VRFs included by `always_include_vrfs_in_tenants`.
                        """
                        deny_vrfs: list[Annotated[str, StrConvert(convert_types=(int))]] | None = Field(["all"], validate_default=True)
                        """
                        Prevent configuration of Network Services defined under these VRFs.
                        This list prevents the given VRFs to be included by
                        any other filtering mechanism.
                        """
                        always_include_vrfs_in_tenants: list[str] | None = None
                        """
                        List of tenants where VRFs will be configured even if VLANs are not included in tags.
                        Useful for L3 "border" leaf.
                        """
                        only_vlans_in_use: bool | None = False
                        """
                        Only configure VLANs, SVIs, VRFs in use by connected endpoints or downstream L2 switches.
                        Note! This feature only
                        considers configuration managed by eos_designs.
                        This excludes structured_config, custom_structured_configuration_,
                        raw_eos_cli, eos_cli, custom templates, configlets etc.
                        """

                    class EvpnGateway(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        class RemotePeersItem(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            hostname: str | None = None
                            """
                            Hostname of remote EVPN GW server.
                            """
                            ip_address: str | None = None
                            """
                            Peering IP of remote Route Server.
                            """
                            bgp_as: Annotated[str, StrConvert(convert_types=(int, float))] | None = None
                            """
                            Remote Route Server's BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
                            For asdot notation in
                            YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number.
                            """

                        class EvpnL2(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            enabled: bool | None = False

                        class EvpnL3(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            enabled: bool | None = False
                            inter_domain: bool | None = True

                        remote_peers: list[RemotePeersItem] | None = None
                        """
                        Define remote peers of the EVPN VXLAN Gateway.
                        If the hostname can be found in the inventory, ip_address and BGP ASN
                        will be automatically populated. Manual override takes precedence.
                        If the peer's hostname can not be found in the
                        inventory, ip_address and bgp_as must be defined.
                        """
                        evpn_l2: EvpnL2 | None = None
                        """
                        Enable EVPN Gateway functionality for route-types 2 (MAC-IP) and 3 (IMET).
                        """
                        evpn_l3: EvpnL3 | None = None
                        """
                        Enable EVPN Gateway functionality for route-type 5 (IP-PREFIX).
                        """

                    class IpvpnGateway(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        class RemotePeersItem(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            hostname: str = None
                            """
                            Hostname of remote IPVPN Peer.
                            """
                            ip_address: str = None
                            """
                            Peering IP of remote IPVPN Peer.
                            """
                            bgp_as: Annotated[str, StrConvert(convert_types=(int, float))] = None
                            """
                            Remote IPVPN Peer's BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
                            For asdot notation in
                            YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number.
                            """

                        enabled: bool = None
                        evpn_domain_id: str | None = "65535:1"
                        """
                        Domain ID to assign to EVPN address family for use with D-path. Format <nn>:<nn>.
                        """
                        ipvpn_domain_id: str | None = "65535:2"
                        """
                        Domain ID to assign to IPVPN address families for use with D-path. Format <nn>:<nn>.
                        """
                        enable_d_path: bool | None = True
                        """
                        Enable D-path for use with BGP bestpath selection algorithm.
                        """
                        maximum_routes: Annotated[int, IntConvert(convert_types=(str))] | None = 0
                        """
                        Maximum routes to accept from IPVPN remote peers.
                        """
                        local_as: Annotated[str, StrConvert(convert_types=(int))] | None = "none"
                        """
                        Local BGP AS applied to peering with IPVPN remote peers.
                        BGP AS <1-4294967295> or AS number in asdot notation
                        "<1-65535>.<0-65535>".
                        For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being
                        interpreted as a float number.
                        """
                        address_families: list[str] | None = Field(["vpn-ipv4"], validate_default=True)
                        """
                        IPVPN address families to enable for remote peers.
                        """
                        remote_peers: list[RemotePeersItem] | None = None

                    class Ptp(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        class Dscp(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            general_messages: Annotated[int, IntConvert(convert_types=(str))] | None = None
                            event_messages: Annotated[int, IntConvert(convert_types=(str))] | None = None

                        class Monitor(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            class Threshold(AvdDictBaseModel):
                                model_config = ConfigDict(defer_build=True, extra="forbid")

                                class Drop(AvdDictBaseModel):
                                    model_config = ConfigDict(defer_build=True, extra="forbid")

                                    offset_from_master: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=1000000000)
                                    mean_path_delay: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=1000000000)

                                offset_from_master: Annotated[int, IntConvert(convert_types=(str))] | None = Field(250, ge=0, le=1000000000)
                                mean_path_delay: Annotated[int, IntConvert(convert_types=(str))] | None = Field(1500, ge=0, le=1000000000)
                                drop: Drop | None = None

                            class MissingMessage(AvdDictBaseModel):
                                model_config = ConfigDict(defer_build=True, extra="forbid")

                                class Intervals(AvdDictBaseModel):
                                    model_config = ConfigDict(defer_build=True, extra="forbid")

                                    announce: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=2, le=255)
                                    follow_up: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=2, le=255)
                                    sync: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=2, le=255)

                                class SequenceIds(AvdDictBaseModel):
                                    model_config = ConfigDict(defer_build=True, extra="forbid")

                                    enabled: bool | None = True
                                    announce: Annotated[int, IntConvert(convert_types=(str))] | None = Field(3, ge=2, le=255)
                                    delay_resp: Annotated[int, IntConvert(convert_types=(str))] | None = Field(3, ge=2, le=255)
                                    follow_up: Annotated[int, IntConvert(convert_types=(str))] | None = Field(3, ge=2, le=255)
                                    sync: Annotated[int, IntConvert(convert_types=(str))] | None = Field(3, ge=2, le=255)

                                intervals: Intervals | None = None
                                sequence_ids: SequenceIds | None = None

                            enabled: bool | None = True
                            threshold: Threshold | None = None
                            missing_message: MissingMessage | None = None

                        enabled: bool | None = False
                        profile: Literal["aes67", "smpte2059-2", "aes67-r16-2016"] | None = "aes67-r16-2016"
                        mlag: bool | None = False
                        """
                        Configure PTP on the MLAG peer-link port-channel when PTP is enabled. By default PTP will not be configured on the MLAG
                        peer-link port-channel.
                        """
                        domain: Annotated[int, IntConvert(convert_types=(str))] | None = Field(127, ge=0, le=255)
                        priority1: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=255)
                        """
                        default -> automatically set based on node_type.
                        """
                        priority2: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=255)
                        """
                        default -> (node_id modulus 256).
                        """
                        auto_clock_identity: bool | None = True
                        """
                        If you prefer to have PTP clock identity be the system MAC-address of the switch, which is the default EOS behaviour,
                        simply disable the automatic PTP clock identity.
                        default -> (clock_identity_prefix = 00:1C:73 (default)) + (PTP priority
                        1 as HEX) + ":00:" + (PTP priority 2 as HEX).
                        """
                        clock_identity_prefix: str | None = None
                        """
                        PTP clock idetentiy 3-byte prefix. i.e. "01:02:03".
                        By default the 3-byte prefix is "00:1C:73".
                        This can be overridden
                        if auto_clock_identity is set to true (which is the default).
                        """
                        clock_identity: str | None = None
                        """
                        Set PTP clock identity manually. 6-byte value i.e. "01:02:03:04:05:06".
                        """
                        source_ip: str | None = None
                        """
                        By default in EOS, PTP packets are sourced with an IP address from the routed port or from the relevant SVI, which is
                        the recommended behaviour.
                        This can be set manually if required, for example, to a value of "10.1.2.3".
                        """
                        mode: Literal["boundary"] | None = "boundary"
                        mode_one_step: bool | None = False
                        ttl: Annotated[int, IntConvert(convert_types=(str))] | None = None
                        forward_unicast: bool | None = False
                        """
                        Enable PTP unicast forwarding.
                        """
                        dscp: Dscp | None = None
                        monitor: Monitor | None = None

                    class WanHa(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        enabled: bool | None = True
                        """
                        Enable / Disable auto CV-Pathfinder HA, when two nodes are defined in the same node_group.
                        """
                        ipsec: bool | None = True
                        """
                        Enable / Disable IPsec over HA path-group when HA is enabled.
                        """

                    class L3InterfacesItem(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        class StaticRoutesItem(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            prefix: str = None
                            """
                            IPv4_network/Mask
                            """

                        class StructuredConfig(EosCliConfigGen.EthernetInterfacesItem, BaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            pass

                        profile: str | None = None
                        """
                        L3 interface profile name. Profile defined under `l3_interface_profiles`.
                        """
                        name: str = Field(None, pattern=r"Ethernet[\d/]+(.[\d]+)?")
                        """
                        Ethernet interface name like 'Ethernet2' or subinterface name like 'Ethernet2.42'
                        For a subinterface, the parent
                        physical interface is automatically created.
                        """
                        description: str | None = None
                        """
                        Interface description.
                        If not set a default description will be configured with '[<peer>[ <peer_interface>]]'
                        """
                        ip_address: str | None = None
                        """
                        Node IPv4 address/Mask or 'dhcp'.
                        """
                        dhcp_ip: str | None = None
                        """
                        When the `ip_address` is `dhcp`, this optional field allows to indicate the expected
                        IPv4 address (without mask) to be
                        allocated on the interface if known.
                        This is not rendered in the configuration but can be used for substitution of
                        'interface_ip' in the Access-list
                        set under `ipv4_acl_in` and `ipv4_acl_out`.
                        """
                        public_ip: str | None = None
                        """
                        Node IPv4 address (no mask).

                        This is used to get the public IP (if known) when the device is behind NAT.
                        This is only
                        used for `wan_rr` routers (AutoVPN RRs and Pathfinders) to determine the Public IP
                        with the following preference:
                        `wan_route_servers.path_groups.interfaces.ip_address`
                              -> `l3_interfaces.public_ip`
                                  ->
                        `l3_interfaces.ip_address`

                        The determined Public IP is used by WAN routers when peering with this interface.
                        """
                        encapsulation_dot1q_vlan: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=4094)
                        """
                        For subinterfaces the dot1q vlan is derived from the interface name by default, but can also be specified.
                        """
                        dhcp_accept_default_route: bool | None = True
                        """
                        Accept a default route from DHCP if `ip_address` is set to `dhcp`.
                        """
                        enabled: bool | None = True
                        """
                        Enable or Shutdown the interface.
                        """
                        speed: str | None = None
                        """
                        Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`.
                        """
                        peer: str | None = None
                        """
                        The peer device name. Used for description and documentation
                        """
                        peer_interface: str | None = None
                        """
                        The peer device interface. Used for description and documentation
                        """
                        peer_ip: str | None = None
                        """
                        The peer device IPv4 address (no mask). Used as default route gateway if `set_default_route` is true and `ip` is an IP
                        address.
                        """
                        ipv4_acl_in: Annotated[str, StrConvert(convert_types=(int))] | None = None
                        """
                        Name of the IPv4 access-list to be assigned in the ingress direction.
                        The access-list must be defined under `ipv4_acls`.
                        Required for all WAN interfaces (`wan_carrier` is set) unless the carrier is marked as 'trusted' under `wan_carriers`.
                        """
                        ipv4_acl_out: Annotated[str, StrConvert(convert_types=(int))] | None = None
                        """
                        Name of the IPv4 Access-list to be assigned in the egress direction.
                        The access-list must be defined under `ipv4_acls`.
                        """
                        static_routes: list[StaticRoutesItem] | None = Field(None, min_length=1)
                        """
                        Configure IPv4 static routes pointing to `peer_ip`.
                        """
                        qos_profile: str | None = None
                        """
                        QOS service profile.
                        """
                        wan_carrier: str | None = None
                        """
                        The WAN carrier this interface is connected to.
                        This is used to infer the path-groups in which this interface should be
                        configured.
                        Unless the carrier is marked as 'trusted' under `wan_carriers`, `ipv4_acl_in` is also required on all WAN
                        interfaces.
                        """
                        wan_circuit_id: Annotated[str, StrConvert(convert_types=(int))] | None = None
                        """
                        The WAN circuit ID for this interface.
                        This is not rendered in the configuration but used for WAN designs.
                        """
                        connected_to_pathfinder: bool | None = True
                        """
                        For a WAN interface (`wan_carrier` is set), allow to disable the static tunnel towards Pathfinders.
                        """
                        raw_eos_cli: str | None = None
                        """
                        EOS CLI rendered directly on the interface in the final EOS configuration.
                        """
                        structured_config: StructuredConfig | None = None
                        """
                        Custom structured config for the Ethernet interface.
                        """

                    name: str = None
                    """
                    The Node Name is used as "hostname".
                    """
                    id: Annotated[int, IntConvert(convert_types=(str))] | None = None
                    """
                    Unique identifier used for IP addressing and other algorithms.
                    """
                    platform: Annotated[str, StrConvert(convert_types=(int))] | None = None
                    """
                    Arista platform family.
                    """
                    mac_address: str | None = None
                    """
                    Leverage to document management interface mac address.
                    """
                    system_mac_address: str | None = None
                    """
                    System MAC Address in this following format: "xx:xx:xx:xx:xx:xx".
                    Set to the same MAC address as available in "show
                    version" on the device.
                    "system_mac_address" can also be set directly as a hostvar.
                    If both are set, the setting under
                    node type settings takes precedence.
                    """
                    serial_number: str | None = None
                    """
                    Set to the Serial Number of the device.
                    Only used for documentation purpose in the fabric documentation and part of the
                    structured_config.
                    "serial_number" can also be set directly as a hostvar.
                    If both are set, the setting under node type
                    settings takes precedence.
                    """
                    rack: str | None = None
                    """
                    Rack that the switch is located in (only used in snmp_settings location).
                    """
                    mgmt_ip: str | None = None
                    """
                    Node management interface IPv4 address.
                    """
                    ipv6_mgmt_ip: str | None = None
                    """
                    Node management interface IPv6 address.
                    """
                    mgmt_interface: str | None = None
                    """
                    Management Interface Name.
                    Default -> platform_management_interface -> mgmt_interface -> "Management1".
                    """
                    link_tracking: LinkTracking | None = None
                    """
                    This configures the Link Tracking Group on a switch as well as adds the p2p-uplinks of the switch as the upstream
                    interfaces.
                    Useful in EVPN multhoming designs.
                    """
                    lacp_port_id_range: LacpPortIdRange | None = None
                    """
                    This will generate the "lacp port-id range", "begin" and "end" values based on node "id" and the number of nodes in the
                    "node_group".
                    Unique LACP port-id ranges are recommended for EVPN Multihoming designs.
                    """
                    always_configure_ip_routing: bool | None = False
                    """
                    Force configuration of "ip routing" even on L2 devices.
                    Use this to retain behavior of AVD versions below 4.0.0.
                    """
                    raw_eos_cli: str | None = None
                    """
                    EOS CLI rendered directly on the root level of the final EOS configuration.
                    """
                    structured_config: StructuredConfig | None = None
                    """
                    Custom structured config for eos_cli_config_gen.
                    """
                    uplink_type: Literal["p2p", "port-channel", "p2p-vrfs", "lan"] | None = "p2p"
                    """
                    Override the default `uplink_type` set at the `node_type_key` level.
                    `uplink_type` must be "p2p" if `vtep` or
                    `underlay_router` is true for the `node_type_key` definition.
                    """
                    uplink_ipv4_pool: str | None = None
                    """
                    IPv4 subnet to use to connect to uplink switches.
                    """
                    uplink_interfaces: list[str] | None = None
                    """
                    Local uplink interfaces
                    Each list item supports range syntax that can be expanded into a list of interfaces.
                    If
                    uplink_interfaces is not defined, platform-specific defaults (defined under default_interfaces) will be used instead.
                    Please note that default_interfaces are not defined by default, you should define these yourself.
                    """
                    uplink_switch_interfaces: list[str] | None = None
                    """
                    Interfaces located on uplink switches.
                    """
                    uplink_switches: list[str] | None = None
                    uplink_interface_speed: str | None = None
                    """
                    Set point-to-Point interface speed and will apply to uplink interfaces on both ends.
                    (Uplink switch interface speed can
                    be overridden with `uplink_switch_interface_speed`).
                    Speed should be set in the format `<interface_speed>` or `forced
                    <interface_speed>` or `auto <interface_speed>`.
                    """
                    uplink_switch_interface_speed: str | None = None
                    """
                    Set point-to-Point interface speed for the uplink switch interface only.
                    Speed should be set in the format
                    `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`.
                    """
                    max_uplink_switches: Annotated[int, IntConvert(convert_types=(str))] | None = None
                    """
                    Maximum number of uplink switches.
                    Changing this value may change IP Addressing on uplinks.
                    Can be used to reserve IP
                    space for future expansions.
                    """
                    max_parallel_uplinks: Annotated[int, IntConvert(convert_types=(str))] | None = None
                    """
                    Number of parallel links towards uplink switches.
                    Changing this value may change interface naming on uplinks (and
                    corresponding downlinks).
                    Can be used to reserve interfaces for future parallel uplinks.
                    """
                    uplink_bfd: bool | None = False
                    """
                    Enable bfd on uplink interfaces.
                    """
                    uplink_native_vlan: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=4094)
                    """
                    Only applicable to switches with layer-2 port-channel uplinks.
                    A suspended (disabled) vlan will be created in both ends
                    of the link unless the vlan is defined under network services.
                    By default the uplink will not have a native_vlan
                    configured, so EOS defaults to vlan 1.
                    """
                    uplink_ptp: UplinkPtp | None = None
                    """
                    Enable PTP on all infrastructure links.
                    """
                    uplink_macsec: UplinkMacsec | None = None
                    """
                    Enable MacSec on all uplinks.
                    """
                    uplink_port_channel_id: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=999999)
                    """
                    Only applicable for L2 switches with `uplink_type: port-channel`.
                    By default the uplink Port-channel ID will be set to
                    the number of the lowest member interface defined under `uplink_interfaces`.
                    For example:
                      member ports [ Eth22, Eth23
                    ] -> ID 22
                      member ports [ Eth11/1, Eth22/1 ] -> ID 111
                    For MLAG port-channels ID will be based on the lowest member
                    interface on the first MLAG switch.
                    This option overrides the default behavior and statically sets the local Port-
                    channel ID.
                    Note! Make sure the ID is unique and does not overlap with autogenerated Port-channel IDs in the Network
                    Services.
                    Note! For MLAG pairs the ID must be between 1 and 2000 and both MLAG switches must have the same value.
                    """
                    uplink_switch_port_channel_id: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=999999)
                    """
                    Only applicable for L2 switches with `uplink_type: port-channel`.
                    By default the uplink switch Port-channel ID will be
                    set to the number of the first interface defined under `uplink_switch_interfaces`.
                    For example:
                      member ports [ Eth22,
                    Eth23 ] -> ID 22
                      member ports [ Eth11/1, Eth22/1 ] -> ID 111
                    For MLAG port-channels ID will be based on the lowest
                    member interface on the first MLAG switch.
                    This option overrides the default behavior and statically sets the Port-
                    channel ID on the uplink switch.
                    Note! Make sure the ID is unique and does not overlap with autogenerated Port-channel
                    IDs in the Network Services.
                    Note! For MLAG pairs the ID must be between 1 and 2000 and both MLAG switches must have the
                    same value.
                    """
                    uplink_structured_config: dict | None = None
                    """
                    Custom structured config applied to "uplink_interfaces", and "uplink_switch_interfaces".
                    When uplink_type == "p2p",
                    custom structured config added under ethernet_interfaces.[name=<interface>] for eos_cli_config_gen overrides the
                    settings on the ethernet interface level.
                    When uplink_type == "port-channel", custom structured config added under
                    port_channel_interfaces.[name=<interface>] for eos_cli_config_gen overrides the settings on the port-channel interface
                    level.
                    "uplink_structured_config" is applied after "structured_config", so it can override "structured_config" defined
                    on node-level.
                    Note! The content of this dictionary is _not_ validated by the schema, since it can be either
                    ethernet_interfaces or port_channel_interfaces.
                    """
                    mlag_port_channel_structured_config: MlagPortChannelStructuredConfig | None = None
                    """
                    Custom structured config applied to MLAG peer link port-channel id.
                    Added under
                    port_channel_interfaces.[name=<interface>] for eos_cli_config_gen.
                    Overrides the settings on the port-channel interface
                    level.
                    "mlag_port_channel_structured_config" is applied after "structured_config", so it can override
                    "structured_config" defined on node-level.
                    """
                    mlag_peer_vlan_structured_config: MlagPeerVlanStructuredConfig | None = None
                    """
                    Custom structured config applied to MLAG Peer Link (control link) SVI interface id.
                    Added under
                    vlan_interfaces.[name=<interface>] for eos_cli_config_gen.
                    Overrides the settings on the vlan interface level.
                    "mlag_peer_vlan_structured_config" is applied after "structured_config", so it can override "structured_config" defined
                    on node-level.
                    """
                    mlag_peer_l3_vlan_structured_config: MlagPeerL3VlanStructuredConfig | None = None
                    """
                    Custom structured config applied to MLAG underlay L3 peering SVI interface id.
                    Added under
                    vlan_interfaces.[name=<interface>] for eos_cli_config_gen.
                    Overrides the settings on the vlan interface level.
                    "mlag_peer_l3_vlan_structured_config" is applied after "structured_config", so it can override "structured_config"
                    defined on node-level.
                    """
                    short_esi: str | None = None
                    """
                    short_esi only valid for l2leaf devices using port-channel uplink.
                    Setting short_esi to "auto" generates the short_esi
                    automatically using a hash of configuration elements.
                    < 0000:0000:0000 | auto >.
                    """
                    isis_system_id_prefix: str | None = Field(None, pattern=r"[0-9a-f]{4}\.[0-9a-f]{4}")
                    """
                    (4.4 hexadecimal).
                    """
                    isis_maximum_paths: Annotated[int, IntConvert(convert_types=(str))] | None = None
                    """
                    Number of path to configure in ECMP for ISIS.
                    """
                    is_type: Literal["level-1-2", "level-1", "level-2"] | None = "level-2"
                    node_sid_base: Annotated[int, IntConvert(convert_types=(str))] | None = 0
                    """
                    Node-SID base for isis-sr underlay variants. Combined with node id to generate ISIS-SR node-SID.
                    """
                    loopback_ipv4_pool: str | None = None
                    """
                    IPv4 subnet for Loopback0 allocation.
                    """
                    vtep_loopback_ipv4_pool: str | None = None
                    """
                    IPv4 subnet for VTEP-Loopback allocation.
                    """
                    loopback_ipv4_offset: Annotated[int, IntConvert(convert_types=(str))] | None = 0
                    """
                    Offset all assigned loopback IP addresses.
                    Required when the < loopback_ipv4_pool > is same for 2 different node_types
                    (like spine and l3leaf) to avoid over-lapping IPs.
                    For example, set the minimum offset
                    l3leaf.defaults.loopback_ipv4_offset: < total # spine switches > or vice versa.
                    """
                    loopback_ipv6_pool: str | None = None
                    """
                    IPv6 subnet for Loopback0 allocation.
                    """
                    loopback_ipv6_offset: Annotated[int, IntConvert(convert_types=(str))] | None = 0
                    """
                    Offset all assigned loopback IPv6 addresses.
                    Required when the < loopback_ipv6_pool > is same for 2 different node_types
                    (like spine and l3leaf) to avoid overlapping IPs.
                    For example, set the minimum offset
                    l3leaf.defaults.loopback_ipv6_offset: < total # spine switches > or vice versa.
                    """
                    vtep: bool | None = None
                    """
                    Node is configured as a VTEP when applicable based on 'overlay_routing_protocol'.
                    Overrides VTEP setting inherited from
                    node_type_keys.
                    """
                    vtep_loopback: str | None = Field(None, pattern=r"Loopback[\d/]+")
                    """
                    Set VXLAN source interface.
                    """
                    bgp_as: Annotated[str, StrConvert(convert_types=(int, float))] | None = None
                    """
                    BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
                    For asdot notation in YAML inputs, the value
                    must be put in quotes, to prevent it from being interpreted as a float number.
                    Required with eBGP.
                    """
                    bgp_defaults: list[str] | None = None
                    """
                    List of EOS commands to apply to BGP daemon.
                    """
                    evpn_role: Literal["client", "server", "none"] | None = None
                    """
                    Acting role in EVPN control plane.
                    Default is set in node_type definition from node_type_keys.
                    """
                    evpn_route_servers: list[str] | None = None
                    """
                    List of nodes acting as EVPN Route-Servers / Route-Reflectors.
                    """
                    evpn_services_l2_only: bool | None = False
                    """
                    Possibility to prevent configuration of Tenant VRFs and SVIs.
                    Override node definition "network_services_l3" from
                    node_type_keys.
                    This allows support for centralized routing.
                    """
                    filter: Filter | None = None
                    """
                    Filter L3 and L2 network services based on tenant and tags (and operation filter).
                    If filter is not defined it will
                    default to all.
                    """
                    igmp_snooping_enabled: bool | None = True
                    """
                    Activate or deactivate IGMP snooping on device level.
                    """
                    evpn_gateway: EvpnGateway | None = None
                    """
                    Node is acting as EVPN Multi-Domain Gateway.
                    New BGP peer-group is generated between EVPN GWs in different domains or
                    between GWs and Route Servers.
                    Name can be changed under "bgp_peer_groups.evpn_overlay_core" variable.
                    L3 rechability
                    for different EVPN GWs must be already in place, it is recommended to use DCI & L3 Edge if Route Servers and GWs are not
                    defined under the same Ansible inventory.
                    """
                    ipvpn_gateway: IpvpnGateway | None = None
                    """
                    Node is acting as IP-VPN Gateway for EVPN to MPLS-IP-VPN Interworking. The BGP peer group used for this is
                    "bgp_peer_groups.ipvpn_gateway_peers".
                    L3 Reachability is required for this to work, the preferred method to establish
                    underlay connectivity is to use core_interfaces.
                    """
                    mlag: bool | None = True
                    """
                    Enable / Disable auto MLAG, when two nodes are defined in node group.
                    """
                    mlag_dual_primary_detection: bool | None = False
                    """
                    Enable / Disable MLAG dual primary detection.
                    """
                    mlag_ibgp_origin_incomplete: bool | None = True
                    """
                    Set origin of routes received from MLAG iBGP peer to incomplete.
                    The purpose is to optimize routing for leaf loopbacks
                    from spine perspective and
                    avoid suboptimal routing via peerlink for control plane traffic.
                    """
                    mlag_interfaces: list[str] | None = None
                    """
                    Each list item supports range syntax that can be expanded into a list of interfaces.
                    Required when MLAG leafs are
                    present in the topology.
                    """
                    mlag_interfaces_speed: str | None = None
                    """
                    Set MLAG interface speed.
                    Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto
                    <interface_speed>`.
                    """
                    mlag_peer_l3_vlan: Annotated[int, IntConvert(convert_types=(str, bool))] | None = Field(4093, ge=0, le=4094)
                    """
                    Underlay L3 peering SVI interface id.
                    If set to 0 or the same vlan as mlag_peer_vlan, the mlag_peer_vlan will be used
                    for L3 peering.
                    """
                    mlag_peer_l3_ipv4_pool: str | None = None
                    """
                    IP address pool used for MLAG underlay L3 peering. IP is derived from the node id.
                    Required when MLAG leafs present in
                    topology and they are using a separate L3 peering VLAN.
                    """
                    mlag_peer_vlan: Annotated[int, IntConvert(convert_types=(str))] | None = Field(4094, ge=1, le=4094)
                    """
                    MLAG Peer Link (control link) SVI interface id.
                    """
                    mlag_peer_link_allowed_vlans: str | None = None
                    mlag_peer_ipv4_pool: str | None = None
                    """
                    IP address pool used for MLAG Peer Link (control link). IP is derived from the node id.
                    Required when MLAG leafs present
                    in topology.
                    """
                    mlag_port_channel_id: Annotated[int, IntConvert(convert_types=(str))] | None = None
                    """
                    If not set, the mlag port-channel id is generated based on the digits of the first interface present in
                    'mlag_interfaces'.
                    Valid port-channel id numbers are < 1-2000 > for EOS < 4.25.0F and < 1 - 999999 > for EOS >= 4.25.0F.
                    """
                    mlag_domain_id: str | None = None
                    """
                    MLAG Domain ID. If not set the node group name (Set with "group" key) will be used.
                    """
                    spanning_tree_mode: Literal["mstp", "rstp", "rapid-pvst", "none"] | None = None
                    spanning_tree_priority: Annotated[int, IntConvert(convert_types=(str))] | None = 32768
                    """
                    Spanning-tree priority configured for the selected mode.
                    For `rapid-pvst` the priority can also be set per VLAN under
                    network services.
                    """
                    spanning_tree_root_super: bool | None = False
                    virtual_router_mac_address: str | None = None
                    """
                    Virtual router mac address for anycast gateway.
                    """
                    inband_mgmt_interface: str | None = None
                    """
                    Pointer to interface used for inband management.
                    All configuration must be done using other data models like network
                    services or structured_config.
                    'inband_mgmt_interface' is only used to refer to this interface as source in various
                    management protocol settings (future feature).

                    On L2 switches, this defaults to Vlan<inband_mgmt_vlan> if either
                    'inband_mgmt_subnet' or 'inband_mgmt_ip' is set.
                    """
                    inband_mgmt_vlan: Annotated[int, IntConvert(convert_types=(str))] | None = 4092
                    """
                    VLAN number used for inband management on L2 switches (switches using port-channel trunks as uplinks).
                    When using
                    'inband_mgmt_subnet' the VLAN and SVIs will be created automatically on this switch as well as all 'uplink_switches'.
                    When using 'inband_mgmt_ip' the VLAN and SVI will only be created on this device and added to uplink trunk. The VLAN and
                    SVI on the parent switches must be created using network services data models.
                    """
                    inband_mgmt_subnet: str | None = None
                    """
                    Optional IP subnet assigned to inband management SVIs on L2 switches (switches using port-channels as uplinks).
                    Parent
                    l3leafs will have SVI with "ip virtual-router" and host-route injection based on ARP.
                    This allows all l3leafs to reuse
                    the same subnet across multiple racks without VXLAN extension.
                    SVI IP address will be assigned as follows:
                    virtual-
                    router: <subnet> + 1
                    l3leaf A      : <subnet> + 2 (same IP on all l3leaf A)
                    l3leaf B      : <subnet> + 3 (same IP on all
                    l3leaf B)
                    l2leafs       : <subnet> + 3 + <l2leaf id>
                    GW on l2leafs : <subnet> + 1
                    Assign range larger than total l2leafs
                    + 5

                    Setting is ignored if 'inband_mgmt_ip' is set.

                    This setting is applicable to L2 switches (switches using port-
                    channel trunks as uplinks).
                    """
                    inband_mgmt_ip: str | None = None
                    """
                    IP address assigned to the inband management interface set with 'inband_mgmt_vlan'.
                    This overrides 'inband_mgmt_subnet',
                    hence all behavior of 'inband_mgmt_subnet' is removed.

                    If this is set the VLAN and SVI will only be created on the L2
                    switch and added to uplink trunk.
                    The VLAN and SVI on the parent switches must be created using network services data
                    models.

                    This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).
                    """
                    inband_mgmt_gateway: str | None = None
                    """
                    Default gateway configured in the 'inband_mgmt_vrf' when using 'inband_mgmt_ip'. Otherwise gateway is derived from
                    'inband_mgmt_subnet' if set.

                    This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).
                    """
                    inband_mgmt_ipv6_address: str | None = None
                    """
                    IPv6 address assigned to the inband management interface set with 'inband_mgmt_vlan'.
                    This overrides
                    'inband_mgmt_ipv6_subnet', hence the configuration of 'inband_mgmt_ipv6_subnet' is ignored.

                    If this is set the VLAN and
                    SVI will only be created on the L2 switch and added to uplink trunk.
                    The VLAN and SVI on the parent switches must be
                    created using network services data models.

                    This setting is applicable to L2 switches (switches using port-channel
                    trunks as uplinks).
                    """
                    inband_mgmt_ipv6_subnet: str | None = None
                    """
                    Optional IPv6 prefix assigned to inband management SVIs on L2 switches (switches using port-channels as uplinks).
                    Parent
                    l3leafs will have SVI with "ipv6 virtual-router" and host-route injection based on ARP.
                    This allows all l3leafs to reuse
                    the same subnet across multiple racks without VXLAN extension.
                    SVI IP address will be assigned as follows:
                    virtual-
                    router: <subnet> + 1
                    l3leaf A      : <subnet> + 2 (same IP on all l3leaf A)
                    l3leaf B      : <subnet> + 3 (same IP on all
                    l3leaf B)
                    l2leafs       : <subnet> + 3 + <l2leaf id>
                    GW on l2leafs : <subnet> + 1
                    Assign range larger than total l2leafs
                    + 5

                    Setting is ignored if 'inband_mgmt_ipv6_address' is set.

                    This setting is applicable to L2 switches (switches using
                    port-channel trunks as uplinks).
                    """
                    inband_mgmt_ipv6_gateway: str | None = None
                    """
                    Default gateway configured in the 'inband_mgmt_vrf'.
                    Used when `inband_mgmt_ipv6_address` is set.
                    Ignored when
                    'inband_mgmt_ipv6_subnet' is set (first IP in subnet used as gateway).

                    This setting is applicable to L2 switches
                    (switches using port-channel trunks as uplinks).
                    """
                    inband_mgmt_description: str | None = "Inband Management"
                    """
                    Description configured on the Inband Management SVI.

                    This setting is only applied on the devices where it is set, it
                    does not automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-
                    group/node-type as needed.
                    """
                    inband_mgmt_vlan_name: str | None = "Inband Management"
                    """
                    Name configured on the Inband Management VLAN.
                    This setting is only applied on the devices where it is set, it does not
                    automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-group/node-
                    type as needed.
                    """
                    inband_mgmt_vrf: Annotated[str, StrConvert(convert_types=(int))] | None = "default"
                    """
                    VRF configured on the Inband Management Interface.
                    The VRF is created if not already created by other means.
                    This
                    setting is only applied on the devices where it is set, it does not automatically affect any parent/child devices
                    configuration, so it must be set on each applicable node/node-group/node-type as needed.
                    """
                    inband_mgmt_mtu: int | None = 1500
                    """
                    MTU configured on the Inband Management Interface.
                    This setting is only applied on the devices where it is set, it does
                    not automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-
                    group/node-type as needed.
                    """
                    inband_ztp: bool | None = False
                    """
                    Enable to configure upstream device with proper configuration to allow downstream devices to ZTP inband.
                    This setting
                    also requires that the `inband_mgmt_vlan` is set for the node.
                    """
                    inband_ztp_lacp_fallback_delay: int | None = Field(30, ge=0, le=300)
                    """
                    Set the LACP fallback timeout of the upstream device's port-channel towards the downstream inband ZTP node.
                    This setting
                    also requires that `inband_ztp` is set for the node.
                    """
                    inband_management_subnet: str | None = None
                    """
                    Optional IP subnet assigned to inband management SVIs on L2 switches (switches using port-channels as uplinks).
                    Parent
                    l3leafs will have SVI with "ip virtual-router" and host-route injection based on ARP.
                    This allows all l3leafs to reuse
                    the same subnet across multiple racks without VXLAN extension.
                    SVI IP address will be assigned as follows:
                    virtual-
                    router: <subnet> + 1
                    l3leaf A      : <subnet> + 2 (same IP on all l3leaf A)
                    l3leaf B      : <subnet> + 3 (same IP on all
                    l3leaf B)
                    l2leafs       : <subnet> + 3 + <l2leaf id>
                    GW on l2leafs : <subnet> + 1
                    Assign range larger than total l2leafs
                    + 5

                    Setting is ignored if 'inband_mgmt_ip' is set.

                    This setting is applicable to L2 switches (switches using port-
                    channel trunks as uplinks).
                    """
                    inband_management_vlan: Annotated[int, IntConvert(convert_types=(str))] | None = 4092
                    """
                    VLAN number used for inband management on L2 switches (switches using port-channel trunks as uplinks).
                    When using
                    'inband_mgmt_subnet' the VLAN and SVIs will be created automatically on this switch as well as all 'uplink_switches'.
                    When using 'inband_mgmt_ip' the VLAN and SVI will only be created on this device and added to uplink trunk. The VLAN and
                    SVI on the parent switches must be created using network services data models.
                    """
                    mpls_overlay_role: Literal["client", "server", "none"] | None = None
                    """
                    Set the default mpls overlay role.
                    Acting role in overlay control plane.
                    """
                    overlay_address_families: list[str] | None = None
                    """
                    Set the default overlay address families.
                    """
                    mpls_route_reflectors: list[str] | None = None
                    """
                    List of inventory hostname acting as MPLS route-reflectors.
                    """
                    bgp_cluster_id: Annotated[str, StrConvert(convert_types=(int))] | None = None
                    """
                    Set BGP cluster id.
                    """
                    ptp: Ptp | None = None
                    wan_role: Literal["client", "server"] | None = None
                    """
                    Override the default WAN role.

                    This is used both for AutoVPN and Pathfinder designs.
                    That means if `wan_mode` root key
                    is set to `autovpn` or `cv-pathfinder`.
                    `server` indicates that the router is a route-reflector.

                    Only supported if
                    `overlay_routing_protocol` is set to `ibgp`.
                    """
                    cv_pathfinder_transit_mode: Literal["region", "zone"] | None = None
                    """
                    Configure the transit mode for a WAN client for CV Pathfinder designs
                    only when the `wan_mode` root key is set to
                    `cv_pathfinder`.

                    'zone' is currently not supported.
                    """
                    cv_pathfinder_region: str | None = None
                    """
                    The CV Pathfinder region name.
                    This key is required for WAN routers but optional for pathfinders.
                    The region name must
                    be defined under 'cv_pathfinder_regions'.
                    """
                    cv_pathfinder_site: str | None = None
                    """
                    The CV Pathfinder site name.
                    This key is required for WAN routers but ignored for pathfinders.
                    The site name must be
                    defined for the relevant region under 'cv_pathfinder_regions'.
                    """
                    wan_ha: WanHa | None = None
                    """
                    PREVIEW: This key is currently not supported

                    The key is supported only if `wan_mode` == `cv-pathfinder`.
                    AutoVPN
                    support is still to be determined.

                    Maximum 2 devices supported by group for HA.
                    """
                    dps_mss_ipv4: Annotated[str, StrConvert(convert_types=(int))] | None = "auto"
                    """
                    IPv4 MSS value configured under "router path-selection" on WAN Devices.
                    """
                    l3_interfaces: list[L3InterfacesItem] | None = None
                    """
                    L3 Interfaces to configure on the node.
                    Used to define the node for WAN interfaces when `wan_carrier` is set.
                    """
                    data_plane_cpu_allocation_max: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=128)
                    """
                    Set the maximum number of CPU used for the data plane.
                    This setting is useful on virtual Route Reflectors and
                    Pathfinders where more CPU cores should be allocated for control plane.
                    """

                defaults: Defaults | None = None
                """
                Define variables for all nodes of this type.
                """
                node_groups: list[NodeGroupsItem] | None = None
                """
                Define variables related to all nodes part of this group.
                """
                nodes: list[NodesItem] | None = None
                """
                Define variables per node.
                """

            key: str
            """
            Key used as dynamic key
            """
            value: NodeTypeKeysKey | None = None
            """
            Value of dynamic key
            """

        connected_endpoints_keys: list[DynamicConnectedEndpointsKeys] | None = None
        """
        List of dynamic 'connected_endpoints_keys'.
        """
        network_services_keys: list[DynamicNetworkServicesKeys] | None = None
        """
        List of dynamic 'network_services_keys'.
        """
        node_type_keys: list[DynamicNodeTypeKeys] | None = None
        """
        List of dynamic 'node_type_keys'.
        """
        _dynamic_key_maps: list[dict] = [
            {"dynamic_keys_path": "connected_endpoints_keys.key", "model_key": "connected_endpoints_keys"},
            {"dynamic_keys_path": "network_services_keys.name", "model_key": "network_services_keys"},
            {"dynamic_keys_path": "node_type_keys.key", "model_key": "node_type_keys"},
        ]
        """
        Internal list of mappings from dynamic_keys_path to model_key.
        """

    application_classification: ApplicationClassification | None = None
    avd_data_conversion_mode: Literal["disabled", "error", "warning", "info", "debug", "quiet"] | None = "debug"
    """
    Conversion Mode for AVD input data conversion.
    Input data conversion will perform type conversion of input variables as
    defined in the schema.
    The type conversion is intended to help the user to identify minor issues with the input data,
    while still allowing the data to be validated.
    During conversion, messages will generated with information about the
    host(s) and key(s) which required conversion.
    "disabled" means that conversion will not run - avoid this since
    conversion is also handling data deprecation and upgrade.
    "error" will produce error messages and fail the task.
    "warning" will produce warning messages.
    "info" will produce regular log messages.
    "debug" will produce hidden debug
    messages viewable with -v.
    "quiet" will not produce any messages
    """
    avd_data_validation_mode: Literal["disabled", "error", "warning", "info", "debug"] | None = "warning"
    """
    Validation Mode for AVD input data validation.
    Input data validation will validate the input variables according to the
    schema.
    During validation, messages will generated with information about the host(s) and key(s) which failed
    validation.
    "disabled" means that validation will not run.
    "error" will produce error messages and fail the task.
    "warning" will produce warning messages.
    "info" will produce regular log messages.
    "debug" will produce hidden debug
    messages viewable with -v.
    """
    bfd_multihop: BfdMultihop | None = Field({"interval": 300, "min_rx": 300, "multiplier": 3}, validate_default=True)
    """
    BFD Multihop tuning.
    """
    bgp_as: Annotated[str, StrConvert(convert_types=(int))] | None = None
    """
    BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>" to use to configure overlay when
    "overlay_routing_protocol" == ibgp.
    For asdot notation in YAML inputs, the value must be put in quotes, to prevent it
    from being interpreted as a float number.
    """
    bgp_default_ipv4_unicast: bool | None = False
    """
    Default activation of IPv4 unicast address-family on all IPv4 neighbors.
    It is best practice to disable activation.
    """
    bgp_distance: BgpDistance | None = None
    bgp_ecmp: Annotated[int, IntConvert(convert_types=(str))] | None = None
    """
    Maximum ECMP for BGP multi-path.
    The default value is 4 except for WAN Routers where the default value is unset (falls
    back to EOS default).
    """
    bgp_graceful_restart: BgpGracefulRestart | None = None
    """
    BGP graceful-restart allows a BGP speaker with separate control plane and data plane processing to continue forwarding
    traffic during a BGP restart.
    Its neighbors (receiving speakers) may retain routing information from the restarting
    speaker while a BGP session with it is being re-established, reducing route flapping.
    """
    bgp_maximum_paths: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=512)
    """
    Maximum Paths for BGP multi-path.
    The default value is 4 except for WAN Routers where the default value is 16.
    """
    bgp_mesh_pes: bool | None = False
    """
    Configure an iBGP full mesh between PEs, either because there is no RR used or other reasons.
    Only supported in
    combination with MPLS overlay.
    """
    bgp_peer_groups: BgpPeerGroups | None = None
    """
    Leverage an Arista EOS switch to generate the encrypted password using the correct peer group name.
    Note that the name
    of the peer groups use '-' instead of '_' in EOS configuration.
    """
    bgp_update_wait_install: bool | None = None
    """
    Do not advertise reachability to a prefix until that prefix has been installed in hardware.
    This will eliminate any
    temporary black holes due to a BGP speaker advertising reachability to a prefix that may not yet be installed into the
    forwarding plane.
    """
    bgp_update_wait_for_convergence: bool | None = None
    """
    Disables FIB updates and route advertisement when the BGP instance is initiated until the BGP convergence state is
    reached.
    """
    connected_endpoints_keys: list[ConnectedEndpointsKeysItem] | None = Field(
        [
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
        ],
        validate_default=True,
    )
    """
    Endpoints connecting to the fabric can be grouped by using separate keys.
    The keys can be customized to provide a better
    better organization or grouping of your data.
    `connected_endpoints_keys` should be defined in the top level group_vars
    for the fabric.
    The default values will be overridden if defining this key, so it is recommended to copy the defaults
    and modify them.
    """
    core_interfaces: CoreInterfaces | None = None
    custom_structured_configuration_list_merge: Literal["replace", "append", "keep", "prepend", "append_rp", "prepend_rp"] | None = "append_rp"
    """
    The List-merge strategy used when merging custom structured configurations.

    This applies to all vars prefixed by
    prefixes in `custom_structured_configuration_prefix`
    and all data under the various `structured_config` options.

    The
    available list merge strategies:
    - `replace`:
      - Any list will be replaced with the list defined in custom structured
    configurations.
    - `append`:
      - Existing list items with the same "Primary key"-value will be updated.
      - New items
    will be appended to the existing list (including duplicates).
    - `keep`:
      - Only set list if there is no existing list
    or existing list is `None`.
    - `prepend`:
      - Existing list items with the same "Primary key"-value will be updated.
      -
    New items will be prepended to the existing list (including duplicates).
    - `append_rp`:
      - Existing list items with the
    same "Primary key"-value will be updated.
      - New unique items will be appended to the existing list.
    - `prepend_rp`:
    - Existing list items with the same "Primary key"-value will be updated.
      - New unique items will be prepended to the
    existing list.
    """
    custom_structured_configuration_prefix: list[str] | None = Field(["custom_structured_configuration_"], validate_default=True)
    """
    Custom EOS Structured Configuration keys can be set on any group or host_var level using the name
    of the corresponding
    `eos_cli_config_gen` key prefixed with content of `custom_structured_configuration_prefix`.

    The content of Custom
    Structured Configuration variables will be merged with the structured config generated by the eos_designs role.

    The
    merge is done recursively, so it is possible to update a sub-key of a variable set by `eos_designs` role already.

    The
    merge follow these recursive merge strategies:
    - New keys will be added for all types.
    - Existing keys of type "List"
    with a "Primary key" set in the schema:
      - Strategy can be changed with `custom_structured_configuration_list_merge`.
    Default strategy:
        - Existing list items with the same "Primary key"-value will be updated.
        - New unique items
    will be appended to the existing list
    - Other keys of type "List" will have new unique items appended the the existing
    list.
    - Existing keys of type "Dictionary" will recursively merge
    - Other existing keys will be replaced.
    """
    cv_pathfinder_regions: list[CvPathfinderRegionsItem] | None = None
    """
    Define the CV Pathfinder hierarchy.
    """
    cv_tags_topology_type: Literal["leaf", "spine", "core", "edge"] | None = None
    """
    PREVIEW: This key is currently not supported
    Device type that CloudVision should use when generating the Topology.
    Defaults to the setting under node_type_keys.
    """
    cv_topology: list[CvTopologyItem] | None = None
    """
    Generate AVD configurations directly from the given CloudVision topology.
    Activate this feature by setting
    `use_cv_topology` to `true`.
    Requires `default_interfaces` to be set for the relevant platforms and node types to detect
    the proper interface roles automatically.
    Neighbor hostnames must match the inventory hostnames of the AVD inventory to
    be taken into consideration.
    """
    cvp_ingestauth_key: str | None = None
    """
    On-premise CVP ingest auth key. If set, TerminAttr will be configured with key-based authentication for on-premise CVP.
    If not set, TerminAttr will be configured with certificate based authentication:
    - On-premise using token onboarding.
    Default token path is '/tmp/token'.
    - CVaaS using token-secure onboarding. Default token path is '/tmp/cv-onboarding-
    token'.
    Token must be copied to the device first.
    """
    cvp_instance_ip: str | None = None
    """
    IPv4 address or DNS name for CloudVision.
    This variable only supports an on-premise single-node cluster or the DNS name
    of a CloudVision as a Service instance.
    """
    cvp_instance_ips: list[str] | None = None
    """
    List of IPv4 addresses or DNS names for CloudVision.
    For on-premise CloudVision enter all the nodes of the cluster.
    For
    CloudVision as a Service enter the DNS name of the instance.
    `eos_designs` only supports one CloudVision cluster.
    """
    cvp_token_file: str | None = None
    """
    cvp_token_file is the path to the token file on the switch.
    If not set the default locations for on-premise or CVaaS
    will be used.
    See cvp_ingestauth_key for details.
    """
    dc_name: str | None = None
    """
    POD Name is used in:
    - Fabric Documentation (Optional, falls back to fabric_name)
    - SNMP Location:
    `snmp_settings.location` (Optional)
    - HER Overlay DC scoped flood lists: `overlay_her_flood_list_scope: dc` (Required)
    """
    default_igmp_snooping_enabled: bool | None = True
    """
    When set to false, disables IGMP snooping at fabric level and overrides per vlan settings.
    """
    default_interface_mtu: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=68, le=65535)
    """
    Default interface MTU configured on EOS under "interface defaults".
    Can be overriden per platform under platform
    settings.
    """
    default_interfaces: list[DefaultInterfacesItem] | None = None
    """
    Default uplink, downlink, and MLAG interfaces, which will be used if these interfaces are not defined on a device
    (either directly or through inheritance).
    """
    default_mgmt_method: Literal["oob", "inband", "none"] | None = "oob"
    """
    `default_mgmt_method` controls the default VRF and source interface used for the following management and monitoring
    protocols configured with `eos_designs`:
      - `cv_settings`
      - `dns_settings`
      - `ntp_settings`
      - `sflow_settings`
    `oob` means the protocols will be configured with the VRF set by `mgmt_interface_vrf` and `mgmt_interface` as the source
    interface.
    `inband` means the protocols will be configured with the VRF set by `inband_mgmt_vrf` and
    `inband_mgmt_interface` as the source interface.
    `none` means the VRF and or interface must be manually set for each
    protocol.
    This can be overridden under the settings for each protocol.
    """
    default_node_types: list[DefaultNodeTypesItem] | None = None
    """
    Uses hostname matches against a regular expression to determine the node type.
    """
    design: Design | None = None
    enable_trunk_groups: bool | None = False
    """
    Enable Trunk Group support across eos_designs.
    Warning: Because of the nature of the EOS Trunk Group feature, enabling
    this is "all or nothing".
    *All* vlans and *all* trunks towards connected endpoints must be using trunk groups as well.
    If trunk groups are not assigned to a trunk, no vlans will be enabled on that trunk.
    See "Details on
    enable_trunk_groups" below before enabling this feature.
    """
    eos_designs_custom_templates: list[EosDesignsCustomTemplatesItem] | None = None
    eos_designs_documentation: EosDesignsDocumentation | None = None
    """
    Control fabric documentation generation.
    """
    event_handlers: list[EventHandlersItem] | None = None
    """
    Gives the ability to monitor and react to Syslog messages.
    Event Handlers provide a powerful and flexible tool that can
    be used to apply self-healing actions,
    customize the system behavior, and implement workarounds to problems discovered
    in the field.
    """
    evpn_ebgp_gateway_inter_domain: bool | None = None
    evpn_ebgp_gateway_multihop: Annotated[int, IntConvert(convert_types=(str))] | None = 15
    """
    Default of 15, considering a large value to avoid BGP reachability issues in very complex DCI networks.
    Adapt the value
    for your specific topology.
    """
    evpn_ebgp_multihop: Annotated[int, IntConvert(convert_types=(str))] | None = 3
    """
    Default of 3, the recommended value for a 3 stage spine and leaf topology.
    Set to a higher value to allow for very large
    and complex topologies.
    """
    evpn_hostflap_detection: EvpnHostflapDetection | None = None
    evpn_import_pruning: bool | None = False
    """
    Enable VPN import pruning (Min. EOS 4.24.2F).
    The Route Target extended communities carried by incoming VPN paths will
    be examined.
    If none of those Route Targets have been configured for import, the path will be immediately discarded.
    """
    evpn_multicast: bool | None = False
    """
    General Configuration required for EVPN Multicast. "evpn_l2_multicast" or "evpn_l3_multicast" must also be configured
    under the Network Services (tenants).
    Requires "underlay_multicast: true" and IGMP snooping enabled globally (default).
    For MLAG devices Route Distinguisher must be unique since this feature will create multi-vtep configuration.
    Warning !!!
    For Trident3 based platforms i.e 7050X3, 7300X3, 720XP and 722XP
      The Following default platform setting will be
    configured: "platform trident forwarding-table partition flexible exact-match 16384 l2-shared 98304 l3-shared 131072"
    All forwarding agents will be restarted when this configuration is applied.
      You can tune the settings by overriding
    the default variable: "platform_settings[platforms].trident_forwarding_table_partition:"
      Please contact an Arista
    representative for help with determining the appropriate values for your environment.
    """
    evpn_overlay_bgp_rtc: bool | None = False
    """
    Enable Route Target Membership Constraint Address Family on EVPN overlay BGP peerings (Min. EOS 4.25.1F).
    Requires use
    eBGP as overlay protocol.
    """
    evpn_prevent_readvertise_to_server: bool | None = False
    """
    Configure route-map on eBGP sessions towards route-servers, where prefixes with the peer's ASN in the AS Path are
    filtered away.
    This is very useful in large-scale networks, where convergence will be quicker by not returning all
    updates received
    from Route-server-1 to Router-server-2 just for Route-server-2 to throw them away because of AS Path
    loop detection.
    """
    evpn_short_esi_prefix: str | None = "0000:0000:"
    """
    Configure prefix for "short_esi" values.
    """
    evpn_vlan_aware_bundles: bool | None = False
    """
    Enable vlan aware bundles for EVPN MAC-VRF.
    """
    evpn_vlan_bundles: list[EvpnVlanBundlesItem] | None = None
    fabric_evpn_encapsulation: Literal["vxlan", "mpls"] | None = "vxlan"
    """
    Should be set to mpls for evpn-mpls scenario.
    """
    fabric_ip_addressing: FabricIpAddressing | None = None
    fabric_name: str = None
    """
    Fabric Name, required to match Ansible Group name covering all devices in the Fabric, **must** be an inventory group
    name.
    """
    fabric_sflow: FabricSflow | None = None
    """
    Default enabling of sFlow for various interface types across the fabric.
    sFlow can also be enabled/disabled under each
    of the specific data models.
    For general sFlow settings see `sflow_settings`.
    """
    flow_tracking_settings: FlowTrackingSettings | None = None
    """
    PREVIEW: This key is currently not supported

    Define the flow tracking parameters for this topology.
    """
    generate_cv_tags: GenerateCvTags | None = None
    """
    PREVIEW: This key is currently not supported
    Generate CloudVision Tags based on AVD data.
    """
    hardware_counters: HardwareCounters | None = None
    internal_vlan_order: InternalVlanOrder | None = Field({"allocation": "ascending", "range": {"beginning": 1006, "ending": 1199}}, validate_default=True)
    """
    Internal vlan allocation order and range.
    """
    ipv4_acls: list[Ipv4AclsItem] | None = None
    """
    IPv4 extended access-lists supporting substitution on certain fields.
    These access-lists can be referenced under node
    settings `l3_interfaces`, and will only be configured on devices where they are in use.

    The substitution is useful when
    assigning the same access-list on multiple interfaces,
    but where certain fields require unique values like the
    "interface_ip" or "peer_ip".
    When using substitution, the interface name will be appended to the ACL name.
    """
    ipv6_mgmt_destination_networks: list[str] | None = None
    """
    List of IPv6 prefixes to configure as static routes towards the OOB IPv6 Management interface gateway.
    Replaces the
    default route.
    """
    ipv6_mgmt_gateway: str | None = None
    """
    OOB Management interface gateway in IPv6 format.
    Used as next-hop for default gateway or static routes defined under
    'ipv6_mgmt_destination_networks'.
    """
    is_deployed: bool | None = True
    """
    If the device is already deployed in the fabric.
    When set to false, interfaces toward this device may be shutdown
    depending on the `shutdown_interfaces_towards_undeployed_peers` setting.
    Furthermore `eos_config_deploy_cvp` will not
    attempt to move or apply configurations to the device.
    """
    isis_advertise_passive_only: bool | None = False
    isis_area_id: Annotated[str, StrConvert(convert_types=(int, float))] | None = "49.0001"
    isis_default_circuit_type: Literal["level-1-2", "level-1", "level-2"] | None = "level-2"
    """
    These fabric level parameters can be used with core_interfaces running ISIS, and may be overridden on link profile or
    link level.
    """
    isis_default_is_type: Literal["level-1-2", "level-1", "level-2"] | None = Field("level-2", title="ISIS Default IS Type")
    isis_default_metric: Annotated[int, IntConvert(convert_types=(str))] | None = 50
    """
    These fabric level parameters can be used with core_interfaces running ISIS, and may be overridden at link profile or
    link level.
    """
    isis_maximum_paths: Annotated[int, IntConvert(convert_types=(str))] | None = None
    """
    Number of path to configure in ECMP for ISIS.
    """
    isis_ti_lfa: IsisTiLfa | None = None
    l3_edge: L3Edge | None = None
    l3_interface_profiles: list[L3InterfaceProfilesItem] | None = None
    """
    Profiles to inherit common settings for l3_interfaces defined under the node type key.
    These profiles will *not* work
    for `l3_interfaces` defined under `vrfs`.
    """
    local_users: list[LocalUsersItem] | None = None
    mac_address_table: MacAddressTable | None = None
    """
    MAC address-table aging time.
    Use to change the EOS default of 300.
    """
    management_eapi: ManagementEapi | None = None
    """
    Default is HTTPS management eAPI enabled.
    The VRF is set to < mgmt_interface_vrf >.
    """
    mgmt_destination_networks: list[str] | None = None
    """
    List of IPv4 prefixes to configure as static routes towards the OOB Management interface gateway.
    Replaces the default
    route.
    """
    mgmt_gateway: str | None = None
    """
    OOB Management interface gateway in IPv4 format.
    Used as next-hop for default gateway or static routes defined under
    'mgmt_destination_networks'.
    """
    mgmt_interface: str | None = "Management1"
    """
    OOB Management interface.
    """
    mgmt_interface_description: str | None = "oob_management"
    """
    Management interface description.
    """
    mgmt_interface_vrf: Annotated[str, StrConvert(convert_types=(int))] | None = "MGMT"
    """
    OOB Management VRF.
    """
    mgmt_vrf_routing: bool | None = False
    """
    Configure IP routing for the OOB Management VRF.
    """
    mlag_ibgp_peering_vrfs: MlagIbgpPeeringVrfs | None = None
    """
    On mlag leafs, an SVI interface is defined per vrf, to establish iBGP peering (required when there are MLAG leafs in
    topology).
    The SVI id will be derived from the base vlan defined: mlag_ibgp_peering_vrfs.base_vlan + (vrf_id or vrf_vni)
    - 1.
    Depending on the values of vrf_id / vrf_vni it may be required to adjust the base_vlan to avoid overlaps or invalid
    vlan ids.
    The SVI ip address derived from mlag_l3_peer_ipv4_pool is re-used across all iBGP peerings.
    """
    mlag_on_orphan_port_channel_downlink: bool | None = True
    """
    If `true` (default) an MLAG ID will always be configured on a Port-Channel downlink even if the downlink is only on one
    node in the MLAG pair.
    If `false` an MLAG ID will only be configured on Port-Channel downlinks dual-homed to two MLAG
    switches.
    Note the default value will change to `false` in AVD version 5.0
    """
    name_servers: list[str] | None = None
    """
    List of DNS servers. The VRF is set to < mgmt_interface_vrf >.
    """
    network_ports: list[NetworkPortsItem] | None = None
    network_services_keys: list[NetworkServicesKeysItem] | None = Field([{"name": "tenants"}], validate_default=True)
    """
    Network Services can be grouped by using separate keys.
    The keys can be customized to provide a better better
    organization or grouping of your data.
    `network_services_keys` should be defined in the top level group_vars for the
    fabric.
    The default values will be overridden if defining this key, so it is recommended to copy the defaults and modify
    them.
    """
    new_network_services_bgp_vrf_config: bool | None = None
    """
    Set this key to `true` in the node type to generate full BGP configuration
    for network services even when `evpn` is not
    in the address families
    (`evpn` is the default address family for `l3ls-evpn` but not for `l2ls`).

    This is `false` by
    default except if `uplink_type` is set to `p2p-vrfs`, then the default value is `true`.

    This may introduce breaking
    changes to your configuration.
    """
    node_type_keys: list[NodeTypeKeysItem] | None = None
    """
    Define Node Type Keys, to specify the properties of each node type in the fabric.
    This allows for complete customization
    of the fabric layout and functionality.
    `node_type_keys` should be defined in top level group_var for the fabric.
    The
    default values will be overridden if defining this key, so it is recommended to copy the defaults and modify them.
    """
    ntp_settings: NtpSettings | None = None
    """
    NTP settings
    """
    only_local_vlan_trunk_groups: bool | None = False
    """
    A vlan can have many trunk_groups assigned.
    To avoid unneeded configuration changes on all leaf switches when a new
    trunk group is added,
    this feature will only configure the vlan trunk groups matched with local connected_endpoints.
    See
    "Details on only_local_vlan_trunk_groups" below.
    Requires "enable_trunk_groups: true".
    """
    overlay_cvx_servers: list[str] | None = None
    """
    List of CVX vxlan overlay controllers.
    Required if overlay_routing_protocol == CVX.
    CVX servers (VMs) are peering using
    their management interface, so mgmt_ip must be set for all CVX servers.
    """
    overlay_her_flood_list_per_vni: bool | None = False
    """
    When using Head-End Replication, configure flood-lists per VNI.
    By default HER will be configured with a common flood-
    list containing all VTEPs.
    This behavior can be changed to per-VNI flood-lists by setting
    `overlay_her_flood_list_per_vni: true`.
    This will make `eos_designs` consider configured VLANs per VTEP, and only
    include the relevant VTEPs to each VNI's flood-list.
    """
    overlay_her_flood_list_scope: Literal["fabric", "dc"] | None = "fabric"
    """
    When using Head-End Replication, set the scope of flood-lists to Fabric or DC.
    By default all VTEPs in the Fabric (part
    of the inventory group referenced by "fabric_name") are added to the flood-lists.
    This can be changed to all VTEPs in
    the DC (sharing the same "dc_name" value).
    This is useful if Border Leaf switches are dividing the VXLAN overlay into
    separate domains.
    """
    overlay_loopback_description: str | None = None
    """
    Customize the description on overlay interface Loopback0.
    """
    overlay_mlag_rfc5549: bool | None = False
    """
    IPv6 Unnumbered for MLAG iBGP connections.
    Requires "underlay_rfc5549: true".
    """
    overlay_rd_type: OverlayRdType | None = None
    """
    Configuration options for the Administrator subfield (first part of RD) and the Assigned Number subfield (second part of
    RD).

    By default Route Distinguishers (RD) are set to:
    - `<overlay_loopback>:<mac_vrf_id_base + vlan_id or
    mac_vrf_vni_base + vlan_id>` for VLANs and VLAN-Aware Bundles with L2 vlans.
    -
    `<overlay_loopback>:<vlan_aware_bundle_number_base + vrf_id>` for VLAN-Aware Bundles with SVIs.
    -
    `<overlay_loopback>:<vlan_aware_bundle_number_base + id>` for VLAN-Aware Bundles defined under 'evpn_vlan_bundles'.
    -
    `<overlay_loopback>:<vrf_id>` for VRFs.

    Note:
    RD is a 48-bit value which is split into <16-bit>:<32-bit> or
    <32-bit>:<16-bit>.
    When using loopback or 32-bit ASN/number the assigned number can only be a 16-bit number. This may be
    a problem with large VNIs.
    For 16-bit ASN/number the assigned number can be a 32-bit number.
    """
    overlay_routing_protocol: Annotated[Literal["ebgp", "ibgp", "cvx", "her", "none"], StrConvert(to_lower=True)] | None = "ebgp"
    """
    - The following overlay routing protocols are supported:
      - eBGP: Configures fabric with eBGP, default for l3ls-evpn
    design.
      - iBGP: Configured fabric with iBGP, only supported with OSPF or ISIS variants in underlay, default for mpls
    design.
      - CVX: Configures fabric to leverage CloudVision eXchange as the overlay controller.
      - HER: Configures
    fabric with Head-End Replication, configures static VXLAN flood-lists instead of using a dynamic overlay protocol.
      -
    none: No overlay configuration will be generated, default for l2ls design.
    """
    overlay_routing_protocol_address_family: Literal["ipv4", "ipv6"] | None = "ipv4"
    """
    When set to `ipv6`, enable overlay EVPN peering with IPv6 addresses.
    This feature depends on underlay_ipv6 variable. As
    of today, only RFC5549 is capable to transport IPv6 in the underlay.
    """
    overlay_rt_type: OverlayRtType | None = None
    """
    Configuration options for the Administrator subfield (first part of RT) and the Assigned Number subfield (second part of
    RT).

    By default Route Targets (RT) are set to:
    - `<(mac_vrf_id_base or mac_vrf_vni_base) + vlan_id>:<(mac_vrf_id_base
    or mac_vrf_vni_base) + vlan_id>` for VLANs and VLAN-Aware Bundles with L2 vlans.
    - `<vlan_aware_bundle_number_base +
    vrf_id>:<vlan_aware_bundle_number_base + vrf_id>` for VLAN-Aware Bundles with SVIs.
    - `<vlan_aware_bundle_number_base +
    id>:<vlan_aware_bundle_number_base + id>` for VLAN-Aware Bundles defined under 'evpn_vlan_bundles'.
    -
    `<vrf_id>:<vrf_id>` for VRFs.

    Notes:
    RT is a 48-bit value which is split into <16-bit>:<32-bit> or <32-bit>:<16-bit>.
    When using 32-bit ASN/number the VNI can only be a 16-bit number. Alternatively use vlan_id/vrf_id as assigned number.
    For 16-bit ASN/number the assigned number can be a 32-bit number.
    """
    p2p_uplinks_mtu: Annotated[int, IntConvert(convert_types=(str))] | None = Field(9214, ge=68, le=65535)
    """
    Point to Point Links MTU.
    """
    p2p_uplinks_qos_profile: str | None = None
    """
    QOS Profile assigned on all infrastructure links.
    """
    platform_settings: list[PlatformSettingsItem] | None = Field(
        [
            {"platforms": ["default"], "feature_support": {"queue_monitor_length_notify": False}, "reload_delay": {"mlag": 300, "non_mlag": 330}},
            {
                "platforms": ["7050X3"],
                "feature_support": {"queue_monitor_length_notify": False},
                "reload_delay": {"mlag": 300, "non_mlag": 330},
                "trident_forwarding_table_partition": "flexible exact-match 16384 l2-shared 98304 l3-shared 131072",
            },
            {
                "platforms": ["720XP"],
                "feature_support": {"poe": True, "queue_monitor_length_notify": False},
                "reload_delay": {"mlag": 300, "non_mlag": 330},
                "trident_forwarding_table_partition": "flexible exact-match 16384 l2-shared 98304 l3-shared 131072",
            },
            {
                "platforms": ["750", "755", "758"],
                "management_interface": "Management0",
                "feature_support": {"poe": True, "queue_monitor_length_notify": False},
                "reload_delay": {"mlag": 300, "non_mlag": 330},
            },
            {
                "platforms": ["720DP", "722XP", "710P"],
                "feature_support": {"poe": True, "queue_monitor_length_notify": False},
                "reload_delay": {"mlag": 300, "non_mlag": 330},
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
            {
                "platforms": ["7358X4"],
                "management_interface": "Management1/1",
                "reload_delay": {"mlag": 300, "non_mlag": 330},
                "feature_support": {
                    "queue_monitor_length_notify": False,
                    "interface_storm_control": True,
                    "bgp_update_wait_for_convergence": True,
                    "bgp_update_wait_install": False,
                },
            },
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
        ],
        validate_default=True,
    )
    platform_speed_groups: list[PlatformSpeedGroupsItem] | None = None
    """
    Set Hardware Speed Groups per Platform.
    """
    pod_name: str | None = None
    """
    POD Name is used in:
    - Fabric Documentation (Optional, falls back to dc_name and then to fabric_name)
    - SNMP Location:
    `snmp_settings.location` (Optional)
    - VRF Loopbacks: `vtep_diagnostic.loopback_ip_pools.pod` (Required)

    Recommended to
    be common between Spines and Leafs within a POD (One l3ls topology).
    """
    port_profiles: list[PortProfilesItem] | None = None
    """
    Optional profiles to share common settings for connected_endpoints and/or network_ports.
    Keys are the same used under
    endpoints adapters. Keys defined under endpoints adapters take precedence.
    """
    ptp: Ptp | None = None
    ptp_profiles: list[PtpProfilesItem] | None = Field(
        [
            {"announce": {"interval": 0, "timeout": 3}, "delay_req": -3, "profile": "aes67-r16-2016", "sync_message": {"interval": -3}, "transport": "ipv4"},
            {"announce": {"interval": -2, "timeout": 3}, "delay_req": -4, "profile": "smpte2059-2", "sync_message": {"interval": -4}, "transport": "ipv4"},
            {"announce": {"interval": 2, "timeout": 3}, "delay_req": 0, "profile": "aes67", "sync_message": {"interval": 0}, "transport": "ipv4"},
        ],
        validate_default=True,
    )
    queue_monitor_length: QueueMonitorLength | None = None
    redundancy: Redundancy | None = None
    """
    Redundancy for chassis platforms with dual supervisors | Optional.
    """
    serial_number: Annotated[str, StrConvert(convert_types=(int))] | None = None
    """
    Serial Number of the device.
    Used for documentation purpose in the fabric documentation as can also be used by the
    'eos_config_deploy_cvp' role.
    "serial_number" can also be set directly under node type settings.
    If both are set, the
    value under node type settings takes precedence.
    """
    sflow_settings: SflowSettings | None = None
    """
    sFlow settings.
    The sFlow process will only be configured if any interface is enabled for sFlow.
    For default enabling of
    sFlow for various interface types across the fabric see `fabric_sflow`.
    """
    shutdown_interfaces_towards_undeployed_peers: bool | None = False
    """
    - It is possible to provision configurations for a complete topology but flag devices as undeployed using the host level
    variable `is_deployed: false`.

    ```yaml
    # Use at the host level
    is_deployed: < true or false or default -> true >
    ```

    -
    By default, this will have no impact within the `eos_designs` role. Configs will still be generated by the
    `eos_cli_config_gen` role and will still be pushed by the `eos_config_deploy_eapi` directly to devices if used.
    -
    However, if the `eos_config_deploy_cvp` role is used to push configurations, CloudVision will ignore the devices flagged
    as `is_deployed: false` and not attempt to configure them.
    - If the device is not present in the network due to
    CloudVision not configuring the device, `eos_validate_state` role will fail tests on peers of the undeployed device
    trying to verify that interfaces are up.
    - To overcome this and shutdown interfaces towards undeployed peers, the
    variable `shutdown_interfaces_towards_undeployed_peers` can be used, satisfying the `eos_validate_state` role interface
    tests.
    - Again, this is only an issue if `eos_config_deploy_cvp` is used and the devices are not present in the network.
    """
    snmp_settings: SnmpSettings | None = None
    """
    SNMP settings
    For SNMP local-interfaces see "source_interfaces.snmp"
    Configuration of remote SNMP engine IDs are
    currently only possible using `structured_config`.
    """
    source_interfaces: SourceInterfaces | None = None
    """
    Configure source-interfaces based on the management interfaces set for other `eos_designs` data models.
    By default, no
    source-interfaces will be configured. They can still be configured manually using `eos_cli_config_gen` and custom
    structured configuration.
    EOS supports a single source-interface per VRF, so an error will be raised in case of
    conflicts.
    Errors will also be raised if an interface is not found for a device.
    """
    svi_profiles: list[SviProfilesItem] | None = None
    """
    Profiles to share common settings for SVIs under `<network_services_key>.[].vrfs.svis`.
    Keys are the same used under
    SVIs. Keys defined under SVIs take precedence.
    Note: structured configuration is not merged recursively and will be
    taken directly from the most specific level in the following order:
    1. svi.nodes[inventory_hostname].structured_config
    2. svi_profile.nodes[inventory_hostname].structured_config
    3.
    svi_parent_profile.nodes[inventory_hostname].structured_config
    4. svi.structured_config
    5. svi_profile.structured_config
    6. svi_parent_profile.structured_config
    """
    system_mac_address: str | None = None
    """
    Set to the same MAC address as available in "show version" on the device.
    "system_mac_address" can also be set under
    node type settings.
    If both are set, the value under node type settings takes precedence.
    """
    terminattr_disable_aaa: bool | None = False
    terminattr_ingestexclude: str | None = "/Sysdb/cell/1/agent,/Sysdb/cell/2/agent"
    terminattr_ingestgrpcurl_port: Annotated[int, IntConvert(convert_types=(str))] | None = 9910
    """
    Port number used for Terminattr connection to an on-premise CloudVision cluster.
    The port number is always 443 when
    using CloudVision as a Service, so this value is ignored.
    """
    terminattr_smashexcludes: str | None = "ale,flexCounter,hardware,kni,pulse,strata"
    timezone: str | None = None
    """
    Clock timezone like "CET" or "US/Pacific".
    """
    trunk_groups: TrunkGroups | None = None
    type: str | None = None
    """
    The `type:` variable needs to be defined for each device in the fabric.
    This is leveraged to load the appropriate
    template to generate the configuration.
    """
    underlay_filter_peer_as: bool | None = False
    """
    Configure route-map on eBGP sessions towards underlay peers, where prefixes with the peer's ASN in the AS Path are
    filtered away.
    This is very useful in very large scale networks not using EVPN overlays, where convergence will be
    quicker by not having to return
    all updates received from Spine-1 to Spine-2 just for Spine-2 to throw them away because
    of AS Path loop detection.
    Note that this setting cannot be used while there are EVPN services present in the default
    VRF.
    """
    underlay_filter_redistribute_connected: bool | None = True
    """
    Filter redistribution of connected into the underlay routing protocol.
    Only applicable when overlay_routing_protocol !=
    'none' and underlay_routing_protocol == BGP.
    Creates a route-map and prefix-list assigned to redistribute connected
    permitting only loopbacks and inband management subnets.
    """
    underlay_ipv6: bool | None = False
    """
    This feature allows IPv6 underlay routing protocol with RFC5549 addresses to be used along with IPv4 advertisements as
    VXLAN tunnel endpoints.
    Requires "underlay_rfc5549: true" and "loopback_ipv6_pool" under the node type settings.
    """
    underlay_isis_instance_name: str | None = None
    """
    Default -> "EVPN_UNDERLAY" for l3ls, "CORE" for mpls.
    """
    underlay_multicast: bool | None = False
    """
    Enable Multicast in the underlay on all p2p uplink interfaces and mlag l3 peer interface.
    Specifically PIM Sparse-Mode
    will be configured on all routed underlay interfaces.
    No other configuration is added, so the underlay will only support
    Source-Specific Multicast (SSM).
    The configuration is intended to be used as multicast underlay for EVPN OISM overlay.
    """
    underlay_multicast_anycast_rp: UnderlayMulticastAnycastRp | None = None
    """
    If multiple nodes are configured under 'underlay_multicast_rps.[].nodes' for the same RP address, they will be
    configured
    with one of the following methods:
    - Anycast RP using PIM (RFC4610).
    - Anycast RP using MSDP (RFC4611).
    NOTE: When using MSDP, all nodes across all MSDP enabled RPs will be added to a single MSDP mesh group named "ANYCAST-
    RP".
    """
    underlay_multicast_rps: list[UnderlayMulticastRpsItem] | None = None
    """
    List of PIM Sparse-Mode Rendevouz Points configured for underlay multicast on all devices.
    The device(s) listed under
    'nodes', will be configured as the Rendevouz point router(s).
    If multiple nodes are configured under 'nodes' for the
    same RP address, they will be configured
    according to the 'underlay_multicast_anycast_rp.mode' setting.

    Requires
    'underlay_multicast: true'.
    """
    underlay_ospf_area: Annotated[str, StrConvert(convert_types=(int))] | None = "0.0.0.0"
    underlay_ospf_bfd_enable: bool | None = False
    underlay_ospf_max_lsa: Annotated[int, IntConvert(convert_types=(str))] | None = 12000
    underlay_ospf_process_id: Annotated[int, IntConvert(convert_types=(str))] | None = 100
    underlay_rfc5549: bool | None = False
    """
    Point to Point Underlay with RFC 5549(eBGP), i.e. IPv6 Unnumbered.
    Requires "underlay_routing_protocol: ebgp".
    """
    underlay_routing_protocol: (
        Annotated[Literal["ebgp", "ospf", "ospf-ldp", "isis", "isis-sr", "isis-ldp", "isis-sr-ldp", "none"], StrConvert(to_lower=True)] | None
    ) = None
    """
    - The following underlay routing protocols are supported:
      - EBGP (default for l3ls-evpn)
      - OSPF.
      - OSPF-LDP*.
      -
    ISIS.
      - ISIS-SR*.
      - ISIS-LDP*.
      - ISIS-SR-LDP*.
      - No underlay routing protocol (none)
    - The variables should be
    applied to all devices in the fabric.
    *Only supported with core_interfaces data model.
    """
    uplink_ptp: UplinkPtp | None = None
    """
    Enable PTP on all infrastructure links.
    """
    use_cv_topology: bool | None = None
    """
    Generate AVD configurations directly from a given CloudVision topology.
    See `cv_topology` for details.
    """
    vtep_vvtep_ip: str | None = None
    """
    IP Address used as Virtual VTEP. Will be configured as secondary IP on Loopback1.
    This is only needed for centralized
    routing designs.
    """
    wan_carriers: list[WanCarriersItem] | None = None
    """
    List of carriers used for the WAN configuration and their mapping to path-groups.
    """
    wan_ha: WanHa | None = None
    """
    PREVIEW: The `wan_ha` key is currently not supported
    """
    wan_ipsec_profiles: WanIpsecProfiles | None = None
    """
    Define IPsec profiles parameters for WAN configuration.
    """
    wan_mode: Literal["autovpn", "cv-pathfinder"] | None = "cv-pathfinder"
    """
    Select if the WAN should be run using CV Pathfinder or AutoVPN only.
    """
    wan_path_groups: list[WanPathGroupsItem] | None = None
    """
    List of path-groups used for the WAN configuration.
    """
    wan_route_servers: list[WanRouteServersItem] | None = None
    """
    List of the AutoVPN RRs when using `wan_mode`=`autovpn`, or the Pathfinders
    when using `wan_mode`=`cv-pathfinder`, to
    which the device should connect to.
    This is also used to establish iBGP sessions between WAN route servers.

    When the
    route server is part of the same inventory as the WAN routers,
    only the name is required.
    """
    wan_stun_dtls_disable: bool | None = False
    """
    WAN STUN connections are authenticated and secured with DTLS by default.
    For CV Pathfinder deployments CloudVision will
    automatically deploy certificates on the devices.
    In case of AutoVPN the certificates must be deployed manually to all
    devices.

    For LAB environments this can be disabled, if there are no certificates available.
    This should NOT be disabled
    for a WAN network connected to the internet, since it will leave the STUN service exposed with no authentication.
    """
    wan_stun_dtls_profile_name: str | None = "STUN-DTLS"
    """
    Name of the SSL profile used for DTLS on WAN STUN connections.
    When using automatic ceritficate deployment via
    CloudVision this name must be the same on all WAN routers.
    """
    wan_virtual_topologies: WanVirtualTopologies | None = None
    """
    Configure Virtual Topologies for CV Pathfinder and AutoVPN.
    Auto create a control plane profile/policy/application and
    enforce it being first in the default VRF.
    """
    custom_structured_configurations: list[CustomStructuredConfiguration] | None = None
    dynamic_keys: DynamicKeys | None = None
    """
    Dynamic keys
    """
