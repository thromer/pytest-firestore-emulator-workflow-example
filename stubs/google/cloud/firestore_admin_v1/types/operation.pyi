import proto
from _typeshed import Incomplete
from google.cloud.firestore_admin_v1.types import index as gfa_index
from google.protobuf import timestamp_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class OperationState(proto.Enum):
    OPERATION_STATE_UNSPECIFIED: int
    INITIALIZING: int
    PROCESSING: int
    CANCELLING: int
    FINALIZING: int
    SUCCESSFUL: int
    FAILED: int
    CANCELLED: int

class IndexOperationMetadata(proto.Message):
    start_time: timestamp_pb2.Timestamp
    end_time: timestamp_pb2.Timestamp
    index: str
    state: OperationState
    progress_documents: Progress
    progress_bytes: Progress

class FieldOperationMetadata(proto.Message):
    class IndexConfigDelta(proto.Message):
        class ChangeType(proto.Enum):
            CHANGE_TYPE_UNSPECIFIED: int
            ADD: int
            REMOVE: int
        change_type: FieldOperationMetadata.IndexConfigDelta.ChangeType
        index: gfa_index.Index
    class TtlConfigDelta(proto.Message):
        class ChangeType(proto.Enum):
            CHANGE_TYPE_UNSPECIFIED: int
            ADD: int
            REMOVE: int
        change_type: FieldOperationMetadata.TtlConfigDelta.ChangeType
    start_time: timestamp_pb2.Timestamp
    end_time: timestamp_pb2.Timestamp
    field: str
    index_config_deltas: MutableSequence[IndexConfigDelta]
    state: OperationState
    progress_documents: Progress
    progress_bytes: Progress
    ttl_config_delta: TtlConfigDelta

class ExportDocumentsMetadata(proto.Message):
    start_time: timestamp_pb2.Timestamp
    end_time: timestamp_pb2.Timestamp
    operation_state: OperationState
    progress_documents: Progress
    progress_bytes: Progress
    collection_ids: MutableSequence[str]
    output_uri_prefix: str
    namespace_ids: MutableSequence[str]
    snapshot_time: timestamp_pb2.Timestamp

class ImportDocumentsMetadata(proto.Message):
    start_time: timestamp_pb2.Timestamp
    end_time: timestamp_pb2.Timestamp
    operation_state: OperationState
    progress_documents: Progress
    progress_bytes: Progress
    collection_ids: MutableSequence[str]
    input_uri_prefix: str
    namespace_ids: MutableSequence[str]

class BulkDeleteDocumentsMetadata(proto.Message):
    start_time: timestamp_pb2.Timestamp
    end_time: timestamp_pb2.Timestamp
    operation_state: OperationState
    progress_documents: Progress
    progress_bytes: Progress
    collection_ids: MutableSequence[str]
    namespace_ids: MutableSequence[str]
    snapshot_time: timestamp_pb2.Timestamp

class ExportDocumentsResponse(proto.Message):
    output_uri_prefix: str

class RestoreDatabaseMetadata(proto.Message):
    start_time: timestamp_pb2.Timestamp
    end_time: timestamp_pb2.Timestamp
    operation_state: OperationState
    database: str
    backup: str
    progress_percentage: Progress

class Progress(proto.Message):
    estimated_work: int
    completed_work: int
