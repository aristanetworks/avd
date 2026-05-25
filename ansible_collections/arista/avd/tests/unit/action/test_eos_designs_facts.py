# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING
from unittest.mock import MagicMock, patch

import pytest
from ansible.errors import AnsibleActionFail

from ansible_collections.arista.avd.plugins.action.eos_designs_facts import ActionModule

if TYPE_CHECKING:
    from collections.abc import Callable

MODULE_PATH = "ansible_collections.arista.avd.plugins.action.eos_designs_facts"
MOCK_TMP_DIR = "/avd/mocked/tmp"


@pytest.fixture
def action_module() -> Callable[..., ActionModule]:
    def _factory(task_args: dict | None = None) -> ActionModule:
        mock_task = MagicMock()
        mock_task.args = task_args or {}
        mock_task.async_val = False
        mock_task.check_mode = False
        return ActionModule(
            task=mock_task,
            connection=MagicMock(),
            play_context=MagicMock(),
            loader=MagicMock(),
            templar=MagicMock(),
            shared_loader_obj=MagicMock(),
        )

    return _factory


def test_run_raises_when_pyavd_not_installed(action_module: Callable[..., ActionModule]) -> None:
    """Test that AnsibleActionFail is raised immediately when pyavd is missing."""
    module = action_module()

    with (
        patch(f"{MODULE_PATH}.HAS_PYAVD", new=False),
        patch("ansible.plugins.action.ActionBase.run", return_value={}),
        pytest.raises(AnsibleActionFail, match=r"The arista.avd.eos_designs_facts' plugin requires the 'pyavd' Python library. Got import error"),
    ):
        module.run(task_vars={})


def test_run_raises_when_play_hosts_not_in_fabric_group(action_module: Callable[..., ActionModule]) -> None:
    """Test that AnsibleActionFail is raised when ansible_play_hosts_all is not a subset of the fabric group."""
    module = action_module({"tmp_dir": MOCK_TMP_DIR})
    module._templar.template.side_effect = lambda value: value

    task_vars = {
        "groups": {"FABRIC_A": ["spine-1", "spine-2"]},
        "fabric_name": "FABRIC_A",
        "ansible_play_hosts_all": ["spine-1", "outsider-1"],
    }

    with (
        patch(f"{MODULE_PATH}.HAS_PYAVD", new=True),
        patch("ansible.plugins.action.ActionBase.run", return_value={}),
        patch(f"{MODULE_PATH}.get_eos_designs_facts_path"),
        patch(f"{MODULE_PATH}.natural_sort", side_effect=lambda value, ignore_case=False: sorted(value)),
        pytest.raises(AnsibleActionFail) as exc_info,
    ):
        module.run(task_vars=task_vars)

    assert exc_info.value.message == (
        "Invalid/missing 'fabric_name' variable. "
        "All hosts in the play must have the same 'fabric_name' value "
        "which must point to an Ansible Group containing the hosts."
        "play_hosts: ['spine-1', 'outsider-1']"
    )


def test_load_validated_inputs_raises_when_file_missing(action_module: Callable[..., ActionModule]) -> None:
    """Test that AnsibleActionFail is raised with a message identifying the missing host."""
    module = action_module()
    module.tmp_dir = MOCK_TMP_DIR

    mock_file_path = MagicMock()
    mock_file_path.exists.return_value = False
    mock_validated_path = MagicMock()
    mock_validated_path.__truediv__ = MagicMock(return_value=mock_file_path)

    with (
        patch(f"{MODULE_PATH}.get_tmp_paths", return_value=(MagicMock(), mock_validated_path)),
        pytest.raises(
            AnsibleActionFail,
            match=(
                r"Missing validated inputs for host 'my-spine-device'. "
                r"Ensure the 'arista.avd.validate_inputs' task ran successfully for this host "
                r"and that no validation errors occurred."
            ),
        ),
    ):
        module.load_validated_inputs(["my-spine-device"])


def test_render_facts_wraps_arista_avd_error_as_action_fail(action_module: Callable[..., ActionModule]) -> None:
    """Test that AristaAvdError raised by pyavd.get_facts is wrapped and chained as AnsibleActionFail."""
    module = action_module()
    module._digital_twin = False
    module.template_output = False

    from pyavd._errors import AristaAvdError

    original_error = AristaAvdError("pyavd blew up")

    with (
        patch(f"{MODULE_PATH}.get_facts", side_effect=original_error),
        pytest.raises(AnsibleActionFail, match=r"pyavd blew up") as exc_info,
    ):
        module.render_facts(all_inputs={}, pool_manager=MagicMock(), all_hostvars={}, templar=MagicMock())

    assert exc_info.value.__cause__ is original_error


