# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from typing import TYPE_CHECKING

from pyavd._lazy_import import LazyImports, install_lazy_imports

if TYPE_CHECKING:
    from .avd_catalog_generation_settings import AVDCatalogGenerationSettings as AVDCatalogGenerationSettings
    from .avd_fabric_data import AVDFabricData as AVDFabricData
    from .avd_test_spec import AVDTestSpec as AVDTestSpec

_LAZY_IMPORTS: LazyImports = {
    "AVDCatalogGenerationSettings": ("pyavd.api.anta.avd_catalog_generation_settings", "AVDCatalogGenerationSettings"),
    "AVDFabricData": ("pyavd.api.anta.avd_fabric_data", "AVDFabricData"),
    "AVDTestSpec": ("pyavd.api.anta.avd_test_spec", "AVDTestSpec"),
}

install_lazy_imports(_LAZY_IMPORTS, globals())
