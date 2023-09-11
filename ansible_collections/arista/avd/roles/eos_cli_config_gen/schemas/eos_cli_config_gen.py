# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

from pydantic import BaseModel, Field


class EosCliConfigGen(BaseModel):
    class AaaAccounting(BaseModel):
        class Exec(BaseModel):
            class Console(BaseModel):
                type: str | None = Field(default=None)
                group: str | None = Field(default=None)
                logging: bool | None = Field(default=None)

            class Default(BaseModel):
                type: str | None = Field(default=None)
                group: str | None = Field(default=None)
                logging: bool | None = Field(default=None)

            console: Console | None = Field(default=None)
            default: Default | None = Field(default=None)

        class System(BaseModel):
            class Default(BaseModel):
                type: str | None = Field(default=None)
                group: str | None = Field(default=None)

            default: Default | None = Field(default=None)

        class Dot1x(BaseModel):
            class Default(BaseModel):
                type: str | None = Field(default=None)
                group: str | None = Field(default=None)

            default: Default | None = Field(default=None)

        class Commands(BaseModel):
            class ConsoleItem(BaseModel):
                commands: str | None = Field(default=None)
                type: str | None = Field(default=None)
                group: str | None = Field(default=None)
                logging: bool | None = Field(default=None)

            class DefaultItem(BaseModel):
                commands: str | None = Field(default=None)
                type: str | None = Field(default=None)
                group: str | None = Field(default=None)
                logging: bool | None = Field(default=None)

            console: list[ConsoleItem] | None = Field(default=None)
            default: list[DefaultItem] | None = Field(default=None)

        exec: Exec | None = Field(default=None)
        system: System | None = Field(default=None)
        dot1x: Dot1x | None = Field(default=None)
        commands: Commands | None = Field(default=None)

    class AaaAuthentication(BaseModel):
        class Login(BaseModel):
            default: str | None = Field(default=None)
            console: str | None = Field(default=None)

        class Enable(BaseModel):
            default: str | None = Field(default=None)

        class Dot1x(BaseModel):
            default: str | None = Field(default=None)

        class Policies(BaseModel):
            class Local(BaseModel):
                allow_nopassword: bool | None = Field(default=None)

            class Lockout(BaseModel):
                failure: int | None = Field(default=None)
                duration: int | None = Field(default=None)
                window: int | None = Field(default=None)

            on_failure_log: bool | None = Field(default=None)
            on_success_log: bool | None = Field(default=None)
            local: Local | None = Field(default=None)
            lockout: Lockout | None = Field(default=None)

        login: Login | None = Field(default=None)
        enable: Enable | None = Field(default=None)
        dot1x: Dot1x | None = Field(default=None)
        policies: Policies | None = Field(default=None)

    class AaaAuthorization(BaseModel):
        class Policy(BaseModel):
            local_default_role: str | None = Field(default=None)

        class Exec(BaseModel):
            default: str | None = Field(default=None)

        class Dynamic(BaseModel):
            dot1x_additional_groups: list[str] | None = Field(default=None)

        class Commands(BaseModel):
            class PrivilegeItem(BaseModel):
                level: str | None = Field(default=None)
                default: str | None = Field(default=None)

            all_default: str | None = Field(default=None)
            privilege: list[PrivilegeItem] | None = Field(default=None)

        policy: Policy | None = Field(default=None)
        exec: Exec | None = Field(default=None)
        config_commands: bool | None = Field(default=None)
        serial_console: bool | None = Field(default=None)
        dynamic: Dynamic | None = Field(default=None)
        commands: Commands | None = Field(default=None)

    class AaaRoot(BaseModel):
        class Secret(BaseModel):
            sha512_password: str | None = Field(default=None)

        secret: Secret | None = Field(default=None)

    class AaaServerGroupsItem(BaseModel):
        class ServersItem(BaseModel):
            server: str | None = Field(default=None)
            vrf: str | None = Field(default=None)

        name: str | None = Field(default=None)
        type: str | None = Field(default=None)
        servers: list[ServersItem] | None = Field(default=None)

    class AccessListsItem(BaseModel):
        class SequenceNumbersItem(BaseModel):
            sequence: int | None = Field(default=None)
            action: str = Field(default=None)

        name: str | None = Field(default=None)
        counters_per_entry: bool | None = Field(default=None)
        sequence_numbers: list[SequenceNumbersItem] = Field(default=None)

    class AddressLocking(BaseModel):
        class LeasesItem(BaseModel):
            ip: str = Field(default=None)
            mac: str = Field(default=None)

        class LockedAddress(BaseModel):
            expiration_mac_disabled: bool | None = Field(default=None)
            ipv4_enforcement_disabled: bool | None = Field(default=None)
            ipv6_enforcement_disabled: bool | None = Field(default=None)

        dhcp_servers_ipv4: list[str] | None = Field(default=None)
        disabled: bool | None = Field(default=None)
        leases: list[LeasesItem] | None = Field(default=None)
        local_interface: str | None = Field(default=None)
        locked_address: LockedAddress | None = Field(default=None)

    class Arp(BaseModel):
        class Aging(BaseModel):
            timeout_default: int | None = Field(default=None)

        aging: Aging | None = Field(default=None)

    class AsPath(BaseModel):
        class AccessListsItem(BaseModel):
            class EntriesItem(BaseModel):
                type: str | None = Field(default=None)
                match: str | None = Field(default=None)
                origin: str = Field(default="any")

            name: str | None = Field(default=None)
            entries: list[EntriesItem] | None = Field(default=None)

        regex_mode: str | None = Field(default=None)
        access_lists: list[AccessListsItem] | None = Field(default=None)

    class Banners(BaseModel):
        login: str | None = Field(default=None)
        motd: str | None = Field(default=None)

    class BgpGroupsItem(BaseModel):
        name: str | None = Field(default=None)
        vrf: str | None = Field(default=None)
        neighbors: list[str] | None = Field(default=None)
        bgp_maintenance_profiles: list[str] | None = Field(default=None)

    class Boot(BaseModel):
        class Secret(BaseModel):
            hash_algorithm: str = Field(default="sha512")
            key: str | None = Field(default=None)

        secret: Secret | None = Field(default=None)

    class ClassMaps(BaseModel):
        class PbrItem(BaseModel):
            class Ip(BaseModel):
                access_group: str | None = Field(default=None)

            name: str | None = Field(default=None)
            ip: Ip | None = Field(default=None)

        class QosItem(BaseModel):
            class Ip(BaseModel):
                access_group: str | None = Field(default=None)

            class Ipv6(BaseModel):
                access_group: str | None = Field(default=None)

            name: str | None = Field(default=None)
            vlan: int | None = Field(default=None)
            cos: int | None = Field(default=None)
            ip: Ip | None = Field(default=None)
            ipv6: Ipv6 | None = Field(default=None)

        pbr: list[PbrItem] | None = Field(default=None)
        qos: list[QosItem] | None = Field(default=None)

    class Clock(BaseModel):
        timezone: str | None = Field(default=None)

    class CommunityListsItem(BaseModel):
        name: str | None = Field(default=None)
        action: str = Field(default=None)

    class Cvx(BaseModel):
        class Services(BaseModel):
            class Mcs(BaseModel):
                class Redis(BaseModel):
                    password: str | None = Field(default=None)
                    password_type: str = Field(default="7")

                redis: Redis | None = Field(default=None)
                shutdown: bool | None = Field(default=None)

            class Vxlan(BaseModel):
                shutdown: bool | None = Field(default=None)
                vtep_mac_learning: str | None = Field(default=None)

            mcs: Mcs | None = Field(default=None)
            vxlan: Vxlan | None = Field(default=None)

        shutdown: bool | None = Field(default=None)
        peer_hosts: list[str] | None = Field(default=None)
        services: Services | None = Field(default=None)

    class DaemonTerminattr(BaseModel):
        class ClustersItem(BaseModel):
            class Cvauth(BaseModel):
                method: str | None = Field(default=None)
                key: str | None = Field(default=None)
                token_file: str | None = Field(default=None)
                cert_file: str | None = Field(default=None)
                ca_file: str | None = Field(default=None)
                key_file: str | None = Field(default=None)

            name: str | None = Field(default=None)
            cvaddrs: list[str] | None = Field(default=None)
            cvauth: Cvauth | None = Field(default=None)
            cvobscurekeyfile: bool | None = Field(default=None)
            cvproxy: str | None = Field(default=None)
            cvsourceip: str | None = Field(default=None)
            cvsourceintf: str | None = Field(default=None)
            cvvrf: str | None = Field(default=None)

        class Cvauth(BaseModel):
            method: str | None = Field(default=None)
            key: str | None = Field(default=None)
            token_file: str | None = Field(default=None)
            cert_file: str | None = Field(default=None)
            ca_file: str | None = Field(default=None)
            key_file: str | None = Field(default=None)

        cvaddrs: list[str] | None = Field(default=None)
        clusters: list[ClustersItem] | None = Field(default=None)
        cvauth: Cvauth | None = Field(default=None)
        cvobscurekeyfile: bool | None = Field(default=None)
        cvproxy: str | None = Field(default=None)
        cvsourceip: str | None = Field(default=None)
        cvsourceintf: str | None = Field(default=None)
        cvvrf: str | None = Field(default=None)
        cvgnmi: bool | None = Field(default=None)
        disable_aaa: bool | None = Field(default=None)
        grpcaddr: str | None = Field(default=None)
        grpcreadonly: bool | None = Field(default=None)
        ingestexclude: str | None = Field(default=None)
        smashexcludes: str | None = Field(default=None)
        taillogs: str | None = Field(default=None)
        ecodhcpaddr: str | None = Field(default=None)
        ipfix: bool | None = Field(default=None)
        ipfixaddr: str | None = Field(default=None)
        sflow: bool | None = Field(default=None)
        sflowaddr: str | None = Field(default=None)
        cvconfig: bool | None = Field(default=None)
        cvcompression: str | None = Field(default=None)

    class DaemonsItem(BaseModel):
        name: str | None = Field(default=None)
        exec: str = Field(default=None)
        enabled: bool = Field(default=True)

    class DhcpRelay(BaseModel):
        servers: list[str] | None = Field(default=None)
        tunnel_requests_disabled: bool | None = Field(default=None)

    class Dot1x(BaseModel):
        class MacBasedAuthentication(BaseModel):
            delay: int | None = Field(default=None)
            hold_period: int | None = Field(default=None)

        class RadiusAvPair(BaseModel):
            service_type: bool | None = Field(default=None)
            framed_mtu: int | None = Field(default=None)

        system_auth_control: bool | None = Field(default=None)
        protocol_lldp_bypass: bool | None = Field(default=None)
        dynamic_authorization: bool | None = Field(default=None)
        mac_based_authentication: MacBasedAuthentication | None = Field(default=None)
        radius_av_pair: RadiusAvPair | None = Field(default=None)

    class DynamicPrefixListsItem(BaseModel):
        class PrefixList(BaseModel):
            ipv4: str | None = Field(default=None)
            ipv6: str | None = Field(default=None)

        name: str | None = Field(default=None)
        match_map: str | None = Field(default=None)
        prefix_list: PrefixList | None = Field(default=None)

    class EnablePassword(BaseModel):
        hash_algorithm: str | None = Field(default=None)
        key: str | None = Field(default=None)

    class EosCliConfigGenConfiguration(BaseModel):
        hide_passwords: bool = Field(default=False)

    class EosCliConfigGenDocumentation(BaseModel):
        hide_passwords: bool = Field(default=True)

    class Errdisable(BaseModel):
        class Detect(BaseModel):
            causes: list[str] | None = Field(default=None)

        class Recovery(BaseModel):
            causes: list[str] | None = Field(default=None)
            interval: int = Field(default=300)

        detect: Detect | None = Field(default=None)
        recovery: Recovery | None = Field(default=None)

    class EthernetInterfacesItem(BaseModel):
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

                dynamic: list[DynamicItem] | None = Field(default=None)
                static: list[StaticItem] | None = Field(default=None)

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

                dynamic: list[DynamicItem] | None = Field(default=None)
                static: list[StaticItem] | None = Field(default=None)

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

                boundaries: list[BoundariesItem] | None = Field(default=None)
                static: bool | None = Field(default=None)

            class Ipv6(BaseModel):
                class BoundariesItem(BaseModel):
                    boundary: str | None = Field(default=None)

                boundaries: list[BoundariesItem] | None = Field(default=None)
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
            priorities: list[PrioritiesItem] | None = Field(default=None)

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
        trunk_groups: list[str] | None = Field(default=None)
        type: str | None = Field(default=None)
        snmp_trap_link_change: bool | None = Field(default=None)
        address_locking: AddressLocking | None = Field(default=None)
        flowcontrol: Flowcontrol | None = Field(default=None)
        vrf: str | None = Field(default=None)
        flow_tracker: FlowTracker | None = Field(default=None)
        error_correction_encoding: ErrorCorrectionEncoding | None = Field(default=None)
        link_tracking_groups: list[LinkTrackingGroupsItem] | None = Field(default=None)
        evpn_ethernet_segment: EvpnEthernetSegment | None = Field(default=None)
        encapsulation_dot1q_vlan: int | None = Field(default=None)
        encapsulation_vlan: EncapsulationVlan | None = Field(default=None)
        vlan_id: int | None = Field(default=None)
        ip_address: str | None = Field(default=None)
        ip_address_secondaries: list[str] | None = Field(default=None)
        ip_helpers: list[IpHelpersItem] | None = Field(default=None)
        ip_nat: IpNat | None = Field(default=None)
        ipv6_enable: bool | None = Field(default=None)
        ipv6_address: str | None = Field(default=None)
        ipv6_address_link_local: str | None = Field(default=None)
        ipv6_nd_ra_disabled: bool | None = Field(default=None)
        ipv6_nd_managed_config_flag: bool | None = Field(default=None)
        ipv6_nd_prefixes: list[Ipv6NdPrefixesItem] | None = Field(default=None)
        ipv6_dhcp_relay_destinations: list[Ipv6DhcpRelayDestinationsItem] | None = Field(default=None)
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
        ospf_message_digest_keys: list[OspfMessageDigestKeysItem] | None = Field(default=None)
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
        vlan_translations: list[VlanTranslationsItem] | None = Field(default=None)
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

    class EventHandlersItem(BaseModel):
        name: str | None = Field(default=None)
        action_type: str | None = Field(default=None)
        action: str | None = Field(default=None)
        delay: int | None = Field(default=None)
        trigger: str | None = Field(default=None)
        regex: str | None = Field(default=None)
        asynchronous: bool = Field(default=False)

    class EventMonitor(BaseModel):
        enabled: bool | None = Field(default=None)

    class FlowTrackingsItem(BaseModel):
        class TrackersItem(BaseModel):
            class RecordExport(BaseModel):
                on_inactive_timeout: int | None = Field(default=None)
                on_interval: int | None = Field(default=None)
                mpls: bool | None = Field(default=None)

            class ExportersItem(BaseModel):
                class Collector(BaseModel):
                    host: str | None = Field(default=None)
                    port: int | None = Field(default=None)

                class Format(BaseModel):
                    ipfix_version: int | None = Field(default=None)

                name: str | None = Field(default=None)
                collector: Collector | None = Field(default=None)
                format: Format | None = Field(default=None)
                local_interface: str | None = Field(default=None)
                template_interval: int | None = Field(default=None)

            name: str | None = Field(default=None)
            record_export: RecordExport | None = Field(default=None)
            exporters: list[ExportersItem] | None = Field(default=None)
            table_size: int | None = Field(default=None)

        type: str | None = Field(default=None)
        sample: int | None = Field(default=None)
        trackers: list[TrackersItem] | None = Field(default=None)
        shutdown: bool = Field(default=False)

    class Hardware(BaseModel):
        class AccessList(BaseModel):
            mechanism: str | None = Field(default=None)

        class SpeedGroupsItem(BaseModel):
            speed_group: int | None = Field(default=None)
            serdes: str | None = Field(default=None)

        access_list: AccessList | None = Field(default=None)
        speed_groups: list[SpeedGroupsItem] | None = Field(default=None)

    class HardwareCounters(BaseModel):
        class FeaturesItem(BaseModel):
            name: str | None = Field(default=None)
            direction: str | None = Field(default=None)
            address_type: str | None = Field(default=None)
            layer3: bool | None = Field(default=None)
            vrf: str | None = Field(default=None)
            prefix: str | None = Field(default=None)
            units_packets: bool | None = Field(default=None)

        features: list[FeaturesItem] | None = Field(default=None)

    class InterfaceDefaults(BaseModel):
        class Ethernet(BaseModel):
            shutdown: bool | None = Field(default=None)

        ethernet: Ethernet | None = Field(default=None)
        mtu: int | None = Field(default=None)

    class InterfaceGroupsItem(BaseModel):
        name: str | None = Field(default=None)
        interfaces: list[str] | None = Field(default=None)
        bgp_maintenance_profiles: list[str] | None = Field(default=None)
        interface_maintenance_profiles: list[str] | None = Field(default=None)

    class InterfaceProfilesItem(BaseModel):
        name: str | None = Field(default=None)
        commands: list[str] = Field(default=None)

    class IpAccessListsItem(BaseModel):
        class EntriesItem(BaseModel):
            sequence: int | None = Field(default=None)
            remark: str | None = Field(default=None)
            action: str | None = Field(default=None)
            protocol: str | None = Field(default=None)
            source: str | None = Field(default=None)
            source_ports_match: str = Field(default="eq")
            source_ports: list[str] | None = Field(default=None)
            destination: str | None = Field(default=None)
            destination_ports_match: str = Field(default="eq")
            destination_ports: list[str] | None = Field(default=None)
            tcp_flags: list[str] | None = Field(default=None)
            fragments: bool | None = Field(default=None)
            log: bool | None = Field(default=None)
            ttl: int | None = Field(default=None)
            ttl_match: str = Field(default="eq")
            icmp_type: str | None = Field(default=None)
            icmp_code: str | None = Field(default=None)
            nexthop_group: str | None = Field(default=None)
            tracked: bool | None = Field(default=None)
            dscp: str | None = Field(default=None)
            vlan_number: int | None = Field(default=None)
            vlan_inner: bool = Field(default=False)
            vlan_mask: str | None = Field(default=None)

        name: str | None = Field(default=None)
        counters_per_entry: bool | None = Field(default=None)
        entries: list[EntriesItem] | None = Field(default=None)

    class IpCommunityListsItem(BaseModel):
        class EntriesItem(BaseModel):
            action: str = Field(default=None)
            communities: list[str] | None = Field(default=None)
            regexp: str | None = Field(default=None)

        name: str | None = Field(default=None)
        entries: list[EntriesItem] = Field(default=None)

    class IpDhcpRelay(BaseModel):
        information_option: bool | None = Field(default=None)

    class IpDomainLookup(BaseModel):
        class SourceInterfacesItem(BaseModel):
            name: str | None = Field(default=None)
            vrf: str | None = Field(default=None)

        source_interfaces: list[SourceInterfacesItem] | None = Field(default=None)

    class IpExtcommunityListsItem(BaseModel):
        class EntriesItem(BaseModel):
            type: str = Field(default=None)
            extcommunities: str = Field(default=None)

        name: str | None = Field(default=None)
        entries: list[EntriesItem] = Field(default=None)

    class IpExtcommunityListsRegexpItem(BaseModel):
        class EntriesItem(BaseModel):
            type: str = Field(default=None)
            regexp: str = Field(default=None)

        name: str | None = Field(default=None)
        entries: list[EntriesItem] = Field(default=None)

    class IpHardware(BaseModel):
        class Fib(BaseModel):
            class Optimize(BaseModel):
                class Prefixes(BaseModel):
                    profile: str | None = Field(default=None)

                prefixes: Prefixes | None = Field(default=None)

            optimize: Optimize | None = Field(default=None)

        fib: Fib | None = Field(default=None)

    class IpHttpClientSourceInterfacesItem(BaseModel):
        name: str | None = Field(default=None)
        vrf: str | None = Field(default=None)

    class IpIgmpSnooping(BaseModel):
        class Querier(BaseModel):
            enabled: bool | None = Field(default=None)
            address: str | None = Field(default=None)
            query_interval: int | None = Field(default=None)
            max_response_time: int | None = Field(default=None)
            last_member_query_interval: int | None = Field(default=None)
            last_member_query_count: int | None = Field(default=None)
            startup_query_interval: int | None = Field(default=None)
            startup_query_count: int | None = Field(default=None)
            version: int | None = Field(default=None)

        class VlansItem(BaseModel):
            class Querier(BaseModel):
                enabled: bool | None = Field(default=None)
                address: str | None = Field(default=None)
                query_interval: int | None = Field(default=None)
                max_response_time: int | None = Field(default=None)
                last_member_query_interval: int | None = Field(default=None)
                last_member_query_count: int | None = Field(default=None)
                startup_query_interval: int | None = Field(default=None)
                startup_query_count: int | None = Field(default=None)
                version: int | None = Field(default=None)

            id: int | None = Field(default=None)
            enabled: bool | None = Field(default=None)
            querier: Querier | None = Field(default=None)
            max_groups: int | None = Field(default=None)
            fast_leave: bool | None = Field(default=None)
            proxy: bool | None = Field(default=None)

        globally_enabled: bool = Field(default=True)
        robustness_variable: int | None = Field(default=None)
        restart_query_interval: int | None = Field(default=None)
        interface_restart_query: int | None = Field(default=None)
        fast_leave: bool | None = Field(default=None)
        querier: Querier | None = Field(default=None)
        proxy: bool | None = Field(default=None)
        vlans: list[VlansItem] | None = Field(default=None)

    class IpNameServersItem(BaseModel):
        ip_address: str | None = Field(default=None)
        vrf: str | None = Field(default=None)
        priority: int | None = Field(default=None)

    class IpNat(BaseModel):
        class PoolsItem(BaseModel):
            class RangesItem(BaseModel):
                first_ip: str = Field(default=None)
                last_ip: str = Field(default=None)
                first_port: int | None = Field(default=None)
                last_port: int | None = Field(default=None)

            name: str | None = Field(default=None)
            prefix_length: int = Field(default=None)
            ranges: list[RangesItem] | None = Field(default=None)
            utilization_log_threshold: int | None = Field(default=None)

        class Synchronization(BaseModel):
            class PortRange(BaseModel):
                first_port: int | None = Field(default=None)
                last_port: int | None = Field(default=None)
                split_disabled: bool | None = Field(default=None)

            description: str | None = Field(default=None)
            expiry_interval: int | None = Field(default=None)
            local_interface: str | None = Field(default=None)
            peer_address: str | None = Field(default=None)
            port_range: PortRange | None = Field(default=None)
            shutdown: bool | None = Field(default=None)

        class Translation(BaseModel):
            class AddressSelection(BaseModel):
                any: bool | None = Field(default=None)
                hash_field_source_ip: bool | None = Field(default=None)

            class LowMark(BaseModel):
                percentage: int | None = Field(default=None)
                host_percentage: int | None = Field(default=None)

            class MaxEntries(BaseModel):
                class IpLimitsItem(BaseModel):
                    ip: str | None = Field(default=None)
                    limit: int = Field(default=None)

                limit: int | None = Field(default=None)
                host_limit: int | None = Field(default=None)
                ip_limits: list[IpLimitsItem] | None = Field(default=None)

            class TimeoutsItem(BaseModel):
                protocol: str | None = Field(default=None)
                timeout: int = Field(default=None)

            address_selection: AddressSelection | None = Field(default=None)
            counters: bool | None = Field(default=None)
            low_mark: LowMark | None = Field(default=None)
            max_entries: MaxEntries | None = Field(default=None)
            timeouts: list[TimeoutsItem] | None = Field(default=None)

        kernel_buffer_size: int | None = Field(default=None)
        pools: list[PoolsItem] | None = Field(default=None)
        synchronization: Synchronization | None = Field(default=None)
        translation: Translation | None = Field(default=None)

    class IpRadiusSourceInterfacesItem(BaseModel):
        name: str | None = Field(default=None)
        vrf: str | None = Field(default=None)

    class IpSshClientSourceInterfacesItem(BaseModel):
        name: str | None = Field(default=None)
        vrf: str = Field(default="default")

    class IpTacacsSourceInterfacesItem(BaseModel):
        name: str | None = Field(default=None)
        vrf: str | None = Field(default=None)

    class Ipv6AccessListsItem(BaseModel):
        class SequenceNumbersItem(BaseModel):
            sequence: int | None = Field(default=None)
            action: str = Field(default=None)

        name: str | None = Field(default=None)
        counters_per_entry: bool | None = Field(default=None)
        sequence_numbers: list[SequenceNumbersItem] = Field(default=None)

    class Ipv6Hardware(BaseModel):
        class Fib(BaseModel):
            class Optimize(BaseModel):
                class Prefixes(BaseModel):
                    profile: str | None = Field(default=None)

                prefixes: Prefixes | None = Field(default=None)

            optimize: Optimize | None = Field(default=None)

        fib: Fib | None = Field(default=None)

    class Ipv6PrefixListsItem(BaseModel):
        class SequenceNumbersItem(BaseModel):
            sequence: int | None = Field(default=None)
            action: str = Field(default=None)

        name: str | None = Field(default=None)
        sequence_numbers: list[SequenceNumbersItem] = Field(default=None)

    class Ipv6StandardAccessListsItem(BaseModel):
        class SequenceNumbersItem(BaseModel):
            sequence: int | None = Field(default=None)
            action: str = Field(default=None)

        name: str | None = Field(default=None)
        counters_per_entry: bool | None = Field(default=None)
        sequence_numbers: list[SequenceNumbersItem] = Field(default=None)

    class Ipv6StaticRoutesItem(BaseModel):
        vrf: str | None = Field(default=None)
        destination_address_prefix: str | None = Field(default=None)
        interface: str | None = Field(default=None)
        gateway: str | None = Field(default=None)
        track_bfd: bool | None = Field(default=None)
        distance: int | None = Field(default=None)
        tag: int | None = Field(default=None)
        name: str | None = Field(default=None)
        metric: int | None = Field(default=None)

    class L2Protocol(BaseModel):
        class ForwardingProfilesItem(BaseModel):
            class ProtocolsItem(BaseModel):
                name: str | None = Field(default=None)
                forward: bool | None = Field(default=None)
                tagged_forward: bool | None = Field(default=None)
                untagged_forward: bool | None = Field(default=None)

            name: str | None = Field(default=None)
            protocols: list[ProtocolsItem] | None = Field(default=None)

        forwarding_profiles: list[ForwardingProfilesItem] | None = Field(default=None)

    class Lacp(BaseModel):
        class PortId(BaseModel):
            class Range(BaseModel):
                begin: int | None = Field(default=None)
                end: int | None = Field(default=None)

            range: Range | None = Field(default=None)

        class RateLimit(BaseModel):
            default: bool | None = Field(default=None)

        port_id: PortId | None = Field(default=None)
        rate_limit: RateLimit | None = Field(default=None)
        system_priority: int | None = Field(default=None)

    class LinkTrackingGroupsItem(BaseModel):
        name: str | None = Field(default=None)
        links_minimum: int | None = Field(default=None)
        recovery_delay: int | None = Field(default=None)

    class Lldp(BaseModel):
        class TlvsItem(BaseModel):
            name: str | None = Field(default=None)
            transmit: bool | None = Field(default=None)

        timer: int | None = Field(default=None)
        timer_reinitialization: str | None = Field(default=None)
        holdtime: int | None = Field(default=None)
        management_address: str | None = Field(default=None)
        vrf: str | None = Field(default=None)
        receive_packet_tagged_drop: str | None = Field(default=None)
        tlvs: list[TlvsItem] | None = Field(default=None)
        run: bool | None = Field(default=None)

    class LoadInterval(BaseModel):
        default: int | None = Field(default=None)

    class LocalUsersItem(BaseModel):
        name: str | None = Field(default=None)
        disabled: bool | None = Field(default=None)
        privilege: int | None = Field(default=None)
        role: str | None = Field(default=None)
        sha512_password: str | None = Field(default=None)
        no_password: bool | None = Field(default=None)
        ssh_key: str | None = Field(default=None)
        shell: str | None = Field(default=None)

    class Logging(BaseModel):
        class Buffered(BaseModel):
            size: int | None = Field(default=None)
            level: str | None = Field(default=None)

        class Synchronous(BaseModel):
            level: str = Field(default="critical")

        class Format(BaseModel):
            timestamp: str | None = Field(default=None)
            hostname: str | None = Field(default=None)
            sequence_numbers: bool | None = Field(default=None)

        class VrfsItem(BaseModel):
            class HostsItem(BaseModel):
                name: str | None = Field(default=None)
                protocol: str = Field(default="udp")
                ports: list[int] | None = Field(default=None)

            name: str | None = Field(default=None)
            source_interface: str | None = Field(default=None)
            hosts: list[HostsItem] | None = Field(default=None)

        class Policy(BaseModel):
            class Match(BaseModel):
                class MatchListsItem(BaseModel):
                    name: str | None = Field(default=None)
                    action: str | None = Field(default=None)

                match_lists: list[MatchListsItem] | None = Field(default=None)

            match: Match | None = Field(default=None)

        class Event(BaseModel):
            class StormControl(BaseModel):
                class Discards(BaseModel):
                    global_key: bool | None = Field(default=None, alias="global")
                    interval: int | None = Field(default=None)

                discards: Discards | None = Field(default=None)

            storm_control: StormControl | None = Field(default=None)

        console: str | None = Field(default=None)
        monitor: str | None = Field(default=None)
        buffered: Buffered | None = Field(default=None)
        trap: str | None = Field(default=None)
        synchronous: Synchronous | None = Field(default=None)
        format: Format | None = Field(default=None)
        facility: str | None = Field(default=None)
        source_interface: str | None = Field(default=None)
        vrfs: list[VrfsItem] | None = Field(default=None)
        policy: Policy | None = Field(default=None)
        event: Event | None = Field(default=None)

    class LoopbackInterfacesItem(BaseModel):
        class Mpls(BaseModel):
            class Ldp(BaseModel):
                interface: bool | None = Field(default=None)

            ldp: Ldp | None = Field(default=None)

        class NodeSegment(BaseModel):
            ipv4_index: int | None = Field(default=None)
            ipv6_index: int | None = Field(default=None)

        name: str | None = Field(default=None)
        description: str | None = Field(default=None)
        shutdown: bool | None = Field(default=None)
        vrf: str | None = Field(default=None)
        ip_address: str | None = Field(default=None)
        ip_address_secondaries: list[str] | None = Field(default=None)
        ipv6_enable: bool | None = Field(default=None)
        ipv6_address: str | None = Field(default=None)
        ip_proxy_arp: bool | None = Field(default=None)
        ospf_area: str | None = Field(default=None)
        mpls: Mpls | None = Field(default=None)
        isis_enable: str | None = Field(default=None)
        isis_passive: bool | None = Field(default=None)
        isis_metric: int | None = Field(default=None)
        isis_network_point_to_point: bool | None = Field(default=None)
        node_segment: NodeSegment | None = Field(default=None)
        eos_cli: str | None = Field(default=None)

    class MacAccessListsItem(BaseModel):
        class EntriesItem(BaseModel):
            sequence: int | None = Field(default=None)
            action: str | None = Field(default=None)

        name: str | None = Field(default=None)
        counters_per_entry: bool | None = Field(default=None)
        entries: list[EntriesItem] | None = Field(default=None)

    class MacAddressTable(BaseModel):
        class NotificationHostFlap(BaseModel):
            class Detection(BaseModel):
                window: int | None = Field(default=None)
                moves: int | None = Field(default=None)

            logging: bool | None = Field(default=None)
            detection: Detection | None = Field(default=None)

        aging_time: int | None = Field(default=None)
        notification_host_flap: NotificationHostFlap | None = Field(default=None)

    class MacSecurity(BaseModel):
        class License(BaseModel):
            license_name: str = Field(default=None)
            license_key: str = Field(default=None)

        class ProfilesItem(BaseModel):
            class ConnectionKeysItem(BaseModel):
                id: str | None = Field(default=None)
                encrypted_key: str | None = Field(default=None)
                fallback: bool | None = Field(default=None)

            class Mka(BaseModel):
                class Session(BaseModel):
                    rekey_period: int | None = Field(default=None)

                key_server_priority: int | None = Field(default=None)
                session: Session | None = Field(default=None)

            class L2Protocols(BaseModel):
                class EthernetFlowControl(BaseModel):
                    mode: str = Field(default=None)

                class Lldp(BaseModel):
                    mode: str = Field(default=None)

                ethernet_flow_control: EthernetFlowControl | None = Field(default=None)
                lldp: Lldp | None = Field(default=None)

            name: str | None = Field(default=None)
            cipher: str | None = Field(default=None)
            connection_keys: list[ConnectionKeysItem] | None = Field(default=None)
            mka: Mka | None = Field(default=None)
            sci: bool | None = Field(default=None)
            l2_protocols: L2Protocols | None = Field(default=None)

        license: License = Field(default=None)
        fips_restrictions: bool = Field(default=None)
        profiles: list[ProfilesItem] | None = Field(default=None)

    class Maintenance(BaseModel):
        class InterfaceProfilesItem(BaseModel):
            class RateMonitoring(BaseModel):
                load_interval: int | None = Field(default=None)
                threshold: int | None = Field(default=None)

            class Shutdown(BaseModel):
                max_delay: int | None = Field(default=None)

            name: str | None = Field(default=None)
            rate_monitoring: RateMonitoring | None = Field(default=None)
            shutdown: Shutdown | None = Field(default=None)

        class BgpProfilesItem(BaseModel):
            class Initiator(BaseModel):
                route_map_inout: str | None = Field(default=None)

            name: str | None = Field(default=None)
            initiator: Initiator | None = Field(default=None)

        class UnitProfilesItem(BaseModel):
            class OnBoot(BaseModel):
                duration: int | None = Field(default=None)

            name: str | None = Field(default=None)
            on_boot: OnBoot | None = Field(default=None)

        class UnitsItem(BaseModel):
            class Groups(BaseModel):
                bgp_groups: list[str] | None = Field(default=None)
                interface_groups: list[str] | None = Field(default=None)

            name: str | None = Field(default=None)
            quiesce: bool | None = Field(default=None)
            profile: str | None = Field(default=None)
            groups: Groups | None = Field(default=None)

        default_interface_profile: str | None = Field(default=None)
        default_bgp_profile: str | None = Field(default=None)
        default_unit_profile: str | None = Field(default=None)
        interface_profiles: list[InterfaceProfilesItem] | None = Field(default=None)
        bgp_profiles: list[BgpProfilesItem] | None = Field(default=None)
        unit_profiles: list[UnitProfilesItem] | None = Field(default=None)
        units: list[UnitsItem] | None = Field(default=None)

    class ManagementAccounts(BaseModel):
        class Password(BaseModel):
            policy: str | None = Field(default=None)

        password: Password | None = Field(default=None)

    class ManagementApiGnmi(BaseModel):
        class Transport(BaseModel):
            class GrpcItem(BaseModel):
                name: str | None = Field(default=None)
                ssl_profile: str | None = Field(default=None)
                vrf: str | None = Field(default=None)
                notification_timestamp: str | None = Field(default=None)
                ip_access_group: str | None = Field(default=None)

            class GrpcTunnelsItem(BaseModel):
                class Destination(BaseModel):
                    address: str = Field(default=None)
                    port: int = Field(default=None)

                class LocalInterface(BaseModel):
                    name: str = Field(default=None)
                    port: int = Field(default=None)

                class Target(BaseModel):
                    use_serial_number: bool | None = Field(default=None)
                    target_ids: list[str] | None = Field(default=None)

                name: str | None = Field(default=None)
                shutdown: bool | None = Field(default=None)
                tunnel_ssl_profile: str | None = Field(default=None)
                gnmi_ssl_profile: str | None = Field(default=None)
                vrf: str | None = Field(default=None)
                destination: Destination | None = Field(default=None)
                local_interface: LocalInterface | None = Field(default=None)
                target: Target | None = Field(default=None)

            grpc: list[GrpcItem] | None = Field(default=None)
            grpc_tunnels: list[GrpcTunnelsItem] | None = Field(default=None)

        class EnableVrfsItem(BaseModel):
            name: str | None = Field(default=None)
            access_group: str | None = Field(default=None)

        provider: str = Field(default="eos-native")
        transport: Transport | None = Field(default=None)
        enable_vrfs: list[EnableVrfsItem] | None = Field(default=None)
        octa: dict | None = Field(default=None)

    class ManagementApiHttp(BaseModel):
        class EnableVrfsItem(BaseModel):
            name: str | None = Field(default=None)
            access_group: str | None = Field(default=None)
            ipv6_access_group: str | None = Field(default=None)

        class ProtocolHttpsCertificate(BaseModel):
            certificate: str | None = Field(default=None)
            private_key: str | None = Field(default=None)

        enable_http: bool | None = Field(default=None)
        enable_https: bool | None = Field(default=None)
        https_ssl_profile: str | None = Field(default=None)
        default_services: bool | None = Field(default=None)
        enable_vrfs: list[EnableVrfsItem] | None = Field(default=None)
        protocol_https_certificate: ProtocolHttpsCertificate | None = Field(default=None)

    class ManagementApiModels(BaseModel):
        class ProvidersItem(BaseModel):
            class PathsItem(BaseModel):
                path: str | None = Field(default=None)
                disabled: bool = Field(default=False)

            name: str | None = Field(default=None)
            paths: list[PathsItem] | None = Field(default=None)

        providers: list[ProvidersItem] | None = Field(default=None)

    class ManagementConsole(BaseModel):
        idle_timeout: int | None = Field(default=None)

    class ManagementCvx(BaseModel):
        shutdown: bool | None = Field(default=None)
        server_hosts: list[str] | None = Field(default=None)
        source_interface: str | None = Field(default=None)
        vrf: str | None = Field(default=None)

    class ManagementDefaults(BaseModel):
        class Secret(BaseModel):
            hash: str | None = Field(default=None)

        secret: Secret | None = Field(default=None)

    class ManagementInterfacesItem(BaseModel):
        name: str | None = Field(default=None)
        description: str | None = Field(default=None)
        shutdown: bool | None = Field(default=None)
        mtu: int | None = Field(default=None)
        vrf: str | None = Field(default=None)
        ip_address: str | None = Field(default=None)
        ipv6_enable: bool | None = Field(default=None)
        ipv6_address: str | None = Field(default=None)
        type: str = Field(default="oob")
        gateway: str | None = Field(default=None)
        ipv6_gateway: str | None = Field(default=None)
        mac_address: str | None = Field(default=None)
        eos_cli: str | None = Field(default=None)

    class ManagementSecurity(BaseModel):
        class Password(BaseModel):
            class PoliciesItem(BaseModel):
                class Minimum(BaseModel):
                    digits: int | None = Field(default=None)
                    length: int | None = Field(default=None)
                    lower: int | None = Field(default=None)
                    special: int | None = Field(default=None)
                    upper: int | None = Field(default=None)

                class Maximum(BaseModel):
                    repetitive: int | None = Field(default=None)
                    sequential: int | None = Field(default=None)

                name: str | None = Field(default=None)
                minimum: Minimum | None = Field(default=None)
                maximum: Maximum | None = Field(default=None)

            minimum_length: int | None = Field(default=None)
            encryption_key_common: bool | None = Field(default=None)
            encryption_reversible: str | None = Field(default=None)
            policies: list[PoliciesItem] | None = Field(default=None)

        class SslProfilesItem(BaseModel):
            class TrustCertificate(BaseModel):
                class Requirement(BaseModel):
                    basic_constraint_ca: bool | None = Field(default=None)
                    hostname_fqdn: bool | None = Field(default=None)

                certificates: list[str] | None = Field(default=None)
                requirement: Requirement | None = Field(default=None)
                policy_expiry_date_ignore: bool | None = Field(default=None)
                system: bool | None = Field(default=None)

            class ChainCertificate(BaseModel):
                class Requirement(BaseModel):
                    basic_constraint_ca: bool | None = Field(default=None)
                    include_root_ca: bool | None = Field(default=None)

                certificates: list[str] | None = Field(default=None)
                requirement: Requirement | None = Field(default=None)

            class Certificate(BaseModel):
                file: str | None = Field(default=None)
                key: str | None = Field(default=None)

            name: str | None = Field(default=None)
            tls_versions: str | None = Field(default=None)
            cipher_list: str | None = Field(default=None)
            trust_certificate: TrustCertificate | None = Field(default=None)
            chain_certificate: ChainCertificate | None = Field(default=None)
            certificate: Certificate | None = Field(default=None)

        entropy_source: str | None = Field(default=None)
        password: Password | None = Field(default=None)
        ssl_profiles: list[SslProfilesItem] | None = Field(default=None)

    class ManagementSsh(BaseModel):
        class AccessGroupsItem(BaseModel):
            name: str | None = Field(default=None)
            vrf: str | None = Field(default=None)

        class Ipv6AccessGroupsItem(BaseModel):
            name: str | None = Field(default=None)
            vrf: str | None = Field(default=None)

        class Hostkey(BaseModel):
            server: list[str] | None = Field(default=None)

        class Connection(BaseModel):
            limit: int | None = Field(default=None)
            per_host: int | None = Field(default=None)

        class VrfsItem(BaseModel):
            name: str | None = Field(default=None)
            enable: bool | None = Field(default=None)

        access_groups: list[AccessGroupsItem] | None = Field(default=None)
        ipv6_access_groups: list[Ipv6AccessGroupsItem] | None = Field(default=None)
        idle_timeout: int | None = Field(default=None)
        cipher: list[str] | None = Field(default=None)
        key_exchange: list[str] | None = Field(default=None)
        mac: list[str] | None = Field(default=None)
        hostkey: Hostkey | None = Field(default=None)
        enable: bool | None = Field(default=None)
        connection: Connection | None = Field(default=None)
        vrfs: list[VrfsItem] | None = Field(default=None)
        log_level: str | None = Field(default=None)

    class ManagementTechSupport(BaseModel):
        class PolicyShowTechSupport(BaseModel):
            class ExcludeCommandsItem(BaseModel):
                command: str | None = Field(default=None)
                type: str = Field(default="text")

            class IncludeCommandsItem(BaseModel):
                command: str | None = Field(default=None)

            exclude_commands: list[ExcludeCommandsItem] | None = Field(default=None)
            include_commands: list[IncludeCommandsItem] | None = Field(default=None)

        policy_show_tech_support: PolicyShowTechSupport | None = Field(default=None)

    class MatchListInput(BaseModel):
        class StringItem(BaseModel):
            class SequenceNumbersItem(BaseModel):
                sequence: int | None = Field(default=None)
                match_regex: str = Field(default=None)

            name: str | None = Field(default=None)
            sequence_numbers: list[SequenceNumbersItem] = Field(default=None)

        string: list[StringItem] | None = Field(default=None)

    class McsClient(BaseModel):
        class CvxSecondary(BaseModel):
            name: str | None = Field(default=None)
            shutdown: bool | None = Field(default=None)
            server_hosts: list[str] | None = Field(default=None)

        shutdown: bool | None = Field(default=None)
        cvx_secondary: CvxSecondary | None = Field(default=None)

    class MlagConfiguration(BaseModel):
        class PeerAddressHeartbeat(BaseModel):
            peer_ip: str | None = Field(default=None)
            vrf: str | None = Field(default=None)

        domain_id: str | None = Field(default=None)
        heartbeat_interval: int | None = Field(default=None)
        local_interface: str | None = Field(default=None)
        peer_address: str | None = Field(default=None)
        peer_address_heartbeat: PeerAddressHeartbeat | None = Field(default=None)
        dual_primary_detection_delay: int | None = Field(default=None)
        dual_primary_recovery_delay_mlag: int | None = Field(default=None)
        dual_primary_recovery_delay_non_mlag: int | None = Field(default=None)
        peer_link: str | None = Field(default=None)
        reload_delay_mlag: str | None = Field(default=None)
        reload_delay_non_mlag: str | None = Field(default=None)

    class MonitorConnectivity(BaseModel):
        class InterfaceSetsItem(BaseModel):
            name: str | None = Field(default=None)
            interfaces: str | None = Field(default=None)

        class HostsItem(BaseModel):
            name: str | None = Field(default=None)
            description: str | None = Field(default=None)
            ip: str | None = Field(default=None)
            local_interfaces: str | None = Field(default=None)
            url: str | None = Field(default=None)

        class VrfsItem(BaseModel):
            class InterfaceSetsItem(BaseModel):
                name: str | None = Field(default=None)
                interfaces: str | None = Field(default=None)

            class HostsItem(BaseModel):
                name: str | None = Field(default=None)
                description: str | None = Field(default=None)
                ip: str | None = Field(default=None)
                local_interfaces: str | None = Field(default=None)
                url: str | None = Field(default=None)

            name: str | None = Field(default=None)
            description: str | None = Field(default=None)
            interface_sets: list[InterfaceSetsItem] | None = Field(default=None)
            local_interfaces: str | None = Field(default=None)
            hosts: list[HostsItem] | None = Field(default=None)

        shutdown: bool | None = Field(default=None)
        interval: int | None = Field(default=None)
        interface_sets: list[InterfaceSetsItem] | None = Field(default=None)
        local_interfaces: str | None = Field(default=None)
        hosts: list[HostsItem] | None = Field(default=None)
        vrfs: list[VrfsItem] | None = Field(default=None)

    class MonitorSessionsItem(BaseModel):
        class SourcesItem(BaseModel):
            class AccessGroup(BaseModel):
                type: str | None = Field(default=None)
                name: str | None = Field(default=None)
                priority: int | None = Field(default=None)

            name: str | None = Field(default=None)
            direction: str | None = Field(default=None)
            access_group: AccessGroup | None = Field(default=None)

        class AccessGroup(BaseModel):
            type: str | None = Field(default=None)
            name: str | None = Field(default=None)

        class Truncate(BaseModel):
            enabled: bool | None = Field(default=None)
            size: int | None = Field(default=None)

        name: str = Field(default=None)
        sources: list[SourcesItem] | None = Field(default=None)
        destinations: list[str] | None = Field(default=None)
        encapsulation_gre_metadata_tx: bool | None = Field(default=None)
        header_remove_size: int | None = Field(default=None)
        access_group: AccessGroup | None = Field(default=None)
        rate_limit_per_ingress_chip: str | None = Field(default=None)
        rate_limit_per_egress_chip: str | None = Field(default=None)
        sample: int | None = Field(default=None)
        truncate: Truncate | None = Field(default=None)

    class Mpls(BaseModel):
        class Ldp(BaseModel):
            interface_disabled_default: bool | None = Field(default=None)
            router_id: str | None = Field(default=None)
            shutdown: bool | None = Field(default=None)
            transport_address_interface: str | None = Field(default=None)

        ip: bool | None = Field(default=None)
        ldp: Ldp | None = Field(default=None)

    class NameServer(BaseModel):
        class Source(BaseModel):
            vrf: str | None = Field(default=None)

        source: Source | None = Field(default=None)
        nodes: list[str] | None = Field(default=None)

    class Ntp(BaseModel):
        class LocalInterface(BaseModel):
            name: str | None = Field(default=None)
            vrf: str | None = Field(default=None)

        class ServersItem(BaseModel):
            name: str | None = Field(default=None)
            burst: bool | None = Field(default=None)
            iburst: bool | None = Field(default=None)
            key: int | None = Field(default=None)
            local_interface: str | None = Field(default=None)
            maxpoll: int | None = Field(default=None)
            minpoll: int | None = Field(default=None)
            preferred: bool | None = Field(default=None)
            version: int | None = Field(default=None)
            vrf: str | None = Field(default=None)

        class AuthenticationKeysItem(BaseModel):
            id: int | None = Field(default=None)
            hash_algorithm: str | None = Field(default=None)
            key: str | None = Field(default=None)
            key_type: str | None = Field(default=None)

        local_interface: LocalInterface | None = Field(default=None)
        servers: list[ServersItem] | None = Field(default=None)
        authenticate: bool | None = Field(default=None)
        authenticate_servers_only: bool | None = Field(default=None)
        authentication_keys: list[AuthenticationKeysItem] | None = Field(default=None)
        trusted_keys: str | None = Field(default=None)

    class PatchPanel(BaseModel):
        class PatchesItem(BaseModel):
            class ConnectorsItem(BaseModel):
                id: str | None = Field(default=None)
                type: str = Field(default=None)
                endpoint: str = Field(default=None)

            name: str | None = Field(default=None)
            enabled: bool | None = Field(default=None)
            connectors: list[ConnectorsItem] | None = Field(default=None)

        patches: list[PatchesItem] | None = Field(default=None)

    class PeerFiltersItem(BaseModel):
        class SequenceNumbersItem(BaseModel):
            sequence: int | None = Field(default=None)
            match: str = Field(default=None)

        name: str | None = Field(default=None)
        sequence_numbers: list[SequenceNumbersItem] = Field(default=None)

    class Platform(BaseModel):
        class Trident(BaseModel):
            class Mmu(BaseModel):
                class QueueProfilesItem(BaseModel):
                    class MulticastQueuesItem(BaseModel):
                        class Drop(BaseModel):
                            precedence: int = Field(default=None)
                            threshold: str = Field(default=None)

                        id: int = Field(default=None)
                        unit: str | None = Field(default=None)
                        reserved: int | None = Field(default=None)
                        threshold: str | None = Field(default=None)
                        drop: Drop | None = Field(default=None)

                    class UnicastQueuesItem(BaseModel):
                        class Drop(BaseModel):
                            precedence: int = Field(default=None)
                            threshold: str = Field(default=None)

                        id: int = Field(default=None)
                        unit: str | None = Field(default=None)
                        reserved: int | None = Field(default=None)
                        threshold: str | None = Field(default=None)
                        drop: Drop | None = Field(default=None)

                    name: str | None = Field(default=None)
                    multicast_queues: list[MulticastQueuesItem] | None = Field(default=None)
                    unicast_queues: list[UnicastQueuesItem] | None = Field(default=None)

                active_profile: str | None = Field(default=None)
                queue_profiles: list[QueueProfilesItem] | None = Field(default=None)

            forwarding_table_partition: str | None = Field(default=None)
            mmu: Mmu | None = Field(default=None)

        class Sand(BaseModel):
            class QosMapsItem(BaseModel):
                traffic_class: int | None = Field(default=None)
                to_network_qos: int | None = Field(default=None)

            class Lag(BaseModel):
                hardware_only: bool | None = Field(default=None)
                mode: str | None = Field(default=None)

            class MulticastReplication(BaseModel):
                default: str | None = Field(default=None)

            qos_maps: list[QosMapsItem] | None = Field(default=None)
            lag: Lag | None = Field(default=None)
            forwarding_mode: str | None = Field(default=None)
            multicast_replication: MulticastReplication | None = Field(default=None)

        trident: Trident | None = Field(default=None)
        sand: Sand | None = Field(default=None)

    class Poe(BaseModel):
        class Reboot(BaseModel):
            action: str | None = Field(default=None)

        class InterfaceShutdown(BaseModel):
            action: str | None = Field(default=None)

        reboot: Reboot | None = Field(default=None)
        interface_shutdown: InterfaceShutdown | None = Field(default=None)

    class PolicyMaps(BaseModel):
        class PbrItem(BaseModel):
            class ClassesItem(BaseModel):
                class Set(BaseModel):
                    class Nexthop(BaseModel):
                        ip_address: str | None = Field(default=None)
                        recursive: bool | None = Field(default=None)

                    nexthop: Nexthop | None = Field(default=None)

                name: str | None = Field(default=None)
                index: int | None = Field(default=None)
                drop: bool | None = Field(default=None)
                set: Set | None = Field(default=None)

            name: str | None = Field(default=None)
            classes: list[ClassesItem] | None = Field(default=None)

        class QosItem(BaseModel):
            class ClassesItem(BaseModel):
                class Set(BaseModel):
                    cos: int | None = Field(default=None)
                    dscp: str | None = Field(default=None)
                    traffic_class: int | None = Field(default=None)
                    drop_precedence: int | None = Field(default=None)

                name: str | None = Field(default=None)
                set: Set | None = Field(default=None)

            name: str | None = Field(default=None)
            classes: list[ClassesItem] | None = Field(default=None)

        pbr: list[PbrItem] | None = Field(default=None)
        qos: list[QosItem] | None = Field(default=None)

    class PortChannelInterfacesItem(BaseModel):
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

                dynamic: list[DynamicItem] | None = Field(default=None)
                static: list[StaticItem] | None = Field(default=None)

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

                dynamic: list[DynamicItem] | None = Field(default=None)
                static: list[StaticItem] | None = Field(default=None)

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
        link_tracking_groups: list[LinkTrackingGroupsItem] | None = Field(default=None)
        phone: Phone | None = Field(default=None)
        l2_protocol: L2Protocol | None = Field(default=None)
        mtu: int | None = Field(default=None)
        mlag: int | None = Field(default=None)
        trunk_groups: list[str] | None = Field(default=None)
        lacp_fallback_timeout: int = Field(default=90)
        lacp_fallback_mode: str | None = Field(default=None)
        qos: Qos | None = Field(default=None)
        bfd: Bfd | None = Field(default=None)
        service_policy: ServicePolicy | None = Field(default=None)
        mpls: Mpls | None = Field(default=None)
        trunk_private_vlan_secondary: bool | None = Field(default=None)
        pvlan_mapping: str | None = Field(default=None)
        vlan_translations: list[VlanTranslationsItem] | None = Field(default=None)
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
        ipv6_nd_prefixes: list[Ipv6NdPrefixesItem] | None = Field(default=None)
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
        ospf_message_digest_keys: list[OspfMessageDigestKeysItem] | None = Field(default=None)
        flow_tracker: FlowTracker | None = Field(default=None)
        bgp: Bgp | None = Field(default=None)
        peer: str | None = Field(default=None)
        peer_interface: str | None = Field(default=None)
        peer_type: str | None = Field(default=None)
        sflow: Sflow | None = Field(default=None)
        eos_cli: str | None = Field(default=None)

    class PrefixListsItem(BaseModel):
        class SequenceNumbersItem(BaseModel):
            sequence: int | None = Field(default=None)
            action: str = Field(default=None)

        name: str | None = Field(default=None)
        sequence_numbers: list[SequenceNumbersItem] | None = Field(default=None)

    class PriorityFlowControl(BaseModel):
        class Watchdog(BaseModel):
            action: str | None = Field(default=None)
            timeout: str | None = Field(default=None)
            polling_interval: str | None = Field(default=None)
            recovery_time: str | None = Field(default=None)
            override_action_drop: bool | None = Field(default=None)

        all_off: bool | None = Field(default=None)
        watchdog: Watchdog | None = Field(default=None)

    class Ptp(BaseModel):
        class Source(BaseModel):
            ip: str | None = Field(default=None)

        class MessageType(BaseModel):
            class General(BaseModel):
                dscp: int | None = Field(default=None)

            class Event(BaseModel):
                dscp: int | None = Field(default=None)

            general: General | None = Field(default=None)
            event: Event | None = Field(default=None)

        class Monitor(BaseModel):
            class Threshold(BaseModel):
                class Drop(BaseModel):
                    offset_from_master: int | None = Field(default=None)
                    mean_path_delay: int | None = Field(default=None)

                offset_from_master: int | None = Field(default=None)
                mean_path_delay: int | None = Field(default=None)
                drop: Drop | None = Field(default=None)

            class MissingMessage(BaseModel):
                class Intervals(BaseModel):
                    announce: int | None = Field(default=None)
                    follow_up: int | None = Field(default=None)
                    sync: int | None = Field(default=None)

                class SequenceIds(BaseModel):
                    enabled: bool | None = Field(default=None)
                    announce: int | None = Field(default=None)
                    delay_resp: int | None = Field(default=None)
                    follow_up: int | None = Field(default=None)
                    sync: int | None = Field(default=None)

                intervals: Intervals | None = Field(default=None)
                sequence_ids: SequenceIds | None = Field(default=None)

            enabled: bool = Field(default=True)
            threshold: Threshold | None = Field(default=None)
            missing_message: MissingMessage | None = Field(default=None)

        mode: str | None = Field(default=None)
        forward_unicast: bool | None = Field(default=None)
        clock_identity: str | None = Field(default=None)
        source: Source | None = Field(default=None)
        priority1: int | None = Field(default=None)
        priority2: int | None = Field(default=None)
        ttl: int | None = Field(default=None)
        domain: int | None = Field(default=None)
        message_type: MessageType | None = Field(default=None)
        monitor: Monitor | None = Field(default=None)

    class Qos(BaseModel):
        class Map(BaseModel):
            cos: list[str] | None = Field(default=None)
            dscp: list[str] | None = Field(default=None)
            traffic_class: list[str] | None = Field(default=None)

        map: Map | None = Field(default=None)
        rewrite_dscp: bool | None = Field(default=None)

    class QosProfilesItem(BaseModel):
        class Shape(BaseModel):
            rate: str | None = Field(default=None)

        class ServicePolicy(BaseModel):
            class Type(BaseModel):
                qos_input: str | None = Field(default=None)

            type: Type | None = Field(default=None)

        class TxQueuesItem(BaseModel):
            class Shape(BaseModel):
                rate: str | None = Field(default=None)

            id: int | None = Field(default=None)
            bandwidth_percent: int | None = Field(default=None)
            bandwidth_guaranteed_percent: int | None = Field(default=None)
            priority: str | None = Field(default=None)
            shape: Shape | None = Field(default=None)
            comment: str | None = Field(default=None)

        class UcTxQueuesItem(BaseModel):
            class Shape(BaseModel):
                rate: str | None = Field(default=None)

            id: int | None = Field(default=None)
            bandwidth_percent: int | None = Field(default=None)
            bandwidth_guaranteed_percent: int | None = Field(default=None)
            priority: str | None = Field(default=None)
            shape: Shape | None = Field(default=None)
            comment: str | None = Field(default=None)

        class McTxQueuesItem(BaseModel):
            class Shape(BaseModel):
                rate: str | None = Field(default=None)

            id: int | None = Field(default=None)
            bandwidth_percent: int | None = Field(default=None)
            bandwidth_guaranteed_percent: int | None = Field(default=None)
            priority: str | None = Field(default=None)
            shape: Shape | None = Field(default=None)
            comment: str | None = Field(default=None)

        class PriorityFlowControl(BaseModel):
            class Watchdog(BaseModel):
                class Timer(BaseModel):
                    timeout: str = Field(default=None)
                    polling_interval: str = Field(default=None)
                    recovery_time: str = Field(default=None)
                    forced: bool | None = Field(default=None)

                enabled: bool = Field(default=None)
                action: str | None = Field(default=None)
                timer: Timer | None = Field(default=None)

            class PrioritiesItem(BaseModel):
                priority: int = Field(default=None)
                no_drop: bool = Field(default=None)

            enabled: bool | None = Field(default=None)
            watchdog: Watchdog | None = Field(default=None)
            priorities: list[PrioritiesItem] | None = Field(default=None)

        name: str | None = Field(default=None)
        trust: str | None = Field(default=None)
        cos: int | None = Field(default=None)
        dscp: int | None = Field(default=None)
        shape: Shape | None = Field(default=None)
        service_policy: ServicePolicy | None = Field(default=None)
        tx_queues: list[TxQueuesItem] | None = Field(default=None)
        uc_tx_queues: list[UcTxQueuesItem] | None = Field(default=None)
        mc_tx_queues: list[McTxQueuesItem] | None = Field(default=None)
        priority_flow_control: PriorityFlowControl | None = Field(default=None)

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
        default_thresholds: DefaultThresholds | None = Field(default=None)
        log: int | None = Field(default=None)
        notifying: bool | None = Field(default=None)
        cpu: Cpu | None = Field(default=None)

    class QueueMonitorStreaming(BaseModel):
        enable: bool | None = Field(default=None)
        ip_access_group: str | None = Field(default=None)
        ipv6_access_group: str | None = Field(default=None)
        max_connections: int | None = Field(default=None)
        vrf: str | None = Field(default=None)

    class RadiusServer(BaseModel):
        class Attribute32IncludeInAccessReq(BaseModel):
            hostname: bool | None = Field(default=None)
            format: str | None = Field(default=None)

        class DynamicAuthorization(BaseModel):
            port: int | None = Field(default=None)
            tls_ssl_profile: str | None = Field(default=None)

        class HostsItem(BaseModel):
            host: str | None = Field(default=None)
            vrf: str | None = Field(default=None)
            timeout: int | None = Field(default=None)
            retransmit: int | None = Field(default=None)
            key: str | None = Field(default=None)

        attribute_32_include_in_access_req: Attribute32IncludeInAccessReq | None = Field(default=None)
        dynamic_authorization: DynamicAuthorization | None = Field(default=None)
        hosts: list[HostsItem] | None = Field(default=None)

    class RadiusServersItem(BaseModel):
        host: str | None = Field(default=None)
        vrf: str | None = Field(default=None)
        key: str | None = Field(default=None)

    class Redundancy(BaseModel):
        protocol: str | None = Field(default=None)

    class RolesItem(BaseModel):
        class SequenceNumbersItem(BaseModel):
            sequence: int | None = Field(default=None)
            action: str | None = Field(default=None)
            mode: str | None = Field(default=None)
            command: str | None = Field(default=None)

        name: str | None = Field(default=None)
        sequence_numbers: list[SequenceNumbersItem] | None = Field(default=None)

    class RouteMapsItem(BaseModel):
        class SequenceNumbersItem(BaseModel):
            class Continue(BaseModel):
                enabled: bool | None = Field(default=None)
                sequence_number: int | None = Field(default=None)

            sequence: int | None = Field(default=None)
            type: str = Field(default=None)
            description: str | None = Field(default=None)
            match: list[str] | None = Field(default=None)
            set: list[str] | None = Field(default=None)
            sub_route_map: str | None = Field(default=None)
            continue_key: Continue | None = Field(default=None, alias="continue")

        name: str | None = Field(default=None)
        sequence_numbers: list[SequenceNumbersItem] = Field(default=None)

    class RouterBfd(BaseModel):
        class Multihop(BaseModel):
            interval: int | None = Field(default=None)
            min_rx: int | None = Field(default=None)
            multiplier: int | None = Field(default=None)

        class Sbfd(BaseModel):
            class LocalInterface(BaseModel):
                class Protocols(BaseModel):
                    ipv4: bool | None = Field(default=None)
                    ipv6: bool | None = Field(default=None)

                name: str | None = Field(default=None)
                protocols: Protocols | None = Field(default=None)

            class Reflector(BaseModel):
                min_rx: int | None = Field(default=None)
                local_discriminator: str | None = Field(default=None)

            local_interface: LocalInterface | None = Field(default=None)
            initiator_interval: int | None = Field(default=None)
            initiator_multiplier: int | None = Field(default=None)
            reflector: Reflector | None = Field(default=None)

        interval: int | None = Field(default=None)
        min_rx: int | None = Field(default=None)
        multiplier: int | None = Field(default=None)
        multihop: Multihop | None = Field(default=None)
        sbfd: Sbfd | None = Field(default=None)

    class RouterBgp(BaseModel):
        class Distance(BaseModel):
            external_routes: int = Field(default=None)
            internal_routes: int = Field(default=None)
            local_routes: int = Field(default=None)

        class GracefulRestart(BaseModel):
            enabled: bool | None = Field(default=None)
            restart_time: int | None = Field(default=None)
            stalepath_time: int | None = Field(default=None)

        class GracefulRestartHelper(BaseModel):
            enabled: bool | None = Field(default=None)
            restart_time: int | None = Field(default=None)
            long_lived: bool | None = Field(default=None)

        class MaximumPaths(BaseModel):
            paths: int = Field(default=None)
            ecmp: int | None = Field(default=None)

        class Updates(BaseModel):
            wait_for_convergence: bool | None = Field(default=None)
            wait_install: bool | None = Field(default=None)

        class Bgp(BaseModel):
            class Default(BaseModel):
                ipv4_unicast: bool | None = Field(default=None)
                ipv4_unicast_transport_ipv6: bool | None = Field(default=None)

            class RouteReflectorPreserveAttributes(BaseModel):
                enabled: bool | None = Field(default=None)
                always: bool | None = Field(default=None)

            class Bestpath(BaseModel):
                d_path: bool | None = Field(default=None)

            default: Default | None = Field(default=None)
            route_reflector_preserve_attributes: RouteReflectorPreserveAttributes | None = Field(default=None)
            bestpath: Bestpath | None = Field(default=None)

        class ListenRangesItem(BaseModel):
            prefix: str | None = Field(default=None)
            peer_id_include_router_id: bool | None = Field(default=None)
            peer_group: str | None = Field(default=None)
            peer_filter: str | None = Field(default=None)
            remote_as: str | None = Field(default=None)

        class PeerGroupsItem(BaseModel):
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

        class NeighborsItem(BaseModel):
            class AsPath(BaseModel):
                remote_as_replace_out: bool | None = Field(default=None)
                prepend_own_disabled: bool | None = Field(default=None)

            class DefaultOriginate(BaseModel):
                enabled: bool | None = Field(default=None)
                always: bool | None = Field(default=None)
                route_map: str | None = Field(default=None)

            class AllowasIn(BaseModel):
                enabled: bool | None = Field(default=None)
                times: int | None = Field(default=None)

            class LinkBandwidth(BaseModel):
                enabled: bool | None = Field(default=None)
                default: str | None = Field(default=None)

            class RibInPrePolicyRetain(BaseModel):
                enabled: bool | None = Field(default=None)
                all: bool | None = Field(default=None)

            class RemovePrivateAs(BaseModel):
                enabled: bool | None = Field(default=None)
                all: bool | None = Field(default=None)
                replace_as: bool | None = Field(default=None)

            class RemovePrivateAsIngress(BaseModel):
                enabled: bool | None = Field(default=None)
                replace_as: bool | None = Field(default=None)

            ip_address: str | None = Field(default=None)
            peer_group: str | None = Field(default=None)
            remote_as: str | None = Field(default=None)
            local_as: str | None = Field(default=None)
            as_path: AsPath | None = Field(default=None)
            description: str | None = Field(default=None)
            route_reflector_client: bool | None = Field(default=None)
            passive: bool | None = Field(default=None)
            shutdown: bool | None = Field(default=None)
            update_source: str | None = Field(default=None)
            bfd: bool | None = Field(default=None)
            weight: int | None = Field(default=None)
            timers: str | None = Field(default=None)
            route_map_in: str | None = Field(default=None)
            route_map_out: str | None = Field(default=None)
            default_originate: DefaultOriginate | None = Field(default=None)
            send_community: str | None = Field(default=None)
            maximum_routes: int | None = Field(default=None)
            maximum_routes_warning_limit: str | None = Field(default=None)
            maximum_routes_warning_only: bool | None = Field(default=None)
            allowas_in: AllowasIn | None = Field(default=None)
            ebgp_multihop: int | None = Field(default=None)
            next_hop_self: bool | None = Field(default=None)
            link_bandwidth: LinkBandwidth | None = Field(default=None)
            rib_in_pre_policy_retain: RibInPrePolicyRetain | None = Field(default=None)
            remove_private_as: RemovePrivateAs | None = Field(default=None)
            remove_private_as_ingress: RemovePrivateAsIngress | None = Field(default=None)
            session_tracker: str | None = Field(default=None)

        class NeighborInterfacesItem(BaseModel):
            name: str | None = Field(default=None)
            remote_as: str | None = Field(default=None)
            peer_group: str = Field(default="Peer-group name")
            description: str | None = Field(default=None)
            peer_filter: str | None = Field(default=None)

        class AggregateAddressesItem(BaseModel):
            prefix: str | None = Field(default=None)
            advertise_only: bool | None = Field(default=None)
            as_set: bool | None = Field(default=None)
            summary_only: bool | None = Field(default=None)
            attribute_map: str | None = Field(default=None)
            match_map: str | None = Field(default=None)

        class RedistributeRoutesItem(BaseModel):
            source_protocol: str | None = Field(default=None)
            route_map: str | None = Field(default=None)
            include_leaked: bool | None = Field(default=None)

        class VlanAwareBundlesItem(BaseModel):
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

                both: list[str] | None = Field(default=None)
                import_key: list[str] | None = Field(default=None, alias="import")
                export: list[str] | None = Field(default=None)
                import_evpn_domains: list[ImportEvpnDomainsItem] | None = Field(default=None)
                export_evpn_domains: list[ExportEvpnDomainsItem] | None = Field(default=None)
                import_export_evpn_domains: list[ImportExportEvpnDomainsItem] | None = Field(default=None)

            name: str | None = Field(default=None)
            tenant: str | None = Field(default=None)
            description: str | None = Field(default=None)
            rd: str | None = Field(default=None)
            rd_evpn_domain: RdEvpnDomain | None = Field(default=None)
            route_targets: RouteTargets | None = Field(default=None)
            redistribute_routes: list[str] | None = Field(default=None)
            no_redistribute_routes: list[str] | None = Field(default=None)
            vlan: str | None = Field(default=None)

        class VlansItem(BaseModel):
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

                both: list[str] | None = Field(default=None)
                import_key: list[str] | None = Field(default=None, alias="import")
                export: list[str] | None = Field(default=None)
                import_evpn_domains: list[ImportEvpnDomainsItem] | None = Field(default=None)
                export_evpn_domains: list[ExportEvpnDomainsItem] | None = Field(default=None)
                import_export_evpn_domains: list[ImportExportEvpnDomainsItem] | None = Field(default=None)

            id: int | None = Field(default=None)
            tenant: str | None = Field(default=None)
            rd: str | None = Field(default=None)
            rd_evpn_domain: RdEvpnDomain | None = Field(default=None)
            eos_cli: str | None = Field(default=None)
            route_targets: RouteTargets | None = Field(default=None)
            redistribute_routes: list[str] | None = Field(default=None)
            no_redistribute_routes: list[str] | None = Field(default=None)

        class VpwsItem(BaseModel):
            class RouteTargets(BaseModel):
                import_export: str | None = Field(default=None)

            class PseudowiresItem(BaseModel):
                name: str | None = Field(default=None)
                id_local: int | None = Field(default=None)
                id_remote: int | None = Field(default=None)

            name: str | None = Field(default=None)
            rd: str | None = Field(default=None)
            route_targets: RouteTargets | None = Field(default=None)
            mpls_control_word: bool | None = Field(default=None)
            label_flow: bool | None = Field(default=None)
            mtu: int | None = Field(default=None)
            pseudowires: list[PseudowiresItem] | None = Field(default=None)

        class AddressFamilyEvpn(BaseModel):
            class NeighborDefault(BaseModel):
                class NextHopSelfReceivedEvpnRoutes(BaseModel):
                    enable: bool | None = Field(default=None)
                    inter_domain: bool | None = Field(default=None)

                encapsulation: str | None = Field(default=None)
                next_hop_self_source_interface: str | None = Field(default=None)
                next_hop_self_received_evpn_routes: NextHopSelfReceivedEvpnRoutes | None = Field(default=None)

            class PeerGroupsItem(BaseModel):
                name: str | None = Field(default=None)
                activate: bool | None = Field(default=None)
                route_map_in: str | None = Field(default=None)
                route_map_out: str | None = Field(default=None)
                domain_remote: bool | None = Field(default=None)
                encapsulation: str | None = Field(default=None)

            class EvpnHostflapDetection(BaseModel):
                enabled: bool | None = Field(default=None)
                window: int | None = Field(default=None)
                threshold: int | None = Field(default=None)
                expiry_timeout: int | None = Field(default=None)

            class Route(BaseModel):
                import_match_failure_action: str | None = Field(default=None)

            domain_identifier: str | None = Field(default=None)
            neighbor_default: NeighborDefault | None = Field(default=None)
            peer_groups: list[PeerGroupsItem] | None = Field(default=None)
            evpn_hostflap_detection: EvpnHostflapDetection | None = Field(default=None)
            route: Route | None = Field(default=None)

        class AddressFamilyRtc(BaseModel):
            class PeerGroupsItem(BaseModel):
                class DefaultRouteTarget(BaseModel):
                    only: bool | None = Field(default=None)
                    encoding_origin_as_omit: str | None = Field(default=None)

                name: str | None = Field(default=None)
                activate: bool | None = Field(default=None)
                default_route_target: DefaultRouteTarget | None = Field(default=None)

            peer_groups: list[PeerGroupsItem] | None = Field(default=None)

        class AddressFamilyIpv4(BaseModel):
            class NetworksItem(BaseModel):
                prefix: str | None = Field(default=None)
                route_map: str | None = Field(default=None)

            class PeerGroupsItem(BaseModel):
                class DefaultOriginate(BaseModel):
                    always: bool | None = Field(default=None)
                    route_map: str | None = Field(default=None)

                class NextHop(BaseModel):
                    class AddressFamilyIpv6(BaseModel):
                        enabled: bool = Field(default=None)
                        originate: bool | None = Field(default=None)

                    address_family_ipv6: AddressFamilyIpv6 | None = Field(default=None)
                    address_family_ipv6_originate: bool | None = Field(default=None)

                name: str | None = Field(default=None)
                activate: bool | None = Field(default=None)
                route_map_in: str | None = Field(default=None)
                route_map_out: str | None = Field(default=None)
                default_originate: DefaultOriginate | None = Field(default=None)
                next_hop: NextHop | None = Field(default=None)
                prefix_list_in: str | None = Field(default=None)
                prefix_list_out: str | None = Field(default=None)

            class NeighborsItem(BaseModel):
                class DefaultOriginate(BaseModel):
                    always: bool | None = Field(default=None)
                    route_map: str | None = Field(default=None)

                ip_address: str | None = Field(default=None)
                activate: bool | None = Field(default=None)
                route_map_in: str | None = Field(default=None)
                route_map_out: str | None = Field(default=None)
                prefix_list_in: str | None = Field(default=None)
                prefix_list_out: str | None = Field(default=None)
                default_originate: DefaultOriginate | None = Field(default=None)

            networks: list[NetworksItem] | None = Field(default=None)
            peer_groups: list[PeerGroupsItem] | None = Field(default=None)
            neighbors: list[NeighborsItem] | None = Field(default=None)

        class AddressFamilyIpv4Multicast(BaseModel):
            class PeerGroupsItem(BaseModel):
                name: str | None = Field(default=None)
                activate: bool | None = Field(default=None)
                route_map_in: str | None = Field(default=None)
                route_map_out: str | None = Field(default=None)

            class NeighborsItem(BaseModel):
                ip_address: str | None = Field(default=None)
                activate: bool | None = Field(default=None)
                route_map_in: str | None = Field(default=None)
                route_map_out: str | None = Field(default=None)

            class RedistributeRoutesItem(BaseModel):
                source_protocol: str | None = Field(default=None)
                route_map: str | None = Field(default=None)

            peer_groups: list[PeerGroupsItem] | None = Field(default=None)
            neighbors: list[NeighborsItem] | None = Field(default=None)
            redistribute_routes: list[RedistributeRoutesItem] | None = Field(default=None)

        class AddressFamilyIpv6(BaseModel):
            class NetworksItem(BaseModel):
                prefix: str | None = Field(default=None)
                route_map: str | None = Field(default=None)

            class PeerGroupsItem(BaseModel):
                name: str | None = Field(default=None)
                activate: bool | None = Field(default=None)
                route_map_in: str | None = Field(default=None)
                route_map_out: str | None = Field(default=None)
                prefix_list_in: str | None = Field(default=None)
                prefix_list_out: str | None = Field(default=None)

            class NeighborsItem(BaseModel):
                ip_address: str | None = Field(default=None)
                activate: bool | None = Field(default=None)
                route_map_in: str | None = Field(default=None)
                route_map_out: str | None = Field(default=None)
                prefix_list_in: str | None = Field(default=None)
                prefix_list_out: str | None = Field(default=None)

            class RedistributeRoutesItem(BaseModel):
                source_protocol: str | None = Field(default=None)
                route_map: str | None = Field(default=None)
                include_leaked: bool | None = Field(default=None)

            networks: list[NetworksItem] | None = Field(default=None)
            peer_groups: list[PeerGroupsItem] | None = Field(default=None)
            neighbors: list[NeighborsItem] | None = Field(default=None)
            redistribute_routes: list[RedistributeRoutesItem] | None = Field(default=None)

        class AddressFamilyIpv6Multicast(BaseModel):
            class Bgp(BaseModel):
                class MissingPolicy(BaseModel):
                    direction_in_action: str | None = Field(default=None)
                    direction_out_action: str | None = Field(default=None)

                class AdditionalPaths(BaseModel):
                    receive: bool | None = Field(default=None)

                missing_policy: MissingPolicy | None = Field(default=None)
                additional_paths: AdditionalPaths | None = Field(default=None)

            class NeighborsItem(BaseModel):
                ip_address: str | None = Field(default=None)
                activate: bool | None = Field(default=None)
                route_map_in: str | None = Field(default=None)
                route_map_out: str | None = Field(default=None)

            class PeerGroupsItem(BaseModel):
                name: str | None = Field(default=None)
                activate: bool | None = Field(default=None)

            class NetworksItem(BaseModel):
                prefix: str | None = Field(default=None)
                route_map: str | None = Field(default=None)

            bgp: Bgp | None = Field(default=None)
            neighbors: list[NeighborsItem] | None = Field(default=None)
            peer_groups: list[PeerGroupsItem] | None = Field(default=None)
            networks: list[NetworksItem] | None = Field(default=None)

        class AddressFamilyFlowSpecIpv4(BaseModel):
            class Bgp(BaseModel):
                class MissingPolicy(BaseModel):
                    direction_in_action: str | None = Field(default=None)
                    direction_out_action: str | None = Field(default=None)

                missing_policy: MissingPolicy | None = Field(default=None)

            class NeighborsItem(BaseModel):
                ip_address: str | None = Field(default=None)
                activate: bool | None = Field(default=None)

            class PeerGroupsItem(BaseModel):
                name: str | None = Field(default=None)
                activate: bool | None = Field(default=None)

            bgp: Bgp | None = Field(default=None)
            neighbors: list[NeighborsItem] | None = Field(default=None)
            peer_groups: list[PeerGroupsItem] | None = Field(default=None)

        class AddressFamilyFlowSpecIpv6(BaseModel):
            class Bgp(BaseModel):
                class MissingPolicy(BaseModel):
                    direction_in_action: str | None = Field(default=None)
                    direction_out_action: str | None = Field(default=None)

                missing_policy: MissingPolicy | None = Field(default=None)

            class NeighborsItem(BaseModel):
                ip_address: str | None = Field(default=None)
                activate: bool | None = Field(default=None)

            class PeerGroupsItem(BaseModel):
                name: str | None = Field(default=None)
                activate: bool | None = Field(default=None)

            bgp: Bgp | None = Field(default=None)
            neighbors: list[NeighborsItem] | None = Field(default=None)
            peer_groups: list[PeerGroupsItem] | None = Field(default=None)

        class AddressFamilyVpnIpv4(BaseModel):
            class PeerGroupsItem(BaseModel):
                name: str | None = Field(default=None)
                activate: bool | None = Field(default=None)
                route_map_in: str | None = Field(default=None)
                route_map_out: str | None = Field(default=None)

            class Route(BaseModel):
                import_match_failure_action: str | None = Field(default=None)

            class NeighborsItem(BaseModel):
                ip_address: str | None = Field(default=None)
                activate: bool | None = Field(default=None)
                route_map_in: str | None = Field(default=None)
                route_map_out: str | None = Field(default=None)

            class NeighborDefaultEncapsulationMplsNextHopSelf(BaseModel):
                source_interface: str | None = Field(default=None)

            domain_identifier: str | None = Field(default=None)
            peer_groups: list[PeerGroupsItem] | None = Field(default=None)
            route: Route | None = Field(default=None)
            neighbors: list[NeighborsItem] | None = Field(default=None)
            neighbor_default_encapsulation_mpls_next_hop_self: NeighborDefaultEncapsulationMplsNextHopSelf | None = Field(default=None)

        class AddressFamilyVpnIpv6(BaseModel):
            class PeerGroupsItem(BaseModel):
                name: str | None = Field(default=None)
                activate: bool | None = Field(default=None)
                route_map_in: str | None = Field(default=None)
                route_map_out: str | None = Field(default=None)

            class Route(BaseModel):
                import_match_failure_action: str | None = Field(default=None)

            class NeighborsItem(BaseModel):
                ip_address: str | None = Field(default=None)
                activate: bool | None = Field(default=None)
                route_map_in: str | None = Field(default=None)
                route_map_out: str | None = Field(default=None)

            class NeighborDefaultEncapsulationMplsNextHopSelf(BaseModel):
                source_interface: str | None = Field(default=None)

            domain_identifier: str | None = Field(default=None)
            peer_groups: list[PeerGroupsItem] | None = Field(default=None)
            route: Route | None = Field(default=None)
            neighbors: list[NeighborsItem] | None = Field(default=None)
            neighbor_default_encapsulation_mpls_next_hop_self: NeighborDefaultEncapsulationMplsNextHopSelf | None = Field(default=None)

        class VrfsItem(BaseModel):
            class EvpnMulticastAddressFamily(BaseModel):
                class Ipv4(BaseModel):
                    transit: bool | None = Field(default=None)

                ipv4: Ipv4 | None = Field(default=None)

            class RouteTargets(BaseModel):
                class ImportItem(BaseModel):
                    address_family: str | None = Field(default=None)
                    route_targets: list[str] | None = Field(default=None)

                class ExportItem(BaseModel):
                    address_family: str | None = Field(default=None)
                    route_targets: list[str] | None = Field(default=None)

                import_key: list[ImportItem] | None = Field(default=None, alias="import")
                export: list[ExportItem] | None = Field(default=None)

            class NetworksItem(BaseModel):
                prefix: str | None = Field(default=None)
                route_map: str | None = Field(default=None)

            class Updates(BaseModel):
                wait_for_convergence: bool | None = Field(default=None)
                wait_install: bool | None = Field(default=None)

            class ListenRangesItem(BaseModel):
                prefix: str | None = Field(default=None)
                peer_id_include_router_id: bool | None = Field(default=None)
                peer_group: str | None = Field(default=None)
                peer_filter: str | None = Field(default=None)
                remote_as: str | None = Field(default=None)

            class NeighborsItem(BaseModel):
                class RemovePrivateAs(BaseModel):
                    enabled: bool | None = Field(default=None)
                    all: bool | None = Field(default=None)
                    replace_as: bool | None = Field(default=None)

                class RemovePrivateAsIngress(BaseModel):
                    enabled: bool | None = Field(default=None)
                    replace_as: bool | None = Field(default=None)

                class AsPath(BaseModel):
                    remote_as_replace_out: bool | None = Field(default=None)
                    prepend_own_disabled: bool | None = Field(default=None)

                class RibInPrePolicyRetain(BaseModel):
                    enabled: bool | None = Field(default=None)
                    all: bool | None = Field(default=None)

                class AllowasIn(BaseModel):
                    enabled: bool | None = Field(default=None)
                    times: int | None = Field(default=None)

                class DefaultOriginate(BaseModel):
                    enabled: bool | None = Field(default=None)
                    always: bool | None = Field(default=None)
                    route_map: str | None = Field(default=None)

                ip_address: str | None = Field(default=None)
                peer_group: str | None = Field(default=None)
                remote_as: str | None = Field(default=None)
                password: str | None = Field(default=None)
                passive: bool | None = Field(default=None)
                remove_private_as: RemovePrivateAs | None = Field(default=None)
                remove_private_as_ingress: RemovePrivateAsIngress | None = Field(default=None)
                weight: int | None = Field(default=None)
                local_as: str | None = Field(default=None)
                as_path: AsPath | None = Field(default=None)
                description: str | None = Field(default=None)
                route_reflector_client: bool | None = Field(default=None)
                ebgp_multihop: int | None = Field(default=None)
                next_hop_self: bool | None = Field(default=None)
                shutdown: bool | None = Field(default=None)
                bfd: bool | None = Field(default=None)
                timers: str | None = Field(default=None)
                rib_in_pre_policy_retain: RibInPrePolicyRetain | None = Field(default=None)
                send_community: str | None = Field(default=None)
                maximum_routes: int | None = Field(default=None)
                maximum_routes_warning_limit: str | None = Field(default=None)
                maximum_routes_warning_only: bool | None = Field(default=None)
                allowas_in: AllowasIn | None = Field(default=None)
                default_originate: DefaultOriginate | None = Field(default=None)
                update_source: str | None = Field(default=None)
                route_map_in: str | None = Field(default=None)
                route_map_out: str | None = Field(default=None)
                prefix_list_in: str | None = Field(default=None)
                prefix_list_out: str | None = Field(default=None)

            class NeighborInterfacesItem(BaseModel):
                name: str | None = Field(default=None)
                remote_as: str | None = Field(default=None)
                peer_group: str | None = Field(default=None)
                peer_filter: str | None = Field(default=None)
                description: str | None = Field(default=None)

            class RedistributeRoutesItem(BaseModel):
                source_protocol: str | None = Field(default=None)
                route_map: str | None = Field(default=None)
                include_leaked: bool | None = Field(default=None)

            class AggregateAddressesItem(BaseModel):
                prefix: str | None = Field(default=None)
                advertise_only: bool | None = Field(default=None)
                as_set: bool | None = Field(default=None)
                summary_only: bool | None = Field(default=None)
                attribute_map: str | None = Field(default=None)
                match_map: str | None = Field(default=None)

            class AddressFamilyIpv4(BaseModel):
                class Bgp(BaseModel):
                    class MissingPolicy(BaseModel):
                        direction_in_action: str | None = Field(default=None)
                        direction_out_action: str | None = Field(default=None)

                    class AdditionalPaths(BaseModel):
                        class Send(BaseModel):
                            any: bool | None = Field(default=None)
                            backup: bool | None = Field(default=None)
                            ecmp: bool | None = Field(default=None)
                            ecmp_limit: int | None = Field(default=None)
                            limit: int | None = Field(default=None)

                        install: bool | None = Field(default=None)
                        install_ecmp_primary: bool | None = Field(default=None)
                        receive: bool | None = Field(default=None)
                        send: Send | None = Field(default=None)

                    missing_policy: MissingPolicy | None = Field(default=None)
                    additional_paths: AdditionalPaths | None = Field(default=None)

                class NeighborsItem(BaseModel):
                    class NextHop(BaseModel):
                        class AddressFamilyIpv6(BaseModel):
                            enabled: bool = Field(default=None)
                            originate: bool | None = Field(default=None)

                        address_family_ipv6: AddressFamilyIpv6 | None = Field(default=None)

                    ip_address: str | None = Field(default=None)
                    activate: bool | None = Field(default=None)
                    route_map_in: str | None = Field(default=None)
                    route_map_out: str | None = Field(default=None)
                    next_hop: NextHop | None = Field(default=None)

                class NetworksItem(BaseModel):
                    prefix: str | None = Field(default=None)
                    route_map: str | None = Field(default=None)

                bgp: Bgp | None = Field(default=None)
                neighbors: list[NeighborsItem] | None = Field(default=None)
                networks: list[NetworksItem] | None = Field(default=None)

            class AddressFamilyIpv6(BaseModel):
                class Bgp(BaseModel):
                    class MissingPolicy(BaseModel):
                        direction_in_action: str | None = Field(default=None)
                        direction_out_action: str | None = Field(default=None)

                    class AdditionalPaths(BaseModel):
                        class Send(BaseModel):
                            any: bool | None = Field(default=None)
                            backup: bool | None = Field(default=None)
                            ecmp: bool | None = Field(default=None)
                            ecmp_limit: int | None = Field(default=None)
                            limit: int | None = Field(default=None)

                        install: bool | None = Field(default=None)
                        install_ecmp_primary: bool | None = Field(default=None)
                        receive: bool | None = Field(default=None)
                        send: Send | None = Field(default=None)

                    missing_policy: MissingPolicy | None = Field(default=None)
                    additional_paths: AdditionalPaths | None = Field(default=None)

                class NeighborsItem(BaseModel):
                    ip_address: str | None = Field(default=None)
                    activate: bool | None = Field(default=None)
                    route_map_in: str | None = Field(default=None)
                    route_map_out: str | None = Field(default=None)

                class NetworksItem(BaseModel):
                    prefix: str | None = Field(default=None)
                    route_map: str | None = Field(default=None)

                bgp: Bgp | None = Field(default=None)
                neighbors: list[NeighborsItem] | None = Field(default=None)
                networks: list[NetworksItem] | None = Field(default=None)

            class AddressFamilyIpv4Multicast(BaseModel):
                class Bgp(BaseModel):
                    class MissingPolicy(BaseModel):
                        direction_in_action: str | None = Field(default=None)
                        direction_out_action: str | None = Field(default=None)

                    class AdditionalPaths(BaseModel):
                        receive: bool | None = Field(default=None)

                    missing_policy: MissingPolicy | None = Field(default=None)
                    additional_paths: AdditionalPaths | None = Field(default=None)

                class NeighborsItem(BaseModel):
                    ip_address: str | None = Field(default=None)
                    activate: bool | None = Field(default=None)
                    route_map_in: str | None = Field(default=None)
                    route_map_out: str | None = Field(default=None)

                class NetworksItem(BaseModel):
                    prefix: str | None = Field(default=None)
                    route_map: str | None = Field(default=None)

                bgp: Bgp | None = Field(default=None)
                neighbors: list[NeighborsItem] | None = Field(default=None)
                networks: list[NetworksItem] | None = Field(default=None)

            class AddressFamilyIpv6Multicast(BaseModel):
                class Bgp(BaseModel):
                    class MissingPolicy(BaseModel):
                        direction_in_action: str | None = Field(default=None)
                        direction_out_action: str | None = Field(default=None)

                    class AdditionalPaths(BaseModel):
                        receive: bool | None = Field(default=None)

                    missing_policy: MissingPolicy | None = Field(default=None)
                    additional_paths: AdditionalPaths | None = Field(default=None)

                class NeighborsItem(BaseModel):
                    ip_address: str | None = Field(default=None)
                    activate: bool | None = Field(default=None)
                    route_map_in: str | None = Field(default=None)
                    route_map_out: str | None = Field(default=None)

                class NetworksItem(BaseModel):
                    prefix: str | None = Field(default=None)
                    route_map: str | None = Field(default=None)

                bgp: Bgp | None = Field(default=None)
                neighbors: list[NeighborsItem] | None = Field(default=None)
                networks: list[NetworksItem] | None = Field(default=None)

            class AddressFamilyFlowSpecIpv4(BaseModel):
                class Bgp(BaseModel):
                    class MissingPolicy(BaseModel):
                        direction_in_action: str | None = Field(default=None)
                        direction_out_action: str | None = Field(default=None)

                    missing_policy: MissingPolicy | None = Field(default=None)

                class NeighborsItem(BaseModel):
                    ip_address: str | None = Field(default=None)
                    activate: bool | None = Field(default=None)

                bgp: Bgp | None = Field(default=None)
                neighbors: list[NeighborsItem] | None = Field(default=None)

            class AddressFamilyFlowSpecIpv6(BaseModel):
                class Bgp(BaseModel):
                    class MissingPolicy(BaseModel):
                        direction_in_action: str | None = Field(default=None)
                        direction_out_action: str | None = Field(default=None)

                    missing_policy: MissingPolicy | None = Field(default=None)

                class NeighborsItem(BaseModel):
                    ip_address: str | None = Field(default=None)
                    activate: bool | None = Field(default=None)

                bgp: Bgp | None = Field(default=None)
                neighbors: list[NeighborsItem] | None = Field(default=None)

            class AddressFamiliesItem(BaseModel):
                class Bgp(BaseModel):
                    class MissingPolicy(BaseModel):
                        direction_in_action: str | None = Field(default=None)
                        direction_out_action: str | None = Field(default=None)

                    missing_policy: MissingPolicy | None = Field(default=None)
                    additional_paths: list[str] | None = Field(default=None)

                class NeighborsItem(BaseModel):
                    ip_address: str | None = Field(default=None)
                    activate: bool | None = Field(default=None)
                    route_map_in: str | None = Field(default=None)
                    route_map_out: str | None = Field(default=None)

                class PeerGroupsItem(BaseModel):
                    class NextHop(BaseModel):
                        address_family_ipv6_originate: bool | None = Field(default=None)

                    name: str | None = Field(default=None)
                    activate: bool | None = Field(default=None)
                    next_hop: NextHop | None = Field(default=None)

                class NetworksItem(BaseModel):
                    prefix: str | None = Field(default=None)
                    route_map: str | None = Field(default=None)

                address_family: str | None = Field(default=None)
                bgp: Bgp | None = Field(default=None)
                neighbors: list[NeighborsItem] | None = Field(default=None)
                peer_groups: list[PeerGroupsItem] | None = Field(default=None)
                networks: list[NetworksItem] | None = Field(default=None)

            name: str | None = Field(default=None)
            rd: str | None = Field(default=None)
            evpn_multicast: bool | None = Field(default=None)
            evpn_multicast_address_family: EvpnMulticastAddressFamily | None = Field(default=None)
            route_targets: RouteTargets | None = Field(default=None)
            router_id: str | None = Field(default=None)
            timers: str | None = Field(default=None)
            networks: list[NetworksItem] | None = Field(default=None)
            updates: Updates | None = Field(default=None)
            listen_ranges: list[ListenRangesItem] | None = Field(default=None)
            neighbors: list[NeighborsItem] | None = Field(default=None)
            neighbor_interfaces: list[NeighborInterfacesItem] | None = Field(default=None)
            redistribute_routes: list[RedistributeRoutesItem] | None = Field(default=None)
            aggregate_addresses: list[AggregateAddressesItem] | None = Field(default=None)
            address_family_ipv4: AddressFamilyIpv4 | None = Field(default=None)
            address_family_ipv6: AddressFamilyIpv6 | None = Field(default=None)
            address_family_ipv4_multicast: AddressFamilyIpv4Multicast | None = Field(default=None)
            address_family_ipv6_multicast: AddressFamilyIpv6Multicast | None = Field(default=None)
            address_family_flow_spec_ipv4: AddressFamilyFlowSpecIpv4 | None = Field(default=None)
            address_family_flow_spec_ipv6: AddressFamilyFlowSpecIpv6 | None = Field(default=None)
            address_families: list[AddressFamiliesItem] | None = Field(default=None)
            eos_cli: str | None = Field(default=None)

        class SessionTrackersItem(BaseModel):
            name: str | None = Field(default=None)
            recovery_delay: int | None = Field(default=None)

        as_key: str | None = Field(default=None, alias="as")
        router_id: str | None = Field(default=None)
        distance: Distance | None = Field(default=None)
        graceful_restart: GracefulRestart | None = Field(default=None)
        graceful_restart_helper: GracefulRestartHelper | None = Field(default=None)
        maximum_paths: MaximumPaths | None = Field(default=None)
        updates: Updates | None = Field(default=None)
        bgp_cluster_id: str | None = Field(default=None)
        bgp_defaults: list[str] | None = Field(default=None)
        bgp: Bgp | None = Field(default=None)
        listen_ranges: list[ListenRangesItem] | None = Field(default=None)
        peer_groups: list[PeerGroupsItem] | None = Field(default=None)
        neighbors: list[NeighborsItem] | None = Field(default=None)
        neighbor_interfaces: list[NeighborInterfacesItem] | None = Field(default=None)
        aggregate_addresses: list[AggregateAddressesItem] | None = Field(default=None)
        redistribute_routes: list[RedistributeRoutesItem] | None = Field(default=None)
        vlan_aware_bundles: list[VlanAwareBundlesItem] | None = Field(default=None)
        vlans: list[VlansItem] | None = Field(default=None)
        vpws: list[VpwsItem] | None = Field(default=None)
        address_family_evpn: AddressFamilyEvpn | None = Field(default=None)
        address_family_rtc: AddressFamilyRtc | None = Field(default=None)
        address_family_ipv4: AddressFamilyIpv4 | None = Field(default=None)
        address_family_ipv4_multicast: AddressFamilyIpv4Multicast | None = Field(default=None)
        address_family_ipv6: AddressFamilyIpv6 | None = Field(default=None)
        address_family_ipv6_multicast: AddressFamilyIpv6Multicast | None = Field(default=None)
        address_family_flow_spec_ipv4: AddressFamilyFlowSpecIpv4 | None = Field(default=None)
        address_family_flow_spec_ipv6: AddressFamilyFlowSpecIpv6 | None = Field(default=None)
        address_family_vpn_ipv4: AddressFamilyVpnIpv4 | None = Field(default=None)
        address_family_vpn_ipv6: AddressFamilyVpnIpv6 | None = Field(default=None)
        vrfs: list[VrfsItem] | None = Field(default=None)
        session_trackers: list[SessionTrackersItem] | None = Field(default=None)

    class RouterGeneral(BaseModel):
        class RouterId(BaseModel):
            ipv4: str | None = Field(default=None)
            ipv6: str | None = Field(default=None)

        class VrfsItem(BaseModel):
            class LeakRoutesItem(BaseModel):
                source_vrf: str | None = Field(default=None)
                subscribe_policy: str | None = Field(default=None)

            class Routes(BaseModel):
                class DynamicPrefixListsItem(BaseModel):
                    name: str | None = Field(default=None)

                dynamic_prefix_lists: list[DynamicPrefixListsItem] | None = Field(default=None)

            name: str | None = Field(default=None)
            leak_routes: list[LeakRoutesItem] | None = Field(default=None)
            routes: Routes | None = Field(default=None)

        router_id: RouterId | None = Field(default=None)
        nexthop_fast_failover: bool = Field(default=False)
        vrfs: list[VrfsItem] | None = Field(default=None)

    class RouterIgmp(BaseModel):
        ssm_aware: bool | None = Field(default=None)

    class RouterIsis(BaseModel):
        class Timers(BaseModel):
            class LocalConvergence(BaseModel):
                protected_prefixes: bool | None = Field(default=None)
                delay: int = Field(default=10000)

            local_convergence: LocalConvergence | None = Field(default=None)

        class Advertise(BaseModel):
            passive_only: bool | None = Field(default=None)

        class RedistributeRoutesItem(BaseModel):
            source_protocol: str = Field(default=None)
            route_map: str | None = Field(default=None)
            include_leaked: bool | None = Field(default=None)
            ospf_route_type: str | None = Field(default=None)

        class AddressFamilyIpv4(BaseModel):
            class FastRerouteTiLfa(BaseModel):
                class Srlg(BaseModel):
                    enable: bool | None = Field(default=None)
                    strict: bool | None = Field(default=None)

                mode: str | None = Field(default=None)
                level: str | None = Field(default=None)
                srlg: Srlg | None = Field(default=None)

            class TunnelSourceLabeledUnicast(BaseModel):
                enabled: bool | None = Field(default=None)
                rcf: str | None = Field(default=None)

            enabled: bool | None = Field(default=None)
            maximum_paths: int | None = Field(default=None)
            fast_reroute_ti_lfa: FastRerouteTiLfa | None = Field(default=None)
            tunnel_source_labeled_unicast: TunnelSourceLabeledUnicast | None = Field(default=None)

        class AddressFamilyIpv6(BaseModel):
            class FastRerouteTiLfa(BaseModel):
                class Srlg(BaseModel):
                    enable: bool | None = Field(default=None)
                    strict: bool | None = Field(default=None)

                mode: str | None = Field(default=None)
                level: str | None = Field(default=None)
                srlg: Srlg | None = Field(default=None)

            enabled: bool | None = Field(default=None)
            maximum_paths: int | None = Field(default=None)
            fast_reroute_ti_lfa: FastRerouteTiLfa | None = Field(default=None)

        class SegmentRoutingMpls(BaseModel):
            class PrefixSegmentsItem(BaseModel):
                prefix: str | None = Field(default=None)
                index: int | None = Field(default=None)

            enabled: bool | None = Field(default=None)
            router_id: str | None = Field(default=None)
            prefix_segments: list[PrefixSegmentsItem] | None = Field(default=None)

        instance: str = Field(default=None)
        net: str | None = Field(default=None)
        router_id: str | None = Field(default=None)
        is_type: str | None = Field(default=None)
        log_adjacency_changes: bool | None = Field(default=None)
        mpls_ldp_sync_default: bool | None = Field(default=None)
        timers: Timers | None = Field(default=None)
        advertise: Advertise | None = Field(default=None)
        address_family: list[str] | None = Field(default=None)
        isis_af_defaults: list[str] | None = Field(default=None)
        redistribute_routes: list[RedistributeRoutesItem] | None = Field(default=None)
        address_family_ipv4: AddressFamilyIpv4 | None = Field(default=None)
        address_family_ipv6: AddressFamilyIpv6 | None = Field(default=None)
        segment_routing_mpls: SegmentRoutingMpls | None = Field(default=None)

    class RouterL2Vpn(BaseModel):
        class ArpProxy(BaseModel):
            prefix_list: str | None = Field(default=None)

        class NdProxy(BaseModel):
            prefix_list: str | None = Field(default=None)

        arp_learning_bridged: bool | None = Field(default=None)
        arp_proxy: ArpProxy | None = Field(default=None)
        arp_selective_install: bool | None = Field(default=None)
        nd_learning_bridged: bool | None = Field(default=None)
        nd_proxy: NdProxy | None = Field(default=None)
        nd_rs_flooding_disabled: bool | None = Field(default=None)
        virtual_router_nd_ra_flooding_disabled: bool | None = Field(default=None)

    class RouterMsdp(BaseModel):
        class GroupLimitsItem(BaseModel):
            source_prefix: str | None = Field(default=None)
            limit: int = Field(default=None)

        class PeersItem(BaseModel):
            class DefaultPeer(BaseModel):
                enabled: bool | None = Field(default=None)
                prefix_list: str | None = Field(default=None)

            class MeshGroupsItem(BaseModel):
                name: str | None = Field(default=None)

            class Keepalive(BaseModel):
                keepalive_timer: int = Field(default=None)
                hold_timer: int = Field(default=None)

            class SaFilter(BaseModel):
                in_list: str | None = Field(default=None)
                out_list: str | None = Field(default=None)

            ipv4_address: str | None = Field(default=None)
            default_peer: DefaultPeer | None = Field(default=None)
            local_interface: str | None = Field(default=None)
            description: str | None = Field(default=None)
            disabled: bool | None = Field(default=None)
            sa_limit: int | None = Field(default=None)
            mesh_groups: list[MeshGroupsItem] | None = Field(default=None)
            keepalive: Keepalive | None = Field(default=None)
            sa_filter: SaFilter | None = Field(default=None)

        class VrfsItem(BaseModel):
            class GroupLimitsItem(BaseModel):
                source_prefix: str | None = Field(default=None)
                limit: int = Field(default=None)

            class PeersItem(BaseModel):
                class DefaultPeer(BaseModel):
                    enabled: bool | None = Field(default=None)
                    prefix_list: str | None = Field(default=None)

                class MeshGroupsItem(BaseModel):
                    name: str | None = Field(default=None)

                class Keepalive(BaseModel):
                    keepalive_timer: int = Field(default=None)
                    hold_timer: int = Field(default=None)

                class SaFilter(BaseModel):
                    in_list: str | None = Field(default=None)
                    out_list: str | None = Field(default=None)

                ipv4_address: str | None = Field(default=None)
                default_peer: DefaultPeer | None = Field(default=None)
                local_interface: str | None = Field(default=None)
                description: str | None = Field(default=None)
                disabled: bool | None = Field(default=None)
                sa_limit: int | None = Field(default=None)
                mesh_groups: list[MeshGroupsItem] | None = Field(default=None)
                keepalive: Keepalive | None = Field(default=None)
                sa_filter: SaFilter | None = Field(default=None)

            name: str | None = Field(default=None)
            originator_id_local_interface: str | None = Field(default=None)
            rejected_limit: int | None = Field(default=None)
            forward_register_packets: bool | None = Field(default=None)
            connection_retry_interval: int | None = Field(default=None)
            group_limits: list[GroupLimitsItem] | None = Field(default=None)
            peers: list[PeersItem] | None = Field(default=None)

        originator_id_local_interface: str | None = Field(default=None)
        rejected_limit: int | None = Field(default=None)
        forward_register_packets: bool | None = Field(default=None)
        connection_retry_interval: int | None = Field(default=None)
        group_limits: list[GroupLimitsItem] | None = Field(default=None)
        peers: list[PeersItem] | None = Field(default=None)
        vrfs: list[VrfsItem] | None = Field(default=None)

    class RouterMulticast(BaseModel):
        class Ipv4(BaseModel):
            class Counters(BaseModel):
                rate_period_decay: int | None = Field(default=None)

            class Rpf(BaseModel):
                class RoutesItem(BaseModel):
                    class DestinationsItem(BaseModel):
                        nexthop: str = Field(default=None)
                        distance: int | None = Field(default=None)

                    source_prefix: str = Field(default=None)
                    destinations: list[DestinationsItem] = Field(default=None)

                routes: list[RoutesItem] | None = Field(default=None)

            counters: Counters | None = Field(default=None)
            routing: bool | None = Field(default=None)
            multipath: str | None = Field(default=None)
            software_forwarding: str | None = Field(default=None)
            rpf: Rpf | None = Field(default=None)

        class VrfsItem(BaseModel):
            class Ipv4(BaseModel):
                routing: bool | None = Field(default=None)

            name: str | None = Field(default=None)
            ipv4: Ipv4 | None = Field(default=None)

        ipv4: Ipv4 | None = Field(default=None)
        vrfs: list[VrfsItem] | None = Field(default=None)

    class RouterOspf(BaseModel):
        class ProcessIdsItem(BaseModel):
            class Distance(BaseModel):
                external: int | None = Field(default=None)
                inter_area: int | None = Field(default=None)
                intra_area: int | None = Field(default=None)

            class NetworkPrefixesItem(BaseModel):
                ipv4_prefix: str | None = Field(default=None)
                area: str | None = Field(default=None)

            class DistributeListIn(BaseModel):
                route_map: str | None = Field(default=None)

            class Timers(BaseModel):
                class Lsa(BaseModel):
                    class TxDelay(BaseModel):
                        initial: int | None = Field(default=None)
                        min: int | None = Field(default=None)
                        max: int | None = Field(default=None)

                    rx_min_interval: int | None = Field(default=None)
                    tx_delay: TxDelay | None = Field(default=None)

                class SpfDelay(BaseModel):
                    initial: int | None = Field(default=None)
                    min: int | None = Field(default=None)
                    max: int | None = Field(default=None)

                lsa: Lsa | None = Field(default=None)
                spf_delay: SpfDelay | None = Field(default=None)

            class DefaultInformationOriginate(BaseModel):
                always: bool | None = Field(default=None)
                metric: int | None = Field(default=None)
                metric_type: int | None = Field(default=None)

            class SummaryAddressesItem(BaseModel):
                prefix: str | None = Field(default=None)
                tag: int | None = Field(default=None)
                attribute_map: str | None = Field(default=None)
                not_advertise: bool | None = Field(default=None)

            class Redistribute(BaseModel):
                class Static(BaseModel):
                    route_map: str | None = Field(default=None)
                    include_leaked: bool | None = Field(default=None)

                class Connected(BaseModel):
                    route_map: str | None = Field(default=None)
                    include_leaked: bool | None = Field(default=None)

                class Bgp(BaseModel):
                    route_map: str | None = Field(default=None)
                    include_leaked: bool | None = Field(default=None)

                static: Static | None = Field(default=None)
                connected: Connected | None = Field(default=None)
                bgp: Bgp | None = Field(default=None)

            class AreasItem(BaseModel):
                class Filter(BaseModel):
                    networks: list[str] | None = Field(default=None)
                    prefix_list: str | None = Field(default=None)

                class DefaultInformationOriginate(BaseModel):
                    metric: int | None = Field(default=None)
                    metric_type: int | None = Field(default=None)

                id: str | None = Field(default=None)
                filter: Filter | None = Field(default=None)
                type: str = Field(default="normal")
                no_summary: bool | None = Field(default=None)
                nssa_only: bool | None = Field(default=None)
                default_information_originate: DefaultInformationOriginate | None = Field(default=None)

            class MaxMetric(BaseModel):
                class RouterLsa(BaseModel):
                    class ExternalLsa(BaseModel):
                        override_metric: int | None = Field(default=None)

                    class SummaryLsa(BaseModel):
                        override_metric: int | None = Field(default=None)

                    external_lsa: ExternalLsa | None = Field(default=None)
                    include_stub: bool | None = Field(default=None)
                    on_startup: str | None = Field(default=None)
                    summary_lsa: SummaryLsa | None = Field(default=None)

                router_lsa: RouterLsa | None = Field(default=None)

            id: int | None = Field(default=None)
            vrf: str | None = Field(default=None)
            passive_interface_default: bool | None = Field(default=None)
            router_id: str | None = Field(default=None)
            distance: Distance | None = Field(default=None)
            log_adjacency_changes_detail: bool | None = Field(default=None)
            network_prefixes: list[NetworkPrefixesItem] | None = Field(default=None)
            bfd_enable: bool | None = Field(default=None)
            bfd_adjacency_state_any: bool | None = Field(default=None)
            no_passive_interfaces: list[str] | None = Field(default=None)
            distribute_list_in: DistributeListIn | None = Field(default=None)
            max_lsa: int | None = Field(default=None)
            timers: Timers | None = Field(default=None)
            default_information_originate: DefaultInformationOriginate | None = Field(default=None)
            summary_addresses: list[SummaryAddressesItem] | None = Field(default=None)
            redistribute: Redistribute | None = Field(default=None)
            auto_cost_reference_bandwidth: int | None = Field(default=None)
            areas: list[AreasItem] | None = Field(default=None)
            maximum_paths: int | None = Field(default=None)
            max_metric: MaxMetric | None = Field(default=None)
            mpls_ldp_sync_default: bool | None = Field(default=None)
            eos_cli: str | None = Field(default=None)

        process_ids: list[ProcessIdsItem] | None = Field(default=None)

    class RouterPimSparseMode(BaseModel):
        class Ipv4(BaseModel):
            class RpAddressesItem(BaseModel):
                address: str | None = Field(default=None)
                groups: list[str] | None = Field(default=None)
                access_lists: list[str] | None = Field(default=None)
                priority: int | None = Field(default=None)
                hashmask: int | None = Field(default=None)
                override: bool | None = Field(default=None)

            class AnycastRpsItem(BaseModel):
                class OtherAnycastRpAddressesItem(BaseModel):
                    address: str | None = Field(default=None)
                    register_count: int | None = Field(default=None)

                address: str | None = Field(default=None)
                other_anycast_rp_addresses: list[OtherAnycastRpAddressesItem] | None = Field(default=None)

            bfd: bool | None = Field(default=None)
            ssm_range: str | None = Field(default=None)
            rp_addresses: list[RpAddressesItem] | None = Field(default=None)
            anycast_rps: list[AnycastRpsItem] | None = Field(default=None)

        class VrfsItem(BaseModel):
            class Ipv4(BaseModel):
                class RpAddressesItem(BaseModel):
                    address: str = Field(default=None)
                    groups: list[str] | None = Field(default=None)
                    access_lists: list[str] | None = Field(default=None)
                    priority: int | None = Field(default=None)
                    hashmask: int | None = Field(default=None)
                    override: bool | None = Field(default=None)

                bfd: bool | None = Field(default=None)
                rp_addresses: list[RpAddressesItem] | None = Field(default=None)

            name: str | None = Field(default=None)
            ipv4: Ipv4 | None = Field(default=None)

        ipv4: Ipv4 | None = Field(default=None)
        vrfs: list[VrfsItem] | None = Field(default=None)

    class RouterTrafficEngineering(BaseModel):
        class RouterId(BaseModel):
            ipv4: str | None = Field(default=None)
            ipv6: str | None = Field(default=None)

        class SegmentRouting(BaseModel):
            class PolicyEndpointsItem(BaseModel):
                class ColorsItem(BaseModel):
                    class PathGroupItem(BaseModel):
                        class SegmentListItem(BaseModel):
                            label_stack: str | None = Field(default=None)
                            weight: int | None = Field(default=None)
                            index: int | None = Field(default=None)

                        preference: int | None = Field(default=None)
                        explicit_null: str | None = Field(default=None)
                        segment_list: list[SegmentListItem] | None = Field(default=None)

                    value: int | None = Field(default=None)
                    binding_sid: int | None = Field(default=None)
                    description: str | None = Field(default=None)
                    name: str | None = Field(default=None)
                    sbfd_remote_discriminator: str | None = Field(default=None)
                    path_group: list[PathGroupItem] | None = Field(default=None)

                address: str | None = Field(default=None)
                colors: list[ColorsItem] | None = Field(default=None)

            colored_tunnel_rib: bool | None = Field(default=None)
            policy_endpoints: list[PolicyEndpointsItem] | None = Field(default=None)

        router_id: RouterId | None = Field(default=None)
        segment_routing: SegmentRouting | None = Field(default=None)

    class ServiceRoutingConfigurationBgp(BaseModel):
        no_equals_default: bool | None = Field(default=None)

    class ServiceUnsupportedTransceiver(BaseModel):
        license_name: str | None = Field(default=None)
        license_key: str | None = Field(default=None)

    class Sflow(BaseModel):
        class VrfsItem(BaseModel):
            class DestinationsItem(BaseModel):
                destination: str | None = Field(default=None)
                port: int | None = Field(default=None)

            name: str | None = Field(default=None)
            destinations: list[DestinationsItem] | None = Field(default=None)
            source: str | None = Field(default=None)
            source_interface: str | None = Field(default=None)

        class DestinationsItem(BaseModel):
            destination: str | None = Field(default=None)
            port: int | None = Field(default=None)

        class ExtensionsItem(BaseModel):
            name: str | None = Field(default=None)
            enabled: bool = Field(default=None)

        class Interface(BaseModel):
            class Disable(BaseModel):
                default: bool | None = Field(default=None)

            class Egress(BaseModel):
                enable_default: bool | None = Field(default=None)
                unmodified: bool | None = Field(default=None)

            disable: Disable | None = Field(default=None)
            egress: Egress | None = Field(default=None)

        class HardwareAcceleration(BaseModel):
            class ModulesItem(BaseModel):
                name: str | None = Field(default=None)
                enabled: bool = Field(default=True)

            enabled: bool | None = Field(default=None)
            sample: int | None = Field(default=None)
            modules: list[ModulesItem] | None = Field(default=None)

        sample: int | None = Field(default=None)
        dangerous: bool | None = Field(default=None)
        polling_interval: int | None = Field(default=None)
        vrfs: list[VrfsItem] | None = Field(default=None)
        destinations: list[DestinationsItem] | None = Field(default=None)
        source: str | None = Field(default=None)
        source_interface: str | None = Field(default=None)
        extensions: list[ExtensionsItem] | None = Field(default=None)
        interface: Interface | None = Field(default=None)
        run: bool | None = Field(default=None)
        hardware_acceleration: HardwareAcceleration | None = Field(default=None)

    class SnmpServer(BaseModel):
        class EngineIds(BaseModel):
            class RemotesItem(BaseModel):
                id: str | None = Field(default=None)
                address: str | None = Field(default=None)
                udp_port: int | None = Field(default=None)

            local: str | None = Field(default=None)
            remotes: list[RemotesItem] | None = Field(default=None)

        class CommunitiesItem(BaseModel):
            class AccessListIpv4(BaseModel):
                name: str | None = Field(default=None)

            class AccessListIpv6(BaseModel):
                name: str | None = Field(default=None)

            name: str | None = Field(default=None)
            access: str | None = Field(default=None)
            access_list_ipv4: AccessListIpv4 | None = Field(default=None)
            access_list_ipv6: AccessListIpv6 | None = Field(default=None)
            view: str | None = Field(default=None)

        class Ipv4AclsItem(BaseModel):
            name: str | None = Field(default=None)
            vrf: str | None = Field(default=None)

        class Ipv6AclsItem(BaseModel):
            name: str | None = Field(default=None)
            vrf: str | None = Field(default=None)

        class LocalInterfacesItem(BaseModel):
            name: str | None = Field(default=None)
            vrf: str | None = Field(default=None)

        class ViewsItem(BaseModel):
            name: str | None = Field(default=None)
            mib_family_name: str | None = Field(default=None)
            included: bool | None = Field(default=None)
            MIB_family_name_key: str | None = Field(default=None, alias="MIB_family_name")

        class GroupsItem(BaseModel):
            name: str | None = Field(default=None)
            version: str | None = Field(default=None)
            authentication: str | None = Field(default=None)
            read: str | None = Field(default=None)
            write: str | None = Field(default=None)
            notify: str | None = Field(default=None)

        class UsersItem(BaseModel):
            name: str | None = Field(default=None)
            group: str | None = Field(default=None)
            remote_address: str | None = Field(default=None)
            udp_port: int | None = Field(default=None)
            version: str | None = Field(default=None)
            localized: str | None = Field(default=None)
            auth: str | None = Field(default=None)
            auth_passphrase: str | None = Field(default=None)
            priv: str | None = Field(default=None)
            priv_passphrase: str | None = Field(default=None)

        class HostsItem(BaseModel):
            class UsersItem(BaseModel):
                username: str | None = Field(default=None)
                authentication_level: str | None = Field(default=None)

            host: str | None = Field(default=None)
            vrf: str | None = Field(default=None)
            version: str | None = Field(default=None)
            community: str | None = Field(default=None)
            users: list[UsersItem] | None = Field(default=None)

        class Traps(BaseModel):
            class SnmpTrapsItem(BaseModel):
                name: str | None = Field(default=None)
                enabled: bool = Field(default=True)

            enable: bool = Field(default=False)
            snmp_traps: list[SnmpTrapsItem] | None = Field(default=None)

        class VrfsItem(BaseModel):
            name: str | None = Field(default=None)
            enable: bool | None = Field(default=None)

        engine_ids: EngineIds | None = Field(default=None)
        contact: str | None = Field(default=None)
        location: str | None = Field(default=None)
        communities: list[CommunitiesItem] | None = Field(default=None)
        ipv4_acls: list[Ipv4AclsItem] | None = Field(default=None)
        ipv6_acls: list[Ipv6AclsItem] | None = Field(default=None)
        local_interfaces: list[LocalInterfacesItem] | None = Field(default=None)
        views: list[ViewsItem] | None = Field(default=None)
        groups: list[GroupsItem] | None = Field(default=None)
        users: list[UsersItem] | None = Field(default=None)
        hosts: list[HostsItem] | None = Field(default=None)
        traps: Traps | None = Field(default=None)
        vrfs: list[VrfsItem] | None = Field(default=None)

    class SpanningTree(BaseModel):
        class EdgePort(BaseModel):
            bpdufilter_default: bool | None = Field(default=None)
            bpduguard_default: bool | None = Field(default=None)

        class BpduguardRateLimit(BaseModel):
            default: bool | None = Field(default=None)
            count: int | None = Field(default=None)

        class Mst(BaseModel):
            class Configuration(BaseModel):
                class InstancesItem(BaseModel):
                    id: int | None = Field(default=None)
                    vlans: str | None = Field(default=None)

                name: str | None = Field(default=None)
                revision: int | None = Field(default=None)
                instances: list[InstancesItem] | None = Field(default=None)

            pvst_border: bool | None = Field(default=None)
            configuration: Configuration | None = Field(default=None)

        class MstInstancesItem(BaseModel):
            id: str | None = Field(default=None)
            priority: int | None = Field(default=None)

        class RapidPvstInstancesItem(BaseModel):
            id: str | None = Field(default=None)
            priority: int | None = Field(default=None)

        root_super: bool | None = Field(default=None)
        edge_port: EdgePort | None = Field(default=None)
        mode: str | None = Field(default=None)
        bpduguard_rate_limit: BpduguardRateLimit | None = Field(default=None)
        rstp_priority: int | None = Field(default=None)
        mst: Mst | None = Field(default=None)
        mst_instances: list[MstInstancesItem] | None = Field(default=None)
        no_spanning_tree_vlan: str | None = Field(default=None)
        rapid_pvst_instances: list[RapidPvstInstancesItem] | None = Field(default=None)

    class StandardAccessListsItem(BaseModel):
        class SequenceNumbersItem(BaseModel):
            sequence: int | None = Field(default=None)
            action: str = Field(default=None)

        name: str | None = Field(default=None)
        counters_per_entry: bool | None = Field(default=None)
        sequence_numbers: list[SequenceNumbersItem] = Field(default=None)

    class StaticRoutesItem(BaseModel):
        vrf: str | None = Field(default=None)
        destination_address_prefix: str | None = Field(default=None)
        interface: str | None = Field(default=None)
        gateway: str | None = Field(default=None)
        track_bfd: bool | None = Field(default=None)
        distance: int | None = Field(default=None)
        tag: int | None = Field(default=None)
        name: str | None = Field(default=None)
        metric: int | None = Field(default=None)

    class SwitchportDefault(BaseModel):
        class Phone(BaseModel):
            cos: int | None = Field(default=None)
            trunk: str | None = Field(default=None)
            vlan: int | None = Field(default=None)

        mode: str | None = Field(default=None)
        phone: Phone | None = Field(default=None)

    class System(BaseModel):
        class ControlPlane(BaseModel):
            class TcpMss(BaseModel):
                ipv4: int | None = Field(default=None)
                ipv6: int | None = Field(default=None)

            class Ipv4AccessGroupsItem(BaseModel):
                acl_name: str | None = Field(default=None)
                vrf: str | None = Field(default=None)

            class Ipv6AccessGroupsItem(BaseModel):
                acl_name: str | None = Field(default=None)
                vrf: str | None = Field(default=None)

            tcp_mss: TcpMss | None = Field(default=None)
            ipv4_access_groups: list[Ipv4AccessGroupsItem] | None = Field(default=None)
            ipv6_access_groups: list[Ipv6AccessGroupsItem] | None = Field(default=None)

        control_plane: ControlPlane | None = Field(default=None)

    class TacacsServers(BaseModel):
        class HostsItem(BaseModel):
            host: str | None = Field(default=None)
            vrf: str | None = Field(default=None)
            key: str | None = Field(default=None)
            key_type: str = Field(default="7")
            single_connection: bool | None = Field(default=None)
            timeout: int | None = Field(default=None)

        hosts: list[HostsItem] | None = Field(default=None)
        policy_unknown_mandatory_attribute_ignore: bool | None = Field(default=None)

    class TapAggregation(BaseModel):
        class Mode(BaseModel):
            class Exclusive(BaseModel):
                enabled: bool | None = Field(default=None)
                profile: str | None = Field(default=None)
                no_errdisable: list[str] | None = Field(default=None)

            exclusive: Exclusive | None = Field(default=None)

        class Mac(BaseModel):
            class Timestamp(BaseModel):
                class Header(BaseModel):
                    format: str | None = Field(default=None)
                    eth_type: int | None = Field(default=None)

                replace_source_mac: bool | None = Field(default=None)
                header: Header | None = Field(default=None)

            timestamp: Timestamp | None = Field(default=None)
            fcs_append: bool | None = Field(default=None)
            fcs_error: str | None = Field(default=None)

        mode: Mode | None = Field(default=None)
        encapsulation_dot1br_strip: bool | None = Field(default=None)
        encapsulation_vn_tag_strip: bool | None = Field(default=None)
        protocol_lldp_trap: bool | None = Field(default=None)
        truncation_size: int | None = Field(default=None)
        mac: Mac | None = Field(default=None)

    class TcamProfile(BaseModel):
        class ProfilesItem(BaseModel):
            name: str | None = Field(default=None)
            config: str | None = Field(default=None)
            source: str | None = Field(default=None)

        system: str | None = Field(default=None)
        profiles: list[ProfilesItem] | None = Field(default=None)

    class Terminal(BaseModel):
        length: int | None = Field(default=None)
        width: int | None = Field(default=None)

    class TrackersItem(BaseModel):
        name: str | None = Field(default=None)
        interface: str = Field(default=None)
        tracked_property: str = Field(default="line-protocol")

    class TrafficPolicies(BaseModel):
        class Options(BaseModel):
            counter_per_interface: bool | None = Field(default=None)

        class FieldSets(BaseModel):
            class Ipv4Item(BaseModel):
                name: str | None = Field(default=None)
                prefixes: list[str] | None = Field(default=None)

            class Ipv6Item(BaseModel):
                name: str | None = Field(default=None)
                prefixes: list[str] | None = Field(default=None)

            class PortsItem(BaseModel):
                name: str | None = Field(default=None)
                port_range: str | None = Field(default=None)

            ipv4: list[Ipv4Item] | None = Field(default=None)
            ipv6: list[Ipv6Item] | None = Field(default=None)
            ports: list[PortsItem] | None = Field(default=None)

        class PoliciesItem(BaseModel):
            class MatchesItem(BaseModel):
                class Source(BaseModel):
                    prefixes: list[str] | None = Field(default=None)
                    prefix_lists: list[str] | None = Field(default=None)

                class Destination(BaseModel):
                    prefixes: list[str] | None = Field(default=None)
                    prefix_lists: list[str] | None = Field(default=None)

                class Fragment(BaseModel):
                    offset: str | None = Field(default=None)

                class ProtocolsItem(BaseModel):
                    protocol: str | None = Field(default=None)
                    src_port: str | None = Field(default=None)
                    dst_port: str | None = Field(default=None)
                    src_field: str | None = Field(default=None)
                    dst_field: str | None = Field(default=None)
                    flags: list[str] | None = Field(default=None)
                    icmp_type: list[str] | None = Field(default=None)

                class Actions(BaseModel):
                    dscp: int | None = Field(default=None)
                    traffic_class: int | None = Field(default=None)
                    count: str | None = Field(default=None)
                    drop: bool | None = Field(default=None)
                    log: bool | None = Field(default=None)

                name: str | None = Field(default=None)
                type: str | None = Field(default=None)
                source: Source | None = Field(default=None)
                destination: Destination | None = Field(default=None)
                ttl: str | None = Field(default=None)
                fragment: Fragment | None = Field(default=None)
                protocols: list[ProtocolsItem] | None = Field(default=None)
                actions: Actions | None = Field(default=None)

            class DefaultActions(BaseModel):
                class Ipv4(BaseModel):
                    dscp: int | None = Field(default=None)
                    traffic_class: int | None = Field(default=None)
                    count: str | None = Field(default=None)
                    drop: bool | None = Field(default=None)
                    log: bool | None = Field(default=None)

                class Ipv6(BaseModel):
                    dscp: int | None = Field(default=None)
                    traffic_class: int | None = Field(default=None)
                    count: str | None = Field(default=None)
                    drop: bool | None = Field(default=None)
                    log: bool | None = Field(default=None)

                ipv4: Ipv4 | None = Field(default=None)
                ipv6: Ipv6 | None = Field(default=None)

            name: str | None = Field(default=None)
            matches: list[MatchesItem] | None = Field(default=None)
            default_actions: DefaultActions | None = Field(default=None)

        options: Options | None = Field(default=None)
        field_sets: FieldSets | None = Field(default=None)
        policies: list[PoliciesItem] | None = Field(default=None)

    class TunnelInterfacesItem(BaseModel):
        class TcpMssCeiling(BaseModel):
            ipv4: int | None = Field(default=None)
            ipv6: int | None = Field(default=None)
            direction: str | None = Field(default=None)

        name: str | None = Field(default=None)
        description: str | None = Field(default=None)
        shutdown: bool | None = Field(default=None)
        mtu: int | None = Field(default=None)
        vrf: str | None = Field(default=None)
        ip_address: str | None = Field(default=None)
        ipv6_enable: bool | None = Field(default=None)
        ipv6_address: str | None = Field(default=None)
        access_group_in: str | None = Field(default=None)
        access_group_out: str | None = Field(default=None)
        ipv6_access_group_in: str | None = Field(default=None)
        ipv6_access_group_out: str | None = Field(default=None)
        tcp_mss_ceiling: TcpMssCeiling | None = Field(default=None)
        source_interface: str | None = Field(default=None)
        destination: str | None = Field(default=None)
        path_mtu_discovery: bool | None = Field(default=None)
        eos_cli: str | None = Field(default=None)

    class VirtualSourceNatVrfsItem(BaseModel):
        name: str | None = Field(default=None)
        ip_address: str | None = Field(default=None)

    class VlanInterfacesItem(BaseModel):
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

                dynamic: list[DynamicItem] | None = Field(default=None)
                static: list[StaticItem] | None = Field(default=None)

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

                dynamic: list[DynamicItem] | None = Field(default=None)
                static: list[StaticItem] | None = Field(default=None)

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

                boundaries: list[BoundariesItem] | None = Field(default=None)
                source_route_export: SourceRouteExport | None = Field(default=None)
                static: bool | None = Field(default=None)

            class Ipv6(BaseModel):
                class BoundariesItem(BaseModel):
                    boundary: str | None = Field(default=None)

                class SourceRouteExport(BaseModel):
                    enabled: bool = Field(default=None)
                    administrative_distance: int | None = Field(default=None)

                boundaries: list[BoundariesItem] | None = Field(default=None)
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
            tracked_object: list[TrackedObjectItem] | None = Field(default=None)
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
        ip_address_secondaries: list[str] | None = Field(default=None)
        ip_virtual_router_addresses: list[str] | None = Field(default=None)
        ip_address_virtual: str | None = Field(default=None)
        ip_address_virtual_secondaries: list[str] | None = Field(default=None)
        ip_igmp: bool | None = Field(default=None)
        ip_igmp_version: int | None = Field(default=None)
        ip_helpers: list[IpHelpersItem] | None = Field(default=None)
        ip_nat: IpNat | None = Field(default=None)
        ipv6_enable: bool | None = Field(default=None)
        ipv6_address: str | None = Field(default=None)
        ipv6_address_virtual: str | None = Field(default=None)
        ipv6_address_virtuals: list[str] | None = Field(default=None)
        ipv6_address_link_local: str | None = Field(default=None)
        ipv6_virtual_router_address: str | None = Field(default=None)
        ipv6_virtual_router_addresses: list[str] | None = Field(default=None)
        ipv6_nd_ra_disabled: bool | None = Field(default=None)
        ipv6_nd_managed_config_flag: bool | None = Field(default=None)
        ipv6_nd_prefixes: list[Ipv6NdPrefixesItem] | None = Field(default=None)
        ipv6_dhcp_relay_destinations: list[Ipv6DhcpRelayDestinationsItem] | None = Field(default=None)
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
        ospf_message_digest_keys: list[OspfMessageDigestKeysItem] | None = Field(default=None)
        pim: Pim | None = Field(default=None)
        isis_enable: str | None = Field(default=None)
        isis_passive: bool | None = Field(default=None)
        isis_metric: int | None = Field(default=None)
        isis_network_point_to_point: bool | None = Field(default=None)
        mtu: int | None = Field(default=None)
        no_autostate: bool | None = Field(default=None)
        vrrp_ids: list[VrrpIdsItem] | None = Field(default=None)
        vrrp: Vrrp | None = Field(default=None)
        ip_attached_host_route_export: IpAttachedHostRouteExport | None = Field(default=None)
        bfd: Bfd | None = Field(default=None)
        service_policy: ServicePolicy | None = Field(default=None)
        pvlan_mapping: str | None = Field(default=None)
        tenant: str | None = Field(default=None)
        tags: list[str] | None = Field(default=None)
        type: str | None = Field(default=None)
        eos_cli: str | None = Field(default=None)

    class VlanInternalOrder(BaseModel):
        class Range(BaseModel):
            beginning: int = Field(default=None)
            ending: int = Field(default=None)

        allocation: str = Field(default=None)
        range: Range = Field(default=None)

    class VlansItem(BaseModel):
        class PrivateVlan(BaseModel):
            type: str | None = Field(default=None)
            primary_vlan: int | None = Field(default=None)

        id: int | None = Field(default=None)
        name: str | None = Field(default=None)
        state: str | None = Field(default=None)
        trunk_groups: list[str] | None = Field(default=None)
        private_vlan: PrivateVlan | None = Field(default=None)
        tenant: str | None = Field(default=None)

    class VmtracerSessionsItem(BaseModel):
        name: str | None = Field(default=None)
        url: str | None = Field(default=None)
        username: str | None = Field(default=None)
        password: str | None = Field(default=None)
        autovlan_disable: bool | None = Field(default=None)
        source_interface: str | None = Field(default=None)

    class VrfsItem(BaseModel):
        name: str | None = Field(default=None)
        description: str | None = Field(default=None)
        ip_routing: bool | None = Field(default=None)
        ipv6_routing: bool | None = Field(default=None)
        ip_routing_ipv6_interfaces: bool | None = Field(default=None)
        tenant: str | None = Field(default=None)

    class VxlanInterface(BaseModel):
        class Vxlan1(BaseModel):
            class Vxlan(BaseModel):
                class ControllerClient(BaseModel):
                    enabled: bool | None = Field(default=None)

                class BfdVtepEvpn(BaseModel):
                    interval: int | None = Field(default=None)
                    min_rx: int | None = Field(default=None)
                    multiplier: int | None = Field(default=None)
                    prefix_list: str | None = Field(default=None)

                class Qos(BaseModel):
                    dscp_propagation_encapsulation: bool | None = Field(default=None)
                    ecn_propagation: bool | None = Field(default=None)
                    map_dscp_to_traffic_class_decapsulation: bool | None = Field(default=None)

                class VlansItem(BaseModel):
                    id: int | None = Field(default=None)
                    vni: int | None = Field(default=None)
                    multicast_group: str | None = Field(default=None)
                    flood_vteps: list[str] | None = Field(default=None)

                class VrfsItem(BaseModel):
                    name: str | None = Field(default=None)
                    vni: int | None = Field(default=None)
                    multicast_group: str | None = Field(default=None)

                source_interface: str | None = Field(default=None)
                controller_client: ControllerClient | None = Field(default=None)
                mlag_source_interface: str | None = Field(default=None)
                udp_port: int | None = Field(default=None)
                virtual_router_encapsulation_mac_address: str | None = Field(default=None)
                bfd_vtep_evpn: BfdVtepEvpn | None = Field(default=None)
                qos: Qos | None = Field(default=None)
                vlans: list[VlansItem] | None = Field(default=None)
                vrfs: list[VrfsItem] | None = Field(default=None)
                flood_vteps: list[str] | None = Field(default=None)
                flood_vtep_learned_data_plane: bool | None = Field(default=None)

            description: str | None = Field(default=None)
            vxlan: Vxlan | None = Field(default=None)
            eos_cli: str | None = Field(default=None)

        Vxlan1_key: Vxlan1 | None = Field(default=None, alias="Vxlan1")

    aaa_accounting: AaaAccounting | None = Field(default=None)
    aaa_authentication: AaaAuthentication | None = Field(default=None)
    aaa_authorization: AaaAuthorization | None = Field(default=None)
    aaa_root: AaaRoot | None = Field(default=None)
    aaa_server_groups: list[AaaServerGroupsItem] | None = Field(default=None)
    access_lists: list[AccessListsItem] | None = Field(default=None)
    address_locking: AddressLocking | None = Field(default=None)
    aliases: str | None = Field(default=None)
    arp: Arp | None = Field(default=None)
    as_path: AsPath | None = Field(default=None)
    avd_data_conversion_mode: str = Field(default="debug")
    avd_data_validation_mode: str = Field(default="warning")
    banners: Banners | None = Field(default=None)
    bgp_groups: list[BgpGroupsItem] | None = Field(default=None)
    boot: Boot | None = Field(default=None)
    class_maps: ClassMaps | None = Field(default=None)
    clock: Clock | None = Field(default=None)
    community_lists: list[CommunityListsItem] | None = Field(default=None)
    custom_templates: list[str] | None = Field(default=None)
    cvx: Cvx | None = Field(default=None)
    daemon_terminattr: DaemonTerminattr | None = Field(default=None)
    daemons: list[DaemonsItem] | None = Field(default=None)
    dhcp_relay: DhcpRelay | None = Field(default=None)
    dns_domain: str | None = Field(default=None)
    domain_list: list[str] | None = Field(default=None)
    dot1x: Dot1x | None = Field(default=None)
    dynamic_prefix_lists: list[DynamicPrefixListsItem] | None = Field(default=None)
    enable_password: EnablePassword | None = Field(default=None)
    eos_cli: str | None = Field(default=None)
    eos_cli_config_gen_configuration: EosCliConfigGenConfiguration | None = Field(default=None)
    eos_cli_config_gen_documentation: EosCliConfigGenDocumentation | None = Field(default=None)
    errdisable: Errdisable | None = Field(default=None)
    ethernet_interfaces: list[EthernetInterfacesItem] | None = Field(default=None)
    event_handlers: list[EventHandlersItem] | None = Field(default=None)
    event_monitor: EventMonitor | None = Field(default=None)
    flow_trackings: list[FlowTrackingsItem] | None = Field(default=None)
    generate_default_config: bool = Field(default=True)
    generate_device_documentation: bool = Field(default=True)
    hardware: Hardware | None = Field(default=None)
    hardware_counters: HardwareCounters | None = Field(default=None)
    hostname: str | None = Field(default=None)
    interface_defaults: InterfaceDefaults | None = Field(default=None)
    interface_groups: list[InterfaceGroupsItem] | None = Field(default=None)
    interface_profiles: list[InterfaceProfilesItem] | None = Field(default=None)
    ip_access_lists: list[IpAccessListsItem] | None = Field(default=None)
    ip_access_lists_max_entries: int | None = Field(default=None)
    ip_community_lists: list[IpCommunityListsItem] | None = Field(default=None)
    ip_dhcp_relay: IpDhcpRelay | None = Field(default=None)
    ip_domain_lookup: IpDomainLookup | None = Field(default=None)
    ip_extcommunity_lists: list[IpExtcommunityListsItem] | None = Field(default=None)
    ip_extcommunity_lists_regexp: list[IpExtcommunityListsRegexpItem] | None = Field(default=None)
    ip_hardware: IpHardware | None = Field(default=None)
    ip_http_client_source_interfaces: list[IpHttpClientSourceInterfacesItem] | None = Field(default=None)
    ip_icmp_redirect: bool | None = Field(default=None)
    ip_igmp_snooping: IpIgmpSnooping | None = Field(default=None)
    ip_name_servers: list[IpNameServersItem] | None = Field(default=None)
    ip_nat: IpNat | None = Field(default=None)
    ip_radius_source_interfaces: list[IpRadiusSourceInterfacesItem] | None = Field(default=None)
    ip_routing: bool | None = Field(default=None)
    ip_routing_ipv6_interfaces: bool | None = Field(default=None)
    ip_ssh_client_source_interfaces: list[IpSshClientSourceInterfacesItem] | None = Field(default=None)
    ip_tacacs_source_interfaces: list[IpTacacsSourceInterfacesItem] | None = Field(default=None)
    ip_virtual_router_mac_address: str | None = Field(default=None)
    ipv6_access_lists: list[Ipv6AccessListsItem] | None = Field(default=None)
    ipv6_hardware: Ipv6Hardware | None = Field(default=None)
    ipv6_icmp_redirect: bool | None = Field(default=None)
    ipv6_prefix_lists: list[Ipv6PrefixListsItem] | None = Field(default=None)
    ipv6_standard_access_lists: list[Ipv6StandardAccessListsItem] | None = Field(default=None)
    ipv6_static_routes: list[Ipv6StaticRoutesItem] | None = Field(default=None)
    ipv6_unicast_routing: bool | None = Field(default=None)
    l2_protocol: L2Protocol | None = Field(default=None)
    lacp: Lacp | None = Field(default=None)
    link_tracking_groups: list[LinkTrackingGroupsItem] | None = Field(default=None)
    lldp: Lldp | None = Field(default=None)
    load_interval: LoadInterval | None = Field(default=None)
    local_users: list[LocalUsersItem] | None = Field(default=None)
    logging: Logging | None = Field(default=None)
    loopback_interfaces: list[LoopbackInterfacesItem] | None = Field(default=None)
    mac_access_lists: list[MacAccessListsItem] | None = Field(default=None)
    mac_address_table: MacAddressTable | None = Field(default=None)
    mac_security: MacSecurity | None = Field(default=None)
    maintenance: Maintenance | None = Field(default=None)
    management_accounts: ManagementAccounts | None = Field(default=None)
    management_api_gnmi: ManagementApiGnmi | None = Field(default=None)
    management_api_http: ManagementApiHttp | None = Field(default=None)
    management_api_models: ManagementApiModels | None = Field(default=None)
    management_console: ManagementConsole | None = Field(default=None)
    management_cvx: ManagementCvx | None = Field(default=None)
    management_defaults: ManagementDefaults | None = Field(default=None)
    management_interfaces: list[ManagementInterfacesItem] | None = Field(default=None)
    management_security: ManagementSecurity | None = Field(default=None)
    management_ssh: ManagementSsh | None = Field(default=None)
    management_tech_support: ManagementTechSupport | None = Field(default=None)
    match_list_input: MatchListInput | None = Field(default=None)
    mcs_client: McsClient | None = Field(default=None)
    mlag_configuration: MlagConfiguration | None = Field(default=None)
    monitor_connectivity: MonitorConnectivity | None = Field(default=None)
    monitor_sessions: list[MonitorSessionsItem] | None = Field(default=None)
    mpls: Mpls | None = Field(default=None)
    name_server: NameServer | None = Field(default=None)
    ntp: Ntp | None = Field(default=None)
    patch_panel: PatchPanel | None = Field(default=None)
    peer_filters: list[PeerFiltersItem] | None = Field(default=None)
    platform: Platform | None = Field(default=None)
    poe: Poe | None = Field(default=None)
    policy_maps: PolicyMaps | None = Field(default=None)
    port_channel_interfaces: list[PortChannelInterfacesItem] | None = Field(default=None)
    prefix_lists: list[PrefixListsItem] | None = Field(default=None)
    priority_flow_control: PriorityFlowControl | None = Field(default=None)
    prompt: str | None = Field(default=None)
    ptp: Ptp | None = Field(default=None)
    qos: Qos | None = Field(default=None)
    qos_profiles: list[QosProfilesItem] | None = Field(default=None)
    queue_monitor_length: QueueMonitorLength | None = Field(default=None)
    queue_monitor_streaming: QueueMonitorStreaming | None = Field(default=None)
    radius_server: RadiusServer | None = Field(default=None)
    radius_servers: list[RadiusServersItem] | None = Field(default=None)
    redundancy: Redundancy | None = Field(default=None)
    roles: list[RolesItem] | None = Field(default=None)
    route_maps: list[RouteMapsItem] | None = Field(default=None)
    router_bfd: RouterBfd | None = Field(default=None)
    router_bgp: RouterBgp | None = Field(default=None)
    router_general: RouterGeneral | None = Field(default=None)
    router_igmp: RouterIgmp | None = Field(default=None)
    router_isis: RouterIsis | None = Field(default=None)
    router_l2_vpn: RouterL2Vpn | None = Field(default=None)
    router_msdp: RouterMsdp | None = Field(default=None)
    router_multicast: RouterMulticast | None = Field(default=None)
    router_ospf: RouterOspf | None = Field(default=None)
    router_pim_sparse_mode: RouterPimSparseMode | None = Field(default=None)
    router_traffic_engineering: RouterTrafficEngineering | None = Field(default=None)
    service_routing_configuration_bgp: ServiceRoutingConfigurationBgp | None = Field(default=None)
    service_routing_protocols_model: str | None = Field(default=None)
    service_unsupported_transceiver: ServiceUnsupportedTransceiver | None = Field(default=None)
    sflow: Sflow | None = Field(default=None)
    snmp_server: SnmpServer | None = Field(default=None)
    spanning_tree: SpanningTree | None = Field(default=None)
    standard_access_lists: list[StandardAccessListsItem] | None = Field(default=None)
    static_routes: list[StaticRoutesItem] | None = Field(default=None)
    switchport_default: SwitchportDefault | None = Field(default=None)
    system: System | None = Field(default=None)
    tacacs_servers: TacacsServers | None = Field(default=None)
    tap_aggregation: TapAggregation | None = Field(default=None)
    tcam_profile: TcamProfile | None = Field(default=None)
    terminal: Terminal | None = Field(default=None)
    trackers: list[TrackersItem] | None = Field(default=None)
    traffic_policies: TrafficPolicies | None = Field(default=None)
    tunnel_interfaces: list[TunnelInterfacesItem] | None = Field(default=None)
    virtual_source_nat_vrfs: list[VirtualSourceNatVrfsItem] | None = Field(default=None)
    vlan_interfaces: list[VlanInterfacesItem] | None = Field(default=None)
    vlan_internal_order: VlanInternalOrder | None = Field(default=None)
    vlans: list[VlansItem] | None = Field(default=None)
    vmtracer_sessions: list[VmtracerSessionsItem] | None = Field(default=None)
    vrfs: list[VrfsItem] | None = Field(default=None)
    vxlan_interface: VxlanInterface | None = Field(default=None)
