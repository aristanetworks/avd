# Copyright (c) 2025-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

from pathlib import Path

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
