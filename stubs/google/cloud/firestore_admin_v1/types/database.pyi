import proto
from _typeshed import Incomplete
from google.protobuf import duration_pb2, timestamp_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class Database(proto.Message):
    class DatabaseType(proto.Enum):
        DATABASE_TYPE_UNSPECIFIED: int
        FIRESTORE_NATIVE: int
        DATASTORE_MODE: int
    class ConcurrencyMode(proto.Enum):
        CONCURRENCY_MODE_UNSPECIFIED: int
        OPTIMISTIC: int
        PESSIMISTIC: int
        OPTIMISTIC_WITH_ENTITY_GROUPS: int
    class PointInTimeRecoveryEnablement(proto.Enum):
        POINT_IN_TIME_RECOVERY_ENABLEMENT_UNSPECIFIED: int
        POINT_IN_TIME_RECOVERY_ENABLED: int
        POINT_IN_TIME_RECOVERY_DISABLED: int
    class AppEngineIntegrationMode(proto.Enum):
        APP_ENGINE_INTEGRATION_MODE_UNSPECIFIED: int
        ENABLED: int
        DISABLED: int
    class DeleteProtectionState(proto.Enum):
        DELETE_PROTECTION_STATE_UNSPECIFIED: int
        DELETE_PROTECTION_DISABLED: int
        DELETE_PROTECTION_ENABLED: int
    class CmekConfig(proto.Message):
        kms_key_name: str
        active_key_version: MutableSequence[str]
    class SourceInfo(proto.Message):
        class BackupSource(proto.Message):
            backup: str
        backup: Database.SourceInfo.BackupSource
        operation: str
    class EncryptionConfig(proto.Message):
        class GoogleDefaultEncryptionOptions(proto.Message): ...
        class SourceEncryptionOptions(proto.Message): ...
        class CustomerManagedEncryptionOptions(proto.Message):
            kms_key_name: str
        google_default_encryption: Database.EncryptionConfig.GoogleDefaultEncryptionOptions
        use_source_encryption: Database.EncryptionConfig.SourceEncryptionOptions
        customer_managed_encryption: Database.EncryptionConfig.CustomerManagedEncryptionOptions
    name: str
    uid: str
    create_time: timestamp_pb2.Timestamp
    update_time: timestamp_pb2.Timestamp
    delete_time: timestamp_pb2.Timestamp
    location_id: str
    type_: DatabaseType
    concurrency_mode: ConcurrencyMode
    version_retention_period: duration_pb2.Duration
    earliest_version_time: timestamp_pb2.Timestamp
    point_in_time_recovery_enablement: PointInTimeRecoveryEnablement
    app_engine_integration_mode: AppEngineIntegrationMode
    key_prefix: str
    delete_protection_state: DeleteProtectionState
    cmek_config: CmekConfig
    previous_id: str
    source_info: SourceInfo
    etag: str
