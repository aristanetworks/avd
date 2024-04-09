# Copyright (c) 2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field
from typing_extensions import Annotated

from .models import AvdDictBaseModel
from .types import IntConvert, StrConvert


class EosCliConfigGen(BaseModel):
    model_config = ConfigDict(defer_build=True)

    class AaaAccounting(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Exec(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Console(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                type: Literal["none", "start-stop", "stop-only"] | None = None
                group: str | None = None
                """
                Group Name
                """
                logging: bool | None = None

            class Default(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                type: Literal["none", "start-stop", "stop-only"] | None = None
                group: str | None = None
                """
                Group Name
                """
                logging: bool | None = None

            console: Console | None = None
            default: Default | None = None

        class System(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Default(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                type: Literal["none", "start-stop", "stop-only"] | None = None
                group: str | None = None
                """
                Group Name
                """

            default: Default | None = None

        class Dot1x(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Default(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                type: Literal["start-stop", "stop-only"] | None = None
                group: str | None = None
                """
                Group Name
                """

            default: Default | None = None

        class Commands(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class ConsoleItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                commands: Annotated[str, StrConvert(convert_types=(int))] | None = None
                """
                Privelege level 'all' or 0-15
                """
                type: Literal["none", "start-stop", "stop-only"] | None = None
                group: str | None = None
                """
                Group Name
                """
                logging: bool | None = None

            class DefaultItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                commands: Annotated[str, StrConvert(convert_types=(int))] | None = None
                """
                Privelege level 'all' or 0-15
                """
                type: Literal["none", "start-stop", "stop-only"] | None = None
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

    class AaaAuthentication(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Login(AvdDictBaseModel):
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

        class Enable(AvdDictBaseModel):
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

        class Dot1x(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            default: str | None = None
            """
            802.1x authentication method(s) as a string.
            Examples:
            - "group radius"
            - "group MYGROUP group radius"
            """

        class Policies(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Local(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                allow_nopassword: bool | None = None

            class Lockout(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                failure: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=255)
                duration: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=4294967295)
                window: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=4294967295)

            on_failure_log: bool | None = None
            on_success_log: bool | None = None
            local: Local | None = None
            lockout: Lockout | None = None

        login: Login | None = None
        enable: Enable | None = None
        dot1x: Dot1x | None = None
        policies: Policies | None = None

    class AaaAuthorization(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Policy(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            local_default_role: str | None = None

        class Exec(AvdDictBaseModel):
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

        class Dynamic(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            dot1x_additional_groups: list[str] | None = Field(None, min_length=1)

        class Commands(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class PrivilegeItem(AvdDictBaseModel):
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

    class AaaRoot(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Secret(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            sha512_password: str | None = None

        secret: Secret | None = None

    class AaaServerGroupsItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class ServersItem(AvdDictBaseModel):
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
        type: Literal["tacacs+", "radius", "ldap"] | None = None
        servers: list[ServersItem] | None = None

    class AccessListsItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class SequenceNumbersItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            sequence: Annotated[int, IntConvert(convert_types=(str))] = None
            """
            Sequence ID
            """
            action: str = None
            """
            Action as string
            Example: "deny ip any any"
            """

        name: Annotated[str, StrConvert(convert_types=(int))] = None
        """
        Access-list Name
        """
        counters_per_entry: bool | None = None
        sequence_numbers: list[SequenceNumbersItem] = None

    class AddressLocking(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class LeasesItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            ip: str = None
            """
            IP address
            """
            mac: str = None
            """
            MAC address (hhhh.hhhh.hhhh or hh:hh:hh:hh:hh:hh)
            """

        class LockedAddress(AvdDictBaseModel):
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

    class AgentsItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class EnvironmentVariablesItem(AvdDictBaseModel):
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

    class ApplicationTrafficRecognition(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class CategoriesItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class ApplicationsItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                name: str | None = None
                """
                Application name.
                """
                service: Literal["audio-video", "chat", "default", "file-transfer", "networking-protocols", "peer-to-peer", "software-update"] | None = None
                """
                Service Name.
                Specific service to target for this application.
                If no service is specified, all supported services of the
                application are matched.
                Not all valid values are valid for all applications, check on EOS CLI.
                """

            name: str = None
            """
            Category name.
            """
            applications: list[ApplicationsItem] | None = None
            """
            List of applications.
            """

        class FieldSets(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class L4PortsItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                name: str = None
                """
                L4 port field-set name.
                """
                port_values: list[Annotated[str, StrConvert(convert_types=(int))]] | None = None

            class Ipv4PrefixesItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                name: str = None
                """
                IPv4 prefix field-set name.
                """
                prefix_values: list[str] | None = None

            l4_ports: list[L4PortsItem] | None = None
            """
            L4 port field-set.
            """
            ipv4_prefixes: list[Ipv4PrefixesItem] | None = None
            """
            IPv4 prefix field set.
            """

        class Applications(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Ipv4ApplicationsItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                name: str = None
                """
                Application name.
                """
                src_prefix_set_name: str | None = None
                """
                Source prefix set name.
                """
                dest_prefix_set_name: str | None = None
                """
                Destination prefix set name.
                """
                protocols: list[str] | None = None
                """
                List of protocols to consider for this application.

                To use port field-sets (source, destination or both), the list
                must
                contain only one or two protocols, either `tcp` or `udp`.
                When using both protocols, one line is rendered for each in
                the configuration,
                hence the field-sets must have the same value for `tcp_src_port_set_name` and
                `udp_src_port_set_name`
                and for `tcp_dest_port_set_name` and `udp_dest_port_set_name`
                if set in order to generate valid configuration in EOS.
                """
                protocol_ranges: list[Annotated[str, StrConvert(convert_types=(int))]] | None = None
                """
                Acccept protocol value(s) or range(s).
                Protocol values can be between 1 and 255.
                """
                udp_src_port_set_name: str | None = None
                """
                Name of field set for UDP source ports.

                When the `protocols` list contain both `tcp` and `udp`, this key value
                must be
                the same as `tcp_src_port_set_name`.
                """
                tcp_src_port_set_name: str | None = None
                """
                Name of field set for TCP source ports.

                When the `protocols` list contain both `tcp` and `udp`, this key value
                must be
                the same as `udp_src_port_set_name`.
                """
                udp_dest_port_set_name: str | None = None
                """
                Name of field set for UDP destination ports.

                When the `protocols` list contain both `tcp` and `udp`, this key value
                must be the same as `tcp_dest_port_set_name`.
                """
                tcp_dest_port_set_name: str | None = None
                """
                Name of field set for TCP destination ports.

                When the `protocols` list contain both `tcp` and `udp`, this key value
                must be the same as `udp_dest_port_set_name`.
                """

            ipv4_applications: list[Ipv4ApplicationsItem] | None = None
            """
            List of user defined IPv4 applications.
            """

        class ApplicationProfilesItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class ApplicationsItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                name: str | None = None
                """
                Application Name.
                """
                service: Literal["audio-video", "chat", "default", "file-transfer", "networking-protocols", "peer-to-peer", "software-update"] | None = None
                """
                Service Name.
                Specific service to target for this application.
                If no service is specified, all supported services of the
                application are matched.
                Not all valid values are valid for all applications, check on EOS CLI.
                """

            class CategoriesItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                name: str | None = None
                """
                Name of a category.
                """
                service: Literal["audio-video", "chat", "default", "file-transfer", "networking-protocols", "peer-to-peer", "software-update"] | None = None
                """
                Service Name.
                Specific service to target for this application.
                If no service is specified, all supported services of the
                application are matched.
                Not all valid values are valid for all applications, check on EOS CLI.
                """

            name: str | None = None
            """
            Application Profile name.
            """
            applications: list[ApplicationsItem] | None = None
            """
            List of applications part of the application profile.
            """
            application_transports: list[str] | None = None
            """
            List of transport protocols.
            """
            categories: list[CategoriesItem] | None = None
            """
            Categories under this application profile.
            """

        categories: list[CategoriesItem] | None = None
        """
        List of categories.
        """
        field_sets: FieldSets | None = None
        applications: Applications | None = None
        application_profiles: list[ApplicationProfilesItem] | None = None
        """
        Group of applications.
        """

    class Arp(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Aging(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            timeout_default: int | None = Field(None, ge=60, le=65535)
            """
            Timeout in seconds
            """

        class StaticEntriesItem(AvdDictBaseModel):
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

    class AsPath(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class AccessListsItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class EntriesItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                type: Literal["permit", "deny"] | None = None
                match: str | None = None
                """
                Regex To Match
                """
                origin: Literal["any", "egp", "igp", "incomplete"] | None = "any"

            name: str | None = None
            """
            Access List Name
            """
            entries: list[EntriesItem] | None = None

        regex_mode: Literal["asn", "string"] | None = None
        access_lists: list[AccessListsItem] | None = None

    class Banners(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        login: str | None = None
        """
        Multiline string ending with EOF on the last line
        """
        motd: str | None = None
        """
        Multiline string ending with EOF on the last line
        """

    class BgpGroupsItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        name: str = None
        """
        Group Name
        """
        vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
        neighbors: list[str] | None = None
        bgp_maintenance_profiles: list[str] | None = None

    class Boot(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Secret(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            hash_algorithm: Literal["md5", "sha512"] | None = "sha512"
            key: str | None = None
            """
            Hashed Password
            """

        secret: Secret | None = None

    class ClassMaps(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class PbrItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Ip(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                access_group: Annotated[str, StrConvert(convert_types=(int))] | None = None
                """
                Standard Access-List Name
                """

            name: str = None
            """
            Class-Map Name
            """
            ip: Ip | None = None

        class QosItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Ip(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                access_group: Annotated[str, StrConvert(convert_types=(int))] | None = None
                """
                IPv4 Access-List Name
                """

            class Ipv6(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                access_group: Annotated[str, StrConvert(convert_types=(int))] | None = None
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

    class Clock(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        timezone: str | None = None

    class CommunityListsItem(AvdDictBaseModel):
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

    class Cvx(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Services(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Mcs(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Redis(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    password: str | None = None
                    """
                    Hashed password using the password_type
                    """
                    password_type: Annotated[Literal["0", "7", "8a"], StrConvert(convert_types=(int))] | None = "7"

                redis: Redis | None = None
                shutdown: bool | None = None

            class Vxlan(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                shutdown: bool | None = None
                vtep_mac_learning: Literal["control-plane", "data-plane"] | None = None

            mcs: Mcs | None = None
            vxlan: Vxlan | None = None
            """
            VXLAN Controller service
            """

        shutdown: bool | None = None
        peer_hosts: list[str] | None = None
        services: Services | None = None

    class DaemonTerminattr(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class ClustersItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Cvauth(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                method: Literal["token", "token-secure", "key", "certs"] | None = None
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
            Set source interface in case of in-band managament. Available as of TerminAttr v1.23.0.
            The interface name is case
            sensitive and has to match the interface name in the running-config, e.g.:Vlan100.
            """
            cvvrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
            """
            The VRF to use to connect to CloudVision
            """

        class Cvauth(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            method: Literal["token", "token-secure", "key", "certs"] | None = None
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
        Set source interface in case of in-band managament.
        The interface name is case sensitive and has to match the interface
        name in the running-config, e.g.:Vlan100.
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

    class DaemonsItem(AvdDictBaseModel):
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

    class DhcpRelay(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        servers: list[str] | None = None
        tunnel_requests_disabled: bool | None = None
        mlag_peerlink_requests_disabled: bool | None = None

    class DhcpServersItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Ipv4VendorOptionsItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class SubOptionsItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                code: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=1, le=254)
                string: str | None = None
                """
                String value for suboption data.
                Only one of `string`, `ipv4_address` and `array_ipv4_address` variables should be used
                for any one suboption.
                The order of precedence if multiple of these variables are defined is `string` -> `ipv4_address`
                -> `array_ipv4_address`.
                """
                ipv4_address: str | None = None
                """
                IPv4 address value for suboption data.
                Only one of `string`, `ipv4_address` and `array_ipv4_address` variables should be
                used for any one suboption.
                The order of precedence if multiple of these variables are defined is `string` ->
                `ipv4_address` -> `array_ipv4_address`.
                """
                array_ipv4_address: list[str] | None = None
                """
                Array of IPv4 addresses for suboption data.
                Only one of `string`, `ipv4_address` and `array_ipv4_address` variables
                should be used for any one suboption.
                The order of precedence if multiple of these variables are defined is `string` ->
                `ipv4_address` -> `array_ipv4_address`.
                """

            vendor_id: Annotated[str, StrConvert(convert_types=(int))] = None
            sub_options: list[SubOptionsItem] | None = None

        class SubnetsItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class RangesItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                start: str = None
                end: str = None

            class LeaseTime(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                days: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=0, le=2000)
                hours: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=0, le=23)
                minutes: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=0, le=59)

            subnet: str = None
            name: Annotated[str, StrConvert(convert_types=(int))] | None = None
            default_gateway: str | None = None
            dns_servers: list[str] | None = None
            ranges: list[RangesItem] | None = None
            lease_time: LeaseTime | None = None

        disabled: bool | None = None
        vrf: Annotated[str, StrConvert(convert_types=(int))] = None
        """
        VRF in which to configure the DHCP server, use `default` to indicate default VRF.
        """
        dns_domain_name_ipv4: str | None = None
        dns_domain_name_ipv6: str | None = None
        ipv4_vendor_options: list[Ipv4VendorOptionsItem] | None = None
        subnets: list[SubnetsItem] | None = None

    class Dot1x(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class MacBasedAuthentication(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            delay: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=300)
            hold_period: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=300)

        class RadiusAvPair(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            service_type: bool | None = None
            framed_mtu: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=68, le=9236)

        system_auth_control: bool | None = None
        protocol_lldp_bypass: bool | None = None
        protocol_bpdu_bypass: bool | None = None
        dynamic_authorization: bool | None = None
        mac_based_authentication: MacBasedAuthentication | None = None
        radius_av_pair: RadiusAvPair | None = None

    class DpsInterfacesItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class FlowTracker(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            sampled: str | None = None
            """
            Sampled flow tracker name.
            """
            hardware: str | None = None
            """
            Hardware flow tracker name,
            """

        class TcpMssCeiling(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            ipv4: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=64, le=65495)
            """
            Segment Size for IPv4.
            """
            ipv6: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=64, le=65475)
            """
            Segment Size for IPv6.
            """
            direction: Literal["ingress", "egress"] | None = None
            """
            Optional direction ('ingress', 'egress')  for tcp mss ceiling.
            """

        name: Literal["Dps1"] = None
        """
        "Dps1" is currently the only supported interface.
        """
        description: str | None = None
        shutdown: bool | None = None
        mtu: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=68, le=65535)
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

    class DynamicPrefixListsItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class PrefixList(AvdDictBaseModel):
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

    class EnablePassword(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        hash_algorithm: Literal["md5", "sha512"] | None = None
        key: str | None = None
        """
        Must be the hash of the password using the specified algorithm.
        By default EOS salts the password, so the simplest is to
        generate the hash on an EOS device.
        """

    class EosCliConfigGenConfiguration(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        hide_passwords: bool | None = False
        """
        Replace the input data using the `hide_passwords` filter in the Jinja2 templates by '<removed>' in the configruation if
        true
        """

    class EosCliConfigGenDocumentation(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        hide_passwords: bool | None = True
        """
        Replace the input data using the `hide_passwords` filter in the Jinja2 templates by '<removed>' in the documentation if
        true
        """

    class Errdisable(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Detect(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            causes: list[str] | None = None

        class Recovery(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            causes: list[str] | None = None
            interval: Annotated[int, IntConvert(convert_types=(str))] | None = Field(300, ge=30, le=86400)
            """
            Interval in seconds
            """

        detect: Detect | None = None
        recovery: Recovery | None = None

    class EthernetInterfacesItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Phone(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            trunk: Literal["tagged", "tagged phone", "untagged", "untagged phone"] | None = None
            vlan: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=4094)

        class L2Protocol(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            encapsulation_dot1q_vlan: Annotated[int, IntConvert(convert_types=(str))] | None = None
            """
            Vlan tag to configure on sub-interface
            """
            forwarding_profile: str | None = None
            """
            L2 protocol forwarding profile
            """

        class AddressLocking(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            ipv4: bool | None = None
            """
            Enable address locking for IPv4
            """
            ipv6: bool | None = None
            """
            Enable address locking for IPv6
            """

        class Flowcontrol(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            received: Literal["desired", "on", "off"] | None = None

        class FlowTracker(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            sampled: str | None = None
            """
            Sampled flow tracker name.
            """
            hardware: str | None = None
            """
            Hardware flow tracker name.
            """

        class ErrorCorrectionEncoding(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            enabled: bool | None = True
            fire_code: bool | None = None
            reed_solomon: bool | None = None

        class LinkTrackingGroupsItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str = None
            """
            Group name
            """
            direction: Literal["upstream", "downstream"] | None = None

        class EvpnEthernetSegment(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class DesignatedForwarderElection(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                algorithm: Literal["modulus", "preference"] | None = None
                preference_value: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=65535)
                """
                Preference_value is only used when "algorithm" is "preference"
                """
                dont_preempt: bool | None = None
                """
                Dont_preempt is only used when "algorithm" is "preference"
                """
                hold_time: Annotated[int, IntConvert(convert_types=(str))] | None = None
                subsequent_hold_time: Annotated[int, IntConvert(convert_types=(str))] | None = None
                candidate_reachability_required: bool | None = None

            class Mpls(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                shared_index: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=1024)
                tunnel_flood_filter_time: Annotated[int, IntConvert(convert_types=(str))] | None = None

            identifier: str | None = None
            """
            EVPN Ethernet Segment Identifier (Type 1 format)
            """
            redundancy: Literal["all-active", "single-active"] | None = None
            designated_forwarder_election: DesignatedForwarderElection | None = None
            mpls: Mpls | None = None
            route_target: str | None = None
            """
            EVPN Route Target for ESI with format xx:xx:xx:xx:xx:xx
            """

        class EncapsulationVlan(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Client(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Dot1q(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    vlan: Annotated[int, IntConvert(convert_types=(str))] | None = None
                    """
                    Client VLAN ID
                    """
                    outer: Annotated[int, IntConvert(convert_types=(str))] | None = None
                    """
                    Client Outer VLAN ID
                    """
                    inner: Annotated[int, IntConvert(convert_types=(str))] | None = None
                    """
                    Client Inner VLAN ID
                    """

                dot1q: Dot1q | None = None
                unmatched: bool | None = None

            class Network(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Dot1q(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    vlan: Annotated[int, IntConvert(convert_types=(str))] | None = None
                    """
                    Network VLAN ID
                    """
                    outer: Annotated[int, IntConvert(convert_types=(str))] | None = None
                    """
                    Network outer VLAN ID
                    """
                    inner: Annotated[int, IntConvert(convert_types=(str))] | None = None
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

        class IpHelpersItem(AvdDictBaseModel):
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

        class IpNat(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Destination(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class DynamicItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    access_list: str = None
                    comment: str | None = None
                    pool_name: str = None
                    priority: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=4294967295)

                class StaticItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    access_list: str | None = None
                    """
                    'access_list' and 'group' are mutual exclusive
                    """
                    comment: str | None = None
                    direction: Literal["egress", "ingress"] | None = None
                    """
                    Egress or ingress can be the default. This depends on source/destination, EOS version, and hardware platform.
                    EOS might
                    remove this keyword in the configuration. So, check the configuration on targeted HW/SW.
                    """
                    group: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)
                    """
                    'access_list' and 'group' are mutual exclusive
                    """
                    original_ip: str = None
                    """
                    IPv4 address
                    """
                    original_port: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)
                    priority: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=4294967295)
                    protocol: Literal["udp", "tcp"] | None = None
                    translated_ip: str = None
                    """
                    IPv4 address
                    """
                    translated_port: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)
                    """
                    requires 'original_port'
                    """

                dynamic: list[DynamicItem] | None = None
                static: list[StaticItem] | None = None

            class Source(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class DynamicItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    access_list: str = None
                    comment: str | None = None
                    nat_type: Literal["overload", "pool", "pool-address-only", "pool-full-cone"] = None
                    pool_name: str | None = None
                    """
                    required if 'nat_type' is pool, pool-address-only or pool-full-cone
                    ignored if 'nat_type' is overload
                    """
                    priority: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=4294967295)

                class StaticItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    access_list: str | None = None
                    """
                    'access_list' and 'group' are mutual exclusive
                    """
                    comment: str | None = None
                    direction: Literal["egress", "ingress"] | None = None
                    """
                    Egress or ingress can be the default. This depends on source/destination, EOS version, and hardware platform.
                    EOS might
                    remove this keyword in the configuration. So, check the configuration on targeted HW/SW.
                    """
                    group: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)
                    """
                    'access_list' and 'group' are mutual exclusive
                    """
                    original_ip: str = None
                    """
                    IPv4 address
                    """
                    original_port: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)
                    priority: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=4294967295)
                    protocol: Literal["udp", "tcp"] | None = None
                    translated_ip: str = None
                    """
                    IPv4 address
                    """
                    translated_port: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)
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

        class Ipv6NdPrefixesItem(AvdDictBaseModel):
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

        class Ipv6DhcpRelayDestinationsItem(AvdDictBaseModel):
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

        class Multicast(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Ipv4(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class BoundariesItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    boundary: str | None = None
                    """
                    ACL name or multicast IP subnet
                    """
                    out: bool | None = None

                boundaries: list[BoundariesItem] | None = None
                static: bool | None = None

            class Ipv6(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class BoundariesItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    boundary: str | None = None
                    """
                    ACL name or multicast IP subnet
                    """

                boundaries: list[BoundariesItem] | None = None
                static: bool | None = None

            ipv4: Ipv4 | None = None
            ipv6: Ipv6 | None = None

        class OspfMessageDigestKeysItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            id: Annotated[int, IntConvert(convert_types=(str))] = None
            hash_algorithm: Literal["md5", "sha1", "sha256", "sha384", "sha512"] | None = None
            key: str | None = None
            """
            Encrypted password - only type 7 supported
            """

        class Pim(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Ipv4(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Hello(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    count: Annotated[str, StrConvert(convert_types=(int, float))] | None = None
                    """
                    Number of missed hellos after which the neighbor expires. Range <1.5-65535>.
                    """
                    interval: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)
                    """
                    PIM hello interval in seconds.
                    """

                border_router: bool | None = None
                """
                Configure PIM border router. EOS default is false.
                """
                dr_priority: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=429467295)
                sparse_mode: bool | None = None
                bfd: bool | None = None
                """
                Set the default for whether Bidirectional Forwarding Detection is enabled for PIM.
                """
                bidirectional: bool | None = None
                hello: Hello | None = None

            ipv4: Ipv4 | None = None

        class MacSecurity(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            profile: str | None = None

        class ChannelGroup(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            id: Annotated[int, IntConvert(convert_types=(str))] | None = None
            mode: Literal["on", "active", "passive"] | None = None

        class Poe(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Reboot(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                action: Literal["maintain", "power-off"] | None = None
                """
                PoE action for interface
                """

            class LinkDown(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                action: Literal["maintain", "power-off"] | None = None
                """
                PoE action for interface
                """
                power_off_delay: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=86400)
                """
                Number of seconds to delay shutting the power off after a link down event occurs. Default value is 5 seconds in EOS.
                """

            class Shutdown(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                action: Literal["maintain", "power-off"] | None = None
                """
                PoE action for interface
                """

            class Limit(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                field_class: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, alias="class", ge=0, le=8)
                watts: Annotated[str, StrConvert(convert_types=(int, float))] | None = None
                fixed: bool | None = None
                """
                Set to ignore hardware classification
                """

            disabled: bool | None = False
            """
            Disable PoE on a POE capable port. PoE is enabled on all ports that support it by default in EOS.
            """
            priority: Literal["critical", "high", "medium", "low"] | None = None
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

        class Ptp(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Announce(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                interval: Annotated[int, IntConvert(convert_types=(str))] | None = None
                timeout: Annotated[int, IntConvert(convert_types=(str))] | None = None

            class SyncMessage(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                interval: Annotated[int, IntConvert(convert_types=(str))] | None = None

            enable: bool | None = None
            announce: Announce | None = None
            delay_req: Annotated[int, IntConvert(convert_types=(str))] | None = None
            delay_mechanism: Literal["e2e", "p2p"] | None = None
            sync_message: SyncMessage | None = None
            role: Literal["master", "dynamic"] | None = None
            vlan: Annotated[str, StrConvert(convert_types=(int))] | None = None
            """
            VLAN can be 'all' or list of vlans as string
            """
            transport: Literal["ipv4", "ipv6", "layer2"] | None = None

        class StormControl(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class All(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                level: Annotated[str, StrConvert(convert_types=(int, float))] | None = None
                """
                Configure maximum storm-control level
                """
                unit: Literal["percent", "pps"] | None = "percent"
                """
                Optional field and is hardware dependent
                """

            class Broadcast(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                level: Annotated[str, StrConvert(convert_types=(int, float))] | None = None
                """
                Configure maximum storm-control level
                """
                unit: Literal["percent", "pps"] | None = "percent"
                """
                Optional field and is hardware dependent
                """

            class Multicast(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                level: Annotated[str, StrConvert(convert_types=(int, float))] | None = None
                """
                Configure maximum storm-control level
                """
                unit: Literal["percent", "pps"] | None = "percent"
                """
                Optional field and is hardware dependent
                """

            class UnknownUnicast(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                level: Annotated[str, StrConvert(convert_types=(int, float))] | None = None
                """
                Configure maximum storm-control level
                """
                unit: Literal["percent", "pps"] | None = "percent"
                """
                Optional field and is hardware dependent
                """

            all: All | None = None
            broadcast: Broadcast | None = None
            multicast: Multicast | None = None
            unknown_unicast: UnknownUnicast | None = None

        class Logging(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Event(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                link_status: bool | None = None
                congestion_drops: bool | None = None
                spanning_tree: bool | None = None
                storm_control_discards: bool | None = None
                """
                Discards due to storm-control.
                """

            event: Event | None = None

        class Lldp(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            transmit: bool | None = None
            receive: bool | None = None
            ztp_vlan: Annotated[int, IntConvert(convert_types=(str))] | None = None
            """
            ZTP vlan number
            """

        class VlanTranslationsItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            field_from: Annotated[str, StrConvert(convert_types=(int))] | None = Field(None, alias="from")
            """
            List of vlans as string (only one vlan if direction is "both")
            """
            to: Annotated[int, IntConvert(convert_types=(str))] | None = None
            """
            VLAN ID
            """
            direction: Literal["in", "out", "both"] | None = "both"

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
                Value can be 60-4294967295 or 'server'
                """
                reauth_timeout_ignore: bool | None = None
                tx_period: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)

            class Unauthorized(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                access_vlan_membership_egress: bool | None = None
                native_vlan_membership_egress: bool | None = None

            class Eapol(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class AuthenticationFailureFallbackMba(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    enabled: bool | None = None
                    timeout: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=65535)

                disabled: bool | None = None
                authentication_failure_fallback_mba: AuthenticationFailureFallbackMba | None = None

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
            eapol: Eapol | None = None

        class Shape(AvdDictBaseModel):
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

        class Qos(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            trust: Literal["dscp", "cos", "disabled"] | None = None
            dscp: Annotated[int, IntConvert(convert_types=(str))] | None = None
            """
            DSCP value
            """
            cos: Annotated[int, IntConvert(convert_types=(str))] | None = None
            """
            COS value
            """

        class PriorityFlowControl(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class PrioritiesItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                priority: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=0, le=7)
                no_drop: bool | None = None

            enabled: bool | None = None
            priorities: list[PrioritiesItem] | None = None

        class Bfd(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            echo: bool | None = None
            interval: Annotated[int, IntConvert(convert_types=(str))] | None = None
            """
            Interval in milliseconds
            """
            min_rx: Annotated[int, IntConvert(convert_types=(str))] | None = None
            """
            Rate in milliseconds
            """
            multiplier: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=3, le=50)

        class ServicePolicy(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Pbr(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                input: str | None = None
                """
                Policy Based Routing Policy-map name
                """

            class Qos(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                input: str = None
                """
                Quality of Service Policy-map name
                """

            pbr: Pbr | None = None
            qos: Qos | None = None

        class Mpls(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Ldp(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                interface: bool | None = None
                igp_sync: bool | None = None

            ip: bool | None = None
            ldp: Ldp | None = None

        class LacpTimer(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            mode: Literal["fast", "normal"] | None = None
            multiplier: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=3, le=3000)

        class Transceiver(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Media(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                override: str | None = None
                """
                Transceiver type
                """

            media: Media | None = None

        class TrafficPolicy(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            input: str | None = None
            """
            Ingress traffic policy
            """
            output: str | None = None
            """
            Egress traffic policy
            """

        class Bgp(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            session_tracker: str | None = None
            """
            Name of session tracker
            """

        class IpIgmpHostProxy(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class GroupsItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class ExcludeItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    source: str = None

                class IncludeItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    source: str = None

                group: str = None
                """
                Multicast Address.
                """
                exclude: list[ExcludeItem] | None = None
                """
                The same source must not be present both in `exclude` and `include` list.
                """
                include: list[IncludeItem] | None = None
                """
                The same source must not be present both in `exclude` and `include` list.
                """

            class AccessListsItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                name: str = None

            enabled: bool | None = None
            groups: list[GroupsItem] | None = None
            report_interval: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=31744)
            """
            Time interval between unsolicited reports.
            """
            access_lists: list[AccessListsItem] | None = None
            """
            Non-standard Access List name.
            """
            version: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=3)
            """
            IGMP version on IGMP host-proxy interface.
            """

        class Sflow(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Egress(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                enable: bool | None = None
                unmodified_enable: bool | None = None

            enable: bool | None = None
            egress: Egress | None = None

        class UcTxQueuesItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class RandomDetect(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Ecn(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class Threshold(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        units: Literal["segments", "bytes", "kbytes", "mbytes", "milliseconds"] = None
                        """
                        Indicate the units to be used for the threshold values
                        """
                        min: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=1, le=256000000)
                        """
                        Set the random-detect ECN minimum-threshold
                        """
                        max: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=1, le=256000000)
                        """
                        Set the random-detect ECN maximum-threshold
                        """
                        max_probability: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=100)
                        """
                        Set the random-detect ECN max-mark-probability
                        """
                        weight: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=15)
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

            id: Annotated[int, IntConvert(convert_types=(str))] = None
            """
            TX-Queue ID
            """
            random_detect: RandomDetect | None = None

        class TxQueuesItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class RandomDetect(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Ecn(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class Threshold(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        units: Literal["segments", "bytes", "kbytes", "mbytes", "milliseconds"] = None
                        """
                        Indicate the units to be used for the threshold values
                        """
                        min: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=256000000)
                        """
                        Set the random-detect ECN minimum-threshold
                        """
                        max: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=1, le=256000000)
                        """
                        Set the random-detect ECN maximum-threshold
                        """
                        max_probability: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=1, le=100)
                        """
                        Set the random-detect ECN max-mark-probability
                        """
                        weight: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=15)
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

            id: Annotated[int, IntConvert(convert_types=(str))] = None
            """
            TX-Queue ID
            """
            random_detect: RandomDetect | None = None

        class VrrpIdsItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Advertisement(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                interval: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=255)
                """
                Interval in seconds
                """

            class Preempt(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Delay(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    minimum: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=3600)
                    """
                    Minimum preempt delay in seconds
                    """
                    reload: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=3600)
                    """
                    Reload preempt delay in seconds
                    """

                enabled: bool = None
                delay: Delay | None = None

            class Timers(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Delay(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    reload: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=3600)
                    """
                    Delay after reload in seconds.
                    """

                delay: Delay | None = None

            class TrackedObjectItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                name: str = None
                """
                Tracked object name
                """
                decrement: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=254)
                """
                Decrement VRRP priority by 1-254
                """
                shutdown: bool | None = None

            class Ipv4(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                address: str = None
                """
                Virtual IPv4 address
                """
                version: Annotated[Literal[2, 3], IntConvert(convert_types=(str))] | None = None

            class Ipv6(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                address: str = None
                """
                Virtual IPv6 address
                """

            id: Annotated[int, IntConvert(convert_types=(str))] = None
            """
            VRID
            """
            priority_level: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=254)
            """
            Instance priority
            """
            advertisement: Advertisement | None = None
            preempt: Preempt | None = None
            timers: Timers | None = None
            tracked_object: list[TrackedObjectItem] | None = None
            ipv4: Ipv4 | None = None
            ipv6: Ipv6 | None = None

        class Switchport(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class PortSecurity(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class MacAddressMaximum(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    disabled: bool | None = None
                    """
                    Disable port level check for port security (only in violation 'shutdown' mode).
                    """
                    limit: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=1000)
                    """
                    MAC address limit.
                    """

                class Violation(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    mode: Literal["shutdown", "protect"] | None = None
                    """
                    Configure port security mode.
                    """
                    protect_log: bool | None = None
                    """
                    Log new addresses seen after limit is reached in protect mode.
                    """

                class VlansItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    range: Annotated[str, StrConvert(convert_types=(int))] = None
                    """
                    VLAN ID or range(s) of VLAN IDs, <1-4094>.
                    Example:
                      - 3
                      - 1,3
                      - 1-10
                    """
                    mac_address_maximum: Annotated[int, IntConvert(convert_types=(str))] | None = None

                enabled: bool | None = None
                mac_address_maximum: MacAddressMaximum | None = None
                """
                Maximum number of MAC addresses allowed on the interface.
                """
                violation: Violation | None = None
                """
                Configure violation mode (shutdown or protect), EOS default is 'shutdown'.
                """
                vlan_default_mac_address_maximum: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=1000)
                """
                Default maximum MAC addresses for all VLANs on this interface.
                """
                vlans: list[VlansItem] | None = None

            port_security: PortSecurity | None = None

        name: str = None
        description: str | None = None
        shutdown: bool | None = None
        load_interval: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=600)
        """
        Interval in seconds for updating interface counters"
        """
        speed: str | None = None
        """
        Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`.
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
        vlans: Annotated[str, StrConvert(convert_types=(int))] | None = None
        """
        List of switchport vlans as string
        For a trunk port this would be a range like "1-200,300"
        For an access port this would
        be a single vlan "123"
        """
        native_vlan: Annotated[int, IntConvert(convert_types=(str))] | None = None
        native_vlan_tag: bool | None = None
        """
        If setting both native_vlan and native_vlan_tag, native_vlan_tag takes precedence
        """
        mode: Literal["access", "dot1q-tunnel", "trunk", "trunk phone"] | None = None
        phone: Phone | None = None
        l2_protocol: L2Protocol | None = None
        trunk_groups: list[str] | None = None
        type: Literal["routed", "switched", "l3dot1q", "l2dot1q", "port-channel-member"] | None = None
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
        encapsulation_dot1q_vlan: Annotated[int, IntConvert(convert_types=(str))] | None = None
        """
        VLAN tag to configure on sub-interface
        """
        encapsulation_vlan: EncapsulationVlan | None = None
        vlan_id: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=4094)
        ip_address: str | None = None
        """
        IPv4 address/mask or "dhcp"
        """
        ip_address_secondaries: list[str] | None = None
        ip_verify_unicast_source_reachable_via: Literal["any", "rx"] | None = None
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
        ospf_cost: Annotated[int, IntConvert(convert_types=(str))] | None = None
        ospf_authentication: Literal["none", "simple", "message-digest"] | None = None
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
        isis_metric: Annotated[int, IntConvert(convert_types=(str))] | None = None
        isis_network_point_to_point: bool | None = None
        isis_circuit_type: Literal["level-1-2", "level-1", "level-2"] | None = None
        isis_hello_padding: bool | None = None
        isis_authentication_mode: Literal["text", "md5"] | None = None
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
        spanning_tree_bpdufilter: Annotated[Literal["enabled", "disabled", "True", "False", "true", "false"], StrConvert(convert_types=(bool))] | None = None
        spanning_tree_bpduguard: Annotated[Literal["enabled", "disabled", "True", "False", "true", "false"], StrConvert(convert_types=(bool))] | None = None
        spanning_tree_guard: Literal["loop", "root", "disabled"] | None = None
        spanning_tree_portfast: Literal["edge", "network"] | None = None
        vmtracer: bool | None = None
        priority_flow_control: PriorityFlowControl | None = None
        bfd: Bfd | None = None
        service_policy: ServicePolicy | None = None
        mpls: Mpls | None = None
        lacp_timer: LacpTimer | None = None
        lacp_port_priority: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=65535)
        transceiver: Transceiver | None = None
        ip_proxy_arp: bool | None = None
        traffic_policy: TrafficPolicy | None = None
        bgp: Bgp | None = None
        ip_igmp_host_proxy: IpIgmpHostProxy | None = None
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
        validate_state: bool | None = None
        """
        Set to false to disable interface validation by the `eos_validate_state` role
        """
        switchport: Switchport | None = None
        eos_cli: str | None = None
        """
        Multiline EOS CLI rendered directly on the ethernet interface in the final EOS configuration
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

    class EventMonitor(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        enabled: bool | None = None

    class FlowTracking(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Sampled(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Encapsulation(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                ipv4_ipv6: bool | None = None
                mpls: bool | None = None

            class HardwareOffload(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                ipv4: bool | None = None
                """
                Configure hardware offload for IPv4 traffic.
                """
                ipv6: bool | None = None
                """
                Configure hardware offload for IPv6 traffic.
                """
                threshold_minimum: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=4294967295)
                """
                Minimum number of samples.
                """

            class TrackersItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class RecordExport(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    mpls: bool | None = None
                    """
                    Export MPLS forwarding information.
                    """
                    on_inactive_timeout: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=3000, le=900000)
                    """
                    Flow record inactive export timeout in milliseconds
                    """
                    on_interval: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1000, le=36000000)
                    """
                    Flow record export interval in milliseconds
                    """

                class ExportersItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class Collector(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        host: str | None = None
                        """
                        Collector IPv4 address or IPv6 address or fully qualified domain name
                        """
                        port: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)
                        """
                        Collector Port Number
                        """

                    class Format(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        ipfix_version: Annotated[int, IntConvert(convert_types=(str))] | None = None

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
                    template_interval: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=5000, le=3600000)
                    """
                    Template interval in milliseconds
                    """

                table_size: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=614400)
                """
                Maximum number of entries in flow table.
                """
                record_export: RecordExport | None = None
                name: str = None
                """
                Tracker Name
                """
                exporters: list[ExportersItem] | None = None

            encapsulation: Encapsulation | None = None
            sample: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=4294967295)
            hardware_offload: HardwareOffload | None = None
            trackers: list[TrackersItem] | None = None
            shutdown: bool | None = False

        class Hardware(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Record(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                format_ipfix_standard_timestamps_counters: bool | None = None
                """
                Enable software export of IPFIX data records.
                """

            class TrackersItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class RecordExport(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    on_inactive_timeout: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=3000, le=900000)
                    """
                    Flow record inactive export timeout in milliseconds
                    """
                    on_interval: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1000, le=36000000)
                    """
                    Flow record export interval in milliseconds
                    """

                class ExportersItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class Collector(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        host: str | None = None
                        """
                        Collector IPv4 address or IPv6 address or fully qualified domain name
                        """
                        port: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)
                        """
                        Collector Port Number
                        """

                    class Format(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        ipfix_version: Annotated[int, IntConvert(convert_types=(str))] | None = None

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
                    template_interval: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=5000, le=3600000)
                    """
                    Template interval in milliseconds
                    """

                name: str = None
                """
                Tracker Name
                """
                record_export: RecordExport | None = None
                exporters: list[ExportersItem] | None = None

            record: Record | None = None
            trackers: list[TrackersItem] | None = None
            shutdown: bool | None = False

        sampled: Sampled | None = None
        hardware: Hardware | None = None

    class FlowTrackingsItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class TrackersItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class RecordExport(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                on_inactive_timeout: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=3000, le=900000)
                """
                Flow record inactive export timeout in milliseconds
                """
                on_interval: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1000, le=36000000)
                """
                Flow record export interval in milliseconds
                """
                mpls: bool | None = None
                """
                Export MPLS forwarding information
                """

            class ExportersItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Collector(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    host: str | None = None
                    """
                    Collector IPv4 address or IPv6 address or fully qualified domain name
                    """
                    port: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)
                    """
                    Collector Port Number
                    """

                class Format(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    ipfix_version: Annotated[int, IntConvert(convert_types=(str))] | None = None

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
                template_interval: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=5000, le=3600000)
                """
                Template interval in milliseconds
                """

            name: str = None
            """
            Tracker Name
            """
            record_export: RecordExport | None = None
            exporters: list[ExportersItem] | None = None
            table_size: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=614400)
            """
            Maximum number of entries in flow table.
            """

        type: Literal["sampled"] = None
        """
        Flow Tracking Type - only 'sampled' supported for now
        """
        sample: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=4294967295)
        trackers: list[TrackersItem] | None = None
        shutdown: bool | None = False

    class Hardware(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class AccessList(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            mechanism: Literal["algomatch", "none", "tcam"] | None = None

        class SpeedGroupsItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            speed_group: Annotated[str, StrConvert(convert_types=(int))] = None
            serdes: str | None = None
            """
            Serdes speed like "10g" or "25g"
            """

        access_list: AccessList | None = None
        speed_groups: list[SpeedGroupsItem] | None = None

    class HardwareCounters(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class FeaturesItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: (
                Literal[
                    "acl",
                    "decap-group",
                    "directflow",
                    "ecn",
                    "flow-spec",
                    "gre tunnel interface",
                    "ip",
                    "mpls interface",
                    "mpls lfib",
                    "mpls tunnel",
                    "multicast",
                    "nexthop",
                    "pbr",
                    "pdp",
                    "policing interface",
                    "qos",
                    "qos dual-rate-policer",
                    "route",
                    "routed-port",
                    "subinterface",
                    "tapagg",
                    "traffic-class",
                    "traffic-policy",
                    "vlan",
                    "vlan-interface",
                    "vni decap",
                    "vni encap",
                    "vtep decap",
                    "vtep encap",
                ]
                | None
            ) = None
            direction: Literal["in", "out", "cpu"] | None = None
            """
            Most features support only 'in' and 'out'. Some like traffic-policy support 'cpu'.
            Some features DO NOT have any
            direction.
            This validation IS NOT made by the schemas.
            """
            address_type: Literal["ipv4", "ipv6", "mac"] | None = None
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

    class InterfaceDefaults(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Ethernet(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            shutdown: bool | None = None

        ethernet: Ethernet | None = None
        mtu: Annotated[int, IntConvert(convert_types=(str))] | None = None

    class InterfaceGroupsItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        name: str = None
        """
        Interface-Group name
        """
        interfaces: list[str] | None = None
        bgp_maintenance_profiles: list[str] | None = None
        interface_maintenance_profiles: list[str] | None = None

    class InterfaceProfilesItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        name: str = None
        """
        Interface-Profile Name
        """
        commands: list[str] = None

    class IpAccessListsItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class EntriesItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

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
            source: str | None = None
            """
            "any", "<ip>/<mask>" or "<ip>".
            "<ip>" without a mask means host.
            Required except for remarks.
            """
            source_ports_match: Literal["eq", "gt", "lt", "neq", "range"] | None = "eq"
            source_ports: list[Annotated[str, StrConvert(convert_types=(int))]] | None = None
            destination: str | None = None
            """
            "any", "<ip>/<mask>" or "<ip>".
            "<ip>" without a mask means host.
            Required except for remarks.
            """
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
        Access-list Name.
        """
        counters_per_entry: bool | None = None
        entries: list[EntriesItem] | None = None
        """
        ACL Entries.
        """

    class IpCommunityListsItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class EntriesItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            action: Literal["permit", "deny"] = None
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

    class IpDhcpRelay(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        information_option: bool | None = None
        """
        Insert Option-82 information
        """

    class IpDhcpSnooping(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class InformationOption(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            enabled: bool | None = None
            """
            Enable insertion of option-82 in DHCP request packets
            """
            circuit_id_type: Annotated[str, StrConvert(convert_types=(int))] | None = None
            """
            "none" or <0 - 255>
            """
            circuit_id_format: Literal["%h:%p", "%p:%v"] | None = None
            """
            Required if `circuit_id_type` is set.
            - "%h:%p" Hostname and interface name
            - "%p:%v" Interface name and VLAN ID
            """

        enabled: bool | None = None
        bridging: bool | None = None
        information_option: InformationOption | None = None
        vlan: Annotated[str, StrConvert(convert_types=(int))] | None = None
        """
        VLAN range as string.
        "< vlan_id >, < vlan_id >-< vlan_id >"
        Example: 15,16,17,18
        """

    class IpDomainLookup(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class SourceInterfacesItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str = None
            """
            Source Interface
            """
            vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None

        source_interfaces: list[SourceInterfacesItem] | None = None

    class IpExtcommunityListsItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class EntriesItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            type: Literal["permit", "deny"] = None
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

    class IpExtcommunityListsRegexpItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class EntriesItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            type: Literal["permit", "deny"] = None
            regexp: str = None
            """
            Regular Expression
            """

        name: str = None
        """
        Community-list Name
        """
        entries: list[EntriesItem] = None

    class IpFtpClientSourceInterfacesItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        name: str = None
        """
        Interface Name
        """
        vrf: str | None = None
        """
        VRF Name
        """

    class IpHardware(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Fib(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Optimize(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Prefixes(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    profile: Literal["internet", "urpf-internet"] | None = None

                prefixes: Prefixes | None = None

            optimize: Optimize | None = None

        fib: Fib | None = None

    class IpHttpClientSourceInterfacesItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        name: str | None = None
        """
        Interface Name
        """
        vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None

    class IpIgmpSnooping(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Querier(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            enabled: bool | None = None
            address: str | None = None
            """
            IP Address
            """
            query_interval: Annotated[int, IntConvert(convert_types=(str))] | None = None
            max_response_time: Annotated[int, IntConvert(convert_types=(str))] | None = None
            last_member_query_interval: Annotated[int, IntConvert(convert_types=(str))] | None = None
            last_member_query_count: Annotated[int, IntConvert(convert_types=(str))] | None = None
            startup_query_interval: Annotated[int, IntConvert(convert_types=(str))] | None = None
            startup_query_count: Annotated[int, IntConvert(convert_types=(str))] | None = None
            version: Annotated[int, IntConvert(convert_types=(str))] | None = None

        class VlansItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Querier(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                enabled: bool | None = None
                address: str | None = None
                """
                IP Address
                """
                query_interval: Annotated[int, IntConvert(convert_types=(str))] | None = None
                max_response_time: Annotated[int, IntConvert(convert_types=(str))] | None = None
                last_member_query_interval: Annotated[int, IntConvert(convert_types=(str))] | None = None
                last_member_query_count: Annotated[int, IntConvert(convert_types=(str))] | None = None
                startup_query_interval: Annotated[int, IntConvert(convert_types=(str))] | None = None
                startup_query_count: Annotated[int, IntConvert(convert_types=(str))] | None = None
                version: Annotated[int, IntConvert(convert_types=(str))] | None = None

            id: Annotated[int, IntConvert(convert_types=(str))] = None
            """
            VLAN ID
            """
            enabled: bool | None = None
            querier: Querier | None = None
            max_groups: Annotated[int, IntConvert(convert_types=(str))] | None = None
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
        robustness_variable: Annotated[int, IntConvert(convert_types=(str))] | None = None
        restart_query_interval: Annotated[int, IntConvert(convert_types=(str))] | None = None
        interface_restart_query: Annotated[int, IntConvert(convert_types=(str))] | None = None
        fast_leave: bool | None = None
        querier: Querier | None = None
        proxy: bool | None = None
        vlans: list[VlansItem] | None = None

    class IpNameServersItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        ip_address: str | None = None
        """
        IPv4 or IPv6 address for DNS server
        """
        vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
        """
        VRF Name
        """
        priority: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=4)
        """
        Priority value (lower is first)
        """

    class IpNat(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class ProfilesItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Destination(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class DynamicItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    access_list: str = None
                    comment: str | None = None
                    pool_name: str = None
                    priority: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=4294967295)

                class StaticItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    access_list: str | None = None
                    """
                    'access_list' and 'group' are mutual exclusive
                    """
                    comment: str | None = None
                    direction: Literal["egress", "ingress"] | None = None
                    """
                    Egress or ingress can be the default. This depends on source/destination, EOS version, and hardware platform.
                    EOS might
                    remove this keyword in the configuration. So, check the configuration on targeted HW/SW.
                    """
                    group: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)
                    """
                    'access_list' and 'group' are mutual exclusive
                    """
                    original_ip: str = None
                    """
                    IPv4 address
                    """
                    original_port: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)
                    priority: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=4294967295)
                    protocol: Literal["udp", "tcp"] | None = None
                    translated_ip: str = None
                    """
                    IPv4 address
                    """
                    translated_port: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)
                    """
                    requires 'original_port'
                    """

                dynamic: list[DynamicItem] | None = None
                static: list[StaticItem] | None = None

            class Source(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class DynamicItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    access_list: str = None
                    comment: str | None = None
                    nat_type: Literal["overload", "pool", "pool-address-only", "pool-full-cone"] = None
                    pool_name: str | None = None
                    """
                    required if 'nat_type' is pool, pool-address-only or pool-full-cone
                    ignored if 'nat_type' is overload
                    """
                    priority: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=4294967295)

                class StaticItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    access_list: str | None = None
                    """
                    'access_list' and 'group' are mutual exclusive
                    """
                    comment: str | None = None
                    direction: Literal["egress", "ingress"] | None = None
                    """
                    Egress or ingress can be the default. This depends on source/destination, EOS version, and hardware platform.
                    EOS might
                    remove this keyword in the configuration. So, check the configuration on targeted HW/SW.
                    """
                    group: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)
                    """
                    'access_list' and 'group' are mutual exclusive
                    """
                    original_ip: str = None
                    """
                    IPv4 address
                    """
                    original_port: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)
                    priority: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=4294967295)
                    protocol: Literal["udp", "tcp"] | None = None
                    translated_ip: str = None
                    """
                    IPv4 address
                    """
                    translated_port: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)
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

        class PoolsItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class RangesItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                first_ip: str = None
                """
                IPv4 address
                """
                last_ip: str = None
                """
                IPv4 address
                """
                first_port: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)
                last_port: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)

            name: str = None
            prefix_length: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=16, le=32)
            ranges: list[RangesItem] | None = None
            utilization_log_threshold: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=100)

        class Synchronization(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class PortRange(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                first_port: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1024, le=65535)
                last_port: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1024, le=65535)
                """
                >= first_port
                """
                split_disabled: bool | None = None

            description: str | None = None
            expiry_interval: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=60, le=3600)
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

        class Translation(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class AddressSelection(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                any: bool | None = None
                hash_field_source_ip: bool | None = None

            class LowMark(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                percentage: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=99)
                """
                Used to render 'ip nat translation low-mark <percentage>'
                """
                host_percentage: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=99)
                """
                Used to render 'ip nat translation low-mark <host_percentage> host'
                """

            class MaxEntries(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class IpLimitsItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    ip: str = None
                    """
                    IPv4 address
                    """
                    limit: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=0, le=4294967295)

                limit: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=4294967295)
                host_limit: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=4294967295)
                ip_limits: list[IpLimitsItem] | None = None

            class TimeoutsItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                protocol: Literal["tcp", "udp"] = None
                timeout: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=0, le=4294967295)
                """
                in seconds
                """

            address_selection: AddressSelection | None = None
            counters: bool | None = None
            low_mark: LowMark | None = None
            max_entries: MaxEntries | None = None
            timeouts: list[TimeoutsItem] | None = None

        kernel_buffer_size: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=64)
        """
        Buffer size in MB
        """
        profiles: list[ProfilesItem] | None = None
        pools: list[PoolsItem] | None = None
        synchronization: Synchronization | None = None
        translation: Translation | None = None

    class IpRadiusSourceInterfacesItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        name: str | None = None
        """
        Interface Name
        """
        vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
        """
        VRF Name
        """

    class IpSecurity(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class IkePoliciesItem(AvdDictBaseModel):
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
            ike_lifetime: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=24)
            """
            IKE lifetime in hours.
            """
            encryption: Literal["3des", "aes128", "aes256"] | None = None
            """
            IKE encryption algorithm.
            """
            dh_group: Annotated[Literal[1, 2, 5, 14, 15, 16, 17, 20, 21, 24], IntConvert(convert_types=(str))] | None = None
            """
            Diffie-Hellman group for the key exchange.
            """

        class SaPoliciesItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Esp(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                integrity: Literal["disabled", "sha1", "sha256", "null"] | None = None
                encryption: Literal["disabled", "aes128", "aes128gcm128", "aes128gcm64", "aes256", "aes256gcm128", "null"] | None = None

            name: str = None
            """
            Name of the SA policy. The "null" value is deprecated and will be removed in AVD 5.0.0
            """
            esp: Esp | None = None
            pfs_dh_group: Annotated[Literal[1, 2, 5, 14, 15, 16, 17, 20, 21, 24], IntConvert(convert_types=(str))] | None = None

        class ProfilesItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Dpd(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                interval: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=2, le=3600)
                """
                Interval (in seconds) between keep-alive messages.
                """
                time: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=10, le=3600)
                """
                Time (in seconds) after which the action is applied.
                """
                action: Literal["clear", "hold", "restart"] = None
                """
                Action to apply

                * 'clear': Delete all connections
                * 'hold': Re-negotiate connection on demand
                * 'restart': Restart
                connection immediately
                """

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
            connection: Literal["add", "start", "route"] | None = None
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
            mode: Literal["transport", "tunnel"] | None = None
            """
            Ipsec mode type.
            """
            flow_parallelization_encapsulation_udp: bool | None = None
            """
            Enable flow parallelization.
            When enabled, multiple cores are used to parallelize the IPsec encryption and decryption
            processing.
            """

        class KeyController(AvdDictBaseModel):
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
        hardware_encryption_disabled: bool | None = False
        """
        Disable hardware encryption.
        An SFE restart is needed for this change to take effect.
        """

    class IpSshClientSourceInterfacesItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        name: str | None = None
        """
        Interface Name
        """
        vrf: Annotated[str, StrConvert(convert_types=(int))] | None = "default"

    class IpTacacsSourceInterfacesItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        name: str | None = None
        """
        Interface name
        """
        vrf: Annotated[str, StrConvert(convert_types=(int))] | None = Field(None, title="VRF")

    class IpTelnetClientSourceInterfacesItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        name: str = None
        """
        Interface Name
        """
        vrf: str | None = None
        """
        VRF Name
        """

    class IpTftpClientSourceInterfacesItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        name: str = None
        """
        Interface Name
        """
        vrf: str | None = None
        """
        VRF Name
        """

    class Ipv6AccessListsItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class SequenceNumbersItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            sequence: Annotated[int, IntConvert(convert_types=(str))] = None
            """
            Sequence ID
            """
            action: str = None
            """
            Action as string
            Example: "deny ipv6 any any"
            """

        name: Annotated[str, StrConvert(convert_types=(int))] = None
        """
        IPv6 Access-list Name
        """
        counters_per_entry: bool | None = None
        sequence_numbers: list[SequenceNumbersItem] = None

    class Ipv6Hardware(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Fib(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Optimize(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Prefixes(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    profile: str | None = None
                    """
                    Pre-defined profile 'internet' or user-defined profile name
                    """

                prefixes: Prefixes | None = None

            optimize: Optimize | None = None

        fib: Fib | None = None

    class Ipv6PrefixListsItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class SequenceNumbersItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            sequence: Annotated[int, IntConvert(convert_types=(str))] = None
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

    class Ipv6StandardAccessListsItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class SequenceNumbersItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            sequence: Annotated[int, IntConvert(convert_types=(str))] = None
            """
            Sequence ID
            """
            action: str = None
            """
            Action as string
            Example: "deny ipv6 any any"
            """

        name: Annotated[str, StrConvert(convert_types=(int))] = None
        """
        Access-list Name
        """
        counters_per_entry: bool | None = None
        sequence_numbers: list[SequenceNumbersItem] = None

    class Ipv6StaticRoutesItem(AvdDictBaseModel):
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
        distance: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=255)
        tag: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=4294967295)
        name: str | None = None
        """
        Description
        """
        metric: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=4294967295)

    class L2Protocol(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class ForwardingProfilesItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class ProtocolsItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                name: Literal["bfd per-link rfc-7130", "e-lmi", "isis", "lacp", "lldp", "macsec", "pause", "stp"] = None
                forward: bool | None = None
                tagged_forward: bool | None = None
                untagged_forward: bool | None = None

            name: str = None
            protocols: list[ProtocolsItem] | None = None

        forwarding_profiles: list[ForwardingProfilesItem] | None = None

    class Lacp(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class PortId(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Range(AvdDictBaseModel):
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

        class RateLimit(AvdDictBaseModel):
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

    class LinkTrackingGroupsItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        name: str = None
        links_minimum: int | None = Field(None, ge=1, le=100000)
        recovery_delay: int | None = Field(None, ge=0, le=3600)

    class Lldp(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class TlvsItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: Literal[
                "link-aggregation",
                "management-address",
                "max-frame-size",
                "med",
                "port-description",
                "port-vlan",
                "power-via-mdi",
                "system-capabilities",
                "system-description",
                "system-name",
                "vlan-name",
            ] = None
            transmit: bool | None = None

        timer: int | None = None
        timer_reinitialization: str | None = None
        holdtime: int | None = None
        management_address: str | None = None
        vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
        receive_packet_tagged_drop: str | None = None
        tlvs: list[TlvsItem] | None = None
        run: bool | None = None

    class LoadInterval(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        default: Annotated[int, IntConvert(convert_types=(str))] | None = None
        """
        Default load interval in seconds
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

    class Logging(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Buffered(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            size: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=10, le=2147483647)
            level: Literal["alerts", "critical", "debugging", "emergencies", "errors", "informational", "notifications", "warnings", "disabled"] | None = None
            """
            Buffer logging severity level
            """

        class Synchronous(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            level: (
                Literal["alerts", "all", "critical", "debugging", "emergencies", "errors", "informational", "notifications", "warnings", "disabled"] | None
            ) = "critical"
            """
            Synchronous logging severity level
            """

        class Format(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            timestamp: (
                Literal["high-resolution", "traditional", "traditional timezone", "traditional year", "traditional timezone year", "traditional year timezone"]
                | None
            ) = None
            """
            Timestamp format
            """
            hostname: Literal["fqdn", "ipv4"] | None = None
            """
            Hostname format in syslogs. For hostname _only_, remove the line. (default EOS CLI behaviour).
            """
            sequence_numbers: bool | None = None
            """
            Add sequence numbers to log messages
            """
            rfc5424: bool | None = None
            """
            Forward logs in RFC5424 format
            """

        class VrfsItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class HostsItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                name: str = None
                """
                Syslog server name
                """
                protocol: Literal["tcp", "udp"] | None = "udp"
                ports: list[Annotated[int, IntConvert(convert_types=(str))]] | None = None

            name: Annotated[str, StrConvert(convert_types=(int))] = None
            """
            VRF name
            """
            source_interface: str | None = None
            """
            Source interface name
            """
            hosts: list[HostsItem] | None = None

        class Policy(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Match(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class MatchListsItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    name: str = None
                    """
                    Match list
                    """
                    action: Literal["discard"] | None = None

                match_lists: list[MatchListsItem] | None = None

            match: Match | None = None

        class Event(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class StormControl(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Discards(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    field_global: bool | None = Field(None, alias="global")
                    interval: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=10, le=65535)
                    """
                    Logging interval in seconds
                    """

                discards: Discards | None = None

            storm_control: StormControl | None = None

        console: Literal["debugging", "informational", "notifications", "warnings", "errors", "critical", "alerts", "emergencies", "disabled"] | None = None
        """
        Console logging severity level
        """
        monitor: Literal["debugging", "informational", "notifications", "warnings", "errors", "critical", "alerts", "emergencies", "disabled"] | None = None
        """
        Monitor logging severity level
        """
        buffered: Buffered | None = None
        trap: Literal["alerts", "critical", "debugging", "emergencies", "errors", "informational", "notifications", "system", "warnings", "disabled"] | None = (
            None
        )
        """
        Trap logging severity level
        """
        synchronous: Synchronous | None = None
        format: Format | None = None
        facility: (
            Literal[
                "auth",
                "cron",
                "daemon",
                "kern",
                "local0",
                "local1",
                "local2",
                "local3",
                "local4",
                "local5",
                "local6",
                "local7",
                "lpr",
                "mail",
                "news",
                "sys9",
                "sys10",
                "sys11",
                "sys12",
                "sys13",
                "sys14",
                "syslog",
                "user",
                "uucp",
            ]
            | None
        ) = None
        source_interface: str | None = None
        """
        Source Interface Name
        """
        vrfs: list[VrfsItem] | None = None
        policy: Policy | None = None
        event: Event | None = None

    class LoopbackInterfacesItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Mpls(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Ldp(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                interface: bool | None = None

            ldp: Ldp | None = None

        class NodeSegment(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            ipv4_index: Annotated[int, IntConvert(convert_types=(str))] | None = None
            ipv6_index: Annotated[int, IntConvert(convert_types=(str))] | None = None

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
        isis_metric: Annotated[int, IntConvert(convert_types=(str))] | None = None
        isis_network_point_to_point: bool | None = None
        node_segment: NodeSegment | None = None
        eos_cli: str | None = None
        """
        EOS CLI rendered directly on the loopback interface in the final EOS configuration
        """

    class MacAccessListsItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class EntriesItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            sequence: Annotated[int, IntConvert(convert_types=(str))] | None = None
            action: str | None = None

        name: Annotated[str, StrConvert(convert_types=(int))] = None
        """
        MAC Access-list Name
        """
        counters_per_entry: bool | None = None
        entries: list[EntriesItem] | None = None

    class MacAddressTable(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class NotificationHostFlap(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Detection(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                window: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=2, le=300)
                moves: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=2, le=10)

            logging: bool | None = None
            detection: Detection | None = None

        aging_time: Annotated[int, IntConvert(convert_types=(str))] | None = None
        """
        Aging time in seconds
        """
        notification_host_flap: NotificationHostFlap | None = None

    class MacSecurity(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class License(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            license_name: str = None
            license_key: str = None

        class ProfilesItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class ConnectionKeysItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                id: str = None
                encrypted_key: str | None = None
                fallback: bool | None = None

            class Mka(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Session(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    rekey_period: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=30, le=100000)
                    """
                    Rekey period in seconds
                    """

                key_server_priority: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=255)
                session: Session | None = None

            class L2Protocols(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class EthernetFlowControl(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    mode: Literal["encrypt", "bypass"] = None

                class Lldp(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    mode: Literal["bypass", "bypass unauthorized"] = None

                ethernet_flow_control: EthernetFlowControl | None = None
                lldp: Lldp | None = None

            name: str = None
            """
            Profile-Name
            """
            cipher: Literal["aes128-gcm", "aes128-gcm-xpn", "aes256-gcm", "aes256-gcm-xpn"] | None = None
            connection_keys: list[ConnectionKeysItem] | None = None
            mka: Mka | None = None
            sci: bool | None = None
            l2_protocols: L2Protocols | None = None

        license: License | None = None
        fips_restrictions: bool | None = None
        profiles: list[ProfilesItem] | None = None

    class Maintenance(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class InterfaceProfilesItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class RateMonitoring(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                load_interval: Annotated[int, IntConvert(convert_types=(str))] | None = None
                """
                Load Interval in Seconds
                """
                threshold: Annotated[int, IntConvert(convert_types=(str))] | None = None
                """
                Threshold in kbps
                """

            class Shutdown(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                max_delay: Annotated[int, IntConvert(convert_types=(str))] | None = None
                """
                Max delay in seconds
                """

            name: str = None
            rate_monitoring: RateMonitoring | None = None
            shutdown: Shutdown | None = None

        class BgpProfilesItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Initiator(AvdDictBaseModel):
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

        class UnitProfilesItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class OnBoot(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                duration: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=300, le=3600)
                """
                On-boot in seconds
                """

            name: str = None
            """
            Unit Profile Name
            """
            on_boot: OnBoot | None = None

        class UnitsItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Groups(AvdDictBaseModel):
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

    class ManagementAccounts(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Password(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            policy: str | None = None

        password: Password | None = None

    class ManagementApiGnmi(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Transport(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class GrpcItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

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
                notification_timestamp: Literal["send-time", "last-change-time"] | None = None
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
                port: Annotated[int, IntConvert(convert_types=(str))] | None = None
                """
                GNMI port.
                Make sure to update the control-plane ACL accordingly in order for the service to be reachable by external
                applications.
                """

            class GrpcTunnelsItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Destination(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    address: str = None
                    """
                    IP address or hostname
                    """
                    port: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=1, le=65535)
                    """
                    TCP Port
                    """

                class LocalInterface(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    name: str = None
                    """
                    Interface name
                    """
                    port: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=1, le=65535)
                    """
                    TCP Port
                    """

                class Target(AvdDictBaseModel):
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

        class EnableVrfsItem(AvdDictBaseModel):
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

    class ManagementApiHttp(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class EnableVrfsItem(AvdDictBaseModel):
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

        class ProtocolHttpsCertificate(AvdDictBaseModel):
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

    class ManagementApiModels(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class ProvidersItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class PathsItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                path: str | None = None
                disabled: bool | None = False

            name: Literal["sysdb", "smash"] | None = None
            paths: list[PathsItem] | None = None

        providers: list[ProvidersItem] | None = None

    class ManagementConsole(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        idle_timeout: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=86400)

    class ManagementCvx(AvdDictBaseModel):
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

    class ManagementDefaults(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Secret(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            hash: Literal["md5", "sha512"] | None = None

        secret: Secret | None = None

    class ManagementInterfacesItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Lldp(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            transmit: bool | None = None
            receive: bool | None = None
            ztp_vlan: Annotated[int, IntConvert(convert_types=(str))] | None = None
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
        type: Literal["oob", "inband"] | None = "oob"
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

    class ManagementSecurity(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Password(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class PoliciesItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Minimum(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    digits: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)
                    length: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)
                    lower: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)
                    special: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)
                    upper: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)

                class Maximum(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    repetitive: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)
                    sequential: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)

                name: str = None
                minimum: Minimum | None = None
                maximum: Maximum | None = None

            minimum_length: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=32)
            encryption_key_common: bool | None = None
            encryption_reversible: str | None = None
            policies: list[PoliciesItem] | None = None

        class SslProfilesItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class TrustCertificate(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Requirement(AvdDictBaseModel):
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

            class ChainCertificate(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Requirement(AvdDictBaseModel):
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

            class Certificate(AvdDictBaseModel):
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
            certificate_revocation_lists: list[str] | None = None
            """
            List of CRLs (Certificate Revocation List).
            If specified, one CRL needs to be provided for every certificate in the
            chain, even if the revocation list in the CRL is empty.
            """

        entropy_source: str | None = None
        password: Password | None = None
        ssl_profiles: list[SslProfilesItem] | None = None

    class ManagementSsh(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class AccessGroupsItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str | None = None
            """
            Standard ACL Name
            """
            vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
            """
            VRF Name
            """

        class Ipv6AccessGroupsItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str | None = None
            """
            Standard ACL Name
            """
            vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
            """
            VRF Name
            """

        class Hostkey(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            server: list[str] | None = None
            """
            SSH host key settings.
            """
            server_cert: str | None = None
            """
            Configure switch's hostkey cert file.
            """
            client_strict_checking: bool | None = None
            """
            Enforce strict host key checking.
            """

        class Connection(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            limit: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=100)
            """
            Maximum total number of SSH sessions to device
            """
            per_host: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=20)
            """
            Maximum number of SSH sessions to device from a single host
            """

        class VrfsItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: Annotated[str, StrConvert(convert_types=(int))] = None
            """
            VRF Name
            """
            enable: bool | None = None
            """
            Enable SSH in VRF
            """

        class ClientAlive(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            count_max: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=1000)
            """
            Number of keep-alive packets that can be sent without a response before the connection is assumed dead.
            """
            interval: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=1000)
            """
            Time period (in seconds) to send SSH keep-alive packets.
            """

        access_groups: list[AccessGroupsItem] | None = None
        ipv6_access_groups: list[Ipv6AccessGroupsItem] | None = None
        idle_timeout: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=86400)
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
        fips_restrictions: bool | None = None
        """
        Use FIPS compliant algorithms.
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

    class ManagementTechSupport(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class PolicyShowTechSupport(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class ExcludeCommandsItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                command: str | None = None
                """
                Command to exclude from tech-support
                """
                type: Literal["text", "json"] | None = "text"
                """
                The supported values for type are platform dependent.
                """

            class IncludeCommandsItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                command: str | None = None
                """
                Command to include in tech-support
                """

            exclude_commands: list[ExcludeCommandsItem] | None = None
            include_commands: list[IncludeCommandsItem] | None = None

        policy_show_tech_support: PolicyShowTechSupport | None = None

    class MatchListInput(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class PrefixIpv4Item(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str = None
            """
            Prefix-List Name.
            """
            prefixes: list[str] = Field(None, min_length=1)
            """
            List of IPv4 prefixes (with the subnet mask e.g. 192.0.2.0/24).
            """

        class PrefixIpv6Item(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str = None
            """
            Prefix-List Name.
            """
            prefixes: list[str] = Field(None, min_length=1)
            """
            List of IPv6 prefixes (with the subnet mask e.g. 2001:db8:abcd:0013::/64).
            """

        class StringItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class SequenceNumbersItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                sequence: Annotated[int, IntConvert(convert_types=(str))] = None
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

        prefix_ipv4: list[PrefixIpv4Item] | None = None
        prefix_ipv6: list[PrefixIpv6Item] | None = None
        string: list[StringItem] | None = None

    class McsClient(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class CvxSecondary(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str | None = None
            shutdown: bool | None = None
            server_hosts: list[str] | None = None

        shutdown: bool | None = None
        cvx_secondary: CvxSecondary | None = None

    class Metadata(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class CvTags(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class DeviceTagsItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                name: str = None
                value: str = None

            class InterfaceTagsItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class TagsItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    name: str = None
                    value: str = None

                interface: str = None
                tags: list[TagsItem] | None = None

            device_tags: list[DeviceTagsItem] | None = None
            interface_tags: list[InterfaceTagsItem] | None = None

        class CvPathfinder(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class PathfindersItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                vtep_ip: str | None = None

            class InterfacesItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                name: str | None = None
                carrier: str | None = None
                circuit_id: str | None = None
                pathgroup: str | None = None
                public_ip: str | None = None

            class PathgroupsItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class CarriersItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    name: str | None = None

                class ImportedCarriersItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    name: str | None = None

                name: str | None = None
                carriers: list[CarriersItem] | None = None
                imported_carriers: list[ImportedCarriersItem] | None = None

            class RegionsItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class ZonesItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class SitesItem(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        class Location(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            address: str | None = None

                        id: int | None = None
                        name: str | None = None
                        location: Location | None = None

                    id: int | None = None
                    name: str | None = None
                    sites: list[SitesItem] | None = None

                id: int | None = None
                name: str | None = None
                zones: list[ZonesItem] | None = None

            class VrfsItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class AvtsItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class Constraints(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        jitter: int | None = None
                        latency: int | None = None
                        lossrate: Annotated[str, StrConvert(convert_types=(float))] | None = None

                    class PathgroupsItem(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        name: str | None = None
                        preference: str | None = None

                    constraints: Constraints | None = None
                    description: str | None = None
                    id: int | None = None
                    name: str | None = None
                    pathgroups: list[PathgroupsItem] | None = None

                name: str | None = None
                vni: int | None = None
                avts: list[AvtsItem] | None = None

            role: str | None = None
            region: str | None = None
            zone: str | None = None
            site: str | None = None
            vtep_ip: str | None = None
            ssl_profile: str | None = None
            pathfinders: list[PathfindersItem] | None = None
            interfaces: list[InterfacesItem] | None = None
            pathgroups: list[PathgroupsItem] | None = None
            regions: list[RegionsItem] | None = None
            vrfs: list[VrfsItem] | None = None

        platform: str | None = None
        system_mac_address: str | None = None
        cv_tags: CvTags | None = None
        cv_pathfinder: CvPathfinder | None = None
        """
        Metadata used for CV Pathfinder visualization on CloudVision
        """

    class MlagConfiguration(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class PeerAddressHeartbeat(AvdDictBaseModel):
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
        heartbeat_interval: Annotated[int, IntConvert(convert_types=(str))] | None = None
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
        dual_primary_detection_delay: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=86400)
        """
        Delay in seconds
        """
        dual_primary_recovery_delay_mlag: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=86400)
        """
        Delay in seconds
        """
        dual_primary_recovery_delay_non_mlag: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=86400)
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

    class MonitorConnectivity(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class InterfaceSetsItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str | None = None
            interfaces: str | None = None
            """
            Interface range(s) should be of same type, Ethernet, Loopback, Management etc.
            Multiple interface ranges can be
            specified separated by ","
            """

        class HostsItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str | None = None
            """
            Host Name
            """
            description: str | None = None
            ip: str | None = None
            local_interfaces: str | None = None
            url: str | None = None

        class VrfsItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class InterfaceSetsItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                name: str | None = None
                interfaces: str | None = None

            class HostsItem(AvdDictBaseModel):
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
        interval: Annotated[int, IntConvert(convert_types=(str))] | None = None
        interface_sets: list[InterfaceSetsItem] | None = None
        local_interfaces: str | None = None
        hosts: list[HostsItem] | None = None
        vrfs: list[VrfsItem] | None = None

    class MonitorLayer1(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class LoggingTransceiver(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            dom: bool | None = None
            """
            Enable transceiver Digital Optical Monitoring (DOM) logging.
            """
            communication: bool | None = None
            """
            Enable transceiver SMBus fail and reset logging.
            """

        enabled: bool = None
        """
        Enable monitor layer1
        """
        logging_mac_fault: bool | None = None
        """
        Enable MAC fault logging.
        """
        logging_transceiver: LoggingTransceiver | None = None
        """
        Configure transceiver monitoring logging.
        """

    class MonitorSessionsItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class SourcesItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class AccessGroup(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                type: Literal["ip", "ipv6", "mac"] | None = None
                name: str | None = None
                """
                ACL Name
                """
                priority: Annotated[int, IntConvert(convert_types=(str))] | None = None

            name: str | None = None
            """
            Interface name, range or comma separated list
            """
            direction: Literal["rx", "tx", "both"] | None = None
            access_group: AccessGroup | None = None

        class AccessGroup(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            type: Literal["ip", "ipv6", "mac"] | None = None
            name: str | None = None
            """
            ACL Name
            """

        class Truncate(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            enabled: bool | None = None
            size: Annotated[int, IntConvert(convert_types=(str))] | None = None
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
        header_remove_size: Annotated[int, IntConvert(convert_types=(str))] | None = None
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
        sample: Annotated[int, IntConvert(convert_types=(str))] | None = None
        truncate: Truncate | None = None

    class Mpls(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Ldp(AvdDictBaseModel):
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

    class NameServer(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Source(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
            """
            VRF Name
            """

        source: Source | None = None
        nodes: list[str] | None = None

    class Ntp(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class LocalInterface(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str | None = None
            """
            Source interface
            """
            vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
            """
            VRF name
            """

        class ServersItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str | None = None
            """
            IP or hostname e.g., 2.2.2.55, ie.pool.ntp.org
            """
            burst: bool | None = None
            iburst: bool | None = None
            key: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)
            local_interface: str | None = None
            """
            Source interface
            """
            maxpoll: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=3, le=17)
            """
            Value of maxpoll between 3 - 17 (Logarithmic)
            """
            minpoll: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=3, le=17)
            """
            Value of minpoll between 3 - 17 (Logarithmic)
            """
            preferred: bool | None = None
            version: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=4)
            vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
            """
            VRF name
            """

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

        local_interface: LocalInterface | None = None
        servers: list[ServersItem] | None = None
        authenticate: bool | None = None
        authenticate_servers_only: bool | None = None
        authentication_keys: list[AuthenticationKeysItem] | None = None
        trusted_keys: Annotated[str, StrConvert(convert_types=(int))] | None = None
        """
        List of trusted-keys as string ex. 10-12,15
        """

    class PatchPanel(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class PatchesItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class ConnectorsItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                id: Annotated[str, StrConvert(convert_types=(int))] = None
                type: Literal["interface", "pseudowire"] = None
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

    class PeerFiltersItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class SequenceNumbersItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            sequence: Annotated[int, IntConvert(convert_types=(str))] = None
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

    class Platform(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Trident(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Mmu(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class QueueProfilesItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class MulticastQueuesItem(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        class Drop(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            precedence: Literal[1, 2] = None
                            threshold: Annotated[str, StrConvert(convert_types=(int))] = None
                            """
                            Drop Treshold. This value may also be fractions.
                            Example: 7/8 or 3/4 or 1/2
                            """

                        id: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=0, le=7)
                        unit: Literal["bytes", "cells"] | None = None
                        """
                        Unit to be used for the reservation value. If not specified, default is bytes.
                        """
                        reserved: Annotated[int, IntConvert(convert_types=(str))] | None = None
                        """
                        Amount of memory that should be reserved for this
                        queue.
                        """
                        threshold: Annotated[str, StrConvert(convert_types=(int))] | None = None
                        """
                        Dynamic Shared Memory threshold.
                        """
                        drop: Drop | None = None

                    class UnicastQueuesItem(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        class Drop(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            precedence: Literal[1, 2] = None
                            threshold: Annotated[str, StrConvert(convert_types=(int))] = None
                            """
                            Drop Treshold. This value may also be fractions.
                            Example: 7/8 or 3/4 or 1/2
                            """

                        id: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=0, le=7)
                        unit: Literal["bytes", "cells"] | None = None
                        """
                        Unit to be used for the reservation value. If not specified, default is bytes.
                        """
                        reserved: Annotated[int, IntConvert(convert_types=(str))] | None = None
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

        class Sand(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class QosMapsItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                traffic_class: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=7)
                to_network_qos: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=63)

            class Lag(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                hardware_only: bool | None = None
                mode: str | None = None

            class MulticastReplication(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                default: Literal["ingress", "egress"] | None = None

            qos_maps: list[QosMapsItem] | None = None
            lag: Lag | None = None
            forwarding_mode: str | None = None
            multicast_replication: MulticastReplication | None = None
            mdb_profile: Literal["balanced", "balanced-xl", "l3", "l3-xl", "l3-xxl", "l3-xxxl"] | None = None
            """
            Sand platforms MDB Profile configuration. Note: l3-xxxl does not support MLAG.
            """

        class Sfe(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            data_plane_cpu_allocation_max: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=128)
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

    class Poe(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Reboot(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            action: Literal["power-off", "maintain"] | None = None
            """
            PoE action for interface. By default in EOS, reboot action is set to power-off.
            """

        class InterfaceShutdown(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            action: Literal["power-off", "maintain"] | None = None
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

    class PolicyMaps(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class PbrItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class ClassesItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Set(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class Nexthop(AvdDictBaseModel):
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
                index: Annotated[int, IntConvert(convert_types=(str))] | None = None
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

        class QosItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class ClassesItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Set(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    cos: Annotated[int, IntConvert(convert_types=(str))] | None = None
                    dscp: Annotated[str, StrConvert(convert_types=(int))] | None = None
                    traffic_class: Annotated[int, IntConvert(convert_types=(str))] | None = None
                    drop_precedence: Annotated[int, IntConvert(convert_types=(str))] | None = None

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

    class PortChannelInterfacesItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Logging(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Event(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                link_status: bool | None = None
                storm_control_discards: bool | None = None
                """
                Discards due to storm-control.
                """

            event: Event | None = None

        class EncapsulationVlan(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Client(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Dot1q(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    vlan: Annotated[int, IntConvert(convert_types=(str))] | None = None
                    """
                    Client VLAN ID
                    """
                    outer: Annotated[int, IntConvert(convert_types=(str))] | None = None
                    """
                    Client Outer VLAN ID
                    """
                    inner: Annotated[int, IntConvert(convert_types=(str))] | None = None
                    """
                    Client Inner VLAN ID
                    """

                dot1q: Dot1q | None = None
                unmatched: bool | None = None

            class Network(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Dot1q(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    vlan: Annotated[int, IntConvert(convert_types=(str))] | None = None
                    """
                    Network VLAN ID
                    """
                    outer: Annotated[int, IntConvert(convert_types=(str))] | None = None
                    """
                    Network Outer VLAN ID
                    """
                    inner: Annotated[int, IntConvert(convert_types=(str))] | None = None
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

        class LinkTrackingGroupsItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str = None
            """
            Group name
            """
            direction: Literal["upstream", "downstream"] | None = None

        class Phone(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            trunk: Literal["tagged", "untagged"] | None = None
            vlan: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=4094)

        class L2Protocol(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            encapsulation_dot1q_vlan: Annotated[int, IntConvert(convert_types=(str))] | None = None
            """
            Vlan tag to configure on sub-interface
            """
            forwarding_profile: str | None = None
            """
            L2 protocol forwarding profile
            """

        class Qos(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            trust: Literal["dscp", "cos", "disabled"] | None = None
            dscp: Annotated[int, IntConvert(convert_types=(str))] | None = None
            """
            DSCP value
            """
            cos: Annotated[int, IntConvert(convert_types=(str))] | None = None
            """
            COS value
            """

        class Bfd(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class PerLink(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                enabled: bool | None = None
                rfc_7130: bool | None = None

            echo: bool | None = None
            interval: Annotated[int, IntConvert(convert_types=(str))] | None = None
            """
            Interval in milliseconds
            """
            min_rx: Annotated[int, IntConvert(convert_types=(str))] | None = None
            """
            Rate in milliseconds
            """
            multiplier: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=3, le=50)
            neighbor: str | None = None
            """
            IPv4 or IPv6 address. When the Port-channel is a L2 interface, a local L3 BFD address (router_bfd.local_address) has to
            be defined globally on the switch.
            """
            per_link: PerLink | None = None

        class ServicePolicy(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Pbr(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                input: str | None = None
                """
                Policy Based Routing Policy-map name
                """

            class Qos(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                input: str = None
                """
                Quality of Service Policy-map name
                """

            pbr: Pbr | None = None
            qos: Qos | None = None

        class Mpls(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Ldp(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                interface: bool | None = None
                igp_sync: bool | None = None

            ip: bool | None = None
            ldp: Ldp | None = None

        class VlanTranslationsItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            field_from: Annotated[str, StrConvert(convert_types=(int))] | None = Field(None, alias="from")
            """
            List of vlans as string (only one vlan if direction is "both")
            """
            to: Annotated[int, IntConvert(convert_types=(str))] | None = None
            """
            VLAN ID
            """
            direction: Literal["in", "out", "both"] | None = "both"

        class Shape(AvdDictBaseModel):
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

        class StormControl(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class All(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                level: Annotated[str, StrConvert(convert_types=(int, float))] | None = None
                """
                Configure maximum storm-control level
                """
                unit: Literal["percent", "pps"] | None = "percent"
                """
                Optional field and is hardware dependent
                """

            class Broadcast(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                level: Annotated[str, StrConvert(convert_types=(int, float))] | None = None
                """
                Configure maximum storm-control level
                """
                unit: Literal["percent", "pps"] | None = "percent"
                """
                Optional field and is hardware dependent
                """

            class Multicast(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                level: Annotated[str, StrConvert(convert_types=(int, float))] | None = None
                """
                Configure maximum storm-control level
                """
                unit: Literal["percent", "pps"] | None = "percent"
                """
                Optional field and is hardware dependent
                """

            class UnknownUnicast(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                level: Annotated[str, StrConvert(convert_types=(int, float))] | None = None
                """
                Configure maximum storm-control level
                """
                unit: Literal["percent", "pps"] | None = "percent"
                """
                Optional field and is hardware dependent
                """

            all: All | None = None
            broadcast: Broadcast | None = None
            multicast: Multicast | None = None
            unknown_unicast: UnknownUnicast | None = None

        class TrafficPolicy(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            input: str | None = None
            """
            Ingress traffic policy
            """
            output: str | None = None
            """
            Egress traffic policy
            """

        class EvpnEthernetSegment(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class DesignatedForwarderElection(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                algorithm: Literal["modulus", "preference"] | None = None
                preference_value: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=65535)
                """
                Preference_value is only used when "algorithm" is "preference"
                """
                dont_preempt: bool | None = False
                """
                Dont_preempt is only used when "algorithm" is "preference"
                """
                hold_time: Annotated[int, IntConvert(convert_types=(str))] | None = None
                subsequent_hold_time: Annotated[int, IntConvert(convert_types=(str))] | None = None
                candidate_reachability_required: bool | None = None

            class Mpls(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                shared_index: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=1024)
                tunnel_flood_filter_time: Annotated[int, IntConvert(convert_types=(str))] | None = None

            identifier: str | None = None
            """
            EVPN Ethernet Segment Identifier (Type 1 format)
            """
            redundancy: Literal["all-active", "single-active"] | None = None
            designated_forwarder_election: DesignatedForwarderElection | None = None
            mpls: Mpls | None = None
            route_target: str | None = None
            """
            EVPN Route Target for ESI with format xx:xx:xx:xx:xx:xx
            """

        class Ptp(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Announce(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                interval: Annotated[int, IntConvert(convert_types=(str))] | None = None
                timeout: Annotated[int, IntConvert(convert_types=(str))] | None = None

            class SyncMessage(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                interval: Annotated[int, IntConvert(convert_types=(str))] | None = None

            enable: bool | None = None
            announce: Announce | None = None
            delay_req: Annotated[int, IntConvert(convert_types=(str))] | None = None
            delay_mechanism: Literal["e2e", "p2p"] | None = None
            sync_message: SyncMessage | None = None
            role: Literal["master", "dynamic"] | None = None
            vlan: Annotated[str, StrConvert(convert_types=(int))] | None = None
            """
            VLAN can be 'all' or list of vlans as string
            """
            transport: Literal["ipv4", "ipv6", "layer2"] | None = None

        class IpNat(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Destination(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class DynamicItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    access_list: str = None
                    comment: str | None = None
                    pool_name: str = None
                    priority: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=4294967295)

                class StaticItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    access_list: str | None = None
                    """
                    'access_list' and 'group' are mutual exclusive
                    """
                    comment: str | None = None
                    direction: Literal["egress", "ingress"] | None = None
                    """
                    Egress or ingress can be the default. This depends on source/destination, EOS version, and hardware platform.
                    EOS might
                    remove this keyword in the configuration. So, check the configuration on targeted HW/SW.
                    """
                    group: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)
                    """
                    'access_list' and 'group' are mutual exclusive
                    """
                    original_ip: str = None
                    """
                    IPv4 address
                    """
                    original_port: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)
                    priority: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=4294967295)
                    protocol: Literal["udp", "tcp"] | None = None
                    translated_ip: str = None
                    """
                    IPv4 address
                    """
                    translated_port: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)
                    """
                    requires 'original_port'
                    """

                dynamic: list[DynamicItem] | None = None
                static: list[StaticItem] | None = None

            class Source(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class DynamicItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    access_list: str = None
                    comment: str | None = None
                    nat_type: Literal["overload", "pool", "pool-address-only", "pool-full-cone"] = None
                    pool_name: str | None = None
                    """
                    required if 'nat_type' is pool, pool-address-only or pool-full-cone
                    ignored if 'nat_type' is overload
                    """
                    priority: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=4294967295)

                class StaticItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    access_list: str | None = None
                    """
                    'access_list' and 'group' are mutual exclusive
                    """
                    comment: str | None = None
                    direction: Literal["egress", "ingress"] | None = None
                    """
                    Egress or ingress can be the default. This depends on source/destination, EOS version, and hardware platform.
                    EOS might
                    remove this keyword in the configuration. So, check the configuration on targeted HW/SW.
                    """
                    group: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)
                    """
                    'access_list' and 'group' are mutual exclusive
                    """
                    original_ip: str = None
                    """
                    IPv4 address
                    """
                    original_port: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)
                    priority: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=4294967295)
                    protocol: Literal["udp", "tcp"] | None = None
                    translated_ip: str = None
                    """
                    IPv4 address
                    """
                    translated_port: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)
                    """
                    requires 'original_port'
                    """

                dynamic: list[DynamicItem] | None = None
                static: list[StaticItem] | None = None

            destination: Destination | None = None
            source: Source | None = None

        class Ipv6NdPrefixesItem(AvdDictBaseModel):
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

        class Pim(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Ipv4(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Hello(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    count: Annotated[str, StrConvert(convert_types=(int, float))] | None = None
                    """
                    Number of missed hellos after which the neighbor expires. Range <1.5-65535>.
                    """
                    interval: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)
                    """
                    PIM hello interval in seconds.
                    """

                border_router: bool | None = None
                """
                Configure PIM border router. EOS default is false.
                """
                dr_priority: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=429467295)
                sparse_mode: bool | None = None
                bfd: bool | None = None
                """
                Set the default for whether Bidirectional Forwarding Detection is enabled for PIM.
                """
                bidirectional: bool | None = None
                hello: Hello | None = None

            ipv4: Ipv4 | None = None

        class OspfMessageDigestKeysItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            id: Annotated[int, IntConvert(convert_types=(str))] = None
            hash_algorithm: Literal["md5", "sha1", "sha256", "sha384", "sha512"] | None = None
            key: str | None = None
            """
            Encrypted password
            """

        class FlowTracker(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            sampled: str | None = None
            """
            Sampled flow tracker name.
            """
            hardware: str | None = None
            """
            Hardware flow tracker name.
            """

        class Bgp(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            session_tracker: str | None = None
            """
            Name of session tracker
            """

        class IpIgmpHostProxy(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class GroupsItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class ExcludeItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    source: str = None

                class IncludeItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    source: str = None

                group: str = None
                """
                Multicast Address.
                """
                exclude: list[ExcludeItem] | None = None
                """
                The same source must not be present both in `exclude` and `include` list.
                """
                include: list[IncludeItem] | None = None
                """
                The same source must not be present both in `exclude` and `include` list.
                """

            class AccessListsItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                name: str = None

            enabled: bool | None = None
            groups: list[GroupsItem] | None = None
            report_interval: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=31744)
            """
            Time interval between unsolicited reports.
            """
            access_lists: list[AccessListsItem] | None = None
            """
            Non-standard Access List name.
            """
            version: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=3)
            """
            IGMP version on IGMP host-proxy interface.
            """

        class Sflow(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Egress(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                enable: bool | None = None
                unmodified_enable: bool | None = None

            enable: bool | None = None
            egress: Egress | None = None

        name: str = None
        description: str | None = None
        logging: Logging | None = None
        shutdown: bool | None = None
        l2_mtu: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=68, le=65535)
        """
        "l2_mtu" should only be defined for platforms supporting the "l2 mtu" CLI
        """
        l2_mru: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=68, le=65535)
        """
        "l2_mru" should only be defined for platforms supporting the "l2 mru" CLI
        """
        vlans: Annotated[str, StrConvert(convert_types=(int))] | None = None
        """
        List of switchport vlans as string
        For a trunk port this would be a range like "1-200,300"
        For an access port this would
        be a single vlan "123"
        """
        snmp_trap_link_change: bool | None = None
        type: Literal["routed", "switched", "l3dot1q", "l2dot1q"] | None = None
        """
        l3dot1q and l2dot1q are used for sub-interfaces. The parent interface should be defined as routed.
        Interface will not be
        listed in device documentation, unless "type" is set.
        """
        encapsulation_dot1q_vlan: Annotated[int, IntConvert(convert_types=(str))] | None = None
        """
        VLAN tag to configure on sub-interface
        """
        vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
        """
        VRF name
        """
        encapsulation_vlan: EncapsulationVlan | None = None
        vlan_id: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=4094)
        mode: Literal["access", "dot1q-tunnel", "trunk", "trunk phone"] | None = None
        native_vlan: Annotated[int, IntConvert(convert_types=(str))] | None = None
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
        mtu: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=68, le=65535)
        mlag: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=2000)
        """
        MLAG ID
        """
        trunk_groups: list[str] | None = None
        lacp_fallback_timeout: Annotated[int, IntConvert(convert_types=(str))] | None = Field(90, ge=0, le=300)
        """
        Timeout in seconds
        """
        lacp_fallback_mode: Literal["individual", "static"] | None = None
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
        isis_metric: Annotated[int, IntConvert(convert_types=(str))] | None = None
        isis_network_point_to_point: bool | None = None
        isis_circuit_type: Literal["level-1-2", "level-1", "level-2"] | None = None
        isis_hello_padding: bool | None = None
        isis_authentication_mode: Literal["text", "md5"] | None = None
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
        spanning_tree_bpdufilter: Annotated[Literal["enabled", "disabled", "True", "False", "true", "false"], StrConvert(convert_types=(bool))] | None = None
        spanning_tree_bpduguard: Annotated[Literal["enabled", "disabled", "True", "False", "true", "false"], StrConvert(convert_types=(bool))] | None = None
        spanning_tree_guard: Literal["loop", "root", "disabled"] | None = None
        spanning_tree_portfast: Literal["edge", "network"] | None = None
        vmtracer: bool | None = None
        ptp: Ptp | None = None
        ip_address: str | None = None
        """
        IPv4 address/mask
        """
        ip_verify_unicast_source_reachable_via: Literal["any", "rx"] | None = None
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
        ospf_cost: Annotated[int, IntConvert(convert_types=(str))] | None = None
        ospf_authentication: Literal["none", "simple", "message-digest"] | None = None
        ospf_authentication_key: str | None = None
        """
        Encrypted password
        """
        ospf_message_digest_keys: list[OspfMessageDigestKeysItem] | None = None
        flow_tracker: FlowTracker | None = None
        bgp: Bgp | None = None
        ip_igmp_host_proxy: IpIgmpHostProxy | None = None
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
        validate_state: bool | None = None
        """
        Set to false to disable interface validation by the `eos_validate_state` role
        """
        eos_cli: str | None = None
        """
        Multiline EOS CLI rendered directly on the port-channel interface in the final EOS configuration
        """

    class PrefixListsItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class SequenceNumbersItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            sequence: Annotated[int, IntConvert(convert_types=(str))] = None
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

    class PriorityFlowControl(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Watchdog(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            action: Literal["drop", "no-drop"] | None = None
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

    class Ptp(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Source(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            ip: str | None = None
            """
            Source IP
            """

        class MessageType(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class General(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                dscp: Annotated[int, IntConvert(convert_types=(str))] | None = None

            class Event(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                dscp: Annotated[int, IntConvert(convert_types=(str))] | None = None

            general: General | None = None
            event: Event | None = None

        class Monitor(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Threshold(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Drop(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    offset_from_master: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=1000000000)
                    mean_path_delay: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=1000000000)

                offset_from_master: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=1000000000)
                mean_path_delay: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=1000000000)
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

                    enabled: bool | None = None
                    announce: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=2, le=255)
                    delay_resp: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=2, le=255)
                    follow_up: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=2, le=255)
                    sync: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=2, le=255)

                intervals: Intervals | None = None
                sequence_ids: SequenceIds | None = None

            enabled: bool | None = True
            threshold: Threshold | None = None
            missing_message: MissingMessage | None = None

        mode: Literal["boundary", "disabled", "e2etransparent", "gptp", "ordinarymaster", "p2ptransparent"] | None = None
        mode_one_step: bool | None = None
        forward_unicast: bool | None = None
        clock_identity: str | None = None
        """
        The clock-id in xx:xx:xx:xx:xx:xx format
        """
        source: Source | None = None
        priority1: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=255)
        priority2: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=255)
        ttl: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=255)
        domain: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=255)
        message_type: MessageType | None = None
        monitor: Monitor | None = None

    class Qos(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Map(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            cos: list[str] | None = None
            dscp: list[str] | None = None
            exp: list[str] | None = None
            traffic_class: list[str] | None = None

        class RandomDetect(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Ecn(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class AllowNonEct(AvdDictBaseModel):
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

    class QosProfilesItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Shape(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            rate: str | None = None
            """
            Supported options are platform dependent
            Example: "< rate > kbps", "1-100 percent", "< rate > pps"
            """

        class ServicePolicy(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Type(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                qos_input: str | None = None
                """
                Policy-map name
                """

            type: Type | None = None

        class TxQueuesItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Shape(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                rate: str | None = None
                """
                Supported options are platform dependent
                Example: "< rate > kbps", "1-100 percent", "< rate > pps"
                """

            class RandomDetect(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Ecn(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class Threshold(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        units: Literal["segments", "bytes", "kbytes", "mbytes", "milliseconds"] = None
                        """
                        Units to be used for the threshold values.
                        This should be one of segments, byte, kbytes, mbytes.
                        """
                        min: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=1)
                        """
                        Random-detect ECN minimum-threshold
                        """
                        max: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=1)
                        """
                        Random-detect ECN maximum-threshold
                        """
                        max_probability: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=100)
                        """
                        Random-detect ECN maximum mark probability
                        """
                        weight: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=15)
                        """
                        Random-detect ECN weight
                        """

                    count: bool | None = None
                    """
                    Enable counter for random-detect ECNs
                    """
                    threshold: Threshold | None = None

                class Drop(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class Threshold(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        units: Literal["segments", "bytes", "kbytes", "mbytes", "microseconds", "milliseconds"] = None
                        """
                        Units to be used for the threshold values.
                        """
                        drop_precedence: int | None = Field(None, ge=0, le=2)
                        """
                        Specify Drop Precendence value
                        """
                        min: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=1)
                        """
                        WRED minimum-threshold
                        """
                        max: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=1)
                        """
                        WRED maximum-threshold
                        """
                        drop_probability: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=1, le=100)
                        """
                        WRED drop probability.
                        """
                        weight: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=15)
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

            id: Annotated[int, IntConvert(convert_types=(str))] = None
            """
            TX-Queue ID
            """
            bandwidth_percent: Annotated[int, IntConvert(convert_types=(str))] | None = None
            bandwidth_guaranteed_percent: Annotated[int, IntConvert(convert_types=(str))] | None = None
            priority: Literal["priority strict", "no priority"] | None = None
            shape: Shape | None = None
            comment: str | None = None
            """
            Text comment added to queue
            """
            random_detect: RandomDetect | None = None

        class UcTxQueuesItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Shape(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                rate: str | None = None
                """
                Supported options are platform dependent
                Example: "< rate > kbps", "1-100 percent", "< rate > pps"
                """

            class RandomDetect(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Ecn(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class Threshold(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        units: Literal["segments", "bytes", "kbytes", "mbytes", "milliseconds"] = None
                        """
                        Unit to be used for the threshold values
                        """
                        min: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=1)
                        """
                        Random-detect ECN minimum-threshold
                        """
                        max: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=1)
                        """
                        Random-detect ECN maximum-threshold
                        """
                        max_probability: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=100)
                        """
                        Random-detect ECN maximum mark probability
                        """
                        weight: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=15)
                        """
                        Random-detect ECN weight
                        """

                    count: bool | None = None
                    """
                    Enable counter for random-detect ECNs
                    """
                    threshold: Threshold | None = None

                class Drop(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class Threshold(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        units: Literal["segments", "bytes", "kbytes", "mbytes", "microseconds", "milliseconds"] = None
                        """
                        Units to be used for the threshold values.
                        """
                        drop_precedence: int | None = Field(None, ge=0, le=2)
                        """
                        Specify Drop Precendence value
                        """
                        min: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=1)
                        """
                        WRED minimum-threshold
                        """
                        max: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=1)
                        """
                        WRED maximum-threshold
                        """
                        drop_probability: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=1, le=100)
                        """
                        WRED drop probability.
                        """
                        weight: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=15)
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

            id: Annotated[int, IntConvert(convert_types=(str))] = None
            """
            UC TX queue ID
            """
            bandwidth_percent: Annotated[int, IntConvert(convert_types=(str))] | None = None
            bandwidth_guaranteed_percent: Annotated[int, IntConvert(convert_types=(str))] | None = None
            priority: Literal["priority strict", "no priority"] | None = None
            shape: Shape | None = None
            comment: str | None = None
            """
            Text comment added to queue
            """
            random_detect: RandomDetect | None = None

        class McTxQueuesItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Shape(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                rate: str | None = None
                """
                Supported options are platform dependent
                Example: "< rate > kbps", "1-100 percent", "< rate > pps"
                """

            id: Annotated[int, IntConvert(convert_types=(str))] = None
            """
            MC TX queue ID
            """
            bandwidth_percent: Annotated[int, IntConvert(convert_types=(str))] | None = None
            bandwidth_guaranteed_percent: Annotated[int, IntConvert(convert_types=(str))] | None = None
            priority: Literal["priority strict", "no priority"] | None = None
            shape: Shape | None = None
            comment: str | None = None
            """
            Text comment added to queue.
            """

        class PriorityFlowControl(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Watchdog(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Timer(AvdDictBaseModel):
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
                action: Literal["drop", "notify-only"] | None = None
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

            class PrioritiesItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                priority: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=0, le=7)
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
        trust: Literal["cos", "dscp", "disabled"] | None = None
        cos: Annotated[int, IntConvert(convert_types=(str))] | None = None
        dscp: Annotated[int, IntConvert(convert_types=(str))] | None = None
        shape: Shape | None = None
        service_policy: ServicePolicy | None = None
        tx_queues: list[TxQueuesItem] | None = None
        uc_tx_queues: list[UcTxQueuesItem] | None = None
        mc_tx_queues: list[McTxQueuesItem] | None = None
        priority_flow_control: PriorityFlowControl | None = None
        """
        Priority Flow Control settings
        """

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
        default_thresholds: DefaultThresholds | None = None
        log: Annotated[int, IntConvert(convert_types=(str))] | None = None
        """
        Logging interval in seconds
        """
        notifying: bool | None = None
        """
        Should only be used for platforms supporting the "queue-monitor length notifying" CLI
        """
        cpu: Cpu | None = None
        tx_latency: bool | None = None
        """
        Enable tx-latency mode
        """

    class QueueMonitorStreaming(AvdDictBaseModel):
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
        max_connections: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=100)
        vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None

    class RadiusServer(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Attribute32IncludeInAccessReq(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            hostname: bool | None = None
            format: str | None = None
            """
            Specify the format of the NAS-Identifier. If 'hostname' is set, this is ignored.
            """

        class DynamicAuthorization(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            port: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=65535)
            """
            TCP Port
            """
            tls_ssl_profile: str | None = None
            """
            Name of TLS profile
            """

        class HostsItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            host: str = None
            """
            Host IP address or name
            """
            vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
            timeout: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=1000)
            retransmit: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=100)
            key: str | None = None
            """
            Encrypted key
            """

        attribute_32_include_in_access_req: Attribute32IncludeInAccessReq | None = None
        dynamic_authorization: DynamicAuthorization | None = None
        hosts: list[HostsItem] | None = None

    class RadiusServersItem(AvdDictBaseModel):
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

    class Redundancy(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        protocol: str | None = None
        """
        Redundancy Protocol
        """

    class RolesItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class SequenceNumbersItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            sequence: Annotated[int, IntConvert(convert_types=(str))] | None = None
            """
            Sequence number
            """
            action: Literal["permit", "deny"] | None = None
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

    class RouteMapsItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class SequenceNumbersItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Continue(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                enabled: bool | None = None
                sequence_number: Annotated[int, IntConvert(convert_types=(str))] | None = None

            sequence: Annotated[int, IntConvert(convert_types=(str))] = None
            """
            Sequence ID
            """
            type: Literal["permit", "deny"] = None
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

    class RouterAdaptiveVirtualTopology(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Region(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str = None
            id: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=1, le=255)

        class Zone(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str = None
            id: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=1, le=10000)

        class Site(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str = None
            id: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=1, le=10000)

        class ProfilesItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str = None
            """
            AVT Name.
            """
            load_balance_policy: str | None = None
            """
            Name of the load-balance policy.
            """
            internet_exit_policy: str | None = None
            """
            Name of the internet exit policy.
            """

        class PoliciesItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class MatchesItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                application_profile: str | None = None
                """
                Application profile name.
                """
                avt_profile: str | None = None
                """
                AVT Profile name.
                """
                dscp: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=63)
                """
                Set DSCP for matched traffic.
                """
                traffic_class: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=7)
                """
                Set traffic-class for matched traffic.
                """

            name: str = None
            """
            Policy name.
            """
            matches: list[MatchesItem] | None = None

        class VrfsItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class ProfilesItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                name: str | None = None
                """
                AVT profile name.
                """
                id: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=1, le=254)
                """
                Unique ID for this AVT (per VRF).
                """

            name: str = None
            """
            VRF name.
            """
            policy: str | None = None
            """
            AVT Policy name.
            """
            profiles: list[ProfilesItem] | None = None
            """
            AVT profiles in this VRF.
            """

        topology_role: Literal["edge", "pathfinder", "transit region", "transit zone"] | None = None
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
        profiles: list[ProfilesItem] | None = None
        policies: list[PoliciesItem] | None = None
        """
        A sequence of application profiles mapped to some virtual topologies.

        When `wan_mode` is set to `autovpn`, the rules
        are indexed using 10*<index> in the list.
        """
        vrfs: list[VrfsItem] | None = None

    class RouterBfd(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Multihop(AvdDictBaseModel):
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

        class Sbfd(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class LocalInterface(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Protocols(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    ipv4: bool | None = None
                    ipv6: bool | None = None

                name: str | None = None
                """
                Interface Name
                """
                protocols: Protocols | None = None

            class Reflector(AvdDictBaseModel):
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
            initiator_measurement_round_trip: bool | None = None
            """
            Enable round-trip delay measurement
            """
            reflector: Reflector | None = None

        interval: int | None = None
        """
        Rate in milliseconds
        """
        local_address: str | None = None
        """
        Configure BFD local IP/IPv6 address
        """
        min_rx: int | None = None
        """
        Rate in milliseconds
        """
        multiplier: int | None = Field(None, ge=3, le=50)
        multihop: Multihop | None = None
        session_snapshot_interval: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=3600)
        """
        Interval in seconds.
        Intervals below 10 are considered "dangerous" on EOS and must have
        `session_snapshot_interval_dangerous` set to `true`.
        """
        session_snapshot_interval_dangerous: bool | None = None
        sbfd: Sbfd | None = None

    class RouterBgp(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Distance(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            external_routes: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=1, le=255)
            internal_routes: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=1, le=255)
            local_routes: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=1, le=255)

        class GracefulRestart(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            enabled: bool | None = None
            restart_time: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=3600)
            """
            Number of seconds
            """
            stalepath_time: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=3600)
            """
            Number of seconds
            """

        class GracefulRestartHelper(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            enabled: bool | None = None
            restart_time: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=100000000)
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

        class MaximumPaths(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            paths: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=1, le=600)
            ecmp: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=600)

        class Updates(AvdDictBaseModel):
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

        class Bgp(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Default(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                ipv4_unicast: bool | None = None
                """
                Default activation of IPv4 unicast address-family on all IPv4 neighbors (EOS default = True).
                """
                ipv4_unicast_transport_ipv6: bool | None = None
                """
                Default activation of IPv4 unicast address-family on all IPv6 neighbors (EOS default == False).
                """

            class RouteReflectorPreserveAttributes(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                enabled: bool | None = None
                always: bool | None = None

            class Bestpath(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                d_path: bool | None = None

            default: Default | None = None
            route_reflector_preserve_attributes: RouteReflectorPreserveAttributes | None = None
            bestpath: Bestpath | None = None

        class ListenRangesItem(AvdDictBaseModel):
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
            BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
            For asdot notation in YAML inputs, the value
            must be put in quotes, to prevent it from being interpreted as a float number.
            """

        class PeerGroupsItem(AvdDictBaseModel):
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
            Peer-group name
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

        class NeighborsItem(AvdDictBaseModel):
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

            class AllowasIn(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                enabled: bool | None = None
                times: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=10)
                """
                Number of local ASNs allowed in a BGP update
                """

            class LinkBandwidth(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                enabled: bool | None = None
                default: str | None = None
                """
                nn.nn(K|M|G) link speed in bits/second
                """

            class RibInPrePolicyRetain(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                enabled: bool | None = None
                all: bool | None = None

            class RemovePrivateAs(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                enabled: bool | None = None
                all: bool | None = None
                replace_as: bool | None = None

            class RemovePrivateAsIngress(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                enabled: bool | None = None
                replace_as: bool | None = None

            ip_address: str = None
            peer_group: str | None = None
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
            as_path: AsPath | None = None
            """
            BGP AS-PATH options
            """
            peer: str | None = None
            """
            Key only used for documentation or validation purposes
            """
            description: str | None = None
            route_reflector_client: bool | None = None
            password: str | None = None
            passive: bool | None = None
            shutdown: bool | None = None
            update_source: str | None = None
            """
            Source Interface
            """
            bfd: bool | None = None
            """
            Enable BFD.
            """
            bfd_timers: BfdTimers | None = None
            """
            Override default BFD timers. BFD must be enabled with `bfd: true`.
            """
            weight: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=65535)
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
            allowas_in: AllowasIn | None = None
            ebgp_multihop: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=255)
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
            ttl_maximum_hops: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=254)
            """
            Maximum number of hops.
            """

        class NeighborInterfacesItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str = None
            """
            Interface name
            """
            remote_as: Annotated[str, StrConvert(convert_types=(int))] | None = None
            """
            BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
            For asdot notation in YAML inputs, the value
            must be put in quotes, to prevent it from being interpreted as a float number.
            """
            peer: str | None = None
            """
            Key only used for documentation or validation purposes
            """
            peer_group: str | None = "Peer-group name"
            description: str | None = None
            peer_filter: str | None = None
            """
            Peer-filter name
            """

        class AggregateAddressesItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            prefix: str = None
            """
            IPv4 prefix "A.B.C.D/E" or IPv6 prefix "A:B:C:D:E:F:G:H/I"
            """
            advertise_only: bool | None = None
            as_set: bool | None = None
            advertise_map: str | None = None
            """
            Route-map name
            """
            supress_map: str | None = None
            """
            Route-map name
            """
            summary_only: bool | None = None
            attribute_map: str | None = None
            """
            Route-map name
            """
            match_map: str | None = None
            """
            Route-map name
            """

        class RedistributeRoutesItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            source_protocol: str = None
            route_map: str | None = None
            include_leaked: bool | None = None

        class VlanAwareBundlesItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class RdEvpnDomain(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                domain: Literal["remote", "all"] | None = None
                rd: str | None = None
                """
                Route distinguisher
                """

            class RouteTargets(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class ImportEvpnDomainsItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    domain: Literal["remote", "all"] | None = None
                    route_target: str | None = None

                class ExportEvpnDomainsItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    domain: Literal["remote", "all"] | None = None
                    route_target: str | None = None

                class ImportExportEvpnDomainsItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    domain: Literal["remote", "all"] | None = None
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

        class VlansItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class RdEvpnDomain(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                domain: Literal["remote", "all"] | None = None
                rd: str | None = None
                """
                Route distinguisher
                """

            class RouteTargets(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class ImportEvpnDomainsItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    domain: Literal["remote", "all"] | None = None
                    route_target: str | None = None

                class ExportEvpnDomainsItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    domain: Literal["remote", "all"] | None = None
                    route_target: str | None = None

                class ImportExportEvpnDomainsItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    domain: Literal["remote", "all"] | None = None
                    route_target: str | None = None

                both: list[str] | None = None
                field_import: list[str] | None = Field(None, alias="import")
                export: list[str] | None = None
                import_evpn_domains: list[ImportEvpnDomainsItem] | None = None
                export_evpn_domains: list[ExportEvpnDomainsItem] | None = None
                import_export_evpn_domains: list[ImportExportEvpnDomainsItem] | None = None

            id: Annotated[int, IntConvert(convert_types=(str))] = None
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

        class VpwsItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class RouteTargets(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                import_export: str | None = None
                """
                Route Target
                """

            class PseudowiresItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                name: str = None
                """
                Pseudowire name
                """
                id_local: Annotated[int, IntConvert(convert_types=(str))] | None = None
                """
                Must match id_remote on other pe
                """
                id_remote: Annotated[int, IntConvert(convert_types=(str))] | None = None
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
            mtu: Annotated[int, IntConvert(convert_types=(str))] | None = None
            pseudowires: list[PseudowiresItem] | None = None

        class AddressFamilyEvpn(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class NeighborDefault(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class NextHopSelfReceivedEvpnRoutes(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    enable: bool | None = None
                    inter_domain: bool | None = None

                encapsulation: Literal["vxlan", "mpls"] | None = None
                next_hop_self_source_interface: str | None = None
                """
                Source interface name
                """
                next_hop_self_received_evpn_routes: NextHopSelfReceivedEvpnRoutes | None = None

            class NextHopMplsResolutionRibsItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                rib_type: Literal["system-connected", "tunnel-rib-colored", "tunnel-rib"] = None
                """
                Type of RIB. For 'tunnel-rib', use 'rib_name' to specify the name of the Tunnel-RIB to use.
                """
                rib_name: str | None = None
                """
                The name of the tunnel-rib to use when using 'tunnel-rib' type.
                """

            class NeighborsItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                ip_address: str = None
                activate: bool | None = None

            class PeerGroupsItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class AdditionalPaths(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class Send(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        any: bool | None = None
                        backup: bool | None = None
                        ecmp: bool | None = None
                        ecmp_limit: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=2, le=64)
                        """
                        Amount of ECMP paths to send
                        """
                        limit: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=2, le=64)
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
                encapsulation: Literal["vxlan", "mpls"] | None = None
                additional_paths: AdditionalPaths | None = None

            class EvpnHostflapDetection(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                enabled: bool | None = None
                window: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=4294967295)
                """
                Time (in seconds) to detect a MAC duplication issue
                """
                threshold: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=4294967295)
                """
                Minimum number of MAC moves that indicate a MAC Duplication issue
                """
                expiry_timeout: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=4294967295)
                """
                Time (in seconds) to purge a MAC duplication issue
                """

            class NextHop(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                resolution_disabled: bool | None = None

            class Route(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                import_match_failure_action: Literal["discard"] | None = None
                import_ethernet_segment_ip_mass_withdraw: bool | None = None
                export_ethernet_segment_ip_mass_withdraw: bool | None = None

            domain_identifier: str | None = None
            neighbor_default: NeighborDefault | None = None
            next_hop_mpls_resolution_ribs: list[NextHopMplsResolutionRibsItem] | None = Field(None, min_length=1, max_length=3)
            """
            Specify the RIBs used to resolve MPLS next-hops. The order of this list determines the order of RIB lookups.
            """
            neighbors: list[NeighborsItem] | None = None
            peer_groups: list[PeerGroupsItem] | None = None
            evpn_hostflap_detection: EvpnHostflapDetection | None = None
            next_hop: NextHop | None = None
            route: Route | None = None
            next_hop_unchanged: bool | None = None

        class AddressFamilyRtc(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class PeerGroupsItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class DefaultRouteTarget(AvdDictBaseModel):
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

        class AddressFamilyIpv4(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class NetworksItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                prefix: str = None
                """
                IPv4 prefix "A.B.C.D/E" or IPv6 prefix "A:B:C:D:E:F:G:H/I"
                """
                route_map: str | None = None
                """
                Route-map name
                """

            class PeerGroupsItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class DefaultOriginate(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    always: bool | None = None
                    route_map: str | None = None
                    """
                    Route-map name
                    """

                class NextHop(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class AddressFamilyIpv6(AvdDictBaseModel):
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

            class NeighborsItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class DefaultOriginate(AvdDictBaseModel):
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

        class AddressFamilyIpv4Multicast(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class PeerGroupsItem(AvdDictBaseModel):
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

            class NeighborsItem(AvdDictBaseModel):
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

            class RedistributeRoutesItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                source_protocol: str = None
                route_map: str | None = None

            peer_groups: list[PeerGroupsItem] | None = None
            neighbors: list[NeighborsItem] | None = None
            redistribute_routes: list[RedistributeRoutesItem] | None = None

        class AddressFamilyIpv4SrTe(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class NeighborsItem(AvdDictBaseModel):
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

            class PeerGroupsItem(AvdDictBaseModel):
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

        class AddressFamilyIpv6(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class NetworksItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                prefix: str = None
                """
                IPv4 prefix "A.B.C.D/E" or IPv6 prefix "A:B:C:D:E:F:G:H/I"
                """
                route_map: str | None = None
                """
                Route-map name
                """

            class PeerGroupsItem(AvdDictBaseModel):
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

            class NeighborsItem(AvdDictBaseModel):
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

            class RedistributeRoutesItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                source_protocol: str = None
                route_map: str | None = None
                include_leaked: bool | None = None

            networks: list[NetworksItem] | None = None
            peer_groups: list[PeerGroupsItem] | None = None
            neighbors: list[NeighborsItem] | None = None
            redistribute_routes: list[RedistributeRoutesItem] | None = None

        class AddressFamilyIpv6Multicast(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Bgp(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class MissingPolicy(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    direction_in_action: Literal["deny", "deny-in-out", "permit"] | None = None
                    direction_out_action: Literal["deny", "deny-in-out", "permit"] | None = None

                class AdditionalPaths(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    receive: bool | None = None

                missing_policy: MissingPolicy | None = None
                additional_paths: AdditionalPaths | None = None

            class NeighborsItem(AvdDictBaseModel):
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

            class PeerGroupsItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                name: str = None
                """
                Peer-group name
                """
                activate: bool | None = None

            class NetworksItem(AvdDictBaseModel):
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

        class AddressFamilyIpv6SrTe(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class NeighborsItem(AvdDictBaseModel):
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

            class PeerGroupsItem(AvdDictBaseModel):
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

        class AddressFamilyLinkState(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Bgp(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class MissingPolicy(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    direction_in_action: Literal["deny", "deny-in-out", "permit"] | None = None
                    direction_out_action: Literal["deny", "deny-in-out", "permit"] | None = None

                missing_policy: MissingPolicy | None = None

            class PeerGroupsItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class MissingPolicy(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    direction_in_action: Literal["deny", "deny-in-out", "permit"] | None = None
                    direction_out_action: Literal["deny", "deny-in-out", "permit"] | None = None

                name: str = None
                """
                Peer-group name
                """
                activate: bool | None = None
                missing_policy: MissingPolicy | None = None

            class NeighborsItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class MissingPolicy(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    direction_in_action: Literal["deny", "deny-in-out", "permit"] | None = None
                    direction_out_action: Literal["deny", "deny-in-out", "permit"] | None = None

                ip_address: str = None
                activate: bool | None = None
                missing_policy: MissingPolicy | None = None

            class PathSelection(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Roles(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    producer: bool | None = None
                    consumer: bool | None = None
                    propagator: bool | None = None

                roles: Roles | None = None

            bgp: Bgp | None = None
            peer_groups: list[PeerGroupsItem] | None = None
            neighbors: list[NeighborsItem] | None = None
            path_selection: PathSelection | None = None

        class AddressFamilyFlowSpecIpv4(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Bgp(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class MissingPolicy(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    direction_in_action: Literal["deny", "deny-in-out", "permit"] | None = None
                    direction_out_action: Literal["deny", "deny-in-out", "permit"] | None = None

                missing_policy: MissingPolicy | None = None

            class NeighborsItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                ip_address: str = None
                activate: bool | None = None

            class PeerGroupsItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                name: str = None
                """
                Peer-group name
                """
                activate: bool | None = None

            bgp: Bgp | None = None
            neighbors: list[NeighborsItem] | None = None
            peer_groups: list[PeerGroupsItem] | None = None

        class AddressFamilyFlowSpecIpv6(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Bgp(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class MissingPolicy(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    direction_in_action: Literal["deny", "deny-in-out", "permit"] | None = None
                    direction_out_action: Literal["deny", "deny-in-out", "permit"] | None = None

                missing_policy: MissingPolicy | None = None

            class NeighborsItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                ip_address: str = None
                activate: bool | None = None

            class PeerGroupsItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                name: str = None
                """
                Peer-group name
                """
                activate: bool | None = None

            bgp: Bgp | None = None
            neighbors: list[NeighborsItem] | None = None
            peer_groups: list[PeerGroupsItem] | None = None

        class AddressFamilyPathSelection(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Bgp(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class AdditionalPaths(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class Send(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        any: bool | None = None
                        backup: bool | None = None
                        ecmp: bool | None = None
                        ecmp_limit: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=2, le=64)
                        """
                        Amount of ECMP paths to send
                        """
                        limit: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=2, le=64)
                        """
                        Amount of paths to send
                        """

                    receive: bool | None = None
                    send: Send | None = None

                additional_paths: AdditionalPaths | None = None

            class NeighborsItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class AdditionalPaths(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class Send(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        any: bool | None = None
                        backup: bool | None = None
                        ecmp: bool | None = None
                        ecmp_limit: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=2, le=64)
                        """
                        Amount of ECMP paths to send
                        """
                        limit: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=2, le=64)
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

            class PeerGroupsItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class AdditionalPaths(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class Send(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        any: bool | None = None
                        backup: bool | None = None
                        ecmp: bool | None = None
                        ecmp_limit: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=2, le=64)
                        """
                        Amount of ECMP paths to send
                        """
                        limit: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=2, le=64)
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

        class AddressFamilyVpnIpv4(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class PeerGroupsItem(AvdDictBaseModel):
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

            class Route(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                import_match_failure_action: Literal["discard"] | None = None

            class NeighborsItem(AvdDictBaseModel):
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

            class NeighborDefaultEncapsulationMplsNextHopSelf(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                source_interface: str | None = None

            domain_identifier: str | None = None
            peer_groups: list[PeerGroupsItem] | None = None
            route: Route | None = None
            neighbors: list[NeighborsItem] | None = None
            neighbor_default_encapsulation_mpls_next_hop_self: NeighborDefaultEncapsulationMplsNextHopSelf | None = None

        class AddressFamilyVpnIpv6(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class PeerGroupsItem(AvdDictBaseModel):
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

            class Route(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                import_match_failure_action: Literal["discard"] | None = None

            class NeighborsItem(AvdDictBaseModel):
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

            class NeighborDefaultEncapsulationMplsNextHopSelf(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                source_interface: str | None = None

            domain_identifier: str | None = None
            peer_groups: list[PeerGroupsItem] | None = None
            route: Route | None = None
            neighbors: list[NeighborsItem] | None = None
            neighbor_default_encapsulation_mpls_next_hop_self: NeighborDefaultEncapsulationMplsNextHopSelf | None = None

        class VrfsItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class EvpnMulticastAddressFamily(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Ipv4(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    transit: bool | None = None
                    """
                    Enable EVPN multicast transit mode
                    """

                ipv4: Ipv4 | None = None

            class RouteTargets(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class ImportItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    address_family: str = None
                    route_targets: list[str] | None = None
                    route_map: str | None = None

                class ExportItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    address_family: str = None
                    route_targets: list[str] | None = None
                    route_map: str | None = None

                field_import: list[ImportItem] | None = Field(None, alias="import")
                export: list[ExportItem] | None = None

            class NetworksItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                prefix: str = None
                """
                IPv4 prefix "A.B.C.D/E" or IPv6 prefix "A:B:C:D:E:F:G:H/I"
                """
                route_map: str | None = None

            class Updates(AvdDictBaseModel):
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

            class ListenRangesItem(AvdDictBaseModel):
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
                BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
                For asdot notation in YAML inputs, the value
                must be put in quotes, to prevent it from being interpreted as a float number.
                """

            class NeighborsItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class RemovePrivateAs(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    enabled: bool | None = None
                    all: bool | None = None
                    replace_as: bool | None = None

                class RemovePrivateAsIngress(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    enabled: bool | None = None
                    replace_as: bool | None = None

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

                class RibInPrePolicyRetain(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    enabled: bool | None = None
                    all: bool | None = None

                class AllowasIn(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    enabled: bool | None = None
                    times: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=10)
                    """
                    Number of local ASNs allowed in a BGP update
                    """

                class DefaultOriginate(AvdDictBaseModel):
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
                BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
                For asdot notation in YAML inputs, the value
                must be put in quotes, to prevent it from being interpreted as a float number.
                """
                password: str | None = None
                passive: bool | None = None
                remove_private_as: RemovePrivateAs | None = None
                """
                Remove private AS numbers in outbound AS path
                """
                remove_private_as_ingress: RemovePrivateAsIngress | None = None
                weight: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=65535)
                local_as: Annotated[str, StrConvert(convert_types=(int))] | None = None
                """
                BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
                For asdot notation in YAML inputs, the value
                must be put in quotes, to prevent it from being interpreted as a float number.
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
                """
                Enable BFD.
                """
                bfd_timers: BfdTimers | None = None
                """
                Override default BFD timers. BFD must be enabled with `bfd: true`.
                """
                timers: str | None = None
                """
                BGP Keepalive and Hold Timer values in seconds as string "<0-3600> <0-3600>"
                """
                rib_in_pre_policy_retain: RibInPrePolicyRetain | None = None
                send_community: str | None = None
                """
                'all' or a combination of 'standard', 'extended', 'large' and 'link-bandwidth (w/options)'
                """
                maximum_routes: Annotated[int, IntConvert(convert_types=(str))] | None = None
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

            class NeighborInterfacesItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                name: str = None
                """
                Interface name
                """
                remote_as: Annotated[str, StrConvert(convert_types=(int))] | None = None
                """
                BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
                For asdot notation in YAML inputs, the value
                must be put in quotes, to prevent it from being interpreted as a float number.
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

            class RedistributeRoutesItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                source_protocol: str = None
                route_map: str | None = None
                include_leaked: bool | None = None

            class AggregateAddressesItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                prefix: str = None
                """
                IPv4 prefix "A.B.C.D/E" or IPv6 prefix "A:B:C:D:E:F:G:H/I"
                """
                advertise_only: bool | None = None
                as_set: bool | None = None
                advertise_map: str | None = None
                """
                Route-map name
                """
                supress_map: str | None = None
                """
                Route-map name
                """
                summary_only: bool | None = None
                attribute_map: str | None = None
                match_map: str | None = None

            class AddressFamilyIpv4(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Bgp(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class MissingPolicy(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        direction_in_action: Literal["deny", "deny-in-out", "permit"] | None = None
                        direction_out_action: Literal["deny", "deny-in-out", "permit"] | None = None

                    class AdditionalPaths(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        class Send(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            any: bool | None = None
                            backup: bool | None = None
                            ecmp: bool | None = None
                            ecmp_limit: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=2, le=64)
                            """
                            Amount of ECMP paths to send
                            """
                            limit: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=2, le=64)
                            """
                            Amount of paths to send
                            """

                        install: bool | None = None
                        install_ecmp_primary: bool | None = None
                        receive: bool | None = None
                        send: Send | None = None

                    missing_policy: MissingPolicy | None = None
                    additional_paths: AdditionalPaths | None = None

                class NeighborsItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class NextHop(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        class AddressFamilyIpv6(AvdDictBaseModel):
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
                    prefix_list_in: str | None = None
                    """
                    Inbound prefix-list name
                    """
                    prefix_list_out: str | None = None
                    """
                    Outbound prefix-list name
                    """
                    next_hop: NextHop | None = None

                class NetworksItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    prefix: str = None
                    """
                    IPv4 prefix "A.B.C.D/E"
                    """
                    route_map: str | None = None

                bgp: Bgp | None = None
                neighbors: list[NeighborsItem] | None = None
                networks: list[NetworksItem] | None = None

            class AddressFamilyIpv6(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Bgp(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class MissingPolicy(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        direction_in_action: Literal["deny", "deny-in-out", "permit"] | None = None
                        direction_out_action: Literal["deny", "deny-in-out", "permit"] | None = None

                    class AdditionalPaths(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        class Send(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            any: bool | None = None
                            backup: bool | None = None
                            ecmp: bool | None = None
                            ecmp_limit: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=2, le=64)
                            """
                            Amount of ECMP paths to send
                            """
                            limit: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=2, le=64)
                            """
                            Amount of paths to send
                            """

                        install: bool | None = None
                        install_ecmp_primary: bool | None = None
                        receive: bool | None = None
                        send: Send | None = None

                    missing_policy: MissingPolicy | None = None
                    additional_paths: AdditionalPaths | None = None

                class NeighborsItem(AvdDictBaseModel):
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

                class NetworksItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    prefix: str = None
                    """
                    IPv6 prefix "A:B:C:D:E:F:G:H/I"
                    """
                    route_map: str | None = None

                bgp: Bgp | None = None
                neighbors: list[NeighborsItem] | None = None
                networks: list[NetworksItem] | None = None

            class AddressFamilyIpv4Multicast(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Bgp(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class MissingPolicy(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        direction_in_action: Literal["deny", "deny-in-out", "permit"] | None = None
                        direction_out_action: Literal["deny", "deny-in-out", "permit"] | None = None

                    class AdditionalPaths(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        receive: bool | None = None

                    missing_policy: MissingPolicy | None = None
                    additional_paths: AdditionalPaths | None = None

                class NeighborsItem(AvdDictBaseModel):
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

                class NetworksItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    prefix: str = None
                    """
                    IPv6 prefix "A.B.C.D/E"
                    """
                    route_map: str | None = None

                bgp: Bgp | None = None
                neighbors: list[NeighborsItem] | None = None
                networks: list[NetworksItem] | None = None

            class AddressFamilyIpv6Multicast(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Bgp(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class MissingPolicy(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        direction_in_action: Literal["deny", "deny-in-out", "permit"] | None = None
                        direction_out_action: Literal["deny", "deny-in-out", "permit"] | None = None

                    class AdditionalPaths(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        receive: bool | None = None

                    missing_policy: MissingPolicy | None = None
                    additional_paths: AdditionalPaths | None = None

                class NeighborsItem(AvdDictBaseModel):
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

                class NetworksItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    prefix: str = None
                    """
                    IPv6 prefix "A:B:C:D:E:F:G:H/I"
                    """
                    route_map: str | None = None

                bgp: Bgp | None = None
                neighbors: list[NeighborsItem] | None = None
                networks: list[NetworksItem] | None = None

            class AddressFamilyFlowSpecIpv4(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Bgp(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class MissingPolicy(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        direction_in_action: Literal["deny", "deny-in-out", "permit"] | None = None
                        direction_out_action: Literal["deny", "deny-in-out", "permit"] | None = None

                    missing_policy: MissingPolicy | None = None

                class NeighborsItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    ip_address: str = None
                    activate: bool | None = None

                bgp: Bgp | None = None
                neighbors: list[NeighborsItem] | None = None

            class AddressFamilyFlowSpecIpv6(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Bgp(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class MissingPolicy(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        direction_in_action: Literal["deny", "deny-in-out", "permit"] | None = None
                        direction_out_action: Literal["deny", "deny-in-out", "permit"] | None = None

                    missing_policy: MissingPolicy | None = None

                class NeighborsItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    ip_address: str = None
                    activate: bool | None = None

                bgp: Bgp | None = None
                neighbors: list[NeighborsItem] | None = None

            class AddressFamiliesItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Bgp(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class MissingPolicy(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        direction_in_action: Literal["deny", "deny-in-out", "permit"] | None = None
                        direction_out_action: Literal["deny", "deny-in-out", "permit"] | None = None

                    missing_policy: MissingPolicy | None = None
                    additional_paths: list[str] | None = None

                class NeighborsItem(AvdDictBaseModel):
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

                class PeerGroupsItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class NextHop(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        address_family_ipv6_originate: bool | None = None

                    name: str = None
                    """
                    Peer-group name
                    """
                    activate: bool | None = None
                    next_hop: NextHop | None = None

                class NetworksItem(AvdDictBaseModel):
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

        class SessionTrackersItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str = None
            """
            Name of session tracker
            """
            recovery_delay: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=3600)
            """
            Recovery delay in seconds
            """

        field_as: Annotated[str, StrConvert(convert_types=(int))] | None = Field(None, alias="as")
        """
        BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
        For asdot notation in YAML inputs, the value
        must be put in quotes, to prevent it from being interpreted as a float number.
        """
        as_notation: Literal["asdot", "asplain"] | None = Field(None, title="ASN Notation")
        """
        BGP AS can be deplayed in the asplain <1-4294967295> or asdot notation "<1-65535>.<0-65535>". This flag indicates which
        mode is preferred - asplain is the default.
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
        eos_cli: str | None = None
        """
        Multiline EOS CLI rendered directly on the Router BGP in the final EOS configuration.
        """

    class RouterGeneral(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class RouterId(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            ipv4: str | None = None
            """
            IPv4 Address
            """
            ipv6: str | None = None
            """
            IPv6 Address
            """

        class VrfsItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class LeakRoutesItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                source_vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
                subscribe_policy: str | None = None
                """
                Route-Map Policy
                """

            class Routes(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class DynamicPrefixListsItem(AvdDictBaseModel):
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

    class RouterIgmp(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class VrfsItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str = None
            """
            VRF name
            """
            host_proxy_match_mroute: Literal["all", "iif"] | None = None
            """
            Specify conditions for sending IGMP joins for host-proxy
            'iif' will enable igmp host-proxy to work in iif aware
            'all'
            will enable igmp host-proxy to work in iif unaware mode (EOS default)
            """

        host_proxy_match_mroute: Literal["all", "iif"] | None = None
        """
        Specify conditions for sending IGMP joins for host-proxy
        'iif' will enable igmp host-proxy to work in iif aware
        'all'
        will enable igmp host-proxy to work in iif unaware mode (EOS default)
        """
        ssm_aware: bool | None = None
        vrfs: list[VrfsItem] | None = None
        """
        Configure IGMP in a VRF.
        VRF 'default' is not supported in EOS, please see keys directly under 'router_igmp'.
        """

    class RouterIsis(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Timers(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class LocalConvergence(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                protected_prefixes: bool | None = None
                delay: Annotated[int, IntConvert(convert_types=(str))] | None = 10000
                """
                Delay in milliseconds.
                """

            local_convergence: LocalConvergence | None = None

        class SetOverloadBit(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class OnStartup(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class WaitForBgp(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    enabled: bool | None = None
                    timeout: Annotated[int, IntConvert(convert_types=(str))] | None = None
                    """
                    Number of seconds.
                    """

                delay: Annotated[int, IntConvert(convert_types=(str))] | None = None
                """
                Number of seconds.
                """
                wait_for_bgp: WaitForBgp | None = None

            enabled: bool | None = None
            on_startup: OnStartup | None = None

        class Authentication(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Both(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class KeyIdsItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    id: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=1, le=65535)
                    """
                    Configure authentication key-id.
                    """
                    algorithm: Literal["sha-1", "sha-224", "sha-256", "sha-384", "sha-512"] = None
                    key_type: Annotated[Literal["0", "7", "8a"], StrConvert(convert_types=(int))] = None
                    """
                    Configure authentication key type.
                    """
                    key: str = None
                    """
                    Password string.
                    """
                    rfc_5310: bool | None = None
                    """
                    SHA digest computation according to rfc5310.
                    """

                class Sha(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    key_id: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=1, le=65535)

                class SharedSecret(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    profile: str = None
                    algorithm: Literal["md5", "sha-1", "sha-224", "sha-256", "sha-384", "sha-512"] = None

                key_type: Annotated[Literal["0", "7", "8a"], StrConvert(convert_types=(int))] | None = None
                """
                Configure authentication key type. Default key_id is 0.
                """
                key: str | None = None
                """
                Password string.
                """
                key_ids: list[KeyIdsItem] | None = None
                mode: Literal["md5", "sha", "text", "shared_secret"] | None = None
                """
                Authentication mode.
                """
                sha: Sha | None = None
                """
                Required settings for authentication mode 'sha'.
                """
                shared_secret: SharedSecret | None = None
                """
                Required settings for authentication mode 'shared_secret'.
                """
                rx_disabled: bool | None = None

            class Level1(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class KeyIdsItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    id: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=1, le=65535)
                    """
                    Configure authentication key-id.
                    """
                    algorithm: Literal["sha-1", "sha-224", "sha-256", "sha-384", "sha-512"] = None
                    key_type: Annotated[Literal["0", "7", "8a"], StrConvert(convert_types=(int))] = None
                    """
                    Configure authentication key type.
                    """
                    key: str = None
                    """
                    Password string.
                    """
                    rfc_5310: bool | None = None
                    """
                    SHA digest computation according to rfc5310.
                    """

                class Sha(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    key_id: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=1, le=65535)

                class SharedSecret(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    profile: str = None
                    algorithm: Literal["md5", "sha-1", "sha-224", "sha-256", "sha-384", "sha-512"] = None

                key_type: Annotated[Literal["0", "7", "8a"], StrConvert(convert_types=(int))] | None = None
                """
                Configure authentication key type. Default key_id is 0.
                """
                key: str | None = None
                """
                Password string.
                """
                key_ids: list[KeyIdsItem] | None = None
                mode: Literal["md5", "sha", "text", "shared_secret"] | None = None
                """
                Authentication mode.
                """
                sha: Sha | None = None
                """
                Required settings for authentication mode 'sha'.
                """
                shared_secret: SharedSecret | None = None
                """
                Required settings for authentication mode 'shared_secret'.
                """
                rx_disabled: bool | None = None

            class Level2(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class KeyIdsItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    id: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=1, le=65535)
                    """
                    Configure authentication key-id.
                    """
                    algorithm: Literal["sha-1", "sha-224", "sha-256", "sha-384", "sha-512"] = None
                    key_type: Annotated[Literal["0", "7", "8a"], StrConvert(convert_types=(int))] = None
                    """
                    Configure authentication key type.
                    """
                    key: str = None
                    """
                    Password string.
                    """
                    rfc_5310: bool | None = None
                    """
                    SHA digest computation according to rfc5310.
                    """

                class Sha(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    key_id: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=1, le=65535)

                class SharedSecret(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    profile: str = None
                    algorithm: Literal["md5", "sha-1", "sha-224", "sha-256", "sha-384", "sha-512"] = None

                key_type: Annotated[Literal["0", "7", "8a"], StrConvert(convert_types=(int))] | None = None
                """
                Configure authentication key type. Default key_id is 0.
                """
                key: str | None = None
                """
                Password string.
                """
                key_ids: list[KeyIdsItem] | None = None
                mode: Literal["md5", "sha", "text", "shared_secret"] | None = None
                """
                Authentication mode.
                """
                sha: Sha | None = None
                """
                Required settings for authentication mode 'sha'.
                """
                shared_secret: SharedSecret | None = None
                """
                Required settings for authentication mode 'shared_secret'.
                """
                rx_disabled: bool | None = None

            both: Both | None = None
            """
            Authentication settings for level-1 and level-2. 'both' takes precedence over 'level_1' and 'level_2' settings.
            """
            level_1: Level1 | None = None
            """
            Authentication settings for level-1. 'both' takes precedence over 'level_1' and 'level_2' settings.
            """
            level_2: Level2 | None = None
            """
            Authentication settings for level-2. 'both' takes precedence over 'level_1' and 'level_2' settings.
            """

        class Advertise(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            passive_only: bool | None = None

        class RedistributeRoutesItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            source_protocol: Literal["bgp", "connected", "isis", "ospf", "ospfv3", "static"] = None
            route_map: str | None = None
            """
            Route-map name
            """
            include_leaked: bool | None = None
            ospf_route_type: Literal["external", "internal", "nssa-external"] | None = None
            """
            ospf_route_type is required with source_protocols 'ospf' and 'ospfv3'
            """

        class AddressFamilyIpv4(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class FastRerouteTiLfa(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Srlg(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    enable: bool | None = None
                    strict: bool | None = None

                mode: Literal["link-protection", "node-protection"] | None = None
                level: Literal["level-1", "level-2"] | None = None
                srlg: Srlg | None = None
                """
                Shared Risk Link Group
                """

            class TunnelSourceLabeledUnicast(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                enabled: bool | None = None
                rcf: str | None = None
                """
                Route Control Function
                """

            enabled: bool | None = None
            maximum_paths: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=128)
            bfd_all_interfaces: bool | None = None
            """
            Enable BFD on all interfaces.
            """
            fast_reroute_ti_lfa: FastRerouteTiLfa | None = None
            tunnel_source_labeled_unicast: TunnelSourceLabeledUnicast | None = None

        class AddressFamilyIpv6(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class FastRerouteTiLfa(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Srlg(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    enable: bool | None = None
                    strict: bool | None = None

                mode: Literal["link-protection", "node-protection"] | None = None
                level: Literal["level-1", "level-2"] | None = None
                """
                Optional, default is to protect all levels.
                """
                srlg: Srlg | None = None
                """
                Shared Risk Link Group
                """

            enabled: bool | None = None
            maximum_paths: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=128)
            bfd_all_interfaces: bool | None = None
            """
            Enable BFD on all interfaces.
            """
            fast_reroute_ti_lfa: FastRerouteTiLfa | None = None

        class SegmentRoutingMpls(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class PrefixSegmentsItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                prefix: str | None = None
                index: Annotated[int, IntConvert(convert_types=(str))] | None = None

            enabled: bool | None = None
            router_id: str | None = None
            prefix_segments: list[PrefixSegmentsItem] | None = None

        class SpfInterval(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            interval: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=300)
            """
            Maximum interval between two SPFs in seconds.
            """
            wait_interval: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=300000)
            """
            Initial wait interval for SPF in milliseconds.
            """

        class GracefulRestart(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class T2(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                level_1_wait_time: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=5, le=300)
                """
                Level-1 LSP database sync wait time in seconds.
                """
                level_2_wait_time: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=5, le=300)
                """
                Level-2 LSP database sync wait time in seconds.
                """

            enabled: bool | None = None
            restart_hold_time: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=5, le=300)
            """
            Number of seconds.
            """
            t2: T2 | None = None

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
        is_type: Literal["level-1", "level-1-2", "level-2"] | None = Field(None, title="IS Type")
        log_adjacency_changes: bool | None = None
        mpls_ldp_sync_default: bool | None = None
        timers: Timers | None = None
        set_overload_bit: SetOverloadBit | None = None
        authentication: Authentication | None = None
        advertise: Advertise | None = None
        address_family: list[str] | None = None
        isis_af_defaults: list[str] | None = None
        redistribute_routes: list[RedistributeRoutesItem] | None = None
        address_family_ipv4: AddressFamilyIpv4 | None = None
        address_family_ipv6: AddressFamilyIpv6 | None = None
        segment_routing_mpls: SegmentRoutingMpls | None = None
        spf_interval: SpfInterval | None = None
        graceful_restart: GracefulRestart | None = None
        eos_cli: str | None = None
        """
        Multiline EOS CLI rendered directly on the router isis in the final EOS configuration.
        """

    class RouterL2Vpn(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class ArpProxy(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            prefix_list: str | None = None
            """
            Prefix-list name. ARP Proxying is disabled for IPv4 addresses defined in the prefix-list.
            """

        class NdProxy(AvdDictBaseModel):
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

    class RouterMsdp(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class GroupLimitsItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            source_prefix: str = None
            """
            Source address prefix
            """
            limit: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=0, le=40000)
            """
            Limit for SAs matching the source address prefix
            """

        class PeersItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class DefaultPeer(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                enabled: bool | None = None
                prefix_list: str | None = None
                """
                Prefix list to filter source of SA messages
                """

            class MeshGroupsItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                name: str = None
                """
                Mesh group name
                """

            class Keepalive(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                keepalive_timer: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=1, le=65535)
                hold_timer: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=1, le=65535)
                """
                Must be greater than keepalive timer
                """

            class SaFilter(AvdDictBaseModel):
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
            sa_limit: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=40000)
            """
            Maximum number of SA messages allowed in cache
            """
            mesh_groups: list[MeshGroupsItem] | None = None
            keepalive: Keepalive | None = None
            sa_filter: SaFilter | None = None

        class VrfsItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class GroupLimitsItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                source_prefix: str = None
                """
                Source address prefix
                """
                limit: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=0, le=40000)
                """
                Limit for SAs matching the source address prefix
                """

            class PeersItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class DefaultPeer(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    enabled: bool | None = None
                    prefix_list: str | None = None
                    """
                    Prefix list to filter source of SA messages
                    """

                class MeshGroupsItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    name: str = None
                    """
                    Mesh group name
                    """

                class Keepalive(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    keepalive_timer: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=1, le=65535)
                    hold_timer: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=1, le=65535)
                    """
                    Must be greater than keepalive timer
                    """

                class SaFilter(AvdDictBaseModel):
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
                sa_limit: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=40000)
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
            rejected_limit: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=40000)
            """
            Maximum number of rejected SA messages allowed in cache
            """
            forward_register_packets: bool | None = None
            connection_retry_interval: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)
            group_limits: list[GroupLimitsItem] | None = None
            peers: list[PeersItem] | None = None

        originator_id_local_interface: str | None = None
        """
        Interface to use for originator ID
        """
        rejected_limit: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=40000)
        """
        Maximum number of rejected SA messages allowed in cache
        """
        forward_register_packets: bool | None = None
        connection_retry_interval: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)
        group_limits: list[GroupLimitsItem] | None = None
        peers: list[PeersItem] | None = None
        vrfs: list[VrfsItem] | None = None

    class RouterMulticast(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Ipv4(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Counters(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                rate_period_decay: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=600)
                """
                Rate in seconds
                """

            class Rpf(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class RoutesItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class DestinationsItem(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        nexthop: str = None
                        """
                        Next-hop IP address or interface name
                        """
                        distance: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=255)
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
            multipath: Literal["none", "deterministic", "deterministic color", "deterministic router-id"] | None = None
            software_forwarding: Literal["kernel", "sfe"] | None = None
            rpf: Rpf | None = None

        class VrfsItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Ipv4(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                routing: bool | None = None

            name: Annotated[str, StrConvert(convert_types=(int))] = None
            ipv4: Ipv4 | None = None

        ipv4: Ipv4 | None = None
        vrfs: list[VrfsItem] | None = None

    class RouterOspf(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class ProcessIdsItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Distance(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                external: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=255)
                inter_area: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=255)
                intra_area: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=255)

            class NetworkPrefixesItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                ipv4_prefix: str = None
                area: str | None = None

            class DistributeListIn(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                route_map: str | None = None

            class Timers(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Lsa(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class TxDelay(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        initial: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=600000)
                        """
                        Delay to generate first occurrence of LSA in msecs
                        """
                        min: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=600000)
                        """
                        Min delay between originating the same LSA in msecs
                        """
                        max: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=600000)
                        """
                        1-600000 Maximum delay between originating the same LSA in msec
                        """

                    rx_min_interval: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=600000)
                    """
                    Min interval in msecs between accepting the same LSA
                    """
                    tx_delay: TxDelay | None = None

                class SpfDelay(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    initial: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=600000)
                    """
                    Initial SPF schedule delay in msecs
                    """
                    min: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=65535000)
                    """
                    Min Hold time between two SPFs in msecs
                    """
                    max: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=65535000)
                    """
                    Max wait time between two SPFs in msecs
                    """

                lsa: Lsa | None = None
                spf_delay: SpfDelay | None = None

            class DefaultInformationOriginate(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                always: bool | None = None
                metric: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)
                """
                Metric for default route
                """
                metric_type: Annotated[Literal[1, 2], IntConvert(convert_types=(str))] | None = None
                """
                OSPF metric type for default route
                """

            class SummaryAddressesItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                prefix: str = None
                """
                Summary Prefix Address
                """
                tag: int | None = None
                attribute_map: str | None = None
                not_advertise: bool | None = None

            class Redistribute(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Static(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    route_map: str | None = None
                    """
                    Route Map Name
                    """
                    include_leaked: bool | None = None

                class Connected(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    route_map: str | None = None
                    """
                    Route Map Name
                    """
                    include_leaked: bool | None = None

                class Bgp(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    route_map: str | None = None
                    """
                    Route Map Name
                    """
                    include_leaked: bool | None = None

                static: Static | None = None
                connected: Connected | None = None
                bgp: Bgp | None = None

            class AreasItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Filter(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    networks: list[str] | None = None
                    prefix_list: str | None = None
                    """
                    Prefix-List Name
                    """

                class DefaultInformationOriginate(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    metric: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)
                    """
                    Metric for default route
                    """
                    metric_type: Annotated[Literal[1, 2], IntConvert(convert_types=(str))] | None = None
                    """
                    OSPF metric type for default route
                    """

                id: Annotated[str, StrConvert(convert_types=(int))] = None
                filter: Filter | None = None
                type: Literal["normal", "stub", "nssa"] | None = "normal"
                no_summary: bool | None = None
                nssa_only: bool | None = None
                default_information_originate: DefaultInformationOriginate | None = None

            class MaxMetric(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class RouterLsa(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class ExternalLsa(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        override_metric: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=16777215)

                    class SummaryLsa(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        override_metric: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=16777215)

                    external_lsa: ExternalLsa | None = None
                    include_stub: bool | None = None
                    on_startup: Annotated[str, StrConvert(convert_types=(int))] | None = None
                    """
                    "wait-for-bgp" or Integer 5-86400
                    Example: "wait-for-bgp" Or "222"
                    """
                    summary_lsa: SummaryLsa | None = None

                router_lsa: RouterLsa | None = None

            id: Annotated[int, IntConvert(convert_types=(str))] = None
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
            max_lsa: Annotated[int, IntConvert(convert_types=(str))] | None = None
            timers: Timers | None = None
            default_information_originate: DefaultInformationOriginate | None = None
            summary_addresses: list[SummaryAddressesItem] | None = None
            redistribute: Redistribute | None = None
            auto_cost_reference_bandwidth: Annotated[int, IntConvert(convert_types=(str))] | None = None
            """
            Bandwidth in mbps
            """
            areas: list[AreasItem] | None = None
            maximum_paths: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=128)
            max_metric: MaxMetric | None = None
            mpls_ldp_sync_default: bool | None = None
            eos_cli: str | None = None
            """
            Multiline EOS CLI rendered directly on the Router OSPF process ID in the final EOS configuration
            """

        process_ids: list[ProcessIdsItem] | None = None

    class RouterPathSelection(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class PathGroupsItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class LocalInterfacesItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Stun(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    server_profiles: list[str] = Field(None, min_length=1, max_length=12)
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

            class LocalIpsItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Stun(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    server_profiles: list[str] = Field(None, min_length=1, max_length=12)
                    """
                    STUN server-profile names.
                    """

                ip_address: str = None
                public_address: str | None = None
                """
                Public IP assigned by NAT.
                """
                stun: Stun | None = None

            class DynamicPeers(AvdDictBaseModel):
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

            class StaticPeersItem(AvdDictBaseModel):
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

            class Keepalive(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                auto: bool | None = False
                """
                Enable adaptive keepalive and feedback interval.
                """
                interval: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=50, le=60000)
                """
                Interval in milliseconds.
                """
                failure_threshold: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=2, le=100)
                """
                Failure threshold in number of intervals. Required when `interval` is set.
                """

            name: str = None
            """
            Path group name.
            """
            id: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)
            """
            Path group ID.
            """
            ipsec_profile: str | None = None
            """
            IPSec profile for the path group.
            """
            flow_assignment: Literal["lan"] | None = None
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
            keepalive: Keepalive | None = None

        class LoadBalancePoliciesItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class PathGroupsItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                name: str = None
                """
                Path-group name
                """
                priority: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)
                """
                Priority for this path-group.
                The EOS default value is 1.
                """

            name: str = None
            """
            Load-balance policy name.
            """
            lowest_hop_count: bool | None = None
            """
            Prefer paths with lowest hop-count.
            """
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
            path_groups: list[PathGroupsItem] | None = None
            """
            List of path-groups to use for this load balance policy.
            """

        class PoliciesItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class DefaultMatch(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                load_balance: str | None = None
                """
                Name of the load-balance policy.
                """

            class RulesItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                id: Annotated[int, IntConvert(convert_types=(str))] = Field(None, ge=1, le=255)
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

        class VrfsItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str = None
            """
            VRF name.
            """
            path_selection_policy: str | None = None
            """
            DPS policy name to use for this VRF.
            """

        class TcpMssCeiling(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            ipv4_segment_size: Annotated[str, StrConvert(convert_types=(int))] | None = None
            """
            Segment Size for IPv4.
            Can be an integer in the range 64-65515 or "auto".
            "auto" will enable auto-discovery which clamps
            the TCP MSS value to the minimum of all the direct paths
            and multi-hop path MTU towards a remote VTEP (minus 40bytes to
            account for IP + TCP header).
            """
            direction: Literal["ingress"] | None = "ingress"
            """
            Enforce on packets through DPS tunnel for a specific direction.
            Only 'ingress' direction is supported.
            """

        peer_dynamic_source: Literal["stun"] | None = None
        """
        Source of dynamic peer discovery.
        """
        path_groups: list[PathGroupsItem] | None = None
        load_balance_policies: list[LoadBalancePoliciesItem] | None = None
        policies: list[PoliciesItem] | None = None
        vrfs: list[VrfsItem] | None = None
        tcp_mss_ceiling: TcpMssCeiling | None = None

    class RouterPimSparseMode(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Ipv4(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class RpAddressesItem(AvdDictBaseModel):
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

            class AnycastRpsItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class OtherAnycastRpAddressesItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    address: str = None
                    """
                    Other Anycast RP Address
                    """
                    register_count: Annotated[int, IntConvert(convert_types=(str))] | None = None

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

        class VrfsItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Ipv4(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class RpAddressesItem(AvdDictBaseModel):
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

    class RouterServiceInsertion(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class ConnectionsItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class EthernetInterface(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                name: str = None
                """
                e.g. Ethernet2 or Ethernet2/2.2
                """
                next_hop: str = None
                """
                Next-hop IPv4 address (without mask).
                """

            class TunnelInterface(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                primary: str | None = None
                """
                e.g. Tunnel2
                """
                secondary: str | None = None
                """
                e.g. Tunnel3
                """

            name: str = None
            """
            Connection name.
            """
            ethernet_interface: EthernetInterface | None = None
            """
            Outgoing physical interface or subinterface to use for the connection.
            If both `ethernet_interface` and
            `tunnel_interface` are configured, `ethernet_interface` will be used.
            """
            tunnel_interface: TunnelInterface | None = None
            """
            Outgoing tunnel interface(s) to use for this connection.
            If both `ethernet_interface` and `tunnel_interface` are
            configured, `ethernet_interface` will be used.
            """
            monitor_connectivity_host: str | None = None
            """
            Name of the host defined under `monitor_connectivity.hosts` used to derive the health of the connection.
            """

        enabled: bool | None = None
        connections: list[ConnectionsItem] | None = None

    class RouterTrafficEngineering(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class RouterId(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            ipv4: str | None = None
            ipv6: str | None = None

        class SegmentRouting(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class PolicyEndpointsItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class ColorsItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    class PathGroupItem(AvdDictBaseModel):
                        model_config = ConfigDict(defer_build=True, extra="forbid")

                        class SegmentListItem(AvdDictBaseModel):
                            model_config = ConfigDict(defer_build=True, extra="forbid")

                            label_stack: Annotated[str, StrConvert(convert_types=(int))] | None = None
                            """
                            Label Stack as string.
                            Example: "100 2000 30"
                            """
                            weight: Annotated[int, IntConvert(convert_types=(str))] | None = None
                            index: Annotated[int, IntConvert(convert_types=(str))] | None = None

                        preference: Annotated[int, IntConvert(convert_types=(str))] | None = None
                        explicit_null: Literal["ipv4", "ipv6", "ipv4 ipv6", "none"] | None = None
                        segment_list: list[SegmentListItem] | None = None

                    value: Annotated[int, IntConvert(convert_types=(str))] = None
                    binding_sid: Annotated[int, IntConvert(convert_types=(str))] | None = None
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

    class ServiceRoutingConfigurationBgp(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        no_equals_default: bool | None = None

    class ServiceUnsupportedTransceiver(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        license_name: str | None = None
        license_key: str | None = None

    class Sflow(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class VrfsItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class DestinationsItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                destination: str = None
                """
                Sflow Destination IP Address
                """
                port: Annotated[int, IntConvert(convert_types=(str))] | None = None
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

        class DestinationsItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            destination: str = None
            """
            Sflow Destination IP Address
            """
            port: Annotated[int, IntConvert(convert_types=(str))] | None = None
            """
            Port Number
            """

        class ExtensionsItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str = None
            """
            Extension Name
            """
            enabled: bool = None
            """
            Enable or Disable Extension
            """

        class Interface(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Disable(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                default: bool | None = None

            class Egress(AvdDictBaseModel):
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

        class HardwareAcceleration(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class ModulesItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                name: str = None
                enabled: bool | None = True

            enabled: bool | None = None
            sample: Annotated[int, IntConvert(convert_types=(str))] | None = None
            modules: list[ModulesItem] | None = None

        sample: Annotated[int, IntConvert(convert_types=(str))] | None = None
        sample_input_subinterface: bool | None = None
        sample_output_subinterface: bool | None = None
        dangerous: bool | None = None
        polling_interval: Annotated[int, IntConvert(convert_types=(str))] | None = None
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

    class SnmpServer(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class EngineIds(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class RemotesItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                id: Annotated[str, StrConvert(convert_types=(int))] | None = None
                """
                Remote engine ID in hexadecimal
                """
                address: str | None = None
                """
                Hostname or IP of remote engine
                """
                udp_port: Annotated[int, IntConvert(convert_types=(str))] | None = None

            local: Annotated[str, StrConvert(convert_types=(int))] | None = None
            """
            Engine ID in hexadecimal
            """
            remotes: list[RemotesItem] | None = None

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

        class LocalInterfacesItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            name: str = None
            """
            Interface name
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
            remote_address: str | None = None
            """
            Hostname or ip of remote engine
            The remote_address and udp_port are used for remote users
            """
            udp_port: Annotated[int, IntConvert(convert_types=(str))] | None = None
            """
            udp_port will not be used if no remote_address is configured
            """
            version: Literal["v1", "v2c", "v3"] | None = None
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
            vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
            version: Annotated[Literal["1", "2c", "3"], StrConvert(convert_types=(int))] | None = None
            community: str | None = None
            """
            Community name
            """
            users: list[UsersItem] | None = None

        class Traps(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class SnmpTrapsItem(AvdDictBaseModel):
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

        class VrfsItem(AvdDictBaseModel):
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

    class SpanningTree(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class EdgePort(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            bpdufilter_default: bool | None = None
            bpduguard_default: bool | None = None

        class BpduguardRateLimit(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            default: bool | None = None
            count: Annotated[int, IntConvert(convert_types=(str))] | None = None
            """
            Maximum number of BPDUs per timer interval
            """

        class Mst(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Configuration(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class InstancesItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    id: Annotated[int, IntConvert(convert_types=(str))] = None
                    """
                    Instance ID
                    """
                    vlans: Annotated[str, StrConvert(convert_types=(int))] | None = None
                    """
                    "< vlan_id >, < vlan_id >-< vlan_id >"
                    Example: 15,16,17,18
                    """

                name: str | None = None
                revision: Annotated[int, IntConvert(convert_types=(str))] | None = None
                """
                0-65535
                """
                instances: list[InstancesItem] | None = None

            pvst_border: bool | None = None
            configuration: Configuration | None = None

        class MstInstancesItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            id: Annotated[str, StrConvert(convert_types=(int))] = None
            """
            Instance ID
            """
            priority: Annotated[int, IntConvert(convert_types=(str))] | None = None

        class RapidPvstInstancesItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            id: Annotated[str, StrConvert(convert_types=(int))] = None
            """
            "< vlan_id >, < vlan_id >-< vlan_id >"
            Example: 105,202,505-506
            """
            priority: Annotated[int, IntConvert(convert_types=(str))] | None = None

        root_super: bool | None = None
        edge_port: EdgePort | None = None
        mode: Literal["mstp", "rstp", "rapid-pvst", "none"] | None = None
        bpduguard_rate_limit: BpduguardRateLimit | None = None
        rstp_priority: Annotated[int, IntConvert(convert_types=(str))] | None = None
        mst: Mst | None = None
        mst_instances: list[MstInstancesItem] | None = None
        no_spanning_tree_vlan: Annotated[str, StrConvert(convert_types=(int))] | None = None
        """
        "< vlan_id >, < vlan_id >-< vlan_id >"
        Example: 105,202,505-506
        """
        rapid_pvst_instances: list[RapidPvstInstancesItem] | None = None

    class StandardAccessListsItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class SequenceNumbersItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            sequence: Annotated[int, IntConvert(convert_types=(str))] = None
            """
            Sequence ID
            """
            action: str = None
            """
            Action as string
            Example: "deny ip any any"
            """

        name: Annotated[str, StrConvert(convert_types=(int))] = None
        """
        Access-list Name
        """
        counters_per_entry: bool | None = None
        sequence_numbers: list[SequenceNumbersItem] = None

    class StaticRoutesItem(AvdDictBaseModel):
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
        distance: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=255)
        tag: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=4294967295)
        name: str | None = None
        """
        Description
        """
        metric: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=4294967295)

    class Stun(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Client(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class ServerProfilesItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                name: str = None
                ip_address: str | None = None
                ssl_profile: str | None = None
                """
                SSL profile name.
                """
                port: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)
                """
                Destination port for the request STUN server (default - 3478).
                """

            server_profiles: list[ServerProfilesItem] | None = None
            """
            List of server profiles for the client.
            """

        class Server(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class SslConnectionLifetime(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                minutes: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=1440)
                """
                SSL connection lifetime in minutes (default - 120).
                """
                hours: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=24)
                """
                SSL connection lifetime in hours (default - 2).
                """

            local_interface: str | None = None
            local_interfaces: list[str] | None = Field(None, min_length=1)
            bindings_timeout: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=10, le=7200)
            """
            Timeout for bindings stored on STUN server in seconds.
            """
            ssl_profile: str | None = None
            """
            SSL profile name.
            """
            ssl_connection_lifetime: SslConnectionLifetime | None = None
            """
            SSL connection lifetime in minutes or hours.
            If both are specified, minutes is given higher precedence.
            """
            port: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)
            """
            Listening port for STUN server (default - 3478).
            """

        client: Client | None = None
        """
        STUN client settings.
        """
        server: Server | None = None
        """
        STUN server settings.
        """

    class SwitchportDefault(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Phone(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            cos: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=7)
            trunk: Literal["tagged", "untagged"] | None = None
            vlan: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=4094)
            """
            VLAN ID
            """

        mode: Literal["routed", "access"] | None = None
        phone: Phone | None = None

    class SwitchportPortSecurity(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class MacAddress(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            aging: bool | None = None
            moveable: bool | None = None

        mac_address: MacAddress | None = None
        persistence_disabled: bool | None = None
        violation_protect_chip_based: bool | None = None

    class System(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class ControlPlane(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class TcpMss(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                ipv4: int | None = None
                """
                Segment size
                """
                ipv6: int | None = None
                """
                Segment size
                """

            class Ipv4AccessGroupsItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                acl_name: str = None
                vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None

            class Ipv6AccessGroupsItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                acl_name: str = None
                vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None

            tcp_mss: TcpMss | None = None
            ipv4_access_groups: list[Ipv4AccessGroupsItem] | None = None
            ipv6_access_groups: list[Ipv6AccessGroupsItem] | None = None

        class L1(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            unsupported_speed_action: Literal["error", "warn"] | None = None
            unsupported_error_correction_action: Literal["error", "warn"] | None = None

        control_plane: ControlPlane | None = None
        l1: L1 | None = None

    class TacacsServers(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class HostsItem(AvdDictBaseModel):
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
            key_type: Annotated[Literal["0", "7", "8a"], StrConvert(convert_types=(int))] | None = "7"
            single_connection: bool | None = None
            timeout: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=1000)
            """
            Timeout in seconds
            """

        timeout: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=1000)
        """
        Timeout in seconds
        """
        hosts: list[HostsItem] | None = None
        policy_unknown_mandatory_attribute_ignore: bool | None = None

    class TapAggregation(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Mode(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Exclusive(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                enabled: bool | None = None
                profile: str | None = None
                """
                Profile Name
                """
                no_errdisable: list[str] | None = None

            exclusive: Exclusive | None = None

        class Mac(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Timestamp(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Header(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    format: Literal["48-bit", "64-bit"] | None = None
                    eth_type: Annotated[int, IntConvert(convert_types=(str))] | None = None
                    """
                    EtherType
                    """

                replace_source_mac: bool | None = None
                header: Header | None = None

            timestamp: Timestamp | None = None
            """
            mac.timestamp.replace_source_mac and mac.timestamp.header.format are mutually exclsuive. If both are defined,
            replace_source_mac takes precedence
            """
            fcs_append: bool | None = None
            """
            mac.fcs_append and mac.fcs_error are mutually exclusive. If both are defined, mac.fcs_append takes precedence
            """
            fcs_error: Literal["correct", "discard", "pass-through"] | None = None

        mode: Mode | None = None
        encapsulation_dot1br_strip: bool | None = None
        encapsulation_vn_tag_strip: bool | None = None
        protocol_lldp_trap: bool | None = None
        truncation_size: int | None = None
        """
        Allowed truncation_size values vary depending on the platform
        """
        mac: Mac | None = None

    class TcamProfile(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class ProfilesItem(AvdDictBaseModel):
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

    class Terminal(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        length: int | None = Field(None, ge=0, le=32767)
        width: int | None = Field(None, ge=10, le=32767)

    class TrackersItem(AvdDictBaseModel):
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

    class TrafficPolicies(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Options(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            counter_per_interface: bool | None = None

        class FieldSets(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Ipv4Item(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                name: str = None
                """
                IPv4 Prefix Field Set Name
                """
                prefixes: list[str] | None = None

            class Ipv6Item(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                name: str = None
                """
                IPv6 Prefix Field Set Name
                """
                prefixes: list[str] | None = None

            class PortsItem(AvdDictBaseModel):
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

        class PoliciesItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class MatchesItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Source(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    prefixes: list[str] | None = None
                    prefix_lists: list[str] | None = None
                    """
                    Field-set prefix lists
                    """

                class Destination(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    prefixes: list[str] | None = None
                    prefix_lists: list[str] | None = None
                    """
                    Field-set prefix lists
                    """

                class Fragment(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    offset: str | None = None
                    """
                    Fragment offset range
                    """

                class ProtocolsItem(AvdDictBaseModel):
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

                class Actions(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    dscp: Annotated[int, IntConvert(convert_types=(str))] | None = None
                    traffic_class: Annotated[int, IntConvert(convert_types=(str))] | None = None
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
                type: Literal["ipv4", "ipv6"] | None = None
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

            class DefaultActions(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Ipv4(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    dscp: Annotated[int, IntConvert(convert_types=(str))] | None = None
                    traffic_class: Annotated[int, IntConvert(convert_types=(str))] | None = None
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

                class Ipv6(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    dscp: Annotated[int, IntConvert(convert_types=(str))] | None = None
                    traffic_class: Annotated[int, IntConvert(convert_types=(str))] | None = None
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

    class TunnelInterfacesItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class TcpMssCeiling(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            ipv4: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=64, le=65495)
            """
            Segment Size for IPv4
            """
            ipv6: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=64, le=65475)
            """
            Segment Size for IPv6
            """
            direction: Literal["ingress", "egress"] | None = None
            """
            Optional direction ('ingress', 'egress')  for tcp mss ceiling
            """

        name: str = None
        """
        Tunnel Interface Name
        """
        description: str | None = None
        shutdown: bool | None = None
        mtu: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=68, le=65535)
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

    class VirtualSourceNatVrfsItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        name: Annotated[str, StrConvert(convert_types=(int))] = None
        """
        VRF Name
        """
        ip_address: str | None = None
        """
        IPv4 Address
        """

    class VlanInterfacesItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Logging(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Event(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                link_status: bool | None = None

            event: Event | None = None

        class IpIgmpHostProxy(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class GroupsItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class ExcludeItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    source: str = None

                class IncludeItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    source: str = None

                group: str = None
                """
                Multicast Address.
                """
                exclude: list[ExcludeItem] | None = None
                """
                The same source must not be present both in `exclude` and `include` list.
                """
                include: list[IncludeItem] | None = None
                """
                The same source must not be present both in `exclude` and `include` list.
                """

            class AccessListsItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                name: str = None

            enabled: bool | None = None
            groups: list[GroupsItem] | None = None
            report_interval: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=31744)
            """
            Time interval between unsolicited reports.
            """
            access_lists: list[AccessListsItem] | None = None
            """
            Non-standard Access List name.
            """
            version: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=3)
            """
            IGMP version on IGMP host-proxy interface.
            """

        class IpHelpersItem(AvdDictBaseModel):
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

        class IpNat(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Destination(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class DynamicItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    access_list: str = None
                    comment: str | None = None
                    pool_name: str = None
                    priority: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=4294967295)

                class StaticItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    access_list: str | None = None
                    """
                    'access_list' and 'group' are mutual exclusive
                    """
                    comment: str | None = None
                    direction: Literal["egress", "ingress"] | None = None
                    """
                    Egress or ingress can be the default. This depends on source/destination, EOS version, and hardware platform.
                    EOS might
                    remove this keyword in the configuration. So, check the configuration on targeted HW/SW.
                    """
                    group: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)
                    """
                    'access_list' and 'group' are mutual exclusive
                    """
                    original_ip: str = None
                    """
                    IPv4 address
                    """
                    original_port: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)
                    priority: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=4294967295)
                    protocol: Literal["udp", "tcp"] | None = None
                    translated_ip: str = None
                    """
                    IPv4 address
                    """
                    translated_port: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)
                    """
                    requires 'original_port'
                    """

                dynamic: list[DynamicItem] | None = None
                static: list[StaticItem] | None = None

            class Source(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class DynamicItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    access_list: str = None
                    comment: str | None = None
                    nat_type: Literal["overload", "pool", "pool-address-only", "pool-full-cone"] = None
                    pool_name: str | None = None
                    """
                    required if 'nat_type' is pool, pool-address-only or pool-full-cone
                    ignored if 'nat_type' is overload
                    """
                    priority: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=4294967295)

                class StaticItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    access_list: str | None = None
                    """
                    'access_list' and 'group' are mutual exclusive
                    """
                    comment: str | None = None
                    direction: Literal["egress", "ingress"] | None = None
                    """
                    Egress or ingress can be the default. This depends on source/destination, EOS version, and hardware platform.
                    EOS might
                    remove this keyword in the configuration. So, check the configuration on targeted HW/SW.
                    """
                    group: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)
                    """
                    'access_list' and 'group' are mutual exclusive
                    """
                    original_ip: str = None
                    """
                    IPv4 address
                    """
                    original_port: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)
                    priority: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=4294967295)
                    protocol: Literal["udp", "tcp"] | None = None
                    translated_ip: str = None
                    """
                    IPv4 address
                    """
                    translated_port: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)
                    """
                    requires 'original_port'
                    """

                dynamic: list[DynamicItem] | None = None
                static: list[StaticItem] | None = None

            destination: Destination | None = None
            source: Source | None = None

        class Ipv6NdPrefixesItem(AvdDictBaseModel):
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

        class Ipv6DhcpRelayDestinationsItem(AvdDictBaseModel):
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

        class Multicast(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Ipv4(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class BoundariesItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    boundary: Annotated[str, StrConvert(convert_types=(int))] = None
                    """
                    IPv4 access-list name or IPv4 multicast group prefix with mask
                    """
                    out: bool | None = None

                class SourceRouteExport(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    enabled: bool = None
                    administrative_distance: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=255)

                boundaries: list[BoundariesItem] | None = None
                """
                Boundaries can be either 1 ACL or a list of multicast IP address_range(s)/prefix but not combination of both
                """
                source_route_export: SourceRouteExport | None = None
                static: bool | None = None

            class Ipv6(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class BoundariesItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    boundary: Annotated[str, StrConvert(convert_types=(int))] = None
                    """
                    IPv6 access-list name or IPv6 multicast group prefix with mask
                    """

                class SourceRouteExport(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    enabled: bool = None
                    administrative_distance: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=255)

                boundaries: list[BoundariesItem] | None = None
                """
                Boundaries can be either 1 ACL or a list of multicast IP address_range(s)/prefix but not combination of both
                """
                source_route_export: SourceRouteExport | None = None
                static: bool | None = None

            ipv4: Ipv4 | None = None
            ipv6: Ipv6 | None = None

        class OspfMessageDigestKeysItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            id: Annotated[int, IntConvert(convert_types=(str))] = None
            hash_algorithm: Literal["md5", "sha1", "sha256", "sha384", "sha512"] | None = None
            key: str | None = None
            """
            Encrypted password
            """

        class Pim(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Ipv4(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Hello(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    count: Annotated[str, StrConvert(convert_types=(int, float))] | None = None
                    """
                    Number of missed hellos after which the neighbor expires. Range <1.5-65535>.
                    """
                    interval: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)
                    """
                    PIM hello interval in seconds.
                    """

                border_router: bool | None = None
                """
                Configure PIM border router. EOS default is false.
                """
                dr_priority: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=429467295)
                sparse_mode: bool | None = None
                local_interface: str | None = None
                bfd: bool | None = None
                """
                Set the default for whether Bidirectional Forwarding Detection is enabled for PIM.
                """
                bidirectional: bool | None = None
                hello: Hello | None = None

            ipv4: Ipv4 | None = None

        class VrrpIdsItem(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Advertisement(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                interval: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=255)
                """
                Interval in seconds
                """

            class Preempt(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Delay(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    minimum: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=3600)
                    """
                    Minimum preempt delay in seconds
                    """
                    reload: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=3600)
                    """
                    Reload preempt delay in seconds
                    """

                enabled: bool = None
                delay: Delay | None = None

            class Timers(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Delay(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    reload: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=3600)
                    """
                    Delay after reload in seconds.
                    """

                delay: Delay | None = None

            class TrackedObjectItem(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                name: str = None
                """
                Tracked object name
                """
                decrement: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=254)
                """
                Decrement VRRP priority by 1-254
                """
                shutdown: bool | None = None

            class Ipv4(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                address: str = None
                """
                Virtual IPv4 address
                """
                version: Annotated[Literal[2, 3], IntConvert(convert_types=(str))] | None = None

            class Ipv6(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                address: str = None
                """
                Virtual IPv6 address
                """

            id: Annotated[int, IntConvert(convert_types=(str))] = None
            """
            VRID
            """
            priority_level: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=254)
            """
            Instance priority
            """
            advertisement: Advertisement | None = None
            preempt: Preempt | None = None
            timers: Timers | None = None
            tracked_object: list[TrackedObjectItem] | None = None
            ipv4: Ipv4 | None = None
            ipv6: Ipv6 | None = None

        class Vrrp(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            virtual_router: str | None = None
            """
            Virtual Router ID
            """
            priority: Annotated[int, IntConvert(convert_types=(str))] | None = None
            """
            Instance priority
            """
            advertisement_interval: Annotated[int, IntConvert(convert_types=(str))] | None = None
            preempt_delay_minimum: Annotated[int, IntConvert(convert_types=(str))] | None = None
            ipv4: str | None = None
            """
            Virtual IPv4 address
            """
            ipv6: str | None = None
            """
            Virtual IPv6 address
            """

        class IpAttachedHostRouteExport(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            enabled: bool = None
            distance: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=255)

        class Ipv6AttachedHostRouteExport(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            enabled: bool = None
            distance: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=255)
            """
            Administrative distance for generated routes.
            """
            prefix_length: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=128)
            """
            Prefix length for generated routes.
            """

        class Bfd(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            echo: bool | None = None
            interval: Annotated[int, IntConvert(convert_types=(str))] | None = None
            """
            Rate in milliseconds
            """
            min_rx: Annotated[int, IntConvert(convert_types=(str))] | None = None
            """
            Minimum RX hold time in milliseconds
            """
            multiplier: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=3, le=50)

        class ServicePolicy(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Pbr(AvdDictBaseModel):
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
        logging: Logging | None = None
        shutdown: bool | None = None
        vrf: Annotated[str, StrConvert(convert_types=(int))] | None = None
        """
        VRF name
        """
        arp_aging_timeout: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=65535)
        """
        In seconds
        """
        arp_cache_dynamic_capacity: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=0, le=4294967295)
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
        ip_verify_unicast_source_reachable_via: Literal["any", "rx"] | None = None
        ip_igmp: bool | None = None
        ip_igmp_version: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=1, le=3)
        ip_igmp_host_proxy: IpIgmpHostProxy | None = None
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
        access_group_in: Annotated[str, StrConvert(convert_types=(int))] | None = None
        """
        IPv4 access-list name
        """
        access_group_out: Annotated[str, StrConvert(convert_types=(int))] | None = None
        """
        IPv4 access-list name
        """
        ipv6_access_group_in: Annotated[str, StrConvert(convert_types=(int))] | None = None
        """
        IPv6 access-list name
        """
        ipv6_access_group_out: Annotated[str, StrConvert(convert_types=(int))] | None = None
        """
        IPv6 access-list name
        """
        multicast: Multicast | None = None
        ospf_network_point_to_point: bool | None = None
        ospf_area: Annotated[str, StrConvert(convert_types=(int))] | None = None
        ospf_cost: Annotated[int, IntConvert(convert_types=(str))] | None = None
        ospf_authentication: Literal["none", "simple", "message-digest"] | None = None
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
        isis_metric: Annotated[int, IntConvert(convert_types=(str))] | None = None
        isis_network_point_to_point: bool | None = None
        mtu: Annotated[int, IntConvert(convert_types=(str))] | None = None
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
        ipv6_attached_host_route_export: Ipv6AttachedHostRouteExport | None = None
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

    class VlanInternalOrder(AvdDictBaseModel):
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
        range: Range = None

    class VlansItem(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class PrivateVlan(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            type: Literal["community", "isolated"] | None = None
            primary_vlan: Annotated[int, IntConvert(convert_types=(str))] | None = None
            """
            Primary VLAN ID
            """

        id: Annotated[int, IntConvert(convert_types=(str))] = None
        """
        VLAN ID
        """
        name: str | None = None
        """
        VLAN Name
        """
        state: Literal["active", "suspend"] | None = None
        trunk_groups: list[str] | None = None
        private_vlan: PrivateVlan | None = None
        tenant: str | None = None
        """
        Key only used for documentation or validation purposes
        """

    class VmtracerSessionsItem(AvdDictBaseModel):
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

    class VrfsItem(AvdDictBaseModel):
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

    class VxlanInterface(AvdDictBaseModel):
        model_config = ConfigDict(defer_build=True, extra="forbid")

        class Vxlan1(AvdDictBaseModel):
            model_config = ConfigDict(defer_build=True, extra="forbid")

            class Vxlan(AvdDictBaseModel):
                model_config = ConfigDict(defer_build=True, extra="forbid")

                class Multicast(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    headend_replication: bool | None = None

                class ControllerClient(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    enabled: bool | None = None

                class BfdVtepEvpn(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    interval: Annotated[int, IntConvert(convert_types=(str))] | None = None
                    min_rx: Annotated[int, IntConvert(convert_types=(str))] | None = None
                    multiplier: Annotated[int, IntConvert(convert_types=(str))] | None = Field(None, ge=3, le=50)
                    prefix_list: str | None = None

                class Qos(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    dscp_propagation_encapsulation: bool | None = None
                    ecn_propagation: bool | None = None
                    """
                    Enable copying the ECN marking to/from encapsulated packets.
                    """
                    map_dscp_to_traffic_class_decapsulation: bool | None = None

                class VlansItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    id: Annotated[int, IntConvert(convert_types=(str))] = None
                    """
                    VLAN ID
                    """
                    vni: Annotated[int, IntConvert(convert_types=(str))] | None = None
                    multicast_group: str | None = None
                    """
                    IP Multicast Group Address
                    """
                    flood_vteps: list[str] | None = None

                class VrfsItem(AvdDictBaseModel):
                    model_config = ConfigDict(defer_build=True, extra="forbid")

                    name: Annotated[str, StrConvert(convert_types=(int))] = None
                    """
                    VRF Name
                    """
                    vni: Annotated[int, IntConvert(convert_types=(str))] | None = None
                    multicast_group: str | None = None
                    """
                    IP Multicast Group Address
                    """

                source_interface: str | None = None
                """
                Source Interface Name
                """
                multicast: Multicast | None = None
                controller_client: ControllerClient | None = None
                """
                Client to CVX Controllers
                """
                mlag_source_interface: str | None = None
                udp_port: Annotated[int, IntConvert(convert_types=(str))] | None = None
                vtep_to_vtep_bridging: bool | None = None
                """
                Enable bridging between different VTEPs in vxlan overlay.
                """
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
    application_traffic_recognition: ApplicationTrafficRecognition | None = None
    """
    Application traffic recognition configuration.
    """
    arp: Arp | None = None
    as_path: AsPath | None = None
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
    banners: Banners | None = None
    bgp_groups: list[BgpGroupsItem] | None = None
    boot: Boot | None = Field(None, title="System Boot Settings")
    """
    Set the Aboot password
    """
    class_maps: ClassMaps | None = Field(None, title="QOS Class-maps")
    clock: Clock | None = None
    community_lists: list[CommunityListsItem] | None = Field(None, title="Community Lists (legacy model)")
    config_comment: str | None = None
    """
    Add a comment to provide information about the configuration.
    This comment will be rendered at the top of the generated
    configuration.
    """
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
    dhcp_servers: list[DhcpServersItem] | None = None
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
    ip_access_lists_max_entries: Annotated[int, IntConvert(convert_types=(str))] | None = None
    """
    Limit ACL entries defined under the `ip_access_lists`.
    """
    ip_community_lists: list[IpCommunityListsItem] | None = Field(None, title="IP Community Lists")
    """
    Communities and regexp entries MUST not be configured in the same community-list
    """
    ip_dhcp_relay: IpDhcpRelay | None = None
    ip_dhcp_snooping: IpDhcpSnooping | None = None
    ip_domain_lookup: IpDomainLookup | None = None
    ip_extcommunity_lists: list[IpExtcommunityListsItem] | None = Field(None, title="IP Extended Community Lists")
    ip_extcommunity_lists_regexp: list[IpExtcommunityListsRegexpItem] | None = Field(None, title="IP Extended Community Lists RegExp")
    ip_ftp_client_source_interfaces: list[IpFtpClientSourceInterfacesItem] | None = None
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
    ip_telnet_client_source_interfaces: list[IpTelnetClientSourceInterfacesItem] | None = None
    ip_tftp_client_source_interfaces: list[IpTftpClientSourceInterfacesItem] | None = None
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
    metadata: Metadata | None = None
    """
    The data under `metadata` is used for documentation, validation or integration purposes.
    It will not affect the
    generated EOS configuration.
    """
    mlag_configuration: MlagConfiguration | None = Field(None, title="Multi-Chassis Link Aggregation (MLAG) Configuration")
    monitor_connectivity: MonitorConnectivity | None = None
    monitor_layer1: MonitorLayer1 | None = None
    """
    Enable SYSLOG messages on transceiver SMBus communication failures.
    """
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
    Configure network services inserted to data forwarding.
    """
    router_traffic_engineering: RouterTrafficEngineering | None = None
    service_routing_configuration_bgp: ServiceRoutingConfigurationBgp | None = None
    service_routing_protocols_model: Literal["multi-agent", "ribd"] | None = None
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
    STUN configuration.
    """
    switchport_default: SwitchportDefault | None = None
    switchport_port_security: SwitchportPortSecurity | None = None
    system: System | None = None
    tacacs_servers: TacacsServers | None = None
    tap_aggregation: TapAggregation | None = None
    tcam_profile: TcamProfile | None = Field(None, title="Hardware TCAM Profiles")
    terminal: Terminal | None = Field(None, title="Terminal Settings")
    trackers: list[TrackersItem] | None = None
    traffic_policies: TrafficPolicies | None = None
    transceiver_qsfp_default_mode_4x10: bool | None = True
    """
    On all front panel ports which support this feature, the following global configuration command changes the QSFP mode
    from 40G to 4x10G (default). When set to false the command reverts the default QSFP mode back to 40G.
    """
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
