# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import sys
import warnings

# Check for broken Python versions with split table dictionary bugs
# See: https://github.com/python/cpython/issues/142218
# See: https://github.com/python/cpython/issues/143189
_BROKEN_PYTHON_VERSIONS = {
    (3, 13, 10),
    (3, 13, 11),
}

if sys.version_info[:3] in _BROKEN_PYTHON_VERSIONS:
    warnings.warn(
        f"Python {sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]} has a critical bug "
        "(CPython gh-143189) affecting split table dictionaries that causes crashes in pyavd. "
        "Please upgrade to Python 3.13.12+ or downgrade to Python 3.13.9 or earlier. "
        "See: https://github.com/python/cpython/issues/143189",
        RuntimeWarning,
        stacklevel=2,
    )

from .get_avd_facts import get_avd_facts
from .get_device_config import get_device_config
from .get_device_doc import get_device_doc
from .get_device_structured_config import get_device_structured_config
from .get_device_test_catalog import get_device_test_catalog
from .get_fabric_documentation import get_fabric_documentation
from .validate_inputs import validate_inputs
from .validate_structured_config import validate_structured_config
from .validation_result import ValidationResult

""" Library for running Arista AVD in Python
"""

PYAVD_PRERELEASE = ""  # Set this to aN or bN for alpha and beta releases of pyavd itself. Empty string when pyavd is released.

__author__ = "Arista Networks"
__copyright__ = "Copyright 2023-2026 Arista Networks"
__license__ = "Apache 2.0"
__version__ = "5.7.3"

__all__ = [
    "ValidationResult",
    "get_avd_facts",
    "get_device_config",
    "get_device_doc",
    "get_device_structured_config",
    "get_device_test_catalog",
    "get_fabric_documentation",
    "validate_inputs",
    "validate_structured_config",
]
