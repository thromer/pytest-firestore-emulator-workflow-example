from google.cloud.firestore_v1.query_profile import ExplainMetrics as ExplainMetrics, ExplainOptions as ExplainOptions
from typing import TypeVar

T = TypeVar('T')

class QueryResultsList(list[T]):
    def __init__(self, docs: list, explain_options: ExplainOptions | None = None, explain_metrics: ExplainMetrics | None = None) -> None: ...
    @property
    def explain_options(self) -> ExplainOptions | None: ...
    def get_explain_metrics(self) -> ExplainMetrics: ...
