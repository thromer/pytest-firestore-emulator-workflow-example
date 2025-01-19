import proto
from _typeshed import Incomplete
from google.cloud.firestore_v1.types import document
from typing import MutableMapping

__protobuf__: Incomplete

class AggregationResult(proto.Message):
    aggregate_fields: MutableMapping[str, document.Value]
