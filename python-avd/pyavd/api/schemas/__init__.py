# Copyright (c) 2025-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from typing import TYPE_CHECKING, Any

from pyavd._lazy_import import LazyImports, get_lazy_attr, get_lazy_dir

if TYPE_CHECKING:
    from pyavd._cv.schema import CvDeploy as CVDeploy
    from pyavd._eos_cli_config_gen.schema import EosCliConfigGen as EOSConfig
    from pyavd._eos_designs.schema import EosDesigns as AVDDesign

__all__ = ["AVDDesign", "CVDeploy", "EOSConfig"]

_LAZY_IMPORTS: LazyImports = {
    "AVDDesign": ("pyavd._eos_designs.schema", "EosDesigns"),
    "CVDeploy": ("pyavd._cv.schema", "CvDeploy"),
    "EOSConfig": ("pyavd._eos_cli_config_gen.schema", "EosCliConfigGen"),
}


def __getattr__(name: str) -> Any:
    return get_lazy_attr(name, _LAZY_IMPORTS, globals())


def __dir__() -> list[str]:
    return get_lazy_dir(_LAZY_IMPORTS, globals())
