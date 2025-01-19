from _typeshed import Incomplete
from google.api_core import retry as retries
from google.cloud.firestore_v1.async_stream_generator import AsyncStreamGenerator as AsyncStreamGenerator
from google.cloud.firestore_v1.document import DocumentSnapshot as DocumentSnapshot
from google.cloud.firestore_v1.query_profile import ExplainOptions as ExplainOptions
from google.cloud.firestore_v1.stream_generator import StreamGenerator as StreamGenerator
from typing import Any, AsyncGenerator, Coroutine, Generator

MAX_ATTEMPTS: int

class BaseTransaction:
    def __init__(self, max_attempts=..., read_only: bool = False) -> None: ...
    @property
    def in_progress(self): ...
    @property
    def id(self): ...
    def get_all(self, references: list, retry: retries.Retry | retries.AsyncRetry | object | None = None, timeout: float | None = None) -> Generator[DocumentSnapshot, Any, None] | Coroutine[Any, Any, AsyncGenerator[DocumentSnapshot, Any]]: ...
    def get(self, ref_or_query, retry: retries.Retry | retries.AsyncRetry | object | None = None, timeout: float | None = None, *, explain_options: ExplainOptions | None = None) -> StreamGenerator[DocumentSnapshot] | Generator[DocumentSnapshot, Any, None] | Coroutine[Any, Any, AsyncGenerator[DocumentSnapshot, Any]] | Coroutine[Any, Any, AsyncStreamGenerator[DocumentSnapshot]]: ...

class _BaseTransactional:
    to_wrap: Incomplete
    current_id: Incomplete
    retry_id: Incomplete
    def __init__(self, to_wrap) -> None: ...
    def __call__(self, transaction, *args, **kwargs) -> None: ...
