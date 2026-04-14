# Copyright (c) 2025-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

import sys
from pathlib import Path
from typing import Any
from unittest import mock

import pytest
from ansible.parsing.dataloader import DataLoader
from ansible.release import __version__ as ansible_version
from ansible.template import Templar

from pyavd._utils import AVDTemplar
from pyavd._utils.template_var import template_var


@pytest.mark.parametrize(("my_var_value", "expected"), [pytest.param(42, "42", id="not None"), pytest.param(None, "", id="None")])
def test_template_var(tmp_path: Path, my_var_value: Any, expected: str) -> None:
    """Testing a simple jinja template."""
    file = tmp_path / "dummy.j2"
    content = "{{ my_var }}"
    _ = file.write_text(content)

    loader = DataLoader()
    templar = Templar(loader)
    searchpath = [str(tmp_path)]
    avd_templar = AVDTemplar(templar, loader, searchpath)

    mocked_module = mock.MagicMock(ANSIBLE_ABOVE_2_19=ansible_version.startswith(("2.19", "2.2")))
    with mock.patch.dict(sys.modules, {"ansible_collections.arista.avd.plugins.plugin_utils.utils": mocked_module}):
        result = template_var(str(file), {"my_var": my_var_value}, avd_templar)

    assert result == expected
