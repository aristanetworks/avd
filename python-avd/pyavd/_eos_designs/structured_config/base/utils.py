# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import functools
from hashlib import sha1
from typing import TYPE_CHECKING, Generic, Literal, Protocol, TypeVar, cast

from pyavd._eos_designs.schema import EosDesigns
from pyavd._errors import AristaAvdError, AristaAvdInvalidInputsError, AristaAvdMissingVariableError
from pyavd._schema.models.type_vars import T_AvdModel
from pyavd._utils.password_utils.password import radius_encrypt, tacacs_encrypt

if TYPE_CHECKING:
    from collections.abc import Callable

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


T_ProfileModel = TypeVar("T_ProfileModel", bound="AvdModel")
T_TargetModel = TypeVar("T_TargetModel", bound="AvdModel")


class ProfileModelProtocol(Protocol):
    profile: str
    parent_profile: str


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


def resolve_profile(
    target_object: T_AvdModel,
    profile_list: AvdIndexedList[str, T_ProfileModel],
    profile_id: str | None,
) -> T_AvdModel:
    """
    Resolve the selected profile into a target input model.

    When no profile is selected, the provided target object is returned unchanged.
    Otherwise, the profile catalog is converted into a graph and the selected profile,
    including any parent profiles, is merged into a copy of the target object.

    Args:
        target_object: Input model receiving the resolved profile values.
        profile_list: Catalog of available profiles.
        profile_id: Selected profile ID to resolve.

    Returns:
        The target object with the selected profile applied.
    """
    if not profile_id:
        return target_object

    graph = _ProfileGraph._from_profile_list(profile_list, target_object)
    return graph._get_profile(profile_id)


class _ProfileGraphNode(Generic[T_AvdModel]):
    def __init__(self, profile_id: str, data: T_AvdModel | None = None) -> None:
        """
        Initialize one profile graph node.

        Args:
            profile_id: Profile ID represented by this node.
            data: Profile or target model data attached to the node.
        """
        self.profile_id: str = profile_id
        self.profile: T_AvdModel | None = data
        self.parent: _ProfileGraphNode[T_AvdModel] | None = None
        self.children: list[_ProfileGraphNode[T_AvdModel]] = []

    @functools.cached_property
    def data(self) -> T_AvdModel:
        """
        Return a deep copy of the node data.

        Access data through this property to avoid overwriting an original data. Also, this
        makes data copy a lazy operation, i.e. it's only executed if that's really needed to
        resolve profile
        """
        # Excluded from the coverage as this won't normally happen. _ProfileGraph._check_all_profiles_resolved
        # would raise an exception before reaching this point
        if self.profile is None:  # pragma: no cover
            msg = f"Profile '{self.profile_id}' is missing"
            raise AristaAvdInvalidInputsError(msg)
        return self.profile._deepcopy()

    def _as_target_object(self, target_object_cls: type[T_TargetModel]) -> T_TargetModel:
        """
        Cast node data to the target model type.

        Args:
            target_object_cls: Target input model class to cast the profile data into.

        Returns:
            A copy of the node data cast as the target model.
        """
        return self.data._cast_as(target_object_cls, ignore_extra_keys=True)


_UnifiedGraphNode = _ProfileGraphNode[T_AvdModel | T_ProfileModel]


class _ProfileGraph(Generic[T_AvdModel, T_ProfileModel]):
    """
    Catalog graph used to resolve selected profiles and their parent profiles once per selector.

    Graph has the single root node, which essentially contains the target model (depicted by `T_AvdModel`)
    to which the profiles are applied, and the nested tree from this root node that contains objects
    of type `T_ProfileModel`.
    While `T_ProfileModel` is duck-typing the target `T_AvdModel`, there's no
    inheritance relationship between them. To keep profile resolution lazy, profile models are not
    cast into `T_AvdModel` during the graph initialization, hence the need to treat them as
    2 different types
    """

    # To avoid a slightest chance of naming conflicts we just assume it to be empty string
    ROOT_NODE_ID = ""

    def __init__(self, target_object_cls: type[T_AvdModel]) -> None:
        """
        Initialize an empty profile graph.

        Args:
            target_object_cls: Target model class used when casting profile models during resolution.
        """
        self.nodes: dict[str, _UnifiedGraphNode] = {}
        # Cache ensures that the profile is loaded only when it's needed, and it's resolved exactly once
        self._get_profile_cached: Callable[[str | None], T_AvdModel] = functools.cache(self.__get_profile)
        self._target_object_cls = target_object_cls

    @classmethod
    def _from_profile_list(
        cls,
        catalog_list: AvdIndexedList[str, T_ProfileModel],
        target_object: T_AvdModel,
    ) -> _ProfileGraph[T_AvdModel, T_ProfileModel]:
        """
        Build a profile graph from a profile catalog.

        Args:
            catalog_list: Profile catalog keyed by profile ID.
            target_object: Base target model used as the synthetic root profile.

        Returns:
            A validated profile graph ready for profile resolution.
        """
        target_cls = type(target_object)
        graph = cls(target_cls)

        # Initialize the synthetic root profile. Profiles without parent_profile inherit from this empty root.
        graph.nodes[cls.ROOT_NODE_ID] = _UnifiedGraphNode(cls.ROOT_NODE_ID, target_object)

        for profile_id, profile_data_item in catalog_list.items():
            profile_data = cast("ProfileModelProtocol", profile_data_item)

            # setdefault ensures each profile id gets a single graph node, even if it was referenced as a parent first.
            node = graph.nodes.setdefault(profile_id, _UnifiedGraphNode(profile_id, profile_data_item))
            parent_node = graph.nodes.setdefault(profile_data.parent_profile, _UnifiedGraphNode(profile_data.parent_profile))

            node.profile = profile_data_item
            parent_node.children.append(node)
            node.parent = parent_node

        graph._check_all_profiles_resolved()
        graph._check_cycles()
        return graph

    def _check_all_profiles_resolved(self) -> None:
        """
        Raise if a parent profile reference points to an undefined profile.

        Raises:
            AristaAvdInvalidInputsError: If any referenced parent profile is missing from the catalog.
        """
        # Catch profiles referenced as parent_profile but not defined in the catalog.
        uninitialized = set()
        for profile_id, profile_node in self.nodes.items():
            if profile_id == self.ROOT_NODE_ID:
                continue
            if profile_node.profile is None:
                uninitialized.add(profile_id)
        if uninitialized:
            msg = f"Unresolved `parent_profile` references while trying to resolve profiles for {self._target_object_cls.__qualname__}: {uninitialized}"
            raise AristaAvdInvalidInputsError(msg)

    def _check_cycles(self) -> None:
        """Detect cycles in parent_profile references."""

        def _check_node(node: _UnifiedGraphNode, path: list[str]) -> None:
            """
            Traverse one graph node and raise on circular inheritance.

            Args:
                node: Current graph node being checked.
                path: Ordered profile IDs visited on the current traversal path.
            """
            if node.profile_id in path:
                cycle_path = [*path[path.index(node.profile_id) :], node.profile_id]
                msg = "Cycle detected while trying to resolve profiles for " + self._target_object_cls.__qualname__ + ": " + " -> ".join(cycle_path)
                raise AristaAvdInvalidInputsError(msg)

            if node.profile_id is not None:
                path = [*path, node.profile_id]

            for child in node.children:
                _check_node(child, path)

        for node in self.nodes.values():
            _check_node(node, [])

    def _get_profile(self, profile_id: str) -> T_AvdModel:
        """
        Get the resolved model by applying the giving profile.

        Args:
            profile_id: Id of the profile to apply on the target model

        Returns:
            Target model after the profile resolution
        """
        return self._get_profile_cached(profile_id)

    def __get_profile(self, profile_id: str) -> T_AvdModel:
        """
        Resolve one profile ID into the target model type.

        Args:
            profile_id: Profile ID to resolve.

        Returns:
            Target model data with parent profiles applied.
        """
        node = self.nodes.get(profile_id)
        if node is None:
            msg = f"Profile '{profile_id}' is missing while trying to resolve profiles for " + self._target_object_cls.__qualname__
            raise AristaAvdInvalidInputsError(msg)
        data = node._as_target_object(self._target_object_cls)
        if node.parent:
            sub_model = self._get_profile_cached(node.parent.profile_id)
            # Current profile values are preferred over parent profile values.
            data._deepinherit(sub_model)
        return data
