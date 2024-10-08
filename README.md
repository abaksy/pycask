# pycask
A log-structured disk-based key-value store in Python for educational purposes

This is an implementation of the BitCask database described in [this paper](https://riak.com/assets/bitcask-intro.pdf)

## Usage Guide

```python
import bitcask

datastore = bitcask.BitCaskDataStore()
datastore.put("key1", "value1")
print(datastore.get("key1"))s
datastore.close()
```