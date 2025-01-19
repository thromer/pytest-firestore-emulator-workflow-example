import proto
from _typeshed import Incomplete
from typing import MutableSequence

__protobuf__: Incomplete

class Index(proto.Message):
    class QueryScope(proto.Enum):
        QUERY_SCOPE_UNSPECIFIED: int
        COLLECTION: int
        COLLECTION_GROUP: int
        COLLECTION_RECURSIVE: int
    class ApiScope(proto.Enum):
        ANY_API: int
        DATASTORE_MODE_API: int
    class State(proto.Enum):
        STATE_UNSPECIFIED: int
        CREATING: int
        READY: int
        NEEDS_REPAIR: int
    class IndexField(proto.Message):
        class Order(proto.Enum):
            ORDER_UNSPECIFIED: int
            ASCENDING: int
            DESCENDING: int
        class ArrayConfig(proto.Enum):
            ARRAY_CONFIG_UNSPECIFIED: int
            CONTAINS: int
        class VectorConfig(proto.Message):
            class FlatIndex(proto.Message): ...
            dimension: int
            flat: Index.IndexField.VectorConfig.FlatIndex
        field_path: str
        order: Index.IndexField.Order
        array_config: Index.IndexField.ArrayConfig
        vector_config: Index.IndexField.VectorConfig
    name: str
    query_scope: QueryScope
    api_scope: ApiScope
    fields: MutableSequence[IndexField]
    state: State
