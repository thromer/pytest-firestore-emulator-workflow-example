import proto
from _typeshed import Incomplete
from google.cloud.firestore_v1.types import aggregation_result, common, document as gf_document, query as gf_query, query_profile, write
from google.protobuf import timestamp_pb2, wrappers_pb2
from google.rpc import status_pb2
from typing import MutableMapping, MutableSequence

__protobuf__: Incomplete

class GetDocumentRequest(proto.Message):
    name: str
    mask: common.DocumentMask
    transaction: bytes
    read_time: timestamp_pb2.Timestamp

class ListDocumentsRequest(proto.Message):
    parent: str
    collection_id: str
    page_size: int
    page_token: str
    order_by: str
    mask: common.DocumentMask
    transaction: bytes
    read_time: timestamp_pb2.Timestamp
    show_missing: bool

class ListDocumentsResponse(proto.Message):
    @property
    def raw_page(self): ...
    documents: MutableSequence[gf_document.Document]
    next_page_token: str

class CreateDocumentRequest(proto.Message):
    parent: str
    collection_id: str
    document_id: str
    document: gf_document.Document
    mask: common.DocumentMask

class UpdateDocumentRequest(proto.Message):
    document: gf_document.Document
    update_mask: common.DocumentMask
    mask: common.DocumentMask
    current_document: common.Precondition

class DeleteDocumentRequest(proto.Message):
    name: str
    current_document: common.Precondition

class BatchGetDocumentsRequest(proto.Message):
    database: str
    documents: MutableSequence[str]
    mask: common.DocumentMask
    transaction: bytes
    new_transaction: common.TransactionOptions
    read_time: timestamp_pb2.Timestamp

class BatchGetDocumentsResponse(proto.Message):
    found: gf_document.Document
    missing: str
    transaction: bytes
    read_time: timestamp_pb2.Timestamp

class BeginTransactionRequest(proto.Message):
    database: str
    options: common.TransactionOptions

class BeginTransactionResponse(proto.Message):
    transaction: bytes

class CommitRequest(proto.Message):
    database: str
    writes: MutableSequence[write.Write]
    transaction: bytes

class CommitResponse(proto.Message):
    write_results: MutableSequence[write.WriteResult]
    commit_time: timestamp_pb2.Timestamp

class RollbackRequest(proto.Message):
    database: str
    transaction: bytes

class RunQueryRequest(proto.Message):
    parent: str
    structured_query: gf_query.StructuredQuery
    transaction: bytes
    new_transaction: common.TransactionOptions
    read_time: timestamp_pb2.Timestamp
    explain_options: query_profile.ExplainOptions

class RunQueryResponse(proto.Message):
    transaction: bytes
    document: gf_document.Document
    read_time: timestamp_pb2.Timestamp
    skipped_results: int
    done: bool
    explain_metrics: query_profile.ExplainMetrics

class RunAggregationQueryRequest(proto.Message):
    parent: str
    structured_aggregation_query: gf_query.StructuredAggregationQuery
    transaction: bytes
    new_transaction: common.TransactionOptions
    read_time: timestamp_pb2.Timestamp
    explain_options: query_profile.ExplainOptions

class RunAggregationQueryResponse(proto.Message):
    result: aggregation_result.AggregationResult
    transaction: bytes
    read_time: timestamp_pb2.Timestamp
    explain_metrics: query_profile.ExplainMetrics

class PartitionQueryRequest(proto.Message):
    parent: str
    structured_query: gf_query.StructuredQuery
    partition_count: int
    page_token: str
    page_size: int
    read_time: timestamp_pb2.Timestamp

class PartitionQueryResponse(proto.Message):
    @property
    def raw_page(self): ...
    partitions: MutableSequence[gf_query.Cursor]
    next_page_token: str

class WriteRequest(proto.Message):
    database: str
    stream_id: str
    writes: MutableSequence[write.Write]
    stream_token: bytes
    labels: MutableMapping[str, str]

class WriteResponse(proto.Message):
    stream_id: str
    stream_token: bytes
    write_results: MutableSequence[write.WriteResult]
    commit_time: timestamp_pb2.Timestamp

class ListenRequest(proto.Message):
    database: str
    add_target: Target
    remove_target: int
    labels: MutableMapping[str, str]

class ListenResponse(proto.Message):
    target_change: TargetChange
    document_change: write.DocumentChange
    document_delete: write.DocumentDelete
    document_remove: write.DocumentRemove
    filter: write.ExistenceFilter

class Target(proto.Message):
    class DocumentsTarget(proto.Message):
        documents: MutableSequence[str]
    class QueryTarget(proto.Message):
        parent: str
        structured_query: gf_query.StructuredQuery
    query: QueryTarget
    documents: DocumentsTarget
    resume_token: bytes
    read_time: timestamp_pb2.Timestamp
    target_id: int
    once: bool
    expected_count: wrappers_pb2.Int32Value

class TargetChange(proto.Message):
    class TargetChangeType(proto.Enum):
        NO_CHANGE: int
        ADD: int
        REMOVE: int
        CURRENT: int
        RESET: int
    target_change_type: TargetChangeType
    target_ids: MutableSequence[int]
    cause: status_pb2.Status
    resume_token: bytes
    read_time: timestamp_pb2.Timestamp

class ListCollectionIdsRequest(proto.Message):
    parent: str
    page_size: int
    page_token: str
    read_time: timestamp_pb2.Timestamp

class ListCollectionIdsResponse(proto.Message):
    @property
    def raw_page(self): ...
    collection_ids: MutableSequence[str]
    next_page_token: str

class BatchWriteRequest(proto.Message):
    database: str
    writes: MutableSequence[write.Write]
    labels: MutableMapping[str, str]

class BatchWriteResponse(proto.Message):
    write_results: MutableSequence[write.WriteResult]
    status: MutableSequence[status_pb2.Status]
