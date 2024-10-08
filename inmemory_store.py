from datetime import datetime
import time
import pytz
import struct


class BitCaskKeyDirEntry:
    def __init__(self, valuesize, offset: int) -> None:
        ms = datetime.now()
        self.timestamp = int(time.mktime(ms.timetuple()) * 1000)
        self.valuesize = valuesize
        self.offset = offset


class BitCaskDiskStore:
    def __init__(self, key, value) -> None:
        ms = datetime.now()
        self.timestamp = int(time.mktime(ms.timetuple()) * 1000)
        self.key = str(key)
        self.value = str(value)
        self.keysize = len(key)
        self.valuesize = len(value)

    def encode(self) -> bytes:
        return struct.pack(
            f"<QLL{self.keysize}s{self.valuesize}s",
            self.timestamp,
            self.keysize,
            self.valuesize,
            self.key.encode(),
            self.value.encode(),
        )

    def decode(self, bytedata):
        return struct.unpack_from(f"<QLL{self.keysize}s{self.valuesize}s", bytedata)
