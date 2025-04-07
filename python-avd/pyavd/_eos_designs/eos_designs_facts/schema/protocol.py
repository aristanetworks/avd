# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar, Literal, Protocol

from pyavd._eos_designs.schema import EosDesigns
from pyavd._schema.models.avd_indexed_list import AvdIndexedList
from pyavd._schema.models.avd_list import AvdList
from pyavd._schema.models.avd_model import AvdModel

if TYPE_CHECKING:
    from pyavd._utils import Undefined, UndefinedType


class EosDesignsFactsProtocol(Protocol):
    """Subclass of Protocol."""

    class DownlinkPoolsItem(AvdModel):
        """Subclass of AvdModel."""

        class DownlinkInterfaces(AvdList[str]):
            """Subclass of AvdList with `str` items."""

        DownlinkInterfaces._item_type = str

        _fields: ClassVar[dict] = {"ipv4_pool": {"type": str}, "downlink_interfaces": {"type": DownlinkInterfaces}}
        ipv4_pool: str | None
        """
        Comma separated list of prefixes (IPv4 address/Mask) or ranges (IPv4_address-IPv4_address).
        IPv4
        subnets used for links to downlink switches will be derived from this pool based on index the peer's
        uplink interface's index in 'downlink_interfaces'.
        """
        downlink_interfaces: DownlinkInterfaces
        """
        List of downlink interfaces or ranges of interfaces to use this pool. The index of the interface in
        this list will determine which subnet will be taken from the pool.

        Subclass of AvdList with `str`
        items.
        """

        if TYPE_CHECKING:

            def __init__(
                self, *, ipv4_pool: str | None | UndefinedType = Undefined, downlink_interfaces: DownlinkInterfaces | UndefinedType = Undefined
            ) -> None:
                """
                DownlinkPoolsItem.


                Subclass of AvdModel.

                Args:
                    ipv4_pool:
                       Comma separated list of prefixes (IPv4 address/Mask) or ranges (IPv4_address-IPv4_address).
                       IPv4
                       subnets used for links to downlink switches will be derived from this pool based on index the peer's
                       uplink interface's index in 'downlink_interfaces'.
                    downlink_interfaces:
                       List of downlink interfaces or ranges of interfaces to use this pool. The index of the interface in
                       this list will determine which subnet will be taken from the pool.

                       Subclass of AvdList with `str`
                       items.

                """

    class DownlinkPools(AvdList[DownlinkPoolsItem]):
        """Subclass of AvdList with `DownlinkPoolsItem` items."""

    DownlinkPools._item_type = DownlinkPoolsItem

    class ConnectedEndpointsKeysItem(AvdModel):
        """Subclass of AvdModel."""

        _fields: ClassVar[dict] = {"key": {"type": str}, "type": {"type": str}, "description": {"type": str}}
        key: str
        type: str | None
        """Type used for documentation."""
        description: str | None
        """Description used for documentation."""

        if TYPE_CHECKING:

            def __init__(
                self, *, key: str | UndefinedType = Undefined, type: str | None | UndefinedType = Undefined, description: str | None | UndefinedType = Undefined
            ) -> None:
                """
                ConnectedEndpointsKeysItem.


                Subclass of AvdModel.

                Args:
                    key: key
                    type: Type used for documentation.
                    description: Description used for documentation.

                """

    class ConnectedEndpointsKeys(AvdIndexedList[str, ConnectedEndpointsKeysItem]):
        """Subclass of AvdIndexedList with `ConnectedEndpointsKeysItem` items. Primary key is `key` (`str`)."""

        _primary_key: ClassVar[str] = "key"

    ConnectedEndpointsKeys._item_type = ConnectedEndpointsKeysItem

    class PortProfileNamesItem(AvdModel):
        """Subclass of AvdModel."""

        _fields: ClassVar[dict] = {"profile": {"type": str}, "parent_profile": {"type": str}}
        profile: str
        parent_profile: str | None

        if TYPE_CHECKING:

            def __init__(self, *, profile: str | UndefinedType = Undefined, parent_profile: str | None | UndefinedType = Undefined) -> None:
                """
                PortProfileNamesItem.


                Subclass of AvdModel.

                Args:
                    profile: profile
                    parent_profile: parent_profile

                """

    class PortProfileNames(AvdList[PortProfileNamesItem]):
        """Subclass of AvdList with `PortProfileNamesItem` items."""

    PortProfileNames._item_type = PortProfileNamesItem

    class MlagInterfaces(AvdList[str]):
        """Subclass of AvdList with `str` items."""

    MlagInterfaces._item_type = str

    class MlagSwitchIds(AvdModel):
        """Subclass of AvdModel."""

        _fields: ClassVar[dict] = {"primary": {"type": int}, "secondary": {"type": int}}
        primary: int
        secondary: int

        if TYPE_CHECKING:

            def __init__(self, *, primary: int | UndefinedType = Undefined, secondary: int | UndefinedType = Undefined) -> None:
                """
                MlagSwitchIds.


                Subclass of AvdModel.

                Args:
                    primary: primary
                    secondary: secondary

                """

    class EvpnRouteServers(AvdList[str]):
        """Subclass of AvdList with `str` items."""

    EvpnRouteServers._item_type = str

    class MplsRouteReflectors(AvdList[str]):
        """Subclass of AvdList with `str` items."""

    MplsRouteReflectors._item_type = str

    class Overlay(AvdModel):
        """Subclass of AvdModel."""

        _fields: ClassVar[dict] = {"peering_address": {"type": str}, "evpn_mpls": {"type": bool}}
        peering_address: str | None
        evpn_mpls: bool

        if TYPE_CHECKING:

            def __init__(self, *, peering_address: str | None | UndefinedType = Undefined, evpn_mpls: bool | UndefinedType = Undefined) -> None:
                """
                Overlay.


                Subclass of AvdModel.

                Args:
                    peering_address: peering_address
                    evpn_mpls: evpn_mpls

                """

    class UplinksItem(AvdModel):
        """Subclass of AvdModel."""

        class Ptp(AvdModel):
            """Subclass of AvdModel."""

            _fields: ClassVar[dict] = {"enable": {"type": bool, "default": False}}
            enable: bool
            """Default value: `False`"""

            if TYPE_CHECKING:

                def __init__(self, *, enable: bool | UndefinedType = Undefined) -> None:
                    """
                    Ptp.


                    Subclass of AvdModel.

                    Args:
                        enable: enable

                    """

        class MacSecurity(AvdModel):
            """Subclass of AvdModel."""

            _fields: ClassVar[dict] = {"profile": {"type": str}}
            profile: str

            if TYPE_CHECKING:

                def __init__(self, *, profile: str | UndefinedType = Undefined) -> None:
                    """
                    MacSecurity.


                    Subclass of AvdModel.

                    Args:
                        profile: profile

                    """

        class LinkTrackingGroupsItem(AvdModel):
            """Subclass of AvdModel."""

            _fields: ClassVar[dict] = {"name": {"type": str}, "direction": {"type": str}}
            name: str
            direction: Literal["upstream", "downstream"]

            if TYPE_CHECKING:

                def __init__(self, *, name: str | UndefinedType = Undefined, direction: Literal["upstream", "downstream"] | UndefinedType = Undefined) -> None:
                    """
                    LinkTrackingGroupsItem.


                    Subclass of AvdModel.

                    Args:
                        name: name
                        direction: direction

                    """

        class LinkTrackingGroups(AvdIndexedList[str, LinkTrackingGroupsItem]):
            """Subclass of AvdIndexedList with `LinkTrackingGroupsItem` items. Primary key is `name` (`str`)."""

            _primary_key: ClassVar[str] = "name"

        LinkTrackingGroups._item_type = LinkTrackingGroupsItem

        class TrunkGroups(AvdList[str]):
            """Subclass of AvdList with `str` items."""

        TrunkGroups._item_type = str

        class PeerTrunkGroups(AvdList[str]):
            """Subclass of AvdList with `str` items."""

        PeerTrunkGroups._item_type = str

        class SubinterfacesItem(AvdModel):
            """Subclass of AvdModel."""

            _fields: ClassVar[dict] = {
                "interface": {"type": str},
                "peer_interface": {"type": str},
                "vrf": {"type": str},
                "encapsulation_dot1q_vlan": {"type": int},
                "ipv6_enable": {"type": bool},
                "prefix_length": {"type": int},
                "ip_address": {"type": str},
                "peer_ip_address": {"type": str},
                "structured_config": {"type": dict},
            }
            interface: str
            peer_interface: str
            vrf: str
            encapsulation_dot1q_vlan: int
            ipv6_enable: bool | None
            prefix_length: int | None
            ip_address: str | None
            peer_ip_address: str | None
            structured_config: dict
            """
            Custom structured config applied to "uplink_interfaces", and "uplink_switch_interfaces".
            When
            uplink_type == "p2p", custom structured config added under ethernet_interfaces.[name=<interface>]
            for eos_cli_config_gen overrides the settings on the ethernet interface level.
            When uplink_type ==
            "port-channel", custom structured config added under port_channel_interfaces.[name=<interface>] for
            eos_cli_config_gen overrides the settings on the port-channel interface level.
            "uplink_structured_config" is applied after "structured_config", so it can override
            "structured_config" defined on node-level.
            Note! The content of this dictionary is _not_ validated
            by the schema, since it can be either ethernet_interfaces or port_channel_interfaces.
            """

            if TYPE_CHECKING:

                def __init__(
                    self,
                    *,
                    interface: str | UndefinedType = Undefined,
                    peer_interface: str | UndefinedType = Undefined,
                    vrf: str | UndefinedType = Undefined,
                    encapsulation_dot1q_vlan: int | UndefinedType = Undefined,
                    ipv6_enable: bool | None | UndefinedType = Undefined,
                    prefix_length: int | None | UndefinedType = Undefined,
                    ip_address: str | None | UndefinedType = Undefined,
                    peer_ip_address: str | None | UndefinedType = Undefined,
                    structured_config: dict | UndefinedType = Undefined,
                ) -> None:
                    """
                    SubinterfacesItem.


                    Subclass of AvdModel.

                    Args:
                        interface: interface
                        peer_interface: peer_interface
                        vrf: vrf
                        encapsulation_dot1q_vlan: encapsulation_dot1q_vlan
                        ipv6_enable: ipv6_enable
                        prefix_length: prefix_length
                        ip_address: ip_address
                        peer_ip_address: peer_ip_address
                        structured_config:
                           Custom structured config applied to "uplink_interfaces", and "uplink_switch_interfaces".
                           When
                           uplink_type == "p2p", custom structured config added under ethernet_interfaces.[name=<interface>]
                           for eos_cli_config_gen overrides the settings on the ethernet interface level.
                           When uplink_type ==
                           "port-channel", custom structured config added under port_channel_interfaces.[name=<interface>] for
                           eos_cli_config_gen overrides the settings on the port-channel interface level.
                           "uplink_structured_config" is applied after "structured_config", so it can override
                           "structured_config" defined on node-level.
                           Note! The content of this dictionary is _not_ validated
                           by the schema, since it can be either ethernet_interfaces or port_channel_interfaces.

                    """

        class Subinterfaces(AvdIndexedList[str, SubinterfacesItem]):
            """Subclass of AvdIndexedList with `SubinterfacesItem` items. Primary key is `interface` (`str`)."""

            _primary_key: ClassVar[str] = "interface"

        Subinterfaces._item_type = SubinterfacesItem

        _fields: ClassVar[dict] = {
            "interface": {"type": str},
            "peer": {"type": str},
            "peer_interface": {"type": str},
            "peer_type": {"type": str},
            "peer_is_deployed": {"type": bool},
            "peer_bgp_as": {"type": str},
            "type": {"type": str},
            "speed": {"type": str},
            "bfd": {"type": bool},
            "peer_speed": {"type": str},
            "ptp": {"type": Ptp},
            "mac_security": {"type": MacSecurity},
            "underlay_multicast": {"type": bool},
            "ipv6_enable": {"type": bool},
            "prefix_length": {"type": int},
            "ip_address": {"type": str},
            "peer_ip_address": {"type": str},
            "link_tracking_groups": {"type": LinkTrackingGroups},
            "peer_node_group": {"type": str},
            "node_group": {"type": str},
            "mlag": {"type": bool},
            "peer_mlag": {"type": bool},
            "channel_group_id": {"type": int},
            "peer_channel_group_id": {"type": int},
            "trunk_groups": {"type": TrunkGroups},
            "peer_trunk_groups": {"type": PeerTrunkGroups},
            "vlans": {"type": str},
            "native_vlan": {"type": int},
            "short_esi": {"type": str},
            "peer_short_esi": {"type": str},
            "spanning_tree_portfast": {"type": str},
            "peer_spanning_tree_portfast": {"type": str},
            "sflow_enabled": {"type": bool},
            "flow_tracking": {"type": EosDesigns.FabricFlowTracking.Uplinks},
            "inband_ztp_vlan": {"type": int},
            "inband_ztp_lacp_fallback_delay": {"type": int},
            "dhcp_server": {"type": bool},
            "structured_config": {"type": dict},
            "subinterfaces": {"type": Subinterfaces},
        }
        interface: str
        peer: str
        peer_interface: str
        peer_type: str
        peer_is_deployed: bool
        peer_bgp_as: str | None
        type: Literal["underlay_p2p", "underlay_l2"]
        speed: str | None
        bfd: bool | None
        peer_speed: str | None
        ptp: Ptp
        """
        Enable PTP on all infrastructure links.

        Subclass of AvdModel.
        """
        mac_security: MacSecurity
        """Subclass of AvdModel."""
        underlay_multicast: bool | None
        ipv6_enable: bool | None
        prefix_length: int | None
        ip_address: str | None
        peer_ip_address: str | None
        link_tracking_groups: LinkTrackingGroups
        """Subclass of AvdIndexedList with `LinkTrackingGroupsItem` items. Primary key is `name` (`str`)."""
        peer_node_group: str | None
        node_group: str | None
        mlag: bool | None
        peer_mlag: bool | None
        channel_group_id: int | None
        peer_channel_group_id: int | None
        trunk_groups: TrunkGroups
        """Subclass of AvdList with `str` items."""
        peer_trunk_groups: PeerTrunkGroups
        """Subclass of AvdList with `str` items."""
        vlans: str | None
        native_vlan: int | None
        short_esi: str | None
        peer_short_esi: str | None
        spanning_tree_portfast: Literal["edge", "network"] | None
        peer_spanning_tree_portfast: Literal["edge", "network"] | None
        sflow_enabled: bool | None
        flow_tracking: EosDesigns.FabricFlowTracking.Uplinks
        """Enable flow-tracking on all fabric uplinks."""
        inband_ztp_vlan: int | None
        inband_ztp_lacp_fallback_delay: int | None
        dhcp_server: bool | None
        structured_config: dict
        """
        Custom structured config applied to "uplink_interfaces", and "uplink_switch_interfaces".
        When
        uplink_type == "p2p", custom structured config added under ethernet_interfaces.[name=<interface>]
        for eos_cli_config_gen overrides the settings on the ethernet interface level.
        When uplink_type ==
        "port-channel", custom structured config added under port_channel_interfaces.[name=<interface>] for
        eos_cli_config_gen overrides the settings on the port-channel interface level.
        "uplink_structured_config" is applied after "structured_config", so it can override
        "structured_config" defined on node-level.
        Note! The content of this dictionary is _not_ validated
        by the schema, since it can be either ethernet_interfaces or port_channel_interfaces.
        """
        subinterfaces: Subinterfaces
        """Subclass of AvdIndexedList with `SubinterfacesItem` items. Primary key is `interface` (`str`)."""

        if TYPE_CHECKING:

            def __init__(
                self,
                *,
                interface: str | UndefinedType = Undefined,
                peer: str | UndefinedType = Undefined,
                peer_interface: str | UndefinedType = Undefined,
                peer_type: str | UndefinedType = Undefined,
                peer_is_deployed: bool | UndefinedType = Undefined,
                peer_bgp_as: str | None | UndefinedType = Undefined,
                type: Literal["underlay_p2p", "underlay_l2"] | UndefinedType = Undefined,
                speed: str | None | UndefinedType = Undefined,
                bfd: bool | None | UndefinedType = Undefined,
                peer_speed: str | None | UndefinedType = Undefined,
                ptp: Ptp | UndefinedType = Undefined,
                mac_security: MacSecurity | UndefinedType = Undefined,
                underlay_multicast: bool | None | UndefinedType = Undefined,
                ipv6_enable: bool | None | UndefinedType = Undefined,
                prefix_length: int | None | UndefinedType = Undefined,
                ip_address: str | None | UndefinedType = Undefined,
                peer_ip_address: str | None | UndefinedType = Undefined,
                link_tracking_groups: LinkTrackingGroups | UndefinedType = Undefined,
                peer_node_group: str | None | UndefinedType = Undefined,
                node_group: str | None | UndefinedType = Undefined,
                mlag: bool | None | UndefinedType = Undefined,
                peer_mlag: bool | None | UndefinedType = Undefined,
                channel_group_id: int | None | UndefinedType = Undefined,
                peer_channel_group_id: int | None | UndefinedType = Undefined,
                trunk_groups: TrunkGroups | UndefinedType = Undefined,
                peer_trunk_groups: PeerTrunkGroups | UndefinedType = Undefined,
                vlans: str | None | UndefinedType = Undefined,
                native_vlan: int | None | UndefinedType = Undefined,
                short_esi: str | None | UndefinedType = Undefined,
                peer_short_esi: str | None | UndefinedType = Undefined,
                spanning_tree_portfast: Literal["edge", "network"] | None | UndefinedType = Undefined,
                peer_spanning_tree_portfast: Literal["edge", "network"] | None | UndefinedType = Undefined,
                sflow_enabled: bool | None | UndefinedType = Undefined,
                flow_tracking: EosDesigns.FabricFlowTracking.Uplinks | UndefinedType = Undefined,
                inband_ztp_vlan: int | None | UndefinedType = Undefined,
                inband_ztp_lacp_fallback_delay: int | None | UndefinedType = Undefined,
                dhcp_server: bool | None | UndefinedType = Undefined,
                structured_config: dict | UndefinedType = Undefined,
                subinterfaces: Subinterfaces | UndefinedType = Undefined,
            ) -> None:
                """
                UplinksItem.


                Subclass of AvdModel.

                Args:
                    interface: interface
                    peer: peer
                    peer_interface: peer_interface
                    peer_type: peer_type
                    peer_is_deployed: peer_is_deployed
                    peer_bgp_as: peer_bgp_as
                    type: type
                    speed: speed
                    bfd: bfd
                    peer_speed: peer_speed
                    ptp:
                       Enable PTP on all infrastructure links.

                       Subclass of AvdModel.
                    mac_security: Subclass of AvdModel.
                    underlay_multicast: underlay_multicast
                    ipv6_enable: ipv6_enable
                    prefix_length: prefix_length
                    ip_address: ip_address
                    peer_ip_address: peer_ip_address
                    link_tracking_groups: Subclass of AvdIndexedList with `LinkTrackingGroupsItem` items. Primary key is `name` (`str`).
                    peer_node_group: peer_node_group
                    node_group: node_group
                    mlag: mlag
                    peer_mlag: peer_mlag
                    channel_group_id: channel_group_id
                    peer_channel_group_id: peer_channel_group_id
                    trunk_groups: Subclass of AvdList with `str` items.
                    peer_trunk_groups: Subclass of AvdList with `str` items.
                    vlans: vlans
                    native_vlan: native_vlan
                    short_esi: short_esi
                    peer_short_esi: peer_short_esi
                    spanning_tree_portfast: spanning_tree_portfast
                    peer_spanning_tree_portfast: peer_spanning_tree_portfast
                    sflow_enabled: sflow_enabled
                    flow_tracking: Enable flow-tracking on all fabric uplinks.
                    inband_ztp_vlan: inband_ztp_vlan
                    inband_ztp_lacp_fallback_delay: inband_ztp_lacp_fallback_delay
                    dhcp_server: dhcp_server
                    structured_config:
                       Custom structured config applied to "uplink_interfaces", and "uplink_switch_interfaces".
                       When
                       uplink_type == "p2p", custom structured config added under ethernet_interfaces.[name=<interface>]
                       for eos_cli_config_gen overrides the settings on the ethernet interface level.
                       When uplink_type ==
                       "port-channel", custom structured config added under port_channel_interfaces.[name=<interface>] for
                       eos_cli_config_gen overrides the settings on the port-channel interface level.
                       "uplink_structured_config" is applied after "structured_config", so it can override
                       "structured_config" defined on node-level.
                       Note! The content of this dictionary is _not_ validated
                       by the schema, since it can be either ethernet_interfaces or port_channel_interfaces.
                    subinterfaces: Subclass of AvdIndexedList with `SubinterfacesItem` items. Primary key is `interface` (`str`).

                """

    class Uplinks(AvdList[UplinksItem]):
        """Subclass of AvdList with `UplinksItem` items."""

    Uplinks._item_type = UplinksItem

    class UplinkPeers(AvdList[str]):
        """Subclass of AvdList with `str` items."""

    UplinkPeers._item_type = str

    class UplinkSwitchVrfs(AvdList[str]):
        """Subclass of AvdList with `str` items."""

    UplinkSwitchVrfs._item_type = str

    class LocalEndpointTrunkGroups(AvdList[str]):
        """Subclass of AvdList with `str` items."""

    LocalEndpointTrunkGroups._item_type = str

    class EndpointTrunkGroups(AvdList[str]):
        """Subclass of AvdList with `str` items."""

    EndpointTrunkGroups._item_type = str

    class WanPathGroupsItem(AvdModel):
        """Subclass of AvdModel."""

        class InterfacesItem(AvdModel):
            """Subclass of AvdModel."""

            _fields: ClassVar[dict] = {
                "name": {"type": str},
                "public_ip": {"type": str},
                "connected_to_pathfinder": {"type": bool},
                "wan_circuit_id": {"type": str},
            }
            name: str
            public_ip: str | None
            connected_to_pathfinder: bool
            wan_circuit_id: str | None

            if TYPE_CHECKING:

                def __init__(
                    self,
                    *,
                    name: str | UndefinedType = Undefined,
                    public_ip: str | None | UndefinedType = Undefined,
                    connected_to_pathfinder: bool | UndefinedType = Undefined,
                    wan_circuit_id: str | None | UndefinedType = Undefined,
                ) -> None:
                    """
                    InterfacesItem.


                    Subclass of AvdModel.

                    Args:
                        name: name
                        public_ip: public_ip
                        connected_to_pathfinder: connected_to_pathfinder
                        wan_circuit_id: wan_circuit_id

                    """

        class Interfaces(AvdList[InterfacesItem]):
            """Subclass of AvdList with `InterfacesItem` items."""

        Interfaces._item_type = InterfacesItem

        class Ipsec(AvdModel):
            """Subclass of AvdModel."""

            _fields: ClassVar[dict] = {"dynamic_peers": {"type": bool, "default": True}, "static_peers": {"type": bool, "default": True}}
            dynamic_peers: bool
            """
            Enable IPSec for dynamic peers.

            Default value: `True`
            """
            static_peers: bool
            """
            Enable IPSec for static peers.

            Default value: `True`
            """

            if TYPE_CHECKING:

                def __init__(self, *, dynamic_peers: bool | UndefinedType = Undefined, static_peers: bool | UndefinedType = Undefined) -> None:
                    """
                    Ipsec.


                    Subclass of AvdModel.

                    Args:
                        dynamic_peers: Enable IPSec for dynamic peers.
                        static_peers: Enable IPSec for static peers.

                    """

        class ImportPathGroupsItem(AvdModel):
            """Subclass of AvdModel."""

            _fields: ClassVar[dict] = {"remote": {"type": str}, "local": {"type": str}}
            remote: str | None
            """Remote path-group to import."""
            local: str | None
            """Optional, if not set, the path-group `name` is used as local."""

            if TYPE_CHECKING:

                def __init__(self, *, remote: str | None | UndefinedType = Undefined, local: str | None | UndefinedType = Undefined) -> None:
                    """
                    ImportPathGroupsItem.


                    Subclass of AvdModel.

                    Args:
                        remote: Remote path-group to import.
                        local: Optional, if not set, the path-group `name` is used as local.

                    """

        class ImportPathGroups(AvdList[ImportPathGroupsItem]):
            """Subclass of AvdList with `ImportPathGroupsItem` items."""

        ImportPathGroups._item_type = ImportPathGroupsItem

        class DpsKeepalive(AvdModel):
            """Subclass of AvdModel."""

            _fields: ClassVar[dict] = {"interval": {"type": str}, "failure_threshold": {"type": int, "default": 5}}
            interval: str | None
            """
            Interval in milliseconds. Valid values are 50-60000 | "auto".

            When auto, the interval and
            failure_threshold are automatically determined based on
            path state.
            """
            failure_threshold: int
            """
            Failure threshold in number of lost keep-alive messages.

            Default value: `5`
            """

            if TYPE_CHECKING:

                def __init__(self, *, interval: str | None | UndefinedType = Undefined, failure_threshold: int | UndefinedType = Undefined) -> None:
                    """
                    DpsKeepalive.


                    Subclass of AvdModel.

                    Args:
                        interval:
                           Interval in milliseconds. Valid values are 50-60000 | "auto".

                           When auto, the interval and
                           failure_threshold are automatically determined based on
                           path state.
                        failure_threshold: Failure threshold in number of lost keep-alive messages.

                    """

        _fields: ClassVar[dict] = {
            "interfaces": {"type": Interfaces},
            "name": {"type": str},
            "id": {"type": int},
            "description": {"type": str},
            "ipsec": {"type": Ipsec},
            "import_path_groups": {"type": ImportPathGroups},
            "default_preference": {"type": str, "default": "preferred"},
            "excluded_from_default_policy": {"type": bool, "default": False},
            "dps_keepalive": {"type": DpsKeepalive},
        }
        interfaces: Interfaces
        """Subclass of AvdList with `InterfacesItem` items."""
        name: str
        """Path-group name."""
        id: int
        """
        Path-group id.
        Required until an auto ID algorithm is implemented.
        """
        description: str | None
        """Additional information about the path-group for documentation purposes."""
        ipsec: Ipsec
        """
        Configuration of IPSec at the path-group level.

        Subclass of AvdModel.
        """
        import_path_groups: ImportPathGroups
        """
        List of path-groups to import in this path-group.

        Subclass of AvdList with `ImportPathGroupsItem`
        items.
        """
        default_preference: str
        """
        Preference value used when a preference is not given for a path-group in the
        `wan_virtual_topologies.policies` input or when
        the path-group is used in an auto generated policy
        except if `excluded_from_default_policy` is set to `true.

        Valid values are 1-65535 | "preferred" |
        "alternate".

        `preferred` is converted to priority 1.
        `alternate` is converted to priority 2.

        Default value: `"preferred"`
        """
        excluded_from_default_policy: bool
        """
        When set to `true`, the path-group is excluded from AVD auto generated policies.

        Default value: `False`
        """
        dps_keepalive: DpsKeepalive
        """
        Period between the transmission of consecutive keepalive messages, and failure threshold.

        Subclass
        of AvdModel.
        """

        if TYPE_CHECKING:

            def __init__(
                self,
                *,
                interfaces: Interfaces | UndefinedType = Undefined,
                name: str | UndefinedType = Undefined,
                id: int | UndefinedType = Undefined,
                description: str | None | UndefinedType = Undefined,
                ipsec: Ipsec | UndefinedType = Undefined,
                import_path_groups: ImportPathGroups | UndefinedType = Undefined,
                default_preference: str | UndefinedType = Undefined,
                excluded_from_default_policy: bool | UndefinedType = Undefined,
                dps_keepalive: DpsKeepalive | UndefinedType = Undefined,
            ) -> None:
                """
                WanPathGroupsItem.


                Subclass of AvdModel.

                Args:
                    interfaces: Subclass of AvdList with `InterfacesItem` items.
                    name: Path-group name.
                    id:
                       Path-group id.
                       Required until an auto ID algorithm is implemented.
                    description: Additional information about the path-group for documentation purposes.
                    ipsec:
                       Configuration of IPSec at the path-group level.

                       Subclass of AvdModel.
                    import_path_groups:
                       List of path-groups to import in this path-group.

                       Subclass of AvdList with `ImportPathGroupsItem`
                       items.
                    default_preference:
                       Preference value used when a preference is not given for a path-group in the
                       `wan_virtual_topologies.policies` input or when
                       the path-group is used in an auto generated policy
                       except if `excluded_from_default_policy` is set to `true.

                       Valid values are 1-65535 | "preferred" |
                       "alternate".

                       `preferred` is converted to priority 1.
                       `alternate` is converted to priority 2.
                    excluded_from_default_policy: When set to `true`, the path-group is excluded from AVD auto generated policies.
                    dps_keepalive:
                       Period between the transmission of consecutive keepalive messages, and failure threshold.

                       Subclass
                       of AvdModel.

                """

    class WanPathGroups(AvdIndexedList[str, WanPathGroupsItem]):
        """Subclass of AvdIndexedList with `WanPathGroupsItem` items. Primary key is `name` (`str`)."""

        _primary_key: ClassVar[str] = "name"

    WanPathGroups._item_type = WanPathGroupsItem

    class UplinkSwitchInterfaces(AvdList[str]):
        """Subclass of AvdList with `str` items."""

    UplinkSwitchInterfaces._item_type = str

    class DownlinkSwitches(AvdList[str]):
        """Subclass of AvdList with `str` items."""

    DownlinkSwitches._item_type = str

    class EvpnRouteServerClients(AvdList[str]):
        """Subclass of AvdList with `str` items."""

    EvpnRouteServerClients._item_type = str

    class MplsRouteReflectorClients(AvdList[str]):
        """Subclass of AvdList with `str` items."""

    MplsRouteReflectorClients._item_type = str

    _fields: ClassVar[dict] = {
        "id": {"type": int},
        "type": {"type": str},
        "platform": {"type": str},
        "is_deployed": {"type": bool},
        "serial_number": {"type": str},
        "mgmt_interface": {"type": str},
        "mgmt_ip": {"type": str},
        "mpls_lsr": {"type": bool},
        "evpn_multicast": {"type": bool},
        "loopback_ipv4_pool": {"type": str},
        "uplink_ipv4_pool": {"type": str},
        "downlink_pools": {"type": DownlinkPools},
        "bgp_as": {"type": str},
        "underlay_routing_protocol": {"type": str},
        "vtep_loopback_ipv4_pool": {"type": str},
        "inband_mgmt_subnet": {"type": str},
        "inband_mgmt_ipv6_subnet": {"type": str},
        "inband_mgmt_vlan": {"type": int},
        "inband_ztp": {"type": bool},
        "inband_ztp_vlan": {"type": int},
        "inband_ztp_lacp_fallback_delay": {"type": int},
        "dc_name": {"type": str},
        "group": {"type": str},
        "router_id": {"type": str},
        "inband_mgmt_ip": {"type": str},
        "inband_mgmt_interface": {"type": str},
        "pod": {"type": str},
        "connected_endpoints_keys": {"type": ConnectedEndpointsKeys},
        "port_profile_names": {"type": PortProfileNames},
        "mlag_peer": {"type": str},
        "mlag_port_channel_id": {"type": int},
        "mlag_interfaces": {"type": MlagInterfaces},
        "mlag_ip": {"type": str},
        "mlag_l3_ip": {"type": str},
        "mlag_switch_ids": {"type": MlagSwitchIds},
        "evpn_role": {"type": str},
        "mpls_overlay_role": {"type": str},
        "evpn_route_servers": {"type": EvpnRouteServers},
        "mpls_route_reflectors": {"type": MplsRouteReflectors},
        "overlay": {"type": Overlay},
        "vtep_ip": {"type": str},
        "max_parallel_uplinks": {"type": int, "default": 1},
        "max_uplink_switches": {"type": int},
        "uplinks": {"type": Uplinks},
        "uplink_peers": {"type": UplinkPeers},
        "uplink_switch_vrfs": {"type": UplinkSwitchVrfs},
        "vlans": {"type": str},
        "endpoint_vlans": {"type": str},
        "local_endpoint_trunk_groups": {"type": LocalEndpointTrunkGroups},
        "endpoint_trunk_groups": {"type": EndpointTrunkGroups},
        "wan_path_groups": {"type": WanPathGroups},
        "uplink_switch_interfaces": {"type": UplinkSwitchInterfaces},
        "downlink_switches": {"type": DownlinkSwitches},
        "evpn_route_server_clients": {"type": EvpnRouteServerClients},
        "mpls_route_reflector_clients": {"type": MplsRouteReflectorClients},
    }
    id: int | None
    type: str
    platform: str | None
    is_deployed: bool
    serial_number: str | None
    mgmt_interface: str | None
    mgmt_ip: str | None
    mpls_lsr: bool
    evpn_multicast: bool | None
    loopback_ipv4_pool: str | None
    uplink_ipv4_pool: str | None
    downlink_pools: DownlinkPools
    """
    IPv4 pools used for links to downlink switches. Set this on the parent switch. Cannot be combined
    with `uplink_ipv4_pool` set on the downlink switch.

    Subclass of AvdList with `DownlinkPoolsItem`
    items.
    """
    bgp_as: str | None
    underlay_routing_protocol: str
    vtep_loopback_ipv4_pool: str | None
    inband_mgmt_subnet: str | None
    inband_mgmt_ipv6_subnet: str | None
    inband_mgmt_vlan: int | None
    inband_ztp: bool | None
    inband_ztp_vlan: int | None
    inband_ztp_lacp_fallback_delay: int | None
    dc_name: str | None
    group: str | None
    router_id: str | None
    inband_mgmt_ip: str | None
    """Used for fabric docs."""
    inband_mgmt_interface: str | None
    """Used for fabric docs."""
    pod: str
    """Used for fabric docs."""
    connected_endpoints_keys: ConnectedEndpointsKeys
    """
    List of connected_endpoints_keys in use on this device.
    Used for fabric docs.

    Subclass of
    AvdIndexedList with `ConnectedEndpointsKeysItem` items. Primary key is `key` (`str`).
    """
    port_profile_names: PortProfileNames
    """
    List of port_profiles configured - including the ones not in use.
    Used for fabric docs.

    Subclass of
    AvdList with `PortProfileNamesItem` items.
    """
    mlag_peer: str | None
    mlag_port_channel_id: int | None
    mlag_interfaces: MlagInterfaces
    """Subclass of AvdList with `str` items."""
    mlag_ip: str | None
    mlag_l3_ip: str | None
    mlag_switch_ids: MlagSwitchIds
    """
    The switch ids of both primary and secondary switches for a this node group.

    Subclass of AvdModel.
    """
    evpn_role: str | None
    mpls_overlay_role: str | None
    evpn_route_servers: EvpnRouteServers
    """
    For evpn clients the default value for EVPN Route Servers is the content of the uplink_switches
    variable set elsewhere.
    For all other evpn roles there is no default.

    Subclass of AvdList with
    `str` items.
    """
    mpls_route_reflectors: MplsRouteReflectors
    """
    List of inventory hostname acting as MPLS route-reflectors.

    Subclass of AvdList with `str` items.
    """
    overlay: Overlay
    """Subclass of AvdModel."""
    vtep_ip: str | None
    max_parallel_uplinks: int
    """
    Number of parallel links towards uplink switches.
    Changing this value may change interface naming on
    uplinks (and corresponding downlinks).
    Can be used to reserve interfaces for future parallel
    uplinks.

    Default value: `1`
    """
    max_uplink_switches: int
    uplinks: Uplinks
    """
    List of uplinks with all parameters
    These facts are leveraged by templates for this device when
    rendering uplinks
    and by templates for peer devices when rendering downlinks

    Subclass of AvdList
    with `UplinksItem` items.
    """
    uplink_peers: UplinkPeers
    """Subclass of AvdList with `str` items."""
    uplink_switch_vrfs: UplinkSwitchVrfs
    """Subclass of AvdList with `str` items."""
    vlans: str
    """
    Compressed list of vlans to be defined on this switch after filtering network services.
    The filter
    is based on filter.tenants, filter.tags but not filter.only_vlans_in_use.

    Ex. "1-100, 201-202"
    This excludes the optional "uplink_native_vlan" if that vlan is not used for anything else.
    This is
    to ensure that native vlan is not necessarily permitted on the uplink trunk.
    """
    endpoint_vlans: str | None
    """
    Compressed list of vlans in use by endpoints connected to this switch, downstream switches or MLAG
    peer and it's downstream switches.
    """
    local_endpoint_trunk_groups: LocalEndpointTrunkGroups
    """
    List of trunk_groups in use by endpoints connected to this switch.

    Subclass of AvdList with `str`
    items.
    """
    endpoint_trunk_groups: EndpointTrunkGroups
    """
    List of trunk_groups in use by endpoints connected to this switch, downstream switches or MLAG peer
    and it's downstream switches.

    Subclass of AvdList with `str` items.
    """
    wan_path_groups: WanPathGroups
    """
    List of path-groups used for the WAN configuration.

    Subclass of AvdIndexedList with
    `WanPathGroupsItem` items. Primary key is `name` (`str`).
    """
    uplink_switch_interfaces: UplinkSwitchInterfaces
    """Subclass of AvdList with `str` items."""
    downlink_switches: DownlinkSwitches
    """Subclass of AvdList with `str` items."""
    evpn_route_server_clients: EvpnRouteServerClients
    """Subclass of AvdList with `str` items."""
    mpls_route_reflector_clients: MplsRouteReflectorClients
    """Subclass of AvdList with `str` items."""

    if TYPE_CHECKING:

        def __init__(
            self,
            *,
            id: int | None | UndefinedType = Undefined,
            type: str | UndefinedType = Undefined,
            platform: str | None | UndefinedType = Undefined,
            is_deployed: bool | UndefinedType = Undefined,
            serial_number: str | None | UndefinedType = Undefined,
            mgmt_interface: str | None | UndefinedType = Undefined,
            mgmt_ip: str | None | UndefinedType = Undefined,
            mpls_lsr: bool | UndefinedType = Undefined,
            evpn_multicast: bool | None | UndefinedType = Undefined,
            loopback_ipv4_pool: str | None | UndefinedType = Undefined,
            uplink_ipv4_pool: str | None | UndefinedType = Undefined,
            downlink_pools: DownlinkPools | UndefinedType = Undefined,
            bgp_as: str | None | UndefinedType = Undefined,
            underlay_routing_protocol: str | UndefinedType = Undefined,
            vtep_loopback_ipv4_pool: str | None | UndefinedType = Undefined,
            inband_mgmt_subnet: str | None | UndefinedType = Undefined,
            inband_mgmt_ipv6_subnet: str | None | UndefinedType = Undefined,
            inband_mgmt_vlan: int | None | UndefinedType = Undefined,
            inband_ztp: bool | None | UndefinedType = Undefined,
            inband_ztp_vlan: int | None | UndefinedType = Undefined,
            inband_ztp_lacp_fallback_delay: int | None | UndefinedType = Undefined,
            dc_name: str | None | UndefinedType = Undefined,
            group: str | None | UndefinedType = Undefined,
            router_id: str | None | UndefinedType = Undefined,
            inband_mgmt_ip: str | None | UndefinedType = Undefined,
            inband_mgmt_interface: str | None | UndefinedType = Undefined,
            pod: str | UndefinedType = Undefined,
            connected_endpoints_keys: ConnectedEndpointsKeys | UndefinedType = Undefined,
            port_profile_names: PortProfileNames | UndefinedType = Undefined,
            mlag_peer: str | None | UndefinedType = Undefined,
            mlag_port_channel_id: int | None | UndefinedType = Undefined,
            mlag_interfaces: MlagInterfaces | UndefinedType = Undefined,
            mlag_ip: str | None | UndefinedType = Undefined,
            mlag_l3_ip: str | None | UndefinedType = Undefined,
            mlag_switch_ids: MlagSwitchIds | UndefinedType = Undefined,
            evpn_role: str | None | UndefinedType = Undefined,
            mpls_overlay_role: str | None | UndefinedType = Undefined,
            evpn_route_servers: EvpnRouteServers | UndefinedType = Undefined,
            mpls_route_reflectors: MplsRouteReflectors | UndefinedType = Undefined,
            overlay: Overlay | UndefinedType = Undefined,
            vtep_ip: str | None | UndefinedType = Undefined,
            max_parallel_uplinks: int | UndefinedType = Undefined,
            max_uplink_switches: int | UndefinedType = Undefined,
            uplinks: Uplinks | UndefinedType = Undefined,
            uplink_peers: UplinkPeers | UndefinedType = Undefined,
            uplink_switch_vrfs: UplinkSwitchVrfs | UndefinedType = Undefined,
            vlans: str | UndefinedType = Undefined,
            endpoint_vlans: str | None | UndefinedType = Undefined,
            local_endpoint_trunk_groups: LocalEndpointTrunkGroups | UndefinedType = Undefined,
            endpoint_trunk_groups: EndpointTrunkGroups | UndefinedType = Undefined,
            wan_path_groups: WanPathGroups | UndefinedType = Undefined,
            uplink_switch_interfaces: UplinkSwitchInterfaces | UndefinedType = Undefined,
            downlink_switches: DownlinkSwitches | UndefinedType = Undefined,
            evpn_route_server_clients: EvpnRouteServerClients | UndefinedType = Undefined,
            mpls_route_reflector_clients: MplsRouteReflectorClients | UndefinedType = Undefined,
        ) -> None:
            """
            EosDesignsFactsProtocol.


            Subclass of Protocol.

            Args:
                id: id
                type: type
                platform: platform
                is_deployed: is_deployed
                serial_number: serial_number
                mgmt_interface: mgmt_interface
                mgmt_ip: mgmt_ip
                mpls_lsr: mpls_lsr
                evpn_multicast: evpn_multicast
                loopback_ipv4_pool: loopback_ipv4_pool
                uplink_ipv4_pool: uplink_ipv4_pool
                downlink_pools:
                   IPv4 pools used for links to downlink switches. Set this on the parent switch. Cannot be combined
                   with `uplink_ipv4_pool` set on the downlink switch.

                   Subclass of AvdList with `DownlinkPoolsItem`
                   items.
                bgp_as: bgp_as
                underlay_routing_protocol: underlay_routing_protocol
                vtep_loopback_ipv4_pool: vtep_loopback_ipv4_pool
                inband_mgmt_subnet: inband_mgmt_subnet
                inband_mgmt_ipv6_subnet: inband_mgmt_ipv6_subnet
                inband_mgmt_vlan: inband_mgmt_vlan
                inband_ztp: inband_ztp
                inband_ztp_vlan: inband_ztp_vlan
                inband_ztp_lacp_fallback_delay: inband_ztp_lacp_fallback_delay
                dc_name: dc_name
                group: group
                router_id: router_id
                inband_mgmt_ip: Used for fabric docs.
                inband_mgmt_interface: Used for fabric docs.
                pod: Used for fabric docs.
                connected_endpoints_keys:
                   List of connected_endpoints_keys in use on this device.
                   Used for fabric docs.

                   Subclass of
                   AvdIndexedList with `ConnectedEndpointsKeysItem` items. Primary key is `key` (`str`).
                port_profile_names:
                   List of port_profiles configured - including the ones not in use.
                   Used for fabric docs.

                   Subclass of
                   AvdList with `PortProfileNamesItem` items.
                mlag_peer: mlag_peer
                mlag_port_channel_id: mlag_port_channel_id
                mlag_interfaces: Subclass of AvdList with `str` items.
                mlag_ip: mlag_ip
                mlag_l3_ip: mlag_l3_ip
                mlag_switch_ids:
                   The switch ids of both primary and secondary switches for a this node group.

                   Subclass of AvdModel.
                evpn_role: evpn_role
                mpls_overlay_role: mpls_overlay_role
                evpn_route_servers:
                   For evpn clients the default value for EVPN Route Servers is the content of the uplink_switches
                   variable set elsewhere.
                   For all other evpn roles there is no default.

                   Subclass of AvdList with
                   `str` items.
                mpls_route_reflectors:
                   List of inventory hostname acting as MPLS route-reflectors.

                   Subclass of AvdList with `str` items.
                overlay: Subclass of AvdModel.
                vtep_ip: vtep_ip
                max_parallel_uplinks:
                   Number of parallel links towards uplink switches.
                   Changing this value may change interface naming on
                   uplinks (and corresponding downlinks).
                   Can be used to reserve interfaces for future parallel
                   uplinks.
                max_uplink_switches: max_uplink_switches
                uplinks:
                   List of uplinks with all parameters
                   These facts are leveraged by templates for this device when
                   rendering uplinks
                   and by templates for peer devices when rendering downlinks

                   Subclass of AvdList
                   with `UplinksItem` items.
                uplink_peers: Subclass of AvdList with `str` items.
                uplink_switch_vrfs: Subclass of AvdList with `str` items.
                vlans:
                   Compressed list of vlans to be defined on this switch after filtering network services.
                   The filter
                   is based on filter.tenants, filter.tags but not filter.only_vlans_in_use.

                   Ex. "1-100, 201-202"
                   This excludes the optional "uplink_native_vlan" if that vlan is not used for anything else.
                   This is
                   to ensure that native vlan is not necessarily permitted on the uplink trunk.
                endpoint_vlans:
                   Compressed list of vlans in use by endpoints connected to this switch, downstream switches or MLAG
                   peer and it's downstream switches.
                local_endpoint_trunk_groups:
                   List of trunk_groups in use by endpoints connected to this switch.

                   Subclass of AvdList with `str`
                   items.
                endpoint_trunk_groups:
                   List of trunk_groups in use by endpoints connected to this switch, downstream switches or MLAG peer
                   and it's downstream switches.

                   Subclass of AvdList with `str` items.
                wan_path_groups:
                   List of path-groups used for the WAN configuration.

                   Subclass of AvdIndexedList with
                   `WanPathGroupsItem` items. Primary key is `name` (`str`).
                uplink_switch_interfaces: Subclass of AvdList with `str` items.
                downlink_switches: Subclass of AvdList with `str` items.
                evpn_route_server_clients: Subclass of AvdList with `str` items.
                mpls_route_reflector_clients: Subclass of AvdList with `str` items.

            """
