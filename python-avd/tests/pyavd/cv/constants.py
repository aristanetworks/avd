# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

from pyavd._cv.api.arista.workspace.v1 import ResponseCode, ResponseStatus

MOCKED_WORKSPACE_ID = "ws-cbf7c7ea-a57c-481d-b96b-97c12856395e"
MOCKED_WORKSPACE_NAME = "MOCKED_WS_NAME"
MOCKED_WORKSPACE_DESCRIPTION = "MOCKED_WS_DESCRIPTION"
MOCKED_WORKSPACE_REQUESTED_STATE_SUBMITTED = "submitted"

"""
recorded mocked api Set responses:
  tests/pyavd/cv/mocked_api_recordings/arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/\\
  1fdd6fcd02728621447eeb8a1d8c9cbfdd9201c9.json
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
  094fa72d5437063770b645129730633334c7e4ed.json
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
  c3455eeb927146c3ba4e5fbb3d51b959fc84da17.json
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
  54f25797c08b0d4ca2c4497e73b4afbfd2959b6f.json
  FORCED: tests/pyavd/cv/mocked_api_recordings/arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/\\
  a081b80838db991bd8bcd669f64f7aa24c00b715.json
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
  0bc6d413bab676fd90504b4ba0d2a81d8fa54e03.json
  FORCED: tests/pyavd/cv/mocked_api_recordings/arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/\\
  a8201f6621fc75b37306a45e91ecf1db776ac617.json
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
  ba83e98eab07691e8b079958618ab2973822bfe8.json
  FORCED: tests/pyavd/cv/mocked_api_recordings/arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/\\
  47049c8a6b520f110540f81bcd892ba0e4954908.json
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
