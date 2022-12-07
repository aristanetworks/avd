from __future__ import annotations

import re
from functools import cached_property
from hashlib import sha256

from ansible_collections.arista.avd.plugins.filter.convert_dicts import convert_dicts
from ansible_collections.arista.avd.plugins.filter.esi_management import generate_esi, generate_route_target
from ansible_collections.arista.avd.plugins.plugin_utils.merge import merge
from ansible_collections.arista.avd.plugins.plugin_utils.utils import default, get, get_item
from ansible_collections.arista.avd.roles.eos_designs.python_modules.interface_descriptions import AvdInterfaceDescriptions
from ansible_collections.arista.avd.roles.eos_designs.python_modules.ip_addressing import AvdIpAddressing


class UtilsMixin:
    """
    Mixin Class with internal functions.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    # Set type hints for Attributes of the main class as needed
    _hostvars: dict
    _avd_ip_addressing: AvdIpAddressing
    _avd_interface_descriptions: AvdInterfaceDescriptions

    @cached_property
    def _filtered_connected_endpoints(self) -> list:
        """
        Return list of endpoints defined under one of the keys in "connected_endpoint_keys"
        which are connected to this switch.

        Adapters are filtered to contain only the ones connected to this switch.
        """
        filtered_connected_endpoints = []
        for connected_endpoints_key in self._connected_endpoints_keys:
            connected_endpoints = convert_dicts(get(self._hostvars, connected_endpoints_key["key"], default=[]), "name")
            for connected_endpoint in connected_endpoints:
                if "adapters" not in connected_endpoint:
                    continue

                connected_endpoint["adapters"] = [adapter for adapter in connected_endpoint["adapters"] if self._hostname in adapter.get("switches", [])]

                for adapter_index, adapter in enumerate(connected_endpoint["adapters"]):
                    if "profile" not in adapter:
                        continue

                    port_profile = get_item(self._merged_port_profiles, "profile", adapter["profile"], default={})
                    adapter = merge(port_profile, adapter, list_merge="replace", destructive_merge=False)
                    adapter.pop("profile")
                    connected_endpoint["adapters"][adapter_index] = adapter

                connected_endpoint["type"] = connected_endpoints_key["type"]
                filtered_connected_endpoints.append(connected_endpoint)

        return filtered_connected_endpoints

    @cached_property
    def _filtered_network_ports(self) -> list:
        """
        Return list of endpoints defined under "network_ports"
        which are connected to this switch.
        """
        filtered_network_ports = []
        for network_port in get(self._hostvars, "network_ports", default=[]):
            if not self._match_regexes(network_port.get("switches"), self._hostname):
                continue

            if "profile" in network_port:
                port_profile = get_item(self._merged_port_profiles, "profile", network_port["profile"], default={})
                network_port = merge(port_profile, network_port, list_merge="replace", destructive_merge=False)
                network_port.pop("profile")

            filtered_network_ports.append(network_port)

        return filtered_network_ports

    def _match_regexes(self, regexes: list, value: str) -> bool:
        for regex in regexes:
            if re.match(rf"^{regex}$", value):
                return True

        return False

    @cached_property
    def _port_profiles(self) -> list:
        """
        Return list of "port_profiles"
        """
        return convert_dicts(get(self._hostvars, "port_profiles", default=[]), "profile")

    @cached_property
    def _merged_port_profiles(self) -> list:
        """
        Return list of merged "port_profiles" where "parent_profile" has been applied.
        """
        merged_port_profiles = []

        for port_profile in self._port_profiles:
            if "parent_profile" in port_profile:
                parent_profile = get_item(self._port_profiles, "profile", port_profile["parent_profile"], default={})
                port_profile = merge(parent_profile, port_profile, list_merge="replace", destructive_merge=False)
                port_profile.pop("parent_profile")
            merged_port_profiles.append(port_profile)

        return merged_port_profiles

    @cached_property
    def _connected_endpoints_keys(self) -> list:
        """
        Return connected_endpoints_keys converted to list
        """
        return convert_dicts(get(self._hostvars, "connected_endpoints_keys", default=[]), "key")

    @cached_property
    def _hostname(self) -> str:
        return get(self._hostvars, "switch.hostname", required=True)

    @cached_property
    def _link_tracking_groups(self) -> list | None:
        return get(self._hostvars, "switch.link_tracking_groups")

    @cached_property
    def _mlag(self) -> bool:
        return get(self._hostvars, "switch.mlag") is True

    @cached_property
    def _enable_trunk_groups(self) -> bool:
        return get(self._hostvars, "switch.enable_trunk_groups") is True

    @cached_property
    def _platform_settings_feature_support_interface_storm_control(self) -> bool:
        return get(self._hostvars, "switch.platform_settings.feature_support.interface_storm_control", default=True) is True

    @cached_property
    def _evpn_short_esi_prefix(self) -> str:
        return get(self._hostvars, "evpn_short_esi_prefix", required=True)

    def _get_short_esi(self, adapter: dict, channel_group_id: int, short_esi: str = None, hash_extra_value: str = "") -> str | None:
        """
        Return short_esi for one adapter
        """
        if len(set(adapter["switches"])) < 2:
            # Only configure ESI for multi-homing.
            return None

        # short_esi is only set when called from sub-interface port-channels.
        if short_esi is None:
            # Setting short_esi under port_channel will be deprecated in AVD4.0
            port_channel_short_esi = get(adapter, "port_channel.short_esi")
            if (short_esi := get(adapter, "ethernet_segment.short_esi", default=port_channel_short_esi)) is None:
                return None

        endpoint_ports: list = default(
            adapter.get("endpoint_ports"),
            adapter.get("server_ports"),
        )
        short_esi = str(short_esi)
        if short_esi.lower() == "auto":
            esi_hash_switches = "".join(adapter["switches"][:2])
            esi_hash_switch_ports = "".join(adapter["switch_ports"][:2])
            esi_hash_endpoint_ports = "".join(endpoint_ports[:2])
            esi_hash = sha256(
                f"{hash_extra_value}{esi_hash_switches}{esi_hash_switch_ports}{esi_hash_endpoint_ports}{channel_group_id}".encode("UTF-8")
            ).hexdigest()
            short_esi = re.sub(r"([0-9a-f]{4})", "\\1:", esi_hash)[:14]

        if len(short_esi.split(":")) != 3:
            return None

        return short_esi

    def _get_adapter_trunk_groups(self, adapter: dict, connected_endpoint: dict) -> dict | None:
        """
        Return trunk_groups for one adapter
        """
        if self._enable_trunk_groups and "trunk" in adapter.get("mode", ""):
            return get(adapter, "trunk_groups", required=True, org_key=f"'trunk_groups' for the connected_endpoint {connected_endpoint['name']}")

        return None

    def _get_adapter_storm_control(self, adapter: dict) -> dict | None:
        """
        Return storm_control for one adapter
        """
        if self._platform_settings_feature_support_interface_storm_control:
            return get(adapter, "storm_control")

        return None

    def _get_adapter_evpn_ethernet_segment_cfg(
        self,
        adapter: dict,
        short_esi: str,
        node_index: int,
        connected_endpoint: dict,
        default_df_algo: str = None,
        default_redundancy: str = None,
    ) -> dict | None:
        """
        Return evpn_ethernet_segment_cfg for one adapter
        """
        if short_esi is None:
            return None

        adapter_ethernet_segment: dict = adapter.get("ethernet_segment", {})
        evpn_ethernet_segment = {
            "identifier": generate_esi(short_esi, self._evpn_short_esi_prefix),
            "redundancy": adapter_ethernet_segment.get("redundancy", default_redundancy),
            "route_target": generate_route_target(short_esi),
        }
        if (designated_forwarder_algorithm := adapter_ethernet_segment.get("designated_forwarder_algorithm", default_df_algo)) is None:
            return evpn_ethernet_segment

        if designated_forwarder_algorithm == "modulus":
            evpn_ethernet_segment["designated_forwarder_election"] = {"algorithm": "modulus"}

        elif designated_forwarder_algorithm == "auto":
            auto_preferences = range((len(adapter["switches"]) - 1) * 100, -1, -100)
            evpn_ethernet_segment["designated_forwarder_election"] = {
                "algorithm": "preference",
                "preference_value": auto_preferences[node_index],
                "dont_preempt": adapter_ethernet_segment.get("dont_preempt"),
            }

        elif designated_forwarder_algorithm == "preference":
            # TODO: Add check for length of designated_forwarder_preferences
            designated_forwarder_preferences = get(
                adapter_ethernet_segment,
                "designated_forwarder_preferences",
                required=True,
                org_key=f"ethernet_segment.designated_forwarder_preferences for the connected_endpoint {connected_endpoint['name']}",
            )
            evpn_ethernet_segment["designated_forwarder_election"] = {
                "algorithm": "preference",
                "preference_value": designated_forwarder_preferences[node_index],
                "dont_preempt": adapter_ethernet_segment.get("dont_preempt"),
            }

        return evpn_ethernet_segment

    def _get_adapter_link_tracking_groups(self, adapter: dict) -> dict | None:
        """
        Return link_tracking_groups for one adapter
        """
        if not (get(adapter, "link_tracking.enabled") is True and self._link_tracking_groups is not None):
            return None

        return [
            {
                "name": get(adapter, "link_tracking.name", default=self._link_tracking_groups[0]["name"]),
                "direction": "downstream",
            }
        ]

    @cached_property
    def _ptp_profile(self) -> str | None:
        return get(self._hostvars, "switch.ptp.profile")

    @cached_property
    def _ptp_profiles(self) -> list:
        """
        Return ptp_profiles or []
        """
        return get(self._hostvars, "ptp_profiles", default=[])

    def _get_adapter_ptp(self, adapter: dict) -> dict | None:
        """
        Return ptp for one adapter
        """
        if get(adapter, "ptp.enable") is not True:
            return None

        ptp_config = {}

        # Apply PTP profile config
        if (ptp_profile_name := get(adapter, "ptp.profile", default=self._ptp_profile)) is not None:
            ptp_config.update(get_item(self._ptp_profiles, "profile", ptp_profile_name, default={}))

        # Apply Adapter PTP config
        ptp_config.update(adapter["ptp"])

        if ptp_config.pop("endpoint_role", None) != "bmca":
            ptp_config["role"] = "master"

        ptp_config.pop("profile", None)

        return ptp_config
