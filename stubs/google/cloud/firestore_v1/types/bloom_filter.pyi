import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class BitSequence(proto.Message):
    bitmap: bytes
    padding: int

class BloomFilter(proto.Message):
    bits: BitSequence
    hash_count: int
