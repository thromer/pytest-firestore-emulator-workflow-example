import proto
from _typeshed import Incomplete
from google.protobuf import struct_pb2, timestamp_pb2
from google.type import latlng_pb2
from typing import MutableMapping, MutableSequence

__protobuf__: Incomplete

class Document(proto.Message):
    name: str
    fields: MutableMapping[str, 'Value']
    create_time: timestamp_pb2.Timestamp
    update_time: timestamp_pb2.Timestamp

class Value(proto.Message):
    null_value: struct_pb2.NullValue
    boolean_value: bool
    integer_value: int
    double_value: float
    timestamp_value: timestamp_pb2.Timestamp
    string_value: str
    bytes_value: bytes
    reference_value: str
    geo_point_value: latlng_pb2.LatLng
    array_value: ArrayValue
    map_value: MapValue

class ArrayValue(proto.Message):
    values: MutableSequence['Value']

class MapValue(proto.Message):
    fields: MutableMapping[str, 'Value']
