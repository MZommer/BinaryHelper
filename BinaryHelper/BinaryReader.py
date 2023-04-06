from .IO import BaseIO
from . import __types__ as dtypes
from .logger import logger
import struct

class BinaryReader(BaseIO):

    def __init__(self, **kwargs):
        super().__init__(**kwargs, mode="rb")
    def raw(self, size: int):
        return self.read(size)

    def bytes(self, size: int):
        return self.raw(size)

    def auto(self, _dtype: any):
        # TODO: add support for lists and tuples
        value = self.unpack(self._endianess_sign + dtypes.get_type_format(_dtype))
        return value if value else _dtype()

    ### Types ###

    def bool(self):
        return self.auto(dtypes.bool)

    def int8(self):
        return self.auto(dtypes.int8)

    def uint8(self):
        return self.auto(dtypes.uint8)

    def char(self):
        return self.int8()

    def uchar(self):
        return self.uint8()

    def byte(self):
        return self.int8()

    def ubyte(self):
        return self.uint8()

    def int16(self):
        return self.auto(dtypes.int16)

    def uint16(self):
        return self.auto(dtypes.uint16)

    def short(self):
        return self.int16()

    def ushort(self):
        return self.uint16()

    def int32(self):
        return self.auto(dtypes.int32)

    def uint32(self):
        return self.auto(dtypes.uint32)

    def int(self):
        return self.int32()

    def uint(self):
        return self.uint32()

    def long(self):
        return self.int32()

    def ulong(self):
        return self.uint32()

    def int64(self):
        return self.auto(dtypes.int64)

    def uint64(self):
        return self.auto(dtypes.uint64)

    def longlong(self):
        return self.int64()

    def ulonglong(self):
        return self.uint64()

    def float16(self):
        return self.auto(dtypes.float16)

    def half(self):
        return self.float16()

    def float32(self):
        return self.auto(dtypes.float32)

    def float(self):
        return self.float32()

    def single(self):
        return self.float32()

    def float64(self):
        return self.auto(dtypes.float64)

    def double(self):
        return self.float64()

    # TODO: string methods string4-8 size
