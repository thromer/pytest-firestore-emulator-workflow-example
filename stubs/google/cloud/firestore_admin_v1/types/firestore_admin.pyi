import proto
from _typeshed import Incomplete
from google.cloud.firestore_admin_v1.types import backup as gfa_backup, database as gfa_database, field as gfa_field, index as gfa_index, schedule
from google.protobuf import field_mask_pb2, timestamp_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class ListDatabasesRequest(proto.Message):
    parent: str
    show_deleted: bool

class CreateDatabaseRequest(proto.Message):
    parent: str
    database: gfa_database.Database
    database_id: str

class CreateDatabaseMetadata(proto.Message): ...

class ListDatabasesResponse(proto.Message):
    databases: MutableSequence[gfa_database.Database]
    unreachable: MutableSequence[str]

class GetDatabaseRequest(proto.Message):
    name: str

class UpdateDatabaseRequest(proto.Message):
    database: gfa_database.Database
    update_mask: field_mask_pb2.FieldMask

class UpdateDatabaseMetadata(proto.Message): ...

class DeleteDatabaseRequest(proto.Message):
    name: str
    etag: str

class DeleteDatabaseMetadata(proto.Message): ...

class CreateBackupScheduleRequest(proto.Message):
    parent: str
    backup_schedule: schedule.BackupSchedule

class GetBackupScheduleRequest(proto.Message):
    name: str

class UpdateBackupScheduleRequest(proto.Message):
    backup_schedule: schedule.BackupSchedule
    update_mask: field_mask_pb2.FieldMask

class ListBackupSchedulesRequest(proto.Message):
    parent: str

class ListBackupSchedulesResponse(proto.Message):
    backup_schedules: MutableSequence[schedule.BackupSchedule]

class DeleteBackupScheduleRequest(proto.Message):
    name: str

class CreateIndexRequest(proto.Message):
    parent: str
    index: gfa_index.Index

class ListIndexesRequest(proto.Message):
    parent: str
    filter: str
    page_size: int
    page_token: str

class ListIndexesResponse(proto.Message):
    @property
    def raw_page(self): ...
    indexes: MutableSequence[gfa_index.Index]
    next_page_token: str

class GetIndexRequest(proto.Message):
    name: str

class DeleteIndexRequest(proto.Message):
    name: str

class UpdateFieldRequest(proto.Message):
    field: gfa_field.Field
    update_mask: field_mask_pb2.FieldMask

class GetFieldRequest(proto.Message):
    name: str

class ListFieldsRequest(proto.Message):
    parent: str
    filter: str
    page_size: int
    page_token: str

class ListFieldsResponse(proto.Message):
    @property
    def raw_page(self): ...
    fields: MutableSequence[gfa_field.Field]
    next_page_token: str

class ExportDocumentsRequest(proto.Message):
    name: str
    collection_ids: MutableSequence[str]
    output_uri_prefix: str
    namespace_ids: MutableSequence[str]
    snapshot_time: timestamp_pb2.Timestamp

class ImportDocumentsRequest(proto.Message):
    name: str
    collection_ids: MutableSequence[str]
    input_uri_prefix: str
    namespace_ids: MutableSequence[str]

class BulkDeleteDocumentsRequest(proto.Message):
    name: str
    collection_ids: MutableSequence[str]
    namespace_ids: MutableSequence[str]

class BulkDeleteDocumentsResponse(proto.Message): ...

class GetBackupRequest(proto.Message):
    name: str

class ListBackupsRequest(proto.Message):
    parent: str

class ListBackupsResponse(proto.Message):
    backups: MutableSequence[gfa_backup.Backup]
    unreachable: MutableSequence[str]

class DeleteBackupRequest(proto.Message):
    name: str

class RestoreDatabaseRequest(proto.Message):
    parent: str
    database_id: str
    backup: str
    encryption_config: gfa_database.Database.EncryptionConfig
