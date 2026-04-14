# Copyright (c) 2025-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

import sys
from pathlib import Path
from unittest import mock

import pytest
from ansible.parsing.dataloader import DataLoader
from ansible.release import __version__ as ansible_version
from ansible.template import Templar

from pyavd._utils import AVDTemplar
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
    avd_templar = AVDTemplar(templar, loader, searchpath)

    mocked_module = mock.MagicMock(ANSIBLE_ABOVE_2_19=ansible_version.startswith(("2.19", "2.2")))
    with mock.patch.dict(sys.modules, {"ansible_collections.arista.avd.plugins.plugin_utils.utils": mocked_module}):
        result = template(str(file), {"my_var": 42}, avd_templar)

    assert result == 42
