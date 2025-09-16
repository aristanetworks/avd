# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

from pathlib import Path
from unittest.mock import MagicMock

import pytest

from pyavd._utils.template import template


def test_template_empty_templar_raise() -> None:
    with pytest.raises(NotImplementedError, match=r"Jinja Templating is not implemented in pyavd"):
        template("dummy", {}, None)


def test_template(tmp_path: Path) -> None:
    """
    Mocking ansible Templar otherwise we need ansible for pytest.

    This is not really a good test.
    """
    file = tmp_path / "dummy.j2"
    content = "{{ my_var }}"
    # not useful
    _ = file.write_text(content)

    # magic mocking Ansible stuff
    templar = MagicMock()
    loader = MagicMock()
    loader._get_file_contents.return_value = (content, {})
    templar._loader = loader

    template(str(file), {"my_var": 42}, templar)
    loader.path_dwim_relative_stack.assert_called_once()
    loader._get_file_contents.assert_called_once()
    templar.set_temporary_context.assert_called_once_with(available_variables={"my_var": 42})
    templar.template.assert_called_once_with(content, convert_data=False, escape_backslashes=False)
