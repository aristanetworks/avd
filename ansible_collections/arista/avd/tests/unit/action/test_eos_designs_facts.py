# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING
from unittest.mock import MagicMock, patch

import pytest
from ansible.errors import AnsibleActionFail

from ansible_collections.arista.avd.plugins.action.eos_designs_facts import ActionModule
from pyavd._errors import AristaAvdError

if TYPE_CHECKING:
    from collections.abc import Callable

MODULE_PATH = "ansible_collections.arista.avd.plugins.action.eos_designs_facts"
MOCK_TMP_DIR = "/avd/mocked/tmp"
MOCK_OUTPUT_DIR = "/avd/mocked/output"


def test_run_raises_when_pyavd_not_installed(action_module: Callable[..., ActionModule]) -> None:
    """Test that plugin execution fails when pyavd is missing."""
    module = action_module(
        ActionModule,
        {"tmp_dir": MOCK_TMP_DIR, "output_dir": MOCK_OUTPUT_DIR},
        ansible_name="arista.avd.eos_designs_facts",
    )

    with (
        patch(f"{MODULE_PATH}.HAS_PYAVD", new=False),
        pytest.raises(
            AnsibleActionFail,
            match=r"Error during plugin 'arista.avd.eos_designs_facts' execution: plugin requires the 'pyavd' Python library. Got import error",
        ),
    ):
        module.run(task_vars={})


@pytest.mark.parametrize(
    ("fabric_name", "ansible_play_hosts_all"),
    [
        pytest.param("FABRIC_A", ["spine-1", "outsider-1"], id="play_hosts_not_subset_of_fabric_group"),
        pytest.param(None, ["spine-1"], id="fabric_name_is_none"),
    ],
)
def test_run_raises_when_fabric_name_invalid(
    action_module: Callable[..., ActionModule],
    fabric_name: str | None,
    ansible_play_hosts_all: list[str],
) -> None:
    """Test that plugin execution fails when fabric_name is missing or invalid."""
    module = action_module(
        ActionModule,
        {"tmp_dir": MOCK_TMP_DIR, "output_dir": MOCK_OUTPUT_DIR},
        ansible_name="arista.avd.eos_designs_facts",
    )
    module._templar.template.side_effect = lambda value: value

    task_vars = {
        "groups": {"FABRIC_A": ["spine-1", "spine-2"]},
        "fabric_name": fabric_name,
        "ansible_play_hosts_all": ansible_play_hosts_all,
    }

    with (
        patch(f"{MODULE_PATH}.HAS_PYAVD", new=True),
        patch(f"{MODULE_PATH}.get_eos_designs_facts_path"),
        patch(f"{MODULE_PATH}.natural_sort", side_effect=lambda value, *_, **__: sorted(value or [])),
        pytest.raises(AnsibleActionFail) as exc_info,
    ):
        module.run(task_vars=task_vars)

    assert exc_info.value.message == (
        "Error during plugin 'arista.avd.eos_designs_facts' execution: "
        "Invalid/missing 'fabric_name' variable. "
        "All hosts in the play must have the same 'fabric_name' value "
        "which must point to an Ansible Group containing the hosts."
        f"play_hosts: {ansible_play_hosts_all}"
    )


def test_load_validated_inputs_raises_when_file_missing(action_module: Callable[..., ActionModule]) -> None:
    """Test that FileNotFoundError is raised with a message identifying the missing host."""
    module = action_module(ActionModule)
    module.tmp_dir = MOCK_TMP_DIR

    mock_file_path = MagicMock()
    mock_file_path.exists.return_value = False
    mock_validated_path = MagicMock()
    mock_validated_path.__truediv__ = MagicMock(return_value=mock_file_path)

    with (
        patch(f"{MODULE_PATH}.get_tmp_paths", return_value=(MagicMock(), mock_validated_path)),
        pytest.raises(
            FileNotFoundError,
            match=(
                r"Missing validated inputs for host 'my-spine-device'. "
                r"Ensure the 'arista.avd.validate_inputs' task ran successfully for this host "
                r"and that no validation errors occurred."
            ),
        ),
    ):
        module.load_validated_inputs(["my-spine-device"])


def test_render_facts_raises_arista_avd_error(action_module: Callable[..., ActionModule]) -> None:
    """Test that AristaAvdError raised by pyavd.get_facts bubbles up from render_facts."""
    module = action_module(ActionModule)
    module._digital_twin = False
    module.template_output = False

    original_error = AristaAvdError("pyavd blew up")

    with (
        patch(f"{MODULE_PATH}.get_facts", side_effect=original_error),
        pytest.raises(AristaAvdError, match=r"pyavd blew up") as exc_info,
    ):
        module.render_facts(all_inputs={}, pool_manager=MagicMock(), all_hostvars={}, templar=MagicMock())

    assert exc_info.value is original_error
