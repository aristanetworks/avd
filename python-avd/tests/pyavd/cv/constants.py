# Copyright (c) 2024-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

from pyavd._cv.api.arista.workspace.v1 import ResponseCode, ResponseStatus

MOCKED_EMPTY_CONFIGLET_ID = ""
MOCKED_CONFIGLET_ID = "avd-B51AA89B6E51E89E1422107EDE3A9438"
MOCKED_CONFIGLET_NAME = "TEST_CONFIGLET_NAME"
MOCKED_CONFIGLET_DESCRIPTION = "Configuration created and uploaded by AVD for avd-ci-leaf2"
MOCKED_CONFIGLET_BODY = "alias test test"

MOCKED_MISSING_WORKSPACE_ID = "ws-missing-workspace-id"
MOCKED_WORKSPACE_ID = "ws-cbf7c7ea-a57c-481d-b96b-97c12856395e"
MOCKED_WORKSPACE_NAME = "MOCKED_WS_NAME"
MOCKED_WORKSPACE_DESCRIPTION = "MOCKED_WS_DESCRIPTION"
MOCKED_WORKSPACE_REQUESTED_STATE_SUBMITTED = "submitted"

"""
recorded mocked api Set responses:
  tests/pyavd/cv/mocked_api_recordings/arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/\\
  f4718a9ef72056a50d7666e8d40074fd373b24e6.json
"""
MOCKED_WORKSPACE_REQUEST_ID_BUILD_SUCCESS = {
    "id": "req-914310f3-08dd-4239-bd42-6d78bf781229",
    "status": ResponseStatus.SUCCESS,
    "message": "Build req-914310f3-08dd-4239-bd42-6d78bf781229 finished successfully",
    "code": ResponseCode.UNSPECIFIED,
}

"""
recorded mocked api Set responses:
  tests/pyavd/cv/mocked_api_recordings/arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/\\
  e8a74f4575582e9482183bc24da1060315724a27.json
"""
MOCKED_WORKSPACE_REQUEST_ID_BUILD_FAIL_CONFIG_VALIDATION = {
    "id": "req-914310f3-08dd-4239-bd42-6d78b0000100",
    "status": ResponseStatus.FAIL,
    "message": "device build error",
    "code": ResponseCode.UNSPECIFIED,
}

"""
recorded mocked api Set responses:
  tests/pyavd/cv/mocked_api_recordings/arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/\\
  0934ef194be6eb4e504ec69e407e913131fe2a6c.json
"""
MOCKED_WORKSPACE_REQUEST_ID_BUILD_FAIL = {
    "id": "req-914310f3-08dd-4239-bd42-6d78b0000000",
    "status": ResponseStatus.FAIL,
    "message": "Build req-914310f3-08dd-4239-bd42-6d78b0000000 failed",
    "code": ResponseCode.UNSPECIFIED,
}

"""
recorded mocked api Set responses:
  tests/pyavd/cv/mocked_api_recordings/arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/\\
  3685e73031be59df577e9ff9772e1ca6763879ec.json
"""
MOCKED_WORKSPACE_REQUEST_ID_ABANDON = {
    "id": "req-b65374c1-4333-4c68-9b09-d753e8560609",
    "status": ResponseStatus.SUCCESS,
    "message": "Abandoned",
    "code": ResponseCode.UNSPECIFIED,
}

"""
recorded mocked api arista.workspace.v1.WorkspaceConfigService/Set responses:
  UNFORCED: tests/pyavd/cv/mocked_api_recordings/arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/\\
  c8277b3e8f7e14937563d6323e2e57fe374596b0.json
  FORCED: tests/pyavd/cv/mocked_api_recordings/arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/\\
  b8f80b0453873a911a9ec2c117782e4c82c9929f.json
recorded mocked api arista.workspace.v1.WorkspaceService/Subscribe responses:
  tests/pyavd/cv/mocked_api_recordings/arista.workspace.v1.WorkspaceService/Subscribe/www.cv-prod-us-central1-c.arista.io/\\
  1560c66d73da2be39448d710f15853fb124b2548.json
"""
MOCKED_WORKSPACE_REQUEST_ID_SUBMIT_FAILURE_INACTIVE_DEVICES = {
    "id": "req-18654b6a-9f75-4a57-878d-d40d73701238",
    "status": ResponseStatus.FAIL,
    "message": "some devices are inactive",
    "code": ResponseCode.INACTIVE_DEVICES_EXIST,
}

"""
recorded mocked api arista.workspace.v1.WorkspaceConfigService/Set responses:
  UNFORCED: tests/pyavd/cv/mocked_api_recordings/arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/\\
  3c99caeecf2e9fc98aa476a467933d312b413323.json
  FORCED: tests/pyavd/cv/mocked_api_recordings/arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/\\
  75a436da72f300a8640af1faedca2e2588d62f16.json
recorded mocked api arista.workspace.v1.WorkspaceService/Subscribe responses:
  tests/pyavd/cv/mocked_api_recordings/arista.workspace.v1.WorkspaceService/Subscribe/www.cv-prod-us-central1-c.arista.io/\\
  1560c66d73da2be39448d710f15853fb124b2548.json
"""
MOCKED_WORKSPACE_REQUEST_ID_SUBMIT_FAILURE_OTHER_EXCEPTION = {
    "id": "req-725669d2-2ec5-4572-8c6a-453b1fea27c0",
    "status": ResponseStatus.FAIL,
    "message": "Unknown exception faced",
    "code": ResponseCode.UNSPECIFIED,
}

"""
recorded mocked api arista.workspace.v1.WorkspaceConfigService/Set responses:
  UNFORCED: tests/pyavd/cv/mocked_api_recordings/arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/\\
  dc43e8052333db424deab3d2fc084c4d4109a112.json
  FORCED: tests/pyavd/cv/mocked_api_recordings/arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/\\
  e0ee78aaa706da8a8f08c7db86e58060c082fc7e.json
recorded mocked api arista.workspace.v1.WorkspaceService/Subscribe responses:
  tests/pyavd/cv/mocked_api_recordings/arista.workspace.v1.WorkspaceService/Subscribe/www.cv-prod-us-central1-c.arista.io/\\
  1560c66d73da2be39448d710f15853fb124b2548.json
"""
MOCKED_WORKSPACE_REQUEST_ID_SUBMIT_SUCCESS = {
    "id": "req-b8f4e511-58de-4afe-99f0-b75abf980131",
    "status": ResponseStatus.SUCCESS,
    "message": "Submitted successfully. No change control was created because no config or software changes were created.",
    "code": ResponseCode.UNSPECIFIED,
}

"""Workspace 'B' used to test rebasing of the Workspace."""
MOCKED_WORKSPACE_B_ID = "ws-833a9e6b-9cc0-484b-a5bb-a57f7fa1438f"
MOCKED_WORKSPACE_B_NAME = "MOCKED_REBASE_WS_NAME"
MOCKED_WORKSPACE_B_DESCRIPTION = "MOCKED_REBASE_WS_DESCRIPTION"
MOCKED_WORKSPACE_B_REQUESTED_STATE_SUBMITTED = "submitted"

"""
Successful synchronization/rebase request made when both Workspace.needs_build and Workspace.needs_rebase are False.

recorded mocked api arista.workspace.v1.WorkspaceConfigService/Set response:
  tests/pyavd/cv/mocked_api_recordings/arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/\\
  9c3c1c2a6d572ea4ac06a4d2aef65b9e58d27f2c.json
"""
MOCKED_WORKSPACE_B_REQUEST_ID_REBASE_1_SUCCESS = {
    "id": "req-73d17f5a-3db7-4527-ae9a-e43ca99d983c",
    "status": ResponseStatus.SUCCESS,
    "message": "Workspace is already up to date",
    "code": ResponseCode.UNSPECIFIED,
}
