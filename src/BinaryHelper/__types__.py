from numpy import (
    dtype,
    _bool,
    int8, uint8,
    int16, uint16,
    int32, uint32,
    int64, uint64,
    float16, float32, float64, 
    float96, float128, complex64, complex128, complex192, complex256,  # unused
)
from .IO import Endianess

### Aliases ###

byte = int8
ubyte = uint8
uchar = uint8
char = int8
short = int16
ushort = uint16
_int = int32
uint = uint32
long = int32
ulong = uint32
longlong = int64
ulonglong = uint64
half = float16
_float = float32
single = float32
double = float64

### Types utils ###

type_format_table = {
    int8: "b",  uint8: "B",  # byte
    int16: "h", uint16: "H", # short
    int32: "i", uint32: "I", # int
    int64: "q", uint64: "Q", # long long
    float16: "e", # half
    float32: "f", # float
    float64: "d", # double
    _bool: "?",
    bool: "?",
    Endianess.BIG: "<", Endianess.LITTLE: ">",
}

def get_type_format(type: dtype, default: str = "x") -> str:
    """dtype to struct format char"""
    return type_format_table.get(type, default)

def get_sizeof(type: dtype) -> int:
    return type.itemsize