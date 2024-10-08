from inmemory_store import BitCaskKeyDirEntry, BitCaskDiskStore
import os
from typing import Dict
import struct


class BitCaskDataStore:
    def __init__(self, datafile_name="database.db") -> None:
        self.datafile = datafile_name
        self.file_handle =  open(self.datafile, "a+b")
        self.keydir: Dict[str, BitCaskKeyDirEntry] = dict()

    def get(self, key):
        # Get the offset information from the keydir
        # Use the offset info to read the key and the value from the data file
        if key not in self.keydir:
            return ""
        offset_info = self.keydir[key]
        file_offset = offset_info.offset
        with open(self.datafile, 'rb') as f:
            f.seek(file_offset)
            byte_data = f.read(16)
            timestamp, keysize, valuesize = struct.unpack("<QLL", byte_data)
            _ = f.read(keysize)
            value_bytes = f.read(valuesize)
        return value_bytes.decode()

    def put(self, key, value):
        # Insert a key-value pair into the bitcask database
        # First, insert the key-value into the in-memory keydir
        valsize = len(value)

        offset = os.path.getsize(self.datafile)
        kdEntry = BitCaskKeyDirEntry(valsize, offset)
        self.keydir[key] = kdEntry

        # Append the key-value to the disk store now
        diskstore = BitCaskDiskStore(key, value)
        byte_data = diskstore.encode()
        with open(self.datafile, "ab") as f:
            f.write(byte_data)

    def list_keys(self):
        return list(self.keydir.keys())

    def merge(self):
        pass

    def sync(self):
        pass

    def close(self):
        self.file_handle.flush()
        os.fsync(self.file_handle)
        self.file_handle.close()
