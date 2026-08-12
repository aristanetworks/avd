# Copyright (c) 2025-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

from pathlib import Path
from typing import Any

import pytest
from ansible.parsing.dataloader import DataLoader
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
    avd_templar = AVDTemplar(templar, loader, searchpath, ansible_above_2_19=True)

    result = template_var(str(file), {"my_var": my_var_value}, avd_templar)

    assert result == expected
