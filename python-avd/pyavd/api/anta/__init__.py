# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from typing import TYPE_CHECKING, Any

from pyavd._lazy_import import LazyImports, get_lazy_attr, get_lazy_dir

if TYPE_CHECKING:
    from .avd_catalog_generation_settings import AVDCatalogGenerationSettings
    from .avd_fabric_data import AVDFabricData
    from .avd_test_spec import AVDTestSpec

__all__ = ["AVDCatalogGenerationSettings", "AVDFabricData", "AVDTestSpec"]

_LAZY_IMPORTS: LazyImports = {
    "AVDCatalogGenerationSettings": ("pyavd.api.anta.avd_catalog_generation_settings", "AVDCatalogGenerationSettings"),
    "AVDFabricData": ("pyavd.api.anta.avd_fabric_data", "AVDFabricData"),
    "AVDTestSpec": ("pyavd.api.anta.avd_test_spec", "AVDTestSpec"),
}


def __getattr__(name: str) -> Any:
    return get_lazy_attr(name, _LAZY_IMPORTS, globals())


def __dir__() -> list[str]:
    return get_lazy_dir(_LAZY_IMPORTS, globals())
