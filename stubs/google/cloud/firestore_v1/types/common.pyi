import proto
from _typeshed import Incomplete
from google.protobuf import timestamp_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class DocumentMask(proto.Message):
    field_paths: MutableSequence[str]

class Precondition(proto.Message):
    exists: bool
    update_time: timestamp_pb2.Timestamp

class TransactionOptions(proto.Message):
    class ReadWrite(proto.Message):
        retry_transaction: bytes
    class ReadOnly(proto.Message):
        read_time: timestamp_pb2.Timestamp
    read_only: ReadOnly
    read_write: ReadWrite
