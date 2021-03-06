import idaapi
import idc

import hashlib

from .vector import Vector


class NameHashVector(Vector):
  type = 'name_hash'
  type_version = 0

  def include(self):
    name = idc.Name(self.offset)
    return not idaapi.is_uname(name)

  def _data(self):
    md5 = hashlib.md5()
    md5.update(idc.Name(self.offset))
    return md5.hexdigest()
