import proto
from _typeshed import Incomplete
from google.cloud.firestore_v1.types import document as document_pb2, query as query_pb2
from google.protobuf import timestamp_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class BundledQuery(proto.Message):
    class LimitType(proto.Enum):
        FIRST: int
        LAST: int
    parent: str
    structured_query: query_pb2.StructuredQuery
    limit_type: LimitType

class NamedQuery(proto.Message):
    name: str
    bundled_query: BundledQuery
    read_time: timestamp_pb2.Timestamp

class BundledDocumentMetadata(proto.Message):
    name: str
    read_time: timestamp_pb2.Timestamp
    exists: bool
    queries: MutableSequence[str]

class BundleMetadata(proto.Message):
    id: str
    create_time: timestamp_pb2.Timestamp
    version: int
    total_documents: int
    total_bytes: int

class BundleElement(proto.Message):
    metadata: BundleMetadata
    named_query: NamedQuery
    document_metadata: BundledDocumentMetadata
    document: document_pb2.Document
