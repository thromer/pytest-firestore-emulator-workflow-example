from _typeshed import Incomplete
from google.api_core import retry as retries
from google.cloud import firestore_v1 as firestore_v1
from google.cloud.firestore_v1 import transaction
from google.cloud.firestore_v1.base_document import DocumentSnapshot
from google.cloud.firestore_v1.base_query import BaseCollectionGroup, BaseQuery, QueryPartition
from google.cloud.firestore_v1.base_vector_query import DistanceMeasure as DistanceMeasure
from google.cloud.firestore_v1.field_path import FieldPath as FieldPath
from google.cloud.firestore_v1.query_profile import ExplainMetrics as ExplainMetrics, ExplainOptions as ExplainOptions
from google.cloud.firestore_v1.query_results import QueryResultsList
from google.cloud.firestore_v1.stream_generator import StreamGenerator
from google.cloud.firestore_v1.vector import Vector as Vector
from google.cloud.firestore_v1.watch import Watch
from typing import Callable, Generator

class Query(BaseQuery):
    def __init__(self, parent, projection: Incomplete | None = None, field_filters=(), orders=(), limit: Incomplete | None = None, limit_to_last: bool = False, offset: Incomplete | None = None, start_at: Incomplete | None = None, end_at: Incomplete | None = None, all_descendants: bool = False, recursive: bool = False) -> None: ...
    def get(self, transaction: Incomplete | None = None, retry: retries.Retry | object | None = ..., timeout: float | None = None, *, explain_options: ExplainOptions | None = None) -> QueryResultsList[DocumentSnapshot]: ...
    def find_nearest(self, vector_field: str, query_vector: Vector, limit: int, distance_measure: DistanceMeasure, *, distance_result_field: str | None = None, distance_threshold: float | None = None) -> type['firestore_v1.vector_query.VectorQuery']: ...
    def count(self, alias: str | None = None) -> type['firestore_v1.aggregation.AggregationQuery']: ...
    def sum(self, field_ref: str | FieldPath, alias: str | None = None) -> type['firestore_v1.aggregation.AggregationQuery']: ...
    def avg(self, field_ref: str | FieldPath, alias: str | None = None) -> type['firestore_v1.aggregation.AggregationQuery']: ...
    def stream(self, transaction: transaction.Transaction | None = None, retry: retries.Retry | object | None = ..., timeout: float | None = None, *, explain_options: ExplainOptions | None = None) -> StreamGenerator[DocumentSnapshot]: ...
    def on_snapshot(self, callback: Callable) -> Watch: ...

class CollectionGroup(Query, BaseCollectionGroup):
    def __init__(self, parent, projection: Incomplete | None = None, field_filters=(), orders=(), limit: Incomplete | None = None, limit_to_last: bool = False, offset: Incomplete | None = None, start_at: Incomplete | None = None, end_at: Incomplete | None = None, all_descendants: bool = True, recursive: bool = False) -> None: ...
    def get_partitions(self, partition_count, retry: retries.Retry | object | None = ..., timeout: float | None = None) -> Generator[QueryPartition, None, None]: ...
