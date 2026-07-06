# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from collections import ChainMap
from copy import deepcopy
from typing import Any, ClassVar

import pytest

from pyavd import ConfigRenderConfiguration, DocRenderConfiguration, get_device_config, get_device_doc
from pyavd.api.schemas import EOSConfig


class MockTemplar:
    rendered_template_vars: ClassVar[dict[str, Any] | ChainMap[str, Any]] = {}

    def __init__(self, precompiled_templates_path: str) -> None:
        del precompiled_templates_path

    def render_template_from_file(self, template_file: str, template_vars: dict[str, Any] | ChainMap[str, Any]) -> str:
        del template_file
        MockTemplar.rendered_template_vars = template_vars
        return "rendered"


@pytest.fixture(autouse=True)
def mock_templar(monkeypatch: pytest.MonkeyPatch) -> None:
    MockTemplar.rendered_template_vars = {}
    monkeypatch.setattr("pyavd.templater.Templar", MockTemplar)


def get_rendered_template_vars() -> dict[str, Any] | ChainMap[str, Any]:
    return MockTemplar.rendered_template_vars


@pytest.fixture
def structured_config() -> dict[str, Any]:
    return {
        "enable_password": {
            "hash_algorithm": "sha512",
            "key": "super-secret",
        },
        "eos_cli_config_gen_configuration": {
            "hide_passwords": True,
        },
        "eos_cli_config_gen_documentation": {
            "hide_passwords": True,
        },
    }


def test_get_device_config_hide_passwords_uses_structured_config_by_default(structured_config: dict[str, Any]) -> None:
    """Verify structured config hide_passwords behavior is preserved."""
    get_device_config(structured_config)
    rendered_template_vars = get_rendered_template_vars()

    assert rendered_template_vars is structured_config
    assert rendered_template_vars["eos_cli_config_gen_configuration"]["hide_passwords"] is True
    assert "_eos_cli_config_gen_hide_passwords" not in rendered_template_vars


def test_get_device_config_hide_passwords_configuration_overrides_structured_config(structured_config: dict[str, Any]) -> None:
    """Verify explicit config render option overrides structured config."""
    original_structured_config = deepcopy(structured_config)

    get_device_config(structured_config, configuration=ConfigRenderConfiguration(hide_passwords=False))
    rendered_template_vars = get_rendered_template_vars()

    assert isinstance(rendered_template_vars, ChainMap)
    assert rendered_template_vars.maps == [structured_config, {"_eos_cli_config_gen_hide_passwords": False}]
    assert rendered_template_vars["_eos_cli_config_gen_hide_passwords"] is False
    assert rendered_template_vars["eos_cli_config_gen_configuration"]["hide_passwords"] is True
    assert structured_config == original_structured_config


def test_get_device_config_hide_passwords_configuration_without_structured_config_key(structured_config: dict[str, Any]) -> None:
    """Verify config render option works when structured config files do not contain the role setting."""
    structured_config.pop("eos_cli_config_gen_configuration")

    get_device_config(structured_config, configuration=ConfigRenderConfiguration(hide_passwords=True))
    rendered_template_vars = get_rendered_template_vars()

    assert isinstance(rendered_template_vars, ChainMap)
    assert rendered_template_vars["_eos_cli_config_gen_hide_passwords"] is True
    assert "eos_cli_config_gen_configuration" not in structured_config
    assert "eos_cli_config_gen_configuration" not in rendered_template_vars


def test_get_device_config_hide_passwords_configuration_updates_dumped_eosconfig(structured_config: dict[str, Any]) -> None:
    """Verify config render option overlays the dumped EOSConfig without an extra copy."""
    get_device_config(EOSConfig._from_dict(structured_config), configuration=ConfigRenderConfiguration(hide_passwords=False))
    rendered_template_vars = get_rendered_template_vars()

    assert isinstance(rendered_template_vars, ChainMap)
    assert rendered_template_vars["_eos_cli_config_gen_hide_passwords"] is False
    assert rendered_template_vars["eos_cli_config_gen_configuration"]["hide_passwords"] is True


def test_get_device_doc_hide_passwords_uses_structured_config_by_default(structured_config: dict[str, Any]) -> None:
    """Verify structured config documentation hide_passwords behavior is preserved."""
    get_device_doc(structured_config)
    rendered_template_vars = get_rendered_template_vars()

    assert rendered_template_vars is structured_config
    assert rendered_template_vars["eos_cli_config_gen_documentation"]["hide_passwords"] is True
    assert "_eos_cli_config_gen_hide_passwords" not in rendered_template_vars


def test_get_device_doc_hide_passwords_configuration_overrides_structured_config(structured_config: dict[str, Any]) -> None:
    """Verify explicit documentation render option overrides structured config."""
    original_structured_config = deepcopy(structured_config)

    get_device_doc(structured_config, configuration=DocRenderConfiguration(hide_passwords=False))
    rendered_template_vars = get_rendered_template_vars()

    assert isinstance(rendered_template_vars, ChainMap)
    assert rendered_template_vars.maps == [structured_config, {"_eos_cli_config_gen_hide_passwords": False}]
    assert rendered_template_vars["_eos_cli_config_gen_hide_passwords"] is False
    assert rendered_template_vars["eos_cli_config_gen_documentation"]["hide_passwords"] is True
    assert structured_config == original_structured_config


def test_get_device_doc_hide_passwords_configuration_without_structured_config_key(structured_config: dict[str, Any]) -> None:
    """Verify documentation render option works when structured config files do not contain the role setting."""
    structured_config.pop("eos_cli_config_gen_documentation")

    get_device_doc(structured_config, configuration=DocRenderConfiguration(hide_passwords=True))
    rendered_template_vars = get_rendered_template_vars()

    assert isinstance(rendered_template_vars, ChainMap)
    assert rendered_template_vars["_eos_cli_config_gen_hide_passwords"] is True
    assert "eos_cli_config_gen_documentation" not in structured_config
    assert "eos_cli_config_gen_documentation" not in rendered_template_vars


def test_get_device_doc_hide_passwords_configuration_updates_dumped_eosconfig(structured_config: dict[str, Any]) -> None:
    """Verify documentation render option overlays the dumped EOSConfig without an extra copy."""
    get_device_doc(EOSConfig._from_dict(structured_config), configuration=DocRenderConfiguration(hide_passwords=False))
    rendered_template_vars = get_rendered_template_vars()

    assert isinstance(rendered_template_vars, ChainMap)
    assert rendered_template_vars["_eos_cli_config_gen_hide_passwords"] is False
    assert rendered_template_vars["eos_cli_config_gen_documentation"]["hide_passwords"] is True
