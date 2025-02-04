import grpc
from .base import FirestoreTransport
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials
from google.cloud.firestore_v1.types import document, document as gf_document, firestore
from google.longrunning import operations_pb2
from google.protobuf import empty_pb2
from typing import Callable, Sequence

__all__ = ['FirestoreGrpcTransport']

class FirestoreGrpcTransport(FirestoreTransport):
    def __init__(self, *, host: str = 'firestore.googleapis.com', credentials: ga_credentials.Credentials | None = None, credentials_file: str | None = None, scopes: Sequence[str] | None = None, channel: grpc.Channel | Callable[..., grpc.Channel] | None = None, api_mtls_endpoint: str | None = None, client_cert_source: Callable[[], tuple[bytes, bytes]] | None = None, ssl_channel_credentials: grpc.ChannelCredentials | None = None, client_cert_source_for_mtls: Callable[[], tuple[bytes, bytes]] | None = None, quota_project_id: str | None = None, client_info: gapic_v1.client_info.ClientInfo = ..., always_use_jwt_access: bool | None = False, api_audience: str | None = None) -> None: ...
    @classmethod
    def create_channel(cls, host: str = 'firestore.googleapis.com', credentials: ga_credentials.Credentials | None = None, credentials_file: str | None = None, scopes: Sequence[str] | None = None, quota_project_id: str | None = None, **kwargs) -> grpc.Channel: ...
    @property
    def grpc_channel(self) -> grpc.Channel: ...
    @property
    def get_document(self) -> Callable[[firestore.GetDocumentRequest], document.Document]: ...
    @property
    def list_documents(self) -> Callable[[firestore.ListDocumentsRequest], firestore.ListDocumentsResponse]: ...
    @property
    def update_document(self) -> Callable[[firestore.UpdateDocumentRequest], gf_document.Document]: ...
    @property
    def delete_document(self) -> Callable[[firestore.DeleteDocumentRequest], empty_pb2.Empty]: ...
    @property
    def batch_get_documents(self) -> Callable[[firestore.BatchGetDocumentsRequest], firestore.BatchGetDocumentsResponse]: ...
    @property
    def begin_transaction(self) -> Callable[[firestore.BeginTransactionRequest], firestore.BeginTransactionResponse]: ...
    @property
    def commit(self) -> Callable[[firestore.CommitRequest], firestore.CommitResponse]: ...
    @property
    def rollback(self) -> Callable[[firestore.RollbackRequest], empty_pb2.Empty]: ...
    @property
    def run_query(self) -> Callable[[firestore.RunQueryRequest], firestore.RunQueryResponse]: ...
    @property
    def run_aggregation_query(self) -> Callable[[firestore.RunAggregationQueryRequest], firestore.RunAggregationQueryResponse]: ...
    @property
    def partition_query(self) -> Callable[[firestore.PartitionQueryRequest], firestore.PartitionQueryResponse]: ...
    @property
    def write(self) -> Callable[[firestore.WriteRequest], firestore.WriteResponse]: ...
    @property
    def listen(self) -> Callable[[firestore.ListenRequest], firestore.ListenResponse]: ...
    @property
    def list_collection_ids(self) -> Callable[[firestore.ListCollectionIdsRequest], firestore.ListCollectionIdsResponse]: ...
    @property
    def batch_write(self) -> Callable[[firestore.BatchWriteRequest], firestore.BatchWriteResponse]: ...
    @property
    def create_document(self) -> Callable[[firestore.CreateDocumentRequest], document.Document]: ...
    def close(self) -> None: ...
    @property
    def delete_operation(self) -> Callable[[operations_pb2.DeleteOperationRequest], None]: ...
    @property
    def cancel_operation(self) -> Callable[[operations_pb2.CancelOperationRequest], None]: ...
    @property
    def get_operation(self) -> Callable[[operations_pb2.GetOperationRequest], operations_pb2.Operation]: ...
    @property
    def list_operations(self) -> Callable[[operations_pb2.ListOperationsRequest], operations_pb2.ListOperationsResponse]: ...
    @property
    def kind(self) -> str: ...
