import grpc
from .base import FirestoreAdminTransport
from google.api_core import gapic_v1, operations_v1
from google.auth import credentials as ga_credentials
from google.cloud.firestore_admin_v1.types import backup, database, field, firestore_admin, index, schedule
from google.longrunning import operations_pb2
from google.protobuf import empty_pb2
from typing import Callable, Sequence

__all__ = ['FirestoreAdminGrpcTransport']

class FirestoreAdminGrpcTransport(FirestoreAdminTransport):
    def __init__(self, *, host: str = 'firestore.googleapis.com', credentials: ga_credentials.Credentials | None = None, credentials_file: str | None = None, scopes: Sequence[str] | None = None, channel: grpc.Channel | Callable[..., grpc.Channel] | None = None, api_mtls_endpoint: str | None = None, client_cert_source: Callable[[], tuple[bytes, bytes]] | None = None, ssl_channel_credentials: grpc.ChannelCredentials | None = None, client_cert_source_for_mtls: Callable[[], tuple[bytes, bytes]] | None = None, quota_project_id: str | None = None, client_info: gapic_v1.client_info.ClientInfo = ..., always_use_jwt_access: bool | None = False, api_audience: str | None = None) -> None: ...
    @classmethod
    def create_channel(cls, host: str = 'firestore.googleapis.com', credentials: ga_credentials.Credentials | None = None, credentials_file: str | None = None, scopes: Sequence[str] | None = None, quota_project_id: str | None = None, **kwargs) -> grpc.Channel: ...
    @property
    def grpc_channel(self) -> grpc.Channel: ...
    @property
    def operations_client(self) -> operations_v1.OperationsClient: ...
    @property
    def create_index(self) -> Callable[[firestore_admin.CreateIndexRequest], operations_pb2.Operation]: ...
    @property
    def list_indexes(self) -> Callable[[firestore_admin.ListIndexesRequest], firestore_admin.ListIndexesResponse]: ...
    @property
    def get_index(self) -> Callable[[firestore_admin.GetIndexRequest], index.Index]: ...
    @property
    def delete_index(self) -> Callable[[firestore_admin.DeleteIndexRequest], empty_pb2.Empty]: ...
    @property
    def get_field(self) -> Callable[[firestore_admin.GetFieldRequest], field.Field]: ...
    @property
    def update_field(self) -> Callable[[firestore_admin.UpdateFieldRequest], operations_pb2.Operation]: ...
    @property
    def list_fields(self) -> Callable[[firestore_admin.ListFieldsRequest], firestore_admin.ListFieldsResponse]: ...
    @property
    def export_documents(self) -> Callable[[firestore_admin.ExportDocumentsRequest], operations_pb2.Operation]: ...
    @property
    def import_documents(self) -> Callable[[firestore_admin.ImportDocumentsRequest], operations_pb2.Operation]: ...
    @property
    def bulk_delete_documents(self) -> Callable[[firestore_admin.BulkDeleteDocumentsRequest], operations_pb2.Operation]: ...
    @property
    def create_database(self) -> Callable[[firestore_admin.CreateDatabaseRequest], operations_pb2.Operation]: ...
    @property
    def get_database(self) -> Callable[[firestore_admin.GetDatabaseRequest], database.Database]: ...
    @property
    def list_databases(self) -> Callable[[firestore_admin.ListDatabasesRequest], firestore_admin.ListDatabasesResponse]: ...
    @property
    def update_database(self) -> Callable[[firestore_admin.UpdateDatabaseRequest], operations_pb2.Operation]: ...
    @property
    def delete_database(self) -> Callable[[firestore_admin.DeleteDatabaseRequest], operations_pb2.Operation]: ...
    @property
    def get_backup(self) -> Callable[[firestore_admin.GetBackupRequest], backup.Backup]: ...
    @property
    def list_backups(self) -> Callable[[firestore_admin.ListBackupsRequest], firestore_admin.ListBackupsResponse]: ...
    @property
    def delete_backup(self) -> Callable[[firestore_admin.DeleteBackupRequest], empty_pb2.Empty]: ...
    @property
    def restore_database(self) -> Callable[[firestore_admin.RestoreDatabaseRequest], operations_pb2.Operation]: ...
    @property
    def create_backup_schedule(self) -> Callable[[firestore_admin.CreateBackupScheduleRequest], schedule.BackupSchedule]: ...
    @property
    def get_backup_schedule(self) -> Callable[[firestore_admin.GetBackupScheduleRequest], schedule.BackupSchedule]: ...
    @property
    def list_backup_schedules(self) -> Callable[[firestore_admin.ListBackupSchedulesRequest], firestore_admin.ListBackupSchedulesResponse]: ...
    @property
    def update_backup_schedule(self) -> Callable[[firestore_admin.UpdateBackupScheduleRequest], schedule.BackupSchedule]: ...
    @property
    def delete_backup_schedule(self) -> Callable[[firestore_admin.DeleteBackupScheduleRequest], empty_pb2.Empty]: ...
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
