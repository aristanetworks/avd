# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

from types import SimpleNamespace
from unittest.mock import MagicMock

from pyavd._eos_designs.schema import EosDesigns
from pyavd._eos_designs.structured_config.connected_endpoints.utils import UtilsMixin


def test_get_adapter_dot1x_with_ipv4_standard_acl() -> None:
    adapter_type = EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem.AdaptersItem
    adapter = adapter_type(
        dot1x=adapter_type.Dot1x(
            authentication_failure=adapter_type.Dot1x.AuthenticationFailure(action="allow", allow_ipv4_access_list="ACL1"),
        ),
    )
    structured_config_utils = MagicMock()
    structured_config_generator = SimpleNamespace(
        inputs=SimpleNamespace(dot1x_settings=SimpleNamespace(enabled=True)),
        structured_config_utils=structured_config_utils,
    )

    dot1x = UtilsMixin._get_adapter_dot1x(structured_config_generator, adapter)  # type: ignore[arg-type]

    assert dot1x.authentication_failure.allow_access_list == "ACL1"
    structured_config_utils._set_ipv4_standard_acl.assert_called_once_with("ACL1")
