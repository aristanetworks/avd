# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import json
from contextlib import contextmanager
from copy import deepcopy
from dataclasses import replace
from ipaddress import IPv4Network
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import TYPE_CHECKING, Any
from unittest.mock import patch

from yaml import safe_dump, safe_load

from pyavd import get_avd_facts, get_device_structured_config, validate_inputs
from pyavd._eos_designs.eos_designs_facts.schema import EosDesignsFacts
from pyavd._errors import AristaAvdError
from pyavd.api.pool_manager import PoolManager
from pyavd.api.pool_manager.ipv4_allocations import Ipv4AllocationCollection
from pyavd.api.pool_manager.ipv4_pools import Ipv4PoolCollection, Ipv4PoolDefinition, link_owner, node_owner

if TYPE_CHECKING:
    from collections.abc import Iterator


def inputs(nodes: dict[str, dict], algorithm: str = "auto", **settings: Any) -> dict[str, dict]:
    base = {
        "fabric_name": "MGMT_TEST",
        "type": "l2leaf",
        "mgmt_interface_settings": {"vrf": "MGMT"},
        "ipv4_subnets": [{"name": "OOB", "subnet": "192.0.2.0/24", "range": "192.0.2.10-192.0.2.20"}],
        "fabric_ip_addressing": {"oob_mgmt": {"ipv4_subnet": {"algorithm": algorithm}}},
        "devices": [{"name": name, "type": "l2leaf", "mgmt_ipv4_subnet": "OOB", **node} for name, node in nodes.items()],
        **settings,
    }
    return {name: deepcopy(base) for name in nodes}


def addresses(facts: dict[str, EosDesignsFacts]) -> dict[str, str | None]:
    return {name: fact.mgmt_ip for name, fact in facts.items()}


@contextmanager
def fails(fragment: str) -> Iterator[None]:
    try:
        yield
    except AristaAvdError as error:
        assert fragment in str(error), str(error)  # noqa: PT017
    else:
        message = f"Expected an allocation error containing {fragment!r}"
        raise AssertionError(message)


def persistent_builds(directory: Path) -> None:
    """Assignments survive process-local manager replacement, ID changes, and additions."""
    tied_names = inputs({"leaf1": {}, "leaf01": {}})
    assert addresses(get_avd_facts(tied_names, pool_manager=PoolManager(directory / "ties1"))) == addresses(
        get_avd_facts(dict(reversed(list(tied_names.items()))), pool_manager=PoolManager(directory / "ties2")),
    )
    initial = inputs({"leaf2": {}, "leaf3": {}, "static": {"mgmt_ip": "192.0.2.10/24"}})
    manager = PoolManager(directory)
    first = get_avd_facts(initial, pool_manager=manager)
    assert addresses(first) == {"leaf2": "192.0.2.11/24", "leaf3": "192.0.2.12/24", "static": "192.0.2.10/24"}
    assert manager.save_updated_pools()
    path = directory / "data/MGMT_TEST-ipv4-allocations.yml"
    before = path.read_bytes()
    before_mtime = path.stat().st_mtime_ns
    reloaded = PoolManager(directory)
    second = get_avd_facts(dict(reversed(list(initial.items()))), pool_manager=reloaded)
    assert addresses(second) == addresses(first)
    assert not reloaded.save_updated_pools()
    assert path.read_bytes() == before
    assert path.stat().st_mtime_ns == before_mtime

    expanded = inputs({"leaf1": {}, "leaf2": {"id": 42}, "leaf3": {}, "static": {"mgmt_ip": "192.0.2.10/24"}})
    manager = PoolManager(directory)
    third = get_avd_facts(expanded, pool_manager=manager)
    assert addresses(third) == {"leaf1": "192.0.2.13/24", "leaf2": "192.0.2.11/24", "leaf3": "192.0.2.12/24", "static": "192.0.2.10/24"}
    manager.save_updated_pools()

    # Partial builds and static/DHCP transitions do not release reservations belonging to absent owners.
    manager = PoolManager(directory)
    partial = get_avd_facts(inputs({"leaf4": {}, "leaf2": {"mgmt_ip": "dhcp"}}), pool_manager=manager)
    assert addresses(partial) == {"leaf4": "192.0.2.10/24", "leaf2": "dhcp"}
    manager.save_updated_pools()
    assert set(manager.get_ipv4_allocation_collection("MGMT_TEST").assignments) == {"leaf1", "leaf2", "leaf3", "leaf4"}

    # A static claim may match its own reservation, but may not displace another owner.
    own_override = inputs({"leaf2": {"mgmt_ip": "192.0.2.11/24"}, "leaf3": {}})
    get_avd_facts(own_override, pool_manager=PoolManager(directory))
    with fails("conflicts between"):
        get_avd_facts(inputs({"intruder": {"mgmt_ip": "192.0.2.11/24"}, "leaf3": {}}), pool_manager=PoolManager(directory))

    invalid_range = inputs({"leaf2": {}}, ipv4_subnets=[{"name": "OOB", "subnet": "192.0.2.0/24", "range": "192.0.2.15-192.0.2.20"}])
    with fails("Persisted management IPv4 assignment"):
        get_avd_facts(invalid_range, pool_manager=PoolManager(directory))


def overrides_and_collisions(directory: Path) -> None:
    for algorithm in ("auto", "device_id"):
        # Overrides require neither an addressing ID nor an IP state manager.
        facts = get_avd_facts(inputs({"static": {"mgmt_ip": "198.51.100.50/24"}, "dhcp": {"mgmt_ip": "dhcp"}}, algorithm))
        assert addresses(facts) == {"static": "198.51.100.50/24", "dhcp": "dhcp"}
        # Existing legacy inheritance is also honored.
        legacy = inputs({"legacy": {}}, algorithm)["legacy"]
        del legacy["devices"]
        legacy["l2leaf"] = {"defaults": {"mgmt_ip": "192.0.2.50/24"}, "nodes": [{"name": "legacy"}]}
        assert get_avd_facts({"legacy": legacy})["legacy"].mgmt_ip == "192.0.2.50/24"
        profiled = inputs({"profiled": {"profile": "STATIC"}}, algorithm, device_profiles=[{"name": "STATIC", "mgmt_ip": "192.0.2.50/24"}])
        assert get_avd_facts(profiled)["profiled"].mgmt_ip == "192.0.2.50/24"
        manager = PoolManager(directory / algorithm)
        get_avd_facts(inputs({"static": {"mgmt_ip": "192.0.2.50/24"}}, algorithm), pool_manager=manager)
        assert not manager.save_updated_pools()
        assert not (directory / algorithm / "data/MGMT_TEST-ipv4-allocations.yml").exists()

    with fails("requires a PoolManager"):
        get_avd_facts(inputs({"leaf": {}}))
    with fails("positive device 'id'"):
        get_avd_facts(inputs({"leaf": {}}, "device_id"))
    with fails("exceeds the available host range"):
        get_avd_facts(inputs({"leaf": {"id": 12}}, "device_id"))

    collision = inputs({"leaf1": {"id": 1}, "leaf2": {"id": 1}}, "device_id")
    with fails("conflicts between"):
        get_avd_facts(collision)
    # Address-space context, rather than ID or subnet name, defines collisions.
    collision["leaf2"]["mgmt_interface_settings"]["vrf"] = "OTHER"
    assert set(addresses(get_avd_facts(collision)).values()) == {"192.0.2.10/24"}
    collision["leaf2"]["mgmt_interface_settings"]["vrf"] = "MGMT"
    collision["leaf2"]["devices"][1]["mgmt_ipv4_subnet"] = "ALIAS"
    collision["leaf2"]["ipv4_subnets"][0]["name"] = "ALIAS"
    with fails("conflicts between"):
        get_avd_facts(collision)

    static = inputs({"generated": {"id": 1}, "static": {"mgmt_ip": "192.0.2.10/24"}}, "device_id")
    for ordered in (static, dict(reversed(list(static.items())))):
        with fails("conflicts between"):
            get_avd_facts(ordered)
    gateway = inputs({"leaf": {"id": 1}}, "device_id", mgmt_gateway="192.0.2.10")
    with fails("management gateway"):
        get_avd_facts(gateway)
    gateway["leaf"]["fabric_ip_addressing"]["oob_mgmt"]["ipv4_subnet"]["algorithm"] = "auto"
    assert get_avd_facts(gateway, pool_manager=PoolManager(directory))["leaf"].mgmt_ip == "192.0.2.11/24"


def node_subnet_inheritance(directory: Path) -> None:
    """Node selectors inherit through both input models and retain explicit-address precedence."""
    subnets = [
        {"name": "OOB", "subnet": "192.0.2.0/24", "range": "192.0.2.10-192.0.2.20"},
        {"name": "GROUP", "subnet": "198.51.100.0/24", "range": "198.51.100.10-198.51.100.20"},
        {"name": "NODE", "subnet": "203.0.113.0/24", "range": "203.0.113.10-203.0.113.20"},
    ]
    expected = {"inherited": "192.0.2.10/24", "grouped": "198.51.100.10/24", "overridden": "203.0.113.10/24"}
    for algorithm in ("device_id", "auto"):
        for model in ("legacy", "profiles"):
            base = inputs({"inherited": {}}, algorithm, ipv4_subnets=subnets)["inherited"]
            if model == "legacy":
                del base["devices"]
                base["l2leaf"] = {
                    "defaults": {"mgmt_ipv4_subnet": "OOB"},
                    "nodes": [{"name": "inherited", "id": 1}],
                    "node_groups": [
                        {
                            "group": "GROUP",
                            "mlag": False,
                            "mgmt_ipv4_subnet": "GROUP",
                            "nodes": [
                                {"name": "grouped", "id": 1},
                                {"name": "overridden", "id": 1, "mgmt_ipv4_subnet": "NODE"},
                            ],
                        }
                    ],
                }
            else:
                base["device_profiles"] = [
                    {"name": "PARENT", "mgmt_ipv4_subnet": "OOB"},
                    {"name": "CHILD", "parent_profile": "PARENT"},
                    {"name": "GROUP", "parent_profile": "PARENT", "mgmt_ipv4_subnet": "GROUP"},
                ]
                base["devices"] = [
                    {"name": "inherited", "type": "l2leaf", "profile": "CHILD", "id": 1},
                    {"name": "grouped", "type": "l2leaf", "profile": "GROUP", "id": 1},
                    {"name": "overridden", "type": "l2leaf", "profile": "GROUP", "id": 1, "mgmt_ipv4_subnet": "NODE"},
                ]
            data = {hostname: deepcopy(base) for hostname in expected}
            for host_inputs in data.values():
                assert validate_inputs(host_inputs).validated_data is not None
            manager = PoolManager(directory / algorithm / model)
            facts = get_avd_facts(data, pool_manager=manager)
            assert addresses(facts) == expected
            for hostname, address in expected.items():
                config = get_device_structured_config(hostname, data[hostname], facts)._dump()
                assert config["management_interfaces"][0]["ip_address"] == address

        # Explicit addresses bypass even an unknown subnet reference; unselected nodes need no manager or ID.
        explicit = inputs(
            {
                "static": {"mgmt_ipv4_subnet": "MISSING", "mgmt_ip": "192.0.2.50/24"},
                "dhcp": {"mgmt_ipv4_subnet": "MISSING", "mgmt_ip": "dhcp"},
            },
            algorithm,
        )
        assert addresses(get_avd_facts(explicit)) == {"static": "192.0.2.50/24", "dhcp": "dhcp"}
        unselected = inputs({"unselected": {}}, algorithm)
        del unselected["unselected"]["devices"][0]["mgmt_ipv4_subnet"]
        assert get_avd_facts(unselected)["unselected"].mgmt_ip is None


def subnet_boundaries(directory: Path) -> None:
    for cidr, expected in (("192.0.2.0/30", "192.0.2.1/30"), ("192.0.2.0/31", "192.0.2.0/31"), ("192.0.2.1/32", "192.0.2.1/32"), ("0.0.0.0/0", "0.0.0.1/0")):
        data = inputs({"leaf": {"id": 1}}, "device_id", ipv4_subnets=[{"name": "OOB", "subnet": cidr}])
        assert get_avd_facts(data)["leaf"].mgmt_ip == expected
    descending = inputs(
        {"leaf": {"id": 2}},
        "device_id",
        ipv4_subnets=[
            {
                "name": "OOB",
                "subnet": "192.0.2.0/24",
                "range": "192.0.2.10-192.0.2.20",
                "allocation_policy": {"algorithm": "descend"},
            }
        ],
    )
    assert get_avd_facts(descending)["leaf"].mgmt_ip == "192.0.2.19/24"
    automatic_descending = inputs(
        {"leaf1": {}, "leaf2": {}},
        ipv4_subnets=descending["leaf"]["ipv4_subnets"],
    )
    manager = PoolManager(directory / "descending")
    expected = {"leaf1": "192.0.2.20/24", "leaf2": "192.0.2.19/24"}
    assert addresses(get_avd_facts(automatic_descending, pool_manager=manager)) == expected
    manager.save_updated_pools()
    for host_inputs in automatic_descending.values():
        host_inputs["ipv4_subnets"][0]["allocation_policy"]["algorithm"] = "ascend"
    assert addresses(get_avd_facts(automatic_descending, pool_manager=PoolManager(directory / "descending"))) == expected
    for definition in (
        {"subnet": "2001:db8::/64"},
        {"subnet": "192.0.2.1/24"},
        {"subnet": "192.0.2.0/24 trailing"},
        {"subnet": "192.0.2.0/24", "range": "192.0.2.20-192.0.2.10"},
        {"subnet": "192.0.2.0/24", "range": "192.0.2.0-192.0.2.10"},
    ):
        with fails("Invalid ipv4_subnets entry"):
            get_avd_facts(inputs({"leaf": {"id": 1}}, "device_id", ipv4_subnets=[{"name": "OOB", **definition}]))
    with fails("was not found"):
        get_avd_facts(inputs({"leaf": {"id": 1}}, "device_id", ipv4_subnets=[]))
    with fails("No available IPv4 addresses"):
        get_avd_facts(inputs({"leaf1": {}, "leaf2": {}}, ipv4_subnets=[{"name": "OOB", "subnet": "192.0.2.1/32"}]), pool_manager=PoolManager(directory))


def facts_to_configuration(directory: Path) -> None:
    data = inputs(
        {"leaf": {}},
        ntp_settings={
            "server_vrf": "use_mgmt_interface_vrf",
            "servers": [
                {
                    "name": "203.0.113.123",
                    "source_address": "use_mgmt_interface_ipv4",
                }
            ],
        },
    )
    facts = get_avd_facts(data, pool_manager=PoolManager(directory))
    serialized = json.dumps({name: fact._dump() for name, fact in facts.items()})
    restored = {name: EosDesignsFacts._from_dict(fact) for name, fact in json.loads(serialized).items()}
    config = get_device_structured_config("leaf", data["leaf"], restored)._dump()
    assert config["management_interfaces"][0]["ip_address"] == "192.0.2.10/24"
    assert config["ntp"]["servers"][0]["source_address"] == "192.0.2.10"

    for algorithm in ("auto", "device_id"):
        # An explicit twin address needs neither an allocator nor a device ID.
        twin = inputs(
            {"leaf": {"digital_twin": {"mgmt_ip": "198.51.100.10/24", "mgmt_gateway": "198.51.100.1"}}},
            algorithm,
            digital_twin={"environment": "act"},
            ntp_settings=data["leaf"]["ntp_settings"],
        )
        twin_facts = get_avd_facts(twin, digital_twin=True)
        assert twin_facts["leaf"].mgmt_ip == "198.51.100.10/24"
        serialized = json.dumps({name: fact._dump() for name, fact in twin_facts.items()})
        restored = {name: EosDesignsFacts._from_dict(fact) for name, fact in json.loads(serialized).items()}
        twin_config = get_device_structured_config("leaf", twin["leaf"], restored, digital_twin=True)._dump()
        assert twin_config["management_interfaces"][0]["ip_address"] == "198.51.100.10/24"
        assert twin_config["ntp"]["servers"][0]["source_address"] == "198.51.100.10"
        assert twin_config["static_routes"][0]["next_hop"] == "198.51.100.1"
        assert twin_config["metadata"]["digital_twin"]["ip_addr"] == "198.51.100.10/24"


def digital_twin_allocations(directory: Path) -> None:
    """The caller's output directories isolate production and twin state, including retained reservations."""
    production_dir = directory / "intended"
    twin_dir = directory / "digital_twin/intended"
    production = inputs({"leaf": {}, "spare": {}})
    manager = PoolManager(production_dir)
    production_addresses = addresses(get_avd_facts(production, pool_manager=manager))
    assert manager.save_updated_pools()
    production_path = production_dir / "data/MGMT_TEST-ipv4-allocations.yml"
    production_state = production_path.read_bytes()
    production_mtime = production_path.stat().st_mtime_ns

    twin_settings = {
        "digital_twin": {"environment": "act"},
        "mgmt_gateway": "192.0.2.1",
        "ipv4_subnets": [{"name": "OOB", "subnet": "198.51.100.0/24", "range": "198.51.100.10-198.51.100.20"}],
    }
    twin = inputs(
        {
            "leaf": {"digital_twin": {"mgmt_ip": "198.51.100.10/24", "mgmt_gateway": "198.51.100.11"}},
            "auto1": {"digital_twin": {"mgmt_gateway": "198.51.100.11"}},
            "auto2": {"digital_twin": {"mgmt_gateway": "198.51.100.11"}},
        },
        **twin_settings,
    )
    manager = PoolManager(twin_dir)
    twin_facts = get_avd_facts(twin, pool_manager=manager, digital_twin=True)
    assert addresses(twin_facts) == {"leaf": "198.51.100.10/24", "auto1": "198.51.100.12/24", "auto2": "198.51.100.13/24"}
    assert manager.save_updated_pools()
    twin_path = twin_dir / "data/MGMT_TEST-ipv4-allocations.yml"
    twin_state = twin_path.read_bytes()
    twin_config = get_device_structured_config("auto1", twin["auto1"], twin_facts, digital_twin=True)._dump()
    assert twin_config["management_interfaces"][0]["ip_address"] == "198.51.100.12/24"
    assert twin_config["static_routes"][0]["next_hop"] == "198.51.100.11"
    assert twin_config["metadata"]["digital_twin"]["ip_addr"] == "198.51.100.12/24"

    # An overridden owner and an absent owner both retain their twin reservations.
    manager = PoolManager(twin_dir)
    overridden = inputs({"auto1": {"digital_twin": {"mgmt_ip": "198.51.100.50/24"}}}, **twin_settings)
    assert get_avd_facts(overridden, pool_manager=manager, digital_twin=True)["auto1"].mgmt_ip == "198.51.100.50/24"
    assert not manager.save_updated_pools()
    assert twin_path.read_bytes() == twin_state

    # Returning to production reuses its assignments without touching either state file.
    manager = PoolManager(production_dir)
    assert addresses(get_avd_facts(production, pool_manager=manager)) == production_addresses
    assert not manager.save_updated_pools()
    assert production_path.read_bytes() == production_state
    assert production_path.stat().st_mtime_ns == production_mtime
    assert twin_path.read_bytes() == twin_state


def state_safety(directory: Path) -> None:
    # Two managers that loaded the same revision must not overwrite each other.
    manager1, manager2 = PoolManager(directory), PoolManager(directory)
    get_avd_facts(inputs({"leaf1": {}}), pool_manager=manager1)
    get_avd_facts(inputs({"leaf2": {}}), pool_manager=manager2)
    manager1.save_updated_pools()
    path = directory / "data/MGMT_TEST-ipv4-allocations.yml"
    snapshot = path.read_bytes()
    with fails("changed during this build"):
        manager2.save_updated_pools()
    assert path.read_bytes() == snapshot

    # A busy or abandoned lock cannot be bypassed and cannot overwrite state.
    locked = PoolManager(directory)
    get_avd_facts(inputs({"leaf3": {}}), pool_manager=locked)
    lock_path = path.with_suffix(".yml.lock")
    lock_path.touch()
    with fails("locked by another writer"):
        locked.save_updated_pools()
    assert path.read_bytes() == snapshot
    lock_path.unlink()

    failed = PoolManager(directory)
    with fails("No available IPv4 addresses"):
        get_avd_facts(
            inputs(
                {"leaf3": {"mgmt_ipv4_subnet": "TINY"}, "leaf4": {"mgmt_ipv4_subnet": "TINY"}},
                ipv4_subnets=[
                    {
                        "name": "TINY",
                        "subnet": "198.51.100.1/32",
                    }
                ],
            ),
            pool_manager=failed,
        )
    assert not failed.save_updated_pools()
    assert path.read_bytes() == snapshot

    # A later facts-rendering failure also cannot publish assignments staged by this build.
    failed_facts = PoolManager(directory)
    with fails("inband_mgmt"):
        get_avd_facts(inputs({"leaf3": {"inband_mgmt_subnet": "10.1.0.0/24"}}), pool_manager=failed_facts)
    assert not failed_facts.save_updated_pools()
    assert path.read_bytes() == snapshot

    path.write_text("version: 99\nallocations: []\n")
    with fails("Invalid IPv4 allocation state"):
        Ipv4AllocationCollection(path)
    path.write_text("version: 1\nallocations: [broken]\n")
    with fails("Invalid IPv4 allocation state"):
        Ipv4AllocationCollection(path)


def schema_contract() -> None:
    for algorithm in ("device_id", "auto"):
        data = inputs({"leaf": {"id": 1}}, algorithm)["leaf"]
        assert validate_inputs(data).validated_data is not None
    invalid = inputs({"leaf": {"id": 1}}, "unknown")["leaf"]
    assert validate_inputs(invalid).validated_data is None
    invalid = inputs({"leaf": {"id": 1}})["leaf"]
    invalid["ipv4_subnets"][0]["allocation_policy"] = {"algorithm": "unknown"}
    assert validate_inputs(invalid).validated_data is None
    invalid = inputs({"leaf": {"id": 1}})["leaf"]
    invalid["ipv4_subnets"].append(deepcopy(invalid["ipv4_subnets"][0]))
    assert validate_inputs(invalid).validated_data is None


def pool_foundation(directory: Path) -> None:
    """Exercise host and shared-link resources through the existing manager and pool hierarchy."""
    manager = PoolManager(directory)
    path = directory / "data/FABRIC-ipv4-allocations.yml"
    collection = manager.get_pool_collection("ipv4_pools", path)
    assert manager.get_pool_collection("ipv4_pools", path) is collection
    definition = Ipv4PoolDefinition("HOSTS", "MGMT", IPv4Network("192.0.2.0/24"))
    for settings, fragment in (
        ({"first": int(definition.network.network_address)}, "Invalid allocation bounds"),
        ({"last": int(definition.network.broadcast_address)}, "Invalid allocation bounds"),
        ({"resource_type": "subnet", "prefix_length": 23}, "Requested prefix length"),
        ({"resource_type": "subnet", "prefix_length": True}, "Requested prefix length"),
        ({"prefix_length": 31}, "host pool"),
    ):
        try:
            replace(definition, **settings)
        except ValueError as error:
            if fragment not in str(error):
                raise AssertionError(str(error)) from error
        else:
            msg = f"Expected invalid IPv4 pool definition: {settings}"
            raise AssertionError(msg)
    hosts = collection.get_ipv4_pool(definition)
    oob = node_owner("leaf1", "oob_mgmt")
    inband = node_owner("leaf1", "inband_mgmt")
    assert hosts.get_assignment(oob).value == "192.0.2.1/24"

    links = collection.get_ipv4_pool(replace(definition, subnet="LINKS", resource_type="subnet", prefix_length=31))
    link = link_owner(("leaf1", "Ethernet1"), ("spine1", "Ethernet2"), "uplink")
    reverse = link_owner(("spine1", "Ethernet2"), ("leaf1", "Ethernet1"), "uplink")
    assert link == reverse
    assert links.get_assignment(link).value == "192.0.2.2/31"
    assert links.get_assignment(reverse).value == "192.0.2.2/31"
    with fails("conflicts between"):
        links.get_assignment("conflicting-link", "192.0.2.0/31")

    wider = collection.get_ipv4_pool(replace(definition, subnet="OTHER_LINKS", resource_type="subnet", prefix_length=30))
    assert wider.get_assignment("other-link").value == "192.0.2.4/30"
    assert hosts.get_assignment(inband).value == "192.0.2.8/24"
    with fails("conflicts between"):
        hosts.get_assignment("intruder", "192.0.2.3/24")
    with fails("outside pool"):
        hosts.get_assignment("out-of-range", "198.51.100.10/24")
    with fails("outside pool"):
        hosts.get_assignment("network-address", "192.0.2.0/24")
    with fails("nonempty strings"):
        hosts.get_assignment("")
    with fails("Invalid requested IPv4 allocation"):
        links.get_assignment("unaligned", "192.0.2.3/31")
    with fails("Persisted IPv4 assignment"):
        hosts.get_assignment(oob, "192.0.2.9/24")
    assert hosts.get_assignment("next-host").value == "192.0.2.9/24"
    other_vrf = collection.get_ipv4_pool(replace(definition, vrf="OTHER"))
    assert other_vrf.get_assignment(node_owner("leaf1", "other_vrf")).value == "192.0.2.1/24"
    assert manager.save_updated_pools()
    before = path.read_bytes()
    reloaded = PoolManager(directory)
    retained = reloaded.get_pool_collection("ipv4_pools", path)
    assert retained.get_ipv4_pool(definition).get_assignment(oob).value == "192.0.2.1/24"
    assert retained.get_ipv4_pool(replace(definition, subnet="LINKS", resource_type="subnet", prefix_length=31)).get_assignment(reverse).value == "192.0.2.2/31"
    assert not reloaded.save_updated_pools()
    assert path.read_bytes() == before

    # Staging also isolates accessed flags, dirty flags and transient reservations.
    staged = retained.stage()
    staged.get_ipv4_pool(definition).get_assignment("staged-only")
    assert not reloaded.save_updated_pools()
    assert path.read_bytes() == before
    retained.publish(staged)
    assert reloaded.save_updated_pools()

    # A very large occupied subnet must be skipped as an interval, not address by address.
    large = Ipv4PoolCollection(directory / "large.yml")
    parent = Ipv4PoolDefinition("LARGE", "default", IPv4Network("0.0.0.0/0"), "subnet", 1)
    assert large.get_ipv4_pool(parent).get_assignment("half").value == "0.0.0.0/1"
    assert large.get_ipv4_pool(replace(parent, resource_type="host", prefix_length=None)).get_assignment("host").value == "128.0.0.0/0"

    descending = Ipv4PoolCollection(directory / "descending.yml")
    parent = Ipv4PoolDefinition("LINKS", "default", IPv4Network("192.0.2.0/29"), "subnet", 31, descending=True)
    pool = descending.get_ipv4_pool(parent)
    assert [pool.get_assignment(str(index)).value for index in range(4)] == ["192.0.2.6/31", "192.0.2.4/31", "192.0.2.2/31", "192.0.2.0/31"]
    with fails("No available IPv4 subnets"):
        pool.get_assignment("exhausted")
    tiny = descending.get_ipv4_pool(Ipv4PoolDefinition("TINY", "OTHER", IPv4Network("192.0.2.1/32"), "subnet", 32))
    assert tiny.get_assignment("tiny").value == "192.0.2.1/32"
    with fails("No available IPv4 subnets"):
        tiny.get_assignment("exhausted")

    # Bounds can cut through aligned prefixes; only fully contained child subnets are usable.
    bounded = descending.get_ipv4_pool(
        replace(
            parent,
            subnet="BOUNDED",
            vrf="BOUNDED",
            first=int(parent.network.network_address) + 1,
            last=int(parent.network.broadcast_address) - 1,
            descending=False,
        )
    )
    assert bounded.get_assignment("link1").value == "192.0.2.2/31"
    assert bounded.get_assignment("link2").value == "192.0.2.4/31"
    with fails("No available IPv4 subnets"):
        bounded.get_assignment("exhausted")

    # Adding hosts must not repeatedly rescan all earlier reservations.
    sequential = Ipv4PoolCollection(directory / "sequential.yml")
    hosts = sequential.get_ipv4_pool(Ipv4PoolDefinition("HOSTS", "default", IPv4Network("10.0.0.0/16")))
    with patch.object(sequential.reservations, "conflict", wraps=sequential.reservations.conflict) as conflicts:
        for index in range(512):
            hosts.get_assignment(str(index))
        assert conflicts.call_count <= 3 * 512


def pool_state_validation(directory: Path) -> None:
    """A clean textual merge must not hide conflicting or malformed reservations."""
    definition = Ipv4PoolDefinition("HOSTS", "MGMT", IPv4Network("192.0.2.0/24"))
    branches = []
    for name in ("leaf1", "leaf2"):
        collection = Ipv4PoolCollection(directory / f"{name}.yml")
        collection.get_ipv4_pool(definition).get_assignment(node_owner(name, "oob_mgmt"))
        assert collection.save_updates()
        branches.append(safe_load(collection.pools_file.read_text()))
    merged = branches[0]
    merged["ipv4_pools"][definition.key].update(branches[1]["ipv4_pools"][definition.key])
    path = directory / "merged.yml"
    path.write_text(safe_dump(merged))
    with fails("leaf1"):
        Ipv4PoolCollection(path)
    with fails("leaf2"):
        Ipv4PoolCollection(path)
    with fails(str(path)):
        Ipv4PoolCollection(path)
    with fails("VRF 'MGMT'"):
        Ipv4PoolCollection(path)

    owner = node_owner("leaf1", "oob_mgmt")
    valid = {"version": 2, "ipv4_pools": {definition.key: {owner: "192.0.2.1/24"}}}
    for contents, message in (
        ("version: 2\nversion: 2\nipv4_pools: {}\n", "Duplicate YAML key"),
        ("version: 2\nipv4_pools: [\n", "Invalid IPv4 allocation state"),
        ("", "Expected a versioned"),
        ("version: true\nipv4_pools: {}\n", "Expected a versioned"),
        (safe_dump({"version": 2, "ipv4_pools": {"broken": {}}}), "Invalid IPv4 allocation state"),
        (safe_dump({"version": 2, "ipv4_pools": {definition.key: {owner: "192.0.2.1"}}}), "address/prefix"),
        (
            safe_dump(
                {"version": 2, "ipv4_pools": {definition.key: {owner: "192.0.2.1/24"}, replace(definition, subnet="ALIAS").key: {owner: "192.0.2.2/24"}}}
            ),
            "Duplicate allocation owner",
        ),
    ):
        path.write_text(contents)
        with fails(message):
            Ipv4PoolCollection(path)
    # Duplicate assignment keys would otherwise silently discard one reservation in a YAML mapping.
    content = safe_dump(valid)
    assignment_line = next(line for line in content.splitlines() if "192.0.2.1/24" in line)
    path.write_text(content.replace(assignment_line, f"{assignment_line}\n{assignment_line.replace('192.0.2.1', '192.0.2.2')}"))
    with fails("Duplicate YAML key"):
        Ipv4PoolCollection(path)


def main() -> None:
    schema_contract()
    with TemporaryDirectory(prefix="avd-ipv4-allocation-tests-") as temporary:
        root = Path(temporary)
        for test in (
            pool_foundation,
            pool_state_validation,
            persistent_builds,
            overrides_and_collisions,
            node_subnet_inheritance,
            subnet_boundaries,
            facts_to_configuration,
            digital_twin_allocations,
            state_safety,
        ):
            test(root / test.__name__)
    print("IPv4 management allocation integration checks passed.")  # noqa: T201


if __name__ == "__main__":
    main()
