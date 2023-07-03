from .get_avd_facts import get_avd_facts
from .get_device_config import get_device_config
from .get_device_doc import get_device_doc
from .get_device_structured_config import get_device_structured_config
from .validate_inputs import validate_inputs
from .vendor.version import VERSION

""" Library for running Arista Validated Designs (AVD) in Python
"""

PYAVD_VERSION = "a3"
AVD_VERSION = VERSION.split("-", maxsplit=1)[0]

if "-dev" in VERSION:
    DEV_VERSION = f"-dev{VERSION.split('-dev')[1]}"
if "-rc" in VERSION:
    DEV_VERSION = f"-dev{VERSION.split('-rc')[1]}"
else:
    DEV_VERSION = ""

__author__ = "Arista Networks"
__copyright__ = "Copyright 2023 Arista Networks"
__license__ = "Apache 2.0"
__version__ = f"{AVD_VERSION}{PYAVD_VERSION}{DEV_VERSION}"

__all__ = [
    "get_avd_facts",
    "get_device_config",
    "get_device_doc",
    "get_device_structured_config",
    "validate_inputs",
]
