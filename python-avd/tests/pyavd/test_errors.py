# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

from pyavd._errors import AvdFutureBehaviorWarning


def test_future_behavior_warning_is_visible_by_default() -> None:
    """Future-behavior warnings must target end users and remain visible under Python's default warning filters."""
    assert issubclass(AvdFutureBehaviorWarning, FutureWarning)
    assert not issubclass(AvdFutureBehaviorWarning, DeprecationWarning)


def test_future_behavior_warning_detailed_message() -> None:
    """The detailed message must include the future version without changing the normal warning message."""
    warning = AvdFutureBehaviorWarning("This configuration is unsupported.", version="7.0.0")

    assert str(warning) == "This configuration is unsupported."
    assert warning.version == "7.0.0"
    assert warning.detailed_message == ("This configuration is unsupported. This configuration is deprecated and will no longer be supported in AVD 7.0.0.")
