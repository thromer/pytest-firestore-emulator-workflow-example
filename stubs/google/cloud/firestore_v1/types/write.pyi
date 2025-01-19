import proto
from _typeshed import Incomplete
from google.cloud.firestore_v1.types import bloom_filter, common, document as gf_document
from google.protobuf import timestamp_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class Write(proto.Message):
    update: gf_document.Document
    delete: str
    transform: DocumentTransform
    update_mask: common.DocumentMask
    update_transforms: MutableSequence['DocumentTransform.FieldTransform']
    current_document: common.Precondition

class DocumentTransform(proto.Message):
    class FieldTransform(proto.Message):
        class ServerValue(proto.Enum):
            SERVER_VALUE_UNSPECIFIED: int
            REQUEST_TIME: int
        field_path: str
        set_to_server_value: DocumentTransform.FieldTransform.ServerValue
        increment: gf_document.Value
        maximum: gf_document.Value
        minimum: gf_document.Value
        append_missing_elements: gf_document.ArrayValue
        remove_all_from_array: gf_document.ArrayValue
    document: str
    field_transforms: MutableSequence[FieldTransform]

class WriteResult(proto.Message):
    update_time: timestamp_pb2.Timestamp
    transform_results: MutableSequence[gf_document.Value]

class DocumentChange(proto.Message):
    document: gf_document.Document
    target_ids: MutableSequence[int]
    removed_target_ids: MutableSequence[int]

class DocumentDelete(proto.Message):
    document: str
    removed_target_ids: MutableSequence[int]
    read_time: timestamp_pb2.Timestamp

class DocumentRemove(proto.Message):
    document: str
    removed_target_ids: MutableSequence[int]
    read_time: timestamp_pb2.Timestamp

class ExistenceFilter(proto.Message):
    target_id: int
    count: int
    unchanged_names: bloom_filter.BloomFilter
