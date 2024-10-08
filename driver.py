# Driver program for bitcask datastore

import bitcask


datastore = bitcask.BitCaskDataStore()

datastore.put("key1", "value1")
print("Wrote data key1 to store")
datastore.put("key2", "value2")
print("Wrote data key2 to store")

print(datastore.get("key1"))
# print("Got data key1 from store")
print(datastore.get("key2"))
# print("Got data key2 from store")

datastore.put("key1", "value3")
print(datastore.get("key1"))

datastore.close()
