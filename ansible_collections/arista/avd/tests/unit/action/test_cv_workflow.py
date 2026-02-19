# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

from dataclasses import asdict, dataclass
from pathlib import Path

import pytest
from ansible.errors import AnsibleVariableTypeError
from ansible.executor.task_result import CallbackTaskResult
from ansible.inventory.host import Host
from ansible.playbook.task import Task

from pyavd._cv.workflows.models import AvdConfiglet, AvdManifest


@dataclass(frozen=True)
class MockedAvdConfiglet:
    """Mocked AvdConfiglet with Path type file attribute."""

    name: str
    file: Path


@dataclass(frozen=True)
class MockedAvdManifest:
    """Mocked AvdManifest with MockedAvdConfiglets."""

    configlets: tuple[MockedAvdConfiglet, ...]


class TestCvWorkflowReturnValueSerialization:
    """Test that cv_workflow's return values can be processed by Ansible."""

    def test_avd_configlet_serialization_success(self) -> None:
        """Test that AvdConfiglet can be successfully serialized in Ansible return values."""
        configlet = AvdConfiglet.from_dict({"name": "TestConfiglet", "file": "/path/to/file.cfg"})
        result = asdict(configlet)

        # Confirm that asdict() preserves the string type
        assert isinstance(result["file"], str)

        host = Host(name="test_host")
        task = Task()
        task._uuid = "test-uuid"

        callback_result = CallbackTaskResult(host=host, task=task, return_data=result, task_fields={})
        transformed = callback_result.result

        assert transformed["name"] == "TestConfiglet"
        assert transformed["file"] == "/path/to/file.cfg"
        assert isinstance(transformed["name"], str)
        assert isinstance(transformed["file"], str)

    def test_avd_configlet_serialization_failure(self) -> None:
        """Test that MockedAvdConfiglet dataclass with Path field can not be successfully serialized in Ansible return values."""
        configlet = MockedAvdConfiglet(name="TestConfiglet", file=Path("/path/to/file.cfg"))
        result = asdict(configlet)

        # Confirm that asdict() preserves the Path object
        assert isinstance(result["file"], Path)

        host = Host(name="test_host")
        task = Task()
        task._uuid = "test-uuid"

        callback_result = CallbackTaskResult(host=host, task=task, return_data=result, task_fields={})

        with pytest.raises(AnsibleVariableTypeError, match="Type 'PosixPath' is unsupported for variable storage"):
            # Avoiding C0104: Disallowed name "_" (disallowed-name)
            _unused = callback_result.result

    def test_avd_manifest_serialization_success(self) -> None:
        """Test that AvdManifest with AvdConfiglets can be successfully serialized in Ansible return values."""
        configlet1 = AvdConfiglet.from_dict({"name": "TestConfiglet1", "file": "/path/to/file1.cfg"})
        configlet2 = AvdConfiglet.from_dict({"name": "TestConfiglet2", "file": "/path/to/file2.cfg"})
        manifest = AvdManifest(configlets=(configlet1, configlet2), containers=())

        result = {"static_config_manifest": asdict(manifest)}

        # Confirm that asdict() preserves the string type
        assert isinstance(result["static_config_manifest"]["configlets"][0]["file"], str)
        assert isinstance(result["static_config_manifest"]["configlets"][1]["file"], str)

        host = Host(name="test_host")
        task = Task()
        task._uuid = "test-uuid"

        callback_result = CallbackTaskResult(host=host, task=task, return_data=result, task_fields={})

        transformed = callback_result.result

        assert len(transformed["static_config_manifest"]["configlets"]) == 2
        assert all(isinstance(configlet["file"], str) for configlet in transformed["static_config_manifest"]["configlets"])

    def test_avd_manifest_serialization_failure(self) -> None:
        """Test that MockedAvdManifest with MockedAvdConfiglets containing Path fields can not be successfully serialized in Ansible return values."""
        configlet1 = MockedAvdConfiglet(name="TestConfiglet1", file=Path("/path/to/file1.cfg"))
        configlet2 = MockedAvdConfiglet(name="TestConfiglet2", file=Path("/path/to/file2.cfg"))
        manifest = MockedAvdManifest(configlets=(configlet1, configlet2))

        result = {"static_config_manifest": asdict(manifest)}

        # Confirm that asdict() preserves the Path typeructure
        assert isinstance(result["static_config_manifest"]["configlets"][0]["file"], Path)
        assert isinstance(result["static_config_manifest"]["configlets"][1]["file"], Path)

        host = Host(name="test_host")
        task = Task()
        task._uuid = "test-uuid"

        callback_result = CallbackTaskResult(host=host, task=task, return_data=result, task_fields={})

        with pytest.raises(AnsibleVariableTypeError, match="Type 'PosixPath' is unsupported for variable storage"):
            # Avoiding C0104: Disallowed name "_" (disallowed-name)
            _unused = callback_result.result
