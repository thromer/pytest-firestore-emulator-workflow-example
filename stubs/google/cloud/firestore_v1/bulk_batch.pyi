from _typeshed import Incomplete
from google.api_core import retry as retries
from google.cloud.firestore_v1.base_batch import BaseBatch
from google.cloud.firestore_v1.types.firestore import BatchWriteResponse as BatchWriteResponse

class BulkWriteBatch(BaseBatch):
    def __init__(self, client) -> None: ...
    write_results: Incomplete
    def commit(self, retry: retries.Retry | object | None = ..., timeout: float | None = None) -> BatchWriteResponse: ...
