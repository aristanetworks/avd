#
# natural_sort filter
#
from jinja2 import TemplateError

import re

class FilterModule(object):

  def natural_sort(self,iterable):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', str(key)) ]
    return sorted(iterable, key = alphanum_key)

  def filters(self):
    return {
      'natural_sort' : self.natural_sort,
    }
