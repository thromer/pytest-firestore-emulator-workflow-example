from _typeshed import Incomplete
from google.api_core import retry_async as retries
from google.cloud import firestore_v1 as firestore_v1
from google.cloud.firestore_v1.async_stream_generator import AsyncStreamGenerator
from google.cloud.firestore_v1.async_transaction import AsyncTransaction as AsyncTransaction
from google.cloud.firestore_v1.async_vector_query import AsyncVectorQuery
from google.cloud.firestore_v1.base_document import DocumentSnapshot as DocumentSnapshot
from google.cloud.firestore_v1.base_query import BaseCollectionGroup, BaseQuery, QueryPartition
from google.cloud.firestore_v1.base_vector_query import DistanceMeasure as DistanceMeasure
from google.cloud.firestore_v1.field_path import FieldPath as FieldPath
from google.cloud.firestore_v1.query_profile import ExplainMetrics as ExplainMetrics, ExplainOptions as ExplainOptions
from google.cloud.firestore_v1.query_results import QueryResultsList
from google.cloud.firestore_v1.vector import Vector as Vector
from typing import AsyncGenerator

class AsyncQuery(BaseQuery):
    def __init__(self, parent, projection: Incomplete | None = None, field_filters=(), orders=(), limit: Incomplete | None = None, limit_to_last: bool = False, offset: Incomplete | None = None, start_at: Incomplete | None = None, end_at: Incomplete | None = None, all_descendants: bool = False, recursive: bool = False) -> None: ...
    async def get(self, transaction: AsyncTransaction | None = None, retry: retries.AsyncRetry | object | None = ..., timeout: float | None = None, *, explain_options: ExplainOptions | None = None) -> QueryResultsList[DocumentSnapshot]: ...
    def find_nearest(self, vector_field: str, query_vector: Vector, limit: int, distance_measure: DistanceMeasure, *, distance_result_field: str | None = None, distance_threshold: float | None = None) -> AsyncVectorQuery: ...
    def count(self, alias: str | None = None) -> type['firestore_v1.async_aggregation.AsyncAggregationQuery']: ...
    def sum(self, field_ref: str | FieldPath, alias: str | None = None) -> type['firestore_v1.async_aggregation.AsyncAggregationQuery']: ...
    def avg(self, field_ref: str | FieldPath, alias: str | None = None) -> type['firestore_v1.async_aggregation.AsyncAggregationQuery']: ...
    def stream(self, transaction: AsyncTransaction | None = None, retry: retries.AsyncRetry | object | None = ..., timeout: float | None = None, *, explain_options: ExplainOptions | None = None) -> AsyncStreamGenerator[DocumentSnapshot]: ...

class AsyncCollectionGroup(AsyncQuery, BaseCollectionGroup):
    def __init__(self, parent, projection: Incomplete | None = None, field_filters=(), orders=(), limit: Incomplete | None = None, limit_to_last: bool = False, offset: Incomplete | None = None, start_at: Incomplete | None = None, end_at: Incomplete | None = None, all_descendants: bool = True, recursive: bool = False) -> None: ...
    async def get_partitions(self, partition_count, retry: retries.AsyncRetry | object | None = ..., timeout: float | None = None) -> AsyncGenerator[QueryPartition, None]: ...
