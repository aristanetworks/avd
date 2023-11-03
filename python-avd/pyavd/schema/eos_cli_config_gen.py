# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, ConfigDict, Field
from typing_extensions import Annotated

from .types import StrConvert


class EosCliConfigGen(BaseModel):
    model_config = ConfigDict(defer_build=True, use_enum_values=True)

    class AaaAccounting(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Exec(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Console(BaseModel):
                model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                class TypeEnum(Enum):
                    value_0 = "none"
                    value_1 = "start-stop"
                    value_2 = "stop-only"

                type: TypeEnum | None = None
                group: str | None = None
                """
                Group Name
                """
                logging: bool | None = None

            class Default(BaseModel):
                model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                class TypeEnum(Enum):
                    value_0 = "none"
                    value_1 = "start-stop"
                    value_2 = "stop-only"

                type: TypeEnum | None = None
                group: str | None = None
                """
                Group Name
                """
                logging: bool | None = None

            console: Console | None = None
            default: Default | None = None

        class System(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Default(BaseModel):
                model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                class TypeEnum(Enum):
                    value_0 = "none"
                    value_1 = "start-stop"
                    value_2 = "stop-only"

                type: TypeEnum | None = None
                group: str | None = None
                """
                Group Name
                """

            default: Default | None = None

        class Dot1x(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Default(BaseModel):
                model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                class TypeEnum(Enum):
                    value_0 = "start-stop"
                    value_1 = "stop-only"

                type: TypeEnum | None = None
                group: str | None = None
                """
                Group Name
                """

            default: Default | None = None

        class Commands(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class ConsoleItem(BaseModel):
                model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                class TypeEnum(Enum):
                    value_0 = "none"
                    value_1 = "start-stop"
                    value_2 = "stop-only"

                commands: Annotated[str, StrConvert(convert_types=(int))] | None = None
                """
                Privelege level 'all' or 0-15
                """
                type: TypeEnum | None = None
                group: str | None = None
                """
                Group Name
                """
                logging: bool | None = None

            class DefaultItem(BaseModel):
                model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                class TypeEnum(Enum):
                    value_0 = "none"
                    value_1 = "start-stop"
                    value_2 = "stop-only"

                commands: Annotated[str, StrConvert(convert_types=(int))] | None = None
                """
                Privelege level 'all' or 0-15
                """
                type: TypeEnum | None = None
                group: str | None = None
                """
                Group Name
                """
                logging: bool | None = None

            console: list[ConsoleItem] | None = None
            default: list[DefaultItem] | None = None

        exec: Exec | None = None
        system: System | None = None
        dot1x: Dot1x | None = None
        commands: Commands | None = None

    class AaaAuthentication(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Login(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            default: str | None = None
            """
            Login authentication method(s) as a string.
            Examples:
            - "group tacacs+ local"
            - "group MYGROUP none"
            - "group radius
            group MYGROUP local"
            """
            console: str | None = None
            """
            Console authentication method(s) as a string.
            Examples:
            - "group tacacs+ local"
            - "group MYGROUP none"
            - "group radius
            group MYGROUP local"
            """

        class Enable(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            default: str | None = None
            """
            Enable authentication method(s) as a string.
            Examples:
            - "group tacacs+ local"
            - "group MYGROUP none"
            - "group radius
            group MYGROUP local"
            """

        class Dot1x(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            default: str | None = None
            """
            802.1x authentication method(s) as a string.
            Examples:
            - "group radius"
            - "group MYGROUP group radius"
            """

        class Policies(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Local(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                allow_nopassword: bool | None = None

            class Lockout(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                failure: int | None = Field(None, ge=1, le=255)
                duration: int | None = Field(None, ge=1, le=4294967295)
                window: int | None = Field(None, ge=1, le=4294967295)

            on_failure_log: bool | None = None
            on_success_log: bool | None = None
            local: Local | None = None
            lockout: Lockout | None = None

        login: Login | None = None
        enable: Enable | None = None
        dot1x: Dot1x | None = None
        policies: Policies | None = None

    class AaaAuthorization(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Policy(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            local_default_role: str | None = None

        class Exec(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            default: str | None = None
            """
            Exec authorization method(s) as a string.
            Examples:
            - "group tacacs+ local"
            - "group MYGROUP none"
            - "group radius group
            MYGROUP local"
            """

        class Dynamic(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            dot1x_additional_groups: list[str] | None = Field(None, min_length=1)

        class Commands(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class PrivilegeItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                level: Annotated[str, StrConvert(convert_types=(int))] | None = None
                """
                Privilege level(s) 0-15
                """
                default: str | None = None
                """
                Command authorization method(s) as a string.
                Examples:
                - "group tacacs+ local"
                - "group MYGROUP none"
                - "group tacacs+
                group MYGROUP local"
                """

            all_default: str | None = None
            """
            Command authorization method(s) as a string.
            Examples:
            - "group tacacs+ local"
            - "group MYGROUP none"
            - "group tacacs+
            group MYGROUP local
            """
            privilege: list[PrivilegeItem] | None = None

        policy: Policy | None = None
        exec: Exec | None = None
        config_commands: bool | None = None
        serial_console: bool | None = None
        dynamic: Dynamic | None = None
        commands: Commands | None = None

    class AaaRoot(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Secret(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            sha512_password: str | None = None

        secret: Secret | None = None

    class AaaServerGroupsItem(BaseModel):
        model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

        class TypeEnum(Enum):
            value_0 = "tacacs+"
            value_1 = "radius"
            value_2 = "ldap"

        class ServersItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            server: str | None = None
            """
            Hostname or IP address
            """
            vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
            """
            VRF name
            """

        name: str | None = None
        """
        Group name
        """
        type: TypeEnum | None = None
        servers: list[ServersItem] | None = None

    class AccessListsItem(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class SequenceNumbersItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            sequence: int = None
            """
            Sequence ID
            """
            action: str = None
            """
            Action as string
            Example: "deny ip any any"
            """

        name: str = None
        """
        Access-list Name
        """
        counters_per_entry: bool | None = None
        sequence_numbers: list[SequenceNumbersItem] = None

    class AddressLocking(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class LeasesItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            ip: str = None
            """
            IP address
            """
            mac: str = None
            """
            MAC address (hhhh.hhhh.hhhh or hh:hh:hh:hh:hh:hh)
            """

        class LockedAddress(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            expiration_mac_disabled: bool | None = None
            """
            Configure deauthorizing locked addresses upon MAC aging out
            """
            ipv4_enforcement_disabled: bool | None = None
            """
            Configure enforcement for locked IPv4 addresses
            """
            ipv6_enforcement_disabled: bool | None = None
            """
            Configure enforcement for locked IPv6 addresses
            """

        dhcp_servers_ipv4: list[str] | None = None
        disabled: bool | None = None
        """
        Disable IP locking on configured ports
        """
        leases: list[LeasesItem] | None = None
        local_interface: str | None = None
        locked_address: LockedAddress | None = None

    class AgentsItem(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class EnvironmentVariablesItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str = None
            """
            Environment variable name.
            """
            value: Annotated[str, StrConvert(convert_types=(int, bool))] = None
            """
            Environment variable value.
            """

        name: str = None
        """
        Agent name.
        """
        environment_variables: list[EnvironmentVariablesItem] | None = Field(None, min_length=1)

    class Arp(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Aging(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            timeout_default: int | None = Field(None, ge=60, le=65535)
            """
            Timeout in seconds
            """

        class StaticEntriesItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            ipv4_address: str = None
            """
            ARP entry IPv4 address.
            """
            vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
            """
            ARP entry VRF.
            """
            mac_address: str = Field(None, pattern=r"^[0-9A-Fa-f]{4}\.[0-9A-Fa-f]{4}\.[0-9A-Fa-f]{4}$")
            """
            ARP entry MAC address.
            """

        aging: Aging | None = None
        static_entries: list[StaticEntriesItem] | None = None
        """
        Static ARP entries.
        """

    class AsPath(BaseModel):
        model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

        class RegexModeEnum(Enum):
            value_0 = "asn"
            value_1 = "string"

        class AccessListsItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class EntriesItem(BaseModel):
                model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                class TypeEnum(Enum):
                    value_0 = "permit"
                    value_1 = "deny"

                class OriginEnum(Enum):
                    value_0 = "any"
                    value_1 = "egp"
                    value_2 = "igp"
                    value_3 = "incomplete"

                type: TypeEnum | None = None
                match: str | None = None
                """
                Regex To Match
                """
                origin: OriginEnum | None = "any"

            name: str | None = None
            """
            Access List Name
            """
            entries: list[EntriesItem] | None = None

        regex_mode: RegexModeEnum | None = None
        access_lists: list[AccessListsItem] | None = None

    class AvdDataConversionModeEnum(Enum):
        value_0 = "disabled"
        value_1 = "error"
        value_2 = "warning"
        value_3 = "info"
        value_4 = "debug"
        value_5 = "quiet"

    class AvdDataValidationModeEnum(Enum):
        value_0 = "disabled"
        value_1 = "error"
        value_2 = "warning"
        value_3 = "info"
        value_4 = "debug"

    class Banners(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        login: str | None = None
        """
        Multiline string ending with EOF on the last line
        """
        motd: str | None = None
        """
        Multiline string ending with EOF on the last line
        """

    class BgpGroupsItem(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        name: str = None
        """
        Group Name
        """
        vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
        neighbors: list[str] | None = None
        bgp_maintenance_profiles: list[str] | None = None

    class Boot(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Secret(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class HashAlgorithmEnum(Enum):
                value_0 = "md5"
                value_1 = "sha512"

            hash_algorithm: HashAlgorithmEnum | None = "sha512"
            key: str | None = None
            """
            Hashed Password
            """

        secret: Secret | None = None

    class ClassMaps(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class PbrItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Ip(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                access_group: str | None = None
                """
                Standard Access-List Name
                """

            name: str = None
            """
            Class-Map Name
            """
            ip: Ip | None = None

        class QosItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Ip(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                access_group: str | None = None
                """
                IPv4 Access-List Name
                """

            class Ipv6(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                access_group: str | None = None
                """
                IPv6 Access-List Name
                """

            name: str = None
            """
            Class-Map Name
            """
            vlan: Annotated[str, StrConvert(convert_types=(int))] | None = None
            """
            VLAN value(s) or range(s) of VLAN values
            """
            cos: Annotated[str, StrConvert(convert_types=(int))] | None = None
            """
            CoS value(s) or range(s) of CoS values
            """
            ip: Ip | None = None
            ipv6: Ipv6 | None = None

        pbr: list[PbrItem] | None = None
        qos: list[QosItem] | None = None

    class Clock(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        timezone: str | None = None

    class CommunityListsItem(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        name: str = None
        """
        Community-list Name
        """
        action: str = None
        """
        Action as string
        Example: "permit GSHUT 65123:123"
        """

    class Cvx(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Services(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Mcs(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Redis(BaseModel):
                    model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                    class PasswordTypeEnum(Enum):
                        value_0 = "0"
                        value_1 = "7"
                        value_2 = "8a"

                    password: str | None = None
                    """
                    Hashed password using the password_type
                    """
                    password_type: Annotated[PasswordTypeEnum, StrConvert(convert_types=(int))] | None = "7"

                redis: Redis | None = None
                shutdown: bool | None = None

            class Vxlan(BaseModel):
                model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                class VtepMacLearningEnum(Enum):
                    value_0 = "control-plane"
                    value_1 = "data-plane"

                shutdown: bool | None = None
                vtep_mac_learning: VtepMacLearningEnum | None = None

            mcs: Mcs | None = None
            vxlan: Vxlan | None = None
            """
            VXLAN Controller service
            """

        shutdown: bool | None = None
        peer_hosts: list[str] | None = None
        services: Services | None = None

    class DaemonTerminattr(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class ClustersItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Cvauth(BaseModel):
                model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                class MethodEnum(Enum):
                    value_0 = "token"
                    value_1 = "token-secure"
                    value_2 = "key"
                    value_3 = "certs"

                method: MethodEnum | None = None
                key: str | None = None
                token_file: str | None = None
                """
                Token file path
                e.g. "/tmp/token"
                """
                cert_file: str | None = None
                """
                Client certificate file path
                e.g. "/persist/secure/ssl/terminattr/primary/certs/client.crt"
                """
                ca_file: str | None = None
                """
                CA certificate file path (on-prem only)
                e.g. "/persist/secure/ssl/terminattr/primary/certs/ca.crt"
                """
                key_file: str | None = None
                """
                Client certificate key file path
                e.g. "/persist/secure/ssl/terminattr/primary/keys/client.key"
                """

            name: str = None
            """
            Cluster Name
            """
            cvaddrs: list[str] | None = None
            """
            Streaming address(es) for CloudVision cluster
            - TCP 9910 is used for CV on-prem
            - TCP 443 is used for CV as a Service
            """
            cvauth: Cvauth | None = None
            """
            Authentication scheme used to connect to CloudVision
            """
            cvobscurekeyfile: bool | None = None
            """
            Encrypt the private key used for authentication to CloudVision
            """
            cvproxy: str | None = None
            """
            Proxy server through which CloudVision is reachable. Useful when the CloudVision server is hosted in the cloud.
            The
            expected form is http://[user:password@]ip:port, e.g.: `http://arista:arista@10.83.12.78:3128`. Available as of
            TerminAttr v1.13.0
            """
            cvsourceip: str | None = None
            """
            Set source IP address in case of in-band managament
            """
            cvsourceintf: str | None = None
            """
            Set source interface in case of in-band managament. Available as of TerminAttr v1.23.0
            """
            cvvrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
            """
            The VRF to use to connect to CloudVision
            """

        class Cvauth(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class MethodEnum(Enum):
                value_0 = "token"
                value_1 = "token-secure"
                value_2 = "key"
                value_3 = "certs"

            method: MethodEnum | None = None
            key: str | None = None
            token_file: str | None = None
            """
            Token file path
            e.g. "/tmp/token"
            """
            cert_file: str | None = None
            """
            Client certificate file path
            e.g. "/persist/secure/ssl/terminattr/primary/certs/client.crt"
            """
            ca_file: str | None = None
            """
            CA certificate file path (on-prem only)
            e.g. "/persist/secure/ssl/terminattr/primary/certs/ca.crt"
            """
            key_file: str | None = None
            """
            Client certificate key file path
            e.g. "/persist/secure/ssl/terminattr/primary/keys/client.key"
            """

        cvaddrs: list[str] | None = None
        """
        Streaming address(es) for CloudVision single cluster
        - TCP 9910 is used for CV on-prem
        - TCP 443 is used for CV as a
        Service
        """
        clusters: list[ClustersItem] | None = None
        """
        Multiple CloudVision clusters
        """
        cvauth: Cvauth | None = None
        """
        Authentication scheme used to connect to CloudVision
        """
        cvobscurekeyfile: bool | None = None
        """
        Encrypt the private key used for authentication to CloudVision
        """
        cvproxy: str | None = None
        """
        Proxy server through which CloudVision is reachable. Useful when the CloudVision server is hosted in the cloud.
        The
        expected form is http://[user:password@]ip:port, e.g.: `http://arista:arista@10.83.12.78:3128`. Available as of
        TerminAttr v1.13.0
        """
        cvsourceip: str | None = None
        """
        Set source IP address in case of in-band managament
        """
        cvsourceintf: str | None = None
        """
        Set source interface in case of in-band managament
        """
        cvvrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
        """
        The VRF to use to connect to CloudVision
        """
        cvgnmi: bool | None = None
        """
        Stream states from EOS gNMI servers (Openconfig) to CloudVision. Available as of TerminAttr v1.13.1
        """
        disable_aaa: bool | None = None
        """
        Disable AAA authorization and accounting.
        When setting this flag, all commands pushed from CloudVision are applied
        directly to the CLI without authorization
        """
        grpcaddr: str | None = None
        """
        Set the gRPC server address, the default is 127.0.0.1:6042
        e.g. "MGMT/0.0.0.0:6042"
        """
        grpcreadonly: bool | None = None
        """
        gNMI read-only mode - Disable gnmi.Set()
        """
        ingestexclude: str | None = None
        """
        Exclude paths from Sysdb on the ingest side.
        e.g. "/Sysdb/cell/1/agent,/Sysdb/cell/2/agent"
        """
        smashexcludes: str | None = None
        """
        Exclude paths from the shared memory table.
        e.g. "ale,flexCounter,hardware,kni,pulse,strata"
        """
        taillogs: str | None = None
        """
        Enable log file collection; /var/log/messages is streamed by default if no path is set.
        e.g. "/var/log/messages"
        """
        ecodhcpaddr: str | None = None
        """
        ECO DHCP Collector address or ECO DHCP Fingerprint listening address in standalone mode (default "127.0.0.1:67")
        """
        ipfix: bool | None = None
        """
        Enable IPFIX provider (TerminAttr default is true).
        This flag is enabled by default and does not have to be added to the
        daemon configuration.
        """
        ipfixaddr: str | None = None
        """
        ECO IPFIX Collector address to listen on to receive IPFIX packets (TerminAttr default "127.0.0.1:4739").
        """
        sflow: bool | None = None
        """
        Enable sFlow provider (TerminAttr default is true).
        """
        sflowaddr: str | None = None
        """
        ECO sFlow Collector address to listen on to receive sFlow packets (TerminAttr default "127.0.0.1:6343").
        """
        cvconfig: bool | None = None
        """
        Subscribe to dynamic device configuration from CloudVision (TerminAttr default is false).
        """
        cvcompression: str | None = None
        """
        The default compression scheme when streaming to CloudVision is gzip since TerminAttr 1.6.1 and CVP 2019.1.0.
        There is
        no need to change the compression scheme.
        """

    class DaemonsItem(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        name: str = None
        """
        Daemon Name
        """
        exec: str = None
        """
        command to run as a daemon
        """
        enabled: bool | None = True

    class DhcpRelay(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        servers: list[str] | None = None
        tunnel_requests_disabled: bool | None = None
        mlag_peerlink_requests_disabled: bool | None = None

    class Dot1x(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class MacBasedAuthentication(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            delay: int | None = Field(None, ge=0, le=300)
            hold_period: int | None = Field(None, ge=1, le=300)

        class RadiusAvPair(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            service_type: bool | None = None
            framed_mtu: int | None = Field(None, ge=68, le=9236)

        system_auth_control: bool | None = None
        protocol_lldp_bypass: bool | None = None
        dynamic_authorization: bool | None = None
        mac_based_authentication: MacBasedAuthentication | None = None
        radius_av_pair: RadiusAvPair | None = None

    class DpsInterfacesItem(BaseModel):
        model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

        class NameEnum(Enum):
            value_0 = "Dps1"

        class FlowTracker(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            sampled: str | None = None
            """
            Sampled flow tracker name.
            """
            hardware: str | None = None
            """
            Hardware flow tracker name,
            """

        class TcpMssCeiling(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class DirectionEnum(Enum):
                value_0 = "ingress"
                value_1 = "egress"

            ipv4: int | None = Field(None, ge=64, le=65495)
            """
            Segment Size for IPv4.
            """
            ipv6: int | None = Field(None, ge=64, le=65475)
            """
            Segment Size for IPv6.
            """
            direction: DirectionEnum | None = None
            """
            Optional direction ('ingress', 'egress')  for tcp mss ceiling.
            """

        name: NameEnum = None
        """
        "Dps1" is currently the only supported interface.
        """
        description: str | None = None
        shutdown: bool | None = None
        mtu: int | None = Field(None, ge=68, le=65535)
        """
        Maximum Transmission Unit in bytes.
        """
        ip_address: str | None = None
        """
        IPv4 address/mask.
        """
        flow_tracker: FlowTracker | None = None
        tcp_mss_ceiling: TcpMssCeiling | None = None
        eos_cli: str | None = None
        """
        Multiline String with EOS CLI rendered directly on the Dps interface in the final EOS configuration.
        """

    class DynamicPrefixListsItem(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class PrefixList(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            ipv4: str | None = None
            """
            Prefix-list name
            """
            ipv6: str | None = None
            """
            Prefix-list name
            """

        name: str | None = None
        """
        Dynamic prefix-list name
        """
        match_map: str | None = None
        """
        Route-map name
        """
        prefix_list: PrefixList | None = None

    class EnablePassword(BaseModel):
        model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

        class HashAlgorithmEnum(Enum):
            value_0 = "md5"
            value_1 = "sha512"

        hash_algorithm: HashAlgorithmEnum | None = None
        key: str | None = None
        """
        Must be the hash of the password using the specified algorithm.
        By default EOS salts the password, so the simplest is to
        generate the hash on an EOS device.
        """

    class EosCliConfigGenConfiguration(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        hide_passwords: bool | None = False
        """
        Replace the input data using the `hide_passwords` filter in the Jinja2 templates by '<removed>' in the configruation if
        true
        """

    class EosCliConfigGenDocumentation(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        hide_passwords: bool | None = True
        """
        Replace the input data using the `hide_passwords` filter in the Jinja2 templates by '<removed>' in the documentation if
        true
        """

    class Errdisable(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Detect(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            causes: list[str] | None = None

        class Recovery(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            causes: list[str] | None = None
            interval: int | None = Field(300, ge=30, le=86400)
            """
            Interval in seconds
            """

        detect: Detect | None = None
        recovery: Recovery | None = None

    class EthernetInterfacesItem(BaseModel):
        model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

        class ModeEnum(Enum):
            value_0 = "access"
            value_1 = "dot1q-tunnel"
            value_2 = "trunk"
            value_3 = "trunk phone"

        class Phone(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class TrunkEnum(Enum):
                value_0 = "tagged"
                value_1 = "tagged phone"
                value_2 = "untagged"
                value_3 = "untagged phone"

            trunk: TrunkEnum | None = None
            vlan: int | None = Field(None, ge=1, le=4094)

        class L2Protocol(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            encapsulation_dot1q_vlan: int | None = None
            """
            Vlan tag to configure on sub-interface
            """
            forwarding_profile: str | None = None
            """
            L2 protocol forwarding profile
            """

        class TypeEnum(Enum):
            value_0 = "routed"
            value_1 = "switched"
            value_2 = "l3dot1q"
            value_3 = "l2dot1q"
            value_4 = "port-channel-member"

        class AddressLocking(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            ipv4: bool | None = None
            """
            Enable address locking for IPv4
            """
            ipv6: bool | None = None
            """
            Enable address locking for IPv6
            """

        class Flowcontrol(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class ReceivedEnum(Enum):
                value_0 = "desired"
                value_1 = "on"
                value_2 = "off"

            received: ReceivedEnum | None = None

        class FlowTracker(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            sampled: str | None = None
            """
            Sampled flow tracker name.
            """
            hardware: str | None = None
            """
            Hardware flow tracker name.
            """

        class ErrorCorrectionEncoding(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            enabled: bool | None = True
            fire_code: bool | None = None
            reed_solomon: bool | None = None

        class LinkTrackingGroupsItem(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class DirectionEnum(Enum):
                value_0 = "upstream"
                value_1 = "downstream"

            name: str = None
            """
            Group name
            """
            direction: DirectionEnum | None = None

        class EvpnEthernetSegment(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class RedundancyEnum(Enum):
                value_0 = "all-active"
                value_1 = "single-active"

            class DesignatedForwarderElection(BaseModel):
                model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                class AlgorithmEnum(Enum):
                    value_0 = "modulus"
                    value_1 = "preference"

                algorithm: AlgorithmEnum | None = None
                preference_value: int | None = Field(None, ge=0, le=65535)
                """
                Preference_value is only used when "algorithm" is "preference"
                """
                dont_preempt: bool | None = None
                """
                Dont_preempt is only used when "algorithm" is "preference"
                """
                hold_time: int | None = None
                subsequent_hold_time: int | None = None
                candidate_reachability_required: bool | None = None

            class Mpls(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                shared_index: int | None = Field(None, ge=1, le=1024)
                tunnel_flood_filter_time: int | None = None

            identifier: str | None = None
            """
            EVPN Ethernet Segment Identifier (Type 1 format)
            """
            redundancy: RedundancyEnum | None = None
            designated_forwarder_election: DesignatedForwarderElection | None = None
            mpls: Mpls | None = None
            route_target: str | None = None
            """
            EVPN Route Target for ESI with format xx:xx:xx:xx:xx:xx
            """

        class EncapsulationVlan(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Client(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Dot1q(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    vlan: int | None = None
                    """
                    Client VLAN ID
                    """
                    outer: int | None = None
                    """
                    Client Outer VLAN ID
                    """
                    inner: int | None = None
                    """
                    Client Inner VLAN ID
                    """

                dot1q: Dot1q | None = None
                unmatched: bool | None = None

            class Network(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Dot1q(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    vlan: int | None = None
                    """
                    Network VLAN ID
                    """
                    outer: int | None = None
                    """
                    Network outer VLAN ID
                    """
                    inner: int | None = None
                    """
                    Network inner VLAN ID
                    """

                dot1q: Dot1q | None = None
                client: bool | None = None

            client: Client | None = None
            network: Network | None = None
            """
            Network encapsulations are all optional and skipped if using client unmatched
            """

        class IpHelpersItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            ip_helper: str = None
            source_interface: str | None = None
            """
            Source interface name
            """
            vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
            """
            VRF name
            """

        class IpNat(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Destination(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class DynamicItem(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    access_list: str = None
                    comment: str | None = None
                    pool_name: str = None
                    priority: int | None = Field(None, ge=0, le=4294967295)

                class StaticItem(BaseModel):
                    model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                    class DirectionEnum(Enum):
                        value_0 = "egress"
                        value_1 = "ingress"

                    class ProtocolEnum(Enum):
                        value_0 = "udp"
                        value_1 = "tcp"

                    access_list: str | None = None
                    """
                    'access_list' and 'group' are mutual exclusive
                    """
                    comment: str | None = None
                    direction: DirectionEnum | None = None
                    """
                    Egress or ingress can be the default. This depends on source/destination, EOS version, and hardware platform.
                    EOS might
                    remove this keyword in the configuration. So, check the configuration on targeted HW/SW.
                    """
                    group: int | None = Field(None, ge=1, le=65535)
                    """
                    'access_list' and 'group' are mutual exclusive
                    """
                    original_ip: str = None
                    """
                    IPv4 address
                    """
                    original_port: int | None = Field(None, ge=1, le=65535)
                    priority: int | None = Field(None, ge=0, le=4294967295)
                    protocol: ProtocolEnum | None = None
                    translated_ip: str = None
                    """
                    IPv4 address
                    """
                    translated_port: int | None = Field(None, ge=1, le=65535)
                    """
                    requires 'original_port'
                    """

                dynamic: list[DynamicItem] | None = None
                static: list[StaticItem] | None = None

            class Source(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class DynamicItem(BaseModel):
                    model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                    class NatTypeEnum(Enum):
                        value_0 = "overload"
                        value_1 = "pool"
                        value_2 = "pool-address-only"
                        value_3 = "pool-full-cone"

                    access_list: str = None
                    comment: str | None = None
                    nat_type: NatTypeEnum = None
                    pool_name: str | None = None
                    """
                    required if 'nat_type' is pool, pool-address-only or pool-full-cone
                    ignored if 'nat_type' is overload
                    """
                    priority: int | None = Field(None, ge=0, le=4294967295)

                class StaticItem(BaseModel):
                    model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                    class DirectionEnum(Enum):
                        value_0 = "egress"
                        value_1 = "ingress"

                    class ProtocolEnum(Enum):
                        value_0 = "udp"
                        value_1 = "tcp"

                    access_list: str | None = None
                    """
                    'access_list' and 'group' are mutual exclusive
                    """
                    comment: str | None = None
                    direction: DirectionEnum | None = None
                    """
                    Egress or ingress can be the default. This depends on source/destination, EOS version, and hardware platform.
                    EOS might
                    remove this keyword in the configuration. So, check the configuration on targeted HW/SW.
                    """
                    group: int | None = Field(None, ge=1, le=65535)
                    """
                    'access_list' and 'group' are mutual exclusive
                    """
                    original_ip: str = None
                    """
                    IPv4 address
                    """
                    original_port: int | None = Field(None, ge=1, le=65535)
                    priority: int | None = Field(None, ge=0, le=4294967295)
                    protocol: ProtocolEnum | None = None
                    translated_ip: str = None
                    """
                    IPv4 address
                    """
                    translated_port: int | None = Field(None, ge=1, le=65535)
                    """
                    requires 'original_port'
                    """

                dynamic: list[DynamicItem] | None = None
                static: list[StaticItem] | None = None

            service_profile: str | None = None
            """
            NAT interface profile.
            """
            destination: Destination | None = None
            source: Source | None = None

        class Ipv6NdPrefixesItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            ipv6_prefix: str = None
            valid_lifetime: Annotated[str, StrConvert(convert_types=(int))] | None = None
            """
            Infinite or lifetime in seconds
            """
            preferred_lifetime: Annotated[str, StrConvert(convert_types=(int))] | None = None
            """
            Infinite or lifetime in seconds
            """
            no_autoconfig_flag: bool | None = None

        class Ipv6DhcpRelayDestinationsItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            address: str = None
            """
            DHCP server's IPv6 address
            """
            vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
            local_interface: str | None = None
            """
            Local interface to communicate with DHCP server - mutually exclusive to source_address
            """
            source_address: str | None = None
            """
            Source IPv6 address to communicate with DHCP server - mutually exclusive to local_interface
            """
            link_address: str | None = None
            """
            Override the default link address specified in the relayed DHCP packet
            """

        class Multicast(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Ipv4(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class BoundariesItem(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    boundary: str | None = None
                    """
                    ACL name or multicast IP subnet
                    """
                    out: bool | None = None

                boundaries: list[BoundariesItem] | None = None
                static: bool | None = None

            class Ipv6(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class BoundariesItem(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    boundary: str | None = None
                    """
                    ACL name or multicast IP subnet
                    """

                boundaries: list[BoundariesItem] | None = None
                static: bool | None = None

            ipv4: Ipv4 | None = None
            ipv6: Ipv6 | None = None

        class OspfAuthenticationEnum(Enum):
            value_0 = "none"
            value_1 = "simple"
            value_2 = "message-digest"

        class OspfMessageDigestKeysItem(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class HashAlgorithmEnum(Enum):
                value_0 = "md5"
                value_1 = "sha1"
                value_2 = "sha256"
                value_3 = "sha384"
                value_4 = "sha512"

            id: int = None
            hash_algorithm: HashAlgorithmEnum | None = None
            key: str | None = None
            """
            Encrypted password - only type 7 supported
            """

        class Pim(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Ipv4(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                dr_priority: int | None = Field(None, ge=0, le=429467295)
                sparse_mode: bool | None = None

            ipv4: Ipv4 | None = None

        class MacSecurity(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            profile: str | None = None

        class ChannelGroup(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class ModeEnum(Enum):
                value_0 = "on"
                value_1 = "active"
                value_2 = "passive"

            id: int | None = None
            mode: ModeEnum | None = None

        class IsisCircuitTypeEnum(Enum):
            value_0 = "level-1-2"
            value_1 = "level-1"
            value_2 = "level-2"

        class IsisAuthenticationModeEnum(Enum):
            value_0 = "text"
            value_1 = "md5"

        class Poe(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class PriorityEnum(Enum):
                value_0 = "critical"
                value_1 = "high"
                value_2 = "medium"
                value_3 = "low"

            class Reboot(BaseModel):
                model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                class ActionEnum(Enum):
                    value_0 = "maintain"
                    value_1 = "power-off"

                action: ActionEnum | None = None
                """
                PoE action for interface
                """

            class LinkDown(BaseModel):
                model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                class ActionEnum(Enum):
                    value_0 = "maintain"
                    value_1 = "power-off"

                action: ActionEnum | None = None
                """
                PoE action for interface
                """
                power_off_delay: int | None = Field(None, ge=1, le=86400)
                """
                Number of seconds to delay shutting the power off after a link down event occurs. Default value is 5 seconds in EOS.
                """

            class Shutdown(BaseModel):
                model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                class ActionEnum(Enum):
                    value_0 = "maintain"
                    value_1 = "power-off"

                action: ActionEnum | None = None
                """
                PoE action for interface
                """

            class Limit(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                field_class: int | None = Field(None, alias="class", ge=0, le=8)
                watts: Annotated[str, StrConvert(convert_types=(int, float))] | None = None
                fixed: bool | None = None
                """
                Set to ignore hardware classification
                """

            disabled: bool | None = False
            """
            Disable PoE on a POE capable port. PoE is enabled on all ports that support it by default in EOS.
            """
            priority: PriorityEnum | None = None
            """
            Prioritize a port's power in the event that one of the switch's power supplies loses power
            """
            reboot: Reboot | None = None
            """
            Set the PoE power behavior for a PoE port when the system is rebooted
            """
            link_down: LinkDown | None = None
            """
            Set the PoE power behavior for a PoE port when the port goes down
            """
            shutdown: Shutdown | None = None
            """
            Set the PoE power behavior for a PoE port when the port is admin down
            """
            limit: Limit | None = None
            """
            Override the hardware-negotiated power limit using either wattage or a power class. Note that if using a power class,
            AVD will automatically convert the class value to the wattage value corresponding to that power class.
            """
            negotiation_lldp: bool | None = None
            """
            Disable to prevent port from negotiating power with powered devices over LLDP. Enabled by default in EOS.
            """
            legacy_detect: bool | None = None
            """
            Allow a subset of legacy devices to work with the PoE switch. Disabled by default in EOS because it can cause false
            positive detections.
            """

        class Ptp(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class Announce(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                interval: int | None = None
                timeout: int | None = None

            class DelayMechanismEnum(Enum):
                value_0 = "e2e"
                value_1 = "p2p"

            class SyncMessage(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                interval: int | None = None

            class RoleEnum(Enum):
                value_0 = "master"
                value_1 = "dynamic"

            class TransportEnum(Enum):
                value_0 = "ipv4"
                value_1 = "ipv6"
                value_2 = "layer2"

            enable: bool | None = None
            announce: Announce | None = None
            delay_req: int | None = None
            delay_mechanism: DelayMechanismEnum | None = None
            sync_message: SyncMessage | None = None
            role: RoleEnum | None = None
            vlan: Annotated[str, StrConvert(convert_types=(int))] | None = None
            """
            VLAN can be 'all' or list of vlans as string
            """
            transport: TransportEnum | None = None

        class StormControl(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class All(BaseModel):
                model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                class UnitEnum(Enum):
                    value_0 = "percent"
                    value_1 = "pps"

                level: Annotated[str, StrConvert(convert_types=(int, float))] | None = None
                """
                Configure maximum storm-control level
                """
                unit: UnitEnum | None = "percent"
                """
                Optional field and is hardware dependent
                """

            class Broadcast(BaseModel):
                model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                class UnitEnum(Enum):
                    value_0 = "percent"
                    value_1 = "pps"

                level: Annotated[str, StrConvert(convert_types=(int, float))] | None = None
                """
                Configure maximum storm-control level
                """
                unit: UnitEnum | None = "percent"
                """
                Optional field and is hardware dependent
                """

            class Multicast(BaseModel):
                model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                class UnitEnum(Enum):
                    value_0 = "percent"
                    value_1 = "pps"

                level: Annotated[str, StrConvert(convert_types=(int, float))] | None = None
                """
                Configure maximum storm-control level
                """
                unit: UnitEnum | None = "percent"
                """
                Optional field and is hardware dependent
                """

            class UnknownUnicast(BaseModel):
                model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                class UnitEnum(Enum):
                    value_0 = "percent"
                    value_1 = "pps"

                level: Annotated[str, StrConvert(convert_types=(int, float))] | None = None
                """
                Configure maximum storm-control level
                """
                unit: UnitEnum | None = "percent"
                """
                Optional field and is hardware dependent
                """

            all: All | None = None
            broadcast: Broadcast | None = None
            multicast: Multicast | None = None
            unknown_unicast: UnknownUnicast | None = None

        class Logging(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Event(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                link_status: bool | None = None
                congestion_drops: bool | None = None
                spanning_tree: bool | None = None
                storm_control_discards: bool | None = None

            event: Event | None = None

        class Lldp(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            transmit: bool | None = None
            receive: bool | None = None
            ztp_vlan: int | None = None
            """
            ZTP vlan number
            """

        class VlanTranslationsItem(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class DirectionEnum(Enum):
                value_0 = "in"
                value_1 = "out"
                value_2 = "both"

            field_from: Annotated[str, StrConvert(convert_types=(int))] | None = Field(None, alias="from")
            """
            List of vlans as string (only one vlan if direction is "both")
            """
            to: int | None = None
            """
            VLAN ID
            """
            direction: DirectionEnum | None = "both"

        class Dot1x(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class PortControlEnum(Enum):
                value_0 = "auto"
                value_1 = "force-authorized"
                value_2 = "force-unauthorized"

            class Pae(BaseModel):
                model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                class ModeEnum(Enum):
                    value_0 = "authenticator"

                mode: ModeEnum | None = None

            class AuthenticationFailure(BaseModel):
                model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                class ActionEnum(Enum):
                    value_0 = "allow"
                    value_1 = "drop"

                action: ActionEnum | None = None
                allow_vlan: int | None = Field(None, ge=1, le=4094)

            class HostMode(BaseModel):
                model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                class ModeEnum(Enum):
                    value_0 = "multi-host"
                    value_1 = "single-host"

                mode: ModeEnum | None = None
                multi_host_authenticated: bool | None = None

            class MacBasedAuthentication(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                enabled: bool | None = None
                always: bool | None = None
                host_mode_common: bool | None = None

            class Timeout(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                idle_host: int | None = Field(None, ge=10, le=65535)
                quiet_period: int | None = Field(None, ge=1, le=65535)
                reauth_period: Annotated[str, StrConvert(convert_types=(int))] | None = None
                """
                Value can be 60-4294967295 or 'server'
                """
                reauth_timeout_ignore: bool | None = None
                tx_period: int | None = Field(None, ge=1, le=65535)

            class Unauthorized(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                access_vlan_membership_egress: bool | None = None
                native_vlan_membership_egress: bool | None = None

            class Eapol(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class AuthenticationFailureFallbackMba(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    enabled: bool | None = None
                    timeout: int | None = Field(None, ge=0, le=65535)

                disabled: bool | None = None
                authentication_failure_fallback_mba: AuthenticationFailureFallbackMba | None = None

            port_control: PortControlEnum | None = None
            port_control_force_authorized_phone: bool | None = None
            reauthentication: bool | None = None
            pae: Pae | None = None
            authentication_failure: AuthenticationFailure | None = None
            host_mode: HostMode | None = None
            mac_based_authentication: MacBasedAuthentication | None = None
            timeout: Timeout | None = None
            reauthorization_request_limit: int | None = Field(None, ge=1, le=10)
            unauthorized: Unauthorized | None = None
            eapol: Eapol | None = None

        class Shape(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            rate: str | None = None
            """
            Rate in kbps, pps or percent
            Supported options are platform dependent
            Examples:
            - "5000 kbps"
            - "1000 pps"
            - "20
            percent"
            """

        class Qos(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class TrustEnum(Enum):
                value_0 = "dscp"
                value_1 = "cos"
                value_2 = "disabled"

            trust: TrustEnum | None = None
            dscp: int | None = None
            """
            DSCP value
            """
            cos: int | None = None
            """
            COS value
            """

        class SpanningTreeBpdufilterEnum(Enum):
            value_0 = "enabled"
            value_1 = "disabled"
            value_2 = "True"
            value_3 = "False"
            value_4 = "true"
            value_5 = "false"

        class SpanningTreeBpduguardEnum(Enum):
            value_0 = "enabled"
            value_1 = "disabled"
            value_2 = "True"
            value_3 = "False"
            value_4 = "true"
            value_5 = "false"

        class SpanningTreeGuardEnum(Enum):
            value_0 = "loop"
            value_1 = "root"
            value_2 = "disabled"

        class SpanningTreePortfastEnum(Enum):
            value_0 = "edge"
            value_1 = "network"

        class PriorityFlowControl(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class PrioritiesItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                priority: int = Field(None, ge=0, le=7)
                no_drop: bool | None = None

            enabled: bool | None = None
            priorities: list[PrioritiesItem] | None = None

        class Bfd(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            echo: bool | None = None
            interval: int | None = None
            """
            Interval in milliseconds
            """
            min_rx: int | None = None
            """
            Rate in milliseconds
            """
            multiplier: int | None = Field(None, ge=3, le=50)

        class ServicePolicy(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Pbr(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                input: str | None = None
                """
                Policy Based Routing Policy-map name
                """

            class Qos(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                input: str = None
                """
                Quality of Service Policy-map name
                """

            pbr: Pbr | None = None
            qos: Qos | None = None

        class Mpls(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Ldp(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                interface: bool | None = None
                igp_sync: bool | None = None

            ip: bool | None = None
            ldp: Ldp | None = None

        class LacpTimer(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class ModeEnum(Enum):
                value_0 = "fast"
                value_1 = "normal"

            mode: ModeEnum | None = None
            multiplier: int | None = Field(None, ge=3, le=3000)

        class Transceiver(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Media(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                override: str | None = None
                """
                Transceiver type
                """

            media: Media | None = None

        class TrafficPolicy(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            input: str | None = None
            """
            Ingress traffic policy
            """
            output: str | None = None
            """
            Egress traffic policy
            """

        class Bgp(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            session_tracker: str | None = None
            """
            Name of session tracker
            """

        class Sflow(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Egress(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                enable: bool | None = None
                unmodified_enable: bool | None = None

            enable: bool | None = None
            egress: Egress | None = None

        class UcTxQueuesItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class RandomDetect(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Ecn(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class Threshold(BaseModel):
                        model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                        class UnitsEnum(Enum):
                            value_0 = "segments"
                            value_1 = "bytes"
                            value_2 = "kbytes"
                            value_3 = "mbytes"
                            value_4 = "milliseconds"

                        units: UnitsEnum = None
                        """
                        Indicate the units to be used for the threshold values
                        """
                        min: int = Field(None, ge=1, le=256000000)
                        """
                        Set the random-detect ECN minimum-threshold
                        """
                        max: int = Field(None, ge=1, le=256000000)
                        """
                        Set the random-detect ECN maximum-threshold
                        """
                        max_probability: int | None = Field(None, ge=1, le=100)
                        """
                        Set the random-detect ECN max-mark-probability
                        """
                        weight: int | None = Field(None, ge=0, le=15)
                        """
                        Set the random-detect ECN weight
                        """

                    count: bool | None = None
                    """
                    Enable counter for random-detect ECNs
                    """
                    threshold: Threshold | None = None

                ecn: Ecn | None = None
                """
                Explicit Congestion Notification
                """

            id: int = None
            """
            TX-Queue ID
            """
            random_detect: RandomDetect | None = None

        class TxQueuesItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class RandomDetect(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Ecn(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class Threshold(BaseModel):
                        model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                        class UnitsEnum(Enum):
                            value_0 = "segments"
                            value_1 = "bytes"
                            value_2 = "kbytes"
                            value_3 = "mbytes"
                            value_4 = "milliseconds"

                        units: UnitsEnum = None
                        """
                        Indicate the units to be used for the threshold values
                        """
                        min: int | None = Field(None, ge=1, le=256000000)
                        """
                        Set the random-detect ECN minimum-threshold
                        """
                        max: int = Field(None, ge=1, le=256000000)
                        """
                        Set the random-detect ECN maximum-threshold
                        """
                        max_probability: int = Field(None, ge=1, le=100)
                        """
                        Set the random-detect ECN max-mark-probability
                        """
                        weight: int | None = Field(None, ge=0, le=15)
                        """
                        Set the random-detect ECN weight
                        """

                    count: bool | None = None
                    """
                    Enable counter for random-detect ECNs
                    """
                    threshold: Threshold | None = None

                ecn: Ecn | None = None
                """
                Explicit Congestion Notification
                """

            id: int = None
            """
            TX-Queue ID
            """
            random_detect: RandomDetect | None = None

        class VrrpIdsItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Advertisement(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                interval: int | None = Field(None, ge=1, le=255)
                """
                Interval in seconds
                """

            class Preempt(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Delay(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    minimum: int | None = Field(None, ge=0, le=3600)
                    """
                    Minimum preempt delay in seconds
                    """
                    reload: int | None = Field(None, ge=0, le=3600)
                    """
                    Reload preempt delay in seconds
                    """

                enabled: bool = None
                delay: Delay | None = None

            class Timers(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Delay(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    reload: int | None = Field(None, ge=0, le=3600)
                    """
                    Delay after reload in seconds.
                    """

                delay: Delay | None = None

            class TrackedObjectItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                name: str = None
                """
                Tracked object name
                """
                decrement: int | None = Field(None, ge=1, le=254)
                """
                Decrement VRRP priority by 1-254
                """
                shutdown: bool | None = None

            class Ipv4(BaseModel):
                model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                class VersionEnum(Enum):
                    value_0 = 2
                    value_1 = 3

                address: str = None
                """
                Virtual IPv4 address
                """
                version: VersionEnum | None = None

            class Ipv6(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                address: str = None
                """
                Virtual IPv6 address
                """

            id: int = None
            """
            VRID
            """
            priority_level: int | None = Field(None, ge=1, le=254)
            """
            Instance priority
            """
            advertisement: Advertisement | None = None
            preempt: Preempt | None = None
            timers: Timers | None = None
            tracked_object: list[TrackedObjectItem] | None = None
            ipv4: Ipv4 | None = None
            ipv6: Ipv6 | None = None

        name: str = None
        description: str | None = None
        shutdown: bool | None = None
        load_interval: int | None = Field(None, ge=0, le=600)
        """
        Interval in seconds for updating interface counters"
        """
        speed: str | None = None
        """
        Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`.
        """
        mtu: int | None = None
        l2_mtu: int | None = None
        """
        "l2_mtu" should only be defined for platforms supporting the "l2 mtu" CLI
        """
        vlans: Annotated[str, StrConvert(convert_types=(int))] | None = None
        """
        List of switchport vlans as string
        For a trunk port this would be a range like "1-200,300"
        For an access port this would
        be a single vlan "123"
        """
        native_vlan: int | None = None
        native_vlan_tag: bool | None = None
        """
        If setting both native_vlan and native_vlan_tag, native_vlan_tag takes precedence
        """
        mode: ModeEnum | None = None
        phone: Phone | None = None
        l2_protocol: L2Protocol | None = None
        trunk_groups: list[str] | None = None
        type: TypeEnum | None = None
        """
        l3dot1q and l2dot1q are used for sub-interfaces. The parent interface should be defined as routed.
        Interface will not be
        listed in device documentation, unless "type" is set.
        """
        snmp_trap_link_change: bool | None = None
        address_locking: AddressLocking | None = None
        flowcontrol: Flowcontrol | None = None
        vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
        """
        VRF name
        """
        flow_tracker: FlowTracker | None = None
        error_correction_encoding: ErrorCorrectionEncoding | None = None
        link_tracking_groups: list[LinkTrackingGroupsItem] | None = None
        evpn_ethernet_segment: EvpnEthernetSegment | None = None
        encapsulation_dot1q_vlan: int | None = None
        """
        VLAN tag to configure on sub-interface
        """
        encapsulation_vlan: EncapsulationVlan | None = None
        vlan_id: int | None = Field(None, ge=1, le=4094)
        ip_address: str | None = None
        """
        IPv4 address/mask or "dhcp"
        """
        ip_address_secondaries: list[str] | None = None
        dhcp_client_accept_default_route: bool | None = None
        """
        Install default-route obtained via DHCP
        """
        dhcp_server_ipv4: bool | None = None
        """
        Enable IPv4 DHCP server.
        """
        dhcp_server_ipv6: bool | None = None
        """
        Enable IPv6 DHCP server.
        """
        ip_helpers: list[IpHelpersItem] | None = None
        ip_nat: IpNat | None = None
        ipv6_enable: bool | None = None
        ipv6_address: str | None = None
        ipv6_address_link_local: str | None = None
        """
        Link local IPv6 address/mask
        """
        ipv6_nd_ra_disabled: bool | None = None
        ipv6_nd_managed_config_flag: bool | None = None
        ipv6_nd_prefixes: list[Ipv6NdPrefixesItem] | None = None
        ipv6_dhcp_relay_destinations: list[Ipv6DhcpRelayDestinationsItem] | None = None
        access_group_in: str | None = None
        """
        Access list name
        """
        access_group_out: str | None = None
        """
        Access list name
        """
        ipv6_access_group_in: str | None = None
        """
        IPv6 access list name
        """
        ipv6_access_group_out: str | None = None
        """
        IPv6 access list name
        """
        mac_access_group_in: str | None = None
        """
        MAC access list name
        """
        mac_access_group_out: str | None = None
        """
        MAC access list name
        """
        multicast: Multicast | None = None
        """
        Boundaries can be either 1 ACL or a list of multicast IP address_range(s)/prefix but not combination of both
        """
        ospf_network_point_to_point: bool | None = None
        ospf_area: Annotated[str, StrConvert(convert_types=(int))] | None = None
        ospf_cost: int | None = None
        ospf_authentication: OspfAuthenticationEnum | None = None
        ospf_authentication_key: str | None = None
        """
        Encrypted password - only type 7 supported
        """
        ospf_message_digest_keys: list[OspfMessageDigestKeysItem] | None = None
        pim: Pim | None = None
        mac_security: MacSecurity | None = None
        channel_group: ChannelGroup | None = None
        isis_enable: str | None = None
        """
        ISIS instance
        """
        isis_passive: bool | None = None
        isis_metric: int | None = None
        isis_network_point_to_point: bool | None = None
        isis_circuit_type: IsisCircuitTypeEnum | None = None
        isis_hello_padding: bool | None = None
        isis_authentication_mode: IsisAuthenticationModeEnum | None = None
        isis_authentication_key: str | None = None
        """
        Type-7 encrypted password
        """
        poe: Poe | None = None
        ptp: Ptp | None = None
        profile: str | None = None
        """
        Interface profile
        """
        storm_control: StormControl | None = None
        logging: Logging | None = None
        lldp: Lldp | None = None
        trunk_private_vlan_secondary: bool | None = None
        pvlan_mapping: Annotated[str, StrConvert(convert_types=(int))] | None = None
        """
        List of vlans as string
        """
        vlan_translations: list[VlanTranslationsItem] | None = None
        dot1x: Dot1x | None = None
        service_profile: str | None = None
        """
        QOS profile
        """
        shape: Shape | None = None
        qos: Qos | None = None
        spanning_tree_bpdufilter: Annotated[SpanningTreeBpdufilterEnum, StrConvert(convert_types=(bool))] | None = None
        spanning_tree_bpduguard: Annotated[SpanningTreeBpduguardEnum, StrConvert(convert_types=(bool))] | None = None
        spanning_tree_guard: SpanningTreeGuardEnum | None = None
        spanning_tree_portfast: SpanningTreePortfastEnum | None = None
        vmtracer: bool | None = None
        priority_flow_control: PriorityFlowControl | None = None
        bfd: Bfd | None = None
        service_policy: ServicePolicy | None = None
        mpls: Mpls | None = None
        lacp_timer: LacpTimer | None = None
        lacp_port_priority: int | None = Field(None, ge=0, le=65535)
        transceiver: Transceiver | None = None
        ip_proxy_arp: bool | None = None
        traffic_policy: TrafficPolicy | None = None
        bgp: Bgp | None = None
        peer: str | None = None
        """
        Key only used for documentation or validation purposes
        """
        peer_interface: str | None = None
        """
        Key only used for documentation or validation purposes
        """
        peer_type: str | None = None
        """
        Key only used for documentation or validation purposes
        """
        sflow: Sflow | None = None
        port_profile: str | None = None
        """
        Key only used for documentation or validation purposes
        """
        uc_tx_queues: list[UcTxQueuesItem] | None = None
        tx_queues: list[TxQueuesItem] | None = None
        vrrp_ids: list[VrrpIdsItem] | None = None
        """
        VRRP model.
        """
        eos_cli: str | None = None
        """
        Multiline EOS CLI rendered directly on the ethernet interface in the final EOS configuration
        """

    class EventHandlersItem(BaseModel):
        model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

        class ActionTypeEnum(Enum):
            value_0 = "bash"
            value_1 = "increment"
            value_2 = "log"

        class TriggerEnum(Enum):
            value_0 = "on-boot"
            value_1 = "on-logging"
            value_2 = "on-startup-config"

        name: str = None
        """
        Event Handler Name
        """
        action_type: ActionTypeEnum | None = None
        action: str | None = None
        """
        Command to execute
        """
        delay: int | None = None
        """
        Event-handler delay in seconds
        """
        trigger: TriggerEnum | None = None
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

    class EventMonitor(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        enabled: bool | None = None

    class FlowTracking(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Sampled(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class TrackersItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class RecordExport(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    mpls: bool | None = None
                    """
                    Export MPLS forwarding information
                    """
                    on_inactive_timeout: int | None = Field(None, ge=3000, le=900000)
                    """
                    Flow record inactive export timeout in milliseconds
                    """
                    on_interval: int | None = Field(None, ge=1000, le=36000000)
                    """
                    Flow record export interval in milliseconds
                    """

                class ExportersItem(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class Collector(BaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        host: str | None = None
                        """
                        Collector IPv4 address or IPv6 address or fully qualified domain name
                        """
                        port: int | None = Field(None, ge=1, le=65535)
                        """
                        Collector Port Number
                        """

                    class Format(BaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        ipfix_version: int | None = None

                    name: str = None
                    """
                    Exporter Name
                    """
                    collector: Collector | None = None
                    format: Format | None = None
                    local_interface: str | None = None
                    """
                    Local Source Interface
                    """
                    template_interval: int | None = Field(None, ge=5000, le=3600000)
                    """
                    Template interval in milliseconds
                    """

                table_size: int | None = Field(None, ge=1, le=614400)
                """
                Maximum number of entries in flow table.
                """
                record_export: RecordExport | None = None
                name: str = None
                """
                Tracker Name
                """
                exporters: list[ExportersItem] | None = None

            sample: int | None = Field(None, ge=1, le=4294967295)
            trackers: list[TrackersItem] | None = None
            shutdown: bool | None = False

        class Hardware(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class TrackersItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class RecordExport(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    on_inactive_timeout: int | None = Field(None, ge=3000, le=900000)
                    """
                    Flow record inactive export timeout in milliseconds
                    """
                    on_interval: int | None = Field(None, ge=1000, le=36000000)
                    """
                    Flow record export interval in milliseconds
                    """

                class ExportersItem(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class Collector(BaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        host: str | None = None
                        """
                        Collector IPv4 address or IPv6 address or fully qualified domain name
                        """
                        port: int | None = Field(None, ge=1, le=65535)
                        """
                        Collector Port Number
                        """

                    class Format(BaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        ipfix_version: int | None = None

                    name: str = None
                    """
                    Exporter Name
                    """
                    collector: Collector | None = None
                    format: Format | None = None
                    local_interface: str | None = None
                    """
                    Local Source Interface
                    """
                    template_interval: int | None = Field(None, ge=5000, le=3600000)
                    """
                    Template interval in milliseconds
                    """

                name: str = None
                """
                Tracker Name
                """
                record_export: RecordExport | None = None
                exporters: list[ExportersItem] | None = None

            trackers: list[TrackersItem] | None = None
            shutdown: bool | None = False

        sampled: Sampled | None = None
        hardware: Hardware | None = None

    class FlowTrackingsItem(BaseModel):
        model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

        class TypeEnum(Enum):
            value_0 = "sampled"

        class TrackersItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class RecordExport(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                on_inactive_timeout: int | None = Field(None, ge=3000, le=900000)
                """
                Flow record inactive export timeout in milliseconds
                """
                on_interval: int | None = Field(None, ge=1000, le=36000000)
                """
                Flow record export interval in milliseconds
                """
                mpls: bool | None = None
                """
                Export MPLS forwarding information
                """

            class ExportersItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Collector(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    host: str | None = None
                    """
                    Collector IPv4 address or IPv6 address or fully qualified domain name
                    """
                    port: int | None = Field(None, ge=1, le=65535)
                    """
                    Collector Port Number
                    """

                class Format(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    ipfix_version: int | None = None

                name: str = None
                """
                Exporter Name
                """
                collector: Collector | None = None
                format: Format | None = None
                local_interface: str | None = None
                """
                Local Source Interface
                """
                template_interval: int | None = Field(None, ge=5000, le=3600000)
                """
                Template interval in milliseconds
                """

            name: str = None
            """
            Tracker Name
            """
            record_export: RecordExport | None = None
            exporters: list[ExportersItem] | None = None
            table_size: int | None = Field(None, ge=1, le=614400)
            """
            Maximum number of entries in flow table.
            """

        type: TypeEnum = None
        """
        Flow Tracking Type - only 'sampled' supported for now
        """
        sample: int | None = Field(None, ge=1, le=4294967295)
        trackers: list[TrackersItem] | None = None
        shutdown: bool | None = False

    class Hardware(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class AccessList(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class MechanismEnum(Enum):
                value_0 = "algomatch"
                value_1 = "none"
                value_2 = "tcam"

            mechanism: MechanismEnum | None = None

        class SpeedGroupsItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            speed_group: Annotated[str, StrConvert(convert_types=(int))] = None
            serdes: str | None = None
            """
            Serdes speed like "10g" or "25g"
            """

        access_list: AccessList | None = None
        speed_groups: list[SpeedGroupsItem] | None = None

    class HardwareCounters(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class FeaturesItem(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class NameEnum(Enum):
                value_0 = "acl"
                value_1 = "decap-group"
                value_2 = "directflow"
                value_3 = "ecn"
                value_4 = "flow-spec"
                value_5 = "gre tunnel interface"
                value_6 = "ip"
                value_7 = "mpls interface"
                value_8 = "mpls lfib"
                value_9 = "mpls tunnel"
                value_10 = "multicast"
                value_11 = "nexthop"
                value_12 = "pbr"
                value_13 = "pdp"
                value_14 = "policing interface"
                value_15 = "qos"
                value_16 = "qos dual-rate-policer"
                value_17 = "route"
                value_18 = "routed-port"
                value_19 = "subinterface"
                value_20 = "tapagg"
                value_21 = "traffic-class"
                value_22 = "traffic-policy"
                value_23 = "vlan"
                value_24 = "vlan-interface"
                value_25 = "vni decap"
                value_26 = "vni encap"
                value_27 = "vtep decap"
                value_28 = "vtep encap"

            class DirectionEnum(Enum):
                value_0 = "in"
                value_1 = "out"
                value_2 = "cpu"

            class AddressTypeEnum(Enum):
                value_0 = "ipv4"
                value_1 = "ipv6"
                value_2 = "mac"

            name: NameEnum | None = None
            direction: DirectionEnum | None = None
            """
            Most features support only 'in' and 'out'. Some like traffic-policy support 'cpu'.
            Some features DO NOT have any
            direction.
            This validation IS NOT made by the schemas.
            """
            address_type: AddressTypeEnum | None = None
            """
            Supported only for the following features:
            - acl: [ipv4, ipv6, mac] if direction is 'out'
            - multicast: [ipv4, ipv6]
            -
            route: [ipv4, ipv6]
            This validation IS NOT made by the schemas.
            """
            layer3: bool | None = None
            """
            Supported only for the 'ip' feature
            """
            vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
            """
            Supported only for the 'route' feature.
            This validation IS NOT made by the schemas.
            """
            prefix: str | None = None
            """
            Supported only for the 'route' feature.
            Mandatory for the 'route' feature.
            This validation IS NOT made by the schemas.
            """
            units_packets: bool | None = None

        features: list[FeaturesItem] | None = None
        """
        This data model allows to configure the list of hardware counters feature
        available on Arista platforms.

        The `name` key
        accepts a list of valid_values which MUST be updated to support
        new feature as they are released in EOS.

        The available
        values of the different keys like 'direction' or 'address_type'
        are feature and hardware dependent and this model DOES
        NOT validate that the
        combinations are valid. It is the responsability of the user of this data model
        to make sure that
        the rendered CLI is accepted by the targeted device.

        Examples:

          * Use:
            ```yaml
            hardware_counters:
        features:
                - name: ip
                  direction: out
                  layer3: true
                  units_packets: true
            ```
        to render:
            ```eos
            hardware counter feature ip out layer3 units packets
            ```
          * Use:
            ```yaml
        hardware_counters:
              features:
                - name: route
                  address_type: ipv4
                  vrf: test
        prefix: 192.168.0.0/24
            ```

            to render:
            ```eos
            hardware counter feature route ipv4 vrf test
        192.168.0.0/24
            ```
        """

    class InterfaceDefaults(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Ethernet(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            shutdown: bool | None = None

        ethernet: Ethernet | None = None
        mtu: int | None = None

    class InterfaceGroupsItem(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        name: str = None
        """
        Interface-Group name
        """
        interfaces: list[str] | None = None
        bgp_maintenance_profiles: list[str] | None = None
        interface_maintenance_profiles: list[str] | None = None

    class InterfaceProfilesItem(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        name: str = None
        """
        Interface-Profile Name
        """
        commands: list[str] = None

    class IpAccessListsItem(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class EntriesItem(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class ActionEnum(Enum):
                value_0 = "permit"
                value_1 = "deny"

            class SourcePortsMatchEnum(Enum):
                value_0 = "eq"
                value_1 = "gt"
                value_2 = "lt"
                value_3 = "neq"
                value_4 = "range"

            class DestinationPortsMatchEnum(Enum):
                value_0 = "eq"
                value_1 = "gt"
                value_2 = "lt"
                value_3 = "neq"
                value_4 = "range"

            class TtlMatchEnum(Enum):
                value_0 = "eq"
                value_1 = "gt"
                value_2 = "lt"
                value_3 = "neq"

            sequence: int | None = None
            """
            ACL entry sequence number.
            """
            remark: str | None = None
            """
            Comment up to 100 characters.
            If remark is defined, other keys in acl entry will be ignored.
            """
            action: ActionEnum | None = None
            """
            ACL action.
            Required for standard entry.
            """
            protocol: str | None = None
            """
            ip, tcp, udp, icmp or other protocol name or number.
            Required for standard entry.
            """
            source: str | None = None
            """
            any, A.B.C.D/E or A.B.C.D.
            A.B.C.D without a mask means host.
            Required for standard entry.
            """
            source_ports_match: SourcePortsMatchEnum | None = "eq"
            source_ports: list[Annotated[str, StrConvert(convert_types=(int))]] | None = None
            destination: str | None = None
            """
            any, A.B.C.D/E or A.B.C.D.
            A.B.C.D without a mask means host.
            Required for standard entry.
            """
            destination_ports_match: DestinationPortsMatchEnum | None = "eq"
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
            ttl: int | None = Field(None, ge=0, le=255)
            """
            TTL value
            """
            ttl_match: TtlMatchEnum | None = "eq"
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
            vlan_number: int | None = None
            vlan_inner: bool | None = False
            vlan_mask: str | None = None
            """
            0x000-0xFFF VLAN mask.
            """

        name: str = None
        """
        Access-list Name
        """
        counters_per_entry: bool | None = None
        entries: list[EntriesItem] | None = None
        """
        ACL Entries
        """

    class IpCommunityListsItem(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class EntriesItem(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class ActionEnum(Enum):
                value_0 = "permit"
                value_1 = "deny"

            action: ActionEnum = None
            communities: list[str] | None = None
            """
            If defined, a standard community-list will be configured.
            Supported community strings (case insensitive):
            - GSHUT
            -
            internet
            - local-as
            - no-advertise
            - no-export
            - <1-4294967040>
            - aa:nn
            """
            regexp: str | None = None
            """
            Regular Expression
            If defined, a regex community-list will be configured
            """

        name: str = None
        """
        IP Community-list Name
        """
        entries: list[EntriesItem] = None

    class IpDhcpRelay(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        information_option: bool | None = None
        """
        Insert Option-82 information
        """

    class IpDomainLookup(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class SourceInterfacesItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str = None
            """
            Source Interface
            """
            vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None

        source_interfaces: list[SourceInterfacesItem] | None = None

    class IpExtcommunityListsItem(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class EntriesItem(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class TypeEnum(Enum):
                value_0 = "permit"
                value_1 = "deny"

            type: TypeEnum = None
            extcommunities: str = None
            """
            Communities as string
            Example: "65000:65000"
            """

        name: str = None
        """
        Community-list Name
        """
        entries: list[EntriesItem] = None

    class IpExtcommunityListsRegexpItem(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class EntriesItem(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class TypeEnum(Enum):
                value_0 = "permit"
                value_1 = "deny"

            type: TypeEnum = None
            regexp: str = None
            """
            Regular Expression
            """

        name: str = None
        """
        Community-list Name
        """
        entries: list[EntriesItem] = None

    class IpHardware(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Fib(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Optimize(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Prefixes(BaseModel):
                    model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                    class ProfileEnum(Enum):
                        value_0 = "internet"
                        value_1 = "urpf-internet"

                    profile: ProfileEnum | None = None

                prefixes: Prefixes | None = None

            optimize: Optimize | None = None

        fib: Fib | None = None

    class IpHttpClientSourceInterfacesItem(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        name: str | None = None
        """
        Interface Name
        """
        vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None

    class IpIgmpSnooping(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Querier(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            enabled: bool | None = None
            address: str | None = None
            """
            IP Address
            """
            query_interval: int | None = None
            max_response_time: int | None = None
            last_member_query_interval: int | None = None
            last_member_query_count: int | None = None
            startup_query_interval: int | None = None
            startup_query_count: int | None = None
            version: int | None = None

        class VlansItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Querier(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                enabled: bool | None = None
                address: str | None = None
                """
                IP Address
                """
                query_interval: int | None = None
                max_response_time: int | None = None
                last_member_query_interval: int | None = None
                last_member_query_count: int | None = None
                startup_query_interval: int | None = None
                startup_query_count: int | None = None
                version: int | None = None

            id: int = None
            """
            VLAN ID
            """
            enabled: bool | None = None
            querier: Querier | None = None
            max_groups: int | None = None
            fast_leave: bool | None = None
            proxy: bool | None = None
            """
            Global proxy settings should be enabled before enabling per-vlan
            """

        globally_enabled: bool | None = True
        """
        Activate or deactivate IGMP snooping for all vlans where `vlans` allows user to activate / deactivate IGMP snooping per
        vlan.
        """
        robustness_variable: int | None = None
        restart_query_interval: int | None = None
        interface_restart_query: int | None = None
        fast_leave: bool | None = None
        querier: Querier | None = None
        proxy: bool | None = None
        vlans: list[VlansItem] | None = None

    class IpNameServersItem(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        ip_address: str | None = None
        """
        IPv4 or IPv6 address for DNS server
        """
        vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
        """
        VRF Name
        """
        priority: int | None = Field(None, ge=0, le=4)
        """
        Priority value (lower is first)
        """

    class IpNat(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class ProfilesItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Destination(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class DynamicItem(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    access_list: str = None
                    comment: str | None = None
                    pool_name: str = None
                    priority: int | None = Field(None, ge=0, le=4294967295)

                class StaticItem(BaseModel):
                    model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                    class DirectionEnum(Enum):
                        value_0 = "egress"
                        value_1 = "ingress"

                    class ProtocolEnum(Enum):
                        value_0 = "udp"
                        value_1 = "tcp"

                    access_list: str | None = None
                    """
                    'access_list' and 'group' are mutual exclusive
                    """
                    comment: str | None = None
                    direction: DirectionEnum | None = None
                    """
                    Egress or ingress can be the default. This depends on source/destination, EOS version, and hardware platform.
                    EOS might
                    remove this keyword in the configuration. So, check the configuration on targeted HW/SW.
                    """
                    group: int | None = Field(None, ge=1, le=65535)
                    """
                    'access_list' and 'group' are mutual exclusive
                    """
                    original_ip: str = None
                    """
                    IPv4 address
                    """
                    original_port: int | None = Field(None, ge=1, le=65535)
                    priority: int | None = Field(None, ge=0, le=4294967295)
                    protocol: ProtocolEnum | None = None
                    translated_ip: str = None
                    """
                    IPv4 address
                    """
                    translated_port: int | None = Field(None, ge=1, le=65535)
                    """
                    requires 'original_port'
                    """

                dynamic: list[DynamicItem] | None = None
                static: list[StaticItem] | None = None

            class Source(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class DynamicItem(BaseModel):
                    model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                    class NatTypeEnum(Enum):
                        value_0 = "overload"
                        value_1 = "pool"
                        value_2 = "pool-address-only"
                        value_3 = "pool-full-cone"

                    access_list: str = None
                    comment: str | None = None
                    nat_type: NatTypeEnum = None
                    pool_name: str | None = None
                    """
                    required if 'nat_type' is pool, pool-address-only or pool-full-cone
                    ignored if 'nat_type' is overload
                    """
                    priority: int | None = Field(None, ge=0, le=4294967295)

                class StaticItem(BaseModel):
                    model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                    class DirectionEnum(Enum):
                        value_0 = "egress"
                        value_1 = "ingress"

                    class ProtocolEnum(Enum):
                        value_0 = "udp"
                        value_1 = "tcp"

                    access_list: str | None = None
                    """
                    'access_list' and 'group' are mutual exclusive
                    """
                    comment: str | None = None
                    direction: DirectionEnum | None = None
                    """
                    Egress or ingress can be the default. This depends on source/destination, EOS version, and hardware platform.
                    EOS might
                    remove this keyword in the configuration. So, check the configuration on targeted HW/SW.
                    """
                    group: int | None = Field(None, ge=1, le=65535)
                    """
                    'access_list' and 'group' are mutual exclusive
                    """
                    original_ip: str = None
                    """
                    IPv4 address
                    """
                    original_port: int | None = Field(None, ge=1, le=65535)
                    priority: int | None = Field(None, ge=0, le=4294967295)
                    protocol: ProtocolEnum | None = None
                    translated_ip: str = None
                    """
                    IPv4 address
                    """
                    translated_port: int | None = Field(None, ge=1, le=65535)
                    """
                    requires 'original_port'
                    """

                dynamic: list[DynamicItem] | None = None
                static: list[StaticItem] | None = None

            name: str = None
            vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
            """
            Specify VRF for NAT profile.
            """
            destination: Destination | None = None
            source: Source | None = None

        class PoolsItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class RangesItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                first_ip: str = None
                """
                IPv4 address
                """
                last_ip: str = None
                """
                IPv4 address
                """
                first_port: int | None = Field(None, ge=1, le=65535)
                last_port: int | None = Field(None, ge=1, le=65535)

            name: str = None
            prefix_length: int = Field(None, ge=16, le=32)
            ranges: list[RangesItem] | None = None
            utilization_log_threshold: int | None = Field(None, ge=1, le=100)

        class Synchronization(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class PortRange(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                first_port: int | None = Field(None, ge=1024, le=65535)
                last_port: int | None = Field(None, ge=1024, le=65535)
                """
                >= first_port
                """
                split_disabled: bool | None = None

            description: str | None = None
            expiry_interval: int | None = Field(None, ge=60, le=3600)
            """
            in seconds
            """
            local_interface: str | None = None
            """
            EOS interface name
            """
            peer_address: str | None = None
            """
            IPv4 address
            """
            port_range: PortRange | None = None
            shutdown: bool | None = None

        class Translation(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class AddressSelection(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                any: bool | None = None
                hash_field_source_ip: bool | None = None

            class LowMark(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                percentage: int | None = Field(None, ge=1, le=99)
                """
                Used to render 'ip nat translation low-mark <percentage>'
                """
                host_percentage: int | None = Field(None, ge=1, le=99)
                """
                Used to render 'ip nat translation low-mark <host_percentage> host'
                """

            class MaxEntries(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class IpLimitsItem(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    ip: str = None
                    """
                    IPv4 address
                    """
                    limit: int = Field(None, ge=0, le=4294967295)

                limit: int | None = Field(None, ge=0, le=4294967295)
                host_limit: int | None = Field(None, ge=0, le=4294967295)
                ip_limits: list[IpLimitsItem] | None = None

            class TimeoutsItem(BaseModel):
                model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                class ProtocolEnum(Enum):
                    value_0 = "tcp"
                    value_1 = "udp"

                protocol: ProtocolEnum = None
                timeout: int = Field(None, ge=0, le=4294967295)
                """
                in seconds
                """

            address_selection: AddressSelection | None = None
            counters: bool | None = None
            low_mark: LowMark | None = None
            max_entries: MaxEntries | None = None
            timeouts: list[TimeoutsItem] | None = None

        kernel_buffer_size: int | None = Field(None, ge=1, le=64)
        """
        Buffer size in MB
        """
        profiles: list[ProfilesItem] | None = None
        pools: list[PoolsItem] | None = None
        synchronization: Synchronization | None = None
        translation: Translation | None = None

    class IpRadiusSourceInterfacesItem(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        name: str | None = None
        """
        Interface Name
        """
        vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
        """
        VRF Name
        """

    class IpSecurity(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class IkePoliciesItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str = None
            """
            Policy name.
            """
            local_id: str | None = None
            """
            Local IKE Identification.
            Can be an IPv4 or an IPv6 address.
            """

        class SaPoliciesItem(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class Esp(BaseModel):
                model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                class IntegrityEnum(Enum):
                    value_0 = "null"
                    value_1 = "sha1"
                    value_2 = "sha256"

                class EncryptionEnum(Enum):
                    value_0 = "null"
                    value_1 = "aes128"
                    value_2 = "aes128gcm128"
                    value_3 = "aes128gcm64"
                    value_4 = "aes256"
                    value_5 = "aes256gcm256"

                integrity: IntegrityEnum | None = None
                encryption: EncryptionEnum | None = None

            class PfsDhGroupEnum(Enum):
                value_0 = 1
                value_1 = 2
                value_2 = 5
                value_3 = 14
                value_4 = 15
                value_5 = 16
                value_6 = 17
                value_7 = 20
                value_8 = 21
                value_9 = 24

            name: str = None
            """
            Name of the SA policy.
            """
            esp: Esp | None = None
            pfs_dh_group: PfsDhGroupEnum | None = None

        class ProfilesItem(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class ConnectionEnum(Enum):
                value_0 = "add"
                value_1 = "start"
                value_2 = "route"

            class Dpd(BaseModel):
                model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                class ActionEnum(Enum):
                    value_0 = "clear"
                    value_1 = "hold"
                    value_2 = "restart"

                interval: int = Field(None, ge=2, le=3600)
                """
                Interval (in seconds) between keep-alive messages.
                """
                time: int = Field(None, ge=10, le=3600)
                """
                Time (in seconds) after which the action is applied.
                """
                action: ActionEnum = None
                """
                Action to apply

                * 'clear': Delete all connections
                * 'hold': Re-negotiate connection on demand
                * 'restart': Restart
                connection immediately
                """

            class ModeEnum(Enum):
                value_0 = "transport"
                value_1 = "tunnel"

            name: str = None
            """
            Name of the IPsec profile.
            """
            ike_policy: str | None = None
            """
            Name of the IKE policy to use in this profile.
            """
            sa_policy: str | None = None
            """
            Name of the Security Association to use in this profile.
            """
            connection: ConnectionEnum | None = None
            """
            IPsec connection (Initiator/Responder/Dynamic).
            """
            shared_key: str | None = None
            """
            Encrypted password - only type 7 supported.
            """
            dpd: Dpd | None = None
            """
            Dead Peer Detection.
            """
            mode: ModeEnum | None = None
            """
            Ipsec mode type.
            """

        class KeyController(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            profile: str | None = None
            """
            IPsec profile name to use.
            """

        ike_policies: list[IkePoliciesItem] | None = None
        """
        Internet Security Association and Key Mgmt Protocol.
        """
        sa_policies: list[SaPoliciesItem] | None = None
        """
        Security Association policies.
        """
        profiles: list[ProfilesItem] | None = None
        """
        IPSec profiles.
        """
        key_controller: KeyController | None = None

    class IpSshClientSourceInterfacesItem(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        name: str | None = None
        """
        Interface Name
        """
        vrf: Annotated[str, StrConvert(convert_types=(int))] | None = "default"

    class IpTacacsSourceInterfacesItem(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        name: str | None = None
        """
        Interface name
        """
        vrf: Annotated[str, StrConvert(convert_types=(int))] | None = Field(None, title="VRF")

    class Ipv6AccessListsItem(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class SequenceNumbersItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            sequence: int = None
            """
            Sequence ID
            """
            action: str = None
            """
            Action as string
            Example: "deny ipv6 any any"
            """

        name: str = None
        """
        IPv6 Access-list Name
        """
        counters_per_entry: bool | None = None
        sequence_numbers: list[SequenceNumbersItem] = None

    class Ipv6Hardware(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Fib(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Optimize(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Prefixes(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    profile: str | None = None
                    """
                    Pre-defined profile 'internet' or user-defined profile name
                    """

                prefixes: Prefixes | None = None

            optimize: Optimize | None = None

        fib: Fib | None = None

    class Ipv6PrefixListsItem(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class SequenceNumbersItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            sequence: int = None
            """
            Sequence ID
            """
            action: str = None
            """
            Action as string
            Example: "permit 1b11:3a00:22b0:0082::/64 eq 128"
            """

        name: str = None
        """
        Prefix-list Name
        """
        sequence_numbers: list[SequenceNumbersItem] = None

    class Ipv6StandardAccessListsItem(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class SequenceNumbersItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            sequence: int = None
            """
            Sequence ID
            """
            action: str = None
            """
            Action as string
            Example: "deny ipv6 any any"
            """

        name: str = None
        """
        Access-list Name
        """
        counters_per_entry: bool | None = None
        sequence_numbers: list[SequenceNumbersItem] = None

    class Ipv6StaticRoutesItem(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
        destination_address_prefix: str | None = None
        """
        IPv6 Network/Mask
        """
        interface: str | None = None
        gateway: str | None = None
        """
        IPv6 Address
        """
        track_bfd: bool | None = None
        """
        Track next-hop using BFD
        """
        distance: int | None = Field(None, ge=1, le=255)
        tag: int | None = Field(None, ge=0, le=4294967295)
        name: str | None = None
        """
        Description
        """
        metric: int | None = Field(None, ge=0, le=4294967295)

    class L2Protocol(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class ForwardingProfilesItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class ProtocolsItem(BaseModel):
                model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                class NameEnum(Enum):
                    value_0 = "bfd per-link rfc-7130"
                    value_1 = "e-lmi"
                    value_2 = "isis"
                    value_3 = "lacp"
                    value_4 = "lldp"
                    value_5 = "macsec"
                    value_6 = "pause"
                    value_7 = "stp"

                name: NameEnum = None
                forward: bool | None = None
                tagged_forward: bool | None = None
                untagged_forward: bool | None = None

            name: str = None
            protocols: list[ProtocolsItem] | None = None

        forwarding_profiles: list[ForwardingProfilesItem] | None = None

    class Lacp(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class PortId(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Range(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                begin: int | None = None
                """
                Minimum LACP port-ID range.
                """
                end: int | None = None
                """
                Maximum LACP port-ID range.
                """

            range: Range | None = None

        class RateLimit(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            default: bool | None = None
            """
            Enable LACPDU rate limiting by default on all ports.
            """

        port_id: PortId | None = None
        """
        LACP port-ID range configuration.
        """
        rate_limit: RateLimit | None = None
        """
        Set LACPDU rate limit options.
        """
        system_priority: int | None = Field(None, ge=0, le=65535)
        """
        Set local system LACP priority.
        """

    class LinkTrackingGroupsItem(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        name: str = None
        links_minimum: int | None = Field(None, ge=1, le=100000)
        recovery_delay: int | None = Field(None, ge=0, le=3600)

    class Lldp(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class TlvsItem(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class NameEnum(Enum):
                value_0 = "link-aggregation"
                value_1 = "management-address"
                value_2 = "max-frame-size"
                value_3 = "med"
                value_4 = "port-description"
                value_5 = "port-vlan"
                value_6 = "power-via-mdi"
                value_7 = "system-capabilities"
                value_8 = "system-description"
                value_9 = "system-name"
                value_10 = "vlan-name"

            name: NameEnum = None
            transmit: bool | None = None

        timer: int | None = None
        timer_reinitialization: str | None = None
        holdtime: int | None = None
        management_address: str | None = None
        vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
        receive_packet_tagged_drop: str | None = None
        tlvs: list[TlvsItem] | None = None
        run: bool | None = None

    class LoadInterval(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        default: int | None = None
        """
        Default load interval in seconds
        """

    class LocalUsersItem(BaseModel):
        model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

        class ShellEnum(Enum):
            value_0 = "/bin/bash"
            value_1 = "/bin/sh"
            value_2 = "/sbin/nologin"

        name: str = None
        """
        Username
        """
        disabled: bool | None = None
        """
        If true, the user will be removed and all other settings are ignored.
        Useful for removing the default "admin" user.
        """
        privilege: int | None = Field(None, ge=0, le=15)
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
        shell: ShellEnum | None = None
        """
        Specify shell for the user
        """

    class Logging(BaseModel):
        model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

        class ConsoleEnum(Enum):
            value_0 = "debugging"
            value_1 = "informational"
            value_2 = "notifications"
            value_3 = "warnings"
            value_4 = "errors"
            value_5 = "critical"
            value_6 = "alerts"
            value_7 = "emergencies"
            value_8 = "disabled"

        class MonitorEnum(Enum):
            value_0 = "debugging"
            value_1 = "informational"
            value_2 = "notifications"
            value_3 = "warnings"
            value_4 = "errors"
            value_5 = "critical"
            value_6 = "alerts"
            value_7 = "emergencies"
            value_8 = "disabled"

        class Buffered(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class LevelEnum(Enum):
                value_0 = "alerts"
                value_1 = "critical"
                value_2 = "debugging"
                value_3 = "emergencies"
                value_4 = "errors"
                value_5 = "informational"
                value_6 = "notifications"
                value_7 = "warnings"
                value_8 = "disabled"

            size: int | None = Field(None, ge=10, le=2147483647)
            level: LevelEnum | None = None
            """
            Buffer logging severity level
            """

        class TrapEnum(Enum):
            value_0 = "alerts"
            value_1 = "critical"
            value_2 = "debugging"
            value_3 = "emergencies"
            value_4 = "errors"
            value_5 = "informational"
            value_6 = "notifications"
            value_7 = "system"
            value_8 = "warnings"
            value_9 = "disabled"

        class Synchronous(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class LevelEnum(Enum):
                value_0 = "alerts"
                value_1 = "all"
                value_2 = "critical"
                value_3 = "debugging"
                value_4 = "emergencies"
                value_5 = "errors"
                value_6 = "informational"
                value_7 = "notifications"
                value_8 = "warnings"
                value_9 = "disabled"

            level: LevelEnum | None = "critical"
            """
            Synchronous logging severity level
            """

        class Format(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class TimestampEnum(Enum):
                value_0 = "high-resolution"
                value_1 = "traditional"
                value_2 = "traditional timezone"
                value_3 = "traditional year"
                value_4 = "traditional timezone year"
                value_5 = "traditional year timezone"

            class HostnameEnum(Enum):
                value_0 = "fqdn"
                value_1 = "ipv4"

            timestamp: TimestampEnum | None = None
            """
            Timestamp format
            """
            hostname: HostnameEnum | None = None
            """
            Hostname format
            """
            sequence_numbers: bool | None = None
            """
            Add sequence numbers to log messages
            """

        class FacilityEnum(Enum):
            value_0 = "auth"
            value_1 = "cron"
            value_2 = "daemon"
            value_3 = "kern"
            value_4 = "local0"
            value_5 = "local1"
            value_6 = "local2"
            value_7 = "local3"
            value_8 = "local4"
            value_9 = "local5"
            value_10 = "local6"
            value_11 = "local7"
            value_12 = "lpr"
            value_13 = "mail"
            value_14 = "news"
            value_15 = "sys9"
            value_16 = "sys10"
            value_17 = "sys11"
            value_18 = "sys12"
            value_19 = "sys13"
            value_20 = "sys14"
            value_21 = "syslog"
            value_22 = "user"
            value_23 = "uucp"

        class VrfsItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class HostsItem(BaseModel):
                model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                class ProtocolEnum(Enum):
                    value_0 = "tcp"
                    value_1 = "udp"

                name: str = None
                """
                Syslog server name
                """
                protocol: ProtocolEnum | None = "udp"
                ports: list[int] | None = None

            name: Annotated[str, StrConvert(convert_types=(int))] = None
            """
            VRF name
            """
            source_interface: str | None = None
            """
            Source interface name
            """
            hosts: list[HostsItem] | None = None

        class Policy(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Match(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class MatchListsItem(BaseModel):
                    model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                    class ActionEnum(Enum):
                        value_0 = "discard"

                    name: str = None
                    """
                    Match list
                    """
                    action: ActionEnum | None = None

                match_lists: list[MatchListsItem] | None = None

            match: Match | None = None

        class Event(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class StormControl(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Discards(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    field_global: bool | None = Field(None, alias="global")
                    interval: int | None = Field(None, ge=10, le=65535)
                    """
                    Logging interval in seconds
                    """

                discards: Discards | None = None

            storm_control: StormControl | None = None

        console: ConsoleEnum | None = None
        """
        Console logging severity level
        """
        monitor: MonitorEnum | None = None
        """
        Monitor logging severity level
        """
        buffered: Buffered | None = None
        trap: TrapEnum | None = None
        """
        Trap logging severity level
        """
        synchronous: Synchronous | None = None
        format: Format | None = None
        facility: FacilityEnum | None = None
        source_interface: str | None = None
        """
        Source Interface Name
        """
        vrfs: list[VrfsItem] | None = None
        policy: Policy | None = None
        event: Event | None = None

    class LoopbackInterfacesItem(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Mpls(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Ldp(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                interface: bool | None = None

            ldp: Ldp | None = None

        class NodeSegment(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            ipv4_index: int | None = None
            ipv6_index: int | None = None

        name: str = None
        """
        Loopback interface name e.g. "Loopback0"
        """
        description: str | None = None
        shutdown: bool | None = None
        vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
        """
        VRF name
        """
        ip_address: str | None = None
        """
        IPv4_address/Mask
        """
        ip_address_secondaries: list[str] | None = None
        ipv6_enable: bool | None = None
        ipv6_address: str | None = None
        """
        IPv6_address/Mask
        """
        ip_proxy_arp: bool | None = None
        ospf_area: Annotated[str, StrConvert(convert_types=(int))] | None = None
        mpls: Mpls | None = None
        isis_enable: str | None = None
        """
        ISIS instance name
        """
        isis_passive: bool | None = None
        isis_metric: int | None = None
        isis_network_point_to_point: bool | None = None
        node_segment: NodeSegment | None = None
        eos_cli: str | None = None
        """
        EOS CLI rendered directly on the loopback interface in the final EOS configuration
        """

    class MacAccessListsItem(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class EntriesItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            sequence: int | None = None
            action: str | None = None

        name: str = None
        """
        MAC Access-list Name
        """
        counters_per_entry: bool | None = None
        entries: list[EntriesItem] | None = None

    class MacAddressTable(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class NotificationHostFlap(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Detection(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                window: int | None = Field(None, ge=2, le=300)
                moves: int | None = Field(None, ge=2, le=10)

            logging: bool | None = None
            detection: Detection | None = None

        aging_time: int | None = None
        """
        Aging time in seconds
        """
        notification_host_flap: NotificationHostFlap | None = None

    class MacSecurity(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class License(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            license_name: str = None
            license_key: str = None

        class ProfilesItem(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class CipherEnum(Enum):
                value_0 = "aes128-gcm"
                value_1 = "aes128-gcm-xpn"
                value_2 = "aes256-gcm"
                value_3 = "aes256-gcm-xpn"

            class ConnectionKeysItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                id: str = None
                encrypted_key: str | None = None
                fallback: bool | None = None

            class Mka(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Session(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    rekey_period: int | None = Field(None, ge=30, le=100000)
                    """
                    Rekey period in seconds
                    """

                key_server_priority: int | None = Field(None, ge=0, le=255)
                session: Session | None = None

            class L2Protocols(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class EthernetFlowControl(BaseModel):
                    model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                    class ModeEnum(Enum):
                        value_0 = "encrypt"
                        value_1 = "bypass"

                    mode: ModeEnum = None

                class Lldp(BaseModel):
                    model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                    class ModeEnum(Enum):
                        value_0 = "bypass"
                        value_1 = "bypass unauthorized"

                    mode: ModeEnum = None

                ethernet_flow_control: EthernetFlowControl | None = None
                lldp: Lldp | None = None

            name: str = None
            """
            Profile-Name
            """
            cipher: CipherEnum | None = None
            connection_keys: list[ConnectionKeysItem] | None = None
            mka: Mka | None = None
            sci: bool | None = None
            l2_protocols: L2Protocols | None = None

        license: License | None = None
        fips_restrictions: bool | None = None
        profiles: list[ProfilesItem] | None = None

    class Maintenance(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class InterfaceProfilesItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class RateMonitoring(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                load_interval: int | None = None
                """
                Load Interval in Seconds
                """
                threshold: int | None = None
                """
                Threshold in kbps
                """

            class Shutdown(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                max_delay: int | None = None
                """
                Max delay in seconds
                """

            name: str = None
            rate_monitoring: RateMonitoring | None = None
            shutdown: Shutdown | None = None

        class BgpProfilesItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Initiator(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                route_map_inout: str | None = None
                """
                Route Map
                """

            name: str = None
            """
            BGP Profile Name
            """
            initiator: Initiator | None = None

        class UnitProfilesItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class OnBoot(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                duration: int | None = Field(None, ge=300, le=3600)
                """
                On-boot in seconds
                """

            name: str = None
            """
            Unit Profile Name
            """
            on_boot: OnBoot | None = None

        class UnitsItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Groups(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                bgp_groups: list[str] | None = None
                interface_groups: list[str] | None = None

            name: str = None
            """
            Unit Name
            """
            quiesce: bool | None = None
            profile: str | None = None
            """
            Name of Unit Profile
            """
            groups: Groups | None = None

        default_interface_profile: str | None = None
        """
        Name of default Interface Profile
        """
        default_bgp_profile: str | None = None
        """
        Name of default BGP Profile
        """
        default_unit_profile: str | None = None
        """
        Name of default Unit Profile
        """
        interface_profiles: list[InterfaceProfilesItem] | None = None
        bgp_profiles: list[BgpProfilesItem] | None = None
        unit_profiles: list[UnitProfilesItem] | None = None
        units: list[UnitsItem] | None = None

    class ManagementAccounts(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Password(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            policy: str | None = None

        password: Password | None = None

    class ManagementApiGnmi(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Transport(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class GrpcItem(BaseModel):
                model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                class NotificationTimestampEnum(Enum):
                    value_0 = "send-time"
                    value_1 = "last-change-time"

                name: str | None = None
                """
                Transport name
                """
                ssl_profile: str | None = None
                """
                SSL profile name
                """
                vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
                """
                VRF name is optional
                """
                notification_timestamp: NotificationTimestampEnum | None = None
                """
                Per the gNMI specification, the default timestamp field of a notification message is set to be
                the time at which the
                value of the underlying data source changes or when the reported event takes place.
                In order to facilitate integration
                in legacy environments oriented around polling style operations,
                an option to support overriding the timestamp field to
                the send-time is available from EOS 4.27.0F.
                """
                ip_access_group: str | None = None
                """
                ACL name
                """
                port: int | None = None
                """
                GNMI port.
                Make sure to update the control-plane ACL accordingly in order for the service to be reachable by external
                applications.
                """

            class GrpcTunnelsItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Destination(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    address: str = None
                    """
                    IP address or hostname
                    """
                    port: int = Field(None, ge=1, le=65535)
                    """
                    TCP Port
                    """

                class LocalInterface(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    name: str = None
                    """
                    Interface name
                    """
                    port: int = Field(None, ge=1, le=65535)
                    """
                    TCP Port
                    """

                class Target(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    use_serial_number: bool | None = None
                    """
                    Use serial number as the Target ID
                    """
                    target_ids: list[str] | None = None
                    """
                    Target IDs as a list.
                    """

                name: str = None
                """
                Transport name
                """
                shutdown: bool | None = None
                """
                Operational status of the gRPC tunnel
                """
                tunnel_ssl_profile: str | None = None
                """
                Tunnel SSL profile name
                """
                gnmi_ssl_profile: str | None = None
                """
                gNMI SSL profile name
                """
                vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
                """
                VRF name
                """
                destination: Destination | None = None
                local_interface: LocalInterface | None = None
                target: Target | None = None

            grpc: list[GrpcItem] | None = None
            grpc_tunnels: list[GrpcTunnelsItem] | None = None

        class EnableVrfsItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: Annotated[str, StrConvert(convert_types=(int))] = None
            """
            VRF name
            """
            access_group: str | None = None
            """
            Standard IPv4 ACL name
            """

        provider: str | None = "eos-native"
        transport: Transport | None = None
        enable_vrfs: list[EnableVrfsItem] | None = None
        """
        These should not be mixed with the new keys above.
        """
        octa: dict | None = None
        """
        These should not be mixed with the new keys above.
        Octa activates `eos-native` provider and it is the only provider
        currently supported by EOS.
        """

    class ManagementApiHttp(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class EnableVrfsItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: Annotated[str, StrConvert(convert_types=(int))] = None
            """
            VRF Name
            """
            access_group: str | None = None
            """
            Standard IPv4 ACL name
            """
            ipv6_access_group: str | None = None
            """
            Standard IPv6 ACL name
            """

        class ProtocolHttpsCertificate(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            certificate: str | None = None
            """
            Name of certificate; private key must also be specified
            """
            private_key: str | None = None
            """
            Name of private key; certificate must also be specified
            """

        enable_http: bool | None = None
        enable_https: bool | None = None
        https_ssl_profile: str | None = None
        """
        SSL Profile Name
        """
        default_services: bool | None = None
        """
        Enable default services: capi-doc and tapagg
        """
        enable_vrfs: list[EnableVrfsItem] | None = None
        protocol_https_certificate: ProtocolHttpsCertificate | None = None

    class ManagementApiModels(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class ProvidersItem(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class NameEnum(Enum):
                value_0 = "sysdb"
                value_1 = "smash"

            class PathsItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                path: str | None = None
                disabled: bool | None = False

            name: NameEnum | None = None
            paths: list[PathsItem] | None = None

        providers: list[ProvidersItem] | None = None

    class ManagementConsole(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        idle_timeout: int | None = Field(None, ge=0, le=86400)

    class ManagementCvx(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        shutdown: bool | None = None
        server_hosts: list[str] | None = None
        source_interface: str | None = None
        """
        Interface name
        """
        vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
        """
        VRF Name
        """

    class ManagementDefaults(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Secret(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class HashEnum(Enum):
                value_0 = "md5"
                value_1 = "sha512"

            hash: HashEnum | None = None

        secret: Secret | None = None

    class ManagementInterfacesItem(BaseModel):
        model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

        class TypeEnum(Enum):
            value_0 = "oob"
            value_1 = "inband"

        class Lldp(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            transmit: bool | None = None
            receive: bool | None = None
            ztp_vlan: int | None = None
            """
            ZTP vlan number
            """

        name: str = None
        """
        Management Interface Name
        """
        description: str | None = None
        shutdown: bool | None = None
        speed: str | None = None
        """
        Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`.
        """
        mtu: int | None = None
        vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
        """
        VRF Name
        """
        ip_address: str | None = None
        """
        IPv4_address/Mask
        """
        ipv6_enable: bool | None = None
        ipv6_address: str | None = None
        """
        IPv6_address/Mask
        """
        type: TypeEnum | None = "oob"
        """
        For documentation purposes only
        """
        gateway: str | None = None
        """
        IPv4 address of default gateway in management VRF
        """
        ipv6_gateway: str | None = None
        """
        IPv6 address of default gateway in management VRF
        """
        mac_address: str | None = None
        """
        MAC address
        """
        lldp: Lldp | None = None
        eos_cli: str | None = None
        """
        Multiline EOS CLI rendered directly on the management interface in the final EOS configuration
        """

    class ManagementSecurity(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Password(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class PoliciesItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Minimum(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    digits: int | None = Field(None, ge=1, le=65535)
                    length: int | None = Field(None, ge=1, le=65535)
                    lower: int | None = Field(None, ge=1, le=65535)
                    special: int | None = Field(None, ge=1, le=65535)
                    upper: int | None = Field(None, ge=1, le=65535)

                class Maximum(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    repetitive: int | None = Field(None, ge=1, le=65535)
                    sequential: int | None = Field(None, ge=1, le=65535)

                name: str = None
                minimum: Minimum | None = None
                maximum: Maximum | None = None

            minimum_length: int | None = Field(None, ge=1, le=32)
            encryption_key_common: bool | None = None
            encryption_reversible: str | None = None
            policies: list[PoliciesItem] | None = None

        class SslProfilesItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class TrustCertificate(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Requirement(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    basic_constraint_ca: bool | None = None
                    hostname_fqdn: bool | None = None
                    """
                    Enforce hostname to be FQDN without wildcard.
                    """

                certificates: list[str] | None = None
                """
                List of trust certificate names
                Examples:
                  - test1.crt
                  - test2.crt
                """
                requirement: Requirement | None = None
                policy_expiry_date_ignore: bool | None = None
                system: bool | None = None
                """
                Use system-supplied trust certificates.
                """

            class ChainCertificate(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Requirement(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    basic_constraint_ca: bool | None = None
                    include_root_ca: bool | None = None

                certificates: list[str] | None = None
                """
                List of chain certificate names
                Examples:
                  - chain1.crt
                  - chain2.crt
                """
                requirement: Requirement | None = None

            class Certificate(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                file: str | None = None
                key: str | None = None

            name: str | None = None
            tls_versions: Annotated[str, StrConvert(convert_types=(float))] | None = None
            """
            List of allowed TLS versions as string
            Examples:
              - "1.0"
              - "1.0 1.1"
            """
            cipher_list: str | None = None
            """
            cipher_list syntax follows the openssl cipher strings format.
            Colon (:) separated list of allowed ciphers as a string
            """
            trust_certificate: TrustCertificate | None = None
            chain_certificate: ChainCertificate | None = None
            certificate: Certificate | None = None

        entropy_source: str | None = None
        password: Password | None = None
        ssl_profiles: list[SslProfilesItem] | None = None

    class ManagementSsh(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class AccessGroupsItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str | None = None
            """
            Standard ACL Name
            """
            vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
            """
            VRF Name
            """

        class Ipv6AccessGroupsItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str | None = None
            """
            Standard ACL Name
            """
            vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
            """
            VRF Name
            """

        class Hostkey(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            server: list[str] | None = None
            """
            SSH host key settings
            """

        class Connection(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            limit: int | None = Field(None, ge=1, le=100)
            """
            Maximum total number of SSH sessions to device
            """
            per_host: int | None = Field(None, ge=1, le=20)
            """
            Maximum number of SSH sessions to device from a single host
            """

        class VrfsItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: Annotated[str, StrConvert(convert_types=(int))] = None
            """
            VRF Name
            """
            enable: bool | None = None
            """
            Enable SSH in VRF
            """

        class ClientAlive(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            count_max: int | None = Field(None, ge=1, le=1000)
            """
            Number of keep-alive packets that can be sent without a response before the connection is assumed dead.
            """
            interval: int | None = Field(None, ge=1, le=1000)
            """
            Time period (in seconds) to send SSH keep-alive packets.
            """

        access_groups: list[AccessGroupsItem] | None = None
        ipv6_access_groups: list[Ipv6AccessGroupsItem] | None = None
        idle_timeout: int | None = Field(None, ge=0, le=86400)
        """
        Idle timeout in minutes
        """
        cipher: list[str] | None = None
        """
        Cryptographic ciphers for SSH to use
        """
        key_exchange: list[str] | None = None
        """
        Cryptographic key exchange methods for SSH to use
        """
        mac: list[str] | None = None
        """
        Cryptographic MAC algorithms for SSH to use
        """
        hostkey: Hostkey | None = None
        enable: bool | None = None
        """
        Enable SSH daemon
        """
        connection: Connection | None = None
        vrfs: list[VrfsItem] | None = None
        log_level: str | None = None
        """
        SSH daemon log level
        """
        client_alive: ClientAlive | None = None

    class ManagementTechSupport(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class PolicyShowTechSupport(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class ExcludeCommandsItem(BaseModel):
                model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                class TypeEnum(Enum):
                    value_0 = "text"
                    value_1 = "json"

                command: str | None = None
                """
                Command to exclude from tech-support
                """
                type: TypeEnum | None = "text"
                """
                The supported values for type are platform dependent.
                """

            class IncludeCommandsItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                command: str | None = None
                """
                Command to include in tech-support
                """

            exclude_commands: list[ExcludeCommandsItem] | None = None
            include_commands: list[IncludeCommandsItem] | None = None

        policy_show_tech_support: PolicyShowTechSupport | None = None

    class MatchListInput(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class StringItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class SequenceNumbersItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                sequence: int = None
                """
                Sequence ID
                """
                match_regex: str = None
                """
                Regular Expression
                """

            name: str = None
            """
            Match-list Name
            """
            sequence_numbers: list[SequenceNumbersItem] = None

        string: list[StringItem] | None = None

    class McsClient(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class CvxSecondary(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str | None = None
            shutdown: bool | None = None
            server_hosts: list[str] | None = None

        shutdown: bool | None = None
        cvx_secondary: CvxSecondary | None = None

    class MlagConfiguration(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class PeerAddressHeartbeat(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            peer_ip: str | None = None
            """
            IPv4 Address
            """
            vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
            """
            VRF Name
            """

        domain_id: str | None = None
        heartbeat_interval: int | None = None
        """
        Heartbeat interval in milliseconds
        """
        local_interface: str | None = None
        """
        Local Interface Name
        """
        peer_address: str | None = None
        """
        IPv4 Address
        """
        peer_address_heartbeat: PeerAddressHeartbeat | None = None
        dual_primary_detection_delay: int | None = Field(None, ge=0, le=86400)
        """
        Delay in seconds
        """
        dual_primary_recovery_delay_mlag: int | None = Field(None, ge=0, le=86400)
        """
        Delay in seconds
        """
        dual_primary_recovery_delay_non_mlag: int | None = Field(None, ge=0, le=86400)
        """
        Delay in seconds
        """
        peer_link: str | None = None
        """
        Port-Channel interface name
        """
        reload_delay_mlag: Annotated[str, StrConvert(convert_types=(int))] | None = None
        """
        Delay in seconds <0-86400> or 'infinity'
        """
        reload_delay_non_mlag: Annotated[str, StrConvert(convert_types=(int))] | None = None
        """
        Delay in seconds <0-86400> or 'infinity'
        """

    class MonitorConnectivity(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class InterfaceSetsItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str | None = None
            interfaces: str | None = None
            """
            Interface range(s) should be of same type, Ethernet, Loopback, Management etc.
            Multiple interface ranges can be
            specified separated by ","
            """

        class HostsItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str | None = None
            """
            Host Name
            """
            description: str | None = None
            ip: str | None = None
            local_interfaces: str | None = None
            url: str | None = None

        class VrfsItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class InterfaceSetsItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                name: str | None = None
                interfaces: str | None = None

            class HostsItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                name: str | None = None
                """
                Host name
                """
                description: str | None = None
                ip: str | None = None
                local_interfaces: str | None = None
                url: str | None = None

            name: Annotated[str, StrConvert(convert_types=(int))] = None
            """
            VRF Name
            """
            description: str | None = None
            interface_sets: list[InterfaceSetsItem] | None = None
            local_interfaces: str | None = None
            hosts: list[HostsItem] | None = None

        shutdown: bool | None = None
        interval: int | None = None
        interface_sets: list[InterfaceSetsItem] | None = None
        local_interfaces: str | None = None
        hosts: list[HostsItem] | None = None
        vrfs: list[VrfsItem] | None = None

    class MonitorSessionsItem(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class SourcesItem(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class DirectionEnum(Enum):
                value_0 = "rx"
                value_1 = "tx"
                value_2 = "both"

            class AccessGroup(BaseModel):
                model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                class TypeEnum(Enum):
                    value_0 = "ip"
                    value_1 = "ipv6"
                    value_2 = "mac"

                type: TypeEnum | None = None
                name: str | None = None
                """
                ACL Name
                """
                priority: int | None = None

            name: str | None = None
            """
            Interface name, range or comma separated list
            """
            direction: DirectionEnum | None = None
            access_group: AccessGroup | None = None

        class AccessGroup(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class TypeEnum(Enum):
                value_0 = "ip"
                value_1 = "ipv6"
                value_2 = "mac"

            type: TypeEnum | None = None
            name: str | None = None
            """
            ACL Name
            """

        class Truncate(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            enabled: bool | None = None
            size: int | None = None
            """
            Size in bytes
            """

        name: str = None
        """
        Session Name
        """
        sources: list[SourcesItem] | None = None
        destinations: list[str] | None = None
        encapsulation_gre_metadata_tx: bool | None = None
        header_remove_size: int | None = None
        """
        Number of bytes to remove from header
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
        sample: int | None = None
        truncate: Truncate | None = None

    class Mpls(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Ldp(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            interface_disabled_default: bool | None = None
            router_id: str | None = None
            shutdown: bool | None = None
            transport_address_interface: str | None = None
            """
            Interface Name
            """

        ip: bool | None = None
        ldp: Ldp | None = None

    class NameServer(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Source(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
            """
            VRF Name
            """

        source: Source | None = None
        nodes: list[str] | None = None

    class Ntp(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class LocalInterface(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str | None = None
            """
            Source interface
            """
            vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
            """
            VRF name
            """

        class ServersItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str | None = None
            """
            IP or hostname e.g., 2.2.2.55, ie.pool.ntp.org
            """
            burst: bool | None = None
            iburst: bool | None = None
            key: int | None = Field(None, ge=1, le=65535)
            local_interface: str | None = None
            """
            Source interface
            """
            maxpoll: int | None = Field(None, ge=3, le=17)
            """
            Value of maxpoll between 3 - 17 (Logarithmic)
            """
            minpoll: int | None = Field(None, ge=3, le=17)
            """
            Value of minpoll between 3 - 17 (Logarithmic)
            """
            preferred: bool | None = None
            version: int | None = Field(None, ge=1, le=4)
            vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
            """
            VRF name
            """

        class AuthenticationKeysItem(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class HashAlgorithmEnum(Enum):
                value_0 = "md5"
                value_1 = "sha1"

            class KeyTypeEnum(Enum):
                value_0 = "0"
                value_1 = "7"
                value_2 = "8a"

            id: int = Field(None, ge=1, le=65534)
            """
            Key identifier
            """
            hash_algorithm: HashAlgorithmEnum | None = None
            key: str | None = None
            """
            Obfuscated key
            """
            key_type: Annotated[KeyTypeEnum, StrConvert(convert_types=(int))] | None = None

        local_interface: LocalInterface | None = None
        servers: list[ServersItem] | None = None
        authenticate: bool | None = None
        authenticate_servers_only: bool | None = None
        authentication_keys: list[AuthenticationKeysItem] | None = None
        trusted_keys: str | None = None
        """
        List of trusted-keys as string ex. 10-12,15
        """

    class PatchPanel(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class PatchesItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class ConnectorsItem(BaseModel):
                model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                class TypeEnum(Enum):
                    value_0 = "interface"
                    value_1 = "pseudowire"

                id: Annotated[str, StrConvert(convert_types=(int))] = None
                type: TypeEnum = None
                endpoint: str = None
                """
                String with relevant endpoint depending on type.
                Examples:
                - "Ethernet1"
                - "Ethernet1 dot1q vlan 123"
                - "bgp vpws
                TENANT_A pseudowire VPWS_PW_1"
                - "ldp LDP_PW_1"
                """

            name: str = None
            enabled: bool | None = None
            connectors: list[ConnectorsItem] | None = Field(None, min_length=2, max_length=2)
            """
            Must have exactly two connectors to a patch of which at least one must be of type "interface"
            """

        patches: list[PatchesItem] | None = None

    class PeerFiltersItem(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class SequenceNumbersItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            sequence: int = None
            """
            Sequence ID
            """
            match: str = None
            """
            Match as string
            Example: "as-range 1-100 result accept"
            """

        name: str = None
        """
        Peer-filter Name
        """
        sequence_numbers: list[SequenceNumbersItem] = None

    class Platform(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Trident(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Mmu(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class QueueProfilesItem(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class MulticastQueuesItem(BaseModel):
                        model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                        class UnitEnum(Enum):
                            value_0 = "bytes"
                            value_1 = "cells"

                        class Drop(BaseModel):
                            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                            class PrecedenceEnum(Enum):
                                value_0 = 1
                                value_1 = 2

                            precedence: PrecedenceEnum = None
                            threshold: Annotated[str, StrConvert(convert_types=(int))] = None
                            """
                            Drop Treshold. This value may also be fractions.
                            Example: 7/8 or 3/4 or 1/2
                            """

                        id: int = Field(None, ge=0, le=7)
                        unit: UnitEnum | None = None
                        """
                        Unit to be used for the reservation value. If not specified, default is bytes.
                        """
                        reserved: int | None = None
                        """
                        Amount of memory that should be reserved for this
                        queue.
                        """
                        threshold: Annotated[str, StrConvert(convert_types=(int))] | None = None
                        """
                        Dynamic Shared Memory threshold.
                        """
                        drop: Drop | None = None

                    class UnicastQueuesItem(BaseModel):
                        model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                        class UnitEnum(Enum):
                            value_0 = "bytes"
                            value_1 = "cells"

                        class Drop(BaseModel):
                            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                            class PrecedenceEnum(Enum):
                                value_0 = 1
                                value_1 = 2

                            precedence: PrecedenceEnum = None
                            threshold: Annotated[str, StrConvert(convert_types=(int))] = None
                            """
                            Drop Treshold. This value may also be fractions.
                            Example: 7/8 or 3/4 or 1/2
                            """

                        id: int = Field(None, ge=0, le=7)
                        unit: UnitEnum | None = None
                        """
                        Unit to be used for the reservation value. If not specified, default is bytes.
                        """
                        reserved: int | None = None
                        """
                        Amount of memory that should be reserved for this
                        queue.
                        """
                        threshold: Annotated[str, StrConvert(convert_types=(int))] | None = None
                        """
                        Dynamic Shared Memory threshold.
                        """
                        drop: Drop | None = None

                    name: str = None
                    multicast_queues: list[MulticastQueuesItem] | None = None
                    unicast_queues: list[UnicastQueuesItem] | None = None

                active_profile: str | None = None
                """
                The queue profile to be applied to the platform.
                """
                queue_profiles: list[QueueProfilesItem] | None = None

            forwarding_table_partition: Annotated[str, StrConvert(convert_types=(int))] | None = None
            mmu: Mmu | None = None
            """
            Memory Management Unit settings.
            """

        class Sand(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class QosMapsItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                traffic_class: int | None = Field(None, ge=0, le=7)
                to_network_qos: int | None = Field(None, ge=0, le=63)

            class Lag(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                hardware_only: bool | None = None
                mode: str | None = None

            class MulticastReplication(BaseModel):
                model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                class DefaultEnum(Enum):
                    value_0 = "ingress"
                    value_1 = "egress"

                default: DefaultEnum | None = None

            qos_maps: list[QosMapsItem] | None = None
            lag: Lag | None = None
            forwarding_mode: str | None = None
            multicast_replication: MulticastReplication | None = None

        class Sfe(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            data_plane_cpu_allocation_max: int | None = Field(None, ge=1, le=128)
            """
            Maximum number of CPUs used for data plane traffic forwarding.
            """

        trident: Trident | None = None
        sand: Sand | None = None
        """
        Most of the platform sand options are hardware dependent and optional
        """
        sfe: Sfe | None = None
        """
        Sfe (Software Forwarding Engine) settings.
        """

    class Poe(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Reboot(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class ActionEnum(Enum):
                value_0 = "power-off"
                value_1 = "maintain"

            action: ActionEnum | None = None
            """
            PoE action for interface. By default in EOS, reboot action is set to power-off.
            """

        class InterfaceShutdown(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class ActionEnum(Enum):
                value_0 = "power-off"
                value_1 = "maintain"

            action: ActionEnum | None = None
            """
            PoE action for interface. By default in EOS, interface shutdown action is set to maintain.
            """

        reboot: Reboot | None = None
        """
        Set the global PoE power behavior for PoE ports when the system is rebooted.
        """
        interface_shutdown: InterfaceShutdown | None = None
        """
        Set the global PoE power behavior for PoE ports when ports are admin down
        """

    class PolicyMaps(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class PbrItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class ClassesItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Set(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class Nexthop(BaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        ip_address: str | None = None
                        """
                        IPv4 or IPv6 Address
                        """
                        recursive: bool | None = None

                    nexthop: Nexthop | None = None

                name: str = None
                """
                Class Name
                """
                index: int | None = None
                drop: bool | None = None
                """
                'drop' and 'set' are mutually exclusive
                """
                set: Set | None = None
                """
                Set Nexthop
                'drop' and 'set' are mutually exclusive
                """

            name: str = None
            """
            Policy-Map Name
            """
            classes: list[ClassesItem] | None = None

        class QosItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class ClassesItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Set(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    cos: int | None = None
                    dscp: Annotated[str, StrConvert(convert_types=(int))] | None = None
                    traffic_class: int | None = None
                    drop_precedence: int | None = None

                name: str = None
                """
                Class Name
                """
                set: Set | None = None

            name: str = None
            """
            Policy-Map Name
            """
            classes: list[ClassesItem] | None = None

        pbr: list[PbrItem] | None = None
        """
        PBR Policy-Maps
        """
        qos: list[QosItem] | None = None
        """
        QOS Policy-Maps
        """

    class PortChannelInterfacesItem(BaseModel):
        model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

        class Logging(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Event(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                link_status: bool | None = None

            event: Event | None = None

        class TypeEnum(Enum):
            value_0 = "routed"
            value_1 = "switched"
            value_2 = "l3dot1q"
            value_3 = "l2dot1q"

        class EncapsulationVlan(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Client(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Dot1q(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    vlan: int | None = None
                    """
                    Client VLAN ID
                    """
                    outer: int | None = None
                    """
                    Client Outer VLAN ID
                    """
                    inner: int | None = None
                    """
                    Client Inner VLAN ID
                    """

                dot1q: Dot1q | None = None
                unmatched: bool | None = None

            class Network(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Dot1q(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    vlan: int | None = None
                    """
                    Network VLAN ID
                    """
                    outer: int | None = None
                    """
                    Network Outer VLAN ID
                    """
                    inner: int | None = None
                    """
                    Network Inner VLAN ID
                    """

                dot1q: Dot1q | None = None
                client: bool | None = None

            client: Client | None = None
            network: Network | None = None
            """
            Network encapsulation are all optional, and skipped if using client unmatched
            """

        class ModeEnum(Enum):
            value_0 = "access"
            value_1 = "dot1q-tunnel"
            value_2 = "trunk"
            value_3 = "trunk phone"

        class LinkTrackingGroupsItem(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class DirectionEnum(Enum):
                value_0 = "upstream"
                value_1 = "downstream"

            name: str = None
            """
            Group name
            """
            direction: DirectionEnum | None = None

        class Phone(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class TrunkEnum(Enum):
                value_0 = "tagged"
                value_1 = "untagged"

            trunk: TrunkEnum | None = None
            vlan: int | None = Field(None, ge=1, le=4094)

        class L2Protocol(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            encapsulation_dot1q_vlan: int | None = None
            """
            Vlan tag to configure on sub-interface
            """
            forwarding_profile: str | None = None
            """
            L2 protocol forwarding profile
            """

        class LacpFallbackModeEnum(Enum):
            value_0 = "individual"
            value_1 = "static"

        class Qos(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class TrustEnum(Enum):
                value_0 = "dscp"
                value_1 = "cos"
                value_2 = "disabled"

            trust: TrustEnum | None = None
            dscp: int | None = None
            """
            DSCP value
            """
            cos: int | None = None
            """
            COS value
            """

        class Bfd(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            echo: bool | None = None
            interval: int | None = None
            """
            Interval in milliseconds
            """
            min_rx: int | None = None
            """
            Rate in milliseconds
            """
            multiplier: int | None = Field(None, ge=3, le=50)

        class ServicePolicy(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Pbr(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                input: str | None = None
                """
                Policy Based Routing Policy-map name
                """

            class Qos(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                input: str = None
                """
                Quality of Service Policy-map name
                """

            pbr: Pbr | None = None
            qos: Qos | None = None

        class Mpls(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Ldp(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                interface: bool | None = None
                igp_sync: bool | None = None

            ip: bool | None = None
            ldp: Ldp | None = None

        class VlanTranslationsItem(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class DirectionEnum(Enum):
                value_0 = "in"
                value_1 = "out"
                value_2 = "both"

            field_from: Annotated[str, StrConvert(convert_types=(int))] | None = Field(None, alias="from")
            """
            List of vlans as string (only one vlan if direction is "both")
            """
            to: int | None = None
            """
            VLAN ID
            """
            direction: DirectionEnum | None = "both"

        class Shape(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            rate: str | None = None
            """
            Rate in kbps, pps or percent
            Supported options are platform dependent
            Examples:
            - "5000 kbps"
            - "1000 pps"
            - "20
            percent"
            """

        class StormControl(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class All(BaseModel):
                model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                class UnitEnum(Enum):
                    value_0 = "percent"
                    value_1 = "pps"

                level: Annotated[str, StrConvert(convert_types=(int, float))] | None = None
                """
                Configure maximum storm-control level
                """
                unit: UnitEnum | None = "percent"
                """
                Optional field and is hardware dependent
                """

            class Broadcast(BaseModel):
                model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                class UnitEnum(Enum):
                    value_0 = "percent"
                    value_1 = "pps"

                level: Annotated[str, StrConvert(convert_types=(int, float))] | None = None
                """
                Configure maximum storm-control level
                """
                unit: UnitEnum | None = "percent"
                """
                Optional field and is hardware dependent
                """

            class Multicast(BaseModel):
                model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                class UnitEnum(Enum):
                    value_0 = "percent"
                    value_1 = "pps"

                level: Annotated[str, StrConvert(convert_types=(int, float))] | None = None
                """
                Configure maximum storm-control level
                """
                unit: UnitEnum | None = "percent"
                """
                Optional field and is hardware dependent
                """

            class UnknownUnicast(BaseModel):
                model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                class UnitEnum(Enum):
                    value_0 = "percent"
                    value_1 = "pps"

                level: Annotated[str, StrConvert(convert_types=(int, float))] | None = None
                """
                Configure maximum storm-control level
                """
                unit: UnitEnum | None = "percent"
                """
                Optional field and is hardware dependent
                """

            all: All | None = None
            broadcast: Broadcast | None = None
            multicast: Multicast | None = None
            unknown_unicast: UnknownUnicast | None = None

        class IsisCircuitTypeEnum(Enum):
            value_0 = "level-1-2"
            value_1 = "level-1"
            value_2 = "level-2"

        class IsisAuthenticationModeEnum(Enum):
            value_0 = "text"
            value_1 = "md5"

        class TrafficPolicy(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            input: str | None = None
            """
            Ingress traffic policy
            """
            output: str | None = None
            """
            Egress traffic policy
            """

        class EvpnEthernetSegment(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class RedundancyEnum(Enum):
                value_0 = "all-active"
                value_1 = "single-active"

            class DesignatedForwarderElection(BaseModel):
                model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                class AlgorithmEnum(Enum):
                    value_0 = "modulus"
                    value_1 = "preference"

                algorithm: AlgorithmEnum | None = None
                preference_value: int | None = Field(None, ge=0, le=65535)
                """
                Preference_value is only used when "algorithm" is "preference"
                """
                dont_preempt: bool | None = False
                """
                Dont_preempt is only used when "algorithm" is "preference"
                """
                hold_time: int | None = None
                subsequent_hold_time: int | None = None
                candidate_reachability_required: bool | None = None

            class Mpls(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                shared_index: int | None = Field(None, ge=1, le=1024)
                tunnel_flood_filter_time: int | None = None

            identifier: str | None = None
            """
            EVPN Ethernet Segment Identifier (Type 1 format)
            """
            redundancy: RedundancyEnum | None = None
            designated_forwarder_election: DesignatedForwarderElection | None = None
            mpls: Mpls | None = None
            route_target: str | None = None
            """
            EVPN Route Target for ESI with format xx:xx:xx:xx:xx:xx
            """

        class SpanningTreeBpdufilterEnum(Enum):
            value_0 = "enabled"
            value_1 = "disabled"
            value_2 = "True"
            value_3 = "False"
            value_4 = "true"
            value_5 = "false"

        class SpanningTreeBpduguardEnum(Enum):
            value_0 = "enabled"
            value_1 = "disabled"
            value_2 = "True"
            value_3 = "False"
            value_4 = "true"
            value_5 = "false"

        class SpanningTreeGuardEnum(Enum):
            value_0 = "loop"
            value_1 = "root"
            value_2 = "disabled"

        class SpanningTreePortfastEnum(Enum):
            value_0 = "edge"
            value_1 = "network"

        class Ptp(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class Announce(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                interval: int | None = None
                timeout: int | None = None

            class DelayMechanismEnum(Enum):
                value_0 = "e2e"
                value_1 = "p2p"

            class SyncMessage(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                interval: int | None = None

            class RoleEnum(Enum):
                value_0 = "master"
                value_1 = "dynamic"

            class TransportEnum(Enum):
                value_0 = "ipv4"
                value_1 = "ipv6"
                value_2 = "layer2"

            enable: bool | None = None
            announce: Announce | None = None
            delay_req: int | None = None
            delay_mechanism: DelayMechanismEnum | None = None
            sync_message: SyncMessage | None = None
            role: RoleEnum | None = None
            vlan: Annotated[str, StrConvert(convert_types=(int))] | None = None
            """
            VLAN can be 'all' or list of vlans as string
            """
            transport: TransportEnum | None = None

        class IpNat(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Destination(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class DynamicItem(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    access_list: str = None
                    comment: str | None = None
                    pool_name: str = None
                    priority: int | None = Field(None, ge=0, le=4294967295)

                class StaticItem(BaseModel):
                    model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                    class DirectionEnum(Enum):
                        value_0 = "egress"
                        value_1 = "ingress"

                    class ProtocolEnum(Enum):
                        value_0 = "udp"
                        value_1 = "tcp"

                    access_list: str | None = None
                    """
                    'access_list' and 'group' are mutual exclusive
                    """
                    comment: str | None = None
                    direction: DirectionEnum | None = None
                    """
                    Egress or ingress can be the default. This depends on source/destination, EOS version, and hardware platform.
                    EOS might
                    remove this keyword in the configuration. So, check the configuration on targeted HW/SW.
                    """
                    group: int | None = Field(None, ge=1, le=65535)
                    """
                    'access_list' and 'group' are mutual exclusive
                    """
                    original_ip: str = None
                    """
                    IPv4 address
                    """
                    original_port: int | None = Field(None, ge=1, le=65535)
                    priority: int | None = Field(None, ge=0, le=4294967295)
                    protocol: ProtocolEnum | None = None
                    translated_ip: str = None
                    """
                    IPv4 address
                    """
                    translated_port: int | None = Field(None, ge=1, le=65535)
                    """
                    requires 'original_port'
                    """

                dynamic: list[DynamicItem] | None = None
                static: list[StaticItem] | None = None

            class Source(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class DynamicItem(BaseModel):
                    model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                    class NatTypeEnum(Enum):
                        value_0 = "overload"
                        value_1 = "pool"
                        value_2 = "pool-address-only"
                        value_3 = "pool-full-cone"

                    access_list: str = None
                    comment: str | None = None
                    nat_type: NatTypeEnum = None
                    pool_name: str | None = None
                    """
                    required if 'nat_type' is pool, pool-address-only or pool-full-cone
                    ignored if 'nat_type' is overload
                    """
                    priority: int | None = Field(None, ge=0, le=4294967295)

                class StaticItem(BaseModel):
                    model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                    class DirectionEnum(Enum):
                        value_0 = "egress"
                        value_1 = "ingress"

                    class ProtocolEnum(Enum):
                        value_0 = "udp"
                        value_1 = "tcp"

                    access_list: str | None = None
                    """
                    'access_list' and 'group' are mutual exclusive
                    """
                    comment: str | None = None
                    direction: DirectionEnum | None = None
                    """
                    Egress or ingress can be the default. This depends on source/destination, EOS version, and hardware platform.
                    EOS might
                    remove this keyword in the configuration. So, check the configuration on targeted HW/SW.
                    """
                    group: int | None = Field(None, ge=1, le=65535)
                    """
                    'access_list' and 'group' are mutual exclusive
                    """
                    original_ip: str = None
                    """
                    IPv4 address
                    """
                    original_port: int | None = Field(None, ge=1, le=65535)
                    priority: int | None = Field(None, ge=0, le=4294967295)
                    protocol: ProtocolEnum | None = None
                    translated_ip: str = None
                    """
                    IPv4 address
                    """
                    translated_port: int | None = Field(None, ge=1, le=65535)
                    """
                    requires 'original_port'
                    """

                dynamic: list[DynamicItem] | None = None
                static: list[StaticItem] | None = None

            destination: Destination | None = None
            source: Source | None = None

        class Ipv6NdPrefixesItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            ipv6_prefix: str = None
            valid_lifetime: Annotated[str, StrConvert(convert_types=(int))] | None = None
            """
            Infinite or lifetime in seconds
            """
            preferred_lifetime: Annotated[str, StrConvert(convert_types=(int))] | None = None
            """
            Infinite or lifetime in seconds
            """
            no_autoconfig_flag: bool | None = None

        class Pim(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Ipv4(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                dr_priority: int | None = Field(None, ge=0, le=429467295)
                sparse_mode: bool | None = None

            ipv4: Ipv4 | None = None

        class OspfAuthenticationEnum(Enum):
            value_0 = "none"
            value_1 = "simple"
            value_2 = "message-digest"

        class OspfMessageDigestKeysItem(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class HashAlgorithmEnum(Enum):
                value_0 = "md5"
                value_1 = "sha1"
                value_2 = "sha256"
                value_3 = "sha384"
                value_4 = "sha512"

            id: int = None
            hash_algorithm: HashAlgorithmEnum | None = None
            key: str | None = None
            """
            Encrypted password
            """

        class FlowTracker(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            sampled: str | None = None
            """
            Sampled flow tracker name.
            """
            hardware: str | None = None
            """
            Hardware flow tracker name.
            """

        class Bgp(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            session_tracker: str | None = None
            """
            Name of session tracker
            """

        class Sflow(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Egress(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                enable: bool | None = None
                unmodified_enable: bool | None = None

            enable: bool | None = None
            egress: Egress | None = None

        name: str = None
        description: str | None = None
        logging: Logging | None = None
        shutdown: bool | None = None
        l2_mtu: int | None = None
        """
        "l2_mtu" should only be defined for platforms supporting the "l2 mtu" CLI
        """
        vlans: Annotated[str, StrConvert(convert_types=(int))] | None = None
        """
        List of switchport vlans as string
        For a trunk port this would be a range like "1-200,300"
        For an access port this would
        be a single vlan "123"
        """
        snmp_trap_link_change: bool | None = None
        type: TypeEnum | None = None
        """
        l3dot1q and l2dot1q are used for sub-interfaces. The parent interface should be defined as routed.
        Interface will not be
        listed in device documentation, unless "type" is set.
        """
        encapsulation_dot1q_vlan: int | None = None
        """
        VLAN tag to configure on sub-interface
        """
        vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
        """
        VRF name
        """
        encapsulation_vlan: EncapsulationVlan | None = None
        vlan_id: int | None = Field(None, ge=1, le=4094)
        mode: ModeEnum | None = None
        native_vlan: int | None = None
        """
        If setting both native_vlan and native_vlan_tag, native_vlan_tag takes precedence
        """
        native_vlan_tag: bool | None = False
        """
        If setting both native_vlan and native_vlan_tag, native_vlan_tag takes precedence
        """
        link_tracking_groups: list[LinkTrackingGroupsItem] | None = None
        phone: Phone | None = None
        l2_protocol: L2Protocol | None = None
        mtu: int | None = None
        mlag: int | None = Field(None, ge=1, le=2000)
        """
        MLAG ID
        """
        trunk_groups: list[str] | None = None
        lacp_fallback_timeout: int | None = Field(90, ge=0, le=300)
        """
        Timeout in seconds
        """
        lacp_fallback_mode: LacpFallbackModeEnum | None = None
        qos: Qos | None = None
        bfd: Bfd | None = None
        service_policy: ServicePolicy | None = None
        mpls: Mpls | None = None
        trunk_private_vlan_secondary: bool | None = None
        pvlan_mapping: Annotated[str, StrConvert(convert_types=(int))] | None = None
        """
        List of vlans as string
        """
        vlan_translations: list[VlanTranslationsItem] | None = None
        shape: Shape | None = None
        storm_control: StormControl | None = None
        ip_proxy_arp: bool | None = None
        isis_enable: str | None = None
        """
        ISIS instance
        """
        isis_passive: bool | None = None
        isis_metric: int | None = None
        isis_network_point_to_point: bool | None = None
        isis_circuit_type: IsisCircuitTypeEnum | None = None
        isis_hello_padding: bool | None = None
        isis_authentication_mode: IsisAuthenticationModeEnum | None = None
        isis_authentication_key: str | None = None
        """
        Type-7 encrypted password
        """
        traffic_policy: TrafficPolicy | None = None
        evpn_ethernet_segment: EvpnEthernetSegment | None = None
        esi: str | None = None
        """
        EVPN Ethernet Segment Identifier (Type 1 format)
        If both "esi" and "evpn_ethernet_segment.identifier" are defined, the
        new variable takes precedence
        """
        rt: str | None = None
        """
        EVPN Route Target for ESI with format xx:xx:xx:xx:xx:xx
        If both "rt" and "evpn_ethernet_segment.route_target" are
        defined, the new variable takes precedence
        """
        lacp_id: str | None = None
        """
        LACP ID with format xxxx.xxxx.xxxx
        """
        spanning_tree_bpdufilter: Annotated[SpanningTreeBpdufilterEnum, StrConvert(convert_types=(bool))] | None = None
        spanning_tree_bpduguard: Annotated[SpanningTreeBpduguardEnum, StrConvert(convert_types=(bool))] | None = None
        spanning_tree_guard: SpanningTreeGuardEnum | None = None
        spanning_tree_portfast: SpanningTreePortfastEnum | None = None
        vmtracer: bool | None = None
        ptp: Ptp | None = None
        ip_address: str | None = None
        """
        IPv4 address/mask
        """
        ip_nat: IpNat | None = None
        ipv6_enable: bool | None = None
        ipv6_address: str | None = None
        """
        IPv6 address/mask
        """
        ipv6_address_link_local: str | None = None
        """
        Link local IPv6 address/mask
        """
        ipv6_nd_ra_disabled: bool | None = None
        ipv6_nd_managed_config_flag: bool | None = None
        ipv6_nd_prefixes: list[Ipv6NdPrefixesItem] | None = None
        access_group_in: str | None = None
        """
        Access list name
        """
        access_group_out: str | None = None
        """
        Access list name
        """
        ipv6_access_group_in: str | None = None
        """
        IPv6 access list name
        """
        ipv6_access_group_out: str | None = None
        """
        IPv6 access list name
        """
        mac_access_group_in: str | None = None
        """
        MAC access list name
        """
        mac_access_group_out: str | None = None
        """
        MAC access list name
        """
        pim: Pim | None = None
        service_profile: str | None = None
        """
        QOS profile
        """
        ospf_network_point_to_point: bool | None = None
        ospf_area: Annotated[str, StrConvert(convert_types=(int))] | None = None
        ospf_cost: int | None = None
        ospf_authentication: OspfAuthenticationEnum | None = None
        ospf_authentication_key: str | None = None
        """
        Encrypted password
        """
        ospf_message_digest_keys: list[OspfMessageDigestKeysItem] | None = None
        flow_tracker: FlowTracker | None = None
        bgp: Bgp | None = None
        peer: str | None = None
        """
        Key only used for documentation or validation purposes
        """
        peer_interface: str | None = None
        """
        Key only used for documentation or validation purposes
        """
        peer_type: str | None = None
        """
        Key only used for documentation or validation purposes
        """
        sflow: Sflow | None = None
        eos_cli: str | None = None
        """
        Multiline EOS CLI rendered directly on the port-channel interface in the final EOS configuration
        """

    class PrefixListsItem(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class SequenceNumbersItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            sequence: int = None
            """
            Sequence ID
            """
            action: str = None
            """
            Action as string
            Example: "permit 10.255.0.0/27 eq 32"
            """

        name: str = None
        """
        Prefix-list Name
        """
        sequence_numbers: list[SequenceNumbersItem] | None = None

    class PriorityFlowControl(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Watchdog(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class ActionEnum(Enum):
                value_0 = "drop"
                value_1 = "no-drop"

            action: ActionEnum | None = None
            """
            Action on stuck queue.
            """
            timeout: Annotated[str, StrConvert(convert_types=(int, float))] | None = Field(None, pattern=r"^\d+(\.\d{1,2})?$")
            """
            Timeout in seconds after which port should be errdisabled or
            should start dropping on congested priorities.
            This should
            be decimal with up to 2 decimal point.
            Example: 0.01 or 60
            """
            polling_interval: Annotated[str, StrConvert(convert_types=(int, float))] | None = Field(None, pattern=r"^\d+(\.\d{1,3})?$")
            """
            Time interval in seconds at which the watchdog should poll the queues.
            This should be decimal with up to 3 decimal
            point.
            Example: 0.005 or 60
            """
            recovery_time: Annotated[str, StrConvert(convert_types=(int, float))] | None = Field(None, pattern=r"^\d+(\.\d{1,2})?$")
            """
            Recovery-time in seconds after which stuck queue should
            recover and start forwarding again.
            This should be decimal with
            up to 2 decimal point.
            Example: 0.01 or 60
            """
            override_action_drop: bool | None = None
            """
            Override configured action on stuck queue to drop.
            """

        all_off: bool | None = None
        """
        Disable PFC on all interfaces.
        """
        watchdog: Watchdog | None = None

    class Ptp(BaseModel):
        model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

        class ModeEnum(Enum):
            value_0 = "boundary"
            value_1 = "transparent"

        class Source(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            ip: str | None = None
            """
            Source IP
            """

        class MessageType(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class General(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                dscp: int | None = None

            class Event(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                dscp: int | None = None

            general: General | None = None
            event: Event | None = None

        class Monitor(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Threshold(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Drop(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    offset_from_master: int | None = Field(None, ge=0, le=1000000000)
                    mean_path_delay: int | None = Field(None, ge=0, le=1000000000)

                offset_from_master: int | None = Field(None, ge=0, le=1000000000)
                mean_path_delay: int | None = Field(None, ge=0, le=1000000000)
                drop: Drop | None = None

            class MissingMessage(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Intervals(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    announce: int | None = Field(None, ge=2, le=255)
                    follow_up: int | None = Field(None, ge=2, le=255)
                    sync: int | None = Field(None, ge=2, le=255)

                class SequenceIds(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    enabled: bool | None = None
                    announce: int | None = Field(None, ge=2, le=255)
                    delay_resp: int | None = Field(None, ge=2, le=255)
                    follow_up: int | None = Field(None, ge=2, le=255)
                    sync: int | None = Field(None, ge=2, le=255)

                intervals: Intervals | None = None
                sequence_ids: SequenceIds | None = None

            enabled: bool | None = True
            threshold: Threshold | None = None
            missing_message: MissingMessage | None = None

        mode: ModeEnum | None = None
        forward_unicast: bool | None = None
        clock_identity: str | None = None
        """
        The clock-id in xx:xx:xx:xx:xx:xx format
        """
        source: Source | None = None
        priority1: int | None = Field(None, ge=0, le=255)
        priority2: int | None = Field(None, ge=0, le=255)
        ttl: int | None = Field(None, ge=1, le=255)
        domain: int | None = Field(None, ge=0, le=255)
        message_type: MessageType | None = None
        monitor: Monitor | None = None

    class Qos(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Map(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            cos: list[str] | None = None
            dscp: list[str] | None = None
            exp: list[str] | None = None
            traffic_class: list[str] | None = None

        class RandomDetect(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Ecn(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class AllowNonEct(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    enabled: bool | None = None
                    """
                    Allow non-ect and set drop-precedence 1 in a policy map simultaneously.
                    Check which command is required for your
                    platform.
                    """
                    chip_based: bool | None = None
                    """
                    Allow non-ect chip-based
                    """

                allow_non_ect: AllowNonEct | None = None

            ecn: Ecn | None = None
            """
            Global ECN Configuration
            """

        map: Map | None = None
        rewrite_dscp: bool | None = None
        random_detect: RandomDetect | None = None
        """
        Global random-detect settings
        """

    class QosProfilesItem(BaseModel):
        model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

        class TrustEnum(Enum):
            value_0 = "cos"
            value_1 = "dscp"
            value_2 = "disabled"

        class Shape(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            rate: str | None = None
            """
            Supported options are platform dependent
            Example: "< rate > kbps", "1-100 percent", "< rate > pps"
            """

        class ServicePolicy(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Type(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                qos_input: str | None = None
                """
                Policy-map name
                """

            type: Type | None = None

        class TxQueuesItem(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class PriorityEnum(Enum):
                value_0 = "priority strict"
                value_1 = "no priority"

            class Shape(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                rate: str | None = None
                """
                Supported options are platform dependent
                Example: "< rate > kbps", "1-100 percent", "< rate > pps"
                """

            class RandomDetect(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Ecn(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class Threshold(BaseModel):
                        model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                        class UnitsEnum(Enum):
                            value_0 = "segments"
                            value_1 = "bytes"
                            value_2 = "kbytes"
                            value_3 = "mbytes"
                            value_4 = "milliseconds"

                        units: UnitsEnum = None
                        """
                        Units to be used for the threshold values.
                        This should be one of segments, byte, kbytes, mbytes.
                        """
                        min: int = Field(None, ge=1)
                        """
                        Random-detect ECN minimum-threshold
                        """
                        max: int = Field(None, ge=1)
                        """
                        Random-detect ECN maximum-threshold
                        """
                        max_probability: int | None = Field(None, ge=1, le=100)
                        """
                        Random-detect ECN maximum mark probability
                        """
                        weight: int | None = Field(None, ge=0, le=15)
                        """
                        Random-detect ECN weight
                        """

                    count: bool | None = None
                    """
                    Enable counter for random-detect ECNs
                    """
                    threshold: Threshold | None = None

                class Drop(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class Threshold(BaseModel):
                        model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                        class UnitsEnum(Enum):
                            value_0 = "segments"
                            value_1 = "bytes"
                            value_2 = "kbytes"
                            value_3 = "mbytes"
                            value_4 = "microseconds"
                            value_5 = "milliseconds"

                        units: UnitsEnum = None
                        """
                        Units to be used for the threshold values.
                        """
                        drop_precedence: int | None = Field(None, ge=0, le=2)
                        """
                        Specify Drop Precendence value
                        """
                        min: int = Field(None, ge=1)
                        """
                        WRED minimum-threshold
                        """
                        max: int = Field(None, ge=1)
                        """
                        WRED maximum-threshold
                        """
                        drop_probability: int = Field(None, ge=1, le=100)
                        """
                        WRED drop probability.
                        """
                        weight: int | None = Field(None, ge=0, le=15)
                        """
                        WRED weight
                        """

                    threshold: Threshold | None = None

                ecn: Ecn | None = None
                """
                Explicit Congestion Notification
                """
                drop: Drop | None = None
                """
                Set WRED parameters
                """

            id: int = None
            """
            TX-Queue ID
            """
            bandwidth_percent: int | None = None
            bandwidth_guaranteed_percent: int | None = None
            priority: PriorityEnum | None = None
            shape: Shape | None = None
            comment: str | None = None
            """
            Text comment added to queue
            """
            random_detect: RandomDetect | None = None

        class UcTxQueuesItem(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class PriorityEnum(Enum):
                value_0 = "priority strict"
                value_1 = "no priority"

            class Shape(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                rate: str | None = None
                """
                Supported options are platform dependent
                Example: "< rate > kbps", "1-100 percent", "< rate > pps"
                """

            class RandomDetect(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Ecn(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class Threshold(BaseModel):
                        model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                        class UnitsEnum(Enum):
                            value_0 = "segments"
                            value_1 = "bytes"
                            value_2 = "kbytes"
                            value_3 = "mbytes"
                            value_4 = "milliseconds"

                        units: UnitsEnum = None
                        """
                        Unit to be used for the threshold values
                        """
                        min: int = Field(None, ge=1)
                        """
                        Random-detect ECN minimum-threshold
                        """
                        max: int = Field(None, ge=1)
                        """
                        Random-detect ECN maximum-threshold
                        """
                        max_probability: int | None = Field(None, ge=1, le=100)
                        """
                        Random-detect ECN maximum mark probability
                        """
                        weight: int | None = Field(None, ge=0, le=15)
                        """
                        Random-detect ECN weight
                        """

                    count: bool | None = None
                    """
                    Enable counter for random-detect ECNs
                    """
                    threshold: Threshold | None = None

                class Drop(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class Threshold(BaseModel):
                        model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                        class UnitsEnum(Enum):
                            value_0 = "segments"
                            value_1 = "bytes"
                            value_2 = "kbytes"
                            value_3 = "mbytes"
                            value_4 = "microseconds"
                            value_5 = "milliseconds"

                        units: UnitsEnum = None
                        """
                        Units to be used for the threshold values.
                        """
                        drop_precedence: int | None = Field(None, ge=0, le=2)
                        """
                        Specify Drop Precendence value
                        """
                        min: int = Field(None, ge=1)
                        """
                        WRED minimum-threshold
                        """
                        max: int = Field(None, ge=1)
                        """
                        WRED maximum-threshold
                        """
                        drop_probability: int = Field(None, ge=1, le=100)
                        """
                        WRED drop probability.
                        """
                        weight: int | None = Field(None, ge=0, le=15)
                        """
                        WRED weight
                        """

                    threshold: Threshold | None = None

                ecn: Ecn | None = None
                """
                Explicit Congestion Notification
                """
                drop: Drop | None = None
                """
                Set WRED parameters
                """

            id: int = None
            """
            UC TX queue ID
            """
            bandwidth_percent: int | None = None
            bandwidth_guaranteed_percent: int | None = None
            priority: PriorityEnum | None = None
            shape: Shape | None = None
            comment: str | None = None
            """
            Text comment added to queue
            """
            random_detect: RandomDetect | None = None

        class McTxQueuesItem(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class PriorityEnum(Enum):
                value_0 = "priority strict"
                value_1 = "no priority"

            class Shape(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                rate: str | None = None
                """
                Supported options are platform dependent
                Example: "< rate > kbps", "1-100 percent", "< rate > pps"
                """

            id: int = None
            """
            MC TX queue ID
            """
            bandwidth_percent: int | None = None
            bandwidth_guaranteed_percent: int | None = None
            priority: PriorityEnum | None = None
            shape: Shape | None = None
            comment: str | None = None
            """
            Text comment added to queue.
            """

        class PriorityFlowControl(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Watchdog(BaseModel):
                model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                class ActionEnum(Enum):
                    value_0 = "drop"
                    value_1 = "notify-only"

                class Timer(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    timeout: Annotated[str, StrConvert(convert_types=(int, float))] = Field(None, pattern=r"^\d+(\.\d{1,2})?$")
                    """
                    Timeout in seconds after which port should be errdisabled or
                    should start dropping on congested priorities.
                    This should
                    be decimal with up to 2 decimal point
                    Example: 0.01 or 60
                    """
                    polling_interval: Annotated[str, StrConvert(convert_types=(int, float))] = Field(None, pattern=r"^auto|\d+(\.\d{1,3})?$")
                    """
                    Time interval in seconds at which the watchdog should poll the queues.
                    This should be decimal with up to 3 decimal point
                    or set
                    to 'auto' based on recovery_time and timeout values.
                    Example: 0.005 or 60
                    """
                    recovery_time: Annotated[str, StrConvert(convert_types=(int, float))] = Field(None, pattern=r"^\d+(\.\d{1,2})?$")
                    """
                    Recovery-time in seconds after which stuck queue should
                    recover and start forwarding again.
                    This should be decimal with
                    up to 2 decimal point.
                    Example: 0.01 or 60
                    """
                    forced: bool | None = None
                    """
                    Force recover any stuck queue(s) after the duration,
                    irrespective of whether PFC frames are being
                    received or not.
                    """

                enabled: bool = None
                """
                Enable the watchdog on stuck transmit queues.
                """
                action: ActionEnum | None = None
                """
                Override the default error-disable action to either drop
                traffic on the stuck queue or notify-only
                without making any
                actions on the stuck queue.
                """
                timer: Timer | None = None
                """
                Timer thresholds whilst monitoring queues.
                """

            class PrioritiesItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                priority: int = Field(None, ge=0, le=7)
                """
                Priority queue number (COS value)
                """
                no_drop: bool = None
                """
                Enable Priority Flow Control frames on this queue
                """

            enabled: bool | None = None
            """
            Enable Priority Flow control.
            """
            watchdog: Watchdog | None = None
            """
            Watchdog can detect stuck transmit queues.
            """
            priorities: list[PrioritiesItem] | None = None
            """
            Set the drop/no_drop on each queue
            """

        name: str = None
        """
        Profile-Name
        """
        trust: TrustEnum | None = None
        cos: int | None = None
        dscp: int | None = None
        shape: Shape | None = None
        service_policy: ServicePolicy | None = None
        tx_queues: list[TxQueuesItem] | None = None
        uc_tx_queues: list[UcTxQueuesItem] | None = None
        mc_tx_queues: list[McTxQueuesItem] | None = None
        priority_flow_control: PriorityFlowControl | None = None
        """
        Priority Flow Control settings
        """

    class QueueMonitorLength(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class DefaultThresholds(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            high: int = None
            """
            Default high threshold for Ethernet Interfaces.
            """
            low: int | None = None
            """
            Default low threshold for Ethernet Interfaces.
            Low threshold support is platform dependent.
            """

        class Cpu(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Thresholds(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                high: int = None
                low: int | None = None

            thresholds: Thresholds | None = None

        enabled: bool = None
        default_thresholds: DefaultThresholds | None = None
        log: int | None = None
        """
        Logging interval in seconds
        """
        notifying: bool | None = None
        """
        Should only be used for platforms supporting the "queue-monitor length notifying" CLI
        """
        cpu: Cpu | None = None

    class QueueMonitorStreaming(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        enable: bool | None = None
        ip_access_group: str | None = None
        """
        Name of IP ACL
        """
        ipv6_access_group: str | None = None
        """
        Name of IPv6 ACL
        """
        max_connections: int | None = Field(None, ge=1, le=100)
        vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None

    class RadiusServer(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Attribute32IncludeInAccessReq(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            hostname: bool | None = None
            format: str | None = None
            """
            Specify the format of the NAS-Identifier. If 'hostname' is set, this is ignored.
            """

        class DynamicAuthorization(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            port: int | None = Field(None, ge=0, le=65535)
            """
            TCP Port
            """
            tls_ssl_profile: str | None = None
            """
            Name of TLS profile
            """

        class HostsItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            host: str = None
            """
            Host IP address or name
            """
            vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
            timeout: int | None = Field(None, ge=1, le=1000)
            retransmit: int | None = Field(None, ge=0, le=100)
            key: str | None = None
            """
            Encrypted key
            """

        attribute_32_include_in_access_req: Attribute32IncludeInAccessReq | None = None
        dynamic_authorization: DynamicAuthorization | None = None
        hosts: list[HostsItem] | None = None

    class RadiusServersItem(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        host: str | None = None
        """
        Host IP address or name
        """
        vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
        key: str | None = None
        """
        Encrypted key
        """

    class Redundancy(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        protocol: str | None = None
        """
        Redundancy Protocol
        """

    class RolesItem(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class SequenceNumbersItem(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class ActionEnum(Enum):
                value_0 = "permit"
                value_1 = "deny"

            sequence: int | None = None
            """
            Sequence number
            """
            action: ActionEnum | None = None
            mode: str | None = None
            """
            "config", "config-all", "exec" or mode key as string
            """
            command: str | None = None
            """
            Command as string
            """

        name: str | None = None
        """
        Role name
        """
        sequence_numbers: list[SequenceNumbersItem] | None = None

    class RouteMapsItem(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class SequenceNumbersItem(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class TypeEnum(Enum):
                value_0 = "permit"
                value_1 = "deny"

            class Continue(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                enabled: bool | None = None
                sequence_number: int | None = None

            sequence: int = None
            """
            Sequence ID
            """
            type: TypeEnum = None
            description: str | None = None
            match: list[str] | None = None
            """
            List of "match" statements
            """
            set: list[str] | None = None
            """
            List of "set" statements
            """
            sub_route_map: str | None = None
            """
            Name of Sub-Route-map
            """
            field_continue: Continue | None = Field(None, alias="continue")

        name: str = None
        """
        Route-map Name
        """
        sequence_numbers: list[SequenceNumbersItem] = None

    class RouterAdaptiveVirtualTopology(BaseModel):
        model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

        class TopologyRoleEnum(Enum):
            value_0 = "edge"
            value_1 = "pathfinder"
            value_2 = "transit region"
            value_3 = "transit zone"

        class Region(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str = None
            id: int = Field(None, ge=1, le=255)

        class Zone(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str = None
            id: int = Field(None, ge=1, le=10000)

        class Site(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str = None
            id: int = Field(None, ge=1, le=10000)

        topology_role: TopologyRoleEnum | None = None
        """
        Role name.
        """
        region: Region | None = None
        """
        Region name and ID.
        """
        zone: Zone | None = None
        """
        Zone name and ID.
        """
        site: Site | None = None
        """
        Site name and ID.
        """

    class RouterBfd(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Multihop(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            interval: int | None = None
            """
            Rate in milliseconds
            """
            min_rx: int | None = None
            """
            Rate in milliseconds
            """
            multiplier: int | None = Field(None, ge=3, le=50)

        class Sbfd(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class LocalInterface(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Protocols(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    ipv4: bool | None = None
                    ipv6: bool | None = None

                name: str | None = None
                """
                Interface Name
                """
                protocols: Protocols | None = None

            class Reflector(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                min_rx: int | None = None
                """
                Rate in milliseconds
                """
                local_discriminator: str | None = None
                """
                IPv4 address or 32 bit integer
                """

            local_interface: LocalInterface | None = None
            initiator_interval: int | None = None
            """
            Rate in milliseconds
            """
            initiator_multiplier: int | None = Field(None, ge=3, le=50)
            reflector: Reflector | None = None

        interval: int | None = None
        """
        Rate in milliseconds
        """
        min_rx: int | None = None
        """
        Rate in milliseconds
        """
        multiplier: int | None = Field(None, ge=3, le=50)
        multihop: Multihop | None = None
        sbfd: Sbfd | None = None

    class RouterBgp(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Distance(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            external_routes: int = Field(None, ge=1, le=255)
            internal_routes: int = Field(None, ge=1, le=255)
            local_routes: int = Field(None, ge=1, le=255)

        class GracefulRestart(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            enabled: bool | None = None
            restart_time: int | None = Field(None, ge=1, le=3600)
            """
            Number of seconds
            """
            stalepath_time: int | None = Field(None, ge=1, le=3600)
            """
            Number of seconds
            """

        class GracefulRestartHelper(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            enabled: bool | None = None
            restart_time: int | None = Field(None, ge=1, le=100000000)
            """
            Number of seconds
            graceful-restart-help long-lived and restart-time are mutually exclusive in CLI.
            restart-time will
            take precedence if both are configured.
            """
            long_lived: bool | None = None
            """
            graceful-restart-help long-lived and restart-time are mutually exclusive in CLI.
            restart-time will take precedence if
            both are configured.
            """

        class MaximumPaths(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            paths: int = Field(None, ge=1, le=600)
            ecmp: int | None = Field(None, ge=1, le=600)

        class Updates(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            wait_for_convergence: bool | None = None
            """
            Disables FIB updates and route advertisement when the BGP instance is initiated until the BGP convergence state is
            reached.
            """
            wait_install: bool | None = None
            """
            Do not advertise reachability to a prefix until that prefix has been installed in hardware.
            This will eliminate any
            temporary black holes due to a BGP speaker advertising reachability to a prefix that may not yet be installed into the
            forwarding plane.
            """

        class Bgp(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Default(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                ipv4_unicast: bool | None = None
                """
                Default activation of IPv4 unicast address-family on all IPv4 neighbors (EOS default = True).
                """
                ipv4_unicast_transport_ipv6: bool | None = None
                """
                Default activation of IPv4 unicast address-family on all IPv6 neighbors (EOS default == False).
                """

            class RouteReflectorPreserveAttributes(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                enabled: bool | None = None
                always: bool | None = None

            class Bestpath(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                d_path: bool | None = None

            default: Default | None = None
            route_reflector_preserve_attributes: RouteReflectorPreserveAttributes | None = None
            bestpath: Bestpath | None = None

        class ListenRangesItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            prefix: str | None = None
            """
            IPv4 prefix "A.B.C.D/E" or IPv6 prefix "A:B:C:D:E:F:G:H/I"
            """
            peer_id_include_router_id: bool | None = None
            """
            Include router ID as part of peer filter
            """
            peer_group: str | None = None
            """
            Peer group name
            """
            peer_filter: str | None = None
            """
            Peer-filter name
            note: `peer_filter` or `remote_as` is required but mutually exclusive.
            If both are defined,
            `peer_filter` takes precedence
            """
            remote_as: Annotated[str, StrConvert(convert_types=(int))] | None = None
            """
            BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>"
            """

        class PeerGroupsItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class AsPath(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                remote_as_replace_out: bool | None = None
                """
                Replace AS number with local AS number
                """
                prepend_own_disabled: bool | None = None
                """
                Disable prepending own AS number to AS path
                """

            class RemovePrivateAs(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                enabled: bool | None = None
                all: bool | None = None
                replace_as: bool | None = None

            class RemovePrivateAsIngress(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                enabled: bool | None = None
                replace_as: bool | None = None

            class DefaultOriginate(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                enabled: bool | None = None
                always: bool | None = None
                route_map: str | None = None
                """
                Route-map name
                """

            class LinkBandwidth(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                enabled: bool | None = None
                default: str | None = None
                """
                nn.nn(K|M|G) link speed in bits/second
                """

            class AllowasIn(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                enabled: bool | None = None
                times: int | None = Field(None, ge=1, le=10)
                """
                Number of local ASNs allowed in a BGP update
                """

            class RibInPrePolicyRetain(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                enabled: bool | None = None
                all: bool | None = None

            name: str = None
            """
            Peer-group name
            """
            type: str | None = None
            """
            Key only used for documentation or validation purposes
            """
            remote_as: Annotated[str, StrConvert(convert_types=(int))] | None = None
            """
            BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>"
            """
            local_as: Annotated[str, StrConvert(convert_types=(int))] | None = None
            """
            BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>"
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
            ebgp_multihop: int | None = Field(None, ge=1, le=255)
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
            maximum_routes: int | None = Field(None, ge=0, le=4294967294)
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
            weight: int | None = Field(None, ge=0, le=65535)
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

        class NeighborsItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class AsPath(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                remote_as_replace_out: bool | None = None
                """
                Replace AS number with local AS number
                """
                prepend_own_disabled: bool | None = None
                """
                Disable prepending own AS number to AS path
                """

            class DefaultOriginate(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                enabled: bool | None = None
                always: bool | None = None
                route_map: str | None = None

            class AllowasIn(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                enabled: bool | None = None
                times: int | None = Field(None, ge=1, le=10)
                """
                Number of local ASNs allowed in a BGP update
                """

            class LinkBandwidth(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                enabled: bool | None = None
                default: str | None = None
                """
                nn.nn(K|M|G) link speed in bits/second
                """

            class RibInPrePolicyRetain(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                enabled: bool | None = None
                all: bool | None = None

            class RemovePrivateAs(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                enabled: bool | None = None
                all: bool | None = None
                replace_as: bool | None = None

            class RemovePrivateAsIngress(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                enabled: bool | None = None
                replace_as: bool | None = None

            ip_address: str = None
            peer_group: str | None = None
            remote_as: Annotated[str, StrConvert(convert_types=(int))] | None = None
            """
            BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>"
            """
            local_as: Annotated[str, StrConvert(convert_types=(int))] | None = None
            """
            BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>"
            """
            as_path: AsPath | None = None
            """
            BGP AS-PATH options
            """
            description: str | None = None
            route_reflector_client: bool | None = None
            passive: bool | None = None
            shutdown: bool | None = None
            update_source: str | None = None
            """
            Source Interface
            """
            bfd: bool | None = None
            weight: int | None = Field(None, ge=0, le=65535)
            timers: str | None = None
            """
            BGP Keepalive and Hold Timer values in seconds as string "<0-3600> <0-3600>"
            """
            route_map_in: str | None = None
            """
            Inbound route-map name
            """
            route_map_out: str | None = None
            """
            Outbound route-map name
            """
            default_originate: DefaultOriginate | None = None
            send_community: str | None = None
            """
            'all' or a combination of 'standard', 'extended', 'large' and 'link-bandwidth (w/options)'
            """
            maximum_routes: int | None = Field(None, ge=0, le=4294967294)
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
            allowas_in: AllowasIn | None = None
            ebgp_multihop: int | None = Field(None, ge=1, le=255)
            """
            Time-to-live in range of hops
            """
            next_hop_self: bool | None = None
            link_bandwidth: LinkBandwidth | None = None
            rib_in_pre_policy_retain: RibInPrePolicyRetain | None = None
            remove_private_as: RemovePrivateAs | None = None
            """
            Remove private AS numbers in outbound AS path
            """
            remove_private_as_ingress: RemovePrivateAsIngress | None = None
            session_tracker: str | None = None

        class NeighborInterfacesItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str = None
            """
            Interface name
            """
            remote_as: Annotated[str, StrConvert(convert_types=(int))] | None = None
            peer_group: str | None = "Peer-group name"
            description: str | None = None
            peer_filter: str | None = None
            """
            Peer-filter name
            """

        class AggregateAddressesItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            prefix: str = None
            """
            IPv4 prefix "A.B.C.D/E" or IPv6 prefix "A:B:C:D:E:F:G:H/I"
            """
            advertise_only: bool | None = None
            as_set: bool | None = None
            summary_only: bool | None = None
            attribute_map: str | None = None
            """
            Route-map name
            """
            match_map: str | None = None
            """
            Route-map name
            """

        class RedistributeRoutesItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            source_protocol: str = None
            route_map: str | None = None
            include_leaked: bool | None = None

        class VlanAwareBundlesItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class RdEvpnDomain(BaseModel):
                model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                class DomainEnum(Enum):
                    value_0 = "remote"
                    value_1 = "all"

                domain: DomainEnum | None = None
                rd: str | None = None
                """
                Route distinguisher
                """

            class RouteTargets(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class ImportEvpnDomainsItem(BaseModel):
                    model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                    class DomainEnum(Enum):
                        value_0 = "remote"
                        value_1 = "all"

                    domain: DomainEnum | None = None
                    route_target: str | None = None

                class ExportEvpnDomainsItem(BaseModel):
                    model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                    class DomainEnum(Enum):
                        value_0 = "remote"
                        value_1 = "all"

                    domain: DomainEnum | None = None
                    route_target: str | None = None

                class ImportExportEvpnDomainsItem(BaseModel):
                    model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                    class DomainEnum(Enum):
                        value_0 = "remote"
                        value_1 = "all"

                    domain: DomainEnum | None = None
                    route_target: str | None = None

                both: list[str] | None = None
                field_import: list[str] | None = Field(None, alias="import")
                export: list[str] | None = None
                import_evpn_domains: list[ImportEvpnDomainsItem] | None = None
                export_evpn_domains: list[ExportEvpnDomainsItem] | None = None
                import_export_evpn_domains: list[ImportExportEvpnDomainsItem] | None = None

            name: str = None
            """
            VLAN aware bundle name
            """
            tenant: str | None = None
            """
            Key only used for documentation or validation purposes
            """
            description: str | None = None
            """
            Key only used for documentation or validation purposes
            """
            rd: str | None = None
            """
            Route distinguisher
            """
            rd_evpn_domain: RdEvpnDomain | None = None
            route_targets: RouteTargets | None = None
            redistribute_routes: list[str] | None = None
            no_redistribute_routes: list[str] | None = None
            vlan: Annotated[str, StrConvert(convert_types=(int))] | None = None
            """
            VLAN range as string. Example "100-200,300"
            """
            eos_cli: str | None = None
            """
            Multiline EOS CLI rendered directly on the Router BGP, VLAN-aware-bundle definition in the final EOS configuration
            """

        class VlansItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class RdEvpnDomain(BaseModel):
                model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                class DomainEnum(Enum):
                    value_0 = "remote"
                    value_1 = "all"

                domain: DomainEnum | None = None
                rd: str | None = None
                """
                Route distinguisher
                """

            class RouteTargets(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class ImportEvpnDomainsItem(BaseModel):
                    model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                    class DomainEnum(Enum):
                        value_0 = "remote"
                        value_1 = "all"

                    domain: DomainEnum | None = None
                    route_target: str | None = None

                class ExportEvpnDomainsItem(BaseModel):
                    model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                    class DomainEnum(Enum):
                        value_0 = "remote"
                        value_1 = "all"

                    domain: DomainEnum | None = None
                    route_target: str | None = None

                class ImportExportEvpnDomainsItem(BaseModel):
                    model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                    class DomainEnum(Enum):
                        value_0 = "remote"
                        value_1 = "all"

                    domain: DomainEnum | None = None
                    route_target: str | None = None

                both: list[str] | None = None
                field_import: list[str] | None = Field(None, alias="import")
                export: list[str] | None = None
                import_evpn_domains: list[ImportEvpnDomainsItem] | None = None
                export_evpn_domains: list[ExportEvpnDomainsItem] | None = None
                import_export_evpn_domains: list[ImportExportEvpnDomainsItem] | None = None

            id: int = None
            tenant: str | None = None
            """
            Key only used for documentation or validation purposes
            """
            rd: str | None = None
            """
            Route distinguisher
            """
            rd_evpn_domain: RdEvpnDomain | None = None
            eos_cli: str | None = None
            """
            Multiline EOS CLI rendered directly on the Router BGP, VLAN definition in the final EOS configuration
            """
            route_targets: RouteTargets | None = None
            redistribute_routes: list[str] | None = None
            no_redistribute_routes: list[str] | None = None

        class VpwsItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class RouteTargets(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                import_export: str | None = None
                """
                Route Target
                """

            class PseudowiresItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                name: str = None
                """
                Pseudowire name
                """
                id_local: int | None = None
                """
                Must match id_remote on other pe
                """
                id_remote: int | None = None
                """
                Must match id_local on other pe
                """

            name: str = None
            """
            VPWS instance name
            """
            rd: str | None = None
            """
            Route distinguisher
            """
            route_targets: RouteTargets | None = None
            mpls_control_word: bool | None = None
            label_flow: bool | None = None
            mtu: int | None = None
            pseudowires: list[PseudowiresItem] | None = None

        class AddressFamilyEvpn(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class NeighborDefault(BaseModel):
                model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                class EncapsulationEnum(Enum):
                    value_0 = "vxlan"
                    value_1 = "mpls"

                class NextHopSelfReceivedEvpnRoutes(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    enable: bool | None = None
                    inter_domain: bool | None = None

                encapsulation: EncapsulationEnum | None = None
                next_hop_self_source_interface: str | None = None
                """
                Source interface name
                """
                next_hop_self_received_evpn_routes: NextHopSelfReceivedEvpnRoutes | None = None

            class PeerGroupsItem(BaseModel):
                model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                class EncapsulationEnum(Enum):
                    value_0 = "vxlan"
                    value_1 = "mpls"

                class AdditionalPaths(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class Send(BaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        any: bool | None = None
                        backup: bool | None = None
                        ecmp: bool | None = None
                        ecmp_limit: int | None = Field(None, ge=2, le=64)
                        """
                        Amount of ECMP paths to send
                        """
                        limit: int | None = Field(None, ge=2, le=64)
                        """
                        Amount of paths to send
                        """

                    receive: bool | None = None
                    send: Send | None = None

                name: str = None
                """
                Peer-group name
                """
                activate: bool | None = None
                route_map_in: str | None = None
                """
                Inbound route-map name
                """
                route_map_out: str | None = None
                """
                Outbound route-map name
                """
                domain_remote: bool | None = None
                encapsulation: EncapsulationEnum | None = None
                additional_paths: AdditionalPaths | None = None

            class EvpnHostflapDetection(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                enabled: bool | None = None
                window: int | None = Field(None, ge=0, le=4294967295)
                """
                Time (in seconds) to detect a MAC duplication issue
                """
                threshold: int | None = Field(None, ge=0, le=4294967295)
                """
                Minimum number of MAC moves that indicate a MAC Duplication issue
                """
                expiry_timeout: int | None = Field(None, ge=0, le=4294967295)
                """
                Time (in seconds) to purge a MAC duplication issue
                """

            class NextHop(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                resolution_disabled: bool | None = None

            class Route(BaseModel):
                model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                class ImportMatchFailureActionEnum(Enum):
                    value_0 = "discard"

                import_match_failure_action: ImportMatchFailureActionEnum | None = None

            domain_identifier: str | None = None
            neighbor_default: NeighborDefault | None = None
            peer_groups: list[PeerGroupsItem] | None = None
            evpn_hostflap_detection: EvpnHostflapDetection | None = None
            next_hop: NextHop | None = None
            route: Route | None = None
            next_hop_unchanged: bool | None = None

        class AddressFamilyRtc(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class PeerGroupsItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class DefaultRouteTarget(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    only: bool | None = None
                    encoding_origin_as_omit: str | None = None

                name: str = None
                """
                Peer-group name
                """
                activate: bool | None = None
                default_route_target: DefaultRouteTarget | None = None

            peer_groups: list[PeerGroupsItem] | None = None

        class AddressFamilyIpv4(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class NetworksItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                prefix: str = None
                """
                IPv4 prefix "A.B.C.D/E" or IPv6 prefix "A:B:C:D:E:F:G:H/I"
                """
                route_map: str | None = None
                """
                Route-map name
                """

            class PeerGroupsItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class DefaultOriginate(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    always: bool | None = None
                    route_map: str | None = None
                    """
                    Route-map name
                    """

                class NextHop(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class AddressFamilyIpv6(BaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        enabled: bool = None
                        originate: bool | None = None

                    address_family_ipv6: AddressFamilyIpv6 | None = None
                    address_family_ipv6_originate: bool | None = None

                name: str = None
                """
                Peer-group name
                """
                activate: bool | None = None
                route_map_in: str | None = None
                """
                Inbound route-map name
                """
                route_map_out: str | None = None
                """
                Outbound route-map name
                """
                default_originate: DefaultOriginate | None = None
                next_hop: NextHop | None = None
                prefix_list_in: str | None = None
                """
                Inbound prefix-list name
                """
                prefix_list_out: str | None = None
                """
                Outbound prefix-list name
                """

            class NeighborsItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class DefaultOriginate(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    always: bool | None = None
                    route_map: str | None = None

                ip_address: str = None
                activate: bool | None = None
                route_map_in: str | None = None
                """
                Inbound route-map name
                """
                route_map_out: str | None = None
                """
                Outbound route-map name
                """
                prefix_list_in: str | None = None
                """
                Inbound prefix-list name
                """
                prefix_list_out: str | None = None
                """
                Prefix-list name
                """
                default_originate: DefaultOriginate | None = None

            networks: list[NetworksItem] | None = None
            peer_groups: list[PeerGroupsItem] | None = None
            neighbors: list[NeighborsItem] | None = None

        class AddressFamilyIpv4Multicast(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class PeerGroupsItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                name: str = None
                """
                Peer-group name
                """
                activate: bool | None = None
                route_map_in: str | None = None
                """
                Inbound route-map name
                """
                route_map_out: str | None = None
                """
                Outbound route-map name
                """

            class NeighborsItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                ip_address: str = None
                activate: bool | None = None
                route_map_in: str | None = None
                """
                Inbound route-map name
                """
                route_map_out: str | None = None
                """
                Outbound route-map name
                """

            class RedistributeRoutesItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                source_protocol: str = None
                route_map: str | None = None

            peer_groups: list[PeerGroupsItem] | None = None
            neighbors: list[NeighborsItem] | None = None
            redistribute_routes: list[RedistributeRoutesItem] | None = None

        class AddressFamilyIpv4SrTe(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class NeighborsItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                ip_address: str = None
                activate: bool | None = None
                route_map_in: str | None = None
                """
                Inbound route-map name
                """
                route_map_out: str | None = None
                """
                Outbound route-map name
                """

            class PeerGroupsItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                name: str = None
                """
                Peer-group name
                """
                activate: bool | None = None
                route_map_in: str | None = None
                """
                Inbound route-map name
                """
                route_map_out: str | None = None
                """
                Outbound route-map name
                """

            neighbors: list[NeighborsItem] | None = None
            peer_groups: list[PeerGroupsItem] | None = None

        class AddressFamilyIpv6(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class NetworksItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                prefix: str = None
                """
                IPv4 prefix "A.B.C.D/E" or IPv6 prefix "A:B:C:D:E:F:G:H/I"
                """
                route_map: str | None = None
                """
                Route-map name
                """

            class PeerGroupsItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                name: str = None
                """
                Peer-group name
                """
                activate: bool | None = None
                route_map_in: str | None = None
                """
                Inbound route-map name
                """
                route_map_out: str | None = None
                """
                Outbound route-map name
                """
                prefix_list_in: str | None = None
                """
                Inbound prefix-list name
                """
                prefix_list_out: str | None = None
                """
                Outbound prefix-list name
                """

            class NeighborsItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                ip_address: str = None
                activate: bool | None = None
                route_map_in: str | None = None
                """
                Inbound route-map name
                """
                route_map_out: str | None = None
                """
                Outbound route-map name
                """
                prefix_list_in: str | None = None
                """
                Inbound prefix-list name
                """
                prefix_list_out: str | None = None
                """
                Outbound prefix-list name
                """

            class RedistributeRoutesItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                source_protocol: str = None
                route_map: str | None = None
                include_leaked: bool | None = None

            networks: list[NetworksItem] | None = None
            peer_groups: list[PeerGroupsItem] | None = None
            neighbors: list[NeighborsItem] | None = None
            redistribute_routes: list[RedistributeRoutesItem] | None = None

        class AddressFamilyIpv6Multicast(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Bgp(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class MissingPolicy(BaseModel):
                    model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                    class DirectionInActionEnum(Enum):
                        value_0 = "deny"
                        value_1 = "deny-in-out"
                        value_2 = "permit"

                    class DirectionOutActionEnum(Enum):
                        value_0 = "deny"
                        value_1 = "deny-in-out"
                        value_2 = "permit"

                    direction_in_action: DirectionInActionEnum | None = None
                    direction_out_action: DirectionOutActionEnum | None = None

                class AdditionalPaths(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    receive: bool | None = None

                missing_policy: MissingPolicy | None = None
                additional_paths: AdditionalPaths | None = None

            class NeighborsItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                ip_address: str = None
                activate: bool | None = None
                route_map_in: str | None = None
                """
                Inbound route-map name
                """
                route_map_out: str | None = None
                """
                Outbound route-map name
                """

            class PeerGroupsItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                name: str = None
                """
                Peer-group name
                """
                activate: bool | None = None

            class NetworksItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                prefix: str = None
                """
                IPv6 prefix "A:B:C:D:E:F:G:H/I"
                """
                route_map: str | None = None

            bgp: Bgp | None = None
            neighbors: list[NeighborsItem] | None = None
            peer_groups: list[PeerGroupsItem] | None = None
            networks: list[NetworksItem] | None = None

        class AddressFamilyIpv6SrTe(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class NeighborsItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                ip_address: str = None
                activate: bool | None = None
                route_map_in: str | None = None
                """
                Inbound route-map name
                """
                route_map_out: str | None = None
                """
                Outbound route-map name
                """

            class PeerGroupsItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                name: str = None
                """
                Peer-group name
                """
                activate: bool | None = None
                route_map_in: str | None = None
                """
                Inbound route-map name
                """
                route_map_out: str | None = None
                """
                Outbound route-map name
                """

            neighbors: list[NeighborsItem] | None = None
            peer_groups: list[PeerGroupsItem] | None = None

        class AddressFamilyLinkState(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Bgp(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class MissingPolicy(BaseModel):
                    model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                    class DirectionInActionEnum(Enum):
                        value_0 = "deny"
                        value_1 = "deny-in-out"
                        value_2 = "permit"

                    class DirectionOutActionEnum(Enum):
                        value_0 = "deny"
                        value_1 = "deny-in-out"
                        value_2 = "permit"

                    direction_in_action: DirectionInActionEnum | None = None
                    direction_out_action: DirectionOutActionEnum | None = None

                missing_policy: MissingPolicy | None = None

            class PeerGroupsItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class MissingPolicy(BaseModel):
                    model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                    class DirectionInActionEnum(Enum):
                        value_0 = "deny"
                        value_1 = "deny-in-out"
                        value_2 = "permit"

                    class DirectionOutActionEnum(Enum):
                        value_0 = "deny"
                        value_1 = "deny-in-out"
                        value_2 = "permit"

                    direction_in_action: DirectionInActionEnum | None = None
                    direction_out_action: DirectionOutActionEnum | None = None

                name: str = None
                """
                Peer-group name
                """
                activate: bool | None = None
                missing_policy: MissingPolicy | None = None

            class NeighborsItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class MissingPolicy(BaseModel):
                    model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                    class DirectionInActionEnum(Enum):
                        value_0 = "deny"
                        value_1 = "deny-in-out"
                        value_2 = "permit"

                    class DirectionOutActionEnum(Enum):
                        value_0 = "deny"
                        value_1 = "deny-in-out"
                        value_2 = "permit"

                    direction_in_action: DirectionInActionEnum | None = None
                    direction_out_action: DirectionOutActionEnum | None = None

                ip_address: str = None
                activate: bool | None = None
                missing_policy: MissingPolicy | None = None

            class PathSelection(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Roles(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    producer: bool | None = None
                    consumer: bool | None = None
                    propagator: bool | None = None

                roles: Roles | None = None

            bgp: Bgp | None = None
            peer_groups: list[PeerGroupsItem] | None = None
            neighbors: list[NeighborsItem] | None = None
            path_selection: PathSelection | None = None

        class AddressFamilyFlowSpecIpv4(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Bgp(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class MissingPolicy(BaseModel):
                    model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                    class DirectionInActionEnum(Enum):
                        value_0 = "deny"
                        value_1 = "deny-in-out"
                        value_2 = "permit"

                    class DirectionOutActionEnum(Enum):
                        value_0 = "deny"
                        value_1 = "deny-in-out"
                        value_2 = "permit"

                    direction_in_action: DirectionInActionEnum | None = None
                    direction_out_action: DirectionOutActionEnum | None = None

                missing_policy: MissingPolicy | None = None

            class NeighborsItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                ip_address: str = None
                activate: bool | None = None

            class PeerGroupsItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                name: str = None
                """
                Peer-group name
                """
                activate: bool | None = None

            bgp: Bgp | None = None
            neighbors: list[NeighborsItem] | None = None
            peer_groups: list[PeerGroupsItem] | None = None

        class AddressFamilyFlowSpecIpv6(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Bgp(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class MissingPolicy(BaseModel):
                    model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                    class DirectionInActionEnum(Enum):
                        value_0 = "deny"
                        value_1 = "deny-in-out"
                        value_2 = "permit"

                    class DirectionOutActionEnum(Enum):
                        value_0 = "deny"
                        value_1 = "deny-in-out"
                        value_2 = "permit"

                    direction_in_action: DirectionInActionEnum | None = None
                    direction_out_action: DirectionOutActionEnum | None = None

                missing_policy: MissingPolicy | None = None

            class NeighborsItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                ip_address: str = None
                activate: bool | None = None

            class PeerGroupsItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                name: str = None
                """
                Peer-group name
                """
                activate: bool | None = None

            bgp: Bgp | None = None
            neighbors: list[NeighborsItem] | None = None
            peer_groups: list[PeerGroupsItem] | None = None

        class AddressFamilyPathSelection(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Bgp(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class AdditionalPaths(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class Send(BaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        any: bool | None = None
                        backup: bool | None = None
                        ecmp: bool | None = None
                        ecmp_limit: int | None = Field(None, ge=2, le=64)
                        """
                        Amount of ECMP paths to send
                        """
                        limit: int | None = Field(None, ge=2, le=64)
                        """
                        Amount of paths to send
                        """

                    receive: bool | None = None
                    send: Send | None = None

                additional_paths: AdditionalPaths | None = None

            class NeighborsItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class AdditionalPaths(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class Send(BaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        any: bool | None = None
                        backup: bool | None = None
                        ecmp: bool | None = None
                        ecmp_limit: int | None = Field(None, ge=2, le=64)
                        """
                        Amount of ECMP paths to send
                        """
                        limit: int | None = Field(None, ge=2, le=64)
                        """
                        Amount of paths to send
                        """

                    install: bool | None = None
                    install_ecmp_primary: bool | None = None
                    receive: bool | None = None
                    send: Send | None = None

                ip_address: str = None
                activate: bool | None = None
                additional_paths: AdditionalPaths | None = None

            class PeerGroupsItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class AdditionalPaths(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class Send(BaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        any: bool | None = None
                        backup: bool | None = None
                        ecmp: bool | None = None
                        ecmp_limit: int | None = Field(None, ge=2, le=64)
                        """
                        Amount of ECMP paths to send
                        """
                        limit: int | None = Field(None, ge=2, le=64)
                        """
                        Amount of paths to send
                        """

                    install: bool | None = None
                    install_ecmp_primary: bool | None = None
                    receive: bool | None = None
                    send: Send | None = None

                name: str = None
                """
                Peer-group name
                """
                activate: bool | None = None
                additional_paths: AdditionalPaths | None = None

            bgp: Bgp | None = None
            neighbors: list[NeighborsItem] | None = None
            peer_groups: list[PeerGroupsItem] | None = None

        class AddressFamilyVpnIpv4(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class PeerGroupsItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                name: str = None
                """
                Peer-group name
                """
                activate: bool | None = None
                route_map_in: str | None = None
                """
                Inbound route-map name
                """
                route_map_out: str | None = None
                """
                Outbound route-map name
                """

            class Route(BaseModel):
                model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                class ImportMatchFailureActionEnum(Enum):
                    value_0 = "discard"

                import_match_failure_action: ImportMatchFailureActionEnum | None = None

            class NeighborsItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                ip_address: str = None
                activate: bool | None = None
                route_map_in: str | None = None
                """
                Inbound route-map name
                """
                route_map_out: str | None = None
                """
                Outbound route-map name
                """

            class NeighborDefaultEncapsulationMplsNextHopSelf(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                source_interface: str | None = None

            domain_identifier: str | None = None
            peer_groups: list[PeerGroupsItem] | None = None
            route: Route | None = None
            neighbors: list[NeighborsItem] | None = None
            neighbor_default_encapsulation_mpls_next_hop_self: NeighborDefaultEncapsulationMplsNextHopSelf | None = None

        class AddressFamilyVpnIpv6(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class PeerGroupsItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                name: str = None
                """
                Peer-group name
                """
                activate: bool | None = None
                route_map_in: str | None = None
                """
                Inbound route-map name
                """
                route_map_out: str | None = None
                """
                Outbound route-map name
                """

            class Route(BaseModel):
                model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                class ImportMatchFailureActionEnum(Enum):
                    value_0 = "discard"

                import_match_failure_action: ImportMatchFailureActionEnum | None = None

            class NeighborsItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                ip_address: str = None
                activate: bool | None = None
                route_map_in: str | None = None
                """
                Inbound route-map name
                """
                route_map_out: str | None = None
                """
                Outbound route-map name
                """

            class NeighborDefaultEncapsulationMplsNextHopSelf(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                source_interface: str | None = None

            domain_identifier: str | None = None
            peer_groups: list[PeerGroupsItem] | None = None
            route: Route | None = None
            neighbors: list[NeighborsItem] | None = None
            neighbor_default_encapsulation_mpls_next_hop_self: NeighborDefaultEncapsulationMplsNextHopSelf | None = None

        class VrfsItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class EvpnMulticastAddressFamily(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Ipv4(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    transit: bool | None = None
                    """
                    Enable EVPN multicast transit mode
                    """

                ipv4: Ipv4 | None = None

            class RouteTargets(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class ImportItem(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    address_family: str = None
                    route_targets: list[str] | None = None
                    route_map: str | None = None

                class ExportItem(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    address_family: str = None
                    route_targets: list[str] | None = None
                    route_map: str | None = None

                field_import: list[ImportItem] | None = Field(None, alias="import")
                export: list[ExportItem] | None = None

            class NetworksItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                prefix: str = None
                """
                IPv4 prefix "A.B.C.D/E" or IPv6 prefix "A:B:C:D:E:F:G:H/I"
                """
                route_map: str | None = None

            class Updates(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                wait_for_convergence: bool | None = None
                """
                Disables FIB updates and route advertisement when the BGP instance is initiated until the BGP convergence state is
                reached.
                """
                wait_install: bool | None = None
                """
                Do not advertise reachability to a prefix until that prefix has been installed in hardware.
                This will eliminate any
                temporary black holes due to a BGP speaker advertising reachability to a prefix that may not yet be installed into the
                forwarding plane.
                """

            class ListenRangesItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                prefix: str | None = None
                """
                IPv4 prefix "A.B.C.D/E" or IPv6 prefix "A:B:C:D:E:F:G:H/I"
                """
                peer_id_include_router_id: bool | None = None
                """
                Include router ID as part of peer filter
                """
                peer_group: str | None = None
                """
                Peer-group name
                """
                peer_filter: str | None = None
                """
                Peer-filter name
                note: `peer_filter`` or `remote_as` is required but mutually exclusive.
                If both are defined,
                peer_filter takes precedence
                """
                remote_as: Annotated[str, StrConvert(convert_types=(int))] | None = None
                """
                BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>"
                """

            class NeighborsItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class RemovePrivateAs(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    enabled: bool | None = None
                    all: bool | None = None
                    replace_as: bool | None = None

                class RemovePrivateAsIngress(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    enabled: bool | None = None
                    replace_as: bool | None = None

                class AsPath(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    remote_as_replace_out: bool | None = None
                    """
                    Replace AS number with local AS number
                    """
                    prepend_own_disabled: bool | None = None
                    """
                    Disable prepending own AS number to AS path
                    """

                class RibInPrePolicyRetain(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    enabled: bool | None = None
                    all: bool | None = None

                class AllowasIn(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    enabled: bool | None = None
                    times: int | None = Field(None, ge=1, le=10)
                    """
                    Number of local ASNs allowed in a BGP update
                    """

                class DefaultOriginate(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    enabled: bool | None = None
                    always: bool | None = None
                    route_map: str | None = None

                ip_address: str = None
                peer_group: str | None = None
                """
                Peer-group name
                """
                remote_as: Annotated[str, StrConvert(convert_types=(int))] | None = None
                """
                BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>"
                """
                password: str | None = None
                passive: bool | None = None
                remove_private_as: RemovePrivateAs | None = None
                """
                Remove private AS numbers in outbound AS path
                """
                remove_private_as_ingress: RemovePrivateAsIngress | None = None
                weight: int | None = Field(None, ge=0, le=65535)
                local_as: Annotated[str, StrConvert(convert_types=(int))] | None = None
                """
                BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>"
                """
                as_path: AsPath | None = None
                """
                BGP AS-PATH options
                """
                description: str | None = None
                route_reflector_client: bool | None = None
                ebgp_multihop: int | None = Field(None, ge=1, le=255)
                """
                Time-to-live in range of hops
                """
                next_hop_self: bool | None = None
                shutdown: bool | None = None
                bfd: bool | None = None
                timers: str | None = None
                """
                BGP Keepalive and Hold Timer values in seconds as string "<0-3600> <0-3600>"
                """
                rib_in_pre_policy_retain: RibInPrePolicyRetain | None = None
                send_community: str | None = None
                """
                'all' or a combination of 'standard', 'extended', 'large' and 'link-bandwidth (w/options)'
                """
                maximum_routes: int | None = None
                maximum_routes_warning_limit: Annotated[str, StrConvert(convert_types=(int))] | None = None
                """
                Maximum number of routes after which a warning is issued (0 means never warn) or
                Percentage of maximum number of routes
                at which to warn ("<1-100> percent")
                """
                maximum_routes_warning_only: bool | None = None
                allowas_in: AllowasIn | None = None
                default_originate: DefaultOriginate | None = None
                update_source: str | None = None
                route_map_in: str | None = None
                """
                Inbound route-map name
                """
                route_map_out: str | None = None
                """
                Outbound route-map name
                """
                prefix_list_in: str | None = None
                """
                Inbound prefix-list name
                """
                prefix_list_out: str | None = None
                """
                Outbound prefix-list name
                """

            class NeighborInterfacesItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                name: str = None
                """
                Interface name
                """
                remote_as: Annotated[str, StrConvert(convert_types=(int))] | None = None
                """
                BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>"
                """
                peer_group: str | None = None
                """
                Peer-group name
                """
                peer_filter: str | None = None
                """
                Peer-filter name
                """
                description: str | None = None

            class RedistributeRoutesItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                source_protocol: str = None
                route_map: str | None = None
                include_leaked: bool | None = None

            class AggregateAddressesItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                prefix: str = None
                """
                IPv4 prefix "A.B.C.D/E" or IPv6 prefix "A:B:C:D:E:F:G:H/I"
                """
                advertise_only: bool | None = None
                as_set: bool | None = None
                summary_only: bool | None = None
                attribute_map: str | None = None
                match_map: str | None = None

            class AddressFamilyIpv4(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Bgp(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class MissingPolicy(BaseModel):
                        model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                        class DirectionInActionEnum(Enum):
                            value_0 = "deny"
                            value_1 = "deny-in-out"
                            value_2 = "permit"

                        class DirectionOutActionEnum(Enum):
                            value_0 = "deny"
                            value_1 = "deny-in-out"
                            value_2 = "permit"

                        direction_in_action: DirectionInActionEnum | None = None
                        direction_out_action: DirectionOutActionEnum | None = None

                    class AdditionalPaths(BaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        class Send(BaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            any: bool | None = None
                            backup: bool | None = None
                            ecmp: bool | None = None
                            ecmp_limit: int | None = Field(None, ge=2, le=64)
                            """
                            Amount of ECMP paths to send
                            """
                            limit: int | None = Field(None, ge=2, le=64)
                            """
                            Amount of paths to send
                            """

                        install: bool | None = None
                        install_ecmp_primary: bool | None = None
                        receive: bool | None = None
                        send: Send | None = None

                    missing_policy: MissingPolicy | None = None
                    additional_paths: AdditionalPaths | None = None

                class NeighborsItem(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class NextHop(BaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        class AddressFamilyIpv6(BaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            enabled: bool = None
                            originate: bool | None = None

                        address_family_ipv6: AddressFamilyIpv6 | None = None

                    ip_address: str = None
                    activate: bool | None = None
                    route_map_in: str | None = None
                    """
                    Inbound route-map name
                    """
                    route_map_out: str | None = None
                    """
                    Outbound route-map name
                    """
                    next_hop: NextHop | None = None

                class NetworksItem(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    prefix: str = None
                    """
                    IPv4 prefix "A.B.C.D/E"
                    """
                    route_map: str | None = None

                bgp: Bgp | None = None
                neighbors: list[NeighborsItem] | None = None
                networks: list[NetworksItem] | None = None

            class AddressFamilyIpv6(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Bgp(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class MissingPolicy(BaseModel):
                        model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                        class DirectionInActionEnum(Enum):
                            value_0 = "deny"
                            value_1 = "deny-in-out"
                            value_2 = "permit"

                        class DirectionOutActionEnum(Enum):
                            value_0 = "deny"
                            value_1 = "deny-in-out"
                            value_2 = "permit"

                        direction_in_action: DirectionInActionEnum | None = None
                        direction_out_action: DirectionOutActionEnum | None = None

                    class AdditionalPaths(BaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        class Send(BaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            any: bool | None = None
                            backup: bool | None = None
                            ecmp: bool | None = None
                            ecmp_limit: int | None = Field(None, ge=2, le=64)
                            """
                            Amount of ECMP paths to send
                            """
                            limit: int | None = Field(None, ge=2, le=64)
                            """
                            Amount of paths to send
                            """

                        install: bool | None = None
                        install_ecmp_primary: bool | None = None
                        receive: bool | None = None
                        send: Send | None = None

                    missing_policy: MissingPolicy | None = None
                    additional_paths: AdditionalPaths | None = None

                class NeighborsItem(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    ip_address: str = None
                    activate: bool | None = None
                    route_map_in: str | None = None
                    """
                    Inbound route-map name
                    """
                    route_map_out: str | None = None
                    """
                    Outbound route-map name
                    """

                class NetworksItem(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    prefix: str = None
                    """
                    IPv6 prefix "A:B:C:D:E:F:G:H/I"
                    """
                    route_map: str | None = None

                bgp: Bgp | None = None
                neighbors: list[NeighborsItem] | None = None
                networks: list[NetworksItem] | None = None

            class AddressFamilyIpv4Multicast(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Bgp(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class MissingPolicy(BaseModel):
                        model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                        class DirectionInActionEnum(Enum):
                            value_0 = "deny"
                            value_1 = "deny-in-out"
                            value_2 = "permit"

                        class DirectionOutActionEnum(Enum):
                            value_0 = "deny"
                            value_1 = "deny-in-out"
                            value_2 = "permit"

                        direction_in_action: DirectionInActionEnum | None = None
                        direction_out_action: DirectionOutActionEnum | None = None

                    class AdditionalPaths(BaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        receive: bool | None = None

                    missing_policy: MissingPolicy | None = None
                    additional_paths: AdditionalPaths | None = None

                class NeighborsItem(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    ip_address: str = None
                    activate: bool | None = None
                    route_map_in: str | None = None
                    """
                    Inbound route-map name
                    """
                    route_map_out: str | None = None
                    """
                    Outbound route-map name
                    """

                class NetworksItem(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    prefix: str = None
                    """
                    IPv6 prefix "A.B.C.D/E"
                    """
                    route_map: str | None = None

                bgp: Bgp | None = None
                neighbors: list[NeighborsItem] | None = None
                networks: list[NetworksItem] | None = None

            class AddressFamilyIpv6Multicast(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Bgp(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class MissingPolicy(BaseModel):
                        model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                        class DirectionInActionEnum(Enum):
                            value_0 = "deny"
                            value_1 = "deny-in-out"
                            value_2 = "permit"

                        class DirectionOutActionEnum(Enum):
                            value_0 = "deny"
                            value_1 = "deny-in-out"
                            value_2 = "permit"

                        direction_in_action: DirectionInActionEnum | None = None
                        direction_out_action: DirectionOutActionEnum | None = None

                    class AdditionalPaths(BaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        receive: bool | None = None

                    missing_policy: MissingPolicy | None = None
                    additional_paths: AdditionalPaths | None = None

                class NeighborsItem(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    ip_address: str = None
                    activate: bool | None = None
                    route_map_in: str | None = None
                    """
                    Inbound route-map name
                    """
                    route_map_out: str | None = None
                    """
                    Outbound route-map name
                    """

                class NetworksItem(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    prefix: str = None
                    """
                    IPv6 prefix "A:B:C:D:E:F:G:H/I"
                    """
                    route_map: str | None = None

                bgp: Bgp | None = None
                neighbors: list[NeighborsItem] | None = None
                networks: list[NetworksItem] | None = None

            class AddressFamilyFlowSpecIpv4(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Bgp(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class MissingPolicy(BaseModel):
                        model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                        class DirectionInActionEnum(Enum):
                            value_0 = "deny"
                            value_1 = "deny-in-out"
                            value_2 = "permit"

                        class DirectionOutActionEnum(Enum):
                            value_0 = "deny"
                            value_1 = "deny-in-out"
                            value_2 = "permit"

                        direction_in_action: DirectionInActionEnum | None = None
                        direction_out_action: DirectionOutActionEnum | None = None

                    missing_policy: MissingPolicy | None = None

                class NeighborsItem(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    ip_address: str = None
                    activate: bool | None = None

                bgp: Bgp | None = None
                neighbors: list[NeighborsItem] | None = None

            class AddressFamilyFlowSpecIpv6(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Bgp(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class MissingPolicy(BaseModel):
                        model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                        class DirectionInActionEnum(Enum):
                            value_0 = "deny"
                            value_1 = "deny-in-out"
                            value_2 = "permit"

                        class DirectionOutActionEnum(Enum):
                            value_0 = "deny"
                            value_1 = "deny-in-out"
                            value_2 = "permit"

                        direction_in_action: DirectionInActionEnum | None = None
                        direction_out_action: DirectionOutActionEnum | None = None

                    missing_policy: MissingPolicy | None = None

                class NeighborsItem(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    ip_address: str = None
                    activate: bool | None = None

                bgp: Bgp | None = None
                neighbors: list[NeighborsItem] | None = None

            class AddressFamiliesItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Bgp(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class MissingPolicy(BaseModel):
                        model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                        class DirectionInActionEnum(Enum):
                            value_0 = "deny"
                            value_1 = "deny-in-out"
                            value_2 = "permit"

                        class DirectionOutActionEnum(Enum):
                            value_0 = "deny"
                            value_1 = "deny-in-out"
                            value_2 = "permit"

                        direction_in_action: DirectionInActionEnum | None = None
                        direction_out_action: DirectionOutActionEnum | None = None

                    missing_policy: MissingPolicy | None = None
                    additional_paths: list[str] | None = None

                class NeighborsItem(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    ip_address: str = None
                    activate: bool | None = None
                    route_map_in: str | None = None
                    """
                    Inbound route-map name
                    """
                    route_map_out: str | None = None
                    """
                    Outbound route-map name
                    """

                class PeerGroupsItem(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class NextHop(BaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        address_family_ipv6_originate: bool | None = None

                    name: str = None
                    """
                    Peer-group name
                    """
                    activate: bool | None = None
                    next_hop: NextHop | None = None

                class NetworksItem(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    prefix: str = None
                    """
                    IPv4 prefix "A.B.C.D/E" or IPv6 prefix "A:B:C:D:E:F:G:H/I"
                    """
                    route_map: str | None = None

                address_family: str = None
                bgp: Bgp | None = None
                neighbors: list[NeighborsItem] | None = None
                peer_groups: list[PeerGroupsItem] | None = None
                networks: list[NetworksItem] | None = None

            name: Annotated[str, StrConvert(convert_types=(int))] = None
            """
            VRF name
            """
            rd: str | None = None
            """
            Route distinguisher
            """
            evpn_multicast: bool | None = None
            evpn_multicast_address_family: EvpnMulticastAddressFamily | None = None
            """
            Enable per-AF EVPN multicast settings
            """
            route_targets: RouteTargets | None = None
            router_id: str | None = None
            """
            in IP address format A.B.C.D
            """
            timers: str | None = None
            """
            BGP Keepalive and Hold Timer values in seconds as string "<0-3600> <0-3600>"
            """
            networks: list[NetworksItem] | None = None
            updates: Updates | None = None
            listen_ranges: list[ListenRangesItem] | None = None
            """
            Improved "listen_ranges" data model to support multiple listen ranges and additional filter capabilities
            """
            neighbors: list[NeighborsItem] | None = None
            neighbor_interfaces: list[NeighborInterfacesItem] | None = None
            redistribute_routes: list[RedistributeRoutesItem] | None = None
            aggregate_addresses: list[AggregateAddressesItem] | None = None
            address_family_ipv4: AddressFamilyIpv4 | None = None
            address_family_ipv6: AddressFamilyIpv6 | None = None
            address_family_ipv4_multicast: AddressFamilyIpv4Multicast | None = None
            address_family_ipv6_multicast: AddressFamilyIpv6Multicast | None = None
            address_family_flow_spec_ipv4: AddressFamilyFlowSpecIpv4 | None = None
            address_family_flow_spec_ipv6: AddressFamilyFlowSpecIpv6 | None = None
            address_families: list[AddressFamiliesItem] | None = None
            eos_cli: str | None = None
            """
            Multiline EOS CLI rendered directly on the Router BGP, VRF definition in the final EOS configuration
            """

        class SessionTrackersItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str = None
            """
            Name of session tracker
            """
            recovery_delay: int | None = Field(None, ge=1, le=3600)
            """
            Recovery delay in seconds
            """

        field_as: Annotated[str, StrConvert(convert_types=(int))] | None = Field(None, alias="as")
        """
        BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>"
        """
        router_id: str | None = None
        """
        In IP address format A.B.C.D
        """
        distance: Distance | None = None
        graceful_restart: GracefulRestart | None = None
        graceful_restart_helper: GracefulRestartHelper | None = None
        maximum_paths: MaximumPaths | None = None
        updates: Updates | None = None
        bgp_cluster_id: str | None = None
        """
        IP Address A.B.C.D
        """
        bgp_defaults: list[str] | None = None
        """
        BGP command as string
        """
        bgp: Bgp | None = None
        listen_ranges: list[ListenRangesItem] | None = None
        """
        Improved "listen_ranges" data model to support multiple listen ranges and additional filter capabilities
        """
        peer_groups: list[PeerGroupsItem] | None = None
        neighbors: list[NeighborsItem] | None = None
        neighbor_interfaces: list[NeighborInterfacesItem] | None = None
        aggregate_addresses: list[AggregateAddressesItem] | None = None
        redistribute_routes: list[RedistributeRoutesItem] | None = None
        vlan_aware_bundles: list[VlanAwareBundlesItem] | None = None
        vlans: list[VlansItem] | None = None
        vpws: list[VpwsItem] | None = None
        address_family_evpn: AddressFamilyEvpn | None = None
        address_family_rtc: AddressFamilyRtc | None = None
        address_family_ipv4: AddressFamilyIpv4 | None = None
        address_family_ipv4_multicast: AddressFamilyIpv4Multicast | None = None
        address_family_ipv4_sr_te: AddressFamilyIpv4SrTe | None = None
        address_family_ipv6: AddressFamilyIpv6 | None = None
        address_family_ipv6_multicast: AddressFamilyIpv6Multicast | None = None
        address_family_ipv6_sr_te: AddressFamilyIpv6SrTe | None = None
        address_family_link_state: AddressFamilyLinkState | None = None
        address_family_flow_spec_ipv4: AddressFamilyFlowSpecIpv4 | None = None
        address_family_flow_spec_ipv6: AddressFamilyFlowSpecIpv6 | None = None
        address_family_path_selection: AddressFamilyPathSelection | None = None
        address_family_vpn_ipv4: AddressFamilyVpnIpv4 | None = None
        address_family_vpn_ipv6: AddressFamilyVpnIpv6 | None = None
        vrfs: list[VrfsItem] | None = None
        session_trackers: list[SessionTrackersItem] | None = None

    class RouterGeneral(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class RouterId(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            ipv4: str | None = None
            """
            IPv4 Address
            """
            ipv6: str | None = None
            """
            IPv6 Address
            """

        class VrfsItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class LeakRoutesItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                source_vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
                subscribe_policy: str | None = None
                """
                Route-Map Policy
                """

            class Routes(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class DynamicPrefixListsItem(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    name: str | None = None
                    """
                    Dynamic Prefix List Name
                    """

                dynamic_prefix_lists: list[DynamicPrefixListsItem] | None = None

            name: Annotated[str, StrConvert(convert_types=(int))] = None
            """
            Destination-VRF
            """
            leak_routes: list[LeakRoutesItem] | None = None
            routes: Routes | None = None

        router_id: RouterId | None = None
        nexthop_fast_failover: bool | None = False
        vrfs: list[VrfsItem] | None = None

    class RouterIgmp(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        ssm_aware: bool | None = None

    class RouterIsis(BaseModel):
        model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

        class IsTypeEnum(Enum):
            value_0 = "level-1"
            value_1 = "level-1-2"
            value_2 = "level-2"

        class Timers(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class LocalConvergence(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                protected_prefixes: bool | None = None
                delay: int | None = 10000
                """
                Delay in milliseconds.
                """

            local_convergence: LocalConvergence | None = None

        class Advertise(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            passive_only: bool | None = None

        class RedistributeRoutesItem(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class SourceProtocolEnum(Enum):
                value_0 = "bgp"
                value_1 = "connected"
                value_2 = "isis"
                value_3 = "ospf"
                value_4 = "ospfv3"
                value_5 = "static"

            class OspfRouteTypeEnum(Enum):
                value_0 = "external"
                value_1 = "internal"
                value_2 = "nssa-external"

            source_protocol: SourceProtocolEnum = None
            route_map: str | None = None
            """
            Route-map name
            """
            include_leaked: bool | None = None
            ospf_route_type: OspfRouteTypeEnum | None = None
            """
            ospf_route_type is required with source_protocols 'ospf' and 'ospfv3'
            """

        class AddressFamilyIpv4(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class FastRerouteTiLfa(BaseModel):
                model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                class ModeEnum(Enum):
                    value_0 = "link-protection"
                    value_1 = "node-protection"

                class LevelEnum(Enum):
                    value_0 = "level-1"
                    value_1 = "level-2"

                class Srlg(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    enable: bool | None = None
                    strict: bool | None = None

                mode: ModeEnum | None = None
                level: LevelEnum | None = None
                srlg: Srlg | None = None
                """
                Shared Risk Link Group
                """

            class TunnelSourceLabeledUnicast(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                enabled: bool | None = None
                rcf: str | None = None
                """
                Route Control Function
                """

            enabled: bool | None = None
            maximum_paths: int | None = Field(None, ge=1, le=128)
            fast_reroute_ti_lfa: FastRerouteTiLfa | None = None
            tunnel_source_labeled_unicast: TunnelSourceLabeledUnicast | None = None

        class AddressFamilyIpv6(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class FastRerouteTiLfa(BaseModel):
                model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                class ModeEnum(Enum):
                    value_0 = "link-protection"
                    value_1 = "node-protection"

                class LevelEnum(Enum):
                    value_0 = "level-1"
                    value_1 = "level-2"

                class Srlg(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    enable: bool | None = None
                    strict: bool | None = None

                mode: ModeEnum | None = None
                level: LevelEnum | None = None
                """
                Optional, default is to protect all levels
                """
                srlg: Srlg | None = None
                """
                Shared Risk Link Group
                """

            enabled: bool | None = None
            maximum_paths: int | None = Field(None, ge=1, le=128)
            fast_reroute_ti_lfa: FastRerouteTiLfa | None = None

        class SegmentRoutingMpls(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class PrefixSegmentsItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                prefix: str | None = None
                index: int | None = None

            enabled: bool | None = None
            router_id: str | None = None
            prefix_segments: list[PrefixSegmentsItem] | None = None

        instance: str = None
        """
        ISIS Instance Name
        """
        net: str | None = None
        """
        CLNS Address like "49.0001.0001.0000.0001.00"
        """
        router_id: str | None = None
        """
        IPv4 Address
        """
        is_type: IsTypeEnum | None = Field(None, title="IS Type")
        log_adjacency_changes: bool | None = None
        mpls_ldp_sync_default: bool | None = None
        timers: Timers | None = None
        advertise: Advertise | None = None
        address_family: list[str] | None = None
        isis_af_defaults: list[str] | None = None
        redistribute_routes: list[RedistributeRoutesItem] | None = None
        address_family_ipv4: AddressFamilyIpv4 | None = None
        address_family_ipv6: AddressFamilyIpv6 | None = None
        segment_routing_mpls: SegmentRoutingMpls | None = None

    class RouterL2Vpn(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class ArpProxy(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            prefix_list: str | None = None
            """
            Prefix-list name. ARP Proxying is disabled for IPv4 addresses defined in the prefix-list.
            """

        class NdProxy(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            prefix_list: str | None = None
            """
            Prefix-list name. ND Proxying is disabled for IPv6 addresses defined in the prefix-list.
            """

        arp_learning_bridged: bool | None = None
        arp_proxy: ArpProxy | None = None
        arp_selective_install: bool | None = None
        nd_learning_bridged: bool | None = None
        nd_proxy: NdProxy | None = None
        nd_rs_flooding_disabled: bool | None = None
        virtual_router_nd_ra_flooding_disabled: bool | None = None

    class RouterMsdp(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class GroupLimitsItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            source_prefix: str = None
            """
            Source address prefix
            """
            limit: int = Field(None, ge=0, le=40000)
            """
            Limit for SAs matching the source address prefix
            """

        class PeersItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class DefaultPeer(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                enabled: bool | None = None
                prefix_list: str | None = None
                """
                Prefix list to filter source of SA messages
                """

            class MeshGroupsItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                name: str = None
                """
                Mesh group name
                """

            class Keepalive(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                keepalive_timer: int = Field(None, ge=1, le=65535)
                hold_timer: int = Field(None, ge=1, le=65535)
                """
                Must be greater than keepalive timer
                """

            class SaFilter(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                in_list: str | None = None
                """
                ACL to filter inbound SA messages
                """
                out_list: str | None = None
                """
                ACL to filter outbound SA messages
                """

            ipv4_address: str = None
            """
            Peer IP Address
            """
            default_peer: DefaultPeer | None = None
            local_interface: str | None = None
            description: str | None = None
            disabled: bool | None = None
            """
            Disable the MSDP peer
            """
            sa_limit: int | None = Field(None, ge=0, le=40000)
            """
            Maximum number of SA messages allowed in cache
            """
            mesh_groups: list[MeshGroupsItem] | None = None
            keepalive: Keepalive | None = None
            sa_filter: SaFilter | None = None

        class VrfsItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class GroupLimitsItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                source_prefix: str = None
                """
                Source address prefix
                """
                limit: int = Field(None, ge=0, le=40000)
                """
                Limit for SAs matching the source address prefix
                """

            class PeersItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class DefaultPeer(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    enabled: bool | None = None
                    prefix_list: str | None = None
                    """
                    Prefix list to filter source of SA messages
                    """

                class MeshGroupsItem(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    name: str = None
                    """
                    Mesh group name
                    """

                class Keepalive(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    keepalive_timer: int = Field(None, ge=1, le=65535)
                    hold_timer: int = Field(None, ge=1, le=65535)
                    """
                    Must be greater than keepalive timer
                    """

                class SaFilter(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    in_list: str | None = None
                    """
                    ACL to filter inbound SA messages
                    """
                    out_list: str | None = None
                    """
                    ACL to filter outbound SA messages
                    """

                ipv4_address: str = None
                """
                Peer IP Address
                """
                default_peer: DefaultPeer | None = None
                local_interface: str | None = None
                description: str | None = None
                disabled: bool | None = None
                """
                Disable the MSDP peer
                """
                sa_limit: int | None = Field(None, ge=0, le=40000)
                """
                Maximum number of SA messages allowed in cache
                """
                mesh_groups: list[MeshGroupsItem] | None = None
                keepalive: Keepalive | None = None
                sa_filter: SaFilter | None = None

            name: Annotated[str, StrConvert(convert_types=(int))] = None
            """
            VRF name
            """
            originator_id_local_interface: str | None = None
            """
            Interface to use for originator ID
            """
            rejected_limit: int | None = Field(None, ge=0, le=40000)
            """
            Maximum number of rejected SA messages allowed in cache
            """
            forward_register_packets: bool | None = None
            connection_retry_interval: int | None = Field(None, ge=1, le=65535)
            group_limits: list[GroupLimitsItem] | None = None
            peers: list[PeersItem] | None = None

        originator_id_local_interface: str | None = None
        """
        Interface to use for originator ID
        """
        rejected_limit: int | None = Field(None, ge=0, le=40000)
        """
        Maximum number of rejected SA messages allowed in cache
        """
        forward_register_packets: bool | None = None
        connection_retry_interval: int | None = Field(None, ge=1, le=65535)
        group_limits: list[GroupLimitsItem] | None = None
        peers: list[PeersItem] | None = None
        vrfs: list[VrfsItem] | None = None

    class RouterMulticast(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Ipv4(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class Counters(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                rate_period_decay: int | None = Field(None, ge=0, le=600)
                """
                Rate in seconds
                """

            class MultipathEnum(Enum):
                value_0 = "none"
                value_1 = "deterministic"
                value_2 = "deterministic color"
                value_3 = "deterministic router-id"

            class SoftwareForwardingEnum(Enum):
                value_0 = "kernel"
                value_1 = "sfe"

            class Rpf(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class RoutesItem(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class DestinationsItem(BaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        nexthop: str = None
                        """
                        Next-hop IP address or interface name
                        """
                        distance: int | None = Field(None, ge=1, le=255)
                        """
                        Administrative distance for this route
                        """

                    source_prefix: str = None
                    """
                    Source address A.B.C.D or Source prefix A.B.C.D/E
                    """
                    destinations: list[DestinationsItem] = None

                routes: list[RoutesItem] | None = None

            counters: Counters | None = None
            routing: bool | None = None
            multipath: MultipathEnum | None = None
            software_forwarding: SoftwareForwardingEnum | None = None
            rpf: Rpf | None = None

        class VrfsItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Ipv4(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                routing: bool | None = None

            name: Annotated[str, StrConvert(convert_types=(int))] = None
            ipv4: Ipv4 | None = None

        ipv4: Ipv4 | None = None
        vrfs: list[VrfsItem] | None = None

    class RouterOspf(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class ProcessIdsItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Distance(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                external: int | None = Field(None, ge=1, le=255)
                inter_area: int | None = Field(None, ge=1, le=255)
                intra_area: int | None = Field(None, ge=1, le=255)

            class NetworkPrefixesItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                ipv4_prefix: str = None
                area: str | None = None

            class DistributeListIn(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                route_map: str | None = None

            class Timers(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Lsa(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class TxDelay(BaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        initial: int | None = Field(None, ge=0, le=600000)
                        """
                        Delay to generate first occurrence of LSA in msecs
                        """
                        min: int | None = Field(None, ge=1, le=600000)
                        """
                        Min delay between originating the same LSA in msecs
                        """
                        max: int | None = Field(None, ge=1, le=600000)
                        """
                        1-600000 Maximum delay between originating the same LSA in msec
                        """

                    rx_min_interval: int | None = Field(None, ge=0, le=600000)
                    """
                    Min interval in msecs between accepting the same LSA
                    """
                    tx_delay: TxDelay | None = None

                class SpfDelay(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    initial: int | None = Field(None, ge=0, le=600000)
                    """
                    Initial SPF schedule delay in msecs
                    """
                    min: int | None = Field(None, ge=0, le=65535000)
                    """
                    Min Hold time between two SPFs in msecs
                    """
                    max: int | None = Field(None, ge=0, le=65535000)
                    """
                    Max wait time between two SPFs in msecs
                    """

                lsa: Lsa | None = None
                spf_delay: SpfDelay | None = None

            class DefaultInformationOriginate(BaseModel):
                model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                class MetricTypeEnum(Enum):
                    value_0 = 1
                    value_1 = 2

                always: bool | None = None
                metric: int | None = Field(None, ge=1, le=65535)
                """
                Metric for default route
                """
                metric_type: MetricTypeEnum | None = None
                """
                OSPF metric type for default route
                """

            class SummaryAddressesItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                prefix: str = None
                """
                Summary Prefix Address
                """
                tag: int | None = None
                attribute_map: str | None = None
                not_advertise: bool | None = None

            class Redistribute(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Static(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    route_map: str | None = None
                    """
                    Route Map Name
                    """
                    include_leaked: bool | None = None

                class Connected(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    route_map: str | None = None
                    """
                    Route Map Name
                    """
                    include_leaked: bool | None = None

                class Bgp(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    route_map: str | None = None
                    """
                    Route Map Name
                    """
                    include_leaked: bool | None = None

                static: Static | None = None
                connected: Connected | None = None
                bgp: Bgp | None = None

            class AreasItem(BaseModel):
                model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                class Filter(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    networks: list[str] | None = None
                    prefix_list: str | None = None
                    """
                    Prefix-List Name
                    """

                class TypeEnum(Enum):
                    value_0 = "normal"
                    value_1 = "stub"
                    value_2 = "nssa"

                class DefaultInformationOriginate(BaseModel):
                    model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                    class MetricTypeEnum(Enum):
                        value_0 = 1
                        value_1 = 2

                    metric: int | None = Field(None, ge=1, le=65535)
                    """
                    Metric for default route
                    """
                    metric_type: MetricTypeEnum | None = None
                    """
                    OSPF metric type for default route
                    """

                id: Annotated[str, StrConvert(convert_types=(int))] = None
                filter: Filter | None = None
                type: TypeEnum | None = "normal"
                no_summary: bool | None = None
                nssa_only: bool | None = None
                default_information_originate: DefaultInformationOriginate | None = None

            class MaxMetric(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class RouterLsa(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class ExternalLsa(BaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        override_metric: int | None = Field(None, ge=1, le=16777215)

                    class SummaryLsa(BaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        override_metric: int | None = Field(None, ge=1, le=16777215)

                    external_lsa: ExternalLsa | None = None
                    include_stub: bool | None = None
                    on_startup: Annotated[str, StrConvert(convert_types=(int))] | None = None
                    """
                    "wait-for-bgp" or Integer 5-86400
                    Example: "wait-for-bgp" Or "222"
                    """
                    summary_lsa: SummaryLsa | None = None

                router_lsa: RouterLsa | None = None

            id: int = None
            """
            OSPF Process ID
            """
            vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
            """
            VRF Name for OSPF Process
            """
            passive_interface_default: bool | None = None
            router_id: str | None = None
            """
            IPv4 Address
            """
            distance: Distance | None = None
            log_adjacency_changes_detail: bool | None = None
            network_prefixes: list[NetworkPrefixesItem] | None = None
            bfd_enable: bool | None = None
            bfd_adjacency_state_any: bool | None = None
            no_passive_interfaces: list[str] | None = None
            distribute_list_in: DistributeListIn | None = None
            max_lsa: int | None = None
            timers: Timers | None = None
            default_information_originate: DefaultInformationOriginate | None = None
            summary_addresses: list[SummaryAddressesItem] | None = None
            redistribute: Redistribute | None = None
            auto_cost_reference_bandwidth: int | None = None
            """
            Bandwidth in mbps
            """
            areas: list[AreasItem] | None = None
            maximum_paths: int | None = Field(None, ge=1, le=128)
            max_metric: MaxMetric | None = None
            mpls_ldp_sync_default: bool | None = None
            eos_cli: str | None = None
            """
            Multiline EOS CLI rendered directly on the Router OSPF process ID in the final EOS configuration
            """

        process_ids: list[ProcessIdsItem] | None = None

    class RouterPathSelection(BaseModel):
        model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

        class PeerDynamicSourceEnum(Enum):
            value_0 = "stun"

        class PathGroupsItem(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class FlowAssignmentEnum(Enum):
                value_0 = "lan"

            class LocalInterfacesItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Stun(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    server_profiles: list[str] = Field(None, min_length=1, max_length=2)
                    """
                    STUN server-profile names.
                    """

                name: str = Field(None, pattern=r"^Ethernet\d+(/\d+)*(\.\d+)?$")
                """
                Local interface name.
                """
                public_address: str | None = None
                """
                Public IP assigned by NAT.
                """
                stun: Stun | None = None

            class LocalIpsItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Stun(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    server_profiles: list[str] = Field(None, min_length=1, max_length=2)
                    """
                    STUN server-profile names.
                    """

                ip_address: str = None
                public_address: str | None = None
                """
                Public IP assigned by NAT.
                """
                stun: Stun | None = None

            class DynamicPeers(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                enabled: bool | None = None
                """
                Enable `peer dynamic`.
                """
                ip_local: bool | None = None
                """
                Prefer local IP address.
                """
                ipsec: bool | None = None
                """
                IPsec configuration for dynamic peers.
                """

            class StaticPeersItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                router_ip: str = None
                """
                Peer router IP.
                """
                name: str | None = None
                """
                Name of the site.
                """
                ipv4_addresses: list[str] | None = None
                """
                Static IPv4 addresses.
                """

            name: str = None
            """
            Path group name.
            """
            id: int | None = Field(None, ge=1, le=65535)
            """
            Path group ID.
            """
            ipsec_profile: str | None = None
            """
            IPSec profile for the path group.
            """
            flow_assignment: FlowAssignmentEnum | None = None
            """
            Flow assignement `lan` can not be configured in a path group with dynamic peers.
            """
            local_interfaces: list[LocalInterfacesItem] | None = None
            local_ips: list[LocalIpsItem] | None = None
            dynamic_peers: DynamicPeers | None = None
            """
            Flow assignement `lan` can not be configured in a path group with dynamic peers.
            """
            static_peers: list[StaticPeersItem] | None = None

        class LoadBalancePoliciesItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str = None
            """
            Load-balance policy name.
            """
            path_groups: list[str] | None = None
            """
            List of path-groups to use for this load balance policy.
            """

        class PoliciesItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class DefaultMatch(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                load_balance: str | None = None
                """
                Name of the load-balance policy.
                """

            class RulesItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                id: int = Field(None, ge=1, le=255)
                """
                Rule ID.
                """
                application_profile: str = None
                load_balance: str | None = None
                """
                Name of the load-balance policy.
                """

            name: str = None
            """
            DPS policy name.
            """
            default_match: DefaultMatch | None = None
            rules: list[RulesItem] | None = None

        class VrfsItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str = None
            """
            VRF name.
            """
            path_selection_policy: str | None = None
            """
            DPS policy name to use for this VRF.
            """

        peer_dynamic_source: PeerDynamicSourceEnum | None = None
        """
        Source of dynamic peer discovery.
        """
        path_groups: list[PathGroupsItem] | None = None
        load_balance_policies: list[LoadBalancePoliciesItem] | None = None
        policies: list[PoliciesItem] | None = None
        vrfs: list[VrfsItem] | None = None

    class RouterPimSparseMode(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Ipv4(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class RpAddressesItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                address: str = None
                """
                RP Address
                """
                groups: list[str] | None = None
                access_lists: list[str] | None = None
                priority: int | None = Field(None, ge=0, le=255)
                hashmask: int | None = Field(None, ge=0, le=32)
                override: bool | None = None

            class AnycastRpsItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class OtherAnycastRpAddressesItem(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    address: str = None
                    """
                    Other Anycast RP Address
                    """
                    register_count: int | None = None

                address: str = None
                """
                Anycast RP Address
                """
                other_anycast_rp_addresses: list[OtherAnycastRpAddressesItem] | None = None

            bfd: bool | None = None
            """
            Enable/Disable BFD
            """
            ssm_range: str | None = None
            """
            IPv4 Prefix associated with SSM
            """
            rp_addresses: list[RpAddressesItem] | None = None
            anycast_rps: list[AnycastRpsItem] | None = None

        class VrfsItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Ipv4(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class RpAddressesItem(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    address: str = None
                    """
                    RP Address
                    """
                    groups: list[str] | None = None
                    access_lists: list[str] | None = None
                    priority: int | None = Field(None, ge=0, le=255)
                    hashmask: int | None = Field(None, ge=0, le=32)
                    override: bool | None = None

                bfd: bool | None = None
                """
                Enable/Disable BFD
                """
                rp_addresses: list[RpAddressesItem] | None = None

            name: Annotated[str, StrConvert(convert_types=(int))] = None
            """
            VRF Name
            """
            ipv4: Ipv4 | None = None

        ipv4: Ipv4 | None = None
        vrfs: list[VrfsItem] | None = None

    class RouterServiceInsertion(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        enabled: bool | None = None

    class RouterTrafficEngineering(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class RouterId(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            ipv4: str | None = None
            ipv6: str | None = None

        class SegmentRouting(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class PolicyEndpointsItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class ColorsItem(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class PathGroupItem(BaseModel):
                        model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                        class ExplicitNullEnum(Enum):
                            value_0 = "ipv4"
                            value_1 = "ipv6"
                            value_2 = "ipv4 ipv6"
                            value_3 = "none"

                        class SegmentListItem(BaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            label_stack: Annotated[str, StrConvert(convert_types=(int))] | None = None
                            """
                            Label Stack as string.
                            Example: "100 2000 30"
                            """
                            weight: int | None = None
                            index: int | None = None

                        preference: int | None = None
                        explicit_null: ExplicitNullEnum | None = None
                        segment_list: list[SegmentListItem] | None = None

                    value: int = None
                    binding_sid: int | None = None
                    description: str | None = None
                    name: str | None = None
                    sbfd_remote_discriminator: Annotated[str, StrConvert(convert_types=(int))] | None = None
                    """
                    IPv4 address or 32 bit integer
                    """
                    path_group: list[PathGroupItem] | None = None

                address: str | None = None
                """
                IPv4 or IPv6 address
                """
                colors: list[ColorsItem] | None = None

            colored_tunnel_rib: bool | None = None
            policy_endpoints: list[PolicyEndpointsItem] | None = None

        enabled: bool | None = None
        router_id: RouterId | None = None
        segment_routing: SegmentRouting | None = None

    class ServiceRoutingConfigurationBgp(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        no_equals_default: bool | None = None

    class ServiceRoutingProtocolsModelEnum(Enum):
        value_0 = "multi-agent"
        value_1 = "ribd"

    class ServiceUnsupportedTransceiver(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        license_name: str | None = None
        license_key: str | None = None

    class Sflow(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class VrfsItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class DestinationsItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                destination: str = None
                """
                Sflow Destination IP Address
                """
                port: int | None = None
                """
                Port Number
                """

            name: Annotated[str, StrConvert(convert_types=(int))] = None
            destinations: list[DestinationsItem] | None = None
            source: str | None = None
            """
            Source IP Address.
            "source" and "source_interface" are mutually exclusive. If both are defined, "source_interface" takes
            precedence.
            """
            source_interface: str | None = None
            """
            Source Interface
            """

        class DestinationsItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            destination: str = None
            """
            Sflow Destination IP Address
            """
            port: int | None = None
            """
            Port Number
            """

        class ExtensionsItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str = None
            """
            Extension Name
            """
            enabled: bool = None
            """
            Enable or Disable Extension
            """

        class Interface(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Disable(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                default: bool | None = None

            class Egress(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                enable_default: bool | None = None
                """
                Enable egress sFlow by default.
                """
                unmodified: bool | None = None
                """
                Enable egress sFlow unmodified.
                Platform dependent feature.
                """

            disable: Disable | None = None
            egress: Egress | None = None

        class HardwareAcceleration(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class ModulesItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                name: str = None
                enabled: bool | None = True

            enabled: bool | None = None
            sample: int | None = None
            modules: list[ModulesItem] | None = None

        sample: int | None = None
        dangerous: bool | None = None
        polling_interval: int | None = None
        """
        Polling interval in seconds
        """
        vrfs: list[VrfsItem] | None = None
        destinations: list[DestinationsItem] | None = None
        source: str | None = None
        """
        Source IP Address.
        "source" and "source_interface" are mutually exclusive. If both are defined, "source_interface" takes
        precedence.
        """
        source_interface: str | None = None
        """
        Source Interface
        """
        extensions: list[ExtensionsItem] | None = None
        interface: Interface | None = None
        run: bool | None = None
        hardware_acceleration: HardwareAcceleration | None = None

    class SnmpServer(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class EngineIds(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class RemotesItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                id: Annotated[str, StrConvert(convert_types=(int))] | None = None
                """
                Remote engine ID in hexadecimal
                """
                address: str | None = None
                """
                Hostname or IP of remote engine
                """
                udp_port: int | None = None

            local: Annotated[str, StrConvert(convert_types=(int))] | None = None
            """
            Engine ID in hexadecimal
            """
            remotes: list[RemotesItem] | None = None

        class CommunitiesItem(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class AccessEnum(Enum):
                value_0 = "ro"
                value_1 = "rw"

            class AccessListIpv4(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                name: str | None = None
                """
                IPv4 access list name
                """

            class AccessListIpv6(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                name: str | None = None
                """
                IPv6 access list name
                """

            name: str = None
            """
            Community name
            """
            access: AccessEnum | None = None
            access_list_ipv4: AccessListIpv4 | None = None
            access_list_ipv6: AccessListIpv6 | None = None
            view: str | None = None

        class Ipv4AclsItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str | None = None
            """
            IPv4 access list name
            """
            vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None

        class Ipv6AclsItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str | None = None
            """
            IPv6 access list name
            """
            vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None

        class LocalInterfacesItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str = None
            """
            Interface name
            """
            vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None

        class ViewsItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str | None = None
            """
            SNMP view name
            """
            mib_family_name: str | None = None
            included: bool | None = None
            field_MIB_family_name: str | None = Field(None, alias="MIB_family_name")

        class GroupsItem(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class VersionEnum(Enum):
                value_0 = "v1"
                value_1 = "v2c"
                value_2 = "v3"

            class AuthenticationEnum(Enum):
                value_0 = "auth"
                value_1 = "noauth"
                value_2 = "priv"

            name: str | None = None
            """
            Group name
            """
            version: VersionEnum | None = None
            authentication: AuthenticationEnum | None = None
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

        class UsersItem(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class VersionEnum(Enum):
                value_0 = "v1"
                value_1 = "v2c"
                value_2 = "v3"

            name: str | None = None
            """
            Username
            """
            group: str | None = None
            """
            Group name
            """
            remote_address: str | None = None
            """
            Hostname or ip of remote engine
            The remote_address and udp_port are used for remote users
            """
            udp_port: int | None = None
            """
            udp_port will not be used if no remote_address is configured
            """
            version: VersionEnum | None = None
            localized: Annotated[str, StrConvert(convert_types=(int))] | None = None
            """
            Engine ID in hexadecimal for localizing auth and/or priv
            """
            auth: str | None = None
            """
            Hash algorithm
            """
            auth_passphrase: str | None = None
            """
            Hashed authentication passphrase if localized is used else cleartext authentication passphrase
            """
            priv: str | None = None
            """
            Encryption algorithm
            """
            priv_passphrase: str | None = None
            """
            Hashed privacy passphrase if localized is used else cleartext privacy passphrase
            """

        class HostsItem(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class VersionEnum(Enum):
                value_0 = "1"
                value_1 = "2c"
                value_2 = "3"

            class UsersItem(BaseModel):
                model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                class AuthenticationLevelEnum(Enum):
                    value_0 = "auth"
                    value_1 = "noauth"
                    value_2 = "priv"

                username: str | None = None
                authentication_level: AuthenticationLevelEnum | None = None

            host: str | None = None
            """
            Host IP address or name
            """
            vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
            version: Annotated[VersionEnum, StrConvert(convert_types=(int))] | None = None
            community: str | None = None
            """
            Community name
            """
            users: list[UsersItem] | None = None

        class Traps(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class SnmpTrapsItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                name: str | None = None
                """
                Enable or disable specific snmp-traps and their sub_traps
                Examples:
                - "bgp"
                - "bgp established"
                """
                enabled: bool | None = True

            enable: bool | None = False
            """
            Enable or disable all snmp-traps
            """
            snmp_traps: list[SnmpTrapsItem] | None = None

        class VrfsItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: Annotated[str, StrConvert(convert_types=(int))] = None
            """
            VRF name
            """
            enable: bool | None = None

        engine_ids: EngineIds | None = None
        contact: str | None = None
        """
        SNMP contact
        """
        location: str | None = None
        """
        SNMP location
        """
        communities: list[CommunitiesItem] | None = None
        ipv4_acls: list[Ipv4AclsItem] | None = None
        ipv6_acls: list[Ipv6AclsItem] | None = None
        local_interfaces: list[LocalInterfacesItem] | None = None
        views: list[ViewsItem] | None = None
        groups: list[GroupsItem] | None = None
        users: list[UsersItem] | None = None
        hosts: list[HostsItem] | None = None
        traps: Traps | None = None
        vrfs: list[VrfsItem] | None = None

    class SpanningTree(BaseModel):
        model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

        class EdgePort(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            bpdufilter_default: bool | None = None
            bpduguard_default: bool | None = None

        class ModeEnum(Enum):
            value_0 = "mstp"
            value_1 = "rstp"
            value_2 = "rapid-pvst"
            value_3 = "none"

        class BpduguardRateLimit(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            default: bool | None = None
            count: int | None = None
            """
            Maximum number of BPDUs per timer interval
            """

        class Mst(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Configuration(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class InstancesItem(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    id: int = None
                    """
                    Instance ID
                    """
                    vlans: Annotated[str, StrConvert(convert_types=(int))] | None = None
                    """
                    "< vlan_id >, < vlan_id >-< vlan_id >"
                    Example: 15,16,17,18
                    """

                name: str | None = None
                revision: int | None = None
                """
                0-65535
                """
                instances: list[InstancesItem] | None = None

            pvst_border: bool | None = None
            configuration: Configuration | None = None

        class MstInstancesItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            id: Annotated[str, StrConvert(convert_types=(int))] = None
            """
            Instance ID
            """
            priority: int | None = None

        class RapidPvstInstancesItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            id: Annotated[str, StrConvert(convert_types=(int))] = None
            """
            "< vlan_id >, < vlan_id >-< vlan_id >"
            Example: 105,202,505-506
            """
            priority: int | None = None

        root_super: bool | None = None
        edge_port: EdgePort | None = None
        mode: ModeEnum | None = None
        bpduguard_rate_limit: BpduguardRateLimit | None = None
        rstp_priority: int | None = None
        mst: Mst | None = None
        mst_instances: list[MstInstancesItem] | None = None
        no_spanning_tree_vlan: Annotated[str, StrConvert(convert_types=(int))] | None = None
        """
        "< vlan_id >, < vlan_id >-< vlan_id >"
        Example: 105,202,505-506
        """
        rapid_pvst_instances: list[RapidPvstInstancesItem] | None = None

    class StandardAccessListsItem(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class SequenceNumbersItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            sequence: int = None
            """
            Sequence ID
            """
            action: str = None
            """
            Action as string
            Example: "deny ip any any"
            """

        name: str = None
        """
        Access-list Name
        """
        counters_per_entry: bool | None = None
        sequence_numbers: list[SequenceNumbersItem] = None

    class StaticRoutesItem(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
        """
        VRF Name
        """
        destination_address_prefix: str | None = None
        """
        IPv4_network/Mask
        """
        interface: str | None = None
        gateway: str | None = None
        """
        IPv4 Address
        """
        track_bfd: bool | None = None
        """
        Track next-hop using BFD
        """
        distance: int | None = Field(None, ge=1, le=255)
        tag: int | None = Field(None, ge=0, le=4294967295)
        name: str | None = None
        """
        Description
        """
        metric: int | None = Field(None, ge=0, le=4294967295)

    class Stun(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Client(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class ServerProfilesItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                name: str = None
                ip_address: str | None = None

            server_profiles: list[ServerProfilesItem] | None = None
            """
            List of server profiles for the client
            """

        class Server(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            local_interface: str | None = None
            local_interfaces: list[str] | None = Field(None, min_length=1)

        client: Client | None = None
        """
        STUN client settings
        """
        server: Server | None = None
        """
        STUN server settings
        """

    class SwitchportDefault(BaseModel):
        model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

        class ModeEnum(Enum):
            value_0 = "routed"
            value_1 = "access"

        class Phone(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class TrunkEnum(Enum):
                value_0 = "tagged"
                value_1 = "untagged"

            cos: int | None = Field(None, ge=0, le=7)
            trunk: TrunkEnum | None = None
            vlan: int | None = Field(None, ge=1, le=4094)
            """
            VLAN ID
            """

        mode: ModeEnum | None = None
        phone: Phone | None = None

    class System(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class ControlPlane(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class TcpMss(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                ipv4: int | None = None
                """
                Segment size
                """
                ipv6: int | None = None
                """
                Segment size
                """

            class Ipv4AccessGroupsItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                acl_name: str = None
                vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None

            class Ipv6AccessGroupsItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                acl_name: str = None
                vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None

            tcp_mss: TcpMss | None = None
            ipv4_access_groups: list[Ipv4AccessGroupsItem] | None = None
            ipv6_access_groups: list[Ipv6AccessGroupsItem] | None = None

        class L1(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class UnsupportedSpeedActionEnum(Enum):
                value_0 = "error"
                value_1 = "warn"

            class UnsupportedErrorCorrectionActionEnum(Enum):
                value_0 = "error"
                value_1 = "warn"

            unsupported_speed_action: UnsupportedSpeedActionEnum | None = None
            unsupported_error_correction_action: UnsupportedErrorCorrectionActionEnum | None = None

        control_plane: ControlPlane | None = None
        l1: L1 | None = None

    class TacacsServers(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class HostsItem(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class KeyTypeEnum(Enum):
                value_0 = "0"
                value_1 = "7"
                value_2 = "8a"

            host: str | None = None
            """
            Host IP address or name
            """
            vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
            key: str | None = None
            """
            Encrypted key
            """
            key_type: Annotated[KeyTypeEnum, StrConvert(convert_types=(int))] | None = "7"
            single_connection: bool | None = None
            timeout: int | None = Field(None, ge=1, le=1000)
            """
            Timeout in seconds
            """

        timeout: int | None = Field(None, ge=1, le=1000)
        """
        Timeout in seconds
        """
        hosts: list[HostsItem] | None = None
        policy_unknown_mandatory_attribute_ignore: bool | None = None

    class TapAggregation(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Mode(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Exclusive(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                enabled: bool | None = None
                profile: str | None = None
                """
                Profile Name
                """
                no_errdisable: list[str] | None = None

            exclusive: Exclusive | None = None

        class Mac(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class Timestamp(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Header(BaseModel):
                    model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                    class FormatEnum(Enum):
                        value_0 = "48-bit"
                        value_1 = "64-bit"

                    format: FormatEnum | None = None
                    eth_type: int | None = None
                    """
                    EtherType
                    """

                replace_source_mac: bool | None = None
                header: Header | None = None

            class FcsErrorEnum(Enum):
                value_0 = "correct"
                value_1 = "discard"
                value_2 = "pass-through"

            timestamp: Timestamp | None = None
            """
            mac.timestamp.replace_source_mac and mac.timestamp.header.format are mutually exclsuive. If both are defined,
            replace_source_mac takes precedence
            """
            fcs_append: bool | None = None
            """
            mac.fcs_append and mac.fcs_error are mutually exclusive. If both are defined, mac.fcs_append takes precedence
            """
            fcs_error: FcsErrorEnum | None = None

        mode: Mode | None = None
        encapsulation_dot1br_strip: bool | None = None
        encapsulation_vn_tag_strip: bool | None = None
        protocol_lldp_trap: bool | None = None
        truncation_size: int | None = None
        """
        Allowed truncation_size values vary depending on the platform
        """
        mac: Mac | None = None

    class TcamProfile(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class ProfilesItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str = None
            """
            Tcam-Profile Name
            """
            config: str | None = None
            """
            TCAM Profile Config. Since these can be very long, it is often a good idea to import the config from a file.
            Example:
            "{{ lookup('file', 'TCAM_TRAFFIC_POLICY.conf') }}"
            """
            source: str | None = None
            """
            TCAM profile local source path. Used to read the TCAM profile from a local path existing on the device.
            """

        system: str | None = None
        """
        TCAM profile name to activate
        """
        profiles: list[ProfilesItem] | None = None

    class Terminal(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        length: int | None = Field(None, ge=0, le=32767)
        width: int | None = Field(None, ge=10, le=32767)

    class TrackersItem(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        name: str = None
        """
        Name of tracker object
        """
        interface: str = None
        """
        Name of tracked interface
        """
        tracked_property: str | None = "line-protocol"
        """
        Property to track
        """

    class TrafficPolicies(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Options(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            counter_per_interface: bool | None = None

        class FieldSets(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Ipv4Item(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                name: str = None
                """
                IPv4 Prefix Field Set Name
                """
                prefixes: list[str] | None = None

            class Ipv6Item(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                name: str = None
                """
                IPv6 Prefix Field Set Name
                """
                prefixes: list[str] | None = None

            class PortsItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                name: str = None
                """
                L4 Port Field Set Name
                """
                port_range: str | None = None
                """
                Example: '10,20,80,440-450'
                """

            ipv4: list[Ipv4Item] | None = None
            ipv6: list[Ipv6Item] | None = None
            ports: list[PortsItem] | None = None

        class PoliciesItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class MatchesItem(BaseModel):
                model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                class TypeEnum(Enum):
                    value_0 = "ipv4"
                    value_1 = "ipv6"

                class Source(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    prefixes: list[str] | None = None
                    prefix_lists: list[str] | None = None
                    """
                    Field-set prefix lists
                    """

                class Destination(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    prefixes: list[str] | None = None
                    prefix_lists: list[str] | None = None
                    """
                    Field-set prefix lists
                    """

                class Fragment(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    offset: str | None = None
                    """
                    Fragment offset range
                    """

                class ProtocolsItem(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    protocol: str = None
                    src_port: str | None = None
                    """
                    Port range
                    """
                    dst_port: str | None = None
                    """
                    Port range
                    """
                    src_field: str | None = None
                    """
                    L4 port range field set
                    """
                    dst_field: str | None = None
                    """
                    L4 port range field set
                    """
                    flags: list[str] | None = None
                    icmp_type: list[str] | None = None

                class Actions(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    dscp: int | None = None
                    traffic_class: int | None = None
                    """
                    Traffic class ID
                    """
                    count: str | None = None
                    """
                    Counter name
                    """
                    drop: bool | None = None
                    log: bool | None = None
                    """
                    Only supported when action is set to drop
                    """

                name: str = None
                """
                Traffic Policy Item
                """
                type: TypeEnum | None = None
                source: Source | None = None
                destination: Destination | None = None
                ttl: str | None = None
                """
                TTL range
                """
                fragment: Fragment | None = None
                """
                The 'fragment' command is not supported when 'source port'
                or 'destination port' command is configured
                """
                protocols: list[ProtocolsItem] | None = None
                actions: Actions | None = None

            class DefaultActions(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Ipv4(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    dscp: int | None = None
                    traffic_class: int | None = None
                    """
                    Traffic class ID
                    """
                    count: str | None = None
                    """
                    Counter name
                    """
                    drop: bool | None = None
                    log: bool | None = None
                    """
                    Only supported when action is set to drop
                    """

                class Ipv6(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    dscp: int | None = None
                    traffic_class: int | None = None
                    """
                    Traffic class ID
                    """
                    count: str | None = None
                    """
                    Counter name
                    """
                    drop: bool | None = None
                    log: bool | None = None
                    """
                    Only supported when action is set to drop
                    """

                ipv4: Ipv4 | None = None
                ipv6: Ipv6 | None = None

            name: str = None
            """
            Traffic Policy Name
            """
            matches: list[MatchesItem] | None = None
            default_actions: DefaultActions | None = None

        options: Options | None = None
        field_sets: FieldSets | None = None
        policies: list[PoliciesItem] | None = None

    class TunnelInterfacesItem(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class TcpMssCeiling(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class DirectionEnum(Enum):
                value_0 = "ingress"
                value_1 = "egress"

            ipv4: int | None = Field(None, ge=64, le=65495)
            """
            Segment Size for IPv4
            """
            ipv6: int | None = Field(None, ge=64, le=65475)
            """
            Segment Size for IPv6
            """
            direction: DirectionEnum | None = None
            """
            Optional direction ('ingress', 'egress')  for tcp mss ceiling
            """

        name: str = None
        """
        Tunnel Interface Name
        """
        description: str | None = None
        shutdown: bool | None = None
        mtu: int | None = Field(None, ge=68, le=65535)
        vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
        """
        VRF Name
        """
        ip_address: str | None = None
        """
        IPv4_address/Mask
        """
        ipv6_enable: bool | None = None
        ipv6_address: str | None = None
        """
        IPv6_address/Mask
        """
        access_group_in: str | None = None
        """
        IPv4 ACL Name for ingress
        """
        access_group_out: str | None = None
        """
        IPv4 ACL Name for egress
        """
        ipv6_access_group_in: str | None = None
        """
        IPv6 ACL Name for ingress
        """
        ipv6_access_group_out: str | None = None
        """
        IPv6 ACL Name for egress
        """
        tcp_mss_ceiling: TcpMssCeiling | None = None
        source_interface: str | None = None
        """
        Tunnel Source Interface Name
        """
        destination: str | None = None
        """
        IPv4 or IPv6 Address Tunnel Destination
        """
        path_mtu_discovery: bool | None = None
        """
        Enable Path MTU Discovery On Tunnel
        """
        eos_cli: str | None = None
        """
        Multiline String with EOS CLI rendered directly on the Tunnel interface in the final EOS configuration.
        """

    class VirtualSourceNatVrfsItem(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        name: Annotated[str, StrConvert(convert_types=(int))] = None
        """
        VRF Name
        """
        ip_address: str | None = None
        """
        IPv4 Address
        """

    class VlanInterfacesItem(BaseModel):
        model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

        class IpHelpersItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            ip_helper: str = None
            """
            IP address or hostname of DHCP server
            """
            source_interface: str | None = None
            """
            Interface used as source for forwarded DHCP packets
            """
            vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
            """
            VRF where DHCP server can be reached
            """

        class IpNat(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Destination(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class DynamicItem(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    access_list: str = None
                    comment: str | None = None
                    pool_name: str = None
                    priority: int | None = Field(None, ge=0, le=4294967295)

                class StaticItem(BaseModel):
                    model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                    class DirectionEnum(Enum):
                        value_0 = "egress"
                        value_1 = "ingress"

                    class ProtocolEnum(Enum):
                        value_0 = "udp"
                        value_1 = "tcp"

                    access_list: str | None = None
                    """
                    'access_list' and 'group' are mutual exclusive
                    """
                    comment: str | None = None
                    direction: DirectionEnum | None = None
                    """
                    Egress or ingress can be the default. This depends on source/destination, EOS version, and hardware platform.
                    EOS might
                    remove this keyword in the configuration. So, check the configuration on targeted HW/SW.
                    """
                    group: int | None = Field(None, ge=1, le=65535)
                    """
                    'access_list' and 'group' are mutual exclusive
                    """
                    original_ip: str = None
                    """
                    IPv4 address
                    """
                    original_port: int | None = Field(None, ge=1, le=65535)
                    priority: int | None = Field(None, ge=0, le=4294967295)
                    protocol: ProtocolEnum | None = None
                    translated_ip: str = None
                    """
                    IPv4 address
                    """
                    translated_port: int | None = Field(None, ge=1, le=65535)
                    """
                    requires 'original_port'
                    """

                dynamic: list[DynamicItem] | None = None
                static: list[StaticItem] | None = None

            class Source(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class DynamicItem(BaseModel):
                    model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                    class NatTypeEnum(Enum):
                        value_0 = "overload"
                        value_1 = "pool"
                        value_2 = "pool-address-only"
                        value_3 = "pool-full-cone"

                    access_list: str = None
                    comment: str | None = None
                    nat_type: NatTypeEnum = None
                    pool_name: str | None = None
                    """
                    required if 'nat_type' is pool, pool-address-only or pool-full-cone
                    ignored if 'nat_type' is overload
                    """
                    priority: int | None = Field(None, ge=0, le=4294967295)

                class StaticItem(BaseModel):
                    model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                    class DirectionEnum(Enum):
                        value_0 = "egress"
                        value_1 = "ingress"

                    class ProtocolEnum(Enum):
                        value_0 = "udp"
                        value_1 = "tcp"

                    access_list: str | None = None
                    """
                    'access_list' and 'group' are mutual exclusive
                    """
                    comment: str | None = None
                    direction: DirectionEnum | None = None
                    """
                    Egress or ingress can be the default. This depends on source/destination, EOS version, and hardware platform.
                    EOS might
                    remove this keyword in the configuration. So, check the configuration on targeted HW/SW.
                    """
                    group: int | None = Field(None, ge=1, le=65535)
                    """
                    'access_list' and 'group' are mutual exclusive
                    """
                    original_ip: str = None
                    """
                    IPv4 address
                    """
                    original_port: int | None = Field(None, ge=1, le=65535)
                    priority: int | None = Field(None, ge=0, le=4294967295)
                    protocol: ProtocolEnum | None = None
                    translated_ip: str = None
                    """
                    IPv4 address
                    """
                    translated_port: int | None = Field(None, ge=1, le=65535)
                    """
                    requires 'original_port'
                    """

                dynamic: list[DynamicItem] | None = None
                static: list[StaticItem] | None = None

            destination: Destination | None = None
            source: Source | None = None

        class Ipv6NdPrefixesItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            ipv6_prefix: str = None
            """
            IPv6_address/Mask
            """
            valid_lifetime: Annotated[str, StrConvert(convert_types=(int))] | None = None
            """
            In seconds <0-4294967295> or infinite
            """
            preferred_lifetime: Annotated[str, StrConvert(convert_types=(int))] | None = None
            """
            In seconds <0-4294967295> or infinite
            """
            no_autoconfig_flag: bool | None = None

        class Ipv6DhcpRelayDestinationsItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            address: str = None
            """
            DHCP server's IPv6 address
            """
            vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
            local_interface: str | None = None
            """
            Local interface to communicate with DHCP server - mutually exclusive to source_address
            """
            source_address: str | None = None
            """
            Source IPv6 address to communicate with DHCP server - mutually exclusive to local_interface
            """
            link_address: str | None = None
            """
            Override the default link address specified in the relayed DHCP packet
            """

        class Multicast(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Ipv4(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class BoundariesItem(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    boundary: str = None
                    """
                    IPv4 access-list name or IPv4 multicast group prefix with mask
                    """
                    out: bool | None = None

                class SourceRouteExport(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    enabled: bool = None
                    administrative_distance: int | None = Field(None, ge=1, le=255)

                boundaries: list[BoundariesItem] | None = None
                """
                Boundaries can be either 1 ACL or a list of multicast IP address_range(s)/prefix but not combination of both
                """
                source_route_export: SourceRouteExport | None = None
                static: bool | None = None

            class Ipv6(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class BoundariesItem(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    boundary: str = None
                    """
                    IPv6 access-list name or IPv6 multicast group prefix with mask
                    """

                class SourceRouteExport(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    enabled: bool = None
                    administrative_distance: int | None = Field(None, ge=1, le=255)

                boundaries: list[BoundariesItem] | None = None
                """
                Boundaries can be either 1 ACL or a list of multicast IP address_range(s)/prefix but not combination of both
                """
                source_route_export: SourceRouteExport | None = None
                static: bool | None = None

            ipv4: Ipv4 | None = None
            ipv6: Ipv6 | None = None

        class OspfAuthenticationEnum(Enum):
            value_0 = "none"
            value_1 = "simple"
            value_2 = "message-digest"

        class OspfMessageDigestKeysItem(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class HashAlgorithmEnum(Enum):
                value_0 = "md5"
                value_1 = "sha1"
                value_2 = "sha256"
                value_3 = "sha384"
                value_4 = "sha512"

            id: int = None
            hash_algorithm: HashAlgorithmEnum | None = None
            key: str | None = None
            """
            Encrypted password
            """

        class Pim(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Ipv4(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                dr_priority: int | None = Field(None, ge=0, le=429467295)
                sparse_mode: bool | None = None
                local_interface: str | None = None

            ipv4: Ipv4 | None = None

        class VrrpIdsItem(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Advertisement(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                interval: int | None = Field(None, ge=1, le=255)
                """
                Interval in seconds
                """

            class Preempt(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Delay(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    minimum: int | None = Field(None, ge=0, le=3600)
                    """
                    Minimum preempt delay in seconds
                    """
                    reload: int | None = Field(None, ge=0, le=3600)
                    """
                    Reload preempt delay in seconds
                    """

                enabled: bool = None
                delay: Delay | None = None

            class Timers(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Delay(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    reload: int | None = Field(None, ge=0, le=3600)
                    """
                    Delay after reload in seconds.
                    """

                delay: Delay | None = None

            class TrackedObjectItem(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                name: str = None
                """
                Tracked object name
                """
                decrement: int | None = Field(None, ge=1, le=254)
                """
                Decrement VRRP priority by 1-254
                """
                shutdown: bool | None = None

            class Ipv4(BaseModel):
                model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

                class VersionEnum(Enum):
                    value_0 = 2
                    value_1 = 3

                address: str = None
                """
                Virtual IPv4 address
                """
                version: VersionEnum | None = None

            class Ipv6(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                address: str = None
                """
                Virtual IPv6 address
                """

            id: int = None
            """
            VRID
            """
            priority_level: int | None = Field(None, ge=1, le=254)
            """
            Instance priority
            """
            advertisement: Advertisement | None = None
            preempt: Preempt | None = None
            timers: Timers | None = None
            tracked_object: list[TrackedObjectItem] | None = None
            ipv4: Ipv4 | None = None
            ipv6: Ipv6 | None = None

        class Vrrp(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            virtual_router: str | None = None
            """
            Virtual Router ID
            """
            priority: int | None = None
            """
            Instance priority
            """
            advertisement_interval: int | None = None
            preempt_delay_minimum: int | None = None
            ipv4: str | None = None
            """
            Virtual IPv4 address
            """
            ipv6: str | None = None
            """
            Virtual IPv6 address
            """

        class IpAttachedHostRouteExport(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            enabled: bool = None
            distance: int | None = Field(None, ge=1, le=255)

        class Bfd(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            echo: bool | None = None
            interval: int | None = None
            """
            Rate in milliseconds
            """
            min_rx: int | None = None
            """
            Minimum RX hold time in milliseconds
            """
            multiplier: int | None = Field(None, ge=3, le=50)

        class ServicePolicy(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Pbr(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                input: str | None = None
                """
                Name of policy-map used for policy based routing
                """

            pbr: Pbr | None = None

        name: str = None
        """
        VLAN interface name like "Vlan123"
        """
        description: str | None = None
        shutdown: bool | None = None
        vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
        """
        VRF name
        """
        arp_aging_timeout: int | None = Field(None, ge=1, le=65535)
        """
        In seconds
        """
        arp_cache_dynamic_capacity: int | None = Field(None, ge=0, le=4294967295)
        arp_gratuitous_accept: bool | None = None
        arp_monitor_mac_address: bool | None = None
        ip_proxy_arp: bool | None = None
        ip_directed_broadcast: bool | None = None
        ip_address: str | None = None
        """
        IPv4_address/Mask
        """
        ip_address_secondaries: list[str] | None = None
        ip_virtual_router_addresses: list[str] | None = None
        ip_address_virtual: str | None = None
        """
        IPv4_address/Mask
        """
        ip_address_virtual_secondaries: list[str] | None = None
        ip_igmp: bool | None = None
        ip_igmp_version: int | None = Field(None, ge=1, le=3)
        ip_helpers: list[IpHelpersItem] | None = None
        """
        List of DHCP servers
        """
        ip_nat: IpNat | None = None
        ipv6_enable: bool | None = None
        ipv6_address: str | None = None
        """
        IPv6_address/Mask
        """
        ipv6_address_virtual: str | None = None
        """
        IPv6_address/Mask
        If both "ipv6_address_virtual" and "ipv6_address_virtuals" are set, all addresses will be configured
        """
        ipv6_address_virtuals: list[str] | None = None
        """
        The new "ipv6_address_virtuals" key support multiple virtual ipv6 addresses.
        """
        ipv6_address_link_local: str | None = None
        """
        IPv6_address/Mask
        """
        ipv6_virtual_router_address: str | None = None
        """
        "ipv6_virtual_router_address" should not be mixed with
        the new "ipv6_virtual_router_addresses" key below to avoid
        conflicts.
        """
        ipv6_virtual_router_addresses: list[str] | None = None
        """
        Improved "VARPv6" data model to support multiple VARPv6 addresses.
        """
        ipv6_nd_ra_disabled: bool | None = None
        ipv6_nd_managed_config_flag: bool | None = None
        ipv6_nd_prefixes: list[Ipv6NdPrefixesItem] | None = None
        ipv6_dhcp_relay_destinations: list[Ipv6DhcpRelayDestinationsItem] | None = None
        access_group_in: str | None = None
        """
        IPv4 access-list name
        """
        access_group_out: str | None = None
        """
        IPv4 access-list name
        """
        ipv6_access_group_in: str | None = None
        """
        IPv6 access-list name
        """
        ipv6_access_group_out: str | None = None
        """
        IPv6 access-list name
        """
        multicast: Multicast | None = None
        ospf_network_point_to_point: bool | None = None
        ospf_area: Annotated[str, StrConvert(convert_types=(int))] | None = None
        ospf_cost: int | None = None
        ospf_authentication: OspfAuthenticationEnum | None = None
        ospf_authentication_key: str | None = None
        """
        Encrypted password used for simple authentication
        """
        ospf_message_digest_keys: list[OspfMessageDigestKeysItem] | None = None
        """
        Keys used for message-digest authentication
        """
        pim: Pim | None = None
        isis_enable: str | None = None
        """
        ISIS instance name
        """
        isis_passive: bool | None = None
        isis_metric: int | None = None
        isis_network_point_to_point: bool | None = None
        mtu: int | None = None
        no_autostate: bool | None = None
        vrrp_ids: list[VrrpIdsItem] | None = None
        """
        Improved "vrrp" data model to support multiple VRRP IDs
        """
        vrrp: Vrrp | None = None
        """
        "vrrp" should not be mixed with the new "vrrp_ids" key above to avoid conflicts.
        """
        ip_attached_host_route_export: IpAttachedHostRouteExport | None = None
        bfd: Bfd | None = None
        service_policy: ServicePolicy | None = None
        pvlan_mapping: str | None = None
        """
        List of VLANs as string
        """
        tenant: str | None = None
        """
        Key only used for documentation or validation purposes
        """
        tags: list[str] | None = None
        """
        Key only used for documentation or validation purposes
        """
        type: str | None = None
        """
        Key only used for documentation or validation purposes
        """
        eos_cli: str | None = None
        """
        Multiline EOS CLI rendered directly on the VLAN interface in the final EOS configuration
        """

    class VlanInternalOrder(BaseModel):
        model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

        class AllocationEnum(Enum):
            value_0 = "ascending"
            value_1 = "descending"

        class Range(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            beginning: int = Field(None, ge=2, le=4094)
            """
            First VLAN ID.
            """
            ending: int = Field(None, ge=2, le=4094)
            """
            Last VLAN ID.
            """

        allocation: AllocationEnum = None
        range: Range = None

    class VlansItem(BaseModel):
        model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

        class StateEnum(Enum):
            value_0 = "active"
            value_1 = "suspend"

        class PrivateVlan(BaseModel):
            model_config = ConfigDict(defer_build=True, use_enum_values=True, extra="forbid")

            class TypeEnum(Enum):
                value_0 = "community"
                value_1 = "isolated"

            type: TypeEnum | None = None
            primary_vlan: int | None = None
            """
            Primary VLAN ID
            """

        id: int = None
        """
        VLAN ID
        """
        name: str | None = None
        """
        VLAN Name
        """
        state: StateEnum | None = None
        trunk_groups: list[str] | None = None
        private_vlan: PrivateVlan | None = None
        tenant: str | None = None
        """
        Key only used for documentation or validation purposes
        """

    class VmtracerSessionsItem(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        name: str = None
        """
        Vmtracer Session Name
        """
        url: str | None = None
        username: str | None = None
        password: str | None = None
        """
        Type 7 Password Hash
        """
        autovlan_disable: bool | None = None
        source_interface: str | None = None

    class VrfsItem(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        name: Annotated[str, StrConvert(convert_types=(int))] = None
        """
        VRF Name
        """
        description: str | None = None
        ip_routing: bool | None = None
        ipv6_routing: bool | None = None
        ip_routing_ipv6_interfaces: bool | None = None
        tenant: str | None = None
        """
        Key only used for documentation or validation purposes
        """

    class VxlanInterface(BaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Vxlan1(BaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Vxlan(BaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class ControllerClient(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    enabled: bool | None = None

                class BfdVtepEvpn(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    interval: int | None = None
                    min_rx: int | None = None
                    multiplier: int | None = Field(None, ge=3, le=50)
                    prefix_list: str | None = None

                class Qos(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    dscp_propagation_encapsulation: bool | None = None
                    ecn_propagation: bool | None = None
                    """
                    Enable copying the ECN marking to/from encapsulated packets.
                    """
                    map_dscp_to_traffic_class_decapsulation: bool | None = None

                class VlansItem(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    id: int = None
                    """
                    VLAN ID
                    """
                    vni: int | None = None
                    multicast_group: str | None = None
                    """
                    IP Multicast Group Address
                    """
                    flood_vteps: list[str] | None = None

                class VrfsItem(BaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    name: Annotated[str, StrConvert(convert_types=(int))] = None
                    """
                    VRF Name
                    """
                    vni: int | None = None
                    multicast_group: str | None = None
                    """
                    IP Multicast Group Address
                    """

                source_interface: str | None = None
                """
                Source Interface Name
                """
                controller_client: ControllerClient | None = None
                """
                Client to CVX Controllers
                """
                mlag_source_interface: str | None = None
                udp_port: int | None = None
                virtual_router_encapsulation_mac_address: str | None = None
                """
                "mlag-system-id" or ethernet_address (H.H.H)
                """
                bfd_vtep_evpn: BfdVtepEvpn | None = None
                qos: Qos | None = None
                """
                For the Traffic Class to be derived based on the outer DSCP field of the incoming VxLan packet, the core ports must be
                in "DSCP Trust" mode.
                !!!Warning, only few hardware types with software version >= 4.26.0 support the below knobs to
                configure Vxlan DSCP mapping.
                """
                vlans: list[VlansItem] | None = None
                vrfs: list[VrfsItem] | None = None
                flood_vteps: list[str] | None = None
                flood_vtep_learned_data_plane: bool | None = None

            description: str | None = None
            vxlan: Vxlan | None = None
            eos_cli: str | None = None
            """
            Multiline String with EOS CLI rendered directly on the Vxlan interface in the final EOS configuration.
            """

        field_Vxlan1: Vxlan1 | None = Field(None, alias="Vxlan1")

    aaa_accounting: AaaAccounting | None = None
    aaa_authentication: AaaAuthentication | None = None
    aaa_authorization: AaaAuthorization | None = None
    aaa_root: AaaRoot | None = None
    aaa_server_groups: list[AaaServerGroupsItem] | None = None
    access_lists: list[AccessListsItem] | None = Field(None, title="IP Extended Access-Lists (legacy model)")
    address_locking: AddressLocking | None = None
    agents: list[AgentsItem] | None = None
    aliases: str | None = None
    """
    Multi-line string with one or more alias commands.

    Example:

    ```yaml
    aliases: |
      alias wr copy running-config startup-
    config
      alias siib show ip interface brief
    ```
    """
    arp: Arp | None = None
    as_path: AsPath | None = None
    avd_data_conversion_mode: AvdDataConversionModeEnum | None = "debug"
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
    avd_data_validation_mode: AvdDataValidationModeEnum | None = "warning"
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
    banners: Banners | None = None
    bgp_groups: list[BgpGroupsItem] | None = None
    boot: Boot | None = Field(None, title="System Boot Settings")
    """
    Set the Aboot password
    """
    class_maps: ClassMaps | None = Field(None, title="QOS Class-maps")
    clock: Clock | None = None
    community_lists: list[CommunityListsItem] | None = Field(None, title="Community Lists (legacy model)")
    custom_templates: list[str] | None = Field(None, title="Extensibility with Custom Templates")
    """
    - Custom templates can be added below the playbook directory.
    - If a location above the directory is desired, a symbolic
    link can be used.
    - Example under the `playbooks` directory create symbolic link with the following command:

      ```bash
    ln -s ../../shared_repo/custom_avd_templates/ ./custom_avd_templates
      ```

    - The output will be rendered at the end of
    the configuration.
    - The order of custom templates in the list can be important if they overlap.
    - It is recommended to
    use a `!` delimiter at the top of each custom template.

    Add `custom_templates` to group/host variables:
    """
    cvx: Cvx | None = None
    """
    CVX server features are not supported on physical switches. See `management_cvx` for client configurations.
    """
    daemon_terminattr: DaemonTerminattr | None = None
    """
    You can either provide a list of IPs/FQDNs to target on-premise Cloudvision cluster or use DNS name for your Cloudvision
    as a Service instance.
    Streaming to multiple clusters both on-prem and cloud service is supported.

    !!! note
        For
    TerminAttr version recommendation and EOS compatibility matrix, please refer to the latest TerminAttr Release Notes
    which always contain the latest recommended versions and minimum required versions per EOS release.
    """
    daemons: list[DaemonsItem] | None = Field(None, title="Custom Daemons")
    """
    This will add a daemon to the eos configuration that is most useful when trying to run OpenConfig clients like
    ocprometheus.
    """
    dhcp_relay: DhcpRelay | None = None
    dns_domain: str | None = None
    """
    Domain Name
    """
    domain_list: list[str] | None = None
    """
    Search list of DNS domains
    """
    dot1x: Dot1x | None = Field(None, title="Global 802.1x Authentication")
    dps_interfaces: list[DpsInterfacesItem] | None = Field(None, min_length=1, max_length=1)
    dynamic_prefix_lists: list[DynamicPrefixListsItem] | None = None
    enable_password: EnablePassword | None = None
    eos_cli: str | None = None
    """
    Multiline string with EOS CLI rendered directly on the root level of the final EOS configuration
    """
    eos_cli_config_gen_configuration: EosCliConfigGenConfiguration | None = None
    eos_cli_config_gen_documentation: EosCliConfigGenDocumentation | None = None
    errdisable: Errdisable | None = None
    ethernet_interfaces: list[EthernetInterfacesItem] | None = None
    event_handlers: list[EventHandlersItem] | None = None
    """
    Gives the ability to monitor and react to Syslog messages.
    Event Handlers provide a powerful and flexible tool that can
    be used to apply self-healing actions,
    customize the system behavior, and implement workarounds to problems discovered
    in the field.
    """
    event_monitor: EventMonitor | None = None
    flow_tracking: FlowTracking | None = None
    flow_trackings: list[FlowTrackingsItem] | None = None
    generate_default_config: bool | None = True
    """
    The `generate_default_config` knob allows to omit default EOS configuration.
    This can be useful when leveraging
    `eos_cli_config_gen` to generate configlets with CloudVision.

    The following commands will be omitted when
    `generate_default_config` is set to `false`:

    - RANCID Content Type
    - Hostname
    - Default configuration for `aaa`
    -
    Default configuration for `enable password`
    - Transceiver qsfp default mode
    - End of configuration delimiter
    """
    generate_device_documentation: bool | None = True
    hardware: Hardware | None = None
    hardware_counters: HardwareCounters | None = None
    hostname: str | None = None
    interface_defaults: InterfaceDefaults | None = None
    interface_groups: list[InterfaceGroupsItem] | None = Field(None, title="Maintenance Interface Groups")
    interface_profiles: list[InterfaceProfilesItem] | None = None
    ip_access_lists: list[IpAccessListsItem] | None = Field(None, title="IP Extended Access-Lists (improved model)")
    ip_access_lists_max_entries: int | None = None
    """
    Limit ACL entries defined under the `ip_access_lists`.
    """
    ip_community_lists: list[IpCommunityListsItem] | None = Field(None, title="IP Community Lists")
    """
    Communities and regexp entries MUST not be configured in the same community-list
    """
    ip_dhcp_relay: IpDhcpRelay | None = None
    ip_domain_lookup: IpDomainLookup | None = None
    ip_extcommunity_lists: list[IpExtcommunityListsItem] | None = Field(None, title="IP Extended Community Lists")
    ip_extcommunity_lists_regexp: list[IpExtcommunityListsRegexpItem] | None = Field(None, title="IP Extended Community Lists RegExp")
    ip_hardware: IpHardware | None = None
    ip_http_client_source_interfaces: list[IpHttpClientSourceInterfacesItem] | None = None
    ip_icmp_redirect: bool | None = None
    ip_igmp_snooping: IpIgmpSnooping | None = None
    ip_name_servers: list[IpNameServersItem] | None = None
    ip_nat: IpNat | None = None
    ip_radius_source_interfaces: list[IpRadiusSourceInterfacesItem] | None = None
    ip_routing: bool | None = None
    ip_routing_ipv6_interfaces: bool | None = None
    ip_security: IpSecurity | None = None
    ip_ssh_client_source_interfaces: list[IpSshClientSourceInterfacesItem] | None = None
    ip_tacacs_source_interfaces: list[IpTacacsSourceInterfacesItem] | None = Field(None, title="IP Tacacs Source Interfaces")
    ip_virtual_router_mac_address: str | None = None
    """
    MAC address (hh:hh:hh:hh:hh:hh)
    """
    ipv6_access_lists: list[Ipv6AccessListsItem] | None = Field(None, title="IPv6 Extended Access-Lists")
    ipv6_hardware: Ipv6Hardware | None = None
    ipv6_icmp_redirect: bool | None = None
    ipv6_prefix_lists: list[Ipv6PrefixListsItem] | None = None
    ipv6_standard_access_lists: list[Ipv6StandardAccessListsItem] | None = None
    ipv6_static_routes: list[Ipv6StaticRoutesItem] | None = None
    ipv6_unicast_routing: bool | None = None
    is_deployed: bool | None = True
    """
    Key only used for documentation or validation purposes
    """
    l2_protocol: L2Protocol | None = None
    lacp: Lacp | None = None
    """
    Set Link Aggregation Control Protocol (LACP) parameters.
    """
    link_tracking_groups: list[LinkTrackingGroupsItem] | None = None
    lldp: Lldp | None = None
    load_interval: LoadInterval | None = None
    local_users: list[LocalUsersItem] | None = None
    logging: Logging | None = None
    loopback_interfaces: list[LoopbackInterfacesItem] | None = None
    mac_access_lists: list[MacAccessListsItem] | None = None
    mac_address_table: MacAddressTable | None = None
    mac_security: MacSecurity | None = Field(None, title="MAC Security (MACsec)")
    maintenance: Maintenance | None = Field(None, title="Maintenance Mode")
    management_accounts: ManagementAccounts | None = None
    management_api_gnmi: ManagementApiGnmi | None = None
    management_api_http: ManagementApiHttp | None = None
    management_api_models: ManagementApiModels | None = None
    management_console: ManagementConsole | None = None
    management_cvx: ManagementCvx | None = None
    management_defaults: ManagementDefaults | None = None
    management_interfaces: list[ManagementInterfacesItem] | None = None
    management_security: ManagementSecurity | None = None
    management_ssh: ManagementSsh | None = None
    management_tech_support: ManagementTechSupport | None = None
    match_list_input: MatchListInput | None = Field(None, title="Match Lists")
    mcs_client: McsClient | None = None
    mlag_configuration: MlagConfiguration | None = Field(None, title="Multi-Chassis Link Aggregation (MLAG) Configuration")
    monitor_connectivity: MonitorConnectivity | None = None
    monitor_sessions: list[MonitorSessionsItem] | None = None
    mpls: Mpls | None = None
    name_server: NameServer | None = None
    ntp: Ntp | None = None
    patch_panel: PatchPanel | None = None
    peer_filters: list[PeerFiltersItem] | None = None
    platform: Platform | None = None
    """
    Every key below this point is platform dependent.
    """
    poe: Poe | None = None
    policy_maps: PolicyMaps | None = None
    port_channel_interfaces: list[PortChannelInterfacesItem] | None = None
    prefix_lists: list[PrefixListsItem] | None = None
    priority_flow_control: PriorityFlowControl | None = None
    """
    Global Priority Flow Control settings.
    """
    prompt: str | None = None
    ptp: Ptp | None = None
    qos: Qos | None = None
    qos_profiles: list[QosProfilesItem] | None = None
    queue_monitor_length: QueueMonitorLength | None = None
    queue_monitor_streaming: QueueMonitorStreaming | None = None
    radius_server: RadiusServer | None = None
    radius_servers: list[RadiusServersItem] | None = None
    redundancy: Redundancy | None = None
    roles: list[RolesItem] | None = None
    route_maps: list[RouteMapsItem] | None = None
    router_adaptive_virtual_topology: RouterAdaptiveVirtualTopology | None = None
    router_bfd: RouterBfd | None = None
    router_bgp: RouterBgp | None = None
    router_general: RouterGeneral | None = Field(None, title="Router General configuration")
    router_igmp: RouterIgmp | None = Field(None, title="Router IGMP Configuration")
    router_isis: RouterIsis | None = None
    router_l2_vpn: RouterL2Vpn | None = None
    router_msdp: RouterMsdp | None = None
    router_multicast: RouterMulticast | None = None
    router_ospf: RouterOspf | None = Field(None, title="Router OSPF Configuration")
    router_path_selection: RouterPathSelection | None = None
    """
    Dynamic path selection configuration.
    """
    router_pim_sparse_mode: RouterPimSparseMode | None = None
    router_service_insertion: RouterServiceInsertion | None = None
    """
    Configure network services inserted to data forwarding
    """
    router_traffic_engineering: RouterTrafficEngineering | None = None
    service_routing_configuration_bgp: ServiceRoutingConfigurationBgp | None = None
    service_routing_protocols_model: ServiceRoutingProtocolsModelEnum | None = None
    service_unsupported_transceiver: ServiceUnsupportedTransceiver | None = None
    sflow: Sflow | None = None
    snmp_server: SnmpServer | None = None
    """
    SNMP settings
    """
    spanning_tree: SpanningTree | None = None
    standard_access_lists: list[StandardAccessListsItem] | None = None
    static_routes: list[StaticRoutesItem] | None = None
    stun: Stun | None = None
    """
    STUN configuration
    """
    switchport_default: SwitchportDefault | None = None
    system: System | None = None
    tacacs_servers: TacacsServers | None = None
    tap_aggregation: TapAggregation | None = None
    tcam_profile: TcamProfile | None = Field(None, title="Hardware TCAM Profiles")
    terminal: Terminal | None = Field(None, title="Terminal Settings")
    trackers: list[TrackersItem] | None = None
    traffic_policies: TrafficPolicies | None = None
    tunnel_interfaces: list[TunnelInterfacesItem] | None = None
    virtual_source_nat_vrfs: list[VirtualSourceNatVrfsItem] | None = None
    vlan_interfaces: list[VlanInterfacesItem] | None = None
    vlan_internal_order: VlanInternalOrder | None = None
    vlans: list[VlansItem] | None = None
    vmtracer_sessions: list[VmtracerSessionsItem] | None = None
    vrfs: list[VrfsItem] | None = None
    """
    These keys are ignored if the name of the vrf is 'default'
    """
    vxlan_interface: VxlanInterface | None = None
