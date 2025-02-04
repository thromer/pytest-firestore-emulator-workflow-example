from _typeshed import Incomplete
from google.api_core import retry_async as retries
from google.cloud.firestore_v1.async_batch import AsyncWriteBatch
from google.cloud.firestore_v1.async_collection import AsyncCollectionReference
from google.cloud.firestore_v1.async_document import AsyncDocumentReference, DocumentSnapshot as DocumentSnapshot
from google.cloud.firestore_v1.async_query import AsyncCollectionGroup
from google.cloud.firestore_v1.async_transaction import AsyncTransaction
from google.cloud.firestore_v1.base_client import BaseClient
from google.cloud.firestore_v1.bulk_writer import BulkWriter as BulkWriter
from typing import Any, AsyncGenerator, Iterable

class AsyncClient(BaseClient):
    def __init__(self, project: Incomplete | None = None, credentials: Incomplete | None = None, database: Incomplete | None = None, client_info=..., client_options: Incomplete | None = None) -> None: ...
    def collection(self, *collection_path: str) -> AsyncCollectionReference: ...
    def collection_group(self, collection_id: str) -> AsyncCollectionGroup: ...
    def document(self, *document_path: str) -> AsyncDocumentReference: ...
    async def get_all(self, references: list[AsyncDocumentReference], field_paths: Iterable[str] | None = None, transaction: AsyncTransaction | None = None, retry: retries.AsyncRetry | object | None = ..., timeout: float | None = None) -> AsyncGenerator[DocumentSnapshot, Any]: ...
    async def collections(self, retry: retries.AsyncRetry | object | None = ..., timeout: float | None = None) -> AsyncGenerator[AsyncCollectionReference, Any]: ...
    async def recursive_delete(self, reference: AsyncCollectionReference | AsyncDocumentReference, *, bulk_writer: BulkWriter | None = None, chunk_size: int = 5000) -> int: ...
    def batch(self) -> AsyncWriteBatch: ...
    def transaction(self, **kwargs) -> AsyncTransaction: ...
