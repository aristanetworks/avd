#!/usr/bin/env python3
from sys import path

path.append(".")

from pyavd.constants import JINJA2_TEMPLATE_PATHS
from pyavd.templater import Templar

templar = Templar()
templar.compile_templates_in_paths(JINJA2_TEMPLATE_PATHS)
