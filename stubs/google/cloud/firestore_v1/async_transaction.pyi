from google.api_core import retry_async as retries
from google.cloud.firestore_v1 import async_batch
from google.cloud.firestore_v1.async_document import AsyncDocumentReference
from google.cloud.firestore_v1.async_query import AsyncQuery
from google.cloud.firestore_v1.async_stream_generator import AsyncStreamGenerator as AsyncStreamGenerator
from google.cloud.firestore_v1.base_document import DocumentSnapshot as DocumentSnapshot
from google.cloud.firestore_v1.base_transaction import BaseTransaction, _BaseTransactional
from google.cloud.firestore_v1.query_profile import ExplainOptions as ExplainOptions
from typing import Any, AsyncGenerator, Callable

class AsyncTransaction(async_batch.AsyncWriteBatch, BaseTransaction):
    def __init__(self, client, max_attempts=..., read_only: bool = False) -> None: ...
    async def get_all(self, references: list, retry: retries.AsyncRetry | object | None = ..., timeout: float | None = None) -> AsyncGenerator[DocumentSnapshot, Any]: ...
    async def get(self, ref_or_query: AsyncDocumentReference | AsyncQuery, retry: retries.AsyncRetry | object | None = ..., timeout: float | None = None, *, explain_options: ExplainOptions | None = None) -> AsyncGenerator[DocumentSnapshot, Any] | AsyncStreamGenerator[DocumentSnapshot]: ...

class _AsyncTransactional(_BaseTransactional):
    def __init__(self, to_wrap) -> None: ...
    async def __call__(self, transaction, *args, **kwargs): ...

def async_transactional(to_wrap: Callable[[AsyncTransaction], Any]) -> _AsyncTransactional: ...
