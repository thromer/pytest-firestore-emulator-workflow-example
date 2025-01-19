from _typeshed import Incomplete
from google.api_core import retry_async as retries
from google.cloud.firestore_v1 import transaction
from google.cloud.firestore_v1.async_stream_generator import AsyncStreamGenerator
from google.cloud.firestore_v1.base_aggregation import AggregationResult as AggregationResult, BaseAggregationQuery
from google.cloud.firestore_v1.query_profile import ExplainMetrics as ExplainMetrics, ExplainOptions as ExplainOptions
from google.cloud.firestore_v1.query_results import QueryResultsList

class AsyncAggregationQuery(BaseAggregationQuery):
    def __init__(self, nested_query) -> None: ...
    async def get(self, transaction: Incomplete | None = None, retry: retries.AsyncRetry | None | object = ..., timeout: float | None = None, *, explain_options: ExplainOptions | None = None) -> QueryResultsList[list[AggregationResult]]: ...
    def stream(self, transaction: transaction.Transaction | None = None, retry: retries.AsyncRetry | object | None = ..., timeout: float | None = None, *, explain_options: ExplainOptions | None = None) -> AsyncStreamGenerator[list[AggregationResult]]: ...
