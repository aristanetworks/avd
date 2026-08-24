# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from typing import TYPE_CHECKING

from ._lazy_import import LazyImports, install_lazy_imports

if TYPE_CHECKING:
    from .api.eos_cli_config_gen import ConfigRenderConfiguration as ConfigRenderConfiguration
    from .api.eos_cli_config_gen import DocRenderConfiguration as DocRenderConfiguration
    from .api.eos_cli_config_gen import RenderConfiguration as RenderConfiguration
    from .get_avd_facts import get_avd_facts as get_avd_facts
    from .get_device_config import get_device_config as get_device_config
    from .get_device_doc import get_device_doc as get_device_doc
    from .get_device_structured_config import get_device_structured_config as get_device_structured_config
    from .get_device_test_catalog import get_device_test_catalog as get_device_test_catalog
    from .get_fabric_documentation import get_fabric_documentation as get_fabric_documentation
    from .validate_inputs import validate_inputs as validate_inputs
    from .validate_structured_config import validate_structured_config as validate_structured_config

""" Library for running Arista AVD in Python
"""

PYAVD_PRERELEASE = ""  # Set this to aN or bN for alpha and beta releases of pyavd itself. Empty string when pyavd is released.

__author__ = "Arista Networks"
__copyright__ = "Copyright 2023-2026 Arista Networks"
__license__ = "Apache 2.0"
__version__ = "6.4.0.dev1"

_LAZY_IMPORTS: LazyImports = {
    "ConfigRenderConfiguration": ("pyavd.api.eos_cli_config_gen", "ConfigRenderConfiguration"),
    "DocRenderConfiguration": ("pyavd.api.eos_cli_config_gen", "DocRenderConfiguration"),
    "RenderConfiguration": ("pyavd.api.eos_cli_config_gen", "RenderConfiguration"),
    "get_avd_facts": ("pyavd.get_avd_facts", "get_avd_facts"),
    "get_device_config": ("pyavd.get_device_config", "get_device_config"),
    "get_device_doc": ("pyavd.get_device_doc", "get_device_doc"),
    "get_device_structured_config": ("pyavd.get_device_structured_config", "get_device_structured_config"),
    "get_device_test_catalog": ("pyavd.get_device_test_catalog", "get_device_test_catalog"),
    "get_fabric_documentation": ("pyavd.get_fabric_documentation", "get_fabric_documentation"),
    "validate_inputs": ("pyavd.validate_inputs", "validate_inputs"),
    "validate_structured_config": ("pyavd.validate_structured_config", "validate_structured_config"),
}

install_lazy_imports(_LAZY_IMPORTS, globals())
