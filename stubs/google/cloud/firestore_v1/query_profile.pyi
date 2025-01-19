import datetime
from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True)
class ExplainOptions:
    analyze: bool = ...
    def __init__(self, analyze=...) -> None: ...

@dataclass(frozen=True)
class PlanSummary:
    indexes_used: list[dict[str, Any]]
    def __init__(self, indexes_used) -> None: ...

@dataclass(frozen=True)
class ExecutionStats:
    results_returned: int
    execution_duration: datetime.timedelta
    read_operations: int
    debug_stats: dict[str, Any]
    def __init__(self, results_returned, execution_duration, read_operations, debug_stats) -> None: ...

@dataclass(frozen=True)
class ExplainMetrics:
    plan_summary: PlanSummary
    @property
    def execution_stats(self) -> ExecutionStats: ...
    def __init__(self, plan_summary) -> None: ...

@dataclass(frozen=True)
class _ExplainAnalyzeMetrics(ExplainMetrics):
    plan_summary: PlanSummary
    @property
    def execution_stats(self) -> ExecutionStats: ...
    def __init__(self, plan_summary, _execution_stats) -> None: ...

class QueryExplainError(Exception): ...
