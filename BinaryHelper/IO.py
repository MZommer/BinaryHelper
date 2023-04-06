from io import BytesIO
from enum import Enum
import struct


class Endianess(Enum):
    BIG: str = "BIG"
    LITTLE: str = "LITTLE"


class BaseIO:
    _buffer: BytesIO
    _endianess: Endianess
    _endianess_sign: str
    sizeOf: int

    def __init__(self, path=None, mode: str = None, encoding: str = "ASCII", buffer: BytesIO = None,
                 endianess: Endianess = Endianess.BIG) -> None:
        # Endianess
        self.set_endianess(endianess)
        self._endianess_sign = "<" if self._endianess == Endianess.BIG else ">"

        # Open syntax
        if path and mode:
            self._buffer = open(path, mode=mode)

        # Buffer (BytesIO)
        if buffer:
            self._buffer = buffer

    ### Endianess ###

    def flip_endianess(self) -> None:
        if self._endianess == Endianess.BIG:
            self._endianess = Endianess.LITTLE
        else:
            self._endianess = Endianess.BIG

    def set_endianess(self, endianess: Endianess = None):
        if not endianess:
            return self.flip_endianess()
        if isinstance(endianess, str):
            self._endianess = Endianess(endianess.upper())
        else:
            self._endianess = endianess

    ### Struct methods ###

    def pack(self, fmt: str, *args) -> bytes:
        return struct.pack(fmt, *args)

    def pack_into(self, fmt: str, *args) -> None:
        return struct.pack_into(fmt, self._buffer, *args)

    @staticmethod
    def unpack(fmt: str, *args) -> bytes:
        return struct.unpack(fmt, *args)[0]

    def unpack_into(self, fmt: str) -> None:
        return struct.unpack_from(fmt, self._buffer, self._buffer.tell())[0]

    ### Flush and close ###

    def close(self, exc_type, exc_val, exc_tb) -> None:
        """
        Close the file.
        A closed file cannot be used for further I/O operations.  close() may be
        called more than once without error.
        """
        self._buffer.close(exc_type, exc_val, exc_tb)

    def flush(self) -> None:
        """Flush the write buffers of the stream if applicable. This does nothing for read-only and non-blocking streams."""
        return self._buffer.flush()

    ### Positioning ###

    def seek(self, offset: int, whence: int = 0) -> None:
        """
        Change stream position.
        Change the stream position to byte offset pos. Argument pos is
        interpreted relative to the position indicated by whence.  Values
        for whence are ints:
        * 0 -- start of stream (the default); offset should be zero or positive
        * 1 -- current stream position; offset may be negative
        * 2 -- end of stream; offset is usually negative
        Some operating systems / file systems could provide additional values.
        Return an int indicating the new absolute position.
        """
        return self._buffer.seek(offset, whence)

    def tell(self) -> int:
        """Return an int indicating the current stream position."""
        return self._buffer.tell()

    ### Inquiries ###

    def seekable(self) -> bool:
        """
        Return a bool indicating whether object supports random access.
        If False, seek(), tell() and truncate() will raise OSError.
        This method may need to do a test seek().
        """
        return self._buffer.seekable()

    def readable(self) -> bool:
        """
        Return a bool indicating whether object was opened for reading.
        If False, read() will raise OSError.
        """
        return self._buffer.readable()

    def writable(self) -> bool:
        """
        Return a bool indicating whether object was opened for writing.
        If False, write() and truncate() will raise OSError.
        """
        return self._buffer.writable()

    @property
    def closed(self) -> bool:
        """True if the stream is closed."""
        return self._buffer.closed

        ### Context manager ###

    def __enter__(self):
        """Context management protocol.  Returns self (an instance of IOBase)."""
        self._checkClosed()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Context management protocol.  Calls close()"""
        self.close(exc_type, exc_val, exc_tb)

    def isatty(self) -> bool:
        """
        Return a bool indicating whether this is an 'interactive' stream.
        Return False if it can't be determined.
        """
        return self._buffer.isatty()

    ### Read[s] and Write[s] ###

    def read(self, size: int = -1) -> bytes or str:
        """
        Read up to size bytes from the object and return them.
        As a convenience, if size is unspecified or -1,
        all bytes until EOF are returned.
        Otherwise, only one system call is ever made.
        Fewer than size bytes may be returned
        if the operating system call returns fewer than size bytes.
        
        If 0 bytes are returned, and size was not 0,
        this indicates end of file.
        If the object is in non-blocking mode
        and no bytes are available, None is returned.
        """
        return self._buffer.read(size)

    def readline(self, size: int = -1) -> str:
        """
        Read until newline or EOF.
        Returns an empty string if EOF is hit immediately.
        """
        return self._buffer.readline(size)

    def readlines(self, hint: int = -1) -> list[str]:
        """
        Return a list of lines from the stream.
        hint can be specified to control the number of lines read: no more
        lines will be read if the total size (in bytes/characters) of all
        lines so far exceeds hint.
        """
        return self._buffer.readlines(hint)

    def write(self, data: bytes or str) -> None:
        """
        Write the given data,
        and return the number of bytes written
        (always equal to the length of b in bytes, since if the write fails an OSError will be raised).
        """
        return self._buffer.write(data)
