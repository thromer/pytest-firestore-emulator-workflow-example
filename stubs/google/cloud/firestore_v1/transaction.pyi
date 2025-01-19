from google.api_core import retry as retries
from google.cloud.firestore_v1 import batch
from google.cloud.firestore_v1.base_document import DocumentSnapshot as DocumentSnapshot
from google.cloud.firestore_v1.base_transaction import BaseTransaction, _BaseTransactional
from google.cloud.firestore_v1.document import DocumentReference
from google.cloud.firestore_v1.query import Query
from google.cloud.firestore_v1.query_profile import ExplainOptions as ExplainOptions
from google.cloud.firestore_v1.stream_generator import StreamGenerator as StreamGenerator
from typing import Any, Callable, Generator

class Transaction(batch.WriteBatch, BaseTransaction):
    def __init__(self, client, max_attempts=..., read_only: bool = False) -> None: ...
    def get_all(self, references: list, retry: retries.Retry | object | None = ..., timeout: float | None = None) -> Generator[DocumentSnapshot, Any, None]: ...
    def get(self, ref_or_query: DocumentReference | Query, retry: retries.Retry | object | None = ..., timeout: float | None = None, *, explain_options: ExplainOptions | None = None) -> StreamGenerator[DocumentSnapshot] | Generator[DocumentSnapshot, Any, None]: ...

class _Transactional(_BaseTransactional):
    def __init__(self, to_wrap) -> None: ...
    def __call__(self, transaction: Transaction, *args, **kwargs): ...

def transactional(to_wrap: Callable) -> _Transactional: ...
