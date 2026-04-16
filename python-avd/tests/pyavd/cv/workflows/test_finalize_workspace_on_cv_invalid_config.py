# Copyright (c) 2024-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import re
from logging import WARNING
from typing import TYPE_CHECKING, ClassVar
from unittest.mock import patch

import pytest

from pyavd._cv.client.exceptions import CVWorkspaceBuildFailed
from pyavd._cv.workflows.constants import EOS_CLI_WARNINGS
from pyavd._cv.workflows.finalize_workspace_on_cv import _produce_cvworkspace_build_result, finalize_workspace_on_cv
from pyavd._cv.workflows.models import (
    CVDevice,
    CVWorkspace,
    CVWorkspaceBuildConfigValidationError,
    CVWorkspaceBuildConfigValidationWarning,
    CVWorkspaceBuildWarningsConfig,
)
from tests.pyavd.cv.constants import (
    MOCKED_WORKSPACE_ID,
    MOCKED_WORKSPACE_REQUEST_ID_BUILD_FAIL_CONFIG_VALIDATION,
    MOCKED_WORKSPACE_REQUEST_ID_BUILD_SUCCESS,
)
from tests.pyavd.cv.mockery import mocked_cvdevices

if TYPE_CHECKING:
    from pyavd._cv.client import CVClient


@pytest.mark.asyncio
@pytest.mark.parametrize("cv_client", [{"static_recording": True}], ids=["CV_CLIENT_STATIC_RECORDINGS"], indirect=True)
class TestFinalizeWorkspaceOnCVBuildErrors:
    """
    Test class for different ways to trigger configuration errors and warnings during the build of the Workspace when referencing invalid EOS configuration.

    All test methods that trigger config validation errors and warnings reference the following invalid designed configlets:

        - avd-ci-leaf1

            !
            interface Ethernet2
            spanning-tree portfast
            !

        - avd-ci-spine1

            spanning-tree mode spine1
            !
            ip prefix-list PL-LOOPBACKS-EVPN-OVERLAY
            seqq 10 permit 10.20.0.0/24 eq 32
            !
            !
            interface Ethernet2
            spanning-tree portfast
            !
            interface Ethernet3
            no shutdown
            mtu 1500
            no switchport
            ip address 10.23.0.8/31
            node-segment ipv4 index 1
            !

        - avd-ci-spine2

            spanning-tree mode spine2

    Each test method of the class executes the following test steps (unless other steps specified at the method level):

        -   description: Start Workspace build
            request: 'WorkspaceConfigSetRequest(value=WorkspaceConfig(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'),
                request=Request.START_BUILD, request_params=RequestParams(request_id='req-914310f3-08dd-4239-bd42-6d78b0000100')))'
            targeted_file: 'arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/3e5f35a5e74c704bd5ab2489162a937d7205b1da.json'

        -   description: Fetch build results
            request: 'WorkspaceStreamRequest(partial_eq_filter=[Workspace(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'))])'
            targeted_file: 'arista.workspace.v1.WorkspaceService/Subscribe/www.cv-prod-us-central1-c.arista.io/1560c66d73da2be39448d710f15853fb124b2548.json'

        -   description: Fetch build details
            request: 'WorkspaceBuildDetailsStreamRequest(partial_eq_filter=[WorkspaceBuildDetails(key=WorkspaceBuildDetailsKey(
                workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e', build_id='req-914310f3-08dd-4239-bd42-6d78b0000100'))])'
            targeted_file: 'arista.workspace.v1.WorkspaceBuildDetailsService/GetAll/www.cv-prod-us-central1-c.arista.io/
                85ff5d81e72ea2e4f36942319dc7329094cdb591.json'

    """

    CV_DEVICES: ClassVar[tuple[CVDevice, ...]] = (
        CVDevice(
            hostname="avd-ci-leaf1",
            serial_number="13C20F1EDCCED2D85F6DB2FB9E3AC5B6",
            system_mac_address="50:00:00:72:8b:31",
            _exists_on_cv=True,
            _streaming=True,
        ),
        CVDevice(
            hostname="avd-ci-spine1",
            serial_number="DCC816CEAC4BBD6319385043AD318362",
            system_mac_address="50:00:00:d7:ee:0b",
            _exists_on_cv=True,
            _streaming=True,
        ),
        CVDevice(
            hostname="avd-ci-spine2",
            serial_number="A7D46613D44DE45D68D5B5C5CBA06B0D",
            system_mac_address="50:00:00:cb:38:c2",
            _exists_on_cv=True,
            _streaming=True,
        ),
    )
    workspace_id: str = MOCKED_WORKSPACE_ID
    workspace_build_id: str = MOCKED_WORKSPACE_REQUEST_ID_BUILD_FAIL_CONFIG_VALIDATION["id"]

    @pytest.mark.parametrize(("build_warnings"), [pytest.param(False, id="BUILD_WARNINGS_FALSE"), pytest.param(True, id="BUILD_WARNINGS_TRUE")])
    async def test_clean_build(self, cv_client: CVClient, build_warnings: bool) -> None:
        """
        Test building clean Workspace (no configuration errors or warnings).

        Exact test steps:
        -   description: Start Workspace build
            request: 'WorkspaceConfigSetRequest(value=WorkspaceConfig(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'),
                request=Request.START_BUILD, request_params=RequestParams(request_id='req-914310f3-08dd-4239-bd42-6d78bf781229')))'
            targeted_file: 'arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/1fdd6fcd02728621447eeb8a1d8c9cbfdd9201c9.json'

        -   description: Fetch build results
            request: 'WorkspaceStreamRequest(partial_eq_filter=[Workspace(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'))])'
            targeted_file: 'arista.workspace.v1.WorkspaceService/Subscribe/www.cv-prod-us-central1-c.arista.io/1560c66d73da2be39448d710f15853fb124b2548.json'

        -   description: Fetch build details
            request: 'WorkspaceBuildDetailsStreamRequest(partial_eq_filter=[WorkspaceBuildDetails(key=WorkspaceBuildDetailsKey(
                workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e', build_id='req-914310f3-08dd-4239-bd42-6d78bf781229'))])'
            targeted_file: 'arista.workspace.v1.WorkspaceBuildDetailsService/GetAll/www.cv-prod-us-central1-c.arista.io/
                f451562f4f8c0dc37965a23121bb11dd6efc0f6a.json'
        """
        workspace_id: str = MOCKED_WORKSPACE_ID
        workspace_build_id: str = MOCKED_WORKSPACE_REQUEST_ID_BUILD_SUCCESS["id"]
        workspace_requested_state: str = "built"
        warnings = []

        with patch("pyavd._cv.client.workspace.uuid4", side_effect=[workspace_build_id.removeprefix("req-")]):
            workspace = CVWorkspace(
                id=workspace_id,
                requested_state=workspace_requested_state,
                build_warnings=CVWorkspaceBuildWarningsConfig(enabled=build_warnings),
            )
            await finalize_workspace_on_cv(workspace, cv_client, mocked_cvdevices(hostnames=["avd-ci-leaf1", "avd-ci-spine1", "avd-ci-spine2"]), warnings)

        assert workspace.build_id == workspace_build_id
        assert workspace.build_warnings.enabled == build_warnings
        assert not workspace.build_warnings.suppress_patterns
        assert not workspace.build_warnings.suppress_portfast
        assert not workspace.device_build_results
        assert not warnings

    async def test_build_failure(self, cv_client: CVClient) -> None:
        """Test building Workspace with invalid designed configuration using default error and warnings handling."""
        warnings = []

        with patch("pyavd._cv.client.workspace.uuid4", side_effect=[self.workspace_build_id.removeprefix("req-")]):
            workspace = CVWorkspace(id=self.workspace_id, requested_state="built")
            with pytest.raises(CVWorkspaceBuildFailed):
                await finalize_workspace_on_cv(workspace, cv_client, list(self.CV_DEVICES), warnings)

        assert workspace.build_id == self.workspace_build_id
        assert workspace.build_warnings.enabled is True
        assert not workspace.build_warnings.suppress_patterns
        assert not workspace.build_warnings.suppress_portfast
        assert not warnings
        assert len(workspace.device_build_results) == 3
        for build_result in workspace.device_build_results:
            match build_result.device.hostname:
                case "avd-ci-leaf1":
                    assert not build_result.config_validation.errors
                    assert len(build_result.config_validation.warnings) == 1
                    assert build_result.config_validation.warnings[0] == CVWorkspaceBuildConfigValidationWarning(
                        # strip start and end of the line markers
                        warning_msg=EOS_CLI_WARNINGS.get("portfast", "")[1:-1],
                        line_num=3,
                        configlet_name="avd-13C20F1EDCCED2D85F6DB2FB9E3AC5B6",
                    )

                case "avd-ci-spine1":
                    assert len(build_result.config_validation.errors) == 2
                    assert (
                        CVWorkspaceBuildConfigValidationError(
                            error_msg="> spanning-tree mode spine1 % Invalid input (at token 2: 'spine1')",
                            line_num=1,
                            configlet_name="avd-DCC816CEAC4BBD6319385043AD318362",
                        )
                        in build_result.config_validation.errors
                    )
                    assert (
                        CVWorkspaceBuildConfigValidationError(
                            error_msg=">    seqq 10 permit 10.20.0.0/24 eq 32 % Invalid input (at token 0: 'seqq')",
                            line_num=4,
                            configlet_name="avd-DCC816CEAC4BBD6319385043AD318362",
                        )
                        in build_result.config_validation.errors
                    )

                    assert len(build_result.config_validation.warnings) == 2
                    assert (
                        CVWorkspaceBuildConfigValidationWarning(
                            # strip start and end of the line markers
                            warning_msg=EOS_CLI_WARNINGS.get("portfast", "")[1:-1],
                            line_num=8,
                            configlet_name="avd-DCC816CEAC4BBD6319385043AD318362",
                        )
                        in build_result.config_validation.warnings
                    )
                    assert (
                        CVWorkspaceBuildConfigValidationWarning(
                            warning_msg="! /32 IPv4 address is not configured on the interface",
                            line_num=15,
                            configlet_name="avd-DCC816CEAC4BBD6319385043AD318362",
                        )
                        in build_result.config_validation.warnings
                    )

                # default case for avd-ci-spine2
                case _:
                    assert len(build_result.config_validation.errors) == 1
                    assert (
                        CVWorkspaceBuildConfigValidationError(
                            error_msg="> spanning-tree mode spine2 % Invalid input (at token 2: 'spine2')",
                            line_num=1,
                            configlet_name="avd-A7D46613D44DE45D68D5B5C5CBA06B0D",
                        )
                        in build_result.config_validation.errors
                    )
                    assert not build_result.config_validation.warnings

    async def test_build_failure_suppress_portfast_by_knob(self, cv_client: CVClient) -> None:
        """Test building Workspace with invalid designed configuration and portfast warnings suppressed by knob."""
        warnings = []

        with patch("pyavd._cv.client.workspace.uuid4", side_effect=[self.workspace_build_id.removeprefix("req-")]):
            workspace = CVWorkspace(
                id=self.workspace_id,
                requested_state="built",
                build_warnings=CVWorkspaceBuildWarningsConfig(suppress_portfast=True),
            )
            with pytest.raises(CVWorkspaceBuildFailed):
                await finalize_workspace_on_cv(workspace, cv_client, list(self.CV_DEVICES), warnings)

        assert workspace.build_id == self.workspace_build_id
        assert workspace.build_warnings.enabled is True
        assert not workspace.build_warnings.suppress_patterns
        assert workspace.build_warnings.suppress_portfast
        assert not warnings
        assert len(workspace.device_build_results) == 2
        for build_result in workspace.device_build_results:
            match build_result.device.hostname:
                case "avd-ci-spine1":
                    assert len(build_result.config_validation.errors) == 2
                    assert (
                        CVWorkspaceBuildConfigValidationError(
                            error_msg="> spanning-tree mode spine1 % Invalid input (at token 2: 'spine1')",
                            line_num=1,
                            configlet_name="avd-DCC816CEAC4BBD6319385043AD318362",
                        )
                        in build_result.config_validation.errors
                    )
                    assert (
                        CVWorkspaceBuildConfigValidationError(
                            error_msg=">    seqq 10 permit 10.20.0.0/24 eq 32 % Invalid input (at token 0: 'seqq')",
                            line_num=4,
                            configlet_name="avd-DCC816CEAC4BBD6319385043AD318362",
                        )
                        in build_result.config_validation.errors
                    )

                    assert len(build_result.config_validation.warnings) == 1
                    assert build_result.config_validation.warnings[0] == CVWorkspaceBuildConfigValidationWarning(
                        warning_msg="! /32 IPv4 address is not configured on the interface",
                        line_num=15,
                        configlet_name="avd-DCC816CEAC4BBD6319385043AD318362",
                    )

                # default case for avd-ci-spine2
                case _:
                    assert len(build_result.config_validation.errors) == 1
                    assert (
                        CVWorkspaceBuildConfigValidationError(
                            error_msg="> spanning-tree mode spine2 % Invalid input (at token 2: 'spine2')",
                            line_num=1,
                            configlet_name="avd-A7D46613D44DE45D68D5B5C5CBA06B0D",
                        )
                        in build_result.config_validation.errors
                    )
                    assert not build_result.config_validation.warnings

    async def test_build_failure_single_manual_suppress(self, cv_client: CVClient) -> None:
        """Test building Workspace with invalid designed configuration with manually suppressed single warning."""
        warnings = []

        with patch("pyavd._cv.client.workspace.uuid4", side_effect=[self.workspace_build_id.removeprefix("req-")]):
            workspace = CVWorkspace(
                id=self.workspace_id,
                requested_state="built",
                build_warnings=CVWorkspaceBuildWarningsConfig(suppress_patterns=[".*! /32 IPv4 address is not [a-z]+ on the.*"]),
            )
            with pytest.raises(CVWorkspaceBuildFailed):
                await finalize_workspace_on_cv(workspace, cv_client, list(self.CV_DEVICES), warnings)

        assert workspace.build_id == self.workspace_build_id
        assert workspace.build_warnings.enabled is True
        assert len(workspace.build_warnings.suppress_patterns) == 1
        assert not workspace.build_warnings.suppress_portfast
        assert not warnings
        assert len(workspace.device_build_results) == 3
        for build_result in workspace.device_build_results:
            match build_result.device.hostname:
                case "avd-ci-leaf1":
                    assert not build_result.config_validation.errors
                    assert len(build_result.config_validation.warnings) == 1
                    assert build_result.config_validation.warnings[0] == CVWorkspaceBuildConfigValidationWarning(
                        # strip start and end of the line markers
                        warning_msg=EOS_CLI_WARNINGS.get("portfast", "")[1:-1],
                        line_num=3,
                        configlet_name="avd-13C20F1EDCCED2D85F6DB2FB9E3AC5B6",
                    )

                case "avd-ci-spine1":
                    assert len(build_result.config_validation.errors) == 2
                    assert (
                        CVWorkspaceBuildConfigValidationError(
                            error_msg="> spanning-tree mode spine1 % Invalid input (at token 2: 'spine1')",
                            line_num=1,
                            configlet_name="avd-DCC816CEAC4BBD6319385043AD318362",
                        )
                        in build_result.config_validation.errors
                    )
                    assert (
                        CVWorkspaceBuildConfigValidationError(
                            error_msg=">    seqq 10 permit 10.20.0.0/24 eq 32 % Invalid input (at token 0: 'seqq')",
                            line_num=4,
                            configlet_name="avd-DCC816CEAC4BBD6319385043AD318362",
                        )
                        in build_result.config_validation.errors
                    )

                    assert len(build_result.config_validation.warnings) == 1
                    assert build_result.config_validation.warnings[0] == CVWorkspaceBuildConfigValidationWarning(
                        # strip start and end of the line markers
                        warning_msg=EOS_CLI_WARNINGS.get("portfast", "")[1:-1],
                        line_num=8,
                        configlet_name="avd-DCC816CEAC4BBD6319385043AD318362",
                    )

                # default case for avd-ci-spine2
                case _:
                    assert len(build_result.config_validation.errors) == 1
                    assert (
                        CVWorkspaceBuildConfigValidationError(
                            error_msg="> spanning-tree mode spine2 % Invalid input (at token 2: 'spine2')",
                            line_num=1,
                            configlet_name="avd-A7D46613D44DE45D68D5B5C5CBA06B0D",
                        )
                        in build_result.config_validation.errors
                    )
                    assert not build_result.config_validation.warnings

    async def test_build_failure_dual_manual_suppress(self, cv_client: CVClient) -> None:
        """Test building Workspace with invalid designed configuration with multiple manually suppressed warning."""
        warnings = []

        with patch("pyavd._cv.client.workspace.uuid4", side_effect=[self.workspace_build_id.removeprefix("req-")]):
            workspace = CVWorkspace(
                id=self.workspace_id,
                requested_state="built",
                build_warnings=CVWorkspaceBuildWarningsConfig(
                    suppress_patterns=[".*! /32 IPv4 address is not [a-z]+ on the.*", EOS_CLI_WARNINGS.get("portfast", "")]
                ),
            )
            with pytest.raises(CVWorkspaceBuildFailed):
                await finalize_workspace_on_cv(workspace, cv_client, list(self.CV_DEVICES), warnings)

        assert workspace.build_id == self.workspace_build_id
        assert workspace.build_warnings.enabled is True
        assert len(workspace.build_warnings.suppress_patterns) == 2
        assert not workspace.build_warnings.suppress_portfast
        assert not warnings
        assert len(workspace.device_build_results) == 2
        for build_result in workspace.device_build_results:
            match build_result.device.hostname:
                case "avd-ci-spine1":
                    assert len(build_result.config_validation.errors) == 2
                    assert (
                        CVWorkspaceBuildConfigValidationError(
                            error_msg="> spanning-tree mode spine1 % Invalid input (at token 2: 'spine1')",
                            line_num=1,
                            configlet_name="avd-DCC816CEAC4BBD6319385043AD318362",
                        )
                        in build_result.config_validation.errors
                    )
                    assert (
                        CVWorkspaceBuildConfigValidationError(
                            error_msg=">    seqq 10 permit 10.20.0.0/24 eq 32 % Invalid input (at token 0: 'seqq')",
                            line_num=4,
                            configlet_name="avd-DCC816CEAC4BBD6319385043AD318362",
                        )
                        in build_result.config_validation.errors
                    )

                    assert not build_result.config_validation.warnings

                # default case for avd-ci-spine2
                case _:
                    assert len(build_result.config_validation.errors) == 1
                    assert (
                        CVWorkspaceBuildConfigValidationError(
                            error_msg="> spanning-tree mode spine2 % Invalid input (at token 2: 'spine2')",
                            line_num=1,
                            configlet_name="avd-A7D46613D44DE45D68D5B5C5CBA06B0D",
                        )
                        in build_result.config_validation.errors
                    )
                    assert not build_result.config_validation.warnings

    async def test_build_failure_mixed_suppression(self, cv_client: CVClient) -> None:
        """Test building Workspace with invalid designed configuration with mixed manual and knob-based suppressed warning."""
        warnings = []

        with patch("pyavd._cv.client.workspace.uuid4", side_effect=[self.workspace_build_id.removeprefix("req-")]):
            workspace = CVWorkspace(
                id=self.workspace_id,
                requested_state="built",
                build_warnings=CVWorkspaceBuildWarningsConfig(
                    suppress_patterns=[".*! /32 IPv4 address is not [a-z]+ on the.*"],
                    suppress_portfast=True,
                ),
            )
            with pytest.raises(CVWorkspaceBuildFailed):
                await finalize_workspace_on_cv(workspace, cv_client, list(self.CV_DEVICES), warnings)

        assert workspace.build_id == self.workspace_build_id
        assert workspace.build_warnings.enabled is True
        assert len(workspace.build_warnings.suppress_patterns) == 1
        assert workspace.build_warnings.suppress_portfast
        assert not warnings
        assert len(workspace.device_build_results) == 2
        for build_result in workspace.device_build_results:
            match build_result.device.hostname:
                case "avd-ci-spine1":
                    assert len(build_result.config_validation.errors) == 2
                    assert (
                        CVWorkspaceBuildConfigValidationError(
                            error_msg="> spanning-tree mode spine1 % Invalid input (at token 2: 'spine1')",
                            line_num=1,
                            configlet_name="avd-DCC816CEAC4BBD6319385043AD318362",
                        )
                        in build_result.config_validation.errors
                    )
                    assert (
                        CVWorkspaceBuildConfigValidationError(
                            error_msg=">    seqq 10 permit 10.20.0.0/24 eq 32 % Invalid input (at token 0: 'seqq')",
                            line_num=4,
                            configlet_name="avd-DCC816CEAC4BBD6319385043AD318362",
                        )
                        in build_result.config_validation.errors
                    )

                    assert not build_result.config_validation.warnings

                # default case for avd-ci-spine2
                case _:
                    assert len(build_result.config_validation.errors) == 1
                    assert (
                        CVWorkspaceBuildConfigValidationError(
                            error_msg="> spanning-tree mode spine2 % Invalid input (at token 2: 'spine2')",
                            line_num=1,
                            configlet_name="avd-A7D46613D44DE45D68D5B5C5CBA06B0D",
                        )
                        in build_result.config_validation.errors
                    )
                    assert not build_result.config_validation.warnings

    async def test_build_failure_invalid_manual_suppression(self, cv_client: CVClient) -> None:
        """Test building Workspace with invalid designed configuration using incorrect Regex to manually suppress warnings."""
        warnings = []

        with patch("pyavd._cv.client.workspace.uuid4", side_effect=[self.workspace_build_id.removeprefix("req-")]):
            workspace = CVWorkspace(
                id=self.workspace_id,
                requested_state="built",
                build_warnings=CVWorkspaceBuildWarningsConfig(
                    suppress_patterns=[r"(?P<invalid"],
                ),
            )
            with pytest.raises(CVWorkspaceBuildFailed):
                await finalize_workspace_on_cv(workspace, cv_client, list(self.CV_DEVICES), warnings)

        assert workspace.build_id == self.workspace_build_id
        assert workspace.build_warnings.enabled is True
        assert len(workspace.build_warnings.suppress_patterns) == 1
        assert not workspace.build_warnings.suppress_portfast
        assert len(warnings) == 1
        assert warnings[0] == (
            r"_prepare_build_warnings_suppress_patterns: Failed to process proposed regex pattern '(?P<invalid'. "
            r"This incorrect pattern will not be used for warnings suppression. Error: 'missing >, unterminated name at position 4'"
        )
        assert len(workspace.device_build_results) == 3
        for build_result in workspace.device_build_results:
            match build_result.device.hostname:
                case "avd-ci-leaf1":
                    assert not build_result.config_validation.errors
                    assert len(build_result.config_validation.warnings) == 1
                    assert build_result.config_validation.warnings[0] == CVWorkspaceBuildConfigValidationWarning(
                        # strip start and end of the line markers
                        warning_msg=EOS_CLI_WARNINGS.get("portfast", "")[1:-1],
                        line_num=3,
                        configlet_name="avd-13C20F1EDCCED2D85F6DB2FB9E3AC5B6",
                    )

                case "avd-ci-spine1":
                    assert len(build_result.config_validation.errors) == 2
                    assert (
                        CVWorkspaceBuildConfigValidationError(
                            error_msg="> spanning-tree mode spine1 % Invalid input (at token 2: 'spine1')",
                            line_num=1,
                            configlet_name="avd-DCC816CEAC4BBD6319385043AD318362",
                        )
                        in build_result.config_validation.errors
                    )
                    assert (
                        CVWorkspaceBuildConfigValidationError(
                            error_msg=">    seqq 10 permit 10.20.0.0/24 eq 32 % Invalid input (at token 0: 'seqq')",
                            line_num=4,
                            configlet_name="avd-DCC816CEAC4BBD6319385043AD318362",
                        )
                        in build_result.config_validation.errors
                    )

                    assert len(build_result.config_validation.warnings) == 2
                    assert (
                        CVWorkspaceBuildConfigValidationWarning(
                            # strip start and end of the line markers
                            warning_msg=EOS_CLI_WARNINGS.get("portfast", "")[1:-1],
                            line_num=8,
                            configlet_name="avd-DCC816CEAC4BBD6319385043AD318362",
                        )
                        in build_result.config_validation.warnings
                    )
                    assert (
                        CVWorkspaceBuildConfigValidationWarning(
                            warning_msg="! /32 IPv4 address is not configured on the interface",
                            line_num=15,
                            configlet_name="avd-DCC816CEAC4BBD6319385043AD318362",
                        )
                        in build_result.config_validation.warnings
                    )

                # default case for avd-ci-spine2
                case _:
                    assert len(build_result.config_validation.errors) == 1
                    assert (
                        CVWorkspaceBuildConfigValidationError(
                            error_msg="> spanning-tree mode spine2 % Invalid input (at token 2: 'spine2')",
                            line_num=1,
                            configlet_name="avd-A7D46613D44DE45D68D5B5C5CBA06B0D",
                        )
                        in build_result.config_validation.errors
                    )
                    assert not build_result.config_validation.warnings

    async def test_build_failure_suppress_portfast_manually_and_by_knob(self, cv_client: CVClient) -> None:
        """Test building Workspace with invalid designed configuration suppressing portfast warnings munually and by knob at the same time."""
        warnings = []

        with patch("pyavd._cv.client.workspace.uuid4", side_effect=[self.workspace_build_id.removeprefix("req-")]):
            workspace = CVWorkspace(
                id=self.workspace_id,
                requested_state="built",
                build_warnings=CVWorkspaceBuildWarningsConfig(
                    suppress_patterns=[".*portfast should only be enabled on ports connected to a single host.*"],
                    suppress_portfast=True,
                ),
            )
            with pytest.raises(CVWorkspaceBuildFailed):
                await finalize_workspace_on_cv(workspace, cv_client, list(self.CV_DEVICES), warnings)

        assert workspace.build_id == self.workspace_build_id
        assert workspace.build_warnings.enabled is True
        assert len(workspace.build_warnings.suppress_patterns) == 1
        assert workspace.build_warnings.suppress_portfast
        assert not warnings
        assert len(workspace.device_build_results) == 2
        for build_result in workspace.device_build_results:
            match build_result.device.hostname:
                case "avd-ci-spine1":
                    assert len(build_result.config_validation.errors) == 2
                    assert (
                        CVWorkspaceBuildConfigValidationError(
                            error_msg="> spanning-tree mode spine1 % Invalid input (at token 2: 'spine1')",
                            line_num=1,
                            configlet_name="avd-DCC816CEAC4BBD6319385043AD318362",
                        )
                        in build_result.config_validation.errors
                    )
                    assert (
                        CVWorkspaceBuildConfigValidationError(
                            error_msg=">    seqq 10 permit 10.20.0.0/24 eq 32 % Invalid input (at token 0: 'seqq')",
                            line_num=4,
                            configlet_name="avd-DCC816CEAC4BBD6319385043AD318362",
                        )
                        in build_result.config_validation.errors
                    )

                    assert len(build_result.config_validation.warnings) == 1
                    assert build_result.config_validation.warnings[0] == CVWorkspaceBuildConfigValidationWarning(
                        warning_msg="! /32 IPv4 address is not configured on the interface",
                        line_num=15,
                        configlet_name="avd-DCC816CEAC4BBD6319385043AD318362",
                    )

                # default case for avd-ci-spine2
                case _:
                    assert len(build_result.config_validation.errors) == 1
                    assert (
                        CVWorkspaceBuildConfigValidationError(
                            error_msg="> spanning-tree mode spine2 % Invalid input (at token 2: 'spine2')",
                            line_num=1,
                            configlet_name="avd-A7D46613D44DE45D68D5B5C5CBA06B0D",
                        )
                        in build_result.config_validation.errors
                    )
                    assert not build_result.config_validation.warnings

    async def test_build_failure_suppress_all_warnings(self, cv_client: CVClient) -> None:
        """Test building Workspace with invalid designed configuration suppressing all warnings."""
        warnings = []

        with patch("pyavd._cv.client.workspace.uuid4", side_effect=[self.workspace_build_id.removeprefix("req-")]):
            workspace = CVWorkspace(
                id=self.workspace_id,
                requested_state="built",
                build_warnings=CVWorkspaceBuildWarningsConfig(
                    enabled=False,
                ),
            )
            with pytest.raises(CVWorkspaceBuildFailed):
                await finalize_workspace_on_cv(workspace, cv_client, list(self.CV_DEVICES), warnings)

        assert workspace.build_id == self.workspace_build_id
        assert not workspace.build_warnings.enabled
        assert not workspace.build_warnings.suppress_patterns
        assert not workspace.build_warnings.suppress_portfast
        assert not warnings
        assert len(workspace.device_build_results) == 2
        for build_result in workspace.device_build_results:
            match build_result.device.hostname:
                case "avd-ci-spine1":
                    assert len(build_result.config_validation.errors) == 2
                    assert (
                        CVWorkspaceBuildConfigValidationError(
                            error_msg="> spanning-tree mode spine1 % Invalid input (at token 2: 'spine1')",
                            line_num=1,
                            configlet_name="avd-DCC816CEAC4BBD6319385043AD318362",
                        )
                        in build_result.config_validation.errors
                    )
                    assert (
                        CVWorkspaceBuildConfigValidationError(
                            error_msg=">    seqq 10 permit 10.20.0.0/24 eq 32 % Invalid input (at token 0: 'seqq')",
                            line_num=4,
                            configlet_name="avd-DCC816CEAC4BBD6319385043AD318362",
                        )
                        in build_result.config_validation.errors
                    )

                    assert len(build_result.config_validation.warnings) == 0

                # default case for avd-ci-spine2
                case _:
                    assert len(build_result.config_validation.errors) == 1
                    assert (
                        CVWorkspaceBuildConfigValidationError(
                            error_msg="> spanning-tree mode spine2 % Invalid input (at token 2: 'spine2')",
                            line_num=1,
                            configlet_name="avd-A7D46613D44DE45D68D5B5C5CBA06B0D",
                        )
                        in build_result.config_validation.errors
                    )
                    assert not build_result.config_validation.warnings

    @pytest.mark.asyncio
    async def test_produce_cvworkspace_build_result(self, caplog: pytest.LogCaptureFixture, cv_client: CVClient) -> None:
        """
        Test possible use case where returned WorkspaceBuildDetails object does not match any of the devices targeted by our deployment.

        Engaged mocked API call:
        -   description: Fetch build details
            request: 'WorkspaceBuildDetailsStreamRequest(partial_eq_filter=[WorkspaceBuildDetails(key=WorkspaceBuildDetailsKey(
                workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e', build_id='req-914310f3-08dd-4239-bd42-6d78b0000100'))])'
            targeted_file: 'arista.workspace.v1.WorkspaceBuildDetailsService/GetAll/www.cv-prod-us-central1-c.arista.io/
                85ff5d81e72ea2e4f36942319dc7329094cdb591.json'

        """
        # Redefine list of CVDevices making sure avd-ci-leaf1 (13C20F1EDCCED2D85F6DB2FB9E3AC5B6) is missing in it
        cv_devices_short: tuple[CVDevice, ...] = (
            CVDevice(
                hostname="avd-ci-spine1",
                serial_number="DCC816CEAC4BBD6319385043AD318362",
                system_mac_address="50:00:00:d7:ee:0b",
                _exists_on_cv=True,
                _streaming=True,
            ),
            CVDevice(
                hostname="avd-ci-spine2",
                serial_number="A7D46613D44DE45D68D5B5C5CBA06B0D",
                system_mac_address="50:00:00:cb:38:c2",
                _exists_on_cv=True,
                _streaming=True,
            ),
        )

        # Fetch mocked/recorded API response which includes config validation warnings for avd-ci-leaf1 (13C20F1EDCCED2D85F6DB2FB9E3AC5B6)
        workspace_build_details = await cv_client.get_workspace_build_details(workspace_id=self.workspace_id, build_id=self.workspace_build_id)

        # Attempt to process CloudVision build details
        with caplog.at_level(WARNING):
            response = _produce_cvworkspace_build_result(
                workspace=CVWorkspace(id=self.workspace_id, requested_state="built"),
                workspace_build_details=workspace_build_details,
                compiled_workspace_build_warnings_suppress_list=[],
                devices=cv_devices_short,
            )

        # Assert that CVWorkspaceDeviceBuildResult objects are generated for avd-ci-spine1 and avd-ci-spine2
        assert len(response) == 2
        assert all((response_item.device.hostname in ["avd-ci-spine1", "avd-ci-spine2"]) for response_item in response)

        # Assert that CVWorkspaceDeviceBuildResult objects are not generated for avd-ci-leaf1
        assert not any(response_item.device.hostname == "avd-ci-leaf1" for response_item in response)

        # Assert that log message is generated for avd-ci-leaf1 which is missing in the list of CVDevices
        assert any(
            re.search(
                re.compile(
                    r"_produce_cvworkspace_build_result: Returned WorkspaceBuildDetails object references device '13C20F1EDCCED2D85F6DB2FB9E3AC5B6'.*"
                    r"warnings=ConfigErrors\(values=\[ConfigError\(error_code=ErrorCode.DEVICE_WARNING, error_msg='! portfast should only be enabled.*"
                ),
                str(record.message),
            )
            for record in caplog.records
        )
