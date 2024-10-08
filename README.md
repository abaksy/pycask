# pycask
A log-structured disk-based key-value store in Python for educational purposes

This is an implementation of the BitCask database described in [this paper](https://riak.com/assets/bitcask-intro.pdf)

## Usage Guide

Run ```driver.py``` to run some basic benchmarks on time needed to retrieve keys from a database of N entries (N ranging from 10 to 10000)

```python
import bitcask

datastore = bitcask.BitCaskDataStore()
datastore.put("key1", "value1")
print(datastore.get("key1"))s
datastore.close()
```


## TODO
- implement multi file scheme as described in the original paper
- implement merge operation as described post the above