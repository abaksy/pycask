from datetime import datetime, timezone
import time
import struct


class BitCaskKeyDirEntry:
    """
    A single KeyDir entry in the bitcask database
    contains the time of entry, offset in the file and the size of the value in bytes.

    The keydir data structure is composed of entries of the form "key":BitCaskKeyDirEntry
    """
    def __init__(self, valuesize, offset: int) -> None:
        ms = datetime.now(tz=timezone.utc)
        self.timestamp = int(time.mktime(ms.timetuple()) * 1000)
        self.valuesize = valuesize
        self.offset = offset


class BitCaskKVPair:
    """
    Individual key-value entries of the bitcask datastore with methods
    that encode/decode the information into a binary string
    """
    def __init__(self, key, value) -> None:
        ms = datetime.now(tz=timezone.utc)
        self.timestamp = int(time.mktime(ms.timetuple()) * 1000)
        self.key = str(key)
        self.value = str(value)
        self.keysize = len(key)
        self.valuesize = len(value)

    def encode(self) -> bytes:
        """
        Encode the key-value data into a single binary string
        """
        return struct.pack(
            f"<QLL{self.keysize}s{self.valuesize}s",
            self.timestamp,
            self.keysize,
            self.valuesize,
            self.key.encode(),
            self.value.encode(),
        )

    def decode(self, bytedata):
        """
        Decode the byte string into a Python object
        """
        return struct.unpack_from(f"<QLL{self.keysize}s{self.valuesize}s", bytedata)
