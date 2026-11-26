# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from dataclasses import dataclass
from ipaddress import IPv4Address, IPv4Interface, IPv4Network
from typing import TYPE_CHECKING

from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._utils.default import default
from pyavd.api.pool_manager.ipv4_pools import Ipv4PoolDefinition, Ipv4Reservations, node_owner
from pyavd.j2filters import natural_sort

if TYPE_CHECKING:
    from collections.abc import Iterable

    from pyavd._eos_designs.schema import EosDesigns
    from pyavd._eos_designs.shared_utils import SharedUtilsProtocol
    from pyavd.api.pool_manager.ipv4_pools import Ipv4PoolCollection


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
    """Resolve eos_designs subnet definitions and submit fixed claims to the shared IP pools."""

    def __init__(self, reservations: dict[str, Ipv4Reservations]) -> None:
        self.definitions: dict[tuple[str, str], Ipv4Subnet] = {}
        self.reservations = reservations

    def claim(self, fabric: str, vrf: str, address: IPv4Address, owner: str, subnet: str) -> None:
        self.reservations[fabric].reserve(vrf, int(address), int(address), node_owner(owner, "oob_mgmt"), subnet)

    def subnet(self, shared_utils: SharedUtilsProtocol) -> Ipv4Subnet:
        name = shared_utils.node_config.mgmt_ipv4_subnet
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


def allocate_management_ips(devices: Iterable[SharedUtilsProtocol]) -> dict[str, tuple[Ipv4PoolCollection, Ipv4PoolCollection]]:
    """Resolve management addresses before facts rendering; stage persistence only after a successful facts build."""
    devices = list(devices)
    enabled_fabrics = {device.fabric_name for device in devices if device.node_config.mgmt_ipv4_subnet is not None}
    if not enabled_fabrics:
        return {}
    devices = [device for device in devices if device.fabric_name in enabled_fabrics]
    requests: list[tuple[SharedUtilsProtocol, Ipv4Subnet]] = []
    collections: dict[str, tuple[Ipv4PoolCollection, Ipv4PoolCollection]] = {}
    reservations = {fabric: Ipv4Reservations(f"fabric '{fabric}'") for fabric in enabled_fabrics}

    # Load and validate every retained reservation before processing this run's claims.
    for device in devices:
        if device.pool_manager is not None and device.fabric_name not in collections:
            collection = device.pool_manager.get_ipv4_allocation_collection(device.fabric_name)
            staged = collection.stage()
            collections[device.fabric_name] = (collection, staged)
            reservations[device.fabric_name] = staged.reservations
            staged.reservations.context = f"fabric '{device.fabric_name}', {staged.context}"
    registry = Ipv4SubnetRegistry(reservations)

    # Gateways and explicit IPs are collected before any generated requests, independent of input order.
    for device in devices:
        fabric, vrf = device.fabric_name, device.mgmt_interface_vrf
        gateway = device.oob_mgmt_gateway
        if gateway is not None:
            try:
                address = int(IPv4Address(gateway))
            except ValueError as error:
                msg = f"Invalid management IPv4 gateway '{gateway}' for host '{device.hostname}': {error}"
                raise AristaAvdInvalidInputsError(msg) from error
            reservations[fabric].reserve(vrf, address, address, f"management gateway {gateway}", "management gateway")
    for device in devices:
        mgmt_ip = device.node_config.mgmt_ip
        if device.is_act_digital_twin and (mgmt_ip is not None or device.node_config.mgmt_ipv4_subnet is not None):
            mgmt_ip = default(device.node_config.digital_twin.mgmt_ip, mgmt_ip)
        if mgmt_ip is not None:
            if mgmt_ip != "dhcp":
                try:
                    address = IPv4Interface(mgmt_ip).ip
                except ValueError as error:
                    msg = f"Invalid explicit management IPv4 address '{mgmt_ip}' for host '{device.hostname}': {error}"
                    raise AristaAvdInvalidInputsError(msg) from error
                registry.claim(device.fabric_name, device.mgmt_interface_vrf, address, device.hostname, "explicit mgmt_ip")
            continue
        if device.node_config.mgmt_ipv4_subnet is None:
            continue
        subnet = registry.subnet(device)
        requests.append((device, subnet))

    # Reserve exact deterministic claims before allocating any automatic endpoint.
    for device, subnet in requests:
        if device.inputs.fabric_ip_addressing.oob_mgmt.ipv4_subnet.algorithm != "device_id":
            continue
        address = subnet.device_address(device.id)
        registry.claim(device.fabric_name, device.mgmt_interface_vrf, address, device.hostname, subnet.name)
        device._allocated_mgmt_ip = f"{address}/{subnet.network.prefixlen}"

    requested_devices = {device.hostname: (device, subnet) for device, subnet in requests}
    for hostname in natural_sort(sorted(requested_devices), ignore_case=False):
        device, subnet = requested_devices[hostname]
        if device.inputs.fabric_ip_addressing.oob_mgmt.ipv4_subnet.algorithm != "auto":
            continue
        if device.pool_manager is None:
            msg = f"Management IPv4 allocation mode 'auto' requires a PoolManager for host '{device.hostname}'."
            raise AristaAvdInvalidInputsError(msg)
        _, staged = collections[device.fabric_name]
        definition = Ipv4PoolDefinition(
            subnet=subnet.name,
            vrf=device.mgmt_interface_vrf,
            network=subnet.network,
            first=subnet.first,
            last=subnet.last,
            descending=subnet.descending,
        )
        pool = staged.get_ipv4_pool(definition)
        device._allocated_mgmt_ip = pool.get_assignment(node_owner(device.hostname, "oob_mgmt")).value
    return collections
