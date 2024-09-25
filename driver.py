# Driver program for bitcask datastore

import bitcask


datastore = bitcask.BitCaskDataStore()

datastore.put("key1", "value1")
datastore.put("key2", "value2")

datastore.get("key1")

datastore.put("key1", "value3")
datastore.get("key1")
