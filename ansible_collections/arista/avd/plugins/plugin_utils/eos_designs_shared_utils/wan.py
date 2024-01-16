# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from ansible_collections.arista.avd.plugins.filter.natural_sort import natural_sort
from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError, AristaAvdMissingVariableError
from ansible_collections.arista.avd.plugins.plugin_utils.strip_empties import strip_empties_from_dict
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get, get_item

if TYPE_CHECKING:
    from .shared_utils import SharedUtils


class WanMixin:
    """
    Mixin Class providing a subset of SharedUtils
    Class should only be used as Mixin to the SharedUtils class
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def wan_mode(self: SharedUtils) -> str:
        return get(self.hostvars, "wan_mode", default="cv-pathfinder")

    @cached_property
    def wan_role(self: SharedUtils) -> str | None:
        if self.underlay_router is False or self.wan_mode is None:
            return None

        default_wan_role = get(self.node_type_key_data, "default_wan_role", default=None)
        wan_role = get(self.switch_data_combined, "wan_role", default=default_wan_role)
        if wan_role is not None and self.overlay_routing_protocol != "ibgp":
            raise AristaAvdError("Only 'ibgp' is supported as 'overlay_routing_protocol' for WAN nodes.")
        if wan_role == "server" and self.evpn_role != "server":
            raise AristaAvdError("'wan_role' server requires 'evpn_role' server.")
        if wan_role == "client" and self.evpn_role != "client":
            raise AristaAvdError("'wan_role' client requires 'evpn_role' client.")
        return wan_role

    @cached_property
    def wan_listen_ranges(self) -> list:
        return get(
            self.bgp_peer_groups["wan_overlay_peers"],
            "listen_range_prefixes",
            required=True,
            org_key="bgp_peer_groups.wan_overlay_peers.listen_range_prefixes",
        )

    @cached_property
    def cv_pathfinder_role(self: SharedUtils) -> str | None:
        if self.underlay_router is False or self.wan_mode != "cv-pathfinder":
            return None

        default_cv_pathfinder_role = get(self.node_type_key_data, "default_cv_pathfinder_role", default=None)
        cv_pathfinder_role = get(self.switch_data_combined, "cv_pathfinder_role", default=default_cv_pathfinder_role)
        if cv_pathfinder_role == "pathfinder" and self.wan_role != "server":
            raise AristaAvdError("'wan_role' must be 'server' when 'cv_pathfinder_role' is set to 'pathfinder'")
        if cv_pathfinder_role in ["transit", "edge"] and self.wan_role != "client":
            raise AristaAvdError("'wan_role' must be 'client' when 'cv_pathfinder_role' is set to 'transit' or 'edge'")
        return cv_pathfinder_role

    @cached_property
    def wan_interfaces(self: SharedUtils) -> list:
        """
        As a first approach, only interfaces under l3edge.l3_interfaces can be considered
        as WAN interfaces.
        This may need to be made wider.
        This also may require a different format for the dictionaries inside the list.
        """
        if self.wan_role is None:
            return []

        wan_interfaces = []
        for interface in self.l3_interfaces:
            if get(interface, "wan_carrier") is not None:
                wan_interfaces.append(interface)

        return wan_interfaces

    @cached_property
    def wan_carriers(self: SharedUtils) -> list:
        return get(self.hostvars, "wan_carriers", required=True)

    @cached_property
    def wan_local_carriers(self: SharedUtils) -> list:
        """
        List of carriers present on this router based on the wan_interfaces with the associated WAN interfaces
            interfaces:
              - name: ...
                ip: ... (for route-servers the IP may come from wan_route_servers)
        """
        if not self.wan_role:
            return []

        local_carriers_dict = {}
        for interface in self.wan_interfaces:
            interface_carrier = interface["wan_carrier"]
            if interface_carrier not in local_carriers_dict:
                local_carriers_dict[interface_carrier] = get_item(
                    self.wan_carriers,
                    "name",
                    interface["wan_carrier"],
                    required=True,
                    custom_error_msg=f"WAN carrier {interface['wan_carrier']} is not in the available carriers defined in `wan_carriers`",
                ).copy()
                local_carriers_dict[interface_carrier]["interfaces"] = []

            local_carriers_dict[interface_carrier]["interfaces"].append(
                {
                    "name": get(interface, "name", required=True),
                    "ip_address": self.get_public_ip_for_wan_interface(interface),
                    "connected_to_pathfinder": get(interface, "connected_to_pathfinder", default=True),
                }
            )

        return list(local_carriers_dict.values())

    @cached_property
    def wan_path_groups(self: SharedUtils) -> list:
        return get(self.hostvars, "wan_path_groups", required=True)

    @cached_property
    def wan_local_path_groups(self: SharedUtils) -> list:
        """
        List of path_groups present on this router based on the local carriers.
        Also add for each path_groups the local interfaces in a data structure
            interfaces:
              - name: ...
                ip: ...
        """
        if self.wan_role is None:
            return []

        local_path_groups_dict = {}

        for carrier in self.wan_local_carriers:
            path_group_name = get(carrier, "path_group", required=True)
            if path_group_name not in local_path_groups_dict:
                local_path_groups_dict[path_group_name] = get_item(
                    self.wan_path_groups,
                    "name",
                    path_group_name,
                    required=True,
                    custom_error_msg=(
                        f"WAN path_group {path_group_name} defined for a WAN carrier is not in the available path_groups defined in `wan_path_groups`"
                    ),
                ).copy()
                local_path_groups_dict[path_group_name]["interfaces"] = []

            local_path_groups_dict[path_group_name]["interfaces"].extend(carrier["interfaces"])

        return list(local_path_groups_dict.values())

    @cached_property
    def this_wan_route_server(self: SharedUtils) -> dict:
        """
        Returns the instance for this wan_rs found under wan_route_servers.
        Should only be called when the device is actually a wan_rs.
        """
        wan_route_servers = get(self.hostvars, "wan_route_servers", default=[])
        return get_item(wan_route_servers, "hostname", self.hostname, default={})

    def get_public_ip_for_wan_interface(self: SharedUtils, interface: dict) -> str:
        """
        Takes a dict which looks like `l3_interface` from node config

        If not a WAN route-server this just returns the interface IP.

        For WAN route-servers we try to find the IP under wan_route_servers.path_groups.interfaces.
        If not found we use the IP under the interface, unless it is "dhcp" where we raise.
        """
        if self.wan_role != "server":
            return interface["ip"]

        for path_group in self.this_wan_route_server.get("path_groups", []):
            if (found_interface := get_item(path_group["interfaces"], "name", interface["name"])) is None:
                continue

            if found_interface.get("ip_address") is not None:
                return found_interface["ip_address"]

        if interface["ip"] == "dhcp":
            raise AristaAvdError(
                f"The IP address for WAN interface '{interface['name']}' on Route Server '{self.hostname}' is set 'dhcp'."
                "Clients need to peer with a static IP which must be set under the 'wan_route_servers.path_groups.interfaces' key."
            )

        return interface["ip"]

    @cached_property
    def wan_site(self: SharedUtils) -> dict:
        """
        WAN site for CV Pathfinder
        """
        node_defined_site = get(
            self.switch_data_combined,
            "cv_pathfinder_site",
            required=True,
            org_key="A node variable 'cv_pathfinder_site' must be defined when 'cv_pathfinder_role' is 'edge' or 'transit'.",
        )
        sites = get(self.wan_region, "sites", required=True, org_key=f"The CV Pathfinder region '{self.wan_region['name']}' is missing a list of sites")
        return get_item(
            sites,
            "name",
            node_defined_site,
            required=True,
            custom_error_msg=(
                f"The 'cv_pathfinder_site '{node_defined_site}' defined at the node level could not be found under the 'sites' list for the region"
                f" '{self.wan_region['name']}'."
            ),
        )

    @cached_property
    def wan_region(self: SharedUtils) -> dict:
        """
        WAN region for CV Pathfinder

        Also checking if site names are unique across all regions.
        """
        node_defined_region = get(
            self.switch_data_combined,
            "cv_pathfinder_region",
            required=True,
            org_key="A node variable 'cv_pathfinder_region' must be defined when 'cv_pathfinder_role' is 'edge' or 'transit'.",
        )
        regions = get(
            self.hostvars, "cv_pathfinder_regions", required=True, org_key="'cv_pathfinder_regions' key must be set when 'wan_mode' is 'cv-pathfinder'."
        )

        # Verify that site names are unique across all regions.
        site_names = [site["name"] for region in regions for site in region["sites"]]
        if len(site_names) != len(set(site_names)):
            # We have some site names that are not unique
            # Now find them (slow so no need to do if we don't have duplicates)
            duplicate_site_names = [site_name for site_name in site_names if site_names.count(site_name) > 1]
            raise AristaAvdError(
                "WAN Site names must be unique across all regions. "
                f"Found the following duplicate site name(s) under 'cv_pathfinder_regions.[].sites. {duplicate_site_names}"
            )

        return get_item(
            regions,
            "name",
            node_defined_region,
            required=True,
            custom_error_msg="The 'cv_pathfinder_region' defined at the node level could not be found under the 'cv_pathfinder_regions' key.",
        )

    @property
    def wan_zone(self: SharedUtils) -> dict:
        """
        WAN zone for Pathfinder

        Currently, only default zone DEFAULT-ZONE with ID 1 is supported.
        """
        # Injecting zone DEFAULT-ZONE with id 1.
        return {"name": "DEFAULT-ZONE", "id": 1}

    @cached_property
    def filtered_wan_route_servers(self: SharedUtils) -> dict:
        """
        Return a dict keyed by Wan RR based on the the wan_mode type with only the path_groups the router should connect to.

        It the RR is part of the inventory, the peer_facts are read..
        If any key is specified in the variables, it overwrites whatever is in the peer_facts.

        If no peer_fact is found the variables are required in the inventory.
        """
        wan_route_servers = {}

        wan_route_servers_list = get(self.hostvars, "wan_route_servers", default=[])

        for wan_rs_dict in natural_sort(wan_route_servers_list, sort_key="hostname"):
            # These remote gw can be outside of the inventory
            wan_rs = wan_rs_dict["hostname"]

            if wan_rs == self.hostname:
                # Don't add yourself
                continue

            if (peer_facts := self.get_peer_facts(wan_rs, required=False)) is not None:
                # Found a matching server in inventory
                bgp_as = peer_facts.get("bgp_as")
                # Only ibgp is supported for WAN so raise if peer from peer_facts BGP AS is different from ours.
                if bgp_as != self.bgp_as:
                    raise AristaAvdError(f"Only iBGP is supported for WAN, the BGP AS {bgp_as} on {wan_rs} is different from our own: {self.bgp_as}.")

                # Prefer values coming from the input variables over peer facts
                router_id = get(wan_rs_dict, "router_id", default=peer_facts.get("router_id"))
                wan_path_groups = get(wan_rs_dict, "path_groups", default=peer_facts.get("wan_path_groups"))

                if router_id is None:
                    raise AristaAvdMissingVariableError(
                        f"'router_id' is missing for peering with {wan_rs}, either set it in under 'wan_route_servers' or something is wrong with the peer"
                        " facts."
                    )
                if wan_path_groups is None:
                    raise AristaAvdMissingVariableError(
                        f"'wan_path_groups' is missing for peering with {wan_rs}, either set it in under 'wan_route_servers'"
                        " or something is wrong with the peer facts."
                    )

            else:
                # Retrieve the values from the dictionary, making them required if the peer_facts were not found
                router_id = get(wan_rs_dict, "router_id", required=True)
                wan_path_groups = get(
                    wan_rs_dict,
                    "path_groups",
                    required=True,
                    org_key=(
                        f"'path_groups' is missing for peering with {wan_rs} which was not found in the inventory, either set it in under 'wan_route_servers'"
                        " or check your inventory."
                    ),
                )

            # Filtering wan_path_groups to only take the ones this device uses to connect to pathfinders.
            wan_rs_result_dict = {
                "router_id": router_id,
                "wan_path_groups": [path_group for path_group in wan_path_groups if self.should_connect_to_wan_rs([path_group["name"]])],
            }

            wan_route_servers[wan_rs] = strip_empties_from_dict(wan_rs_result_dict)

        return wan_route_servers

    def should_connect_to_wan_rs(self: SharedUtils, path_groups: list) -> bool:
        """
        This helper implements whether or not a connection to the wan_router_server should be made or not based on a list of path-groups.

        To do this the logic is the following:
        * Look at the wan_interfaces on the router and check if there is any path-group in common with the RR where
          `connected_to_pathfinder` is not False.
        """
        return any(
            local_path_group["name"] in path_groups and any(wan_interface["connected_to_pathfinder"] for wan_interface in local_path_group["interfaces"])
            for local_path_group in self.wan_local_path_groups
        )
