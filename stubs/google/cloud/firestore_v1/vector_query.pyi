from _typeshed import Incomplete
from google.api_core import retry as retries
from google.cloud.firestore_v1 import transaction
from google.cloud.firestore_v1.base_document import DocumentSnapshot as DocumentSnapshot
from google.cloud.firestore_v1.base_query import BaseQuery as BaseQuery
from google.cloud.firestore_v1.base_vector_query import BaseVectorQuery
from google.cloud.firestore_v1.query_profile import ExplainMetrics as ExplainMetrics, ExplainOptions as ExplainOptions
from google.cloud.firestore_v1.query_results import QueryResultsList
from google.cloud.firestore_v1.stream_generator import StreamGenerator
from typing import TypeVar

TVectorQuery = TypeVar('TVectorQuery', bound='VectorQuery')

class VectorQuery(BaseVectorQuery):
    def __init__(self, nested_query: BaseQuery | TVectorQuery) -> None: ...
    def get(self, transaction: Incomplete | None = None, retry: retries.Retry | object | None = ..., timeout: float | None = None, *, explain_options: ExplainOptions | None = None) -> QueryResultsList[DocumentSnapshot]: ...
    def stream(self, transaction: transaction.Transaction | None = None, retry: retries.Retry | object | None = ..., timeout: float | None = None, *, explain_options: ExplainOptions | None = None) -> StreamGenerator[DocumentSnapshot]: ...
