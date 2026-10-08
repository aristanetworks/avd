# Copyright (c) 2025-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from typing import TYPE_CHECKING

from pyavd._lazy_import import LazyImports, install_lazy_imports

if TYPE_CHECKING:
    from pyavd._cv.schema import CvDeploy as CVDeploy  # noqa: F401
    from pyavd._eos_cli_config_gen.schema import EosCliConfigGen as EOSConfig  # noqa: F401
    from pyavd._eos_designs.schema import EosDesigns as AVDDesign  # noqa: F401

_LAZY_IMPORTS: LazyImports = {
    "AVDDesign": ("pyavd._eos_designs.schema", "EosDesigns"),
    "CVDeploy": ("pyavd._cv.schema", "CvDeploy"),
    "EOSConfig": ("pyavd._eos_cli_config_gen.schema", "EosCliConfigGen"),
}

install_lazy_imports(_LAZY_IMPORTS, globals())
