# Copyright (c) 2025-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

from collections import ChainMap, UserDict
from pathlib import Path
from types import MappingProxyType
from unittest.mock import patch

import pytest
from ansible.parsing.dataloader import DataLoader
from ansible.template import Templar

from pyavd._utils.avd_templar import AVDTemplar
from pyavd._utils.template import template


def test_template_empty_templar_raise() -> None:
    with pytest.raises(NotImplementedError, match=r"Jinja Templating is not implemented in pyavd"):
        template("dummy", {}, None)


def test_template(tmp_path: Path) -> None:
    """Testing a simple jinja template."""
    file = tmp_path / "dummy.j2"
    content = "{{ my_var }}"
    _ = file.write_text(content)

    loader = DataLoader()
    templar = Templar(loader)
    searchpath = [str(tmp_path)]
    avd_templar = AVDTemplar(templar, loader, searchpath, ansible_above_2_19=True)

    result = template(str(file), {"my_var": 42}, avd_templar)

    assert result == 42


def test_template_materializes_non_dict_chainmap_layers(tmp_path: Path) -> None:
    """Non-dict mappings are materialized only when passed to Ansible for rendering."""
    file = tmp_path / "dummy.j2"
    _ = file.write_text("{{ my_var }}")

    loader = DataLoader()
    templar = Templar(loader)
    avd_templar = AVDTemplar(templar, loader, [str(tmp_path)], ansible_above_2_19=True)
    template_vars = ChainMap({}, UserDict({"my_var": 42}))

    result = template(str(file), template_vars, avd_templar)

    assert result == 42


def test_template_reuses_user_dict_data(tmp_path: Path) -> None:
    """Repeated template renders reuse the underlying dictionary for UserDict layers."""
    file = tmp_path / "dummy.j2"
    _ = file.write_text("{{ my_var }}")
    loader = DataLoader()
    templar = Templar(loader)
    avd_templar = AVDTemplar(templar, loader, [str(tmp_path)], ansible_above_2_19=True)
    mapping = UserDict({"my_var": 42})
    overrides = {}
    template_vars = ChainMap(overrides, mapping)

    with patch.object(templar, "copy_with_new_env", wraps=templar.copy_with_new_env) as copy_with_new_env:
        assert template(str(file), template_vars, avd_templar) == 42
        mapping["my_var"] = 43
        assert template(str(file), template_vars, avd_templar) == 43

    assert copy_with_new_env.call_count == 2
    for call in copy_with_new_env.call_args_list:
        assert call.kwargs["available_variables"].maps[0] is overrides
        assert call.kwargs["available_variables"].maps[1] is mapping.data
    assert template_vars.maps[1] is mapping


def test_template_materializes_other_mapping_types(tmp_path: Path) -> None:
    """Mappings without a concrete data accessor still render through the conversion fallback."""
    file = tmp_path / "dummy.j2"
    _ = file.write_text("{{ my_var }}")
    loader = DataLoader()
    templar = Templar(loader)
    avd_templar = AVDTemplar(templar, loader, [str(tmp_path)], ansible_above_2_19=True)
    template_vars = ChainMap({}, MappingProxyType({"my_var": 42}))

    assert template(str(file), template_vars, avd_templar) == 42
