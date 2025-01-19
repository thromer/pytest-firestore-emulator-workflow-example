import abc
from _typeshed import Incomplete
from abc import ABC
from enum import Enum
from google.api_core import retry as retries
from google.cloud.firestore_v1.async_stream_generator import AsyncStreamGenerator as AsyncStreamGenerator
from google.cloud.firestore_v1.base_document import DocumentSnapshot as DocumentSnapshot
from google.cloud.firestore_v1.query_profile import ExplainOptions as ExplainOptions
from google.cloud.firestore_v1.query_results import QueryResultsList as QueryResultsList
from google.cloud.firestore_v1.stream_generator import StreamGenerator as StreamGenerator
from google.cloud.firestore_v1.vector import Vector as Vector
from typing import Any, Coroutine

class DistanceMeasure(Enum):
    EUCLIDEAN = 1
    COSINE = 2
    DOT_PRODUCT = 3

class BaseVectorQuery(ABC, metaclass=abc.ABCMeta):
    def __init__(self, nested_query) -> None: ...
    @abc.abstractmethod
    def get(self, transaction: Incomplete | None = None, retry: retries.Retry | retries.AsyncRetry | object | None = ..., timeout: float | None = None, *, explain_options: ExplainOptions | None = None) -> QueryResultsList[DocumentSnapshot] | Coroutine[Any, Any, QueryResultsList[DocumentSnapshot]]: ...
    def find_nearest(self, vector_field: str, query_vector: Vector, limit: int, distance_measure: DistanceMeasure, *, distance_result_field: str | None = None, distance_threshold: float | None = None): ...
    def stream(self, transaction: Incomplete | None = None, retry: retries.Retry | retries.AsyncRetry | object | None = ..., timeout: float | None = None, *, explain_options: ExplainOptions | None = None) -> StreamGenerator[DocumentSnapshot] | AsyncStreamGenerator[DocumentSnapshot]: ...
