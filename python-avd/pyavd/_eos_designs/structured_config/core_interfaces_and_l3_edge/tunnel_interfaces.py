# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Literal, Protocol, cast

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.schema import EosDesigns
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor
from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._utils.default import default
from pyavd._utils.password_utils.password import isis_encrypt, ospf_message_digest_encrypt

if TYPE_CHECKING:
    from .utils import T_P2pLinksItem

    from . import AvdStructuredConfigCoreInterfacesAndL3EdgeProtocol


class TunnelInterfacesMixin(Protocol):
    """Mixin Class used to generate structured config for tunnel_interfaces."""

    @structured_config_contributor
    def tunnel_interfaces(self: AvdStructuredConfigCoreInterfacesAndL3EdgeProtocol) -> None:
        """Set the structured config for tunnel_interfaces."""
        for p2p_link, p2p_link_data in self._filtered_p2p_links:
            if not p2p_link_data.get("is_tunnel"):
                continue

            tunnel_interface = EosCliConfigGen.TunnelInterfacesItem(
                name=p2p_link_data["interface"],
                shutdown=False,
                mtu=p2p_link._get("mtu", self.shared_utils.p2p_uplinks_mtu),
                tunnel_mode=p2p_link_data["tunnel_mode"],
                source_interface=p2p_link_data["source_interface"],
                destination=p2p_link_data["peer_source_ip"],
                eos_cli=p2p_link.raw_eos_cli,
            )

            if p2p_link.tunnel.path_mtu_discovery is not None:
                tunnel_interface.path_mtu_discovery = p2p_link.tunnel.path_mtu_discovery

            if p2p_link_data["tunnel_mode"] == "ipsec" and p2p_link.tunnel.ipsec_profile:
                tunnel_interface.ipsec_profile = p2p_link.tunnel.ipsec_profile

            if p2p_link_data["ip"]:
                tunnel_interface.ip_address = p2p_link_data["ip"]

            if p2p_link_data["ipv6"]:
                tunnel_interface.ipv6_addresses.append(p2p_link_data["ipv6"])
                self.structured_config.ipv6_unicast_routing = True

            if p2p_link.include_in_underlay_protocol:
                self._apply_tunnel_ospf_config(p2p_link, p2p_link_data, tunnel_interface)
                self._apply_tunnel_isis_config(p2p_link, tunnel_interface)

            self._apply_tunnel_mpls_config(p2p_link, tunnel_interface)

            if p2p_link.tunnel_structured_config:
                self.custom_structured_configs.nested.tunnel_interfaces.obtain(tunnel_interface.name)._deepmerge(
                    p2p_link.tunnel_structured_config,
                    list_merge=self.custom_structured_configs.list_merge_strategy,
                )

            self.structured_config.tunnel_interfaces.append(tunnel_interface)

    def _apply_tunnel_ospf_config(
        self: AvdStructuredConfigCoreInterfacesAndL3EdgeProtocol,
        p2p_link: T_P2pLinksItem,
        p2p_link_data: dict,
        interface: EosCliConfigGen.TunnelInterfacesItem,
    ) -> None:
        if not self.shared_utils.underlay_ospf:
            return

        interface.ospf_network_point_to_point = True
        interface.ospf_area = str(self.inputs.underlay_ospf_area)

        if p2p_link.use_underlay_ospf_authentication is True:
            if not self.inputs.underlay_ospf_authentication.enabled:
                msg = (
                    f"'use_underlay_ospf_authentication' is set to true for {self.data_model}.p2p_links"
                    f"[{p2p_link_data['p2p_link_index']}] but 'underlay_ospf_authentication.enabled' is false. "
                    "Enable 'underlay_ospf_authentication.enabled'."
                )
                raise AristaAvdInvalidInputsError(msg)
            interface.ospf_authentication = "message-digest"
            for ospf_key in self.inputs.underlay_ospf_authentication.message_digest_keys:
                interface.ospf_message_digest_keys.append_new(
                    id=ospf_key.id,
                    hash_algorithm=ospf_key.hash_algorithm,
                    key=ospf_message_digest_encrypt(
                        password=ospf_key.cleartext_key,
                        key=interface.name,
                        hash_algorithm=ospf_key.hash_algorithm,
                        key_id=str(ospf_key.id),
                    ),
                )

    def _apply_tunnel_isis_config(
        self: AvdStructuredConfigCoreInterfacesAndL3EdgeProtocol,
        p2p_link: T_P2pLinksItem,
        interface: EosCliConfigGen.TunnelInterfacesItem,
    ) -> None:
        if not self.shared_utils.underlay_isis:
            return

        interface.isis_enable = self.shared_utils.isis_instance_name
        interface.isis_bfd = self.inputs.underlay_isis_bfd or None
        interface.isis_metric = default(p2p_link.isis_metric, self.inputs.isis_default_metric)
        interface.isis_network_point_to_point = p2p_link.isis_network_type == "point-to-point"
        interface.isis_hello_padding = p2p_link.isis_hello_padding

        isis_circuit_type: Literal["level-1", "level-2", "level-1-2"] = default(p2p_link.isis_circuit_type, self.inputs.isis_default_circuit_type)
        interface.isis_circuit_type = isis_circuit_type

        mode: Literal["md5", "text"] | None = default(p2p_link.isis_authentication_mode, self.inputs.underlay_isis_authentication_mode)
        interface.isis_authentication.both.mode = mode

        if p2p_link.isis_authentication_key is not None:
            interface.isis_authentication.both._update(key=p2p_link.isis_authentication_key, key_type="7")
        elif p2p_link.isis_authentication_cleartext_key is not None:
            interface.isis_authentication.both._update(
                key=isis_encrypt(
                    password=p2p_link.isis_authentication_cleartext_key,
                    key=cast("str", self.shared_utils.isis_instance_name),
                    mode=mode or "none",
                ),
                key_type="7",
            )
        elif (isis_authentication_key := self.shared_utils.underlay_isis_authentication_key) is not None:
            interface.isis_authentication.both._update(key=isis_authentication_key, key_type="7")

    def _apply_tunnel_mpls_config(
        self: AvdStructuredConfigCoreInterfacesAndL3EdgeProtocol,
        p2p_link: T_P2pLinksItem,
        interface: EosCliConfigGen.TunnelInterfacesItem,
    ) -> None:
        if not (self.shared_utils.mpls_lsr and default(p2p_link.mpls_ip, True)):  # noqa: FBT003
            return

        interface.mpls.ip = True
        if p2p_link.include_in_underlay_protocol is True and self.shared_utils.underlay_ldp and default(p2p_link.mpls_ldp, True):  # noqa: FBT003
            interface.mpls.ldp.interface = True
            interface.mpls.ldp.igp_sync = True
