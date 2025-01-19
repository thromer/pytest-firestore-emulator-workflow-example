import proto
from _typeshed import Incomplete
from google.cloud.firestore_admin_v1.types import index
from typing import MutableSequence

__protobuf__: Incomplete

class Field(proto.Message):
    class IndexConfig(proto.Message):
        indexes: MutableSequence[index.Index]
        uses_ancestor_config: bool
        ancestor_field: str
        reverting: bool
    class TtlConfig(proto.Message):
        class State(proto.Enum):
            STATE_UNSPECIFIED: int
            CREATING: int
            ACTIVE: int
            NEEDS_REPAIR: int
        state: Field.TtlConfig.State
    name: str
    index_config: IndexConfig
    ttl_config: TtlConfig
