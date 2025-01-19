from _typeshed import Incomplete
from google.api_core import retry as retries
from google.cloud.firestore_v1.async_stream_generator import AsyncStreamGenerator
from google.cloud.firestore_v1.base_document import DocumentSnapshot as DocumentSnapshot
from google.cloud.firestore_v1.base_query import BaseQuery as BaseQuery
from google.cloud.firestore_v1.base_vector_query import BaseVectorQuery
from google.cloud.firestore_v1.query_profile import ExplainMetrics as ExplainMetrics, ExplainOptions as ExplainOptions
from google.cloud.firestore_v1.query_results import QueryResultsList
from typing import TypeVar

TAsyncVectorQuery = TypeVar('TAsyncVectorQuery', bound='AsyncVectorQuery')

class AsyncVectorQuery(BaseVectorQuery):
    def __init__(self, nested_query: BaseQuery | TAsyncVectorQuery) -> None: ...
    async def get(self, transaction: Incomplete | None = None, retry: retries.AsyncRetry | object | None = ..., timeout: float | None = None, *, explain_options: ExplainOptions | None = None) -> QueryResultsList[DocumentSnapshot]: ...
    def stream(self, transaction: Incomplete | None = None, retry: retries.AsyncRetry | object | None = ..., timeout: float | None = None, *, explain_options: ExplainOptions | None = None) -> AsyncStreamGenerator[DocumentSnapshot]: ...
