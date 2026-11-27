# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from copy import deepcopy
from typing import TYPE_CHECKING

import pytest

from pyavd import (
    ConfigRenderConfiguration,
    DocRenderConfiguration,
    get_avd_facts,
    get_device_config,
    get_device_doc,
    get_device_structured_config,
    validate_inputs,
    validate_structured_config,
)
from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._schema.avd_version import FUTURE_SETTINGS, get_future_defaults
from pyavd._schema.store import create_store
from pyavd.api.schemas import AVDDesign, EOSConfig

if TYPE_CHECKING:
    from collections.abc import Callable

    from pyavd.api.validation import ValidatedDataResult


@pytest.mark.parametrize(("schema_name", "future_key"), [("eos_designs", "avd_design_future"), ("eos_cli_config_gen", "eos_config_future")])
def test_future_settings_match_schema(schema_name: str, future_key: str) -> None:
    """Require every future flag and its availability version to be registered correctly."""
    flags = create_store()[schema_name]["keys"][future_key]["keys"]
    expected = {}
    for name, schema in flags.items():
        assert schema["type"] == "bool"
        version = schema["description"].splitlines()[0].removeprefix("Available from AVD ").removesuffix(".")
        expected[name] = tuple(int(part) for part in version.split("."))
    actual = {name: since for since, names in FUTURE_SETTINGS[future_key].items() for name in names}
    assert actual == expected


@pytest.mark.parametrize("model", [AVDDesign, EOSConfig])
@pytest.mark.parametrize("version", [None, "6.0.0", "6.1.0", "6.2.0", "6.3.0", "6.4.0", "6.4.99", "6.5.0", "6.6.0", "6.10.0"])
def test_version_defaults(model: type[AVDDesign | EOSConfig], version: str | None) -> None:
    inputs = {} if version is None else {"avd_version": version}
    loaded = model._from_dict(inputs)
    for future_key, versions in FUTURE_SETTINGS.items():
        if future_key not in model._fields:
            continue
        settings = getattr(loaded, future_key)
        selected = tuple(int(part) for part in version.split(".")) if version else (0, 0, 0)
        for since, flags in versions.items():
            for flag in flags:
                assert getattr(settings, flag) is (since <= selected)
    assert inputs == ({} if version is None else {"avd_version": version})


def test_explicit_design_overrides() -> None:
    inputs = {
        "avd_version": "6.3.0",
        "avd_design_future": {
            "accept_dhcp_default_route_for_mgmt_ip_dhcp": False,
            "allow_recursive_profile_inheritance": True,
        },
        "eos_config_future": {"render_spanning_tree_portfast_edge": False, "new_bgp_peer_group_cli_order": True},
    }
    original = deepcopy(inputs)
    loaded = AVDDesign._from_dict(inputs)
    assert loaded.avd_design_future.accept_dhcp_default_route_for_mgmt_ip_dhcp is False
    assert loaded.avd_design_future.allow_recursive_profile_inheritance is True
    assert loaded.avd_design_future.configure_inband_mgmt_ipv6_vrf is True
    assert loaded.eos_config_future.render_spanning_tree_portfast_edge is False
    assert loaded.eos_config_future.new_bgp_peer_group_cli_order is True
    assert inputs == original


def test_model_constructor_does_not_modify_supplied_settings() -> None:
    settings = EOSConfig.EosConfigFuture(new_ip_radius_cli_order=False)
    model = EOSConfig(avd_version="6.5.0", eos_config_future=settings)
    assert model.eos_config_future.new_ip_radius_cli_order is False
    assert model.eos_config_future.render_spanning_tree_portfast_edge is True
    assert settings._as_dict() == {"new_ip_radius_cli_order": False}


@pytest.mark.parametrize("as_model", [False, True])
@pytest.mark.parametrize(
    ("version", "override", "expected_edge"), [(None, None, False), ("6.2.0", None, False), ("6.3.0", None, True), ("6.5.0", False, False)]
)
def test_config_rendering(as_model: bool, version: str | None, override: bool | None, expected_edge: bool) -> None:
    inputs = {"hostname": "test", "ethernet_interfaces": [{"name": "Ethernet1", "spanning_tree_portfast": "edge"}]}
    if version is not None:
        inputs["avd_version"] = version
    if override is not None:
        inputs["eos_config_future"] = {"render_spanning_tree_portfast_edge": override}
    original = deepcopy(inputs)
    data = EOSConfig._from_dict(inputs) if as_model else inputs
    output = get_device_config(data, configuration=ConfigRenderConfiguration(hide_passwords=True))
    command = "   spanning-tree portfast edge\n" if expected_edge else "   spanning-tree portfast\n"
    assert command in output
    assert inputs == original


@pytest.mark.parametrize("as_model", [False, True])
@pytest.mark.parametrize("override", [None, False])
def test_documentation_rendering(as_model: bool, override: bool | None) -> None:
    inputs = {"hostname": "test", "avd_version": "6.3.0", "monitor_layer1": {"enabled": False, "logging_mac_fault": True}}
    if override is not None:
        inputs["eos_config_future"] = {"render_monitor_layer1_without_enabled": override}
    original = deepcopy(inputs)
    data = EOSConfig._from_dict(inputs) if as_model else inputs
    output = get_device_doc(data, configuration=DocRenderConfiguration(hide_passwords=True))
    assert ("monitor layer1" in output) is (override is None)
    assert inputs == original


@pytest.mark.parametrize("validator", [validate_inputs, validate_structured_config])
@pytest.mark.parametrize("version", ["6.5.0", "6.4.99", "6.10.0", "invalid", "6.5", "6.5.0rc1", "", "6.5.0\n"])
def test_version_validation(validator: Callable[..., ValidatedDataResult], version: str) -> None:
    inputs = {"fabric_name": "FABRIC", "avd_version": version} if validator is validate_inputs else {"avd_version": version}
    result = validator(inputs)
    assert (result.validated_data is not None) is (version in {"6.5.0", "6.4.99", "6.10.0"})


@pytest.mark.parametrize("version", ["invalid", "6.5", "6.5.0rc1", "", "6.5.0\n"])
def test_invalid_version_without_validation(version: str) -> None:
    with pytest.raises(AristaAvdInvalidInputsError, match="avd_version"):
        get_future_defaults(version, "eos_config_future")


@pytest.mark.parametrize("as_model", [False, True])
def test_design_to_config_propagation(as_model: bool) -> None:
    inputs = {
        "fabric_name": "FABRIC",
        "avd_version": "6.3.0",
        "devices": [{"name": "testhost1", "type": "l2leaf"}],
        "eos_config_future": {"new_ip_radius_cli_order": False},
    }
    result = validate_inputs(inputs)
    assert result.validated_data is not None
    assert not result.validation_result.ignored_eos_config_keys
    data = AVDDesign._from_dict(result.validated_data) if as_model else result.validated_data
    facts = get_avd_facts({"testhost1": data})
    config = get_device_structured_config("testhost1", data, facts)
    assert config.avd_version == "6.3.0"
    assert config.eos_config_future.new_ip_radius_cli_order is False
    assert config.eos_config_future.render_spanning_tree_portfast_edge is True
    assert config.eos_config_future.new_bgp_peer_group_cli_order is False


@pytest.mark.parametrize("as_model", [False, True])
@pytest.mark.parametrize("settings", [None, {"render_spanning_tree_portfast_edge": None}])
def test_explicit_null_does_not_enable_flag(as_model: bool, settings: dict | None) -> None:
    inputs = {
        "hostname": "test",
        "avd_version": "6.5.0",
        "eos_config_future": settings,
        "ethernet_interfaces": [{"name": "Ethernet1", "spanning_tree_portfast": "edge"}],
    }
    data = EOSConfig._from_dict(inputs) if as_model else inputs
    assert "   spanning-tree portfast\n" in get_device_config(data)
