# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from dataclasses import dataclass
from ipaddress import IPv4Address, IPv4Interface, IPv4Network
from typing import TYPE_CHECKING

from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._utils.default import default
from pyavd.api.pool_manager.ipv4_allocations import Ipv4Allocation
from pyavd.j2filters import natural_sort

if TYPE_CHECKING:
    from collections.abc import Iterable

    from pyavd._eos_designs.schema import EosDesigns
    from pyavd._eos_designs.shared_utils import SharedUtilsProtocol
    from pyavd.api.pool_manager.ipv4_allocations import Ipv4AllocationCollection


@dataclass(frozen=True)
class Ipv4Subnet:
    """Resolved address space, independent of how a future parent pool supplies the subnet."""

    name: str
    network: IPv4Network
    first: int
    last: int
    descending: bool

    @classmethod
    def from_definition(cls, definition: EosDesigns.Ipv4SubnetsItem) -> Ipv4Subnet:
        try:
            network = IPv4Network(definition.subnet)
            if str(network) != definition.subnet:
                message = "Use canonical IPv4 CIDR notation."
                raise ValueError(message)  # noqa: TRY301
            first = int(network.network_address) + (network.prefixlen < 31)
            last = int(network.broadcast_address) - (network.prefixlen < 31)
            if definition.range is not None:
                start, end = definition.range.split("-")
                range_first, range_last = int(IPv4Address(start)), int(IPv4Address(end))
                if not first <= range_first <= range_last <= last:
                    message = "The inclusive range must contain usable hosts inside the subnet."
                    raise ValueError(message)  # noqa: TRY301
                first, last = range_first, range_last
        except ValueError as error:
            msg = f"Invalid ipv4_subnets entry '{definition.name}': {error}"
            raise AristaAvdInvalidInputsError(msg) from error
        return cls(definition.name, network, first, last, definition.allocation_policy.algorithm == "descend")

    def device_address(self, device_id: int | None) -> IPv4Address:
        if device_id is None or device_id < 1:
            msg = f"A positive device 'id' is required for management allocation from IPv4 subnet '{self.name}' using 'device_id'."
            raise AristaAvdInvalidInputsError(msg)
        address = self.last - device_id + 1 if self.descending else self.first + device_id - 1
        if not self.first <= address <= self.last:
            msg = f"Device ID {device_id} exceeds the available host range in IPv4 subnet '{self.name}'."
            raise AristaAvdInvalidInputsError(msg)
        return IPv4Address(address)


class Ipv4SubnetRegistry:
    """Build-scoped, VRF-aware endpoint claims shared by deterministic and automatic allocation."""

    def __init__(self) -> None:
        self.definitions: dict[tuple[str, str], Ipv4Subnet] = {}
        self.claims: dict[tuple[str, str, IPv4Address], tuple[str, str]] = {}
        self.gateways: set[tuple[str, str, IPv4Address]] = set()
        self.next_candidates: dict[tuple[str, str, str], int] = {}

    def claim(self, fabric: str, vrf: str, address: IPv4Address, owner: str, subnet: str) -> None:
        key = (fabric, vrf, address)
        if key in self.gateways:
            msg = f"IPv4 address '{address}' for '{owner}' in subnet '{subnet}' conflicts with a management gateway in fabric '{fabric}', VRF '{vrf}'."
            raise AristaAvdInvalidInputsError(msg)
        previous = self.claims.get(key)
        if previous is not None and previous[0] != owner:
            msg = (
                f"IPv4 address '{address}' conflicts between '{previous[0]}' (subnet '{previous[1]}') and '{owner}' "
                f"(subnet '{subnet}') in fabric '{fabric}', VRF '{vrf}'."
            )
            raise AristaAvdInvalidInputsError(msg)
        self.claims[key] = (owner, subnet)

    def subnet(self, shared_utils: SharedUtilsProtocol) -> Ipv4Subnet:
        name = shared_utils.inputs.mgmt_interface_settings.ipv4_subnet
        # The allocator only resolves a subnet after filtering out unselected devices.
        assert name is not None  # noqa: S101
        definition = shared_utils.inputs.ipv4_subnets.get(name, None)
        if definition is None:
            msg = f"Management IPv4 subnet '{name}' for host '{shared_utils.hostname}' was not found in 'ipv4_subnets'."
            raise AristaAvdInvalidInputsError(msg)
        subnet = Ipv4Subnet.from_definition(definition)
        key = (shared_utils.fabric_name, subnet.name)
        previous = self.definitions.setdefault(key, subnet)
        if previous != subnet:
            msg = f"Conflicting definitions of IPv4 subnet '{name}' in fabric '{shared_utils.fabric_name}'."
            raise AristaAvdInvalidInputsError(msg)
        return subnet

    def next_address(self, fabric: str, vrf: str, subnet: Ipv4Subnet) -> IPv4Address:
        cursor_key = (fabric, vrf, subnet.name)
        first = self.next_candidates.get(cursor_key, subnet.last if subnet.descending else subnet.first)
        step = -1 if subnet.descending else 1
        candidates = range(first, subnet.first - 1, -1) if subnet.descending else range(first, subnet.last + 1)
        for candidate in candidates:
            address = IPv4Address(candidate)
            key = (fabric, vrf, address)
            if key not in self.claims and key not in self.gateways:
                self.next_candidates[cursor_key] = candidate + step
                return address
        msg = f"No available IPv4 addresses in subnet '{subnet.name}' for fabric '{fabric}', VRF '{vrf}'."
        raise AristaAvdInvalidInputsError(msg)


def allocate_management_ips(devices: Iterable[SharedUtilsProtocol]) -> dict[str, tuple[Ipv4AllocationCollection, dict[str, Ipv4Allocation]]]:
    """Resolve management addresses before facts rendering; stage persistence only after a successful facts build."""
    devices = list(devices)
    enabled_fabrics = {device.fabric_name for device in devices if device.inputs.mgmt_interface_settings.ipv4_subnet is not None}
    if not enabled_fabrics:
        return {}
    devices = [device for device in devices if device.fabric_name in enabled_fabrics]
    registry = Ipv4SubnetRegistry()
    requests: list[tuple[SharedUtilsProtocol, Ipv4Subnet]] = []
    collections: dict[str, tuple[Ipv4AllocationCollection, dict[str, Ipv4Allocation]]] = {}

    # Gateways and explicit IPs are collected before any generated requests, independent of input order.
    for device in devices:
        fabric, vrf = device.fabric_name, device.mgmt_interface_vrf
        gateway = default(device.node_config.mgmt_gateway, device.inputs.mgmt_gateway)
        if gateway is not None:
            try:
                registry.gateways.add((fabric, vrf, IPv4Address(gateway)))
            except ValueError as error:
                msg = f"Invalid management IPv4 gateway '{gateway}' for host '{device.hostname}': {error}"
                raise AristaAvdInvalidInputsError(msg) from error
    for device in devices:
        # Also validate explicit overrides against retained state when a manager is available.
        if device.pool_manager is not None and device.fabric_name not in collections:
            collection = device.pool_manager.get_ipv4_allocation_collection(device.fabric_name)
            collections[device.fabric_name] = (collection, collection.assignments.copy())
        if device.node_config.mgmt_ip is not None:
            if device.node_config.mgmt_ip != "dhcp":
                try:
                    address = IPv4Interface(device.node_config.mgmt_ip).ip
                except ValueError as error:
                    msg = f"Invalid explicit management IPv4 address '{device.node_config.mgmt_ip}' for host '{device.hostname}': {error}"
                    raise AristaAvdInvalidInputsError(msg) from error
                registry.claim(device.fabric_name, device.mgmt_interface_vrf, address, device.hostname, "explicit mgmt_ip")
            continue
        if device.inputs.mgmt_interface_settings.ipv4_subnet is None:
            continue
        subnet = registry.subnet(device)
        requests.append((device, subnet))

    # Reserve exact deterministic claims before allocating any automatic endpoint.
    for device, subnet in requests:
        if device.inputs.fabric_ip_addressing.management.ipv4_subnet.algorithm != "device_id":
            continue
        address = subnet.device_address(device.id)
        registry.claim(device.fabric_name, device.mgmt_interface_vrf, address, device.hostname, subnet.name)
        device._allocated_mgmt_ip = f"{address}/{subnet.network.prefixlen}"

    # All persisted addresses, including absent owners, remain reservations. A matching owner is not a conflict.
    for fabric, (_, assignments) in collections.items():
        for allocation in assignments.values():
            registry.claim(fabric, allocation.vrf, IPv4Interface(allocation.address).ip, allocation.owner, allocation.subnet)

    requested_devices = {device.hostname: (device, subnet) for device, subnet in requests}
    for hostname in natural_sort(sorted(requested_devices), ignore_case=False):
        device, subnet = requested_devices[hostname]
        if device.inputs.fabric_ip_addressing.management.ipv4_subnet.algorithm != "auto":
            continue
        if device.pool_manager is None:
            msg = f"Management IPv4 allocation mode 'auto' requires a PoolManager for host '{device.hostname}'."
            raise AristaAvdInvalidInputsError(msg)
        _, assignments = collections[device.fabric_name]
        allocation = assignments.get(device.hostname)
        if allocation is not None:
            interface = IPv4Interface(allocation.address)
            if (
                allocation.subnet != subnet.name
                or allocation.vrf != device.mgmt_interface_vrf
                or interface.network != subnet.network
                or not subnet.first <= int(interface.ip) <= subnet.last
            ):
                msg = (
                    f"Persisted management IPv4 assignment '{allocation.address}' for '{device.hostname}' is invalid for subnet '{subnet.name}' "
                    f"and VRF '{device.mgmt_interface_vrf}'. Restore the definition or explicitly release the reservation before reallocating."
                )
                raise AristaAvdInvalidInputsError(msg)
        else:
            address = registry.next_address(device.fabric_name, device.mgmt_interface_vrf, subnet)
            allocation = Ipv4Allocation(device.hostname, subnet.name, device.mgmt_interface_vrf, f"{address}/{subnet.network.prefixlen}")
            assignments[device.hostname] = allocation
            registry.claim(device.fabric_name, allocation.vrf, address, allocation.owner, allocation.subnet)
        device._allocated_mgmt_ip = allocation.address
    return collections
