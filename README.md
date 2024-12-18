# pycask
A log-structured disk-based key-value store implemented in Python

This is an implementation of the BitCask database described in [this paper](https://riak.com/assets/bitcask-intro.pdf). 
The implementation is ideally independent of machine and environment considerations. 

## Usage Guide

Gemeric usage: basic functionality for getting and setting key/value pairs is exposed in [bitcask.py](https://github.com/abaksy/pycask/blob/main/bitcask.py)

```python
import bitcask

datastore = bitcask.BitCaskDataStore()
datastore.put("key1", "value1")
print(datastore.get("key1"))s
datastore.close()
```

### Benchmark Tests

[driver.py](https://github.com/abaksy/pycask/blob/main/driver.py) runs some benchmark tests for key access times for different database sizes (ranging from 10 entries to 1mn entries)

## How bitcask works
