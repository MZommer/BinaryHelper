from . import __types__ as dtypes
from .IO import BaseIO
from .logger import logger


class BinaryWriter(BaseIO):

    def raw(self, value: bytes):
        self.sizeOf += len(value)
        return self.write(value)

    def bytes(self, value: bytes):
        return self.raw(value)

    def auto(self, value: any):
        # TODO: add support for lists and tuples
        self.sizeOf += dtypes.get_sizeof(value)
        return self.pack_into(self._endianess_sign + dtypes.get_type_format(type(value)), value)

    ### Types ###
    def bool(self, value: bool | int):
        if not isinstance(value, bool):
            value = bool(value)
        return self.auto(value)

    def char(self, value: dtypes.int8 | int):
        return self.int8(value)

    def uchar(self, value: dtypes.uint8 | int):
        return self.uint8(value)

    def byte(self, value: dtypes.int8 | int):
        return self.int8(value)

    def ubyte(self, value: dtypes.uint8 | int):
        return self.uint8(value)

    def int8(self, value: dtypes.int8 | int):
        if not isinstance(value, dtypes.int8):
            logger.warning(f"Casting {type(value).__name__} into an int8, risk of a data loss")
            value = dtypes.int8(value)
        return self.auto(value)

    def uint8(self, value: dtypes.uint8 | int):
        if not isinstance(value, dtypes.uint8):
            logger.warning(f"Casting {type(value).__name__} into an uint8, risk of a data loss")
            value = dtypes.uint8(value)
        return self.auto(value)

    def short(self, value: dtypes.int16 | int):
        return self.int16(value)

    def ushort(self, value: dtypes.uint16 | int):
        return self.uint16(value)

    def int16(self, value: dtypes.int16 | int):
        if not isinstance(value, dtypes.int16):
            logger.warning(f"Casting {type(value).__name__} into an int16, risk of a data loss")
            value = dtypes.int16(value)
        return self.auto(value)

    def uint16(self, value: dtypes.uint16 | int):
        if not isinstance(value, dtypes.uint16):
            logger.warning(f"Casting {type(value).__name__} into an uint16, risk of a data loss")
            value = dtypes.uint16(value)
        return self.auto(value)

    def long(self, value: dtypes.int32 | int):
        return self.int32(value)

    def ulong(self, value: dtypes.uint32 | int):
        return self.uint32(value)

    def int32(self, value: dtypes.int32 | int):
        if not isinstance(value, dtypes.int32):
            logger.warning(f"Casting {type(value).__name__} into an int32, risk of a data loss")
            value = dtypes.int32(value)
        return self.auto(value)

    def uint32(self, value: dtypes.uint32 | int):
        if not isinstance(value, dtypes.uint32):
            logger.warning(f"Casting {type(value).__name__} into an uint32, risk of a data loss")
            value = dtypes.uint32(value)
        return self.auto(value)

    def longlong(self, value: dtypes.int64 | int):
        return self.int64(value)

    def ulonglong(self, value: dtypes.uint64 | int):
        return self.uint64(value)

    def int64(self, value: dtypes.int64 | int):
        if not isinstance(value, dtypes.int64):
            logger.warning(f"Casting {type(value).__name__} into an int64, risk of a data loss")
            value = dtypes.int64(value)
        return self.auto(value)

    def uint64(self, value: dtypes.uint64 | int):
        if not isinstance(value, dtypes.uint64):
            logger.warning(f"Casting {type(value).__name__} into an uint64, risk of a data loss")
            value = dtypes.uint64(value)
        return self.auto(value)

    def half(self, value: dtypes.float16 | float | int):
        return self.float16(value)

    def float16(self, value: dtypes.float16 | float | int):
        if not isinstance(value, dtypes.float16):
            logger.warning(f"Casting {type(value).__name__} into a float16, risk of a data loss")
            value = dtypes.float16(value)
        return self.auto(value)

    def single(self, value: dtypes.float32 | float | int):
        return self.float32(value)

    def float32(self, value: dtypes.float32 | float | int):
        if not isinstance(value, dtypes.float32):
            if not isinstance(value, float):
                logger.warning(f"Casting {type(value).__name__} into a float32, risk of a data loss")
            value = dtypes.float32(value)
        return self.auto(value)

    def double(self, value: dtypes.float64 | float | int):
        return self.float64(value)

    def float64(self, value: dtypes.float64 | float | int):
        if not isinstance(value, dtypes.float64):
            if not isinstance(value, float):
                logger.warning(f"Casting {type(value).__name__} into a float64, risk of a data loss")
            value = dtypes.float64(value)
        return self.auto(value)

    def float(self, value: dtypes.float32 | float | int):
        return self.float32(value)

    # TODO: string methods string4-8 size
