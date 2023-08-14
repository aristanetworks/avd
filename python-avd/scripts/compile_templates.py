#!/usr/bin/env python3
from sys import path

# Override global path to load pyavd from pwd instead of any installed version.
path.insert(0, ".")

from pyavd.constants import JINJA2_TEMPLATE_PATHS
from pyavd.templater import Templar

templar = Templar()
templar.compile_templates_in_paths(JINJA2_TEMPLATE_PATHS)
