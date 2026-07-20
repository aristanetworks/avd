# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from re import escape
from typing import Any

import pytest
from jinja2.runtime import Undefined

from pyavd._errors import AristaAvdInvalidInputsError
from pyavd.j2filters._mandatory import _mandatory


def test_mandatory_returns_defined_value() -> None:
    assert _mandatory("value", "custom error") == "value"


@pytest.mark.parametrize("value", [Undefined(name="a_non_existing_var"), None])
def test_mandatory_raises_custom_message(value: Any) -> None:
    with pytest.raises(AristaAvdInvalidInputsError, match=escape("The number of ACL entries is above defined maximum!")):
        _mandatory(value, "The number of ACL entries is above defined maximum!")


def test_mandatory_raises_default_message() -> None:
    with pytest.raises(AristaAvdInvalidInputsError, match=escape("Mandatory variable is not defined.")):
        _mandatory(Undefined(name="a_non_existing_var"))
