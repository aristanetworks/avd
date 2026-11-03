# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

from pyavd._errors import AvdFutureBehaviorWarning


def test_future_behavior_warning_is_visible_by_default() -> None:
    """Future-behavior warnings must target end users and remain visible under Python's default warning filters."""
    assert issubclass(AvdFutureBehaviorWarning, FutureWarning)
    assert not issubclass(AvdFutureBehaviorWarning, DeprecationWarning)
