import proto
from _typeshed import Incomplete
from google.protobuf import timestamp_pb2

__protobuf__: Incomplete

class Backup(proto.Message):
    class State(proto.Enum):
        STATE_UNSPECIFIED: int
        CREATING: int
        READY: int
        NOT_AVAILABLE: int
    class Stats(proto.Message):
        size_bytes: int
        document_count: int
        index_count: int
    name: str
    database: str
    database_uid: str
    snapshot_time: timestamp_pb2.Timestamp
    expire_time: timestamp_pb2.Timestamp
    stats: Stats
    state: State
