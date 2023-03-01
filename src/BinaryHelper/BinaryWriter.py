from .IO import BaseIO
from .__types__ import *
from .logger import logger

class BinaryWriter(BaseIO):

    
    def raw(self, value: bytes):
        self.sizeOf += len(value)
        return self.write(value)
    
    def bytes(self, value: bytes):
        return self.raw(value)
    
    def auto(self, value: any):
        # TODO: add support for lists and tuples
        self.sizeOf += get_sizeof(value)
        return self.pack_into(self._endianess_sign + get_type_format(type(value)), value)
    
    ### Types ###
    
    def bool(self, value: bool):
        if not isinstance(value, bool):
            value = bool(value)
        return self.auto(value)
    
    def int8(self, value: int8):
        if not isinstance(value, int8):
            logger.warning(f"Casting {type(value).__name__} into an int8, risk of a data loss")
            value = int8(value)
        return self.auto(value)
    
    def uint8(self, value: uint8):
        if not isinstance(value, uint8):
            logger.warning(f"Casting {type(value).__name__} into an uint8, risk of a data loss")
            value = uint8(value)
        return self.auto(value)
    
    def char(self, value: int8):
        return self.int8(value)
    
    def uchar(self, value: uint8):
        return self.uint8(value)
    
    def byte(self, value: int8):
        return self.int8(value)
    
    def ubyte(self, value: uint8):
        return self.uint8(value)

    def int16(self, value: int16):
        if not isinstance(value, int16):
            logger.warning(f"Casting {type(value).__name__} into an int16, risk of a data loss")
            value = int16(value)
        return self.auto(value)

    def uint16(self, value: uint16):
        if not isinstance(value, uint16):
            logger.warning(f"Casting {type(value).__name__} into an uint16, risk of a data loss")
            value = uint16(value)
        return self.auto(value)
    
    def short(self, value: int16):
        return self.int16(value)
    
    def ushort(self, value: uint16):
        return self.uint16(value)

    def int32(self, value: int32):
        if not isinstance(value, int32):
            logger.warning(f"Casting {type(value).__name__} into an int32, risk of a data loss")
            value = int32(value)
        return self.auto(value)

    def uint32(self, value: uint32):
        if not isinstance(value, uint32):
            logger.warning(f"Casting {type(value).__name__} into an uint32, risk of a data loss")
            value = uint32(value)
        return self.auto(value)

    def int(self, value: int32):
        return self.int32(value)
    
    def uint(self, value: uint32):
        return self.uint32(value)
    
    def long(self, value: int32):
        return self.int32(value)
    
    def ulong(self, value: uint32):
        return self.uint32(value)

    def int64(self, value: int64):
        if not isinstance(value, int64):
            logger.warning(f"Casting {type(value).__name__} into an int64, risk of a data loss")
            value = int64(value)
        return self.auto(value)

    def uint64(self, value: uint64):
        if not isinstance(value, uint64):
            logger.warning(f"Casting {type(value).__name__} into an uint64, risk of a data loss")
            value = uint64(value)
        return self.auto(value)
    
    def longlong(self, value: int64):
        return self.int64(value)
    
    def ulonglong(self, value: uint64):
        return self.uint64(value)

    def float16(self, value: float16):
        if not isinstance(value, float16):
            logger.warning(f"Casting {type(value).__name__} into a float16, risk of a data loss")
            value = float16(value)
        return self.auto(value)
    
    def half(self, value: float16):
        return self.float16(value)
    
    def float32(self, value: float32):
        if not isinstance(value, float32):
            if not isinstance(value, float):
                logger.warning(f"Casting {type(value).__name__} into a float32, risk of a data loss")
            value = float32(value)
        return self.auto(value)
    
    def float(self, value: float32):
        return self.float32(value)
    
    def single(self, value: float32):
        return self.float32(value)
    
    def float64(self, value: float64):
        if not isinstance(value, float64):
            if not isinstance(value, float):
                logger.warning(f"Casting {type(value).__name__} into a float64, risk of a data loss")
            value = float64(value)
        return self.auto(value)

    def double(self, value: float64):
        return self.float64(value)

    # TODO: string methods string4-8 size