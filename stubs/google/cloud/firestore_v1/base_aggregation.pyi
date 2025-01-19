import abc
from _typeshed import Incomplete
from abc import ABC
from google.api_core import retry as retries
from google.cloud.firestore_v1 import transaction
from google.cloud.firestore_v1.async_stream_generator import AsyncStreamGenerator as AsyncStreamGenerator
from google.cloud.firestore_v1.field_path import FieldPath
from google.cloud.firestore_v1.query_profile import ExplainOptions as ExplainOptions
from google.cloud.firestore_v1.query_results import QueryResultsList as QueryResultsList
from google.cloud.firestore_v1.stream_generator import StreamGenerator as StreamGenerator
from typing import Any, Coroutine

class AggregationResult:
    alias: Incomplete
    value: Incomplete
    read_time: Incomplete
    def __init__(self, alias: str, value: float, read_time: Incomplete | None = None) -> None: ...

class BaseAggregation(ABC, metaclass=abc.ABCMeta):
    alias: Incomplete
    def __init__(self, alias: str | None = None) -> None: ...

class CountAggregation(BaseAggregation):
    def __init__(self, alias: str | None = None) -> None: ...

class SumAggregation(BaseAggregation):
    field_ref: Incomplete
    def __init__(self, field_ref: str | FieldPath, alias: str | None = None) -> None: ...

class AvgAggregation(BaseAggregation):
    field_ref: Incomplete
    def __init__(self, field_ref: str | FieldPath, alias: str | None = None) -> None: ...

class BaseAggregationQuery(ABC, metaclass=abc.ABCMeta):
    def __init__(self, nested_query, alias: str | None = None) -> None: ...
    def count(self, alias: str | None = None): ...
    def sum(self, field_ref: str | FieldPath, alias: str | None = None): ...
    def avg(self, field_ref: str | FieldPath, alias: str | None = None): ...
    def add_aggregation(self, aggregation: BaseAggregation) -> None: ...
    def add_aggregations(self, aggregations: list[BaseAggregation]) -> None: ...
    @abc.abstractmethod
    def get(self, transaction: Incomplete | None = None, retry: retries.Retry | retries.AsyncRetry | None | object = ..., timeout: float | None = None, *, explain_options: ExplainOptions | None = None) -> QueryResultsList[AggregationResult] | Coroutine[Any, Any, list[list[AggregationResult]]]: ...
    @abc.abstractmethod
    def stream(self, transaction: transaction.Transaction | None = None, retry: retries.Retry | retries.AsyncRetry | object | None = ..., timeout: float | None = None, *, explain_options: ExplainOptions | None = None) -> StreamGenerator[list[AggregationResult]] | AsyncStreamGenerator[list[AggregationResult]]: ...
