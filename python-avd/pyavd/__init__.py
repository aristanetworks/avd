# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from .get_avd_facts import get_avd_facts
from .get_device_config import get_device_config
from .get_device_doc import get_device_doc
from .get_device_structured_config import get_device_structured_config
from .validate_inputs import validate_inputs
from .validate_structured_config import validate_structured_config
from .validation_result import ValidationResult

""" Library for running Arista Validated Designs (AVD) in Python
"""

PYAVD_PRERELEASE = ""  # Set this to aN or bN for alpha and beta releases of pyavd itself. Empty string when pyavd is released.

__author__ = "Arista Networks"
__copyright__ = "Copyright 2023-2024 Arista Networks"
__license__ = "Apache 2.0"
__version__ = "5.0.0.dev4"

__all__ = [
    "get_avd_facts",
    "get_device_config",
    "get_device_doc",
    "get_device_structured_config",
    "validate_inputs",
    "validate_structured_config",
    "ValidationResult",
]
