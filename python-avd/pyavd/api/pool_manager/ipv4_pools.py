# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import json
import os
from bisect import bisect_left
from copy import deepcopy
from dataclasses import dataclass, field
from ipaddress import IPv4Address, IPv4Interface, IPv4Network
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import TYPE_CHECKING, Any, Literal, cast

from yaml import CSafeLoader, YAMLError, dump, load

from pyavd._errors import AristaAvdInvalidInputsError

from .base_classes import Pool, PoolAssignment, PoolCollection

if TYPE_CHECKING:
    from yaml.nodes import MappingNode

ResourceType = Literal["host", "subnet"]

FILE_HEADER = """\
# This file contains persistent IPv4 reservations managed by AVD eos_designs.
# After merging, run AVD to validate reservations, including those for absent devices.
# Resolve conflicting reservations deliberately before deployment; AVD will not silently renumber owners.
"""


def node_owner(hostname: str, purpose: str) -> str:
    """Identify an allocation independently of a node ID, subnet selection, or allocation order."""
    return json.dumps(["node", hostname, purpose], separators=(",", ":"))


def link_owner(endpoint_a: tuple[str, str], endpoint_b: tuple[str, str], purpose: str) -> str:
    """Identify a link independently of which endpoint requests its shared subnet first."""
    return json.dumps(["link", *sorted((endpoint_a, endpoint_b)), purpose], separators=(",", ":"))


def _describe_owner(owner: str) -> str:
    """Keep persistent identity encoding out of allocation diagnostics."""
    try:
        identity = json.loads(owner)
    except ValueError:
        return owner
    if isinstance(identity, list):
        if len(identity) == 3 and identity[0] == "node" and all(isinstance(item, str) for item in identity):
            return f"{identity[1]} ({identity[2]})"
        if (
            len(identity) == 4
            and identity[0] == "link"
            and isinstance(identity[3], str)
            and all(isinstance(endpoint, list) and len(endpoint) == 2 and all(isinstance(item, str) for item in endpoint) for endpoint in identity[1:3])
        ):
            return f"{identity[1][0]}:{identity[1][1]} <-> {identity[2][0]}:{identity[2][1]} ({identity[3]})"
    return owner


class _UniqueKeyLoader(CSafeLoader):
    """Reject duplicate YAML keys before constructing dictionaries can discard reservations."""

    def construct_mapping(self, node: MappingNode, deep: bool = False) -> dict:
        self.flatten_mapping(node)
        result = {}
        for key_node, value_node in node.value:
            key = self.construct_object(key_node, deep=deep)
            if not isinstance(key, str):
                msg = "IPv4 state mapping keys must be strings."
                raise TypeError(msg)
            if key in result:
                msg = f"Duplicate YAML key '{key}'."
                raise ValueError(msg)
            result[key] = self.construct_object(value_node, deep=deep)
        return result


@dataclass(frozen=True)
class Ipv4PoolDefinition:
    """Allocation constraints supplied by a consumer; no eos_designs or SharedUtils dependency."""

    subnet: str
    vrf: str
    network: IPv4Network
    resource_type: ResourceType = "host"
    prefix_length: int | None = None
    first: int | None = None
    last: int | None = None
    descending: bool = False

    def __post_init__(self) -> None:
        if not self.subnet or not self.vrf or self.resource_type not in ("host", "subnet"):
            msg = "An IPv4 pool requires a subnet name, VRF, and host or subnet resource type."
            raise ValueError(msg)
        if self.resource_type == "subnet":
            if type(self.prefix_length) is not int or not self.network.prefixlen <= self.prefix_length <= 32:
                msg = f"Requested prefix length must be between {self.network.prefixlen} and 32 for '{self.subnet}'."
                raise ValueError(msg)
        elif self.prefix_length is not None:
            msg = "A host pool uses its parent network's prefix length."
            raise ValueError(msg)
        first, last = self.bounds
        exclude_endpoints = self.resource_type == "host" and self.network.prefixlen < 31
        if not int(self.network.network_address) + exclude_endpoints <= first <= last <= int(self.network.broadcast_address) - exclude_endpoints:
            msg = f"Invalid allocation bounds for IPv4 subnet '{self.subnet}'."
            raise ValueError(msg)

    @property
    def bounds(self) -> tuple[int, int]:
        exclude_endpoints = self.resource_type == "host" and self.network.prefixlen < 31
        return (
            int(self.network.network_address) + exclude_endpoints if self.first is None else self.first,
            int(self.network.broadcast_address) - exclude_endpoints if self.last is None else self.last,
        )

    @property
    def key(self) -> str:
        return json.dumps([self.vrf, self.subnet, self.resource_type, self.prefix_length], separators=(",", ":"))


@dataclass(frozen=True)
class _Reservation:
    first: int
    last: int
    owner: str
    source: str


class Ipv4Reservations:
    """VRF-aware reservations shared by host and subnet pools, including transient fixed claims."""

    def __init__(self, context: str) -> None:
        self.context = context
        self._claims: dict[str, list[_Reservation]] = {}

    def conflict(self, vrf: str, first: int, last: int) -> _Reservation | None:
        claims = self._claims.get(vrf, [])
        index = bisect_left(claims, first, key=lambda claim: claim.first)
        if index and claims[index - 1].last >= first:
            return claims[index - 1]
        if index < len(claims) and claims[index].first <= last:
            return claims[index]
        return None

    def reserve(self, vrf: str, first: int, last: int, owner: str, source: str) -> None:
        previous = self.conflict(vrf, first, last)
        if previous is not None:
            if (previous.owner, previous.first, previous.last) == (owner, first, last):
                return
            address = str(IPv4Address(first)) if first == last else f"{IPv4Address(first)}-{IPv4Address(last)}"
            msg = (
                f"IPv4 allocation '{address}' conflicts between '{_describe_owner(previous.owner)}' "
                f"({previous.source}) and '{_describe_owner(owner)}' ({source}) in {self.context}, VRF '{vrf}'. "
                "Correct or explicitly release the intended reservation and re-run AVD before deployment."
            )
            raise AristaAvdInvalidInputsError(msg)
        claims = self._claims.setdefault(vrf, [])
        index = bisect_left(claims, first, key=lambda claim: claim.first)
        claims.insert(index, _Reservation(first, last, owner, source))


@dataclass
class Ipv4Pool(Pool[str]):
    """A host or subnet pool using the shared assignment lifecycle and fabric-wide reservations."""

    definition: Ipv4PoolDefinition | None = None
    _next_candidate: int | None = field(init=False, default=None, repr=False)

    @property
    def identity(self) -> tuple[str, str, ResourceType, int | None]:
        key = json.loads(self.pool_key)
        if (
            not isinstance(key, list)
            or len(key) != 4
            or not all(isinstance(item, str) and item for item in key[:2])
            or key[2] not in ("host", "subnet")
            or (key[2] == "host" and key[3] is not None)
            or (key[2] == "subnet" and (type(key[3]) is not int or not 0 <= key[3] <= 32))
        ):
            msg = f"Invalid IPv4 pool key '{self.pool_key}'."
            raise ValueError(msg)
        if json.dumps(key, separators=(",", ":")) != self.pool_key:
            msg = f"Noncanonical IPv4 pool key '{self.pool_key}'."
            raise ValueError(msg)
        return key[0], key[1], key[2], key[3]

    def extent(self, value: str) -> tuple[int, int]:
        _, _, resource_type, prefix_length = self.identity
        if "/" not in value:
            msg = f"Expected an IPv4 address/prefix, got '{value}'."
            raise ValueError(msg)
        if resource_type == "host":
            interface = IPv4Interface(value)
            if str(interface) == value:
                return int(interface.ip), int(interface.ip)
        else:
            network = IPv4Network(value)
            if str(network) == value and network.prefixlen == prefix_length:
                return int(network.network_address), int(network.broadcast_address)
        msg = f"Invalid canonical {resource_type} allocation '{value}' for pool '{self.pool_key}'."
        raise ValueError(msg)

    @property
    def description(self) -> str:
        vrf, subnet, resource_type, _ = self.identity
        return f"{resource_type} pool '{subnet}' in VRF '{vrf}'"

    def _in_bounds(self, value: str) -> bool:
        if self.definition is None:
            msg = f"IPv4 pool '{self.pool_key}' must be configured before allocating."
            raise ValueError(msg)
        first, last = self.extent(value)
        lower, upper = self.definition.bounds
        if self.definition.resource_type == "host" and IPv4Interface(value).network != self.definition.network:
            return False
        return lower <= first <= last <= upper

    def _is_value_available(self, value: str, key: str | None = None) -> bool:
        if not self._in_bounds(value):
            return False
        first, last = self.extent(value)
        collection = self._ipv4_collection
        conflict = collection.reservations.conflict(self.identity[0], first, last)
        return conflict is None or (conflict.owner, conflict.first, conflict.last) == (key, first, last)

    @property
    def _ipv4_collection(self) -> Ipv4PoolCollection:
        # Pools are only constructed by their matching collection type.
        if not isinstance(self.collection, Ipv4PoolCollection):
            msg = "An IPv4 pool requires an IPv4 pool collection."
            raise TypeError(msg)
        return self.collection

    def _next_available(self) -> str:
        if self.definition is None:
            msg = f"IPv4 pool '{self.pool_key}' must be configured before allocating."
            raise ValueError(msg)
        definition = self.definition
        first, last = definition.bounds
        size = 1 if definition.prefix_length is None else 1 << (32 - definition.prefix_length)
        candidate = self._next_candidate
        if candidate is None:
            candidate = (last + 1) // size * size - size if definition.descending else (first + size - 1) // size * size
        while first <= candidate and candidate + size - 1 <= last:
            conflict = self._ipv4_collection.reservations.conflict(definition.vrf, candidate, candidate + size - 1)
            if conflict is None:
                prefix = definition.network.prefixlen if definition.resource_type == "host" else definition.prefix_length
                self._next_candidate = candidate - size if definition.descending else candidate + size
                return f"{IPv4Address(candidate)}/{prefix}"
            # Skip a whole conflicting interval, including very large reserved prefixes.
            candidate = conflict.first // size * size - size if definition.descending else (conflict.last + size) // size * size
        resource = "addresses" if definition.resource_type == "host" else "subnets"
        msg = f"No available IPv4 {resource} in subnet '{definition.subnet}', VRF '{definition.vrf}', {self._ipv4_collection.context}."
        raise AristaAvdInvalidInputsError(msg)

    def get_assignment(self, key: str, requested_value: str | None = None) -> PoolAssignment[str]:
        collection = self._ipv4_collection
        if not isinstance(key, str) or not key:
            msg = f"Allocation owners must be nonempty strings, {collection.context}."
            raise AristaAvdInvalidInputsError(msg)
        for pool in collection._pools.values():
            if key in pool.assignments and pool is not self:
                previous_pool = cast("Ipv4Pool", pool)
                msg = (
                    f"Persisted IPv4 assignment for '{_describe_owner(key)}' belongs to "
                    f"{previous_pool.description}, not {self.description}, {collection.context}. "
                    "Restore the selection or explicitly release the reservation before reallocating."
                )
                raise AristaAvdInvalidInputsError(msg)
        previous = self.assignments.get(key)
        if previous is not None and (not self._in_bounds(previous.value) or requested_value not in (None, previous.value)):
            msg = (
                f"Persisted IPv4 assignment '{previous.value}' for '{_describe_owner(key)}' is invalid for {self.description}, {collection.context}. "
                "Restore the definition or explicitly release the reservation before reallocating."
            )
            raise AristaAvdInvalidInputsError(msg)
        if requested_value is not None:
            try:
                in_bounds = self._in_bounds(requested_value)
            except ValueError as error:
                msg = f"Invalid requested IPv4 allocation '{requested_value}' for '{_describe_owner(key)}', {collection.context}: {error}"
                raise AristaAvdInvalidInputsError(msg) from error
            if not in_bounds:
                msg = (
                    f"Requested IPv4 allocation '{requested_value}' for '{_describe_owner(key)}' is outside pool '{self.identity[1]}' "
                    f"in VRF '{self.identity[0]}', {collection.context}."
                )
                raise AristaAvdInvalidInputsError(msg)
            first, last = self.extent(requested_value)
            collection.reservations.reserve(self.identity[0], first, last, key, f"{self.description}, {requested_value}")
        assignment = super().get_assignment(key, requested_value)
        first, last = self.extent(assignment.value)
        collection.reservations.reserve(self.identity[0], first, last, key, f"{self.description}, {assignment.value}")
        return assignment


@dataclass
class Ipv4PoolCollection(PoolCollection[str]):
    """Persistent IPv4 pools retain reservations and share the base collection lifecycle."""

    pools_key: str = "ipv4_pools"
    pool_cls: type[Pool[str]] = Ipv4Pool
    assignment_cls: type[PoolAssignment[str]] = PoolAssignment[str]
    value_type: type = str
    min_value: str = ""
    remove_stale_assignments: bool = False
    reservations: Ipv4Reservations = field(init=False)
    _snapshot: bytes | None = field(init=False, default=None)
    _needs_migration: bool = field(init=False, default=False)

    @property
    def context(self) -> str:
        try:
            display_path = self.pools_file.relative_to(Path.cwd())
        except ValueError:
            display_path = self.pools_file
        return f"IPv4 allocation state '{display_path}'"

    def _invalid_state_error(self, error: Exception) -> Exception:
        return AristaAvdInvalidInputsError(f"Invalid {self.context}: {error}")

    def _read_file_data(self) -> Any:
        self._snapshot = self._read()
        if self._snapshot is None:
            return None
        try:
            return load(self._snapshot, Loader=_UniqueKeyLoader)  # noqa: S506 - CSafeLoader subclass rejecting duplicate keys.
        except YAMLError as error:
            raise self._invalid_state_error(error) from error

    def _load_file_data(self, file_data: Any) -> dict[str, Pool[str]]:
        if self._snapshot is None:
            return {}
        if not isinstance(file_data, dict) or type(file_data.get("version")) is not int:
            msg = "Expected a versioned IPv4 pool collection."
            raise ValueError(msg)
        if file_data["version"] == 1:
            return self._load_v1(file_data)
        if file_data["version"] != 2 or set(file_data) != {"version", self.pools_key} or not isinstance(file_data[self.pools_key], dict):
            msg = "Expected version: 2 and an ipv4_pools mapping."
            raise ValueError(msg)
        return self.load(file_data[self.pools_key])

    def _load_v1(self, data: dict) -> dict[str, Pool[str]]:
        if set(data) != {"version", "allocations"} or not isinstance(data["allocations"], list):
            msg = "Expected version: 1 and an allocations list."
            raise ValueError(msg)
        pools: dict[str, dict[str, str]] = {}
        owners: set[str] = set()
        for record in data["allocations"]:
            if not isinstance(record, dict) or set(record) != {"owner", "subnet", "vrf", "address"}:
                msg = "Each allocation must contain owner, subnet, vrf, and address."
                raise ValueError(msg)
            if not all(isinstance(value, str) and value for value in record.values()):
                msg = "Allocation fields must be nonempty strings."
                raise ValueError(msg)
            owner = node_owner(record["owner"], "oob_mgmt")
            if owner in owners:
                msg = f"Duplicate allocation owner '{record['owner']}'."
                raise ValueError(msg)
            owners.add(owner)
            definition = Ipv4PoolDefinition(record["subnet"], record["vrf"], IPv4Interface(record["address"]).network)
            pools.setdefault(definition.key, {})[owner] = record["address"]
        # Loading alone must not publish a migration after a failed facts build.
        self._needs_migration = True
        return self.load(pools)

    def validate(self) -> None:
        self.reservations = Ipv4Reservations(self.context)
        owners: set[str] = set()
        for pool in self._pools.values():
            if not isinstance(pool, Ipv4Pool):
                msg = "Expected an IPv4 pool."
                raise TypeError(msg)
            vrf, _, _, _ = pool.identity
            for assignment in pool.assignments.values():
                if not assignment.key:
                    msg = "Allocation owners must be nonempty strings."
                    raise ValueError(msg)
                if assignment.key in owners:
                    msg = f"Duplicate allocation owner '{_describe_owner(assignment.key)}' in {self.context}."
                    raise ValueError(msg)
                owners.add(assignment.key)
                first, last = pool.extent(assignment.value)
                self.reservations.reserve(vrf, first, last, assignment.key, f"{pool.description}, {assignment.value}")

    def get_ipv4_pool(self, definition: Ipv4PoolDefinition) -> Ipv4Pool:
        pool = self.get_pool(definition.key)
        if not isinstance(pool, Ipv4Pool):
            msg = "Expected an IPv4 pool."
            raise TypeError(msg)
        if pool.definition is not None and pool.definition != definition:
            msg = f"Conflicting definitions of IPv4 pool '{definition.key}' in {self.context}."
            raise AristaAvdInvalidInputsError(msg)
        pool.definition = definition
        return pool

    def stage(self) -> Ipv4PoolCollection:
        """Prepare isolated working pools; callers publish them only after successful facts generation."""
        staged = deepcopy(self)
        for pool in staged._pools.values():
            if isinstance(pool, Ipv4Pool):
                pool.definition = None
                pool._next_candidate = None
        staged.validate()
        staged.changed = staged.changed or staged._needs_migration
        return staged

    def publish(self, staged: Ipv4PoolCollection) -> None:
        """Publish a successful build's pool state without retaining its transient reservations."""
        if staged.pools_file != self.pools_file or staged._snapshot != self._snapshot:
            msg = "Cannot publish IPv4 pools staged from a different collection revision."
            raise ValueError(msg)
        staged.validate()
        self._pools = staged._pools
        for pool in self._pools.values():
            pool.collection = self
        self.changed = staged.changed
        self._needs_migration = staged._needs_migration
        self.validate()

    def _serialize_file(self, dumper_cls: type) -> str:
        return FILE_HEADER + dump({"version": 2, self.pools_key: self.as_dict()}, Dumper=dumper_cls, sort_keys=False)

    def _read(self) -> bytes | None:
        try:
            return self.pools_file.read_bytes()
        except FileNotFoundError:
            return None

    def _write_file(self, content: str) -> None:
        self.pools_file.parent.mkdir(mode=0o775, parents=True, exist_ok=True)
        lock_path = self.pools_file.with_suffix(".yml.lock")
        try:
            lock_path.touch(exist_ok=False)
        except FileExistsError as error:
            msg = f"{self.context} is locked by another writer. Re-run when that build completes."
            raise AristaAvdInvalidInputsError(msg) from error
        try:
            if self._read() != self._snapshot:
                msg = f"{self.context} changed during this build. Re-run against the updated state."
                raise AristaAvdInvalidInputsError(msg)
            temporary_path: Path | None = None
            try:
                with NamedTemporaryFile(dir=self.pools_file.parent, prefix=f".{self.pools_file.name}.", delete=False) as temporary:
                    temporary_path = Path(temporary.name)
                    temporary.write(content.encode())
                    temporary.flush()
                    os.fsync(temporary.fileno())
                temporary_path.replace(self.pools_file)
            finally:
                if temporary_path is not None:
                    temporary_path.unlink(missing_ok=True)
            self._snapshot = content.encode()
            self._needs_migration = False
        except OSError as error:
            msg = f"Could not write {self.context}: {error}"
            raise type(error)(msg) from error
        finally:
            lock_path.unlink()
