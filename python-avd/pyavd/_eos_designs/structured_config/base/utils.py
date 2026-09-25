# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import functools
from hashlib import sha1
from typing import TYPE_CHECKING, Literal, Protocol, cast

from pyavd._eos_designs.schema import EosDesigns
from pyavd._errors import AristaAvdError, AristaAvdInvalidInputsError, AristaAvdMissingVariableError
from pyavd._utils.password_utils.password import radius_encrypt, tacacs_encrypt

if TYPE_CHECKING:
    from collections.abc import Callable
    from typing import TypeAlias, TypeVar

    from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
    from pyavd._schema.models.avd_indexed_list import AvdIndexedList
    from pyavd._schema.models.avd_model import AvdModel

    from . import AvdStructuredConfigBaseProtocol

    T_Source_Interfaces = TypeVar(
        "T_Source_Interfaces",
        EosCliConfigGen.IpHttpClient,
        EosCliConfigGen.IpSshClient,
    )

    T_RadiusOrTacacsServer = TypeVar("T_RadiusOrTacacsServer", EosDesigns.AaaSettings.Radius.ServersItem, EosDesigns.AaaSettings.Tacacs.ServersItem)

    T_AvdStructuredConfigBase = TypeVar(
        "T_AvdStructuredConfigBase",
        bound="AvdStructuredConfigBaseProtocol",
    )
    StructuredConfigMethod: TypeAlias = Callable[[T_AvdStructuredConfigBase], None]


class UtilsMixin(Protocol):
    """
    Mixin Class with internal functions.

    Class should only be used as Mixin to a AvdStructuredConfig class or other Mixins.
    """

    def _build_source_interfaces(
        self: AvdStructuredConfigBaseProtocol,
        include_mgmt_interface: bool,
        include_inband_mgmt_interface: bool,
        error_context: str,
        output_type: type[T_Source_Interfaces],
    ) -> T_Source_Interfaces:
        """
        Return list of source interfaces with VRFs.

        Error context should be short and fit in "... configure {error_context} source-interface ..."

        Raises errors for duplicate VRFs or missing interfaces with the given error context.
        """
        source_interfaces = output_type()
        if include_mgmt_interface:
            if (self.shared_utils.oob_mgmt_ip is None) and (self.shared_utils.node_config.ipv6_mgmt_ip is None):
                msg = f"Unable to configure {error_context} source-interface since 'mgmt_ip' or 'ipv6_mgmt_ip' are not set."
                raise AristaAvdInvalidInputsError(msg)

            # mgmt_interface is always set (defaults to "Management1") so no need for error handling missing interface.
            if self.shared_utils.mgmt_interface_vrf != "default":
                source_interfaces.vrfs.append_new(source_interface=self.shared_utils.mgmt_interface, name=self.shared_utils.mgmt_interface_vrf)
            else:
                source_interfaces.source_interface = self.shared_utils.mgmt_interface

        if include_inband_mgmt_interface:
            # Check for missing interface
            if self.shared_utils.inband_mgmt_interface is None:
                msg = f"Unable to configure {error_context} source-interface since 'inband_mgmt_interface' is not set."
                raise AristaAvdInvalidInputsError(msg)

            # Check for duplicate VRF
            # inband_mgmt_vrf returns None in case of VRF "default", but here we want the "default" VRF name to have proper duplicate detection.
            inband_mgmt_vrf = self.shared_utils.inband_mgmt_vrf or "default"
            if include_mgmt_interface and (inband_mgmt_vrf == self.shared_utils.mgmt_interface_vrf):
                msg = f"Unable to configure multiple {error_context} source-interfaces for the same VRF '{inband_mgmt_vrf}'."
                raise AristaAvdError(msg)

            if inband_mgmt_vrf == "default":
                source_interfaces.source_interface = self.shared_utils.inband_mgmt_interface
            else:
                source_interfaces.vrfs.append_new(
                    source_interface=self.shared_utils.inband_mgmt_interface,
                    name=inband_mgmt_vrf,
                )

        return source_interfaces

    def _get_tacacs_or_radius_server_password(self: AvdStructuredConfigBaseProtocol, radius_or_tacacs_server: T_RadiusOrTacacsServer) -> str:
        """
        Retrieve the type 7 encrypted key for a RADIUS or TACACS+ server.

        This function checks for a pre-encrypted key or a cleartext key to generate
        the encrypted password. If neither is provided, it raises an error.

        Args:
            radius_or_tacacs_server: A server object from either RADIUS or TACACS+ configuration.

        Returns:
            The type 7 encrypted password.

        Raises:
            AristaAvdMissingVariableError: If both `key` and `cleartext_key` are missing.
        """
        if radius_or_tacacs_server.key is not None:
            return radius_or_tacacs_server.key

        if isinstance(radius_or_tacacs_server, EosDesigns.AaaSettings.Radius.ServersItem):
            encrypt_func = radius_encrypt
            path_prefix = f"aaa_settings.radius.servers[host={radius_or_tacacs_server.host}]"
        else:
            encrypt_func = tacacs_encrypt
            path_prefix = f"aaa_settings.tacacs.servers[host={radius_or_tacacs_server.host}]"

        if radius_or_tacacs_server.cleartext_key is not None:
            salt = cast("Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]", sum(ord(c) for c in radius_or_tacacs_server.host) % 16)
            return encrypt_func(radius_or_tacacs_server.cleartext_key, salt)

        msg = f"`{path_prefix}.key` or `{path_prefix}.cleartext_key`"
        raise AristaAvdMissingVariableError(msg)

    def get_salt(self: AvdStructuredConfigBaseProtocol, string: str) -> str:
        """
        Computes the SHA1 hash of the input string and returns a truncated version of the hash.

        The SHA1 hash is computed, and the resulting hexadecimal digest is truncated to a maximum of 16 characters.
        This function is flagged with 'NOSONAR' to indicate that the use of SHA1 is intentional
        and not a security vulnerability in this context, as it is used for generating a salt.

        Args:
            string: The input string to be hashed.

        Returns:
            A string representing the truncated SHA1 hash (salt), with a maximum length of 16 characters.
        """
        return sha1(string.encode(), usedforsecurity=False).hexdigest()[:16]  # NOSONAR

    def _set_monitor_connectivity_hosts(
        self: AvdStructuredConfigBaseProtocol,
        hosts: EosDesigns.MonitorConnectivity.Hosts | EosDesigns.MonitorConnectivity.VrfsItem.Hosts,
        monitor_connectivity_hosts: EosCliConfigGen.MonitorConnectivity.Hosts | EosCliConfigGen.MonitorConnectivity.VrfsItem.Hosts,
        interface_sets: EosDesigns.MonitorConnectivity.InterfaceSets | EosDesigns.MonitorConnectivity.VrfsItem.InterfaceSets,
        context: str,
    ) -> None:
        """
        Populate monitor connectivity hosts from EOS Designs host entries.

        Iterates over the provided design-level hosts and appends each one to the
        CLI config gen monitor connectivity hosts list, mapping all relevant fields.

        Args:
            hosts: Source host entries from EOS Designs, either at the global or
                VRF level of monitor connectivity configuration.
            monitor_connectivity_hosts: Target host list in the EOS CLI config gen
                structure where the mapped entries will be appended.
            interface_sets: The parent interface_sets to validate host local_interfaces against.
            context: Path prefix used in error messages (e.g. "monitor_connectivity" or "monitor_connectivity.vrfs[name=MGMT]").
        """
        for host in hosts:
            if host.local_interfaces is not None and host.local_interfaces not in interface_sets:
                msg = f"{context}.hosts[name={host.name}].local_interfaces '{host.local_interfaces}' has to be defined in {context}.interface_sets."
                raise AristaAvdInvalidInputsError(msg)
            monitor_connectivity_hosts.append_new(
                name=host.name,
                description=host.description,
                single_line_description=host.single_line_description,
                ip=host.ip,
                icmp_echo_size=host.icmp_echo_size,
                local_interfaces=host.local_interfaces,
                address_only=host.address_only,
                url=host.url,
            )


class Profileable:
    def __init__(self, catalog: str, profile_field: str, target_field: str) -> None:
        """
        Initialize profile handling for a structured config contributor.

        Args:
            catalog: attribute in the root of eos_designs schema from where the profile list is taken
            profile_field: attribute within node_config that selects which profile to apply
            target_field: attribute in the root of eos_desings schema where the target would be merged
                To ensure data is not lost, the original field is preserved and restored once the function exit
        """
        self._catalog = catalog
        self._profile_field = profile_field
        self._target_field = target_field

    def __call__(
        self,
        func: StructuredConfigMethod[T_AvdStructuredConfigBase],
    ) -> StructuredConfigMethod[T_AvdStructuredConfigBase]:
        catalog = self._catalog
        profile_field = self._profile_field
        target_field = self._target_field

        @functools.wraps(func)
        def wrapper(self: T_AvdStructuredConfigBase) -> None:
            profile_list = getattr(self.inputs, catalog)
            profile_id = getattr(self.shared_utils.node_config, profile_field)
            if not profile_id:
                func(self)
                return

            backup = getattr(self.inputs, target_field)
            graph = ProfileGraph._from_profile_list(profile_list, backup)
            setattr(self.inputs, target_field, graph._get_profile(profile_id))
            try:
                func(self)
            finally:
                setattr(self.inputs, target_field, backup)

        return wrapper


class ProfileGraphNode:
    def __init__(self, profile_id: str, data: AvdModel | None = None) -> None:
        self.profile_id: str = profile_id
        self.profile: AvdModel | None = data
        self.parent: ProfileGraphNode | None = None
        self.children: list[ProfileGraphNode] = []

    @property
    def id(self) -> str | None:
        return None if not self.profile_id else self.profile_id

    @functools.cached_property
    def data(self) -> AvdModel:
        # Access data through this property to avoid overwriting an original data. Also, this
        # makes data copy a lazy operation, i.e. it's only executed if that's really needed to
        # resolve profile
        if not self.profile:
            msg = f"Profile '{self.profile_id}' is missing"
            raise AristaAvdInvalidInputsError(msg)
        return self.profile._deepcopy()


class ProfileGraph:
    """Catalog graph used to resolve selected profiles and their parent profiles once per selector."""

    def __init__(self, target_object_cls: type[AvdModel]) -> None:
        self.nodes: dict[str, ProfileGraphNode] = {}
        # Cache ensures that the profile is loaded only when it's needed, and it's resolved exactly once
        self._lazy_load_profile: Callable[[str], AvdModel] = functools.cache(self._get_profile)
        self._target_object_cls = target_object_cls

    @classmethod
    def _from_profile_list(cls, catalog_list: AvdIndexedList, target_object: AvdModel) -> ProfileGraph:
        target_cls = type(target_object)
        graph = ProfileGraph(target_cls)

        # Initialize the synthetic root profile. Profiles without parent_profile inherit from this empty root.
        graph.nodes[""] = ProfileGraphNode("", target_object)

        for profile_id, profile_data in catalog_list.items():
            # setdefault ensures each profile id gets a single graph node, even if it was referenced as a parent first.
            node = graph.nodes.setdefault(profile_id, ProfileGraphNode(profile_id, profile_data))
            parent_node = graph.nodes.setdefault(
                profile_data.parent_profile, ProfileGraphNode(profile_data.parent_profile)
            )

            node.profile = profile_data
            parent_node.children.append(node)
            node.parent = parent_node

        graph._check_all_profiles_resolved()
        graph._check_cycles()
        return graph

    def _check_all_profiles_resolved(self) -> None:
        # Catch profiles referenced as parent_profile but not defined in the catalog.
        uninitialized = set()
        for profile_id, profile_node in self.nodes.items():
            if not profile_id:
                # Skip the synthetic root node.
                continue
            if not profile_node.profile:
                uninitialized.add(profile_id)
        if uninitialized:
            msg = f"Unresolved `parent_profile` references: {uninitialized}"
            raise AristaAvdInvalidInputsError(msg)

    def _check_cycles(self) -> None:
        """Detect cycles in parent_profile references."""
        def _check_node(node: ProfileGraphNode, path: list[str]) -> None:
            if node.id in path:
                cycle_path = [*path[path.index(node.id) :], cast("str", node.id)]
                msg = "Cycle detected: " + " -> ".join(cycle_path)
                raise AristaAvdInvalidInputsError(msg)

            if node.id is not None:
                path = [*path, node.id]

            for child in node.children:
                _check_node(child, path)

        for node in self.nodes.values():
            _check_node(node, [])

    def _get_profile(self, profile_id: str) -> AvdModel:
        node = self.nodes.get(profile_id)
        if node is None:
            msg = f"Profile '{profile_id}' is missing"
            raise AristaAvdInvalidInputsError(msg)
        if node.parent and node.parent.id:
            sub_model = self._lazy_load_profile(node.parent.id)
            # Current profile values are preferred over parent profile values.
            node.data._deepinherit(sub_model)
        return node.data
